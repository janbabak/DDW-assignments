# HW 6 - Recommender systems

## Description

I've implemented 4 movie recommender systems, which takes movies and ratings dataset as an input. I've created the following implementations:

-   **Content based**
-   **Collaborative filtering**
-   **Hybrid**
-   **Tensorflow recommenders**

The dataset for movies has three columns:

-   **movieId**: ID of the movie
-   **title**: name of the movie
-   **genres**: list of genres separated by "|"

The dataset for ratings has four columns:

-   **userId**: ID of the user
-   **movieId**: ID of the rated movie
-   **rating**: score given on a 5-star scale with half-star increments from 0.5 to 5.0 stars.
-   **timestamp**: the number of seconds since January 1, 1970, at midnight Coordinated Universal Time (UTC).

## Implementation

### Content based recommendation

Content-based recommendation suggests movies to users based on the content or features of the movie, such as genres in this implementation.

To start, I identified all unique genres and created a dataframe/matrix of movies. The first column of this matrix represents the movie ID, followed by a column for each genre. This is a binary matrix, where 0 represents that the movie does not have that genre, and 1 represents that it does.

Next, I created a dataframe/matrix for each user. The first column of this matrix represents the user ID, followed by columns for each genre. This matrix is not binary and uses a rating system. A value of 0 means the user has not seen a movie of that genre or did not rate it highly. A number greater than 0 indicates that the user rated a movie from that genre with 2.5 or more stars, with each additional movie adding +1 to that value.

I then computed the cosine similarity, set seen movies to 0, normalized the data, and created the recommendation function.

### Collaborative Filtering recommendation

Collaborative filtering recommendation suggests movies to users based on the similarity between their preferences.

Firstly, I created a user-movie matrix with one row for each user and one column for each movie. Then, I computed a matrix of cosine similarities between users (where rows and columns are user IDs). After that, I set the similarity of every user to himself as 0 and normalized the matrix.

Next, I created a watch matrix with rows for users and columns for movies. This binary matrix indicates whether a user has watched a movie or not.

To obtain recommended movies, I multiplied the watch matrix by user similarities and normalized it.

### Hybrid recommendation

This is basically just a combination of previous two methods weighted by some coefficients. These coefficients can be set as parameters, allowing you to choose which method should have a higher weight in the final recommendation.

### Tensorflow recommenders

I attempted to utilize the TensorFlow recommenders mentioned in the task, but encountered difficulties due to incompatibility with my M1 CPU. Despite being able to eventually run TensorFlow on my hardware, the example code for TensorFlow recommenders continued to throw errors. As a result, I switched to using Google Colab, but the free version did not provide sufficient RAM for my Jupyter notebook. Therefore, I only ran the last task on Colab and split the first task into two separate notebooks: [main.ipynb](/src/main.ipynb) and [tensorflow-recommenders.ipynb](/src/tensorflow-recommenders.ipynb). Additionally, I have no prior experience with machine learning and am unfamiliar with how this code operates. I solely used the code provided by the tutorial, modifying only the input dataset and output.

## Results

I split the ratings.csv file into two files, one containing odd lines and the other containing even lines. I randomly selected one of the files for training and the other for testing. I then compared the results from both inputs and attempted to recommend the top 10 movies to user 2.

The following are the results:

- collaborativeFiltering.txt: recall = 0.0, precision = 0.0, f-measure = 0
- hybrid-0.3-0.7.txt: recall = 0.0, precision = 0.0, f-measure = 0
- hybrid-0.7-0.3.txt: recall = 0.1, precision = 0.1, f-measure = 0.10000000000000002
- contentBased.txt: recall = 0.0, precision = 0.0, f-measure = 0
- hybrid-0.5-0.5.txt: recall = 0.0, precision = 0.0, f-measure = 0

The precision and recall values are identical because the count of testing data and training data are the same. A value of 0 indicates that the movies recommended by different methods aren't the same and their intersections are empty most of the time.

The results are stored in the [results](/results/) folder.

The results of Tensorflow recommenders are strange because they suggest one movie several times. As an ML beginner, I have no idea why this is happening.

Top 10 recommendations for user 2: [[b'The Drop (2014)' b'The Drop (2014)' b'The Drop (2014)'
  b'Warrior (2011)' b'Warrior (2011)' b'Warrior (2011)' b'Warrior (2011)'
  b'Warrior (2011)' b'Warrior (2011)' b'Warrior (2011)']]