import asyncpg
from datetime import datetime

#Проверка есть ли компании в базе (ДА-возвращает id, НЕТ-возвращает null)
async def check_company(conn, name, inn):
    query = '''
        SELECT id
        FROM new_comp
        WHERE name = $1 AND inn = $2
    '''
    id = await conn.fetchrow(query, name, inn)
    if id is None:
        return None
    else:
        return id['id']

#Добавление новой компании в new_comp
async def add_company(conn, name, inn, comp_link):
    query = '''
    INSERT INTO new_comp (name, inn, comp_link)
    VALUES ($1, $2, $3)
    '''
    await conn.execute(query, name, inn, comp_link)
    return True

#Добавление публикации
async def add_pub(conn, pub_info, id_pub, id_deb):
    query = '''
    INSERT INTO new_pub (title, date_time, pub_link, id_pub, id_deb, inn_sro, name_sro)
    VALUES ($1, $2, $3, $4, $5, $6, $7)
    '''
    await conn.execute(query, pub_info['title'], datetime.strptime(pub_info['date_time'], "%Y-%m-%d %H:%M:%S"), pub_info['pub_link'], id_pub, id_deb, pub_info['inn_sro'], pub_info['name_sro'])

#Запись в sql
async def write_in_sql(data):
    conn = await asyncpg.connect(database="sb_bd", user="postgres", password="2003", host="87.242.118.178", port="5432")
    for d in data:
        if d['inn_deb'] is not None and d['name_deb'] is not None:
            if (await check_company(conn, d['name_deb'], d['inn_deb'])) is None:
                await add_company(conn, d['name_deb'], d['inn_deb'], d['comp_link'])
        if d['inn_pub'] is not None and d['name_pub'] is not None:
            if (await check_company(conn, d['name_pub'], d['inn_pub'])) is None:
                await add_company(conn, d['name_pub'], d['inn_pub'], d['comp_link'])
        id_pub = await check_company(conn, d['name_pub'], d['inn_pub'])
        id_deb = await check_company(conn, d['name_deb'], d['inn_deb'])
        await add_pub(conn, d, id_pub, id_deb)
    await conn.close()
