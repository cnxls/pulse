DROP SCHEMA IF EXISTS raw, features, metrics CASCADE;
CREATE SCHEMA raw;
CREATE SCHEMA features;
CREATE SCHEMA metrics;

CREATE TABLE raw.members ( 
    msno TEXT PRIMARY KEY,
    city INT,
    bd INT,
    gender TEXT,
    registered_via INT,
    registration_init_time INT
); 

CREATE TABLE raw.train (
    msno TEXT PRIMARY KEY, 
    is_churn boolean
);

CREATE TABLE raw.transactions (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    msno TEXT NOT NULL,
    payment_method_id INT,
    payment_plan_days INT,
    plan_list_price INT,
    actual_amount_paid INT,
    is_auto_renew BOOLEAN,
    transaction_date INT,
    membership_expire_date INT,
    is_cancel BOOLEAN
);
