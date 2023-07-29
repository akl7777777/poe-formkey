import asyncio
from time import sleep

from pyppeteer import launch


async def main():
    # 定义pb数组
    pbList = [
        # 'vk**********************QmHlg%3D%3D',
        # 'rI**********************3MRhw%3D%3D',
    ]
    # 启动浏览器
    browser = await launch(headless=False)
    page = await browser.newPage()
    # 遍历
    for pb in pbList:
        # 设置 cookie
        await page.setCookie({'name': 'p-b', 'value': pb, 'domain': 'poe.com'})
        await page.goto('https://poe.com/settings')  # 打开页面以获取Cookie
        sleep(1)
        content = await page.content()
        # 执行js脚本
        form_key = await page.evaluate('''
            window.ereNdsRqhp2Rd3LEW()
        ''')
        # 去掉最后两位
        form_key = form_key[:-2]
        # 判断content中是否包含Subscribe to Poe
        expired = False
        if "Continue with Google" in content:
            # banned
            print('pb:', pb, 'formKey:', form_key, '**banned**')
            sleep(3)
            continue
        if 'Subscribe to Poe' in content:
            expired = True
        print('pb:', pb, 'formKey:', form_key, 'expired:', expired)
        sleep(3)
        # 进行其他操作...
        # 关闭浏览器
        # await browser.close()


asyncio.get_event_loop().run_until_complete(main())
