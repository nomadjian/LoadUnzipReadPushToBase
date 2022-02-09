import WorkWithSite
import Unzip
import PostgresDatabase


urls_list = WorkWithSite.get_urls_for_load()  # работает исправно)


for i in range(3):# это тестовая штучка,
    print(urls_list.pop(0))
    WorkWithSite.load_file(urls_list.pop(0))

Unzip.get_and_unzip()  # распаковываем
prepared_for_table = Unzip.parse_data_from_files()  # парсим данные из файлов

Unzip.clean_up_dir(Unzip.ARCHIVES_PATH)  # чистим директорию с архивами
Unzip.clean_up_dir(Unzip.DECOMPRESSED_PATH)  # чистим директорию с распакованными файлами

print("инициализация датабазы")

database = {
            'host': 'ec2-52-49-56-163.eu-west-1.compute.amazonaws.com',
            'db_name': 'd3v098n9ebeee9',
            'user': 'yhtlrwhaqqbdsq',
            'password': 'bdfce12f81a5b9dfc938f9ba3c1adc0a5eba546588cdb8deb7a10f56ca872804',
            'port': '5432'
           }


connection = PostgresDatabase.DataBaseWorker(database)
print("соединие установлено")
print(prepared_for_table)


# тестовый вкид в базу heroku
for i in range(len(prepared_for_table)):
    print(prepared_for_table[i])
    connection.add_company(prepared_for_table[i])


if (input("Чистим базу?")) == 'y':
    connection.test_delete()

print("закрываем соединение")
connection.close_connection()
