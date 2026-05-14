class NhanVien:
    def __init__(self, ma_nv, ten):
        self.ma_nv = ma_nv
        self.ten = ten

    def tinh_luong(self):
        pass


class NhanVienFullTime(NhanVien):
    def __init__(self, ma_nv, ten, luong_co_ban):
        super().__init__(ma_nv, ten)
        self.luong_co_ban = luong_co_ban

    def tinh_luong(self):
        return self.luong_co_ban


class NhanVienPartTime(NhanVien):
    def __init__(self, ma_nv, ten, so_gio_lam, luong_theo_gio):
        super().__init__(ma_nv, ten)
        self.so_gio_lam = so_gio_lam
        self.luong_theo_gio = luong_theo_gio

    def tinh_luong(self):
        return self.so_gio_lam * self.luong_theo_gio


# Tạo danh sách nhân viên
danh_sach_nhan_vien = [
    NhanVienFullTime("FT01", "Nguyễn Văn A", 15000000),
    NhanVienFullTime("FT02", "Trần Thị B", 12000000),
    NhanVienPartTime("PT01", "Lê Văn C", 80, 50000),
    NhanVienPartTime("PT02", "Phạm Thị D", 60, 40000)
]

# Hiển thị thông tin và lương
print("DANH SÁCH NHÂN VIÊN")
print("-" * 40)

for nhan_vien in danh_sach_nhan_vien:
    print("Mã nhân viên:", nhan_vien.ma_nv)
    print("Tên nhân viên:", nhan_vien.ten)
    print("Lương:", nhan_vien.tinh_luong(), "VNĐ")
    print("-" * 40)