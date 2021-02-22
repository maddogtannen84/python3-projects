""" Contact Generator
----------------------------------------
"""
# //Loop back to this point once code finishes
loop = 1
while (loop < 10):

# // All the questions that the program asks the user
    firstName = input("What is your FIRST name?: ")
    lastName = input("What is your LAST name?: ")
# // Welcomes the user the the application
    print ("--------------------------------------------------")
    print ("Welcome",firstName.capitalize(), lastName.capitalize(),"!!!")
# // Continues to ask more questions about the user
    nameOfEmployer = input("Who do you work for?: ")
    workTitle = input("What is your position at this company?: ")
    workExperience = input("How many years have you been working for this company?:")
    workEmail = input("Last question... what email can we contact you at?: ")
# // Displays the story based on the users input
    print ("--------------------------------------------------")
    print ("Thank you! Please validate the following sentence:")
    print ("--------------------------------------------------")
    print ("Hello, my name is", firstName.capitalize(), lastName.capitalize(),". I have been working for", nameOfEmployer,"as a", workTitle,"for the last", workExperience,"years.")
    print ("If you have any questions please feel free to contact me at", workEmail,". Thank you,", firstName)
    print ("--------------------------------------------------")
    x = input("Was this correct? True or False:")
    if x == "True" or "true" or "no" or "nope":
        print ("--------------------------------------------------")
        print ("That's great! Have a wonderful day!")
        print ("--------------------------------------------------")
        loop = loop + 10
    else:
        print ("--------------------------------------------------")
        print ("Oh man! Let's try that again!")
        print ("--------------------------------------------------")
        loop = loop + 1
# // Loop back to the top if the information is NOT correct
