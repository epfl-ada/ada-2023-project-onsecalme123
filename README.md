# Movies' Looking Glass: a Reflection of the Modern World 


## Abstract 💡

The last century witnessed key social and political events that transformed many facets of human society. Cinema being a way to depict real-life (as many other forms of art), can reflect all those core societal events and changes in terms of  movies’ genres, scenarios, and characters.
The aim of our project is to see whether we can find specific trends, genres and characters for specific historical events in movies. For this we will regroup the countries of origin of the movies by continent or culture (maybe only look at two continents depending on the completeness of our dataset).
We will then search how specific historical events are influencing the movies and whether we can see specific trends and groupments. Examples of such events are:
- World War I: 1914-1918 (see if we have enough data
- World War II: 1939-1945
- Atomic bombing Hiroshima & Nagasaki: 1945
- Decolonialization (Middle East and Asia ~1945, Africa: ~1955)
- McCarthy hearings: 1954
- Vietnam war: 1955 – 1975
- Contraception pill legalization: 1960 
- Assassination Martin Luther King, Jr: 1968 (which would only be specific for the US but might be interesting to look at)
- Moon Landing: 1969
- Summer of love: 1970
- AIDS: 1981
- Fall of the Berlin Wall: 1989
- Introduction of smartphones: ~ 1995
- 9/11: 2001
- Climate Change: ~2000? 

Throughout these events we can analyze the popular movie genres, plots, whether we can see tendencies for main characters, and which actors are being casted.


## Research Questions 🔍

To determine the most impactful events/movements of the 20th and beginning of the 21st century, we define the importance of an event/movement through movies' characteristics analysis. To drive our reflexion, we formulated several main research questions:

- What are the most ```number of movies``` about ? When were they produced ? How many countries are producing them ?
- What are the most profitable movies in terms of ```box office revenues``` ? What events are the most profitable subject for films ?
- Which movies receive the highest ```rating``` average from the public ? Do these movies deal with a particular event ? How many people were involved and concerned about the rating of a movie ? 
- Do movies have similar ```emotional impact``` on the population independently of events they touch on ? Is there a significant difference between positive and negative emotional impact ?
- In how many ```countries``` was a specific event described ? How does this vary over time and events?
- How ```popular``` is a movie ? Does this significantly depend on the event it is mentioning ?
- How many ```famous actors``` starred in a movie ? How does this influence the impact of a film on the public ? Can actors be cofounders of the impact of an event in movies ?


## Additional Datasets 📈

To answer our research questions, we used a few datasets to enrich our data and proceed to better analysis. Their usefulness and sources are described below:

- ```ethnicities.wikidata.csv```: this dataset contains people's ethnicities mapped to their corresponding freebase ID. Since the freebase database is not accessible anymore, we downloaded this data from [Wikidata](https://query.wikidata.org). It allowed us to complete the *characters.metadata.tsv*  file from the *CMU Movie Summary Corpus* dataset.

- ```reviews.csv```: this dataset contains ratings and reviews of about 500k movies from the IMDB website. It is a cleaned version of a [large reviews' dataset from imdb](https://www.kaggle.com/datasets/ebiswas/imdb-review-dataset) and can be found on [Kaggle](https://www.kaggle.com/datasets/raynardj/imdb-vision-and-nlp?select=reviews.csv). More precisely, it consists of:
  - a *review_id*;
  - the username or real name of the *reviewer*;
  - the *movie* 's title;
  - a *rating* given by the reviewer (grade between 0 and 10, 10 being the best);
  - a *review_summary*;
  - a *spoiler_tag* (0 if a movies' spoil is not present in the review or else 1);
  - a *review_detail* text;
  - and a *helpful* column showing how *list[0]* found the review helpful out of *list[1]*.

- ```imdb_movies.csv```: this dataset contains metadata for all 45,000 movies listed in the *Full MovieLens Dataset*, including 26 million ratings from 270,000 users and movies' revenues for all 45,000 movies. Ratings are on a scale of 1-5. This data was downloaded from [Kaggle](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset).


## Methods 📚

To be completed before the milestone 3 deadline


## Timeline ⏳

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

>**Note**: every team member participated actively in many data processing and analysis and we distributed the tasks evenly among ourselves.
