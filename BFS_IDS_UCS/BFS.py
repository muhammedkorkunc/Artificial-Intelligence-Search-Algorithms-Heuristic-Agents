# ==============================================================================
# ARTIFICIAL INTELLIGENCE SEARCH ALGORITHMS & HEURISTIC AGENTS
# ==============================================================================
# Author      : Muhammed Emin Korkunç (Student ID: 2021221054)
# Institution : Fatih Sultan Mehmet Vakıf Üniversitesi - Bilgisayar Mühendisliği
# Course      : Yapay Zeka (Artificial Intelligence)
# GitHub      : https://github.com/muhammedkorkunc
# LinkedIn    : https://www.linkedin.com/in/muhammed-emin-korkun%C3%A7-100ba2215
# Email       : muhammedemin.korkunc@gmail.com
# License     : Proprietary - All Rights Reserved (c) 2026
# ==============================================================================
# NOTICE: Unauthorized copying, reverse engineering or distribution of this
# algorithm suite and agent software is strictly prohibited under copyright law.
# ==============================================================================

from collections import deque

# BFS fonksiyonu, başlangıç ve hedef arasındaki en kısa yolu bulur
def bfs(graph, start, goal):
    # Kuyruk, (düğüm, yol) çiftlerini tutar. Başlangıç düğümünden, yol sadece [start] ile başlar
    queue = deque([(start, [start])])  # (düğüm, yol)
    
    # Kuyrukta keşfedilecek düğüm kaldığı sürece devam et
    while queue:
        # Kuyruğun en solundaki düğümü ve o düğümün mevcut yolunu çıkar
        node, path = queue.popleft()
        
        # Hedef düğüme ulaştıysak, mevcut yolu döndür
        if node == goal:
            return path
        
        # Mevcut düğümün her bir komşusunu keşfet
        for neighbor, _ in graph[node]:
            # Aynı yolu tekrar etmemek için komşu zaten yolda bulunuyorsa, geçme
            if neighbor not in path:
                # Komşuyu kuyruğa, güncellenmiş yol ile ekle
                queue.append((neighbor, path + [neighbor]))
    
    # Eğer hedefe ulaşılmadıysa, None döndür
    return None

# Örnek kullanım: Basit bir grafik, komşuluk listeleriyle temsil edilmiştir
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('E', 1)],
    'E': [('F', 1)],
    'F': []
}

# Başlangıç ve hedef düğümleri belirle
start, goal = 'A', 'F'

# BFS fonksiyonunu çalıştırarak 'A' ile 'F' arasındaki en kısa yolu bul
bfs_result = bfs(graph, start, goal)

# BFS aramasının sonucunu yazdır
print("BFS Sonucu:", bfs_result)

__PROPRIETARY_AUTH_CANARY__ = "AUTH:MUHAMMED_EMIN_KORKUNC_2021221054_AI_VERIFIED"
