---
name: Canaan Avalon Mini 3
description: Konfigurieren Ihres ASIC Avalon für Solomining oder Miner-Pooling
---

![cover](assets/cover.webp)



In dieser Anleitung sehen wir uns an, wie man den Canaan Avalon Mini 3 für die einfache Nutzung des Miner zu Hause einrichtet.



Bislang waren ASIC-Maschinen (*Application Specific Integrated Circuit*), die speziell für eine bestimmte Aufgabe entwickelt wurden - in diesem Fall die Berechnung von Hash (SHA-256) für Miner von Bitcoin - für den Hausgebrauch besonders ungeeignet. Die Lärmbelästigung, die Wärmeentwicklung und die Notwendigkeit, die Elektroinstallation an die enorme Leistung dieser Geräte anzupassen, hielten die meisten von uns davon ab, daran teilzunehmen.



Heute hat Canaan, einer der führenden Hersteller von ASIC-Maschinen, beschlossen, den Markt für Privatpersonen zu erschließen, die Miner zu Hause nutzen wollen, und bietet eine Reihe von Produkten an, die relativ leise und sehr einfach zu installieren sind (Plug & Play).



Diese Geräte werden entweder als Zusatzheizung im Falle des **Avalon Nano 3S (140W)** oder als Mini-Heizkörper mit einer Leistung von **800W** im Falle des **Avalon Mini 3** vermarktet.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

Bitte beachten Sie, dass der Preisunterschied zu herkömmlichen Heizgeräten mit gleicher Leistung in den allermeisten Fällen keinen finanziellen Gewinn ermöglicht. Die durch die Tätigkeit von Mining erzeugten Satoshis werden diesen Preisunterschied niemals ausgleichen, es sei denn, Sie haben Zugang zu kostenlosem (überschüssigem) oder sehr billigem Strom.



Meiner Meinung nach sollten diese Geräte eher als eine einfache Möglichkeit gesehen werden, Miner zu Hause für diejenigen zu nutzen, die dies aus persönlichen Gründen tun möchten: *nicht-KYC-Satss / Lotterie spielen durch Solominating / Teilnahme an der Hashrate Dezentralisierung usw.*., während man **als Bonus** von der erzeugten Wärme profitiert, um sein Zimmer im Winter zu heizen. Aber nicht als Möglichkeit, Geld zu sparen, zumindest in den meisten Fällen (westliche Länder).



## Unboxing und Eigenschaften



### Avalon Nano 3S



Schauen wir uns zunächst an, was sich in der Schachtel des Avalon Mini 3 befindet.



![image](assets/fr/24.webp)



Wenn Sie die Schachtel öffnen, liegt die Bedienungsanleitung direkt vor Ihnen, aber noch wichtiger ist, dass sich das WIFI-Empfängermodul unter dem runden weißen Aufkleber links neben der Bedienungsanleitung verbirgt. Sie werden es später brauchen.



![image](assets/fr/25.webp)



Unter dem Schaumstoffblock befindet sich das Gerät, und sobald es aus dem Karton entfernt ist, die Supply-Einheit.



![image](assets/fr/26.webp)




![image](assets/fr/27.webp)



## Einschalten und Verbinden mit dem lokalen Netzwerk



Stellen Sie Ihren Avalon Mini 3 nach dem Auspacken möglichst an einen relativ offenen Ort, damit die Wärme gut zirkulieren kann. Beginnen Sie dann damit, das kleine WIFI-Empfängermodul in den USB-Anschluss an der Unterseite des Geräts zu stecken, den Strom Supply einzustecken und sicherzustellen, dass der Netzschalter auf Position "1" steht.



![image](assets/fr/28.webp)



Sobald diese Schritte abgeschlossen sind, leuchtet die LED-Anzeige des Geräts auf und zeigt das "Bluetooth"-Symbol an, was bedeutet, dass das Gerät bereit ist, über die Avalon Family-Anwendung mit Ihrem lokalen Netzwerk verbunden zu werden.



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



Gehen Sie dazu in den Store für mobile Anwendungen, suchen Sie nach der Anwendung **Avalon Family** und laden Sie sie herunter.



![image](assets/fr/11.webp)


Nach der Installation öffnen Sie es, indem Sie oben rechts auf "Überspringen", dann auf die Schaltfläche "Hinzufügen" und schließlich auf "Suchen" klicken. Stellen Sie sicher, dass Bluetooth auf Ihrem Smartphone aktiviert ist, damit die Erkennung des Geräts reibungslos funktioniert.



![image](assets/fr/12.webp)


Sobald das Gerät von der Anwendung erkannt wurde, klicken Sie es an und wählen Sie "Verbinden". Sie gelangen dann zu einem Bildschirm, auf dem Sie Ihre WIFI-Verbindungsdaten eingeben können.


![image](assets/fr/13.webp)


Sobald eine Verbindung zu Ihrem lokalen Netzwerk besteht, zeigt Ihr Mini 3 Informationen wie IP Address, Uhrzeit, Hashrate und Stromverbrauch an.



Nachstehend finden Sie eine Übersichtstabelle mit den allgemeinen technischen Daten des Mini 3:



| Caractéristique                                      | Valeur                                                    |
| ---------------------------------------------------- | --------------------------------------------------------- |
| Hashrate                                             | 37.5 Th/s +- 5%                                           |
| Consommation électrique                              | 800 W                                                     |
| Bruit                                                | 35-55 dB                                                  |
| Température de l'air en sortie                       | 60-70°C (sous température ambiante 25°C)                  |
| Exigences de température ambiante pour l'utilisation | -5° C - 40°C                                              |
| Plage d'entrée de l'appareil                         | 110V-240V AC 50/60Hz                                      |
| Taille de la machine                                 | Longueur: 760 mm / Profondeur: 104 mm / Hauteur: 214.5 mm |
| Poids de la machine                                  |  8.35 kg                                                  |

