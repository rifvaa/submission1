import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from babel.numbers import format_currency




st.set_page_config(layout="wide")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)
st.set_option('deprecation.showPyplotGlobalUse', False)


with st.sidebar:
    tabs = on_hover_tabs(tabName=['Profile', 'Projects', 'Other'], 
                         iconName=['📃', '💻', '❕'], default_choice=0)

if tabs =='Profile':
    st.subheader("Name : Muhammad Rifva Maulana \n\n ✉\t gmail : maulanarifva@gmailcom\n\n ID Dicoding : muhammad_rifva")
   
    
elif tabs == 'Projects':
    st.header("Proyek Analisis Data: Bike-sharing-dataset")
    st.subheader("\n\nVisualization & Explanatory Analysis")
    st.write("Pertanyaan 1: Bagaimana perkembangan penyewaan sepeda selama 1 tahun ?\n\n Pertanyaan 2: Apa penyebab minat penyewa sepeda naik & turun ?")
    
    def plot_bike_rental_by_month(day_df):
        plt.figure(figsize=(8, 4))  
        plt.bar(day_df['Bulan'], day_df['Ttl_Penyewa'], color='skyblue')
        plt.title('Perbandingan Jumlah Penyewaan Sepeda berdasarkan Bulan')
        plt.xlabel('Bulan')
        plt.ylabel('Jumlah Penyewaan')
        plt.xticks(rotation=45)
        st.pyplot()
        
        expander = st.expander("Kesimpulan")
        expander.write("Kenaikan: Dari histogram, terlihat bahwa jumlah penyewa cenderung meningkat dari bulan Januari hingga Mei, mencapai puncaknya pada bulan Mei, dan kemudian menurun secara bertahap hingga Desember. Ini bisa mengindikasikan tren musiman di mana permintaan penyewaan meningkat pada musim semi dan kemudian menurun menjelang akhir tahun.")
        expander.write("Bulanan: Beberapa bulan memiliki lonjakan tajam dalam jumlah penyewa, sementara yang lain mungkin memiliki fluktuasi yang lebih stabil.")
        expander.write("Prediksi & Ramalan: Histogram ini memberikan gambaran umum tentang pola perilaku penyewa sepanjang tahun. Informasi ini dapat digunakan untuk merencanakan strategi bisnis seperti penentuan harga, promosi, dan manajemen persediaan untuk mengakomodasi fluktuasi permintaan.")
        
    def plot_bike_usage_by_factors(day_df):
        plt.figure(figsize=(8, 4))

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
        
        st.pyplot()
        
        expander = st.expander("Kesimpulan")
        expander.write("Musim: Penggunaan sepeda cenderung lebih tinggi pada musim Fall dan musim dingin Winter, mungkin karena kondisi cuaca yang lebih nyaman dan menjadi bersemangat melakukan aktivitas.")
        expander.write("Cuaca: Cuaca cerah atau sebagian berawan terkait dengan penggunaan sepeda yang lebih tinggi dibandingkan dengan cuaca berkabut atau berawan dan cuaca salju ringan atau hujan, yang mungkin memengaruhi kenyamanan dan keamanan bersepeda.")
        expander.write("Hari Kerja: Meskipun penggunaan sepeda pada hari libur sedikit lebih tinggi, tidak ada perbedaan yang signifikan antara penggunaan sepeda pada hari kerja dan hari libur.")
        expander.write("Hari dalam Seminggu/weekday: Penggunaan sepeda cenderung lebih tinggi pada akhir pekan dibandingkan dengan hari-hari kerja lainnya, yang mungkin karena orang memiliki lebih banyak waktu luang pada akhir pekan untuk bersepeda.")

    def load_data():
        day_df = pd.read_csv("day_all.csv")
        return day_df

    def main():

        st.header('Analisis Penyewaan Sepeda')
        option = st.selectbox('Pilih Analisis:', ('Perbandingan Penyewaan Sepeda per Bulan', 'Penggunaan Sepeda Berdasarkan Faktor-faktor'))

        if option == 'Perbandingan Penyewaan Sepeda per Bulan':
            st.subheader('Perbandingan Jumlah Penyewaan Sepeda per Bulan')
            day_df = load_data()
            plot_bike_rental_by_month(day_df)
        elif option == 'Penggunaan Sepeda Berdasarkan Faktor-faktor':
            st.subheader('Penggunaan Sepeda Berdasarkan Faktor-faktor')
            day_df = load_data()
            plot_bike_usage_by_factors(day_df)

    if __name__ == "__main__":
        main()
        
elif tabs == 'Other':
    st.title("NOTHING")
    st.write("HEHE...")
    
