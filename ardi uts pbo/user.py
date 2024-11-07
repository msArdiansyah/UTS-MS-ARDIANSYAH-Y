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

# Kelas turunan pertama dari User: BasicUser
class BasicUser(User):
    def viewProduct(self, productId):
        print(f"Menampilkan informasi produk dengan ID: {productId}.")

    def addToCart(self, productId, quantity):
        print(f"Menambahkan produk ID {productId} sejumlah {quantity} ke keranjang.")

# Kelas turunan kedua dari BasicUser: PremiumUser
class PremiumUser(BasicUser):
    def applyVoucher(self, voucherCode, cartTotal):
        print(f"Menerapkan voucher {voucherCode} pada total belanja {cartTotal}.")

    def requestPrioritySupport(self, issueDescription):
        print(f"Menghubungi dukungan prioritas dengan masalah: {issueDescription}.")

# Kelas turunan Seller dari User
class Seller(User):
    def addProduct(self, productName, description, price, stock):
        print(f"Produk baru '{productName}' ditambahkan dengan deskripsi '{description}', harga {price}, stok awal {stock}.")

    def processOrder(self, orderId, status):
        print(f"Pesanan dengan ID {orderId} diproses dengan status: {status}.")

# Pembuatan Objek dan Penggunaan Metode
# Objek PremiumUser
premium_user = PremiumUser("Buddy-Anduk", "buddy22@example.com", 101)
premium_user.viewProduct("P5678")
premium_user.addToCart("P5678", 3)
premium_user.applyVoucher("VIPDISCOUNT", 250000)
premium_user.requestPrioritySupport("Produk rusak saat diterima.")

# Objek Seller
seller = Seller("sellerPro", "seller@example.com", 202)
seller.addProduct("Smartphone", "Smartphone dengan fitur unggulan", 3500000, 20)
seller.processOrder("O2002", "selesai")
