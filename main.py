import mysql.connector
from customer import add_customer,update_customer
from computer import add_computer,update_computer
from delete_existing import delete_data
from display_single_data import display_data
from display_table import display_table
from bill import bill

if _name_=='_main_':
#Main program
    while True:
        print('**********CYBERCAFE MANAGEMENT SYSTEM**********')
        print('1: To display all the records of a table.\n'
              '2: To Display a single data.\n'
              '3: To Add Customer details.\n'
              '4: To Add Computer details.\n'
              '5: To Update Customer details.\n'
              '6: To Update Computer details.\n'
              '7: To Delete a record.\n'
              '8: For Billing.\n'
              '9: To Quit.')
        try:
            choice=int(input('Enter your choice:'))
            if choice==1:
                display_table()
            elif choice==2:
                display_data()
            elif choice==3:
                add_customer()
            elif choice==4:
                add_computer()
            elif choice==5:
                update_customer()
            elif choice==6:
                update_computer()
            elif choice==7:
                delete_data()
            elif choice==8:
                bill()
            elif choice==9:
                print('Existing')
                break
            else:
                print('Wrong Choice!')
        except ValueError:
            print('Invalid Input. Please Enter a number')

        ch=input('\nDo u want to continue?').lower()
        if ch=='no':
            print('Existing')
            break

