from flask import Blueprint, render_template
from .models import Habit

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html', habits=Habit.query.all())
