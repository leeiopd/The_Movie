# movie_project

##   - accounts_app

#### 1. 1일차

* movie DB 완료 후부터 시작
* 계정 관련 동작 및 페이지 구현
  * signup
  * signin
  * logout
* Profile 수정 페이지 구현
  * 회원가입(signup) 후, 자동 로그인
  * 최초 로그인 시, 프로필 작성 페이지 호출
* Profile 조회 페이지 간이 구현





#### 2. 2일차

* subscibe 관련 기능 및 페이지 구현
  * subscribe 기능
  * 구독자 수 조회, 구독자 리스트 조회
  * 구독 수 조회, 구독 리스트 조회
* 프로필 수정창에서 좋아하는 장르 수정 페이지의 중간 링크 페이지 구현
  * profileTogenre 페이지
  * 좋아하는 장르 설정 유도
    * YES  -> 장르 설정 페이지
    * No -> 유저 프로필 페이지
* 내 정보 조회 페이지와 다른 유저 정보 조회 페이지 통합
  * userInfo 페이지로 통합
  * 정보 수정 페이지 수정
    * url 정리
    * 함수 명 통일화
* likes 관련 페이지 구현
  * 기능 구현은 movies_app 에서 구현
  * <user_id>/likes/casts - 페이지
    * 좋아하는 배우 리스트 조회
  * <user_id>/likes/directors - 페이지
    * 좋아하는 감독 리스트 조회

* 추가 예정
  * accounts 페이지 진입시, accounts 전용 세로 navbar 구현
  * 각 페이지 디테일 및 디자인

#### 3. 3일차

* profile 기능 및 페이지 구현 완료
  * My page와 타 유저 정보 페이지의 구분
    * My page
      * My page
      * 새 피드 확인 ( 로그인 유저 전용 my page 기능)
      * 구독
      * 구독자 목록
      * 나의 추천 영화
      * 나의 장르 추천 영화
      * 나의 배우 추천 영화
      * 나의 감독 추천 영화
    * 타 유저의 정보 페이지
      * 유저 정보
      * 구독 목록
      * 구독자 리스트
      * 유저 추천 영화
      * 유저 장르 추천영화
      * 유저 배우 추천영화
      * 유저 감독 추천영화
* 유저의 개인 페이지의 추천영화 관련은 모두 4개의 영화를 평점순으로 추천
* 구독ㅡ 구독자 관련 페이지
  * 유저 리스트를 간단 정보와 함께 호출
    * ID
    * level
    * point
    * review
    * comment
    * 상세 정보 바로가기 버튼
  * 추가적으로 user 정보의 순서를 POINT 순으로 나타낼수 있으면 좋을듯
* CSS 적용
* 추가 필요 기능(가능하다면)
  * 감독 전용 페이지
  * 배우 전용 페이지
  * 구독 버튼



#### 4. 4일차

* Rank 페이지 구현
  * 유저 구독 목록 페이지에서 접속 가능
  * 유저의 point 순위 정렬 페이지
  * 포인트가 높은 유저들을 구독을 유도 함으로서 정보 공유 유도
* 구독 버튼 변경
  * 구독, 구독자 페이지에서도 구독 버튼 활성화
  * 버튼 css적용
* 디테일 CSS적용





#### 5. 완성

* 기능
  * accounts_app
    * user_info - 유저 정보 조회(accounts_app의 main 페이지)
    * signup - 회원가입
    * updateUser - 프로필 작성/수정
    * profileTogenre - 프로필 작성/수정 후 장르 취향 정보 입력 유도
    * updateGenre - 장르 작성/수정
    * login - 로그인
    * logout - 로그아웃
    * subscribe - 구독기능
    * subscribeList - 구독한 유저 조회
      * 페이지 내에서 구독 및 유저 정보 조회 가능
    * subscriberList - 구독하고 있는 유저 조회
      * 페이지 내에서 구독 및 유저 정보 조회 가능
    * feed - 내가 구독하고 있는 유저의 최신 review 조회
    * favoritesCasts - 좋아하는 배우의 영화 리스트 조회
      * 영화 포스터를 통해 영화 detail페이지로 이동
    * favoritesDirectors - 좋아하는 감독의  영화 리스트 조회
      * 영화 포스터를 통해 영화 detail페이지로 이동
    * favoritesGenres - 좋아하는 배우 리스트 조회
      * 영화 포스터를 통해 영화 detail페이지로 이동
    * favoritesMovies - 좋아하는 영화 리스트 조회
      * 영화 포스터를 통해 영화 detail페이지로 이동
    * reviewsList - 작성한 리뷰 리스트
    * rank - 전체 유저 랭킹 리스트
      * 구독기능 사용 유도
      * 페이지 내 구독 기능 사용 가능
    * 추가 - 유저 정보 페이지에서 sidebar를 이용하여 접근 가능