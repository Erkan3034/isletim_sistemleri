from concurrent.futures import ThreadPoolExecutor
import time

def calisma_fonksiyonu(x):
    time.sleep(0.5)  # örnek iş
    return x * x

if __name__ == "__main__":
    veri_listesi = list(range(10))
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(calisma_fonksiyonu, veri_listesi))
    print(results)