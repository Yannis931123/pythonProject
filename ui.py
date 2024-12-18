from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 创建 Edge WebDriver 实例，不指定 executable_path，因为已经设置在系统变量中
driver = webdriver.Edge()

try:
    # 打开指定的网页
    driver.get('https://www.baidu.com')

    # 等待几秒钟以加载页面（可选）
    time.sleep(5)

    # 示例：查找搜索框并输入内容（这里需要根据实际网页元素调整）
    # 假设网页上有一个 name 属性为 'q' 的输入框作为搜索框
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('Selenium WebDriver')
    search_box.send_keys(Keys.RETURN)

    # 再次等待几秒钟以查看搜索结果
    time.sleep(500)

finally:
    # 关闭浏览器
    driver.quit()