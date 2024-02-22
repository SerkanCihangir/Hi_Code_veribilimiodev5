liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]
print(liste[3])
print(liste[5])
print(liste[-1])
degerler = liste[2:6]  # 2. indisteki elemandan başlayıp 6. indisteki elemandan önce sonlanır.
print(degerler)  # [9, "3", 8.4, "Hi-Kod"] yazdırır.
degerler = liste[4:]  # 4. indisteki elemandan başlayıp sonuna kadar gider.
print(degerler)  # [8.4, "Hi-Kod", "False", 4.7] yazdırır.
#Verilen listede bulunan string veri tipindeki öğeleri yeni_liste isimli listeye eklenir.

yeni_liste=[]
for i in liste:
   if isinstance(i,str):
        yeni_liste.append(i)

for i in yeni_liste:
    print(i)
#Enumerate methodunu araştırın ve aşağıdaki örneği enumerate methodu ile yapın.
meyveler=['Elma','Armut','Şeftali','Muz','Kiraz']
for indis, eleman in enumerate(meyveler):
      print(f"Indis: {indis}, Eleman: {eleman}")
    