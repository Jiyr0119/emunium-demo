import asyncio
from playwright.async_api import async_playwright
from emunium import EmuniumPlaywright
from pyautogui import ImageNotFoundException

async def main():
    async with async_playwright() as p:
        # 启动浏览器
        browser = await p.chromium.launch(
            executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
            headless=False
        )
        page = await browser.new_page()
        emunium = EmuniumPlaywright(page)

        # 访问 DuckDuckGo 网站
        await page.goto('https://duckduckgo.com/')

        try:
            # 尝试使用 Emunium 进行操作
            element = await page.wait_for_selector('[data-state="suggesting"]')
            await emunium.type_at(element, 'Automating searches')

            submit = await page.wait_for_selector('[aria-label="Search"]')
            await emunium.click_at(submit)
        except (ImageNotFoundException, Exception) as e:
            print(f"Emunium 操作失败，错误信息: {e}. 使用 Playwright 进行操作。")

            # 如果 Emunium 操作失败，使用 Playwright API 进行操作
            try:
                search_input = await page.wait_for_selector('[name="q"]')
                await search_input.type('Automating searches')

                search_button = await page.wait_for_selector('[aria-label="Search"]')
                await search_button.click()
            except Exception as e:
                print(f"Playwright 操作也失败了，错误信息: {e}")

        # 等待搜索结果加载
        await page.wait_for_load_state('networkidle')

        # 关闭浏览器
        await browser.close()

# 运行主函数
asyncio.run(main())
