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
upper               this will capital all the characters in the string
lower               this will small all the character in the string 
center              this will center the string
capitalize          this will capital only the first character in the string
title               this will capital ever first character of the word in the string
swapcase            this will capital small character and capital letter will turn into small
strip               with this we can strip down menans canncel out the last or first character or word in the string
replace             we have to input character aslo we have to mention from the string where we want to replace it (for example i wnat to replace light from flight so i have to mention like that)
split               this will convert you string to an list form 
count               to count howm many times a perticular character is present in the string

startwith           it will check from the input that the string start with that input, if yes then return true and if the string does not start with the given character than return false
endwith             it will check from the input that the string end with the input, if yes than return true and if the string does not end with the given charcter then return false
isspace             it will check that the string is void or not. if the string does not containig any single tpye of charcater then return true. example ---> myspace("            ") this exmplace will return true as it is null
isprintabel         this will check that in the string only character are there or not and if there are any king on eccape sequence then return false
isalpha             it will check then in string only alpahbets are present or not. if only alphaber are prensent then true or else false
isalnum             it will check then in string there are alpahbets and also number present or not. if only alphaber or even nuber are prensent then true or else false
find                to ceck the character first time appear where in the string by simplely puting that character in the input  and it will output the index of the character. if the input character is not present in the string it will return -1 and porgrmae will go further to execute in next line.
# index               to ceck the character first time appear where in the string by simplely puting that character in the input  and it will output the index of the character. if the input character is not present in string then it will return an erro and the programe will stop rghte there and further execution will not perform in the next line."""
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
"------------- 2  list and there methods-------------------------------"
" list are changable order datatype "

list1 = ["nikhil", "rajendra", "gaikwad", 2, 3, 1, 2, 2, 4]
# print(type(list1))
"""
append               to insert
pop                  to remover a character or number from a index
sort assendending    to print the given list in assending order no further change
sort decending       to print a list in decending order no further changes
reverser             to print a list as it is but in reverse form
index                to print index of a character or number where it first time.
count                to print how many times given charcter or number is in list
copy                 to copy a perticluar stirng and make a mew independent string from it
insert               it is similar to append by here addidtion you have to mention the index where you want this input to be present
extent                to add a list into another list
"""
#------------ 1  append
list1.append("rahul")
# print(list1)
" to add any character or numbers at last of the string we use append "
" it will add the input to the last of the string that's the work of append"

#------------ 11  pop
# ra.pop(1)
# print(ra)
"to remove a character or number from the list then use pop in pop you have "
"to mention the index at which you want to remove a perticular value"

#--------------------- 2   sort assending
list2 = [2, 3, 4, 3, 6, 3, 9, 5, 6, 78, 4, 5, 7]
# list2.sort()
# print(list2)
" it will print number from smaller to bigger "

#------------------- 3  sort decending
# list2.sort(reverse=True)
# print(list2)
"this will print the higheest number first and then smaller than that of till the last one"

#---------------4  reverse method
list2.reverse()
# print(list2)
" it will reverse the numbers that's it"
"the major difference difference between sort decending and reverse it that"
"sort decending will print the list in an order of higher then lowers"
"where as reverse will not see the oder or anyting it will just print the given stirng in reverse form"

#-------------5  index
newlist = [2, 3, 4, 1, 2, 3, 41, "nikhil"]
# print(newlist.index("nikhil"))
"this is used to find out index where the value is first time appear"
"so the user will put a value so ouput will show it's index"

#-----------6  count method
# print(newlist.count("nikhil"))

#-------------7   copy method

# oldlist=copy(newlist
oldlist = newlist.copy()
# print(oldlist)
"from this we can copy the list and make a separate independent list"

#--------------- 8  insert method
oldlist.insert(1, "rahul")
# print(oldlist)
" it will insert a new character or number at a given perticular index"

#-------------- 9  exteeend method
ra = [1, "nikhil", 2, 3, 4, 5, 5, 6]
# oldlist.extend(ra)
# print(oldlist)
"it will extenned the given list"

#------------ 10  concanitataing two list
# print(ra+oldlist)

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
"------------------------------tuples----------------------------------------"
"tuples are imutable means once they are formend, they can't be changed and they are ordered as well"

tuple1 = ("nikhil", "rahul", "rajendra")
# print(tuple1)
# print(type(tuple1))
'as we know that tuple are immutable so we have to first convert it into list and then proform task and again convert it back to tauple'

# for example
# print(type(tuple1))  # here it is the original tupple
# listof_tuple = list(
# tuple1
# )  # here we declare a new varialbe and assign value of tuple1 vaeiable in it be telling it is the list version of tuple1
# print(listof_tuple)
# listof_tuple.pop(0)
# print(listof_tuple)
# listof_tuple.append("light")
# print(listof_tuple)
# print(type(listof_tuple))
# tuple1 = tuple(listof_tuple)
# print(tuple1)
# print(type(tuple1))
"""
['nikhil', 'rahul', 'rajendra']
['rahul', 'rajendra']
['rahul', 'rajendra', 'light']
<class 'list'>
('rahul', 'rajendra', 'light')
<class 'tuple'>

"""

