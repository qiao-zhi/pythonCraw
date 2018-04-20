# set用法，set与list一样，只是存储的不能有重复元素，其次存储的是不可变对象，类似于list就是可变对象
# 创建set(如果集合中有重复元素会自动删除重复元素)
set1=set([1,2,'kkk',3,'wiwiwi'])
print(set1)
print("set1的长度此时是:", len(set1))

# 遍历set(只能用下面这种方式遍历，不能根据下标遍历，set元素没有下标)
for ele in set1:
    print(ele)

# 追加元素(如果元素不存在会加入到set中，如果元素存在则不会追加)
set1.add("mmm")
print(set1)

# 删除元素(如果直接删除而元素不存在于set中会报错)
if 'mmm' in set1:
    set1.remove('mmm')
print(set1)









