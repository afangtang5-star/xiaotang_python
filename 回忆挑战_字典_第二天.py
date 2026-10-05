customers = {
    "C001": {"name": "张三", "budget": 300, "area": "A区"},
    "C002": {"name": "李四", "budget": 500, "area": "B区"}
}

# 2. 改掉一个客户的预算（两刀切：先定位门牌，再切内页签）
customers["C001"]["budget"] = 280  # 张三预算改为280万

# 3. get查一个不存在的人，给句你的话术
# 查C003，不存在则返回默认话术，不报错
result = customers.get("C003", "该客户暂未入库，管家继续巡房中")
print(result)

# 4. 任选一种巡法巡一遍（遍历外层门牌 + 里层页签）
for cid, info in customers.items():
    print(f"门牌:{cid} | 客户:{info['name']} | 预算:{info['budget']}万 | 区域:{info['area']}")

# 假号检查（确认C001已修改，C002未动）
print("假号检查:", customers["C001"]["budget"], customers["C002"]["budget"])
