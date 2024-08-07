import asyncio
from pyppeteer import launch


async def main():
    # 启动浏览器并创建一个新的页面
    browser = await launch(headless=False)  # 将 headless 模式关闭以进行调试
    page = await browser.newPage()

    try:
        # 设置超时时间为 60 秒并加载页面
        await page.goto('https://accounts.google.com/accountchooser/identifier?continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&ddm=0&flowName=GlifWebSignIn&hl=zh-CN&ifkv=AdF4I76hopAOI_8OXuBuWoRWbVpPVtLJon2KZQww4prN9ReOqxIgNKw0WKDLJucL2O-xQxSehLc06w&flowEntry=AccountChooser', {'timeout': 60000})
        print("Page loaded successfully")

        # 等待并选择电子邮件输入框
        email_input = await page.waitForSelector('#identifierId', {'timeout': 60000})
        print("Found email input field")

        # 在输入框中输入电子邮件地址
        await email_input.type('gaojonathan7@gmail.com')
        print("Typed in email field")

        # 等待并选择“下一步”按钮
        next_button = await page.waitForSelector('#identifierNext', {'timeout': 60000})
        print("Found next button")

        # 点击“下一步”按钮
        await next_button.click()
        print("Clicked on Next button")

        # 等待导航完成
        await page.waitForNavigation({'timeout': 60000})
        print("Navigation completed")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        print("finally")
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
