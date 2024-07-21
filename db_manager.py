import sqlite3
from datetime import datetime

import sqlite3
from datetime import datetime

class ProductRecords:
    def __init__(self, db_name="productrecords.sql"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS products (
            product_name TEXT,
            barcode TEXT,
            purchase_price REAL,
            selling_price REAL,
            piece INTEGER,
            unit TEXT,
            time TEXT,
            date TEXT,
            user TEXT,
            process_type TEXT,
            customer TEXT,
            payment_status TEXT
        )''')
        self.conn.commit()

    def add(self, product_name, barcode, purchase_price, selling_price, piece, unit, user, process_type, customer, payment_status):
        now = datetime.now()
        time = now.strftime("%H:%M")
        date = now.strftime("%d/%m/%Y")
        self.cursor.execute('''INSERT INTO products (
            product_name, barcode, purchase_price, selling_price, piece, unit, time, date, user, process_type, customer, payment_status
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
        (product_name, barcode, float(purchase_price), float(selling_price), int(piece), unit, time, date, user, process_type, customer, payment_status))
        self.conn.commit()

    def get_stock(self, identifier):
        self.cursor.execute('''SELECT SUM(piece) FROM products WHERE product_name=? OR barcode=?''', (identifier, identifier))
        result = self.cursor.fetchone()
        return result[0] if result else 0

    def get_customer(self, customer):
        self.cursor.execute('''SELECT * FROM products WHERE customer=?''', (customer,))
        return self.cursor.fetchall()
    def get_product(self, product):
        self.cursor.execute('''SELECT * FROM products WHERE product_name=?''', (product,))
        return self.cursor.fetchall()
    def get_barcode(self, barcode):
        self.cursor.execute('''SELECT * FROM products WHERE barcode=?''', (barcode,))
        return self.cursor.fetchall()

    def get_min_data(self, identifier):
        self.cursor.execute('''SELECT * FROM products WHERE product_name=? OR barcode=? ORDER BY ROWID DESC LIMIT 1''', (identifier, identifier))
        result = self.cursor.fetchone()
        if result:
            return {
                "product_name": result[0],
                "barcode": result[1],
                "purchase_price": result[2],
                "selling_price": result[3],
                "piece": result[4],
                "unit": result[5],
                "time": result[6],
                "date": result[7],
                "user": result[8],
                "process_type": result[9],
                "customer": result[10],
                "payment_status": result[11]
            }
        return None

    def get_table(self):
        self.cursor.execute('SELECT * FROM products')
        return self.cursor.fetchall()

    def delete_row(self, row_id):
        self.cursor.execute('DELETE FROM products WHERE ROWID=?', (row_id,))
        self.conn.commit()

    def find(self, column, value):
        query = f'SELECT * FROM products WHERE {column}=?'
        self.cursor.execute(query, (value,))
        return self.cursor.fetchall()

    def get_unique_product_names(self):
        self.cursor.execute('SELECT DISTINCT product_name FROM products')
        return [row[0] for row in self.cursor.fetchall()]
    def get_unique_product_units(self):
        self.cursor.execute('SELECT DISTINCT unit FROM products')
        return [row[0] for row in self.cursor.fetchall()]
    def get_numerate_table(self):
        list_=self.get_table()
        return [(i + 1,) + list_[i] for i in range(len(list_))]
    def get_numerate(self,list_):
        return [(i + 1,) + list_[i] for i in range(len(list_))]
class PasswordManager:
    def __init__(self):
        self.file_name = "AccessData.sql"
        self.connect()
        self.create_table()
        if self.find_data("main") is None:
            self.insert_data("main","main")
            print(self.find_data("main"))

    def connect(self):
        self.connection = sqlite3.connect(self.file_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Data(
                number INTEGER PRIMARY KEY,
                name TEXT UNIQUE,
                password TEXT
            )
        ''')
        self.connection.commit()

    def list_name(self):
        self.cursor.execute("SELECT name FROM Data")
        return self.cursor.fetchall()
    def insert_data(self, name, password):
        #id_name = self.generate_unique_id_name(id_name)
        self.cursor.execute('''
            INSERT INTO Data (name,password)
            VALUES (?, ?)
        ''', (name,password))
        self.connection.commit()
        print(f"Inserted data with name: {name}")

    def delete_data(self, name):
        self.cursor.execute('''
            DELETE FROM Data WHERE name=?
        ''', (name,))
        self.connection.commit()

    def find_data(self, name):
        try:
            self.cursor.execute('''
                SELECT * FROM Data WHERE name=?
            ''', (name,))
            return self.cursor.fetchone()
        except:
            return None

    def close_connection(self):
        self.connection.close()
    



# Usage example
if __name__ == "__main__":
    db = ProductRecords()

    # Adding 25 complex records
    records = [
        ('tadelle', '902349304234', 10, 20, 2000, 'kutu', 'yavuzhan', 'ürün_alımı', 'can', 'nakit'),
        ('biskrem', '902306304234', 12, 14, 50000, 'adet', 'mehmet', 'ürün_alımı', 'selim', 'yarısı nakit'),
        ('coca cola', '8690645010212', 3, 5, 10000, 'şişe', 'ayşe', 'ürün_satışı', 'ahmet', 'kredi kartı'),
        ('pepsi', '8714789650123', 2.5, 4.5, 1000, 'şişe', 'ali', 'ürün_satışı', 'veli', 'nakit'),
        ('fanta', '8690645010223', 3, 5, 12000, 'şişe', 'cem', 'ürün_alımı', 'kemal', 'nakit'),
        ('ulker cikolata', '8690343034321', 5, 8, 8000, 'kutu', 'melis', 'ürün_satışı', 'deniz', 'havale'),
        ('snickers', '5000159440025', 2, 3.5, 6000, 'adet', 'hakan', 'ürün_alımı', 'elif', 'kredi kartı'),
        ('nestle', '7613035339635', 4, 6, 700, 'adet', 'levent', 'ürün_satışı', 'hasan', 'nakit'),
        ('milka', '7622200012366', 4.5, 7, 6500, 'kutu', 'gizem', 'ürün_alımı', 'burak', 'havale'),
        ('dore', '7622300000012', 3.5, 5.5, 10000, 'adet', 'taner', 'ürün_satışı', 'mert', 'kredi kartı'),
        ('torku', '8690123456789', 3, 5, 9000, 'adet', 'can', 'ürün_alımı', 'buse', 'nakit'),
        ('eti', '8690100000001', 4, 6, 12000, 'kutu', 'selin', 'ürün_satışı', 'dilara', 'havale'),
        ('pringles', '5028881039250', 7, 10, 4000, 'kutu', 'kadir', 'ürün_alımı', 'kerem', 'kredi kartı'),
        ('lays', '8719200082842', 5, 8, 7000, 'kutu', 'ferhat', 'ürün_satışı', 'ozan', 'nakit'),
        ('doritos', '8714789642023', 6, 9, 9000, 'kutu', 'ozlem', 'ürün_alımı', 'metin', 'havale'),
        ('ruffles', '8714789624021', 5, 8, 6000, 'kutu', 'selim', 'ürün_satışı', 'erol', 'kredi kartı'),
        ('albeni', '8690343000001', 2.5, 4, 10000, 'adet', 'fatih', 'ürün_alımı', 'ayşe', 'nakit'),
        ('bebeto', '8690343000012', 3, 5, 1000, 'adet', 'serkan', 'ürün_satışı', 'can', 'havale'),
        ('tadelle', '902349304234', 10, 20, 1000, 'kutu', 'yavuzhan', 'ürün_alımı', 'can', 'nakit'),
        ('biskrem', '902306304234', 12, 14, 50000, 'adet', 'mehmet', 'ürün_alımı', 'selim', 'yarısı nakit'),
        ('coca cola', '8690645010212', 3, 5, 30000, 'şişe', 'ayşe', 'ürün_satışı', 'ahmet', 'kredi kartı'),
        ('pepsi', '8714789650123', 2.5, 4.5, 15000, 'şişe', 'ali', 'ürün_satışı', 'veli', 'nakit'),
        ('haribo', '4001686300321', 4, 6, 9000, 'adet', 'sinem', 'ürün_alımı', 'mehmet', 'kredi kartı'),
        ('danone', '7613035339646', 2, 3.5, 7000, 'kutu', 'yigit', 'ürün_satışı', 'sevgi', 'nakit'),
        ('lindt', '7610400012345', 5, 8, 6000, 'kutu', 'dilan', 'ürün_alımı', 'salih', 'havale'),
        ('godiva', '0312901234567', 10, 15, -3000, 'kutu', 'muharrem', 'ürün_satışı', 'emre', 'kredi kartı'),
        ('ulker biskrem', '8690123456790', 4, 6, 8000, 'adet', 'hulya', 'ürün_alımı', 'furkan', 'nakit'),
        ('nutella', '8000500029124', 15, 20, 2000, 'kutu', 'kenan', 'ürün_satışı', 'emine', 'havale'),
        ('pınar süt', '8690526012345', 2, 3, 12000, 'litre', 'burcu', 'ürün_alımı', 'yasemin', 'kredi kartı')
    ]

    for record in records:
        db.add(*record)

    # Display the entire tabl

    stock_tadelle = db.get_stock('tadelle')
    print(f'Stock for "tadelle": {stock_tadelle}')

    # Get customer records for 'can'
    customer_can = db.get_customer('can')
    print('Records for customer "can":')
    for record in customer_can:
        print(record)

    # Get the most recent data entry for 'tadelle'
    min_data_tadelle = db.get_min_data('tadelle')
    print('Most recent entry for "tadelle":')
    print(min_data_tadelle)

    # Display the entire table
    print('Entire table:')
    all_records = db.get_table()
    for record in all_records:
        print(record)

    # Delete a row by id (e.g., id=1)
    db.delete_row(1)
    print('Table after deleting row with id=1:')
    all_records_after_deletion = db.get_table()
    for record in all_records_after_deletion:
        print(record)
    print(f"\n\nall name:{db.get_unique_product_names()}")
    # Find records where product_name is 'tadelle'
    found_records = db.find('product_name', 'tadelle')
    print('Records with product_name "tadelle":')
    for record in found_records:
        print(record)