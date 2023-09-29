#XỬ LÝ SỐ LIỆU THỐNG KÊ
#NHÓM: KHOA HỌC DỮ DỘI 

import numpy as np
import math as m
from scipy import stats

#-----------------------------------------------------------
# Lab 1
# Trung Binh Mau
def trung_binh_mau(array):
    sumTbMau = sum(array)
    tbMau = sumTbMau/len(array)
    print("Trung Binh Mau: ", tbMau)

# Tính phương sai mẫu
def phuong_sai_mau(array):
    # Độ lệch của mỗi phần tử so với giá trị trung bình
    deviations = data - sample_mean
    sample_variance = np.mean(deviations ** 2)

# Tính độ lệch chuẩn mẫu
def do_lech_chuan(data):
    sample_mean = np.mean(data)
    print("Do Lech Chuan: ", sample_mean)

# Min
def min(array):
    min = np.min(array)
    return min
    print("Min: ", min)

# Max
def max(array):
    max = np.max(array)
    print("Max: ", max)

# Trung Vi
def trung_vi(arr):
    # Sắp xếp mảng theo thứ tự tăng dần
    sorted_arr = sorted(arr)
    
    n = len(sorted_arr)
    
    # Nếu số lượng phần tử trong mảng là chẵn
    if len(array) % 2 == 0:
        middle1 = sorted_arr[len(array) // 2 - 1]
        middle2 = sorted_arr[len(array) // 2]
        median = (middle1 + middle2) / 2
    # Nếu số lượng phần tử trong mảng là lẻ
    else:
        median = sorted_arr[len(array) // 2]
    
    print("Trung Vi: ", median)
        
# Lab 1b
def tim_phan_vi(array, phan_vi):
    sorted_arr = np.sort(array)
    
    index = (len(array) - 1) * phan_vi
    
    if isinstance(index, int): 
        print("Phan vi {:.0%} la: {}".format(phanVi,sorted_arr[int(index)]))

    
    else:
        lower_index = int(index)
        upper_index = lower_index + 1
        lower_value = sorted_arr[lower_index]
        upper_value = sorted_arr[upper_index]
        return (lower_value + upper_value) / 2
        print("Phan vi {:.0%} la: {}".format(phanVi,(lower_value + upper_value) / 2))
    
#-----------------------------------------------------------
# Lab 2
# Tao Bang Tan So
def tao_bang_tan_suat(array, k):
    # Sắp xếp mảng số liệu
    sorted_arr = np.sort(array)
    
    # Tính giá trị tối thiểu và tối đa trong mảng
    min_value = min(array)
    max_value = max(array)
    
    # Khởi tạo danh sách khoảng và danh sách tần suất tương ứng
    ranges = []
    frequencies = []
    
    # Bắt đầu từ giá trị tối thiểu
    current_range_start = min_value
    current_range_end = min_value + k
    current_frequency = 0
    
    while current_range_start <= max_value:
        # Đếm số lượng phần tử trong khoảng
        for num in array:
            if current_range_start <= num < current_range_end:
                current_frequency += 1
        
        # Thêm khoảng và tần suất vào danh sách
        ranges.append((current_range_start, current_range_end))
        frequencies.append(current_frequency)
        
        # Di chuyển đến khoảng tiếp theo
        current_range_start = current_range_end
        current_range_end += k
        current_frequency = 0

    print("Bang Tan Suat: ", ranges, frequencies)

#------------------------------------------------------
# Lab 3
def t_test(data, mu, alternative="two-sided", alpha=0.05):
    # Tính trung bình mẫu và phương sai mẫu
    x_bar = np.mean(data)
    s2 = np.var(data, ddof=1)
    n = len(data)

    # Tính giá trị kiểm định t
    t_stat = (x_bar - mu) / (np.sqrt(s2 / n))

    # Tính sai số
    if alternative == "two-sided":
        t_alpha_2 = stats.t.ppf(1 - alpha / 2, df=n - 1)
        margin_of_error = t_alpha_2 * (np.sqrt(s2) / np.sqrt(n))
    elif alternative == "greater":
        t_alpha = stats.t.ppf(1 - alpha, df=n - 1)
        margin_of_error = t_alpha * (np.sqrt(s2) / np.sqrt(n))
    elif alternative == "less":
        t_alpha = stats.t.ppf(alpha, df=n - 1)
        margin_of_error = t_alpha * (np.sqrt(s2) / np.sqrt(n))

    # Tính giá trị p-value
    if alternative == "two-sided":
        p_value = 2 * (1 - stats.t.cdf(np.abs(t_stat), df=n - 1))
    elif alternative == "greater":
        p_value = 1 - stats.t.cdf(t_stat, df=n - 1)
    elif alternative == "less":
        p_value = stats.t.cdf(t_stat, df=n - 1)

    # Tính khoảng tin cậy
    confidence_interval = (x_bar - margin_of_error, x_bar + margin_of_error)
    result = p_value < alpha
    return x_bar, p_value, confidence_interval, result

def Thong_ke_1_mau(array, alternative, alpha):
    x_bar, p_value, confidence_interval, result = t_test(array, trung_binh_mau(array), alternative, alpha)
    print("Trung bình mẫu:", x_bar)
    print("p-value:", p_value)
    print("Khoảng tin cậy:", confidence_interval)
    if result:
        print("Bác bỏ giả thuyết H0")
    else:
        print("Chưa đủ cơ sở bác bỏ giả thuyết H0")  

#------------------------------------------------------
# Lab 4


# Chuong Trinh Chinh
array = np.array([94.1, 86.1, 95.3, 84.9, 88.8, 84.6, 94.4, 84.1, 93.2, 90.4, 94.1, 78.3, 86.4, 83.6, 96.1, 83.7, 90.6, 89.1, 97.8, 89.6, 85.1, 85.4, 98.0, 82.9, 91.4, 87.3, 93.1, 90.3, 84.0, 89.7, 85.4, 87.3, 88.2, 84.1, 86.4, 93.1, 93.7, 87.6, 86.6, 86.4, 86.1, 90.1, 87.6, 94.6, 87.7, 85.1, 91.7, 84.5, 95.1, 95.2, 94.1, 96.3, 90.6, 89.6, 87.5, 90.0, 86.1, 92.1, 94.7, 89.4, 90.0, 84.2, 92.4, 94.3, 96.4, 91.1, 88.6, 90.1, 85.1, 87.3, 93.2, 88.2, 92.4, 84.1, 94.3, 90.5, 86.6, 86.7, 86.4, 90.6, 82.6, 97.3, 95.6, 91.2, 83.0, 85.0, 89.1, 83.1, 96.8, 88.3])

k = int(input("Nhap Khoang: "))
phanVi = float(input("Nhap Phan Vi: "))

trung_binh_mau(array)


            
            