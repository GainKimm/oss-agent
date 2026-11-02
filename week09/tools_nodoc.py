from secret import API_KEY
import requests

url = "https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"


def get_movie_name(date):
    """
    그 날짜의 박스오피스 1위 영화 제목을 반환한다.
    """

    params = {
        "key": API_KEY,
        "targetDt": date
    }

    response = requests.get(url, params=params, timeout=10)

    data = response.json()
    movies = data["boxOfficeResult"]["dailyBoxOfficeList"]

    return movies[0]["movieNm"]


def get_boxoffice_rank1(date):
    return get_movie_name(date)