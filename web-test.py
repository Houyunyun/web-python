from flask import Flask

app = Flask(__name__)


# 创建了网址 /show/info和函数show_info之间的映射关系
# 用户在浏览器上访问/show/info时，会执行show_info函数，并返回字符串'This is a test page'
@app.route('/')
def show_info():
    return 'This is a test page'

if __name__ == '__main__':
    app.run()