#--------------------tuple methods

"""
append                              if you want to add or do amy kind of ugrade first you have to convert that tuple to an list and then porfomr operaions and then again convert it in to tuple
concaniting two tuple               as we cannot do upgrad directly in the tuple datatype but we can add tuple vairalbe and create a new varaible which will be addition of them or we can say concaniting of them
count                               this will count howm many times a pertiuclar charcter or number is present in the tupele 
index                               you have to put here index and input you will get value stored in that perticular index
len                                 to ceck the len of the tuple. len start from 1.
"""
#----------- 1  append
toadd = (1, 2, 3, 4, 5)
# print(toadd)
copytoadd = list(toadd)
copytoadd.append(23)
toadd = tuple(copytoadd)
# print(toadd)
" as we know that we cannot make any kind of changes directly first we have to make it as list and then we have to append it that means add the values in the list and then convert it back to tuple"

#----------- 2  concanitaction two tuples
my_tupe1 = ("nikhil", "rajendra", "rahul")
# print(my_tupe1)
my_tupe2 = (28, 23, 10)
# print(my_tupe2)

# print(my_tupe1 + my_tupe2)
# print(type(my_tupe1 + my_tupe2))
" as well cannot make changes directly to the tuple but we can make two tuple join together by adding them or we say concanitating them"
"""
('nikhil', 'rajendra', 'rahul', 28, 23, 10)
<class 'tuple'>
"""

#--------------- 3  count
howmnay = [2, 3, 4, 5, 1, 2, 3, 2, 3, 2, 1, 2, 2, 2]
# print(howmnay.count(2))
"we can check how many times a perticular character or number is present in the tuple"

#----------  4 index
# print(howmnay.index(5))
"to check at which index what values are stored"

#----------- 5 len
# print(len(howmnay))
'THis is something to remember that len always starts from 1 and range or index start from 0'

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
"--------------------------------sets--------------------------------------------------"
"sets are changeabel they are unorder as well they are denoted by {} repetation are also now allowed in sets"

set1 = {"rahul", "nikhil"}
# print(set1)
# print(type(set1))
"""
union                       if you want to create a new set where it must be addition of two sets in such case you must use union
update                      if you want to add a set to another set then we cas use update
intersection                it will print only those data which are common in both the sets
intersection update         it we want to make a set where we want only intersection of both the set and we have to declare any one of them as intersecto update of ther counter part
symetric difference         if we print those value which are not common in them

disjoint                    in both the sets if non of the values of identical to each other then only it will return true
issuperset                  it mean all the values of set 1 must be present in set 2 only then it will return true
issubset                    it means all the values of set 2 must be present in set 1 only then it will return true
add                         to add a single data in the set
update                      to add multiple data in the set
remove/discard              both are used to cancel out the data from the string. Key difference is that if give input is not present in the set then remove wil throw and erro and prograem will stop whereas disced will still accepet the wrong input and go the next line for the further execution of the code
pop                         to take out any random value from the set 
del                         to delet entire the set to delet it existence
clear                       it will clear only the data in the set and hence the set will be null set

"""

#----------------------------------  union

set2 = {"chintu", "honey", "nikhil"}
# print(set1.union(set2))
"if you want to merget bothe the set or you want to merge the two set and put there values to a new set such things can be done using union"

set3 = set1.union(
    set2
)  #this is how we can add to sets and assign there both vales to a new set and print them
# print(set3)

#-------------------------------------   update

numbset = {2, 3, 4, 2}
numbset.update(set2)
# print(numbset)
" if you want to add a set to another set and assign set1 values ot set 2 or assign set 2 values to set 1 such things can done using update"

#----------------------------------  intersaction

set4 = {23, 4, 5, 1, 2, 3, "nikhil"}
set5 = {23, 4, 33, 12, 456, 42, 12, 432, 23, "nikhil", 1}
intersection_x = set5.intersection(set4)
# print(intersection_x)
" the above is the only way to use intersection "
"to use intersection first we have to make two set make sure some valus are common in them"
"""
then declare a new varialbe stating set1 will be intersection of set 2

so only the values which are same in both the shall get printed

"""

#------------------------------------------- intersection update

set4 = {23, 4, 5, 1, 2, 3, "nikhil"}
# print(set4)  #------set 4 THEN
set4.intersection_update(set5)
# print(set4)  #--------SET 4 NOW
"as the result set 4 is updated and now only the intersection values are presented in the set4"

#------------------------------   symetric differene

set4 = {23, 4, 5, 1, 2, 3, "nikhil"}
set5 = {23, 4, 33, 12, 456, 42, 12, 432, 23, "nikhil", 1}
set4.difference(set5)
# print(set4)
" only those value will print which are in both the sets"

