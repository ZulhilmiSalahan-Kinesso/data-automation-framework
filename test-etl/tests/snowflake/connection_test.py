import pytest

from module.snow_connection import SnowConnection, SNOW_DB


def test_connection():
    conn = SnowConnection().get_config()
    conn.execute('SELECT 1')
    conn.get_query_result()
