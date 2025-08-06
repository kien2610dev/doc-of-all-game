import re

# Đoạn chuỗi gốc
base_string = "1:LV4-SKILL2#11:LV4-SKILL2:LV1-SKILL5#21:LV4-SKILL2:LV2-SKILL5#31:LV4-SKILL2:LV3-SKILL5#41:LV4-SKILL2:LV4-SKILL5#51:LV5-SKILL2:LV5-SKILL5#61:LV5-SKILL2:LV6-SKILL5#71:LV5-SKILL2:LV7-SKILL5#81:LV5-SKILL2:LV8-SKILL5#91:LV5-SKILL2:LV9-SKILL5#101:LV6-SKILL2:LV10-SKILL5"

# Hàm để thay thế các biến
def replace_skills(base_string, skill_replacements):
    # Hàm thay thế cho từng match
    def replace_match(match):
        return skill_replacements.get(match.group(0), match.group(0))

    # Sửa đổi mẫu regex để bao gồm cả LV10-SKILL5
    pattern = r'\b(LV[0-9]{1,2}-SKILL[0-9]|lv[0-9]{1,2}-skill[0-9])\b'
    return re.sub(pattern, replace_match, base_string)

# Nhập các biến cần thay thế
skill_replacements = {
    "LV4-SKILL2": "20230240",
    "LV5-SKILL2": "20230250",
    "LV6-SKILL2": "20230260",
    "LV1-SKILL5": "20231100",
    "LV2-SKILL5": "20231110",
    "LV3-SKILL5": "20231120",
    "LV4-SKILL5": "20231130",
    "LV5-SKILL5": "20231140",
    "LV6-SKILL5": "20231150",
    "LV7-SKILL5": "20231160",
    "LV8-SKILL5": "20231170",
    "LV9-SKILL5": "20231180",
    "LV10-SKILL5": "20231190",  # Đảm bảo LV10-SKILL5 có trong danh sách thay thế
}

# Gọi hàm và in kết quả
result_string = replace_skills(base_string, skill_replacements)
print(result_string)  # In ra chuỗi đã được thay thế
