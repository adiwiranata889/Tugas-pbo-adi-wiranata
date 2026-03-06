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

# =====================================
# CLASS RESTAURANT
# =====================================

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} adalah restoran yang menyajikan {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} sekarang sudah buka!\n")


# =====================================
# MEMBUAT OBJEK DENGAN NAMA BARU
# =====================================

restaurant1 = Restaurant("Rasa Nusantara", "Masakan Indonesia")
restaurant2 = Restaurant("La Dolce Vita", "Masakan Italia")
restaurant3 = Restaurant("El Toro", "Masakan Meksiko")

# =====================================
# MENAMPILKAN DATA
# =====================================

print("=== DATA RESTORAN 1 ===")
print("Nama Restoran :", restaurant1.restaurant_name)
print("Jenis Masakan :", restaurant1.cuisine_type)
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

print("=== DATA RESTORAN 2 ===")
print("Nama Restoran :", restaurant2.restaurant_name)
print("Jenis Masakan :", restaurant2.cuisine_type)
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

print("=== DATA RESTORAN 3 ===")
print("Nama Restoran :", restaurant3.restaurant_name)
print("Jenis Masakan :", restaurant3.cuisine_type)
restaurant3.describe_restaurant()
restaurant3.open_restaurant()
