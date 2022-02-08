import os
import psycopg2
from psycopg2 import Error

def connect():
        connection = psycopg2.connect(database='d2em5jcg4ukl5p',
                                      user="vwwreudwxkqxjh",
                                      password="ebbab1438a8861b491532d7557c4aa4c8c01dd5b6d42ef246a6077c26a0c68f6",
                                      host="ec2-54-224-64-114.compute-1.amazonaws.com",
                                      port="5432"
                                      )
        return connection

def send_to_base(list_of_data, connection):
    for i in range(len(list_of_data)):
        cursor = connection.cursor()
        try:
            cursor.execute(f''' INSERT INTO company (name,cik,sic,business_street,business_city,business_state ,
                            business_zip,main_street,main_city,main_state,main_zip)

                            VALUES({list_of_data[i][0]},{list_of_data[i][1]},{list_of_data[i][2]},{list_of_data[i][3]},
                            {list_of_data[i][4]},{list_of_data[i][5]},{list_of_data[i][6]},{list_of_data[i][7]},
                            {list_of_data[i][8]if list_of_data[i][8]else "NULL"},  
                            {list_of_data[i][9]if list_of_data[i][9]else "NULL"},  
                            {list_of_data[i][10]if list_of_data[i][10]else "NULL"});''')

        except Error:
            print(Error)
            print("мы отвалились")
            cursor.commit()
            connection.close()

        cursor.commit()


#cursor.execute(''' CREATE TABLE Company (
#   id VARCHAR(255),
#   date VARCHAR(255),
#   name VARCHAR(255),
#   cik VARCHAR(255),
#   sic VARCHAR(255),
#   business_street VARCHAR(255) NULL,
#   business_city VARCHAR(255) NULL,
#   business_state VARCHAR(255) NULL,
#   business_zip VARCHAR(255) NULL,
#   main_street VARCHAR(255) NULL,
#   main_city VARCHAR(255) NULL,
#   main_state VARCHAR(255) NULL,
#   main_zip VARCHAR(255) NULL,
#   create_company_date VARCHAR(255) NULL,
#   PRIMARY KEY (id)
#);''')


