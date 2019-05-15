import requests
import json, csv

# key
moviedb_key = "893975ab9d270ba1a8a8c1b31e213386"

# keys
keys = ['adult', 'original_language', 'original_title', 'overview', 'vote_average',
                'release_date', 'revenue', 'runtime', 'tagline', 'title', 
                'genres', 'casts', 'role_data', 'director', 'poster_path']
movies = []
casts = []
directors = []

# 장르는 따로 받아와서 한 번에 생성

for i in range(1, 100):
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={moviedb_key}&language=ko-KR&page={i}"
    response = requests.get(url).json()
    lists = response['results']
    for movie in lists:
        detail_url = f"https://api.themoviedb.org/3/movie/{movie['id']}?api_key={moviedb_key}&language=ko-KR"
        movie_info = requests.get(detail_url).json()
        
        fields = {}
        for key in keys[:-5]:
            fields[key] = movie_info[key]
        for key in keys[-5: -2]:
            fields[key] = []
        fields['director'] = "-"
        fields['like_users'] = []
        if movie_info['poster_path']:
            poster_path = "https://image.tmdb.org/t/p/w600_and_h900_bestv2/" + movie_info['poster_path']
        else:
            poster_path = ""
        fields['poster_path'] = poster_path
        
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
                if crew['profile_path']:
                    profile_path = "https://image.tmdb.org/t/p/w600_and_h900_bestv2/" + crew['profile_path']
                else:
                    profile_path = ""
                directors.append({"model": "movies.director", "pk": crew["id"], "fields": {"name": crew["name"], "profile_path":profile_path, "like_users": []}})
                break
        tmp = []
        for cast in casts_p:
            if cast['profile_path']:
                profile_path = "https://image.tmdb.org/t/p/w600_and_h900_bestv2/" + cast['profile_path']
            else:
                profile_path = ""
            casts.append({"model": "movies.cast", "pk": cast["id"], "fields":{"name": cast['name'], "profile_path": profile_path, "like_users": []}})
            tmp.append(cast['id'])
        fields['casts'] = tmp
        fields['role_data'] = casts_p
        
        movie = {"model": "movies.movie", "pk": movie_info["id"], "fields": fields}
        movies.append(movie)
        
        # 최초 쓰기
        with open('casts10.json', 'w', encoding='utf-8') as f:
            json.dump(casts, f, ensure_ascii=False, indent="\t")
        with open('directors10.json','w', encoding='utf-8') as f:
            json.dump(directors, f, ensure_ascii=False, indent="\t")
        with open('movies10.json','w', encoding='utf-8') as f:
            json.dump(movies, f, ensure_ascii=False, indent="\t")
                
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
        