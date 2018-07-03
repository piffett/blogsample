# blogsample
Django sample
ブログみたいなのを作る予定。Djangoの機能サンプルに
# 実装予定の機能
## 会員機能
コメントをつけるのを会員制にする
## バッチ処理
アクセス解析機能をもとに一日一回アイキャッチ記事を変更する
## API機能
謎の拡張子[.json]で記事情報が出てくる
## 記事投稿機能
前半200をdescriptionに入れる。しばらくhtmlベタうちだけど，Markdown好きなので勝手にhtmlファイルに変換する機能にしたい
## Reactでの動的表示
Ajax的なのの実装をする。昔PHPでやってたけどこの規模感だとめんどくさそう
## Twitter連携
記事が上がるとTwitterで宣伝してくれるやつ
## コメント機能
コメントをつけられる。
# 頑張ったやつ
## プラグイン改良
テンプレートのブロックタグが複数使えないのがありえないのでプラグインをPython3用に改良
## OGP設定
最近のWebサイトには導入が当たり前。画像周りは手を付けてない

python manage.py loaddata blog/fixtures/initial_data.json