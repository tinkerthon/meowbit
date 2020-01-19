# Meowbit

Infos und Beispiele zum Meowbit von https://kittenbot.cn

Das [Meowbit](https://www.kittenbot.cc/collections/frontpage/products/meowbit-codable-console-for-microsoft-makecode-arcade) ist eine kleine Spielekonsole des chinesischen Herstellers Kittenbot. Du kannst es [auf Amazon kaufen](https://amzn.to/2R8b7Ja). Auch Adafruit [vertreibt es](https://blog.adafruit.com/2019/08/01/new-product-kittenbot-meowbit-codable-console-for-makecode-arcade/) seit August 2018.

Das Meowbit kann auf drei Arten programmiert werden:

* https://arcade.makecode.com/ von Microsoft. Das Meowbit ist eine der offiziell unterstützten Spielekonsolen
  
  ![Microsoft Arcade](images/00-arcade.png)

* https://www.kittenbot.cc/pages/software von Kittenbot. Es gibt eine Variante namens Kittenblock von MIT Scratch mit MicroPython-Integration für Windows und macOS und eine angepasste Version des Mu-Editors, diesen leider nur für Windows.
* https://codewith.mu/en/download von Mu-Editor. Ich habe hiermit allerdings noch nicht geschafft, die REPL (Befehlszeile) auf dem Meowbit aufzurufen.

## Python mit Kittenblock

Das Meowbit ist eigentlich [sehr gut dokumentiert](https://meowbit-doc.kittenbot.cn/#/kittenblock/kittenblockQS), leider allerdings nur in Chinesisch. Hier hilft der Chrome-Browser mit seiner automatischen Übersetzungsfunktion.

![Meowbit Dokumentation](images/00-meowbit-doc.png)

Um die Hardware des Meowbit in MicroPython nutzen zu können, müssen einige Bibliotheken auf ddas PYBFLASH-Laufwerk gezogen werden. Diese Bibliotheken liegen im Ordner `Applications/Kittenblock.app/Contents/extensions/s3ext-meowbit`:

* buzz.py - für den Summer
* mpu6050.py - für das sechsachsige Gyroskop
* tft.py - für den Farbbildschirm
* turtle.py - für Zeichnungen mit Turtle-Grafik

## 01 Blinkende LED

Hier ist ein erstes Programm zum Blinken der LED

![Blinkende LED](images/01-blink-led.png)

## Bildschirm und Tasten

Der Bildschirm hat eine Auflösung von 160 (horizontal) und 128 (vertikal). Der Ursprung (Punkt 0,0) ist oben links. Die Bildschirmmitte liegt demnach bei (80, 64).



