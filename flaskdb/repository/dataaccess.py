"""
A Sample Web-DB Application for DB-DESIGN lecture
Copyright (C) 2022 Yasuhiro Hayashi
"""
from psycopg2 import sql, connect, ProgrammingError
import flaskdb.var as v
from flaskdb.model.itemModel import Item
from flaskdb.model.memoModel import Memo


class DataAccess:

    # Constractor called when this class is used. 
    # It is set for hostname, port, dbname, useranme and password as parameters.
    def __init__(self, hostname, port, dbname, username, password):
        self.dburl = "host=" + hostname + " port=" + str(port) + \
                     " dbname=" + dbname + " user=" + username + \
                     " password=" + password

    # This method is used to actually issue query sql to database. 
    def execute(self, query, autocommit=True):
        with connect(self.dburl) as conn:
            if v.SHOW_SQL:
                print(query.as_string(conn))
            conn.autocommit = autocommit
            with conn.cursor() as cur:
                cur.execute(query)
                if not autocommit:
                    conn.commit()
                try:
                    return cur.fetchall()
                except ProgrammingError as e:
                    return None

    # For mainly debug, This method is used to show sql to be issued to database. 
    def show_sql(self, query):
        with connect(self.dburl) as conn:
            print(query.as_string(conn))

    # search item data
    def search_items(self):
        query = sql.SQL("""
            SELECT * FROM \"items\"
        """)
        # self.show_sql(query)
        results = self.execute(query, autocommit=True)
        item_list = []
        for r in results:
            item = Item()
            item.id = r[0]
            item.user_id = r[1]
            item.itemname = r[2]
            item.price = r[3]
            item_list.append(item)
        return item_list

    # search item data by itemname
    def search_items_by_itemname(self, itemname):
        query = sql.SQL("""
            SELECT * FROM \"items\" WHERE itemname LIKE {itemname}
        """).format(
            itemname = sql.Literal(itemname)
        )
        # self.show_sql(query)
        results = self.execute(query, autocommit=True)
        item_list = []
        for r in results:
            item = Item()
            item.id = r[0]
            item.user_id = r[1]
            item.itemname = r[2]
            item.price = r[3]
            item_list.append(item)
        return item_list

    def add_item(self, item):
        query = sql.SQL("""
            INSERT INTO \"items\" ( {fields} ) VALUES ( {values} )
        """).format(
            tablename = sql.Identifier("items"),
            fields = sql.SQL(", ").join([
                sql.Identifier("itemname"),
                sql.Identifier("price")
            ]),
            values = sql.SQL(", ").join([
                sql.Literal(item.itemname),
                sql.Literal(item.price)
            ])
        )
        self.execute(query, autocommit=True)
    
    def insert_memo(self, memo):
        query = sql.SQL("""
            INSERT INTO \"files\" ( {fields} ) VALUES ( {values} )
        """).format(
            tablename = sql.Identifier("files"),
            fields = sql.SQL(", ").join([
                sql.Identifier("file_name"),
                sql.Identifier("user_name"),
                sql.Identifier("share")
            ]),
            values = sql.SQL(", ").join([
                sql.Literal(memo.file_name),
                sql.Literal(memo.user_name).
                sql.Literal(memo.share)
            ])
        )
        self.execute(query, autocommit=True)


    # search item data by itemname
    def search_items_by_itemname(self):
        query = sql.SQL("""
            SELECT (id, files_name, user_id, share, updated_at) FROM \"files\" WHERE share = 1
        """)
        # self.show_sql(query)
        results = self.execute(query, autocommit=True)
        memo_list = []
        for r in results:
            memo = Memo()
            memo.id = r[0]
            memo.file_name = r[1]
            memo.user_id = r[2]
            memo.user_name = r[3]
            memo.share = r[4]
            memo.append(memo)
        return memo_list

