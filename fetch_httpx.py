import httpx
from fake_useragent import UserAgent
import random
from datetime import datetime, time, timedelta
import asyncio
import itertools
# from httpx_parse.proxy_old import *
import json
from config import *

# #Получение guid самой свежей публикаций компании (вне зависимости была ли она сделана по доверенности или нет)
# async def fetch_pub_last_guid(guid):
#     for i in range(3):
#         # try:
#         url_pub = f"https://fedresurs.ru/backend/companies/{guid}/publications"
#         url_pub_from_publisher = f"https://fedresurs.ru/backend/companies/{guid}/publications-from-bankrupt-publisher"
#         params = {
#             "limit": 15,
#             "offset": 0,
#             "isActive": "true"
#         }
#         ua = UserAgent()
#         headers = {
#             "User-Agent": ua.random,
#             "Accept": "application/json, text/plain, */*",
#             "Referer": "https://fedresurs.ru/entities",
#             "Origin": "https://fedresurs.ru"
#         }

#         async with httpx.AsyncClient(proxy=await class_proxy.get_proxy()) as client:
#             response = await client.get(url_pub, params=params, headers=headers, timeout=httpx_timeout)
#             with open("response.txt", "w", encoding="utf-8") as file:
#                 file.write(response.text)
#             print(url_pub)
#             print(response)
#             pub = response.json()
            
#         # await asyncio.sleep(0.5)
#         async with httpx.AsyncClient(proxy=await class_proxy.get_proxy()) as client:
#             response = await client.get(url_pub_from_publisher, params=params, headers=headers, timeout=httpx_timeout)
#             pub_from_publisher = response.json()     
#             print(url_pub_from_publisher)
#             print(response)
#             pub = response.json()
            


#             if pub['found'] == 0 and pub_from_publisher['found'] != 0:
#                 return {"guid_pub" : (pub_from_publisher['pageData'][0])['guid'], "time_pub" : (pub_from_publisher['pageData'][0])['datePublish']}
#             if pub_from_publisher['found'] == 0 and pub['found'] != 0:
#                 return {"guid_pub" : (pub['pageData'][0])['guid'], "time_pub" :  (pub['pageData'][0])['datePublish']}
#             time_format = "%Y-%m-%dT%H:%M:%S.%f"
#             time_pub = datetime.strptime((pub['pageData'][0])['datePublish'], time_format)
#             time_pub_from_publisher = datetime.strptime((pub_from_publisher['pageData'][0])['datePublish'], time_format)
#             if time_pub_from_publisher > time_pub:
#                 return {"guid_pub" : (pub_from_publisher['pageData'][0])['guid'], "time_pub" : time_pub_from_publisher}
#             elif time_pub_from_publisher < time_pub:
#                 return {"guid_pub" : (pub['pageData'][0])['guid'], "time_pub" : time_pub}
#             else:
#                 return None
#         # except Exception as e:
#         #     print(f"Получаю guid {e}")

#             pass
#     return None

#Получение guid самой свежей публикаций компании (вне зависимости была ли она сделана по доверенности или нет)
async def fetch_pub_last_guid(guid):
    for i in range(3):
        try:
            url_pub = f"https://fedresurs.ru/backend/companies/{guid}/publications"
            url_pub_from_publisher = f"https://fedresurs.ru/backend/companies/{guid}/publications-from-bankrupt-publisher"
            params = {
                "limit": 15,
                "offset": 0,
                "isActive": "true"
            }
            ua = UserAgent()
            headers = {
            'accept': 'application/json, text/plain, */*',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'referer': 'https://fedresurs.ru/entities',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
            'Cookie': 'qrator_msid2=v2.0.1745222735.793.54fc93fdGEBAmBYB|gHe9eHbBMNMxCgX8|rhSeQh3xtoFHzbxnCD4flFTJ82UB0/VmGoFa2nN6do/dqtZIkDrhMA8wGBdCwNr5HR3dgUsNLwAb3Akwp5NY9o5kAxKyPRL9nkSEFtbmjkI=-mVdKYuu1moNhBxMmY5QPBbImtqY='
            }

            async with httpx.AsyncClient(proxy=await class_proxy.get_proxy()) as client:
                response = await client.get(url_pub, params=params, headers=headers, timeout=httpx_timeout)
                with open("response.txt", "w", encoding="utf-8") as file:
                    file.write(response.text)
                # print(url_pub)
                # print(response)
                pub = response.json()
                
            # await asyncio.sleep(0.5)
            async with httpx.AsyncClient(proxy=await class_proxy.get_proxy()) as client:
                response = await client.get(url_pub_from_publisher, params=params, headers=headers, timeout=httpx_timeout)
                pub_from_publisher = response.json()     
                # print(url_pub_from_publisher)
                # print(response)
                pub = response.json()
                


                if pub['found'] == 0 and pub_from_publisher['found'] != 0:
                    return {"guid_pub" : (pub_from_publisher['pageData'][0])['guid'], "time_pub" : (pub_from_publisher['pageData'][0])['datePublish']}
                if pub_from_publisher['found'] == 0 and pub['found'] != 0:
                    return {"guid_pub" : (pub['pageData'][0])['guid'], "time_pub" :  (pub['pageData'][0])['datePublish']}
                time_format = "%Y-%m-%dT%H:%M:%S.%f"
                time_pub = datetime.strptime((pub['pageData'][0])['datePublish'], time_format)
                time_pub_from_publisher = datetime.strptime((pub_from_publisher['pageData'][0])['datePublish'], time_format)
                if time_pub_from_publisher > time_pub:
                    return {"guid_pub" : (pub_from_publisher['pageData'][0])['guid'], "time_pub" : time_pub_from_publisher}
                elif time_pub_from_publisher < time_pub:
                    return {"guid_pub" : (pub['pageData'][0])['guid'], "time_pub" : time_pub}
                else:
                    return None
        except Exception as e:
            # print(f"Получаю guid {e}")
            pass
    return None

