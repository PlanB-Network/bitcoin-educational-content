---
name: Sats.mobi

description: A Telegramm-zugänglicher verwahrter Wallet
---

![cover](assets/cover.webp)


dieses Tutorium wurde geschrieben von_ [Bitcoin Campus] (https://linktr.ee/bitcoincampus_)


## Sats.Mobi

SatsMobi ist ein Wallet, der auf Telegram läuft und alle Funktionen eines Lightning Network (custodial) Wallet sowie eine Reihe von sehr unterhaltsamen Funktionen bietet. Er ist aus einem Fork des inzwischen eingestellten LightningTipBot entstanden und hat alle seine Funktionen geerbt, aber auch aktuellere hinzugefügt, wodurch er moderner geworden ist. Wie der LNTipBot folgt auch der Sats.Mobi der Open-Source-Philosophie. Der Wallet kann unabhängig konfiguriert und verwaltet werden, indem man ihn aus diesem [Repository] (https://github.com/massmux/SatsMobiBot) klont.


Wenn Sie ihn einfach nur benutzen möchten, können Sie einen Chat auf Telegram starten, um zu sehen, dass es sich um einen Bot handelt.


## Einstellungen

Suchen Sie in der Telegram-Suchleiste nach "satsmobi" und der Link zum [bot](@SatsMobiBot) wird angezeigt.


**Achtung**: Wenn Sie sich nicht sicher sind, ob Sie über Telegram suchen sollen, können Sie über den folgenden [Link](https://t.me/SatsMobiBot) sicher auf den Bot zugreifen


![image](assets/it/01.webp)


Alles, was Sie tun müssen, ist _START_ zu drücken, um loszulegen


![image](assets/it/02.webp)


Um das Wallet zu erkunden, können Sie unten links _Menüu_ wählen.


![image](assets/it/03.webp)


Wählen Sie nun _/help_ unter den Hauptbefehlen.


![image](assets/it/04.webp)


Sats.Mobi begrüßt uns mit einer Nachricht, in der alle wichtigen Funktionen aufgeführt sind. Beim Start erstellt der Bot auch einen LN Address, der mit dem gewählten Handle auf Telegram verknüpft ist (der standardmäßig eindeutig ist). Die Befehle zum Senden und Empfangen von Sats mit diesem Wallet sind sichtbar, ebenso wie andere Funktionen, die wir später sehen werden. Interessant ist auch ein Blick auf das Menü _/erweitert_


![image](assets/it/05.webp)


Es fällt auf, dass Sats.Mobi auch einen anonymen LN Address erstellt hat, der zur Wahrung der Privatsphäre verwendet werden soll. Der Bot arbeitet mit Befehlen: Klicken Sie einfach auf das entsprechende Wort, oder geben Sie den Schrägstrich "/" in die Nachrichtenleiste ein, gefolgt von dem Befehl, den Sie ausführen möchten. Auch wenn der Wallet gerade erst erstellt wurde, wählen Sie zum Beispiel _/transactions_


![image](assets/it/06.webp)


Dieser Befehl zeigt die Liste der letzten Transaktionen an, die in diesem Fall gleich Null ist.


![image](assets/it/07.webp)


## Empfangen von Sats

Der Befehl zur Erstellung eines Invoice und zum Empfang von Sats lautet _/invoice_. Sats.Mobi arbeitet ausschließlich in Satoshi, der kleinsten Einheit von Bitcoin; daher ist es zur Erstellung des Invoice erforderlich, den Betrag in Sats in die Nachrichtenleiste zu schreiben und ihn dann im Chat mit dem Bot zu senden.

![image](assets/it/08.webp)


Im folgenden Beispiel wurde ein Betrag von 210 Sats gewählt.


![cover](assets/it/09.webp)


Nach einigen Augenblicken des Wartens auf die Vorbereitung des Invoice ist dieser als Text und als QR-Code verfügbar. Nach dem Bezahlen des Invoice zeigt das Wallet den Saldo an. Wenn aus irgendeinem Grund der Gesamtbetrag nicht aktualisiert wird, schreiben Sie _/balance_ und drücken Sie die "Enter"-Taste.


![image](assets/it/10.webp)


## Senden von Sats


Obwohl Sats ein äußerst wertvolles Gut sind, von dem man sich nicht leichtfertig trennen sollte, macht Sats.Mobi diesen Teil attraktiv, einige kurze Tests (d.h. ein paar Probetransaktionen) durchzuführen wird kein Problem sein.


### Bezahlen einer Invoice


Der einfachste Weg, einen Invoice zu bezahlen, ist, die Nachrichtenzeichenfolge `lnbc1xxxxx` zu kopieren und sie in die Nachrichtenleiste einzufügen, nachdem Sie den Befehl _/pay_ eingegeben haben. **Die korrekte Syntax erfordert, dass nach dem Befehl ein Leerzeichen steht.


![image](assets/it/11.webp)


Das Wallet sendet eine Nachricht mit der Bitte um Bestätigung. Wenn Sie auf _Bezahlen_ klicken, wird das Invoice bezahlt.


![image](assets/it/12.webp)


Sats.Mobi kann sich auf einen effizienten und gut vernetzten Lightning-Knoten verlassen, nur selten kommt es zu Zahlungsausfällen, weil es immer die richtige Weiterleitung findet.


### Bequemes Bezahlen vom Handy aus


Browsing auf Telegram, Sats.Mobi ist auch auf dem Handy verfügbar. Die bequemste Funktion für das Bezahlen mit dem Handy ist das Scannen eines QR-Codes, aber diesem Wallet fehlt sie vom Design her, da es keine eigenständige App ist, sondern in einem sozialen Netzwerk enthalten ist. Sats.Mobi ist daher so programmiert, dass es das mobile Erlebnis so weit wie möglich erleichtert: Es kann in der Tat ein Bild entschlüsseln, z. B. ein Foto des QR-Codes des Invoice, den Sie bezahlen möchten.


Nehmen wir an, Sie möchten eine Invoice von 50 Sats bezahlen.


![image](assets/it/20.webp)


Wenn uns dieser angezeigt wird, können wir ein Foto des entsprechenden QR-Codes machen.


![image](assets/it/21.webp)


Dann öffnen wir Telegram auf dem Handy und hängen im Chat mit Sats.Mobi das soeben aufgenommene Foto des QR-Codes an


![cover](assets/it/22.webp)


Nach der Auswahl senden wir sie an den Bot:


![image](assets/it/23.webp)

Sats.Mobi entschlüsselt das Foto und **zeigt sofort den Zahlungsantrag** mit der richtigen Beschreibung an. Der Chat bittet um eine Bestätigung, um fortzufahren, müssen Sie _/Bezahlen_ drücken

![image](assets/it/24.webp)


Bitte warten Sie einen Moment, damit die Zahlung bearbeitet werden kann.


![image](assets/it/25.webp)


Der Invoice wurde für 50 Sats bezahlt, ein Ergebnis, das ohne den Einsatz einer Kamera und ihrer integrierten Scanfunktion erzielt wurde.


### Sats.Mobi in Telegrammgruppen


![image](assets/it/27.webp)


Zu den Funktionen, die LNTipBot berühmt gemacht haben und die Sats.Mobi in Telegram einbringt, gehört diejenige, die das Erlebnis für die Mitglieder einer Gruppe unterhaltsam und interaktiv macht.

Die Besitzer können den Bot einladen, dem Gruppenchat beizutreten, und dann Sats.Mobi als Administrator ernennen. Von diesem Moment an beginnt der Spaß, denn die Mitglieder können beginnen, andere Nutzer für ihren Beitrag zur Gruppe zu belohnen.


- _/tip_ fügt einen Tipp hinzu, indem er auf eine Nachricht antwortet;
- _/send_ sendet Geldmittel unter Angabe eines LN Address oder eines Telegram-Handles als Empfänger;
- mit _/faucet_ (im Menü _/erweitert_) können Sie eine Reihe von Tipps erstellen, die die schnellsten Mitglieder der Gruppe sammeln können, indem sie auf _/collect_ klicken;
- mit _/tipjar_ (im Menü _/erweitert_) wird eine weitere Art von Verteilung erstellt, die an die Benutzer der Gruppe gesendet werden kann.


Jeder dieser Befehle hat seine eigene Syntax, die im Hauptmenü erklärt wird.


Und wenn wir nicht der Besitzer einer Gruppe sind? Kein Problem: Bitten Sie einfach den Gründer, Sats.Mobi einzuladen, fügen Sie es als Administrator der Gruppe hinzu, und Sie sind fertig!


## Verkaufsstelle (POS)


Wenn Sats.Mobi zum ersten Mal gestartet wird, erstellt der Bot auch eine weitere Funktion für den Benutzer: **den POS**. Das "Gerät" wird vom Benutzer mit dem Befehl _/pos_ oder durch Klicken auf die entsprechende Schaltfläche in der Konsole unten rechts aktiviert. Tatsächlich ist der POS eine Web-App, die sich als Pop-up im Telegram-Chat öffnet


![image](assets/it/14.webp)


Das Interface zeigt oben links das persönliche Telegram-Handle des Benutzers an und wird einfach so verwendet, wie alle Kassen verwendet werden: durch Eingabe des Betrags auf der Tastatur. Nehmen wir nun an, wir wollen 21 Cent für eine Dienstleistung kassieren. Da Sats.Mobi von Haus aus nur Sats verwaltet, ist es nicht einfach, die Umrechnung im Kopf vorzunehmen. Im Gegenteil, die Kasse zeigt den Euro als Rechnungseinheit an und zeigt gleichzeitig den Gegenwert in Satoshi.


![image](assets/it/15.webp)

Wenn Sie auf _/OK_ klicken, wird der Invoice angezeigt, der dem Kunden über einen QR-Code angezeigt oder als String über Instant Messaging gesendet werden kann, um ihn zu bezahlen.

![image](assets/it/16.webp)

![image](assets/it/17.webp)


Natürlich ist der POS auch auf Mobiltelefonen verfügbar, auf die auf die gleiche Weise zugegriffen werden kann wie auf die zuvor gezeigten.


![image](assets/it/18.webp)


Sie wird auch auf dem Bildschirm des Mobiltelefons gut angezeigt:


![image](assets/it/19.webp)


## Zusätzliche Merkmale


Es gibt noch weitere Funktionen, die das Angebot des Sats.Mobi Wallet vervollständigen, das, wie wir gesehen haben, das Konzept eines Wallet über die Vorgänge des Empfangens und Sendens von Zahlungen hinaus erweitert:


- _/nostr_: um den Wallet mit einem eigenen Nostr-Benutzer zu verbinden, um Zaps zu empfangen;
- /cashback_: zeigt einen Code an, der einem Händler vorgelegt werden kann, um eine Rückvergütung für einen Einkauf zu erhalten;
- _/buy_: startet eine geführte Prozedur innerhalb des Bots, die den Kauf von Sats für Euro ermöglicht;
- _/activatecard_: um die Aktivierung einer NFC-Debitkarte zu beantragen, die über das Sats.Mobi Wallet aufgeladen werden kann und für die Benachrichtigungen aktiviert werden können;
- _/link_: erstellt einen Link für Ihren eigenen Zeus oder Blue Wallet, die als Fernbedienungen für diesen Wallet verwendet werden können.


## Schlussfolgerung

Sats.Mobi ist ein angenehmer und unterhaltsamer Wallet, der an die Erfahrungen mit LNTipBot und den fortgeschrittenen Funktionen von LNBits anknüpft. Es ist jedoch wichtig, sich daran zu erinnern, dass **es sich um einen Verwahrungsdienst handelt**. Daher sollte er dazu verwendet werden, sehr wenige Sats zu halten, er ist kein Haupt-Wallet für Ihre Lightning Network-Fonds. Es gibt auch ein intrinsisches Kapazitätslimit, das 500.000 Sats entspricht, ein Limit, das nicht überschritten werden sollte.


Wenn Sie auf der Suche nach Lightning Network-Geldbörsen sind, die nicht für die Aufbewahrung bestimmt sind, sollten Sie sich unbedingt andere Produkte ansehen.


---
### Dokumentation


- [Github](https://github.com/massmux/SatsMobiBot)
- Wiedergabeliste von [videos](https://www.youtube.com/results?search_query=Sats.mobi) demo