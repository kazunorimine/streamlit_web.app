# データ分析関連

import streamlit as st
import pandas as pd

df = pd.read_csv('./data/data.csv',encoding="shift-jis")
st.dataframe(df)
st.table(df)

    # 折れ線グラフ
st.line_chart(df,x='年月日',y='平均気温(℃)')

    # 棒グラフ
st.bar_chart(df['平均気温(℃)'])