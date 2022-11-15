import time
print("                                                                         Luigie's Resturaunt")
print("Input 1 to Sign In")
print("Input 2 to Sign Up")
print("Input 3 to Quit")
stage_1_input = input("")
username_berney = "Berney"
password_berney = "BerneyIsaBird"
username_simdi = "Simdi"
password_simdi = "LOL"
if stage_1_input == "1":
    username = input("Username: ")
    password = input("Password: ")
    if username == username_berney and password == password_berney or username == username_simdi and password == password_simdi:
        print("The Menu Is In Downloads Folder")
        order = input("Welcome, What Would You Like To Order? ")
        if order == "0":
            print(f"Your Chicken Nuggets Will Be Ready In 5 minutes")
            time.sleep(300)
            print("Thank You For Using Our App *1109811098*")
        elif order == "1":
            print(f"Your Steak Will Be Ready In 1 hour")
            time.sleep(3600)
            print("Thank You For Using Our App *1109811098*")
        elif order == "2":
            print(f"Your Ostritch Egg Will Be Ready In 40 minutes")
            time.sleep(2400)
            print("Thank You For Using Our App *1109811098*")
        elif order == "3":
            print(f"Your Chucken Soup Will Be Ready In 50 minutes")
            time.sleep(1800)
            print("Thank You For Using Our App *1109811098*")
        elif order == "665511":
            print(f"The Secret Masterpiece Is Coming Up!!!")
            time.sleep(3)
            print("Recepie Keeper: I see you, want the secret dish?")
            time.sleep(3)
            print("Recepie Keeper: Then there is one more challenge")
            time.sleep(3)
            secret_number = input("Recepie Keeper: You Guessed The Secret Dish So What Is The Secret Number? ")
            if secret_number == "1109811098":
                print("Recepie Keeper: Fine, You Guessed It Right.")
                time.sleep(3)
                print("Recepie Keeper: The Recepie For The Secret Food Is")
                time.sleep(3)
                print("Recepie Keeper: #1 ------------")
                time.sleep(1)
                print("Recepie Keeper: #2 ------------")
                time.sleep(1)
                print("Recepie Keeper: #3 ------------")
                time.sleep(1)
                print("Recepie Keeper: #4 ------------")
                time.sleep(1)
                print("Recepie Keeper: #5 ------------")
                time.sleep(1)
                print("Recepie Keeper: #6 ------------")
                time.sleep(1)
                print("Recepie Keeper: #7 ------------")
                time.sleep(1)
                print("Recepie Keeper: #8 ------------")
                time.sleep(1)
                print("Recepie Keeper: #9 ------------")
                time.sleep(1)
                print("Recepie Keeper: #10 ------------")
                time.sleep(1)
                print("Recepie Keeper: #11 ------------")
                time.sleep(1)
                print("Recepie Keeper: #12 ------------")
                print("Recepie Keeper: That's All. DO NOT TELL ANYONE THE NUMBER OR DISH OR ELSE I WILL ---------------------------------------")
                time.sleep(5)
            else:
                print("That Is Not Correct. Come Back When You Are Ready")
    else:
        print("Incorrect Username Or Password")


elif stage_1_input == "2":

    new_user = input("Username: ")
    new_pass = input("Password: ")
    print("                                                                         Luigie's Resturaunt")
    print("Input 1 to Sign In")
    print("Input 2 to Log Out")
    print("Input 3 to Quit")
    stage_1_input = input("")
    username_berney = "Berney"
    password_berney = "BerneyIsaBird"
    username_simdi = "Simdi"
    password_simdi = "LOL"
    if stage_1_input == "1":
        username = input("Username: ")
        password = input("Password: ")
        if username == username_berney and password == password_berney or username == username_simdi and password == password_simdi or username == new_user and password == new_pass:
            print("The Menu Is In Downloads Folder")
            order = input("Welcome, What Would You Like To Order? ")
            if order == "0":
                print(f"Your Chicken Nuggets Will Be Ready In 5 minutes")
                time.sleep(300)
                print("Thank You For Using Our App *1109811098*")
            elif order == "1":
                print(f"Your Steak Will Be Ready In 1 hour")
                time.sleep(3600)
                print("Thank You For Using Our App *1109811098*")
            elif order == "2":
                print(f"Your Ostritch Egg Will Be Ready In 40 minutes")
                time.sleep(2400)
                print("Thank You For Using Our App *1109811098*")
            elif order == "3":
                print(f"Your Chucken Soup Will Be Ready In 30 minutes")
                time.sleep(1800)
                print("Thank You For Using Our App *1109811098*")
            elif order == "665511":
                print(f"The Secret Masterpiece Is Coming Up!!!")
                time.sleep(3)
                print("Recepie Keeper: I see you, want the secret dish?")
                time.sleep(3)
                print("Recepie Keeper: Then there is one more challenge")
                time.sleep(3)
                secret_number = input("Recepie Keeper: You Guessed The Secret Dish So What Is The Secret Number? ")
                if secret_number == "1109811098":
                    print("Recepie Keeper: Fine, You Guessed It Right.")
                    time.sleep(3)
                    print("Recepie Keeper: The Recepie For The Secret Food Is")
                    time.sleep(3)
                    print("Recepie Keeper: #1 ------------")
                    time.sleep(1)
                    print("Recepie Keeper: #2 ------------")
                    time.sleep(1)
                    print("Recepie Keeper: #3 ------------")
                    time.sleep(1)
                    print("Recepie Keeper: #4 ------------")
                    time.sleep(1)
                    print("Recepie Keeper: #5 ------------")
                    time.sleep(1)
                    print("Recepie Keeper: #6 ------------")
                    time.sleep(1)
                    print("Recepie Keeper: #7 ------------")
                    time.sleep(1)
                    print("Recepie Keeper: #8 ------------")
                    time.sleep(1)
                    print("Recepie Keeper: #9 ------------")
                    time.sleep(1)
                    print("Recepie Keeper: #10 ------------")
                    time.sleep(1)
                    print("Recepie Keeper: #11 ------------")
                    time.sleep(1)
                    print("Recepie Keeper: #12 ------------")
                    print("Recepie Keeper: That's All. DO NOT TELL ANYONE THE NUMBER OR DISH OR ELSE I WILL ---------------------------------------")
                    time.sleep(5)
                else:
                    print("That Is Not Correct. Come Back When You Are Ready")
        else:
            print("Incorrect Username Or Password")


    elif stage_1_input == "2":
        new_user = input("Username: ")
        new_pass = input("Password: ")

    elif stage_1_input == "3":
        print("Thank You For Using Our App *1109811098*")

elif stage_1_input == "3":
    print("Thank You For Using Our App *1109811098*")