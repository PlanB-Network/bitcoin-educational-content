---
name: Braiins Pool

description: Einführung in Braiins Pool
---

![signup](assets/cover.webp)

Braiins Pool, ehemals bekannt als Slush Pool, ist der allererste Bitcoin-Mining-Pool. Gegründet im November 2010, hat er seinen ersten Block am 16. Dezember 2010, Block 97834, gemined.

Stand Mai 2024 verfügt Braiins Pool über eine Rechenleistung von 13 EH/s, was etwa 1,8% der gesamten Bitcoin-Hashrate entspricht. Es wurden insgesamt 1.307.188 Bitcoins gemined, was ungefähr 6% der maximal 21 Millionen Bitcoins entspricht, die jemals existieren werden.

### Vergütungssystem

Seit Ende 2023 hat Braiins Pool sein Vergütungssystem geändert und das FPPS (Full Pay Per Share) System übernommen. Das bedeutet, dass Miner täglich Belohnungen für ihre gesamte Arbeit vom Vortag erhalten, auch wenn der Pool keinen Block gefunden hat. Dies unterscheidet sich vom alten System, bei dem Miner nur dann eine Belohnung erhielten, wenn der Pool einen Block fand.

**Es ist erwähnenswert, [laut einem Tweet von Mononaut](https://x.com/mononautical/status/1777686545715089605), der die Bitcoin TimeChain analysiert, dass viele Mining-Pools, die das FPPS-System verwenden, die gemineden Bitcoins an eine Adresse von AntPool senden würden, was bedeuten würde, dass AntPool die Hashrate all dieser Pools kontrolliert, etwa 47% der globalen Bitcoin-Hashrate. Das ist eine sehr schlechte Nachricht für die Dezentralisierung des Netzwerks.**

### Pool-Gebühren

Die Gebühren für Braiins Pool betragen 2,5%, jedoch, wenn Sie BraiinsOS auf Ihren Maschinen verwenden, betragen die Gebühren 0%

### Auszahlungen

**Lightning-Auszahlungen**
Lightning-Auszahlungen ermöglichen es Ihnen, Ihre Belohnungen einmal täglich ohne Mindestbetrag über eine Lightning-Adresse abzuheben.
Um diese Methode zu verwenden, müssen Sie ein Wallet haben, das mit Lightning-Adressen kompatibel ist.

**On-Chain-Auszahlungen**
On-Chain-Auszahlungen sind auf einen Mindestbetrag beschränkt und können Gebühren unterliegen.
Mindestbetrag: 20.000 Sats
Gebühren: 10.000 Sats für Beträge unter 500.000 Sats
Kostenlos für Beträge über 500.000 Sats
Auszahlungen können durch Zeitintervall oder durch Betrag ausgelöst werden.

## Kontoerstellung

Um Braiins Pool zu nutzen, [gehen Sie auf deren Website](https://braiins.com/pool) und klicken Sie oben rechts auf "SIGN UP"


![signup](assets/3.webp)

Geben Sie Ihre Informationen ein und bestätigen Sie, dann erhalten Sie eine E-Mail, die Sie bittet, Ihre Adresse zu bestätigen. Bestätigen Sie mit dem Link in der E-Mail, die Sie erhalten haben, und loggen Sie sich dann auf der Plattform ein

![signup](assets/4.webp)


## Einen "Worker" hinzufügen
Ein Worker ist der Miner, den Sie mit dem Pool verbinden werden. Um einen neuen Miner hinzuzufügen, klicken Sie im linken Seitenmenü auf "Workers".
![signup](assets/7.webp)

Klicken Sie dann auf den lila "Connect Workers +" Button.

In diesem Fenster wählen Sie Ihren geografischen Bereich.

Wenn der Miner, den Sie verbinden möchten, BraiinsOS verwendet, wählen Sie das "Stratum V2" Protokoll. Andernfalls wählen Sie "Stratum V1".

![signup](assets/8.webp)

Sie erhalten die Informationen, die Sie auf der Webseite Ihres Miners eingeben müssen (beziehen Sie sich auf die Dokumentation Ihres Miners, um zu wissen, wo Sie diese Informationen eingeben müssen).

Hier ist **"stratum+tcp://eu.stratum.braiins.com:3333"** die Pool-URL.
**JimZap.workerName** ist Ihr Kennzeichen und der Name Ihres Miners, wobei JimZap das Kennzeichen und .workerName der Name des Miners ist. Wenn Sie mehrere Miner haben, können Sie ihnen entweder den gleichen Namen geben, in diesem Fall wird ihre Rechenleistung auf dem Dashboard zusammengezählt, oder Sie geben ihnen unterschiedliche Namen, um sie einzeln zu überwachen.
Und das Passwort ist immer dasselbe **"anything123"**

Sobald Sie diese Informationen auf der Webseite Ihres Miners eingegeben haben und er mit dem Mining begonnen hat, werden Sie ihn nach einigen Minuten auf dem Braiins Pool Dashboard sehen.

## Übersicht Dashboard

![signup](assets/9.webp)

Im oberen Banner können Sie die durchschnittliche Gesamthashrate aller Ihrer Miner über 5 Minuten, 1 Stunde und 24 Stunden sehen. Und eine Zusammenfassung der Anzahl der Miner, die online oder offline sind.
Unten ermöglicht Ihnen ein Diagramm, die Entwicklung Ihrer Rechenleistung zu verfolgen.

![signup](assets/10.webp)

Unter diesem Diagramm finden Sie mehrere Informationen über Ihre Belohnungen in Sats.

**"Heutige Mining-Belohnungen"** Zeigt die Anzahl der Sats, die Sie heute abgebaut haben. Am Ende des Tages wird dieser Wert auf 0 zurückgesetzt und die Sats werden Ihrem Konto gutgeschrieben.

**"Gesamte Belohnung von gestern"** Die Anzahl der Sats, die Sie am Tag zuvor abgebaut haben

**"Geschätzte Rentabilität (1 TH/s)"** Ist eine Schätzung der Anzahl der Sats, die Sie an einem Tag für eine Rechenleistung von 1 TH/s verdienen. Wenn der Wert zum Beispiel 77 Sats beträgt und Sie eine Rechenleistung von 10 TH/s kontinuierlich über den Tag haben, dann würden Sie theoretisch 77 x 10 = 770 Sats pro Tag verdienen.

**"Gesamte Belohnung aller Zeiten"** Die gesamten Sats, die Sie mit Braiins Pool abgebaut haben

**"Belohnungsschema"** Die vom Pool angewendete Gebührenrate

**"Nächste Auszahlung ETA"** Schätzung der Zeit, die vergehen wird, bevor Sie die Sats von der Plattform abheben können. Hier zeigt die Schätzung nichts an, da das Mining erst seit wenigen Minuten läuft.

**"Kontostand"** Die Anzahl der Sats, die auf Ihrem Konto verfügbar sind, die Sie dann abheben können.
## Einrichtung von Auszahlungen
Sie können Ihre Belohnungen entweder on-chain oder über Lightning mit einer Adresse abheben.

Klicken Sie oben auf "Funds". Standardmäßig haben Sie ein "Bitcoin-Konto". Sie können weitere erstellen, um die Belohnungen zu teilen. Wir werden darauf im nächsten Abschnitt zurückkommen.

Klicken Sie nun auf "Einrichten".

![signup](assets/17.webp)

In diesem neuen Fenster können Sie "Onchain-Auszahlung" wählen.

Benennen Sie dieses Wallet, geben Sie eine BTC-Adresse an und wählen Sie die Art des Auslösers, den Sie möchten. "Schwelle" bedeutet, dass die Zahlung ausgelöst wird, wenn Sie eine festgelegte Menge an BTC angesammelt haben, und mit "Zeitintervall" wird die Zahlung in regelmäßigen Abständen (Tag/Woche/Monat) ausgelöst.

Beachten Sie, dass der Mindestbetrag 0,0002 BTC beträgt und dass unter 0,005 BTC eine Gebühr von 0,0001 BTC erhoben wird.

![signup](assets/18.webp)

Wenn Sie Lightning-Auszahlungen verwenden möchten, benötigen Sie ein Wallet, das eine Lightning-Adresse bereitstellt. Zum Beispiel können Sie getAlby verwenden.

Klicken Sie oben im Fenster auf "Lightning-Auszahlung".

Geben Sie Ihre Lightning-Adresse ein und markieren Sie das Kästchen "Ich verstehe..." und bestätigen Sie.

Mit dieser Auszahlungsmethode werden Ihre Belohnungen jeden Tag an Ihr Wallet gesendet.

![signup](assets/14.webp)
Sobald Sie Ihre Auszahlungseinstellungen validiert haben, erhalten Sie eine Bestätigungs-E-Mail.
![signup](assets/15.webp)

## Belohnungen teilen

Braiins Pool ermöglicht es Ihnen auch, Ihre Belohnungen über mehrere Wallets zu verteilen.

Um dies zu tun, klicken Sie oben auf "Mining" und dann links auf "Einstellungen".

![signup](assets/19.webp)

Auf dieser Seite können Sie ein weiteres "Finanzkonto" hinzufügen, indem Sie auf "Ein weiteres Finanzkonto hinzufügen" klicken und Ihre Belohnungen in % auf diese verschiedenen Konten verteilen, denen Sie ein Wallet zuordnen müssen. Um ein neues Wallet mit einem Finanzkonto zu verknüpfen, beziehen Sie sich auf den vorherigen Abschnitt.