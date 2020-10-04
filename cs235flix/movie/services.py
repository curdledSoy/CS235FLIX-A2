from datetime import datetime

from cs235flix.adapters.repository import AbstractRepository
from cs235flix.authentication.services import UnknownUserException
from cs235flix.domain.model import Movie, Review, make_review


class UnknownMovieException(Exception):
    pass


def get_movie(title: str, year: str, repo: AbstractRepository):
    movie = repo.get_movie(title, int(year))
    if not movie:
        raise UnknownMovieException
    return movie_to_dict(movie)


def movie_to_dict(movie: Movie):
    movie_dict = dict(rank=movie.rank, title=movie.title, year=movie.release_year, runtime=movie.runtime_minutes,
                      actors=[actor.actor_full_name for actor in movie.actors],
                      director=movie.director.director_full_name, genres=[genre.genre_name for genre in movie.genres],
                      description=movie.description, rating=movie.rating, votes=movie.votes, revenue=movie.revenue,
                      meta_score=movie.metascore, reviews=reviews_to_dict(movie.reviews))
    return movie_dict


def add_review(title: str, year: str, review_text: str,username: str, rating: int, repo: AbstractRepository):
    movie = repo.get_movie(title, int(year))
    if movie is None:
        raise UnknownMovieException

    user = repo.get_user(username)
    if user is None:
        raise UnknownUserException

    review = make_review(user, movie, review_text, rating)
    repo.add_review(review)




def reviews_to_dict(reviews):
    return sorted([review_to_dict(review) for review in reviews],reverse=True, key=lambda x: x['timestamp'])


def review_to_dict(review: Review):
    review_dict = dict(author=review.author.user_name,
        review_text=review.review_text,
        rating=review.rating)
    if datetime.today().strftime('%m/%d/%Y') == review.timestamp.strftime('%m/%d/%Y'):
        review_dict['timestamp'] = review.timestamp.strftime('%H:%M')
    else:
        review_dict['timestamp'] = review.timestamp.strftime('%d/%m')
    return review_dict
