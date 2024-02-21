import os
import csv
import time

welcome_message = """
        ╭╮╱╱╱╱╱╱╱╭╮╱╭━━╮
        ┃┃╱╱╱╱╱╱╱┃┃╱╰┫┣╯
        ┃╰━┳━━┳━━┫┃╭╮┃┃╭━╮╭━╮
        ┃╭╮┃╭╮┃╭╮┃╰╯╯┃┃┃╭╮┫╭╮╮
        ┃╰╯┃╰╯┃╰╯┃╭╮┳┫┣┫┃┃┃┃┃┃
        ╰━━┻━━┻━━┻╯╰┻━━┻╯╰┻╯╰╯
**********Welcome to bookInn**********"""
login_message = "Please login or register to use the application:"
login_options = """\
1. Login as normal user
2. Login as admin
3. Register and login as new user
4. Exit application
-> """

user_options = """User Options:
1. Start booking
2. Booking history
3. Account setting
4. Logout
5. Quit application"""

admin_options = user_options + """
Admin Options:
6. Remove user
7. Add admin
8. Remove admin
9. Add booking rooms
10. Remove booking rooms"""

account_setting_options = """
Settings:-
1. Change account info
2. Terminate account
Select an option to continue. (Press Enter to return to menu page)
-> """

user_info_options = """Choose an option to change the info. (Press Enter to cancel)
1. Change Name
2. Change Username
3. Change Password"""

admin_info_options = user_info_options + "\n4. Change Secure PIN"

user_info = "user_info.csv"
admin_info= "admin_info.csv"
rooms_info = "rooms_info.csv"
book_history = "book_history.csv"


def new_screen(username=None, login_as=None):
    """Clear terminal screen and show current user if have."""
    # Check if Operating System is Mac and Linux or Windows
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # Else Operating System is Windows (os.name = nt)
        _ = os.system('cls')
        
    if username != None and login_as != None:
        print(f"Current user: {username}\t\tLogin as: {login_as}\n")

def extract_info(filename):
    info_data = []
    
    with open(filename, "r") as f:
        info_reader = csv.DictReader(f)
    
        for info in info_reader:
            info_data.append(info)
        
    return info_data

def import_info(filename, new_info, import_as):
    if import_as == "user":
        field = ['First Name', 'Last Name', 'Username', 'Password']
    elif import_as == "admin":
        field = ['First Name', 'Last Name', 'Username', 'Password', "Secure PIN"]

    with open(filename, "a", newline="") as f:
        info_writter = csv.DictWriter(f, fieldnames=field)
        info_writter.writerow(new_info)

def user_login():
    user_accounts = extract_info(user_info)
    
    print("Please login with your account. (Press Enter to return to menu page)")
    while True:
        username = input("Username: ")
        if username == "":
            new_screen()
            return None
        password = input("Password: ")
        if password == "":
            new_screen()
            return None
        
        for account in user_accounts:
            if account['Username'] == username:
                if account['Password'] == password:
                    new_screen()
                    credentials = [username, password]   
                    return credentials
                else:
                    error_message = "Incorrect password. Please try again."
                    break
            else:
                error_message = "Account not found. Please try again"
        
        print(error_message)

def admin_login():
    admin_accounts = extract_info(admin_info)
    
    print("Please login with your account. (Press Enter to return to menu page)")
    while True:
        username = input("Username: ")
        if username == "":
            new_screen()
            return None
        password = input("Password: ")
        if password == "":
            new_screen()
            return None
        secure_pin = input("Secure PIN: ")
        if secure_pin == "":
            new_screen()
            return None
        
        for account in admin_accounts:
            if account['Username'] == username:
                if account['Password'] == password:
                    if account['Secure PIN'] == secure_pin:
                        new_screen()
                        credentials = [username, password, secure_pin]
                        return credentials
                    else:
                        error_message = "Incorrect PIN. Please try again."
                        break
                else:
                    error_message = "Incorrect password. Please try again."
                    break
            else:
                error_message = "Account not found. Please try again"
        
        print(error_message)

