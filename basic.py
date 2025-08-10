# 以下兩者是等價的
print('')
print("")

print('") # 這是不正確的寫法，會導致語法錯誤，需要以同樣地符號來結束字串

# A trial of skill

# 試著打印除 "hello——world" 這個字串以外的所有字串

# frting 
fstring = "hello——world"
print(f"{fstring}")  # 正確的寫法，使用 f-string 格式化輸出

name = "小明"
age = 25
city = "嘉義"

message = f"我是 {name}，今年 {age} 歲，住在 {city}"
print(message)  # 我是 小明，今年 25 歲，住在 嘉義

x, y = 10, 20
print(f"加法：{x} + {y} = {x + y}")      # 加法：10 + 20 = 30
print(f"乘法：{x} * {y} = {x * y}")      # 乘法：10 * 20 = 200

# 複雜表達式
radius = 5
print(f"圓面積 = {3.14159 * radius ** 2:.2f}")  # 圓面積 = 78.54

# 條件表達式
temperature = 30
print(f"今天{temperature}°C，{'很熱' if temperature > 25 else '涼爽'}")
# 今天30°C，很熱

# 結合多種格式控制的實際應用
students = [
    {"name": "張三", "math": 85.5, "english": 92.0},
    {"name": "李四", "math": 78.3, "english": 88.5},
    {"name": "王五", "math": 95.8, "english": 91.2}
]

print("學生成績表")
print("-" * 40)
print(f"{'姓名':^8} {'數學':^8} {'英文':^8} {'平均':^8}")
print("-" * 40)

for student in students:
    avg = (student['math'] + student['english']) / 2
    print(f"{student['name']:^8} {student['math']:^8.1f} {student['english']:^8.1f} {avg:^8.1f}")
