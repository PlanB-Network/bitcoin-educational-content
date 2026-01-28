---
name: Canaan Avalon Nano 3S
description: Konfigurieren Ihres ASIC Avalon für Solomining oder Miner-Pooling
---

![cover](assets/cover.webp)



In diesem Tutorial werden wir einen Blick darauf werfen, wie man den Canaan Avalon Nano 3S für die einfache Nutzung des Miner zu Hause einrichtet.



Bislang waren ASIC-Maschinen (*Application Specific Integrated Circuit*), die speziell für eine bestimmte Aufgabe entwickelt wurden - in diesem Fall die Berechnung von Hash (SHA-256) für Miner von Bitcoin - für den Hausgebrauch besonders ungeeignet. Die Lärmbelästigung, die Wärmeentwicklung und die Notwendigkeit, die Elektroinstallation an die enorme Leistung dieser Geräte anzupassen, hielten die meisten von uns davon ab, daran teilzunehmen.



Heute hat Canaan, einer der führenden Hersteller von ASIC-Maschinen, beschlossen, den Markt für Privatpersonen zu erschließen, die Miner zu Hause nutzen wollen, und bietet eine Reihe von Produkten an, die relativ leise und sehr einfach zu installieren sind (Plug & Play).



Diese Geräte werden entweder als Zusatzheizung im Falle des **Avalon Nano 3S (140W)** oder als Mini-Heizkörper mit einer Leistung von **800W** im Falle des **Avalon Mini 3** vermarktet.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

Bitte beachten Sie, dass der Preisunterschied zu herkömmlichen Heizgeräten mit gleicher Leistung in den allermeisten Fällen keinen finanziellen Gewinn ermöglicht. Die durch die Tätigkeit von Mining erzeugten Satoshis werden diesen Preisunterschied niemals ausgleichen, es sei denn, Sie haben Zugang zu kostenlosem (überschüssigem) oder sehr billigem Strom.



Meiner Meinung nach sollten diese Geräte eher als eine einfache Möglichkeit gesehen werden, Miner zu Hause für diejenigen zu nutzen, die dies aus persönlichen Gründen tun möchten: *nicht-KYC-Satss / Lotterie spielen durch Solominating / Teilnahme an der Hashrate Dezentralisierung usw.*., während man **als Bonus** von der erzeugten Wärme profitiert, um sein Zimmer im Winter zu heizen. Aber nicht als Möglichkeit, Geld zu sparen, zumindest in den meisten Fällen (westliche Länder).



## Unboxing und Eigenschaften



Sehen wir uns zunächst an, was sich in der Avalon Nano 3S-Box befindet.



![image](assets/fr/01.webp)




![image](assets/fr/02.webp)



Nach dem Öffnen des Kartons finden Sie eine Papphülse mit einem WIFI-Empfänger, den Sie, wie wir später sehen werden, in den USB-Anschluss des Geräts stecken müssen, damit es sich mit Ihrem lokalen Netzwerk verbinden kann. Ebenfalls enthalten sind die Bedienungsanleitung und ein Metallstift, mit dem Sie das Gerät bei Bedarf auf die Werkseinstellungen zurücksetzen können.



![image](assets/fr/03.webp)




![image](assets/fr/04.webp)



Nach dem Auspacken sind folgende Dinge enthalten: das Gerät selbst, das Benutzerhandbuch, der WIFI-Empfänger, die bereits erwähnte Metallspitze und der Supply-Stromanschluss des Geräts. Die mitgelieferte Kreditkarte ist unserer Meinung nach nicht erwähnenswert.



![image](assets/fr/05.webp)



Nachstehend finden Sie eine Tabelle mit den allgemeinen technischen Daten des Nano 3S:




| Merkmal                                      | Wert                                                  |
| ---------------------------------------------------- | ------------------------------------------------------- |
| Hash-Rate                                      | 6 Th/s +- 5%                                            |
| Stromverbrauch                               | 140 W                                                   |
| Lärm                                                | 30 - 40 dB                                              |
| Bereich der Ausgangslufttemperatur                 | 60-70°C (bei Umgebungstemperatur 25°C)                |
| Umgebungstemperaturanforderungen für den Betrieb | von -5 bis 30°C                                            |
| Eingangsspannungsbereich des Geräts                         | 28V 5A kontinuierlich                                          |
| Eingangsspannungsbereich des Adapters                       | 110-240V AC 50/60Hz                                     |
| Gerätegröße                                 | Länge: 205 mm / Breite: 115 mm / Höhe: 58.5 mm |
| Gerätegewicht                                  | 0.86 kg                                                 |

## Einschalten und Verbinden mit dem lokalen Netzwerk



