
import configparser
config=configparser.ConfigParser()
config.read("config.ini")
depth = config["DEPTH"]["depth"]

import random

from Matrix import Matrix
my_matrix = Matrix(depth)
my_matrix.fill("cities_in_Brittany.txt")

'''
print("hello world")
table={
    None : {None:0, "a":0.5 , "b":0.5},
    "a" : {None:0.1 , "a":0.45 , "b":0.45},
    "b" : {None:0.1 , "a":0.55 , "b":0.35},
    "aa" : {None:0.1 , "a":0.55 , "b":0.35},
    "ab" : {None:0.1 , "a":0.55 , "b":0.35},
    "ba" : {None:0.1 , "a":0.55 , "b":0.35},
    "bb" : {None:1 , "a":0 , "b":0}
}
'''

word = my_matrix.generate_word()
print(word)