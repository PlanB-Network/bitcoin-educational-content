---
term: OUTPUT SCRIPT DESCRIPTORS
---

Output Script Descriptors, oder einfach nur Descriptors, sind strukturierte Ausdrücke, die ein Ausgabeskript (`scriptPubKey`) vollständig beschreiben und alle notwendigen Informationen liefern, um Transaktionen zu oder von einem bestimmten Skript zu verfolgen. Diese Descriptors erleichtern die Verwaltung von Schlüsseln in HD-Wallets durch eine standardisierte Beschreibung der Struktur und der verwendeten Adresstypen.

Das Hauptinteresse an Descriptors liegt in ihrer Fähigkeit, alle wesentlichen Informationen zur Wiederherstellung eines Wallets in einer einzigen Zeichenkette zu kapseln (zusätzlich zur Wiederherstellungsphrase). Durch das Speichern eines Descriptors mit den entsprechenden mnemonischen Phrasen ist es möglich, nicht nur die privaten Schlüssel, sondern auch die genaue Struktur des Wallets und die zugehörigen Skriptparameter wiederherzustellen. Tatsächlich erfordert die Wiederherstellung eines Wallets nicht nur die Kenntnis des ursprünglichen Seeds, sondern auch spezifische Indizes für die Ableitung von Kind-Schlüsselpaaren sowie den `xpub` jedes Faktors im Falle eines Multisig-Wallets. Früher wurde angenommen, dass diese Informationen implizit von allen bekannt waren. Jedoch könnte mit der Diversifizierung von Skripten und dem Aufkommen komplexerer Konfigurationen diese Information schwer zu extrapolieren sein, wodurch diese Daten zu privaten und schwer zu brute-force Informationen werden. Die Verwendung von Descriptors vereinfacht den Prozess erheblich: Es genügt, die Wiederherstellungsphrase(n) und den entsprechenden Descriptor zu kennen, um alles zuverlässig und sicher wiederherzustellen.

Ein Descriptor besteht aus mehreren Elementen:
* Skriptfunktionen wie `pk` (Pay-to-PubKey), `pkh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-Witness-Script-Hash), `tr` (Pay-to-Taproot), `multi` (Mehrfachsignatur) und `sortedmulti` (Mehrfachsignatur mit sortierten Schlüsseln);
* Ableitungspfade, zum Beispiel `[d34db33f/44h/0h/0h]`, die einen abgeleiteten Pfad und einen spezifischen Master-Schlüssel-Fingerabdruck anzeigen;
* Schlüssel in verschiedenen Formaten wie hexadezimale öffentliche Schlüssel oder erweiterte öffentliche Schlüssel (`xpub`);
* Eine Prüfsumme, vorangestellt von einem Hash, um die Integrität des Descriptors zu überprüfen.

Ein Beispiel für einen Descriptor für ein P2WPKH-Wallet könnte so aussehen:

```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```
In diesem Descriptor zeigt die Ableitungsfunktion `wpkh` einen Pay-to-Witness-Public-Key-Hash-Skripttyp an. Es folgt der Ableitungspfad, der enthält:
* `cdeab12f`: der Fingerabdruck des Master-Schlüssels;
* `84h`: was die Verwendung eines BIP84-Zwecks anzeigt, bestimmt für SegWit v0-Adressen;
* `0h`: was darauf hinweist, dass es sich um eine BTC-Währung im Hauptnetz handelt;
* `0h`: was sich auf die spezifische Kontonummer bezieht, die im Wallet verwendet wird.

Der Descriptor enthält auch den erweiterten öffentlichen Schlüssel, der in diesem Wallet verwendet wird:
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U

Als Nächstes gibt die Notation `/<0;1>/*` an, dass der Deskriptor Adressen von der externen (`0`) und internen (`1`) Kette generieren kann, wobei das Wildcard-Symbol (`*`) die sequenzielle Ableitung mehrerer Adressen in einer konfigurierbaren Weise ermöglicht, ähnlich der Verwaltung eines "Gap-Limits" in traditioneller Wallet-Software.

Schließlich repräsentiert `#jy0l7nr4` die Prüfsumme, um die Integrität des Deskriptors zu verifizieren.