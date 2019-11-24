from linebot import LineBotApi
from linebot.models import TextSendMessage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import re
import time
import os

# リングフィットアドベンチャー
item_id = '4902370543278'
# item_id = '4988013097025'


# ブラウザーを起動
options = Options()
options.binary_location = os.getenv('GOOGLE_CHROME_SHIM')
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
# driver.implicitly_wait(100)

# Google検索画面にアクセス
url = 'https://www.net-zaiko.com/item/' + item_id
driver.get(url)
time.sleep(5)
targetElements = driver.find_elements_by_css_selector("#sl0 .siSa,.siSb,.siSc,.siSd,.siSe")
title = driver.find_element_by_id("itmH0").text
# htmlを取得・表示
# html = driver.page_source
# print(html)

# rを付けることを推奨。
# バックスラッシュをそのままで分かりやすいため。
# print(targetElement)
flag = False
for el in targetElements:
    pattern = r'Amazon\.co\.jp'
    result = re.search(pattern, el.text)
    if not result:
        flag = True
        print('在庫あり')
    print(el.text)
    print(title)
    # print(result)

# ブラウザーを終了
driver.quit()


# リモートリポジトリに"ご自身のチャネルのアクセストークン"をpushするのは、避けてください。
# 理由は、そのアクセストークンがあれば、あなたになりすまして、プッシュ通知を送れてしまうからです。
line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))

if flag:
    messages = TextSendMessage(text=f"{title}の商品在庫があります！\nこちらよりアクセスして下さい{url}")
    line_bot_api.broadcast(messages=messages)



# if __name__ == "__main__":
#     main()

