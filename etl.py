import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    The function execute the query that is in each element of the copy_table_queries list,
    which is to copy the defined dataset.
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    The function execute the query that is in each element of the insert_table_queries list,
    which is to insert some data to a specific table.
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    The function read the variables in the dwh.cfg file,
    make the connection to the cluster and then, invoke the load staging and insert tables functions.
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
