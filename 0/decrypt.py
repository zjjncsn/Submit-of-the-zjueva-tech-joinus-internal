#这段代码用于解密文件
in_list = input("Enter the ciphertext:").split("/")
in_key = input("Enter the key:")
decode = lambda s_hex, key: "".join([chr(int(int(s_hex[i],16) / ord(in_key[i]))) for i in range(4)])
output = decode(in_list, in_key)
print(output)
input("Press Enter to exit.")