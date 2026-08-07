---
name: BTCPay Server aktualisieren
description: Ein Sicherheitsupdate auf deine BTCPay-Server-Instanz anwenden und die wichtigen Zugangsdaten erneuern
---

![cover](assets/cover.webp)

Wer seinen eigenen Zahlungsprozessor betreibt, ist auch sein eigenes Sicherheitsteam. Wenn die BTCPay-Server-Maintainer ein Sicherheitsupdate veröffentlichen, wird niemand deine Instanz für dich patchen: Das Update, die Überprüfung und die anschließende Rotation der Zugangsdaten musst du selbst durchführen.

Dieses Tutorial führt dich durch das gesamte Verfahren, unabhängig davon, wie du BTCPay Server bereitgestellt hast: die laufende Version prüfen, das Update für deinen Bereitstellungstyp anwenden, verifizieren, dass es tatsächlich angekommen ist, und die Geheimnisse rotieren, die ein Angreifer möglicherweise erbeutet hat, solange deine Instanz verwundbar war.

Falls du BTCPay Server noch nicht bereitgestellt hast, beginne mit der Installationsanleitung:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc

## Die kritische Sicherheitslücke vom August 2026

⚠️ **Kritischer Sicherheitshinweis (7. August 2026):** Eine kritische Sicherheitslücke in BTCPay Server wird aktiv ausgenutzt und kann zum Verlust von Geldern führen. Aktualisiere deine Instanz sofort auf **Version 2.4.2** über `Admin Dashboard > Server > Maintenance > Update` und prüfe anschließend, dass die Fußzeile `2.4.2` anzeigt. Falls du nicht sofort aktualisieren kannst, fahre deinen BTCPay Server herunter. Nach dem Update musst du außerdem deine Macaroons und deine `macaroons.db` vollständig erneuern, die Authentifizierungsstrings jedes anderen Lightning-Backends vollständig erneuern und, falls du innerhalb von BTCPay Server ein Hot-On-Chain-Wallet erzeugt hast, diese Gelder verschieben und das Wallet neu erstellen. Integratoren sollten außerdem NBXplorer auf Version 2.6.10 aktualisieren. Quelle: [BTCPay Server 2.4.2 Release Notes](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

Version 2.4.2 wurde am 7. August 2026 veröffentlicht. Die Release Notes besagen, dass sie eine kritische Sicherheitslücke beheben, die bereits in freier Wildbahn ausgenutzt wurde, gemeldet von `brunoerg` und `benthecarman` im Rahmen des Bitcoin-Red-Team-Projekts. Dasselbe Release behebt außerdem eine Umgehung der TOTP-Zwei-Faktor-Authentifizierung über die Greenfield-Basic-Authentifizierung und deaktiviert die Greenfield-Basic-Authentifizierung standardmäßig fünf Minuten nach der Kontoerstellung.

Aus „aktiv ausgenutzt" folgen zwei Konsequenzen:

- **Das Update ist nicht optional und nichts, das man für nächste Woche einplant.** Eine ungepatchte Instanz, die aus dem Internet erreichbar ist, muss entweder aktualisiert oder abgeschaltet werden.
- **Das Update allein reicht nicht aus.** Falls deine Instanz kompromittiert wurde, bevor du gepatcht hast, besitzt der Angreifer möglicherweise bereits Kopien deiner Lightning-Zugangsdaten und jeglichen Hot-Wallet-Schlüsselmaterials, das BTCPay Server für dich erzeugt hat. Diese Geheimnisse bleiben nach dem Update gültig, bis du sie rotierst. Der Abschnitt zur Rotation weiter unten ist der Teil, den die meisten überspringen, und genau der Teil, der deine Gelder tatsächlich schützt.

## Schritt 1 — Herausfinden, welche Version du betreibst

Melde dich bei deinem BTCPay Server an und schau in die **Fußzeile jeder Seite**: Dort wird die Versionsangabe angezeigt. Du kannst auch `Admin Dashboard > Server > Maintenance` öffnen, wo die aktuelle Version und die Update-Steuerung angezeigt werden.

Falls deine Instanz die Greenfield-API bereitstellt, liefert `GET /api/v1/server/info` die Version ebenfalls.

Alles unter `2.4.2` ist verwundbar.

## Schritt 2 — Aktualisieren

### Selbstgehostete Docker-Bereitstellung (die Standardinstallation)

Dies betrifft die offizielle Docker-Bereitstellung, die man aus der BTCPay-Server-Dokumentation, dem LunaNode-One-Click-Launcher und den meisten VPS-Installationen erhält.

Der einfachste Weg ist die Weboberfläche:

1. Gehe zu `Admin Dashboard > Server > Maintenance`.
2. Klicke auf **Update**.
3. Warte, bis die Container heruntergeladen und neu gestartet werden. Die Oberfläche wird für einige Minuten nicht verfügbar sein.

Falls die Weboberfläche nicht erreichbar ist oder du die Protokolle sehen möchtest, erledige es über SSH:

```bash
sudo su -
cd "$BTCPAY_BASE_DIRECTORY/btcpayserver-docker"
. ./btcpay-update.sh
```

Bei einer Standardinstallation ist `$BTCPAY_BASE_DIRECTORY` gleich `/root`, das Verzeichnis lautet also `/root/btcpayserver-docker`. Das Skript lädt die neuesten Images herunter, erstellt die Container neu und gibt die resultierenden Versionen aus.

Die Docker-Bereitstellung liefert NBXplorer zusammen mit BTCPay Server mit, sodass ein Standardupdate auch NBXplorer auf die empfohlene Version `2.6.10` bringt. Falls du NBXplorer separat betreibst — typisch für Integratoren und individuelle Stacks — aktualisiere es explizit.

### Umbrel

Öffne das Umbrel-Dashboard, gehe zum **App Store**, suche BTCPay Server und wende das Update an, falls eines angeboten wird.

⚠️ **Wichtig:** App-Store-Pakete werden vom Umbrel-Team neu paketiert und können dem Upstream um Stunden oder Tage hinterherhinken. Prüfe nach dem Update die Version in der BTCPay-Server-Fußzeile. Falls sie immer noch unter `2.4.2` liegt, **stoppe die App** über das Umbrel-Dashboard und warte auf das paketierte Release, statt eine verwundbare Instanz laufen zu lassen.

Die dedizierte Umbrel-Anleitung behandelt die App selbst:

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

### Start9 / StartOS

Gleiche Logik: BTCPay Server über den StartOS-Marketplace aktualisieren, dann die Version in der Fußzeile überprüfen. Falls die paketierte Version noch nicht `2.4.2` ist, den Dienst stoppen, bis sie es ist.

### Verwaltete und Drittanbieter-Hosting-Lösungen

Falls jemand anderes deine Instanz betreibt (ein Hosting-Anbieter, ein Verein, der Server eines Freundes), brauchst du trotzdem die Bestätigung. Frage den Betreiber nach der in der Fußzeile angezeigten Versionsangabe und frage ausdrücklich, ob die unten beschriebene Rotation der Zugangsdaten nach dem Update durchgeführt wurde. „Wir haben aktualisiert" ist nicht dieselbe Antwort wie „wir haben deine Macaroons rotiert".

## Schritt 3 — Verifizieren, dass das Update tatsächlich angekommen ist

Lade die BTCPay-Server-Oberfläche neu und lies die Version in der Fußzeile. Sie muss `2.4.2` oder höher anzeigen.

Verlasse dich nicht darauf, dass der Update-Befehl ohne Fehler endet: Auf ressourcenbeschränkten Maschinen kann ein Image-Pull stillschweigend fehlschlagen und den vorherigen Container weiterlaufen lassen. Lies die Version, jedes Mal.

## Schritt 4 — Deine Zugangsdaten rotieren

Dieser Schritt macht aus „gepatcht" „sicher". Da die Sicherheitslücke bereits ausgenutzt wurde, bevor der Fix veröffentlicht wurde, behandle jedes Geheimnis, das deine Instanz besaß, als potenziell einem Angreifer bekannt.

### Lightning: LND

Erneuere die Macaroons **und** die Datei `macaroons.db`. Es reicht nicht aus, nur die Macaroon-Dateien zu löschen — LND leitet Macaroons aus dem in `macaroons.db` gespeicherten Root-Key ab, sodass ein Angreifer mit einer Kopie eines alten Macaroons so lange Zugriff behält, bis diese Datenbank neu erstellt wird.

Das Vorgehen ist: LND stoppen, `macaroons.db` und die `*.macaroon`-Dateien aus dem Netzwerkverzeichnis entfernen (für Mainnet `data/chain/bitcoin/mainnet/` innerhalb des LND-Datenverzeichnisses), dann LND neu starten und entsperren, wodurch sie neu erzeugt werden. Sichere das Verzeichnis zuvor und koppele jede Anwendung, die die alten Macaroons verwendet hat, neu — BTCPay Server selbst, Zeus, Thunderhub, RTL, Alby und jedes eigene Skript.

Falls du LND außerdem über das Internet exponierst, überprüfe gleichzeitig dessen TLS-Zertifikat und alle Zugangsdaten in `lnd.conf`.

### Lightning: andere Backends

Alles, was sich mit einem String bei deinem Node authentifiziert, braucht einen neuen String:

- **Core Lightning**: Erneuere die Rune oder die für die Verbindung verwendeten Zugangsdaten.
- **Phoenixd**: Rotiere das HTTP-Passwort.
- **LNbits und Ähnliches**: Widerrufe und erneuere die Admin- und Invoice-Keys.
- **In den BTCPay-Server-Store-Einstellungen gespeicherte Remote-Node-Verbindungsstrings**: Schreibe sie mit den neuen Geheimnissen neu.

### Innerhalb von BTCPay Server erzeugtes Hot-On-Chain-Wallet

Falls du BTCPay Server ein On-Chain-Wallet für dich erzeugen ließest — im Gegensatz zum Verbinden eines Hardware-Wallets oder zum Importieren eines xpub, dessen Keys nie den Server berührt haben —, lag dieser Seed auf der Maschine.

Betrachte ihn als verbrannt:

1. Erstelle ein neues Wallet, idealerweise mit einem Hardware-Wallet, damit die Keys nie wieder auf dem Server liegen.
2. Verschiebe die Gelder aus dem alten Wallet in das neue.
3. Ersetze das Ableitungsschema in den Store-Einstellungen durch das neue Wallet.
4. Verwende den alten Seed niemals wieder.

Watch-only-Setups (xpub oder Hardware-Wallet) benötigen das nicht: Die privaten Keys lagen nie auf dem Server. Genau deshalb empfiehlt die Installationsanleitung sie.

### BTCPay-Server-Konten und API-Keys

Solange du dabei bist:

- Ändere die Passwörter aller Benutzerkonten auf der Instanz.
- Widerrufe und erneuere alle Greenfield-**API-Keys**.
- Registriere die Zwei-Faktor-Authentifizierung neu, da 2.4.2 eine 2FA-Umgehung behebt.
- Öffne `Admin Dashboard > Server > Users` und prüfe, dass kein unerwartetes Konto existiert.
- Überprüfe kürzliche **Auszahlungen**, **Pull Payments** und **Rückerstattungen** auf Einträge, die du nicht selbst erstellt hast.
- Überprüfe deine Webhooks und deren Geheimnisse.

## Schritt 5 — Für das nächste Mal informiert bleiben

Sicherheitsupdates helfen nur den Betreibern, die davon erfahren:

- Beobachte die [BTCPay-Server-Releases auf GitHub](https://github.com/btcpayserver/btcpayserver/releases) — GitHub kann dich bei jedem neuen Release eines Repositorys per E-Mail benachrichtigen.
- Folge den Ankündigungskanälen des Projekts und dem [offiziellen Blog](https://blog.btcpayserver.org/).
- Halte deine Instanz auf einer Version, die du schnell aktualisieren kannst: Je weiter du zurückliegst, desto schmerzhafter wird ein Notfall-Update.

Self-Hosting verschafft dir Souveränität über deine Zahlungen. Der Preis dieser Souveränität ist genau das: Release Notes lesen und derjenige sein, der patcht.
