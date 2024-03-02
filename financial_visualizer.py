import matplotlib.pyplot as plt
print("--------------------------------")
print("----- FINANCIAL VISUALIZER -----")
print("--------------------------------")
salary = input("Annual Salary:\n")
housing = input("Monthly Housing:\n")
bills = input("Monthly Bills:\n")
food = input("Weekly Food:\n")
travel = input("Annual Travel:\n")

def isValid(x):
    for i in x:
        if i.isnumeric() == False and i != '.':
            return False
    return True

if isValid(salary) and isValid(housing) and isValid(bills) and isValid(food) and isValid(travel):
    print('All inputs confirmed valid.')
else:
    print('Invalid input, please try again.')

salary = float(salary)
housing = float(housing)
bills = float(bills)
food = float(food)
travel = float(travel)

if salary >= 0 and salary <= 10000:
    tax = round(salary*0.05, 2)
elif salary >= 10001 and salary <= 40000:
    tax = round(salary*0.1, 2)
elif salary >= 40001 and salary <= 80000:
    tax = round(salary*0.15, 2)
else:
    tax = round(salary*0.2, 2)

print(tax)

annual_housing = housing*12
annual_bills = bills*12
annual_food = food*52
annual_travel = travel
annual_tax = tax
annual_extra = salary - annual_housing - annual_bills - annual_food - annual_travel - annual_tax

percent_housing = round(annual_housing/salary*100, 1)
percent_bills = round(annual_bills/salary*100, 1)
percent_food = round(annual_food/salary*100, 1)
percent_travel = round(annual_travel/salary*100, 1)
percent_tax = round(annual_tax/salary*100,1)
percent_extra = round(annual_extra/salary*100,1)

width = int(max(percent_housing, percent_bills, percent_food, percent_travel, percent_tax, percent_extra))

boundary = '----------------------------------' + ('-' * width)
print()
print(boundary)
print('housing | $' + format(annual_housing, '11,.2f') + ' ', end='')
print('| ' + format(percent_housing, '5,.1f') + '% | ' + ('#' * int(percent_housing)))
print('  bills | $' + format(annual_bills, '11,.2f') + ' ', end='')
print('| ' + format(percent_bills, '5,.1f') + '% | ' + ('#' * int(percent_bills)))
print('   food | $' + format(annual_food, '11,.2f') + ' ', end='')
print('| ' + format(percent_food, '5,.1f') + '% | ' + ('#' * int(percent_food)))
print(' travel | $' + format(annual_travel, '11,.2f') + ' ', end='')
print('| ' + format(percent_travel, '5,.1f') + '% | ' + ('#' * int(percent_travel)))
print('    tax | $' + format(annual_tax, '11,.2f') + ' ', end='')
print('| ' + format(percent_tax, '5,.1f') + '% | ' + ('#' * int(percent_tax)))
print('  extra | $' + format(annual_extra, '11,.2f') + ' ', end='')
print('| ' + format(percent_extra, '5,.1f') + '% | ' + ('#' * int(percent_extra)))
print(boundary)

categories = ['housing', 'bills', 'food', 'travel', 'tax', 'extra']
values = [annual_housing, annual_bills, annual_food, annual_travel, annual_tax, annual_extra]
plt.bar(categories, values, color='skyblue')

plt.xlabel('Categories')
plt.ylabel('Value')
plt.title('Distribution')

# Show the chart
plt.show()