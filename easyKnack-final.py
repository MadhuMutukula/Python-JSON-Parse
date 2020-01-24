# -*- coding: utf-8 -*-
"""
/*  Written by Madhu Mutukula */
Ask
1. Parse the json file.
2. Load the parsed json onto the screen.
3. Apply data normalization to create appropriate schema.? you mean DB schema
Tables (Json levels)
  level1 -main :address,city,medianHouseValue,zip,districtId
  level2 -Schools: name, grade
  level3 -faculty: name, role,startDate

4. Push the code to Github (please double check it runs) and send us the repo where we can pull it down to run it ourselves.
5. Present your work and explain how you tackle this problem through a video call.
"""
import pandas as pd
import json
import sys, os, shutil  # needed to perform any Os commands
import datetime
from collections import namedtuple
#import cx_oracle  if we want load to oracle
from pandas.io.json import json_normalize
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# using nornamlize functions -
def main():
    with open('sample_api_output.json','r',encoding='Utf8', errors='replace') as f:
        data=json.load(f)
        print(data)  #prints original data i json format
        #result = json_normalize(json.load(f)) #1st level
        #result = json_normalize(json.load(f), record_path=['schoolDistrict','schools'],meta=['address','city','medianHouseValue','zip',['schoolDistrict','districtId']]) #2nd level
        result = json_normalize(json.load(f), record_path=['schoolDistrict','schools','faculty'],meta=['address','city','medianHouseValue','zip',['schoolDistrict','districtId'],['schoolDistrict','schools','schoolGrade'],['schoolDistrict','schools','schoolName']])#3rd level
        print(result)  #prints normlized data with all3levels
        # create sql from above result data from and laod to db
# using loops
def main1():
    with open('sample_api_output.json','r',encoding='Utf8', errors='replace') as f:
        data = json.load(f)
        #print(json.dumps(data, indent = 4, sort_keys=True))  # prints with indent
        df = pd.io.json.json_normalize(data)
        #print(df['medianHouseValue'])
        sql_main='insert into school_main (address, city, meadian_value, zip, districtid )'
        sql_main +='values(\''+df['address']+'\',\''+ df['city']+'\',\''+ str(df['medianHouseValue'])+'\',\''+ df['zip']+'\',\''+ str(df['schoolDistrict.districtId'])+'\')'
        print(sql_main)
        #print(df['schoolDistrict.districtId'])
        #print(df.keys())

        for i in df['schoolDistrict.schools']:
            for  j in i:
                sql_school='insert into schools (school_name, school_grade) '
                sql_school+='values(\''+ j['schoolName']+'\',\''+ j['schoolGrade']+'\')'
                #print(sql_school)
                    
                for k in j['faculty']:
                    sql_faculty='insert into faculty (name, role,start_Date, school_name) '
                    sql_faculty+='values(\''+ k['name']+'\',\''+ k['role']+'\',\''+k['startDate']+'\',\''+j['schoolName']+'\')'
                    #print(sql_faculty)
                   

if __name__ == "__main__":
    main()

                                         

      
#print(data)  # prints json on to screen


