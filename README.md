# İŞLETİM SİSTEMLERİ KAVRAM HARİTASI
#### İşletim sistemlerine dair kişisel notlarım.

/
└── 1. TEMEL KAVRAMLAR VE MİMARİ
    ├── 1.1 İŞLETİM SİSTEMİ TANIMI VE AMAÇLARI
    │   ├── ROL: Kaynak Dağıtıcı (Resource Allocator)
    │   ├── ROL: Kontrol Programı (Control Program)
    │   └── HEDEFLER: Kullanımı kolaylaştırmak, program çalıştırmayı kolaylaştırmak, donanımı verimli kullanmak.
    │
    ├── 1.2 BİLGİSAYAR SİSTEMİ YAPISI (4 Bileşen)
    │   ├── DONANIM (Hardware)
    │   ├── İŞLETİM SİSTEMİ (Operating System)
    │   ├── UYGULAMA PROGRAMLARI (Compilers, Games, vb.)
    │   └── KULLANICILAR (İnsanlar, Makinalar)
    │
    ├── 1.3 ÇEKİRDEK (Kernel)
    │   ├── TANIM: Bilgisayarda her zaman çalışan tek programdır.
    │   ├── GÖREV: İşlemci, bellek ve dosya sistemini yönetir.
    │   └── ETKİLEŞİM: Kullanıcı ile doğrudan etkileşime girmez, sadece sistem çağrıları aracılığıyla çalışır.
    │
    ├── 1.4 KABUK (Shell)
    │   ├── TANIM: Kullanıcı ile çekirdek arasında köprü görevi gören komut yorumlayıcısıdır.
    │   ├── GÖREV: Kullanıcının komutlarını alır ve çekirdeğe iletir.
    │   └── TÜRLER:
    │       • CLI (Bash, PowerShell)
    │       • GUI (Windows Explorer, GNOME)
    │       • Sesli Asistanlar (Siri)
    │
    └── 1.5 İŞLETİM SİSTEMİ MİMARİLERİ
        ├── MONOLİTİK KERNEL
        │   ├── Özellik: Tüm çekirdek bileşenleri tek bir blok içinde çalışır.
        │   ├── Avantaj: Hızlı çalışır.
        │   └── Dezavantaj: Hata tüm sistemi çökertme riski taşır.
        │
        ├── MİKRO KERNEL
        │   └── Özellik: Çekirdekteki işlevlerin çoğu kullanıcı alanına taşınır (message passing ile iletişim).
        │
        ├── HİBRİT KERNEL
        │   ├── Özellik: Monolitik ve mikro çekirdeklerin birleşimidir.
        │   └── Örnekler: Windows NT, macOS XNU
        │
        ├── KATMANLI YAKLAŞIM
        │   └── Özellik: İS, donanım (Layer 0) ve kullanıcı arayüzü (Layer N) arasında katmanlara ayrılır.
        │
        └── SANAL MAKİNALAR (Virtual Machines)
            ├── Kullanım: Donanımı ve İS çekirdeğini donanım katmanı gibi kullanır.
            └── Fayda: Birden fazla çalıştırma ortamı aynı donanımı paylaşabilir; sistem geliştirmek ve test etmek için kullanışlıdır.

└── 2. SİSTEM ÇALIŞMASI VE I/O MEKANİZMALARI
    ├── 2.1 KESİNTİLER VE TUZAKLAR
    │   ├── KESİNTİ (Interrupt): Cihaz denetleyicisi I/O işlemi bittiğinde işlemciye gönderir.
    │   └── TUZAK (Trap): Yazılım tarafından oluşturulan kesintilerdir (hata veya kullanıcı isteği).
    │
    ├── 2.2 DİREK HAFIZA ERİŞİMİ (DMA)
    │   ├── Amaç: Yüksek hızlı I/O cihazları için kullanılır.
    │   └── Mekanizma: Cihaz denetleyicisinin veri bloklarını CPU’yu bölmeden direk hafızaya aktarmasıdır (her blok için 1 kesinti gönderilir).
    │
    └── 2.3 SİSTEM ÇAĞRILARI (System Calls)
        ├── Tanım: İS tarafından sunulan servisler için programlama arayüzüdür.
        ├── Kullanım: Genellikle API’ler (örneğin Win32 API) aracılığıyla kullanılır.
        └── Çeşitleri: İşlem kontrolü, dosya yönetimi, cihaz yönetimi, iletişim, koruma, bilgi sağlama.

