import { mkdir, writeFile } from "node:fs/promises";
import { dirname, resolve } from "node:path";

const username = process.env.GITHUB_USERNAME || "sweethr100";
const token = process.env.GITHUB_TOKEN || process.env.GH_TOKEN;
const outputFile = resolve(process.env.OUTPUT_FILE || "data/github-contributions.json");

if (!token) {
  throw new Error("GITHUB_TOKEN or GH_TOKEN is required to fetch contribution data.");
}

const now = new Date();
const fromDate = new Date(now);
fromDate.setUTCFullYear(fromDate.getUTCFullYear() - 1);

const graphqlQuery = `
query UserContributionCalendar($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    login
    name
    url
    contributionsCollection(from: $from, to: $to) {
      contributionCalendar {
        totalContributions
        weeks {
          firstDay
          contributionDays {
            date
            contributionCount
            color
            contributionLevel
            weekday
          }
        }
      }
    }
  }
}
`;

function normalizeLevel(level) {
  const levels = {
    NONE: 0,
    FIRST_QUARTILE: 1,
    SECOND_QUARTILE: 2,
    THIRD_QUARTILE: 3,
    FOURTH_QUARTILE: 4,
  };

  return levels[level] ?? 0;
}

async function fetchJson(url, options) {
  const response = await fetch(url, {
    ...options,
    headers: {
      Accept: "application/vnd.github+json",
      Authorization: `Bearer ${token}`,
      "User-Agent": `${username}-github-pages`,
      ...(options?.headers || {}),
    },
  });

  if (!response.ok) {
    const body = await response.text();
    throw new Error(`GitHub request failed: ${response.status} ${response.statusText}\n${body}`);
  }

  return response.json();
}

const [graphqlResult, profile] = await Promise.all([
  fetchJson("https://api.github.com/graphql", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      query: graphqlQuery,
      variables: {
        login: username,
        from: fromDate.toISOString(),
        to: now.toISOString(),
      },
    }),
  }),
  fetchJson(`https://api.github.com/users/${encodeURIComponent(username)}`),
]);

if (graphqlResult.errors?.length) {
  throw new Error(JSON.stringify(graphqlResult.errors, null, 2));
}

const user = graphqlResult.data?.user;
if (!user) {
  throw new Error(`GitHub user not found: ${username}`);
}

const calendar = user.contributionsCollection.contributionCalendar;
const weeks = calendar.weeks.map((week) => ({
  firstDay: week.firstDay,
  contributionDays: week.contributionDays.map((day) => ({
    date: day.date,
    count: day.contributionCount,
    color: day.color,
    level: normalizeLevel(day.contributionLevel),
    contributionLevel: day.contributionLevel,
    weekday: day.weekday,
  })),
}));

const days = weeks.flatMap((week) => week.contributionDays);
const payload = {
  username: user.login,
  name: user.name,
  profileUrl: user.url,
  generatedAt: now.toISOString(),
  range: {
    from: days[0]?.date || fromDate.toISOString().slice(0, 10),
    to: days.at(-1)?.date || now.toISOString().slice(0, 10),
  },
  publicRepos: profile.public_repos,
  totalContributions: calendar.totalContributions,
  activeDays: days.filter((day) => day.count > 0).length,
  maxDailyContributions: Math.max(0, ...days.map((day) => day.count)),
  calendar: {
    weeks,
  },
};

await mkdir(dirname(outputFile), { recursive: true });
await writeFile(outputFile, `${JSON.stringify(payload, null, 2)}\n`, "utf8");

console.log(`Wrote ${outputFile}`);
