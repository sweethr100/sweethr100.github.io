# import pickle
#
# gameOption = {
#     "sound":8,
#     "VideoQuality":"HIGH",
#     "Money": 100000,
#     "WeaponList": ["gun", "missile", "knife"]
# }
#
# file = open("save.p", "wb")
# pickle.dump(gameOption, file)
# file.close()



import pickle

file=open("save.p","rb")
obj=pickle.load(open("save.p", "rb"))
print(obj)