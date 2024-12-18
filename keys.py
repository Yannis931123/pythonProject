import json
import random
from time import sleep
import uuid

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 登录页面
def log_in(driver):
    driver.get("http://cube-front.product.poc.za-tech.net/magic/productScan/plan")
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "temppassword").send_keys("Admin@2024")
    driver.find_element(By.ID, "login-btn").click()
    sleep(2)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/button").click()
        sleep(1)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "//*[@id='container-space']/div/div[2]")
        driver.refresh()


# 创建扫描方案
def create_program(driver):
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//*[@id='app']/div/section/div/main/div/div[1]/div[2]/div[1]/button").click()
    loc1 = (By.XPATH, "//*[contains(text(),'创建扫描方案')]")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(loc1))
    driver.find_element(By.XPATH, "//*[@content='请输入']/div/input").send_keys("扫描方案" + str(get_number(8)))
    driver.find_element(By.XPATH, "//*[@content='请输入 设为默认']/div/span").click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@content='请输入']/div/textarea").send_keys("自动化创建扫描方案" + str(get_number(8)))
    driver.find_element(By.XPATH, "//*[@content='请输入 漏洞白名单']/div[2]/button").click()
    loc2 = (By.XPATH, "//*[@placeholder='请输入内容']")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(loc2))
    driver.find_element(By.XPATH, "//*[@placeholder='请输入内容']").send_keys("CVE-2024-0530")
    driver.find_element(By.XPATH, "//*[@id='app']/div/section/div/main/div/div[2]/div/div/section/div/div[3]/button[2]").click()
    sleep(2)


# 获取固定长度随机数
def get_number(length):
    num = random.randint(10 ** (length - 1), 10 ** length - 1)
    return num


# 编辑方案
def edit_program(driver):
    driver.find_element(By.XPATH, "//*[@id='app']/div/section/div/main/div/div[1]/div[3]/div[4]/div[2]/table/tbody/tr[1]/td[8]/div/div/a[1]").click()
    loc1 = (By.XPATH, "//*[contains(text(),'编辑扫描方案')]")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(loc1))
    sleep(1)
    # driver.find_element(By.XPATH, "//*[@content='请输入']/div/input").send_keys("扫描方案" + str(get_number(9)))
    driver.find_element(By.XPATH, "//*[@content='请输入 设为默认']/div/span").click()
    # time.sleep(1)
    # driver.find_element(By.XPATH, "//*[@content='请输入']/div/textarea").send_keys("自动化创建扫描方案")
    # driver.find_element(By.XPATH, "//*[@content='请输入 漏洞白名单']/div[2]/button").click()
    # loc2 = (By.XPATH, "//*[@placeholder='请输入内容']")
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located(loc2))

    driver.find_element(By.XPATH, "//*[text()=' 导入编号 ']/..").click()
    sleep(2)
    driver.find_element(By.XPATH, "//input[@type='file']").send_keys("D:\下载\文档下载\漏洞白名单模板 (3).xlsx")
    driver.find_element(By.XPATH, "//div[2]/div/div[2]/button[2]").click()
    driver.find_element(By.XPATH, "//*[@id='app']/div/section/div/main/div/div[2]/div/div/section/div/div[3]/button[2]").click()
    sleep(5)


# 删除方案
def delete_program(driver):
    driver.find_element(By.XPATH, "//*[@id='app']/div/section/div/main/div/div[1]/div[3]/div[4]/div[2]/table/tbody/tr[1]/td[8]/div/div/a[2]").click()
    text1 = "确定删除当前方案吗"
    loc = (By.XPATH, f"//*[contains(text(), '{text1}')]")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc))
    sleep(3)
    text2 = "确 定"
    driver.find_element(By.XPATH, f"//*[contains(text(), '{text2}')]/..").click()
    sleep(5)


