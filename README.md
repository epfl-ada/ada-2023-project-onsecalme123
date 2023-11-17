# From Protests to Pixels: The Global Film Industry's Reflections on the Biggest Movements and Events of the Last Century

## Abstract 💡

The last century witnessed key social and political events that transformed many facets of human society, ranging from World War I, to Female Emancipation, to the Opioid Crisis. Cinema can be used as a tool to depict real-life (as many other forms of art), and thereby reflects all of those core societal events and movements. 

The goal of our project is to analyse how these events were represented by the Film Industry and how their corresponding movies were received by the public. Were certain movies watched more than others? Did the public like certain movies more? How international was the ensemble of movie producers for each event? By answering these questions and more, we want to evaluate which event of the last century was the most impactful one. 

The following events were analysed:

- World War 1
- World War 2
- Space exploration
- The Cold War
- The Vietnam War
- Women emancipation
- Black history
- Digitalisation
- Sexuality
- The emergence of STDs
- The Opioid Crisis
- Destigmatizing Mental Health
>- The Atomic Bomb
>- The emergence of Genetic Engineering
>- LGBTQ emancipation
>- Terrorism


## Research Questions 🔍

To determine the most impactful events/movements of the last century, we define the importance of an event/movement through movies' characteristics analysis. To drive our reflexion, we formulated several main research questions:

- For each event we evaluate the ```number of movies``` that were produced about it. How does this number vary over time? Can we find a significant difference between the different events that will give us an indication about the most impactful event?
- How many different ```countries``` produced movies discussing the individual events? When an event is discussed in many countries, it can be argued that it had a big worldwide impact. Can we find significant differences concerning the different events?
- What are the most profitable movies in terms of ```box office revenues``` ? High revenues indicate a high interest of the public and thereby may reflect the impactfulness of the movies corresponding event. 
- What events' movies receive the highest ```rating``` average from the public? The higher the rating, the higher the interest of the public in the topic (or in this case event) that the movies discuss. 
- How many people were involved and concerned about the rating of a movie (the ```vote count```)? Events whose movies are rated by more people may have had a higher importance for society. 
- Can we observe a significant difference in the average ```popularity``` of movies belonging to certain events? Higher popularity of movies indicates a bigger impact of the event in the society.
- Is there a significant difference between positive and negative emotional impact of movies depending on events? Can we analyse the emotianal impacts by evaluating written movie reviews by ```sentiment analysis```?


## Additional Datasets 📈

To answer our research questions, we propose these two additional datasets:

