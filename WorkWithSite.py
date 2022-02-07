import re, requests


def get_urls_for_load():
    """Функция внутри себя компилирует три регулярки и последовательно бомбит адрес GET-реквестами,
       выискивая из него сперва совпадения с start_reg_ex, получая список постфиксов адресов, потом
       реквесты по адресу+постфикс и выискивает регулярку mid_reg_ex, и так далее.
       Возвращает список путей, по которым лежат архивы, которые потом потребуется скачать
    """

    start_reg_ex = re.compile(r'\d{4}/')  # компилим эту регулярку для того, чтобы потом пойти по разделу
    mid_reg_ex = re.compile(r'QTR\d+/')  # рега для нахождения каталога
    fin_reg_ex = re.compile(r'\d{8}\.nc\.tar\.gz')  # рега для нахождения файлов

    # это все можно загнать в отдельную функцию, но пока мои мозги этого не позволяют
    urls = eject_postfix(start_reg_ex)
    fulls = []  # временная переменная

    for url in urls:  # вот эти штуки можно вынести в отдельную функцию
        try:  # это делаем для того, чтобы при отстутствии ответа все не  падало)
            urls2 = set(eject_postfix(mid_reg_ex, url))
            print(urls2)
            for url2 in urls2:
                fulls.append(url + url2)
        except ConnectionError:
            break

    urls = []  # снова временная переменная
    for full in fulls:
        try:
            temp = set(eject_postfix(fin_reg_ex, full))
            print(temp)
            for tem in temp:
                urls.append(full + tem)
        except ConnectionError:
            break
    return urls


def get_request_text(post_fix=''):  # работает
    """Функция принимает в себя строковое значение post_fix, конкатенирует его с BASE_URL,
       и отправляет GET-реквест по полученному URL
       (USER_AGENT требуется для обмана защиты от ботов)
     """
    BASE_URL = 'https://www.sec.gov/Archives/edgar/Feed/'
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0'
    print(f"Кидаем реквест на->{BASE_URL+post_fix}")  # не имеет никакого предназначения, просто отладочный принт
    return requests.get(BASE_URL + post_fix, headers={'user-agent': USER_AGENT}).text


def eject_postfix(reg_ex, postfix=''):  # работает
    """Эта функция принимает в себя скомпилированную регулярку и найденный постфикс,
       вызывает функцию get_request_text(postfix), и в полученном request.text ищет
       и извлекает все совпадения с регуляркой.
    """
    return re.findall(reg_ex, get_request_text(postfix))


def load_file(post_fix):  # работает
    """Функция отправляет реквест с адресом архива и качает его в папку """
    BASE_URL = 'https://www.sec.gov/Archives/edgar/Feed/'
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0'
    print('Качаем файл')
    file = requests.get(BASE_URL + post_fix, headers={'user-agent': USER_AGENT}).content
    print('Файл скачан')
    f = open(f'archives/{post_fix.rsplit("/", 1 )[-1]}', 'wb')
    f.write(file)
    f.close()


