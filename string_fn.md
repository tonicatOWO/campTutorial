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
# Python 字串相關函式

| 函式 | 意義 |
|------|------|
| `str(n)` | 將整數變數 n 轉為字串型態 |
| `len(s)` | 計算字串 s 的長度 |
| `s.lower()` | 將字串中的字母轉成小寫 |
| `s.upper()` | 將字串中的字母轉成大寫 |
| `s.islower()` | 判斷字串中的字母是否皆為小寫 |
| `s.isupper()` | 判斷字串中的字母是否皆為大寫 |
| `s.find('abc')` | 尋找字串中 'abc' 的位置 |
| `s.count('abc')` | 計算字串中 'abc' 出現的次數 |
| `s.replace(舊子字串,新子字串)` | 將字串中的舊子字串用新子字串取代 |
| `s.split()` | 將字串分割成數個子字串(以空白區分) |
| `s.strip()` | 去掉字串左右空白 |
| `s.join(sequence)` | 指定字符(s)連接串列(sequence)中的元素後，生成新字串 |
| `'ab' in 'abcd'` | 判斷 'ab' 是否在 'abcd' |
| `s[::-1]` | 將字串反轉 |
| `[]` 操作 | 同 list |
