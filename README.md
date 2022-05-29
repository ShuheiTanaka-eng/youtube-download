
<h1>Youtubeダウンロードツール</h1>

<h2>[概要]</h2>
Youtubeの動画をダウンロードできるツールです。


<h2>[使い方]</h2>
動画をダウンロードしたいフォルダに本スクリプトを配置し実行する。



<h2>[トラブルシュート]</h2>

・実行時SSL: CERTIFICATE_VERIFY_FAILEDのエラーが吐かれてしまう
→pythonの不具合で証明書のパスが通らなくなることがあります。
以下でパスを通すことで解決されます

pip3 install --upgrade certifi<br>
\>\>\> import certifi<br>
\>\>\> certifi.where()<br>
ここにパスが表示される

export SSL_CERT_FILE=ここに上記で表示されたパスを入れる
