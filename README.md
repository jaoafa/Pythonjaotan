# Pythonjaotan

[Javajaotan](https://github.com/jaoafa/Javajaotan)がなんらかの理由により停止していた場合に動作するためのDiscord Botです。  
基本的には常時起動しており、Javajaotanの機能のうち重要な機能のみを実装し停止時の運用を行います。

## 実装機能

以下の機能を実装しています。

### greetingチャンネル投稿時にJavajaotanが動作していなければメッセージを削除

メッセージを受信した場合、3秒間のディレイの後にリアクションがついているかを確認し、ついてなければJavajaotanが停止していると仮定し、メッセージを削除・「SERVICE UNAVAILABLE」のメッセージを送信します。(`jao`・`afa`を除く)  
`jao`・`afa`のいずれかの場合、⚒リアクションをつけます。

メッセージ編集時はメッセージ送信を除く同等の処理を実施します。

### nsfwチャンネルへの画像送信時、スポイラーでなければ削除

メッセージを受信した場合、3秒間のディレイの後にスポイラー画像でなければメッセージを削除します。

## ライセンス

ライセンスは**独自のライセンスである[jaoLicense](https://github.com/jaoafa/jao-Minecraft-Server/blob/master/jaoLICENSE.md)を適用**します。  
ライセンスの適用理由等は[jaoafa/MyMaid3 README.md#このライセンスを適用している理由](https://github.com/jaoafa/MyMaid3/blob/master/README.md#このライセンスを適用している理由)をご覧ください。
