---
name: Lightning Smoke Machine
description: Lösen Sie eine Rauchmaschine mit einer Lightning-Zahlung über ESP32 aus.
---

![cover-lightning-smoke-machine](assets/cover.webp)



## Einführung



Verwandelt eine klassische Nebelmaschine in ein Gerät, das in Bitcoin über Lightning Network bezahlt werden kann. Jede Zahlung löst automatisch einen Rauchstrahl aus!





- Niveau: Fortgeschrittene
- Geschätzte Zeit: 2-3 Stunden
- Anwendungsfälle: Bitcoin-Veranstaltungen, künstlerische Darbietungen, Lightning-Demos, automatisierte Bühneneffekte



## Voraussetzungen



### Wissen





 - Grundlegende Elektronik (Verdrahtung, Relais)
 - Schweißen (oder Verwendung von Dupont-Verbindern)
 - Netzwerkkonfiguration (WiFi, WebSocket)



### Erforderliche Konten





- BTCPay-Server: Funktionsfähige Instanz (selbstgehostet oder gehostet)
- Blink Wallet : Konto + Zugang API



### Zugang





- Admin-Zugang zum BTCPay Server
- WiFi-Verbindung für ESP32



## Erforderliche Materialien



### Hardware - Elektronische Komponenten





- 1 Mikrocontroller - ESP32-WROOM-32


*Der ESP32-WROOM-32 ist ein kompakter, preiswerter WiFi/Bluetooth-Mikrocontroller für die Verbindung elektronischer Geräte mit dem Internet und deren Fernsteuerung*



![ESP32](assets/fr/1.webp)





- 1 Relaismodul - 5V mit Optokoppler


*Ein Relais ist wie ein Schalter, den der ESP32 betätigen kann, um die Nebelmaschine ein- oder auszuschalten*



![relay](assets/fr/2.webp)





- ~10 Dupont-Kabel - Stecker/Stecker und Stecker/Buchse



![dupont-cables](assets/fr/3.webp)





- 1 Spannungsversorgung für ESP32 - 5V USB oder Li-Po-Akku



![battery](assets/fr/4.webp)





- 1 Micro-USB-Kabel - Verbindung zwischen ESP32 und Netzteil



![micro-usb-cables](assets/fr/5.webp)





- 1 220V-Nebelmaschine mit 12V-Batterie-Fernbedienung



![remote-and-smoke-machine](assets/fr/6.webp)





- 1 Flasche mit Flüssigkeit, die mit Ihrer Nebelmaschine kompatibel ist



### Hardware - Werkzeuge





- Lötkolben + Zinn (beim Löten)
- Schraubenzieher
- Multimeter (empfohlen)



### Software





- Firmware BitcoinSwitch : **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- WebSerial-kompatibler Webbrowser (Chrome/Edge/Brave)
- BTCPay Server konfiguriert. Weitere Informationen zur Erstellung einer BTCPay Server-Instanz finden Sie in diesem Tutorial: https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc



## Systemarchitektur



![architecture-lightning-smoke-machine](assets/fr/7.webp)



---


**⚠️** **SICHERHEITSWARNUNG - VOR DEM WEITERLESEN LESEN** **⚠️**



Bei diesem Projekt wird eine Nebelmaschine an eine **220V-Netzversorgung** angeschlossen. Unsachgemäßer Betrieb kann zu **tödlichem Stromschlag** oder **Brand** führen.



**Nicht verhandelbare Regeln:**



1. **Trennen Sie die Nebelmaschine IMMER vom Netz**, bevor Sie die Fernbedienung öffnen oder an der Verkabelung herumhantieren


2. **Entnehmen Sie die Batterie aus der Fernbedienung**, bevor Sie sie anfassen (Gefahr eines Kurzschlusses und der Beschädigung von Bauteilen)


3. **Vergewissern Sie sich, dass alle Ihre Verbindungen isoliert sind, bevor Sie etwas wieder anschließen


