# 2019-nCoV 全国新冠疫情数据可视化



预览地址：http://121.5.177.147:5230/

（加载时间较长，请耐心等待）

（部署项目无数据库建表文件 请自行建表）

### 数据来源

疫情数据来源于腾讯新闻，通过抓包的方式获取源数据URL

### 数据展示

![展示图](https://github.com/dddddkio/2019-nCoV/blob/main/pic.png?) 

### 技术栈

        1. python requests库 用于爬取指定URL数据
        2. mysql 8.0 用于存储采集的数据     
        3. flask 用于编写API 为前端展示调取数据
        4. echarts 用于画统计图形
        5. html、css、js、vue 用于生成静态网页
        6. nginx、腾讯云服务器 用于部署静态网页至公网

### 工程结构

> ```
> |-- 2019-nCoV
>  |-- .gitattributes
>  |-- README.md
>  |-- 有点蠢的课程设计报告....pdf
>  |-- pic.png
>  |-- html
>  |   |-- index.html
>  |   |-- res
>  |       |-- style.css
>  |       |-- images
>  |       |   |-- title-left.png
>  |       |   |-- title-right.png
>  |       |-- js
>  |           |-- c1.js
>  |           |-- c2.js
>  |           |-- china.js
>  |           |-- data-1528971808162-BkOXf61WX.json
>  |           |-- echarts-gl.min.js
>  |           |-- echarts.js
>  |           |-- jquery-3.6.0.js
>  |           |-- l1.js
>  |           |-- l2.js
>  |           |-- r1.js
>  |           |-- r2.js
>  |-- python
>      |-- app.py    -------------------api       
>      |-- spider.py -------------------爬虫
>      |-- test.py
> 
> ```
>
> 
>