def register():
    new_screen()
    user_accounts = extract_info(user_info)
    print("Please enter the following information:")
    
    ask_register = True
    while ask_register:
        continue_register = True
        first_name = input("First Name: ")
        if first_name == "":
            main()
            ask_register = False
        last_name = input("Last Name: ")
        if last_name == "":
            main()
            ask_register = False
            
        username = input("Username: ")
        if username == "":
            main()
            ask_register = False
        for account in user_accounts:
            if account["Username"] == username:
                new_screen()
                print("Username used. Please try again.")
                continue_register = False
                break
        
        if continue_register:
            password = input("Password: ")
            if password == "":
                main()
                ask_register = False
            confirm_password = input("Confirm Password: ")
            if confirm_password == "":
                main()
                ask_register = False
            else:
                if len(password) < 6:
                    new_screen()
                    print("Password too short. Please try again.")
                elif password != confirm_password:
                    new_screen()
                    print("The password confirmation does not match. Please try again.")
                else:
                    ask_register = False
                    new_user_data = {'First Name': first_name, 'Last Name':last_name, 'Username': username, 'Password': password}
                    register_as = "user"
                    import_info(user_info, new_user_data, register_as)
                    print("Account successfully created. Going back to login menu in 3s.")
                    time.sleep(3)
                    main()

def ask_login():
    while True:
        login_option = input(login_options)
        print(login_option)
        if login_option not in ["1", "2", "3"]:
            if login_option == "4":
                print("See you next time.")
                quit()
            elif login_option.isdigit():
                print("Please choose a valid option.")
            else:
                print("Please enter a number.")
        else:
            return int(login_option)

def use_app():
    print("You can start using the application. Please choose the following option.")
    
    check_option = True
    while check_option:
        if login_as == "user":
            print(user_options)
            available_options = 5
        elif login_as == "admin":
            print(admin_options)
            available_options = 10
            
        option = input("-> ")
        if option.isdigit():
            option = int(option)
            if option <= 0 or option > available_options:
                new_screen(current_username, login_as)
                print("Invalid option. You can only choose one of the following options.")
            else:
                check_option = False
        elif option == "":
            new_screen(current_username, login_as)
            print("Please choose an option.")
        else:
            new_screen(current_username, login_as)
            print("Invalid option. Please type a number")
    
    new_screen(current_username, login_as)
    if option == 1:
        start_booking()
    elif option == 2:
        booking_history()
    elif option == 3:
        account_setting()
    elif option == 4:
        main()
    elif option == 5:
        quit_app()
    elif option == 6:
        remove_user()
    elif option == 7:
        add_admin()
    elif option == 8:
        remove_admin()
    elif option == 9:
        add_rooms()
    elif option == 10:
        remove_rooms()

def start_booking():
    room_list = []
    while True:
        print("Choose a room for details. (Press Enter to return to app menu)")
        with open(rooms_info, "r") as f:
            info_reader = csv.DictReader(f)
            for info in info_reader:
                room_list.append(info)
                room_options = f"{info['No.']}: {info['Room Name']}"
                print(room_options)
            
        available_options = len(room_list)

        ask_booking = True
        while ask_booking:
            booking_option = input("-> ")
            
            if booking_option == "":
                ask_booking = False
                new_screen(current_username, login_as)
                use_app()
            elif not booking_option.isdigit():
                print("Invalid option. Please choose a room number.")
            else:
                booking_option = int(booking_option)
                
                if booking_option <= 0 or booking_option > available_options:
                    print("Invalid option. PLease choose only one of the following room number.")
                else:
                    room_index = booking_option - 1
                    
                    new_screen(current_username, login_as)
                    selected_room = room_list[room_index]
                    room_name = f"Room Name: {selected_room['Room Name']}\n"
                    room_location = f"Location: {selected_room['Location']}\n"
                    room_price = f"Price per Night: RM {selected_room['Price per night']}\n"
                    room_details = room_name + room_location + room_price
                    print(room_details)
                    
                    ask_booking = False
                    
        ask_if_book = input("Do you want to book this room. (Type 'y' if yes or any input if no)\n-> ").lower()
        if ask_if_book == 'y':
            start_payment(selected_room)
            break
        new_screen(current_username, login_as)

