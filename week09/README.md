# week09

## 무엇을 하는 코드인가
영화진흥위원회(KOBIS) 오픈 API로 특정 날짜의 박스오피스 1위 영화 제목을 가져옵니다.
핵심 함수는 `tools.py`의 `get_boxoffice_rank1(date)`이며, `date`는 `YYYYMMDD` 형식의 문자열입니다.

## 설치
```
pip install -r requirements.txt
```
KOBIS API 키가 필요합니다. 같은 폴더에 `secret.py`를 만들고 키를 넣으세요.
```python
API_KEY = "발급받은_키"
```

## 실행
```
python -c "from tools import get_boxoffice_rank1; print(get_boxoffice_rank1('20261027'))"
```
