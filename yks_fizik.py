"""
Created on Wed Aug  1 13:43:04 2018

@author: MArabul, Copyleft
"""

# YKS Kafadan Sallama Testi

import numpy as np

# Fizik Soruları Sayısı
n_fizik = 14
# 1 den 5 e kadar rakamlar A B C D E şıklarını temsil ediyor.
# Cevap anahtarı için rastgele bir sıralama oluşturuyoruz önce
dogru_cevaplar = np.random.randint(low=1, high=5, size=n_fizik)
# Toplam öğrenci sayısı 
toplam_test = 1000000
# Başlangıçtaki toplam net sayısı 0
toplam_net = 0

"""
Net hesaplama fonksiyonu
"""
def net_hesapla(deneme_cevaplar, dogru_cevaplar):
    sonuclar = (deneme_cevaplar == dogru_cevaplar)
    n_dogru = np.sum(sonuclar)
    n_yanlis = np.sum(~sonuclar)
    n_net = n_dogru - 0.25 * n_yanlis # 4 yanlış 1 doğru götürüyor
    return n_net

for n_deneme in range(toplam_test):
    # Deneme için rastgele bir sıralama oluşturuyoruz
    deneme_cevaplar = np.random.randint(low=1, high=5, size=n_fizik)
    n_net = net_hesapla(deneme_cevaplar,dogru_cevaplar)
    toplam_net = toplam_net + n_net
    
ortalama = (toplam_net/toplam_test)
print(ortalama)



