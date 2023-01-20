from fastapi import FastAPI
from mangum import Mangum
import requests
from requests import HTTPError

app = FastAPI()

@app.get("/")
def get_quote():
    try:
        res = requests.get("https://animechan.vercel.app/api/random")
        res = res.json()
        anime = res.get("anime")
        character = res.get("character")
        quote = res.get("quote")
        print(f"Anime: {anime}")
        print(f"Character: {character}")
        print(f"Quote: {quote}")
        return { 
            "statusCode": 200,
            "headers": {},
            "body": res
            }
    except HTTPError as e:
        return {
            "statusCode": 404,
            "error": e
        }

handler = Mangum(app)

# if __name__ == "__main__":
#     get_quote()
# def handler(event, context):
#     response = "Received"
#     print(response)
#     return {
#         'statusCode': 200,
#         'body': response
#     }