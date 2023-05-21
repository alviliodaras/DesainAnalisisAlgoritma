def plan_trip(n, graph):
   dp = [[float('inf')] * n for _ in range(1 << n)]
   dp[1][0] = 0
   for s in range(1 << n):
     for i in range(n):
       if s & (1 << i):
         for j in range(n):
           if j != i and s & (1 << j):
             dp[s][i] = min(dp[s][i], dp[s ^ (1 << i)][j] + graph[j][i])
             return min(dp[(1 << n) - 1])
           
# Contoh data aktivitas dan ketergantungan
activities = {
  'A': (3, []),
  'B': (2, []),
  'C': (1, ['A', 'B']),
  'D': (2, ['A']),
  'E': (4, ['C', 'D']),
  'F': (3, ['E'])
}
# Hitung nilai awal untuk setiap aktivitas
dp = {activity: activities[activity][0] for activity in activities if not 
      activities[activity][1]}
# Lakukan penghitungan secara bottom-up
for activity in activities:
  if activities[activity][1]:
    max_dependency_time = max([dp[dependency] for dependency in activities[activity][1]])
    dp[activity] = max_dependency_time + activities[activity][0]
# Cetak waktu yang dibutuhkan untuk menyelesaikan seluruh proyek
print(dp['F'])

