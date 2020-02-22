from flask import Flask
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
import json

app = Flask(__name__)
CORS(app)

# one
# one title-j
@app.route("/one_title")
def onetitle():
    result = requests.get("http://www.one.co.il")
    c = result.content
    soup = BeautifulSoup(c)
    # found head article
    samples = soup.find_all("div", "one-article-main")
    f = samples[0].find_all("a", "TopArticleImage")[0]["style"]
    x = {
        "title-j": samples[0].h1.a.string,
        "head-j": samples[0].find("a", "Subtitle-j").string,
        "image-j": f[f.index("https"):-2]
    }

    return (x)
# one articles
@app.route("/one_articles")
def oneArticle():
    result = requests.get("http://www.one.co.il")
    c = result.content
    artList = []
    soup = BeautifulSoup(c)
    # found head article
    samples = soup.find_all("a", "one-article-secondary")

    for art in samples:
        y = str(art.select("h3")[0]).split("<span")[0]
        f = art.find_all("img", "one-article-image")[0]["src"]
        x = {
            "title-j": art.select("h2")[0].string,
            "head-j": y[5:],
            "image-j": f
        }
        if(x["title-j"] != None and x["head-j"] != None):
            artList.append(x)

    samples = soup.find_all("a", "one-article-plain")
    for art in samples:
        y = str(art.select("h3")[0]).split("<span")[0]
        f = art.find_all("img", "one-article-image")[0]
        if f.has_attr("src"):
            f = f["src"]
        else:
            f = ""
        x = {
            "title-j": art.select("h2")[0].string,
            "head-j": y[5:],
            "image-j": f

        }
        if(x["title-j"] != None and x["head-j"] != None):
            artList.append(x)

    return json.dumps(artList)

# sport5
# sport5 title
@app.route("/sport5_title")
def sport5title():
    result = requests.get("http://www.sport5.co.il")
    c = result.content
    soup = BeautifulSoup(c)
    # found head article
    samples = soup.find_all("div", "bomba-article-home")
    f = samples[0].find("img", "img-responsive")
    x = {
        "title-j": samples[0].find("span").string,
        "head-j": samples[0].find_all("span")[1].string,
        "image-j": f["src"]
    }
    return (x)
# sport5 articles
@app.route("/sport5_articles")
def sport5Article():
    result = requests.get("http://www.sport5.co.il")
    c = result.content
    artList = []
    soup = BeautifulSoup(c)
    # found head article
    samples = soup.find_all("div", "articleBannerSpace")
    # f = soup.find_all("div", "section")
    # f = f[1].find_all("div", "img-holder")
    # print(f[0].select("img")[0]["src"])
    for art in samples:

        x = {
            "title-j": art.select("h2 a")[0].string,
            "head-j": art.select("p a")[0].string
        }
        artList.append(x)
    return json.dumps(artList)
# sport1
# sport1 title
@app.route("/sport1_title")
def sport1title():
    result = requests.get("https://sport1.maariv.co.il/israeli-soccer")
    c = result.content
    soup = BeautifulSoup(c)
    # found head article
    samples = soup.find_all("div", "category-article-content")
    f = soup.find_all("div", "category-article-image")
    f = f[0].select("a img")[0]["src"]
    x = {
        "title-j": samples[0].select("a span")[0].string,
        "head-j": samples[0].select("a h4")[0].string,
        "image-j": f
    }
    return (x)
# sport1 articles
@app.route("/sport1_articles")
def sport1Article():
    result = requests.get("https://sport1.maariv.co.il/israeli-soccer")
    c = result.content
    artList = []
    soup = BeautifulSoup(c)
    # found head article
    samples = soup.find_all("div", "category-article-list-item")

    for art in samples:
        t = art.select(".category-article-content a span")
        h = art.select(".category-article-content a h4")
        i = art.select(".category-article-image a img")
        if(len(t) > 0 and len(h) > 0):
            x = {
                "title-j": t[0].string,
                "head-j": h[0].string,
                "image-j": i[0]["src"]
            }
            artList.append(x)

    return json.dumps(artList)


if __name__ == "__main__":
    app.run(debug=True)