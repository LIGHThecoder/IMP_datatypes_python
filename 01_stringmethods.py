"""
author : Nikhil Rajendra Gaikwad
date : 08-03-24
title : all major datatypes and there methods


"""
"------------------ 1  string and there methods------------------------------"

# print("hello world")
"string are combination of characters"
" we got string methods to access them, changes or even modify them"
" following are the string methods"
"""
upper
lower
center
capitalize
title
swapcase
strip
replace
split
count

startwith
endwith
isspace
isprintabel
isalpha
isalnum
find
index"""
#-----------1 upper
my_name = ("nikhil")
# print(my_name.upper())

#---------------2 lower
my_name = ("RAHUL")
# print(my_name.lower())

#-----------3 center
# print(my_name.center(50))

# -------------4 capitalize
# print(my_name.capitalize())
"all letter in the string will be small only the first letter will be capital"

#------------5 title
my_name = "nikhil rajendra gaikwad and i want to master python"
# print(my_name.title())

#--------------6 swamp case
# print(my_name.swapcase())
"in swapcase upper letter will convert into small and small will convert into capital"

#------------7 stripe
# print(my_name.strip("python"))
"the strip function can only cut word from starting or from ending"
"you must inclued starting letter or ending to work with strip "

#--------------8 replace
# id="thanos"
# print(my_name.replace("nikhil","rahul"))
"replacce is used to change a perticular word in string and replace it with another one"

#----------------9 split
"it will convert string to a list form"
# print(my_name.split())
# print(type(my_name))

#---------------10 count
# print(my_name.count("a"))
"this will count how may time a letter or word or any kind user input is present "
"in the string"

#-----------11 startwith
# print(my_name.startswith("nikhil"))
"this means as user input is matching with the starting of the string"

#---------------12 endwith
# print(my_name.endswith("n"))
"this means as user input is matching with the ending of the string"

#--------------13 isspace
null = ("  ")
# print(null.isspace())
"this will chceck that the perticular string is null or not is null true will be output"

#---------------14 isprintable
# print(my_name.isprintable())
"this will check in string only character are there or not if there are any escape sequace or variables than it will return false"

#--------------15 isalnum
"alppha numeric means A-Z a-z and numberical aswerr"
my_id = "mynameisnikhilandmyrollnoi"
# print(my_id.isalnum())

#-------------16 isalpha
# print(my_id.isalpha())
"isalpha means it must contain only letter of capital and small and not number are allowed"

#-------------17 find
# print(my_id.find("x"))
# print("nikhil")
" if the input is not in the string then -1 is given at output and the programe will contine from the next line and the next line shall get executed"

#-----------18 index
# print(my_id.index("n"))
" it will through an errro meaning the programe will stop at there and next line will not get executed"

# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

print("wow the world")