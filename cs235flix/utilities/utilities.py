from flask import Blueprint, request, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, SelectField
from wtforms.validators import Optional, Length
import cs235flix.utilities.services as services
import cs235flix.adapters.repository as repo

utilities_bp = Blueprint(
    'utilities_bp', __name__)



def get_user_watchlist():
    if 'username' in session:
        user_watchlist = services.get_user_watchlist(username=session['username'], repo=repo.repo_instance)
        for movie in user_watchlist:
            movie['url'] = url_for('movie_bp',title=movie['title'],year=movie['year'])
        return user_watchlist


def add_to_watchlist():
    username = session['username']
    services.add_to_watchlist(username,session)



def ordinal(n):
    n = int(n)
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix



def _add_chosen_class(kwargs):
    """
    Add the class 'chosen-select' to the HTML elements, keeping any
    other specified render parameters or other classes.
    """
    if 'render_kw' in kwargs:
        if 'class' in kwargs['render_kw']:
            kwargs['render_kw']['class'] += ' chosen-select'
        else:
            kwargs['render_kw']['class'] = 'chosen-select'
    else:
        kwargs['render_kw'] = {'class': 'chosen-select'}




class ChosenSelectField(SelectField):
    def __init__(self, *args, **kwargs):
        _add_chosen_class(kwargs)
        super(ChosenSelectField, self).__init__(*args, **kwargs)


class ChosenSelectMultipleField(SelectMultipleField):
    def __init__(self, *args, **kwargs):
        _add_chosen_class(kwargs)
        super(ChosenSelectMultipleField, self).__init__(*args, **kwargs)


class MovieSearchForm(FlaskForm):
    actors = ChosenSelectMultipleField('Filter Movies by Actors', validators=[Optional()])
    director = ChosenSelectField('Filter Movies by Directors', validators=[Optional()])
    genres = ChosenSelectMultipleField('Filter Movies by Genres', validators=[Optional()])
    fuzzy = StringField('Search Movie by Name', validators=[Optional(), Length(min=2)], render_kw={"placeholder": "Search for Movies"})
    submit = SubmitField('Search')

    def any_fields_filled(self):
        return any([self.actors.data, self.director.data, self.genres.data, self.fuzzy.data])

    def validate(self):
        return self.any_fields_filled()