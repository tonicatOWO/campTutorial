value = "5"
try:
    result = value + 3  # TypeError - 不允許隱式轉換
except TypeError:
    result = int(value) + 3  # 必須明確轉換
    print(result)  # 輸出: 8
