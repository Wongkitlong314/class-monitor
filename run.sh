uvicorn app.main:app --reload --host=0.0.0.0 --port=443 --ssl-keyfile=/etc/letsencrypt/live/chatbot.wudao.blog/privkey.pem --ssl-certfile=/etc/letsencrypt/live/chatbot.wudao.blog/fullchain.pem
