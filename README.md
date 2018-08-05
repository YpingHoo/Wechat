# Wechat
基于Flask的微信公众号开发

./functions  ----- 项目相关功能管理<br>
    --access_token.py   ----- 获取微信公众号access_token<br>
    --message_handle.py ----- 接收用户消息，处理并响应<br>
    --token_verify.py   ----- 微信公众号开发配置时的token验证<br>
    --turing_rebot.py   ----- 图灵机器人聊天（目前仅支持文本)<br>
./logs           ----- 程序运行日志<br>
app.py           ----- 配置生成项目app<br>
config.py        ----- 项目相关配置<br>
menu.py          ----- 微信公众号自定义菜单（公众号需认证）<br>
models.py        ----- 模型类，数据库操作（根据需要使用）<br>
views_service.py ----- 响应处理<br>
wechat.py        ----- 项目运行入口<br>

