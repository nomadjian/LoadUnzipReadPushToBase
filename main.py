import WorkWithSite
import Unzip


urls_list = WorkWithSite.get_urls_for_load()  # работает исправно)


for i in range(int(input("Сколько файлов качаем->"))):
    print(urls_list.pop(0))
    WorkWithSite.load_file(urls_list.pop(0))

Unzip.get_and_unzip()
prepared_for_table = Unzip.parse_data_from_files()

for i in range(len(prepared_for_table)):
    print(prepared_for_table[i])