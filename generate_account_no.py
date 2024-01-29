## PROGRAM TO RETRIEVE BANK ACCOUNT ##
## add try except block
## Add users and create accounts for them

import os
import sys
import random


def generate_account_no(number_of_digits):
    ''' function to generate bank account number.
        Pass in number of digits when calling function
    '''
    size = 0
    account_no = '1'
    while size < number_of_digits-1:
        add_number = random.randint(0,9)
        account_no = account_no + str(add_number)
        size += 1
    return account_no


def create_password():
    ''' function to create password. Needed to retrieve bank account number '''
    password = input('Please enter a password: ')
    while len(password) < 5 or len(password) > 10:
        if password == 'q':
            print('closing program....')
            sys.exit()
        else:
            print('Invalid! Password must be between 5 and 10 characters.')
            password = input('Please enter a valid password (q to exit): ')

    print('Password successfully created!')
    return password



def main_program():
    ''' main function to retrieve bank account number'''
    input('Hit any key to start retrieving bank account number..\n')

    password = input('Enter your password: \n')
    attempts = 1
    while not password == my_password:
        if attempts < 4:
            if password != 'q':
                password = input(f'Incorrect! Attempt {attempts}/3. Please re-enter password ([q] to exit): \n')
                attempts += 1
            else:
                print('closing program....')
                sys.exit()
        else:
            print('Attempt exceeded! Closing program!!')
            sys.exit()

    print('\nLogin Success! \n')
    print('Your new account number is: \n' + my_bank_account_no + '\n')



def append_bank_info_to_members_list(list_of_members):
    ''' function to add generated account# to a list dictionary'''
  
    for members in list_of_members:
        print('Processing employee ' + members['first_name'], members['last_name'])
        # members['password'] = create_password()
        members['account_no'] = generate_account_no(8)
    return list_of_members


# sample data for testing
employees = [
    {'first_name': 'Abu', 'last_name': 'Zango', 'title': 'Developer', 'location': 'Texas'},
    {'first_name': 'Jide', 'last_name': 'Kosoko', 'title': 'Cloud Engineer', 'location': 'Wyoming'},
    {'first_name': 'Bisi', 'last_name': 'Awoletu', 'title': 'Auditor', 'location': 'Maryland'},
    {'first_name': 'April', 'last_name': 'Mattiew', 'title': 'Developer', 'location': 'Maryland'},
    {'first_name': 'Patrick', 'last_name': 'Ellis', 'title': 'Manager', 'location': 'Florida'},
]

# function calls
my_password = create_password()
my_bank_account_no = generate_account_no(9)
main_program()


