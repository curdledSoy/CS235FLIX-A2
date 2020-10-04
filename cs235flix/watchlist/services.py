from cs235flix.adapters.repository import AbstractRepository
from cs235flix.domain.model import Movie


def movie_to_dict(movie: Movie):
    movie_dict = dict(rank=movie.rank, title=movie.title, year=movie.release_year, runtime=movie.runtime_minutes,
                      actors=[actor.actor_full_name for actor in movie.actors],
                      director=movie.director.director_full_name, genres=[genre.genre_name for genre in movie.genres],
                      description=movie.description, rating=movie.rating, votes=movie.votes, revenue=movie.revenue,
                      meta_score=movie.metascore)
    return movie_dict


def get_user_watchlist(username: str, repo: AbstractRepository):
    watchlist = repo.get_watchlists_for_user(repo.get_user(username=username))
    if watchlist:
        return [movie_to_dict(movie) for movie in watchlist]
    else:
        return None