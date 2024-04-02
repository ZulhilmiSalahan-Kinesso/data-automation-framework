import pandas as pd
import sqlalchemy as sa
from sqlalchemy.engine import URL
from module.config import Config

config = Config()

from enum import Enum


class MSSQL_DB(Enum):
    MSSQL_DB = 'MSSQL_DB'


class SQLConnection:
    def __init__(self):
        self.df = None
        self.DB_PASS = None
        self.DB_USER = None
        self.SQL_HOST = None
        self.DATABASE_NAME = None
        self.DRIVER_NAME = None

    def get_config(self, section: MSSQL_DB = MSSQL_DB.DB):
        MSSQL_CONFIG = config.get_config(section.value)
        self.DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
        self.DATABASE_NAME = MSSQL_CONFIG['DATABASE']
        self.SQL_HOST = MSSQL_CONFIG['SQL_HOST']
        self.DB_USER = MSSQL_CONFIG['DB_USER']
        self.DB_PASS = MSSQL_CONFIG['DB_PASS']
        return self

    def get_connection(self, database=None):
        database = database or self.DATABASE_NAME
        connection_string = f"DRIVER={{{self.DRIVER_NAME}}};SERVER={self.SQL_HOST};DATABASE={database};UID={self.DB_USER};PWD={self.DB_PASS}"
        resolved_conn_string = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
        return sa.create_engine(resolved_conn_string)

    def execute(self, query: str, database: str = None):
        with self.get_connection(database).begin() as conn:
            self.print_query(query)
            self.df = pd.read_sql(query, conn)
        return self.df

    def get_query_result(self):
        self.print_result()
        return self.df

    def get_query_result_column(self, column_name):
        print("\n" + ("#" * 30) + f" RESULT: {column_name} " + "#" * 30)
        print(self.df[column_name])
        print("#" * 75)
        return self.df[column_name]

    def get_row_count(self):
        print("\n" + ("#" * 30) + " ROW_COUNT " + "#" * 30)
        print(self.df.ROW_COUNT[0])
        print("#" * 75)
        return self.df.ROW_COUNT[0]

    def print_query(self, query):
        print("\n" + ("#" * 30) + " QUERY " + "#" * 30)
        print(query)
        print("#" * 75)
        return self

    def print_result(self):
        print("\n" + ("#" * 30) + " RESULT " + "#" * 30)
        print(self.df)
        print("#" * 75)
