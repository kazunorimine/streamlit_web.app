import streamlit as st


with st.form(key='prfile_form') :
    # テキストボックス
        name = st.text_input('名前')
        address = st.text_input('住所')

    # ラジオボックス
        age_category = st.radio(
            '年齢層',
            ('子供(18未満)','大人(18才以上)')
        )
    
    # ボタン
        submit_btn = st.form_submit_button('送信')
        cancel_btn = st.form_submit_button('キャンセル')
        if submit_btn:
            st.text(f'ようこそ、{name}さん！{address}に書類を送りました！')
            st.text(f'年齢層: {age_category}')