import requests
import json, csv

# key
moviedb_key = "893975ab9d270ba1a8a8c1b31e213386"

# keys
keys = ['adult', 'original_language', 'original_title', 'overview', 
                'release_date', 'revenue', 'runtime', 'tagline', 'title', 
                'genres', 'casts', 'role_data', 'director']
movies = []
casts = []
directors = []

# 배우, 감독은 후에 파일 조작으로 중복 제거
# 장르는 따로 받아와서 한 번에 생성

for i in range(1, 6):
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={moviedb_key}&language=ko-KR&page={i}"
    response = requests.get(url).json()
    lists = response['results']
    for movie in lists:
        detail_url = f"https://api.themoviedb.org/3/movie/{movie['id']}?api_key={moviedb_key}&language=ko-KR"
        movie_info = requests.get(detail_url).json()
        
        fields = {}
        for key in keys[:-4]:
            fields[key] = movie_info[key]
        for key in keys[-4: -1]:
            fields[key] = []
        fields['director'] = "-"
        fields['like_users'] = []
        
        # genres
        tmp = []
        for genre in movie_info['genres']:
            tmp.append(genre['id'])
        fields['genres'] = tmp
            
        # director, casts
        credit_url = f"https://api.themoviedb.org/3/movie/{movie['id']}/credits?api_key={moviedb_key}"
        response = requests.get(credit_url).json()
        casts_p = response['cast'][:5]
        crews = response['crew']
        director = ''
        for crew in crews:
            if crew["job"] == "Director":
                fields["director"] = crew["id"]
                directors.append({"model": "movies.director", "pk": crew["id"], "fields": {"name": crew["name"], "like_users": []}})
                break
        tmp = []
        for cast in casts_p:
            casts.append({"model": "movies.cast", "pk": cast["id"], "fields":{"name": cast['name'], "like_users": []}})
            tmp.append(cast['id'])
        fields['casts'] = tmp
        fields['role_data'] = casts_p
        
        movie = {"model": "movies.movie", "pk": movie_info["id"], "fields": fields}
        movies.append(movie)
        
        # 최초 쓰기
        with open('casts1.json', 'w', encoding='utf-8') as f:
            json.dump(casts, f, ensure_ascii=False, indent="\t")
        # with open('directors.json','w', encoding='utf-8') as f:
        #     json.dump(directors, f, ensure_ascii=False, indent="\t")
        # with open('movies2.json','w', encoding='utf-8') as f:
        #     json.dump(movies, f, ensure_ascii=False, indent="\t")
                
        # 추가
        # with open('casts.json', 'a', encoding='utf-8') as f:
        #     for cast in casts:
        #         json.dump(cast, f, ensure_ascii=False, indent="\t")
        # with open('directors.json','a', encoding='utf-8') as f:
        #     for director in directors:
        #         json.dump(director, f, ensure_ascii=False, indent="\t")
        # with open('movies.json','a', encoding='utf-8') as f:
        #     for movie in movies:
        #         json.dump(movie, f, ensure_ascii=False, indent="\t")






















# movie는 json으로, casts는 중복 제거 위해     
# 처음 파일 생성시에만        
# with open(f'movie1.csv', 'w', encoding='utf-8', newline='') as f:    
#     write = csv.DictWriter(f, fieldnames=keys)
#     write.writeheader()
#     for movie in movies:
#         write.writerow(movie)
# with open(f'cast1.csv', 'w', encoding='utf-8', newline='') as f:    
#     write = csv.DictWriter(f, fieldnames=['id', 'name'])
#     write.writeheader()
#     for cast in casts:
#         write.writerow(cast)
# with open(f'director.csv', 'w', encoding='utf-8', newline='') as f:    
#     write = csv.DictWriter(f, fieldnames=['id', 'name'])
#     write.writeheader()
#     for director in directors:
#         write.writerow(director)
        
# 추가할 때
# with open(f'movie1.csv', 'a', encoding='utf-8', newline='') as f:
#     write = csv.DictWriter(f, fieldnames=keys)
#     for movie in movies:
#         write.writerow(movie)
# with open(f'cast1.csv', 'a', encoding='utf-8', newline='') as f:
#     write = csv.DictWriter(f, fieldnames=['id', 'name', 'character', 'profile_path'])
#     for cast in casts:
#         write.writerow(cast)
# with open(f'director.csv', 'a', encoding='utf-8', newline='') as f:    
#     write = csv.DictWriter(f, fieldnames=['id', 'name'])
#     for director in directors:
#         write.writerow(director)
    
        
    
        
# https://api.themoviedb.org/3/movie/283995?api_key=893975ab9d270ba1a8a8c1b31e213386&language=ko-KR
        