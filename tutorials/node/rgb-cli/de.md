---
name: RGB-CLI
description: Wie erstelle und tausche ich Smart Contracts auf RGB?
---
![cover](assets/cover.webp)

In diesem Tutorial werden wir Schritt für Schritt die Erstellung eines Vertrags mit Hilfe des Kommandozeilen-Tools "rgb" der LNP/BP Association nachvollziehen. Ziel ist es, zu zeigen, wie man die CLI installiert und manipuliert, ein Schema kompiliert, die Schnittstelle und die Schnittstellenimplementierung importiert und dann ein RGB-Asset ausgibt. Wir werden uns auch die zugrundeliegende Logik ansehen, einschließlich Kompilierung und Zustandsvalidierung. Am Ende dieses Tutorials sollten Sie in der Lage sein, den Prozess zu reproduzieren und Ihre eigenen RGB-Verträge zu erstellen.

## RGB-Protokoll-Erinnerung

RGB ist ein Protokoll, das auf Bitcoin läuft und Smart-Contract-Funktionen sowie die Verwaltung digitaler Vermögenswerte emuliert, ohne die Blockchain, auf der es basiert, zu überlasten. Im Gegensatz zu herkömmlichen On-Chain-Smart-Contracts (wie z. B. bei Ethereum) beruht RGB auf einem "*Client-side validation*"-System: Die meisten Daten und Statusverläufe werden ausschließlich von den beteiligten Teilnehmern ausgetauscht und gespeichert, während die Bitcoin-Blockchain nur kleine kryptografische Verpflichtungen (über Mechanismen wie *Tapret* oder *Opret*) enthält. Im RGB-Protokoll dient die Bitcoin-Blockchain daher nur als Zeitstempel-Server und als System zum Schutz vor Doppelausgaben.

Ein RGB-Vertrag ist wie eine evolutionäre Zustandsmaschine aufgebaut. Er beginnt mit einer Genesis, die den Ausgangszustand (der z. B. das Angebot, den Ticker oder andere Metadaten beschreibt) nach einem streng typisierten und kompilierten Schema definiert. Anschließend werden Zustandsübergänge und gegebenenfalls Zustandserweiterungen angewendet, um diesen Zustand zu ändern oder zu erweitern. Jede Operation, sei es die Übertragung vertretbarer Vermögenswerte (RGB20) oder die Erstellung einzigartiger Vermögenswerte (RGB21), beinhaltet *Single-use Seals*. Diese verknüpfen Bitcoin UTXOs mit Off-Chain-States und verhindern doppelte Ausgaben, während sie gleichzeitig Vertraulichkeit und Skalierbarkeit gewährleisten.

Um mehr über die Funktionsweise des RGB-Protokolls zu erfahren, empfehle ich Ihnen diesen umfassenden Schulungskurs:

https://planb.network/courses/csv402
Die interne Logik von RGB basiert auf Rust-Bibliotheken, die Sie als Entwickler in Ihre Projekte importieren können, um den Teil der *Client-side Validation* zu verwalten. Darüber hinaus arbeitet das LNP/BP-Team an Bindungen für andere Sprachen, was aber noch nicht abgeschlossen ist. Darüber hinaus entwickeln andere Unternehmen wie Bitfinex ihre eigenen Integrationsstacks, aber darüber werden wir in einem anderen Tutorial sprechen. Für den Moment ist das `rgb` CLI die offizielle Referenz, auch wenn es noch relativ unausgereift ist.

## Installation und Vorstellung des CLI-Tools rgb

Der Hauptbefehl heißt einfach `rgb`. Es ist so konzipiert, dass es an `git` erinnert, mit einer Reihe von Unterbefehlen für die Bearbeitung von Verträgen, deren Aufruf, die Ausgabe von Vermögenswerten und so weiter. Bitcoin Wallet ist derzeit noch nicht integriert, wird aber in einer der nächsten Versionen (0.11) integriert sein. Diese nächste Version wird es Nutzern ermöglichen, ihre Wallets (über Deskriptoren) direkt von `rgb` aus zu erstellen und zu verwalten, einschließlich PSBT-Generierung, Kompatibilität mit externer Hardware (z.B. einer Hardware-Wallet) zum Signieren und Interoperabilität mit Software wie Sparrow. Dies wird das gesamte Szenario der Ausgabe und Übertragung von Vermögenswerten vereinfachen.

