from ..datasets import RatingData, MovieData


class GlobalMeanEstimator:
    """Estimate every rating as global mean value

    This is dummiest algorithm. Every other realisation must be better.
    In other words, this is our floor estimator.
    """
    def fit(self, ratings: RatingData, movies: MovieData):
        self._mean = ratings.df.rating.mean()

    def estimate(self, user: int, movie: int) -> float:
        return self._mean
