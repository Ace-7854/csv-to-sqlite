from csv_mod import *
from sqlite_mod import ins_new_record

def remv_char(records):
    for rec in records:
        rec.replace("\n","")
    
    return records

def main():
    records = remv_char(get_records())
    print(records)
    sanatized_records = []

    for rec in records:
        sanatized_records.append(rec.split(","))

    print(sanatized_records)

    for record in sanatized_records:
        record[4] = int(record[4])
    
    for record in sanatized_records:
        ins_new_record(record[0], record[1],record[2],record[3],record[4],record[5],record[6])

main()