from fastapi import FastAPI
from app.controllers import user_controller
from app.controllers import filter,question_controller
import logging

logging.basicConfig(filename='app.log', filemode='w', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()

# 注册路由
app.include_router(user_controller.router, prefix="/users", tags=["users"])
app.include_router(filter.router, prefix="/filter", tags=["all"])
app.include_router(question_controller.router, prefix="/questions", tags=["all"])


# 你可以在此处添加其他路由或中间件，或进行其他初始化操作
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=443)