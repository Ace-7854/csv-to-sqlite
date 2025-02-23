import csv

def get_records():
    #get details of record from CSV
    with open("employees.csv","r") as file:
        records = file.readlines()
    
    records.remove(records[0])
    return records

def add_rec_csv(name, salary):
    record = [name,float(salary)]
    with open("employees.csv","a",newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(record)

def overwrite_csv():
    with open("employees.csv","w") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Salary"])
