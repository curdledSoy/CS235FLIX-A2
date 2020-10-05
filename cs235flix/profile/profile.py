from flask import Blueprint, render_template, redirect, url_for, request, session
import cs235flix.profile.services as services
import cs235flix.adapters.repository as repo
from cs235flix.authentication.authentication import login_required
from cs235flix.utilities import utilities as utils

profile_blueprint = Blueprint(
    'profile_bp', __name__,url_prefix='/profile'
)

@profile_blueprint.route('/')
@login_required
def profile():
    profile = services.get_user(session['username'], repo.repo_instance)
    if profile:
        return render_template('profile/profile.html', profile=profile, title="Profile", search_form = utils.MovieSearchForm())
    else:
        return redirect(url_for('home_bp.home'))
