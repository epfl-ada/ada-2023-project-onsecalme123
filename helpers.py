import numpy as np
import pandas as pd
import spacy
from collections import Counter
import nltk
from nltk import punkt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import re
import requests
import sys


def compute_nan_count_and_percentage(df):
    for column_name in df.columns:
        nan_count = df[column_name].isna().sum()
        nan_percentage = df[column_name].isna().mean() * 100

        print(
            f"{column_name}: {nan_count} NaN values, which represents {nan_percentage:.2f} % of the column. \n"
        )


def find_region(country_or_countries, regions):
    if isinstance(country_or_countries, list):
        # since the country is stored as a list and there might be multiple so we have to check them too
        for country in country_or_countries:
            for region, countries in regions.items():
                if country in countries:
                    return region
    return None


# Function to match movies to a specific event based on the threshold


def categorize_event(summary, event_dict, threshold):
    # Remove punctuation and set all words to lower case
    summary_no_punct = remove_punctuation(summary)
    summary_words = summary_no_punct.lower()
    
    # Define your search pattern
    pattern = re.compile(event_dict)

    # Search for the pattern in the text
    matches = re.findall(pattern, summary_words)
    
    common_words_count = len(matches)
                                         
    return common_words_count >= threshold


# Function to add columns to DataFrame based on event categories


def add_event_columns(df, dictionaries_df):
    # Iterate over each event in dictionaries_df and add a column to df
    for event, row in dictionaries_df.iterrows():
        event_words = row["dictionaries"]
        threshold = row["threshold"]
        df[event] = df["summary"].apply(
            lambda x: categorize_event(x, event_words, threshold)
        )
    return df


def create_events_belongs_to_column(df, event_columns):
    df["events_belongs_to"] = df.apply(
        lambda row: [event for event in event_columns if row[event]], axis=1
    )
    return df


# Function to add one column to DataFrame which will be filled by a list of genre categories


def update_new_genre_column(df, genres_considered):
    df["new_genre"] = None

    for name, genre_list in genres_considered.items():
        mask = df["genre"].apply(lambda x: any(item in x for item in genre_list))
        df.loc[mask, "new_genre"] = df.loc[mask, "new_genre"].apply(
            lambda x: [] if x is None else x
        )
        df.loc[mask, "new_genre"] = df.loc[mask, "new_genre"].apply(
            lambda x: x + [name] if isinstance(x, list) else [name]
        )

    return df


def count_genres_for_event(df, event_column):
    # Explode the 'new_genre' column
    df_expanded = df.copy()
    df_expanded = df_expanded.explode("new_genre")

    # Filter rows where the event_column is True
    filtered_df = df_expanded[df_expanded[event_column] == 1]

    # Group by 'new_genre' and count occurrences
    genre_counts = filtered_df.groupby("new_genre").size()

    return genre_counts


def calculate_genre_proportions_by_event(df):
    genre_proportions_by_event = pd.DataFrame()

    for event in df["events_belongs_to"].explode().unique():
        genre_counts = (
            df[df["events_belongs_to"].apply(lambda x: event in x)]["new_genre"]
            .explode()
            .value_counts()
        )
        genre_proportions = 100 * genre_counts / genre_counts.sum()
        genre_proportions_by_event[event] = genre_proportions

    return genre_proportions_by_event


# Function that allows to remove punctuation in a string, we will use it in th eword search process

def remove_punctuation(input_string):
    # Create a translation table to map punctuation characters to None
    translation_table = str.maketrans("", "", string.punctuation)

    # Use translate to remove punctuation
    result_string = input_string.translate(translation_table)

    return result_string


# Function to verify if the movies were correctly assigned to their corresponding event(s) 
# Checks whether the true event/ movement to which the movie corresponds is also a dictionnary-mapped event/movement 

def check_matching(row):
    return row['true_event'] in row['events_belongs_to']


def translations_imbd_to_freebase():

    url = 'https://query.wikidata.org/sparql'
    query = """ SELECT ?item ?imdbID ?freebaseID WHERE {?item wdt:P345 ?imdbID.OPTIONAL {?item wdt:P646 ?freebaseID.}}"""
    headers = {'User-Agent': 'WDQS-example Python/%s.%s' % (sys.version_info[0], sys.version_info[1])}
    data = requests.get(url, headers=headers, params={'query': query, 'format': 'json'}).json()

    imdb = [item['imdbID']['value'] for item in data['results']['bindings']]
    freebase = [item.get('freebaseID', {}).get('value', None) for item in data['results']['bindings']]

    result_df = pd.DataFrame(data ={ 'imdb_id': imdb, 'id_freebase': freebase})

    return result_df

def get_unique_countries(input_list):
    unique_countries = []
    for item in input_list:
        if item not in unique_countries:
            unique_countries.append(item)
    return unique_countries