import asyncio
from playwright.async_api import async_playwright
from emunium import EmuniumPlaywright
from pyautogui import ImageNotFoundException


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
            headless=False
        )
        page = await browser.new_page()
        emunium = EmuniumPlaywright(page)

        await page.goto('https://accounts.google.com/accountchooser/identifier?continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&ddm=0&flowName=GlifWebSignIn&hl=zh-CN&ifkv=AdF4I76hopAOI_8OXuBuWoRWbVpPVtLJon2KZQww4prN9ReOqxIgNKw0WKDLJucL2O-xQxSehLc06w&flowEntry=AccountChooser')

        try:
            # 使用 Emunium 进行操作
            element = await page.wait_for_selector('#identifierId')
            print("Emunium: Found element for typing.")
            await emunium.type_at(element, 'gaojonathan7@gmail.com')
            print("Emunium: Typed text into the element.")

            submit = await page.wait_for_selector('#identifierNext')
            print("Emunium: Found search button.")
            await emunium.click_at(submit)
            print("Emunium: Clicked search button.")
        except (ImageNotFoundException, Exception) as e:
            print(f"Emunium 操作失败，错误信息: {e}. 使用 Playwright 进行操作。")

            # 使用 Playwright API 进行操作
            try:
                search_input = await page.wait_for_selector('#identifierId')
                await search_input.type('gaojonathan7@gmail.com')
                print("Playwright: Typed text into the search input.")

                search_button = await page.wait_for_selector('#identifierNext')
                await search_button.click()
                print("Playwright: Clicked search button.")
            except Exception as e:
                print(f"Playwright 操作也失败了，错误信息: {e}")

        # 等待搜索结果加载
        await page.wait_for_load_state('networkidle')

        # 关闭浏览器
        await browser.close()

# 运行主函数
asyncio.run(main())
