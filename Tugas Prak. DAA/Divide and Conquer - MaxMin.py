def max_in_array(arr, low, high):
    # Base case: jika array hanya memiliki satu elemen
    if low == high:
        return arr[low]
    
    # Divide: menentukan titik tengah array
    mid = (low + high) // 2
    
    # Conquer: mencari nilai maksimum di setiap setengah array
    left_max = max_in_array(arr, low, mid)
    right_max = max_in_array(arr, mid+1, high)
    
    # Combine: membandingkan nilai maksimum dari setengah array
    return max(left_max, right_max)

arr = [3, 5, 2, 7, 9, 1, 4, 6, 8]
max_value = max_in_array(arr, 0, len(arr)-1)
print("Nilai maksimum dalam array adalah:", max_value)