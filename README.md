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
