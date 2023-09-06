print ( "menghitung volume sebuah balok")

panjang = int(input('masukkan panjang balok: '))
lebar = int(input('masukkan lebar balok: '))
tinggi = int(input('masukkan tinggi balok: '))

volume = int(panjang*lebar*tinggi)
print('volume balok adalah: ',volume)

print ("menghitung volume dan luas sebuah tabung")

jari_jari = int(input('masukkan jari_jari         = '))
tinggi = int(input('masukkan tinggi               = '))
luas_alas = int(input('masukkan luas alas         = '))
keliling_alas = int(input('masukkan keliling alas = '))

phi = 22/7

luas = (2*luas_alas)+(keliling_alas*tinggi)
volume = phi*jari_jari*jari_jari*tinggi

print("luas tabung adalah  =", luas )
print("volume tabung adalah  =", volume )
