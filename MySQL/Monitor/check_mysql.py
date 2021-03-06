#!/usr/bin/env python
# -*- coding: utf-8 -*-
from base import DB
class DB_Info(object):
    """数据库信息
    """
    def __init__(self,host,port=3306,user="",passwd="",db="",charset="utf8"):
        """
        """
        self.db = DB(host,port,user,passwd,db,charset)
    def get_status(self):
        """
        """
        self.db.execute("show status")
        rows = self.db.fetchall()
        return dict([(row[0].upper(),row[1]) for row in rows])
    def get_master(self):
        """
        """
        self.db.execute("SHOW MASTER STATUS")
        row = self.db.fetchone()
        master_status = dict(zip(
            ("FILE", "POSITION", "BINLOG_DO_DB", "BINLOG_IGNORE_DB"), row
        ))
        cnt = self.db.execute("SHOW SLAVE HOSTS")
        rows = self.db.fetchall()
        master_hosts= list()
        for row in rows:
            master_hosts.append(
                dict(zip(
                    ("SERVER_ID", "HOST", "PORT", "MASTER_ID"),
                    row)))
        return master_status, master_hosts
    def get_slave(self):
        """
        """
        self.db.execute("SHOW STATUS")
        rows = self.db.fetchall()
        server_status = dict([(row[0].upper(),row[1]) for row in rows])
        cnt = self.db.execute("SHOW SLAVE STATUS")
        row = self.db.fetchone()
        if cnt == 0:
            print "Slave host not start."
            return server_status, None
        replicat_status = dict(zip(
            ("SLAVE_IO_STATE","MASTER_HOST","MASTER_USER","MASTER_PORT","CONNECT_RETRY",
            "MASTER_LOG_FILE","READ_MASTER_LOG_POS","RELAY_LOG_FILE","RELAY_LOG_POS",
            "RELAY_MASTER_LOG_FILE","SLAVE_IO_RUNNING","SLAVE_SQL_RUNNING","REPLICATE_DO_DB",
            "REPLICATE_IGNORE_DB","REPLICATE_DO_TABLE","REPLICATE_IGNORE_TABLE",
            "REPLICATE_WILD_DO_TABLE","REPLICATE_WILD_IGNORE_TABLE","LAST_ERRNO","LAST_ERROR",
            "SKIP_COUNTER","EXEC_MASTER_LOG_POS","RELAY_LOG_SPACE","UNTIL_CONDITION",
            "UNTIL_LOG_FILE","UNTIL_LOG_POS","MASTER_SSL_ALLOWED","MASTER_SSL_CA_FILE",
            "MASTER_SSL_CA_PATH","MASTER_SSL_CERT","MASTER_SSL_CIPHER","MASTER_SSL_KEY",
            "SECONDS_BEHIND_MASTER","MASTER_SSL_VERIFY_SERVER_CERT","LAST_IO_ERRNO","LAST_IO_ERROR",
            "LAST_SQL_ERRNO","LAST_SQL_ERROR","REPLICATE_IGNORE_SERVER_IDS","MASTER_SERVER_ID")
        ,row))
        return server_status, replicat_status
    def get_db(self):
        """
        """
        self.db.execute("""SELECT SCHEMA_NAME,DEFAULT_CHARACTER_SET_NAME,DEFAULT_COLLATION_NAME
            FROM INFORMATION_SCHEMA.SCHEMATA""")
        rows = self.db.fetchall()
        database_status = list()
        for row in rows:
            database_status.append(
                dict(zip(("SCHEMA_NAME","DEFAULT_CHARACTER_SET_NAME","DEFAULT_COLLATION_NAME"),
                    row)))
        return database_status
    def get_table(self):
        """
        """
        SQL = """SELECT TABLE_SCHEMA,TABLE_NAME,TABLE_TYPE,ENGINE,ROW_FORMAT,CREATE_TIME,UPDATE_TIME
        FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'"""
        table_status = list()
        self.db.execute(SQL)
        rows = self.db.fetchall()
        for row in rows:
            table_status.append(dict(zip(("TABLE_SCHEMA","TABLE_NAME","TABLE_TYPE","ENGINE","ROW_FORMAT","CREATE_TIME","UPDATE_TIME"), row)))
        return table_status
    def get_column(self):
        """
        """
        column_status = list()
        SQL = """SELECT TABLE_SCHEMA,TABLE_NAME,COLUMN_NAME,
            IS_NULLABLE,DATA_TYPE,CHARACTER_SET_NAME,COLLATION_NAME,COLUMN_TYPE
            FROM INFORMATION_SCHEMA.COLUMNS"""
        self.db.execute(SQL)
        rows = self.db.fetchall()
        for row in rows:
            column_status.append(dict(zip(("TABLE_SCHEMA","TABLE_NAME","COLUMN_NAME","IS_NULLABLE","DATA_TYPE","CHARACTER_SET_NAME","COLLATION_NAME","COLUMN_TYPE"),
                row)))
        return column_status

def main():
    db_info = DB_Info("192.168.2.30",3306,"root","Sunline")
    print db_info.get_status()
    print db_info.get_master()
    print db_info.get_slave()
    print db_info.get_db()
    print db_info.get_table()
    print db_info.get_column()

if __name__ == "__main__":
    main()
