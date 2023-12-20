from doctest import debug
from flask import Flask, request, jsonify, render_template
from craw_single_page import craw_sigle_page

app = Flask(__name__)
@app.route('/')
def api_docs():
    return render_template('api_docs.html')

@app.route('/craw_sigle_page')
def craw_sigle_page_() -> str:  # 修改返回类型为str
    default_url = "https://www.leadong.com/"
    url = request.args.get('url', default_url)  # 'default_url' 是如果没有提供时的默认值
    return craw_sigle_page(url)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
