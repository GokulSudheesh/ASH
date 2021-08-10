import requests
import datetime
from random import choice

def get_joke(tag):
    # https://github.com/KegenGuyll/DadJokes_API
    url = "https://us-central1-dadsofunny.cloudfunctions.net/DadJokes/random/jokes"
    response = requests.get(url)
    res_json = response.json()
    return (res_json["setup"]+" "+res_json["punchline"])

def get_useless_fact(tag):
    # https://github.com/sameerkumar18/useless-facts-api
    url = "https://useless-facts.sameerkumar.website/api"
    response = requests.get(url)
    res_json = response.json()
    return (res_json["data"])

def get_dog_fact(tag):
    # https://github.com/DukeNgn/Dog-facts-API
    url = "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1"
    response = requests.get(url)
    res_json = response.json()
    return(res_json[0]["fact"])

def get_cat_fact(tag):
    # https://catfact.ninja/
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    res_json = response.json()
    return(res_json["fact"])

def get_cute_cat(tag):
    # https://documenter.getpostman.com/view/5578104/RWgqUxxh
    url = "https://api.thecatapi.com/v1/images/search?format=json"
    response = requests.get(url)
    response_json = response.json()
    return(f"<a href=\"{response_json[0]['url']}\"><img class=\"image-resize\" src=\"{response_json[0]['url']}\"></a>")

def get_cute_dog(tag):
    # https://dog.ceo/dog-api/
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    response_json = response.json()
    return (f"<a href=\"{response_json['message']}\"><img class=\"image-resize\" src=\"{response_json['message']}\"></a>")

def get_quote(tag):
    # https://github.com/lukePeavey/quotable
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    res_json = response.json()
    return (res_json["content"]+" -"+res_json["author"])

def get_news(tag):
    # https://github.com/SauravKanchan/NewsAPI
    categories = ["health", "general", "sports", "business", "technology", "entertainment"]
    category = tag
    if (tag == "news"):
        category = choice(categories)
    url = f"https://saurav.tech/NewsAPI/top-headlines/category/{category}/in.json"
    response = requests.get(url)
    response_json = response.json()
    random_article = choice(response_json["articles"]) # Get a random article from the list of articles
    return(random_article["title"] + f"<br><a href=\"{random_article['url']}\">Link to full article. </a><br><a href=\"{random_article['urlToImage']}\"><img class=\"image-resize\" src=\"{random_article['urlToImage']}\"></a>")

def get_time(tag):
    x = datetime.datetime.now()
    return(x.strftime("%c"))

funsies = {"jokes": get_joke, "useless fact": get_useless_fact, "quote": get_quote,
           "cute dog": get_cute_dog, "cute cat": get_cute_cat, "dog fact": get_dog_fact,
           "cat fact": get_cat_fact, "time": get_time, "cute": choice([get_cute_cat, get_cute_dog]),
           "news": get_news, "health": get_news, "sports": get_news,
           "business": get_news, "technology": get_news,
           "entertainment": get_news}