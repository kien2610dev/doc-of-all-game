from datetime import datetime

# Nhập ngày theo dạng chuỗi
start_date_str = "2025-09-13"

# Chuyển chuỗi thành datetime (format theo năm-tháng-ngày)
start_date = datetime.strptime(start_date_str, "%Y-%m-%d")

# Lấy ngày hôm nay (theo hệ thống)
today = datetime.today()

# Tính số ngày chênh lệch
days_diff = (today - start_date).days

print("Số ngày chênh lệch:", days_diff)