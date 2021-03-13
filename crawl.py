from targetPage import Element, TargetPage, Driver

page_names = ["", ""]
URLs = ['https://www.', 
        'https://www.']
class_names_for_waiting_loading_page = ['', '']
URL_tables = [[Element("//*[@id=\"\"]/div[3]/div[3]/table", "XPATH"), 2, 
                [Element("", "CLASS_NAME"), [-1, "기업명"], [-1, "홈페이지"]]],
              [Element("//*[@id=\"\"]/div[1]/table", "XPATH"), -1, 
                [Element("", "CLASS_NAME"), [0, "법인명"], [1, "홈페이지"]]]]
Pagings = [Element("//*[@id=\"\"]/div[3]/div[4]", "XPATH"),
          Element("//*[@id=\"\"]/div[2]", "XPATH")]
start_page = [1, 11]

target_pages = []
driver = Driver('../chromedriver.exe')
for i in range(len(URLs)-1, -1, -1):
  class_name_for_waiting_loading_page = class_names_for_waiting_loading_page[i]
  target_page = TargetPage(page_names[i], driver, URLs[i], Element(class_name_for_waiting_loading_page, "CLASS_NAME"), 
                          URL_tables[i], Pagings[i], start_page[i])
  target_pages.append(target_page)

for target_page in target_pages:
    target_page.OpenPage()
    # 이후 ref-1을 참고해서 웹 페이지가 잘 열렸는지 확인하고 다음 step 진행하기
    if not target_page.CheckPageLoadingDone():
      print(target_page.name, "페이지 명시적 대기 실패")
    else:
      # 홈페이지가 있는 기업들 및 해당 url들을 추출한다
      target_page.ExportURLs()
    