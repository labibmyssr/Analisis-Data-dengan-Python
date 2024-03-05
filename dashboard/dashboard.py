import pandas as pd
import matplotlib .pyplot as plt
import seaborn as sns
import streamlit as st

def create_stateseller_df(df):
    stateseller_df = df.groupby(by="seller_state").seller_id.nunique().reset_index()
    stateseller_df.rename(columns={
        "seller_id": "seller_count"
    }, inplace=True)
    return stateseller_df

def create_totalstate_df(df):
    totalstate_df = df.groupby(by="seller_state").total_price.sum().reset_index()
    totalstate_df.rename(columns={
        "total_price": "total"
    }, inplace=True)
    return totalstate_df
    

main_df = pd.read_csv("main_data.csv")

stateseller_df = create_stateseller_df(main_df)
totalstate_df = create_totalstate_df(main_df)

st.header('Dashboard Proyek Analisis Data')

tab1, tab2 = st.tabs(["Pertanyaan 1", "Pertanyaan 2"])
with tab1:
    st.subheader("Banyak Negara Bagian dalam Penjual")
    
    fig, ax = plt.subplots(1, 2, figsize=(15, 6))
    colors1 = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(
        y="seller_count",
        x="seller_state",
        data=stateseller_df.sort_values(by="seller_state", ascending=False).head(),
        palette=colors1,
        ax=ax[0]
    )
    ax[0].set_ylabel(None)
    ax[0].set_xlabel(None)
    ax[0].set_title("Tertinggi", loc="center", fontsize=18)
    ax[0].tick_params(axis ='x', labelsize=15)

    sns.barplot(
        y="seller_count",
        x="seller_state",
        data=stateseller_df.sort_values(by="seller_state", ascending=True).head(),
        palette=colors1,
        ax=ax[1]
    )
    ax[1].set_ylabel(None)
    ax[1].set_xlabel(None)
    ax[1].set_title("Terendah", loc="center", fontsize=18)
    ax[1].tick_params(axis='x', labelsize=15)

    plt.suptitle("Banyak Negara Bagian dalam Penjual", fontsize=20)

    st.pyplot(fig)

with tab2:
    st.subheader("Total Harga Item berdasarkan Negara Penjual")

    fig, ax = plt.subplots(1, 2, figsize=(15, 6))
    colors1 = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(
        y="total",
        x="seller_state",
        data=totalstate_df.sort_values(by="seller_state", ascending=False).head(2),
        palette=colors1,
        ax=ax[0]
    )
    ax[0].set_ylabel(None)
    ax[0].set_xlabel(None)
    ax[0].set_title("Tertinggi", loc="center", fontsize=18)
    ax[0].tick_params(axis ='x', labelsize=15)

    sns.barplot(
        y="total",
        x="seller_state",
        data=totalstate_df.sort_values(by="seller_state", ascending=True).head(2),
        palette=colors1,
        ax=ax[1]
    )
    ax[1].set_ylabel(None)
    ax[1].set_xlabel(None)
    ax[1].set_title("Terendah", loc="center", fontsize=18)
    ax[1].tick_params(axis='x', labelsize=15)

    plt.suptitle("Total Harga Item berdasarkan Negara Penjual", fontsize=20)

    st.pyplot(fig)

st.caption('Copyright (c) Dicoding 2023')