#Получить список компаний в ленте определённый <offset>
async def fetch_data(url, params, offset):
    for i in range(3):
        ua = UserAgent()    
        headers = {
            "User-Agent": ua.random,
            "Accept": "application/json, text/plain, */*",
            "Referer": "https://fedresurs.ru/entities",
            "Origin": "https://fedresurs.ru"
        }
        # headers = {
        #     'accept': 'application/json, text/plain, */*',
        #     'cache-control': 'no-cache',
        #     'pragma': 'no-cache',
        #     'referer': 'https://fedresurs.ru/entities',
        #     'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
        #     'sec-ch-ua-mobile': '?0',
        #     'sec-ch-ua-platform': '"Windows"',
        #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
        #     'Cookie': 'qrator_msid2=v2.0.1745222735.793.54fc93fdGEBAmBYB|gHe9eHbBMNMxCgX8|rhSeQh3xtoFHzbxnCD4flFTJ82UB0/VmGoFa2nN6do/dqtZIkDrhMA8wGBdCwNr5HR3dgUsNLwAb3Akwp5NY9o5kAxKyPRL9nkSEFtbmjkI=-mVdKYuu1moNhBxMmY5QPBbImtqY='
        #     }
        updated_params = params.copy()
        updated_params["offset"] = offset
        try:
            async with httpx.AsyncClient(proxy=await class_proxy.get_proxy()) as client:
                response = await client.get(url, params=updated_params, headers=headers, timeout=httpx_timeout)
            print(response.status_code) 
            print(response.text)   
            if response.status_code == 200:
                response = response.json()
                response['page'] = int(int(offset) / 15)
                return response 
        except Exception as e:
            # print(f"Ошибка! (Все компании в ленте) {e}")
            pass
    return None

#Получить список компаний в ленте
async def fetch_guid_comp():
    url = "https://fedresurs.ru/backend/companies"
    params = {
        "limit": 15,
        "offset": 0,
        "isActive": "true"
    }
    offsets = [i * 15 for i in range(count_load_more)]
    tasks = [fetch_data(url, params, offset) for offset in offsets]
    responses = await asyncio.gather(*tasks, return_exceptions=False) 
    responses = [r for r in responses if r is not None]
    # print(responses)
    return responses

