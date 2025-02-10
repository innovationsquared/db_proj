import os
import pandas as pd

csv_directory = '/home/calvin/Documents/AppState/Data_With_Python/Project/vsauce/csvFiles'

dataframe = []

for filename in os.listdir(csv_directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(csv_directory, filename)
        df = pd.read_csv(file_path)
        df['filename'] = filename.replace('.csv', '')
        dataframe.append(df)

combined_dataframe = pd.concat(df_list, ignore_index=True)
combined_df.to_csv('/home/calvin/Documents/AppState/Data_With_Python/Project/vsauce/csvFiles/combined.csv', index=False)

