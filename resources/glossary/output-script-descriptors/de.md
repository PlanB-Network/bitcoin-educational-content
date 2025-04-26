---
term: OUTPUT-SKRIPT-DESKRIPTOREN

---
Ausgabeskript-Deskriptoren, oder einfach Deskriptoren, sind strukturierte Ausdrücke, die ein Ausgabeskript (`scriptPubKey`) vollständig beschreiben und alle notwendigen Informationen liefern, um Transaktionen zu oder von einem bestimmten Skript zu verfolgen. Diese Deskriptoren erleichtern die Verwaltung von Schlüsseln in HD-Wallets durch eine Standardbeschreibung der Struktur und der verwendeten Adresstypen.

Das Hauptinteresse der Deskriptoren liegt in ihrer Fähigkeit, alle wesentlichen Informationen für die Wiederherstellung einer Geldbörse in einer einzigen Zeichenkette zu kapseln (zusätzlich zur Wiederherstellungsphrase). Durch das Speichern eines Deskriptors mit den entsprechenden mnemonischen Phrasen ist es möglich, nicht nur die privaten Schlüssel, sondern auch die genaue Struktur der Brieftasche und die zugehörigen Skriptparameter wiederherzustellen. Die Wiederherstellung einer Brieftasche erfordert nämlich nicht nur die Kenntnis des ursprünglichen Seed, sondern auch spezifische Indizes für die Ableitung von Child-Key-Paaren sowie den "xpub" jedes Faktors im Falle einer Multisig-Brieftasche. Bisher wurde davon ausgegangen, dass diese Informationen allen implizit bekannt sind. Mit der Diversifizierung von Skripten und dem Aufkommen komplexerer Konfigurationen könnten diese Informationen jedoch schwer zu extrapolieren sein, wodurch diese Daten zu privaten und schwer zu erzwingenden Informationen werden. Die Verwendung von Deskriptoren vereinfacht den Prozess erheblich: Es reicht aus, die Wiederherstellungsphrase(n) und den entsprechenden Deskriptor zu kennen, um alles zuverlässig und sicher wiederherzustellen.

Ein Deskriptor besteht aus mehreren Elementen:


- Skriptfunktionen wie `pk` (Pay-to-PubKey), `pkh` (Pay-to-PubKey-Hash), `wpkh` (Pay-to-Witness-PubKey-Hash), `sh` (Pay-to-Script-Hash), `wsh` (Pay-to-Witness-Script-Hash), `tr` (Pay-to-Taproot), `multi` (Multisignatur), und `sortedmulti` (Multisignatur mit sortierten Schlüsseln);
- Ableitungspfade, z. B. "d34db33f/44h/0h/0h", die einen abgeleiteten Pfad und einen bestimmten Hauptschlüssel-Fingerabdruck angeben;
- Schlüssel in verschiedenen Formaten wie hexadezimale öffentliche Schlüssel oder erweiterte öffentliche Schlüssel (xpub);
- Eine Prüfsumme, der ein Hash-Wert vorangestellt ist, um die Integrität des Deskriptors zu überprüfen.

Ein Deskriptor für eine P2WPKH-Geldbörse könnte zum Beispiel so aussehen:

```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17
C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7n
r4
```

In diesem Deskriptor bezeichnet die Ableitungsfunktion "wpkh" einen Pay-to-Witness-Public-Key-Hash-Skripttyp. Es folgt der Ableitungspfad, der Folgendes enthält:


- cdeab12f": der Fingerabdruck des Hauptschlüssels;
- 84h": Dies bedeutet die Verwendung eines BIP84-Zwecks, der für SegWit v0-Adressen bestimmt ist;
- 0h": Das bedeutet, dass es sich um eine BTC-Währung im Mainnet handelt;
- 0h": bezieht sich auf die spezifische Kontonummer, die in der Brieftasche verwendet wird.

Der Deskriptor enthält auch den erweiterten öffentlichen Schlüssel, der in dieser Brieftasche verwendet wird:

```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6
cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```

Als nächstes gibt die Notation `/<0;1>/*` an, dass der Deskriptor Adressen aus der externen (`0`) und internen (`1`) Kette generieren kann, wobei ein Platzhalter (`*`) die sequentielle Ableitung mehrerer Adressen auf konfigurierbare Weise ermöglicht, ähnlich der Verwaltung eines "Gap-Limits" bei herkömmlicher Wallet-Software.

Schließlich steht "#jy0l7nr4" für die Prüfsumme, mit der die Integrität des Deskriptors überprüft wird.