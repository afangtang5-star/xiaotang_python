print("========== 第1题：预算判断（input + int + if） ==========")
# 客户说预算，判断够不够200万
budget = int(input("客户预算（万）？："))
if budget >= 200:
    print("够！安排核心房源")
else:
    print("不够，看看刚需小户型")

print("\n========== 第2题：客源轮流分配（for + % 取余） ==========")
# 10组客源，4个业务员，轮流发（i % 4 让序号循环 0,1,2,3）
print("10组客源，4个业务员，轮流分配：")
for i in range(10):
    print(f"客源{i} → 业务员{i % 4}")

print("\n========== 第3题：接待循环（while） ==========")
# 前台接待：输入y接待下一位，输入其他打烊
choice = input("输入y接待下一位（其他键打烊）：")
while choice == "y":
    print("接待下一位客户~")
    choice = input("继续？输入y：")
print("打烊啦！")