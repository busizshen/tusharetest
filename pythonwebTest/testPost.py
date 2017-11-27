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
data = {
    'json': '{"idCardNo":"130204199901012719","cardMobileNo":"13312345678","empId":"021411279","realName":"李日男","bankCardNo":"6225881001075521","mobileNo":"13488756444"}'

}
postdata = urllib.parse.urlencode(data)
postdata = postdata.encode('utf-8')
print(postdata)
f = urllib.request.urlopen(
    # url='http://192.168.10.163:8131/borrower/borrowerAccountAuth',
    url='http://localhost:8080/borrower/borrowerAccountAuth',
    data=postdata
)
print(f.read().decode("utf-8"))