- ```reviews.csv```: this dataset contains written user reviews of about 500k movies from the IMDB website. It is a cleaned version of a [large reviews' dataset from imdb](https://www.kaggle.com/datasets/ebiswas/imdb-review-dataset) and can be found on [Kaggle](https://www.kaggle.com/datasets/raynardj/imdb-vision-and-nlp?select=reviews.csv). We will use this to perform sentiment analysis on reviews and determine the emotional impact that movies about a specific historical event had.

- ```imdb_movies.csv```: This dataset includes metadata for 45 000 movies from the [Full MovieLens Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset), which contains additinal interesting indicators such as vote-counts, popularity and additional movies revenues. In order to merge it with our current dataset we made queries from [Wikidata](https://query.wikidata.org) to obtain the Freebase_id translation.



## Methods 📚

### Step 1: Data Loading and Preprocessing

Here, we loaded and merged the movies dataset (```movie.metadata.tsv```) with the plot summaries dataset (```plot_summaries.txt```). In the process, we removed all movies not containing a plot summary, as it is essential for our analysis. In addition, we enriched our dataset with the external datasets ```IMDb Dataset``` and the ```Reviews Dataset``` (see Additional Datasets). Furthermore, we preprocessed the data by adapting its format to the form most convinient for us. 

### Step 2: General Statistics about the Dataset

The aim of this section is to explore the size of the dataset and get a sense of its scope. For this we started with an overview of the datasets number of movies and time-span coverage. We then evaluated the datasets' NaN's and outliers (invalid values). Finally, specifically for the countries and the genres of a movie, we regrouped the existing labels into broader categories (for the countries this translates into ```world regions```).

### Step 3: Associating movies to historical events and movements using dictionaries

In our project we focus on the impact of historical event and movements through their representation in movies. To be able to do this, we have to map each movie to the historical event or movement it belongs to. This was done using keyword search in the plot summaries. The keywords specific to each event are defined in event-related dictionaries we created. This was done manually by us while trying to stay as objective and event-specific as possible.

With this approach, introducing bias cannot be completely prevented which is why we performed tests to evaluate the quality of our dictionaries. The following tests were performed:

#### Correlation Matrix:

To measure the strength of the relationship between the different dictionaries we created a correlation matrix, using Pearson's correlation coefficient.

#### Evaluation of Event Classification on a Test Set

To further evaluate the quality of our dictionaires, we tested them on a selected sample of movies with known labels. For this we selected 10 movies per event, where we paid close attention to the fact that they should only correspond to a single event. 

We evaluated the performance of our dictionaries by creating a ```confusion matrix```, indicating the True positives, True negatives, False positives and False negatives of our results. We further performed a statistical evaluation, by calculating its ```accuracy```, ```precision```, ```recall```, ```specificity``` and ```F1 score```. 

### Step 4: Diving into the Analysis of Events

In this section, we will try to answer the different research questions.

#### Number of Movies per Event Over the Years

In this section, we plot the count of movies for each event per year. This not only shows which events are more popular and 'more interesting' to society but also serves as additional testing for our dictionary-based event classification. For example, we don't expect movies about WW2 to occur before 1939. We further calculated the percentage of movies released per year per event (event specific movies in that year / total movies released in that year) and tested for significant differences of the mean percentage of each event over the years (ANOVA). This is a generalized t-test that allows for the comparison of more than two means at once. 

#### Number of Countries producing Movies about given Events

In this section, we want to evaluate how many countries were affected by a certain event, that is, how many countries produced movies about that event. To analyse the difference between events and its magnitude, we calculated the ```coefficient of variation``` and the ```standard deviation```. 

#### Box Office Revenue

In this section, we want to analyse the box office revenues average per event, as this is an indicator of how many people went to watch a movie and thereby an indicator of the impact of its content. The significance of the differences between events were evaluated by plotting 95% Confidance Intervals.

#### Rating

In this section, we want to compare the different rating score averages of movies corresponding to different events. As a first step, we had to decide which dataset to use for the rating scores. We had two options: the ```IMDb Dataset``` and the ```Reviews Dataset```. To decide this, we analysed the number of NaN's contained in both, and picked the one with less NaN's (the ```IMDb Dataset```). The significance of the differences between events were evaluated by plotting 95% Confidance Intervals.

#### Number of Rating Votes

In this section, we want to compare the different rating vote counts (how many people voted) of movies corresponding to different events. The significance of the differences between events were evaluated by plotting 95% Confidance Intervals.

#### Popularity

In this section, we want to compare the different poularities of movies corresponding to different events. The significance of the differences between events were evaluated by plotting 95% Confidance Intervals.

### Review Sentiment Analysis

--> CHARLOTTE


## Steps for the Future 💫 

Now that we have evaluated which methods we can use to measure the impacfulness of our events, we will be able to actually perform this analysis. 

- To find the most impactful event of the last century we will have to decide how to weigh the importance of the different features (box office revenue, rating, etc.) for the final decision. 

- We want to perform further statistical analysis to assess significance of our results. 

- We will have to continue the optimization of our dictionaries, making them as event specific as possible. To address their performance issues, we might consider further testing of our dictionaries for milestone 3. One way to optimize this would be to identify which event-dictionaries are too sensitive. This could be done by examining different statistical metrics while excluding one 'event' dictionary at a time. Furthermore, we will have to reconsider what kind of threshold value we want to use (example: specific threshold for each dictionary).

- It could be interesting to perform clustering on our dataset using our impact indicators as prediction features. This could then be compared to the dictionary-based event-matching method.


## Proposed Timeline ⏳

```
.
├── 03.11.23 - Clear definition of project proposal and research questions
│  
├── 10.11.23 - Perform first data processing and analysis
│  
├── 17.11.23 - Milestone 2 submission deadline
│  
├── 24.11.23 - Enrichment of data analysis and verification of data processing
│  
├── 27.11.23 - Verify and analyze statistics assessments 
│    
├── 01.12.23 - Homework 2 submission deadline
│  
├── 04.12.23 - Website coding  
│  
├── 08.12.23 - Elaborate an interesting datastory
│  
├── 15.12.23 - Finalize code implementations and visualizations on the website
│  
├── 22.12.23 - Milestone 3 submission deadline
│  
├── 25.12.23 - Merry Christmas 🎁
.

```


## About our Team 👥

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <td style="border: 1px solid black; padding: 8px;"> Team Members </td>
    <td style="border: 1px solid black; padding: 8px;"> Roles </td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">Gianna Biino (@giabii) - SV Master Student</td>
    <td style="border: 1px solid black; padding: 8px;">Notebook structure and organisation queen</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">Charlotte Daumal (@charlottedaumal) - SV Master Student</td>
    <td style="border: 1px solid black; padding: 8px;">Keywords processing maestro</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">Sandra Frey (@sancatfrey) - SV Master Student</td>
    <td style="border: 1px solid black; padding: 8px;">Python plots' champion</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">Céline Hirsch (@celinehirsch) - SV Master Student</td>
    <td style="border: 1px solid black; padding: 8px;">Dictionnaries optimisation master</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">Elia Mounier-Poulat (@eliamounier) - Data Science Master Student</td>
    <td style="border: 1px solid black; padding: 8px;">Statistics methods expert</td>
  </tr>
</table>

>**Note**: every team member participated actively in many data processing and analysis. We distributed the tasks evenly among ourselves.
