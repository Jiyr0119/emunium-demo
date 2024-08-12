from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from emunium import EmuniumSelenium

# 配置 Chrome 浏览器的选项
options = webdriver.ChromeOptions()

# 使用本地安装的 Chrome 浏览器路径（可选，如果不设置则使用默认路径）
chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
options.binary_location = chrome_path

# 移除“Chrome 正在受到自动软件的控制”的提示
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

# 启动 Chrome 浏览器
driver = webdriver.Chrome(options=options)
print("Browser launched successfully")

# 浏览器最大化
driver.maximize_window()
print("Browser window maximized")

wait = WebDriverWait(driver, 10)  # 延长等待时间，以确保操作完成
emunium = EmuniumSelenium(driver)
print("Emunium initialized")

try:
    driver.get('https://accounts.google.com/accountchooser/identifier?continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&ddm=0&flowName=GlifWebSignIn&hl=zh-CN&ifkv=AdF4I76hopAOI_8OXuBuWoRWbVpPVtLJon2KZQww4prN9ReOqxIgNKw0WKDLJucL2O-xQxSehLc06w&flowEntry=AccountChooser')
    print("Page loaded")

    # 等待电子邮件输入字段并输入电子邮件
    email_element = wait.until(EC.presence_of_element_located((By.ID, 'identifierId')))
    print("Email field located")

    try:
        # 尝试使用 emunium 进行输入
        emunium.type_at(email_element, 'gaojonathan7@gmail.com')
        print("Typed email using Emunium")
    except Exception as e:
        print(f"An error occurred while typing email using Emunium: {e}")
        print("Attempting to type email using send_keys instead")
        email_element.send_keys('gaojonathan7@gmail.com')
        print("Typed email using send_keys")

    # 等待 Next 按钮并点击
    next_button = wait.until(EC.element_to_be_clickable((By.ID, 'identifierNext')))
    print("Next button located")

    try:
        # 尝试使用 emunium 点击按钮
        emunium.click_at(next_button)
        print("Clicked Next button using Emunium")
    except Exception as e:
        print(f"An error occurred while clicking Next button using Emunium: {e}")
        print("Attempting to click Next button using click instead")
        next_button.click()
        print("Clicked Next button using click")

    # 等待下一步的加载或状态变化，假设我们需要等待登录页面加载
    wait.until(EC.presence_of_element_located((By.ID, 'password'))
               or EC.presence_of_element_located((By.CLASS_NAME, 'next-step')))
    print("Next page loaded or element appeared")

except Exception as e:
    print(f"An error occurred during the process: {e}")

finally:
    driver.quit()
    print("Browser closed")
