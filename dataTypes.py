
#--------------------------String(immutable string)-----------------------

# name = 'yash '
# char = 'a'
# password = 'yash@123'
# para= '''In Python, a string is a 
# sequence of characters used 
# to represent text. It is a 
# fundamental data type for
# handling textual information. '''

# name = 'yash'
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[-1])


# name = 'yash'

# index = 0 
# while index<= 3 : 
#     print(name[index])
#     index += 1


# name = 'yash'
# for char in name:
#     print(char)


# fname = 'yash'
# print(len(fname))


# fname = 'yash'
# lname = 'shrivastav'
# fullname = fname + ' '+ lname 
# print(fullname)



# --------------------case conversion 

# upper()
# lower()
# title()
# capitalize()
# swapcase()




# text = 'hello World what Are you Doing'
# formatted_text = text.upper()
# print(formatted_text)
# formatted_text2 = text.lower()
# print(formatted_text2)
# formatted_text3 = text.title()
# print(formatted_text3)
# formatted_text4 = text.capitalize()
# print(formatted_text4)
# print(text.swapcase())



#--------search and check------
# find()
# rfind()
# index()
# rindex()
# count()
# startswith()
# endswith()

# text = 'Python is a Programming is Language is'

# print(text.find('is'))

# print(text.find('is',8))

# print(text.rfind('is'))

# print(text.find('are'))

# print(text.index('is'))

# # print(text.index('are')) # // error

# print(text.rindex('is'))

# print(text.count('is'))

# print(text.startswith('P'))

# print(text.endswith('is'))

# print(len(text))


# text = ' Python is a Programming is Language is '

# print(len(text))
# print(text.startswith('P'))


# print(text.startswith('P'))

# trimmed_text = text.strip()
# trimmed_text = text.rsplit()
# trimmed_text = text.lsplit()

# print(trimmed_text)

# print(len(trimmed_text))

# print(trimmed_text.startswith('P'))



# text = ' Python is a Programming is Language is '
# new_text = text.replace('Python' , 'Javascript')
# print(new_text)


# text = ' Python is a Programming is Language is '
# new_text = text.replace( 'is' , 'are')
# print(new_text)


# --------------Split
# text = ' Python is a Programming is Language is '
# split_text = text.split()
# print(split_text)

# text = ' Python is, a Programming ,is Language is '
# split_text = text.split(',')
# print(split_text)


# date = "06-10-2025"
# data = date.split('-')
# print(data)

# day = data[0]
# month = data[1]
# year = data[2]
# print(day)
# print(month)
# print(year)

# ----------------------Join

# date = ["06","10","2025"]
# string_date = "-".join(date)
# print(string_date)

# student = ["1", "vivan" ,"mumbai"]
# string_student = ",".join(student)
# print(string_student)

# data = "1,vivan,mumbai"
# data_formatted= data.split(',')
# print(data_formatted)


# ----------------Slicing----------------

# slicing = text[start:end:step]
# start default = 0 
# end default = last char/ Value
# step default = 1


# text = 'Python is a Programming is Language is'
# language = text[0:6]
# print(language)


# text = 'Python is a Programming is Language is'
# language_type = text[12:24]
# print(language_type)


# text = 'Python is a Programming is Language is'
# language_type = text[12:24:2]
# print(language_type)


#----------------create a copy string
# text = 'Python is a Programming is Language is'

# copy_text = "".join(text)
# print(copy_text)
# print(text)
# print(text is copy_text)


# text = "Python"
# reversed_text = text[::-1]
# print(reversed_text)


# text = "madam"
# reversed_text = text[::-1]

# if text == reversed_text:
#     print('palindrome')
# else:
#     print('not palindrome')



#------------------------------List------------------------------

# mutable 
# orderd 
# duplicate allow 
# homo and hetro supported 
# indexed 


# fruits = ['apple' , 'banana' , 'pinapple' , 'cherry']
# print(fruits)
# print(fruits[1])
# print(fruits[-1]) #  // last fruit 
# for fruit in fruits :
#     print(fruits)


# fruits = ['apple' , 'banana' , 'pinapple' , 'cherry' , 'kiwi']
# choice = input('enter your choice -')

# if choice in fruits:
#     print('Available')
# else:
#     print("Out of Stock")


# fruits = ['apple' , 'banana' , 'pinapple' , 'cherry' , 'kiwi']
# selected_fruits = fruits[2:]
# print(selected_fruits)

