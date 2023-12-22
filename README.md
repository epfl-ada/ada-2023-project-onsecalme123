## From Protests to Pixels: The Global Film Industry's Reflections on the Biggest Movements and Events of the Last Century


Link to our Data Story: [From Protests to Pixels](https://celinehirsch.github.io/from-protests-to-pixels/) ✨.

### Abstract 💡

The last century witnessed key social and political events that transformed many facets of human society, ranging from World War I, to Black History, to Digital Revolution. Cinema, being a way to depict real-life, can reflect all those core societal events and movements.

Our project aims to assess the most influential events and movements of the past century by analyzing their societal impact through the film industry. Recognizing cinema as a reflection of society, we will dig into various aspects of the movie industry related to each event. Six different factors, such as the quantity of films produced and their average ratings, will be considered as indicators of impact. The combined results of these assessments will ultimately guide us in determining the event that had the most significant impact on society.

The following events were analysed:

- **World War 1**
- **World War 2**
- The Cold War
- **Atomic Bomb**
- **Space exploration**
- Women Emancipation
- **Black History**
- **Vietnam War**
- **Drug Abuse**
- Sexuality Emancipation
- **The Emergence of STDs** 
- **LGBTQ Emancipation**
- Destigmatizing Mental Health
- **Terrorism**
- **Digital Revolution**
- **Genetic Engineering**

The events marked in bold are the ones whose dictionaries used for keyword analysis were deemed accurate enough to be taken into account for the final analysis to find the most impactful event of the last century.


### Research Questions 🔍

To determine the most impactful events/movements of the last century, we define the importance of an event/movement through movies' characteristics analysis. To drive our reflexion, we formulated several main research questions:

- For each event we evaluate the ```number of movies``` that were produced about it. How does this number vary over time? Can we find a significant difference between the different events that will give us an indication about the most impactful event?
- How many different ```countries``` produced movies discussing the individual events? When an event is discussed in many countries, it can be argued that it had a big worldwide impact. Can we find significant differences concerning the different events?
- What are the most profitable movies in terms of ```box office revenues``` ? High revenues indicate a high interest of the public and thereby may reflect the impactfulness of the movies corresponding event. 
- What events' movies receive the highest ```vote-average``` from the public? The higher the vote-average, the higher the interest of the public in the topic (or in this case event) that the movies discuss. 
- How many people were involved and concerned about the rating of a movie (the ```vote count```)? Events whose movies are rated by more people may have had a higher importance for society. 
- Can we observe a significant difference in the average ```popularity``` of movies belonging to certain events? Higher popularity of movies indicates a bigger impact of the event in the society.
- To what degree does an event affect all areas of life? For this we want to analyze how an event was represented in different ```genres```. Is the event represented equally by genres or is there a specific focus on certain genres?
- Is there a significant difference between positive and negative emotional impact of movies depending on events? Can we analyse the emotional impacts by evaluating written movie reviews by ```sentiment analysis```?


### Additional Datasets 📈

To answer our research questions, we add these two additional datasets:

- ```reviews.csv```: This dataset contains written user reviews of about 500k movies from the IMDb website. It is a cleaned version of a reviews' dataset from [IMDb](https://www.kaggle.com/datasets/ebiswas/imdb-review-dataset) and can be found on [Kaggle](https://www.kaggle.com/datasets/raynardj/imdb-vision-and-nlp?select=reviews.csv). We will use this to perform sentiment analysis on reviews and determine the emotional impact that movies about a specific historical event had on society.

- ```imdb_movies.csv```: This dataset includes metadata for 45 000 movies from the *Full Movie Lens Dataset* obtained from  [Kaggle](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset), which contains additional interesting indicators such as vote-counts, popularity and additional movies revenues. We merged it with our current dataset by querying [Wikidata](https://query.wikidata.org) for Freebase_id translations.

- ```inflation_index.csv```: This dataset stems from the World Bank website and contains the annual inflation indices in percentages for consumer prices between 1980 and 2022. This is needed to adjust the movie box office revenues for inflation.

- ```iso_alpha_cont.csv```: This dataset was generated with the help of ChatGPT and allowed to plot countries on a choropleth map. 



### Methods 📚

#### Step 1: Data Loading and Preprocessing

We merged the movies dataset (```movie.metadata.tsv```) with plot summaries (```plot_summaries.txt```) The dataset was then augmented with external sources, as described above, followed by preprocessing for convenience.

#### Step 2: General Statistics about the Dataset

In this section, we investigate time-span coverage, address NaNs and invalid values, and reorganize country and genre labels into broader categories such as ```world regions``` and ```new genres```.

#### Step 3: Associating movies to historical events and movements using dictionaries

To investigate the influence of historical events and movements in movies, we linked them to films through keyword searches in plot summaries, utilizing event-specific dictionaries we created. In order to determine the ideal minimum threshold of words matched between the plot summaries and the dictionnaries for a movie to be associated to an event, we created a set of movies with known associated events. This set was split into a training and a test set. The ideal dictionary-specific threshold was determined using cross-validation on the training set and the performance of the dictionaries was assessed using the test set. The events ```Cold War```,```Women Emancipation```, ```Sexuality Emancipation``` and ```Destigmatizing Mental Health``` were removed due to their low performance.

#### Step 4: Diving into the Analysis of Events

In this section, we tried to answer the different research questions.

##### Number of Movies Analysis

We plotted the annual movie count for each event, providing insights into event popularity and serving as an additional test for our dictionary-based event classification. We also performed an ```ANOVA test``` to detect significant differences in mean percentages across years per event. To quantitatively evaluate the difference between events, we calculated the percentage of movie releases per year per event.

##### Internationality Analysis

We split the world into its different continents and constructed a world map. In this map, we mark the top three events for each continent to provide a broad overview. To quantitatively evaluate the difference between events, we compare the macroaverage of distributions of events from the different regions.

##### Fame Analysis

To analyse the fame of an event we grouped the parameters ```vote-count```and ```popularity``` together due to their high correlation demonstrated in a correlation analysis. To quantify the difference between events we took the averages of these parameters for each event. These two subparameters will be weighed in the final analysis to count as one full parameter.

##### Box Office Revenue Analysis

For each event the average box office revenue generated per movie was calculated. This was done after having corrected the dataset for inflation.

##### Vote Average Analysis

For each event the vote average for movies was calculated to be able to quantitatively compare the different events.

##### Genre Analysis

For each event we plotted its distribution of genres. To be able to quantify this, the gini coefficients for the distributions were calculated and compared between the individual events. 

##### Sentiment Analysis

We conducted sentiment analysis using imported word lists for [positive](https://ptrckprry.com/course/ssd/data/positive-words.txt) and [negative](https://ptrckprry.com/course/ssd/data/negative-words.txt) emotions. We had two options for analyzing reviews: utilizing the complete review (```Review Detail```) or the filtered keywords from reviews (```Review Summary```), and we chose the latter due to its higher variance in positive and negative emotion ratios, assessed through a ```PCA```. A linear regression analysis of the sentiment scores over time was performed. Finally, the positive versus negative sentiment scores were plotted, their distance from the origin providing a quantitative information of extremity of emotions to be able to compare between events. 


### Proposed Timeline ⏳

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


### About our Team 👥

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <td style="border: 1px solid black; padding: 8px;"> Team Members </td>
    <td style="border: 1px solid black; padding: 8px;"> Roles </td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">Gianna Biino (@giabii) - SV Master Student</td>
    <td style="border: 1px solid black; padding: 8px;">Notebook organisation queen</td>
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
    <td style="border: 1px solid black; padding: 8px;">Web Development master</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">Elia Mounier-Poulat (@eliamounier) - Data Science Master Student</td>
    <td style="border: 1px solid black; padding: 8px;">Statistics methods expert</td>
  </tr>
</table>

>**Note**: every team member participated actively in many data processing and analysis. We distributed the tasks evenly among ourselves.