4. **Schließen Sie die 220V** erst wieder an, wenn der Fernbedienungskasten geschlossen und gesichert ist



Wenn Sie sich mit dieser Art der Handhabung nicht auskennen, nehmen Sie jemanden mit, der sich damit auskennt.



---

## TEIL 1: Montage der Hardware



### Schritt 1: Vorbereiten der Fernbedienung



Zielsetzung: Verbinden Sie das Relais mit der ON/OFF-Taste der Fernsteuerung


1. Fernsteuerung öffnen




    - Identifizieren Sie die Taste ON/OFF
    - Schrauben Sie das Gehäuse ab, um die Fernbedienung zu öffnen


2. Verbindungen lokalisieren




 - Suchen Sie die + und - Klemmen des
 - Durchgangsprüfung mit einem Multimeter (optional)



![smoke-machine-remote](assets/fr/8.webp)



3. Verdrahtung der Tasten (Lötzinn oder Stecker)




    - Löten Sie ein schwarzes Kabel an die - Klemme der Taste
    - Löten Sie ein rotes Kabel an die gemeinsame + Klemme



![smoke-machine-remote](assets/fr/9.webp)



### Schritt 2: Anschließen an das Relaismodul



**Erinnerung: Terminologie der Relais



| **Terminal**         | **Description**           | **Fonction**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (Normally Open)   | Circuit ouvert par défaut | Se ferme quand le relais est activé |
| NC (Normally Closed) | Circuit fermé par défaut  | S'ouvre quand le relais est activé  |
| COM (Common)         | Terminal central          | Bascule entre NO et NC              |

**Verkabelung von der Fernbedienung zum Relaismodul:**




- Schwarzes Kabel von der ON/OFF-Taste **→** NO (Normalerweise offen)
- Rotes Kabel (gemeinsam) **→** COM (gemeinsam)



**Logik:**


Wenn der ESP32 das Relais aktiviert, verbindet er COM und NO, was genau dasselbe ist wie das Drücken der Fernbedienungstaste.


Wenn der ESP32 das Relais abschaltet, trennen sich COM und NO, was dem Loslassen der Taste entspricht.



![remote-relay](assets/fr/10.webp)



### Schritt 3: Anschließen des ESP32 an das Relaismodul



**Schaltplan:**



| **ESP32** | **→** | **Module relais** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (Input)        |

**Verifizierung:**




- VCC und GND gut verbunden (Polarität)
- GPIO 21 wird für Steuersignale verwendet
- Kein sichtbarer Kurzschluss



![relay-esp32](assets/fr/11.webp)



**Checkpoint Hardware**


Prüfen Sie vor dem Wechsel zur Software :




- Korrekt verdrahtete Fernbedienung
- Relaismodul angeschlossen an ESP32
- Keine blanken Drähte, die andere Komponenten berühren
- 220V immer abgeschaltet



![relay-esp32](assets/fr/12.webp)





---


## TEIL 2: Software-Konfiguration



Wir verwenden *Blink* als Beispiel, aber *BTCPay Server* bietet auch *Strike, Breez und Boltz*, wenn Sie eine andere Option bevorzugen.



### Schritt 1: Plugins, Installation *BitcoinSwitch* + *Blink



1 - Gehen Sie zu Ihrer *BTCPay Server* Instanz mit einem Admin-Konto



2 - Erstellen Sie Ihr erstes Rollo



3 - Scrollen Sie auf der linken Seite von *BTCPay Server* ganz nach unten und gehen Sie auf *"Manage Plugins "*



![btcpay-plugins](assets/fr/13.webp)



4 - Wir werden die Plugins *BitcoinSwitch* und *Blink* installieren



![btcpay-plugins](assets/fr/14.webp)



5 - Scrollen Sie in der Liste der Plugins nach unten und klicken Sie auf *"Installieren "* : *BitcoinSwitch und Blink* (oder das verfügbare wallet Ihrer Wahl)



