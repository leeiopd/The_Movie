### 0. Model migrate, DB 반영

* accounts > models.py

* moview > models.py

* makedb.py

* make_genredb.py

* base.html
  * bootstrap, web font, font awsome, axios 등 필요 요소 in
  * favicon : `05.13 3:30pm`
* Movie: poster_path, Cast: profile_path, Director: profile_path 추가 : `05.13 6pm`
* 평점 기본값 default_score로 넣어놓고 annotate한 score_avg가 없으면 대신 출력 : `05.14-05.15`
* 최종 DB : 

### 1. movies, review CRUD

* main page
  * review__score 내림차순으로 20개 정렬 (임시)
* create review
  * +) 임시저장 기능
* detail page
* delete review : `05.13 6:30pm`
* update review : `05.13 6:45pm`
* 리뷰 작성 한 번만 가능하도록 수정 : `05.14 9:30am`

#### Detail Page

* 리뷰 R > collapse 이용

  * 기본 collapse 구현 : `05.13 7:20pm`

* 코멘트 CRUD > axios 이용, 페이지 이동 없이 처리 
  * CR (axios) : `05.13 7:50pm`
  * D (axios) : `05.14 11:00am`
  * U (axios)
    * 수정 버튼을 누르면 - 댓글 내용을 form > input 태그로 바꿔주고 이벤트리스너를 등록해서 수정 요청이 날아가게 해야지. get은 필요 없겠다. 애초에 get 요청이 날아오지 않으니 view에서는 포스트 요청만 처리
  * 코멘트 CRUD 완성 : `05.14 4:50pm`

* Detail Page, Main Page 꾸미기 (기초) : `05.15 10:45am`

* 등급 아이콘 - navbar, review에서 확인 가능 : `05.15 5:40pm`

  * pawn(100) - rook(500) - knight(1000) - bishop(5000) - queen(10000) - king(50000)

  ```django
  <i class="fas fa-lg fa-chess-{% if user.profile.point >= 50000 %}king{% elif user.profile.point >= 10000 %}queen{% elif user.profile.point >= 5000 %}bishop{% elif user.profile.point >= 1000 %}knight{% elif user.profile.point >= 500 %}rook{% else %}pawn{% endif %}"></i>
  ```

* 댓글 수

  * 삭제 시 Eventlistner에서 innerText 변경 : `05.15 5:05pm`

* 댓글 작성 시 +10, 댓글 삭제 시 -10, 글 삭제 시 -100 넣기 : `05.15 6:30pm`

* 리뷰 작성자 구독하기 : `05.16 9:30am`

### Like

* movie, director, cast 좋아요 : `05.15 2:00pm`
  * 내 영화 / 내 감독 / 내 배우 페이지에서 확인 가능
* 리뷰 좋아요, 코멘트 좋아요 : `05.15 3:20pm`

### Main

* 명예의 전당 (평점 top 10, 리뷰수 top 10)
  * view done : `0515 6:30pm`
  * template done : `0515 10:50am`
* 내 장르 영화 추천 / 내 배우 영화 추천 / 내 감독 영화 추천
  * view done : `0515 7:50pm`
  * template done : `0515 10:50am`
* 내가 구독한 사람이 좋아하는 영화
  * view, template done : `0515 10:50am`

### Movie List

* left bar
  * genre filter : `0516 12:15pm`
  * 평점 filter : `0516 12:15pm`
* [django-bootstrap pagination](<https://github.com/jmcclell/django-bootstrap-pagination>)

### Search

* 검색 기능 : `0516 2:00pm`
