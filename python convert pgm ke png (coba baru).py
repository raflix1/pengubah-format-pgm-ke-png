import cv2
import os

# Folder dengan file PGM
folder_input = 'D:\Skripsi Rafli\Dataset\Abnormal'  # Ganti dengan direktori yang sesuai
folder_output = 'D:\Skripsi Rafli\Dataset\Abnormal PNG (coba baru)'  # Ganti dengan direktori tujuan

# Daftar semua file dalam folder input
daftar_file = os.listdir(folder_input)

# Loop melalui setiap file dalam folder
for nama_file in daftar_file:
    if nama_file.endswith('.pgm'):  # Pastikan hanya mengolah file PGM
        # Baca gambar PGM
        path_input = os.path.join(folder_input, nama_file)
        gambar_pgm = cv2.imread(path_input, cv2.IMREAD_GRAYSCALE)
        
        # Simpan gambar dalam format PNG
        nama_file_tanpa_ext = os.path.splitext(nama_file)[0]
        path_output = os.path.join(folder_output, f'{nama_file_tanpa_ext}.png')
        cv2.imwrite(path_output, gambar_pgm)

print('Konversi selesai.')