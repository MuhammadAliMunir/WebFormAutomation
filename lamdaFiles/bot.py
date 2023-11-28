import mysql.connector
import csv
import script as child
import time


accounts = {}
count = 0
with open('config.csv', 'r', errors='ignore') as file:
    reader = csv.reader(file, delimiter=":")
    for row in reader:
      accounts[count] = row[1]
      count += 1
def main():
  mydb = mysql.connector.connect(
    host = accounts[0],
    user = accounts[1],
    passwd = accounts[2],
    database = accounts[3]
  )

  mycursor = mydb.cursor()
  # mycursor.execute("SELECT * FROM `TestLeads` where Status = 'New'")
  proxy = {}
  mycursor.execute("SELECT * FROM `Proxies` ")
  myresult = mycursor.fetchall()
  for elem in myresult:
    proxy[elem[0]] = elem[1]
  # print(proxy) 
  mycursor.execute("SELECT * FROM `TestLeads` where Status = 'New'")
  myresult = mycursor.fetchall()

  # print(myresult)
  # exit()
  # x = []
  # obj = child.script()
  # # obj.ip_requests()
  # obj.putData(x)
  # exit()
  for x in myresult:
      data = []
      data.append(x)
      data.append(proxy)
      print(x)
      try:
        obj = child.script()
        obj.putData(data)
        ip = obj.ip_requests()
        mycursor.execute("UPDATE TestLeads SET Status = 'Done', SubmitedTimestamp = Now(),`IPUsed` = '"+str(ip)+"'  WHERE IdTestLeads = "+str(x[0]))
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")

          
      except Exception as e:
        print(str(x[0])+' error', e)
        mycursor.execute("UPDATE TestLeads SET Status = 'Error accure', SubmitedTimestamp = Now()  WHERE IdTestLeads = "+str(x[0]))
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")

  mydb.close()
while 1 < 2:
  main()
  print("Data updated")
  time.sleep(1)
# print(accounts[0][1])