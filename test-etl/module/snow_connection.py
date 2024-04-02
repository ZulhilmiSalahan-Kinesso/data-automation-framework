from enum import Enum

import snowflake.connector

from cryptography.hazmat.primitives.serialization import load_pem_private_key

from module.config import Config

config = Config()


class SNOW_DB(Enum):
    SNOWFLAKE_WAREHOUSE = 'SNOWFLAKE_WAREHOUSE'


class SnowConnection:
    def __init__(self):
        self.conn = None
        self.df = None
        self.USER = None
        self.ACCOUNT = None
        self.WAREHOUSE = None
        self.DATABASE = None
        self.SCHEMA = None
        self.PRIVATE_KEY = None

    def get_config(self, section: SNOW_DB = SNOW_DB.SNOWFLAKE_WAREHOUSE):
        SNOWFLAKE_CONFIG = config.get_config(section.value)
        self.USER = SNOWFLAKE_CONFIG['USER']
        self.ACCOUNT = SNOWFLAKE_CONFIG['ACCOUNT']
        self.WAREHOUSE = SNOWFLAKE_CONFIG['WAREHOUSE']
        self.DATABASE = SNOWFLAKE_CONFIG['DATABASE']
        self.SCHEMA = SNOWFLAKE_CONFIG['SCHEMA']
        PRIVATE_KEY_STRING = f"""
-----BEGIN PRIVATE KEY-----
{SNOWFLAKE_CONFIG['PRIVATE_KEY']}
-----END PRIVATE KEY-----
"""
        self.PRIVATE_KEY = self.convert_private_key_string_to_rsa_private_key(PRIVATE_KEY_STRING)
        return self

    def convert_private_key_string_to_rsa_private_key(self, private_key_string):
        private_key_bytes = private_key_string.encode('utf-8')
        private_key = load_pem_private_key(private_key_bytes, password=None)
        return private_key

    def get_connection(self, database=None):
        return snowflake.connector.connect(
            account=self.ACCOUNT,
            user=self.USER,
            private_key=self.PRIVATE_KEY,
            warehouse=self.WAREHOUSE,
            database=self.DATABASE,
            schema=self.SCHEMA
        )

    def execute(self, query: str):
        self.print_query(query)
        self.df = self.get_connection().cursor().execute(query).fetch_pandas_all()
        return self.df

    def get_query_result(self):
        print("\n" + ("#" * 25) + " RESULT " + "#" * 25)
        print(self.df)
        print("#" * 56)
        return self.df

    def get_row_count(self):
        return self.get_query_result().ROW_COUNT[0]

    def print_query(self, query):
        print("\n" + ("#" * 30) + " QUERY " + "#" * 30)
        print(query)
        print("#" * 75)
        return self
