from cs235flix.adapters.repository import AbstractRepository
from cs235flix.domain.model import Movie, Genre


class UnknownGenreException(Exception):
    pass


def get_movies_by_genre(genre: str, repo: AbstractRepository):
    genre = repo.get_genre(genre)
    if genre is None:
        raise UnknownGenreException
    movies = repo.get_movies_by_genre(genre)

    return [movie_to_dict(movie) for movie in movies]


def movie_to_dict(movie: Movie):
    movie_dict = dict(rank=movie.rank, title=movie.title, year=movie.release_year, runtime=movie.runtime_minutes,
                      actors=[actor.actor_full_name for actor in movie.actors],
                      director=movie.director.director_full_name, genres=[genre.genre_name for genre in movie.genres],
                      description=movie.description, rating=movie.rating, votes=movie.votes, revenue=movie.revenue,
                      meta_score=movie.metascore)
    return movie_dict



