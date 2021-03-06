import sqlite3
import random


class Database(object):
    """sqlite3 database class that holds testers jobs"""
    DB_LOCATION = "wallet.sqlite"

    def __init__(self, db_location=None):
        """Initialize db class variables"""
        if db_location is not None:
            self.connection = sqlite3.connect(db_location)
        else:
            self.connection = sqlite3.connect(self.DB_LOCATION)
        self.cur = self.connection.cursor()


def generate_transaction_number():
    db = Database()
    query = '''SELECT transaction_ID from transactions;'''
    query_result = db.cur.execute(query)
    transaction_ids = []
    for row in query_result:
        transaction_ids.append(row[0])
    m = 100000000
    transaction_num = random.choice([x for x in range(m) if x not in transaction_ids])
    return transaction_num


def generate_customer_ID():
    db = Database()
    query = '''SELECT customer_id from transactions;'''
    query_result = db.cur.execute(query)
    # db.connection.commit()
    # db.connection.row_factory = sqlite3.Row
    customer_id = []
    for row in query_result:
        customer_id.append(row[0])
    m = 100000000
    customer_num = random.choice([x for x in range(m) if x not in customer_id])
    return customer_num


def write_customer(transaction_id, first, last, wallet_total, wallet_change, flight_number, flight_delay,
                   calculated_payout, customer_id):
    db = Database()

    db.cur.execute('''INSERT INTO transactions (transaction_ID, customer_first_name, customer_last_name,
                          wallet_total, wallet_change, flight_number, flight_delay_amt,
                           calculated_payout, customer_id)
                          VALUES (?,?,?,?,?,?,?,?,?);''', (
        transaction_id, first, last, wallet_total, wallet_change, flight_number, flight_delay, calculated_payout,
        customer_id))
    db.connection.commit()
    # # db.connection.row_factory = sqlite3.Row
    # customer_id = []
    # for row in query_result:
    #     customer_id.append(row[0])
    # m = max(customer_id)
    # customer_num = random.choice([x for x in range(m) if x not in customer_id])
    # return customer_num


def get_wallet_amount():
    db = Database()
    query = '''SELECT dollar_amount from wallet where customer_id = (SELECT MAX(customer_id) FROM wallet);'''
    query_result = db.cur.execute(query)
    transaction_ids = []
    for row in query_result:
        transaction_ids.append(row[0])
    wallet_amount = transaction_ids[0]
    return wallet_amount


def calculate_payout(delay_time):
    payout = 75
    if delay_time <= 30:
        return 0
    else:
        return payout


def get_wallet_change(payout):
    new_value = get_wallet_amount() - payout
    return new_value


def update_insurance_wallet(dollar_amount, transactionID):
    db = Database()
    db.cur.execute('''insert into wallet ( dollar_amount, transactionID)
                    VALUES ( ?, ?);''', (dollar_amount, transactionID))
    db.connection.commit()


