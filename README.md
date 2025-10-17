# İŞLETİM SİSTEMLERİ KAVRAM HARİTASI (KONSOL HİYERARŞİSİ)

/
└── 1. TEMEL_KAVRAMLAR_VE_MİMARİ
    ├── 1.1 IS_TANIMI_VE_AMAÇLARI
    [cite_start]│   ├── ROL: Kaynak Dağıtıcı (Resource Allocator) [cite: 696]
    [cite_start]│   ├── ROL: Kontrol Programı (Control Program) [cite: 699, 700]
    [cite_start]│   └── HEDEFLER: Kullanımı kolaylaştırmak, Program çalıştırmayı kolaylaştırmak, Donanımı verimli kullanmak. [cite: 689, 690, 691]
    │
    [cite_start]├── 1.2 BILGISAYAR_SISTEMI_YAPISI (4 Bileşen) [cite: 655]
    [cite_start]│   ├── DONANIM (Hardware) [cite: 656, 657]
    [cite_start]│   ├── İŞLETİM SİSTEMİ (Operating System) [cite: 658, 659]
    [cite_start]│   ├── UYGULAMA PROGRAMLARI (Compilers, Games, vb.) [cite: 660, 661]
    [cite_start]│   └── KULLANICILAR (İnsanlar, Makinalar) [cite: 662, 663]
    │
    ├── 1.3 CEKİRDEK_KERNEL
    [cite_start]│   ├── TANIM: Bilgisayarda her zaman çalışan tek programdır (olmazsa olmazıdır). [cite: 708]
    [cite_start]│   ├── GOREV: İşlemci, bellek ve dosya sistemini yönetir. [cite: 355, 356]
    [cite_start]│   └── ETKİLEŞİM: Kullanıcı ile doğrudan etkileşime girmez, sadece Sistem Çağrıları aracılığıyla çalışır. [cite: 361, 366, 367, 368]
    │
    ├── 1.4 KABUK_SHELL
    [cite_start]│   ├── TANIM: Kullanıcı ile çekirdek arasında köprü görevi gören komut yorumlayıcısıdır. [cite: 271, 272]
    [cite_start]│   ├── GOREV: Kullanıcının komutlarını alır ve çekirdeğe iletir. [cite: 273, 276]
    [cite_start]│   └── TUR: CLI (Bash, PowerShell) [cite: 288, 289, 290] | [cite_start]GUI (Windows Explorer, GNOME) [cite: 292, 293, 295] | [cite_start]Sesli Asistanlar (Siri) [cite: 296, 329]
    │
    └── 1.5 ISLETİM_SİSTEMİ_MİMARİLERİ
        ├── MONOLİTİK_KERNEL
        [cite_start]│   ├── ÖZELLİK: Tüm çekirdek bileşenleri tek bir blok içinde çalışır. [cite: 388]
        [cite_start]│   ├── AVANTAJ: Hızlı çalışır. [cite: 391]
        [cite_start]│   └── DEZAVANTAJ: Hata tüm sistemi çökertme riski taşır. [cite: 388, 392]
        ├── MİKRO_KERNEL
        [cite_start]│   ├── ÖZELLİK: Çekirdekteki işlevlerin çoğu kullanıcı alanına taşınır (message passing ile iletişim). [cite: 403, 404]
        ├── HİBRİT_KERNEL
        [cite_start]│   ├── ÖZELLİK: Monolitik ve mikro çekirdeklerin birleşimidir. [cite: 394]
        [cite_start]│   └── ÖRNEKLER: Windows NT, macOS XNU. [cite: 395, 396]
        ├── KATMANLI_YAKLASIM
        [cite_start]│   ├── ÖZELLİK: İS, donanım (Layer 0) ve kullanıcı arayüzü (Layer N) arasında katmanlara ayrılır. [cite: 247, 248, 249, 250]
        [cite_start]└── SANAL_MAKİNALAR (Virtual Machines) [cite: 574]
            [cite_start]├── KULLANIM: Donanımı ve İS çekirdeğini donanım katmanı gibi kullanır. [cite: 575]
            └── FAYDA: Birden fazla çalıştırma ortamı aynı donanımı paylaşabilir; [cite_start]Sistem geliştirmek ve test etmek için kullanışlıdır. [cite: 584, 587]

└── 2. SİSTEM_ÇALIŞMASI_VE_I/O_MEKANİZMALARI
    ├── 2.1 KESİNTİLER_VE_TUDAKLAR
    [cite_start]│   ├── KESİNTİ (Interrupt): Cihaz denetleyicisi I/O işlemi bittiğinde işlemciye gönderir. [cite: 746]
    [cite_start]│   └── TUZAK (Trap): Yazılım tarafından oluşturulan kesintilerdir (Hata veya kullanıcı isteği). [cite: 771, 772]
    │
    ├── 2.2 DIREK_HAFIZA_ERİSİMİ (DMA)
    [cite_start]│   ├── AMAÇ: Yüksek hızlı I/O cihazları için kullanılır. [cite: 785]
    [cite_start]│   └── MEKANİZMA: Cihaz denetleyicisinin veri bloklarını CPU'yu bölmeden direk hafızaya aktarmasıdır (Her blok için 1 kesinti gönderilir). [cite: 786, 787]
    │
    └── 2.3 SISTEM_ÇAĞRILARI (System Calls)
        [cite_start]├── TANIM: İS tarafından sunulan servisler için programlama arayüzüdür. [cite: 463]
        [cite_start]├── KULLANIM: Genellikle API'ler (Win32 API gibi) aracılığıyla kullanılır. [cite: 466, 467, 468]
        [cite_start]└── ÇEŞİTLERİ: İşlem kontrolü, Dosya yönetimi, Cihaz yönetimi, İletişim, Koruma, Bilgi sağlama. [cite: 553, 554, 555, 556, 557, 558]

