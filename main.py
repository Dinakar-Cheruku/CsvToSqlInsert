import csv

# Function to read CSV file and generate SQL INSERT statements
# Replace 'path/to/your/file.csv' with the actual path to your CSV file and 'your_table_name' with the name of your database table. This script assumes that the CSV file has a header row, and it uses the header row to generate the column names in the SQL INSERT statement.
def csv_to_sql_insert(csv_file, table_name):
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # assuming the first row is the header

        insert_statements = []

        for row in csv_reader:
            values = ", ".join(f"'{value}'" for value in row)
            insert_statement = f"INSERT INTO {table_name} ({', '.join(header)}) VALUES ({values});"
            insert_statements.append(insert_statement)

    return insert_statements

# Example usage
csv_file_path = 'path/to/your/file.csv'
table_name = 'your_table_name'

insert_scripts = csv_to_sql_insert(csv_file_path, table_name)

# Print or save the generated SQL INSERT statements
for script in insert_scripts:
    print(script)
