import math
from cmath import cos,sin

x = math.pi / 5                 # pi/5'in değeri

tek_terimli = 1 - sin(0) * x        # cos(x)'in türevi = -sin(x)'tir
iki_terimli = 1 - pow(x,2) / math.factorial(2)   #cos(x)'in ikinci türevi - cos(x)
gercek = math.cos(x)                      #gerçek değerimizi "gercek" adlı değişkene atıyoruz
birinci_kesme_h = gercek - tek_terimli
ikinci_kesme_h = gercek - iki_terimli

print("***************************************************")
print("TEK TERİMLİ TAYLOR SERİSİ: ",tek_terimli)
print("İKİ TERİMLİ TAYLOR SERİSİ = " ,iki_terimli)
print("COS(pi/5)'in DEĞERİ: ",gercek)
print("BİRİNCİ KESME HATASI: ",birinci_kesme_h)
print("İKİNCİ KESME HATASI: ",ikinci_kesme_h)
print("***************************************************")