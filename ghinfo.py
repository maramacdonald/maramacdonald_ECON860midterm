import json
import requests
import pandas
import csv

df = pandas.DataFrame()


f = open("token1", "r")
token1 = f.read()
f.close()
#print(token1)

f = open("username", "r")
username = f.read()
f.close()
#print(username)

github_session = requests.Session()
github_session.auth = (username, token1)

userList = list(csv.reader(open("parsed_files/gitusersdata.csv")))
userid = userList[2][0]
print(userid)