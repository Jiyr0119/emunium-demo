import asyncio
from pyppeteer import launch
from emunium import EmuniumPpeteer
import pyautogui
import cv2  # 确保导入 OpenCV


async def main():
    browser = await launch(headless=False)  # 将 headless 模式关闭以进行调试
    page = await browser.newPage()
    emunium = EmuniumPpeteer(page)

    try:
        # 设置超时时间为 60 秒
        await page.goto('https://accounts.google.com/accountchooser/identifier?continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&ddm=0&flowName=GlifWebSignIn&hl=zh-CN&ifkv=AdF4I76hopAOI_8OXuBuWoRWbVpPVtLJon2KZQww4prN9ReOqxIgNKw0WKDLJucL2O-xQxSehLc06w&flowEntry=AccountChooser', {'timeout': 60000})
        print("Page loaded successfully")

        element = await page.waitForSelector('#identifierId', {'timeout': 60000})
        print("identifierId res", element)
        if element:
            print("Typed in email true", emunium)
            try:
                await emunium.type_at(element, 'gaojonathan7@gmail.com')
                print("Typed in email field")
            except Exception as e:
                print(f"An error occurred while typing email: {e}")

        submit = await page.waitForSelector('#identifierNext', {'timeout': 60000})
        print("identifierNext res", submit)
        if submit:
            await emunium.click_at(submit)
            print("Clicked on Next button")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        print("finally")
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
