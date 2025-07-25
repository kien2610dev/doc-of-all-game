import os


folder_path = r"C:\Users\Lê Ann\Documents\Zalo Received Files\iconshop"


for filename in os.listdir(folder_path):
    if filename.endswith('.png'):
        new_name = filename[4:]
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)
        os.rename(old_file, new_file)

print("Đã xóa 4 chữ cái đầu của các file PNG.")