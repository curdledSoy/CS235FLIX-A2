from flask import Blueprint, render_template, url_for, session

from cs235flix.authentication.authentication import login_required
from cs235flix.utilities.utilities import get_user_watchlist

watchlist_blueprint = Blueprint(
    'watchlist_bp', __name__, url_prefix='/watchlist'
)


@watchlist_blueprint.route('/')
@watchlist_blueprint.route('')
@login_required
def watchlist():
    return render_template(
        'watchlist/watchlist.html',
        title='Watchlist',
        watchlist=get_user_watchlist(),
    )
