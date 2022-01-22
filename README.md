## pycon_kyushu_2022_kumamoto_grpc_handson

gRPCで作成したチャットアプリケーションです。

### 概要

- [公式サイト](https://kyushu.pycon.jp/2022/)
- 日時: 2022/1/22（土）
- 講演時間: 15:00～15:30
- 場所: 熊本城ホール メイン会場 / Room B
- [connpassイベントページ](https://pycon-kyushu.connpass.com/event/224167/)

## 依存関係

以下のいずれかの前提環境が必要

python3.9
## 開発環境構築

以下のいずれかの方法で環境構築を行う

```
$ git clone git@github.com:nishidayoshikatsu/pycon_kyushu_2022_kumamoto_grpc_handson.git
$ pip3 install -r requirements.txt
$ python3 proto/codegen.py
$ python3 server.py
$ python3 client.py
```