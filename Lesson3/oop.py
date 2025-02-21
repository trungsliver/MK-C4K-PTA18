# Tính chất kế thừa

class Human():
    # Hàm khởi tạo giá trị
    def __init__(self, name, age, gender):
        # name, age, gender là thuộc tính (đặc điểm)
        self.name = name
        self.age = age
        self.gender = gender
    
    # Phương thức giới thiệu bản thân
    def introduce(self):
        print(f'Xin chào, tôi tên là {self.name}, {self.age} tuổi.')

# Lớp kế thừa
class Student(Human):
    # Hàm khởi tạo giá trị
    def __init__(self, name, age, gender, school):
        # Gọi hàm khởi tạo của lớp cha
        super().__init__(name, age, gender)
        # school là thuộc tính đặc trưng của lớp Student
        self.school = school

    # Hàm để dùng được print()
    def __str__(self):
        return f'Student: {self.name}, {self.age} tuổi, {self.gender}, {self.school}'
    
    # Phương thức giới thiệu bản thân, ghi đè phương thức lớp cha
    def introduce(self):
        print(f'Xin chào, tôi tên là {self.name}, học tại {self.school}')

    # Phương thức hiển thị thông tin
    def display_info(self):
        print(f'''
========== THÔNG TIN ==========
Họ tên:         {self.name}
Tuổi:           {self.age}
Giới tính:      {self.gender}
Trường học:     {self.school}
===============================''')
        
    # Phương thức chỉnh sửa thông tin
        # Chỉnh sửa tuổi
    def edit_age(self):
        new_age = int(input('Nhập tuổi mới: '))
        if new_age <= 0:
            print('Tuổi không hợp lệ.')
        else:
            self.age = new_age
            print('Tuổi đã được chỉnh sửa.')
        self.display_info()

        # Chỉnh sửa tên
    def edit_name(self, new_name):
        # Chỉnh sửa thông tin của đối tượng
        self.name = new_name
        # Hiển thị lại thông tin sau chỉnh sửa
        self.display_info()

# Luyện tập
class Animal():
    # Khởi tạo đối tượng với 2 thuộc tính
    def __init__(self, ten, loai):
        self.ten = ten
        self.loai = loai
    
    # Phương thức giới thiệu
    def display_info(self):
        print(f'''
========== ANIMAL =========
Tên:    {self.ten}
Loại:   {self.loai}
===========================''')

    # Phương thức eat 
    def eat(self):
        print(f'{self.ten} đang ăn')

class Dog(Animal):
    # Khởi tạo và thêm thuộc tính giong
    def __init__(self, ten, loai, giong):
        super().__init__(ten, loai)
        self.giong = giong
    
    # Phương thức giới thiệu
    def display_info(self):
        print(f'''
========== DOG =========
Tên:    {self.ten}
Loại:   {self.loai}
Giong:  {self.giong}
========================''')
        
    # Phương thức mới: chỉnh sửa tên
    def edit_name(self, new_name):
        self.ten = new_name
        self.display_info()