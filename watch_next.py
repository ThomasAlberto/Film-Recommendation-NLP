import spacy


def get_next_film(description):
    '''Returns the film identifier (Movie A, etc) of the most similar film to the film for which the description has
    been passed into the function as an argument.'''

    # Open the model
    nlp = spacy.load('en_core_web_md')

    # Read in the movies file
    with open('movies.txt') as f:
        film_data = f.readlines()

    # Open two new lists
    titles = []
    film_descriptions = []

    # Append to each of these lists from the text file
    for film in film_data:
        title = film.split(":")[0]
        desc = film.split(":")[1]
        desc = nlp(desc)

        titles.append(title)
        film_descriptions.append(desc)

    # define query as the string which will be input through the nlp model.
    # similarity_scores is the list of similarity scores between the input description (when the function is called)
    # and every single "desc" in the text file.
    # most_similar_index gives us the index of the largest number in the similarity_scores list.
    query = nlp(description)
    similarity_scores = [query.similarity(desc) for desc in film_descriptions]
    most_similar_index = similarity_scores.index(max(similarity_scores))

    # the function returns the index of the film with the greatest similarity in the titles list
    return titles[most_similar_index]


description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
next_film = get_next_film(description)
print(next_film)
