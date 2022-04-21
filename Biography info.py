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
i = 0
while True:
    user_input = input("Please enter your sentence to build biography: ")
    name, date_of_birth, address, personal_goals = user_input.split(",")
    if "*" not in name:
        print("- Name: {}".format(name))
        print("- Date of birth: {}".format(date_of_birth))
        print("- Address:{}".format(address))
        print("- Personal goals:{}".format(personal_goals))
        break
    else:
        print("You entered incorrect username , please enter valid name again")
        i = i + 1
        if i == 3:
            print("Too many attempts ,come later and check again")
            break
