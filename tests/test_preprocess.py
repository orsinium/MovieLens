# project
from movielens import MovieData, RatingData, preprocess


def test_users():
    ratings = RatingData()
    movies = MovieData()
    preprocess(ratings=ratings, movies=movies)
    assert ratings.df['userId'][0] == 0
    assert movies.df['movieId'][0] == 0
    assert movies.df['movieId'][1] == 1
