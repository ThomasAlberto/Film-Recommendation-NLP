# Movie Similarity

This Python script uses spaCy to calculate the similarity between a movie description and the descriptions of other 
movies in a text file, and returns the title of the most similar movie.

## Requirements

spaCy

## Download instructions
1. Clone this repo
2. Install Docker
3. Build the Docker image by running the following command in the repository directory:

> docker build -t movie-similarity-nlp .

4. Run the Docker container by running the following command:

> docker run -p 80:80 movie-similarity-nlp

## Functionality

The get_next_film function takes a movie description as a parameter and returns the film identifier (Movie A, etc) of 
the most similar film to the film for which the description has been passed into the function as an argument.

The function uses spaCy to tokenize and process the text data, and calculates the similarity score between the input 
description and the descriptions of other movies in the movies.txt file using spaCy's built-in similarity function.