def start_payment(selected_room):
    new_screen(current_username, login_as)
    print("Selected room details:")
    print("- Room Name:", selected_room['Room Name'])
    print("- Location:", selected_room['Location'])
    print("- Price per night: RM", selected_room['Price per night'])
    
    print("\nHow many nights do you want to stay?")
    while True:
        nights = input("-> ")
        if nights.isdigit():
            nights = int(nights)
            break
        else:
            print("Please enter a number.")
    
    total_price = int(selected_room['Price per night']) * nights
    print("\nTotal price to pay: RM", total_price)
    
    proceed_payment = input("Do you want to proceed with payment? (Type 'y' if yes or any input if no)\n-> ").lower()
    if proceed_payment == 'y':
        add_to_history(selected_room['Room Name'], selected_room['Location'], nights, total_price)
        print(f"\nSuccessfully booked room '{selected_room['Room Name']}'.")
        print("Going back to app menu in 3s.")
        time.sleep(3)
        new_screen(current_username, login_as)
        use_app()
    else:
        new_screen(current_username, login_as)
        start_booking()

def add_to_history(room_name, room_location, nights, total_price):
    field = ["Username", "Booked Room","Location", "Nights", "Total Price"]
    new_history = {'Username': current_username, 'Booked Room': room_name, \
        'Location': room_location, 'Nights': nights, 'Total Price': total_price}
    
    history_info = []
    with open(book_history, "r+", newline="") as f:
        info_reader = csv.DictReader(f)
        
        for info in info_reader:
            history_info.append(info)

        info_writter = csv.DictWriter(f, fieldnames=field)
        info_writter.writerow(new_history)

def booking_history():
    history_info = []
    
    with open(book_history, "r") as f:
        info_reader = csv.DictReader(f)
        for info in info_reader:
            history_info.append(info)
    
    print("Booking History:")
    room = 0
    for history in history_info:
        if history['Username'] == current_username:
            room += 1
            print(f"Room {room}:")
            print(f"Room name: {history['Booked Room']}")
            print(f"Room location: {history['Location']}")
            print(f"Nights stayed: {history['Nights']}")
            print(f"Amount paid: {history['Total Price']}\n")
    
    if room == 0:
        new_screen(current_username, login_as)
        print("No booked room yet. Do you want to book room? (Type 'y' if yes or any input if no)")
        ask_book = input("-> ").lower()
        
        if ask_book == 'y':
            start_booking()
        else:
            use_app()
    
    input("Type any key to return to app menu\n")
    new_screen(current_username, login_as)
    use_app()

def account_setting():
    in_setting = True
    while in_setting:
        new_screen(current_username, login_as)
        
        check_option = True
        while check_option:
            account_info = {}
        
            if login_as == "user":
                with open(user_info, "r") as f:
                    info_reader = csv.DictReader(f)
                    
                    for info in info_reader:
                        if info['Username'] == current_username:
                            account_info = info
                            break
            else:
                with open(admin_info, "r") as f:
                    info_reader = csv.DictReader(f)
                    
                    for info in info_reader:
                        if info['Username'] == current_username:
                            account_info = info
                            break
            
            print(f"{login_as.capitalize()} Info:- ")
            print(f"First Name: {account_info['First Name']}")
            print(f"Last Name: {account_info['Last Name']}")
            print(f"Username: {account_info['Username']}")
            if login_as == "admin":
                print(f"Secure PIN: {account_info['Secure PIN']}")

            option = input(account_setting_options)
            if option.isdigit():
                option = int(option)
                if option <= 0 or option > 2:
                    new_screen(current_username, login_as)
                    print("Invalid option. You can only choose one of the following options.")
                else:
                    check_option = False
            elif option == "":
                new_screen(current_username, login_as)
                use_app()
                check_option = False
                in_setting = False
            else:
                new_screen(current_username, login_as)
                print("Invalid option. Please type a number")
        
        if option == 1:
            change_info(account_info)                    
        elif option == 2:
            terminate_account()

