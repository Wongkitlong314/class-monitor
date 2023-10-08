from fastapi import FastAPI
from .controllers import user_controller

app = FastAPI()

# 注册路由
app.include_router(user_controller.router, prefix="/users", tags=["users"])

# 你可以在此处添加其他路由或中间件，或进行其他初始化操作
