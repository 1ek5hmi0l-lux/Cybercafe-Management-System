#To display single data
def display_data():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='cybercafe')
    mycursor=mydb.cursor()
    print('\n1.Customer details\n'
          '2.Computer details')
    table=int(input('Enter the table to be selected:'))
    if table==1:
        usernm=input('\nEnter Username of the respective Customer whose details to be displayed:')
        query='select * from customer_details where username="%s"'%usernm
        mycursor.execute(query)
        myrecord=mycursor.fetchall()
        flag=0
        for i in myrecord:
            if i[0]==usernm:
                flag=1
                break
        if flag==1:
            print('Displaying the records in the order:')
            for i in myrecord:
                print(i,end='')
        else:
            print('Details of the inputted Username is not found!')
        mycursor.close()
        mydb.close()

    elif table==2:
        compid=int(input('\nEnter Computer ID of the respective Computer which details to be displayed:'))
        query='select * from computer_details where computer_id=%s'%compid
        mycursor.execute(query)
        myrecord=mycursor.fetchall()
        print(myrecord)
        flag=0
        for i in myrecord:
            if i[0]==compid:
                flag=1
                break
        if flag==1:
            print('Displaying the records in the order(Computer ID,Computer Name,IP Address):')
            for i in myrecord:
                print(i,end='')
        else:
            print('Details of the inputted Computer ID is not found!')
        mycursor.close()
        mydb.close()