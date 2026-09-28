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

import math
import heapq


class Graph:
    def __init__(self):
        self.graph = {}  # Grafik, komşuluk listeleriyle temsil edilecek

    # Bir kenar eklemek için fonksiyon (u, v, cost)
    def add_edge(self, u, v, cost):
        if u not in self.graph:
            self.graph[u] = []  # Eğer 'u' düğümü yoksa, yeni bir liste başlat
        self.graph[u].append((v, cost))  # 'v' komşusu, 'u'ya eklenecek

    # Bir düğümün komşularını döndüren fonksiyon
    def neighbors(self, node):
        return self.graph.get(node, [])  # Düğümün komşuları, eğer varsa döndürülür


def rbfs(graph, start, goal, f_limit, h):
    # Recursive Best-First Search (RBFS) fonksiyonu
    def recursive_best_first(node, g, f_limit):
        if node == goal:  # Hedef düğüme ulaşıldığında
            return [node], g  # Hedefi ve maliyeti döndür

        successors = []  # Successorları (komşuları) saklamak için bir liste
        # Komşuları gez ve f-değerlerini hesapla
        for neighbor, cost in graph.neighbors(node):
            f_value = g + cost + h(neighbor)  # f = g + h
            successors.append((f_value, neighbor, g + cost))  # Successorları f değeriyle birlikte ekle

        if not successors:
            return None, math.inf  # Komşu yoksa, None döndür

        successors.sort()  # f değeri ile sıralama

        while successors:
            best_f, best_node, best_g = successors[0]
            if best_f > f_limit:  # f değeri, f_limit'ten büyükse
                return None, best_f  # Durdur, en iyi değeri döndür

            # Alternatif en iyi f değeri
            if len(successors) > 1:
                alternative = successors[1][0]
            else:
                alternative = math.inf

            # En iyi düğümü tekrar kontrol et
            result, best_f = recursive_best_first(best_node, best_g, min(f_limit, alternative))
            successors[0] = (best_f, best_node, best_g)
            successors.sort()
            if result:
                return [node] + result, best_f  # Sonuç varsa döndür

        return None, math.inf  # Eğer yol bulunamazsa

    return recursive_best_first(start, 0, f_limit)  # Başlangıç düğümünden başla


def sma_star(graph, start, goal, h):
    # Simplified Memory-Bounded A* (SMA*) fonksiyonu
    open_list = []  # Açık liste, işlenecek düğümleri tutar
    closed = {}  # Kapalı liste, ziyaret edilen düğümleri tutar
    heapq.heappush(open_list, (h(start), start, 0, None))  # İlk düğümü ekle
    max_open_size = 5  # Açık listedeki maksimum boyut

    while open_list:
        if len(open_list) > max_open_size:  # Eğer açık liste belirli bir boyutu geçerse
            open_list.pop()  # En düşük maliyetli olanı çıkar

        f, node, g, parent = heapq.heappop(open_list)  # En düşük maliyetli düğümü çıkar

        if node == goal:  # Eğer hedef düğüme ulaşıldıysa
            path = []  # Yolu oluştur
            while parent:
                path.append(node)
                node, parent = parent
            path.append(start)
            return path[::-1]  # Yolu ters çevirerek döndür

        closed[node] = g  # Düğümü kapalı listeye ekle

        # Komşuları gez ve her komşu için yeni maliyet hesapla
        for neighbor, cost in graph.neighbors(node):
            new_g = g + cost
            if neighbor in closed and closed[neighbor] <= new_g:
                continue  # Eğer komşuya daha önce ulaşılmışsa, geç

            heapq.heappush(open_list, (new_g + h(neighbor), neighbor, new_g, (node, parent)))  # Komşuyu açık listeye ekle

    return None  # Hedefe ulaşılamazsa, None döndür


# Heuristic fonksiyonu (h)
def heuristic(node):
    # Düğümlerin hedefe olan tahmini uzaklık değerlerini döndürür
    h_values = {
        'A': 6,
        'B': 5,
        'C': 3,
        'D': 3,
        'E': 1,
        'F': 0  # Hedef düğüm F, bu yüzden h(F) = 0
    }
    return h_values.get(node, math.inf)  # Eğer düğüm bilinmiyorsa, sonsuz döndür


# Grafik başlatma
graph = Graph()
edges = [
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'D', 2),
    ('B', 'E', 5),
    ('C', 'F', 3),
    ('D', 'E', 1),
    ('E', 'F', 1)
]
for u, v, cost in edges:
    graph.add_edge(u, v, cost)  # Kenarları ekle

# Başlangıç ve hedef düğümleri
start_node = 'A'
goal_node = 'F'


# RBFS çözümü
path_rbfs, _ = rbfs(graph, start_node, goal_node, math.inf, heuristic)
print("RBFS Yolu:", path_rbfs)


# SMA* çözümü
path_sma = sma_star(graph, start_node, goal_node, heuristic)
print("SMA* Yolu:", path_sma)

__PROPRIETARY_AUTH_CANARY__ = "AUTH:MUHAMMED_EMIN_KORKUNC_2021221054_AI_VERIFIED"
