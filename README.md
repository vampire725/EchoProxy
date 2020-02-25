# Echo

- [Echo](#echo)
  - [介绍](#介绍)
  - [项目结构说明](#项目结构说明)
  - [v2ray客户端使用说明](#v2ray客户端使用说明)

## 介绍

Echo项目主要实现内容：

1. 在线添加/修改/删除代理
2. 提供可实时更新的v2ray代理订阅链接

## 项目结构说明

|     目录     |       说明        |
| :----------: | :---------------: |
|     app      |     项目源码      |
|  app/forms   |     表单验证      |
|  app/helper  |     功能实现      |
|  app/models  |     数据设计      |
|   app/test   |       测试        |
| app/url_file |     订阅文件      |
|   app/web    |     视图函数      |
| settings.py  |   项目配置文件    |
|    client    | v2ray客户端安装包 |
|   echo.py    |    启动server     |

## v2ray客户端使用说明

- [Windows客户端下载](http://faii.com.cn:2525/Architecture/echorun/raw/master/client/v2rayN.zip)，使用方法如下：

1. 手动添加单个代理
   1. 安装完成以后，点击系统托盘的V2RayN图标，弹出程序主界面：

    ![v2rayn 主界面](app/static/images/v2ray.png)
   2. 点`服务器`下拉菜单中的添加`vmess`服务器，出现下面的界面：

    ![v2rayN添加vmess服务器](app/static/images/v2ray_vemess.png)

    根据服务端信息填写服务器地址（域名或ip）、端口、用户id、额外id，加密方式一般都是auto，传输协议一般是tcp。别名可以自定义。

2. 使用订阅链接添加代理
    1. 如果服务端信息是订阅，点击`订阅`下拉框的`订阅设置`，在弹框中点击`添加`，输入订阅网址，然后确定：

    ![v2rayN添加订阅](app/static/images/v2ray_url.png)

- [Android客户端下载](http://faii.com.cn:2525/Architecture/echorun/raw/master/client/v2rayNG_1.1.14.apk)，使用方法如下:
