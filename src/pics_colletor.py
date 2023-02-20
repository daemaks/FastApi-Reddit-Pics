import os as _os
import dotenv as _dotenv
import praw as _praw
import urllib.parse as _parse
import requests as _requests
import shutil as _shutil

_dotenv.load_dotenv()


def _create_reddit_client():
    client = _praw.Reddit(
        client_id=_os.environ["CLIENT_ID"],
        client_secret=_os.environ["CLIENT_SECRET"],
        user_agent=_os.environ["USER_AGENT"],
    )
    return client


def _is_image(post) -> bool:
    try:
        return post.post_hint == "image"
    except AttributeError:
        return False


def _get_pic_urls(client: _praw.Reddit, subreddit_name: str, limit: int):
    hot_pics = client.subreddit(subreddit_name).hot(limit=limit)
    image_urls = list()
    for post in hot_pics:
        if _is_image(post):
            image_urls.append(post.url)

    return image_urls


def _get_pic_name(pic_url: str) -> str:
    pic_name = _parse.urlparse(pic_url)
    return _os.path.basename(pic_name.path)


def _create_folder(folder_name: str):
    try:
        _os.mkdir(folder_name)
    except OSError:
        print("OK!")
    else:
        print("Folder is created")


def _download_image(folder_name: str, raw_response, image_name: str):
    _create_folder(folder_name)
    with open(f"{folder_name}/{image_name}", "wb") as file:
        _shutil.copyfileobj(raw_response, file)


def _collect_pics(subreddit_name: str, limit: int = 10):
    client = _create_reddit_client()
    pics_urls = _get_pic_urls(client=client, subreddit_name=subreddit_name, limit=limit)
    for pic_url in pics_urls:
        pic_name = _get_pic_name(pic_url)
        response = _requests.get(pic_url, stream=True)

        if response.status_code == 200:
            response.raw.decode_content = True
            _download_image(subreddit_name, response.raw, pic_name)


if __name__ == "__main__":
    """
    Instead "Catmemes", type the name of the subreddit.
    You can also change the number of images,
    by add an int value after the subreddit name.
    """
    _collect_pics(
        "Catmemes",
    )
