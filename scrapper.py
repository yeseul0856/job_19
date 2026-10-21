import requests
from bs4 import BeautifulSoup
#from을 쓰는거는 bs4는 파일(모듈)을 모아둔건 라이브러리 라고 하는데 bs4가 라이브러리 import 뒤에는 함수/클래스/변수를 쓴다
# bs4 → 라이브러리(정확히는 패키지)
# BeautifulSoup → 그 안에 있는 클래스
# from 모듈(패키지) import 함수/클래스/변수 
# BeautifulSoup은 HTML 코드를 분석하기 쉬운 형태로 변환



def search_incruit(keyword, pages=1):
    #keyword는 함수 안에서 쓸수있는 매개변수
    jobs = []
    for i in range(pages): 
        page = i * 30

        url = f'https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno={page}'
        r = requests.get(url)
        # print(r.text)
        soup = BeautifulSoup(r.text, "html.parser")

        # print(soup.prettify())

        lis = soup.find_all("li", class_="c_col")
        print(lis)
        # print(len(lis))
        print(f"{i + 1} 페이지 크롤링 중...")

        for li in lis:
            try:
                company = li.find("a", class_="cpname").text
                title = li.find("div", class_="cell_mid").find("a").text
                location = li.find("div", class_="cl_md").find_all("span")[0].text
                link = li.find("div", class_="cell_mid").find("a").get("href")

                job_data = {
                    "company": company,
                    "title": title,
                    "location": location,
                    "link": link
                }
                jobs.append(job_data)
            except:
                pass
    
    return jobs