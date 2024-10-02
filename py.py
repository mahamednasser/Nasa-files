import socket
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
# إنشاء مفتاح تشفير عشوائي (16 bytes)
key = get_random_bytes(16)
# إنشاء كائن تشفير AES
cipher = AES.new(key, AES.MODE_EAX)
# البيانات التي ترغب في تشفيرها (يمكنك تعديل النص)
data = b'Your satellite data'
# تشفير البيانات
ciphertext, tag = cipher.encrypt_and_digest(data)
# طباعة البيانات المشفرة
print(f'Ciphertext: {ciphertext}')
print(f'Key: {key}')
print(f'Nonce: {cipher.nonce}')