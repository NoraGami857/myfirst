# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class DoubanPipeline:

    def process_item(self, item, spider):
        db = pymysql.connect(host='localhost',user='root',password='Mjh842603317',port=3306,db='spider_163_news')

        cursor = db.cursor()
        #表里的name索引 是item【‘name’】
        name = item['name']

        cursor.execute(
            'INSERT INTO douban_name (name) values (%s)',
            (name)
        )
        db.commit()

        cursor.close()
        return item
