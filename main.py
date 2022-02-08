import WorkWithSite
import Unzip
import PostgresDatabase

urls_list = WorkWithSite.get_urls_for_load()  # работает исправно)


for i in range(3):# это тестовая штучка, в конце будет более весомый луп
    print(urls_list.pop(0))
    WorkWithSite.load_file(urls_list.pop(0))

Unzip.get_and_unzip()  # распаковываем
prepared_for_table = Unzip.parse_data_from_files()  # парсим данные из файлов

Unzip.clean_up_dir(Unzip.ARCHIVES_PATH)  # чистим директорию с архивами
Unzip.clean_up_dir(Unzip.DECOMPRESSED_PATH)  # чистим директорию с распакованными файлами

connection = PostgresDatabase.connect()
# тестовый вкид в базу heroku
for i in range(len(prepared_for_table)):
    print(f"{prepared_for_table[i]}"+"\n\n\n")
    PostgresDatabase.send_to_base(prepared_for_table, connection)

connection.close()
