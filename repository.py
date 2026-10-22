'''
database scheme
categories
- id: primary key.
- name: wajib diisi dan tidak boleh kosong.
- type: hanya income atau expense.
- Kombinasi nama dan tipe kategori tidak boleh duplikat.
transactions
- id: primary key dengan AUTOINCREMENT.
- date: tanggal transaksi dengan format ISO.
- type: hanya income atau expense.
- category_id: foreign key ke categories.
- amount: integer positif.
- note: boleh NULL.
budgets
- id: primary key dengan AUTOINCREMENT.
- category_id: foreign key ke kategori pengeluaran.
- period: periode berbentuk YYYY-MM.
- amount: integer positif.
- Kombinasi category_id dan period harus unik agar tidak ada dua budget bulanan untuk kategori yang sama.
'''

import sqlite3
from models import CategoryData, TransactionData, BudgetData, Category, Transaction, Budget
from contextlib import contextmanager

#for consistent transaction and resource management (i.e., commit, rollback, and connection close) using contextmanager as helper
#context manager:controls the setup and teardown of a resource around a block of code
# intuition: 
## Enter (__enter__ dunder) : pick up tool, turn on power, or open a storage locker
## Do : use the tool 
## Clean Up (__exit__ dunder) : tool put away, no matter if task complete successfully, halfway broken, etc
# helps consistenly manage connection in single helper, instead write try except block one by one
@contextmanager
def database_connection(db_name="database.db"):
    # Setup phase (Runs when entering the 'with' block)
    conn = sqlite3.connect(db_name)
    
    try:
    # IMPORTANT: Enable foreign key constraint support explicitly
    # This must be run on every new database connection.
        conn.execute("PRAGMA foreign_keys = ON;")
        
        #passes the resource to the 'as' target variable
        yield conn
        
        conn.commit()
    
    except Exception:
        conn.rollback()
        raise
    finally:
        # Teardown phase (Guaranteed to run when leaving the block)
        conn.close()
        

