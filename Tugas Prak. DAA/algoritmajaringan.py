import heapq
def minimum_spanning_tree(graph, start):
 # Inisialisasi variabel yang diperlukan
 visited = set([start])
 edges = [(cost, start, end) for end, cost in graph[start].items()]
 heapq.heapify(edges)
 mst_cost = 0
 mst_edges = []
 
 # Looping sampai semua simpul dikunjungi
 while edges:
  # Ambil simpul dengan bobot terkecil
  cost, start, end = heapq.heappop(edges)
 # Jika simpul tujuan belum dikunjungi
 if end not in visited:
  # Tambahkan simpul ke daftar simpul yang sudah dikunjungi
  visited.add(end)
  # Tambahkan jarak ke total biaya minimum
  mst_cost += cost
  # Tambahkan edge ke daftar MST
  mst_edges.append((start, end, cost))
  # Tambahkan edge dari simpul tujuan ke daftar edge
  for end_next, cost_next in graph[end].items():
   if end_next not in visited:
    heapq.heappush(edges, (cost_next, end, end_next))
 
 # Kembalikan daftar edge dan total biaya minimum
 return mst_edges, mst_cost

import heapq
# Definisikan grafik dengan jarak antara setiap kota
graph = {
 'Jakarta': {'Bandung': 140, 'Semarang': 400, 'Surabaya': 800},
 'Bandung': {'Jakarta': 140, 'Semarang': 350, 'Surabaya': 900, 'Medan': 1250},
 'Semarang': {'Jakarta': 400, 'Bandung': 350, 'Surabaya': 650},
 'Surabaya': {'Jakarta': 800, 'Bandung': 900, 'Semarang': 650, 'Medan': 1100},
 'Medan': {'Bandung': 1250, 'Surabaya': 1100}
}
# Definisikan fungsi untuk mencari rute terpendek menggunakan algoritma jaringan minimum 
def minimum_spanning_tree(graph, start):
 visited = set([start])
 edges = [(cost, start, end) for end, cost in graph[start].items()]
 heapq.heapify(edges)
 mst_cost = 0
 mst_edges = []
 
 while edges:
  cost, start, end = heapq.heappop(edges)
  if end not in visited:
   visited.add(end)
   mst_cost += cost
   mst_edges.append((start, end, cost))
   for end_next, cost_next in graph[end].items():
    if end_next not in visited:
     heapq.heappush(edges, (cost_next, end, end_next))
 
 return mst_edges, mst_cost
# Cetak rute terpendek dan biaya minimum menggunakan algoritma jaringan minimum
rute, biaya = minimum_spanning_tree(graph, 'Jakarta')
print(f"Rute Terpendek: {rute}")
print(f"Biaya Minimum: {biaya}")