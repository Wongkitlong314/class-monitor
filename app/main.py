import sys
import os
sys.path.append(os.getcwd())
print(sys.path)
from fastapi import FastAPI
from controllers import user_controller

app = FastAPI()

# 注册路由
app.include_router(user_controller.router, prefix="/users", tags=["users"])

# 你可以在此处添加其他路由或中间件，或进行其他初始化操作

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
