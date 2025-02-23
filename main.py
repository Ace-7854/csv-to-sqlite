from sqlite_mod import *
from csv_mod import *
import os,time

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def menu():
    print("1.Add new record to CSV")
    print("2.Read CSV and print")
    print("3.Convert CSV to SQL Table")

def get_choice():
    print("Please enter your choice")
    return int_check(input())

def int_check(usr_inp) -> int:
    try:
        int_user = int(usr_inp)
        return int_user
    except:
        print("Invalid input")
        return -1

def add_rec():
    print("Enter Name:")
    name = input()
    print("Enter Salary")
    salary = input()
    add_rec_csv(name,salary)
    print("Complete")
    time.sleep(5)

def sql_formatting(records):
    conv_to_int = lambda x: int(x)
    new_rec_set = []
    for rec in records:
        new_rec_set.append(rec.split(','))
    
    for i in range(len(new_rec_set)):
        new_rec_set[i][1] = new_rec_set[i][1].replace("\n", "")
        new_rec_set[i][1] = new_rec_set[i][1][0:len(new_rec_set[i][1])-2]
        new_rec_set[i][1] = conv_to_int(new_rec_set[i][1])
    return new_rec_set

def csv_to_sql():
    records = sql_formatting(get_records())
    #records are built 0 being name, 1 being price (it is a list of list so state record first)
    for rec in records:
        ins_new_rec(name=rec[0],salary=rec[1])
    print("Complete, wiping the csv...")
    overwrite_csv()
    time.sleep(5)

def main():
    while True:
        clear_terminal()
        menu()
        choice = get_choice()
 
        if choice == -1:
            pass #this is an invalid choice catch from the int checker
        elif choice == 1:
            add_rec() #add new rec to csv
        elif choice == 2:
            print(get_records()) #read csv and print
            time.sleep(5)
        elif choice == 3:
            csv_to_sql() #convert CSV into SQLite tble
        elif choice == 4: 
            overwrite_csv() #temp
        else:
            break

if __name__ == "__main__":
    main()