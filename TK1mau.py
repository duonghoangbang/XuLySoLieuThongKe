#XỬ LÝ SỐ LIỆU THỐNG KÊ
#NHÓM: KHOA HỌC DỮ DỘI 

import numpy as np
import math as m
from scipy import stats
from scipy.stats import chi2

#-----------------------------------------------------------
# Lab 1
# Trung Binh Mau
def trung_binh_mau(data):
    sumTbMau = sum(data)
    tbMau = sumTbMau/len(data)
    print("Trung Binh Mau: ", tbMau)

# Tính phương sai mẫu
def phuong_sai_mau(data):
    sample_mean = np.mean(data)
    # Độ lệch của mỗi phần tử so với giá trị trung bình
    deviations = data - sample_mean
    sample_variance = np.mean(deviations ** 2)
    print("Phuong Sai Mau: ", sample_variance)

# Tính độ lệch chuẩn mẫu
def do_lech_chuan(data):
    sample_mean = np.mean(data)
    print("Do Lech Chuan: ", sample_mean)

# Min
def Arrmin(data):
    min = np.min(data)
    return min
    print("Min: ", min)

# Max
def Arrmax(data):
    max = np.max(data)
    print("Max: ", max)

# Trung Vi
def trung_vi(arr):
    # Sắp xếp mảng theo thứ tự tăng dần
    sorted_arr = sorted(arr)
    
    n = len(sorted_arr)
    
    # Nếu số lượng phần tử trong mảng là chẵn
    if len(arr) % 2 == 0:
        middle1 = sorted_arr[len(arr) // 2 - 1]
        middle2 = sorted_arr[len(arr) // 2]
        median = (middle1 + middle2) / 2
    # Nếu số lượng phần tử trong mảng là lẻ
    else:
        median = sorted_arr[len(arr) // 2]
    
    print("Trung Vi: ", median)
        
# Lab 1b
def tim_phan_vi(data, phan_vi):
    sorted_arr = np.sort(data)
    
    index = (len(data) - 1) * phan_vi
    
    if isinstance(index, int): 
        print("Phan vi {:.0%} la: {}".format(phan_vi,sorted_arr[int(index)]))

    
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
def tao_bang_tan_suat(data, k):
    # Sắp xếp mảng số liệu
    sorted_arr = np.sort(data)
    
    # Tính giá trị tối thiểu và tối đa trong mảng
    min_value = min(data)
    max_value = max(data)
    
    # Khởi tạo danh sách khoảng và danh sách tần suất tương ứng
    ranges = []
    frequencies = []
    
    # Bắt đầu từ giá trị tối thiểu
    current_range_start = min_value
    current_range_end = min_value + k
    current_frequency = 0
    
    while current_range_start <= max_value:
        # Đếm số lượng phần tử trong khoảng
        for num in data:
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

def Thong_ke_1_mau(data, alternative, alpha):
    x_bar, p_value, confidence_interval, result = t_test(data, trung_binh_mau(data), alternative, alpha)
    print("Trung bình mẫu:", x_bar)
    print("p-value:", p_value)
    print("Khoảng tin cậy:", confidence_interval)
    if result:
        print("Bác bỏ giả thuyết H0")
    else:
        print("Chưa đủ cơ sở bác bỏ giả thuyết H0")  

#------------------------------------------------------
# Lab 4
def variance_test(data, direction, alpha, population_variance):
    n = len(data)
    sample_variance = np.var(data,ddof=1)
    test_statistic = (n - 1) * sample_variance / (population_variance*population_variance)
    
    q1 = chi2.ppf(alpha / 2, n - 1)
    q2 = chi2.ppf(1 - (alpha / 2), n - 1)
    
    # Calculate confidence interval
    lower_ci = (n - 1) * sample_variance / q2
    upper_ci = (n - 1) * sample_variance / q1
    
    if direction == "lower":
        p_value = chi2.cdf(test_statistic, n - 1)
        dof = n - 1
    elif direction == "upper":
        p_value = 1 - chi2.cdf(test_statistic, n - 1)
        dof = n - 1
    else:
        p_value = 2 * min(1 - chi2.cdf(test_statistic, n - 1),chi2.cdf(test_statistic, n - 1))
        dof = n - 1
    
    confidence_interval = (1 - alpha) * 100
    
    if direction == "lower":
        test_type = "Lower Tail Variance Test"
    elif direction == "upper":
        test_type = "Upper Tail Variance Test"
    else:
        test_type = "Two-Tailed Variance Test"
    
    return test_type, p_value, dof, confidence_interval, lower_ci, upper_ci

def Thong_Ke_1_Mau(data, direction, alpha, population_variance):
    test_type, p_value, dof, confidence_interval, lower_ci, upper_ci = variance_test(data, direction, alpha, population_variance)
    print("Loai kiem dinh:", test_type)
    print("p-value:", p_value)
    print("Bac tu do:", dof)
    print(f"Khoảng tin cậy cho phương sai: ({lower_ci}, {upper_ci})")
    if p_value <= alpha:
        print('Reject NULL HYPOTHESIS')
    else:
        print('Accept NULL HYPOTHESIS')

#------------------------------------------------------
# Lab 5
# def Kiem_dinh_2_mau(vector1, vector2, alpha, sample_mean1, sample_mean2, alternative):
#     sample_mean1 = 0
#     sample_mean2 = 0

#     print("Neu khong co do lech chuan mau, nhap 0")
#     sample_mean1 = int(input("Nhap do lech chuan mau 1: "))
#     sample_mean2 = int(input("Nhap do lech chuan mau 2: "))
#     phuong_sai_mau(vector1)
#     trung_binh_mau(vector1)
#     phuong_sai_mau(vector2)
#     trung_binh_mau(vector2)
#     print("Loai kiem dinh: ", alternative)

        



