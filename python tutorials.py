num1 = float(input('enter your first number: '))
num2 = float(input('enter input your second number: '))
sum_results = num1 + num2
print(f"sum: {num1} + {num2} = {sum_results}")


num3 = float(input('enter your third number: '))
num4 = float(input('enter your fourth number: '))
if num4 == 0:
    print('division error, you cannot divide a number by 0')
else:
    div_results = num3 / num4
    print(f'division: {num3} / {num4} = {div_results}')

base = float(input('enter the base of the triangle: '))
height = float(input('enter the height of the triangle: '))
area = 0.5 * base * height 
print(f'the area of the triangle is {area}')

a = input('Enter any value of your choice: ')
b = input('Enter a second value of your choice: ')
print(f'original values: a = {a}, b = {b}')
temp = a
a = b 
b = temp
print(f'Swapped value: a = {a}, b = {b}')