Stellen Sie Ihren Avalon Nano 3 S nach dem Auspacken möglichst an einen relativ offenen Ort, damit die Wärme zirkulieren kann. Beginnen Sie dann mit dem Einsetzen des kleinen WIFI-Empfängermoduls wie unten gezeigt:



![image](assets/fr/06.webp)


Stecken Sie dann den USB-C-Stecker des Power Supply in den USB-C-Anschluss des Geräts, um es mit Strom zu versorgen.



![image](assets/fr/07.webp)


![image](assets/fr/08.webp)



Das Gerät wird hochgefahren und das Avalon Nano-Logo erscheint auf dem Bildschirm, gefolgt von einem "Handy"-Logo mit den Worten "Bitte konfigurieren Sie das Netzwerk mit der Avalon Family App".



![image](assets/fr/09.webp)




![image](assets/fr/10.webp)



Gehen Sie dazu in den Store für mobile Anwendungen, suchen Sie nach der Anwendung **Avalon Family** und laden Sie sie herunter.



![image](assets/fr/11.webp)


Nach der Installation öffnen Sie es, indem Sie oben rechts auf "Überspringen", dann auf die Schaltfläche "Hinzufügen" und schließlich auf "Suchen" klicken. Stellen Sie sicher, dass Bluetooth auf Ihrem Smartphone aktiviert ist, damit die Erkennung des Geräts reibungslos funktioniert.



![image](assets/fr/12.webp)


Sobald das Gerät von der Anwendung erkannt wurde, klicken Sie es an und wählen Sie "Verbinden". Sie gelangen dann zu einem Bildschirm, auf dem Sie Ihre WIFI-Verbindungsdaten eingeben können.


![image](assets/fr/13.webp)


Sobald das Gerät mit Ihrem lokalen Netzwerk verbunden ist, sieht der Bildschirm wie folgt aus:



![image](assets/fr/14.webp)



Es zeigt einen "fiktiven" Hashrate, da noch kein Pool konfiguriert wurde, und die Uhrzeit, das Datum, die Stromversorgung und die IP Address des Geräts - sehr nützlich, wenn Sie über einen PC und einen Browser auf den Interface des Geräts zugreifen möchten (mehr dazu später).



![image](assets/fr/15.webp)




## Anschließen an einen Mining pool



**Dieser Teil ist für den Nano 3s und den Mini 3 gleich, da die Prozesse absolut identisch sind**.



Ob wir nun "solominieren" oder Miner "poolen" wollen, wir müssen eine Verbindung zu einem Mining pool herstellen. Eigentlich ist unser Gerät nichts anderes als ein Hash-Hersteller, der das Bitcoin-Netz nicht kennt. Wenn wir es an einen Pool anschließen, erhält es Zugang zum Bitcoin-Netz und kann Blockvorlagen zur Bearbeitung erhalten.



### Verwendung der Anwendung zur Verbindung mit einem Mining pool



Wählen Sie in der Anwendung Avalon Family das Gerät wie unten dargestellt aus. Sie werden dann automatisch aufgefordert, das Administrator-Passwort des Geräts zu ändern. Klicken Sie auf "OK", wenn Sie dies tun möchten, oder auf "Abbrechen", wenn Sie das Standardzugangspasswort "admin" beibehalten möchten.


![image](assets/fr/16.webp)


Wählen Sie dann "Einstellungen", dann "Poolkonfiguration" und geben Sie die Parameter für die 3 gewünschten Pools ein.


Die Pools Nr. 2 und Nr. 3 dienen als Backup, falls einer der Pools ausfällt, so dass Ihr Miner nicht umsonst funktioniert. Standardmäßig wird Hashrate auf Pool #1 verwiesen



In unserem Fall wählen wir:




- 1 - Öffentliches Schwimmbad,
- 2 - CkPool,
- 3 - Ozean.



![image](assets/fr/17.webp)



Weitere Einzelheiten zur Verbindung mit einem Mining pool finden Sie in diesen Anleitungen:



https://planb.academy/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

https://planb.academy/tutorials/mining/pool/ocean-pool-30c9e2c9-2364-44a1-bae0-2afbdb8b1c9c

Zusammenfassend brauchen wir





- den Pool Address, normalerweise **stratum+tcp://xxxxxxxx:port**.





- der Name des "Workers", bestehend aus *Ihrem Bitcoin Address* und dem *Pseudo*, das Sie für Ihr Gerät gewählt haben, wobei die beiden durch einen *Punkt* getrennt sind, zum Beispiel:**bc1qxxxxxxxxxxxxxxx.MonAvalonNano3S**





- das Passwort, das normalerweise immer "**x**" lautet



