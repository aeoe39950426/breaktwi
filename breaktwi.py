#coding:UTF-8


import twitter
import time


CK = '#########################'                          # Consumer Key
CS = '##################################################' # Consumer Secret
AT = '##########-#######################################' # Access Token
AS = '#############################################'      # Accesss Token Secert


api=twitter.Api(consumer_key=CK,consumer_secret=CS,access_token_key=AT,access_token_secret=AS)

#起動時
print u'システム起動します。'
before = 0
after = 0

#’この中’には自分のスクリーンネーム
user = api.GetUser(screen_name='@hoge')
id = user.id

while 1:
    #ここも
    user = api.GetUser(screen_name='@hoge')
    tweets = api.GetStatus(id)
    before = user.statuses_count
    time.sleep(60)
    #しつこいようだがここも
    user = api.GetUser(screen_name='@hoge')
    after = user.statuses_count
    diff = after-before
    print u'ツイートした数:%d' % (diff)
    if (diff) >= 5:
        i = 0
        #ここで削除
        tweets = api.GetUserTimeline(id )
        while 5 <= (diff-i):
            api.DestroyStatus(tweets[i].id )
            i = i + 1
        print u'削除したゾ。'
        
    else:
        print u'異常なし。'
