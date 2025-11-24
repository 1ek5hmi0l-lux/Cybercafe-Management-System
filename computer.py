#To add Computer Details
def add_computer():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='cybercafe')
    mycursor=mydb.cursor()
    r=int(input('\nEnter the number of records to be added:'))
    for i in range(0,r):
        comp_ID=int(input('Enter the Computer ID:'))
        comp_name=input('Enter the Computer Name:')
        IP=input('Enter the IP Address:')
        query='insert into computer_details values(%s,%s,%s)'
        data=(comp_ID,comp_name,IP)
        mycursor.execute(query,data)
        print('These records are successfully added')
        mydb.commit()
        mycursor.close()
        mydb.close()


#To Update computer details
def update_computer():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='cybercafe')
    mycursor=mydb.cursor()
    print('\n1: To update Computer Name')
    print('2: To update IP address')
    choice=int(input('Enter your choice:'))
    if choice==1:
        comp_ID=int(input('\nEnter the computer ID:'))
        comp_name=input('Enter the new computer name:')
        query='update computer_details set computer_name=%s where computer_ID=%s'
        data=(comp_name,comp_ID)
        mycursor.execute(query,data)
        mydb.commit()
        mycursor.close()
        mydb.close() 
        print('Record is Updated.')
    elif choice==2:
        comp_ID=int(input('\nEnter the computer ID:'))
        IP=input('Enter the new IP address:')
        query='update computer_details set IP_address=%s where computer_ID=%s'
        data=(IP,comp_ID)
        mycursor.execute(query,data)
        mydb.commit()
        mycursor.close()
        mydb.close()
        print('Record is Updated')
    else:
        print('Wrong Choice!')