# Lập trình hướng đối tượng
# OOP - Object oriented programming

# Tổng quát: OOP là cách chúng ta mô phỏng thế giới thực vào chương trình máy tính

# Ví dụ: object (đối tượng) - con người (Human)
    # Thuộc tính (đặc điểm): Tên, tuổi, địa chỉ,...
    # Phương thức (hành động): ăn, ngủ, nói chuyện, giải trí,...

# Khai báo lớp đối tượng
    # Mô phỏng con người từ thế giới thực vào máy tính
    # Mô phỏng tổng quát 
class Human():
    # Hàm khởi tạo giá trị
    def __init__(self, name, age, gender):
        # name, age, gender là thuộc tính (đặc điểm)
        self.name = name
        self.age = age
        self.gender = gender
    
    # Phương thức (hành động)
    # Phương thức giới thiệu bản thân
    def introduce(self):
        print(f'Xin chào, tôi tên là {self.name}, {self.age} tuổi.')

    # Phương thức hát
    def sing(self):
        print(f'{self.name} đang hát: "Baby Shark"')

# Khởi tạo 1 đối tượng mới
human1 = Human('Bách', 12, 'male')
# Truy cập các thuộc tính của đối tượng
print(human1.name)
# Gọi phương thức của đối tượng
human1.introduce()
human1.sing()

