class ThuCung:
    def __init__(self, ma_thu_cung, ten, loai, gia_tien):
        self.__ma_thu_cung = ma_thu_cung
        self.ten = ten
        self.loai = loai
        self.gia_tien = gia_tien

    # Getter
    def get_ma_thu_cung(self):
        return self.__ma_thu_cung

    def get_ten(self):
        return self.ten

    def get_loai(self):
        return self.loai

    def get_gia_tien(self):
        return self.gia_tien

    def hien_thi(self):
        print(f"Mã thú cưng: {self.__ma_thu_cung}")
        print(f"Tên thú cưng: {self.ten}")
        print(f"Loại: {self.loai}")
        print(f"Giá tiền: {self.gia_tien} VNĐ")
        print("-" * 40)


class CuaHangService:
    def __init__(self):
        self.kho_hang = []
        self.doanh_thu = 0

    def nhap_thu_cung(self):
        ma = input("Nhập mã thú cưng: ")
        ten = input("Nhập tên thú cưng: ")
        loai = input("Nhập loại thú cưng: ")
        gia = float(input("Nhập giá tiền: "))

        thu_cung = ThuCung(ma, ten, loai, gia)

        self.kho_hang.append(thu_cung)

        print("Thêm thú cưng thành công")

    def xem_kho_hang(self):
        if len(self.kho_hang) == 0:
            print("Kho hàng trống")
        else:
            print("\n===== DANH SÁCH THÚ CƯNG =====")

            for thu_cung in self.kho_hang:
                thu_cung.hien_thi()

    def ban_thu_cung(self, ma_thu_cung):
        for thu_cung in self.kho_hang:

            if thu_cung.get_ma_thu_cung() == ma_thu_cung:

                self.doanh_thu += thu_cung.get_gia_tien()

                self.kho_hang.remove(thu_cung)

                print("Bán thú cưng thành công")
                return

        print("Không tìm thấy thú cưng")

    def xem_doanh_thu(self):
        print(f"Tổng doanh thu: {self.doanh_thu} VNĐ")


class GiaoDienConsole:
    def __init__(self):
        self.cua_hang = CuaHangService()

    def chay_chuong_trinh(self):

        while True:

            print("\n===== PET STORE =====")
            print("1. Nhập thú cưng mới")
            print("2. Hiển thị kho hàng")
            print("3. Bán thú cưng")
            print("4. Xem tổng doanh thu")
            print("5. Thoát")

            lua_chon = input("Nhập lựa chọn: ")

            if lua_chon == "1":
                self.cua_hang.nhap_thu_cung()

            elif lua_chon == "2":
                self.cua_hang.xem_kho_hang()

            elif lua_chon == "3":
                ma = input("Nhập mã thú cưng cần bán: ")
                self.cua_hang.ban_thu_cung(ma)

            elif lua_chon == "4":
                self.cua_hang.xem_doanh_thu()

            elif lua_chon == "5":
                print("Thoát chương trình")
                break

            else:
                print("Lựa chọn không hợp lệ")


giao_dien = GiaoDienConsole()
giao_dien.chay_chuong_trinh()