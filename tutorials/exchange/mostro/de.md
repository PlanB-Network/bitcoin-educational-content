---
name: Mostro
description: KYC-freie Bitcoin P2P Austauschplattform über Lightning und Nostr
---

![cover](assets/cover.webp)



Wie können Sie Bitcoins erwerben oder verkaufen, ohne Ihre finanzielle Souveränität zu gefährden? Zentralisierte Plattformen führen invasive KYC-Verfahren durch, bei denen Ihre persönlichen Daten offengelegt werden, und es besteht die Möglichkeit, dass Konten willkürlich eingefroren oder staatlich überwacht werden.



**Mostro P2P** bietet eine dezentralisierte Alternative, die Lightning Network, das Nostr-Protokoll und Hold-Rechnungen kombiniert. Seine wichtigste Neuerung: ein automatisches Treuhandsystem, bei dem Ihre Bitcoins während des gesamten Austauschs unter Ihrer Kontrolle bleiben, wodurch das Risiko eines Diebstahls, eines Konkurses der Börse oder einer willkürlichen Beschlagnahmung ausgeschlossen wird.



## Was ist Mostro P2P?



Mostro P2P ist ein quelloffenes Bitcoin-Tauschprotokoll, das von **grunch**, dem Entwickler des beliebten Telegram-Bots **lnp2pbot**, im Jahr 2021 eingeführt wurde. Während lnp2pbot bereits KYC-freien P2P-Austausch über Lightning ermöglichte, wies es eine große Schwachstelle auf: **Telegram stellt einen zentralen Ausfallpunkt** dar, der anfällig für Zensur durch Regierungen ist.



Mostro stellt die **dezentrale Weiterentwicklung** dieses Konzepts dar: Indem es Telegram durch das **Nostr**-Protokoll (ein unzensierbares Netzwerk verteilter Relais) ersetzt, beseitigt Mostro dieses systemische Risiko. Das Protokoll kombiniert Lightning Network für sofortige Transaktionen, Nostr für zensurresistente Kommunikation und **Hold invoices**, um ein wirklich nicht-rechtsstaatliches automatisches Treuhandsystem zu schaffen.



### Technische Architektur



Mostro arbeitet mit drei Komponenten:




- Daemon Mostrod**: koordiniert den Austausch zwischen Benutzern und Lightning Network
- Lightning**-Knoten: erstellt Sperrrechnungen (~24h kryptografisches Treuhandkonto)
- Mostro**-Kunden: Benutzeroberflächen (CLI, Mobile, Web)



Aufträge werden auf Nostr als öffentliche Ereignisse (Typ 38383) veröffentlicht, während private Geschäfte über Ende-zu-Ende-verschlüsselte Nachrichten (NIP-59, NIP-44) übermittelt werden. Jede Mostro-Instanz legt ihre eigenen Gebühren (in der Regel zwischen 0,3 % und 1 %) und Transaktionslimits (je nach Instanz zwischen einigen tausend und mehreren hunderttausend sats) fest.



### Entscheidende Vorteile



**Zensurresistent**: Keine Regierung kann Mostro abschalten, solange es irgendwo auf der Welt Nostr-Relais gibt. Anders als der anfällige lnp2pbot über Telegram ermöglicht Mostro einen Austausch, der **zensursicher** ist.



**Escrow nicht verpfändbar**: Lightning Hold Rechnungen sperren Ihre Bitcoins, ohne sie dauerhaft zu übertragen. Ihre Gelder bleiben unter Ihrer Kontrolle und werden im Falle eines Problems automatisch an Sie zurückgegeben (~24h).



**Vertraulichkeit durch Design**: Zwei Modi stehen zur Verfügung, um Ihren Bedürfnissen gerecht zu werden. Der Reputationsmodus** verknüpft Ihren Ruf mit Ihrem Nostr-Schlüssel, um dauerhaftes Vertrauen aufzubauen. Vollständig privater Modus** bevorzugt absolute Anonymität mit ephemeren Schlüsseln zur einmaligen Verwendung.



## Hauptmerkmale



