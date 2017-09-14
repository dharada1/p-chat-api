# p-chat-api

## 概要

Pの課題に対する新機能提案プレゼン用API

https://github.com/dharada1/eureka_intern をベースに作成

herokuで動かしている

## ユーザーデータのAPI

任意のユーザーIDを指定してGETする。
デモではid=1の男性とid=2〜5の女性データを使用する予定。

~~~
https://guarded-garden-55846.herokuapp.com/api/user/1/
https://guarded-garden-55846.herokuapp.com/api/user/2/
https://guarded-garden-55846.herokuapp.com/api/user/3/
https://guarded-garden-55846.herokuapp.com/api/user/4/
https://guarded-garden-55846.herokuapp.com/api/user/5/
~~~

### レスポンス例

~~~
{
  "user_id": 1,
  "user_name": "砂田勇輔",
  "gender": 1,
  "age": 20,
  "job": "学生"
}
~~~

## メッセージを送信するAPI

マッチ後のチャットでメッセージを送信する。

user_idは自分(送る側), partner_idは相手(受け取る側) のIDを指定、
contentに送信内容を指定してPOSTする。

~~~
curl -F "user_id=1" -F "partner_id=2" -F "content=Hello" https://guarded-garden-55846.herokuapp.com/api/message/create/
~~~

### 保存が成功した時のレスポンス

~~~
{
  "status": "success"
}
~~~

### 失敗したときのレスポンス

~~~
{
  "status": "error"
}
~~~

## メッセージの履歴を取得するAPI

まだ書きかけなのでちゃんと動いてません。
user_idは自分, partner_idは相手のIDを指定してGETしてください。

~~~
https://guarded-garden-55846.herokuapp.com/api/message/history/?user_id=1&partner_id=2
~~~


### メッセージのやり取りが1つもない場合のレスポンス

~~~
{
  "user_id": 1,
  "partner_id": 2,
  "messages": "empty"
}
~~~

### 存在しないIDをパラメータにして叩いた場合のレスポンス

~~~
{
  "status": "error"
}
~~~
