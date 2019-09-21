import os
import sys
import uvicorn
from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastai.vision import (
    ImageDataBunch,
    open_image,
    get_transforms,
    models,
)
import aiohttp
import predicter
import json


app = Starlette()
app.mount('/static', StaticFiles(directory="static"))
app.debug = True

async def get_bytes(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()


@app.route("/upload", methods=["POST"])
async def upload(request):
    data = await request.form()
    file_data = data["file"]
    print(file_data)
    bytes = await (file_data.read())
    p = predicter.predict_from_bytes(bytes)
    label = str(p[0])
    idx = int(p[1])
    confidence = p[2].tolist()[idx]
    return JSONResponse({
         "prediction": label,
         "confidence": confidence
    })
    
@app.route("/classes", methods=["GET"])
async def get_classes(request):
    return JSONResponse(
        {"spiders": ["Big spider", "Little spider", "Eurl"]}
    )


if __name__ == "__main__":
    if "serve" in sys.argv:
        port = int(os.getenv("PORT", "8008"))
        predicter.init()
        uvicorn.run(app, host="0.0.0.0", port=port)