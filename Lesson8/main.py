import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtCore, QtWidgets
from PyQt6 import uic

# xử lý
app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('lesson8.ui', self)
        # Khai báo dự kiện ấn nút
            # 4 nút trên navigation
        # self.pushButton_home_w.clicked.connect(switch_window(Home()))
        # khi thay đổi số lượng vé
        self.spinBox_film1.valueChanged.connect(self.update_price)
        self.spinBox_film2.valueChanged.connect(self.update_price)
        self.spinBox_popcorn.valueChanged.connect(self.update_price)
        self.spinBox_luckyBox.valueChanged.connect(self.update_price)
        # Khi ấn thanh toán
        self.pushButton_checkout.clicked.connect(self.checkout)

    # Phương thức cập nhật số tiền khi thay đổi số lượng vé/popcorn
    def update_price(self):
        # Khởi tạo giá cho các sản phẩm
        price = {
            'film1': 120000,
            'film2': 110000,
            'popcorn': 150000,
            'luckyBox': 100000
        }
        # Biến lưu trữ giá tổng tiền
        total = 0
        # Tính số lượng theo từng loại sản phẩm
        total += price["film1"] * int(self.spinBox_film1.text())
        total += price["film2"] * int(self.spinBox_film2.text())
        total += price["popcorn"] * int(self.spinBox_popcorn.text())
        total += price["luckyBox"] * int(self.spinBox_luckyBox.text())
        # Hiện số tiền lên lineEdit
        self.lineEdit_total.setText(str(total) + ' VND')

    # Phương thức thanh toán
    def checkout(self):
        # Hiện thông báo
        msg_box('Thanh toán thành công', f'Số tiền: {self.lineEdit_total.text()}')

# Hàm hiển thị thông báo
def msg_box(title, content):
    msg = QtWidgets.QMessageBox()
    msg.setStyleSheet("QLabel{min-width: 200px;}"
                          "QLabel{max-width: 200px;}"
                          "QMessageBox{background-color:rgba(35,36,40,255);}"
                          "QPushButton{background-color:rgb(30,95,181);}"
                          "QLabel{color:rgb(255,255,255);}"
                          "QPushButton{color:rgb(255,255,255);}")
    msg.setWindowTitle(title)
    msg.setInformativeText(content)
    msg.exec()

# Chuyển cửa sổ giao diện
def switch_window(classw):
    global window
    window = classw
    window.show()

# Run app
window = MainWindow()
window.show()
sys.exit(app.exec())