# ====================
# Import
# ====================
# Standard Library:OS操作・システム関連モジュール
import os

# Third-party Library:フレームワーク本体・pipでインストールした拡張機能など
from flask import Flask
from dotenv import load_dotenv

# Read .env:アプリ起動前に環境変数を確定
load_dotenv()

# ====================
# Extensions Instance 
# ====================
### 以下は記載位置の例
### db = SQLAlchemy()
### login_manager = LoginManager()

# ====================
# Application Factory 
# ====================
def create_app():
    # --- Framework Instance Creation ---
    app = Flask(__name__)

    # --- Configuration ---
    ## Security
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    ## Database
    ### app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')

    ## Debug

    # --- Initialize Extensions:拡張機能とアプリの紐づけ ---
    ### db.init_app(app)
    ### login_manager.init_app(app)
    
    # --- Error Handling ---
    ### カスタムエラーページの登録
    ### register_error_handlers(app)

    # --- Global Request Hooks ---
    ### 全ルート共通の処理
    ### register_request_hooks(app)

    # --- Local Modules ---
    ## Blueprint import & registration
    from .main import main
    app.register_blueprint(main)

    ##Models import:DBテーブル定義の読込
    ### from . import models

    return app

# ====================
# Helper Functions 
# ====================
def register_error_handlers(app):
    # エラーハンドリングの具体的内容を記入
    #@app.errorhandler(404)
    #def page_not_found(e):
    #    return render_template('404.html'), 404
    pass
