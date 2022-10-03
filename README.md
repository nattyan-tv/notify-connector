# Notify Connector
通知をぶっとばすもの。

# Detail
`LINE Notify`とかへのメッセージ送信を一般的なGETリクエストで行うことが出来るいわゆるコネクター。  
あくまで個人用。（認証を行わないため。）

# Endpoint
各エンドポイントの解説

エンドポイント|解説|要求内容
---|---|---
`/line`|LINE Notifyにメッセージ送信|`message=<送信したいメッセージ内容>`
`/discord`|Discordにメッセージ送信|`content=<送信したいメッセージ内容>&username=<ユーザー名>&avatar_url=<アイコン画像>`

# Method
引数として渡せるものの説明

引数|値|説明
---|---|---
`html`|`true`|`true`の時、HTMLタグを除去します。

# Q&A
- Q.いやいや、こんなん何に使うんだよ
  A.まぁ...うん...Microsoft PowerAutomateのHTTP要求がPREMIUM専用の機能だから、OneDriveの「URLからのファイルのアップロード」(Upload file from URL to Onedrive)が、実は無料で使えるGET要求が出来るコネクタだから、それを使用することでTeamsのチャネルに送られたメッセージをこの「Notify Connector」にGETで飛ばせば、LINE NotifyとかDiscordでTeamsのメッセージを見たりするくらいのことはもしかしたら出来るかもしれませんね知りませんけど...
