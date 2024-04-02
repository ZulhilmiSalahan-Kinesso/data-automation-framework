import pytest

from module.sql_connection import SQLConnection, MSSQL_DB


def test_connection():
    conn = SQLConnection().get_config()
    conn.execute('SELECT 1')
    conn.get_query_result()
