import psycopg2


class DataBaseWorker:

    test_delete = '''DELETE * from company'''

    create_table_query = ''' CREATE TABLE Company (id VARCHAR(255),/
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
                            PRIMARY KEY (id))'''

    add_company_query = '''INSERT INTO company (id,
                                                name,
                                                cik, 
                                                sic, 
                                                business_street, 
                                                business_city, 
                                                business_state, 
                                                business_zip, 
                                                main_street, 
                                                main_city, 
                                                main_state, 
                                                main_zip, 
                                                date)
                                                VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''

    def __init__(self, data_base_dict):
        self.connection = psycopg2.connect(host=data_base_dict['host'],
                                           port=data_base_dict['port'],
                                           user=data_base_dict['user'],
                                           password=data_base_dict['password'],
                                           dbname=data_base_dict['db_name']
                                           )
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute(self.create_table_query)

    def close_connection(self):
        self.connection.close()

    def add_company(self, list_of_data):
        self.cursor.execute(self.add_company_query, (list_of_data[0],
                                                    list_of_data[1],
                                                    list_of_data[2],
                                                    list_of_data[3],
                                                    list_of_data[4],
                                                    list_of_data[5],
                                                    list_of_data[6],
                                                    list_of_data[7],
                                                    list_of_data[8],
                                                    list_of_data[9],
                                                    list_of_data[10],
                                                    list_of_data[11],
                                                    list_of_data[12]
                                                     )
                                )

        self.connection.commit()
        print("Запрос в базе")


    def test_delete(self):
        self.cursor.execute(self.test_delete)



