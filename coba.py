def harga_tiket(umur, hari):
  harga_dasar = 100000
  harga_akhir = harga_dasar

  if umur <10 or umur >80:
    harga_akhir *=0.7

  if hari.lower() in ["Jumat,sabtu","minggu"]:
    harga_akhir +=20000

  if 10 <= umur <=80 and hari.lower() in ["senin","selasa","rabu","kamis"]:
    harga_akhir -=6000

  return int (harga_akhir)

umur = int(input("Masukkan Umur :"))
hari = input("Masukkan Hari :")

harga = harga_tiket(umur, hari)
print(f"Harga tiket yang harus dibayar: Rp{harga}")