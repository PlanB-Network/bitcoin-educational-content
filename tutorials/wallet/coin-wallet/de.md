---
name: Coin Wallet
description: Tutorial über Coin Wallet und Möglichkeiten zur Verbesserung von Datenschutz und Sicherheit
---

![cover](assets/cover.webp)


Dieses Tutorial behandelt [Coin Wallet](https://coin.space/) - ein selbstverwahrendes Krypto-wallet für mobile Geräte, und wie man die Sicherheit und den Datenschutz bei der Verwendung von mobilen wallet-Anwendungen erhöht.



## Über Coin Wallet


**Coin Wallet** ist ein Open-Source-wallet, der 2015 von einem Team von Bitcoin-Enthusiasten entwickelt wurde und sich selbst verwaltet bzw. nicht verwaltet. Es begann als Webanwendung, gefolgt von der iOS-App im Jahr 2017 und der Android-App im Jahr 2020 - verfügbar auf Google Play, Samsung Galaxy Store und Huawei AppGallery.


Die wichtigsten Vorteile:


- Architektur ohne Freiheitsentzug
- Vollständig [Open-Source-Code](https://github.com/CoinSpace/CoinSpace/blob/master/LICENSE)
- Einfaches und klares Design
- Fokussiert auf den Hauptzweck - sichere Speicherung von Kryptowährungen, ohne unnötige Funktionen
- Plattformübergreifende Unterstützung: Mobil (iOS & Android), Desktop, Web
- RBF (Replace-By-Fee)-Unterstützung - beschleunigen Sie festsitzende Transaktionen zu jeder Zeit
- Hardware 2FA mit [YubiKey](https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/) / FIDO2 Schlüssel
- Integrierte Tor-Unterstützung - leiten Sie den gesamten Datenverkehr durch das Tor-Netzwerk für maximale Privatsphäre



## 1️⃣ Installation von Coin Wallet

Coin Wallet ist auf allen wichtigen Plattformen verfügbar.



- [iOS App Store](https://apps.apple.com/app/coin-wallet-bitcoin-crypto/id980719434)



- [Android Google Play](https://play.google.com/store/apps/details?id=com.coinspace.app)



- [Android (Galaxy Store)](https://galaxystore.samsung.com/detail/com.coinspace.app)



- [Android (Huawei AppGallery)](https://appgallery.huawei.com/app/C112183767)



- [Android (Uptodown)](https://coin-wallet.en.uptodown.com/android)



- [Android APK](https://coin.space/api/v3/download/android-apk/any)



- [Alle Freigabelinks](https://github.com/CoinSpace/CoinSpace/releases)


Auch für den Desktop (Windows, Linux, macOS), als Web-App und über Tor verfügbar.


![image](assets/en/01.webp)


## 2️⃣ Erstellen eines Wallet und Festlegen der PIN


Ein wallet wird mit Hilfe eines passphrase erstellt - einer zufälligen Folge von 12 durch Leerzeichen getrennten Wörtern, die aus einer [Liste von 2048 Wörtern](https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts) generiert wird.

Coin Wallet unterstützt Passphrasen mit 12, 15, 18, 21 oder 24 Wörtern, die von anderen Geldbörsen importiert werden.


Die passphrase ist die für Menschen lesbare Form des privaten Hauptschlüssels. Er muss sicher gespeichert werden. Der passphrase ist alles, was benötigt wird, um auf den wallet zuzugreifen oder ihn wiederherzustellen. Wenn die passphrase verloren geht, sind die wallet und alle Gelder dauerhaft verloren. Der passphrase darf niemals weitergegeben werden. Coin Wallet speichert keine Schlüssel auf einem Server oder in einer Datenbank.


**Ist ein passphrase mit 12 Wörtern sicher?

Bei 2048 möglichen Wörtern pro Position gibt es 2048¹² ≈ 10³⁹ Kombinationen - das ergibt ~128 Bit Sicherheit, vergleichbar mit Bitcoin privaten Schlüsseln. Dieses Niveau wird allgemein als ausreichend angesehen.


![image](assets/en/02.webp)


Nachdem die passphrase aufgeschrieben und bestätigt wurde, fordert die App dazu auf, eine **4-stellige PIN** für den täglichen Zugang festzulegen. Für zusätzlichen Komfort können Sie die biometrische Authentifizierung (Fingerabdruck oder Gesichtserkennung) anstelle einer PIN aktivieren.


![image](assets/en/03.webp)



Es gibt kein Konto, keine Schlüsselwiederherstellung, kein Zurücksetzen von passphrase und keine Rückgängigmachung von Transaktionen. Die Sicherheit liegt in der vollen Verantwortung des Nutzers.


Ausführliche Best Practices zum Speichern der mnemonischen Phrase:


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 3️⃣ Passphrase + PIN. Wann und wie sie verwendet werden


**Wann wird der passphrase benötigt?**

Nur in diesen seltenen Fällen:


- Einrichten des wallet auf einem neuen Gerät
- Neuinstallation der Anwendung Coin Wallet
- Löschen der App-/Browserdaten (Lokaler Speicher)
- Entfernen eines Hardwareschlüssels aus dem Konto
- Dreimalige Eingabe der falschen PIN (die App wird zur Sicherheit gesperrt)


Im täglichen Gebrauch reicht die 4-stellige PIN aus, um das wallet zu entsperren.


**Passphrase + PIN: So funktioniert es**

Der passphrase ist der echte private Hauptschlüssel und funktioniert auf jedem Gerät.

Da die Eingabe von 12-24 Wörtern jedes Mal umständlich wäre, verwendet Coin Wallet eine 4-stellige PIN für den schnellen, täglichen Zugriff auf das aktuelle Gerät.

Eine einfache PIN allein ist nicht sicher genug, um den Hauptschlüssel direkt zu schützen, daher wird sie nie zur Verschlüsselung verwendet. Stattdessen:



- Die PIN wird an den Server gesendet und gegen ein langes kryptografisches token ausgetauscht.
- Dieser token entschlüsselt den verschlüsselten Hauptschlüssel, der nur auf dem Gerät gespeichert ist.


Wenn die PIN dreimal falsch eingegeben wird, löscht der Server das token dauerhaft. Der lokal gespeicherte Schlüssel wird unbrauchbar, und die einzige Möglichkeit, das wallet wiederherzustellen, besteht in der Eingabe des ursprünglichen passphrase.

Diese Konstruktion bietet sowohl Bequemlichkeit als auch einen starken Ausweichschutz.



## 4️⃣ Empfang von ₿itcoin - Address Arten und Datenschutz


Coin Wallet unterstützt alle drei Bitcoin-Adressformate:



- Native SegWit (Bech32)** - beginnt mit **bc1q** - niedrigste Gebühren, empfohlen
- Verschachtelte SegWit (P2SH)** - beginnt mit **3**
- Legacy (P2PKH)** - beginnt mit **1**


![image](assets/en/04.webp)


**Warum ändert sich die Adresse nach jeder Einzahlung?**

Dies ist beabsichtigt und dient dem Schutz der Privatsphäre. Jedes Mal, wenn Münzen empfangen werden, generiert Coin Wallet automatisch eine neue, nicht verwendete Adresse. Wenn dieselbe Adresse wiederverwendet würde (z. B. für das monatliche Gehalt), könnte jeder leicht alle eingehenden Transaktionen auf einem Blockchain-Explorer zusammenzählen und das Gesamteinkommen kennen.


Alte Adressen bleiben für immer gültig - Sie können sie weiterhin empfangen - aber es wird empfohlen, jedes Mal eine neue Adresse zu verwenden, um den Datenschutz zu gewährleisten.


**Wie man Bitcoin erhält:**

1. Öffnen Sie die Münze

2. Tippen Sie auf **Empfangen**

3. Wählen Sie den gewünschten Adresstyp (vorzugsweise **bc1q** - "Native SegWit")

4. Zeigen Sie den QR-Code oder kopieren Sie die Adresse und senden Sie sie an den Zahler


**Optional - Mecto (für persönliche Zahlungen):**

Auf demselben Bildschirm "Empfangen" gibt es eine Schaltfläche "Mecto".

Wenn Sie es einschalten:


- Sie werden aufgefordert, einen **Nickname** (Gravatar) einzugeben
- Ihr aktueller Standort und Ihre Empfangsadresse werden vorübergehend mit anderen Coin Wallet-Nutzern geteilt, die ebenfalls Mecto aktiviert haben
- Sie können dich auf einer kleinen Karte entdecken und Münzen verschicken, ohne zu tippen oder zu scannen


Die Daten sind nur für andere Mecto-Benutzer sichtbar und werden automatisch nach 1 Stunde gelöscht (oder sofort, wenn Sie sie ausschalten).

Mecto ist völlig optional - lassen Sie es aus, wenn Sie maximale Privatsphäre wünschen.


![image](assets/en/05.webp)


## 5️⃣ Senden ₿itcoin


Zum Senden von Bitcoin:


1. Öffnen Sie die Münze → tippen Sie auf **Senden**

2. Fügen Sie die Adresse ein oder scannen Sie den QR-Code

3. Betrag eingeben (oder **Max** antippen)

4. Wählen Sie die Transaktionsgeschwindigkeit:


| Speed   | Approx. confirmation time | Fee level     |
|---------|---------------------------|---------------|
| **Slow**    | ~120 minutes              | Lowest
| **Default** | ~60 minutes               | Medium
| **Fast**    | ~20 minutes               | Higher

5. Bestätigen Sie mit Ihrer 4-stelligen PIN → Transaktion wird übertragen


### Wie man eine ausstehende ₿itcoin-Transaktion beschleunigt (RBF)


Wenn Sie eine langsame Gebühr gewählt haben und die Transaktion stecken bleibt:


1. Gehen Sie zur Registerkarte **Geschichte**

2. Tippen Sie auf die ausstehende Transaktion

3. Gewindebohrer **Beschleunigen** (Replace-By-Fee)

4. Bestätigen → die Transaktion wird mit einer höheren Gebühr erneut übertragen


Die RBF-Beschleunigung wird derzeit unterstützt für:

Bitcoin - Avalanche - Binance Smart Chain - Ethereum - Ethereum Classic - Polygon


Mehr über Replace-by-fee (RBF): https://bitcoinops.org/en/topics/replace-by-fee/


## 6️⃣ Exportieren von privaten Schlüsseln


**Wann braucht man eigentlich einen privaten Schlüssel?

(99 % der Nutzer tun dies nie - das 12-Wörter-passphrase reicht aus)


| Situation                                      | Why you need the private key                     |
|------------------------------------------------|--------------------------------------------------|
| Sweeping an old paper wallet                   | To move funds to your current wallet             |
| Importing into a hardware signer (e.g. Coldcard) | For offline signing                              |
| Emergency recovery (lost seed but app still open) | To rescue coins before the app is gone           |
| Using tools that don’t accept seed phrases     | Some watch-only or signing utilities             |

### Wie exportiert man private Schlüssel in Coin Wallet


1. Offen **Bitcoin (BTC)**

2. Scrollen Sie zum unteren Ende der Seite und tippen Sie auf **Private Schlüssel exportieren**

3. Die App zeigt jede Adresse mit Guthaben + ihrem privaten Schlüssel im **WIF**-Format (beginnt mit 5, K oder L) und einem QR-Code.


Es werden nur nicht leere Adressen angezeigt.


**Beispiel WIF-Schlüssel**

`L2v1eK4i9j3k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k3j4k`


**Wie geht es weiter (empfohlen)**


- Öffnen Sie Electrum, Sparrow, BlueWallet oder eine beliebige Hardware wallet
- Privaten Schlüssel importieren/verwenden
- Alle Gelder werden sofort an eine neue sichere Adresse unter Ihrem aktuellen seed übertragen


Speichern Sie den privaten Schlüssel niemals digital im Klartext. Nach dem Sweeping kann er sicher gelöscht werden.


Eine vollständige Anleitung zu privaten Schlüsseln und Ableitungspfaden: [How to Work with Private Keys: The Ultimate Guide](https://coin.space/how-to-work-with-private-keys-the-ultimate-guide/)



## 7️⃣ Technische Details - BIP39, BIP32 und Ableitungspfade


Coin Wallet hält sich streng an die offiziellen Bitcoin-Standards, die von fast allen seriösen Geldbörsen verwendet werden.


bIP39" - wie die passphrase zum privaten Hauptschlüssel wird


- Standardanzahl von Wörtern: 12
- Fakultativ passphrase/Passwort: keine ("")
- Anfangsentropie: 128 Bit (12 Wörter) → 256 Bit (24 Wörter)
- Open-Source-Implementierung: https://github.com/paulmillr/scure-bip39
- Wortliste: standardmäßige englische Liste mit 2048 Wörtern
- Unterstützt den Import von 12-, 15-, 18-, 21- und 24-Wort-Sätzen von jedem anderen BIP39 wallet


bIP32 + BIP44/BIP49/BIP84" - deterministische Erzeugung aller Adressen

Von einem Hauptschlüssel aus kann der wallet generate Milliarden von Adressen in einer streng definierten Reihenfolge abfragen. Aus diesem Grund zeigen dieselben 12 Wörter, die in Electrum, Sparrow, Trezor, Ledger, BlueWallet usw. eingegeben werden, genau dieselben Adressen und Salden an.


**Ableitungspfade, die in Coin Wallet für Bitcoin** verwendet werden


| Address type              | Standard | Derivation path       | Starts with | Comment                              |
|---------------------------|----------|-----------------------|-------------|--------------------------------------|
| Native SegWit (Bech32)    | BIP84    | `m/84'/0'/0'`         | bc1q…       | Modern format, lowest fees           |
| Nested SegWit (P2SH)      | BIP49    | `m/49'/0'/0'`         | 3…          | Compatibility wrapper for old services |
| Legacy (P2PKH)            | BIP44    | `m/44'/0'/0'`         | 1…          | Oldest format, highest fees          |

Innerhalb jedes Pfades:


- /0" - externe Kette (Adressen, die Sie für den Empfang von Zahlungen angeben)
- /1" - interne Kette (Adressen ändern, die der wallet selbst verwendet)


Da Coin Wallet diesen öffentlichen Normen ohne Änderungen folgt, werden Ihre Gelder auch in 10-20-30 Jahren noch in jedem anderen kompatiblen wallet einforderbar sein.


## 8️⃣ Verbesserung der Anonymität mit Tor


**Warum Tor in Coin Wallet** verwenden?

Tor verbirgt deine echte IP-Adresse vor Bitcoin-Knoten, Tauschbörsen und Beobachtern.

Der gesamte Verkehr (Guthaben, Transaktionen, Swaps) läuft über das Tor-Netzwerk - keine direkten Verbindungen, keine IP-Lecks.

Dies ist direkt im Quellcode der Anwendung implementiert (siehe [.env configuration](https://github.com/CoinSpace/CoinSpace/blob/master/web/.env#L31)).


Coin Wallet hat eine versteckte .onion-Adresse und seit v6.6.3 (Dezember 2024) **eingebaute Tor-Unterstützung direkt in der mobilen App**.


### Wie man Tor auf Android und iOS aktiviert


1. **Installiere Orbot** - offizielle Tor-Projekt-App (kostenlos)


   - Android → [Google Play](https://play.google.com/store/apps/details?id=org.torproject.android) / [F-Droid](https://orbot.app/en/)
   - iPhone / iPad → [App Store](https://apps.apple.com/us/app/orbot/id1609461599)


2. **Öffne Orbot → tippe auf Start**

Wähle **Coin Wallet** aus der Liste, damit nur der wallet Tor verwendet (optional, aber empfohlen)

Warten Sie, bis **"Verbunden "** angezeigt wird (10-30 Sekunden)


3. **Öffnen Sie Coin Wallet → Einstellungen → Netzwerk**

Schalte **Tor benutzen** ein


4. **Status prüfen**

Ein **violettes Tor-Zwiebel-Symbol** erscheint in der oberen Leiste → der gesamte Datenverkehr wird nun durch Tor geleitet


![image](assets/en/06.webp)


Das war's - Ihr mobiles Coin Wallet ist vollständig anonymisiert.


Genießen Sie die private Krypto-Verwaltung!


## 📝 Schlussfolgerung


[Coin Wallet](https://coin.space/) - einer der wahren Bitcoin wallet-Pioniere mit einer 10-jährigen Entwicklungsgeschichte.

Es ist bewusst einfach gehalten und konzentriert sich auf seine Kernaufgabe: die sichere Aufbewahrung Ihrer Kryptowährung.

Es gibt keine Werbung, keinen News-Feed, keine Abonnements, keine sozialen Funktionen, keine Ablenkungen - nur einen sauberen, schnellen, selbsterklärenden wallet, der genau das tut, was er tun soll.

Coin Bei Wallet stehen Einfachheit und Sicherheit an erster Stelle - das war schon immer so und wird auch so bleiben.


## 📖 Ressourcen


https://coin.space/


https://support.coin.space/hc/en-us


https://en.bitcoin.it/wiki/Wallet


https://bitcoinops.org/


https://github.com/CoinSpace/CoinSpace/


https://www.yubico.com/works-with-yubikey/catalog/coin-wallet/


https://github.com/paulmillr/scure-bip39/blob/main/src/wordlists/english.ts


https://github.com/paulmillr/scure-bip39