# week09/tools.py 함수 정리

## 개요

`tools.py`는 영화진흥위원회(KOBIS) 오픈 API의 **일별 박스오피스** 엔드포인트를 호출해서, 지정한 날짜의 박스오피스 1위 영화 제목을 가져온다.

- API 키: `secret.py`의 `API_KEY`를 import 해서 사용
- 요청 URL: `https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json`
- HTTP 라이브러리: `requests`

## 함수 목록

### 1. `get_movie_name(date)`

그 날짜의 박스오피스 1위 영화 제목을 반환한다.

- **매개변수**: `date` — 조회할 날짜 문자열 (`targetDt`, `YYYYMMDD` 형식, 예: `"20241101"`)
- **동작**
  1. `key`(API 키)와 `targetDt`(날짜)를 쿼리 파라미터로 만든다.
  2. `requests.get(url, params=params, timeout=10)`으로 API를 호출한다.
  3. 응답 JSON에서 `boxOfficeResult` → `dailyBoxOfficeList` 목록을 꺼낸다.
  4. 목록의 첫 번째 항목(1위)의 `movieNm`(영화 제목)을 반환한다.
- **반환값**: 1위 영화 제목 (문자열)

### 2. `get_boxoffice_rank1(date)`

`get_movie_name(date)`를 그대로 호출해서 결과를 반환하는 래퍼 함수다. 기능은 `get_movie_name`과 같고, 이름만 "박스오피스 1위"라는 의미가 더 잘 드러나게 붙인 것이다.

- **매개변수**: `date` — 조회할 날짜 문자열 (`YYYYMMDD`)
- **반환값**: 1위 영화 제목 (문자열)

## 참고 (현재 코드의 한계)

- HTTP 상태 코드를 확인하지 않는다. (`response.raise_for_status()` 등이 없음)
- API가 오류 응답을 주거나 키가 잘못되면 `data["boxOfficeResult"]`에서 `KeyError`가 발생할 수 있다.
- `dailyBoxOfficeList`가 비어 있으면(예: 미래 날짜) `movies[0]`에서 `IndexError`가 발생한다.
- 네트워크 오류나 타임아웃(10초) 예외도 따로 처리하지 않는다.
- `get_boxoffice_rank1`은 `get_movie_name`과 기능이 겹친다.
