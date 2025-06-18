from proxy import *

#Таймаут для прокси
time_proxy_timeout = 5

#Интервал парсинга каждые (n) минут
time_parse_interval = 5

#Сколько нажимаем загрузить ещё
count_load_more = 15

#Класс менеджера прокси
class_proxy = ProxyManager(time_proxy_timeout)

#Таймаут на запрос
httpx_timeout = 3

#После сколько выпадающих записей останавливаемся
count_for_counter_out_of_range = 8