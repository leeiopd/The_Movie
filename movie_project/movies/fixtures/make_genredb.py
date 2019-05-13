# https://api.themoviedb.org/3/genre/movie/list?api_key=4cfd64a4bb100569ac5eeaf4f3b49c9c&language=ko-KR

import requests, json

key = "4cfd64a4bb100569ac5eeaf4f3b49c9c"

url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={key}&language=ko-KR"

response = requests.get(url).json()

genres = response['genres']
genres_a = []

for genre in genres: 
    data = {"model": "movies.genre", "pk": genre["id"], "fields": {"name": genre["name"], "like_users": []}}
    genres_a.append(data)
    
with open('genre.json', 'w', encoding='utf-8') as f:
    json.dump(genres_a, f, ensure_ascii=False, indent='\t')