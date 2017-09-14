# p-chat-api

## 概要

Pの課題に対する新機能提案プレゼン用API

https://github.com/dharada1/eureka_intern をベースに作成

herokuで動かしている

## ユーザーデータのAPI

~~~
https://guarded-garden-55846.herokuapp.com/api/user/1/
https://guarded-garden-55846.herokuapp.com/api/user/2/
https://guarded-garden-55846.herokuapp.com/api/user/3/
https://guarded-garden-55846.herokuapp.com/api/user/4/
https://guarded-garden-55846.herokuapp.com/api/user/5/
~~~

## ユーザーデータのAPI

~~~
curl -F "user_id=1" -F "partner_id=2" -F "content=Hello" https://guarded-garden-55846.herokuapp.com/api/message/create/
~~~