### Einbau über Cargo

Wir installieren das Tool in Rust mit :

```bash
cargo install rgb-contracts --all-features
```

(Hinweis: Die Kiste heißt `rgb-contracts`, und der installierte Befehl wird `rgb` heißen. Wenn eine Kiste mit dem Namen `rgb` bereits existiert, könnte es eine Kollision gegeben haben, daher der Name)

Die Installation kompiliert eine große Anzahl von Abhängigkeiten (z.B. Befehls-Parsing, Electrum-Integration, Verwaltung von Zero-Knowledge-Proofs usw.).

Sobald die Installation abgeschlossen ist, wird die :

```bash
rgb
```

Wenn Sie `rgb` (ohne Argumente) ausführen, wird eine Liste der verfügbaren Unterbefehle angezeigt, z. B. `Schnittstellen`, `Schema`, `Import`, `Export`, `Ausgabe`, `Rechnung`, `Transfer` usw. Sie können das lokale Speicherverzeichnis (ein Versteck, das alle Protokolle, Schemata und Implementierungen enthält) ändern, das Netzwerk (Testnet, Mainnet) wählen oder Ihren Electrum-Server konfigurieren.

![RGB-CLI](assets/fr/01.webp)

### Erster Überblick über die Kontrollen

Wenn Sie den folgenden Befehl ausführen, werden Sie sehen, dass eine "RGB20"-Schnittstelle bereits standardmäßig integriert ist:

```bash
rgb interfaces
```

Wenn diese Schnittstelle nicht integriert ist, klonen Sie die :

```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```

Kompilieren Sie es:

```bash
cargo run
```

Importieren Sie dann die Schnittstelle Ihrer Wahl:

```bash
rgb import interfaces/RGB20.rgb
```

![RGB-CLI](assets/fr/02.webp)

Es wurde uns jedoch mitgeteilt, dass noch kein Schema in die Software importiert wurde. Es gibt auch keinen Vertrag im Stash. Um ihn zu sehen, führen Sie den Befehl :

```bash
rgb schemata
```

Sie können dann das Repository klonen, um bestimmte Schaltpläne abzurufen:

```bash
git clone https://github.com/RGB-WG/rgb-schemata
```

![RGB-CLI](assets/fr/03.webp)

Dieses Repository enthält in seinem Verzeichnis `src/` mehrere Rust-Dateien (z.B. `nia.rs`), die Schemata definieren (NIA für "*Non Inflatable Asset*", UDA für "*Unique Digital Asset*", usw.). Um zu kompilieren, können Sie dann den Befehl :

```bash
cd rgb-schemata
cargo run
```

Dies erzeugt mehrere `.rgb` und `.rgba` Dateien, die den kompilierten Schemata entsprechen. Zum Beispiel finden Sie `NonInflatableAsset.rgb`.

### Schema und Schnittstellenimplementierung importieren

Sie können nun den Schaltplan in `rgb` importieren:

```bash
rgb import schemata/NonInflatableAssets.rgb
```

![RGB-CLI](assets/fr/04.webp)

Dadurch wird es dem lokalen Stash hinzugefügt. Wenn wir den folgenden Befehl ausführen, sehen wir, dass das Schema jetzt erscheint:

```bash
rgb schemata
```

## Vertragserstellung (Ausstellen)

Es gibt zwei Möglichkeiten, ein neues Asset zu erstellen:


- Entweder verwenden wir ein Skript oder Code in Rust, der einen Vertrag erstellt, indem er Schemafelder ausfüllt (globaler Zustand, eigene Zustände usw.) und eine `.rgb`- oder `.rgba`-Datei erzeugt;
- Oder Sie verwenden direkt den Unterbefehl `issue` mit einer YAML- (oder TOML-) Datei, die die Eigenschaften des Tokens beschreibt.

Im Ordner `examples` finden Sie Beispiele in Rust, die veranschaulichen, wie Sie einen `ContractBuilder` erstellen, den `globalen Status` (Asset-Name, Ticker, Angebot, Datum usw.) ausfüllen, den Owned State definieren (welchem UTXO er zugewiesen ist) und dann all dies zu einer *Vertragssendung* zusammenstellen, die Sie exportieren, validieren und in einen Stash importieren können.

