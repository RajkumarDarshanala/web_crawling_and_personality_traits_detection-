# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class SpiderCrawlPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('heros.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS hero_tb""")
        self.curr.execute("""create table hero_tb(
                            name text,
                            movie text,
                            image_link text,
                            image BLOP,
                            Openness text ,
                            Conscientiousness text ,
                            Extroversion text ,
                            Agreeablenes text ,
                            Neuroticism text 
                            )""")
        # author text,
        # price text,
        # image_link text

    def process_item(self, item, spider):
        self.store_db(item)
        print("pipeline : " + item['name'])
        return item

    def store_db(self, item):
        self.curr.execute("""insert into hero_tb values (?,?,?,?,?,?,?,?,?)""", (
            item['name'],
            item['movie'],
            item['image_link'],
            item['image'],
            item['O'],
            item['C'],
            item['E'],
            item['A'],
            item['N']
        ))
        self.conn.commit()
