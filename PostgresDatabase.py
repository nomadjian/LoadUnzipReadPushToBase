import os
import psycopg2
from psycopg2 import Error

connection = psycopg2.connect(
            database='d2em5jcg4ukl5p',
            user="vwwreudwxkqxjh",
            password="ebbab1438a8861b491532d7557c4aa4c8c01dd5b6d42ef246a6077c26a0c68f6",
            host="ec2-54-224-64-114.compute-1.amazonaws.com",
            port="5432"
            )

cursor = connection.cursor()

cursor.execute(''' CREATE TABLE Company (
   id VARCHAR(255),
   date VARCHAR(255),
   name VARCHAR(255),
   cik VARCHAR(255),
   sic VARCHAR(255),
   business_street VARCHAR(255) NULL,
   business_city VARCHAR(255) NULL,
   business_state VARCHAR(255) NULL,
   business_zip VARCHAR(255) NULL,
   main_street VARCHAR(255) NULL,
   main_city VARCHAR(255) NULL,
   main_state VARCHAR(255) NULL,
   main_zip VARCHAR(255) NULL,
   create_company_date VARCHAR(255) NULL,
   PRIMARY KEY (id)
);''')

connection.commit()

connection.close()