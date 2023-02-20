import fastapi as _fastapi
import fastapi.responses as _responses

import services as _services

app = _fastapi.FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to the pics scraper"}


@app.get("/general-pics")
def get_general_pics():
    pic_path = _services.select_random_pic("Catmemes")
    return _responses.FileResponse(pic_path)


@app.post("/catmemes")
def create_programmer_humor(image: _fastapi.UploadFile = _fastapi.File(...)):
    file_path = _services.upload_pic("Catmemes", image)
    if file_path is None:
        return _fastapi.HTTPException(status_code=409, detail="incorrect file type")
    return _responses.FileResponse(file_path)
