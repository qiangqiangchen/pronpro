# -*- coding: utf-8 -*-
import MySQLdb
import scrapy
from pornpro.DBHelper import DBHelper
from pornpro.items import PornproItem
class PornproPipeline(object):

    def process_item(self, item, spider):
        db=DBHelper()
        select_sql="select * from pornlist where title_url='%s'"%(item['title_url'].encode('utf-8'))
        #print select_sql
        data=db.select(select_sql)
        print data
        if data:
            pass
        else:
            sql="insert into pornlist(title,title_url,author,creat_time,replycount,viewcount) values('%s','%s','%s','%s','%s','%s')"%(item['title'].encode('utf-8'),item['title_url'].encode('utf-8'),item['author'].encode('utf-8'),item['creat_time'].encode('utf-8'),item['replycount'].encode('utf-8'),item['viewcount'].encode('utf-8'))
            print sql
            db.insert(sql)
        return item