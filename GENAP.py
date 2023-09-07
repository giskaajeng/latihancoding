nama_saya = "Giska Ajeng Savitri"
nim = "230441100176"
asal = "bangkalan"
ploting = "A"
print(f"NAMA : {nama_saya}")
print(f"NIM  : {nim}")
print(f"ASAL :{asal}")
print(f"PLOTING: {ploting}")

#input panjang, lebar, tinggi
panjang_balok = int(input(f"masukkan panjang balok ="))
lebar_balok = int(input(f"masukkan lebar balok ="))
tinggi_balok = int(input(f"masukkan tinggi balok ="))
#hitung volome balok
volumebalok = panjang_balok * lebar_balok * tinggi_balok
#tampilkan volume balok
print(f"volume balok adalah: {volumebalok} satuan kubik")

#input jari-jari dan tinggi dari pengguna
jari_jari_tabung = float(input("masukkan jari_jari tabung: "))
tinggitabung = float(input("masukkan tinggi tabung: "))
#hitung volume tabung
volumetabung = 22/7 * jari_jari_tabung*jari_jari_tabung * tinggitabung
#tampilkan hasil volume 
print(f"volume tabung adalah: {volumetabung:.2f}")

#input jari_jari dari pengguna
jari_jaribola = float(input("masukkan jari_jaribola: "))
#hitung volume bola
volumebola = 4/3 * 22/7 * jari_jaribola * jari_jaribola * jari_jaribola
#tampilkan hasil volume bola
print(f"volum bola adalah: {volumebola:.2f}")




