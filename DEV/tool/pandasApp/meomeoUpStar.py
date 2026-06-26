import re

A = 2  

base_element = """
[720012]={name=[[月·司马懿]],name_vi=[[月·司马懿]],name_kr=[[月·司马懿]],father=705012,camp=6,job=2,star=20,hpStarRate=78690,atkStarRate=17090,isElite=1,isFuNeng=1,showDrawEffect=0,height=160,width=160,head=705012,head_kr=705012,body=[[705012]],body_kr=[[705012]],voice=705012,voice_kr=705012,attrs={{101,160},{102,56},{103,1100},{104,205}},up={{101,16},{102,5.6},{103,110},{104,2.08}},normalAtkID=62001,normalAtkID_kr=62001,skillID=62013,skillID_kr=62013,beSkillID={62023,62033,62043},beSkillID_kr={62023,62033,62043},upSkill={},upSkill_kr={},weightLv=0,cd=0,grade=3,seerLv=0,seerLv_tw=0,zhihuanLv=0,zhihuanLv_tw=0,combatOffset={},skin={},gl=0}
"""

# Hàm tạo và in ra các phần tử mới từ 20 đến 50 sao
def generate_elements(base_element, start_star, end_star):
    # Tìm ID hiện tại và star trong chuỗi đầu vào
    id_match = re.search(r'\[(\d+)\]', base_element)
    star_match = re.search(r'star=(\d+)', base_element)

    if id_match and star_match:
        start_id = int(id_match.group(1))  # Lấy ID hiện tại
        current_star = int(star_match.group(1))  # Lấy giá trị star hiện tại
        elements = []
        
        for star in range(current_star, end_star + 1):  # Bắt đầu từ giá trị star hiện tại
            new_id = start_id + (star - current_star) * 1000  # Tăng id thêm 1000 cho mỗi sao
            new_element = base_element.replace(f"[{start_id}]", f"[{new_id}]").replace(f"star={current_star}", f"star={star}")
            elements.append(new_element.strip())  # Loại bỏ khoảng trắng thừa
            
        return elements
    else:
        raise ValueError("Không tìm thấy ID hoặc star trong chuỗi đầu vào.")
#----------------------------------------------------------------------------------------------------------------------------
# Các giá trị ví dụ
current_id = 619015  # ID hiện tại
new_hero = 620015    # newHero
jinjieshi = 55000    # jinjieshi
cond_value = 1500    # Giá trị cuối trong cond
cond_base = 609015   # Giá trị cố định trong cond
#----------------------------------------------------------------------------------------------------------------------------
if A == 1:
    # Gọi hàm để tạo các phần tử từ 20 đến 50 sao
    new_elements = generate_elements(base_element, 20, 50)

    # In ra các phần tử mới, mỗi phần tử trên một dòng mới với dấu phẩy ở cuối, trừ phần tử cuối cùng
    for i, element in enumerate(new_elements):
        if i < len(new_elements) - 1:  # Nếu không phải phần tử cuối cùng
            print(element + ",")  # Thêm dấu phẩy
        else:
            print(element)  # Không thêm dấu phẩy cho phần tử cuối cùng

elif A == 2:
    # Số lượng phần tử cần in ra
    num_elements = 30  # Bạn có thể thay đổi giá trị này nếu cần

    # Hàm để in ra giá trị từ sao 1 đến num_elements
    def print_star_values(current_id, new_hero, jinjieshi, cond_value, cond_base, num_elements):
        # Tính toán và in ra giá trị cho các phần tử từ 1 đến num_elements
        for i in range(num_elements):
            new_id = current_id + (i + 1) * 1000  # Tính toán id mới (tăng dần)
            new_hero_id = new_hero + (i + 1) * 1000  # Tính toán id cho newHero (tăng dần)
            new_jinjieshi = jinjieshi + (i + 1) * 5000  # Tăng dần jinjieshi
            new_cond_value = cond_value + (i + 1) * 300  # Tăng dần giá trị cuối trong cond
            
            # In ra giá trị với dấu phẩy ở cuối, trừ phần tử cuối cùng
            if i < num_elements - 1:
                print(f"[{new_id}]={{newHero={new_hero_id},jinjieshi={new_jinjieshi},cond={{{{1,{cond_base},1}},{{3,399,{new_cond_value}}}}}}},")
            else:
                print(f"[{new_id}]={{newHero={new_hero_id},jinjieshi={new_jinjieshi},cond={{{{1,{cond_base},1}},{{3,399,{new_cond_value}}}}}}}")

    # Gọi hàm để in ra các giá trị từ sao 1 đến num_elements
    print_star_values(current_id, new_hero, jinjieshi, cond_value, cond_base, num_elements)
