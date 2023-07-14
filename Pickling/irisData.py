import pickle

with open(r"C:\Coding\python\projects\Pickling\iris.data" , "r") as f:
    data = f.readlines()
    # print(data)

    d2 = [item.split(",") for item in data if len(item)!=0]
    # print(d2)

# with open(r"C:\Coding\python\projects\Pickling\iris.pkl" , "wb") as f:
#     pickle.dump(d2 , f)

with open(r"C:\Coding\python\projects\Pickling\iris.pkl" , "rb") as f:
    print(pickle.load(f))