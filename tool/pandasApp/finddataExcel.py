import os
import pandas as pd

# Đường dẫn đến thư mục chứa các file Excel
folder_path = 'D:\\Open Game\\a Trung - Tam quốc chiến\\release'

# Tên cột và giá trị cần tìm
column_name_to_find = '赛季'
value_to_find = 1

# Duyệt qua tất cả các file trong thư mục
for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx'):
        file_path = os.path.join(folder_path, filename)
        try:
            # Đọc toàn bộ file Excel (tất cả sheet)
            xls = pd.ExcelFile(file_path)

            for sheet_name in xls.sheet_names:
                df = pd.read_excel(file_path, sheet_name=sheet_name)

                if column_name_to_find in df.columns:
                    filtered = df[df[column_name_to_find] == value_to_find]
                    if not filtered.empty:
                        print(f'File: {filename}, Sheet: {sheet_name} có {len(filtered)} dòng {column_name_to_find} = {value_to_find}')
                        print(filtered)
        except Exception as e:
            print(f'Lỗi khi đọc file {filename}: {e}')
