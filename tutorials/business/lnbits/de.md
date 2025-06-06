---
name: LNbits
description: Buchhaltungsplattform für Händler
---
![presentation](assets/lnbits-intro.webp)

# Buchführungssystem

LNbits ist vollgepackt mit einer Vielzahl von Werkzeugen, um Ihre ein- und ausgehenden Gelder zu kontrollieren und zu kanalisieren, Ihren Webshop oder sogar Geräte wie eine Hardware-Geldbörse oder einen Geldautomaten, die Sie selbst gebaut haben, zu verbinden. Benutzertypen umfassen:


- Wallet-Besitzer, die LNbits als Schnittstelle für die Verwaltung ihrer Gelder sowie deren Zusatzfunktionen nutzen wollen.
- Online- und Offline-Händler oder Dienstleister, die Bitcoin Onchain- und Lightning Network-Zahlungen akzeptieren möchten.
- Entwickler, die Lightning Network-Anwendungen erstellen möchten.
- Betreiber von Knotenpunkten, die ihren Knotenpunkt zu Abrechnungszwecken in das LNbits-System integrieren möchten.
- Jeder von ihnen hat andere Bedürfnisse. Wir bauen LNbits modular auf, so dass jeder Nutzer unsere Funktionen so nutzen kann, wie es für ihn am besten passt.

# Portemonnaie-Manager

LNbits ist ein freies und quelloffenes Buchhaltungssystem - kein Node-Manager. Die Kanalverwaltung ist die Domäne des Lightning-Knotens, der mit LNbits als Finanzierungsquelle wie LND oder c-lightning verbunden ist. Die Superuser oder Admin-User im LNbits-System sind für die Verwaltung der allgemeinen Zugänglichkeit und Konfiguration der Abrechnungsfunktionen und internen Erweiterungen verantwortlich.

LNbits fungiert als Schnittstelle zwischen dem Nutzer und dem Lightning-Knoten und bietet eine einfache, benutzerfreundliche Möglichkeit zur Verwaltung und Interaktion mit dem Zahlungsnetzwerk.

Stellen Sie sich LNbits wie ein "modulares Wordpress-Framework" für Ihren Node vor. Eine einfach zu verwaltende Plattform, die auf Erweiterungen basiert, die Sie für zahlreiche Anwendungsfälle kombinieren können.

Denken Sie an LNbits als Ihre eigene Bank Finanzmanagement-Software. Ihr Knoten bietet Kanäle zu zahlen durch und LNbits erweitert Sie Knoten in der Lage sein, mehr als ein Blitz Brieftasche Ihr Knoten kommt mit laufen. Diese Wallets müssen nicht unbedingt Ihnen selbst gehören. Nehmen wir an, dass Sie als LN-Knotenbetreiber bereits über genügend Liquidität und Geldmittel verfügen und nun Ihren Freunden, Ihrer Familie, Ihrem eigenen Geschäft oder anderen regelmäßigen Händlern einige Bitcoin-Bankdienstleistungen anbieten möchten.

Sie werden ihnen eine einfache Möglichkeit bieten, ein "Bankkonto" auf Ihrem Node zu eröffnen, ohne Zugang zu anderen Wallets auf Ihrem Node und zu Ihrer gesamten Node-Liquidität zu haben, sondern nur zu ihrem Teil. Ihr Knoten (die Bank) fungiert nur als Transportanbieter für ihre Zahlungen (in/out).

HINWEIS: Alle Gelder, die Ihre "Kunden" auf ihre LNbits-Bankkonten auf Ihrem Knoten einzahlen, gehen direkt in die LN-Kanäle Ihres Knotens. Das bedeutet, dass SIE der eigentliche Eigentümer dieser Gelder sind. Du trägst eine große Verantwortung für diese Gelder. Seien Sie nicht böse und laufen Sie mit den Geldern weg, seien Sie nicht böse und verlangen Sie keine hohen Gebühren. Wir wollen die Fiat-Bankster ficken, nicht uns gegenseitig (Bitcoin-Nutzer) ficken.

# Demo-Plattform

