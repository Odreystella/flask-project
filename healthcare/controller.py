from flask import request
from flask_restx import Resource

from .config import Database


class StatisticsView(Resource):
    def get(self):
        """
        환자와 방문 테이블들의 간단한 통계를 제공합니다.
        """
        db = Database()

        person_sqls = [
            "SELECT COUNT(DISTINCT person_id) FROM person",
            "SELECT COUNT(gender_concept_id) FROM person WHERE gender_concept_id=8532",
            "SELECT COUNT(gender_concept_id) FROM person WHERE gender_concept_id=8507",
            "SELECT COUNT(race_concept_id) FROM person WHERE race_concept_id=8527",
            "SELECT COUNT(race_concept_id) FROM person WHERE race_concept_id=8515",
            "SELECT COUNT(race_concept_id) FROM person WHERE race_concept_id=8516",
            "SELECT COUNT(race_concept_id) FROM person WHERE race_concept_id=0",
            "SELECT COUNT(d.person_id) from death AS d INNER JOIN person AS p ON p.person_id=d.person_id"
        ]

        visit_occurrence_sqls = [
            "SELECT COUNT(visit_concept_id) FROM visit_occurrence WHERE visit_concept_id=9201",
            "SELECT COUNT(visit_concept_id) FROM visit_occurrence WHERE visit_concept_id=9202",
            "SELECT COUNT(visit_concept_id) FROM visit_occurrence WHERE visit_concept_id=9203",
            "SELECT COUNT(v.visit_occurrence_id) from visit_occurrence AS v INNER JOIN person AS p ON v.person_id=p.person_id WHERE gender_concept_id=8532",
            "SELECT COUNT(v.visit_occurrence_id) from visit_occurrence AS v INNER JOIN person AS p ON v.person_id=p.person_id WHERE gender_concept_id=8507",
            "SELECT COUNT(v.visit_occurrence_id) from visit_occurrence AS v INNER JOIN person AS p ON v.person_id=p.person_id WHERE race_concept_id=8527",
            "SELECT COUNT(v.visit_occurrence_id) from visit_occurrence AS v INNER JOIN person AS p ON v.person_id=p.person_id WHERE race_concept_id=8515",
            "SELECT COUNT(v.visit_occurrence_id) from visit_occurrence AS v INNER JOIN person AS p ON v.person_id=p.person_id WHERE race_concept_id=8516",
            "SELECT COUNT(v.visit_occurrence_id) from visit_occurrence AS v INNER JOIN person AS p ON v.person_id=p.person_id WHERE race_concept_id=0",
            "SELECT COUNT(v.visit_occurrence_id) from visit_occurrence AS v INNER JOIN person AS p ON v.person_id=p.person_id WHERE birth_datetime<='2022-01-01 00:00:00' AND birth_datetime >= '2014-12-31 00:00:00'",
            "SELECT COUNT(v.visit_occurrence_id) from visit_occurrence AS v INNER JOIN person AS p ON v.person_id=p.person_id WHERE birth_datetime<='2013-01-01 00:00:00' AND birth_datetime >= '2004-12-31 00:00:00'",
            "SELECT COUNT(v.visit_occurrence_id) from visit_occurrence AS v INNER JOIN person AS p ON v.person_id=p.person_id WHERE birth_datetime<='2003-01-01 00:00:00' AND birth_datetime >= '1994-12-31 00:00:00'",
            "SELECT COUNT(v.visit_occurrence_id) from visit_occurrence AS v INNER JOIN person AS p ON v.person_id=p.person_id WHERE birth_datetime<='1993-01-01 00:00:00' AND birth_datetime >= '1984-12-31 00:00:00'",
            "SELECT COUNT(v.visit_occurrence_id) from visit_occurrence AS v INNER JOIN person AS p ON v.person_id=p.person_id WHERE birth_datetime<='1983-01-01 00:00:00' AND birth_datetime >= '1974-12-31 00:00:00'",
            "SELECT COUNT(v.visit_occurrence_id) from visit_occurrence AS v INNER JOIN person AS p ON v.person_id=p.person_id WHERE birth_datetime<='1973-01-01 00:00:00' AND birth_datetime >= '1964-12-31 00:00:00'",
            "SELECT COUNT(v.visit_occurrence_id) from visit_occurrence AS v INNER JOIN person AS p ON v.person_id=p.person_id WHERE birth_datetime<='1963-01-01 00:00:00' AND birth_datetime >= '1954-12-31 00:00:00'",
            "SELECT COUNT(v.visit_occurrence_id) from visit_occurrence AS v INNER JOIN person AS p ON v.person_id=p.person_id WHERE birth_datetime<='1953-01-01 00:00:00' AND birth_datetime >= '1944-12-31 00:00:00'",
            "SELECT COUNT(v.visit_occurrence_id) from visit_occurrence AS v INNER JOIN person AS p ON v.person_id=p.person_id WHERE birth_datetime<='1943-01-01 00:00:00' AND birth_datetime >= '1934-12-31 00:00:00'",
            "SELECT COUNT(v.visit_occurrence_id) from visit_occurrence AS v INNER JOIN person AS p ON v.person_id=p.person_id WHERE birth_datetime<='1933-01-01 00:00:00' AND birth_datetime >= '1924-12-31 00:00:00'",
            "SELECT COUNT(v.visit_occurrence_id) from visit_occurrence AS v INNER JOIN person AS p ON v.person_id=p.person_id WHERE birth_datetime<='1923-01-01 00:00:00' AND birth_datetime >= '1914-12-31 00:00:00'",
            "SELECT COUNT(v.visit_occurrence_id) from visit_occurrence AS v INNER JOIN person AS p ON v.person_id=p.person_id WHERE birth_datetime<='1913-01-01 00:00:00' AND birth_datetime >= '1904-12-31 00:00:00'",
        ]

        person_data = [db.execute(sql)[0] for sql in person_sqls]
        
        visit_occurrence_data = [db.execute(sql)[0] for sql in visit_occurrence_sqls]

        if len(person_data) == 0 or len(visit_occurrence_data) == 0:
            return {"message": "DATA NOT FOUND"}, 404

        result = {
            "환자": {
                "전체 환자 수": person_data[0],
                "성별 환자 수": {
                    "여성": person_data[1],
                    "남성": person_data[2]
                },
                "인종별 환자 수": {
                    "백인": person_data[3],
                    "아시안": person_data[4],
                    "흑인": person_data[5],
                    "그 외": person_data[6],
                },
                "사망 환자 수": person_data[7]
            },
            "방문": {
                "방문 유형별 방문수": {
                    "입원": visit_occurrence_data[0],
                    "외래": visit_occurrence_data[1],
                    "응급": visit_occurrence_data[2],
                },
                "성별 방문 수": {
                    "여성": visit_occurrence_data[3],
                    "남성": visit_occurrence_data[4],
                },
                "인종별 방문 수": {
                    "백인": visit_occurrence_data[5],
                    "아시안": visit_occurrence_data[6],
                    "흑인": visit_occurrence_data[7],
                    "그 외": visit_occurrence_data[8],
                },
                "연령대별 방문 수": {
                    "0~9세": visit_occurrence_data[9],
                    "10~19세": visit_occurrence_data[10],
                    "20~29세": visit_occurrence_data[11],
                    "30~39세": visit_occurrence_data[12],
                    "40~49세": visit_occurrence_data[13],
                    "50~59세": visit_occurrence_data[14],
                    "60~69세": visit_occurrence_data[15],
                    "70~79세": visit_occurrence_data[16],
                    "80~89세": visit_occurrence_data[17],
                    "90~99세": visit_occurrence_data[18],
                    "100~109세": visit_occurrence_data[19],
                }
            }
        }

        return {'result' : result }, 200


class ConceptInfoView(Resource):
    def get(self):
        """
        각 테이블에 사용된 concept_id들의 정보를 제공합니다.
        """
        PAGE   = int(request.args.get("page", 1))
        LIMIT  = int(request.args.get("limit", 20))
        OFFSET = (PAGE - 1) * LIMIT

        concept_id = request.args.get("id")
        concept_name = request.args.get("name")

        db = Database()

        sql = f"SELECT concept_id, concept_name, domain_id FROM concept WHERE concept_id={concept_id}"
        
        if concept_name:
            sql = f"SELECT concept_id, concept_name, domain_id FROM concept WHERE concept_name='{concept_name}'"

        datas = db.execute(sql)[OFFSET:OFFSET+LIMIT]
        
        if not datas:
            return {"message": "NO CONCEPT INFO"}, 404

        return {'result' : datas }, 200
