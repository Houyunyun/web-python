from flask import Flask,render_template

app = Flask(__name__)


# 创建了网址 /show/info和函数show_info之间的映射关系
# 用户在浏览器上访问/show/info时，会执行show_info函数，并返回字符串'This is a test page'
@app.route('/')
def show_info():
    return render_template('index.html')

@app.route('/get/news')
def get_news():
    return render_template('get_news.html')

@app.route('/goods/list')
def goods_list():
    return render_template('goods_list.html')

@app.route('/users/list')
def users_list():
    return render_template('uses_list.html')

# 用户注册页面
@app.route('/register')
def register():
    return render_template('register.html')

# 用户登录页面
@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
