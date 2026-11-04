# week09/tools.py 함수 설명

## 개요

`tools.py`는 영화진흥위원회(KOBIS) 오픈 API의 **일별 박스오피스** 정보를 조회하는 모듈이다.

- `secret.py`에서 `API_KEY`를 가져와 인증에 사용한다.
- `requests` 라이브러리로 아래 URL에 GET 요청을 보낸다.
  - `https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json`

## 함수 목록

| 함수 | 매개변수 | 반환값 | 설명 |
|------|----------|--------|------|
| `get_movie_name(date)` | `date`: 날짜 문자열 (`YYYYMMDD`) | 1위 영화 제목 (`str`) | API를 호출해 해당 날짜 박스오피스 1위 영화 제목을 반환 |
| `get_boxoffice_rank1(date)` | `date`: 날짜 문자열 (`YYYYMMDD`) | 1위 영화 제목 (`str`) | `get_movie_name(date)`를 그대로 호출하는 래퍼 함수 |

### 1. `get_movie_name(date)`

docstring: "그 날짜의 박스오피스 1위 영화 제목을 반환한다."

동작 순서:

1. `key`(API 키)와 `targetDt`(조회 날짜)로 쿼리 파라미터를 만든다.
2. `requests.get(url, params=params, timeout=10)`으로 API를 호출한다. (타임아웃 10초)
3. 응답을 JSON으로 변환한 뒤 `data["boxOfficeResult"]["dailyBoxOfficeList"]`에서 순위 목록을 꺼낸다.
4. 목록의 첫 번째 항목(1위)의 `movieNm` 값을 반환한다.

사용 예:

```python
from tools import get_movie_name
print(get_movie_name("20241101"))
```

### 2. `get_boxoffice_rank1(date)`

`get_movie_name(date)`의 결과를 그대로 반환한다. 별도 로직은 없고, "박스오피스 1위"라는 의도가 이름에 드러나도록 만든 별칭(래퍼) 함수이다. docstring은 없다.

## 참고: 예외 처리 부족

- HTTP 상태 코드를 확인하지 않는다. (`raise_for_status()` 없음)
- API 키 오류 등으로 응답 구조가 다르면 `KeyError`가 발생할 수 있다.
- 결과 목록이 비어 있으면(예: 미래 날짜) `movies[0]`에서 `IndexError`가 발생한다.
- 네트워크 오류·타임아웃 예외를 처리하지 않는다.
