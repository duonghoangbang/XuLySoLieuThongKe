import array as arr
import math

# Lab 1

# Trung Binh Mau
def trung_binh_mau(array):
    sumTbMau = sum(array)
    tbMau = sumTbMau/n
    return tbMau

# Phuong Sai Mau
def phuong_sai_mau(array):
    sumPsMau = 0
    for element in array:
        sumPsMau += (element - trung_binh_mau(array))*(element - trung_binh_mau(array))
    psMau = sumPsMau/(n-1)
    return psMau

# Do Lech Chuan Mau
def do_lech_chuan(array):
    sd = math.sqrt(phuong_sai_mau(array))
    return sd

# Trung Vi
def trung_vi(arr):
    # Sắp xếp mảng theo thứ tự tăng dần
    sorted_arr = sorted(arr)
    
    n = len(sorted_arr)
    
    # Nếu số lượng phần tử trong mảng là chẵn
    if n % 2 == 0:
        middle1 = sorted_arr[n // 2 - 1]
        middle2 = sorted_arr[n // 2]
        median = (middle1 + middle2) / 2
    # Nếu số lượng phần tử trong mảng là lẻ
    else:
        median = sorted_arr[n // 2]
    
    return median
        
# Lab 2

# Tao Bang Tan So
def tao_bang_tan_suat(arr, k):
    # Sắp xếp mảng số liệu
    sorted_arr = sorted(arr)
    
    # Tính giá trị tối thiểu và tối đa trong mảng
    min_value = min(arr)
    max_value = max(arr)
    
    # Khởi tạo danh sách khoảng và danh sách tần suất tương ứng
    ranges = []
    frequencies = []
    
    # Bắt đầu từ giá trị tối thiểu
    current_range_start = min_value
    current_range_end = min_value + k
    current_frequency = 0
    
    while current_range_start <= max_value:
        # Đếm số lượng phần tử trong khoảng
        for num in arr:
            if current_range_start <= num < current_range_end:
                current_frequency += 1
        
        # Thêm khoảng và tần suất vào danh sách
        ranges.append((current_range_start, current_range_end))
        frequencies.append(current_frequency)
        
        # Di chuyển đến khoảng tiếp theo
        current_range_start = current_range_end
        current_range_end += k
        current_frequency = 0
    
    return (ranges, frequencies)
    
# Lab 1b
def tim_phan_vi(arr, phan_vi):
    sorted_arr = sorted(arr)
    
    index = (n - 1) * phan_vi
    
    if isinstance(index, int): 
        return sorted_arr[int(index)]
    
    else:
        lower_index = int(index)
        upper_index = lower_index + 1
        lower_value = sorted_arr[lower_index]
        upper_value = sorted_arr[upper_index]
        return (lower_value + upper_value) / 2
    
def phanvi2(arr,phan_vi):
    n=len(arr)
    if 
# Chuong Trinh Chinh
array = arr.array('f', [94.1, 86.1, 95.3, 84.9, 88.8, 84.6, 94.4, 84.1, 93.2, 90.4, 94.1, 78.3, 86.4, 83.6, 96.1, 83.7, 90.6, 89.1, 97.8, 89.6, 85.1, 85.4, 98.0, 82.9, 91.4, 87.3, 93.1, 90.3, 84.0, 89.7, 85.4, 87.3, 88.2, 84.1, 86.4, 93.1, 93.7, 87.6, 86.6, 86.4, 86.1, 90.1, 87.6, 94.6, 87.7, 85.1, 91.7, 84.5, 95.1, 95.2, 94.1, 96.3, 90.6, 89.6, 87.5, 90.0, 86.1, 92.1, 94.7, 89.4, 90.0, 84.2, 92.4, 94.3, 96.4, 91.1, 88.6, 90.1, 85.1, 87.3, 93.2, 88.2, 92.4, 84.1, 94.3, 90.5, 86.6, 86.7, 86.4, 90.6, 82.6, 97.3, 95.6, 91.2, 83.0, 85.0, 89.1, 83.1, 96.8, 88.3])
k = int(input("Nhap Khoang: "))
phanVi = float(input("Nhap Phan Vi: "))

# Tim N
n = len(array)

print("Trung Binh Mau: ", trung_binh_mau(array))
print("Phuong Sai Mau: ", phuong_sai_mau(array))
print("Do Lech Chuan: ", do_lech_chuan(array))
print("Min: ", min(array))
print("Max: ", max(array))
print("Trung Vi: ", trung_vi(array))
print("Bang Tan Suat: ", tao_bang_tan_suat(array, k))
print("Phan vi {:.0%} la: {}".format(phanVi,tim_phan_vi(array, phanVi)))

            
            
            