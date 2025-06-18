import asyncio
import pytz
from datetime import datetime, time, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.executors.asyncio import AsyncIOExecutor
from pytz import timezone
from apscheduler.triggers.cron import CronTrigger
import psycopg2
from psycopg2 import sql
from sql_func_httpx import *
from parse_EFRSB_httpx import *
from fetch_httpx import *
from config import *

#Из строки в float
def str_to_float(s: str)->float:
    arr = s.split()
    num_str = arr[0].replace(',', '.')
    num = float(num_str)

    if len(arr) == 2:
        return num
    
    else:
        if "млн" in s:
            return num * 1000000
        elif "тыс" in s:
            return num * 1000
        elif "млрд" in s:
            return num * 1000000000
        else:
            return -999
       
async def start_parse():
    print("Начал парсить")
    time_round = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
    time_round = time_round.replace(second=0, minute = ((time_round.minute)//time_parse_interval)*time_parse_interval )
    # Получаем список компаний в ленте
    rez_comp = await fetch_guid_comp()
    print(rez_comp)
    # print(rez_comp)
    #Обработаем массив
    rez_guid_comp = []
    for i in rez_comp:
        for g in i['pageData']:
            rez_guid_comp.append(g['guid'])
    #Получаем текст всех последних публикаций
    rez_guid_comp = list(dict.fromkeys(rez_guid_comp))
    print(f"{rez_guid_comp} rez_guid_comp")
    rez_pub = await fetch_all_pub_list(rez_guid_comp, time_round)
    print(f"rez_pub {rez_pub}")
    
    #Запись в sql
    # await write_in_sql(rez_pub)
    print("Закончил парсить")
async def job():
    await start_parse()

async def main():
    await job()
    # executors = {
    #     'default': AsyncIOExecutor()
    # }
    # scheduler = AsyncIOScheduler(executors=executors)
    # msk_timezone = timezone('Europe/Moscow')
    # scheduler.add_job(
    #     job,
    #     CronTrigger(minute='*/5', timezone=msk_timezone),
    #     max_instances=5, 
    #     misfire_grace_time=15
    # )
    # scheduler.start()
    # while True:
    #     await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main()) 
