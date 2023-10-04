import numpy as np
import pandas as pd 

sozluk = {"Kategori": ["Giyim","Giyim", "Ayakkabı","Aksesuar","Ayakkabı","Giyim","Aksesuar","Aksesuar","Ayakkabı","Giyim"],
          "Ürün" : ["Kazak","T-shirt","Sandalet","Küpe","Spor Ayakkabı","Pantolon","Kolye","Yüzük","Çizme","Ceket"],
          "Fiyat" : [300,180,450,50,700,400,150,80,850,900]}

# Yukarıdaki sözlük DataFrame’e dönüştürülür.
df = pd.DataFrame(sozluk)
# print(df)

# Yukarıdaki DataFrame için 2.indexte bulunan kategori bulunur. (Sadece kategori bilgisi)
kategori_df = df["Kategori"][2]
# print(kategori_df)

# 2. indexte bulunan ürün bulunur. (Sadece ürün bilgisi)
urun_df = df["Ürün"][2]
# print(urun_df)

# 4.indexten 9.indexe kadar olan veriler bulunur. (Kategori,ürün,fiyat bilgisi beraber)
veri_bulma_df = df[4:9]
# print(veri_bulma_df)

# 1.indexten 6.indexe kadar olan ürünler bulunur. (Sadece ürün bilgisi)
index_urun = df.loc[1:6, "Ürün"]
# print(index_urun)

# Yukarıdaki DataFrame için Giyim kategorisinde bulunan ürünler gösterilir.
giyim_kategori = df[(df['Kategori'] == 'Giyim') & (df['Ürün'])]
# print(giyim_kategori)

# Ayakkabı kategorisinde bulunan ürünler gösterilir.
ayakkabi_kategori = df[(df['Kategori'] == 'Ayakkabı') & (df['Ürün'])]
# print(ayakkabi_kategori)

# Aksesuar kategorisinde bulunan ürünler gösterilir.
aksesuar_kategori = df[(df['Kategori'] == 'Aksesuar') & (df["Ürün"])]
# print(aksesuar_kategori)

# Yukarıdaki DataFrame için Giyim kategorisinde fiyatı 300'den fazla olan ürünler gösterilir.
giyim_fiyat = giyim_kategori[df["Fiyat"] > 300]
# print(giyim_fiyat)

# Ayakkabı kategorisinde fiyatı 600'den az olan ürünler gösterilir.
ayakkabi_fiyat = ayakkabi_kategori[df["Fiyat"] < 600]
# print(ayakkabi_fiyat)

# Aksesuar kategorisinde fiyatı 100'den fazla olan aksesuar gösterilir.
aksesuar_fiyat = aksesuar_kategori[df["Fiyat"] > 100]
# print(aksesuar_fiyat)