import os
import pandas as pd

def addDate(file_path, outp):
    try:
        date_str = os.path.basename(file_path).split('_')[0] 
        df = pd.read_csv(file_path)
        df['Date'] = date_str
        df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')
        os.makedirs(outp, exist_ok=True)
        base = os.path.basename(file_path)
        newFile= os.path.join(outp, base.replace('.csv', '_w_date.csv'))
        df.to_csv(newFile, index=False)
        print("Date added to CSV successfully!")
    except Exception as e:
        print(f"messed up {file_path}: {e}")
    

def walk_dir(directory, output_directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                addDate(file_path, output_directory)
input_directory = '/home/calvin/Documents/AppState/Data_With_Python/Project/Veritasium/csvFiles'
output_directory = '/home/calvin/Documents/AppState/Data_With_Python/Project/Veritasium/date'
walk_dir(input_directory, output_directory)