def change_info(account_info):
    global current_username
    global current_password
    global current_pin
    
    new_screen(current_username, login_as)
    changing_info = True
    while changing_info:
        if login_as == "user":
            print(user_info_options)
            available_options = 3
        else:
            print(admin_info_options)
            available_options = 4
        
        change_option = input("-> ")
        if change_option.isdigit():
            change_option = int(change_option)
            if change_option <= 0 or change_option > available_options:
                new_screen(current_username, login_as)
                print("Invalid option. You can only choose one of the following options.")
            else:
                new_screen(current_username, login_as)
                if change_option == 1:
                    current_name = account_info['First Name'] + ' ' + account_info['Last Name']
                    print(f"Current Name is {current_name}")
                    print("Enter new name. (Press Enter to cancel)")
                    
                    new_first_name = input("New First Name: ")
                    if new_first_name != "":
                        new_last_name = input("New Last Name: ")
                        if new_last_name != "":
                            account_info['First Name'] = new_first_name
                            account_info['Last Name'] = new_last_name
                            
                            replace_account(account_info)
                            print("Successfully changed name.")
                        else:
                            print("Cancelled")
                    else:
                        print("Cancelled")
                            
                elif change_option == 2:
                    print(f"Current Username is {current_username}")
                    
                    ask_new_username = True
                    username_updated = False
                    print("Enter new username. (Press Enter to cancel)")
                    while ask_new_username:
                        new_username = input("New username: ")
                        if new_username == "":
                            print("Cancelled")
                            ask_new_username = False
                        else:
                            user_accounts = extract_info(user_info)
                            for account in user_accounts:
                                if new_username == account['Username']:
                                    print("Username already existed. Please try again.")
                                    ask_new_username = True
                                    username_updated = False
                                    break
                                else:
                                    ask_new_username = False
                                    username_updated = True
                    
                            if username_updated == True:
                                account_info['Username'] = new_username
                                replace_account(account_info)
                                print("Successfully changed username.")
                                
                                history_info = []
                                
                                with open(book_history, "r") as f1:
                                    info_reader = csv.DictReader(f1)
                                    
                                    for info in info_reader:
                                        history_info.append(info)
                                
                                for history in history_info:
                                    if history['Username'] == current_username:
                                        history['Username'] = new_username
                                
                                field = ["Username", "Booked Room","Location", "Nights", "Total Price"]
                                with open(book_history, "w", newline="") as f2:
                                    info_writter = csv.DictWriter(f2, fieldnames=field)
                                    info_writter.writeheader()
                                    info_writter.writerows(history_info)
                                
                                current_username = new_username

                elif change_option == 3:
                    print("Changing Password... ")
                    ask_new_password = True
                    while ask_new_password:
                        old_password = input("Enter Old Password: ")
                        if old_password == "":
                            print("Cancelled")
                            ask_new_password = False
                        elif old_password != current_password:
                            print("Password not same. Please try again.")
                        else:
                            new_password = input("Enter New Password: ")
                            if new_password == "":
                                print("Cancelled")
                                ask_new_password = False
                            else:
                                confirm_new_password = input("Confirm Password: ")
                                if confirm_new_password == "":
                                    print("Cancelled")
                                    ask_new_password = False
                                elif new_password == confirm_new_password:
                                    if len(new_password) < 6:
                                        print("Password too short. Please try again.")
                                    else:
                                        account_info['Password'] = new_password
                                        replace_account(account_info)
                                        print("Successfully changed password.")
                                        ask_new_password = False
                                        current_password = new_password
                                else:
                                    print("The password confirmation does not match. Please try again.")
                else:
                    print("Changing Secure PIN... ")
                    ask_new_pin = True
                    while ask_new_pin:
                        old_pin = input("Enter Old PIN: ")
                        if old_pin == "":
                            print("Cancelled")
                            ask_new_pin = False
                        elif old_pin != current_pin:
                            print("Secure PIN not same. Please try again.")
                        else:
                            new_pin = input("Enter New PIN (6-digits): ")
                            if new_pin == "":
                                print("Cancelled")
                                ask_new_pin = False
                            elif len(new_pin) != 6:
                                print("Secure PIN must be 6-digits. Please try again.")
                            else:
                                confirm_new_pin = input("Confirm PIN: ")
                                if confirm_new_pin == "":
                                    print("Cancelled")
                                    ask_new_pin = False
                                elif new_pin == confirm_new_pin:
                                    account_info['Secure PIN'] = new_pin
                                    replace_account(account_info)
                                    print("Successfully changed Secure PIN.")
                                    ask_new_pin = False
                                    current_pin = new_pin
                                else:
                                    print("The Secure PIN confirmation does not match. Please try again.")

                continue_changing = input("Do you want to continue changing account info? (Type 'y' if yes or any input if no)\n-> ").lower()
                if continue_changing == 'y':
                    new_screen(current_username, login_as)
                else:
                    break
        elif change_option == "":
            changing_info = False
        else:
            new_screen(current_username, login_as)
            print("Invalid option. Please type a number")

