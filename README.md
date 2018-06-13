# blogsample
Django sample

## 使い方
　普通のDjangoのサンプルなのでgit cloneしてからなんやかんやしてくれたら動くかと思います。

## 特徴
一応ブログという形式でやってますがいろんな技術を織り交ぜていこうかなと思ってます。

* 会員登録機能などWebサービス開発における定石技術  
メール認証での仮会員登録からの会員登録までRoute53でのDNS設定など。AWSで非課金でいけるリージョンだとメールサービス無理っぽいので僕がSMTPで使うメールサービスの利用設定をタダで使えるようにしておきます

* Ajax的リアルタイム通信システムのReactでの実装  
ID重複確認処理でやる予定

* Bootstrap4の動的処理部分のReactでの書き換え実装  
めんどくさいのでやらないかもしれない

* 決済機能  
直接実装することは無いが、様々な外部APIを導入し比較しやすいようにする

* バッチ処理  
直近のアクセス数を分析し、目立つ位置に乗せる記事を自動で置き換えるようにする。仮会員のテーブルを登録日時から24時間以上経過しているものを削除する

* コンテンツ配信最適化  
NginXを利用した爆速サイトの構築ノウハウをまとめる。cssインライン化、js非同期読み込み、画像コンテンツ圧縮配信など

* SEO等対策最適化
OGP対策など。そのためにblock再利用できるようなライブラリをpython2用だったものを回収したライブラリを使用

* 多言語対応  
最初から多言語に対応するのではなく、途中から多言語に対応する必要が出てきたときどうするかをみたいな部分で実装を思考中。いろんなフレームワーク見てるけどこの辺り結構どうやってもめんどくさい感じがする。割と需要あると思う

* API通信  
スマホアプリをサクッと作って連携する処理みたいなのがあると良いような気がする。トラフィックのほとんどがスマホになっていく時代なのでこういう技術もできるようにならないと仕事先がみつからない。（いろんな社長さんとかと会ったりしたけど「Android java書いてくれ」「iOSアプリ書いてくれ」とよく言われます。）
スマホアプリも作れるようにしたほうが良いし、当然サーバー側と連携させないといけないのでAPIで連携する技術を作ろうかなと。Socket.ioあたりを用いて実装できればベター

* テスト  
一番重要じゃね？開発を進めるたびに実行して問題がないか確認します。機能追加するたびにそのテストを書いていくと。よっぽどシステム構築に自信がない限り書くべきですし、
システム構築に自信がある人はテストが必要になるくらい大きなサービスを構築するので書かないなんてことは無いと思います。