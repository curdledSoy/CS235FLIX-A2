from flask import Blueprint, render_template, url_for, session, redirect, request
import cs235flix.home.services as services
import cs235flix.utilities.utilities as utils
import cs235flix.adapters.repository as repo
import cs235flix.search.search as search
home_blueprint = Blueprint(
    'home_bp', __name__)


@home_blueprint.route('/', methods=['GET', 'POST'])
def home():
    search_form = utils.MovieSearchForm()
    movies = services.get_top_100movies(repo.repo_instance)
    for movie in movies:
        movie['url'] = url_for('movie_bp.movie', title=movie['title'], year=movie['year'])
        movie['rank'] = utils.ordinal(movie['rank'])
    return render_template(
        'home/home.html',
        title='Home',
        watchlist=utils.get_user_watchlist(),
        movies=movies,
        search_form=search_form,
    )
