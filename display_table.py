#To display a table
def display_table():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='cybercafe')
    mycursor=mydb.cursor()
    print('\n1.Customer details\n'
          '2.Computer details')
    table=int(input('\nEnter the table to be displayed:'))
    if table==1:
        mycursor.execute('select*from customer_details')
        for i in mycursor:
            print(i)
    elif table==2:
         mycursor.execute('select*from computer_details')
         for i in mycursor:
            print(i)
    else:
        print('Wrong choice!')
    mycursor.close()
    mydb.close()