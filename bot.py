import mysql.connector
import csv
import script as child
import time
# from pyvirtualdisplay import Display




accounts = {}
count = 0
with open('config.csv', 'r', errors='ignore') as file:
    reader = csv.reader(file, delimiter=":")
    for row in reader:
      accounts[count] = row[1]
      count += 1
def main():
  obj = child.script()
  obj.putData(data = [])


main()
