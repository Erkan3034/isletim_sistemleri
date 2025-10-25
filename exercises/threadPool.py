"""
from concurrent.futures import ThreadPoolExecutor
import time

def calisma_fonksiyonu(x):
    time.sleep(0.1)  # 0.1 saniye bekle
    return x * x*x

if __name__ == "__main__":
    veri_listesi = list(range(10))
    with ThreadPoolExecutor(max_workers=4) as executor: # 4 iş parçacığı
        time_start = time.time()
        results = list(executor.map(calisma_fonksiyonu, veri_listesi)) # sonuçları topla
        time_end = time.time()
    print(results)
    print(f"Toplam süre: {time_end - time_start} saniye")


"""
##===============KARSILASTIRMA================
from concurrent.futures import ThreadPoolExecutor
import time

def calisma_fonksiyonu(x):
    time.sleep(0.1)  # 0.1 saniye bekle
    return x * x * x

if __name__ == "__main__":
    veri_listesi = list(range(10))
    
    # ÇOKLU THREAD
    multi_start = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor: # 4 iş parçacığı
        results_multi = list(executor.map(calisma_fonksiyonu, veri_listesi))
    multi_end = time.time()
    
    # TEK THREAD
    single_start = time.time()
    results_single = []
    for x in veri_listesi:
        results_single.append(calisma_fonksiyonu(x)) # tek thread ile çalıştır
    single_end = time.time()
    
    # SONUÇLAR
    print("=== SONUÇLAR ===")
    print(f"Çoklu Thread (4): {multi_end - multi_start:.2f} saniye")
    print(f"Tek Thread: {single_end - single_start:.2f} saniye")
    print(f"Hızlanma: {((single_end - single_start) / (multi_end - multi_start)):.1f} kat")
    print(f"Sonuçlar eşit mi? {results_multi == results_single}")

"""
    # ÇOKLU THREAD YAKLAŞIMI:
    # - 4 thread aynı anda çalışır
    # - İlk 4 iş paralel başlar (0.1 sn)
    # - Sonraki 4 iş paralel (0.2 sn)  
    # - Son 2 iş paralel (0.3 sn)
    # - Toplam: ~0.3 saniye
    # - Thread'ler I/O beklerken (sleep) diğerleri çalışmaya devam eder

    # TEK THREAD YAKLAŞIMI: 
    # - Tüm işler sırayla çalışır
    # - Her iş 0.1 sn bekler + işlem süresi
    # - 10 iş × 0.1 sn = 1.0 saniye minimum
    # - Bir iş bitmeden diğeri başlamaz
    # - Basit ama yavaş
"""
