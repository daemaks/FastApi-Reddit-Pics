from typing import List
import os as _os
import random as _random
import fastapi as _fastapi
import time as _time


def _get_pics_filenames(directory_name: str) -> List[str]:
    return _os.listdir(directory_name)


def select_random_pic(diretory_name: str) -> str:
    pics = _get_pics_filenames(diretory_name)
    random_pic = _random.choice(pics)
    path = f"{diretory_name}/{random_pic}"
    return path


def _is_image(filename: str) -> bool:
    valid_extensions = (".png", ".jpg", ".jpeg", ".gif")
    return filename.endswith(valid_extensions)


def upload_pic(directory_name: str, img: _fastapi.UploadFile):
    if _is_image(img.filename):
        timestr = _time.strftime("%Y%m%d-%H%M%S")
        pic_name = timestr + img.filename.replace(" ", "-")
        with open(f"{directory_name}/{pic_name}", "wb+") as file:
            file.write(img.file.read())

        return f"{directory_name}/{pic_name}"

    return None
