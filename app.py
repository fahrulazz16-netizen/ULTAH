import os
import random
import time
import streamlit as st

# 1. Konfigurasi Halaman Web
st.set_page_config(
    page_title="Selamat Ulang Tahun, Semestaku ❤️",
    page_icon="🌹",
    layout="centered",
)

# 2. Inisialisasi State Hitungan Klik (Session State)
if "click_count" not in st.session_state:
    st.session_state.click_count = 0

# 3. Styling Kustom (CSS Warm Romantic Theme)
st.markdown(
    """
    <style>
    /* Latar belakang hangat bertema Rose Gold Soft */
    .stApp {
        background-color: #fce4ec;
    }
    
    /* Warna semua teks bawaan Streamlit agar terasa kontras dan lembut */
    .stApp p, .stApp span, .stApp label, .stApp h1, .stApp h2, .stApp h3, .stApp caption {
        color: #3e2723 !important;
    }
    
    /* Judul Utama */
    .title-text {
        color: #880e4f !important;
        text-align: center;
        font-family: 'Georgia', serif;
        font-weight: bold;
        padding-top: 10px;
    }
    
    /* Styling Subheader */
    .sub-text {
        color: #5d4037 !important;
        text-align: center;
        font-style: italic;
        margin-bottom: 25px;
        font-size: 18px;
    }
    
    /* Card / Kontainer Pesan */
    .quote-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #c2185b;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }

    .sweet-card {
        background-color: #fff0f3;
        padding: 20px;
        border-radius: 15px;
        border: 2px dashed #ff4d6d;
        text-align: center;
        margin-top: 15px;
    }
    
    /* Tombol Kustom */
    .stButton>button {
        width: 100%;
        background-color: #c2185b;
        color: white !important;
        border-radius: 12px;
        border: none;
        height: 52px;
        font-size: 18px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #880e4f;
        color: white !important;
        transform: scale(1.01);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Efek Balon saat pertama kali halaman terbuka
st.balloons()

# 4. Header Utama
st.markdown(
    "<h1 class='title-text'>🌹 Selamat Ulang Tahun, Rumahku & Semestaku ❤️</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p class='sub-text'>'Di antara jutaan orang di dunia, aku paling bersyukur karena takdir mempertemukanku denganmu.'</p>",
    unsafe_allow_html=True,
)
st.write("---")

# 5. Pemutar Lagu Pengiring
st.subheader("🎵 Putar Lagu Ini Dulu Ya...")
st.caption("Biarkan musik ini menemani setiap detik saat kamu membaca halaman ini:")
st.video("https://www.youtube.com/watch?v=mAJa4SF_VVI")

st.write("---")

# 6. Surat Cinta Hangat & Panjang
st.subheader("💌 Surat Kecil Dari Lubuk Hati")

st.markdown(
    """
<div class="quote-card">
    <p><b>Untukmu yang paling tersayang,</b></p>
    <p>Selamat ulang tahun ya... Bertambah satu tahun usiamu hari ini, dan aku merasa jadi orang yang sangat beruntung karena masih bisa ada di sisimu untuk merayakannya.</p>
    <p>Terima kasih sudah tumbuh menjadi sosok yang begitu luar biasa. Terima kasih atas setiap senyuman manis yang selalu berhasil menenangkan hariku yang berisik, atas kesabaranmu yang tak pernah habis, dan atas setiap peluk hangat yang selalu membuatku merasa pulang.</p>
    <p>Dunia mungkin sering kali ramai dan melelahkan, tapi bagiku, bersamamu segalanya terasa cukup dan menyenangkan. Jangan pernah ragu pada dirimu sendiri ya, karena di mataku, kamu selalu luar biasa.</p>
</div>
""",
    unsafe_allow_html=True,
)

st.write("---")

# 7. Level Rasa Sayang (15 Klik Bertahap)
st.subheader("💖 Level Rasa Sayang (Tekan Tombol Ini Berulang Kali!)")
st.caption("Setiap klik membuka ungkapan manis yang makin mendalam sampai puncaknya:")

if st.button("Tekan Untuk Buka Kejutan Bertahap ✨"):
    st.session_state.click_count += 1

pesan_level = {
    1: "❤️ **Klik 1:** Kamu tahu tidak? Kehadiranmu itu hal terbaik yang pernah terjadi di hidupku.",
    2: "💕 **Klik 2:** Makasih ya sudah mau bertahan dan berjuang sampai sejauh ini. Aku bangga banget sama kamu!",
    3: "🌹 **Klik 3:** Kalau dunia lagi terasa berat, ingat ya... kamu selalu punya aku sebagai tempat pulang.",
    4: "🥰 **Klik 4:** Aku suka banget cara kamu tersenum, rasanya semua beban langsung hilang gitu aja.",
    5: "✨ **Klik 5:** Aku berdoa semoga kita bisa terus merayakan puluhan ulang tahun berikutnya bersama-sama.",
    6: "💌 **Klik 6:** Kamu itu bukan cuma pasangan, tapi sahabat, penyemangat, dan separuh jiwaku.",
    7: "🎂 **Klik 7:** Di usia yang baru ini, semoga kamu makin bahagia, makin bersinar, dan selalu dilindungi.",
    8: "🫂 **Klik 8:** Peluk erat buat kamu yang hari ini ulang tahun! Jangan pernah merasa sendiri ya.",
    9: "👑 **Klik 9:** Bagi dunia kamu mungkin cuma satu orang, tapi bagiku kamu adalah seluruh duniaku.",
    10: "💎 **Klik 10:** Setiap momen sama kamu selalu jadi kenangan manis yang nggak akan pernah aku lupain.",
    11: "🌸 **Klik 11:** Makasih sudah mengajarkanku arti mencintai dengan tulus dan apa adanya.",
    12: "💫 **Klik 12:** Semoga semua rasa lelahmu dibayar tuntas dengan kebahagiaan melimpah tahun ini.",
    13: "🍓 **Klik 13:** Tetap jadi dirimu yang hangat dan penyayang ya, karena itu yang bikin aku selalu jatuh cinta.",
    14: "🏆 **Klik 14:** Kamu adalah pemenang di hatiku, hari ini, besok, dan selamanya!",
    15: "🔥 **Klik 15 (LEVEL PUNCAK):** Aku sayang banget sama kamu, melebihi kata-kata yang bisa dituliskan di web ini! I love you so much forever! ❤️✨",
}

count = st.session_state.click_count

if count > 0:
    st.balloons()
    current_msg = pesan_level.get(count, pesan_level[15])

    st.markdown(
        f"""
    <div class="sweet-card">
        <h3>Level Kejutan Ke-{count} 💌</h3>
        <p style="font-size: 20px; font-weight: bold; color: #c2185b;">{current_msg}</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

st.write("---")

# 8. Tombol Kotak Kejutan Acak & Pertanyaan Kenangan Interaktif
st.subheader("🎁 Kotak Kejutan Spesial (Pilih Salah Satu!)")
st.caption("Klik tombol di bawah untuk mengambil hadiah virtual & kenanganmu hari ini:")

col_k1, col_k2 = st.columns(2)
col_k3, col_k4 = st.columns(2)

with col_k1:
    if st.button("🤗 Pelukan"):
        st.toast("Virtual Hug Sent! 🫂", icon="🤗")
        st.success("Peluk erat 10 detik dikirim khusus buat kamu hari ini!")

with col_k2:
    if st.button("💋 Cium Pipi"):
        st.toast("Virtual Kiss Sent! 💋", icon="🥰")
        st.success("Kecupan hangat di pipi buat yang lagi ulang tahun!")

with col_k3:
    if st.button("🔮 Ramalan"):
        ramalan = random.choice([
            "Tahun ini kamu akan kejatuhan banyak rezeki dan kebahagiaan!",
            "Semua impian terbesarmu bakal tercapai satu per satu di tahun ini!",
            "Kamu akan makin disayang sama semua orang di sekitarmu!",
            "Hari-harimu bakal penuh tawa dan kehangatan!"
        ])
        st.info(f"**Ramalan Hari Ini:** {ramalan}")

with col_k4:
    if st.button("🤔 Btw ke apart sama ke jogja tuh kapan ya"):
        st.toast("Momen Kangen! 💭", icon="🤔")
        st.warning("Btw... kita ke apartemen sama jalan-jalan ke Jogja tuh kapan ya? 🤔💭❤️")

st.write("---")

# 9. Timeline Perjalanan & Momen Spesial
st.subheader("📖 Jejak Langkah & Kenangan Indah")
st.write("Beberapa babak kecil yang membuatku makin yakin padamu:")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🌿 **Awal Mula**")
    st.write(
        "Saat pertama kali mengenalmu, aku tak pernah menyangka bahwa kamu akan menjadi sosok yang paling berarti di hidupku hari ini."
    )

    st.markdown("### ☕ **Hari-Hari Biasa**")
    st.write(
        "Cerita-cerita acak kita di malam hari, tawa kecil atas hal tidak penting, dan obrolan hangat yang selalu kubawa sampai tidur."
    )

with col2:
    st.markdown("### 🌧️ **Melewati Badai**")
    st.write(
        "Saat hari-hari tidak berjalan mudah, terima kasih sudah saling menggenggam erat dan tidak pernah memilih untuk menyerah."
    )

    st.markdown("### 🌅 **Masa Depan**")
    st.write(
        "Aku ingin terus ada di setiap ulang tahunmu berikutnya. Melihatmu tumbuh, mencapai impianmu, dan bahagia."
    )

st.write("---")

# 10. Amplop Harapan & Doa
st.subheader("🕊️ Harapan & Doa Tulus Untukmu")

with st.expander("✨ Doa Untuk Kesehatan & Kebahagiaanmu"):
    st.write(
        "Semoga langkahmu selalu dilindungi, tubuhmu selalu sehat, dan hatimu selalu dipenuhi ketenangan. Semoga lelahmu selalu berbuah manis."
    )

with st.expander("🌸 Doa Untuk Impian & Cita-Citamu"):
    st.write(
        "Semoga setiap rencana dan impian yang sedang kamu perjuangkan satu per satu menemukan jalan terbukanya. Aku percaya kamu pasti bisa mencapainya!"
    )

with st.expander("🔒 Janjiku Untukmu"):
    st.write(
        "Aku berjanji akan terus ada. Menjadi pendengar pertamamu saat kamu ingin cerita, menjadi pendukung terdepanmu, dan menjadi tempatmu bersandar saat kamu merasa lelah."
    )

st.write("---")

# 11. Wishboard Interaktif
st.subheader("📝 Kotak Harapan Usia Baru")
st.caption("Tuliskan satu impian atau keinginanmu di usia yang baru ini:")
harapan_user = st.text_input("", placeholder="Ketik harapanmu di sini...")

if harapan_user:
    st.balloons()
    st.info(
        f"Aamiin ya Allah... Semoga harapanmu ini: **'{harapan_user}'** segera dikabulkan dan diwujudkan secepatnya! ✨❤️"
    )

st.write("---")

# 12. Hadiah & Kejutan Penutup (Memanggil foto.jpeg)
st.subheader("🎁 Kejutan Spesial Penutup")
st.write("Tekan tombol di bawah untuk membuka ucapan terakhir dariku:")

if st.button("Buka Kejutan Penutup 🎉"):
    st.snow()
    st.balloons()
    st.success("🎂 SELAMAT ULANG TAHUN SAYANG! I LOVE YOU SO MUCH! ❤️✨")

    # Membaca direktori file app.py secara langsung
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    # Daftar prioritas pencarian nama file foto
    kemungkinan_foto = [
        "foto.jpeg",
        "foto.jpg",
        "foto.png",
        "WhatsApp Image 2026-09-04 at 20.51.43.jpeg",
        "WhatsApp Image 2026-09-04 at 20.51.43.jpg",
    ]
    
    foto_ditemukan = None
    for nama_file in kemungkinan_foto:
        path_cek = os.path.join(BASE_DIR, nama_file)
        if os.path.exists(path_cek):
            foto_ditemukan = path_cek
            break

    if foto_ditemukan:
        st.image(
            foto_ditemukan,
            caption="Momen Spesial Bersamamu ❤️",
            use_container_width=True,
        )
    else:
        st.warning(
            f"File foto belum ditemukan di folder: {BASE_DIR}. Pastikan file 'foto.jpeg' berada di dalam folder yang sama dengan app.py."
        )