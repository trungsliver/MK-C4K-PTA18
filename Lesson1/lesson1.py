# Data Types - Kiểu dữ liệu
    # Strings - Chuỗi ký tự / Xâu ký tự
name = 'loopy'
    # Int (integer) - số nguyên
age = 2
    # Float - số thực (số thập phân)
score = 9.5
    # Boolean - True/False, Đúng/Sai
die = False

# Các kiểu print: 4 kiểu
    # cách 1: Dùng dấu +
print('Họ tên: ' + name + ' Tuổi: ' + str(age))
    # cách 2: Dùng dấu ,
print('Điểm:', score, 'Qua đời:', die)
    # cách 3: Dùng f - truyền dữ liệu vào string
print(f'{name} được {score} điểm trong bài kiểm tra')

# Nhập dữ liệu - Input
age = input('Nhập tuổi: ')          # String
age = int(input('Nhập tuổi: '))     # int

# Câu điều kiện:
    # Các phép so sánh: == != <= >= < >
    # Các phép toán logic: and - or - not 
    # Cấu trúc: 3 dạng
        # Dạng thiếu:   if ...
        # Dạng đủ:      if ... else ...
        # Đa nhánh:     if ... elif ... elif ... else ...

# Các phép toán:
    # Thông thường:         + - * /
    # Chia lấy nguyên:      //
    # Chia lấy dư:          %
    # Lũy thừa:             **

# Vòng lặp hữu hạn - Vòng lặp for
    # range(n): chạy từ 0 đến n-1
    # range(start, stop, step):

# Vòng lặp vô hạn - Vòng lặp while
    # while <điều kiện>: lặp đến khi điều kiện sai

# Danh sách - array / list: CRUD
    # C - Create: Tạo PTA18 = []
    # R - Read: Duyệt, in danh sách
        # cách 1: for i in range(len(arr)):
        # cách 2: for item in arr:
        # cách 3: for index, value in enumerate(arr):
        # cách 4: print(arr)
    # U - Update: chỉnh sửa 
        # append(item): thêm phần tử vào cuối danh sách
        # insert(index, item): thêm phần tử vào vị trí index
        # arr[i] = new_value
    # D - Delete: xóa
        # remove(item): xóa bằng giá trị
        # pop(index): xóa bằng chỉ số index
        # clear(): xóa tất cả phần tử
    # Sắp xếp:
        # sort(): sắp xếp tăng dần
        # sort(reversed=True): sắp xếp giảm dần
    # Khác:
        # len(): trả về độ dài (số lượng phần tử)
        # min(): trả về item nhỏ nhất
        # max(): trả về item lớn nhất

# Chuỗi / xâu ký tự
    # len(): độ dài chuỗi
    # strip(): xóa khoảng trắng ở đầu và cuối
    # split(): tách chuỗi
    # replace(): thay thế
    # upper(): chuyển thành chữ hoa
    # lower(): chuyển thành chữ thường
    # capwords(): chuyển chữ cái đầu thành hoa

# Hàm/Chương trình con
    # Hàm có giá trị trả về (return)
    # Hàm có tham số truyền vào: chuvi(cdai, crong)