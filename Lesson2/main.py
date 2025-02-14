from oop import Animal

# Khởi tạo object - đối tượng
a1 = Animal('Dog', 'Ki', 1, 'black')
a2 = Animal('Beaver', 'Loopy', 3, 'pink')

# Hiển thị thông tin của object
    # Cách 1: sử dụng thuộc tính
print(a1.type ,a1.name, a1.age, a1.color)
    # Cách 2: Sử sụng phương thức tự viết
a2.display_info()
    # Cách 3: Sử dụng phương thức có sẵn
print(a2)

# Bài 1: Xây dựng class Rectangle gồm:
# 	- Thuộc tính: width, height
# 	- Phương thức:
# 		+ cvi(): tính chu vi HCN
# 		+ dtich(: tính diện tích HCN

# Bài 2: Xây dựng class BankAccount gồm:
# 	- Thuộc tính: 
# 		+ acc_number (số tài khoản)
# 		+ balance (số dư)
# 	- Phương thức:
# 		+ deposit(): nạp tiền vào tài khoản
# 		+ withdraw(): rút tiền và cập nhật số dư