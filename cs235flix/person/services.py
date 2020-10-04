from cs235flix.adapters.repository import AbstractRepository
from cs235flix.domain.model import Actor, Movie
from cs235flix.cache import cache


class PersonException(Exception):
    pass


@cache.memoize(timeout=30)
def get_movies_by_director(director: str, repo: AbstractRepository):
    director = repo.get_director_by_name(director)
    if director is None:
        raise PersonException
    movies = repo.get_movies_by_director(director)
    return [movie_to_dict(movie) for movie in sorted(movies)]


@cache.memoize(timeout=30)
def get_collegues(actor: Actor):
    collegues = []
    for collegue in actor.has_worked_with:
        collegues.append(dict(fullname=collegue.actor_full_name))
    return collegues


@cache.memoize(timeout=30)
def get_movies_by_actor(actor, repo: AbstractRepository):
    actor = repo.get_actor(actor)
    if actor is None:
        raise PersonException('Actor does not exist')
    movies = repo.get_movies_by_actor(actor)
    return [movie_to_dict(movie) for movie in sorted(movies)], get_collegues(actor)


def movie_to_dict(movie: Movie):
    movie_dict = dict(rank=movie.rank, title=movie.title, year=movie.release_year, runtime=movie.runtime_minutes,
                      actors=[actor.actor_full_name for actor in movie.actors],
                      director=movie.director.director_full_name, genres=[genre.genre_name for genre in movie.genres],
                      description=movie.description, rating=movie.rating, votes=movie.votes, revenue=movie.revenue,
                      meta_score=movie.metascore)
    return movie_dict
