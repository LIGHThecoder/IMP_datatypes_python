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
#-----------------------------------------------------------