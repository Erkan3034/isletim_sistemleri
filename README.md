# İŞLETİM SİSTEMLERİ KAVRAM HARİTASI
#### İşletim sistemlerine dair kişisel notlarım.
---
| **Konu Başlığı** | **Alt Başlık / Açıklama** | **Ek Bilgi / Örnek** |
|------------------|----------------------------|-----------------------|
| **1. TEMEL KAVRAMLAR VE MİMARİ** |  |  |
| **İşletim Sistemi Tanımı** | Bilgisayarın donanım ve yazılım kaynaklarını yöneten programdır. |  |
| **Amaçlar** | Kullanımı kolaylaştırmak, kaynakları verimli kullanmak, program çalıştırmayı kolaylaştırmak. |  |
| **Roller** | Kaynak Dağıtıcı (Resource Allocator), Kontrol Programı (Control Program). |  |
| **Bileşenler** | 1. Donanım (Hardware) <br> 2. İşletim Sistemi (Operating System) <br> 3. Uygulama Programları (Applications) <br> 4. Kullanıcılar (Users) |  |
| **Uygulama Programları** | Compilers, Games, vb. |  |
| **Kullanıcılar** | İnsanlar, makineler |  |
| **1.3 ÇEKİRDEK (Kernel)** | Bilgisayarda her zaman çalışan ana programdır. | İşlemci, bellek ve dosya sistemini yönetir. |
| **Monolitik Kernel** | Tüm çekirdek birlikte çalışır. | Avantaj: Hızlı çalışır. <br> Dezavantaj: Hata tüm sistemi çökertir. |
| **Mikro Kernel** | Çekirdek işlevleri kullanıcı alanına taşınır. | Avantaj: Daha güvenli iletişim. |
| **Hibrit Kernel** | Monolitik ve mikro çekirdeğin birleşimidir. | Örnek: Windows NT, macOS XNU |
| **Katmanlı Yaklaşım** | Donanım (Layer 0) ve kullanıcı arayüzü (Layer N) arasında katmanlar bulunur. |  |
| **Sanal Makineler (Virtual Machines)** | Aynı donanımda birden fazla sistem çalıştırma imkanı sağlar. | Örnek: VMware, VirtualBox |
| **1.4 Kabuk (Shell)** | Kullanıcı ile çekirdek arasındaki arayüzdür. |  |
| **Türleri** | CLI (Bash, PowerShell), GUI (Windows Explorer, GNOME), Sesli Asistanlar (Siri). |  |
| **1.5 İşletim Sistemi Mimarileri** | Kernel türlerini ve kullanıcı etkileşimini kapsar. |  |
| **2. SİSTEM ÇALIŞMASI VE I/O MEKANİZMALARI** | İşletim sisteminin girdi/çıktı işlemleri ve kesinti yönetimi. |  |
| **Kesintiler (Interrupts)** | Donanım veya yazılım tarafından CPU’ya iletilen sinyallerdir. | Örnek: Tuş basımı, disk okuma. |


