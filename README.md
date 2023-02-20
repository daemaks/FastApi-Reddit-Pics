# Scraper pictires from Reddit using Praw and FastAPI

This project is a simple scraper built using Python's **Praw** and **FastAPI**.

## Installation

* Clone this repository to your local machine using
* Navigate to the project directory
    ```
    $ cd FastApi-Reddit-Pics
    ```
* Install the required packages using
    ```
    $ pip install -r requirements.txt
    ```
## Usage
* Before running the script you need to create the ***.env*** file. After that insert your values
    ```
    CLIENT_ID=
    CLIENT_SECRET=
    USER_AGENT=
    ```
    You can get them by following this link: https://www.reddit.com/prefs/apps
* Run the python script *pics_events.py* and wait. By default the script selects "Catmemes" subreddit, but you can change this value in the script itself.
    ```
    $ python3 src/pics_events.py
    ```
* Start the FastAPI server in *src* folder 
    ```
    $ uvicorn main:app --reload
    ```
* Open your web browser and go to http://127.0.0.1:8000/docs
* Select the URL you want to use
* Click on the **"Try it out!"** button to execute the request