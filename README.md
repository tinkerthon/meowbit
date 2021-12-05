# Meowbit

Ich habe [Ende 2021 ein Update](https://meetup.codekulturbonn.de/groups/1/discussions/60) geschrieben.

Infos und Beispiele zum Meowbit von https://kittenbot.cn

Das [Meowbit](https://www.kittenbot.cc/collections/frontpage/products/meowbit-codable-console-for-microsoft-makecode-arcade) ist eine kleine Spielekonsole des chinesischen Herstellers Kittenbot. Du kannst es [auf Amazon kaufen](https://amzn.to/2R8b7Ja). Auch Adafruit [vertreibt es](https://blog.adafruit.com/2019/08/01/new-product-kittenbot-meowbit-codable-console-for-makecode-arcade/) seit August 2019.

![Meowbit, bbc:microbit, Calliope Mini](images/00-meowbit_microbit_calliope.jpg)

Das Meowbit nutzt als Rechenkern einen STM32F401RET6, das ist ein 32-Bit-ARM-Cortex-M4-Prozessor ([Datenblatt](http://www.farnell.com/datasheets/1848998.pdf)). Darüber hinaus ist eine beeindruckende Menge an Hardware eingebaut:

* LED für Lade- / Arbeitsanzeige
* Lichtsensor
* Schiebeschalter zum Ein-/Ausschalten
* zwei programmierbare LED
* Reset-Taste
* DFU-Modus-Taste (auch zum Aufrufen des Menüs durch die Makecode-Firmware)
* 160 x 128 tft Farbbildschirm
* Temperaturfühler
* vier programmierbare Richtungstasten
* programmierbarer Summer
* zwei programmierbare Tasten A und B
* 40-Pin-Goldkontaktleiste, kompatibel zum micro:bit
* USB-Port zum Laden und Programmieren
* SD-Kartenslot (zum Speichern von Programmen und nachträglichen Erweitern um ein Bluetooth- oder WLAN-Modul)
* Klinkenbuchse zum Verbinden mehrerer Geräte (JacDac)
* 6-Achsen-Gyroskop und Beschleunigungsmesser
* 3,7 V Lithium-Batterie-Schnittstelle

Standardmäßig sind 2 MByte des SPI-Flash-Speichers mit einer Unicode-Zeichentabelle
belegt.

Hier ist die Pinbelegung der 40-poligen Steckerleiste (Stand: 2020-01-18. [Original](https://meowbit-doc.kittenbot.cn/#/more/intro)):

![Pinbelegung](images/1Sbv9O.png)

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

## Bildschirm und Tasten

Der Bildschirm hat eine Auflösung von 160 (horizontal) und 128 (vertikal). Der Ursprung (Punkt 0,0) ist oben links. Die Bildschirmmitte liegt demnach bei (80, 64).

Der Code für die folgenden Beispiele liegt im `code/`-Unterverzeichnis.

## 01 Erster Test: 01 Blinkende LED

Hier ist ein erstes Programm zum Blinken der LED

![Blinkende LED](images/01-blink-led.png)

## 02 Befehle für Leuchtdioden (LEDs) 

Dies sind die Befehle für die eine, grüne LED am Gerät oben rechts:

* led1.on()   # LED an
* led1.off()  # LED aus
* led1.toggle()      # LED umschalten
* led1.intensity(x)  # Helligkeit der LED

Hier ein weiteres Beispiel:

![LED-Helligkeit](images/02-led.png)

## 03 Atmende LED

Wie die Statusleuchte an Macs:

![Atmende LED](images/03-breathing-led.png)

## 04 Tasten per Interrupt

Für gute Responsivität können die Tasten per Interrupt abgefragt werden. Einen passenden, blauen Block habe ich nicht gefunden (obwohl er in der [Originaldokumentation](https://meowbit-doc.kittenbot.cn/#/kittenblock/02%E6%8C%89%E9%94%AE%E6%A3%80%E6%B5%8B) abgebildet ist), aber [hier](code/04-keys.py) ist der Python-Code.

Ich habe in der Anleitung ein [komplexeres Beispiel](code/05-keys-intensity.sb3) inklusive der Blöcke gefunden:

![mehr Tasten](images/05-keys-intensity.png)

Die komplette Dokumentation zum Abfragen der Tasten liegt [hier](https://meowbit-doc.kittenbot.cn/#/micropython/reference/%E9%80%9A%E7%94%A8%E6%8C%89%E9%94%AE).

## 05 Töne & Melodien

Für Töne gibt es zwei Blöcke:

![Töne](images/06-sounds.png)

Der erste Block kann einen Ton einer bestimmten Tonhöhe erzeugen. Mit dem zweitren Block lassen sich ganze Melodien abspielen. Die Melodie im Beispiel besteht aus 5 Noten.

Das folgende Beispiel nutzt die Fähigkeit von Scratch 3, Listen zu verwalten, um darin eine Melodie zu speichern:

![Zwei Tiger](images/07-zwei-tiger.png)

Hier sind die Listen auf der Bühne:

![Listen](images/07-zwei-tiger-listen.png)

[Hier](code/07-zwei-tiger.py) ist der erzeugte Python-Code.

Das Lied wird in drei Listen verwaltet:

* _note_ enthält eine Tonleiter
* _song_ speichert die Noten des Liedes als Index der Tonleiter (von 1 an gezählt)
* _beat_ gibt für jede Note die Länge in Millisekunden

Die Dokumentation der Musikfunktionen liegt [hier](https://meowbit-doc.kittenbot.cn/#/micropython/%E8%9C%82%E9%B8%A3%E5%99%A8).

## 08 Bildschirm

Hier sind die Blocke zur Anzeige auf dem Bildschirm:

![Bildschirm](images/08-tft-blocks.png)

Dies sind die Python-Funktionen dazu:

````
import pyb
import framebuf

tft = pyb.SCREEN()
fbuf = bytearray(160*128*2)
fb = framebuf.FrameBuffer(fbuf, 160, 128, framebuf.RGB565)

# Fülle den Bildschirm mit einer Farbe (Hex-Code)
fb.fill(color)

# Zeige einen Bildpunkt bei X und Y kn einer bestimmten Farbe (ein Hex-Wert)
fb.pixel(x, y, color)

# Zeichne eine Linie zwischen dem Startpunkt x1,y1 und x2,y2 in einer bestimmten Farbe (Hex-Code) 
fb.line(x1, y1, x2, y2, color)

# Zeichne ein Rechteck von der Ecke x,y mit Breite w, Höhe h und Farbe color (Hex-Code)
fb.rect(x, y, w, h, color)

# Schreibe den Text "content" ab x,y mit Farbe color
fb.text("content", x, y, color)

# Frische den Bildschirminhalt auf
tft.show(fb)
````

Hier ist ein kleines ["Hallo Welt"-Programm](code/08-hello.py):

![Hallo](images/08-hello.png)

Jetzt noch ein größeres Programm:

Das ist das Ergebnis:

![Ergebnis](images/m5_8.gif)

Die komplette Dokumentation der Framebuffer-Klasse findet sich [hier](https://meowbit-doc.kittenbot.cn/#/micropython/reference/%E9%80%90%E5%B8%A7%E7%BC%93%E5%86%B2). Hier ist eine Zusammenfassung:

* Klasse FrameBuffer (Puffer, Breite, Höhe, Höhe, Format, Schrittweite = Breite)

Methoden auf der FrameBuffer-Klasse:

* fill (Farbe)
* pixel (x, y, Farbe)
* hline (x, y, w, c)
* vline (x, y, h, c)
* line (x1, y1, x2, y2, c)
* rect (x, y, b, h, c)
* fill_rect (x, y, w, h, c)
* text (s, x, y, c)
* loadbmp ('x')
* loadgif ('x', f)
* scroll (xstep, ystep)
* blit (fbuf, x, y, key)

## Kurzdokumentation

Ich habe oben bereits einige Einstiegspunkte in die [Kurzdokumentation](https://meowbit-doc.kittenbot.cn/#/micropython/micropython%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B) für die Pythonprogrammierung des Meowbits genannt. Diese Links führen auf eine chinesische Seite. Es gibt die Dokumentation des Meowbits leider im Augenblick nur so. Die chinesischen Seiten lassen sich allerdings ganz ordentlich über die Übersetzungsfunkton des Chrome-Browsers übersetzen. Hier sind die Abschnitte:

### Grundlagen

* Schnellstart
* LED
* Farbdisplay
* Summer
* Tastenerkennung
* Temperatur- / Lichtsensor
* Gyroskop

### Kurzreferenz

* Universelle Tastenabfrage
* Timing-Sleep verzögern
* Lichtsteuerung-LED
* Pin Control-Pin
* Externer Interrupt-ExtInt
* Zeitsteuerung-Timer
* Pulsweitenmodulation-PWM
* Analog-Digital-Wandler
* Serieller Bus-UART
* Zweidraht-Bus-I2C
* Vierleiter-Bus-SPI
* Framebuf

### Fortgeschritten

* Zeige mehrere Sprachen
* Kreiselwert anzeigen