## Anschließen an einen Mining pool



**Dieser Teil ist für die Nano 3s und Mini 3 Geräte gleich, da die Prozesse absolut identisch sind **



Ob wir nun "solominieren" oder Miner "poolen" wollen, wir müssen eine Verbindung zu einem Mining pool herstellen. Eigentlich ist unser Gerät nichts anderes als ein Hash-Hersteller, der das Bitcoin-Netz nicht kennt. Durch den Anschluss an einen Pool erhält es Zugang zum Bitcoin-Netz und kann Blockvorlagen erhalten, die es bearbeiten kann.



### Verwendung der Anwendung zur Verbindung mit einem Mining pool



Wählen Sie in der Anwendung Avalon Family das Gerät wie unten dargestellt aus. Sie werden dann automatisch aufgefordert, das Administrator-Passwort des Geräts zu ändern. Klicken Sie auf "OK", wenn Sie dies tun möchten, oder auf "Abbrechen", wenn Sie das Standardzugangspasswort "admin" beibehalten möchten.


![image](assets/fr/16.webp)


Wählen Sie dann "Einstellungen", dann "Poolkonfiguration" und geben Sie die Parameter für die 3 gewünschten Pools ein.


Die Pools Nr. 2 und Nr. 3 dienen als Backup für den Fall, dass einer von ihnen ausfällt, so dass Ihr Miner nicht umsonst funktioniert. Standardmäßig wird Hashrate auf Pool #1 verwiesen



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





- den Namen des "Workers", bestehend aus *Ihrem Bitcoin Address* und dem *Pseudo*, das Sie für Ihr Gerät gewählt haben, wobei die beiden durch einen *Punkt* getrennt sind, zum Beispiel:**bc1qxxxxxxxxxxxxxxx.MonAvalonNano3S**





- das Passwort, das normalerweise immer "**x**" lautet



Wenn Sie die Pool-Informationen eingegeben haben, klicken Sie auf "Speichern".



![image](assets/fr/18.webp)


Starten Sie das Gerät gemäß den Anweisungen neu, und warten Sie einige Minuten, bis Ihr Hashrate auf den bevorzugten Pool (#1) ausgerichtet ist.



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



Klicken Sie im Hauptmenü der Avalon-Familienanwendung auf das entsprechende Symbol für den Avalon Mini 3. Sie gelangen direkt in das Menü zur Verwaltung der Betriebsarten.



es stehen 3 Optionen zur Verfügung: modus "Heizen", Modus "Mining" oder Modus "Nacht".





- Im Modus "Heizung" stehen Ihnen 2 Leistungsstufen zur Verfügung: "Eco" und "Super".


Die Stufe "Eco" entspricht einer Heizleistung von 500 W bei einem Hashrate von etwa 25 Th/s und 40 dB für den Schallpegel.


Die Stufe "Super" entspricht einer Ausgangsleistung von 650 W bei ca. 30Th/s und 45 dB. In diesem Modus können Sie eine maximale Umgebungstemperatur einstellen, ab der das Gerät nicht mehr funktioniert.



![image](assets/fr/36.webp)




- Im Modus "Mining" arbeitet das Gerät mit maximaler Geschwindigkeit, ohne die Möglichkeit, eine Zieltemperatur einzustellen (abgesehen von der eingebauten Überhitzungsgrenze natürlich). Ziel ist es, die Leistung des Miner voll auszuschöpfen. In diesem Modus erreicht die Ausgangsleistung 800 W bei etwa 37,5 Th/s und einem Geräuschpegel von 50-55 dB.



![image](assets/fr/37.webp)


Im "Night"-Modus schließlich arbeitet Ihr Mini 3 mit der geringstmöglichen Geschwindigkeit bei minimalem Lärm. 400 W, 20 Th/s und ca. 33 dB.



Auch hier können Sie eine Zieltemperatur einstellen, bei deren Überschreitung das Gerät in den inaktiven Modus wechselt und Miner stoppt. Wenn die Temperatur sinkt, startet das Gerät neu und nimmt die Heizung und Miner wieder auf. In diesem Modus sind die Display-LEDs standardmäßig ausgeschaltet, aber Sie können sie bei Bedarf einschalten, um den Raum im Dunkeln zu beleuchten, wie ein Nachtlicht (siehe Foto unten).



![image](assets/fr/38.webp)



![image](assets/fr/39.webp)



Schließlich können Sie über das Menü "Display" mit den LEDs Ihres Avalon spielen. Sie können wählen, ob Sie durch die relevanten Betriebsinformationen blättern, die Uhrzeit oder sogar ein benutzerdefiniertes (verpixeltes) Bild anzeigen möchten.



![image](assets/fr/40.webp)



![image](assets/fr/41.webp)



Wie beim Avalon Nano 3S können Sie über das Menü "Einstellungen" das Administrator-Passwort und die Pool-Einstellungen ändern, die Filterverstopfung (an der Unterseite des Geräts) überprüfen, den Support kontaktieren oder die Geräteprotokolle einsehen.



![image](assets/fr/42.webp)



Auch hier kann der Filter an der Unterseite des Geräts mit einem Staubsauger gereinigt werden, je regelmäßiger, desto besser.



Wir sind am Ende dieses Tutorials angelangt, in dem wir gelernt haben, wie wir unser Avalon Mini 3 mit unserem lokalen Netzwerk verbinden, wie wir unser Hashrate auf Mining-Pools ausrichten und wie wir mit der Avalon Family-Anwendung durch die Optionen und Einstellungen navigieren.



Weitere Informationen finden Sie in unserem Tutorial über die kleinere Version des Avalon: den Nano 3S.



https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6