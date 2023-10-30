from fastapi import FastAPI

import router
import asyncio

app = FastAPI()

@app.get('/')
async def Home():
  return"Welcome home, Moein"

app.include_router(router.route)
asyncio.create_task(router.consumer())