def replace_account(account_info):
    user_accounts = extract_info(user_info)
    admin_accounts = extract_info(admin_info)
    replacing_account = account_info
    remaining_user_accounts = []
    remaining_admin_accounts = []
    user_field = ['First Name', 'Last Name', 'Username', 'Password']
    admin_field = ['First Name', 'Last Name', 'Username', 'Password', 'Secure PIN']
    
    for user_account in user_accounts:
        if user_account['Username'] != current_username:
            remaining_user_accounts.append(user_account)

    for admin_account in admin_accounts:
        if admin_account['Username'] != current_username:
            remaining_admin_accounts.append(admin_account)
    
    if login_as == "user":
        remaining_user_accounts.append(replacing_account)
        
        with open(user_info, "w", newline="") as f1:
            info_writter = csv.DictWriter(f1, fieldnames=user_field)
            info_writter.writeheader()
            info_writter.writerows(remaining_user_accounts)

        for admin_account in admin_accounts:
            if admin_account['Username'] == current_username:
                replacing_account['Secure PIN'] = admin_account['Secure PIN']
                remaining_admin_accounts.append(replacing_account)
                
                with open(admin_info, "w", newline="") as f2:
                    info_writter = csv.DictWriter(f2, fieldnames=admin_field)
                    info_writter.writeheader()
                    info_writter.writerows(remaining_admin_accounts)
        
    elif login_as == "admin":
        remaining_admin_accounts.append(replacing_account)
        
        with open(admin_info, "w", newline="") as f2:
            info_writter = csv.DictWriter(f2, fieldnames=admin_field)
            info_writter.writeheader()
            info_writter.writerows(remaining_admin_accounts)

        for user_account in user_accounts:
            if user_account['Username'] == current_username:
                del replacing_account['Secure PIN']
                remaining_user_accounts.append(replacing_account)
                
                with open(user_info, "w", newline="") as f1:
                    info_writter = csv.DictWriter(f1, fieldnames=user_field)
                    info_writter.writeheader()
                    info_writter.writerows(remaining_user_accounts)