# fruits = ['apple' , 'banana' , 'pinapple' , 'cherry' , 'kiwi']
# selected_fruits = fruits[:]
# print(selected_fruits)


# fruits = ['apple' , 'banana' , 'pinapple' , 'cherry' , 'kiwi']
# selected_fruits = fruits[::-1]
# print(selected_fruits)


# fruits = ['apple' , 'banana' , 'pinapple' , 'cherry' , 'kiwi']
# fruits.append('orange')
# print(fruits)


# fruits = ['apple' , 'banana' , 'pinapple' , 'cherry' , 'kiwi']
# fruits.insert(1,'orange')
# print(fruits)


# fruits = ["apple", "banana"]
# fruits.extend(["cherry", "orange"])
# print(fruits)

# fruits = ["apple", "banana"]
# fruits.extend(("cherry", "orange"))
# print(fruits)

# fruits = ["apple", "banana"]
# more_fruits = ["cherry", "orange"]
# fruits.extend(more_fruits)
# print(fruits)  




# marks = []
# count = 1 
# while count <=5:
#     sub_marks = int(input('enter marks -')) 
#     marks.append(sub_marks)
#     count+=1 
# print(marks)


# marks = []
# count = 1 
# for count in range(5):
#     sub_marks = int(input('enter marks -'))
#     marks.append(sub_marks)
# print(marks)


#-------------- How to update / change the exising element

# fruits = ['apple' , 'banana' , 'pinapple' , 'cherry' , 'kiwi']
# fruits[2] = "orange"
# print(fruits)


# fruits = ['apple' , 'banana' , 'pinapple' , 'cherry' , 'kiwi']
# print(fruits)
# del fruits
# print(fruits)


# fruits = ['apple' , 'banana' , 'pinapple' , 'cherry' , 'kiwi']
# print(fruits)
# del fruits[2]
# print(fruits)


# fruits = ['apple' , 'banana' , 'pinapple' , 'cherry' , 'kiwi']
# print(fruits)
# fruits.pop(2)
# print(fruits)


# fruits = ['apple' , 'banana' , 'pinapple' , 'cherry' , 'kiwi']
# print(fruits)
# fruits.pop()
# print(fruits) // remove the last element



# fruits = ['apple' , 'banana' , 'pinapple' , 'cherry' , 'kiwi']
# print(fruits)
# fruits.remove('banana')
# print(fruits)


# fruits = ['apple' , 'banana' , 'pinapple' , 'cherry' , 'kiwi']
# print(fruits)
# fruits.sort()
# print(fruits)


# fruits = ['apple' , 'banana' , 'pinapple' , 'cherry' , 'kiwi']
# print(fruits)
# fruits.reverse()
# print(fruits)


# fruits = ['apple' , 'banana' , 'pinapple' , 'cherry' , 'kiwi']
# fruits.clear()
# print(fruits) # //[]


#------serching

# fruits = ['apple' , 'banana' , 'pinapple' , 'cherry' , 'kiwi' ]
# element_pos = fruits.index('banana')
# print(element_pos)


# fruits = ['apple' , 'banana' , 'pinapple' , 'cherry' , 'kiwi' , "cherry"]
# element_pos = fruits.index('cherry' , 2)
# print(element_pos)


# fruits = ['apple' , 'banana' , 'pinapple' , 'cherry' , 'kiwi' ]
# copy_fruits = fruits.copy()
# print(fruits is copy_fruits)


# fruits = ['apple' , 'banana' , 'pinapple' , 'cherry' , 'kiwi' , "cherry"]
# count_cherry = fruits.count('cherry')
# print(count_cherry)


# numbers = [5, 3, 8, 1]
# numbers.sort(reverse=True)
# print(numbers)


# numbers = [1,3,5,3,69,37,65,57]
# reverse_number = sorted(numbers)
# print(reverse_number)
# print(numbers)


# numbers = [1,3,5,3,69,37,65,57]
# max_value = max(numbers)
# print(max_value)


# numbers = [1,3,5,3,69,37,65,57]
# sum_value = sum(numbers)
# print(sum_value)


# numbers = [1,3,5,3,69,37,65,57]
# min_value = min(numbers)
# print(min_value)


# -------------nested List / multi dimension list

# number = [10,20,30] one dimension list


