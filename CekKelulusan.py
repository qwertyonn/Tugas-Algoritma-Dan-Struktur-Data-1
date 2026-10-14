#program cek kelulusan
#I.S.: pengguna memasukkan nama siswa (nama_siswa), nilai Matematika (nilai_mtk), Bahasa Indonesia (nilai_bhs_indo), IPA (nilai_ipa), Bahasa Inggris (nilai_bhs_inggris), dan Standar Kelulusan (standar_kelulusan)
#F.S.: menampilkan status kelulusan siswa
import subprocess
subprocess.run('cls',shell = True)

#badan program
#memasukkan nama siswa (nama_siswa), nilai Matematika (nilai_mtk), Bahasa Indonesia (nilai_bhs_indo), IPA (nilai_ipa), Bahasa Inggris (nilai_bhs_inggris), dan Standar Kelulusan (standar_kelulusan)
nama_siswa        = str(input(  'Masukan Nama siswa          : '))
nilai_mtk         = float(input('Masukan Nilai Matematika    : '))
nilai_bhs_indo    = float(input('Masukan Nilai Bhs Indonesia : '))
nilai_ipa         = float(input('Masukan Nilai IPA           : '))
nilai_bhs_inggris = float(input('Masukan Nilai Bhs Inggris   : '))
standar_kelulusan = int(input(  'Masukan Standar Kelulusan   : '))

#menentukan status kelulusan
if (nilai_mtk >= standar_kelulusan) and (nilai_bhs_indo >= standar_kelulusan) and (nilai_ipa >= standar_kelulusan) and (nilai_bhs_inggris >= standar_kelulusan):
    print(f'Selamat {nama_siswa}, kamu telah lulus semua mata pelajaran')
elif (nilai_mtk < standar_kelulusan) and (nilai_bhs_indo < standar_kelulusan) and (nilai_ipa < standar_kelulusan) and (nilai_bhs_inggris < standar_kelulusan):
    print(f'{nama_siswa} tidak lulus, harus mengikuti remedial semua mata pelajaran')
else:
    print(f'{nama_siswa} tidak lulus, harus mengikuti remedial:')
    if (nilai_mtk < standar_kelulusan):
        print(f'- Matematika')
    if (nilai_bhs_indo < standar_kelulusan):
        print(f'- Bahasa Indonesia')
    if (nilai_ipa < standar_kelulusan):
        print(f'- IPA')
    if (nilai_bhs_inggris < standar_kelulusan):
        print(f'- Bahasa Inggris')
