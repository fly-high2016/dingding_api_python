from dingding_sdk import config
from dingding_sdk import auth
from dingding_sdk import user
from dingding_sdk import department
from dingding_sdk import utils

##access_token = dingding_sdk.auth.get_access_token(dingding_sdk.config.CorpID,dingding_sdk.config.secret)
##if access_token[0] != True:
##    print 'get access_token error!'
##department_list = dingding_sdk.department.get_department_list(access_token[1]['access_token'], False, 56590897)
##if department_list[0] != True:
##    print 'get department_list error!'


is_success, result = auth.get_access_token(config.CorpID, config.Secret)
if is_success == True:
    access_token = result.get('access_token')
else:
    print 'access_token error!'


#is_success, result = department.create_department(access_token,u'钉钉测试1',1)

#is_success, result = department.update_department(access_token, u'钉钉测试2', 59057510, 1, 59010520)

#is_success, result = department.delete_department(access_token,59010520)

#is_success, result = department.get_department_detail(access_token, 56590897)

#is_success, result = department.get_parent_depts_by_dept(access_token, 59057510)

is_success, result = department.get_parent_depts_by_user(access_token, u'13570206541269367') #这里必须是uniconde
