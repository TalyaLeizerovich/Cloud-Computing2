from fastapi import FastAPI
from controllers.shabatcontroller import getShabatInfo
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/shabbat")
async def fetch_shabbat_data():
    answer = await getShabatInfo()
    return JSONResponse(content=answer)

  