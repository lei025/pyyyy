# /爬虫中的用法 有些网站会在请求过程中发送公钥，然后加密参数后传回后台来实现数据的加密。
import binascii

from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

data = '我是心蓝哈哈哈哈'.encode()
# 网页上收到的n值
pubkey_n = '8d7e6949d411ce14d7d233d7160f5b2cc753930caba4d5ad24f923a505253b9c39b09a059732250e56c594d735077cfcb0c3508e9f544f101bdf7e97fe1b0d97f273468264b8b24caaa2a90cd9708a417c51cf8ba35444d37c514a0490441a773ccb121034f29748763c6c4f76eb0303559c57071fd89234d140c8bb965f9725'
# e常常为65537
pbukey_e = 65537
# 生成公钥
recipient_key = RSA.RsaKey(n=int(pubkey_n, 16), e=65537)#16进制转为10进制
# 创建rsa对象
cipher_rsa = PKCS1_OAEP.new(recipient_key)
# 加密数据
msg = cipher_rsa.encrypt(data)
print(msg)
# 输出16进制字符串
print(binascii.b2a_hex(msg))