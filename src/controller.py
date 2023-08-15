# Controller

# Import packages
from src.model import *
from config.conf import *
from includes.helpers import is_not_number
import sys
import time

def control():
    while True:
        try:
            input_csv_file = input('Enter the name of the csv file : ')
            df = pd.read_csv(input_csv_file, encoding="ISO-8859-1")
            if df.shape[0]:
                break
            else:
                print('The file mentionned doesn\'t exist')
        except:
            print('The file mentionned doesn\'t exist')

    handle_database(df)
    sys.exit(0)

    print (df.shape)

    # Shuffle the data
    # Randomly shuffle the rows in the dataframe 
    shuffled_df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    # Number of lines for json
    json_percent = (input('Enter the JSON percentage : '))
    json_percent = 30 if is_not_number(json_percent) else float(json_percent)
    line_json = int((shuffled_df.shape[0] * json_percent) / 100)

    # Number of lines for csv
    csv_percent = (input('Enter the CSV percentage : '))
    csv_percent = 40 if is_not_number(csv_percent) else float(csv_percent)
    line_csv = int((shuffled_df.shape[0] * csv_percent) / 100)

    # Number of lines for database
    db_percent = (input('Enter the database percentage : '))
    db_percent = 30 if is_not_number(db_percent) else float(db_percent)
    line_db = int((shuffled_df.shape[0] * db_percent) / 100)

    print('There will be ',line_json,' rows for the json file')
    print('There will be ',line_csv,' rows for the csv file')
    print('There will be ',line_db,' rows for the database')

    print('Creating files......')
    time.sleep(1)

    # ---------- JSON --------- #
    # Take 30% to json
    json_df = shuffled_df[:line_json]

    # Delete the json df from the shuffled
    shuffled_df.drop(json_df.index, axis='rows', inplace=True)

    # Create json file
    json_df.reset_index(drop=True).to_json('json_file.json')
    print('JSON file created successfully')

    # ---------- CSV --------- #
    # 40% for CSV
    csv_df = shuffled_df[:line_csv]

    # Delete the csv df to the shuffle
    shuffled_df.drop(csv_df.index, axis='rows', inplace=True)

    # Create the csv file
    csv_df.reset_index(drop=True).to_csv('csv_file.csv', index=False, header=False)
    print('CSV file created successfully')

    # --------- DATABASE --------- #
    # 30% for DB
    db_df = shuffled_df[:line_db]

    # Delete the csv df to the shuffle
    shuffled_df.drop(db_df.index, axis='rows', inplace=True)
    print('Connection to database...')

    handle_database(db_df)