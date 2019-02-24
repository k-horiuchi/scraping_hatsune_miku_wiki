from bs4 import BeautifulSoup
from time import sleep
import urllib.request as req
import sys
# 保存先ファイル名
savename = "hatsuneWiki.txt"
# ページ数分ループ(627)
for i in range(627):
    sleep(1) # 1秒待機は優しさ
    # ページのURL
    url = "https://www5.atwiki.jp/hmiku/tag/%E6%9B%B2?&p=" + str(i)
    res = req.urlopen(url)
    soup = BeautifulSoup(res , "html.parser")
    li_list = soup.select("#wikibody > div > ul > li")
    savetext = ""
    # 取得したリストタグ分ループ
    for li in li_list:
        a = li.a # aタグを抽出
        if a != None:
            href = a.attrs["href"] # href属性の中身を抽出
            # このURLはページ末端の共通部品なのでいらない
            if href == "//www5.atwiki.jp/hmiku/tag/?sort=tag":
                # ファイルにStringを上書きしてループを抜ける
                with open(savename, mode="a") as f:
                    f.write(savetext)
                    print(href)
                    break
            else:
                # StringにURLを格納
                savetext += href+"\n"
savename = "musicList.txt"
# 読み取り専用で開く
with open("hatsuneWiki.txt") as f:
    for s_line in f:
        sleep(1)
        savetext = ""
        url = "https:" + s_line
        res = req.urlopen(url)
        soup = BeautifulSoup(res , "html.parser")
        music_tag = soup.select("#wikibody > h2 > a")
        for a in music_tag:
            if a != None:
                music_nm = a.string
                if music_nm != None:
                    savetext += music_nm + "　"
        artist_tag = soup.select("#wikibody > div > a")
        for a in artist_tag:
            if a != None:
                artist_nm = a.string
                if artist_nm != None:
                    savetext += "," + artist_nm
        with open(savename, mode="a") as f:
            f.write(savetext + "\n")
            print(savetext)