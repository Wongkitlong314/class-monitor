from pydantic import BaseModel, Extra
from nonebot.drivers import URL, Request, Response, ASGIMixin, HTTPServerSetup
from nonebot import get_driver
import json
import mysql.connector
import openai

openai.api_key = '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'
def _get_gpt_response(message):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
        ]
    )
    return response['choices'][0]['message']['content']

class Config(BaseModel, extra=Extra.ignore):
    """Plugin Config Here"""

async def hello(request: Request) -> Response:
    conn = mysql.connector.connect(
        host='sg-cdb-30q84dwv.sql.tencentcdb.com',
        user='root',
        password='classmonitor111',
        database='whatsapp',
        port='63957'
    )

    # msg = request.data
    # print(msg)
    print(request.content)
    res = _get_gpt_response(request.content)
    aaa = 'aa'
    # double the aaa
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    conn.close()
    
    return Response(200, content='{"data":"' + res + '"}')


if isinstance((driver := get_driver()), ASGIMixin):
    driver.setup_http_server(
        HTTPServerSetup(
            path=URL("/"),
            method="POST",
            name="hello",
            handle_func=hello,
        )
    )


