from flask import Flask, render_template, request
from scrapper import search_incruit

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

#/hi를 치면 함수 hi를 실행하고 hi 안녕-를 return 하겠다
@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    jobs = search_incruit()
    return render_template("search.html", keyword=keyword, jobs=jobs)

if __name__ == '__main__':
    app.run(debug=True)

