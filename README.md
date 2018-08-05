# Wechat
基于Flask的微信公众号开发

./functions  ----- 项目相关功能管理
    --access_token.py   ----- 获取微信公众号access_token
    --message_handle.py ----- 接收用户消息，处理并响应
    --token_verify.py   ----- 微信公众号开发配置时的token验证
    --turing_rebot.py   ----- 图灵机器人聊天（目前仅支持文本）
./logs           ----- 程序运行日志
app.py           ----- 配置生成项目app
config.py        ----- 项目相关配置
menu.py          ----- 微信公众号自定义菜单（公众号需认证）
models.py        ----- 模型类，数据库操作（根据需要使用）
views_service.py ----- 响应处理
wechat.py        ----- 项目运行入口

