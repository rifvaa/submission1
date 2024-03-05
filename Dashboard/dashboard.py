from st_on_hover_tabs import on_hover_tabs
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from babel.numbers import format_currency



st.set_page_config(layout="wide")

st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)


with st.sidebar:
    tabs = on_hover_tabs(tabName=['Profile', 'Projects', 'Other'], 
                         iconName=['📃', '💻', '❕'], default_choice=0)

if tabs =='Profile':
    st.subheader("Name : Muhammad Rifva Maulana \n\n ✉\t gmail : maulanarifva@gmailcom\n\n")
    
elif tabs == 'Projects':
    st.header("Proyek Analisis Data: Bike-sharing-dataset")
    st.subheader("\n\nVisualization & Explanatory Analysis")
    st.write("Pertanyaan 1: Bagaimana perkembangan penyewaan sepeda selama 1 tahun ?\n\n Pertanyaan 2: Apa penyebab minat penyewa sepeda naik & turun ?")
    
    def main():
        st.title('Perkembangan Penyewaan Sepeda Selama 1 Tahun')

        # Membaca data dari file CSV
        day_df = pd.read_csv("day_all.csv")

        # Mengambil kolom bulan dan jumlah penyewaan
        bulan = day_df['Bulan']
        jumlah_penyewaan = day_df['Ttl_Penyewa']

        # Membuat plot histogram
        fig, ax = plt.subplots()
        ax.bar(bulan, jumlah_penyewaan, color='skyblue')

        # Menambahkan judul dan label sumbu
        ax.set_title('Perkembangan Penyewaan Sepeda Selama 1 Tahun')
        ax.set_xlabel('1 Tahun')
        ax.set_ylabel('Jumlah Penyewaan')

        # Agar label bulan tidak bertumpuk
        plt.xticks(rotation=45)

        # Menampilkan plot histogram di Streamlit
        st.pyplot(fig)

    if __name__ == "__main__":
        main()

    def load_data():
        day_df = pd.read_csv("day_all.csv")
        return day_df
    def plot_bike_usage_by_factors(day_df):
        plt.figure(figsize=(12, 8))

    # Plotting
        categorical_vars = ['Musim', 'Cuaca', 'workingday', 'weekday']
        colors = ['blue', 'red', 'green', 'purple']

        for i, var in enumerate(categorical_vars):
            mean_ttl_penyewa = day_df.groupby(var)['Ttl_Penyewa'].mean()
            plt.bar([x + 0.2*i for x in range(len(mean_ttl_penyewa))], mean_ttl_penyewa, width=0.2, color=colors[i], label=var)

        plt.xlabel('Variabel Kategorikal')
        plt.ylabel('Jumlah Penggunaan Sepeda')
        plt.title('Penggunaan Sepeda Berdasarkan Faktor-faktor')
        plt.xticks(range(len(mean_ttl_penyewa)), mean_ttl_penyewa.index, rotation=45, ha='right')

        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        # Menampilkan plot menggunakan Streamlit
        st.pyplot()

    def main():
        st.title('Penggunaan Sepeda Berdasarkan Faktor-faktor')

        # Load data
        day_df = load_data()
        
        # Plot bike usage by factors
        plot_bike_usage_by_factors(day_df)

    if __name__ == "__main__":
        main()
        
elif tabs == 'Other':
    st.title("NOTHING")
    st.write("HEHE...")
    
