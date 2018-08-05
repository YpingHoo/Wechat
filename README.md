# Wechat
基于Flask的微信公众号开发

./wechat
├── app.py    ---- 项目对象创建
├── config.py ---- 项目相关配置
├── functions ---- 包含各种功能的包
│   ├── access_token.py ---- 获取微信公众号的access_token
│   ├── __init__.py
│   ├── message_handle.py ---- 接收用户发送的信息，对应信息完成响应
│   ├── token_verify.py   ---- 微信公众号接入开发者，配置token
│   └── turing_rebot.py   ---- 图灵机器人聊天（文本）
├── logs   ---- 日志文件
│   └── wechat.log
├── menu.py   ---- 自定义微信公众号菜单
├── models.py ---- 数据库模型类
├── __pycache__
│   ├── app.cpython-35.pyc
│   ├── config.cpython-35.pyc
│   ├── models.cpython-35.pyc
│   └── views_service.cpython-35.pyc
├── static
├── templates
├── views_service.py  ---- 请求处理
└── wechat.py         ---- 项目运行文件