# cities= {"tokyo","madrid","berlin","delhi"}
# cities2= {"tokyo","seoul","kabul","madrid"}
# cities3= cities.difference(cities2)
# print(cities3)# only those value will print which are in the both sets
# it will check values of set 1 is there in set 2.
"-----------------------set methods-------------------------------"

#----------------- 1  disjoint
abc = {2, 3, 4, 21, 12, 34, 12}
exy = {"nikhil", "rajendra", 999, 100}
# print(abc.isdisjoint(exy))
" it will return true only if both set are fully different i.e non of the values should be identical in both set"
" in following case set 1 is not having any king of number idectical to set 2 and set is also not having any such number identical to set 1"
" therefore it will return true as non of the valus are match the called as disjoint"

#------------------  2  issupersest

s1 = {"nikhil", 2.3, 12, 2}
s2 = {"nikhil", 2.3}
# print(s1.issuperset(s2))
" it will print ture only if value of set 2 must be present at set 1"

#--------------------- 3  issubset
s1 = {"nikhil", 2.3, 12, 2}
s2 = {"nikhil", 2.3, 12, 2, "rahul"}
# print(s1.issubset(s2))
"this will return true only if all the values of set 1 must be present at set 2"

#----------------  4  add
" in other datatypes to add data we use append "
" but in sets we use add function to add data in the set"
s2.add("rajendra")
# print(s2)
# print(type(s2))

#-------------------  5  update
"only to be use if you wnat to add data more than 1 "
s2.update([23, 12])  #---------this is the syntax to update in sets
# print(s2)
" some times erro come that int oject is not iterable it means that you have to input you values in a square brackets and that's it "

#------------------ 6 remove/discard
s2 = {"nikhil", 2.3, 12, 2, "rahul"}
# s2.remove(2.323)  #wrong input and it will throught an erro programe gets stop at there it self
# print(s2)
" with this we can remove data from the set"

s1 = {"nikhil", 2.3, 12, 2}
# s1.discard("ikhil") # wrong input problem will then to run
# print(s1)
"-----only difference in remove and discard is that if we put wrong input in terms of remove it will ouput as error  and in terms of discard it will not show an erro repective of what ever value user input------"

#----------- 7  pop
# print(s2.pop())
" it will pop out any random value from the set and come inform of output"

#----------- 8 del
"to delet the hole set "
# print(s1)  # here i can print the values the s1 because it is execting
del s1  #-------deleting the s1 set
# print(s1)  # as we have deleted the set s1 know it basically not exects

#----------- 9 clear
"to only clear values in the set and not to delet the set "
"we use clear"

set1 = {"rahul", "nikhil"}
# print(set1)  #----data will get printed
set1.clear()
# print(set1) # we have clear the data and now just the repective set is remaing

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
"-------------------------- dictionary and ther methods--------------------------------"
"dict are database where we accociate a vaule to another values to link the both value"

dict1 = {
    "big brother": "nikhil",
    "small brother": "rahul",
    "game name": "light",
    "game naem": "joker"
}
# print(dict1)
# print(type(dict1))
"---------------dict methods--------------------"
"""

(----HERE DICT MEANS DICTIONERY----------)

update          if you want to add a dict to another dict use upadte
clear           if you want to clear all values in the dict use clear
delete          if you want to delet the exixtence of the dict then ues del
pop             if you want to remove al value part from the dict the use pop
popitme         this will remove the last pair in the dict
copy            thiy will copy the dict so you can now use to to create a new dict

"""
#-------------- 1  update

ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}
ep1.update(ep2)
# print(ep1)
" if you want to add a dict to another dict we can use update function so it can get updated"

#---------------- 2  clear

# print(ep1)  # first there are data in dict ep1
# ep1.clear()
# print(ep1) # after clear no data remain at ep1 only dict is ramain
# print(type(ep1))

# ep1=set(ep1)
# ep1=set()
# print(type(ep1))

#------------------ 3  pop

# to remove a value in the dict
ep1.pop(122)  #it will remove it's correspondeing number as well
# print(ep1)
" if you want to remove an pair from the dict you use pop"

#--------------  4  popitme
ep1.popitem()
# print(ep1)
"this will remove the last pair from the dict"

#------------ 5  del

# print(ep1)  # this will print the value in dict
del ep1  # here we are deleting the ep1
# print(ep1) # thus ep1 is not in existence

# to make a new dic {} by adding n numbers of dic's{}
dic1 = {"name": "nikhil", "age": 20, "gender": "male"}

dic2 = {"name": "rahul", "age": 14, "gender": "CHAD male"}

dic3 = {"dic1": dic1.copy(), "dic2": dic2.copy()}
"the index of dic1 is 0 and dic2 is 1 to asses them you have to just tell it's index"

# print(dic3)
print(f"{dic3['dic1']}\n{dic3['dic2']}")

print(type(dic3))
"""
{'name': 'nikhil', 'age': 20, 'gender': 'male'}
{'name': 'rahul', 'age': 14, 'gender': 'CHAD male'}
<class 'dict'>"""
