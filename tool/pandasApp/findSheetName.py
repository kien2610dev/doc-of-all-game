import os
import pandas as pd

# Đường dẫn đến thư mục chứa các file Excel
folder_path = 'D:\\zipGame\\yeuki\\data\\game\\excel\\release'

# Tên sheet cần tìm
sheet_name_to_find = '全服BOSS关卡'

# Duyệt qua tất cả các file trong thư mục
for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx'):
        file_path = os.path.join(folder_path, filename)
        try:
            # Đọc file Excel
            xls = pd.ExcelFile(file_path)
            # Kiểm tra xem sheet có tên là 'aaaa' có tồn tại không
            if sheet_name_to_find in xls.sheet_names:
                print(f'Sheet "{sheet_name_to_find}" tìm thấy trong file: {filename}')
        except Exception as e:
            print(f'Lỗi khi đọc file {filename}: {e}')
