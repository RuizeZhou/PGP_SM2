# PGP_SM2
生成公私钥对-->
生成会话密钥-->
用sm2公钥加密会话密钥-->
用会话密钥加密消息（对称加密算法）-->
将两条加密信息拼接，转换成文本数据，即可得到报文数据。
# 项目说明

**1.小组成员**：周睿泽。git账户名称：RuizeZhou

**2,所作项目名称：**

本项目名称为：Project: Implement a PGP scheme with SM2

简介：实现PGP加密方案，编程语言为python。

主要思路是：
生成公私钥对-->
生成会话密钥-->
用sm2公钥加密会话密钥-->
用会话密钥加密消息（对称加密算法）-->
将两条加密信息拼接，转换成文本数据，即可得到报文数据。

完成人：周睿泽

**3.清单：**

完成的项目：

√Project: implement the naïve birthday attack of reduced SM3 

√Project: implement the Rho method of reduced SM3

√Project: implement length extension attack for SM3, SHA256, etc.

√Project: do your best to optimize SM3 implementation (software)

√Project: Impl Merkle Tree following RFC6962

√Project: report on the application of this deduce technique in Ethereum with ECDSA

√Project: Implement sm2 with RFC6979

√Project: verify the above pitfalls with proof-of-concept code

√Project: Implement a PGP scheme with SM2

未完成的项目：

Project: Try to Implement this scheme

Project: Implement the above ECMH scheme

Project: implement sm2 2P sign with real network communication

Project: implement sm2 2P decrypt with real network communication

Project: PoC impl of the scheme, or do implement analysis by Google

Project: forge a signature to pretend that you are Satoshi

Project: send a tx on Bitcoin testnet, and parse the tx data down to every bit, better write script yourself

Project: forge a signature to pretend that you are Satoshi

Project: research report on MPT

Project: Find a key with hash value “sdu_cst_20220610” under a message composed of your name followed by your student ID. For example, “San Zhan 202000460001”.

有问题的项目及问题：\

**4.本项目具体内容：**具体内容如下

# PGP_sm2

### A.具体的项目代码说明

本项目需要导入gmssl库。PGP加密协议主要分为三个部分：

第一部分：公钥部分，首先生成会话密钥，并对该会话密钥进行公钥加密。公钥算法采用sm2

```
    def generate_sys_key(self):#输出 密钥字节生成的是对称密码的密钥
        key_sm4 = secrets.token_hex(16)
        key_sm4=bytes(key_sm4,encoding='utf-8')
        # print(key_sm4)
        return key_sm4

    def encrypt_sys_key(self,datakey,public_key):
        enc_data = self.sm2_crypt.encrypt(datakey)
        return enc_data
```

第二部分：对称部分，使用会话密钥作为对称密钥对消息进行加密。对称加密算法采用sm4。

```
    def encrypt_massage(self,m,sys_key):
        m_b=bytes(m,encoding='utf-8')
        self.crypt_sm4.set_key(sys_key,SM4_ENCRYPT)
        encrypt_value=self.crypt_sm4.crypt_ecb(m_b)
        return encrypt_value
```

第三部分：链接两个加密后的部分，并转换为文本数据。

```
    def catenation(self,enc_sys_key,enc_m):
        caten=enc_sys_key+enc_m
        return caten

    def decode_from_byte(self,caten):
        mss_data2=binascii.b2a_base64(caten).decode('utf-8')
        return mss_data2
```

### B.运行指导(跑不起来的不算成功)

​	任意更改m消息内容，（默认'abcdefg'），直接运行即可得到PGP加密策略得到的该消息的加密文本。

### C.代码运行全过程截图(无截图无说明的代码不给分)

![1659160118677](https://cdn.jsdelivr.net/gh/RuizeZhou/images/1659160118677.png)

### D.每个人的具体贡献说明及贡献排序(复制的代码需要标出引用)

​	本人负责全部。
