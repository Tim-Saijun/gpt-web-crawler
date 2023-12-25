// 这个脚本定义了一个 takeScreenshot 函数，并从命令行参数读取 URL。它将执行截图操作，并在成功时将文件路径打印到控制台。

const puppeteer = require('puppeteer');
const fs = require('fs');

async function takeScreenshot(url) {
    const browser = await puppeteer.launch({headless: "new"});
    const page = await browser.newPage();

    await page.setViewport({
        width: 1920,
        height: 1080
    });

    await page.goto(url, {waitUntil: 'networkidle2'});

    const filename = url.replace(/[^a-zA-Z0-9]/g, '_').toLowerCase() + '.png';
    const dir = './screenshot';

    if (!fs.existsSync(dir)){
        fs.mkdirSync(dir);
    }

    const filePath = `${dir}/${filename}`;
    await page.screenshot({path: filePath, fullPage: true});
    await browser.close();

    return filePath;
}

// 从命令行参数读取 URL
const url = process.argv[2];
takeScreenshot(url)
    .then(filePath => {
        console.log(filePath); // 输出文件路径供 Python 脚本使用
    })
    .catch(error => {
        console.error("Error taking screenshot:", error);
        process.exit(1);
    });
