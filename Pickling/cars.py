import pickle

# Pickling a python object
# cars = ["Audi" , "BMW" , "Mercedes" , "Range Rover"]
# file = r"C:\Coding\python\projects\Pickling\myCars.pkl"
# fileobj = open(file , "wb")
# pickle.dump(cars , fileobj)
# fileobj.close

file = r"C:\Coding\python\projects\Pickling\myCars.pkl"
fileobj = open(file , "rb")
myCars = pickle.load(fileobj)
print(myCars)
print(type(myCars))