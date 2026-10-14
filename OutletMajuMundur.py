#program outlet maju mundur
#I.S.: pengguna memasukkan kode produk, jumlah beli, dan harga satuan
#F.S.: menampilkan total harga, diskon, total bayar, dan uang kembalian
import subprocess
subprocess.run('cls',shell = True)

#badan program
#memasukkan kode produk, jumlah beli, dan harga satuan
kode_produk = str(input('Masukan kode produk  : '))
jumlah_beli = int(input('Masukan jumlah beli  : '))
harga_satuan = int(input('Masukan harga satuan : '))

total_harga = jumlah_beli * harga_satuan

#menentukan diskon
if (total_harga > 500000):
    diskon = total_harga * 0.125
else:
    diskon = 0

#menghitung pembayaran
total_bayar = total_harga - diskon
print(f'Total harga          : Rp. {total_harga:,.0f}')
print(f'Diskon               : Rp. {diskon:,.0f}')
print(f'Total bayar          : Rp. {total_bayar:,.0f}')

#menghitung kembalian
uang_bayar = int(input('Masukan uang bayar   : '))
uang_kembalian = uang_bayar - total_bayar
print(f'Uang kembalian       : Rp. {uang_kembalian:,.0f}')
