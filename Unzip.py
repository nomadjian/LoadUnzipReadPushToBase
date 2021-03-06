import gzip
import os
import shutil
import re
import uuid

ARCHIVES_PATH = os.getcwd()+'/archives'
DECOMPRESSED_PATH = os.getcwd()+'/unzip'


def clean_up_dir(path):
    for way in os.listdir(path):
        print(f"Удаляем файл {path} в директории {path}")
        os.remove(f"{path}/{way}")


def get_and_unzip(archive_path=ARCHIVES_PATH, unzip_path=DECOMPRESSED_PATH):
    """Функция принимает в себя путь к архивам и путь, куда складываем распакованное. При помощи listdir получаем список
      архивов в папке и поочередно распаковываем и выгружаем в папку unzip_path
    """
    for way in os.listdir(archive_path):
        with gzip.open(f"{archive_path}/{way}") as compr_file:

            with open(f"{unzip_path}/{way.rsplit('.',2)[0]}", 'wb') as decompr_file:
                print(f"Декомпрессировали файл:{archive_path+way}")  # cугубо отладочный принт
                shutil.copyfileobj(compr_file, decompr_file)


def parse_data_from_files():
    """Функция создает список с путями к разархивированным данным, поочередно открывает их в режиме чтения,
       при помощи регулярного выражения text извлекает из файла строки, находящиеся промеж тегов <FILER>
       (между ними лежит валидная и неразрозненная информация), потом, поочередно, из этого содержимого парсится
       все,что между тегами <COMPANY-DATA>, <BUSINESS-MAIL> и <MAIL-ADDRESS>, потом извлеченное соединяется в список.

       Возвращает список из 12 элементов
    """
    text = re.compile(r"FILER>(.*?)</FILER>")

    name_reg = re.compile("CONFORMED-NAME>(.*?)"
                          "<CIK>(.*?)"
                          "<ASSIGNED-SIC>(.*?)<")

    business_reg = re.compile("<BUSINESS-ADDRESS><STREET[0-9]>(.*?)"
                              "<CITY>(.*?)"
                              "<STATE>(.*?)"
                              "<ZIP>(.*?)"
                              "<PHONE>(.*?)"
                              "</BUSINESS-ADDRESS>")

    mail_reg = re.compile("<MAIL-ADDRESS><STREET[0-9]>(.*?)"
                          "<(.*?)<CITY>(.*?)"
                          "<STATE>(.*?)"
                          "<ZIP>(.*?)<")
    output = []
    for file_way in os.listdir(DECOMPRESSED_PATH):

        with open(f"{DECOMPRESSED_PATH}\\{file_way}") as file:
            print(f"Читаем файл ->{file_way}")
            search_text = file.read().replace('\n', '')  # чтобы сработала регулярка
            search_text = search_text.replace('\x00', '')  # удаляем NUL значения для нормальной работы с базой
            company_data = re.findall(text, search_text)

            for data in company_data:
                company = re.findall(name_reg, data)
                business = re.findall(business_reg, data)
                mail = re.findall(mail_reg, data)

                temp_data = [str(uuid.uuid1())]
                if company:
                    temp_data = temp_data + list(company[0])
                else:
                    temp_data = temp_data + ['none' for x in range(3)]
                if business:
                    temp_data = temp_data + list(business[0])
                else:
                    temp_data = temp_data + ['none' for x in range(5)]
                if mail:
                    temp_data = temp_data + list(mail[0])
                else:
                    temp_data = temp_data + ['none' for x in range(4)]
                temp_data.append(file_way.split('.')[0])
                output.append(temp_data)
    print("Файлы дочитали")
    return output


