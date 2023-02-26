import datetime

fruits = [{'name': 'orange', 'color': 'red'}, {'name': 'banana', 'color': 'yellow'}, {'name': 'apple', 'color': 'orange'}]

sorted_fruits = sorted(fruits, key=lambda x: x['color'])


print(sorted_fruits)

current_day = datetime.datetime.now().day

print(current_day)
