
from cs235flix.adapters.repository import AbstractRepository
from cs235flix.domain.model import Movie


def get_top_100movies(repo: AbstractRepository):
    movies = repo.get_movies_by_rank()[0:100]

    return [movie_to_dict(movie) for movie in movies]


def movie_to_dict(movie: Movie):
    movie_dict = {
        'rank': movie.rank,
        'title': movie.title,
        'year': movie.release_year
    }
    return movie_dict