Die andere Möglichkeit besteht darin, eine YAML-Datei manuell zu bearbeiten, um den "Ticker", den "Namen", das "Angebot" usw. anzupassen. Nehmen wir an, die Datei heißt `RGB20-demo.yaml`. Sie können angeben:


- spez": Ticker, Name, Genauigkeit ;
- begriffe": ein Feld für rechtliche Hinweise ;
- issuedSupply": die Menge der ausgegebenen Token;
- zuweisungen": gibt das Einweg-Siegel (*Siegeldefinition*) und die freigeschaltete Menge an.

Hier ist ein Beispiel für eine zu erstellende YAML-Datei:

```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```

![RGB-CLI](assets/fr/05.webp)

Führen Sie dann einfach den Befehl :

```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```

![RGB-CLI](assets/fr/06.webp)

In meinem Fall lautet der eindeutige Schema-Bezeichner (der in einfache Anführungszeichen gesetzt werden muss) `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` und ich habe keinen Aussteller angegeben. Meine Bestellung lautet also :

```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```

Wenn Sie die Schema-ID nicht kennen, führen Sie den Befehl :

```bash
rgb schemata
```

Die CLI antwortet, dass ein neuer Vertrag ausgestellt und dem Vorrat hinzugefügt wurde. Wenn wir den folgenden Befehl eingeben, sehen wir, dass es jetzt einen zusätzlichen Vertrag gibt, der dem soeben erteilten Vertrag entspricht:

```bash
rgb contracts
```

![RGB-CLI](assets/fr/07.webp)

Dann zeigt der nächste Befehl die globalen Zustände (Name, Ticker, Versorgung...) und die Liste der Owned States, d.h. der Zuweisungen (z.B. 1 Million `PBN` Token, definiert in UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).

```bash
rgb state '<ContractId>'
```

![RGB-CLI](assets/fr/08.webp)

## Export, Import und Validierung

Um diesen Vertrag mit anderen Nutzern zu teilen, kann er aus dem Versteck in eine :

```bash
rgb export '<ContractId>' myContractPBN.rgb
```

![RGB-CLI](assets/fr/09.webp)

Die Datei `myContractPBN.rgb` kann an einen anderen Benutzer weitergegeben werden, der sie mit dem Befehl zu seinem Vorrat hinzufügen kann:

```bash
rgb import myContractPBN.rgb
```

Wenn es sich beim Import um eine einfache *Vertragssendung* handelt, erhalten wir die Meldung "`Importing consignment rgb`". Handelt es sich um eine größere *Zustandsübergangssendung*, wird der Befehl anders lauten (`rgb accept`).

Um die Gültigkeit sicherzustellen, können Sie auch die lokale Validierungsfunktion verwenden. Sie könnten zum Beispiel die Funktion :

```bash
rgb validate myContract.rgb
```

### Verwendung, Überprüfung und Anzeige von Vorräten

Zur Erinnerung: Der Stash ist ein lokaler Bestand an Schemata, Schnittstellen, Implementierungen und Verträgen (Genesis + Transitionen). Jedes Mal, wenn Sie "import" ausführen, fügen Sie dem Stash ein Element hinzu. Dieser Vorrat kann im Detail mit dem Befehl :

```bash
rgb dump
```

![RGB-CLI](assets/fr/10.webp)

Dadurch wird ein Ordner mit Details über den gesamten Vorrat erstellt.

## Übertragung und PSBT

Um eine Überweisung durchzuführen, müssen Sie eine lokale Bitcoin-Wallet manipulieren, um die "Tapret"- oder "Opret"-Verpflichtungen zu verwalten.

### Eine Rechnung generieren

In den meisten Fällen erfolgt die Interaktion zwischen den Teilnehmern eines Vertrags (z. B. Alice und Bob) über die Erstellung einer Rechnung. Wenn Alice möchte, dass Bob etwas ausführt (eine Token-Übertragung, eine Neuausgabe, eine Aktion in einer DAO usw.), erstellt Alice eine Rechnung, in der sie ihre Anweisungen an Bob detailliert beschreibt. Wir haben also :


- Alice** (der Aussteller der Rechnung) ;
- Bob** (der die Rechnung erhält und ausführt).

