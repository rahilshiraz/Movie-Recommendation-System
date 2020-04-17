The algorithm behind the content based system is very simple, it first takes in all the features of a particular movie 
and searches for movies with similar features, this can be done by calculating cosine similarity using the sklearn package.

Dataset I have used is the moviedataset provided by IMDb consisting of almost 5000 movies with different features like languages,votes,cast,director,genres etc.

I have used features like keywords,genre,cast and director and it recommends me a set of movies which is similar to movie Avatar.
