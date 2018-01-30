import base64
import hashlib
import time
import urllib.request

from Crypto.Cipher import AES


def _pad(s):
    return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)

def _cipher():
    key = 'yGlQ458eSh6DapXj'
    iv = '0000000000000000'
    return AES.new(key=key, mode=AES.MODE_ECB, IV=iv)


def encrypt_token(data):
    print(data)
    return _cipher().encrypt(_pad(data))


def decrypt_token(data):
    return _cipher().decrypt(data)


# data = {
#     'mobileNo': '18810112327',
#     'realName': '测试',
#     'idCardNo': '320502198005132143',
#     'bankCardNo': '6228480402564890018',
#     'empId': '123'
# }

# 6225881001075521
def post(data,url):

    postdata = urllib.parse.urlencode(data)
    postdata = postdata.encode('utf-8')
    print(postdata)
    f = urllib.request.urlopen(
        url=url,
        # url='http://192.168.34.192:13080/custody/requestCustodyCallBack.bl',
        data=postdata
    )
    print(f.read().decode("utf-8"))
def rePost():
    strings='''
    -message:{"status":"AUDIT","platformUserNo":"f642bc4d8cb2482d958e09113cfdecbb","userRole":"BORROWERS","bankcardNo":"31050163380000000054","bankcode":"PCBC","failTime":"20260118","amount":50000000.00,"enterpriseName":"上海越昕潮餐饮管理有限公司","unifiedCode":"91310107342406174U","legal":"王新法","requestNo":"29893490d6084611bdaeddcc99848046","code":"0","description":"企业注册成功"}
    -message:{"status":"AUDIT","platformUserNo":"e95a63f257a94a3db363e433d10dd6e1","userRole":"BORROWERS","bankcardNo":"127908966710701","bankcode":"CMBC","failTime":"20260117","amount":50000000.00,"enterpriseName":"武汉>祥宝合福商贸有限公司","unifiedCode":"91420107MA4KMBPW3Q","legal":"胡珍元","requestNo":"24367eaedd8742f695320f691a650c51","code":"0","description":"企业注册成功"}
    '''
    msgs=strings.split('-message:')
    print(msgs)
    for index, msg in enumerate(msgs):
        if len(msg) <10:
            continue
        print(index, msg)
        data = {
            'msg': msg
        }
        post(data,'https://rxt.yinhu.com/custody/requestCustodyCallBack.bl')
# def getUserInfo():
#     data = {
#         "userId":"70e48b866d3846a08655fdd9079db594"
#     }
#     # url="http://192.168.50.6:8131/enterpriseBorrower/getRegUserInfo?userId=70e48b866d3846a08655fdd9079db594"
#     url="https://rxt.yinhu.com/enterpriseBorrower/getRegUserInfo?userId=70e48b866d3846a08655fdd9079db594"
#     post(data,url)

rePost()