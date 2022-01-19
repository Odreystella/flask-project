# 🔖 목차

- 기술 환경 및 tools
- API 명세서
- 설치 및 실행 방법
<br>


# ⚒️ 기술 환경 및 tools

- Back-End: `Python 3.8`, `flask-restx 0.5.1`
- Deploy: AWS `EC2`
- DB: `postgreSQL`
- ETC: `Git`, `Github`


# 🔖 API 명세서
### 통계 API

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


5.  서버 가동
```
python app.py 
```
