import pickle

f = open('../setting.txt', 'rb')
setting = pickle.load(f)
f.close()
print(setting)