# matrix = [[10,20,30],[40,50,60]] // two dimension list
# print(matrix)
# print(matrix[0])
# print(matrix[0][0])

# numbers = [
#     [[10,20,30],[10,20,30]], 
#     [[10,20,30],[10,20,30]]
#            ]   // three dimension list
# print(numbers[0][0][0])



# find the maximum/highest value from the list without using build in function 

# marks = [10,40,30,20,30]

# max_marks = marks[0]

# # for index in range(1 , len(marks)):
# #     if marks[index]>max_marks:
# #         max_marks = marks[index]

# for value in marks:
#     if value>max_marks:
#         max_marks = value
# print(max_marks)



# H.W 

# find the highsert value 
# lowest value 
# sum of the list 























# matrix1 = [[1,2],[3,4]]
# matrix2 = [[5,6],[2,1]]

# for i in range(len(matrix1)):
#     for j in range(len(matrix1[i])):
#         print(matrix1[i][j]+matrix2[i][j],end=' ')
#     print()



#---------------------Tuple---------------------

# fruits = ('apple' , 'banana' , 'cherry' , 'kiwi' , 'orange' , 'pinapple' , 'banana' , 'kiwi')
# num = 10,
# print(type(num))


# fruits = ('apple' , 'banana' , 'cherry' , 'kiwi' , 'orange' , 'pinapple' , 'banana' , 'kiwi')
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[-1])


# fruits = ('apple' , 'banana' , 'cherry' , 'kiwi' , 'orange' , 'pinapple' , 'banana' , 'kiwi')
# print(fruits.count('kiwi'))

# fruits = ('apple' , 'banana' , 'cherry' , 'kiwi' , 'orange' , 'pinapple' , 'banana' , 'kiwi')
# print(fruits.index('kiwi'))

# num = (10,20,39,49)
# print(max(num))




# fruit1 = ('apple' , 'banana' , 'cherry')
# fruit2 = ('watermalon' , 'pinapple' , 'kiw')
# fruit3 = fruit1 + fruit2
# print(fruit3)


# gender = ('male' , 'female' , 'other')  #  // use tuple this case 
# size = ('s','m','l','xl','xxl')          


# size = ('s','m','l','xl','xxl')   
# print(size)
# list_size = list(size)
# list_size.append('xxxl')
# size = tuple(list_size)
# print(size)



#-----------Set-----------------


# fruits = {'apple' , 'banana' , 'cherry' , 'kiwi' , 'orange' , 'pinapple'}
# print(fruits)
# print(type(fruits))



# fruits = set({})
# fruits.add('apple')
# fruits.add(10)
# fruits.add('cherry')
# print(fruits)


# fruits = {'apple' , 'banana' , 'cherry' , 'kiwi' , 'orange' , 'pinapple'}
# fruits.remove("banana")
# print(fruits)



# fruits = {'apple' , 'banana' , 'cherry' , 'kiwi'}
# fruits.update([ 'orange' , 'pinapple'])
# print(fruits)


# fruits = {'apple' , 'banana' , 'cherry' , 'kiwi' , 'orange' , 'pinapple'}
# fruits.remove('apple')
# print(fruits)


# # pop()
# # clear()
# # union()
# # copy()
# # intersection()
# # intersection_update()
# # defference()
# # symmetric_defference()
# # symmetric_defference_update()


# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7}
# print("A =", A)
# print("B =", B)


# # pop()

# A = {1, 2, 3, 4}
# removed = A.pop()
# print("Removed element:", removed)
# print("After pop:", A)


# # clear()

# A = {1, 2, 3}
# A.clear()
# print(A)


# # union()

# A = {1, 2, 3}
# B = {3, 4, 5}
# C = A.union(B)
# print(C)


# # copy()

# A = {1, 2, 3}
# B = A.copy()
# print(B)


# # intersection()

# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# C = A.intersection(B)
# print(C)


# # intersection_update()

# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# A.intersection_update(B)
# print(A)


# # defference()

# A = {1, 2, 3, 4}
# B = {3, 4, 5}
# C = A.difference(B)
# print(C)


# # symmetric_defference()

# A = {1, 2, 3}
# B = {3, 4, 5}
# C = A.symmetric_difference(B)
# print(C)


# # symmetric_defference_update()

# A = {1, 2, 3}
# B = {3, 4, 5}
# A.symmetric_difference_update(B)
# print(A)



#--------------------------Dictionary------------------------------

