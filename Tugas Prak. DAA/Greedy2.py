def select_restaurant(restaurants, budget):
   selected_restaurant = None
   # Urutkan daftar restoran berdasarkan harga dari murah ke mahal
   sorted_restaurants = sorted(restaurants, key=lambda x: x["price"])
   # Pilih restoran dengan harga yang sesuai dengan budget
   for restaurant in sorted_restaurants:
     if restaurant["price"] <= budget:
       selected_restaurant = restaurant
       break
   # Jika tidak ada restoran yang sesuai, pilih restoran termurah
   if not selected_restaurant:
      selected_restaurant = sorted_restaurants[0]
   return selected_restaurant
     
restaurants = [
   {"name": "Warung Padang", "price": 20000, "rating": 4.0},
   {"name": "Bakso Malang", "price": 25000, "rating": 4.5},
   {"name": "Sate Kambing", "price": 30000, "rating": 4.2},
   {"name": "Ayam Geprek", "price": 35000, "rating": 4.8},
   {"name": "Pizza Hut", "price": 40000, "rating": 4.1}
   ]

budget = 30000

selected_restaurant = select_restaurant(restaurants, budget)
print(f"Restoran yang dipilih adalah {selected_restaurant['name']} dengan harga {selected_restaurant['price']} dan rating {selected_restaurant['rating']}")