**Dezentrale Kommunikation**: Alle Aufträge werden auf Nostr über kryptographisch signierte Ereignisse veröffentlicht. Private Verhandlungen werden über Ende-zu-Ende-verschlüsselte Nachrichten übertragen, wodurch absolute Vertraulichkeit garantiert wird.



**Reputationssystem**: 5-Sterne-Bewertung mit iterativer Berechnung dauerhaft auf Nostr gespeichert. Ermöglicht es Ihnen, sich schrittweise einen Ruf als zuverlässiger Händler aufzubauen.



**Dezentrale Schlichtung**: Im Falle einer Streitigkeit prüft ein unparteiischer Schlichter die Beweise und trifft eine Entscheidung auf der Grundlage transparenter Kriterien. Jeder Streitfall erzeugt eine eindeutige token zur Nachvollziehbarkeit.



**Flexibilität bei der Bezahlung**: Unterstützung für viele Fiat-Währungen über den yadio.io-Wechselkursservice. Akzeptiert SEPA-Überweisungen, PayPal, Revolut, Bargeld und jede zwischen den Parteien vereinbarte Methode.



## Mostro-Kunden verfügbar



Mostro bietet zwei Hauptbetriebsklienten für Ihre P2P-Börsen.



### Mostro CLI - Befehlszeilen-Client



Der **Mostro CLI** ist der ausgereifteste und funktionellste Client. Er ist in Rust geschrieben und bietet die gesamte Palette der Mostro-Funktionen über eine Befehlszeilenschnittstelle. Kompatibel mit macOS, Linux und Windows.



**Hauptbedienelemente** :




- aufträge auflisten": Alle verfügbaren Aufträge anzeigen
- neworder" : Erstellen eines neuen Kauf- oder Verkaufsauftrags
- takesell" / "takebuy": Einen Kauf- oder Verkaufsauftrag annehmen
- fiatsent": Bestätigen Sie den Versand einer Fiat-Zahlung
- freigeben": Freigabe des Treuhandkontos und Abschluss des Umtauschs
- getdm": Direkte Nachrichten anzeigen
- rate": Bewerten Sie Ihre Gegenpartei nach einem Austausch



Ideal für technische Benutzer, Automatisierung und Umgebungen, die maximale Sicherheit erfordern.



### Mostro Mobile - Smartphone-Anwendung



Die **Mobil-App** in der Alpha-Version ermöglicht den P2P-Handel direkt von Ihrem Smartphone aus. Intuitive grafische Interface mit Registerkarten-Navigation, Auftragsanzeige, erweiterten Filtern und integriertem Chat zur Kommunikation mit Ihren Kontrahenten.



Erhältlich für **Android** (via APK auf GitHub), ist es die optimale Wahl für Nutzer, die Einfachheit und gelegentliches mobiles Handeln bevorzugen.



### Mostro-web - Interface web (in Entwicklung)



Interface fortgeschrittene JavaScript-Webanwendung in aktiver Entwicklung. Entwickelt, um eine vollständige Benutzererfahrung mit umfangreichen Handels- und Portfoliomanagement-Funktionen zu bieten. Der Zugriff erfolgt über den Browser, eine Installation ist nicht erforderlich.



## Installation und Konfiguration



Dieser Leitfaden führt Sie durch die Installation und Verwendung der beiden wichtigsten Mostro-Clients: CLI und die mobile Anwendung.



### Wesentliche Voraussetzungen



Bevor Sie beginnen, benötigen Sie :





- Ein funktionierender Lightning Network** wallet mit ausreichender Liquidität (oder Lightning-kompatibel)
 - Empfohlen: Phoenix, Breez, Wallet oder Satoshi...
 - Mindestliquidität von 1000 Satoshis für den Test



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf



