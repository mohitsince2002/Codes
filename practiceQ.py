
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

year = int(input('Enter Any Year:- '))

if year % 400 == 0 or (year %100 != 0 and year % 4 ==0):
    print(f'{year} is a Leap Year')
else:
    print(f'{year} is not Leap Year')