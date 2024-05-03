from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse
import io
from tts_script import run_tts_script  
import base64 
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from tts_script import run_tts_script


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return FileResponse('static/index.html')


@app.post("/generate-tts/")
async def generate_tts(text: str = Form(...)):
    mp3_path = run_tts_script(text)
    # Utilizza FileResponse per inviare il file MP3
    return FileResponse(path=mp3_path, media_type='audio/mpeg', filename='output.mp3')