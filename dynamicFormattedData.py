#!/usr/bin/env python
import snowflake.connector
from snowflake.connector import ProgrammingError

# Create the connecotr
snow_conn_veggie = snowflake.connector.connect(
    user='X',
    password='X',
    account='X',
    warehouse='compute_wh',
    database='GARDEN_PLANTS',
    schema='VEGGIES',
    session_parameters={
        'QUERY_TAG': 'Demo',
        'AUTOCOMMIT' : 'TRUE'
    }
)
snow_cur = snow_conn_veggie.cursor()

try:
    # To get the column count
    tup_col_count = snow_cur.execute("Select count(column_name) from \
        INFORMATION_SCHEMA.columns where table_name='VEGETABLE_DETAILS'").fetchall()
    colCount = int(tup_col_count[0][0])
    results = snow_cur.execute("select * from VEGETABLE_DETAILS").fetchall()
    for rec in results:
        recLine = ''
        for i in range (0,colCount):
            recLine += rec[i] + '|' # Putting a delimeter
        recLine = recLine[:-1]
        print (recLine)
except ProgrammingError as err:
  print('Programming Error: {0}'.format(err))
finally:
    snow_cur.close() # Always close the cursor
snow_conn_veggie.close() # Always close the connection