def terminate_account():
    user_accounts = extract_info(user_info)
    admin_accounts = extract_info(admin_info)
    
    print("By terminating your account, your user account and your admin account will both be deleted")
    confirm_termiante = input("Are you sure you want to proceed? (Type 'y' to proceed or any input to cancel)\n-> ").lower()
    
    if confirm_termiante == 'y':
        terminate_password = input("Enter your password to confirm (Press Enter to cancel): ")
        remaining_users = []
        remaining_admins = []
        
        if terminate_password == current_password:
            for user_account in user_accounts:
                if user_account['Username'] != current_username:
                    remaining_users.append(user_account)

            field = ['First Name', 'Last Name', 'Username', 'Password']
            with open(user_info, "w", newline="") as f1:
                info_writter = csv.DictWriter(f1, fieldnames=field)
                info_writter.writeheader()
                info_writter.writerows(remaining_users)
                        
            for admin_account in admin_accounts:
                if admin_account['Username'] != current_username:
                    remaining_admins.append(admin_account)
                    
                field = ['First Name', 'Last Name', 'Username', 'Password', 'Secure PIN']
                with open(admin_info, "w", newline="") as f1:
                    info_writter = csv.DictWriter(f1, fieldnames=field)
                    info_writter.writeheader()
                    info_writter.writerows(remaining_admins)

            print("Your account has been terminated.")

        print("Going back to login menu in 3s.")
        time.sleep(3)
        new_screen()
        main()

def quit_app():
    new_screen()
    print("See you next time, " + current_username + " :)")
    quit()

def remove_user():
    global remove_index
    
    removing_user = True
    while removing_user: 
        new_screen(current_username, login_as)
        user_accounts = extract_info(user_info)
        admin_accounts = extract_info(admin_info)
        
        user = 0
        print("Available users:-")
        for user_account in user_accounts:
            user += 1
            print(f"{user}: {user_account['Username']}")
        
        ask_remove = True
        while ask_remove:
            print("Select a number to remove user from database. (Press Enter to return to app menu)")
            remove_option = input("-> ")
            
            if remove_option == "":
                new_screen(current_username, login_as)
                use_app()
                ask_remove = False
                removing_user = False
            elif not remove_option.isdigit():
                print("Please enter a number.")
            elif int(remove_option) <= 0 or int(remove_option) > user:
                print("Invalid option. Please try again.")
            else:
                remove_index = int(remove_option) - 1
                if user_accounts[remove_index]['Username'] == current_username:
                    print("You cannot remove yourself. Please try again.")
                else:
                    for admin_account in admin_accounts:
                        if user_accounts[remove_index]['Username'] == admin_account['Username']:
                            print("Removing this user will also remove his/her admin account.")
                            proceed = input("Do you want to proceed? (Type 'y' to proceed or any input to cancel)\n-> ").lower()
                            if proceed == 'y':
                                admin_accounts.remove(admin_account)
                                field = ['First Name', 'Last Name', 'Username', 'Password', 'Secure PIN']
                                with open(admin_info, "w", newline="") as f:
                                    info_writter = csv.DictWriter(f, fieldnames=field)
                                    info_writter.writeheader()
                                    info_writter.writerows(admin_accounts)
                                ask_remove = False
                            else:
                                new_screen(current_username, login_as)
                                user = 0
                                for user_account in user_accounts:
                                    user += 1
                                    print(f"{user}: {user_account['Username']}")

                                ask_remove = True
                            break
                        else:
                            ask_remove = False
        
        user_removed = user_accounts.pop(remove_index)
        field = ['First Name', 'Last Name', 'Username', 'Password']
        with open(user_info, "w", newline="") as f:
            info_writter = csv.DictWriter(f, fieldnames=field)
            info_writter.writeheader()
            info_writter.writerows(user_accounts)
            
        new_screen(current_username, login_as)
        print(f"Successfully removed user: {user_removed['Username']}\n")
        
        continue_remove = input("Do you want to continue to remove user? (Type 'y' if yes or any input if no)\n-> ").lower()
        if continue_remove != 'y':
            new_screen(current_username, login_as)
            use_app()
            removing_user = False

