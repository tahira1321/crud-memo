# ==================== 
# import
# ==================== 
from flask import Blueprint, render_template, request

# ==================== 
# Blueprint Instance Creation
# ==================== 
main = Blueprint('main', __name__)
memos = []

# ==================== 
# Routes:View Function
# ==================== 
## Home
@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('why_title')
        content = request.form.get('why_content')
        date = request.form.get('create_date')
        new_memo = {
                "title": title,
                "content": content,
                "date": date
                }
        memos.append(new_memo)
        # print(f"Title: {title}, Content: {content}, Date: {date}")
    return render_template('index.html', memos=memos)

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
