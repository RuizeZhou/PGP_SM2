#coding:utf-8
import binascii
import base64
from gmssl import sm3, func#,sm2
# import sm2
import secrets
from gmssl import sm2, func
from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT



class PGP:
    def __init__(self,msg):#
        self.iv=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        self.crypt_sm4=CryptSM4()

        #默认公私钥（sm2）
        self.pri_key = '00B9AB0B828FF68872F21A837FC303668428DEA11DCD1B24429D0C99E24EED83D5'
        self.pub_key = 'B9C9A6E04E9C91F7BA880429273747D7EF5DDEB0BB2FF6317EB00BEF331A83081A6994B8993F3F5D6EADDDB81872266C87C018FB4162F5AF347B483E24620207'


        self.sm2_crypt = sm2.CryptSM2(public_key=self.pub_key, private_key=self.pri_key)
        self.message=msg



    '''PGP 加密过程'''
    def encode(self):
        key_sm4=self.generate_sys_key()
        enced_key_sys=self.encrypt_sys_key(key_sm4,self.pub_key)
        enced_m=self.encrypt_massage(self.message,key_sm4)
        caten=self.catenation(enced_key_sys,enced_m)
        mss_date=self.decode_from_byte(caten)
        # self.mss_data=self.encode()
        return mss_date


    '''I 公钥部分，'''
    '''1.生成会话密钥 用来作为消息的对称加密密钥'''
    def generate_sys_key(self):#输出 密钥字节
        key_sm4 = secrets.token_hex(16)
        key_sm4=bytes(key_sm4,encoding='utf-8')
        # print(key_sm4)
        return key_sm4


    '''2.加密会话密钥'''
    def encrypt_sys_key(self,datakey,public_key):
        enc_data = self.sm2_crypt.encrypt(datakey)
        # print(enc_data)
        # print(type(enc_data))
        return enc_data

    '''II 对称部分，'''
    '''用会话密钥 加密 消息'''
    def encrypt_massage(self,m,sys_key):
        m_b=bytes(m,encoding='utf-8')
        self.crypt_sm4.set_key(sys_key,SM4_ENCRYPT)
        encrypt_value=self.crypt_sm4.crypt_ecb(m_b)
        # print(encrypt_value)
        # print(type(encrypt_value))
        return encrypt_value

    '''III 链接 加密后的会话密钥  和  加密后的消息'''
    def catenation(self,enc_sys_key,enc_m):
        # print(enc_sys_key)
        # print(enc_m)
        caten=enc_sys_key+enc_m

        return caten
    '''转换为文本数据，即可得到报文数据'''
    def decode_from_byte(self,caten):
        mss_date1=binascii.b2a_hex(caten).decode('utf-8')
        mss_data2=binascii.b2a_base64(caten).decode('utf-8')

        return mss_data2

    # @property
    # def msg(self):
    #
    #     return self.mss_data













# pri_key=56372074392373104506837008569889162956334264571792929184255150419127723385174
# pub_key=(12299529198150257681899048819418742102464936606019828479837957128854470563669, 66644146168027827388533641210755143163271719463915538838900750259998281731653)
# default_pri = '00B9AB0B828FF68872F21A837FC303668428DEA11DCD1B24429D0C99E24EED83D5'
# default_pub = 'B9C9A6E04E9C91F7BA880429273747D7EF5DDEB0BB2FF6317EB00BEF331A83081A6994B8993F3F5D6EADDDB81872266C87C018FB4162F5AF347B483E24620207'
# sm2_crypt = sm2.CryptSM2(public_key=default_pub, private_key=default_pri )






# '''1.消息经过散列处理  形成摘要：'''
# def hash(message):
#     m_b=bytes(message,encoding='utf-8')
#     digest= sm3.sm3_hash(func.bytes_to_list(m_b))
#     print('type:',type(digest))
#     return digest



# '''2.用公钥密码算法对摘要数字签名：'''
# #sm2
# def sign_by_pri(m,pri_key):
#
#     # data = bytes(m.encode('utf-8')) # bytes类型
#     # random_hex_str = func.random_hex(sm2_crypt.para_len)
#     # sign = sm2_crypt.sign(m,random_hex_str) #  16进制
#
#     signature=sm2.sign(pri_key, m)
#     print('signed:',signature)
#     return signature
#





if __name__=='__main__':
    m='abcdefg'

    mss_data=PGP(m).encode()
    print(mss_data)