import threading

import csv

from collections import defaultdict

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.keys import Keys

from urllib.request import urlopen
from lxml import etree

class Driver:
    def __init__(self, webdriver_executable_path):
        self.driver = webdriver.Chrome(executable_path=webdriver_executable_path)

class Element:
    def __init__(self, element_indicator, indicator_type):
        self.element_indicator = element_indicator
        self.indicator_type = indicator_type

    def GetElement(self, driver):
        if self.indicator_type == "XPATH":
            return driver.driver.find_element_by_xpath(self.element_indicator)
        elif self.indicator_type == "CLASS_NAME":
            return driver.driver.find_element_by_class_name(self.element_indicator)
        return None

class TargetPage:
    def __init__(self, name, driver, target_url, element_for_waiting_page_loading, URL_table, paging, start_page):
        self.name = name
        self.driver = driver
        self.target_url = target_url
        self.element_for_waiting_page_loading = element_for_waiting_page_loading
        self.URL_table = URL_table
        self.paging = paging
        self.start_page = start_page

    def OpenPage(self):
        self.driver.driver.get(url=self.target_url)

    def CheckPageLoadingDone(self, target_element = None):
        try:
            target_element = self.element_for_waiting_page_loading if target_element == None else target_element
            if target_element.indicator_type != "CLASS_NAME":
                return False
            WebDriverWait(self.driver.driver, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, target_element.element_indicator))
            )
            return True
        except:
            return False

    def GetUrlFromTable(self, clickable, target_table, send_keys, cur_index, clickable_info):
        if send_keys:
            clickable.send_keys(Keys.ENTER)
        else:
            js = "document.getElementsByClassName('companyListTbody')[0].getElementsByTagName('tr')[" + \
                str(cur_index - 1) + "]." + \
                "getElementsByTagName('td')[3].click()"
            self.driver.driver.execute_script(js)

        # 대기
        click_cnt = 1
        while click_cnt < 10 and self.CheckPageLoadingDone(target_table[0]) == False:
            if send_keys:
                clickable.send_keys(Keys.ENTER)
            else:
                self.driver.driver.execute_script(js)
        if click_cnt >= 10:
            print(target_table[0].element_indicator, "명시적 대기 실패")
        else:
            url_list = []

            for i in range(1, 3):
                index, name = target_table[i]
                table = target_table[0].GetElement(self.driver)
                if index >= 0:
                    table = (table.find_elements_by_tag_name("table"))[index]

                # 해당 테이블에서 정보 찾기
                name_found = False
                tbody = table.find_element_by_tag_name("tbody")
                rows = tbody.find_elements_by_tag_name("tr")
                for row in rows:
                    th = row.find_element_by_tag_name("th")
                    if th.text == name:
                        td = row.find_element_by_tag_name("td")
                        if len(td.text) > 0:
                            if i == 1:
                                print(str(clickable_info[1]) + ".", name, ":", end=' ')
                            else:
                                print("(", end='')
                            print(td.text, end='')
                            if i != 1:
                                print(")", end='')
                            url_list.append(td.text)
                        name_found = True
                        break

                if not name_found:
                    print(name, "찾기 실패")
                    return
            print()
            return url_list

    def GetUrl(self, clickable, target_table, send_keys, cur_index, clickable_info):
        url_list = self.GetUrlFromTable(clickable, target_table, send_keys, cur_index, clickable_info)

        # 뒤로 가기
        self.driver.driver.back()

        # 대기
        if self.CheckPageLoadingDone() == False:
            print(self.element_for_waiting_page_loading.element_indicator, "명시적 대기 실패")

        return url_list

    def GetClickableElement(self, table_element, i, url_index):
        table = table_element.GetElement(self.driver)
        tbody = table.find_element_by_tag_name("tbody")
        rows = tbody.find_elements_by_tag_name("tr")

        if len(rows) <= i:
            return None

        if url_index < 0:
            js = "return document.getElementsByClassName('companyListTbody')[0].getElementsByTagName('tr')"
            js += "[" + str(i) + "]."
            js += "getElementsByTagName('td')[1].innerHTML"
            submit_status = self.driver.driver.execute_script(js)

            if int(submit_status) != 2:
                print(str(i+1) + ". skipped status = ", submit_status)
                return "skip"

        return rows[i].find_elements_by_tag_name("td")[4] if url_index < 0 \
            else rows[i].find_elements_by_tag_name("td")[url_index].find_element_by_tag_name("a")

    def GoNextPage(self):
        paging = self.paging.GetElement(self.driver)
        num = paging.find_element_by_class_name("num")
        current_page = num.find_element_by_class_name("on").text

        pages = num.find_elements_by_tag_name("a")
        for page in pages:
            if page.text == str(int(current_page) + 1):
                print("Go to the next page: ", str(int(current_page) + 1))
                page.send_keys(Keys.ENTER)
                while True:
                    paging = self.paging.GetElement(self.driver)
                    num = paging.find_element_by_class_name("num")
                    current_page1 = num.find_element_by_class_name("on").text
                    if current_page1 == str(int(current_page) + 1):
                        break
                    threading.sleep(5)
                return True
        
        btns = paging.find_elements_by_class_name("btn")
        for btn in btns:
            href = btn.find_element_by_tag_name("a").get_attribute("href")
            page = href.split("#")[-1]
            if page == str(int(current_page) + 1):
                print("Go to the next page: ", str(int(current_page) + 1))
                btn.find_element_by_tag_name("a").send_keys(Keys.ENTER)
                while True:
                    paging = self.paging.GetElement(self.driver)
                    num = paging.find_element_by_class_name("num")
                    current_page1 = num.find_element_by_class_name("on").text
                    if current_page1 == str(int(current_page) + 1):
                        break
                    threading.sleep(5)
                return True

        return False
        

    def ExportURLs(self):
        table_element, url_index, target_table = self.URL_table
        
        # 테이블 크롤링
        i = 0
        ii = 0

        for j in range(self.start_page - 1):
            i += 10
            self.GoNextPage()

        while True:  
            exported_urls = defaultdict(list)

            # 테이블 크롤링
            while True:
                clickable = self.GetClickableElement(table_element, ii, url_index)
                if clickable == "skip":
                    i += 1
                    ii += 1
                    continue
                if clickable == None:
                    ii = 0
                    break
                exported_url = self.GetUrl(clickable, target_table, url_index >= 0, ii + 1, [table_element, i + 1, url_index])
                if exported_url != None and len(exported_url) == 2:
                    name, url = exported_url
                    exported_urls[name].append(url)
                i += 1
                ii += 1
                
            with open('myResult.csv', 'a') as f:
                w = csv.writer(f)
                for k in exported_urls.keys():
                    for url in exported_urls[k]:
                        s = [k, url]
                        w.writerow(s)

            # 페이지 넘기기
            if not self.GoNextPage():
                break
