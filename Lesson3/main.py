from oop import Human, Student
from oop import Animal, Dog

stu1 = Student('Duc Minh', 12, 'male', 'Vinschool')
stu2 = Student('Quang Huy', 14, 'male', 'Vinschool')

# print(stu1)
# # sử dụng phương thức của lớp cha
# stu1.introduce()
# stu1.display_info()
# # stu1.edit_age()
# stu1.edit_name('Loopy')

# Đề bài:
# Tạo class Animal gồm các thuộc tính: tên, loài
# Viết 2 phương thức cho class Animal

# Tạo class Dog kế thừa từ class Animal và có thêm thuộc tính: giống
# Viết 1 phương thức kế thừa từ class Animal (có sửa đổi)
# Viết 1 phương thức mới cho class Dog

# Yêu cầu:
# - Tạo class ở file oop.py
# - Viết chương trình test tại file main.py

a1 = Animal('Bơ', 'Chó')
a1.display_info()
a1.eat()

dog1 = Dog('Mít', 'Chó', 'Shiba')
dog1.display_info()
dog1.edit_name('Sầu riêng')