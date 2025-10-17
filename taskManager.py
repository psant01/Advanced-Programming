# A simple python program to act as a task manager
# The program makes use of input, conditional and control structures

userName = "paul"
pwd = "L3tM31n"

usernameInput = input("Please enter your username: ")
userPwdInput = input("Please enter your password: ")

while((usernameInput != userName and userPwdInput != pwd)):
    print("sorry, incorrect username or password entered. Please try again")
    usernameInput = input("Please enter your username: ")
    userPwdInput = input("Please enter your password: ")

# Begin with a welcome message

print("Welcome to the Task Manager, what would you like to do?")

print("1. Add a new task")
print("2. Update and existing task in your list")
print("3. Delete a task from your current list")
print("4. Print your list of tasks")
print("Enter exit to leave")

userChoice = input("Please enter which option you would like")

# Check option choice and then execute correct function

if(userChoice == "1"):
    
    taskName = input("Please add a task name: ")
elif(userChoice == "2"):
    taskName = input("Please state which task you wish to update")
elif(userChoice == "3"):
    taskName = input("Please state which task you wish to delete.")
elif(userChoice == "4"):
    print("The tasks in your current list are:")
elif(userChoice == "exit" or userChoice == "Exit"):
    print("Goodbye, and thank you for using the talk list manager.")
else:
    print("Sorry, invalid choice entered, exiting the program...")
