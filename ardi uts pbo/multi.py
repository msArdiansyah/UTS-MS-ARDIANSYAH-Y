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

# Contoh penggunaan
# Membuat objek pengguna Premium
premium_user = PremiumUser("Dimas", "dimas@example.com", 101)

# Login dan logout
premium_user.login()
premium_user.logout()

# Fitur BasicUser
premium_user.viewProduct("P1234")
premium_user.addToCart("P1234", 2)

# Fitur PremiumUser
premium_user.applyVoucher("DISKON50", 500000)
premium_user.requestPrioritySupport("Produk tidak terkirim.")