└── 3. İŞLEM_YÖNETİMİ (PROCESS_MANAGEMENT)
    ├── 3.1 İŞLEM_KAVRAMI
    [cite_start]│   ├── TANIM: Çalışmakta olan programdır (Aktif Varlık). [cite: 1026, 1027]
    [cite_start]│   ├── İHTİYAÇ: CPU, hafıza, I/O, dosyalar gibi kaynaklar. [cite: 1029]
    [cite_start]│   └── İÇERİK: Program Sayacı, Yığın (Stack), Veri Bölümü (Data), Heap (Öbek). [cite: 1272, 1274, 1275, 1276]
    │
    ├── 3.2 İŞLEM_DURUMLARI (STATES)
    [cite_start]│   ├── new (yeni): İşlem oluşturuldu. [cite: 1314]
    [cite_start]│   ├── ready (hazır): Bir işlemciye atanmayı bekliyor. [cite: 1317, 1332]
    [cite_start]│   ├── running (çalışıyor): İşlem komutları çalıştırılıyor. [cite: 1315]
    [cite_start]│   ├── waiting (bekliyor): Bir olayın (I/O) gerçekleşmesini bekliyor. [cite: 1316, 1338]
    [cite_start]│   └── terminated (sonlandırılmış): İşlem çalışmayı bitirmiş. [cite: 1318]
    │
    ├── 3.3 İŞLEM_KONTROL_BLOKU (PCB)
    [cite_start]│   ├── TANIM: Her işlem ile ilişkili bilgileri tutar. [cite: 1378]
    [cite_start]│   ├── İÇERİK: İşlem durumu, İşlem sayacı, CPU yazmaçları, Hafıza bilgileri, I/O durum bilgileri. [cite: 1379, 1380, 1381, 1383, 1385]
    [cite_start]│   └── ORTAM_DEĞİŞİKLİĞİ (Context Switch): CPU başka bir işleme geçerken eski işlemin durumunu PCB'ye kaydeder ve yeni işlemin durumunu yükler. [cite: 1563]
    │
    ├── 3.4 İŞLEM_ZAMANLAYICILARI (Schedulers)
    [cite_start]│   ├── UZUN_VADELİ (Long-Term/Job Scheduler): Hangi işlemlerin hazır kuyruğuna alınacağına karar verir (Çoklu programlama seviyesini kontrol eder). [cite: 1514, 1515, 1517, 1533]
    [cite_start]│   ├── KISA_VADELİ (Short-Term/CPU Scheduler): Sıradaki hangi işlemin CPU tarafından çalıştı rılacağına karar verir (Çok sık çalışır). [cite: 1519, 1525, 1530]
    │   └── ORTA_VADELİ (Medium-Term Scheduler): CPU'da çalışan uygulamayı kısa süreli diske atıp tekrar RAM'e alır (**Swap Out/In**). [cite_start]Sanal bellek sağlar. [cite: 1545]
    │
    ├── 3.5 İŞLEM_OLUŞTURMA_VE_SONLANDIRMA
    [cite_start]│   ├── OLUŞTURMA: Ana işlem (parent) çocuk işlemler (children) oluşturur. [cite: 1574]
    [cite_start]│   ├── UNIX_FORK: Yeni bir işlem oluşturur. [cite: 1621]
    [cite_start]│   ├── UNIX_EXEC: Yeni işlemin hafıza alanına yeni bir program yükler. [cite: 1622, 1624]
    │   └── SONLANDIRMA: İşlem bitince `exit()` ile silinmesini ister; [cite_start]Ana işlem `abort` ile çocukları sonlandırabilir. [cite: 1707, 1710]
    │
    └── 3.6 İŞ_PARÇACIKLARI (Threads)
        [cite_start]└── TANIM: Bir program çalışırken aynı anda yapılması gereken başka işler varsa bunları çalıştırmak için kullanılır. [cite: 1036]

└── 4. DEPOLAMA_VE_HAFIZA_YÖNETİMİ
    ├── 4.1 HAFIZA_YÖNETİMİ
    [cite_start]│   ├── GÖREV: Hafızanın kim tarafından kullanıldığını takip etmek; hangi işlemlerin/verilerin hafızaya alınıp çıkarılacağına karar vermek. [cite: 1064]
    [cite_start]│   └── VİRTUAL_MEMORY: Tümüyle hafızada bulunmayan işlemleri çalıştırmayı sağlar. [cite: 983]
    │
    ├── 4.2 DEPOLAMA_HİYERARŞİSİ
    [cite_start]│   ├── DÜZEN: Hız, maliyet ve kalıcılığa (volatility) göre organize edilir. [cite: 835, 836, 837]
    [cite_start]│   └── HİYERARŞİ: Registers > Cache > Main Memory > Electronic Disk > Magnetic Disk > Optical Disk > Magnetic Tapes. [cite: 825, 827, 830, 834, 841, 842, 843]
    │
    └── 4.3 I/O_ALT_SİSTEMİ
        [cite_start]├── AMAÇ: Donanım cihazlarının karmaşıklıklarını kullanıcıdan gizlemektir. [cite: 1111]
        [cite_start]└── GÖREVLER: Tampon bellek (Buffering), Ön bellek (Caching), Kuyruklama (Spooling). [cite: 1115, 1116, 1117]
