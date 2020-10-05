
from cs235flix.adapters.repository import AbstractRepository
from cs235flix.domain.model import Movie
import cs235flix.utilities.utilities as utils

def get_top_100movies(repo: AbstractRepository):
    movies = repo.get_movies_by_rank()[0:100]

    return [utils.movie_to_dict(movie) for movie in movies]


