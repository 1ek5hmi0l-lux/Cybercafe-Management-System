#To add customer details
def add_customer():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='cybercafe')
    mycursor=mydb.cursor()
    r=int(input('\nNumber of records to be added:'))
    for i in range(0,r):
        usernm=input('Enter the Username:')
        compid=int(input('Enter the Computer ID:'))
        idproof=input('Enter the ID Proof:')
        idno=int(input('Enter the ID Number:'))
        mobileno=int(input('Enter the Mobile Number:'))
        emailid=input('Enter the Email ID:')
        sql_query='insert into customer_details values(%s,%s,%s,%s,%s,%s)'
        data=(usernm,compid,idproof,idno,mobileno,emailid)
        mycursor.execute(sql_query,data)
        print('This record is succesfully added')
        mydb.commit()
        mycursor.close()
        mydb.close()

#To update customer details
def update_customer():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='cybercafe')
    mycursor=mydb.cursor()
    print('\n1:To update Username')
    print('2:To update Computer ID')
    print('3:To update ID Proof')
    print('4:To update ID Number')
    print('5:To update Mobile Number')
    print('6:To update Email ID\n')
    choice=int(input('Enter your choice:'))
    if choice==1:
        compid=int(input('Enter the Computer ID:'))
        usernm=input('Enter the new Username:')
        data=(usernm,compid)
        mycursor=mydb.cursor()
        query='UPDATE customer_details set username=%s where computer_id=%s'
        mycursor.execute(query,data)
        print('Updated Succesfully')
        mydb.commit()
        mycursor.close()
        mydb.close()
    elif choice==2:
        usernm=input('Enter the Username:')
        compid=input('Enter the new Computer ID:')
        data=(compid,usernm)
        mycursor=mydb.cursor()
        query='UPDATE customer_details set computer_id =%s where username=%s'
        mycursor.execute(query,data)
        print('Updated Succesfully')
        mydb.commit()
        mycursor.close()
        mydb.close()
    elif choice==3:
        usernm=input('Enter the Username:')
        idproof=input('Enter the new ID Proof:')
        data=(idproof,usernm)
        mycursor=mydb.cursor()
        query='UPDATE customer_details set id_proof="%s" where username=%s'
        mycursor.execute(query,data)
        print('Updated Succesfully')
        mydb.commit()
        mycursor.close()
        mydb.close()
    elif choice==4:
        usernm=input('Enter the Username:')
        idno=int(input('Enter the new ID Number:'))
        data=(idno,usernm)
        mycursor=mydb.cursor()
        query='UPDATE customer_details set id_number=%s where username=%s'
        mycursor.execute(query,data)
        print('Updated Succesfully')
        mydb.commit()
        mycursor.close()
        mydb.close()
    elif choice==5:
        usernm=input('Enter the Username:')
        mobileno=int(input('Enter the new Mobile Number:'))
        data=(mobileno,usernm)
        mycursor=mydb.cursor()
        query='UPDATE customer_details set mobile_number=%s where username=%s'
        mycursor.execute(query,data)
        print('Updated Succesfully')
        mydb.commit()
        mycursor.close()
        mydb.close()
        
    elif choice==6:
        usernm=input('Enter the Username:')
        emailid=input('Enter the new Email ID:')
        data=(emailid,usernm)
        mycursor=mydb.cursor()
        query='UPDATE customer_details set email_id=%s where username=%s'
        mycursor.execute(query,data)
        print('Updated Succesfully')
        mydb.commit()
        mycursor.close()
        mydb.close()
    else:
        print('Wrong Choice!')