import sqlite3

class Database:

    tables = {}

    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
    
    def create_table(self, new_table, table_name):
        self.cursor.execute(new_table)
        tables[table_name] = new_table
        self.connection.commit()

    def display_table(self, table_name):
        self.cursor.execute(f'SELECT * FROM {table_name}')

    def insert(self, record, table_name):
        new_record = f'INSERT INTO {tables[table_name]} VALUES {record}'
        self.cursor.execute(new_record)
        self.connection.commit()

    def delete(self, record, table_name):
        delete_record = f'DELETE FROM {table_name} WHERE'
        self.cursor.execute(delete_record)
        self.connection.commit()

    def close(self):
        self.connection.close()
