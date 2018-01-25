# 钉钉的服务端API，使用python 2.7


## 2018年1月25日bug修正，功能测试
扩展了user和department的API接口【测试用例test1】
工作通知消息发送文本和图片测试正常【测试用例test2】

## Dependences
- poster 0.8.1

## Usage
- 将conf.py文件复制为config.py，然后修改自己的corpid和secret
- auth/conf/department/user部分工作应该正常
- 调用方式请参考test文件夹中的测试用例

## To Do
- access_token和jsapi_ticket缓存
- access_token 两小时到期问题