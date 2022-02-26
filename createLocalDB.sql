CREATE TABLE transactions (
    transaction_ID INTEGER PRIMARY KEY,
    customer_first_name TEXT NOT NULL ,
    customer_last_name TEXT NOT NULL,
    flight_number TEXT not null,
    flight_delay_amt NUMERIC NOT NULL,
    datetime_departure TEXT NOT NULL ,
    calculated_payout NUMERIC NOT NULL,
    customer_id INTEGER NOT NULL

);


CREATE TABLE wallet  (
    customer_id INTEGER PRIMARY KEY,
    dollar_amount NUMERIC NOT NULL,
    transactionID INTEGER NOT NULL


);