import pandas as pd
from pandas import Series, DataFrame


def clean():
    df = DataFrame(pd.read_csv('./data.csv'))
    # 对列进行重命名
    df.rename(columns={0: 'user_id', 1: 'item_id', 2: 'behavior_type', 3: 'user_geohash', 4: 'item_category'}, inplace=True)
    # 对整行为空值的数据进行删除
    df.dropna(how='all', inplace=True)
    # 使用平均值来填充缺失的值
    df[u'体重'].fillna(int(df[u'user_id'].mean()), inplace=True)
    df.columns = df.columns.str.upper()
    df['user_geohash'].replace({r'[^\x00-\x7f]+': ''}, regex=True, inplace=True)
    df['user_geohash'].replace({r'\?+': ''}, regex=True, inplace=True)
    df['user_geohash'] = df['user_geohash'].map(str.lstrip)
    def format_sex(df):
        return abs(df['behavior_type'])
    df['behavior_type'] = df.apply(format_sex, axis=1)
    # 删除行记录重复的数据，我们可以使用df.drop_duplicates方法:


if __name__ == '__main__':
    clean()