def add_admin():
    global add_index
    
    adding_admin = True
    while adding_admin:
        new_screen(current_username, login_as)
        user_accounts = extract_info(user_info)
        admin_accounts = extract_info(admin_info)
        
        user = 0
        print("Available users:-")
        for account in user_accounts:
            user += 1
            print(f"{user}: {account['Username']}")
        
        ask_add = True
        print("Select a number to add user as admin. (Press Enter to return to app menu)")
        while ask_add:
            selected_user = input("-> ")
            
            if selected_user == "":
                new_screen(current_username, login_as)
                use_app()
                ask_add = False
            elif not selected_user.isdigit():
                print("Please enter a number.")
            elif int(selected_user) <= 0 or int(selected_user) > user:
                print("Invalid option. Please try again.")
            else:
                add_index = int(selected_user) - 1
                for account in admin_accounts:
                    if user_accounts[add_index]['Username'] == account['Username']:
                        print(f"User {user_accounts[add_index]['Username']} is already an admin. Please try again.")
                        ask_add = True
                        break
                    else:
                        ask_add = False

        new_admin_info = user_accounts[add_index]
        ask_pin = True
        print("Create a Secure PIN with 6 digits")
        while ask_pin:
            create_pin = input("-> ")
            
            if create_pin.isdigit and len(create_pin) != 6:
                print("Please enter a 6 digit number")
            else:
                new_admin_info['Secure PIN'] = create_pin
                ask_pin = False
        
        import_info(admin_info, new_admin_info, "admin")
        print(f"Adding user {new_admin_info['Username']} as admin...")
        
        print(f"{new_admin_info['Username']} is now an admin.")
        continue_add_admin = input("Do you want to continue adding admin? (Type 'y' if yes or any input if no)\n-> ").lower()
        if continue_add_admin != 'y':
            new_screen(current_username, login_as)
            use_app()
            adding_admin = False

def remove_admin():
    global remove_index
    while True: 
        new_screen(current_username, login_as)
        admin_accounts = extract_info(admin_info)
        
        admin = 0
        print("Available admins:-")
        for account in admin_accounts:
            admin += 1
            print(f"{admin}: {account['Username']}")
        
        ask_remove = True
        while ask_remove:
            print("Select a number to remove admin from database. (Press Enter to return to app menu)")
            remove_option = input("-> ")
            
            if remove_option == "":
                new_screen(current_username, login_as)
                use_app()
                ask_remove = False
            elif not remove_option.isdigit():
                print("Please enter a number.")
            elif int(remove_option) <= 0 or int(remove_option) > admin:
                print("Invalid option. Please try again.")
            else:
                remove_index = int(remove_option) - 1
                if admin_accounts[remove_index]['Username'] == current_username:
                    print("You cannot remove yourself. Please try again.")
                else:
                    ask_remove = False
        
        admin_removed = admin_accounts.pop(remove_index)
        field = ['First Name', 'Last Name', 'Username', 'Password', 'Secure PIN']
        with open(admin_info, "w", newline="") as f:
            info_writter = csv.DictWriter(f, fieldnames=field)
            info_writter.writeheader()
            info_writter.writerows(admin_accounts)
        print(f"Successfully removed admin: {admin_removed['Username']}")
        
        continue_remove = input("Do you want to continue to remove admin? (Type 'y' if yes or any input if no)\n-> ").lower()
        if continue_remove != 'y':
            new_screen(current_username, login_as)
            use_app()
            break

