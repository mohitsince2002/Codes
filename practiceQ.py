
# Q1 Write a Python program to calculate profit or loss.

cost_price = float(input('Enter Cost Prince :- '))
selling_price = float(input('Enter Selling Prince :- '))

if selling_price > cost_price :
    profit = selling_price - cost_price
    print('Profit:- ' , profit)
elif cost_price > selling_price:
    loss = cost_price - selling_price 
    print('Loss :- ' , loss)
else:
    print('No Loss , No Profit')
    