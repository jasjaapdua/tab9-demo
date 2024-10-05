import psycopg2

# Replace these values with your own database credentials
db_name = "your_database_name"
db_user = "your_database_user"
db_password = "your_database_password"
db_host = "your_database_host"
db_port = "your_database_port"

# Connect to the PostgreSQL database
connection = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create the "products" table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    quantity INTEGER NOT NULL
);
"""
cursor.execute(create_table_query)

# Prompt the user to enter product details
product_name = input("Enter product name: ")
product_price = float(input("Enter product price: "))
product_quantity = int(input("Enter product quantity: "))

# Insert the product into the "products" table
insert_query = """
INSERT INTO products (name, price, quantity)
VALUES (%s, %s, %s);
"""
cursor.execute(insert_query, (product_name, product_price, product_quantity))

# Commit the changes and close the connection
connection.commit()
cursor.close()
connection.close()

print("Product added successfully.")