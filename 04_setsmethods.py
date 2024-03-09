"--------------------------------sets--------------------------------------------------"
"sets are changeabel they are unorder as well they are denoted by {} repetation are also now allowed in sets"

set1 = {"rahul", "nikhil"}
# print(set1)
# print(type(set1))

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
