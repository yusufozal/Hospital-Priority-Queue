# Hastane Acil Servisi Hasta Sıralama ve Yönetim Sistemi

Bu proje, bir hastane acil servisinin hastaları tedavi önceliklerine göre sıralayarak etkili bir şekilde yönetmesini sağlamak amacıyla geliştirilmiştir. Aşağıdaki unsurlar projede ele alınmıştır:

## Kullanılan Teknolojiler
- **Programlama Dili:** Python
- **Veri Yapıları:** Min-Heap, Kuyruk (Queue)
- **Kütüphaneler:** Flask

> [!IMPORTANT]
> Flask kütüphanesini eklemeyi unutmayın.


## Kurulum ve Çalıştırma
1. Proje dosyalarını klonlayın:
   ```bash
   git clone <proje-repo-linki>
   ```
2. Proje dizinine gidin:
   ```bash
   cd <proje-dizini>
   ```
3. Gerekli kütüphaneyei indirin:
   ```bash
   pip install Flask
   ```
4. Python betiğini çalıştırın:
   ```bash
   python main.py
   ```


## Senaryo
Hastane acil servisi, gelen hastaları tedavi önceliğine göre sıralamak istemektedir. Her hasta için şu bilgiler mevcuttur:
- **Hasta ID**: Hastaya özel bir kimlik numarası.
- **Öncelik Seviyesi**: Hastanın durumunun aciliyetini temsil eder (1: en acil, 10: düşük öncelik).
- **Tedavi Süresi**: Hastanın tedavi süresi (dakika cinsinden).

Hastane aşağıdaki işlemleri yapmak istemektedir:
1. **Hastaların Öncelik Seviyesine Göre Sıralanması**: Daha düşük öncelik seviyesine sahip hastalar daha önce tedavi edilir.
2. **Tedavi Sürelerine Göre Zaman Yönetimi**: Her hasta tedavi edilirken, toplam tedavi sürelerinin gün sonunda 420 dakikayı (7 saat) aşmaması sağlanır.
3. **Dinamik Ekleme ve Silme İşlemleri**: Gün içinde gelen yeni hastalar kuyruğa eklenir. Tedavi edilen hastalar ise kuyruğtan çıkarılır.

## Hasta Listesi
Başlangıç için bir hasta listesi verilmiştir:

| HastaID | Öncelik Seviyesi | Tedavi Süresi (dk) |
|---------|--------------------|---------------------|
| 101     | 5                  | 30                  |
| 102     | 3                  | 40                  |
| 103     | 8                  | 20                  |
| 104     | 1                  | 60                  |
| 105     | 7                  | 15                  |
| 106     | 2                  | 45                  |
| 107     | 4                  | 25                  |
| 108     | 6                  | 35                  |
| 109     | 3                  | 30                  |
| 111     | 8                  | 10                  |


## Görevler
1. **Min-Heap Oluşturma**: Başlangıç hasta listesinden bir Min-Heap yapısı oluşturun. Öncelik seviyesi sıralama kriteri olarak kullanılacaktır.
2. **Dinamik Hasta Ekleme**: Gün içinde gelen yeni hastalar heap'e ekleyin ve heap'i düzeltin.
3. **Tedavi Simülasyonu**: Gün sonunda 7 saatlik toplam tedavi süresi aşılmadan, hastalar sırasıyla tedavi edin ve hangi hastaların tedavi edilebildiğini listeleyin.
4. **Tedavi Edilemeyen Hastalar**: Gün sonunda tedavi edilemeyen hastaları ayrı bir liste olarak yazdırın.
5. **Kod Yapısı**: Kodunuzun temiz, okunabilir ve açıklama satırlarıyla desteklenmiş olması gerekmektedir.

## Proje Yapısı
Bu projede aşağıdaki adımlar izlenerek bir kod yapısı geliştirilecektir:

1. **Min-Heap Veri Yapısı**: Hasta listesinin öncelik seviyesine göre düzenlenmesini sağlayacak bir Min-Heap veri yapısı oluşturulacaktır.
2. **Dinamik Kuyruk Yönetimi**: Hastaları eklemek ve çıkartmak için ilgili fonksiyonlar tasarlanacaktır.
3. **Tedavi Simülasyonu**: 7 saatlik tedavi süresini kontrol eden bir algoritma geliştirilecektir.
4. **Raporlama**: Tedavi edilen ve edilemeyen hastaları raporlayan çıktılar yazılacak ve test edilecektir.

## Çıktılar
- [x] **Tedavi Edilen Hastalar**: Tedavi süreleri toplamı 7 saati geçmeden öncelik seviyesine göre tedavi edilen hastalar listesi.
- [x] **Tedavi Edilemeyen Hastalar**: Tedavi süreleri toplamı nedeniyle tedavi edilemeyen hastalar listesi.



## Katkıda Bulunma
**Katkıda bulunmak için lütfen bir **Pull Request** oluşturun ya da proje sahibine ulaşın.**

> [!NOTE]
> İşleri daha iyi veya daha kolay yapmak için faydalı tavsiyeler verebilirsiniz.


## Lisans
Bu proje Kocaeli Üniversitesi Lisansı ile lisanslanmıştır.

