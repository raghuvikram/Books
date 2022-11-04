#!/usr/bin/env python
# coding: utf-8

# In[3]:



import mysql.connector
import pandas as pd

hostname = 'localhost'
db = 'usecase2'
username = 'root'
pwd = 'V4i5k6@456'
port_id = 3306
conn = None
cur = None
try:
    
    
    conn = mysql.connector.connect(
           host = hostname,
           database = db,
           user = username,
           password = pwd,
           port = port_id)
    
    cur = conn.cursor()
    
    cur.execute('select * FROM birds')
    data = cur.fetchall()
    df = pd.DataFrame(data,columns = ['ID','BirdName','TypeOfBird','ScientificName'])
    print(df)
    #df.to_csv('c:/Users/venkata.raghu.mitta/Downloads/Test_data/Birds.csv')
    conn.commit()
    
    
except Exception as error:
    print(error)
    
finally:
    if cur is not None:
        cur.close()


# In[4]:


import requests
import csv



import pandas as pd
url = 'http://api.coincap.io/v2/assets'



headers = {
    'Accept':'application/json',
    'Content-Type':'application/json'
}
response = requests.request("GET",url, headers = headers, data = {})
myjson = response.json()
ourdata = []
csvheader = ['SYMBOL','NAME','PRICE(USD)']



for x in myjson['data']:
    ourdata.append([x['symbol'],x['name'],x['priceUsd']])
df = pd.DataFrame(ourdata,columns = ['SYMBOL','NAME','PRICE(USD)'])



print(df)
df.to_csv('C:/Users/venkata.raghu.mitta/Downloads/Test_data/crypto.csv')


# In[6]:



import mysql.connector
import pandas as pd


hostname = 'localhost'
db = 'usecase1'
username = 'root'
pwd = 'V4i5k6@456'
port_id = 3306
conn = None
cur = None
try:
    
    
    conn = mysql.connector.connect(
           host = hostname,
           database = db,
           user = username,
           password = pwd,
           port = port_id)
    
    cur = conn.cursor()
    
    cur.execute('select * FROM books')
    data = cur.fetchall()
    df = pd.DataFrame(data,columns = ['BookName','Category','Price','Price_Range'])
    print(df)
    #df.to_csv('c:/Users/venkata.raghu.mitta/Downloads/Test_data/Books.csv')
    conn.commit()
    
    
except Exception as error:
    print(error)
    
finally:
    if cur is not None:
        cur.close()


# In[ ]:




