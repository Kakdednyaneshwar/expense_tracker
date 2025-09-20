import mysql.connector
from datetime import datetime
def conn():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='MRkakde@1211',
        database="expense_tracker"
    )
def add_expense():
    Category = input("Enter category of expense like grocery, medicines,bills,etc...")
    Descrition = input("Enter description [OPTIONAL]")
    Amount = float(input("Enter amount spent"))
    date_str  = input("If not todays date, enter date in format yyyy-mm-dd")
    Date = date_str if date_str else datetime.today().strftime('%Y-%m-%d')
    #strftime - function of datetime module which cinvert date to string format
    #%Y-%m-%d = yyyy-mm-dd
    #shorthand if - if date_str is empty will return false
    con = conn()
    cursor = con.cursor()
    cursor.execute('insert into expense(Date,Amount,catagory,Description) values(%s,%s,%s,%s)',(Date,Amount,Category,Descrition))
    con.commit()
    print("Added Successfully")
    cursor.close()
    con.close()

def view_all():
    con = conn()
    cursor = con.cursor()
    cursor.execute("select*from expense")
    records = cursor.fetchall()
    print("  ID    |Date        |Amount Spent        |Category         ")
    for row in records:
        print(f'  {row[0]}     |{row[1]}        |{row[2]}        |{row[3]}')
        
    cursor.close()
    con.close()

def summery():
    month = input("Enter month number like 1 fro january....")
    year = int(input("Enter year in format YYYY"))
    con = conn()
    cursor = con.cursor()
    sql = '''select sum(Amount), catagory from expense where year(Date) = %s and month(Date) = %s group by catagory'''
    cursor.execute(sql,(year,month))
    record = cursor.fetchall()
    print("  Total Amount     |Category         ")
    for row in record:
        print(f'{row[0]}        |{row[1]}')
        
    cursor.close()
    con.close()
def delete():
    rownum = int(input("Enter ID number of record to be deleted :"))
    con = conn()
    cursor = con.cursor()
    cursor.execute("delete from expense where ID = %s",(rownum,))
    con.commit()
    print("Deleted Successfully....")
    cursor.close()
    con.close()

def main():
    while True:
        print("\n----select one of the given---")
        print("1. Add An Expense")
        print("2. Delete/Remove An Expense")
        print("3. View all Expense")
        print("4. Get Monthly Summery")
        print("5. Exit")
        print("\n")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            delete()
        elif choice == '3':
            view_all()
        elif choice == '4':
            summery()
        elif choice == '5':
            print("Thank you for using")
            break
        else:
            print("Not a correct choice!! Please re-enter")
            
if __name__ == "__main__":
    main()
