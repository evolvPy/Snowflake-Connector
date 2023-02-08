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
    snow_cur.execute("select * from VEGETABLE_DETAILS")
    for (col1, col2) in snow_cur:
            print('{0}, {1}'.format(col1, col2))
except ProgrammingError as err:
  print('Programming Error: {0}'.format(err))
finally:
    snow_cur.close() # Always close the cursor
snow_conn_veggie.close() # Always close the connection
