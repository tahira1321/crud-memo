# Memo app (CRUD Practice)
シンプルなCRUD機能のみを備えたメモアプリです

## 1. 主な機能 (Features)
* **一覧表示**: 投稿されたメモを日付順に閲覧
* **新規作成**: タイトル、内容、日付を指定して保存
* **編集機能**: 既存のメモをID指定で安全に上書き
* **論理削除**: `status` カラムを用いた安全なデータ削除（404/500エラーページ完備）

## 2. 使用技術 (Tech Stack)
* **Backend**: Python 3.9 / Flask (Blueprint 構成)
* **Database**: MySQL / PyMySQL (Raw SQL)
* **Infrastructure**: Docker / WSL2 / Ubuntu

## 3. 起動方法 (Setup)

以下の手順でローカル環境を構築してください。

### ① リポジトリの準備
```bash
git clone <your-repository-url>
cd crud-memo
