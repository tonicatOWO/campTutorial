# What is for ? while ?

用來遍歷一個可迭代物件（列表、字串、範圍、字典等），迴圈次數是預先已知或可以由被遍歷的物件決定。

# How to use for & while?

遍歷列表

```Python

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 搭配 range() 產生數字序列
for i in range(5):
    print(i)  # 0 ~ 4

```

簡單的 while example
當需要無限迴圈時，可以使用 while true

```Python
while True:
    print("柚子廚蒸鵝心\n Ciallo～(∠・ω< )⌒☆")
```

也可以加上判斷式，重複直到達成條件

```Python
i = 0
while i < 144514:
    i += 1
    if i % 10000 == 0:
        print(f"[哼] 進度：{i} 次")
    else:
        print("你是一個，一個一個一個…哼啊啊啊啊啊！！！")
```

# break 以及 continue 語句的應用

break 語句可以提前終止迴圈：

```Python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break  # 遇到 banana 就停止
    print(fruit)
# 只輸出：apple

```

continue 語句可以跳過當前迭代，繼續下一次:

```Python
for i in range(1, 6):
    if i == 3:
        continue  # 跳過 3
    print(i)
# 輸出：1, 2, 4, 5
```

還可以...
嵌套迴圈(迴圈內還可以有其他迴圈)：

```Python
# 二維列表遍歷
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for num in row:
        print(num, end=" ")
    print()  # 換行

# 輸出：
# 1 2 3
# 4 5 6
# 7 8 9
```

遍歷字典:

```Python
student = {"name": "小明", "age": 20, "grade": "A"}

# 遍歷鍵
for key in student:
    print(key)

# 遍歷值
for value in student.values():
    print(value)

# 同時遍歷鍵和值
for key, value in student.items():
    print(f"{key}: {value}")
```

# Python 基本索引概念

正索引 (Positive Index)
從左邊開始計算，起始值為 0：

```Python
text = "Python"
#      P y t h o n
#      0 1 2 3 4 5

print(text[0])  # 'P'
print(text[1])  # 'y'
print(text[5])  # 'n'

# 列表索引
numbers = [10, 20, 30, 40, 50]
#          0   1   2   3   4
print(numbers[0])  # 10
print(numbers[3])  # 40
```

負索引 (Negative Index)

從右邊開始計算，起始值為 -1：

```Python
text = "Python"
#      P  y  t  h  o  n
#     -6 -5 -4 -3 -2 -1

print(text[-1])  # 'n' (最後一個)
print(text[-2])  # 'o' (倒數第二個)
print(text[-6])  # 'P' (第一個)

# 列表負索引
numbers = [10, 20, 30, 40, 50]
#         -5  -4  -3  -2  -1
print(numbers[-1])  # 50 (最後一個)
print(numbers[-3])  # 30 (倒數第三個)
```

切片索引 (Slicing)
使用 [start : end : step] 語法來擷取部分序列：

```Python
text = "Python Programming"
#       0123456789...

# 基本切片
print(text[0:6])    # 'Python' (索引 0 到 5)
print(text[7:])     # 'Programming' (索引 7 到結尾)
print(text[:6])     # 'Python' (開頭到索引 5)

# 負索引切片
print(text[-11:])   # 'Programming' (倒數第 11 個到結尾)
print(text[:-12])   # 'Python' (開頭到倒數第 13 個)

# 步長切片
print(text[::2])    # 'Pto rgamn' (每隔 2 個字元)
print(text[::-1])   # 'gnimmargorP nohtyP' (反轉字串)
```

多維序列索引
嵌套列表 (二維列表)

```Python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])     # [1, 2, 3] (第一行)
print(matrix[0][1])  # 2 (第一行第二列)
print(matrix[2][0])  # 7 (第三行第一列)
print(matrix[-1][-1]) # 9 (最後一行最後一列)
```

字典索引
字典使用鍵 (key) 作為索引：

```Python
student = {
    "name": "小明",
    "age": 18,
    "grade": "高三"
}

print(student["name"])   # '小明'
print(student["age"])    # 18

# 安全訪問 (避免 KeyError)
print(student.get("phone", "未設定"))  # '未設定'
```

索引相關方法
enumerate() - 同時取得索引和值

```Python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"索引 {index}: {fruit}")

# 輸出:
# 索引 0: apple
# 索引 1: banana
# 索引 2: cherry
```

index() 方法 - 尋找元素索引

```Python
colors = ["red", "green", "blue", "green"]

print(colors.index("green"))     # 1 (第一個 green 的索引)
print(colors.index("blue"))      # 2

# 在指定範圍內搜尋
print(colors.index("green", 2))  # 3 (從索引 2 開始找 green)
```

實用技巧
取得序列的第一個和最後一個元素:

```Python
data = [1, 2, 3, 4, 5]

first = data[0]    # 第一個元素
last = data[-1]    # 最後一個元素

# 更安全的方式
first = data[0] if data else None # 用於錯誤處理，避免error
last = data[-1] if data else None
```

# Python 字串相關函式

| 函式                           | 意義                                                |
| ------------------------------ | --------------------------------------------------- |
| `str(n)`                       | 將整數變數 n 轉為字串型態                           |
| `len(s)`                       | 計算字串 s 的長度                                   |
| `s.lower()`                    | 將字串中的字母轉成小寫                              |
| `s.upper()`                    | 將字串中的字母轉成大寫                              |
| `s.islower()`                  | 判斷字串中的字母是否皆為小寫                        |
| `s.isupper()`                  | 判斷字串中的字母是否皆為大寫                        |
| `s.find('abc')`                | 尋找字串中 'abc' 的位置                             |
| `s.count('abc')`               | 計算字串中 'abc' 出現的次數                         |
| `s.replace(舊子字串,新子字串)` | 將字串中的舊子字串用新子字串取代                    |
| `s.split()`                    | 將字串分割成數個子字串(以空白區分)                  |
| `s.strip()`                    | 去掉字串左右空白                                    |
| `s.join(sequence)`             | 指定字符(s)連接串列(sequence)中的元素後，生成新字串 |
| `'ab' in 'abcd'`               | 判斷 'ab' 是否在 'abcd'                             |
| `s[::-1]`                      | 將字串反轉                                          |
| `[]` 操作                      | 同 list                                             |
