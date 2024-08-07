from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from emunium import EmuniumSelenium

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)  # 延长等待时间，以确保操作完成
emunium = EmuniumSelenium(driver)

try:
    driver.get('https://accounts.google.com/accountchooser/identifier?continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&ddm=0&flowName=GlifWebSignIn&hl=zh-CN&ifkv=AdF4I76hopAOI_8OXuBuWoRWbVpPVtLJon2KZQww4prN9ReOqxIgNKw0WKDLJucL2O-xQxSehLc06w&flowEntry=AccountChooser')

    # 等待电子邮件输入字段并输入电子邮件
    email_element = wait.until(
        EC.presence_of_element_located((By.ID, 'identifierId')))
    # emunium.type_at(email_element, 'gaojonathan7@gmail.com') // can not type 
    email_element.send_keys('gaojonathan7@gmail.com')
    print("Typed email")

    # 等待 Next 按钮并点击
    next_button = wait.until(
        EC.element_to_be_clickable((By.ID, 'identifierNext')))
    # emunium.click_at(next_button)
    next_button.click()
    print("Clicked Next button")

    # 等待下一步的加载或状态变化，假设我们需要等待登录页面加载
    wait.until(EC.presence_of_element_located((By.ID, 'password'))
               or EC.presence_of_element_located((By.CLASS_NAME, 'next-step')))
    print("Next page loaded or element appeared")

    # 在这里可以添加其他操作逻辑，比如输入密码等
    # password_element = wait.until(EC.presence_of_element_located((By.ID, 'password')))
    # emunium.type_at(password_element, 'your_password')

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
