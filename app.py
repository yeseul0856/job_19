from flask import Flask, render_template, request
from scrapper import search_incruit

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
#templates 폴더에 index.html를 만들어야지 작동이 된다 

#/hi를 치면 함수 hi를 실행하고 hi 안녕-를 return 하겠다
# search라는 함수가 /search라는 주소를 url에서 실행이 되면 search()라는 함수가 실행이 된다 
@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    #request는 requests랑 다르다 http://127.0.0.1:5000/search?keyword=파이썬에서 =뒤에 파이썬을 가져온다
    jobs = search_incruit(keyword)
    return render_template("search.html", keyword=keyword, jobs=enumerate(jobs))
# 선생님은 keyword=keyword, jobs=jobs 이런식으로 변수명을 똑같이 적는게 편하대 그렇게 하신대
# keyword=keyword -> HTML에서 사용할 이름 = 파이썬 변수
if __name__ == '__main__':
    app.run(debug=True)

