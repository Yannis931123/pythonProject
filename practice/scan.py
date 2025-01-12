from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from keys import log_in, create_program, edit_program, delete_program,create_task,edit_task,delete_task

driver = webdriver.Edge()
driver.get("http://cube-front.product.poc.za-tech.net")

# 登录页面
log_in(driver)

# 获取cookies
# cookies = driver.get_cookies()
# print(cookies)

# 创建扫描方案
# create_program(driver)

# 编辑方案
# edit_program(driver)

# 删除方案
# delete_program(driver)

# 创建扫描任务并执行
# create_task(driver)

# 编辑扫描任务并编辑质量门禁
# edit_task(driver)

# 删除扫描任务
delete_task(driver)

driver.quit()
