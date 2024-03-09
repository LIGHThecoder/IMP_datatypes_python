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
update
clear
delete
pop
popitme
copy

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
