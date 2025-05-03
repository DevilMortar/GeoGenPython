from flask import Blueprint, render_template

geogen_bp = Blueprint('geogen', __name__)

@geogen_bp.route('/')
def index():
    return render_template('index.html')
