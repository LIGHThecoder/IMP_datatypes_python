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