![btcpay-plugins](assets/fr/15.webp)



6 - Sobald die Installation abgeschlossen ist, starten Sie *BTCPay Server* neu und warten Sie 1 Minute, bis die Instanz neu gestartet ist



![btcpay-plugins](assets/fr/16.webp)



7 - Wenn Sie zu *"Plugins verwalten "* zurückkehren, überprüfen Sie, ob beide Plugins installiert wurden



![btcpay-plugins](assets/fr/17.webp)



### Schritt 2: Backend: *BTCPay Server + Blink* Konfiguration



**1 - Erstellen eines wallet *Blink***




- Besuchen Sie https://www.blink.sv
- Erstellen Sie Ihr Konto. Bitte beachten Sie die Anleitung :



[https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)



**2 - Erzeugen eines API-Schlüssels *Blink***




- Greifen Sie auf die API-Schnittstelle zu: **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** und melden Sie sich mit demselben Konto an, das Sie zur Erstellung Ihres wallet verwendet haben *Blink*



![blink-api](assets/fr/18.webp)





   - Sobald die Verbindung hergestellt ist, gehen Sie auf die Registerkarte *API Keys*



![blink-api](assets/fr/19.webp)





   - Klicken Sie auf *" + "* in der oberen rechten Ecke, um auf die Konfiguration Ihres API-Schlüssels zuzugreifen



![blink-api](assets/fr/20.webp)





   - Geben Sie Ihrem API-Schlüssel einen Namen und belassen Sie die Standardeinstellungen. Notieren Sie dann im dritten Schritt Ihren API-Schlüssel - Sie werden ihn nur einmal sehen: `blink_mZ5KxxxxxxxxxxxxxNbmX`



![blink-api](assets/fr/21.webp)





   - Sobald er erstellt ist, sollte er in der Liste der aktiven API-Schlüssel erscheinen.



![blink-api](assets/fr/22.webp)



**3 - Verbinden Sie *Blink* mit *BTCPay Server***




- Öffnen Sie Ihren *BTCPay Server*
- Navigieren Sie zu: *Wallet* **→** *Blitz*



![btcpay-server](assets/fr/23.webp)





- Klicken Sie auf *Einen benutzerdefinierten Knoten verwenden*
- Fügen Sie die folgende Verbindungszeichenfolge ein:



```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```



**⚠️** **Wichtig** :




- Der erste Teil darf nicht geändert werden: `type=blink;server=https://api.blink.sv/graphql`;
- Nur austauschen:
    - api-key= *mit Ihrem API Blink* Schlüssel
    - wallet-id= *mit Ihrer wallet Blink* ID
- Klicken Sie dann auf *Verbindung testen*, dann *Speichern*



![btcpay-server](assets/fr/24.webp)





 - Prüfen Sie, ob die Verbindung hergestellt ist (grüner Status)



![btcpay-server](assets/fr/25.webp)



**4 - Erstellen eines Point of Sale (PoS)**




- Gehen Sie in BTCPay Server auf die Registerkarte *Plugins* und klicken Sie auf *Verkaufsstelle*



![btcpay-server](assets/fr/26.webp)





- Geben Sie Ihrem PoS einen Namen und klicken Sie auf *Erstellen*



![btcpay-server](assets/fr/27.webp)





- PoS-Konfiguration :
    - Wählen Sie einen Verkaufsstellenstil = *Druckanzeige*
    - Währung = *SATS*
    - Klicken Sie auf *SPEICHERN*



![btcpay-server](assets/fr/28.webp)





- Produktkonfiguration :
    - Alle Standardprodukte löschen
    - Dann klicken Sie auf *Eintrag hinzufügen*



![btcpay-server](assets/fr/29.webp)



![btcpay-server](assets/fr/30.webp)





