<?php
/*
 * Author: Muhammed Emin Korkunç (2021221054)
 * Artificial Intelligence - Vacuum World Reflex Agent
 * License: Proprietary (c) 2026
 */

// Oda ve temizlik durumu başlangıç değerleri

$rooms = [
    "Oda 1" => "kirli",
    "Oda 2" => "kirli"
];


// Ayarlar

$visitCount = 5; // Her odaya kaç kez gidileceği
$report = []; // Temizlik raporunu tutacak dizi



// Temizlik döngüsü

for ($i = 0; $i < $visitCount; $i++) {
    foreach ($rooms as $roomName => &$status) {
        echo "<h3>$roomName'ye girildi</h3>";
        
        // Oda temiz mi kirli mi kontrolü

        if ($status === "kirli") {
            echo "<p>$roomName kirli, temizleniyor...</p>";
            $status = "temiz";
            $report[$roomName][$i] = "Temizlendi";

        } else {
            echo "<p>$roomName zaten temiz, diğer odaya geçiliyor...</p>";
            $report[$roomName][$i] = "Temiz (Geçildi)";

        }



        // Diğer odanın kirlenme ihtimali

        $otherRoom = ($roomName === "Oda 1") ? "Oda 2" : "Oda 1";
        if ($rooms[$otherRoom] === "temiz" && rand(0, 1) === 1) {
            $rooms[$otherRoom] = "kirli";
            echo "<p>Uyarı: $otherRoom tekrar kirlendi!</p>";

        }
    }
    
    // Her turun sonunda odaların tekrar kirlenme olasılığı

    foreach ($rooms as $roomName => &$status) {
        if (rand(0, 1) === 1) {
            $status = "kirli";
            echo "<p> $roomName tekrar kirlendi!</p>";
        }
    }
}

// Raporun Görsel Grafiğini Oluşturma
echo "<h2>Temizlik Raporu</h2>";
echo "<style>
        .report { display: flex; gap: 20px; }
        .room { width: 100px; height: 100px; border: 1px solid #000; text-align: center; line-height: 100px; margin-top: 10px; }
        .temiz { background-color: lightgreen; }
        .kirli { background-color: lightcoral; }
      </style>";

echo "<div class='report'>";
foreach ($report as $roomName => $actions) {
    echo "<div><h3>$roomName</h3>";
    foreach ($actions as $action) {
        $statusClass = (strpos($action, "Temiz") !== false) ? "temiz" : "kirli";
        echo "<div class='room $statusClass'>$action</div>";
    }
    echo "</div>";
}
echo "</div>";




?>