Die Demo kann unter [https://legend.lnbits.com](https://legend.lnbits.com) gefunden werden. Sie ist voll funktionsfähig und kann verwendet werden, um das Lightning Network und die Funktionen von LNbits und LNURL im Allgemeinen kennenzulernen. Obwohl wir Sie nicht davon abhalten können, möchten wir Sie bitten, es nicht für Ihre Produktionseinrichtung zu verwenden. Wir arbeiten nicht nur häufig an den Servern, um neue Funktionen zu testen, sondern möchten Sie auch ermutigen, Ihren eigenen Knoten und LNbits auf souveräne Weise zu betreiben. Wenn Sie denken, dass der Betrieb eines Knotens im Moment zu viel verlangt ist, können Sie LNbits mit einem Custodian Funding Service in der Cloud wie Opennode, Luna oder Votage oder mit dem Lightning Tipbot auf Telegram verbinden, um nur einige zu nennen.

# LNbits-Flyer

Möchten Sie einem Händler oder einem befreundeten Bauunternehmer einige grundlegende Informationen zukommen lassen? Wir freuen uns sehr, Ihnen unseren ersten Flyer zur Verfügung stellen zu können. Die Größe ist ein weltweit typisches Flyerformat mit 6 Seiten (2 Falzungen) und einer Breite von 3508 und einer Höhe von 2480px.

LNbits für Gewerbetreibende: [EN](/assets/lnbits-merchants-en.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)

LNbits für Bauherren: [EN](/assets/lnbits-builders-en.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)

# Einige Grundlagen

LNbits arbeitet auf der Grundlage des LNURL-Protokolls, was bedeutet, dass Anfragen in zwei Formen gültig sind: entweder als https:// clearnet link (keine selbstsignierten Zertifikate erlaubt) oder als http:// v2/v3 onion link. Um LNbits-Dienste wie LNURLp/w QR-Codes oder NFC-Karten anbieten zu können, die in freier Wildbahn verwendet werden können, müssen Sie LNbits für das Clearnetz (https) öffnen.

Bevor Sie LNbits installieren, vergewissern Sie sich, dass Sie die folgenden allgemeinen Hinweise darüber gelesen und verstanden haben, was LNbits ist und welche Möglichkeiten es für Sie freisetzt.


- [LND-Leitfaden](https://docs.lightning.engineering/) | Installation von LND
- [LND-Konfigurationsbeispiel](https://github.com/lightningnetwork/lnd/blob/master/sample-lnd.conf) | LND-Einstellungen
- [CLN-Leitfaden](https://docs.corelightning.org/docs/installation) | CLN-Installation
- [LUDs](https://github.com/lnurl/luds) LNURL Spec | [NIPs](https://github.com/nostr-protocol/nips) Nostr Spec
- [Einen Wachturm betreiben](https://docs.lightning.engineering/lightning-network-tools/lnd/watchtower) | Sehr wichtig!

Ausführlichere Anleitungen zur Verwendung von LNbits in spezifischen Anwendungsszenarien finden Sie hier:


- [Erste Schritte mit LNbits](https://darthcoin.substack.com/p/getting-started-lnbits) | Substack-Anleitung
- [ToDos für Ihre Sicherheit mit LNbits](https://youtu.be/i5FQf96e6zg) | Youtube Video
- [Privatbanken im Lightning Network](https://darthcoin.substack.com/p/bitcoin-private-banks-over-lightning) | Substack-Leitfaden
- [Führen Sie Geldbörsen für Ihre Freunde & Familie] (https://darthcoin.substack.com/p/the-bank-of-lnbits) | Substack guide
- [LNbits für ein kleines Restaurant / Hotel](https://darthcoin.substack.com/p/lnbits-for-small-merchants) | Substack guide
- [Verwendung von LNbits Streamer Copilot](https://darthcoin.substack.com/p/lnbits-streamer-copilot) | Substack-Anleitung
- [Starten Sie Ihren NOSTR-Markt mit LNbits](https://darthcoin.substack.com/p/lnbits-nostr-market) | Substack-Leitfaden
- [Verwendung von LNbits für Schulprojekte oder Festivalveranstaltungen](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools) Substack-Leitfaden

# LNbits installieren

## Grundlegende Installationsanleitung

LNbits kann auf jedem Rechner mit Linux-Betriebssystem installiert werden. Es erfordert keine leistungsstarke Maschine oder Server, nur genügend RAM-Speicher und etwas Festplattenplatz für die Datenbank. Es kann separat von einem BTC/LN-Knoten (lokaler PC oder Remote-VPS) oder zusammen auf demselben Rechner mit dem Knoten oder bereits in einer Bundle-Node-Software-Maschine installiert ausgeführt werden.

Sie können zwischen den gängigsten Paketmanagern wie Poetry und Nix wählen. Standardmäßig verwendet LNbits SQLite als Datenbank. Sie können auch PostgreSQL verwenden, was für Anwendungen mit einer hohen Last empfohlen wird. [Hier finden Sie eine Anleitung für die grundlegende Installation mit poetry oder nix](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md).

Für alle, die neu in diesem Bereich sind, gibt es eine detaillierte Schritt-für-Schritt-Anleitung, wie Sie Ihre LNbits in bestimmten Umgebungen zum Laufen bringen:


- [LNbits auf clearnet] (https://ereignishorizont.xyz/lnbits-server/en/) von Axel
- [LNbits auf einem VPS] (https://github.com/TrezorHannes/vps-lnbits) von Hannes
- [LNbits auf cloudflare] (https://www.nodeacademy.org/lnbits) von Leo

Sie können auch ein Video auf dem [dockerised Setup auf einem VPS mit PostgreSQ, LightningTipBot als Finanzierungsquelle unter Verwendung von nginx] (https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/) finden.

[Weitere Installationsszenarien hier](https://darthcoin.substack.com/p/build-your-own-lnbits-app-server).

Für Bundle-Software-Knoten lesen Sie bitte deren spezifische Dokumentation über LNbits: [Citadel](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)

## LNbits SaaS

Wenn Sie sich nicht mit dem technischen Kram beschäftigen und weder Ihre Finanzierungsquelle noch Ihre LNbits selbst hosten wollen, gibt es eine [LNbits SaaS-Version](https://saas.lnbits.com) (Software-as-a-Service), die Sie nutzen können. Es ist im Grunde wie LNbits in einer Cloud, aber Sie können die Finanzierungsquelle (z.B. Ihren Node, eine LNbits-Wallet, den LNtipbot, Fakewallet usw.) und Umgebungsvariablen selbst definieren - was bei anderen Cloud-Lösungen meist nicht der Fall ist.

[Hier finden Sie einen detaillierten Leitfaden für die Nutzung von LNbits SaaS für bestimmte Anwendungsfälle] (https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools).

## Quellen der Finanzierung

LNbits ist keine Knotenverwaltungssoftware, sondern ein auf LN ausgerichtetes Buchhaltungssystem, das auf einer LND- oder CLN-Finanzierungsquelle aufbaut. Nach der ersten Installation können Sie Ihre LNbits unter http://localhost:5000/ besuchen.

Um die Finanzierungsquelle zu ändern, gehen Sie auf Ihre Super-User-URL und wählen Sie eine Finanzierungsquelle unter "Server verwalten" oder bearbeiten Sie die .env-Datei, indem Sie `LNBITS_BACKEND_WALLET_CLASS` auf die von Ihnen benötigte Quelle ändern, wenn Sie `adminUI=TRUE` in der `.env` setzen.

Sie finden die .env-Datei in Ihrem lnbits/ oder lnbits/apps/data-Ordner, indem Sie den Befehl erweitern, um die Dateien in Ihrem Verzeichnis mit `ls -a` aufzulisten.

Möglicherweise müssen Sie auch zusätzliche Pakete installieren oder zusätzliche Setup-Schritte durchführen, indem Sie die gewünschte Finanzierungsquelle auswählen. Nach einem Neustart ist Ihre neue Einrichtung aktiv.

Welche Finanzierungsquellen kann ich für LNbits nutzen?

LNbits kann auf vielen Lightning-Network-Finanzierungsquellen laufen. Derzeit gibt es Unterstützung für CoreLightning, LND, LNbits, LNPay, OpenNode, mit mehr regelmäßig hinzugefügt werden.

Es ist wichtig, eine Quelle zu wählen, die eine gute Liquidität hat und mit guten Peers verbunden ist. Wenn Sie LNbits für öffentliche Dienste verwenden, können die Zahlungen Ihrer Nutzer nur dann problemlos in beide Richtungen fließen.

Eine Backend-Wallet (Geldquelle) kann mit den folgenden LNbits-Umgebungsvariablen in der Datei `.env` oder in Ihrem Superuser-Account unter dem Abschnitt Manage-Server konfiguriert werden.

Wenn Sie die .env-Version verwenden möchten, finden Sie die Parameter hier:

### CoreLightning


- CLN
  - lNBITS_BACKEND_WALLET_CLASS": **CoreLightningWallet**
  - cORELIGHTNING_RPC": /file/path/lightning-rpc
- Funke (c-Blitz)
  - lNBITS_BACKEND_WALLET_CLASS": **SparkWallet**
  - `SPARK_URL`: http://10.147.17.230:9737/rpc
   - sPARK_TOKEN": geheimer_Zugangsschlüssel

### Lightning Netzwerk Daemon


- LND (REST)
  - lNBITS_BACKEND_WALLET_CLASS": **LndRestWallet**
  - `LND_REST_ENDPOINT`: http://10.147.17.230:8080/
  - `LND_REST_CERT`: /file/path/tls.cert
  - lND_REST_MACAROON": /file/path/admin.macaroon oder Bech64/Hex
  - lND_REST_MACAROON_ENCRYPTED": eNcRyPtEdMaCaRoOn
- LND (gRPC)
  - lNBITS_BACKEND_WALLET_CLASS": **LndWallet**
  - lND_GRPC_ENDPOINT": ip_address
  - lND_GRPC_PORT": Anschluss
  - `LND_GRPC_CERT`: /file/path/tls.cert
  - lND_GRPC_MACAROON": /file/path/admin.macaroon oder Bech64/Hex

Sie können stattdessen auch ein AES-verschlüsseltes Macaroon (weitere Informationen) verwenden, indem Sie


  - lND_GRPC_MACAROON_ENCRYPTED": eNcRyPtEdMaCaRoOn

Um Ihr Macaroon zu verschlüsseln, führen Sie `./venv/bin/python lnbits/wallets/macaroon/macaroon.py` aus.

### LNbits (eine weitere LNbits-Instanz)


- LNbits-Instanz gehostet auf einem Cloud-Server oder Ihrem eigenen Home-Server
  - lNBITS_BACKEND_WALLET_CLASS": **LNbitsWallet**
  - lNBITS_ENDPOINT": https://lnbits.mydomain.com
  - lNBITS_KEY": my-lnbits-AdminKey
- LNbits Legend Demo Server (!! Verwenden Sie diesen NICHT für die Produktion / kommerzielle Zwecke, nur zum Testen !!)
  - lNBITS_BACKEND_WALLET_CLASS": **LNbitsWallet**
  - lNBITS_ENDPOINT": https://legend.lnbits.com
  - lNBITS_KEY": legend-lnbits-AdminKey

### Blitz-TipBot

Um Ihren [Lightning Tipbot] (https://t.me/LightningTipBot) mit Telegram zu verbinden, müssen Sie die folgenden Parameter einstellen:


  - lNBITS_BACKEND_WALLET_CLASS": **LnTipsWallet**
  - lNBITS_ENDPOINT": https://ln.tips
  - `LNBITS_KEY`: Um den Schlüssel zu erhalten, musst du einmal /api in einem privaten Chat mit dem LightningTipbot auf Telegram ausführen.

Siehe auch diese Anleitung zur Installation von [LNbits mit LightningTipBot via vps](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)

### IBEX HUB

Registrieren Sie sich [hier] (https://ibexpay.ibexmercado.com/onboard) und holen Sie sich Ihre Schlüssel/Tokens von dort, der Endpunkt ist https://ibexpay-api.ibexmercado.com.

Weitere Informationen finden Sie unter [IBEX API-Dokumentation] (https://ibexpay-api.readme.io/reference/getting-started-with-your-api).

### LNPay

Damit der Rechnungshörer funktioniert, müssen Sie eine öffentlich zugängliche URL in Ihrem LNbits haben und einen [LNPay webhook](https://dashboard.lnpay.co/webhook/) einrichten, der auf `<Ihren LNbits-Host>/wallet/webhook` mit dem Ereignis "Wallet Receive" und ohne Angabe eines Geheimnisses zeigt. Die Einstellung `https://mylnbits/wallet/webhook` wird die Endpunkt-URL sein, die über jede Zahlung benachrichtigt wird.


  - lNBITS_BACKEND_WALLET_CLASS": **LNPayWallet**
  - lNPAY_API_ENDPOINT": https://api.lnpay.co/v1/
  - lNPAY_API_KEY": sak_apiKey
  - lNPAY_WALLET_KEY": waka_apiKey

### OpenNode

Damit die Rechnung funktioniert, müssen Sie eine öffentlich zugängliche URL in Ihrem LNbits haben. Die Webhook-Einstellung ist optional.


  - lNBITS_BACKEND_WALLET_CLASS": **OpenNodeWallet**
  - oPENNODE_API_ENDPOINT": https://api.opennode.com/
  - oPENNODE_KEY": opennodeAdminApiKey

### Alby

Alby ist eine Browser-Erweiterung mit LN-Wallet-Funktionen und einem LNDHUB-Konto, das als Finanzierungsquelle für LNbits genutzt werden kann. [Mehr Details hier](https://getalby.com/).

Damit die Rechnung funktioniert, müssen Sie eine öffentlich zugängliche URL in Ihrem LNbits haben. Es ist keine manuelle Webhook-Einstellung erforderlich. Sie können ein Alby-Zugangs-Token hier generieren: https://getalby.com/developer/access_tokens/new


- lNBITS_BACKEND_WALLET_CLASS": AlbyWallet
- aLBY_API_ENDPOINT": https://api.getalby.com/
- aLBY_ACCESS_TOKEN": AlbyAccessToken

## Zusatzinformationen / Anleitungen zur Fehlerbehebung

Hier sind einige zusätzliche Anweisungen für den Fall, dass Sie sie benötigen. Klicken Sie auf den Pfeil, um die Beschreibung zu erweitern.

### Der Killswitch 🚨

In letzter Zeit gab es so viele gefährliche Fehler, nicht nur in der gesamten Branche, sondern auch bei LNbits, dass wir beschlossen haben, etwas dagegen zu unternehmen. Sie können sich nun für Warnungen und/oder direkte Maßnahmen entscheiden, wenn eine Schwachstelle oder ein Fehler, der zum Verlust von Geldern führen könnte, erneut auftritt.

![killswitchn](assets/lnbits-killswitch.webp)

Wenn die Instanz auf void-wallet umgestellt ist, sehen alle Benutzertypen ein gelbes Banner an der Stelle, an der sich normalerweise der Hinweis "LNbits ist in der Beta-Phase" neben dem Themen-/Sprachbereich oben rechts befindet - und das ist der offensichtlichste Hinweis darauf, dass etwas passiert ist. Werfen Sie einen Blick auf Ihren neuen, grün markierten Server-Tab im linken Teil des Fensters.

Wie funktioniert es? Wenn der Killswitch aktiviert ist, wird ein geheimes Github-Repository, das nur dem LNbits-Kernteam zur Verfügung steht, in einem Intervall von X Minuten (das angegeben werden kann) überprüft. Wenn ein verwundbarer Fehler in diesem Repository veröffentlicht wird, dient dies als Signal, das den Killswitch auf allen Installationen, die sich angemeldet haben, auslöst und Ihre Instanz von LNbits auf die Verwendung der leeren Geldbörse umstellt. Wenn sich die Wolken verzogen haben und Sie das Sicherheitsupdate installiert haben, können Sie Ihre Finanzierungsquelle wieder auf Ihren Knoten, Ihre Geldbörse oder was auch immer Sie verwenden, auch über den Abschnitt "Server verwalten" einstellen. Dieses Wiki hat einen Abschnitt über den Wechsel der Finanzierungsquellen, wenn Sie nicht wissen, was zu konfigurieren.

### Unterschied zwischen Admin und Superuser

Mit der LNbits Admin UI können Sie die LNbits-Einstellungen über das LNbits-Frontend ändern. Sie ist standardmäßig deaktiviert und wenn Sie das erste Mal die Umgebungsvariable `LNBITS_ADMIN_UI=true` in der `.env`-Datei setzen, werden die Einstellungen initialisiert und verwendet. Von da an werden die entsprechenden Einstellungen aus der Datenbank und nicht mehr die aus der .env-Datei verwendet.

### Super-Benutzer

Mit der Admin UI haben wir den Superuser eingeführt, der Zugriff auf den Server hat und somit Einstellungen ändern kann, die den Server zum Absturz bringen oder ihn über das Frontend und die API unempfindlich machen könnten, wie z.B. die Änderung der Finanzierungsquelle. Der Superuser ist nur in der Einstellungs-Tabelle der Datenbank gespeichert. Nachdem die Einstellungen auf die Standardwerte zurückgesetzt und neu gestartet wurden, wird ein neuer Superuser erstellt. Wir haben auch einen Dekorator für die API-Routen hinzugefügt, um zu prüfen, ob ein Superuser existiert. Seine ID wird nie über die API und das Frontend gesendet und erhält nur ein bool (ja/nein), ob man Superuser ist oder nicht.

Nur der Superuser kann über den Bereich "Aufladen" Satoshis auf verschiedene Geldbörsen aufladen.

Sie können den Superuser auch per Webhook an einen anderen Dienst senden, wenn dieser erstellt wird. Mehr Infos hier https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `class SaaSSettings`

Im Frontend finden Sie auch die Möglichkeit, das Shop-Bild zu ändern, das auf der Seite "Brieftasche erstellen" angezeigt wird, indem Sie den Bereich Server verwalten öffnen und Theme -> Custom Logo wählen.

### Admin-Benutzer

Umgebungsvariable: `LNBITS_ADMIN_USERS`, kommaseparierte Liste von Benutzer-IDs. Admin-Benutzer können Einstellungen in der Admin-Oberfläche ändern - mit Ausnahme der Einstellungen für die Finanzierungsquelle, da dies einen Server-Neustart erfordern würde und den Server möglicherweise unzugänglich machen könnte. Außerdem haben sie Zugriff auf alle Erweiterungen, die ihnen in `LNBITS_ADMIN_EXTENSIONS` zugewiesen sind.

### Erlaubte Benutzer

Umgebungsvariable: `LNBITS_ALLOWED_USERS`, kommagetrennte Liste von Benutzer-IDs. Durch die Definition dieser Benutzer wird LNbits für die Öffentlichkeit nicht mehr nutzbar sein. Nur definierte Benutzer und Administratoren können dann auf das LNbits-Frontend zugreifen.

#### LNbits aktualisieren

Eine normale Aktualisierung Ihrer lokalen LNbits-Instanz erfolgt einfach durch Kopieren und Einfügen der folgenden CLI-Befehle:

```
cd lnbits
## Stop LNbits with `ctrl + x`
git pull
## Keep your poetry install up to date, this can be done with
poetry self update
poetry install --only main
## or
git checkout main && git pull && poetry install
## Start LNbits with
poetry run lnbits
```

Wenn Sie Raspiblitz oder MyNode verwenden, benötigen Sie möglicherweise zusätzlich eine

```
sudo systemctl restart lnbits
```

am Ende, weil es LNbits als Dienst betreibt.

Bei Umbrel/Citadel lauten die Befehle

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```

#### SQLite zu PostgreSQL Migration

Wenn Sie LNbits bereits auf einer SQLite-Datenbank installiert haben und betreiben, empfehlen wir Ihnen dringend, auf Postgres zu migrieren, wenn Sie LNbits in größerem Umfang betreiben wollen.

Es ist ein Skript enthalten, das die Migration einfach durchführen kann. Sie müssen Postgres bereits installiert haben und es sollte ein Passwort für den Benutzer vorhanden sein (siehe Postgres-Installationsanleitung oben). Außerdem muss Ihre LNbits-Instanz einmal auf Postgres laufen, um das Datenbankschema zu implementieren, bevor die Migration funktionieren kann:

```
# STOP LNbits
# add the database connection string to .env 'nano .env' LNBITS_DATABASE_URL=
# postgres://<user>:<password>@<host>/<database> - alter line bellow with your user, password and db name
LNBITS_DATABASE_URL="postgres://postgres:postgres@localhost/lnbits"
# save and exit
# START LNbits
# STOP LNbits
poetry run python tools/conv.py
# or
make migration
```

Hoffentlich funktioniert jetzt alles und wird migriert... Starten Sie LNbits erneut und überprüfen Sie, ob alles richtig funktioniert.

#### Sicherung und Wiederherstellung der Datenbank

Bitte lesen Sie [diesen sehr ausführlichen Leitfaden über den Sicherungs- und Wiederherstellungsprozess] (https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore).

#### Das Aufladen meiner LNbits-Brieftasche von meinem Node aus funktioniert nicht

Wenn Sie Sats von demselben Knoten senden wollen, der auch die Finanzierungsquelle für Ihre LNbits ist, müssen Sie die Datei lnd.conf bearbeiten.

Die folgenden Parameter müssen angegeben werden: "Rundweg zulassen=1"

Bitte tun Sie dies im Abschnitt Anwendungsoptionen Ihrer lnd.conf. Auf einigen Bundle-Knoten könnte sonst der Start von LND fehlschlagen.

HINWEIS: Es wird empfohlen, stattdessen die neue adminUI-Erweiterung mit der Option "TopUp" zu verwenden, um Geld auf ein LNbits-Konto einzuzahlen.

#### Fehler 426

Ich bekam die Fehlermeldung: "lnurl muss über eine öffentlich zugängliche https-Domäne oder tor geliefert werden. 426 Upgrade erforderlich"</summary>

Dieser Fehler tritt normalerweise auf, weil Ihr LNbits hinter einem ngnix-Tunnel die LNURL-Adresse nicht korrekt weiterleitet. Stoppen Sie Ihr LNbits und bearbeiten Sie die .env-Datei, indem Sie diese Zeile hinzufügen:

wEITERGELEITETE_ERLAUBTE_IPS=*"

Wenn Sie ein ngnix-Setup verwenden, stellen Sie sicher, dass Sie diese Header in der ngnix-Konfiguration haben:

```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```

#### Netzwerkfehler

Ich erhalte "https-Fehler", Netzwerkfehler" oder andere beim Scannen eines QR</summary>

Schlechte Nachrichten, dies ist ein Routing-Fehler, der viele Gründe haben kann. Überprüfen Sie zunächst die LNURL des QRs mit dem [Lightning Decoder](https://lightningdecoder.com/), ob Sie dort etwas Seltsames finden können. Lassen Sie uns einige der möglichen Probleme und ihre Lösungen ausprobieren.

LNbits läuft nur über Tor, du kannst es nicht über eine öffentliche Domain wie lnbits.yourdomain.com öffnen


- Da Sie möchten, dass Ihre Einrichtung so bleibt, öffnen Sie Ihre LNbits-Geldbörse mit der .onion URI und erstellen Sie sie erneut. Auf diese Weise wird die QR generiert, um über diese .onion URI so über tor nur zugänglich sein. Erstelle diesen QR nicht über eine .local URI, da er dann nicht über das Internet erreichbar ist, sondern nur von deinem Home-LAN aus.
- Öffnen Sie Ihre LN-Wallet-App, die Sie zum Scannen des QR verwendet haben, und verwenden Sie diesmal tor (siehe Einstellungen der Wallet-App). Wenn die App tor nicht anbietet, können Sie stattdessen Orbot (Android) verwenden. Im Abschnitt "Installation" finden Sie detaillierte Anweisungen, wie Sie Ihre LNbits für clearnet/https öffnen können.

#### Verhindern, dass andere mit meinen LNbits Geldbörsen erstellen

Wenn Sie Ihre LNbits im Clearnet betreiben, kann im Grunde jeder eine Wallet darauf erstellen. Da die Gelder deines Knotens an diese Wallets gebunden sind, möchtest du das vielleicht verhindern. Es gibt zwei Möglichkeiten, dies zu tun:

Konfigurieren Sie die erlaubten Benutzer und Erweiterungen in der Datei `.env` ([siehe das env-Beispiel hier](https://github.com/lnbits/lnbits/blob/main/.env.example)). Dies funktioniert nur, wenn Sie die Einstellung `adminUI=FALSE` in der .env verwenden, andernfalls müssen Sie dies im Abschnitt Server verwalten -> Benutzer -> Erlaubte Benutzer tun. Alle anderen werden danach nicht mehr zugelassen.

#### Anpassen des Zeitrahmens für den Rechnungsablauf

Jetzt können Sie Rechnungen mit einem individuellen Ablaufdatum erstellen. Kompatibel mit den Backends: LndRestWallet, LndWallet, CoreLightningWallet, EclairWallet, LnbitsWallet, SparkWallet bis jetzt!

Sie können `LIGHTNING_INVOICE_EXPIRY` in Ihrer .env-Datei einstellen oder die AdminUI verwenden, um den Standardwert für alle Rechnungen zu ändern. Es gibt auch ein neues Feld im Endpunkt /api/v1/payments, in dem Sie das Ablaufdatum in den JSON-Daten festlegen können.

## Wallet-URL gelöscht

### Geldbörse auf Demoserver legend.lnbits

Speichern Sie immer eine Kopie Ihrer Wallet-URL, Export2phone-QR oder LNDhub für Ihre eigenen Wallets an einem sicheren Ort. LNbits kann Ihnen NICHT dabei helfen, sie bei Verlust wiederzuerlangen.

### Brieftasche mit eigener Finanzierungsquelle/Knotenpunkt

Speichern Sie immer eine Kopie Ihrer Wallet-URL, Export2phone-QR oder LNDhub für Ihre eigenen Wallets an einem sicheren Ort. Sie finden alle LNbits-Benutzer und Wallet-IDs in Ihrer LNbits-Benutzermanager-Erweiterung oder in Ihrer Sqlite-Datenbank. Um die LNbits-Datenbank zu bearbeiten oder zu lesen, gehen Sie in den Ordner LNbits /data und suchen Sie die Datei sqlite.db. Sie können sie mit Excel oder einem speziellen SQL-Editor wie [SQLite browser] (https://sqlitebrowser.org/) öffnen und bearbeiten.

Außerdem können Sie die Geldbörsen über CLI auslesen und jede Geldbörse in Ihrer Datenbank einsehen.

```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```

Die Ausgabe sieht dann etwa so aus

```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

und Sie möchten diese Werte in eine Url wie diese einfügen

```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```

Dabei ersetzen Sie f8a43fc363ea428db5c53b3559935f1f mit dem Wert, der vor dem Namen steht (in unserem Beispiel f8a43fc363ea428db5c53b3559935f1f) und 1280ff5910a9c485a782a2376f338b6c ist Ihr Benutzer und sollte der Wert sein, der nach dem Namen angezeigt wird. Zum Beenden von sqlite3 geben Sie ein

```
.quit
```

#### LNURL für eine Lightning-Adresse und umgekehrt

Versuchen Sie diesen [Encoder](https://lnurl-codec.netlify.app/) von fiatjaf oder [diesen](https://lightningdecoder.com/). Um eine LNURLp zu bezahlen oder zu überprüfen, können Sie auch [LNurlpay](https://wwww.lnurlpay.com/) verwenden. Es sollte HTTPS NOT HTTP angegeben werden.

#### Konfigurieren Sie einen Kommentar, den die Leute sehen, wenn sie bei meinem LNURLp QR bezahlen

Wenn Sie eine LNURL-p erstellen, wird das Kommentarfeld standardmäßig nicht ausgefüllt. Das bedeutet, dass Kommentare nicht an Zahlungen angehängt werden dürfen.

Um Kommentare zuzulassen, fügen Sie die Zeichenlänge des Feldes hinzu, von 1 bis 250. Sobald Sie dort eine Zahl eingeben, wird das Kommentarfeld beim Zahlungsvorgang angezeigt. Sie können auch eine bereits erstellte LNURL-p bearbeiten und diese Zahl hinzufügen.

![lnbits comments](assets/lnbits-comments.webp)

#### Einzahlung von onchain BTC auf LNbits

Es gibt zwei Möglichkeiten, Sats von onchain BTC in LN BTC (bzw. in LNbits) zu tauschen.

##### Über einen externen Tauschdienst.

Andere Nutzer, die keinen Zugriff auf Ihre LNbits-Instanz haben, können einen Tauschdienst wie [Boltz](https://boltz.exchange/), [FixedFloat](https://fixedfloat.com/), [DiamondHands](https://swap.diamondhands.technology/) oder [ZigZag](https://zigzag.io/) nutzen. Dies ist nützlich, wenn Sie nur LNURL/LN-Rechnungen von Ihrer LNbits-Instanz aus bereitstellen, ein Zahler aber nur Onchain-Sats hat, so dass er diese Sats zuerst auf seiner Seite austauschen muss. Das Verfahren ist einfach: Benutzer sendet onchain btc an den Swap-Service und gibt die LNURL / LN-Rechnung von LNbits als Ziel des Swaps an.

##### Verwendung der LNbits-Erweiterung von Onchain und Boltz.

Beachten Sie, dass es sich hierbei um eine separate Wallet handelt, nicht um die LN btc, die von LNbits als "Ihre Wallet" bei Ihrer LN-Finanzierungsquelle dargestellt wird. Diese Onchain-Wallet kann auch zum Swappen von LN btc auf (z.B. Ihre Hardware-Wallet) verwendet werden, indem Sie die LNbits Boltz- oder Deezy-Erweiterung verwenden. Wenn Sie einen Webshop betreiben, der mit Ihrem LNbits für LN-Zahlungen verbunden ist, ist es sehr praktisch, regelmäßig alle Sats von LN in die Onchain zu leiten. Dies führt zu mehr Platz in Ihren LN-Kanälen, um neue, frische Sats empfangen zu können.

Verfahren für diejenigen, die keine Bitcoin-Hardware-Wallet haben:


- Verwenden Sie Electrum oder Sparrow Wallet, um eine neue Onchain-Wallet zu erstellen und speichern Sie den Backup-Seed an einem sicheren Ort.
- Gehen Sie zu den Brieftascheninformationen und kopieren Sie die xpub.
- Gehen Sie zu LNbits - Onchain-Erweiterung und erstellen Sie eine neue Watch-Only-Brieftasche mit dieser xpub.
- Gehen Sie zu LNbits - Tipjar Erweiterung und erstellen Sie ein neues Tipjar. Wählen Sie neben der LN-Brieftasche auch die Onchain-Option.
- Optional - Gehen Sie zu LNbits - SatsPay Erweiterung und erstellen Sie eine neue Gebühr für onchain btc. Sie können zwischen onchain und LN oder beidem wählen. Es wird dann eine Rechnung erstellen, die geteilt werden kann.
- Optional - Wenn Sie Ihre LNbits mit einer Wordpress- und Woocommerce-Seite verknüpfen, können Sie eine Watch-Only-Brieftasche mit Ihrer LN btc-Shop-Brieftasche verknüpfen, so dass der Kunde beide Zahlungsmöglichkeiten auf demselben Bildschirm hat.

Wenn Sie eine Zahlung in LNbits erhalten, wird im Transaktionsprotokoll nur eine wiederaufgenommene Art der Transaktion angezeigt.

![lnbits payment details](assets/lnbits-payment-details.webp)

In Ihrer Transaktionsübersicht finden Sie einen kleinen grünen Pfeil für erhaltene und einen roten Pfeil für gesendete Gelder.

Wenn Sie auf diese Pfeile klicken, werden in einem Popup-Fenster die angehängten Nachrichten sowie der Name des Absenders angezeigt, sofern vorhanden.

Um einen Namen zu konfigurieren, der bei Zahlungen erscheint, ist dies in LNbits derzeit nicht möglich - aber zu empfangen. Dies ist nur möglich, wenn die LN-Brieftasche des Senders [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (nameDesc) wie [OBW, Blixt, Alby, ZBD, BitBanana](https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents) unterstützt.

Im Detailbereich Ihrer LNbits-Transaktionen wird dann ein Alias/Pseudonym angezeigt (klicken Sie auf die Pfeile). Beachten Sie, dass Sie dort einen beliebigen Namen angeben können, der möglicherweise nicht mit dem echten Namen des Absenders übereinstimmt, falls Sie einen solchen erhalten.

![lnbits namedesc](assets/lnbits-namedesc.webp)

Um Ihr LNbits-Konto in eine Wallet-App zu importieren, öffnen Sie Ihr LNbits mit dem Konto / der Wallet, die Sie verwenden möchten, gehen Sie zu "Erweiterungen verwalten" und aktivieren Sie die LNDHUB-Erweiterung. Öffnen Sie die LNDHUB-Erweiterung, wählen Sie die Wallet, die Sie verwenden möchten, und scannen Sie entweder den "Admin"- oder den "Nur-Rechnung"-QR, je nachdem, welche Sicherheitsstufe Sie für diese Wallet wünschen.

Sie können [Zeus] (https://zeusln.app/) oder [Bluewallet] (https://bluewallet.io/) als Geldbörsen-Apps für ein lndhub-Konto verwenden, wobei BW mehr als eine solche Geldbörse unterstützt.

Wenn du dies tust, empfehlen wir dir, auch die LN-Netzwerk-URI auf die deines eigenen Knotens zu setzen. Wenn deine LNbits-Instanz nur Tor ist, musst du diese Anwendungen auch mit aktiviertem Tor verwenden. Auch in diesem Fall musst du die LNbits-Seite über deine Tor.onion-Adresse öffnen.

Wenn Sie einen Fehler "unsupported hash type" bei der Verwendung eines ypub in der On-chain-Erweiterung haben, überprüfen Sie, ob Ihre LNbits-Instanz Python 3.10 verwendet, es könnte von [diesem Problem] betroffen sein (https://stackoverflow.com/questions/72409563/unsupported-hash-type-ripemd160-with-hashlib-in-python). Bearbeiten Sie die openssl.cnf wie in der Stackoverflow-Antwort beschrieben und starten Sie LNbits neu.

## Werkzeugbau und Bau mit LNbits

LNbits verfügt über alle Arten von [offenen APIs] (https://legend.lnbits.com/docs) und Tools zur Programmierung und Verbindung mit vielen verschiedenen Geräten für eine Unmenge von Anwendungsfällen.

Wenn Sie neu im Bauen sind, beginnen Sie mit dieser [MakerBits-Präsentation] (https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos) von Ben Arc über das Bauen von Gadgets auf der Basis von LNbits.

### WICHTIG!


- LNbits arbeitet auf der Grundlage des LNURL-Protokolls, dessen Anfragen in zwei Formen gültig sind: entweder als https:// clearnet link (keine selbstsignierten Zertifikate erlaubt) oder als http:// v2/v3 onion link. Um LNbits-Dienste wie LNURLp/w-QR-Codes oder NFC-Karten anbieten zu können, die in freier Wildbahn verwendet werden können, müssen Sie LNbits für clearnet (https) öffnen.
- Verwenden Sie für die Stromversorgung Ihres esp32 nur DATA-Kabel. Nicht alle Kabel unterstützen neben der Stromversorgung des esp auch Daten. Sie wären nicht der Erste, wenn das Kabel, das mit dem esp geliefert wurde, ein reines Stromkabel wäre
- Achten Sie darauf, dass Sie keinen USB-Hub mit anderen angeschlossenen Geräten verwenden. Dies kann zu seltsamen Effekten führen, die schwer zu beheben sind (z. B. nicht starten oder stoppen).
- Um esp Projekte mit einem MacOS zu realisieren, benötigen Sie einen UART Bridge Treiber. Wenn Sie Probleme mit dem Treiber auf Mac oder Linux-Systemen haben, finden Sie diese hier oder, wenn es sich um ein TTGO-Display handelt, hier. Wenn Sie unter Windows arbeiten und Probleme mit der Verbindung haben, stellen Sie sicher, dass Sie die alte Version 11.1.0 herunterladen, da die neuere Version nicht funktioniert! Sie können auch ein serielles Terminal hier finden, um Ihre Verbindung zu überprüfen - stellen Sie die Baudrate auf 115200.
- Obwohl es viel komfortabler ist, Platform.io zu verwenden (z.B. werden Abhängigkeiten automatisch installiert), empfehlen wir jedem, der neu im Bauen ist, Arduino zu verwenden.
- TT-Go Display S3: Die Farbe der Lasche der Displayschutzfolie verrät Ihnen, mit welchem Controller (ST7735_redtab, ST7735_blacktag, ST7735_greetab, greentab128, ..) sie gebaut wurde. Bewahren Sie es auf, um eine Fehlersuche durchführen zu können, wenn Sie sich selbst programmieren und der Bildschirm Grafiken nicht korrekt anzeigt, z. B. falsche Farben, gespiegelte Bilder oder streuende Pixel an den Rändern. Falls Sie dies jemals tun müssen, gibt es eine epische Anleitung zur Anpassung an verschiedene Bildschirme
- Verwenden Sie immer die Kleinbuchstaben lnurl239xx anstelle von LNURLl239xx
- Durch Hinzufügen von lightning:lnurl1234xyz wird ein QR erstellt, der beim Scannen die Brieftasche des Benutzers für diese Rechnung öffnet (zuletzt installierte Lightning-App auf iOS, Einstellung in Android)
- Wenn Sie einen esp32 über das Internet flashen, funktioniert das nur mit diesen Browsern (TL:DR Chrome, Edge & Opera).
- Bitte beachten Sie diese PIN-OUT-Referenz für die esp
- Wenn Sie FOSSoftware oder FOSGuides verwenden, verlinken Sie bitte immer den Autor. Jeder liebt es, sein Baby wachsen zu sehen und es initiiert auch eine Baukette, die ziemlich toll zu beobachten ist :)

Komm zur [Makerbits Telegram Group] (https://t.me/makerbits), wenn du Hilfe bei einem Projekt brauchst - wir haben dich!

![lnbits hackathlon](assets/lnbits-hackathlon.webp)

Hier sind einige Projektkategorien, die Sie mit LNbits erstellen können:


- [Nostr Signing Device](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [Archade Machine](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [Gerty] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [Nostr Zap Lampe](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)
- [BTC/LN ATM](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [Lightning Piggy](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [Hardware-Wallet](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-wallet)
- [Bitcoin Switch](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-switch)
- [Verkaufsautomat] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#vending-machine)
- [Bolty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bolty)
- [Nerdminer] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Nerdminer)
- [Bitcoin-Ticker](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-ticker)
- [BTClock](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#btclock)
- [Lora und die Maschenvernetzung] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lora)
- [HELFER & RESSOURCEN](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#resources)
- [Weitere Beispiele für Projekte "Powered by LNbits" hier](https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits).
- [Anwendungsfälle für LNbits](https://github.com/lnbits/lnbits/wiki/Use-Cases-of-LNbits)