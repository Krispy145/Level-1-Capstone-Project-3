#Login details:
from datetime import date
result = 0
user_result = 0
pass_result = 0
months = ['Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec']
usernames = []
passwords = []

#read all possible user details:
with open ( 'user.txt' , 'r+' ) as f:
    for line in f:
        str_list = line.split(',')
        usernames.append(str_list[0])
        passwords.append(str_list[1].strip())

    #check for valid user until user enters valid credentials:
    while result >=0:

        print('')
        username = input("Please enter your username here: ").strip()


        #checks for username in database:
        while user_result >=0:
            if username in usernames:
                int_ref = usernames.index(username)
                user_result = -1
            else:
                print('\n Invalid username, please try again.\n')
                username = input("Please enter your username here: ").strip()

        print('')
        
        password = input("Please enter your password here: ").strip()

        #checks for password equal to username:
        while pass_result >=0:
            if not password == passwords[int_ref]:
                print(f"\n Invalid password for username '{username}'.\n")
                password = input("Please enter your password here: ").strip()
       
            else:
                print(f"\n Welcome back '{username}'")
                result = -1
                pass_result = -1
                          
    print('')

    #options list:
    option = ''
    while not option == 'e': 
        print("Please type in one of the following options: \n\n")
        if username == 'admin':
            print('s  - \tstatistics')
            print('r  - \tregister user')
        print('a  - \tadd task')
        print('va - \tview all tasks')
        print('vm - \tview my tasks')
        print('e  - \texit\n')
        
        option = input("Please type option here: ").strip().lower()

        print('')


        #register option:
        if option == 'r':
            with open ( 'user.txt' , 'a' ) as f:
                print('Register user:\n')
                new_username = input("Please enter new username here to register: ").strip().lower()
                new_password = input("Please enter password for new user here: ").strip()
                confirm_password = input("Please confirm password here: ").strip()

                print('')
                #check for valid password:
                while not new_password == confirm_password:
                    print('')
                    print('Passwords do not match please try again.\n')
                    new_password = input("Please enter password for new user here: ").strip()
                    confirm_password = input("Please confirm password here: ").strip()
                    
                f.write(f"\n{new_username}, {new_password}")
                print('\n ...')
                print('New User Added! \n')


        #add task option:
        if option == 'a':
            with open ( 'tasks.txt' , 'a' ) as f:
                print('Add task to User:\n')
                task_user = input("Assigned username: ").strip()
                title = input("Task Title: ").strip()
                description = input("Task description: ").strip()
                print("Enter the due date as follows:")
                day = int(input("Day (dd): ").strip())
                month = int(input("Month (mm): ").strip())
                year = int(input("Year (yyyy): ").strip())
                due_date = f"{day} {months[month-1]} {year}"
                today = date.today()
                task_date = f"{today.day} {months[today.month-1]} {today.year}"
                completed = 'No'
                f.write(f"{task_user}, {title}, {description}, {task_date}, {due_date}, {completed}\n")
                print('\n ...')
                print('Task Added! \n')


        #view all tasks:
        if option == 'va':
            with open ('tasks.txt','r') as f:
                print('All tasks are lisetd below:\n')
                for line in f:
                    parts = line.split(',')
                    print(f'Task Name: \t\t{parts[0]}')
                    print(f'Assigned To: \t\t{parts[1].strip()}')
                    print(f'Description: \t\t{parts[2].strip()}')
                    print(f'Date Assigned: \t\t{parts[3].strip()}')
                    print(f'Due Date: \t\t{parts[4].strip()}')
                    print(f'Task Complete? \t\t{parts[5].strip()}\n')
                print('End of List...\n')


        #View users' tasks:
        if option == 'vm':
            with open ('tasks.txt','r') as f:
                print('All tasks are lisetd below:\n')
                for line in f:
                    parts = line.split(',')
                    if parts[0].strip().lower() == username.lower(): 
                        print(f'Task Name: \t\t{parts[0]}')
                        print(f'Assigned To: \t\t{parts[1].strip()}')
                        print(f'Description: \t\t{parts[2].strip()}')
                        print(f'Date Assigned: \t\t{parts[3].strip()}')
                        print(f'Due Date: \t\t{parts[4].strip()}')
                        print(f'Task Complete? \t\t{parts[5].strip()}\n')
                print('End of List...\n')
        

        #statistics option:
        if option == 's' and username == 'admin':
            task_count = 0
            with open ('tasks.txt','r') as f:
                print('Statistics:\n')
                for line in f:
                    task_count += 1
                print(f'Total number of Tasks: {task_count}\n')

            user_count = 0    
            with open ('user.txt','r') as f:
                for line in f:
                    user_count += 1
                print(f'Total users: {user_count}\n')
                    


                    
            



            


