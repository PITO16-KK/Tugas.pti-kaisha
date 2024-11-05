# Daftar mata kuliah untuk semester 1
mata_kuliah = [
    "Kalkulus",
    "Statistik",
    "Algoritma",
    "PTI",
    "Bahasa Inggris"
]

# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(tugas, uts, uas):
    return (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)

# Fungsi untuk menentukan huruf nilai
def tentukan_huruf_nilai(nilai_akhir):
    if nilai_akhir >= 85:
        return 'A'
    elif nilai_akhir >= 70:
        return 'B'
    elif nilai_akhir >= 60:
        return 'C'
    elif nilai_akhir >= 50:
        return 'D'
    else:
        return 'E'

# Array untuk menyimpan data mahasiswa
data_mahasiswa = []

# Input data mahasiswa
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
for i in range(jumlah_mahasiswa):
    nama = input(f"\nMasukkan nama mahasiswa ke-{i + 1}: ")
    nilai_mahasiswa = []
    for mata_kuliah_item in mata_kuliah:
        print(f"\nMasukkan nilai untuk {mata_kuliah_item}:")
        tugas = float(input("Nilai Tugas: "))
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        
        # Hitung nilai akhir
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
        huruf_nilai = tentukan_huruf_nilai(nilai_akhir)
        
        # Simpan nilai akhir dan huruf nilai
        nilai_mahasiswa.append({
            "mata_kuliah": mata_kuliah_item,
            "nilai_akhir": nilai_akhir,
            "huruf_nilai": huruf_nilai
        })
    
    # Simpan data mahasiswa
    data_mahasiswa.append({
        "nama": nama,
        "nilai": nilai_mahasiswa
    })

# Menampilkan hasil
print("\n----- Hasil Nilai Mahasiswa -----")
for mahasiswa in data_mahasiswa:
    nama = mahasiswa["nama"]
    print(f"\nNama Mahasiswa: {nama}")
    for nilai_item in mahasiswa["nilai"]:
        mata_kuliah_item = nilai_item["mata_kuliah"]
        nilai_akhir = nilai_item["nilai_akhir"]
        huruf_nilai = nilai_item["huruf_nilai"]
        print(f"{mata_kuliah_item}: Nilai Akhir = {nilai_akhir:.2f}, Huruf Nilai = {huruf_nilai}")
