# coding=utf-8
import requests
from bs4 import BeautifulSoup


s = requests.Session()
s.headers = {'user-agent': 'Chrome/56.0.2924.87'}

# variantname = input()
a = ["Phương thức sản xuất",
     "Chúng ta phải ghi sâu",
     "Một dân tộc dốt",
     "Cấu thành lượng giá trị hàng hóa",
     "Lượng giá trị của hàng hóa",
     "Toàn quốc đồng bào hãy đứng dậy",
     "Học thuyết giá trị thặng dư",
     "Triết học được coi là hạt nhân của",
     "Chân lý (theo Tư tưởng Hồ Chí Minh)",
     "Hai phương pháp sản xuất giá trị thặng dư",
     "Chủ nghĩa dân túy",
     "Hai mặt của nền sản xuất xã hội",
     "Tri giác",
     "Chế độ giai cấp nào",
     "Đối tượng nghiên cứu của Triết học Mác - Lênin",
     "Tồn tại khách quan",
     "Chủ nghĩa xã hội không tưởng",
     "Thống nhất độc lập",
     "Chủ nghĩa cộng sản",
     "Những phát minh mới trong KHTN cuối XIX, đầu XX"]

b = [
    "Cách thức sản xuất vật chất ở những giai đoạn nhất định của lịch sử ",
    "Thuộc tính cơ bản, phổ biến nhất của mọi dạng vật chất",
    "Giai đoan cao",
    "Đem sức ta mà tự giải phóng cho ta ",
    "Những chữ “công bình, chính trực” vào lòng ",
    "Lực lượng sản xuất và quan hệ sản xuất",
    "Chủ nghĩa xã hội phi Mác xít",
    "“Hòn đá tảng” trong hệ thống lý luận của C.Mác về kinh tế chính trị",
    "Cũng có chuyên chính ",
    "Được đo bằng lượng lao động hao phí để sản xuất hàng hóa",
    "Là cái gì có lợi cho Tổ quốc, cho nhân dân ",
    "Nhất định thành công ",
    "Sự kết hợp, tổng hợp nhiều cảm giác ",
    "Sản xuất giá trị thặng dư tuyệt đối và giá trị thặng dư tương đối",
    "Là một dân tộc yếu ",
    "Thế giới quan ",
    "Những quy luật chung nhất của tự nhiên, xã hội và tư duy.",
    "C + v + m",
    "Đã bác bỏ quan niệm siêu hình về vật chất ",
    "Chưa tìm ra được biện pháp cải tạo xã hội cũ, xây dựng xã hội mới	"
]

r = s.get('http://coccoc.vn/search#query=%22cai+gi%22')
bsObj = BeautifulSoup(r.content, 'lxml')
print bsObj.body
token = bsObj.find('div',class_="snippet-result")

print token