- Ein privater Nostr**-Schlüssel (Format `nsec1...`)
 - Erstellen Sie einen eigenen Handelsschlüssel auf [nostrkeygen.com](https://nostrkeygen.com/)
 - Wichtig**: Verwenden Sie niemals Ihren persönlichen Nostr-Schlüssel
 - Bewahren Sie Ihren privaten Schlüssel an einem sicheren Ort auf (Passwortmanager)





- Optional, aber empfohlen**: VPN- oder Tor-Verbindung zur Maskierung Ihrer IP-Adresse



https://planb.academy/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8

### Einbau des Mostro CLI



#### Unter macOS



**Schritt 1: Rust-Prüfung**



Prüfen Sie, ob Rust installiert ist (Version 1.64+ erforderlich):



```bash
rustc --version
```



Wenn Rust nicht installiert ist:



```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```



**Schritt 2: Klonen des Repositorys**



```bash
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
```



![Vérification Rust et clonage](assets/fr/01.webp)



**Schritt 3: Konfiguration**



Kopieren und bearbeiten Sie die :



```bash
cp .env-sample .env
```



Öffnen Sie `.env` und konfigurieren Sie Ihre Einstellungen:



```bash
# Public key of the Mostro instance (choose an instance)
# Main mainnet instance (recommended):
MOSTRO_PUBKEY='npub1ykvsmrmw2hk7jgxgy64zr8tfkx4nnjhq9eyfxdlg3caha3ph0skq6jr3z0'
# Alternative/test instance:
# MOSTRO_PUBKEY='npub19m9laul6k463czdacwx5ta4ap43nlf3lr0p99mqugnz8mdz7wtvskkm5wg'

# Your Nostr private key dedicated to trading
NSEC_PRIVKEY='nsec1votre_cle...'

# List of Nostr relays (use the same ones as the mobile app for synchronization)
RELAYS='wss://nos.lol,wss://relay.damus.io,wss://nostr-pub.wellorder.net,wss://nostr.mutinywallet.com,wss://relay.nostr.band'

POW='0'
```



**Wichtig für die Synchronisierung CLI/Mobile**: Um auf dieselben Aufträge auf dem CLI und der mobilen App zuzugreifen, müssen Sie den **gleichen Mostro Pubkey** und die **gleichen Nostr-Relais** in beiden Clients verwenden. Überprüfen Sie diese Einstellungen in den Einstellungen der mobilen App.



![Configuration .env](assets/fr/02.webp)



**Schritt 4: Installation**



Kompilieren und installieren Sie den CLI :



```bash
cargo install --path .
```



Die Kompilierung dauert 1-2 Minuten. Die ausführbare Datei `mostro-cli` wird in `~/.cargo/bin/` installiert.



![Installation du CLI](assets/fr/03.webp)



**Schritt 5: Kontrolle**



Prüfen Sie, ob alles funktioniert:



```bash
mostro-cli --help
```



Sie sollten die vollständige Liste der Aufträge sehen.



![Vérification avec --help](assets/fr/04.webp)



#### Unter Linux (Ubuntu/Debian)



Die Installation ist identisch mit macOS, mit dem Zusatz von :



```bash
sudo apt update
sudo apt install -y cmake build-essential pkg-config
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Führen Sie dann die Schritte 3 und 4 im Abschnitt macOS aus.



#### Unter Windows



Installieren Sie zunächst Rust über [rustup.rs] (https://rustup.rs/), dann verwenden Sie PowerShell :



```powershell
git clone https://github.com/MostroP2P/mostro-cli.git
cd mostro-cli
cargo build --release
```



Identische Konfiguration: Kopieren Sie `.env-sample` nach `.env` und tragen Sie Ihre Parameter ein.



### Installation von Mostro Mobile



#### Auf Android



**Schritt 1**: Gehen Sie zur [GitHub-Releaseseite] (https://github.com/MostroP2P/mobile/releases) und laden Sie die Datei **app-release.apk** (ca. 65 MB) herunter.



![Page GitHub Releases](assets/fr/10.webp)



**Schritt 2: Nach dem Herunterladen öffnen Sie die APK-Datei aus Ihren Downloads. Android wird Sie auffordern, die Installation aus dieser Quelle zu autorisieren.



![Téléchargement et installation APK](assets/fr/11.webp)



**Schritt 3**: Folgen Sie den Einführungsbildschirmen, auf denen die Funktionen vorgestellt werden:




- Handeln Sie Bitcoin frei - ohne KYC** : Handel ohne Identitätsprüfung dank Nostr
- Standardmäßig Datenschutz**: Wählen Sie zwischen dem Reputationsmodus und dem Modus für vollständigen Datenschutz
- Sicherheit bei jedem Schritt**: Schutz durch Rechnungen mit Sperrvermerk



![Écrans d'accueil Mostro](assets/fr/12.webp)



**Schritt 4**: Fahren Sie mit dem Onboarding fort und entdecken Sie :




- Vollständig verschlüsselter Chat**: Ende-zu-Ende-verschlüsselte Kommunikation
- Nehmen Sie ein Angebot**: Blättern Sie im Auftragsbuch und wählen Sie ein Angebot
- Sie können nicht finden, was Sie brauchen?** : Erstellen Sie Ihre eigene individuelle Bestellung



![Suite onboarding](assets/fr/13.webp)



**Schritt 5: Sobald das Onboarding abgeschlossen ist, generiert die App automatisch ein Paar Nostr-Schlüssel. Gehen Sie zum Menü (☰) und dann **Konto**, um Ihre **Geheimwörter** (Wiederherstellungsphrase) zu speichern. Auf diesem Bildschirm haben Sie auch die Möglichkeit, den bereits erwähnten Datenschutzmodus zu ändern.



![Menu et sauvegarde des clés](assets/fr/15.webp)



**Wichtig**: Notieren Sie sich Ihre Wiederherstellungsphrase an einem sicheren Ort (Passwortmanager, Papiersafe).



### Erste Sicherheitskonfiguration



Welche Plattform Sie auch immer verwenden:





- Dedizierter Schlüssel**: Verwenden Sie eine separate Nostr-Identität für den Handel
- Kleine Beträge**: Beginnen Sie mit weniger als 10.000 sats, um den Einstieg zu schaffen
- Mehrere Relais**: Konfigurieren Sie 3-5 geografisch verteilte Relais
- Netzwerkschutz**: Aktivieren Sie VPN oder Tor, um Ihre IP-Adresse zu verbergen
- Wallet sicher**: Aktivieren Sie die automatische Verriegelung Ihres wallet Lightning



## Verwendung mit CLI



In diesem Abschnitt wird der Kauf von Bitcoins über Mostro CLI anhand eines realen Anwendungsfalls demonstriert.



### Schritt 1: Liste der verfügbaren Aufträge



Mit dem Befehl `listorders` werden alle aktiven Aufträge angezeigt:



```bash
mostro-cli listorders
```



Sie sehen eine Tabelle mit Details zu jeder Bestellung: ID, Art (Kauf/Verkauf), Betrag, Währung, Zahlungsmethode.



![Liste des ordres disponibles](assets/fr/05.webp)



In diesem Beispiel ist ein Auftrag zum Verkauf von 5 EUR über Revolut sichtbar (ID: `305a59d0-dbee-4880-9b9a-44a60486ba4a`).



### Schritt 2: Entgegennahme der Bestellung



Um diese Bitcoins zu kaufen, nehmen Sie die Bestellung mit `takesell` auf:



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



Mostro wird Sie bitten, eine **Blitzrechnung** vorzulegen, um die BTC zu erhalten. Der genaue Betrag in Satoshis ist angegeben (hier: 4715 sats).



![Prise d'ordre de vente](assets/fr/06.webp)



### Schritt 3: Legen Sie Ihre Lightning-Rechnung vor



Erstellen Sie mit Ihrem wallet (Phoenix, Breez usw.) eine Blitzrechnung über den genauen Betrag, und senden Sie sie ab:



```bash
mostro-cli takesell -o 305a59d0-dbee-4880-9b9a-44a60486ba4a --invoice lnbc47150n1p...
```



Das System bestätigt die Sendung und weist Sie darauf hin, dass Sie warten sollen, bis der Verkäufer die Sperrrechnung bezahlt hat, bevor Sie das Treuhandkonto aktivieren.



![Envoi de la Lightning invoice](assets/fr/07.webp)



### Schritt 4: Kontaktaufnahme mit dem Verkäufer



Sobald das Treuhandkonto aktiviert ist, verwenden Sie `dmtouser`, um die Zahlungsdaten vom Verkäufer anzufordern:



```bash
mostro-cli dmtouser --pubkey 7100aed1b44819555b34f90a6ca8dbb7263526e0c580f5ee35fe20d7b0644ae4 \
--orderid 305a59d0-dbee-4880-9b9a-44a60486ba4a \
--message "Hey what's your revtag ?"
```



![Communication avec le vendeur](assets/fr/08.webp)



### Schritt 5: Abrufen der Antwort



Überprüfen Sie die Direktnachrichten, um die Antwort des Verkäufers zu sehen:



```bash
mostro-cli getdm
```



Der Verkäufer gibt Ihnen seine Zahlungs-ID (hier sein Revtag: `@satoshi`).



![Réception de la réponse](assets/fr/09.webp)



### Schritt 6: Durchführung der Fiat-Zahlung



Senden Sie die Zahlung über die vereinbarte Methode (in diesem Beispiel Revolut) an die angegebenen Kontaktdaten. **Bewahren Sie alle Belege** (Screenshots, Transaktionsreferenzen) auf.



### Schritt 7: Bestätigung des Zahlungsversands



Sobald die Zahlung erfolgt ist, benachrichtigen Sie Mostro:



```bash
mostro-cli fiatsent -o 305a59d0-dbee-4880-9b9a-44a60486ba4a
```



### Schritt 8: Erhalt der Bitcoins



Sobald der Verkäufer den Erhalt des Fiatbetrages bestätigt und das Treuhandkonto mit dem Befehl `release` freigibt, erhalten Sie Ihre Bitcoins sofort auf der von Ihnen angegebenen Lightning-Rechnung.



### Schritt 9: Bewertung



Bewerten Sie den Verkäufer, um zur dezentralen Reputation beizutragen:



```bash
mostro-cli rate -o 305a59d0-dbee-4880-9b9a-44a60486ba4a -r 5
```



### Nützliche Befehle



**Eine Bestellung stornieren** (bevor sie angenommen wird) :


```bash
mostro-cli cancel -o <order-id>
```



**Einen neuen Kundenauftrag anlegen** :


```bash
mostro-cli neworder -k sell -c eur -f 20 -m "Revolut" -p 2
```



**Einen Streitfall eröffnen** :


```bash
mostro-cli dispute -o <order-id>
```



## Verwendung mit der mobilen Anwendung



In diesem Abschnitt wird der Verkauf von Bitcoins über Mostro Mobile anhand eines realen Anwendungsfalls demonstriert.



### Interface Haupt



Die Anwendung hat 3 Hauptregisterkarten:





- Auftragsbuch**: Verfügbare Kauf- (BUY BTC) und Verkaufsaufträge (SELL BTC) durchsuchen
- Meine Trades**: Ansicht Ihrer aktiven und historischen Aufträge
- Chat**: Kommunizieren Sie mit Ihren Gesprächspartnern anhand von Zahlen



![Interface principale](assets/fr/14.webp)



### Empfohlene Konfiguration



Bevor Sie handeln, nehmen Sie einige Einstellungen über das Menü (☰) > **Einstellungen** vor:





- Lightning Address** (optional): Um Zahlungen direkt zu erhalten
- Relais**: Hinzufügen mehrerer Nostr-Relais für Ausfallsicherheit (z.B. `wss://nos.lol`, `wss://relay.damus.io`)
- Mostro Pubkey**: Überprüfen Sie den öffentlichen Schlüssel der Mostro-Instanz, die Sie verwenden



![Paramètres de l'application](assets/fr/16.webp)



**Wichtig für die CLI/Mobil-Synchronisierung**: Wenn Sie sowohl den CLI als auch die mobile App verwenden, konfigurieren Sie **exakt die gleichen Nostr-Relais und Mostro Pubkey** in beiden Clients. Ohne diese identische Konfiguration werden Sie nicht die gleichen Aufträge auf beiden Schnittstellen sehen. Die Relais und der Mostro-Pubkey, die in den Einstellungen (Screenshot oben) sichtbar sind, müssen mit denen in der "env"-Datei Ihres CLI übereinstimmen.



### Schritt 1: Erstellen Sie einen Verkaufsauftrag



Drücken Sie die grüne Taste **"+"** unten rechts und wählen Sie dann **Verkaufen** (rote Taste).



![Boutons de création d'ordre](assets/fr/17.webp)



Füllen Sie das Erstellungsformular aus:



1. **Währung**: Wählen Sie die Währung, die Sie erhalten möchten (EUR, USD, usw.)


2. **Betrag** : Geben Sie den Betrag in Fiat ein (z. B. 1 bis 3 EUR)


3. **Zahlungsmethoden** : Wählen Sie die Methode (z.B. "Revolut")


4. **Preistyp**: Wählen Sie "Marktpreis"


5. **Aufschlag**: Prämie anpassen (Schieberegler von -10% bis +10%, empfohlen: 0% für schnellen Verkauf)



Drücken Sie **Senden**, um Ihre Bestellung zu veröffentlichen.



### Schritt 2: Bestätigung der Veröffentlichung



Ihre Bestellung ist jetzt veröffentlicht! Er wird 24 Stunden lang verfügbar sein. Sie können ihn jederzeit stornieren, bevor ein Käufer ihn annimmt, indem Sie den Befehl `cancel` ausführen.



![Ordre publié](assets/fr/18.webp)



Der Auftrag erscheint auf der Registerkarte **Meine Geschäfte** mit dem Status "Ausstehend" und dem Vermerk "Von Ihnen erstellt".



### Schritt 3: Ein Käufer nimmt Ihre Bestellung entgegen



Wenn ein Käufer Ihre Bestellung annimmt, erhalten Sie eine Benachrichtigung. Siehe Details in **Meine Trades**.



![Ordre pris par un acheteur](assets/fr/19.webp)



**Wichtige Anweisung**: Sie müssen jetzt **die angezeigte Hold-Rechnung** bezahlen, um Ihre Bitcoins (hier 4674 sats für 1-5 EUR) im Treuhandkonto zu sperren. Sie haben **maximal 15 Minuten** Zeit, sonst wird der Tausch abgebrochen.



Kopieren Sie die vorgehaltene Rechnung und bezahlen Sie sie mit Ihrem wallet Lightning (Phoenix, Breez, etc.).



### Schritt 4: Kommunizieren Sie mit dem Käufer



Sobald das Treuhandkonto aktiviert ist, drücken Sie **CONTACT**, um den verschlüsselten Chat mit dem Käufer zu öffnen.



Der Käufer (hier "anonymous-gloriaZhao") wird sich mit Ihnen in Verbindung setzen, um Ihre Zahlungsdaten anzufordern. Bitte antworten Sie mit Ihren Angaben (Revtag, IBAN, etc.).



![Chat avec l'acheteur](assets/fr/20.webp)



### Schritt 5: Erhalt der Fiat-Zahlung



Warten Sie, bis Sie die Fiat-Zahlung auf Ihrem Revolut-Konto (oder einer anderen vereinbarten Methode) erhalten. **Prüfen Sie sorgfältig**:




- Der genaue Betrag
- Der Absender
- Die Referenz, falls gewünscht



Der Käufer wird Sie per Chat darüber informieren, dass er die Zahlung abgeschickt hat. Mostro wird auch eine Nachricht anzeigen, die bestätigt, dass die Fiat an Sie gesendet wurden.



![Confirmation d'envoi du paiement](assets/fr/20.webp)



### Schritt 6: Freigabe des Treuhandkontos



Sobald Sie den Eingang der Zahlung auf Ihrem Konto **bestätigt** haben, drücken Sie die grüne Taste **Freigeben** und bestätigen Sie, um die Ware an den Käufer zu senden.



![Libération de l'escrow](assets/fr/20.webp)



Die Bitcoins werden dem Käufer sofort über seine Lightning-Rechnung überwiesen.



### Schritt 7: Bewerten Sie die Überlegungen



Nach der Freigabe drücken Sie **Bewertung**, um den Käufer zu bewerten. Wählen Sie zwischen 1 und 5 Sternen (hier 5/5) und drücken Sie **Bewertung abgeben**.



![Évaluation de la contrepartie](assets/fr/21.webp)



Der Austausch ist beendet!



### Bitcoins kaufen mit der mobilen App



Der Prozess zum **Kauf** von Bitcoins ist ähnlich, aber umgekehrt:



1. Durchsuchen Sie die Registerkarte **Auftragsbuch** > **BUY BTC**, um Verkaufsaufträge anzuzeigen


2. Klicken Sie auf einen interessanten Auftrag, um Details zu sehen


3. Drücken Sie **Bestellung aufnehmen**


4. Legen Sie Ihre Lightning-Rechnung vor (generiert von Ihrem wallet)


5. Warten Sie darauf, dass der Verkäufer das Treuhandkonto aktiviert


6. Kontaktieren Sie den Verkäufer über **CONTACT** für die Zahlungsmodalitäten


7. Fiat-Zahlung senden (Nachweis aufbewahren)


8. Verkäufer gibt Treuhandkonto nach Überprüfung frei


9. Erhalten Sie Bitcoins sofort auf Ihre Lightning-Rechnung


10. Bewerten Sie den Verkäufer (1-5 Sterne)



### Management von Problemen



**Auftrag stornieren**: Drücken Sie in **My Trades** auf Ihre Order und dann auf die Schaltfläche **CANCEL** (nur verfügbar, bevor die Order ausgeführt wird).



**Einen Streitfall eröffnen**: Im Falle einer Unstimmigkeit drücken Sie **DISPUTE** in den Bestelldetails. Fügen Sie alle Beweise bei (Chat-Screenshots, Hinweise auf Banktransaktionen).



## Vorteile und Grenzen



### Vorteile



**Finanzielle Souveränität**: Ihre Bitcoins verlassen dank des Hold-Invoice-Mechanismus nie Ihre direkte Kontrolle, wodurch das Risiko eines Konkurses oder einer Piraterie ausgeschlossen wird.



**Zensurresistent**: Keine Behörde kann das Netz abschalten oder Ihre Aufträge zensieren. Das System funktioniert, solange die Nostr-Relais in Betrieb sind.



**Standardanonymität**: Nur ein pseudonymer Nostr-Schlüssel identifiziert Sie, ohne KYC oder persönliche Daten. End-to-End verschlüsselte Kommunikation.



**Flexibilität bei der Bezahlung**: Jede von beiden Seiten akzeptierte Zahlungsmethode ist möglich (Überweisungen, mobile Apps, Bargeld, Tauschhandel).



### Beschränkungen



**Frühe Entwicklung**: Rudimentäre Schnittstellen und technische Lernkurve erforderlich.



**Beschränkte Liquidität**: Begrenzte Anzahl von Aufträgen, insbesondere bei großen Beträgen oder seltenen Währungen.



**Technische Anforderungen**: Grundkenntnisse in Lightning und Nostr erforderlich.



**Einzelne Verantwortung**: Keine zentralisierte Unterstützung bei Problemen, Vorsicht geboten.



## Schlussfolgerung



Mostro P2P stellt eine vielversprechende Alternative zu zentralisierten Börsen dar und kombiniert Lightning Network, Nostr und automatisierte Treuhand für einen wirklich dezentralen Handel. Trotz der frühen Entwicklung und der begrenzten Liquidität bietet die Plattform bereits finanzielle Souveränität, Zensurresistenz und standardmäßige Anonymität.



Für Bitcoiner, die Autonomie und Vertraulichkeit bevorzugen, ist Mostro eine brauchbare Option, die es wert ist, weiter erforscht zu werden. Seine dezentralisierte Architektur garantiert eher eine gemeinschaftliche als eine kommerzielle Entwicklung und ebnet den Weg für eine Zukunft mit wirklich freien Bitcoin-Börsen.



## Ressourcen



### Offizielle Dokumentation




- [Mostro offizielle Website](https://mostro.network)
- [Technische Dokumentation] (https://mostro.network/docs-english/index.html)
- [Stiftung Mostro](https://mostro.foundation)



### Quellcode und Entwicklung




- [Haupt-GitHub-Repository](https://github.com/MostroP2P/mostro)
- [Web-Client] (https://github.com/MostroP2P/mostro-web)
- [Kunde CLI](https://github.com/MostroP2P/mostro-cli)



### Gemeinschaft




- [Nostr-Protokoll](https://nostr.com)
- [Lightning Network Leitfaden](https://lightning.network)