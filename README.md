# 🔖 목차

- 기술 환경 및 tools
- 디렉토리 구조
- API 명세서
- 설치 및 실행 방법
- 구현하지 못한 부분
- 보완하고 싶은 점 및 느낀점
<br>


# ⚒️ 기술 환경 및 tools

- Back-End: `Python 3.8`, `flask-restx 0.5.1`
- Deploy: `AWS EC2`
- DB: `postgreSQL`
- ETC: `Git`, `Github`
<br>

# 🌲 디렉토리 구조
```
.
├── healthcare
│   ├── __init__.py
│   ├── config.py
│   └── controller.py
├── app.py
├── README.md
├── my_settings.py
└── requirements.txt
```

# 🔖 API 명세서

### 👉 통계 API
1. `SQL`문으로 `COUNT()`함수를 사용하여 데이터의 갯수를 가져와 **환자와 방문자 수에 대한 간단한 통계**를 보여줍니다.
2. 전체 환자수는 중복값을 제거하여 가져왔습니다. 성별 환자수는 `gender_concept_id`로 조건을 주어 가져왔고, 인종별 환자수는 `race_concept_id`로 조건을 주어 가져왔습니다. 민족별 환자 수는 FK가 아니라 데이터를 가져올 수 없었습니다. 사망 환자 수는 내부 조인을 사용하여 환자 테이블에 `person_id`가 같은 경우의 데이터를 가져왔습니다.
3. 방문 유형별 방문수는 `visit_concept_id`로 조건을 주어 가져왔습니다. 성별 방문 수는 환자 테이블과 내부 조인하여 `gender_concept_id`로 조건을 주어 가져왔고, 인종별 방문 수는 환자 테이블과 내부 조인하여  `race_concept_id`로 조건을 주어 가져왔습니다. 민족별 방문 수는 FK가 아니라 데이터를 가져올 수 없었습니다. 연령대 별 방문수는 환자 테이블과 내부 조인하여 `birth_datetime`으로 조건을 주어 가져왔습니다.
4. 데이터가 없는 경우 데이터 없음의 메시지를 반환합니다.

- Method: GET

```
http://3.35.218.65:5000/statistics
```

<br>

- response

```
result": {
    "환자": {
        "전체 환자 수": 1000,
        "성별 환자 수": {
            "여성": 452,
            "남성": 548
        },
        "인종별 환자 수": {
            "백인": 845,
            "아시안": 65,
            "흑인": 86,
            "그 외": 4
        },
        "사망 환자 수": 152
        },
    "방문": {
        "방문 유형별 방문수": {
            "입원": 1309,
            "외래": 37026,
            "응급": 3475
        },
        "성별 방문 수": {
            "여성": 19307,
            "남성": 22503
        },
        "인종별 방문 수": {
            "백인": 35487,
            "아시안": 2826,
            "흑인": 3326,
            "그 외": 171
        },
        "연령대별 방문 수": {
            "0~9세": 723,
            "10~19세": 1498,
            "20~29세": 3430,
            "30~39세": 2871,
            "40~49세": 3256,
            "50~59세": 4275,
            "60~69세": 4537,
            "70~79세": 3626,
            "80~89세": 2736,
            "90~99세": 2415,
            "100~109세": 4757
        }
    }
}
```

<br>

### 👉 조회 API
1. `SQL`문으로 조건절을 사용하여 concept 정보(concept_id, concept_name, domain_id)를 보여줍니다.
2. `query string`으로 concept의 `id`를 전달합니다.
3. concept_id 외에 concept의 `name` 으로도 검색이 가능합니다.
4. `page`, `limit`을 전달하여 페이징 처리 후 데이터를 반환합니다. 전달하지 않을 경우, page의 초기값은 1, limit의 초기값은 20입니다.
5. 데이터가 없는 경우 데이터 없음의 메시지를 반환합니다.

- **concept의 id로 조회한 경우**

    - Method: GET

    ```
    http://3.35.218.65:5000/concept?id=8532
    ```

    - parameter : query string

    - response

    ```
    {
        "result": [
            8532,
            "FEMALE",
            "Gender"
        ]
    }
    ```
