# =====================================
# CLASS USER
# =====================================

class User:
    def __init__(self, first_name, last_name, age, email, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.city = city

    # metode untuk menampilkan informasi user
    def describe_user(self):
        print("=== Informasi User ===")
        print(f"Nama Depan : {self.first_name}")
        print(f"Nama Belakang : {self.last_name}")
        print(f"Umur : {self.age}")
        print(f"Email : {self.email}")
        print(f"Kota : {self.city}")
        print()

    # metode untuk menyapa user
    def greet_user(self):
        print(f"Halo {self.first_name} {self.last_name}, selamat datang!\n")


# =====================================
# MEMBUAT INSTANCE USER
# =====================================

user1 = User("Andi", "Saputra", 20, "andi@gmail.com", "Pekanbaru")
user2 = User("Budi", "Santoso", 22, "budi@gmail.com", "Jakarta")
user3 = User("Siti", "Aisyah", 19, "siti@gmail.com", "Bandung")


# =====================================
# MEMANGGIL METODE
# =====================================

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()