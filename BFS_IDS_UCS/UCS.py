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

import heapq

def ucs(graph, start, goal):
    # Öncelikli kuyruk oluşturulur, başlangıç maliyeti 0'dır ve yol başlangıç düğümünü içerir.
    priority_queue = [(0, start, [start])]  # (cost, node, path)
    
    # Ziyaret edilen düğümleri tutan bir set.
    visited = set()
    
    # Kuyruk boşalana kadar döngü devam eder.
    while priority_queue:
        # En düşük maliyetli yol kuyruktan çıkarılır.
        cost, node, path = heapq.heappop(priority_queue)
        
        # Eğer düğüm daha önce ziyaret edilmişse, bu yol atlanır.
        if node in visited:
            continue
        
        # Düğüm ziyaret edilmiş olarak işaretlenir.
        visited.add(node)
        
        # Eğer hedef düğüme ulaşılmışsa, yol ve maliyet döndürülür.
        if node == goal:
            return path, cost
        
        # Düğümün komşuları dolaşılır.
        for neighbor, edge_cost in graph[node]:
            # Eğer komşu ziyaret edilmemişse, yeni maliyet hesaplanır ve kuyrukta saklanır.
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path + [neighbor]))
    
    # Eğer hedef düğüme ulaşılamazsa, `None` döndürülür.
    return None

# Graf, her düğümün komşularını ve komşulara olan ağırlıklı yollarını içeren bir sözlük.
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('E', 1)],
    'E': [('F', 1)],
    'F': []
}

# Başlangıç ve hedef düğümler belirlenir.
start, goal = 'A', 'F'

# UCS algoritması çağrılır ve sonucu alınır.
ucs_result, ucs_cost = ucs(graph, start, goal)

# Bulunan yol ve toplam maliyet ekrana yazdırılır.
print("UCS Result:", ucs_result, "Cost:", ucs_cost)

__PROPRIETARY_AUTH_CANARY__ = "AUTH:MUHAMMED_EMIN_KORKUNC_2021221054_AI_VERIFIED"