- Konfigurieren Sie das Produkt:
    - Titel : *rauch-Maschine*
    - Preis : *10 sats*
    - Bitcoin GPIO-Schalter : 21
    - Bitcoin Schaltdauer (in Millisekunden) : 5000
    - Klicken Sie auf *Schließen* und dann auf *Speichern*, um das neue Produkt zu speichern



![btcpay-server](assets/fr/31.webp)



### Schritt 3: Firmware: Flashen des ESP32



**1 - Zur Flash-Seite gehen




- Gehe zu : [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)



![bitcoinswitch-lnbits](assets/fr/32.webp)



**2 - Flash die BitcoinSwitch-Firmware**




- Verbinden Sie den ESP32 über das USB/Micro-USB-Kabel mit Ihrem Computer
- Klicken Sie dann auf *Verbinden mit Gerät*
- Ein Fenster öffnet sich, wählen Sie den USB-Anschluss an Ihrem ESP32 und klicken Sie auf *Verbinden*



![bitcoinswitch-lnbits](assets/fr/33.webp)





- Sobald Ihr ESP32 angeschlossen ist, werden wir die BitcoinSwitch-Firmware flashen. Im Abschnitt *T-Display* klicken Sie auf *Firmware hochladen* für die neueste verfügbare Version (derzeit: *bitcoinSwitch T-Display v1.0.1*)



![bitcoinswitch-lnbits](assets/fr/34.webp)





- Warten Sie den Upload ab. Der Vorgang ist abgeschlossen, wenn in den Protokollen *"Leaving... "*


![bitcoinswitch-lnbits](assets/fr/35.webp)





- Trennen Sie den ESP32 vom Stromnetz



**3 - BitcoinSwitch-Firmware-Installation überprüfen




- Seite neu laden: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Schließen Sie den ESP32 mit dem USB/Micro-USB-Kabel wieder an Ihren Computer an
- Klicken Sie dann auf *Verbinden mit Gerät
- Wählen Sie den USB-Anschluss Ihres ESP32 und klicken Sie dann auf *Verbinden* wie oben beschrieben
- Sobald die Verbindung hergestellt ist, drücken Sie die **RESET**-Taste am ESP32
- Prüfen Sie in den Protokollen, ob in den letzten Zeilen :



```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```



(Dies ist normal, es bedeutet, dass noch keine Konfiguration vorhanden ist, aber die Firmware installiert wurde)



![bitcoinswitch-lnbits](assets/fr/36.webp)



**4 - WebSocket LNURL** URL generieren



Erwartetes Endformat :



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



Erzeugungsschritte :




- Öffnen Sie IhreBTCPay Server-Instanz und gehen Sie dann zu dem PoS, den wir später erstellt haben.
- Klicken Sie dann auf "Ansicht", um Ihr PoS im Browser zu öffnen



![btcpay-server-https](assets/fr/37.webp)





- Kopieren Sie die URL der Seite, z. B. :



![btcpay-server-https](assets/fr/38.webp)



Lassen Sie uns diese URL auspacken:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```





- `XXXXv` → die Domäne Ihrer BTCPay-Server-Instanz
- 46XXXXXXXXXXXXXXXXXXXXXXwFB" → Ihr eindeutiger PoS-Bezeichner
- `/pos` → bezeichnet eine Verkaufsstelle



Verwandeln Sie es:




- Ersetzen Sie "https://" durch "wss://"
- Am Ende `/bitcoinswitch` hinzufügen



Ergebnis:



```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```



Bewahren Sie diese URL für zukünftige Konfigurationen auf, da sie es Ihrem ESP32 ermöglicht, in Echtzeit mit dem BTCPay-Server zu kommunizieren. Das WebSocket-Protokoll (`wss://`) stellt eine permanente Verbindung zwischen den beiden her: Sobald eine Lightning-Zahlung an Ihrem PoS bestätigt wird, sendet BTCPay die Informationen sofort an den ESP32, der dann Ihre Nebelmaschine auslösen kann.



