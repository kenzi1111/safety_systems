# アプリ（Care Connect）の概要
一人暮らしかつ要支援者（今後介護が必要になる可能性が高い方）向けの安否確認用チャットアプリケーションです。
管理者（行政の担当者や医師）が対象者にメッセージを送信し、48時間以上返信or既読ボタンのクリックアクションがない場合に
未返信ユーザリスト一覧にユーザ情報が登録されます。
レスポンシブ対応しているためスマホからの確認も可能です。

<img width="729" alt="スクリーンショット 2024-01-31 12 18 53" src="https://github.com/kenzi1111/safety_systems/assets/88967765/318d133f-8446-4a81-b672-ee43d462206d">


# 使用技術
**フロントエンド**

・HTML/CSS

・Javascript

・Bootstrap

**バックエンド**

・Python 3.11.5

・Django 4.2.6

・PostgreSQL

**インフラ**

・Heroku 8.7.1

# インフラ構成図
![スクリーンショット 2024-01-31 16 57 51](https://github.com/kenzi1111/safety_systems/assets/88967765/92370f02-ba24-4623-b6e3-19a03552499e)


# ER図
![スクリーンショット 2024-02-01 0 02 53](https://github.com/kenzi1111/safety_systems/assets/88967765/cf8b816b-d011-4d40-b4ff-018d4164fa40)

# 機能一覧
### ・ユーザー登録（基本情報登録,hostのみ）
![スクリーンショット 2024-01-31 23 21 35](https://github.com/kenzi1111/safety_systems/assets/88967765/fb2d91c2-49ba-4382-a89d-1b40663382bf)

### ・ユーザー登録（詳細情報登録）
<img width="1216" alt="スクリーンショット 2024-02-01 10 26 00" src="https://github.com/kenzi1111/safety_systems/assets/88967765/ea4b916f-aabb-4f57-84a0-9bf892819c9a">

### ・ログイン機能
![スクリーンショット 2024-01-31 23 56 41](https://github.com/kenzi1111/safety_systems/assets/88967765/ac5b3102-5a57-4a33-b065-a497e89c48a7)

### ・チャット機能
<img width="1166" alt="スクリーンショット 2024-02-17 10 32 07" src="https://github.com/kenzi1111/my-first-blog/assets/88967765/0a6548e5-991a-4401-a7a6-4d8856680a63">


### ・メッセージの既読機能
![スクリーンショット 2024-01-31 23 57 49](https://github.com/kenzi1111/safety_systems/assets/88967765/54a4d358-9baa-4c00-aa8e-1113cb1e6536)

### ・未返信ユーザの一覧表示機能
![スクリーンショット 2024-01-31 23 22 28](https://github.com/kenzi1111/safety_systems/assets/88967765/fc999f16-184f-468b-bef8-98a66e4ed871)


# 今後実装したい機能
・ユーザ権限の強化＊host以外のユーザはチャット機能しか使用できないようにする

・バッチ処理：未反応ユーザに対して登録されているメールアドレスに返信を促す

・チャット画面の構成改善：どちらのメッセージなのか判断しづらい

・対象者の住所とメッセージの返信状況を地図上に可視化

・ユーザごとのコメント機能




