import os
import pandas as pd

directory = r"D:\SourceGame\Yeu Ki\data\game\excel\release"
search_text = "3:900010"

for filename in os.listdir(directory):
    if filename.endswith(".xlsx") or filename.endswith(".xlsm"):
        filepath = os.path.join(directory, filename)
        try:
            excel_data = pd.ExcelFile(filepath)
            for sheet_name in excel_data.sheet_names:
                sheet_data = excel_data.parse(sheet_name)
                
                # Kiểm tra xem search_text có trong bất kỳ ô nào của DataFrame không
                if sheet_data.apply(lambda x: x.astype(str).str.contains(search_text, na=False).any()).any():
                    print(f"'{search_text}' found in file: {filename}, sheet: {sheet_name}")
        except Exception as e:
            print(f"Could not read file {filename}: {e}")