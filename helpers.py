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
import matplotlib.pyplot as plt
import seaborn as sns


def compute_nan_count_and_percentage(df):
    """
    Given a DataFrame, print the NaN count per column.
    """

    for column_name in df.columns:
        nan_count = df[column_name].isna().sum()
        nan_percentage = df[column_name].isna().mean() * 100

        print(
            f"{column_name}: {nan_count} NaN values, which represents {nan_percentage:.2f} % of the column.\n"
        )


def find_region(country_or_countries, regions):
    """
    Find the region(s) to which the given country or list of countries belong.
    """

    if isinstance(country_or_countries, list):
        for country in country_or_countries:
            for region, countries in regions.items():
                if country in countries:
                    return region
    return None


def categorize_event(summary, event_dict, threshold):
    """
    Categorize a movie based on the presence of specific words associated with an event.

    Parameters:
    - summary (str): The plot summary of the movie.
    - event_dict (str): A regular expression pattern representing words related to the event.
    - threshold (int): The minimum number of common words required for categorization.

    Returns:
    - bool: True if the movie is categorized based on the threshold, False otherwise.
    """

    summary_no_punct = remove_punctuation(summary)
    summary_words = summary_no_punct.lower()

    pattern = re.compile(event_dict)
    matches = re.findall(pattern, summary_words)

    common_words_count = len(matches)

    return common_words_count >= threshold


def add_event_columns(df, dictionaries_df):
    """
    Add columns to a DataFrame based on event categories.
    """

    for event, row in dictionaries_df.iterrows():
        event_words = row["dictionaries"]
        threshold = row["threshold"]
        df[event] = df["summary"].apply(
            lambda x: categorize_event(x, event_words, threshold)
        )
    return df


def create_events_belongs_to_column(df, event_columns):
    """
    Create an 'events_belongs_to' column in the DataFrame based indicating the events to which each movie belongs.
    """

    df["events_belongs_to"] = df.apply(
        lambda row: [event for event in event_columns if row[event]], axis=1
    )
    return df


def update_new_genre_column(df, genres_considered):
    """
    Add a 'new_genre' column to the DataFrame, indicating the
    corresponding genre categories for each movie.
    """

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
    """
    Count the occurrences of genres for movies belonging to a specific event.
    """
    df_expanded = df.copy()
    df_expanded = df_expanded.explode("new_genre")

    filtered_df = df_expanded[df_expanded[event_column] == 1]

    genre_counts = filtered_df.groupby("new_genre").size()

    return genre_counts


def calculate_genre_proportions_by_event(df):
    """
    Calculate genre proportions for each event based on the provided DataFrame.
    """

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


def remove_punctuation(input_string):
    """
    Remove punctuation characters from the given input string.
    """

    translation_table = str.maketrans("", "", string.punctuation)

    result_string = input_string.translate(translation_table)

    return result_string


def check_matching(row):
    """
    Check if the movie was correctly assigned to its corresponding event(s).
    """

    return row["true_event"] in row["events_belongs_to"]


def translations_imbd_to_freebase():
    """
    Retrieve IMDb to Freebase translations using SPARQL query on Wikidata.

    Returns:
    - pandas.DataFrame: DataFrame containing IMDb IDs and corresponding Freebase IDs.
    """

    url = "https://query.wikidata.org/sparql"
    query = """ SELECT ?item ?imdbID ?freebaseID WHERE {?item wdt:P345 ?imdbID.OPTIONAL {?item wdt:P646 ?freebaseID.}}"""
    headers = {
        "User-Agent": "WDQS-example Python/%s.%s"
        % (sys.version_info[0], sys.version_info[1])
    }
    data = requests.get(
        url, headers=headers, params={"query": query, "format": "json"}
    ).json()

    imdb = [item["imdbID"]["value"] for item in data["results"]["bindings"]]
    freebase = [
        item.get("freebaseID", {}).get("value", None)
        for item in data["results"]["bindings"]
    ]

    result_df = pd.DataFrame(data={"imdb_id": imdb, "id_freebase": freebase})

    return result_df


def get_unique_countries(input_list):
    """
    Extract unique countries from a list.
    """

    unique_countries = []
    for item in input_list:
        if item not in unique_countries:
            unique_countries.append(item)
    return unique_countries


def movie_affected_to_event(df, event):
    """
    Filter the DataFrame to include only rows where a specific 'event' is True.
    """

    return df[df[event] != False]


def plot_events_over_years(movies_events, events, figures_per_row=4):
    """
    Plot for each events, the number of movies over the years.
    """

    columns_to_extract = ["date"] + events
    events_df = movies_events[columns_to_extract]

    num_rows = -(-len(events) // figures_per_row)

    fig, axes = plt.subplots(
        num_rows, figures_per_row, figsize=(20, 5 * num_rows), sharex=True, sharey=True
    )

    axes = axes.flatten()

    palette = sns.color_palette("husl", n_colors=len(events))

    for i, event in enumerate(events):
        row_idx = i // figures_per_row
        col_idx = i % figures_per_row

        event_data = events_df[["date", event]]

        event_melted = pd.melt(
            event_data,
            id_vars=["date"],
            value_vars=[event],
            var_name="event",
            value_name="occurred",
        )

        event_occurred = event_melted[event_melted["occurred"]]

        event_count = event_occurred.groupby("date").size().reset_index(name="count")

        sns.lineplot(
            x="date",
            y="count",
            data=event_count,
            ax=axes[i],
            label=event,
            color=palette[i],
        )

        axes[i].set_title(f"{event}")

    for i in range(len(events), len(axes)):
        fig.delaxes(axes[i])

    plt.tight_layout()
    plt.show()


def get_year_percentage(df, event):
    """
    Calculate the percentage of movies for a specific event over the years.
    """
    event_data = movie_affected_to_event(df, event)
    year_percentage_series = (
        event_data.groupby("date").size() / df.groupby("date").size() * 100
    )
    year_percentage_series = year_percentage_series.fillna(0)

    return year_percentage_series