def add_rooms():
    room_field = ["No.", "Room Name", "Location", "Price per night"]
    ask_new_room = True
    while ask_new_room:
        new_screen(current_username, login_as)
        
        with open(rooms_info, "r+", newline="") as f:
            available_room_name = []
            info_reader = csv.DictReader(f)
            for room in info_reader:
                available_room_name.append(room['Room Name'])
        
            print("Enter details for the new room (Press Enter to return to menu page):")
            new_room_name = input("New Room Name: ")
            if new_room_name == "":
                new_screen(current_username, login_as)
                use_app()
                ask_new_room = False
            elif new_room_name in available_room_name:
                print("Room already existed. Please try again.")
            else:
                new_room_location = input("Room Location: ")
                if new_room_location == "":
                    new_screen(current_username, login_as)
                    use_app()
                    ask_new_room = False
                new_room_price = input("Price per night: RM")
                if new_room_price == "":
                    new_screen(current_username, login_as)
                    use_app()
                    ask_new_room = False
            
            new_room_number = len(available_room_name) + 1
            new_room_info = {'No.':  new_room_number, 'Room Name': new_room_name, 'Location': new_room_location, 'Price per night': new_room_price}
            
            info_writter = csv.DictWriter(f, fieldnames=room_field)
            info_writter.writerow(new_room_info)
        
        print(f"Successfully added room '{new_room_name}'.")
        continue_add_room = input("Do you want to continue adding new rooms? (Type 'y' if yes or any input if no)\n-> ").lower()
        if continue_add_room != 'y':
            print("Going back to app menu in 3s.")
            time.sleep(3)
            new_screen(current_username, login_as)
            use_app()
            ask_new_room = False

def remove_rooms():
    removing_room = True
    while removing_room:
        new_screen(current_username, login_as)
        
        available_rooms = []
        print("Available Rooms: ")
        with open(rooms_info, "r") as f:
            info_reader = csv.DictReader(f)
            
            for existing_room in info_reader:
                print("Room No.", existing_room['No.'])
                print("- Room Name:", existing_room['Room Name'])
                print("- Location:", existing_room['Location'])
                print("- Price per night: RM", existing_room['Price per night'], '\n')
                available_rooms.append(existing_room)
        
        ask_remove_option = True
        print("Enter the room number to remove the room. (Press Enter to cancel): ")
        while ask_remove_option:        
            remove_option = input("-> ")
            if remove_option == "":
                use_app()
                ask_remove_option = False
                removing_room = False
            elif not remove_option.isdigit():
                print("Please enter a number")
            elif int(remove_option) <= 0 or int(remove_option) > len(available_rooms):
                print("Please choose one of the room number to remove.")
            else:
                remove_room_index = int(remove_option) - 1
                available_rooms.pop(remove_room_index)
                
                room_number = 0
                for room in available_rooms:
                    room_number += 1
                    room['No.'] = room_number
                    
                ask_remove_option = False
        
        room_field = ["No.", "Room Name", "Location", "Price per night"]
        with open(rooms_info, "w", newline="") as f:
            info_writter = csv.DictWriter(f, fieldnames=room_field)
            info_writter.writeheader()
            info_writter.writerows(available_rooms)
        
        print("Successfully removed room. ")
        continue_removing = input("Do you want to continue removing room? (Type 'y' if yes or any input if no)\n-> ").lower()
        if continue_removing != 'y':
            removing_room = False

def main():
    global current_username
    global current_password
    global current_pin
    global login_as

    while True:
        new_screen()
        print(welcome_message)
        print(login_message)

        # Ask user to login or register first in order to use the application
        login_option = ask_login()
        if login_option == 1:
            new_screen()
            user_credentials = user_login()
            if user_credentials != None:
                login_as = "user"
                current_username = user_credentials[0]
                current_password = user_credentials[1]
            
            new_screen()
            print(f"Successfully logged in as {login_as}: {current_username}\n")
            
            use_app()

        elif login_option == 2:
            new_screen()
            admin_credentials = admin_login()
            if admin_credentials != None:
                login_as = "admin"
                current_username = admin_credentials[0]
                current_password = admin_credentials[1]
                current_pin = admin_credentials[2]
            
            new_screen()
            print(f"Successfully logged in as {login_as}: {current_username}\n")
            
            use_app()

        else:
            register()
            current_username = None
            login_as = None

main()
