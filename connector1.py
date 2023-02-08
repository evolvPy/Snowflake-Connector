#!/usr/bin/env python
import snowflake.connector
from snowflake.connector import ProgrammingError

# Create the connecotr
snow_conn_veggie = snowflake.connector.connect(
    user='gotuchintu',
    password='$Ummer234',
    account='zv64936.us-east-2.aws',
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
    one_row = snow_cur.fetchone() # For fetching one row
    allRow = snow_cur.fetchall() # For fetching all row
    print(one_row[0]) # For fetching the first column of the dataset
    print(allRow) # For fetching all the rows of the dataset
except ProgrammingError as err:
  print('Programming Error: {0}'.format(err))
finally:
    snow_cur.close() # Always close the cursor
snow_conn_veggie.close() # Always close the connection
