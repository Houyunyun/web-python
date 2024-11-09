# 1.快速开发网站
```
pip install flask
```
```python
from flask import Flask

app = Flask(__name__)


# 创建了网址 /show/info和函数show_info之间的映射关系
# 用户在浏览器上访问/show/info时，会执行show_info函数，并返回字符串'This is a test page'
@app.route('/')
def show_info():
    return 'This is a test page'

if __name__ == '__main__':
    app.run()

```
网站过于丑陋
```
浏览器可以识别很多标签+数据，如：
    <h1>中国</h1>                           -> 浏览器看见会加大加粗
    <span style='color:red;'>联通</span>    -> 浏览器看见会将字体变红
如果能把浏览器能识别的所有标签都学会，就能在网站控制页面长什么样子。
```
[HTML教程](https://developer.mozilla.org/en-US/docs/Web/HTML)
- Flash框架支持将字符串写入到文件中，调用该文件。
```
from flask import Flask,render_template

app = Flask(__name__)


# 创建了网址 /show/info和函数show_info之间的映射关系
# 用户在浏览器上访问/show/info时，会执行show_info函数，并返回字符串'This is a test page'
@app.route('/')
def show_info():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

```

# 2.浏览器能识别的标签
## 2.1 编码(head)
```html
<meta charset="UTF-8">
```
## 2.2 title(head)
```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>购物网页</title>
    <link rel="stylesheet" href="styles.css">
</head>
```

![alt text](image.png)

## 2.3 标题

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>标题示例</title>
</head>
<body>
    <h1>一级标题</h1>
    <h2>二级标题</h2>
    <h3>三级标题</h3>
    <h4>四级标题</h4>
    <h5>五级标题</h5>
</body>
</html>
```
## 2.4 div和span
```html
<div>内容</div>
<span>内容</span>
```
- div，一个人占据一整行，【块级标签】
    - 用途：通常用于将文档中的大块内容分组，如段落、图像、表格等。
```html
<div>
    <h1>标题</h1>
    <p>这是一个段落。</p>
</div>
```
- span, 自己有多大就占多少（内联标签，行内标签）
    - 用途：通常用于将文档中的小块内容分组，如单词、短语或者图标，常用于样式化小块的内容。
```html
<p>这是一个 <span style="color: red;">红色</span> 的单词。</p>
```
注意：这两个标签结合CSS可以定制自己的功能。

### 超链接
```html
跳转到其他人的网页
<a href="www.baidu.com">点击跳转</a>
```
```html
跳转到自己的网页
<a href="http://127.0.0.1:5000/get/news">点击跳转</a>
<a href="/get/news">点击跳转</a>
```
### 图片
```html
<imag src="图片地址"/>
```
```html
显示别人的网址：
<imag src="其他网站的图片地址"/>


