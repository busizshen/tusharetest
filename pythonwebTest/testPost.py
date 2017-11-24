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


data = {
    'json': '{}'
}
postdata = urllib.parse.urlencode(data)
postdata = postdata.encode('utf-8')
print(postdata)
f = urllib.request.urlopen(
    url='url',
    data=postdata
)
print(f.read().decode("utf-8"))