Im Gegensatz zu anderen Ökosystemen ist eine RGB-Rechnung nicht auf den Begriff der Zahlung beschränkt. Sie kann jede mit dem Vertrag verbundene Anfrage enthalten: Widerruf eines Schlüssels, Abstimmung, Erstellung einer Gravur (*Gravur*) auf einer NFT usw. Der entsprechende Vorgang kann in der Vertragsschnittstelle beschrieben werden. Der entsprechende Vorgang kann in der Vertragsschnittstelle beschrieben werden.

Der folgende Befehl erzeugt eine RGB-Rechnung:

```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```

Mit :


- `$CONTRACT`: Vertragskennung (*ContractId*) ;
- $INTERFACE": die zu verwendende Schnittstelle (z. B. "RGB20");
- $ACTION": der Name der in der Schnittstelle angegebenen Operation (für eine einfache fungible Token-Übertragung könnte dies "Transfer" sein). Wenn die Schnittstelle bereits eine Standardaktion vorsieht, brauchen Sie diese hier nicht erneut einzugeben;
- $STATE": die zu übertragenden Statusdaten (z. B. eine Anzahl von Token, wenn ein fungibles Token übertragen wird);
- $SEAL": das Einweg-Siegel des Begünstigten (Alice), d. h. ein ausdrücklicher Verweis auf ein UTXO. Bob verwendet diese Informationen, um die Zeugen-Transaktion zu erstellen, und die entsprechende Ausgabe gehört dann Alice (in *verblendetem UTXO* oder unverschlüsselter Form).

Zum Beispiel mit den folgenden Befehlen

```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```

Die CLI erzeugt eine Rechnung wie :

```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```

Sie kann über einen beliebigen Kanal (Text, QR-Code usw.) an Bob übermittelt werden.

### Eine Überweisung vornehmen

Um von dieser Rechnung zu übertragen:


- Bob (der die Token in seinem Versteck hat) hat eine Bitcoin-Brieftasche. Er muss eine Bitcoin-Transaktion vorbereiten (in Form einer PSBT, z. B. "tx.psbt"), die die UTXOs ausgibt, in denen sich die benötigten RGB-Token befinden, sowie ein UTXO für die Währung (Austausch);
- Bob führt den folgenden Befehl aus:

```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```


- Dies erzeugt eine Datei "consignment.rgb", die :
 - Die Übergangsgeschichte beweist Alice, dass die Token echt sind;
 - Der neue Übergang, der Token auf Alices Einweg-Siegel überträgt;
 - Eine Zeugen-Transaktion (ohne Vorzeichen).
- Bob sendet diese Datei "consignment.rgb" an Alice (per E-Mail, über einen Freigabeserver oder ein RGB-RPC-Protokoll, Storm usw.);
- Alice erhält die Datei "consignment.rgb" und nimmt sie in ihren eigenen Vorrat auf:

```bash
alice$ rgb accept consignment.rgb
```


- Die Befehlszeilenschnittstelle prüft die Gültigkeit des Übergangs und fügt ihn zu Alices Versteck hinzu. Ist sie ungültig, schlägt der Befehl mit detaillierten Fehlermeldungen fehl. Andernfalls ist er erfolgreich und meldet, dass die Beispieltransaktion noch nicht im Bitcoin-Netzwerk verbreitet wurde (Bob wartet auf Alices grünes Licht);
- Zur Bestätigung liefert der Befehl "accept" eine Unterschrift (*payslip*), die Alice an Bob senden kann, um ihm zu zeigen, dass sie die *Sendung* bestätigt hat;
- Bob kann dann seine Bitcoin-Transaktion signieren und veröffentlichen (`--publish`):

```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```


- Sobald diese Transaktion auf der Kette bestätigt wird, gilt das Eigentum an dem Vermögenswert als auf Alice übertragen. Die Wallet von Alice, die das Mining der Transaktion überwacht, sieht den neuen Owned State in ihrem Stash erscheinen.

Sie wissen nun, wie man einen RGB-Vertrag ausstellt und überträgt. Wenn Sie diese Anleitung nützlich fanden, wäre ich Ihnen sehr dankbar, wenn Sie unten einen grünen Daumen setzen würden. Sie können diesen Artikel auch gerne in Ihren sozialen Netzwerken teilen. Herzlichen Dank!

Ich empfehle auch dieses andere Tutorial, in dem ich erkläre, wie man einen RGB-kompatiblen Lightning-Knoten startet, um Token fast sofort auszutauschen:

https://planb.network/tutorials/node/rgb/rln-ffc02528-329b-4e16-bd83-873d0299feea