- **concept의 name 으로 조회한 경우**
    - Method: GET

    ```
    http://3.35.218.65:5000/concept?name=White&page=1&limit=21
    ```

    - parameter : query string


   - response

    ```
    {
        "result": [
            44814658,
            "White",
            "Observation",
            42081612,
            "White",
            "Geography",
            42081613,
            "White",
            "Geography",
            45442861,
            "White",
            "Race",
            719369,
            "White",
            "Meas Value",
            45877987,
            "White",
            "Meas Value",
            8527,
            "White",
            "Race"
        ]
    }
    ```


<br>

# 🔖 설치 및 실행 방법

### 로컬 및 테스트용
1. 해당 프로젝트를 clone하고, 프로젝트로 들어간다.
```
https://github.com/Odreystella/flask_project.git
```

2. 가상환경으로 miniconda를 설치한다. [Go](https://docs.conda.io/en/latest/miniconda.html)

```
conda create -n flask_project python=3.9
conda actvate flask_project
```   

3. 가상환경 생성 후, requirements.txt를 설치한다.

```
pip install -r requirements.txt
```


5.  서버를 가동한다.
```
python app.py 
```
<br>

# ✔️ 구현하지 못한 부분
- 시간 부족으로 인해 각 테이블의 row를 조회하는 API를 구현하지 못했습니다. 각 테이블 마다 **데이터를 상세 조회 하는 API**로 이해했고, 시간이 주어진다면 `id`값을 `path parameter`을 전달하여 해당 테이블에 id값과 일치하는 데이터가 있는지 조회할 것입니다. 
    - `concept` 정보는 `concept` 테이블과 내부 조인하여 해당 row의 `concept_id`와 `concept` 테이블의 `id`가 동일한 경우, concept_name을 반환하게 합니다. 
    - 예를 들어, `person_id`가 `402435`에 해당하는 데이터를 조회할 때 아래와 같이 `SQL`문을 작성할 수 있습니다.
    ```
    SELECT p.person_id, p.gender_concept_id, c.concept_name from person As p INNER JOIN concept As c on p.gender_concept_id=c.concept_id WHERE p.person_id=402435;

    # 결과
    person_id | gender_concept_id | concept_name 
    -----------+-------------------+--------------
       402435 |              8532 | FEMALE
   ```
   - Pagination은 `query parameter`로 `page`와 `limit`를 전달하여 처리할 것입니다.
   - 특정 컬럼 검색은 `query parameter`를 전달하여 `LIKE` 또는 `=` 연산자로 조건을 주어 처리할 것입니다.
<br>

# 👩‍💻 보완하고 싶은 점 및 느낀점
- 보통 이런 과제가 주어질 때, 프로젝트 초기환경 셋팅 -> 모델링 -> API 설계 및 구현 -> 테스트 -> 배포 -> 문서 작성 순으로 진행하는데, 익숙하지 않은 DB, 프레임워크를 사용하다 보니 데이터 구조에 대한 이해, SQL문을 작성하기 위한 DB연결, 프로젝트 구조를 정리하는데 생각보다 시간이 많이 걸렸습니다. 테스트도 진행하지 못해 이 부분도 보완하고 싶습니다.
- 익숙한 Django를 사용하지 않고 상대적으로 이해도가 낮은 Flask를 선택하였습니다. 만에 하나 입사의 기회가 주어진다면 해당 기술 스택에 더 익숙해지는 것이 좋다고 생각했습니다. 그렇기 때문에 ORM 사용, 서버 배포, 프로젝트 구조 등 공부할 부분이 많습니다. 
- ORM을 주로 사용하다 보니까 SQL문을 작성할 때 이해도가 많이 부족한 것을 느꼈습니다. 어떻게 해야 쿼리를 적게 사용할지, 성능을 좋게 할지, 성능이 안좋다면 튜닝은 어떻게 해야할지 등등 공부할 부분이 많다고 느꼈습니다. 
- SQL문을 사용하면 리스트 형태로 데이터를 반환해주어 데이터 처리를 잘 하지 못한게 아쉬웠습니다. pandas 라이브러리를 사용하면 딕셔너리 형태로 데이터를 받을 수 있다고 하였는데, 시도하다가 시간부족으로 넘어가게 되었습니다. 조회 API에서 리턴값 형태가 마음에 들지 않아 보완해보고 싶습니다.

