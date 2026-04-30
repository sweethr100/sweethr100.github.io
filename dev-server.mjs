import { createReadStream, promises as fsPromises, watch } from "node:fs";
import { createServer } from "node:http";
import { extname, join, normalize, relative, resolve, sep } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL(".", import.meta.url)));
const host = process.env.HOST || "0.0.0.0";
const port = Number(process.env.PORT || 8000);
const clients = new Set();

const mimeTypes = new Map([
  [".css", "text/css; charset=utf-8"],
  [".gif", "image/gif"],
  [".html", "text/html; charset=utf-8"],
  [".ico", "image/x-icon"],
  [".jpeg", "image/jpeg"],
  [".jpg", "image/jpeg"],
  [".js", "text/javascript; charset=utf-8"],
  [".json", "application/json; charset=utf-8"],
  [".png", "image/png"],
  [".svg", "image/svg+xml; charset=utf-8"],
  [".webp", "image/webp"],
]);

const liveReloadScript = `
<script>
(() => {
  const source = new EventSource("/__live-reload");
  source.addEventListener("reload", () => window.location.reload());
  source.onerror = () => {
    source.close();
    setTimeout(() => window.location.reload(), 1000);
  };
})();
</script>`;

function sendReload(fileName) {
  const payload = `event: reload\ndata: ${JSON.stringify(fileName || "change")}\n\n`;
  for (const client of clients) {
    client.write(payload);
  }
}

function isInsideRoot(pathName) {
  const rel = relative(root, pathName);
  return rel === "" || (!rel.startsWith("..") && !rel.includes(`..${sep}`));
}

async function resolveRequestPath(url) {
  const { pathname } = new URL(url, `http://localhost:${port}`);
  const decodedPath = decodeURIComponent(pathname);
  const normalizedPath = normalize(decodedPath).replace(/^([/\\])+/, "");
  let filePath = resolve(join(root, normalizedPath));

  if (!isInsideRoot(filePath)) {
    return undefined;
  }

  const stat = await fsPromises.stat(filePath).catch(() => undefined);
  if (stat?.isDirectory()) {
    filePath = join(filePath, "index.html");
  }

  return filePath;
}

async function serveHtml(filePath, response) {
  let html = await fsPromises.readFile(filePath, "utf8");
  if (html.includes("</body>")) {
    html = html.replace("</body>", `${liveReloadScript}\n</body>`);
  } else {
    html += liveReloadScript;
  }

  response.writeHead(200, {
    "Cache-Control": "no-store",
    "Content-Type": "text/html; charset=utf-8",
  });
  response.end(html);
}

const server = createServer(async (request, response) => {
  try {
    if (request.url === "/__live-reload") {
      response.writeHead(200, {
        "Cache-Control": "no-cache",
        Connection: "keep-alive",
        "Content-Type": "text/event-stream",
      });
      response.write(": connected\n\n");
      clients.add(response);
      request.on("close", () => clients.delete(response));
      return;
    }

    const filePath = await resolveRequestPath(request.url || "/");
    if (!filePath) {
      response.writeHead(403);
      response.end("Forbidden");
      return;
    }

    const stat = await fsPromises.stat(filePath).catch(() => undefined);
    if (!stat?.isFile()) {
      response.writeHead(404);
      response.end("Not found");
      return;
    }

    if (extname(filePath) === ".html") {
      await serveHtml(filePath, response);
      return;
    }

    response.writeHead(200, {
      "Cache-Control": "no-store",
      "Content-Length": stat.size,
      "Content-Type": mimeTypes.get(extname(filePath)) || "application/octet-stream",
    });
    createReadStream(filePath).pipe(response);
  } catch (error) {
    response.writeHead(500);
    response.end(error instanceof Error ? error.message : "Server error");
  }
});

let reloadTimer;
watch(root, { recursive: true }, (_eventType, fileName) => {
  const name = String(fileName || "");
  if (
    !name ||
    name.startsWith(".git") ||
    name.endsWith(".log") ||
    name === "dev-server.mjs"
  ) {
    return;
  }

  clearTimeout(reloadTimer);
  reloadTimer = setTimeout(() => sendReload(name), 100);
});

server.listen(port, host, () => {
  console.log(`Live reload server running at http://${host}:${port}/`);
});
