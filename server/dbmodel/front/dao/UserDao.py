# -*- coding: utf-8 -*-
import psycopg2
from dbmodel.front import Config

def getByUserid(ip,dbname,userid):
    conn = psycopg2.connect(database=dbname, user=Config.DATA_USER, password=Config.DATA_PASSWORD, host=ip, port=Config.DATA_PORT)
    cursor = conn.cursor()

    query = "select cu.id,ca.authstring,cu.nickname,cu.xp,cu.gold,cu.rock,cu.feat,cu.vrock from core_user cu JOIN core_account ca on cu.id=ca.user_id where cu.id=%s;"%userid
    cursor.execute(query)
    all = cursor.fetchall()

    conn.commit()
    conn.close()
    return all

def getByAllProds(ip,dbname):
    conn = psycopg2.connect(database=dbname, user=Config.DATA_USER, password=Config.DATA_PASSWORD, host=ip, port=Config.DATA_PORT)
    cursor = conn.cursor()

    query = "select cu.id,cu.jprods from core_user cu;"
    cursor.execute(query)
    all = cursor.fetchall()
    print "all:",all

    conn.commit()
    conn.close()
    return all