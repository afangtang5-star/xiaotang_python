# -*- coding: utf-8 -*-
"""
8.2.4 等效的函数调用 + 8.2.5 避免实参错误
============================================
学习目标：
1. 理解"等效调用"——同一个结果可以有多种写法
2. 认识两类实参错误，会读报错
3. 掌握避错三板斧
"""


def describe_client(name, budget, house_type="公寓"):
    """接需求表：姓名、预算、房源类型（默认公寓）"""
    print("名字:" + name)
    print("预算:" + str(budget) + "万")
    print("类型:" + house_type)
    print("---")


# ========== 8.2.4 等效调用：下面 5 种输出完全一样 ==========
print("【方式1】位置 + 默认值（最简洁）")
describe_client("小王", )

print("【方式2】全位置（显式写清楚）")
describe_client("小王", 50, "公寓","朝南")

print("【方式3】关键字 + 默认值（不怕顺序错）")
describe_client(name="小王", 50)

print("【方式4】关键字乱序（参数多记不住顺序时）")
describe_client(budget=50, name="小王")

print("【方式5】混搭：位置在前，关键字在后")
describe_client("小王", budget=50)


# ========== 8.2.5 避错练习：故意犯错，看报错 ==========
# 取消下面任意一行的注释（删掉行首的 # ），运行看报错

# print("【错误1】少传 budget")
# describe_client("小王")
# 报错：TypeError: describe_client() missing 1 required positional argument: 'budget'

# print("【错误2】多传一个参数")
# describe_client("小王", 50, "公寓", "朝南")
# 报错：TypeError: describe_client() takes 3 positional arguments but 4 were given

# print("【错误3】位置参数放在关键字后面")
# describe_client(name="小王", 50)
# 报错：SyntaxError: positional argument follows keyword argument
