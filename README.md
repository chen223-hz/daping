# 构建工具


## 前端

### 环境准备

```
npm install webpack -g

cd front
npm install
```

打包通用模块

`webpack --config webpack.dll.js`

## 后端

安装 tornado

`pip install tornado`

## git 更新

由于之前打包后的webapp\static\main.js 会引起我们合并的时候代码冲突，
我们再git仓库里屏蔽了这货

```
git rm -r --cached webapp/static/dist 
git commit -m "ignore dist"
```

之后需要我们每个人执行一次

```
git update-index --assume-unchanged
```
update-index的意义参见说明

[https://segmentfault.com/q/1010000000430426]

git update-index --assume-unchanged webapp/static/dist/main.js

## 百度地图

自定义样式

[http://developer.baidu.com/map/custom/]