# 新建扫描任务
def create_task(driver):
    driver.find_element(By.XPATH, "//span[contains(text(),'扫描任务')]/..").click()
    sleep(1)
    text1 = ' 创建 '
    driver.find_element(By.XPATH, f"//*[contains(text(),'{text1}')]/..").click()
    sleep(1)
    # driver.find_element(By.XPATH, "//*[@id='app'']/div/section/div/main/div/div[1]/div[2]/div[1]/button/span")
    text2 = '创建扫描任务'
    loc1 = (By.XPATH, f"//*[contains(text(),'{text2}')]")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(loc1))
    text3 = '所属节点 '
    driver.find_element(By.XPATH, f"//label[contains(text(), '{text3}')]/../div/div").click()
    sleep(1)
    text4 = 'artifact'  # 选择节点
    driver.find_element(By.XPATH, f"//span[contains(text(), '{text4}')]/..").click()
    text5 = '任务名称 '
    driver.find_element(By.XPATH, f"//label[contains(text(), '{text5}')]/../div/div/div/input").send_keys("自动化创建扫描任务" + str(get_number(6)))
    text6 = ' 添加 '
    driver.find_element(By.XPATH, f"//span[contains(text(), '{text6}')]/..").click()
    sleep(1)
    text7 = 'oasis'  # 仓库名称
    driver.find_element(By.XPATH, "//tbody/tr/td[1]/div/div/div/div/div/input").click()
    sleep(1)
    driver.find_element(By.XPATH, f"//span[contains(text(), '{text7}')]/..").click()
    text8 = 'cube-magic-gateway.jar'  # 制品名称
    driver.find_element(By.XPATH, "//tbody/tr/td[2]/div/div/div/div/div[1]/input").click()
    sleep(1)
    driver.find_element(By.XPATH, f"//span[contains(text(), '{text8}')]/..").click()
    text9 = '3.0'  # 制品版本
    driver.find_element(By.XPATH, "//tbody/tr/td[3]/div/div/div/div/div[1]/input").click()
    sleep(1)
    driver.find_element(By.XPATH, f"//span[contains(text(), '{text9}')]/..").click()
    # 仅保存
    # text10 = ' 仅保存 '
    # driver.find_element(By.XPATH, f"//span[contains(text(),'{text10}')]/..").click()
    # 保存并运行
    text10 = ' 保存并立即执行 '
    driver.find_element(By.XPATH, f"//span[contains(text(),'{text10}')]/..").click()
    sleep(5)


# 编辑扫描任务
def edit_task(driver):
    sleep(5)
    driver.find_element(By.XPATH, "//span[contains(text(),'扫描任务')]/..").click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='app']/div/section/div/main/div/div[1]/div[3]/div[5]/div[2]/table/tbody/tr[1]/td[10]/div/div/div[2]").click()
    loc1 = (By.XPATH, "//*[contains(text(),'编辑扫描任务')]")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(loc1))
    input_element = driver.find_element(By.XPATH, "//label[contains(text(), '任务名称')]/../div/div/div/input")
    driver.execute_script("arguments[0].value = '';", input_element)
    sleep(3)
    driver.find_element(By.XPATH, "//label[contains(text(), '任务名称')]/../div/div/div/input").send_keys("自动化创建扫描任务" + str(get_number(8)))
    sleep(3)
    # 打开质量门禁
    driver.find_element(By.XPATH, "//label[contains(text(),'质量门禁')]/../div/div/div").click()
    sleep(3)
    driver.find_element(By.XPATH, "//span[contains(text(),'严重')]/../../../../../td[3]/div/div/div/div/div/input").send_keys(get_number(3))
    driver.find_element(By.XPATH, "//span[contains(text(),'高危')]/../../../../../td[3]/div/div/div/div/div/input").send_keys(get_number(3))
    driver.find_element(By.XPATH, "//span[contains(text(),'中危')]/../../../../../td[3]/div/div/div/div/div/input").send_keys(get_number(3))
    driver.find_element(By.XPATH, "//span[contains(text(),'低危')]/../../../../../td[3]/div/div/div/div/div/input").send_keys(get_number(3))
    driver.find_element(By.XPATH, "//span[contains(text(),'严重')]/../../../../../td[3]/div/div/div/div/div/input").send_keys(get_number(3))
    driver.find_element(By.XPATH, "//span[contains(text(),'未定级')]/../../../../../td[3]/div/div/div/div/div/input").send_keys(get_number(3))
    driver.find_element(By.XPATH, "//span[contains(text(), '仅保存')]/..").click()
    sleep(3)


# 删除扫描任务
def delete_task(driver):
    sleep(5)
    driver.find_element(By.XPATH, "//span[contains(text(),'扫描任务')]/..").click()
    driver.find_element(By.XPATH, "//*[@id='app']/div/section/div/main/div/div[1]/div[3]/div[5]/div[2]/table/tbody/tr[1]/td[10]/div/div/div[3]").click()
    text = '删除后将不能再查看任务的制品扫描结果，请谨慎操作！'
    loc1 = (By.XPATH, f"//*[contains(text(),'{text}')]")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc1))
    driver.find_element(By.XPATH, "//div[3]/div/div[3]/button[2]").click()
    sleep(5)


# 保存cookies
def save_cookies(driver):
    cookies = driver.get_cookies()
    with open('cookies.json', 'w') as f:
        f.write(json.dumps(cookies))


# 使用cookies
def load_cookies(driver):
    try:
        with open('cookies.json') as f:
            cookies = json.loads(f.read())
        # 遍历字典获取cookies信息进行添加
        for cookie in cookies:
            driver.add_cookie(cookie)
        else:
            # 刷新页面，清除缓存
            driver.reflesh()
    except:
        print("没有可用的cookies信息")


# 生成一个随机的UUID
def get_uuid():
    unique_id = uuid.uuid4()

    # 打印UUID（默认格式）
    print("生成的UUID是:", unique_id)

    # 打印UUID的字符串表示
    print("UUID的字符串表示是:", str(unique_id))

    # 打印UUID的十六进制表示
    print("UUID的十六进制表示是:", unique_id.hex)