└── 3. İŞLEM YÖNETİMİ (PROCESS MANAGEMENT)
    ├── 3.1 İŞLEM KAVRAMI
    │   ├── Tanım: Çalışmakta olan programdır (aktif varlık).
    │   ├── İhtiyaç: CPU, hafıza, I/O, dosyalar gibi kaynaklar.
    │   └── İçerik: Program sayacı, yığın (stack), veri bölümü (data), heap (öbek).
    │
    ├── 3.2 İŞLEM DURUMLARI (States)
    │   ├── new: İşlem oluşturuldu.
    │   ├── ready: İşlemciye atanmayı bekliyor.
    │   ├── running: İşlem komutları çalıştırılıyor.
    │   ├── waiting: Bir olayın (I/O) gerçekleşmesini bekliyor.
    │   └── terminated: İşlem çalışmayı bitirmiş.
    │
    ├── 3.3 İŞLEM KONTROL BLOĞU (PCB)
    │   ├── Tanım: Her işlem ile ilişkili bilgileri tutar.
    │   ├── İçerik: İşlem durumu, işlem sayacı, CPU yazmaçları, hafıza bilgileri, I/O durum bilgileri.
    │   └── Ortam Değişikliği (Context Switch): CPU başka bir işleme geçerken eski işlemin durumunu PCB’ye kaydeder ve yeni işlemin durumunu yükler.
    │
    ├── 3.4 İŞLEM ZAMANLAYICILARI (Schedulers)
    │   ├── Uzun Vadeli (Long-Term / Job Scheduler): Hangi işlemlerin hazır kuyruğa alınacağına karar verir.
    │   ├── Kısa Vadeli (Short-Term / CPU Scheduler): Sıradaki işlemin CPU tarafından çalıştırılmasına karar verir.
    │   └── Orta Vadeli (Medium-Term Scheduler): CPU’daki uygulamayı kısa süreli diske atıp tekrar RAM’e alır (swap out/in).
    │
    ├── 3.5 İŞLEM OLUŞTURMA VE SONLANDIRMA
    │   ├── Oluşturma: Ana işlem (parent), çocuk işlemler (children) oluşturur.
    │   ├── UNIX fork(): Yeni bir işlem oluşturur.
    │   ├── UNIX exec(): Yeni işlemin hafıza alanına yeni bir program yükler.
    │   └── Sonlandırma: İşlem bitince `exit()` ile silinmesini ister; ana işlem `abort()` ile çocuklarını sonlandırabilir.
    │
    └── 3.6 İŞ PARÇACIKLARI (Threads)
        └── Tanım: Bir program çalışırken aynı anda yapılması gereken başka işler varsa bunları çalıştırmak için kullanılır.

└── 4. DEPOLAMA VE HAFIZA YÖNETİMİ
    ├── 4.1 HAFIZA YÖNETİMİ
    │   ├── Görev: Hafızanın kim tarafından kullanıldığını takip etmek; hangi işlemlerin/verilerin hafızaya alınıp çıkarılacağına karar vermek.
    │   └── Sanal Bellek (Virtual Memory): Tümüyle hafızada bulunmayan işlemleri çalıştırmayı sağlar.
    │
    ├── 4.2 DEPOLAMA HİYERARŞİSİ
    │   ├── Düzen: Hız, maliyet ve kalıcılığa (volatility) göre organize edilir.
    │   └── Hiyerarşi: Registers > Cache > Main Memory > Electronic Disk > Magnetic Disk > Optical Disk > Magnetic Tapes
    │
    └── 4.3 I/O ALT SİSTEMİ
        ├── Amaç: Donanım cihazlarının karmaşıklıklarını kullanıcıdan gizlemektir.
        └── Görevler: Tampon bellek (Buffering), ön bellek (Caching), kuyruklama (Spooling).

