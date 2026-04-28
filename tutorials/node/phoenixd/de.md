---
name: Phoenixd
description: Stellen Sie Ihren eigenen minimalistischen Lightning-Knoten mit Phoenixd bereit
---

![cover](assets/cover.webp)



Finanzielle Autonomie bedeutet auch die Kontrolle über Ihre Lightning-Infrastruktur. Für Entwickler und Unternehmen, die Bitcoin Lightning in ihre Anwendungen integrieren möchten, stellt **Phoenixd** die ideale Lösung dar: ein minimalistischer, spezialisierter Lightning-Knoten mit automatischem Liquiditätsmanagement.



Phoenixd ist ein von ACINQ entwickelter Lightning-Server, der speziell für das Senden und Empfangen von Lightning-Zahlungen über eine HTTP-API konzipiert wurde. Im Gegensatz zu Implementierungen mit vollem Funktionsumfang, wie LND oder Core Lightning, abstrahiert Phoenixd die gesamte Komplexität der Kanalverwaltung und bewahrt gleichzeitig den Selbstschutz Ihrer Mittel.



In diesem Tutorial zeigen wir Ihnen, wie Sie Phoenixd installieren, konfigurieren und verwenden, um Lightning-Anwendungen mit einer selbst gehosteten Infrastruktur und einer einfach zu verwendenden API zu entwickeln.



## Was ist Phoenixd?



Phoenixd ist ein minimaler, spezialisierter Lightning-Knoten, der von ACINQ entwickelt wurde. Es ist eine Lösung für Entwickler und Unternehmen, die Lightning in ihre Anwendungen integrieren möchten, ohne die Verwaltungskomplexität eines Full node.



### Funktionsprinzip



**Phönixd ist ein minimaler Lightning-Knoten, der ACINQ als LSP (Lightning Service Provider) für automatische Liquidität nutzt. Wenn Sie Lightning-Zahlungen erhalten, öffnet er automatisch Kanäle mit ACINQ-Knoten, um die erforderliche eingehende Kapazität zuzuweisen. Diese "on-the-fly"-Liquidität ist sofort verfügbar, wird aber mit genau **1% + Mining-Gebühren** des empfangenen Betrags berechnet.



**Automatisierte Verwaltung:** Das System verwaltet drei wichtige Elements:




- Lightning**-Kanäle: Öffnen, schließen und verwalten Sie automatisch nach Bedarf
- Eingehende/ausgehende Liquidität**: Automatische Bereitstellung über Spleißen und Kanalöffnung
- Gebührenguthaben** : Kleine Zahlungen, die nicht ausreichen, um einen Kanal zu rechtfertigen, werden als Rückstellung für zukünftige Gebühren gespeichert



### Vorteile von Phoenixd



**Sie kontrollieren Ihre privaten Schlüssel (12-Wort-seed) und Ihr Guthaben. Phoenixd generiert Ihre Wallet lokal, ohne jemals Ihre Schlüssel zu teilen.



**Persönliche Infrastruktur:** Phoenixd läuft auf Ihrem Server, so dass Sie Zugriff auf detaillierte Protokolle, Konfiguration und API-Kontrolle haben. Sie sind für den Zugriff auf Ihre Gelder nicht mehr von einem Drittanbieterdienst abhängig.



**Integrierte API:** Phoenixd verfügt über eine HTTP-API für die Integration mit anderen Diensten, nativer LNURL-Unterstützung und benutzerdefinierter Anwendungsentwicklung.



**Einfache Integration:** Dank seiner einfachen REST-API kann Phoenixd in jede Anwendung oder jeden Dienst, der Lightning-Zahlungen erfordert, integriert werden.



**Wichtiger Hinweis:** Die automatische Liquidität kommt weiterhin von ACINQ als LSP (Lightning Service Provider). Phoenixd verwendet denselben Mechanismus wie Phoenix mobile für die automatische Kanalverwaltung.



## Installation von Phoenixd



### Voraussetzungen



Phoenixd erfordert eine Linux-Umgebung (Ubuntu/Debian empfohlen), mit einigen grundlegenden Kommandozeilen-Kenntnissen. Für optimale Leistung benötigen Sie :





