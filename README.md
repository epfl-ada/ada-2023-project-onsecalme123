# From Protests to Pixels: The Global Film Industry's Reflections on the Biggest Movements and Events of the Last Century

## Abstract 💡

The last century witnessed key social and political events that transformed many facets of human society, ranging from World War I, to Female Emancipation, to the Opioid Crisis.  Cinema being a way to depict real-life (as many other forms of art), can reflect all those core societal events and movements.

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
- Sexuality emancipation
- The rising of STDs 
- The Opioid Crisis
- Destigmatizing Mental Health
- The Atomic Bomb
- The emergence of Genetic Engineering
- LGBTQ emancipation
- Terrorism


## Research Questions 🔍

To determine the most impactful events/movements of the last century, we define the importance of an event/movement through movies' characteristics analysis. To drive our reflexion, we formulated several main research questions:

- For each event we evaluate the ```number of movies``` that were produced about it. How does this number vary over time? Can we find a significant difference between the different events that will give us an indication about the most impactful event?
- How many different ```countries``` produced movies discussing the individual events? When an event is discussed in many countries, it can be argued that it had a big worldwide impact. Can we find significant differences concerning the different events?
- What are the most profitable movies in terms of ```box office revenues``` ? High revenues indicate a high interest of the public and thereby may reflect the impactfulness of the movies corresponding event. 
- What events' movies receive the highest ```rating``` average from the public? The higher the rating, the higher the interest of the public in the topic (or in this case event) that the movies discuss. 
- How many people were involved and concerned about the rating of a movie (the ```vote count```)? Events whose movies are rated by more people may have had a higher importance for society. 
- Can we observe a significant difference in the average ```popularity``` of movies belonging to certain events? Higher popularity of movies indicates a bigger impact of the event in the society.
- Is there a significant difference between positive and negative emotional impact of movies depending on events? Can we analyse the emotional impacts by evaluating written movie reviews by ```sentiment analysis```?


## Additional Datasets 📈

To answer our research questions, we propose these two additional datasets:

- ```reviews.csv```: This dataset contains written user reviews of about 500k movies from the IMDb website. It is a cleaned version of a reviews' dataset from [IMDb](https://www.kaggle.com/datasets/ebiswas/imdb-review-dataset) and can be found on [Kaggle](https://www.kaggle.com/datasets/raynardj/imdb-vision-and-nlp?select=reviews.csv). We will use this to perform sentiment analysis on reviews and determine the emotional impact that movies about a specific historical event had on society.

- ```imdb_movies.csv```: This dataset includes metadata for 45 000 movies from the *Full Movie Lens Dataset* obtained from  [Kaggle](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset), which contains additinal interesting indicators such as vote-counts, popularity and additional movies revenues. We merged it with our current dataset by querying [Wikidata](https://query.wikidata.org) for Freebase_id translations.


## Methods 📚

### Step 1: Data Loading and Preprocessing

We merged the movies dataset (```movie.metadata.tsv```) with plot summaries (```plot_summaries.txt```) The dataset was then augmented with external sources, as described above, followed by preprocessing for convenience.

### Step 2: General Statistics about the Dataset

In this section, we investigate time-span coverage, address NaNs and invalid values, and reorganize country and genre labels into broader categories such as ```world regions``` and ```new genres```.

### Step 3: Associating movies to historical events and movements using dictionaries

To investigate the influence of historical events and movements in movies, we linked them to films through keyword searches in plot summaries, utilizing event-specific dictionaries we created. Despite our objective approach, we conducted tests to assess potential bias in our dictionaries, including the use of a ```correlation matrix``` and the creation of a test set for evaluating other ```performance metrics```.

### Step 4: Diving into the Analysis of Events

In this section, we will try to answer the different research questions.

#### Number of Movies per Event Over the Years

We plotted the annual movie count for each event, providing insights into event popularity and serving as an additional test for our dictionary-based event classification. We also performed an ```ANOVA test``` to detect significant differences in mean percentages across years per event.

#### Number of Countries producing Movies about given Events

To assess the impact of a particular event, specifically the number of countries producing movies about it, we analyzed variations and magnitudes between events by calculating the ```coefficient of variation``` and ```standard deviation```.

#### Box Office Revenue, Rating, Rating Counts and Popularity

To measure audience attendance and the impact of movies based on the events they represent, we decided to use ```95% confidence``` interval plots. This allows us to compare average rating scores, counts, popularity, and box office performance for movies associated with various events.

#### Review Sentiment Analysis

In this section, we conduct sentiment analysis using imported word lists for [positive](https://ptrckprry.com/course/ssd/data/positive-words.txt) and [negative](https://ptrckprry.com/course/ssd/data/negative-words.txt) emotions. We have two options for analyzing reviews: utilizing the complete review (``` Review Detail```) or the filtered keywords from reviews (```Review Summary```), and we chose the latter due to its higher variance in positive and negative emotion ratios, assessed through a ```PCA```. 

## Steps for the Future 💫 

Now that we've identified methods for analyzing event impact, we will be able to proceed with the analysis.

- To find the most impactful event of the last century we will have to decide how to weigh the importance of the different features (box office revenue, rating, etc.) for the final decision. 

- We want to perform further statistical analysis to assess significance of our results. 

- We'll optimize dictionaries for event specificity, addressing performance issues through potential testing in milestone 3. Optimization may involve identifying overly sensitive event-dictionaries, examining statistical metrics while excluding one at a time. We'll also reassess threshold values, considering specific thresholds for each dictionary.

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
├── 27.11.23 - Elaborate an interesting datastory 
│    
├── 01.12.23 - Homework 2 submission deadline
│  
├── 04.12.23 - Getting the analysis and plots finalized
│  
├── 08.12.23 - Website coding
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
