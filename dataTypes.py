
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






















# ---------------------Lish 

# fruits = ['apple' , 'banana' , 'cherry' , 'mango']

# print(fruits)
































