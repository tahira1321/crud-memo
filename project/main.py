# ==================== 
# import
# ==================== 
from flask import Blueprint, render_template

# ==================== 
# Blueprint Instance Creation
# ==================== 
main = Blueprint('main', __name__)

# ==================== 
# Routes:View Function
# ==================== 
## Home
@main.route('/')
def index():
    # return 'Hello World'
    return render_template('index.html')

@main.route('/next')
def next_stage():
    return render_template('next.html')
## Other Public Pages
### @main.route('/profile')
### def profile():
###     return render_template('profile.html')

# ==================== 
# Error Handling:Blueprint Specific
# ==================== 
###  Blueprint内のみで適応したいエラーハンドリング
