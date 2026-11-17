import matplotlib.pyplot as plt

# ÖRNEK VERİ SETİ
# Aşağıdaki veri seti tüm sorular için kullanılacaktır.

aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran"]
satislar = [120, 150, 170, 160, 200, 220]
karlar = [20, 35, 40, 30, 50, 60]
reklam = [5, 8, 10, 7, 12, 15]

# SORU 1
# Aylar ve satışlar verisini kullanarak basit bir çizgi grafiği oluşturun.

plt.plot(aylar,satislar,color ="blue",marker ="o")
plt.title("Aylar ve Satışlar")
plt.xlabel("aylar")
plt.ylabel("satislar")
plt.grid(True)
plt.show()

# SORU 2
# Aylar ve kârlar verisini kullanarak çizgi grafiği oluşturun.
# Çizgi rengi kırmızı olsun.
plt.plot(aylar,karlar,color ="red",marker ="o")
plt.title("Aylar ve Karlar")
plt.xlabel("Aylar")
plt.ylabel("Karlar")
plt.show()


# SORU 3
# Aylar ve satışlar verisini kullanarak marker'lı bir çizgi grafiği oluşturun.
plt.plot(aylar,satislar,marker = "o")
plt.title("Aylar ve Satışlar")
plt.xlabel("Aylar")
plt.ylabel("satışlar")
plt.show()

# SORU 4
# Aylar ve satışlar verisini kullanarak sütun grafiği oluşturun.

plt.bar(aylar,satislar)
plt.title("Aylar ve Satışlar")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")
plt.show()

# SORU 5
# Aylar ve reklam verisini kullanarak yeşil renkli bir sütun grafiği oluşturun.

plt.bar(aylar,reklam,color ="green")
plt.title("Aylar ve Reklam")
plt.xlabel("Aylar")
plt.ylabel("Reklam")
plt.show()

# SORU 6
# Satışlar verisini kullanarak pasta grafiği oluşturun.
# Ay isimlerini etiket olarak gösterin ve yüzdeleri ekrana yazdırın.

etiket = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran"]
plt.pie(satislar,labels=etiket,autopct="%1.1f%%")
plt.title("Aya Göre Satışlar")
plt.show()

plt.scatter(reklam,satislar)
plt.title("Reklam ve Satışlar")
plt.xlabel("Reklam")
plt.ylabel("Satışlar")
plt.show()


# SORU 7
# Reklam ve satışlar verisini kullanarak scatter plot oluşturun.

plt.scatter(reklam, satislar)
plt.title("Reklam ve satışlar")
plt.xlabel("reklam")
plt.ylabel("satışlar")
plt.show()

# SORU 8
# Reklam ve kâr verisini kullanarak kırmızı renkli ve büyük noktalı scatter plot oluşturun.
plt.scatter(reklam,karlar,color ="red",s=100)
plt.title("Reklam ve Karlar")
plt.xlabel("Reklam")
plt.ylabel("karlar")
plt.show()

# SORU 9
# Aynı figür içinde 1 satır 2 sütun olacak şekilde iki grafik oluşturun.
# Solda satışlar için line plot, sağda kârlar için bar chart gösterin.

plt.subplot(1, 2, 1)
plt.plot(aylar,satislar,marker ="o")
plt.title("Satışlar")

plt.subplot(1, 2, 2)
plt.bar(aylar,karlar,color="orange")
plt.title("Karlar")

plt.show()


# SORU 10
# 2 satır 2 sütun olacak şekilde 4 farklı grafik oluşturun.
# 1. grafik: satışlar line plot
# 2. grafik: kârlar bar chart
# 3. grafik: reklam-satış scatter plot
# 4. grafik: satışlar pie chart

plt.subplot(2, 2, 1)
plt.plot(aylar, satislar)
plt.title("Aylar ve Satışlar")

plt.subplot(2, 2, 2)
plt.bar(aylar, karlar)
plt.title("Aylar ve Karlar")

plt.subplot(2, 2, 3)
plt.scatter(reklam, satislar)
plt.title("Reklam ve Satışlar")

plt.subplot(2, 2, 4)
plt.pie(satislar, labels=aylar, autopct="%1.1f%%")
plt.title("Aylar ve Satışlar")

plt.show()