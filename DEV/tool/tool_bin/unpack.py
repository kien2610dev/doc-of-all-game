import zlib

# Giải mã file
with open('ui.bin', 'rb') as f:
    compressed_data = f.read()
    decompressed_data = zlib.decompress(compressed_data)

with open('ui_unpack.json', 'wb') as f:
    f.write(decompressed_data)