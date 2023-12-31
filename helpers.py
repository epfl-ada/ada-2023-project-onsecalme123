import numpy as np
import pandas as pd

import ast
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
from scipy import stats
from sklearn.decomposition import PCA
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import copy
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.cm as cm
import plotly.graph_objects as go


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
        url, headers = headers, params = {"query": query, "format": "json"}
    ).json()

    imdb = [item["imdbID"]["value"] for item in data["results"]["bindings"]]
    freebase = [
        item.get("freebaseID", {}).get("value", None)
        for item in data["results"]["bindings"]
    ]

    result_df = pd.DataFrame(data = {"imdb_id": imdb, "id_freebase": freebase})

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


def plot_events_over_years(movies_events, events, figures_per_row = 4):
    """
    Plot for each events, the number of movies over the years.
    """

    columns_to_extract = ["date"] + events
    events_df = movies_events[columns_to_extract]

    num_rows = -(-len(events) // figures_per_row)

    fig, axes = plt.subplots(
        num_rows, figures_per_row, figsize = (20, 5 * num_rows), sharex = True, sharey = True
    )

    axes = axes.flatten()

    palette = sns.color_palette("colorblind", n_colors = len(events))

    for i, event in enumerate(events):
        row_idx = i // figures_per_row
        col_idx = i % figures_per_row

        event_data = events_df[["date", event]]

        event_melted = pd.melt(
            event_data,
            id_vars = ["date"],
            value_vars = [event],
            var_name = "event",
            value_name = "occurred",
        )

        event_occurred = event_melted[event_melted["occurred"]]

        event_count = event_occurred.groupby("date").size().reset_index(name = "count")

        sns.lineplot(
            x = "date",
            y = "count",
            data = event_count,
            ax = axes[i],
            label = event,
            color = palette[i],
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


def compute_common_words_ratio(text, word_list):
    """
    Compute the common words ratio between a text and a list of words.
    """

    text_nopunct = remove_punctuation(text.lower())
    text_words = text_nopunct.split()

    word_counts = Counter(text_words)

    common_word_counts = sum(word_counts[word] for word in word_list)

    total_words = len(text_words)

    ratio = common_word_counts / total_words if total_words > 0 else 0

    return ratio


def add_common_words_scores(df, column_name, words_list_1, words_list_2):
    """
    Add a column to each DataFrame with the ratio of common words.
    """

    df[f"positive_emotion_ratio_{column_name}"] = df[column_name].apply(
        lambda x: compute_common_words_ratio(x, words_list_1) * 100
    )
    df[f"negative_emotion_ratio_{column_name}"] = df[column_name].apply(
        lambda x: compute_common_words_ratio(x, words_list_2) * 100
    )

    return df


def pca_plot(features_df, target_df, ax):
    """
    Plot a 2D-PCA in a subplot.
    """

    X = features_df
    y = target_df

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    df_pca = pd.DataFrame(data=X_pca, columns=["PC1", "PC2"])
    df_pca["Target"] = y

    for category in df_pca["Target"].unique():
        subset = df_pca[df_pca["Target"] == category]
        ax.scatter(subset["PC1"], subset["PC2"], label = category, alpha = 0.8)

    ax.set_xlabel("Principal Component 1 (PC1)")
    ax.set_ylabel("Principal Component 2 (PC2)")


def scatter_plot_according_events(df, x_column, y_column, axes, events, label):
    """
    Plot scatter plot and linear regression line according to events.
    """

    axes = axes.flatten()

    for i, event in enumerate(events):
        event_specific_df = movie_affected_to_event(df, event)
        sns.regplot(
            x = x_column,
            y = y_column,
            data = event_specific_df,
            ax = axes[i],
            scatter = False,
            label = label,
        )

        axes[i].set_title(event)
        axes[i].legend(loc="upper left")
        axes[i].set_xlabel("Years")
        axes[i].set_ylabel("Emotion scores")
        # axes[i].set_yscale('log')


def plot_confusion_matrix(confusion_matrix):
    """
    Plot confusion matrix given TP, FP, FN, TN
    """

    [[TP, FP], [FN, TN]] = confusion_matrix
    label = np.asarray(
        [
            ["TP {}".format(TP), "FP {}".format(FP)],
            ["FN {}".format(FN), "TN {}".format(TN)],
        ]
    )

    df_cm = pd.DataFrame(
        confusion_matrix, index = ["Yes", "No"], columns = ["Positive", "Negative"]
    )

    return sns.heatmap(
        df_cm, cmap = "YlOrRd", annot = label, annot_kws = {"size": 16}, cbar = False, fmt = ""
    )


def numpy_helper(df, cols):
    """
    Obtain a NumPy array from a specific subset columns of a DataFrame.

    Parameters:
    - df: pd.DataFrame with N rows
    - cols: M column names

    Returns:
    - np.array: corresponding NumPy array of shape (N, M), cast as a float
    """

    return df[cols].values.astype(float)


def custom_list_agg(series):
    """
    Custom aggregation function for pandas DataFrame groupby.

    Parameters:
    - series (pandas.Series): A pandas Series representing a column of a DataFrame.

    Returns:
    - Union[Any, List[Any]]: If the series has only one unique value, the value is returned as-is.
      If there are multiple unique values, a list of unique values is returned.
    """

    unique_values = series.unique()

    if len(unique_values) == 1:
        return unique_values[0]

    else:
        return list(unique_values)


def compute_averages_and_cis(events, columns_to_compare, movies_events_df):
    """
    Compute averages and confidence intervals for specified columns in a DataFrame.

    Parameters:
    - events (list): List of events.
    - columns_to_compare (list): List of columns to compute averages and confidence intervals for.
    - movies_events_df (pd.DataFrame): DataFrame containing movie events data.

    Returns:
    - all_averages (dict): Dictionary containing lists of averages for each column.
    - lower_bounds (dict): Dictionary containing lists of lower bounds of confidence intervals for each column.
    - upper_bounds (dict): Dictionary containing lists of upper bounds of confidence intervals for each column.
    """

    all_averages = {col: [] for col in columns_to_compare}
    all_conf_intervals = {col: [] for col in columns_to_compare}

    for element in events:
        element_events = movie_affected_to_event(movies_events_df, element)

        for col in columns_to_compare:
            element_data = element_events[col].copy()
            element_data_cleaned = element_data.dropna()

            avg = element_data_cleaned.mean()
            conf_interval = stats.t.interval(
                0.95,
                len(element_data_cleaned) - 1,
                loc=avg,
                scale=stats.sem(element_data_cleaned),
            )

            all_averages[col].append(avg)
            all_conf_intervals[col].append(conf_interval)

    lower_bounds = {
        col: [interval[0] for interval in intervals]
        for col, intervals in all_conf_intervals.items()
    }
    upper_bounds = {
        col: [interval[1] for interval in intervals]
        for col, intervals in all_conf_intervals.items()
    }

    return all_averages, lower_bounds, upper_bounds


def generate_classification_report(
    dictionaries_df, threshold, X_train, merged_test_set_plots, events
):
    """
    Generate a classification report using crossvalidation

    Parameters:
    - dictionaries: DataFrame containing the dictionaries
    - threshold: The minimum threshold of words that need to match between a plot summary and the dictionary of an event
    - X: DataFrame containing the training set of movies
    - merged_test_set_plots: DataFrame containing all movies and their plot summaries
    - events: List of events

    Returns:
    - report_model_df (DataFrame): DataFrame containing the classification report

    """

    dictionaries_copy = dictionaries_df.copy()
    dictionaries_copy["threshold"] = threshold

    movies_test_set_events = add_event_columns(X_train, dictionaries_copy).copy()
    movies_test_set_events = create_events_belongs_to_column(
        movies_test_set_events, events
    ).copy()

    movie_one_hot = movies_test_set_events.copy()

    for event in events:
        movie_one_hot.rename(columns = {event: f"{event}-onehot"}, inplace=True)

    one_hot_columns = [col for col in movie_one_hot.columns if col.endswith("-onehot")]
    movie_one_hot[one_hot_columns] = movie_one_hot[one_hot_columns].astype(int).copy()

    common_values = X_train["name"].values
    merged_test_set_plots = merged_test_set_plots.drop_duplicates(subset = ["name"])

    y = merged_test_set_plots[merged_test_set_plots["name"].isin(common_values)][
        ["name", "true_event"]
    ]
    y = pd.merge(X_train[["name"]], y, on = "name", how = "left")[["name", "true_event"]]

    mlb = MultiLabelBinarizer(classes=events)
    y_binary = mlb.fit_transform(y["true_event"])

    X = numpy_helper(movie_one_hot, one_hot_columns)

    report_model = classification_report(
        y_binary, X, target_names = mlb.classes_, output_dict = True, zero_division = 1
    )
    report_model_df = pd.DataFrame(report_model).T

    return report_model_df


def list_to_set(x):
    """
    Convert a list to a set.

    Parameters:
    - x (list or any): The input list or value.

    Returns:
    - set or any: If the input is a list, returns a set with the elements of the list.
                  Otherwise, returns the input value as is.
    """
    return set(x) if isinstance(x, list) else x


def determine_topn_words(section_df, whole_collection_df, n):
    """
    Determine the top n words with TF-IDF coefficients for a specific section of a collection.

    Parameters:
    - section_df (pd.DataFrame): DataFrame containing the text data for a specific section.
    - whole_collection_df (pd.DataFrame): DataFrame containing the entire collection's text data.
    - n (int): Number of top words to extract based on TF-IDF coefficients.

    Returns:
    - list: A list of tuples, each containing a word and its corresponding TF-IDF coefficient,
            sorted in descending order of TF-IDF coefficients.
    """

    section_text = " ".join(section_df["summary"])
    whole_collection_text = " ".join(whole_collection_df["summary"])

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform([section_text, whole_collection_text])
    feature_names = vectorizer.get_feature_names_out()
    section_tfidf = {
        word: tfidf_matrix[0, idx] for idx, word in enumerate(feature_names)
    }

    sorted_section_tfidf = sorted(
        section_tfidf.items(), key = lambda x: x[1], reverse = True
    )
    top_n_words = sorted_section_tfidf[:n]

    return top_n_words


def convert_to_list(country):
    """Convert a string representation of a list to an actual list of strings."""
    try:
        country_list = ast.literal_eval(country)
        country_list = [str(c) for c in country_list]
        return country_list

    except (ValueError, SyntaxError):
        return [str(country)]


def gini_coefficient(arr):
    """
    Calculates the Gini coefficient
    """
    arr = np.asarray(arr)
    n = arr.shape[0]
    indices = np.arange(1, n + 1)
    return (2 * np.sum((indices - 1) * arr)) / (n * np.sum(arr))


def compute_average_emotion(df, events_columns, emotions):
    """
    Compute the average of values in 'value_column' based on the groups defined by 'group_column'.

    Parameters:
    - df: pandas DataFrame
    - events_columns: list of str, the columns based on which you want to group the data
    - emotions: list of str, the emotions for which you are computing averages

    Returns:
    - pandas DataFrame, containing the computed averages for each event
    """

    result_list = []

    for event in events_columns:
        filtered_df = df[df[event] == True]
        event_data = {"event": event}

        for emotion in emotions:
            average_score = filtered_df[
                f"{emotion}_emotion_ratio_review_summary"
            ].mean()
            event_data[f"average_{emotion}_score"] = average_score

        result_list.append(event_data)

    result_df = pd.DataFrame(result_list)

    return result_df


def plot_events_positive_negative_scores_interactive(df, positive_column, negative_column, events):
    """
    Plot an interactive scatter plot with positive scores on the y-axis and negative scores on the x-axis.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data to be plotted.
    - positive_column (str): The column name for positive scores (y-axis).
    - negative_column (str): The column name for negative scores (x-axis).
    - events (list): List of unique event names present in the 'event' column of the DataFrame.

    Returns:
    - go.Figure: An interactive plotly figure displaying events with average positive and negative emotion scores.
    """

    if df.empty:
        print("DataFrame is empty. Skipping plot.")
        return go.Figure()

    fig_sentiment = go.Figure()

    color_scale = [
        f"rgb{tuple(int(x * 255) for x in cm.tab20c(i)[:3])}"
        for i in range(len(events))
    ]
    marker_size = 10

    for event in events:
        event_specific_df = df[df["event"] == event]

        formatted_distances = event_specific_df.apply(
            lambda row: "{:.2f}".format(
                np.sqrt(row[negative_column] * 2 + row[positive_column] * 2)
            ),
            axis=1,
        )
        formatted_distances_values = formatted_distances.values
        scatter_trace = go.Scatter(
            x = event_specific_df[negative_column],
            y = event_specific_df[positive_column],
            mode = "markers",
            marker = dict(color=color_scale[events.index(event)], size = marker_size),
            name = event,
            hovertemplate = f"Event: {event}<br>"
            + f"Average Negative Emotion Score: %{{x}} %<br>"
            + f"Average Positive Emotion Score: %{{y}} %<br>"
            + f"Distance to Origin: {formatted_distances_values[0]} <extra></extra>",
            text = [event] * len(event_specific_df),
        )
        fig_sentiment.add_trace(scatter_trace)

    fig_sentiment.update_layout(
        title = f"Events Plotted According to Average Positive and Negative Emotions Scores",
        xaxis_title = "Average Negative Score (%)",
        yaxis_title = "Average Positive Score (%)",
        legend_title = "Events",
        legend = dict(x = 1.02, y = 1, font = dict(size = 10)),
        height = 450,
        xaxis = dict(range = [0, 17]),
        yaxis = dict(range = [0, 17]),
    )

    return fig_sentiment
