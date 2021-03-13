# web-crawler-with-selenium
python selenium 모듈을 이용하여 구현한 웹 크롤러

# 목적
1. 해당 프로그램은 웹 크롤러입니다.
2. 웹 크롤러를 만들 수 있는 언어 중에서 제가 가장 간편하게 사용할 수 있는 언어가 Python이기에 해당 언어를 채택하였습니다.
3. 특정 페이지에서 여러 페이지들을 순회하면서 필요한 정보들을 얻습니다.
4. 본 프로그램은 해당 페이지에서 "홈페이지"를 가지고 있는 "회사"들의 리스트를 csv 파일로 저장합니다.
5. 해당 프로그램에서 실제로 사용한 url 등은 제거한 상태로 git에 올렸기 때문에 사용을 위해서는 일부 수정이 필요합니다.
![image](https://user-images.githubusercontent.com/46051622/111030600-87737500-8446-11eb-9f73-4abff7cd1eec.png)
6. 위 이미지는 크롤러 실행 출력 결과를 중간에 저장한 내용입니다.
7. 기본적으로 기업명을 확인하고, 추가적으로 홈페이지를 가지고 있을 경우에 해당 url도 추출합니다.
8. Go to the next page는 다음 페이지로 넘어갈때 출력된 문장입니다.
9. 최종적으로는 홈페이지를 가지고 있는 회사들의 리스트를 csv 파일로 저장합니다.
![image](https://user-images.githubusercontent.com/46051622/111030712-20a28b80-8447-11eb-81af-ef4f819f169b.png)

# 파일 구조
1. 크게 2개의 파일을 가지고 있습니다.
   1. targetPage.py: 핵심 기능들을 가지고 있는 함수들이 구현되어 있습니다.
   2. crawl.py targetPage.py 내 구현되어 있는 함수들을 호출하는 파일입니다.

# crawl.py
![image](https://user-images.githubusercontent.com/46051622/111030874-f4d3d580-8447-11eb-84ae-d94c9bc042c2.png)
1. 3번~13번은 사용자가 실제로 주는 입력값들의 모음입니다.
   1. page_names = 첫 시작 페이지들의 이름입니다.
   2. URLs = 첫 시작 페이지들의 url입니다.
   3. class_name_for_waiting_loading_page = 첫 시작 페이지들이 제대로 로딩되었는지의 여부는 해당 클래스 이름이 html에서 존재하는 지에 대한 여부로 결정합니다.
   4. URL_table = 각 기업들의 소개 페이지들의 모음 table의 위치를 가리킵니다.
      1. Element라는 targetPage.py에서 새로 정의한 클래스로 html 요소 표현 방식(CLASS_NAME, XPATH)을 정의합니다.
      2. 또한 각 기업 소개 페이지로 이동하였을 경우 회사이름과 홈페이지가 해당 페이지 내의 몇번째 테이블에 있는지와 해당 테이블 내 어떤 th 요소명인지에 대한 정보가 있습니다.
      3. 만약 테이블 인덱스 값이 음수일 경우에는 첫번째 테이블에 모든 정보가 있다고 프로그램은 판단합니다.
   5. Pagings = 각 기업들의 소개 페이지 번호를 이동시킬 수 있는 번호 요소 위치입니다. (홈페이지 맨 밑의 1 2 3 4 5 6 7 8 9 10 > >> 와 같은 요소입니다)
   6. start_page = 각 시작 페이지들의 시작 페이지 번호를 가리킵니다.
2. 15~21번은 위에서 입력한 사용자들의 입력값들을 TargetPage라고 하는 targetPage.py에 정의한 클래스에 저장합니다.
   1. 16번은 selenium의 webdriver 기능을 사용하기 위해 필요한 실행 파일의 위치를 Driver라고 하는 targetPage.py에 정의한 클래스에 저장합니다.

![image](https://user-images.githubusercontent.com/46051622/111031253-d5d64300-8449-11eb-84bf-7c47d06b75c4.png)

3. 23~30번은 실제로 페이지를 열어서 웹 페이지가 제대로 열릴때까지 대기한 다음에 정보를 추출하는 동작을 실행합니다.
4. 39번부터는 크롤러의 핵심 기능들을 가지고 있는 TargetPage 클래스를 정의하고 있습니다.

![image](https://user-images.githubusercontent.com/46051622/111031482-1edac700-844b-11eb-968f-d2ef6d49a056.png)

5. 40~47번은 클래스 init 함수입니다. 사용자가 입력한 정보들을 저장합니다.
6. 49~50번은 웹 페이지를 여는 함수입니다.

![image](https://user-images.githubusercontent.com/46051622/111031551-72e5ab80-844b-11eb-9c28-cdfbd3524859.png)

7. 52~62번은 웹 페이지가 끝까지 로딩이 되었는지 확인하는 함수입니다.

# targetPage.py
![image](https://user-images.githubusercontent.com/46051622/111031292-306f9f00-844a-11eb-8210-d5db717d3471.png)
1. 23~37번은 각각 selenium의 webdriver를 가리키는 Driver 클래스와 HTML 요소 위치를 저장하는 Element 클래스의 정의하고 있습니다.
2. 64~115번은 각 회사 소개 페이지로 이동하여 해당 페이지의 HTML 테이블에서 회사명과 홈페이지를 찾는 함수입니다.

![image](https://user-images.githubusercontent.com/46051622/111031650-f1dae400-844b-11eb-859a-5eac49448e82.png)

3. 65~81번은 각 회사 소개 페이지로 이동하기 위해 해당 페이지 이동 버튼을 클릭하는 함수입니다.
4. selenium 의 click 함수가 가끔 동작이 안되는 문제가 있어 send_keys 함수를 사용하였습니다.
5. td 등과 같이 키보드 interactable 하지 않은 요소들에 대해서는 직접 js 스크립트 구문을 실행하도록 하여 click 하였습니다.
6. 최대 10번 대기합니다.

![image](https://user-images.githubusercontent.com/46051622/111031953-67937f80-844d-11eb-944a-f30484938719.png)

7. 82~115번은 이동한 회사 소개 페이지 내 HTML 테이블에서 회사명과 홈페이지를 찾습니다.
8. 85번 for 루프 인덱스 i가 1일때는 회사이름, 2일때는 회사 홈페이지를 찾습니다.
9. table > tbody > tr > th > td 순으로 HTML 태그를 탐색하면서 해당 정보들을 찾습니다.
10. 100~106번은 프로그램 중간 실행 결과를 print하기 위한 문자열 처리 과정을 정의하고 있습니다.
11. 실제로 회사명과 홈페이지를 모두 찾으면 url_list 변수에 추가하여 이를 리턴합니다.

![image](https://user-images.githubusercontent.com/46051622/111032121-1b950a80-844e-11eb-8399-735d19e5934c.png)

12. 117~127번은 회사 소개 페이지 내에서 회사명과 홈페이지를 찾는 GetUrlFromTable 함수를 호출하고, 다시 뒤로 가서 회사 소개 페이지 리스트 화면으로 가는 함수입니다.
13. 129~148번은 회사 소개 페이지 리스트 화면에서 각 회사들의 소개 페이지로 가는 HTML 버튼을 찾는 함수입니다.
14. 함수 인자 i는 현재 회사 소개 페이지 리스트 화면에서 몇번째 회사까지 확인했는지를 가리키는 변수입니다.
15. 134~135번에서 인자 i 값과 회사 소개 페이지 리스트 갯수를 비교하여 현재 화면에서 모든 회사를 확인했다고 판단이 되면 None을 리턴합니다.
16. 137~145번은 본 프로젝트에서 탐색한 특정 페이지의 특징을 반영한 코드이며, 회사 소개 페이지 리스트 화면에서 회사 소개 페이지를 가지고 있지 않은 HTML 버튼의 여부를 판단하여 skip하는 부분입니다.
17. 147~148번은 정상적으로 회사 소개 페이지로 갈 수 있는 HTML 요소를 리턴합니다.

![image](https://user-images.githubusercontent.com/46051622/111032353-184e4e80-844f-11eb-955c-becf4a139e5f.png)

18. 150~185번은 회사 소개 페이지 리스트 화면 페이지 번호를 1씩 증가시키는 함수입니다. ( 1 2 3 4 5 6 7 8 9 10 > >> )
19. 만약 현재 번호 리스트 내에서 클릭해야 하는 상황(위의 예시에서 1~10)이면, 155~167번 코드를 통해 해당 번호를 클릭하고 True를 리턴합니다.
20. 만약 다음 번호 리스트로 이동해야 하는 상황(위의 예시에서 >)이면, 169~183번 코드를 통해 해당 화살표 버튼을 클릭하고 True를 리턴합니다.
21. 만약 현재 페이지가 마지막 페이지이면 185번 코드를 통해 False를 리턴합니다.

![image](https://user-images.githubusercontent.com/46051622/111032440-a0ccef00-844f-11eb-9bd0-672cc26982af.png)

22. 188~228번은 위에서 정의한 함수들을 호출하여 현재 시작 페이지에서 홈페이지를 가지고 있는 모든 회사들을 확인하여 csv 파일에 저장하는 함수입니다.
23. 195~197번은 사용자가 입력한 시작 페이지로 이동하는 함수입니다.
24. 203~217번은 현재 회사 소개 페이지 리스트 화면에 있는 회사들을 전부 순회하여 홈페이지를 가지고 있는 회사들을 exported_urls 변수에 저장합니다.
25. 219~224번은 exported_urls 변수에 있는 값들을 csv 파일에 저장합니다. 즉 회사 소개 페이지 리스트 내 회사들을 전부 순회할때마다 csv 파일에 저장합니다.
26. 227~228번은 다음 회사 소개 페이지 리스트 화면으로 이동하는 함수입니다. 만약 현재 회사 소개 페이지 리스트 화면이 마지막이면 해당 함수를 종료합니다.

# 아쉬운 점
1. targetPage.py는 사용자 입력과 독립적으로 실행될 수 있도록 하고 싶었으나, 결과적으로 본 프로젝트에서만 사용할 수 있는 python 파일입니다.
2. 좀 더 다양한 프로젝트에 사용하면서 해당 프로그램을 개선할 예정입니다.
3. 이후 개선 작업과 함께 주석 작업도 진행하여 README에 코드 설명이 줄어들도록 할 예정입니다.

# 코드 사용 관련 이슈
1. BeautifulSoup -> selenium : 처음에 BeautifulSoup 모듈을 사용했으나, 본 프로젝트에서는 웹 상에서 버튼 클릭과 같은 이벤트를 통해 여러 페이지를 순회해야 하기 때문에 selenium 모듈 사용
2. selenium 모듈의 click 함수가 동작을 안하는 경우가 있어서 대신에 send_keys 함수를 사용, 해당 함수를 사용하지 못하는 요소에 대해서는 직접 js script를 호출하여 click 이벤트를 처리 (targetPage.py의 65~71번)
3. 본 프로젝트에서 회사 소개 페이지 이동이 안되는 경우를 테이블의 특정 요소 값을 통해 판단하고 있으나 display:None 속성이기 때문에 innerHTML 요소를 통해 특수 처리 진행함 (targetPage.py의 140번)

# 새로 배운 내용
1. 개발자 모드를 통한 웹 요소들의 기본적인 탐색 방법 - getElementByClassName, getElementByXpath, getElementByTagName 등등
2. 개발자 모드에서의 기본적인 js 디버깅 실행 - 테이블 내 특정 요소 값을 통해 페이지 로딩을 안하는 경우를 확인함 (targetPage.py의 143번 줄에 적용)

# 구현 중 작성한 공부 내용 정리
1. https://dream-winter.tistory.com/14

# 참고
1. python selenium 기본 사용 방법 정리 - https://greeksharifa.github.io/references/2020/10/30/python-selenium-usage/
2. selenium 테이블 크롤링 방법 - https://minjoos.tistory.com/5
3. selenium 에서 특정 element가 갑자기 클릭이 안될때 - https://wkdtjsgur100.github.io/selenium-does-not-work-to-click/
4. 그 외 발생한 자잘한 이슈들을 참고하기 위해 많은 글들을 참고하였으나 미처 정리를 다 하지 못했습니다.
