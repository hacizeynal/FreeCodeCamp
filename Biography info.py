"""
https://www.freecodecamp.org/news/python-projects-junior-developers/

Ask a user for their personal information one question at a time. Then check that the information they entered is
valid. Finally, print a summary of all the information they entered back to them.

Example: What is your name? If the user enters * you prompt them that the input is wrong, and ask them to enter a
valid name.

At the end you print a summary that looks like this:

- Name: John Doe
- Date of birth: Jan 1, 1954
- Address: 24 fifth Ave, NY
- Personal goals: To be the best programmer there ever was.

"""
from datetime import datetime
import re

format_date = "%d-%m-%Y"
special_char = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')

i = 0
while True:
    user_input = input("Please enter your sentence to build biography! ")
    name, date_of_birth, address, personal_goals = user_input.split(",")
    # Validating if string format represent correct date format
    try:
        validate_date = bool(datetime.strptime(date_of_birth, format_date))
    except ValueError:
        validate_date = False
        # print("Incorrect date format")
        # continue  # to go back to beginning of code
    # Validating if string does not contain any special characters.
    if validate_date is False:
        print("Incorrect date format")
        i = i + 1
        if i == 3:
            print("Too many attempts ,come later and check again")
            break
    elif special_char.search(name) is None:
        print("- Name: {}".format(name))
        print("- Date of birth: {}".format(date_of_birth))
        print("- Address:{}".format(address))
        print("- Personal goals:{}".format(personal_goals))
        break
    else:
        print("Special character detected on the name!")
        i = i + 1
        if i == 3:
            print("Too many attempts ,come later and check again")
            break
