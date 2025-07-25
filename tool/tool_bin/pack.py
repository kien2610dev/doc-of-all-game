import zlib

# Mã hóa file
with open('version.json', 'rb') as f:
    plaintext = f.read()
    compressed = zlib.compress(plaintext,level=9)
    with open('version.bin', 'wb') as f:
        f.write(compressed)


