# week09/tools.py 함수 설명

## 파일 개요

`tools.py`는 영화진흥위원회(KOBIS) 오픈 API로 **일별 박스오피스**를 조회하는 모듈이다. 날짜를 넣으면 그날 박스오피스 1위 영화의 제목을 돌려준다.

| 항목 | 내용 |
| --- | --- |
| 외부 의존성 | `requests` (HTTP 요청), `secret.API_KEY` (KOBIS API 키) |
| 호출 API | `searchDailyBoxOfficeList.json` (일별 박스오피스 목록) |
| 모듈 전역 변수 | `url` — API 엔드포인트 주소 |

## 함수 요약

| 함수 | 매개변수 | 반환값 | 역할 |
| --- | --- | --- | --- |
| `get_movie_name(date)` | `date`: `YYYYMMDD` 형식 문자열 | 1위 영화 제목 (`str`) | API를 직접 호출하는 핵심 함수 |
| `get_boxoffice_rank1(date)` | `date`: `YYYYMMDD` 형식 문자열 | 1위 영화 제목 (`str`) | `get_movie_name`을 호출만 하는 래퍼 |

## 함수 상세

### `get_movie_name(date)`

docstring: "그 날짜의 박스오피스 1위 영화 제목을 반환한다."

처리 흐름:

1. `{"key": API_KEY, "targetDt": date}` 형태로 쿼리 파라미터를 만든다.
2. `requests.get(url, params=params, timeout=10)`으로 요청을 보낸다. 10초 안에 응답이 없으면 타임아웃된다.
3. `response.json()`으로 응답을 딕셔너리로 바꾼다.
4. `data["boxOfficeResult"]["dailyBoxOfficeList"]`에서 순위 목록을 꺼낸다.
5. 목록의 0번째 항목(1위)의 `movieNm` 값을 반환한다.

사용 예:

```python
from tools import get_movie_name

print(get_movie_name("20241101"))  # 그날 1위 영화 제목 출력
```

### `get_boxoffice_rank1(date)`

`get_movie_name(date)`를 그대로 호출해서 결과를 돌려준다. 자체 로직은 없고, "박스오피스 1위를 구한다"는 뜻이 이름에 더 잘 드러나도록 만든 별칭 함수다.

```python
def get_boxoffice_rank1(date):
    return get_movie_name(date)
```

## 함수 간 관계

```
get_boxoffice_rank1(date)
        │ 호출
        ▼
get_movie_name(date) ──HTTP GET──▶ KOBIS 일별 박스오피스 API
```

## 개선할 점

- **예외 처리 없음**: 네트워크 오류, 타임아웃, HTTP 오류 상태 코드를 처리하지 않는다.
- **응답 구조를 가정함**: API 키가 잘못됐거나 오류 응답이 오면 `boxOfficeResult` 키가 없어서 `KeyError`가 난다.
- **빈 목록 처리 없음**: 데이터가 없는 날짜(예: 오늘 이후)를 넣으면 `movies[0]`에서 `IndexError`가 난다.
- **입력 검증 없음**: `date`가 `YYYYMMDD` 형식인지 확인하지 않는다.
- **중복 함수**: 두 함수의 기능이 같아서 하나로 합치거나 역할을 나눌 수 있다.
