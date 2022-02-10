import psycopg2


class DataBaseWorker:
    """Класс, реализующий взаимодействие с базой данных, для которого определены методы:
       1. __init__(self, data_base_dict)
       2. create_table(self)
       3. close_connection(self)
       4. add_company(self, list_of_data)
       5. test_delete(self)
    """
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
        """Функция-конструктор объекта класса DataBaseWorker. Принимает ссылку на самого себя и словарь с информацией
            о подключаемой базе данных, содержащий данные о host, port, user, password, db_name.
        """
        self.connection = psycopg2.connect(host=data_base_dict['host'],
                                           port=data_base_dict['port'],
                                           user=data_base_dict['user'],
                                           password=data_base_dict['password'],
                                           dbname=data_base_dict['db_name']
                                           )
        self.cursor = self.connection.cursor()

    def create_table(self):
        """Отладочный метод, создающий в подключенной базе данных таблицу со следующими полями:
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
            PRIMARY KEY (id))
            Функция вызывает метод cursor.execute() с параметром create_table_query
        """
        self.cursor.execute(self.create_table_query)

    def close_connection(self):
        """Метод, закрывающий соединение с базой данных"""
        self.connection.close()

    def add_company(self, list_of_data):
        """Метод, добавляющий в таблицу company строку с параметрами"""
        self.cursor.execute(self.add_company_query, (list_of_data[0],  # id (генерируется посредством uuid.uuid1())
                                                    list_of_data[1],  # имя компании
                                                    list_of_data[2],  # cik
                                                    list_of_data[3],  # assigned_sic
                                                    list_of_data[4],  # улица расположения бизнеса
                                                    list_of_data[5],  # город расположения бизнеса
                                                    list_of_data[6],  # штат расположения города
                                                    list_of_data[7],  # индек
                                                    list_of_data[8],  # почта улица
                                                    list_of_data[9],  # почта город
                                                    list_of_data[10], # почта штат
                                                    list_of_data[11], # почта индекс
                                                    list_of_data[12]  # дата добавления
                                                     )
                                )

        self.connection.commit()
        print("Запрос в базе")



    def test_delete(self):
        """Тестовый метод, существующий для удаления всех срок из таблицы company"""
        self.cursor.execute(self.test_delete)



