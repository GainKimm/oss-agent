<이론>
1. 수락/요청한 일
2. 거절/ 요청한 일 아님
3. 거절/ 되돌리기 어려움
4. 거절/ 작업 폴더 밖
5. 수락/ 요청한 일
6. 다르게 지시/ 되돌리기 어려움

Read C:\osproject\oss-week9\week09-sample\average_pandas.py
Read C:\osproject\oss-week9\week09-sample\average_plain.py
Read C:\osproject\oss-week9\week09-sample\check.py
Read C:\osproject\oss-week9\week09-sample\scores.csv
4, 4

<실습>
1. week09 폴더의 tools.py를 읽고, 각 함수가 무엇을 받고 무엇을 돌려주는지 설명해줘. 파일은 고치지마.
(1) get_movie_name(date) — tools.py:7-22
받는 것

date: 조회할 날짜 문자열입니다. KOBIS(영화진흥위원회) 일별 박스오피스 API의 targetDt 값으로 그대로 들어갑니다. 이 API는 "20261101" 같은 YYYYMMDD 형식을 씁니다.
하는 일

secret.py의 API_KEY와 date로 요청 파라미터를 만듭니다.
KOBIS API에 GET 요청을 보냅니다. 응답을 최대 10초까지 기다립니다.
응답 JSON에서 boxOfficeResult → dailyBoxOfficeList(순위별 영화 목록)를 꺼냅니다.
돌려주는 것

목록의 첫 번째 항목, 즉 그날 박스오피스 1위 영화 제목(movieNm)을 문자열로 돌려줍니다. 예: "영화제목"
참고할 점 (오류 처리가 없어서 생길 수 있는 일)

날짜 형식이 틀렸거나 데이터가 없는 날짜면 목록이 비어 있어 IndexError가 납니다.
API 키가 틀리면 응답에 boxOfficeResult가 없어 KeyError가 날 수 있습니다.
네트워크 문제나 10초 초과 시 requests에서 예외가 발생합니다.
(2) get_boxoffice_rank1(date) — tools.py:25-26
받는 것

date: 위와 똑같은 날짜 문자열(YYYYMMDD)입니다.
돌려주는 것

get_movie_name(date)를 그대로 호출한 결과, 즉 1위 영화 제목 문자열입니다.
이 함수는 같은 기능을 "박스오피스 1위"라는 뜻이 잘 드러나는 이름으로 한 번 감싼 것입니다. 에이전트가 쓰는 도구 이름으로 쓰려고 만든 것으로 보입니다.

2. week09 폴더의 tools_nodac.py 파일만 읽고,
각 함수가 무엇을 받고 무엇을 돌려주는지 설명해줘.
다른 파일은 열지 말고,
파일은 고치지마.

영화진흥위원회(KOBIS) 일별 박스오피스 API를 호출합니다. API 키는 secret 모듈의 API_KEY에서 가져옵니다. secret.py는 열어보지 않았습니다.

(1) get_movie_name(date) — tools_nodoc.py:7-22
받는 값

date: 조회할 날짜입니다. API의 targetDt 파라미터로 그대로 전달됩니다.
코드에는 형식이 적혀 있지 않습니다. KOBIS API 기준으로는 "20261101" 같은 YYYYMMDD 문자열입니다. 이 형식은 파일 내용이 아니라 API 사양에서 알 수 있는 정보입니다.
돌려주는 값

그 날짜 박스오피스 1위 영화의 제목(str)입니다.
응답 JSON의 boxOfficeResult → dailyBoxOfficeList에서 첫 번째 항목의 movieNm을 꺼냅니다.
참고: 오류를 따로 처리하지 않습니다

날짜가 잘못되었거나 결과 목록이 비어 있으면 KeyError 또는 IndexError가 발생합니다.
네트워크 오류나 10초 타임아웃이 나면 requests 예외가 그대로 올라옵니다.
HTTP 상태 코드는 확인하지 않습니다.
(2) get_boxoffice_rank1(date) — tools_nodoc.py:25-26
받는 값

date: get_movie_name과 같은 날짜 값입니다.
돌려주는 값

get_movie_name(date)의 결과를 그대로 돌려줍니다. 즉 1위 영화 제목(str)입니다.
이름만 다른 래퍼(별칭) 함수이고, docstring은 없습니다.

3. 비교
tools.py는 정확함
tools_nodac.py는 추측이 많음