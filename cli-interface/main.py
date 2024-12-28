import login
import register

print("Enter Your Choice:\n\t1. Login\n\t2. Register\n\t0. Quit")
choice = int(input())

while (choice == 1 or choice == 2):
    if(choice == 1):
        login.login()
    elif(choice == 2):
        register.register()
    print("Enter Your Choice:\n\t1. Login\n\t2. Register\n\t0. Quit")
    choice = int(input())
