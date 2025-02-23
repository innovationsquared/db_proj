import os
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def add_sentiment(file_path, output_dir):
    try:
        df = pd.read_csv(file_path)
        if 'Text' in df.columns:
            df['sentiment-score'] = df['Text'].apply(lambda x: analyzer.polarity_scores(str(x))['compound'])
            os.makedirs(output_dir, exist_ok=True)
            base_file = os.path.basename(file_path)
            new_file_path = os.path.join(output_dir, base_file.replace('.csv', '_w_sentiment.csv'))
            df.to_csv(new_file_path, index=False)
            print(f"Processed file for {file_path}")
        else: 
            print(f"Error with {file_path} text column.")
    except Exception as e:
        print(f"Major error with {file_path}: {e}")

def walk_dir(directory, output_directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                add_sentiment(file_path, output_directory)
input_directory = '/home/calvin/Documents/AppState/Data_With_Python/Project/Vsauce/csvFiles/'
output_directory = '/home/calvin/Documents/AppState/Data_With_Python/Project/Vsauce/csvFiles2/'

walk_dir(input_directory, output_directory)