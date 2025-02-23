import os
import pandas as pd

def count_words(file_path):
    try:
        df = pd.read_csv(file_path)
        if 'Text' in df.columns:
            df['word_count'] = df['Text'].str.lower().str.replace('[^\w\s]', '',regex=True)
            new_df = df.word_count.str.split(expand=True).stack().value_counts().reset_index()
            new_df.columns = ['Word', 'Frequency']
            return new_df
        else:
            print(f"Error with {file_path}")
            return None
    except Exception as e:
        print(f"Major fuckup at {file_path}: {e}")
        return None

def crawl_dir(directory, out_directory):
    all_words = pd.DataFrame(columns=['Word', 'Frequency'])
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file) 
                counts = count_words(file_path)
                if counts is not None:
                    all_words = pd.concat([all_words,  counts])
    all_words = all_words.groupby('Word', as_index=False).sum()
    all_words = all_words.sort_values(by='Frequency', ascending=False)
    all_words.to_csv(out_directory, index=False)
    print(f"Saved word count to {out_directory}")

directory = '/home/calvin/Documents/AppState/Data_With_Python/Project/Vsauce/csvFiles' 
out_directory = 'word_counts.csv'
crawl_dir(directory, out_directory)
