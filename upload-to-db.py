import os 
import psycopg2
import pandas as pd 
import configparser 

config = configparser.ConfigParser()
config.read('config.ini')

DATABASE_CREDS = config['Database']

connection = psycopg2.connect(
    host=DATABASE_CREDS['HOST'], 
    database=DATABASE_CREDS['DATABASE'], 
    user=DATABASE_CREDS['USER'], 
    password=DATABASE_CREDS['PASSWORD']
)
cursor = connection.cursor()
connection.autocommit = True


try:
    for file in os.listdir('data'):
        if '.csv' in file:
            sales = pd.read_csv(f'data/{file}')
            for i, row in sales.iterrows():
                query = f"insert into s{file[:3]} values (\
                    '{row['doc_id']}', '{row['item']}', '{row['category']}',\
                        '{row['price']}', '{row['amount']}', '{row['discount']}')"
                cursor.execute(query)
except Exception as e:
    print(f'Something went wrong. {e}')
finally:
    connection.close()
    cursor.close()