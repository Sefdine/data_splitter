# Model

# Import necessary packages
from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, Float, Date, text, inspect, UniqueConstraint
from sqlalchemy.orm import sessionmaker, declarative_base
from includes.helpers import class_name, yes_or_no
from config.conf import *
import pandas as pd


def handle_database(db_df):
    # Connection string for master db
    master_connection_string = f'mssql+pyodbc://{username}:{password}@{server_address}/{database_name}?driver={driver}&Encrypt=No'

    # Engine for master
    master_engine = create_engine(master_connection_string)

        # Transform date type
    db_df['Order_Date'] = pd.to_datetime(db_df['Order_Date'], dayfirst=True)
    db_df['Ship_Date'] = pd.to_datetime(db_df['Ship_Date'], dayfirst=True)

        # Create master session
    MasterSession = sessionmaker(bind=master_engine)
    master_session = MasterSession()

    # Retrieve existing databases
    get_db_query = 'name FROM sys.databases;'

    result = master_session.query(text(get_db_query)).all()

    # Get user database
    user_db = input('Enter the database name : ')

    db_exist = any(row[0] == user_db for row in result)

    if not db_exist:
        print('The database doesn\'t exist. Do you want to create it ?')
        create_db_answer = input('Enter 1 for yes 0 for no : ')
        create_db_answer = yes_or_no(create_db_answer)
        if create_db_answer == '1':
            print('Creation of database ',user_db)
            master_session.execute(f'CREATE DATABASE {user_db}')
        else: 
            print('Do you want to save your data in the master database ?')
            master_save_answer = input('Enter 1 for yes 0 for no : ')
            master_save_answer = yes_or_no(master_save_answer)

            if master_save_answer == '0':
                print('See you again.')
            else:
                create_table(db_df, master_engine)
    else:
        master_session.close()
        master_engine.dispose()
        # Connection string for user_db db
        user_db_connection_string = f'mssql+pyodbc://{username}:{password}@{server_address}/{user_db}?driver={driver}&Encrypt=No'
        user_engine = create_engine(user_db_connection_string)

        print('Connection to ',user_db,'database passed successfully')
        


def create_table(db_df, engine):
    print(' ---------- Table creation ---------')

    # Create a declarative base
    Base = declarative_base()

    # Create table
    class_name = class_name(input_csv_file)
    class class_name:
        __tablename__ = class_name

        # Columns
        id = Column(Integer, primary_key=True, autoincrement=True)
        row_id = Column(Integer, nullable=False)
        order_id = Column(String(), nullable=False)
        order_date = Column(Date, nullable=False)
        ship_mode = Column(String(), nullable=False)
        customer_id = Column(String(50), nullable=False)
        customer_name = Column(String(), nullable=False)
        segment = Column(String(50), nullable=False)
        country = Column(String(), nullable=False)
        city = Column(String(), nullable=False)
        state = Column(String(), nullable=False)
        postal_code = Column(Float, nullable=True)
        region = Column(String(), nullable=False)
        product_id = Column(String(50), nullable=False)
        category = Column(String(50), nullable=False)
        sub_category = Column(String(50), nullable=False)
        product_name = Column(String(), nullable=False)
        sales = Column(Float, nullable=False)
    Base.metadata.create_all(engine)

    inspector = inspect(engine)

    table_names = inspector.get_table_names()
    print(table_names)