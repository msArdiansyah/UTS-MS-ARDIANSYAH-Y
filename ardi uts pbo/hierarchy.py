# Kelas dasar User
class User:
    def __init__(self, username, email, userId):
        self.username = username
        self.email = email
        self.userId = userId

    def login(self):
        print(f"Pengguna {self.username} dengan email {self.email} berhasil login.")

    def logout(self):
        print(f"Pengguna {self.username} berhasil logout.")

# Kelas turunan Seller dari User
class Seller(User):
    def addProduct(self, productName, description, price, stock):
        print(f"Produk baru '{productName}' ditambahkan dengan deskripsi '{description}', harga {price}, stok awal {stock}.")

    def processOrder(self, orderId, status):
        print(f"Pesanan dengan ID {orderId} diproses dengan status: {status}.")

# Kelas turunan Admin dari User
class Admin(User):
    def removeUser(self, userId):
        print(f"Pengguna dengan ID {userId} telah dihapus dari sistem.")

    def generateReport(self, reportType, startDate, endDate):
        print(f"Menghasilkan laporan tipe '{reportType}' dari tanggal {startDate} sampai {endDate}.")

# Contoh penggunaan
# Membuat objek pengguna dengan peran Seller dan Admin
seller = Seller("Toko123", "toko123@example.com", 201)
admin = Admin("Admin01", "admin01@example.com", 301)

# Fitur Seller
seller.login()
seller.addProduct("Laptop", "Laptop gaming dengan spesifikasi tinggi", 15000000, 10)
seller.processOrder("O1001", "dalam pengiriman")
seller.logout()

# Fitur Admin
admin.login()
admin.removeUser(201)
admin.generateReport("transaksi", "2024-01-01", "2024-12-31")
admin.logout()
