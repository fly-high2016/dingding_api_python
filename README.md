# 钉钉的服务端API，使用python 2.7


## 2018年1月25日修正了几个bug，扩展了user和department的API接口

## Dependences
- poster 0.8.1

## Usage
- 将conf.py文件复制为config.py，然后修改自己的corpid和secret
- auth/conf/department/user部分工作应该正常
- 调用方式请参考test文件夹中的测试用例

## To Do
- access_token, jsapi_ticket缓存
- 发送信息部分尚未进行验证【media/message/test】