Klicken Sie nach Eingabe der Poolinformationen auf "Speichern".



![image](assets/fr/18.webp)


Starten Sie das Gerät gemäß den Anweisungen neu, und warten Sie einige Minuten, bis Ihr Hashrate auf den bevorzugten Pool (#1) gerichtet ist.



### Verwenden des Browsers zur Verbindung mit einem Mining pool



Sie können auch eine Verbindung zu einem Mining pool herstellen und ganz allgemein über Ihren bevorzugten Browser auf das Interface-Verwaltungssystem Ihres Geräts zugreifen.



Geben Sie dazu in die Suchleiste des Browsers die IP Address des Geräts ein, das auf dem Bildschirm unten angezeigt wird, in unserem Beispiel **192.168.144.6**



![image](assets/fr/15.webp)



Die folgende Seite wird angezeigt, auf der Sie aufgefordert werden, die Avalon Family-Anwendung zu öffnen und den mit der Anwendung angezeigten QR-Code zu scannen.



![image](assets/fr/20.webp)



Öffnen Sie die Anwendung und klicken Sie auf die 3 Striche oben rechts, dann auf Scannen. Scannen Sie den QR-Code des Browsers, geben Sie dann das Administrator-Passwort der Anwendung ein und klicken Sie auf OK.



![image](assets/fr/21.webp)



Hier befinden Sie sich auf der Webseite, die Ihnen die Interaktion mit Ihrem Avalon ermöglicht. Es handelt sich dabei eher um ein Dashboard, das die Metriken des Geräts anzeigt, als um eine Möglichkeit, es zu konfigurieren.



Auf die Pool-Einstellungen kann man aber trotzdem zugreifen, indem man auf **"Pool Config "** in der rechten unteren Ecke klickt.



![image](assets/fr/22.webp)



Genau wie bei der mobilen Anwendung können Sie hier Ihre Poolparameter eingeben.



![image](assets/fr/23.webp)



## Steuern Sie Ihr Gerät über die Avalon Family App



Wir haben nun unseren Miner an unser lokales Netzwerk angeschlossen und unseren Hashrate auf Pools of Minings ausgerichtet. Jetzt wollen wir die wichtigsten Funktionen unseres Geräts mit Hilfe der Avalon Family-Anwendung entdecken.



Klicken Sie in der Avalon-Familienanwendung auf das Symbol für den Avalon Nano 3S.


werden Ihnen 3 Menüs angezeigt: "Arbeitsmodus", "Lichtsteuerung" und "Einstellungen". Klicken Sie zunächst auf "Arbeitsmodus". Es werden Ihnen dann 3 Leistungsmodi für Ihr Gerät angeboten.



**Low**: bringt Ihnen ca. 3 Th/s Hashrate bei 70 W Stromverbrauch


**Medium**: bringt Ihnen ca. 4,5 Th/s Hashrate für 100W Stromverbrauch


**Hoch**: ergibt etwa 6 Th/s Hashrate bei einem maximalen Verbrauch von 140 W



![image](assets/fr/31.webp)


Gehen wir einen Schritt zurück und erkunden das Menü "Lichtsteuerung". Dies ist rein kosmetisch. Es gibt eine ganze Reihe von Optionen, mit denen Sie die Farbe, die Intensität, die Wärme, das Ausschalten der LEDs des Geräts bei Nacht usw. einstellen können. Das können Sie ganz einfach selbst herausfinden.



![image](assets/fr/32.webp)


![image](assets/fr/33.webp)



![image](assets/fr/34.webp)



Das letzte Menü, das uns zur Verfügung steht, ist das Menü "Einstellungen", das wir bereits für die Verbindung mit unseren Mining-Pools gesehen haben. Hier können Sie Ihre Pools verwalten, das Administrator-Passwort des Geräts ändern und verschiedene Metriken wie das Ablaufdatum der Garantie, die Sauberkeit des Filters oder die Kontaktaufnahme mit dem Support im Falle einer Störung beobachten.



![image](assets/fr/35.webp)


Zur Wartung und um den Filter so sauber wie möglich zu halten, empfehlen wir, einen Staubsauger zu verwenden und die Luftein- und -auslässe regelmäßig abzusaugen, um Verstopfungen zu vermeiden.



Wir sind am Ende dieses Tutorials angelangt, in dem wir gelernt haben, wie wir unser Avalon Nano 3 S mit unserem lokalen Netzwerk verbinden, wie wir unser Hashrate auf Mining-Pools ausrichten und wie wir mit der Avalon Family-Anwendung durch die Optionen und Einstellungen navigieren.



Weitere Informationen finden Sie in unserem Tutorial über die bessere Version des Avalon: den Mini 3.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7