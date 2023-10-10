from app.services import user_service
from app.config.database import SessionLocal
from sqlalchemy import text
from app.core.GPT_request import get_completion
from app.util.responses import ImageResponse, TextResponse
from quickchart import QuickChart
import asyncio
import json
from app.enums.dao_enum import Role
import decimal
from datetime import datetime, timedelta
from logging import getLogger

logger = getLogger()
DEFAULT_WIDTH = 500
DEFAULT_HEIGHT = 300
DEFAULT_RATIO = 2.0
class default_chart(QuickChart):
    def __init__(self):
        super().__init__()
        self.width = DEFAULT_WIDTH
        self.height = DEFAULT_HEIGHT
        self.device_pixel_ratio = DEFAULT_RATIO

def summary(query, sql, data):
    summary_prompt = "You are an intelligent educational chatbot who can query the database, and you have executed " + str(sql) + " and got response " + str(data) + "summary the infomations as brief as possile, make it sounds like a {Role} {Action} {Thing}, and {Performance}"
    print(summary_prompt)
    print(query)
    res = get_completion(prompt=query, sys_prompt=summary_prompt, model="gpt-4", temperature=0.2)
    return res

def find_student_id_by_name(name):
    sql = text("select role_id from `user` where `role` = 'student' and name=:name")
    session = SessionLocal()
    result = session.execute(sql, params={"name":name})
    data = result.fetchall()
    session.close()
    return data[0][0]


def get_student_history_info_by_month(year: str, month: str, name: str = None, query : str = None):
    id = find_student_id_by_name(name)
    sql = text("""
               SELECT 
                    SUM(completed_quiz_num) as total_completed_quiz,
                    SUM(Daily_read_num) as total_daily_read,
                    date
                FROM 
                    `student_learning_log`
                WHERE
                    student_id = :stu_id
                AND
                    DATE_FORMAT(date, '%Y') = :year
                AND
                    DATE_FORMAT(date, '%m') = :month
                GROUP BY
                    date;
               """)
    session = SessionLocal()
    result = session.execute(sql, params={"stu_id":id, "month": month, "year": year})
    data = result.fetchall()
    if not data:
        return TextResponse(summary(query, sql, "No data found on " + str(year) + " " + str(month)))
    data = [(float(item[0]) if isinstance(item[0], decimal.Decimal) else item[0],
         float(item[1]) if isinstance(item[1], decimal.Decimal) else item[1],
         item[2]) for item in data]
    session.close()
    chart = default_chart()
    chart.config = {
        "type": "bar",
        "data": {
            "labels": [item[2].strftime('%Y-%m-%d') for item in data],
            "datasets": [{
                "label": "Quiz",
                "data": [item[0] for item in data]
            },
            {
                "label": "Daily Read",
                "data": [item[1] for item in data]
            },
            ]
        }
    }
    return ImageResponse(chart.get_url() + '.png', text=summary(query, sql, data))


def get_student_history_info_by_year(year: str, name: str = None, query: str = None):
    id = find_student_id_by_name(name)
    sql = text("""
               SELECT 
                    SUM(completed_quiz_num) as total_completed_quiz,
                    SUM(Daily_read_num) as total_daily_read,
                    DATE_FORMAT(date, '%Y-%m') as month
                FROM 
                    `student_learning_log`
                WHERE
                    student_id = :stu_id
                AND
                    DATE_FORMAT(date, '%Y') = :year
                GROUP BY
                    DATE_FORMAT(date, '%Y-%m');
               """)
    session = SessionLocal()
    result = session.execute(sql, params={"stu_id": id, "year": year})
    data = result.fetchall()
    if not data:
        return TextResponse(summary(query, sql, "No data found on " + str(year)))
    data = [(float(item[0]) if isinstance(item[0], decimal.Decimal) else item[0],
             float(item[1]) if isinstance(item[1], decimal.Decimal) else item[1],
             item[2]) for item in data]
    session.close()
    chart = default_chart()
    chart.config = {
        "type": "bar",
        "data": {
            "labels": [item[2] for item in data],
            "datasets": [{
                "label": "Quiz",
                "data": [item[0] for item in data]
            },
            {
                "label": "Daily Read",
                "data": [item[1] for item in data]
            }]
        }
    }
    return ImageResponse(chart.get_url() + '.png', text=summary(query, sql, data))


