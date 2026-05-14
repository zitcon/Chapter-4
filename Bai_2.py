class TaiKhoan:
    def __init__(self, ten_chu_the, so_du=0):
        self.ten_chu_the = ten_chu_the
        self.__so_du = so_du

    def gui_tien(self, so_tien):
        if so_tien > 0:
            self.__so_du += so_tien
            print(f"Gửi thành công {so_tien} VNĐ")
        else:
            print("Số tiền gửi không hợp lệ")

    def rut_tien(self, so_tien):
        if so_tien > 0 and so_tien <= self.__so_du:
            self.__so_du -= so_tien
            print(f"Rút thành công {so_tien} VNĐ")
        else:
            print("Rút tiền thất bại")

    def kiem_tra_so_du(self):
        return self.__so_du


# Tạo tài khoản
tai_khoan_1 = TaiKhoan("Nguyễn Văn A", 1000000)

# Kiểm tra số dư ban đầu
print("Tên chủ thẻ:", tai_khoan_1.ten_chu_the)
print("Số dư ban đầu:", tai_khoan_1.kiem_tra_so_du(), "VNĐ")

print()

# Gửi tiền
tai_khoan_1.gui_tien(500000)

# Kiểm tra số dư
print("Số dư hiện tại:", tai_khoan_1.kiem_tra_so_du(), "VNĐ")

print()

# Rút tiền
tai_khoan_1.rut_tien(300000)

# Kiểm tra số dư
print("Số dư hiện tại:", tai_khoan_1.kiem_tra_so_du(), "VNĐ")

print()

# Thử rút quá số dư
tai_khoan_1.rut_tien(2000000)

# Kiểm tra số dư cuối cùng
print("Số dư cuối cùng:", tai_khoan_1.kiem_tra_so_du(), "VNĐ")