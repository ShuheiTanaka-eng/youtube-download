
[概要]
Youtubeの動画をダウンロードできるツールです。


[使い方]
動画をダウンロードしたいフォルダに本スクリプトを配置し実行する。



[トラブルシュート]

・実行時SSL: CERTIFICATE_VERIFY_FAILEDのエラーが吐かれてしまう
→pythonの不具合で証明書のパスが通らなくなることがあります。
以下でパスを通すことで解決されます

pip3 install --upgrade certifi
>>> import certifi
>>> certifi.where()
ここにパスが表示される

export SSL_CERT_FILE=ここに上記で表示されたパスを入れる
