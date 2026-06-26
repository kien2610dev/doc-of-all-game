import zlib

# Mã hóa file
with open('ui.json', 'rb') as f:
    plaintext = f.read()
    compressed = zlib.compress(plaintext,level=9)
    with open('ui.bin', 'wb') as f:
        f.write(compressed)


