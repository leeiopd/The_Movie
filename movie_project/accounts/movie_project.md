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