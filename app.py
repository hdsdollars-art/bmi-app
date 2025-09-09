import streamlit as st

st.title("💪 Kalkulator BMI dengan Kamera")

nama = st.text_input("Masukkan nama kamu:")
tinggi = st.number_input("Tinggi badan (cm):", min_value=50, max_value=250)
berat = st.number_input("Berat badan (kg):", min_value=10, max_value=300)

if st.button("Hitung BMI"):
    if tinggi > 0 and berat > 0:
        tinggi_meter = tinggi / 100
        bmi = berat / (tinggi_meter ** 2)

        st.success(f"Halo {nama}, BMI kamu adalah **{bmi:.2f}**")

        if bmi < 18.5:
            st.error("Kategori: Kurus ❌")
        elif 18.5 <= bmi < 25:
            st.success("Kategori: Normal ✅")
        elif 25 <= bmi < 30:
            st.warning("Kategori: Gemuk ⚠️")
        else:
            st.error("Kategori: Obesitas ❌")
    else:
        st.error("Isi data tinggi dan berat dengan benar.")

st.subheader("📸 Ambil Foto dengan Kamera")
img = st.camera_input("Klik tombol untuk mengambil foto")
if img:
    st.image(img)
