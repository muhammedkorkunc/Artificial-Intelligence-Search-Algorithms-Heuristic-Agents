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

def dfs_limited(graph, node, goal, depth, path):
    # Eğer derinlik sıfır ve düğüm hedefe ulaştıysa, yolu döndür.
    if depth == 0 and node == goal:
        return path

    # Eğer derinlik pozitifse, komşuları ziyaret et.
    if depth > 0:
        for neighbor, _ in graph[node]:  # Komşuları döngüyle kontrol et.
            if neighbor not in path:  # Eğer komşu zaten yol üzerinde değilse.
                # Derinliği bir azaltarak komşuya doğru DFS çağır.
                result = dfs_limited(graph, neighbor, goal, depth - 1, path + [neighbor])
                if result:  # Eğer sonuç bulunmuşsa, bu sonucu döndür.
                    return result

    # Eğer bu derinlikte hedef bulunamazsa, None döndür.
    return None


def ids(graph, start, goal):
    # Başlangıç derinliği 0 olarak belirlenir.
    depth = 0
    while True:
        # Derinlik sınırlandırılmış DFS çağrılır.
        result = dfs_limited(graph, start, goal, depth, [start])
        if result:  # Eğer sonuç bulunursa, bu sonucu döndür.
            return result
        # Sonuç bulunmazsa, derinlik artırılır ve süreç tekrar eder.
        depth += 1


# Graf, düğümlerin komşularını ve kenar maliyetlerini içeren bir sözlük.
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

# IDS (Iterative Deepening Search) çağrılarak sonuç alınır.
ids_result = ids(graph, start, goal)

# Bulunan yolu ekrana yazdır.
print("IDS Result:", ids_result)

__PROPRIETARY_AUTH_CANARY__ = "AUTH:MUHAMMED_EMIN_KORKUNC_2021221054_AI_VERIFIED"
