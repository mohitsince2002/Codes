
# Q1 Write a Python program to calculate profit or loss.

# cost_price = float(input('Enter Cost Prince :- '))
# selling_price = float(input('Enter Selling Prince :- '))

# if selling_price > cost_price :
#     profit = selling_price - cost_price
#     print('Profit:- ' , profit)
# elif cost_price > selling_price:
#     loss = cost_price - selling_price 
#     print('Loss :- ' , loss)
# else:
#     print('No Loss , No Profit')




# Q2 Write a Python program to check whether a year is a leap year or not.

# year = int(input('Enter Any Year:- '))

# if year % 400 == 0 or (year %100 != 0 and year % 4 ==0):
#     print(f'{year} is a Leap Year')
# else:
#     print(f'{year} is not Leap Year')




# Q3 Write a Python program to check whether a number is divisible by 5 and 11 or not.

# num = int(input('Enter Any Number :- '))

# if num % 5 ==0 and num % 11==0 :
#     print(f'{num} is divide by 5 and 11 both ')
# else: 
#     print(f'{num} is not divide by 5 and 11 both ')





# Q4 Write a Python program to find the maximum between three numbers.

# num1 = float(input('Enter First Number :- '))
# num2 = float(input('enter Second Number :- '))
# num3 = float(input('enter Third Number :- '))

# if num1> num2 and num1 > num3 :
#     print(f'{num1} is a maximum number ')
# elif num2>num1 and num2>num3 :
#     print(f'{num2} is a maximum number ')
# else : 
#     print(f'{num3} is a maximum number ')





# Q5 Write a Python program to input any alphabet and check whether it is a vowel or consonant.

# alfa = str(input('Enter Any Alfabat :- '))

# if alfa == 'a' or alfa == 'A' or alfa == 'e' or alfa == 'E' or alfa =='i' or alfa == 'I' or alfa == 'o' or alfa == 'O' or alfa =='u' or alfa == 'U' :
#     print('Vowel')
# else:
#     print('Consonant')




# Q6 Write a Python program to input any character and check whether it is an alphabet, digit, or special character.

# char = input('Enter any Character :- ')

# if char.isalpha():
#     print('Alphabet')
# elif char.isdigit():
#     print('Digit')
# else:
#     print('Special Character')



# Q7 Write a Python program to input marks of five subjects: Physics, Chemistry, Biology,
# Mathematics and Computer. Calculate percentage and grade according to the following: -
# Percentage >= 90% : Grade A - Percentage >= 80% : Grade B - Percentage >= 70% : Grade C -
# Percentage >= 60% : Grade D - Percentage >= 40% : Grade E - Percentage < 40% : Grade F


phy = float(input('Enter marks of phy:- '))
chem = float(input('Enter marks of chem:- '))
maths = float(input('Enter marks of maths:- '))
hindi = float(input('Enter marks of hindi:- '))
eng = float(input('Enter marks of eng:- '))

total_marks = phy + chem + maths + hindi + eng 
percentage = (total_marks / 500) * 100 

if percentage >= 90 : 
    grade = "A"
elif percentage >=80:
    grade = "B"
elif percentage >=70:
    grade = "C"
elif percentage >=60:
    grade = "D"
elif percentage >=40:
    grade = "E"
else:
    grade = "F"

print(total_marks,"/500")
print("percentage",percentage,"%")
print('Grade:' , grade)


# Q8 Write a Python program to input basic salary of an employee and calculate its Gross salary
# according to the following: - Basic Salary <= 10000 : HRA = 20%, DA = 80% - Basic Salary <=
# 20000 : HRA = 25%, DA = 90% - Basic Salary > 20000 : HRA = 30%, DA = 95%





























