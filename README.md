# 🧠 Classical Artificial Intelligence & Heuristic Search Algorithms

### Arama Stratejileri, Sezgisel Ajanlar, Oyun Teorisi ve Yerel Optimizasyon

Bu depo; Fatih Sultan Mehmet Vakıf Üniversitesi Bilgisayar Mühendisliği **Yapay Zeka (Artificial Intelligence)** dersi kapsamında geliştirilen klasik ve sezgisel arama algoritmalarını, A\* tabanlı akıllı ajan tasarımlarını, yerel arama problemlerini ve akademik analiz raporlarını içerir.

---

## 🛠️ Algoritma ve Proje Modülleri

| Modül                                    | Algoritmalar & Yöntemler        | Açıklama                                                                                        |
| :--------------------------------------- | :------------------------------ | :---------------------------------------------------------------------------------------------- |
| **Arama Algoritmaları (`BFS_IDS_UCS/`)** | BFS, IDS, UCS                   | Seviye öncelikli, derinleşen ve en düşük maliyet öncelikli rota optimizasyonu.                  |
| **Gelişmiş Sezgisel (`RFBMS_SMA.py`)**   | RBFS, SMA\*                     | Bellek kısıtlı A\* (Simplified Memory-Bounded) ve özyinelemeli en iyi öncelikli arama.          |
| **Çift Yönlü Arama (`Bidirectional`)**   | Bidirectional Graph Search      | Başlangıç ve hedef düğümlerden aynı anda ilerleyerek kesişim düğümü bulma analizi.              |
| **N-Vezir Problemi (`vezirproblem/`)**   | Hill Climbing Local Search      | Satranç tahtasında vezirlerin tehdit durumlarını minimize eden yerel arama çözücüsü.            |
| **Akıllı PacMan (`Pacman_*.py`)**        | A\* Pathfinding & Utility Agent | Rastgele labirent üreteci (DFS maze generator), hayaletlerden kaçış ve A\* ile yiyecek toplama. |
| **Vakum Dünyası (`robot.php`)**          | Reflex Agent Simulation         | İki odalı stokastik kirlenme modeline sahip akıllı temizlik ajanı döngüsü.                      |
| **`korumali_raporlar/`**                 | Akademik Raporlar & Analizler   | Çift katmanlı doğrulanmış yazar filigranına sahip teknik çözüm raporları.                       |

---

## 🚀 Çalıştırma Örnekleri

```bash
# Akıllı PacMan oyununu başlat (1: Manuel, 2: Yapay Zeka Ajanı)
python3 Pacman_MuhammedEminKorkunc_2021221054.py

# BFS, IDS ve UCS algoritmalarını çalıştırma
python3 BFS_IDS_UCS/BFS.py
python3 BFS_IDS_UCS/IDS.py
python3 BFS_IDS_UCS/UCS.py

# RBFS ve SMA* sezgisel aramasını çalıştırma
python3 RFBMS_SMA.py
```

Copyright (c) 2026 Muhammed Emin Korkunç. All Rights Reserved.

Yazarın açık yazılı izni olmaksızın kısmen veya tamamen kopyalanması,
dağıtılması, çoğaltılması veya ticari/akademik amaçla izinsiz kullanımı kesinlikle yasaktır.

👨‍💻 Geliştirici / Author
Muhammed Emin Korkunç

GitHub: @muhammedkorkunc

LinkedIn: Muhammed Emin Korkunç

Email: muhammedemin.korkunc@gmail.com
