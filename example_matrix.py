def array_operations():
    # 一維陣列初始化
    arr = [0] * 10  # 建立大小為10，值為0的陣列
    arr_with_value = [4] * 5  # [4, 4, 4, 4, 4]
    
    # 二維陣列初始化
    matrix = [[0 for _ in range(5)] for _ in range(3)]  # 3x5矩陣
    
    return arr, matrix

def array_algorithms():
    nums = [64, 34, 25, 12, 22, 11, 90]
    
    # 排序
    sorted_asc = sorted(nums)
    sorted_desc = sorted(nums, reverse=True)
    
    # 查找最大最小值
    max_val = max(nums)
    min_val = min(nums)
    
    return sorted_asc, max_val, min_val

def subarray_operations(arr):
    n = len(arr)
    # 找出所有子陣列的最大和 (Kadane's Algorithm)
    max_sum = current_sum = arr[0]
    
    for i in range(1, n):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

