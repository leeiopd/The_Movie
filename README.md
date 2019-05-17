# The Movie

## 0. 팀원 정보 및 업무 분담 내역

### * 이주호

* API
* app accounts
  * user_info - 유저 정보 조회(accounts_app의 main 페이지)
  * 회원가입, 로그인, 로그아웃
  * 프로필 작성, 수정
  * Like(좋아요) : 장르
  * Subscribe(구독)
  * user 조회
    * 구독한 유저
    * 나를 구독하는 유저
  * feed
    * 내가 구독하는 유저의 최신 review 조회
  * 영화 목록
    * 좋아하는 배우 / 감독의 영화 목록
    * 좋아하는 영화 목록
  * 작성한 리뷰 리스트
  * 전체 유저 랭킹 페이지
    * 구독 유도
    * 페이지 내 구독(vue.js, axios 사용) 가능
  * 유저 정보 페이지에서 sidebar 이용, 페이지 접근 가능

### * 김희윤

* Modeling, DB 생성
* settings.py, base.html
* app movies
  * review CRUD
  * comment CRUD, Like(좋아요)
    *  `Vue.js`, `axios`를 이용한 single page 동작. 
    * 실시간 댓글 수 확인, 좋아요.
  * Like(좋아요) : 영화, 감독, 배우
  * Main page : 영화 추천 `user가 아직 review를 작성하지 않은 영화` 중 특정 조건을 기준으로 추천
    * 사용자 평점 기준 movie top 10 추천
    * 사용자 리뷰 수 기준 movie top 10 추천
    * themoviedb 평점 기준 movie top 10 추천 (현재 자체 user db가 부족해 themoviedb 참고)
    * 사용자가 좋아하는 `장르`의 영화 themoviedb 평점 기준 top 10 추천
    * 사용자가 좋아하는 `배우`가 출연한 영화 themoviedb 평점 기준 top 10 추천
    * 사용자가 좋아하는 `감독`이 연출한 영화 themoviedb 평점 기준 top 10 추천
    * 사용자가 구독한 `user`가 좋아하는 영화 themoviedb 평점 기준 top 10 추천
  * List page : `pagination` 구현
    * 전체 영화 목록(약 2,000개)
    * `score` 필터 - side bar
    * `genre` 필터 - side bar
    * `검색` - 상단 navbar
  * Search
    * 검색어를 `original title`, `title`, `director`, `cast` 에서 찾아 결과 제공

## 1. 목표 서비스 구현 및 실제 구현 정도(핵심 기능)

* 영화 정보 제공 `v`
* 영화 리뷰, 리뷰 댓글 `v`
* 영화, 감독, 배우, 장르 Like `v`
* 리뷰, 댓글 Like `v`
* 리뷰어 구독 `v`
* 좋아요, 구독 기반 영화 추천 서비스 `v`
* 영화 목록 필터 (점수, 장르 기준) `v`
* 영화 검색 기능(제목, 원제목, 감독, 배우) `v`
* 리뷰, 코멘트 작성 포인트 시스템. 등급 아이콘. `v`

* 관리자 페이지 `v`

## 2. 데이터베이스 모델링

* ERD



## 3. 배포 서버 URL

* [URL]()

  