#Получение информации по публикации
async def fetch_all_info_from_pub(guid_pub, quid_comp):
    for i in range(3):
        try:
            ua = UserAgent()
            # headers = {
            #     "User-Agent": ua.random,
            #     "Accept": "application/json, text/plain, */*",
            #     "Referer": "https://fedresurs.ru/entities",
            #     "Origin": "https://fedresurs.ru"
            # } 
            headers = {
            'accept': 'application/json, text/plain, */*',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'referer': 'https://fedresurs.ru/entities',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
            'Cookie': 'qrator_msid2=v2.0.1745222735.793.54fc93fdGEBAmBYB|gHe9eHbBMNMxCgX8|rhSeQh3xtoFHzbxnCD4flFTJ82UB0/VmGoFa2nN6do/dqtZIkDrhMA8wGBdCwNr5HR3dgUsNLwAb3Akwp5NY9o5kAxKyPRL9nkSEFtbmjkI=-mVdKYuu1moNhBxMmY5QPBbImtqY='
            }
            async with httpx.AsyncClient(proxy=await class_proxy.get_proxy()) as client:
                url = f"https://fedresurs.ru/backend/sfact-messages/{guid_pub}"
                start_pub_url = "https://fedresurs.ru/sfactmessages/"
                response = await client.get(url, headers=headers, timeout=httpx_timeout)
                if response.status_code == 404:
                    url = f"https://fedresurs.ru/backend/bankruptcy-messages/{guid_pub}"
                    start_pub_url = "https://fedresurs.ru/bankruptmessages/"
                    response = await client.get(url, headers=headers, timeout=httpx_timeout)
            response = response.json()

            h_m = {"title" : None, 
                "date_time" : None, 
                "pub_link" : None, 
                "inn_deb" : None, "name_deb" : None, 
                "inn_pub" : None, "name_pub" : None, 
                "inn_sro" : None, "name_sro" : None,
                "comp_link" : None}
            h_m['comp_link'] = "https://fedresurs.ru/companies/" + quid_comp
            
            h_m['title'] = response.get('typeName')

            if response.get('datePublish') is not None:
                date_publish = response.get('datePublish')
                date_publish = date_publish.split('.')[0]
                dt = datetime.fromisoformat(date_publish)
                formatted_date = dt.strftime("%Y-%m-%d %H:%M:%S")
                h_m['date_time'] = formatted_date
            
            h_m['pub_link'] = start_pub_url + response.get('guid')

            #Получение информации о должнике (Если это поле должник есть)
            deb = response.get('bankrupt')
            if deb is not None:
                h_m['inn_deb'] = deb.get('inn')
                h_m['name_deb'] = deb.get('name')
            else:
                deb = response.get('content')
                if deb is not None:
                    deb = deb.get('debtor')
                    if deb is not None:
                        h_m['inn_deb'] = deb.get('inn')
                        h_m['name_deb'] = deb.get('shortName')
                        if h_m['name_deb'] is None:
                            h_m['name_deb'] = deb.get('fio')
            #Получаем информацию о публикаторе
            pub = response.get('publisher')
            if pub is not None:
                h_m['inn_pub'] = pub.get('inn')
                h_m['name_pub'] = pub.get('name')

            #Данные СРО
            sro = (response.get('publisher')).get('sroInfo')
            if sro is not None:
                h_m['inn_sro'] = response.get('inn')
                h_m['name_sro'] = response.get('name')

            if h_m['name_deb'] is None:
                if h_m['title'] == "Намерение должника обратиться в суд с заявлением о банкротстве" or h_m['title'] == "Намерение кредитора обратиться в суд с заявлением о банкротстве":
                    h_m['name_deb'] = h_m['name_pub']
                    h_m['inn_deb'] = h_m['inn_pub']


            return h_m
        except:
            #print("ups получение данных из публикации")
            pass
    return None

#Проверить время
async def check_time(now_time, pub_time, counter):
    if isinstance(pub_time, str):
        pub_time = datetime.strptime(((pub_time.replace("T", " ")).split("."))[0], "%Y-%m-%d %H:%M:%S")
    if pub_time < now_time and pub_time > now_time - timedelta(minutes=time_parse_interval):
        counter['val'] = 0
        return True, False, pub_time.strftime("%Y-%m-%d %H:%M:%S")
    elif pub_time < now_time - timedelta(minutes=time_parse_interval):
        counter['val'] = counter['val'] + 1
        if counter['val'] == count_for_counter_out_of_range:
            return False, False, None
        return False, False, pub_time.strftime("%Y-%m-%d %H:%M:%S")
    elif pub_time < now_time - timedelta(minutes=time_parse_interval) and pub_time > now_time - timedelta(minutes=time_parse_interval*4):
        return False, True, pub_time.strftime("%Y-%m-%d %H:%M:%S")
    else:
        return False, False, None

#Получить список публикаций
async def fetch_all_pub_list(guid_comp, now_time):
    counter = {"val" : 0}
    rez_pub = []
    rez_comp = []
    for g in guid_comp:
        pub_guid = await fetch_pub_last_guid(g)
        # print(pub_guid)
        if pub_guid is not None:
            flag_add, flag_end, time_pub = await check_time(now_time, pub_guid['time_pub'], counter)
            pub_guid['time_pub'] = time_pub
            if flag_end:
                break
            elif flag_add:
                rez_pub.append(pub_guid)
                rez_comp.append(g)
    #Убираем повторы, получаем информацию
    rez_pub_vr = []
    rez_comp_vr = []
    for i, j in zip(rez_pub, rez_comp):
        if i not in rez_pub_vr:
            rez_pub_vr.append(i)
            rez_comp_vr.append(j)
    rez_pub = rez_pub_vr
    rez_comp = rez_comp_vr
    rez_info_pub = []
    for p, c in zip(rez_pub, rez_comp):
        pub_info = await fetch_all_info_from_pub(p['guid_pub'], c)
        if pub_info is not None:
            rez_info_pub.append(pub_info)
    return rez_info_pub