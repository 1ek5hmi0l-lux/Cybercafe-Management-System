#To delete a record from a table
def delete_data():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='cybercafe')
    mycursor=mydb.cursor()
    print('\nChoose the Table')
    print('1.Customer details')
    print('2.Computer details')
    ch=int(input('Enter the your choice:'))
    if ch==1:
        usernm=input('\nEnter the Username to deleted:')
        query='delete from customer_details where username="%s"'%usernm
        mycursor.execute(query)
        print('Record is successfully deleted.')
        mydb.commit()
        mydb.close()
    elif ch==2:
        compid=int(input('\nEnter the Compter ID to deleted:'))
        query='delete from computer_details where computer_id=%s'%(compid,)
        mycursor.execute(query)
        print('Record is successfully deleted.')
        mydb.commit()
        mydb.close()
    else:
        print('Wrong Choice!')



#Billing
def bill():
    print('Please enter the time in 24-hr')
    start=input('Start time:')
    end=input('End time:')
    from datetime import datetime
    t1=datetime.strptime(start,'%H:%M:%S')
    t2=datetime.strptime(end,'%H:%M:%S')
    delta=t2-t1
    time=delta.total_seconds()/60
    price=1*time
    print('price:₹',price,'for duration:',time,'minutes')

