# Animasyon süresini kare sayısı ve FPS değeri üzerinden hesaplamaya çalışır.
dosya_adi = input("Animasyonun dosya adını yazın: ")  # Dosya adını metin olarak kullanıcıdan alır.

kare_sayisi = int(input("Toplam kare sayısını yazın: "))  # Kare sayısını tam sayı olarak kullanıcıdan alır.

fps = float(input("Animasyonun FPS değerini yazın: "))  # FPS değerini ondalıklı sayı olarak kullanıcıdan alır.

fps_gecerli_mi = fps > 0  # FPS değerinin sıfırdan büyük olup olmadığını kontrol eder.

if not fps_gecerli_mi:  # FPS değeri geçerli değilse hata işlemini başlatır.
    print("FPS değeri sıfır veya negatif olamaz.")  # Geçersiz FPS değeri için kullanıcıya bilgi verir.
else:  # FPS değeri geçerliyse süre hesaplamasını başlatır.
    toplam_sure_saniye = (kare_sayisi - 1) / fps  # Kare sayısını FPS değerine bölerek saniye cinsinden süreyi hesaplar.

    toplam_sure_dakika = toplam_sure_saniye / 60  # Saniye cinsinden süreyi dakikaya çevirir.

    print(f"{dosya_adi}: {kare_sayisi} kare / {fps} FPS")  # Animasyon bilgilerini f-string ile ekrana yazdırır.
    print(f"Toplam süre: {toplam_sure_saniye:.2f} saniye")  # Saniye cinsinden toplam süreyi ekrana yazdırır.
    print(f"Toplam süre: {toplam_sure_dakika:.2f} dakika")  # Dakika cinsinden toplam süreyi ekrana yazdırır.
