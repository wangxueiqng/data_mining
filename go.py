# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd


## 方法一：
def apriori(data_set):
    """创建初始候选集,候选项1项集"""
    print('创建初始候选项1项集')
    c1 = set()
    for items in data_set:
        for item in items:
            # frozenset()返回一个冻结的集合,冻结后集合不能再添加或删除任何元素
            item_set = frozenset([item])
            c1.add(item_set)


def generate_freq_supports(data_set, item_set, min_support):
    """从候选项集中选出频繁项集并计算支持度"""
    print('筛选频繁项集并计算支持度')
    freq_set = set()  # 保存频繁项集元素
    item_count = {}  # 保存元素频次，用于计算支持度
    supports = {}  # 保存支持度

    # 如果项集中元素在数据集中则计数
    for record in data_set:
        for item in item_set:
            # issubset()方法用于判断集合的所有元素是否都包含在指定集合中
            if item.issubset(record):
                if item not in item_count:
                    item_count[item] = 1
                else:
                    item_count[item] += 1

    data_len = float(len(data_set))

    # 计算项集支持度
    for item in item_count:
        if (item_count[item] / data_len) >= min_support:
            freq_set.add(item)
            supports[item] = item_count[item] / data_len

    return freq_set, supports


def generate_new_combinations(freq_set, k):
    """
    根据频繁项集，生成新的候选项1项集
    参数：频繁项集列表 freq_set 与项集元素个数 k
    """
    print('生成新组合')
    new_combinations = set()  # 保存新组合
    sets_len = len(freq_set)  # 集合含有元素个数，用于遍历求得组合
    freq_set_list = list(freq_set)  # 集合转为列表用于索引

    for i in range(sets_len):
        for j in range(i + 1, sets_len):
            l1 = list(freq_set_list[i])
            l2 = list(freq_set_list[j])
            l1.sort()
            l2.sort()

            # 若两个集合的前k-2个项相同时,则将两个集合合并
            if l1[0:k - 2] == l2[0:k - 2]:
                freq_item = freq_set_list[i] | freq_set_list[j]
                new_combinations.add(freq_item)

    return new_combinations


def apriori(data_set, min_support, max_len=None):
    """循环生成候选集并计算其支持度"""
    print('循环生成候选集')
    max_items = 2  # 初始项集元素个数
    freq_sets = []  # 保存所有频繁项集
    supports = {}  # 保存所有支持度

    # 候选项1项集
    c1 = set()
    for items in data_set:
        for item in items:
            item_set = frozenset([item])
            c1.add(item_set)

    # 频繁项1项集及其支持度
    l1, support1 = generate_freq_supports(data_set, c1, min_support)

    freq_sets.append(l1)
    supports.update(support1)

    if max_len is None:
        max_len = float('inf')

    while max_items and max_items <= max_len:
        # 生成候选集
        ci = generate_new_combinations(freq_sets[-1], max_items)
        # 生成频繁项集和支持度
        li, support = generate_freq_supports(data_set, ci, min_support)

        # 如果有频繁项集则进入下个循环
        if li:
            freq_sets.append(li)
            supports.update(support)
            max_items += 1
        else:
            max_items = 0

    return freq_sets, supports


def association_rules(freq_sets, supports, min_conf):
    """生成关联规则"""
    print('生成关联规则')
    rules = []
    max_len = len(freq_sets)

    # 筛选符合规则的频繁集计算置信度，满足最小置信度的关联规则添加到列表
    for k in range(max_len - 1):
        for freq_set in freq_sets[k]:
            for sub_set in freq_sets[k + 1]:
                if freq_set.issubset(sub_set):
                    frq = supports[sub_set]
                    conf = supports[sub_set] / supports[freq_set]
                    rule = (freq_set, sub_set - freq_set, frq, conf)
                    if conf >= min_conf:
                        print(freq_set, "-->", sub_set - freq_set, 'frq:', frq, 'conf:', conf)
                        rules.append(rule)
    return rules


if __name__ == '__main__':
    # 读取淘宝用户行为数据
    data = pd.read_csv(r'D:\关联分析\关联分析2\tianchi_mobile_recommend_train_user.zip', encoding='ansi')
    data = data[['user_id', 'item_id']]

    # 关联规则中不考虑多次购买同一件物品，删除重复数据
    data = data.drop_duplicates()

    # 初始化列表
    data_set = []

    # 分组聚合，同一用户购买多种商品的合并为一条数据，只有1件商品的没有意义，需要进行过滤
    groups = data.groupby(by='user_id')
    for group in groups:
        if len(group[1]) >= 2:
            data_set.append(group[1]['item_id'].tolist())

    # L为频繁项集，support_data为支持度
    L, support_data = apriori(data_set, min_support=0.05)
    association_rules = association_rules(L, support_data, min_conf=0.3)
#    print('关联规则：\n',association_rules)