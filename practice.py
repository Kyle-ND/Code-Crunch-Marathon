# this is a practice file where you can play around with the code and test your functions or try new things
#do not change the code in this file just edit on blank lines

students = {
    "jason": 90,
    "james": 80,
    "jane": 70,
    "jill": 60,
    "jerry": 50
}

weather = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

student_names = ["jason", "james", "jane", "jill", "jerry"]


list_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

student_names = ["jason", "james", "jane", "jill", "jerry"]

def pass_students():

    for key, value in students.items():
        if value > 50:
            pass
            # print(key + ' ' + 'passed')

    
    # print(list(students.values())[0])

    number = []

    for i in list_nums:
        number.append(i * 2)

    # print(number)

    new_dict = dict(zip(list_nums, number))

    # print(list_nums)
    # print(number)
    # print(new_dict)
    weather_dict = {}

    for key, value in weather.items():
        convert = value
        weather_dict[key] = (convert * 9 /5) + 32 

    # print(weather_dict)
pass_students()

import random
# Open file
with open('quotes.txt') as file1:
    lines = file1.readlines()

# print(lines)
select_item = random.choice(lines)
print(select_item)





# contact_book = {
#     "key":"value",
#     "Anele":607898787,
#     "Khosi":78965443221

#     }


# for x in contact_book:
#     print(x)

# for value in contact_book.values():
#     print(value)

# for key,value in contact_book.items():
#     if key == "Anele":
#         contact_book[key] = 1
# print(contact_book)


# new_contacts = {"sihle":99886576,"kyle":98876554546}

# contact_book.update(new_contacts)

# print(contact_book)