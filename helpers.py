import numpy as np
import pandas as pd
import spacy
from collections import Counter
import nltk
from nltk import punkt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize



def compute_nan_count_and_percentage(df):
    for column_name in df.columns:
        nan_count = df[column_name].isna().sum()
        nan_percentage = df[column_name].isna().mean() * 100

        print(f"{column_name}: {nan_count} NaN values, which represents {nan_percentage:.2f} % of the column. \n")
        
        
def find_region(country_or_countries, regions):
    if isinstance(country_or_countries, list):
        # since the country is stored as a list and there might be multiple so we have to check them too
        for country in country_or_countries:
            for region, countries in regions.items():
                if country in countries:
                    return region
    return None

# Function to categorize movies based on the threshold for a specific event

def categorize_event(summary, event_dict, threshold):
    summary_words = set(word_tokenize(summary.lower()))
    common_words_count = len(set(event_dict) & summary_words)
    return common_words_count >= threshold


# Function to add columns to DataFrame based on event categories

def add_event_columns(df, dictionaries_df):
    # Iterate over each event in dictionaries_df and add a column to df
    for event, row in dictionaries_df.iterrows():
        event_words = row['dictionary']
        threshold = row['threshold']
        df[event] = df['summary'].apply(lambda x: categorize_event(x, event_words, threshold))
    return df

def create_events_belongs_to_column(df, event_columns):
    df['events_belongs_to'] = df.apply(
        lambda row: [event for event in event_columns if row[event]], axis=1
    )
    return df

# Function to add one column to DataFrame which will be filled by a list of genre categories 

def update_new_genre_column(df, genres_considered):
    df['new_genre'] = None

    for name, genre_list in genres_considered.items():
        mask = df['genre'].apply(lambda x: any(item in x for item in genre_list))
        df.loc[mask, 'new_genre'] = df.loc[mask, 'new_genre'].apply(lambda x: [] if x is None else x)
        df.loc[mask, 'new_genre'] = df.loc[mask, 'new_genre'].apply(lambda x: x + [name] if isinstance(x, list) else [name])

    return df

def count_genres_for_event(df, event_column):
    # Explode the 'new_genre' column
    df_expanded = df.copy()
    df_expanded = df_expanded.explode('new_genre')
    
    # Filter rows where the event_column is True
    filtered_df = df_expanded[df_expanded[event_column] == 1]
    
    # Group by 'new_genre' and count occurrences
    genre_counts = filtered_df.groupby('new_genre').size()
    
    return genre_counts


def calculate_genre_proportions_by_event(df):
    genre_proportions_by_event = pd.DataFrame()
    
    for event in df['events_belongs_to'].explode().unique():
        
        genre_counts = df[df['events_belongs_to'].apply(lambda x: event in x)]['new_genre'].explode().value_counts()
        genre_proportions = 100 * genre_counts / genre_counts.sum()
        genre_proportions_by_event[event] = genre_proportions

    return genre_proportions_by_event