- Linux-Server**: VPS oder lokaler Rechner mit stabiler Verbindung
- OpenJDK 21** : Java-Laufzeitumgebung
- Stabile Internetverbindung**: Für die Synchronisierung mit dem Lightning Network
- Domänenname** (optional) : Für sicheren HTTPS-Zugang zur API



### Herunterladen und Installieren



**1. Phoenixd** herunterladen



Gehen Sie auf die Seite [GitHub releases](https://github.com/ACINQ/phoenixd/releases) und laden Sie die neueste Version für Ihre Architektur herunter:



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2. Erste Inbetriebnahme



Starten Sie Phoenixd zur Initialisierung:



```bash
./phoenixd
```



Beim ersten Start werden Sie aufgefordert, zwei wichtige Schritte zu bestätigen, indem Sie "Ich habe verstanden" eingeben:



**Meldung 1 - Sicherung:**


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**Speichern Sie diese 12 Worte** - sie sind Ihre einzige Garantie für eine Genesung.



**Meldung 2 - Automatische Liquidität:**


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



Geben Sie bei jeder Bestätigung "Ich verstehe" ein.



![Premier démarrage](assets/fr/01.webp)



*Phoenixd startet zum ersten Mal: Sicherungsbestätigungen und automatische Liquidität*



**3. Konfiguration während des Betriebs** (nur auf Französisch)



Für den Dauerbetrieb erstellen Sie eine systemd :



```bash
sudo nano /etc/systemd/system/phoenixd.service
```



```ini
[Unit]
Description=Phoenixd - Minimalist Lightning node
After=network.target

[Service]
User=your_user
WorkingDirectory=/home/your_user
ExecStart=/home/your_user/phoenixd
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```



```bash
sudo systemctl daemon-reload
sudo systemctl enable phoenixd
sudo systemctl start phoenixd
```



![Service systemd](assets/fr/02.webp)



*Phoenixd-Dienst aktiv und betriebsbereit über systemd und `auto-liquidity` bei 2m sat*



## Konfiguration und Sicherheit



### Konfigurationsdatei



Phoenixd erstellt automatisch `~/.phoenix/phoenix.conf` mit den wesentlichen Parametern:



```conf
# Network (mainnet by default)
chain=mainnet

# Size of automatic channels and requested liquidity amount (in satoshis)
auto-liquidity=2000000

# API configuration
http-bind-address=127.0.0.1
http-bind-port=9740
http-password=auto_generated_password
http-password-limited-access=limited_password
```



**Schlüsselparameter:**




- auto-Liquidität": Größe der automatisch geöffneten Kanäle (Standard: 2M Sats)
- http-Passwort": Admin-Passwort für API (Invoice-Erstellung UND Zahlungsversand)
- http-password-limited-access`: Eingeschränktes Passwort (nur Invoice-Erstellung)



### Sicherer Zugang mit HTTPS



Standardmäßig ist die Phoenixd-API nur über lokales HTTP (`http://127.0.0.1:9740`) zugänglich. Um Ihren Knoten von außen zu nutzen (mobile Anwendungen, andere Server, Webintegrationen), müssen Sie einen sicheren HTTPS-Zugang konfigurieren.



**Umgekehrtes Proxy-Prinzip:**


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



**Nginx** fungiert als **Reverse Proxy**: Es hört HTTPS-Anfragen aus dem Internet an Port 443 ab, leitet sie lokal an Phoenixd (Port 9740) weiter und sendet dann verschlüsselte Antworten zurück an den Client.



**Das SSL/TLS**-Zertifikat ist eine digitale Datei, die :




- Beweisen Sie die Identität Ihres Servers** (verhindert Man-in-the-Middle-Angriffe)
- Aktiviert HTTPS**-Verschlüsselung: Alle Daten, einschließlich Ihrer API-Kennwörter, werden während der Übertragung verschlüsselt
- Kostenlos** von Let's Encrypt über das Tool certbot ausgestellt



Diese Konfiguration ermöglicht es Ihnen, :




- Sicherer Zugriff auf die API über das Internet**
- Verschlüsseln Sie Ihre API**-Passwörter während des Transports (um zu verhindern, dass sie im Klartext übertragen werden)
- Integrieren Sie Phoenixd** in externe Anwendungen, die HTTPS erfordern
- Einhaltung von Sicherheitsstandards** für Finanz-APIs



Konfigurieren Sie diesen HTTPS-Reverse-Proxy mit nginx :



**1. Nginx**-Konfiguration



```bash
sudo apt install nginx certbot python3-certbot-nginx
sudo nano /etc/nginx/sites-available/phoenixd.conf
```



```nginx
server {
listen 80;
server_name phoenixd.your-domain.com;

location / {
proxy_pass http://127.0.0.1:9740;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header Host $host;
}
}
```



```bash
sudo ln -s /etc/nginx/sites-available/phoenixd.conf /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```



**2. SSL**-Zertifikat



```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```



### Funktionsprüfung



Überprüfen Sie, ob Phoenixd ordnungsgemäß funktioniert:



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



Diese Befehle sollten JSON-Informationen über den Status und das Guthaben des Knotens (zunächst leer) zurückgeben.



![Commandes CLI](assets/fr/03.webp)



*Getinfo- und Getbalance-Befehle zur Überprüfung des Knotenstatus*



## Verwendung der API



### Erster Empfangstest



**1. Erstellen eines Blitzes** Invoice



Verwenden Sie die API, um Ihr erstes Invoice zu erstellen:



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### Das Verständnis des automatischen Liquiditätsmechanismus



**Grundprinzip:** Wenn Sie eine Blitzzahlung erhalten, muss Phoenixd manchmal einen neuen Kanal öffnen, um sie empfangen zu können. Dieses Öffnen des Kanals kostet eine Gebühr, die **automatisch** von dem erhaltenen Betrag abgezogen wird.



**Konkretes Beispiel mit 100.000 Sats:**



![Premier test de réception](assets/fr/04.webp)



*Erste Abnahmeprüfung: Sats 100k erhalten, Endsaldo von Sats 75.561 nach Abzug der Liquiditätskosten*



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



**Gebührenberechnung:**




- Dienstleistungsgebühr**: 1% der Kanalkapazität (2.115.000 Sats) = 21.150 Sats
- Mining Gebühren**: ~3.289 Sats (für On-Chain Transaktion)
- Gesamt**: 24.439 Sats automatisch abgezogen



**Überprüfung mit CLI-Befehlen:**


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*Restbetrag nach Zahlungseingang: 257 Sats verbleibend nach Blitzversand*



**Gebührenguthaben für kleine Zahlungen:** Wenn Sie Zahlungen erhalten, die zu gering sind, um die Eröffnung eines Kanals zu rechtfertigen (< ca. 25k Sats), werden diese in einem nicht erstattungsfähigen "Gebührenguthaben" gespeichert. Dieses Guthaben wird verwendet, um zukünftige Kanalgebühren zu bezahlen, wenn Sie einen ausreichenden Betrag erhalten.



**2. Kanalöffnung folgen**



Beobachten Sie die Phoenixd-Protokolle:



```bash
journalctl -u phoenixd -f
```



Sie werden die Öffnung des Kanals und den automatischen Abzug der Liquiditätsgebühren sehen. Die Gebühren variieren je nach Mempool Bitcoin Bedingungen, beinhalten aber immer 1% Servicegebühr plus die aktuelle Mining Gebühr.



**3. Kanal prüfen**



```bash
./phoenix-cli listchannels
```



Dieser Befehl zeigt Ihre aktiven Kanäle mit ihrem Status und ihrem Guthaben an.



### Vollständige API-Vorgänge



Phoenixd stellt eine REST-API auf Port 9740 zur Verfügung, die :



**Grundlegende Tätigkeiten:**


```bash
# Create an invoice
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='Test payment' \
-d amountSat=100000

# Send a payment (routing fee 0.4%)
curl -X POST http://localhost:9740/payinvoice \
-u :your_password \
-d invoice='lnbc...'

# Check balance
curl http://localhost:9740/getbalance \
-u :your_password

# Send on-chain funds (in case of channel closure)
./phoenix-cli sendtoaddress \
--address bc1q... \
--amountSat 50000 \
--feerateSatByte 12
```



**Wichtiges zu den Kosten:**




- Quittung**: 1% + Mining Gebühr für automatische Liquidität
- Versand**: 0.4% Routinggebühr für den Lightning Network



**Webhooks:** Webhooks ermöglichen es Phoenixd, Ihre Anwendungen **automatisch zu benachrichtigen**, wenn ein Ereignis eintritt (Zahlungseingang, Invoice bezahlt, Kanal geöffnet, etc.). Anstatt Phoenixd ständig nach Updates zu fragen, erhält Ihre Anwendung eine sofortige HTTP-Benachrichtigung.



**Ihr Online-Shop erhält automatisch eine Benachrichtigung, wenn ein Kunde eine Bestellung bezahlt, so dass die Transaktion sofort validiert werden kann.



Konfiguration in "phoenix.conf" :


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## Fortgeschrittene Anwendungen



### LNURL-Integrationen



Phoenixd unterstützt von Haus aus LNURL-Protokolle für eine erweiterte Integration:



**LNURL-Pay:** Bezahlen für LNURL-kompatible Dienste


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** Abrufen von Mitteln aus LNURL-Diensten


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:** Authentifizierung über Lightning für den Zugriff auf Dienste


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### Integration mit LNbits



LNbits kann Phoenixd gemäß der [offiziellen Dokumentation](https://docs.lnbits.org/guide/wallets.html) als Finanzierungsquelle nutzen:



**LNbits-Konfiguration:**


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



Diese Integration ermöglicht es Ihnen, LNbits-Subkonten zu erstellen, die von Ihrem Phoenixd-Knoten betrieben werden, und bietet einen webbasierten Interface für die Verwaltung mehrerer Lightning-Wallets.



### Kundenspezifische Anwendungen



Dank der umfassenden REST-API können Sie die :



**E-Commerce:** Direkte Integration von Lightning-Zahlungen in Ihren Shop


**Spendendienste:** Spendensysteme mit Rechnungen und automatischen Webhooks


**Bots für soziale Netzwerke:** Telegram/Discord-Bots mit Tippfunktionen


**Paywall Lightning:** Premium-Inhalte sind gegen eine Lightning-Gebühr erhältlich



## Sicherheit und bewährte Praktiken



### Schutz des Zugangs



**API-Passwörter:** Automatisch generierte Passwörter sind die Schlüssel zu Ihrer Lightning-Schatzkammer. Geben Sie sie niemals weiter und ändern Sie sie im Zweifelsfall.



**Firewall:** Lassen Sie Port 9740 niemals direkt zum Internet offen. Verwenden Sie immer nginx mit HTTPS.



**Erweiterte Authentifizierung:** Erwägen Sie ein VPN oder Tailscale, um den Zugang zu Ihrem Server auf autorisierte Geräte zu beschränken.



### Unverzichtbare Backups



**seed Wiederherstellung:** Speichern Sie Ihre 12 Wörter an einem sicheren Ort, außerhalb des Servers. Dies ist Ihre einzige Garantie für eine Wiederherstellung.



*~/.phoenix Verzeichnis:** Sichern Sie diesen Ordner regelmäßig (nachdem Phoenixd heruntergefahren wurde), um den Kanalstatus zu erhalten und die Wiederherstellung zu beschleunigen.



**Dienst-Wiederherstellungscodes:** Bewahren Sie auch Sicherungscodes für alle Dienste auf, bei denen Sie 2FA mit Ihrem Phoenix aktivieren.



### Überwachung und Wartung



**Überwachungsprotokolle:**


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**Aktualisierungen:** Beobachten Sie [GitHub releases](https://github.com/ACINQ/phoenixd/releases) für neue Versionen. Die Aktualisierung ist so einfach wie das Ersetzen der Binärdatei und der Neustart des Dienstes.



## Vergleich mit Alternativen



### Phoenixd vs. Phoenix standard



**Phoenix Standard (mobil) :**




- ✅ Sofortige Installation, keine Konfiguration
- gW-32 mobil intuitiv
- ✅ Gleiche Autospeicherung wie bei Phoenixd
- ❌ Keine API für Entwickler
- ❌ Kein Zugang zu detaillierten Protokollen



**Phoenixd (Server) :**




- ✅ HTTP-API für Integrationen
- ✅ Vollständiger Zugang zu den Protokollen
- ✅ Persönliche Infrastruktur
- ❌ Erfordert technische Fähigkeiten
- ❌ Server-Wartung erforderlich



**Beide verwenden ACINQ als LSP für automatische Liquidität.



### Phoenixd gegen LND/Kernblitz



**LND/Core Lightning :**




- ✅ Vollständige Kontrolle, vollständiges Lightning-Protokoll
- ✅ Große Gemeinschaft, ausgereiftes Ökosystem
- ❌ Komplexes manuelles Liquiditätsmanagement
- ❌ Große Lernkurve



**Phoenixd :*




- ✅ Automatisches Liquiditätsmanagement (wie Phoenix mobile)
- ✅ API für Entwickler
- ✅ Vereinfachte Konfiguration
- ❌ Verwendet ACINQ als LSP (keine unabhängige Leitweglenkung)
- ❌ Weniger flexibel als vollständige Knotenpunkte



## Lösung allgemeiner Probleme



### API-Zugangsprobleme



*fehler "*Authentifizierung fehlgeschlagen":**


1. Überprüfen Sie das Passwort in der Datei `~/.phoenix/phoenix.conf`


2. Authentifizierungsformat `-u:password` prüfen


3. Stellen Sie sicher, dass Phoenixd läuft (`./phoenix-CLI getinfo`)



**Verbindungszeitüberschreitungen:**




- Überprüfen Sie, ob Phoenixd auf dem richtigen Port (9740) lauscht
- Testen Sie den lokalen Zugang, bevor Sie HTTPS konfigurieren
- Protokolle prüfen: `journalctl -u phoenixd -f`



### Liquiditätsprobleme



**Zahlungen kommen nicht an :**


1. Überprüfen Sie, ob der Betrag die Mindestschwelle überschreitet (~30k Sats)


2. Konsultieren Sie die Protokolle, um Kanalfehler zu identifizieren


3. Gegebenenfalls Phoenixd neu starten



**Saldo der "Aufwandsgutschrift":**


Kleine Zahlungen werden als Rückstellung gespeichert. Erhalten Sie einen größeren Betrag, um die Kanalöffnung auszulösen und diese Mittel freizugeben.



## Schlussfolgerung



Phoenixd stellt einen hervorragenden Kompromiss zwischen Benutzerfreundlichkeit und technischer Souveränität für Entwickler dar. Es bietet eine einfache und dennoch leistungsstarke Lightning-API mit automatischem Liquiditätsmanagement, wodurch die Komplexität herkömmlicher Lightning-Knoten entfällt.



Diese Lösung eignet sich besonders gut für Entwickler und Unternehmen, die :




- Integrieren Sie Bitcoin Lightning in Ihre Anwendungen
- Vermeiden Sie die Komplexität des Lightning Channel Management
- Profitieren Sie von einer selbst gehosteten Infrastruktur
- Eine einfache, zuverlässige API



Mit Phoenixd bauen Sie Ihre eigene private Lightning-Infrastruktur mit einer modernen REST-API und einer automatischen Verwaltung der technischen Aspekte auf. Es ist die ideale Lösung für die Demokratisierung der Lightning-Integration in Ihren Projekten.



## Nützliche Ressourcen



### Offizielle Dokumentation




- GitHub Phoenixd** : [github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - Quellcode und Veröffentlichungen
- Phoenix Server** Website: [phoenix.acinq.co/server](https://phoenix.acinq.co/server) - Vollständige Dokumentation
- FAQ Phoenixd** : [phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - Häufig gestellte Fragen



### Unterstützung durch die Gemeinschaft




- GitHub Issues** : [github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - Technische Unterstützung
- Twitter ACINQ** : [@ACINQ_co](https://twitter.com/ACINQ_co) - Nachrichten und Ankündigungen