# Dictionaries are used to store data values in key:value pairs.
# Dictionaries are written with curly brackets, and have keys and values:
# it is a mutable object


# marks = { 
    
#     'phy' : 90,
#     'chem' : 59,
#     'maths' : 78,
#     'eng' : 59
# }

# print(marks)




# marks = {
#     'phy' : 90,
#     'chem' : 59,
#     'maths' : 78,
#     'eng' : 59,
#     'chem' : 40
# }
# print(marks)


# marks = {}
# marks['chem']= 20
# print(marks)


# marks = {
#     'phy' : 90,
#     'chem' : 59,
#     'maths' : 78,
#     'eng' : 59
    
# }
# marks['chem']=40
# print(marks)  # // update a value 



# user = {
#     'name': 'yash',
#     'age': 24,
#     'city' : 'mumbai',
#     'marks' :  {'phy' : 90,'chem' : 59,'maths' : 78,'eng' : 59}
# }

# print(user)
# print(user['name'])
# print(user['marks'])
# print(user['marks']['phy'])



# user = {
#     'name': 'yash',
#     'age': 24,
#     'city' : 'mumbai',
#     'marks' :  {'phy' : 90,'chem' : 59,'maths' : 78,'eng' : 59}
# }

# print(user.get('fname' , 'key does not exist'))


# user = {
#     'name': 'yash',
#     'age': 24,
#     'city' : 'mumbai',
#     'marks' :  {'phy' : 90,'chem' : 59,'maths' : 78,'eng' : 59}
# }

# print(user.keys())
# print(user.values())
# print(user.items())


# user = {
#     'name': 'yash',
#     'age': 24,
#     'city' : 'mumbai',
#     'marks' :  {'phy' : 90,'chem' : 59,'maths' : 78,'eng' : 59}
# }
# address = {
#     'pincode' : 400101,
#     'flat': 404,
#     'landmark' : 'terapanth bhavan'
# }

# user.update(address)
# print(user)



# user = {
#     'name': 'yash',
#     'age': 24,
#     'city' : 'mumbai',
#     'marks' :  {'phy' : 90,'chem' : 59,'maths' : 78,'eng' : 59}
# }

# user.pop('name')
# print(user)


# user = {
#     'name': 'yash',
#     'age': 24,
#     'city' : 'mumbai',
#     'marks' :  {'phy' : 90,'chem' : 59,'maths' : 78,'eng' : 59}
# }

# print(user)
# user_item = user.popitem()
# print(user_item)



user = {
    'name': 'yash',
    'age': 24,
    'city' : 'mumbai',
    'marks' :  {'phy' : 90,'chem' : 59,'maths' : 78,'eng' : 59}
}

# for i in user.key(): 
#     print(i)

# for key,value in user.items():
#     print(f'key: {key} , value: {value}')

# for i in user.values(): 
#     print(i)

# for i in user.items(): 
#     print(i)


# Unpacking of tuple

# fruits = 'apple' , 'orange' , 'banana'
# fruit1 , fruit2 , fruit3 = fruits 
# print(fruit1)


# -------------------------------- List comprehension

# list_name = [var for var in range()]

# num  = []
# for i in range(1,10):
#     num.append(i)
# print(num)


# num = [i for i in range(1,5)]
# print(num)



# fruits = ['apple' , 'orange' , 'banana' , 'kiwi']
# new_fruits = [fruit for fruit in fruits]
# print(new_fruits)


# num = [3,2,5,6,4,3,5,6,7,8,9]
# even_num = [i for i in num if i%2==0]
# print(even_num)


# fruits = ["apple", "banana", "cherry"]
# upper_fruits = [fruit.upper() for fruit in fruits]
# print(upper_fruits)


# num = [1,2,3,4,5,6]
# odd_even = ['Even' if x % 2==0 else 'Odd' for x in num]
# print(odd_even)



# squares = [x**2 for x in range(1,11)]
# print(squares)



# dictionary comrehension 

# [key_Expression : value_Expression for item in iterableif condition]


# squares = {x: x**2 for x in range(1, 6)}
# print(squares)


fruits = ['apple', 'banana', 'cherry']
lengths = {fruit: len(fruit) for fruit in fruits}
print(lengths)


# even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
# print(even_squares)


nums = range(11)
result = {x: ('even' if x % 2 == 0 else 'odd') for x in nums}
print(result)





















