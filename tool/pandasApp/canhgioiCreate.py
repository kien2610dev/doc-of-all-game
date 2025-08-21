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
    "LV4-SKILL2": "60040340",
    "LV5-SKILL2": "60040350",
    "LV6-SKILL2": "60040360",
    "LV1-SKILL5": "60041200",
    "LV2-SKILL5": "60041210",
    "LV3-SKILL5": "60041220",
    "LV4-SKILL5": "60041230",
    "LV5-SKILL5": "60041240",
    "LV6-SKILL5": "60041250",
    "LV7-SKILL5": "60041260",
    "LV8-SKILL5": "60041270",
    "LV9-SKILL5": "60041280",
    "LV10-SKILL5": "60041290",  # Đảm bảo LV10-SKILL5 có trong danh sách thay thế
}

# Gọi hàm và in kết quả
result_string = replace_skills(base_string, skill_replacements)
print(result_string)  # In ra chuỗi đã được thay thế