**5 - WiFi und WebSocket konfigurieren




- Zurück zur Seite: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/) mit Ihrem angeschlossenen ESP32
- Gehen Sie zu *Gerät konfigurieren* → *WLAN-Einstellungen*



Informieren :




- WiFi SSID: der Name Ihres WiFi-Netzwerks
- WiFi-Passwort: Ihr WiFi-Passwort



![bitcoinswitch-lnbits](assets/fr/39.webp)





- Fügen Sie im Abschnitt *LNbits Device URL* die im vorherigen Schritt erstellte WebSocket-URL ein
- Klicken Sie auf *Konfiguration hochladen*



![bitcoinswitch-lnbits](assets/fr/40.webp)





- Warten Sie, bis der Upload abgeschlossen ist. In den Protokollen sollten die soeben eingegebenen Parameter (SSID, Passwort und WebSocket-URL) angezeigt werden



![bitcoinswitch-lnbits](assets/fr/41.webp)





- Warten Sie, während ESP32 die WebSocket-Verbindung herstellt. Sie sollten sehen:



```
WiFi connection established!

[WebSocket] Connected to url: ...
```



![bitcoinswitch-lnbits](assets/fr/42.webp)





- Sie können nun den ESP32 abtrennen



---
## Checkpoint-Software



Prüfen Sie vor der abschließenden Prüfung :





- Blink verbunden mit BTCPay
- PoS erstellt mit mindestens 1 Artikel
- ESP32 geflasht mit BitcoinSwitch
- WiFi auf ESP32 konfiguriert
- WebSocket-URL korrekt
- Fehlerfreie ESP32-Protokolle



---

## Prüfung und Fehlerbehebung



### Abschließende Prüfung



1. Schließen Sie die Nebelmaschine (220 V) an und schalten Sie sie ein


2. Stromversorgung des ESP32 (Batterie oder USB)


3. Öffnen Sie Ihren BTCPay PoS in Ihrem Browser


4. Artikel "Nebelmaschine" scannen


5. Bezahlen mit einem wallet Lightning (Blink oder einem anderen wallet)


6. Beachten Sie:




 - Relais klickt (hörbarer Ton und Relais-LED leuchtet)
 - Die Nebelmaschine wird aktiviert
 - Rauch erzeugt!



### Fairnessprobleme und Lösungen



| **Problème**                        | **Cause probable**              | **Solution**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 ne se connecte pas            | Driver USB manquant             | Installer [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| Relais ne clique pas                | Mauvais câblage GPIO            | Vérifier GPIO 21 → IN                                                                        |
| Smoke machine ne réagit pas         | Télécommande mal câblée         | Vérifier NO/NC/COM                                                                           |
| WebSocket timeout                   | URL incorrecte                  | Vérifier wss:// et /bitcoinswitch                                                            |
| WiFi ne se connecte pas             | SSID/Password erroné            | Re-flasher la config WiFi                                                                    |
| Paiement reçu mais rien ne se passe | ESP32 non connecté au WebSocket | Vérifier les logs RESET                                                                      |

## Ressourcen



### Nützliche Links





- BitcoinSwitch Firmware: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- BTCPay Server Docs : [https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- ESP32 Pinbelegung : [https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)



### Gemeinschaft & Unterstützung





- BTCPay Server** : [chat.btcpayserver.org](https://chat.btcpayserver.org/) - Offizieller Mattermost
- BTCPay Server Telegram** : [t.me/btcpayserver](https://t.me/btcpayserver)
- LNbits** : [t.me/lnbits](https://t.me/lnbits) - Offizieller Telegram, aktive Gemeinschaft
- BitcoinSwitch (Firmware-Fehler)**: [github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)



### Quellcode





- BitcoinSwitch-Firmware-Quellcode: [https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)



---

**⚡** sats stapeln, Rauch machen, Spaß haben, bescheiden bleiben! **⚡**