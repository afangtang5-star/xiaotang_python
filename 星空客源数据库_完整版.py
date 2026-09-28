# 空柜子起步，给2~3个客户建档（假号码！）
kehu = {
    "张姐": {"dianhua": "13800001111", "yusuan": 300, "xuqiu": "三房"},
    "李哥": {"dianhua": "13900002222", "yusuan": 150, "xuqiu": "两房"},
    "王叔": {"dianhua": "13700003333", "yusuan": 500, "xuqiu": "别墅"}
}

# get查一个不存在的人，给句默认话术
chaxun = kehu.get("陈姐", "这个客户还没建档，回头我问问")
print(chaxun)

# 三种巡法各来一遍
print("\n--- 巡法一：keys() 念名字 ---")
for mingzi in kehu.keys():
    print("客户：", mingzi)

print("\n--- 巡法二：values() 看内容 ---")
for neirong in kehu.values():
    print("资料：", neirong)

print("\n--- 巡法三：items() 全套巡 ---")
for mingzi, neirong in kehu.items():
    print(f"{mingzi} → {neirong}")

# 加分题：把某个客户的需求改成一串标签
kehu["李哥"]["xuqiu"] = ["两房", "朝南", "带电梯"]
print("\n--- 改完李哥的需求 ---")
print(kehu["李哥"])
