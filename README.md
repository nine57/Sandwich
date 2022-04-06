# Making Sandwich
<br>

## 샌드위치 만들기와 재료 재고관리를 할 수 있는 API 서버.

- 재료 재고관리 : 빵, 토핑, 치즈, 소스의 목록을 조회하고 각각에 대한 정보를 수정 (이름, 재고, 가격)
- 샌드위치 만들기 : 재료를 선택하여, 샌드위치 정보를 생성(샌드위치 만들기)<br>
샌드위치는 각 재료마다 제한 조건이 있으며, 다음과 같습니다.
  - 빵 : 반드시 1개 선택
  - 토핑 : 1개 또는 2개 선택
  - 치즈 : 반드시 1개 선택
  - 소스 : 1개 또는 2개 선택
- 재료 선택에 따라 재고 정보가 +, - 되며 재료가격에 따라 샌드위치에 총 가격이 매겨집니다.

<br>

## :: 개발 환경

이 프로젝트는 다음의 환경에서 개발하였습니다.
- Python : 3.8.13
- Django : 4.0.3
- django-cors-headers : 3.11.0
- djangorestframework : 3.13.1
- drf-yasg : 1.20.0
- sqlite3 : django 내장

<br>

## :: API 명세

이 프로젝트는 Swagger를 통해 API 명세서를 확인할 수 있으며, endpoint는 다음과 같습니다.

- 재료별 GET, POST : 정보를 조회, 신규 등록
  - /ingredients/breads
  - /ingredients/cheeses
  - /ingredients/sauces
  - /ingredients/toppings
<br><br>
- 재료별 PATCH, DELETE (by 재료 id) : 해당하는 ID의 재료를 수정, 삭제<br>
삭제는 Database상의 완전한 삭제가 아닌 status의 변경으로 구현
  - /ingredients/bread/\<int:bread_id\>
  - /ingredients/cheese/\<int:cheese_id\>
  - /ingredients/sauce/\<int:sauce_id\>
  - /ingredients/topping/\<int:topping_id\>
<br><br>
- 샌드위치 리스트 GET, 샌드위치 신규 POST
  - /sandwiches
  - GET method는 다음의 query parameter key에 따라 리스트 조회가 가능합니다.
    - bread, cheese, topping, sauce 의 id값에 따라 filtering<br>
    - price : 양수는 값보다 큰 대상, 음수는 값보다 작은 대상을 조회
    - offset으로 pagination 설정 (default = 0)
    - limit에 따라 한번에 조회하는 대상 수 설정 (default = 10)
<br><br>
- 샌드위치 DELETE, 샌드위치의 재료 detail 정보 GET
  - /sandwiches/\<int:sandwiches_id\>

<br>

### - 해당 프로젝트를 테스트할 수 있는 더미 데이터가 있는 sqlite db file을 함께 업로드 했습니다.
> db.sqlite3