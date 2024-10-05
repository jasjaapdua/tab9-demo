import psycopg2
from dev_config import (
    db_host,
    db_name,
    db_port,
    db_password,
    db_username,
)


# Connect to the PostgreSQL database
connection = psycopg2.connect(
    dbname=db_name,
    user=db_username,
    password=db_password,
    host=db_host,
    port=db_port
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create the "tab9-demo" schema
create_schema_query = "CREATE SCHEMA IF NOT EXISTS tab9_demo;"
cursor.execute(create_schema_query)

# Commit the changes and close the connection
connection.commit()
cursor.close()
connection.close()

print("Schema 'tab9-demo' created successfully.")
