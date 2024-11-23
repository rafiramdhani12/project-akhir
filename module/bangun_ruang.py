from module.clear import clear

def kubus():
    
    print("menghitung volume kubus")
    s = int(input("masukan panjang sisi kubus : "))
    V = s**3
    luas_permukaan = 6 * s ** 2
    print(f"diketahui sisi kubus adalah masing-masing {s} dan volume kubus adalah {V} maka luas permukaan kubus adalah {luas_permukaan}")
    
def balok():
       print("menghitung volume dan luas balok")
       
       p= int(input("masukkan panjang balok: "))
       l= int(input("masukkan lebar balok : "))
       t= int(input("masukkan tinggi balok : "))
       V = p * l * t
       luas_permukaan = 2 * (p * l + p * t + l *t)
       
       print(f"diketahui panjang balok adalah {p} dan lebar {l} tinggi balok {t} maka volume balok adalah {V} dan luas permukaanya adalah {luas_permukaan}")

def tabung():
      print("menghitung volume dan luas tabung")
      
      r = float(input("masukkan jari-jari : "))
      t = float(input("masukkan tinggi tabung : "))
      V =3.14 * r ** 2 *t
      luas_permukaan = 2 * 3.14 * r * (r+t)
      
      print(f"diketahui jari jari {r} dan tinggi tabung {t} maka volume tabung adalah {V:.2f} dan luas permukaan adalah {luas_permukaan:.2f}")


def kerucut():
    print("menghitung volume dan luas permukaan kerucut")
    
    r = float(input("jari-jari : "))
    t = float(input("tinggi : "))
    s = float(input("sisi pelukis : "))
    V = (1/3) * 3.14 *r **2 *t
    luas_permukaan = 3.14 * r* (r+s)
    
    print(f"diketahui jari jari {r} dan tinggi {t} dan sisi pelukis  {s} maka volume kerucut adalah {V:.2f} dan luas permukaan adalah {luas_permukaan:.3f}")
    print(f"Volume kerucut : {V:.3f}")
    print(f"luas permukaan : {luas_permukaan:.3f}")

def tampilan():
    print(
    '''
    -----------------------------------------------------------------
    |                         Bangun ruang                          |
    =================================================================
    |   1.Kubus         2.Balok     3.Tabung        4.Kerucut       |
    -----------------------------------------------------------------
    ''')

def bangun_ruang():
    try:
        clear()
        while True:
            
            tampilan()
            
            opsi = int(input("masukan opsi [1]/[2]/[3]/[4] : "))
            
            if opsi == 0:
                print("anda telah keluar dari proggram")
                break
            
            if opsi == 1:
                
                kubus()
                
            elif opsi == 2:
                
             balok()
                
            elif opsi ==3:
                
              tabung()
              
            elif opsi == 4:
                
                kerucut()
                
            else:
                print("opsi tidak valid silahkan masukan opsi yg lain")
    except KeyboardInterrupt:
        print("anda telah keluar paksa dari proggram")