def get_student_history_info_by_day(date: str, name: str = None, query: str = None):
    id = find_student_id_by_name(name)
    sql = text("""
               SELECT 
                    completed_quiz_num,
                    Daily_read_num
                FROM 
                    `student_learning_log`
                WHERE
                    student_id = :stu_id
                AND
                    date = :date;
               """)
    session = SessionLocal()
    result = session.execute(sql, params={"stu_id": id, "date": date})
    data = result.fetchone()
    session.close()
    if not data:
        return TextResponse(summary(query, sql, "No data found on " + str(date)))
    chart = default_chart()
    chart.config = {
        "type": "bar",
        "data": {
            "labels": ["Quiz", "Daily Read"],
            "datasets": [{
                "label": "Quiz",
                "data": [item[0] for item in data]
            },
            {
                "label": "Daily Read",
                "data": [item[1] for item in data]
            }]
        }
    }
    return ImageResponse(chart.get_url() + '.png', text=summary(query, sql, data))

def get_student_history_info_all_time(name: str = None, query: str = None):
    id = find_student_id_by_name(name)
    sql = text("""
               SELECT 
                    completed_quiz_num,
                    Daily_read_num,
                    date
                FROM 
                    `student_learning_log`
                WHERE
                    student_id = :stu_id
                ORDER BY 
                    date;
               """)
    session = SessionLocal()
    result = session.execute(sql, params={"stu_id": id})
    data = result.fetchall()
    if not data:
        return TextResponse(summary(query, sql, "No data found on all time"))
    session.close()
    
    chart = default_chart()
    chart.config = {
        "type": "line",
        "data": {
            "labels": [item[2].strftime('%Y-%m-%d') for item in data],
            "datasets": [{
                "label": "Quiz",
                "data": [item[0] for item in data],
                "fill": False,
                "borderColor": "rgb(75, 192, 192)"
            },
            {
                "label": "Daily Read",
                "data": [item[1] for item in data],
                "fill": False,
                "borderColor": "rgb(255, 99, 132)"
            }]
        }
    }
    return ImageResponse(chart.get_url() + '.png', text=summary(query, sql, data))


def get_student_recent_history_info(name: str, days: int, query: str = None):
    id = find_student_id_by_name(name)
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
    
    sql = text("""
               SELECT 
                    completed_quiz_num,
                    Daily_read_num,
                    date
                FROM 
                    `student_learning_log`
                WHERE
                    student_id = :stu_id
                AND 
                    date BETWEEN :start_date AND :end_date
                ORDER BY 
                    date;
               """)
    session = SessionLocal()
    result = session.execute(sql, params={"stu_id": id, "start_date": start_date, "end_date": end_date})
    data = result.fetchall()
    session.close()

    if not data:
        return TextResponse(summary(query, sql, "No data found in the recent specified days"))

    chart = default_chart()
    chart.config = {
        "type": "line",
        "data": {
            "labels": [item[2].strftime('%Y-%m-%d') for item in data],
            "datasets": [{
                "label": "Quiz",
                "data": [item[0] for item in data],
                "fill": False,
                "borderColor": "rgb(75, 192, 192)"
            },
            {
                "label": "Daily Read",
                "data": [item[1] for item in data],
                "fill": False,
                "borderColor": "rgb(255, 99, 132)"
            }]
        }
    }
    return ImageResponse(chart.get_url() + '.png', text=summary(query, sql, data))


if __name__ == "__main__":
    res = get_student_recent_history_info(name="Emma Johnson", query="how were Emma Johnson doing?")
    res2 = asyncio.run(res.send())
    # print(find_student_id_by_name('Emma Johnson'))