def initialize_database_table(db_name = "database.db"):
    
    with database_connection(db_name) as conn:

    # create transactions table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL CHECK (trim(name) <> ''),
            type TEXT NOT NULL CHECK (type IN ('income', 'expense')),
            UNIQUE (name, type)
            );
                        ''')

        # create transactions table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS transactions ( 
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date DATE NOT NULL,
                type TEXT NOT NULL 
                CHECK (type IN ('income', 'expense')),
                category_id INT NOT NULL,
                amount INTEGER NOT NULL CHECK (amount > 0),
                note TEXT,
                FOREIGN KEY (category_id) REFERENCES categories(id)

            )
                        ''') #foreign key definition should put at the last of the parameter query

        # create budget table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS budgets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                period TEXT NOT NULL,
                category_id INTEGER NOT NULL,
                amount INTEGER NOT NULL CHECK (amount > 0),
                UNIQUE (category_id, period),
                FOREIGN KEY (category_id) REFERENCES categories(id)

            )
                        ''')    

# CATEGORY SECTION
def create_category(category_object : CategoryData, db_name = "database.db"):
   
    with database_connection(db_name) as conn:        
        cursor = conn.execute('''
        INSERT INTO categories (name, type)
        VALUES (?,?)
        ON CONFLICT(name, type) DO NOTHING
        ''', (category_object.name,category_object.type))
        insert_success = cursor.rowcount == 1
        
        return insert_success
    

def get_category_by_id(category_id,db_name = "database.db"):
    with database_connection(db_name) as conn:
        #get category
        cursor = conn.execute("SELECT * FROM categories WHERE id =?",(category_id,))
        
        #get the category
        row = cursor.fetchone()
        
        if row is None:
            return None
    
    return Category(*row)

def list_category(db_name = "database.db"):
    with database_connection(db_name) as conn:
        #get category
        cursor = conn.execute("SELECT * FROM categories")
        
        #get the category
        list_category = []
        rows = cursor.fetchall()
        for row in rows:
            category_object = Category(*row)
            list_category.append(category_object)
        
        
        return list_category

def update_category_name(category_object : Category,db_name = "database.db"):
    with database_connection(db_name) as conn:
       cursor = conn.execute("""
                   UPDATE categories
                   SET name = ?
                   WHERE id = ?
               """, (category_object.name, category_object.id))
       update_success = cursor.rowcount == 1
       return update_success 
    
    
def delete_category(category_id,db_name = "database.db"):
    with database_connection(db_name) as conn:        
     #delete category if transaction and budget not using the category   
        cursor = conn.execute('''
        DELETE FROM categories
        WHERE id = ?
        AND NOT EXISTS (
            SELECT 1
            FROM transactions
            WHERE category_id = ?
        )
        AND NOT EXISTS (
            SELECT 1
            FROM budgets
            WHERE category_id = ?
        );
        ''', (category_id, category_id, category_id))
        
        delete_success = True if cursor.rowcount > 0 else False
        
        return delete_success


# TRANSACTION SECTION
def create_transaction(transaction_object : TransactionData,db_name = "database.db"):
    with database_connection(db_name) as conn:    
        cursor = conn.execute('''
        INSERT INTO transactions (date, type, category_id, amount, note)
        VALUES (?,?,?,?,?)
        ''', (transaction_object.date, transaction_object.type, 
            transaction_object.category_id, transaction_object.amount, transaction_object.note))
        
        inserted_id = cursor.lastrowid  
        
        return inserted_id

def get_transaction_by_id(transaction_id, db_name = "database.db"):
    with database_connection(db_name) as conn:
    #get category
        cursor = conn.execute("SELECT * FROM transactions WHERE id = ?", (transaction_id,))
        
        #get the transaction    
        row = cursor.fetchone()
        
        if row is None:
            return None
            
        return Transaction(*row)

def list_transaction(db_name = "database.db"):
    # connect database
    with database_connection(db_name) as conn:
    
        #get category
        cursor = conn.execute("SELECT * FROM transactions")
        
        #get the category
        list_transaction = []
        rows = cursor.fetchall()
        for row in rows:
            transaction_object = Transaction(*row)
            list_transaction.append(transaction_object)
        
        return list_transaction

def update_transaction(transaction : Transaction,db_name = "database.db"):
    with database_connection(db_name) as conn:    
        cursor = conn.execute('''
            UPDATE transactions
            SET date = ?, type =?, category_id=?, amount=?, note=?
            WHERE id = ?
            ''', (transaction.date, transaction.type, transaction.category_id, 
                transaction.amount, transaction.note, transaction.id)
            )
        update_success = True if cursor.rowcount > 0 else False
        
        return update_success

def delete_transaction(transaction_id,db_name = "database.db"):
    with database_connection(db_name) as conn:
        
        cursor = conn.execute('''
        DELETE FROM transactions
        WHERE id = ?
        ''', (transaction_id,)
        )
        
        delete_success = True if cursor.rowcount > 0 else False
        
        return delete_success
   

# BUDGET SECTION
def create_budget(budget_data: BudgetData,db_name = "database.db"):
    with database_connection(db_name) as conn:    
        cursor = conn.execute("""
            INSERT INTO budgets (category_id, period, amount)
            VALUES (?, ?, ?)
            ON CONFLICT(category_id, period) DO NOTHING
            """, (
                budget_data.category_id,
                budget_data.period,
                budget_data.amount
            ))
        
        insert_success = cursor.rowcount == 1
        
        return insert_success

def get_budget_by_id(budget_id, db_name = "database.db"):
    with database_connection(db_name) as conn:
        cursor = conn.execute("SELECT id, category_id, period, amount FROM budgets WHERE id = ?", (budget_id,))
        
        #get the budget
        budget_object = None
        row = cursor.fetchone()
        
        if row is None:
            return None
        
        return Budget(*row)

def list_budget(db_name = "database.db"):
    with database_connection(db_name) as conn:
        cursor = conn.execute("SELECT id, category_id, period, amount FROM budgets")        
        list_budget = []
        rows = cursor.fetchall()
        for row in rows:
            budget_object = Budget(*row)
            list_budget.append(budget_object)
             
        return list_budget    


def update_budget(budget_object : Budget,db_name = "database.db"):
    with database_connection(db_name) as conn:    
        cursor = conn.execute('''
        UPDATE budgets
        SET period = ?, category_id =?, amount=?
        WHERE id = ?
        ''', (budget_object.period, budget_object.category_id, budget_object.amount, budget_object.id)
        )
        update_success = True if cursor.rowcount > 0 else False
        return update_success
    
def delete_budget(budget_id,db_name = "database.db"):
    with database_connection(db_name) as conn:
        cursor = conn.execute('''
        DELETE FROM budgets
        WHERE id = ?
        ''', (budget_id,)
        )
        
        delete_success = True if cursor.rowcount > 0 else False
        
        return delete_success