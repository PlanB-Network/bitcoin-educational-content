---
name: Zeus Embedded - Für Fortgeschrittene
description: Selbstverwahrende Wallet mit mehreren Nodes
---

![Zeus](assets/cover.webp)


## Einführung in ZEUS Wallet


ZEUS ist eine mobile Bitcoin-Wallet- und Node-Management-App mit allen Funktionen einer Bitcoin-Lightning-Wallet, die Bitcoin-Zahlungen vereinfacht, den Nutzern die volle Kontrolle über ihre Finanzen gibt und fortgeschrittenen Nutzern ermöglicht, ihre Lightning-Nodes von der Handfläche aus zu verwalten.


### Für wen ist ZEUS gedacht?

Derzeit richtet sich ZEUS an Personen, die ihren eigenen [Lightning Network Daemon (LND)](https://lightning.engineering/) oder [Core Lightning (CLN)](https://blockstream.com/lightning/) Node für zu Hause oder ihr Geschäft betreiben und diese über ZEUS remote verwalten.

Auch Händler, die [BTCPay](https://btcpayserver.org/) oder [LNBits](https://lnbits.com/) oder [Alby](https://getalby.com/) (oder jedes andere LNDhub-Konto) nutzen, können ihre Nodes / Konten mit ZEUS verbinden, verwenden und verwalten.


[Ab v0.8](https://blog.zeusln.com/zeus-v0-8-0-open-beta/) wird ZEUS auch durchschnittliche Nutzer ansprechen, die eine einfache Möglichkeit suchen, schnelle und kostengünstige Bitcoin-Zahlungen von ihrem Mobilgerät aus zu tätigen, indem sie einen [integrierten mobilen Lightning Node](https://docs.zeusln.app/category/embedded-node) mit einem integrierten [Lightning Service Provider (LSP)](https://docs.zeusln.app/lsp/intro) nutzen.


### Wichtige Zeus-Ressourcen:

- Offizielle Zeus-Webseite - [https://zeusln.app/](https://zeusln.app/)
- Zeus-Dokumentation - [https://docs.zeusln.app/](https://docs.zeusln.app/)
- [Zeus Github Repository](https://github.com/ZeusLN/zeus)
- [Zeus-Telegram-Supportgruppe](https://t.me/ZeusLN)
- [Zeus auf NOSTR](https://iris.to/zeus@zeusln.app)
- [Zeus-Blog-Ankündigungen](https://blog.zeusln.com)


### Zeus Funktionen

#### Allgemeine Funktionen:


- Selbstverwahrte Bitcoin- und Lightning-Only-Wallet
- Keine Verarbeitungsgebühren, kein KYC erforderlich
- Vollständig Open Source (APGLv3)
- Unterstützung mehrerer Nodes/Konten (Du kannst deinen eigenen Heim-Node(s) verwalten, einen eingebetteten LND-Node betreiben, dich mit mehreren LNDhub-Konten verbinden)
- Einfach zu bedienendes Aktivitätsmenü
- PIN- oder Passphrasen-Verschlüsselung, Privatsphären-Modus - verberge deine sensiblen Daten
- Kontaktbuch, verschiedene Designs, mehrere Sprachen


#### Technische Funktionen


- Verbindung über Tor
- Vollständige LNURL-Unterstützung (Bezahlen, Abheben, Authentifizierung, Kanal), Senden an Lightning-Adressen
- Detailliertes Lightning-Kanalmanagement, MPP/AMP-Unterstützung, Keysend, Verwaltung der Routing-Gebühren
- Unterstützung für Replace-by-fee (RBF) und Child-pays-for-parent (CPFP)
- NFC-Zahlungen und -Anfragen, Nachrichten signieren und verifizieren
- Unterstützung von SegWit und Taproot
- Einfache Taproot-Kanäle
- Selbstverwaltete Lightning-Adressen (@zeuspay.com)
- Point of Sale von Square (bald offener PoS)


### Anleitungen und Video-Tutorials

Um ZEUS nutzen und die Lightning-Kanäle, Liquidität, Gebühren usw. verwalten zu können, ist es ratsam, zunächst einige wichtige Anleitungen zum Lightning Network zu lesen.


#### Anleitungen:


- [LND - Lightning Network Daemon Dokumentation](https://docs.lightning.engineering/)
- [CLN - Core Lightning Dokumentation](https://lightning.readthedocs.io/index.html)
- [Anfänger-Leitfaden für Lightning](https://bitcoiner.guide/lightning/) - von Bitcoin Q&A
- [Lightning Node Management](https://www.lightningnode.info/) - von openoms
- [Die Lightning Network und die Flughafen-Analogie](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [Verwaltung der Liquidität eines Lightning Nodes](https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [Wartung eines Lightning Nodes](https://darthcoin.substack.com/p/lightning-node-maintenance)


#### Video-Anleitung von BTC Sessions


![Zeus Bitcoin Lightning Wallet - Mobile Node Management](https://youtu.be/hmmehTnV3ys)



## Eine Schritt-für-Schritt-Anleitung für die Verwendung des eingebetteten Zeus LN-Nodes auf dem Mobilgerät


![Image](assets/en/01.webp)


Ich widme diese Anleitung allen neuen Lightning Network (LN) Nutzern, die eine neue souveräne Reise mit einer selbstverwahrten Node-Wallet auf ihren Mobilgeräten beginnen möchten.


Stellen wir uns vor, dass ihr bereits durch die Vielzahl von verwahrten LN-Wallets gegangen seid, aber noch nicht bereit seid, einen öffentlichen Routing-LN-Node zu betreiben. Ihr möchtet einfach mehr Sats über LN in einer selbstverwahrteren Art und Weise ansammeln und eure regelmäßigen Zahlungen über LN abwickeln.


Hier kommt ZEUS: Ab [Version v0.8.0, welche auf ihrem Blog angekündigt wurde](https://blog.zeusln.com/new-release-zeus-v0-8-0/), bietet ZEUS nun einen eingebetteten LND-Node direkt in der App an. Bislang war Zeus eine App zur Fernverwaltung von Nodes und LNDhub-Konten. Aber jetzt... ist der Node im Handy!


![Image](assets/en/02.webp)


### Kurze Zusammenfassung der wichtigsten Funktionen des Zeus-Nodes:



- **Privater LND-Node** - Das bedeutet, dass dieser Node keine öffentlichen Routings für Zahlungen anderer durch deinen Node durchführen wird. Der Node und die Kanäle sind unangekündigt (privat, nicht sichtbar im öffentlichen LN-Graphen). Um Zahlungen zu empfangen und zu senden, wird dies über deine verbundenen LSP-Peers erfolgen. HINWEIS: Der eingebettete ZEUS-Node wird KEIN öffentliches Routing durchführen!
- **Persistenter LND-Service** - Der Nutzer kann diese Funktion aktivieren und den LND-Service kontinuierlich aktiv halten, wie bei jedem regulären LN-Node. Die App muss nicht geöffnet sein, da der persistente Service die gesamte Kommunikation online hält.
- **Neutrino-Blockfilter** - Der Block-Sync wird mithilfe von [Blockfiltern und dem Neutrino-Protokoll](https://bitcoinops.org/en/topics/compact-block-filters/) durchgeführt (ohne Informationen über die on-chain-Guthaben der Nutzer preiszugeben). Hinweis: Bei hochlatenz- oder langsamen Internetverbindungen kann dieser neutrino-basierte Block-Sync manchmal fehlschlagen. Das Umschalten auf einen nahegelegenen Neutrino-Server könnte helfen, die Synchronisation wiederherzustellen. Ohne diese Synchronisation kann dein LND-Node nicht starten!
- **Einfache Taproot-Kanäle** - Beim Schließen dieser Kanäle fallen für die Nutzer geringere Gebühren an, und sie genießen mehr Privatsphäre, da sie auf der Blockchain wie jede andere Taproot-Ausgabe erscheinen.
- **Integrierter LSP** - Olympus ist der neue LSP-Node für ZEUS. Nutzer können sofort Sats über LN empfangen, ohne vorher LN-Kanäle eingerichtet zu haben. Mit dem 0-Konf-Kanal-Service von ZEUS müssen Sie lediglich eine LN-Invoice erstellen und von jeder anderen LN-Wallet aus zahlen. Weitere Informationen zum ZEUS LSP finden Sie hier. Der LSP bietet den Nutzern zusätzlich Privatsphäre, indem er ihnen Wrapped Invoices bereitstellt, die ihre öffentlichen Node-Schlüssel vor den Zahlern verbergen.
- **Kontaktbuch** - Du kannst Kontakte manuell speichern oder von NOSTR importieren, um Zahlungen an regelmäßigen Empfänger zu senden.
- **Volle Unterstützung für LNURL, LN Addressen zum senden und empfangen** - Jetzt kannst du deine eigene selbstverwahrte LN-Adresse mit @zeuspay.com einrichten. Hinweis: Du kannst ZEUS auch für LN-Auth auf Websites verwenden, bei denen du dich mit einer LN-Authentifizierung anmelden kannst. Das ist sehr praktisch.
- **Point of Sale** - Jetzt können Händler ihre eigenen Produktartikel einrichten und direkt über ZEUS mit integriertem PoS verkaufen. Derzeit enthält es die grundlegenden Funktionen, in der Zukunft werden jedoch erweiterte Funktionen hinzugefügt.
- **LND-logs** - Der Nutzer kann die LND- service logs in Echtzeit lesen und zur Fehlersuche bei möglichen Problemen verwenden (hauptsächlich bei schlechten Verbindungen).
- **Automatisierte Backups** - Die LN-Node-Kanäle werden automatisch auf dem Olympus-Server gesichert. Dieses automatische Backup ist mit deinem Node-Wallet-Seed verschlüsselt (ohne den Seed ist es völlig nutzlos). Der Nutzer kann auch manuell ein SCB (static channels backup) für eine Katastrophenwiederherstellung exportieren.


### Wie man mit dem Zeus LN Node (LND eingebettet) startet


In dieser Anleitung werde ich ausschließlich über den eingebetteten LND-Node sprechen und nicht über die anderen Möglichkeiten, diese großartige App zu nutzen (Fernverwaltung von Nodes und LNDhub-Konten). Für die anderen Arten von Verbindungen verweise ich auf die [Zeus Docs page](https://docs.zeusln.app/category/getting-started), die sehr gut erklärt ist und keine separate Anleitung erfordert.


#### SCHRITT 1 - INITIALE EINRICHTUNG


Da ZEUS ein vollständiger LND-Node ist, habe ich einige initiale Empfehlungen:

- Verwende kein altes Gerät, da dies die Nutzung dieser leistungsstarken App beeinträchtigen könnte. Besonders während der Synchronisationsphase könnte die App intensiven CPU- und RAM-Verbrauch verursachen. Ein Mangel daran könnte die Nutzung der ZEUS-App sogar unmöglich machen.
- Verwende mindestens Android 11 als mobiles Betriebssystem und aktualisiere es so weit wie möglich. Für iOS gilt dasselbe: Versuche, eine möglichst hohe OS-Version zu verwenden.
- Du benötigst mindestens 1 GB Speicherplatz für die Datenspeicherung. Mit der Zeit könnte dies wachsen, aber es gibt eine Funktion, um die Datenbank auf ein Maß von MBs zu komprimieren.
- Es besteht KEINERLEI Bedarf, ZEUS mit Tor oder Orbot zu verwenden. Mach die Dinge nicht komplizierter, als nötig. Tor bietet in diesem Fall keine zusätzliche Privatsphäre, sondern kann die initiale Synchronisation nur erschweren. Sei auch vorsichtig bei der Wahl deines VPNs und überprüfe die Latenz der Verbindung zu den Neutrino-Servern. Beachte, dass Neutrino-Blockfilter deine Geräteidentität nicht offenlegen oder nachverfolgen, sie dienen lediglich der Bereitstellung von Blöcken. Der LN-Verkehr läuft auch hinter einem LSP mit privaten Kanälen, sodass nur sehr wenige Informationen nach außen dringen. Es gibt also keinen Grund, sich um die Privatsphäre zu sorgen.
- Habe Geduld bei der initialen Synchronisation, sie kann mehrere Minuten dauern. Versuche, mit einer Breitband-Internetverbindung mit guter Latenz verbunden zu sein. Wenn du deinen eigenen Bitcoin-Node betreibst, [kannst du den Neutrino-Dienst aktivieren](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) und ZEUS mit deinem eigenen Node verbinden, sogar über das interne LAN, sodass du maximale Geschwindigkeit erzielst.


Sobald du die Verbindungstyp "Embedded Node" eingerichtet hast, wird die App eine Weile mit der Synchronisation beginnen. Warte geduldig, bis dieser Teil abgeschlossen ist, und gehe dann zur Haupt-Einstellungs-Seite.


![Image](assets/en/03.webp)


Lasse uns kurz in die einzelnen Einstellungen eintauchen und einige der wichtigsten Funktionen verstehen, bevor du ZEUS verwendest:


**A - EINSTELLUNGEN**


Dies ist ein Bereich mit allgemeinen Einstellungen für die gesamte App.


**1 - Lightning Service Provider (LSP)**


Hier werden zwei LSP-Dienste vorgestellt:



- _just-in-Time-Kanäle_ - Wenn du keinen Kanal geöffnet oder keine eingehende Liquidität verfügbar hast, öffnet der Dienst bei Aktivierung einen Kanal auf Abruf für dich. Diese Option kann deaktiviert werden, wenn du keine weiteren Kanäle dieses Typs öffnen möchtest.
- _Kanäle im Voraus anfordern_ - Du kannst eingehende Kanäle direkt in der App vom Olympus LSP mit verschiedenen Optionen und Beträgen (für eingehende und ausgehende Liquidität) kaufen.


Der LSP hilft Nutzern, sich mit dem Lightning Network zu verbinden, indem er Zahlungskanäle zu ihren Nodes öffnet. [Mehr über LSPs erfährst du hier](https://medium.com/breez-technology/envisioning-lsps-in-the-lightning-economy-832b45871992). ZEUS hat einen neuen integrierten LSP namens [OLYMPUS by ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581), der für alle Nutzer verfügbar ist, die den neuen eingebetteten Node verwenden.


In diesem Bereich ist standardmäßig der Olympus LSP (https://0conf.lnolymp.us) eingestellt, aber bald kannst du auch einen anderen 0conf LSP einrichten, der dieses Protokoll unterstützt.


_Beachte: Wenn du einen Kanal mit dem Olympus LSP öffnest und dabei eine wrapped LN-Invoice verwendest, erhältst du auch 100k eingehende Liquidität! Das ist eine wirklich gute Option, falls du sofort mehr Sats empfangen musst. Beispiel: Du hinterlegst 400k Sats, um einen LSP-Kanal zu öffnen. Dann öffnet der LSP einen 500k Sats fassenden Kanal zu deinem ZEUS-Node und schiebt die 400k Sats, die du hinterlegt hast, zu deiner Seite. "Eingehende Liquidität" bedeutet mehr "Raum" in deinem Kanal, um zu empfangen._


In der Zukunft hoffen wir, viele weitere LSP in ZEUS integrieren zu können, die alternativ verwendet werden können. Es ist nur eine Frage der Zeit, bis neue LSP einen offenen Standard für diese Art von 0conf-Kanälen übernehmen.

Wenn du keine neuen Kanäle "on the fly" öffnen möchtest, kannst du diese Option deaktivieren.


In diesem selben Bereich hast du auch die Möglichkeit, "Simple Taproot Channels" anzufordern, wenn der LSP einen Kanal zu deinem ZEUS-Node öffnet. Diese Simple Taproot Kanäle bieten bessere On-Chain-Privatsphäre und niedrigere Gebühren beim Schließen des Kanals. Es gibt nur zwei Gründe, warum du sie nicht verwenden möchtest:



- Sie sind neu, und es kann noch Fehler in LND geben, wenn man sie benutzt.
- Dein Gegenüber unterstützt sie nicht. Selbst LND-Nodes müssen sich derzeit explizit für sie entscheiden.


**2 - Zahlungseinstellungen**


Diese Funktion bietet dir die Möglichkeit, deine bevorzugten Gebühren für Zahlungen über LN oder On-Chain festzulegen. Du kannst auch die Option nutzen, die Auszeit für deine Invoice zu erhöhen oder zu verringern.

Wenn einige deiner LN-Zahlungen fehlschlagen, kannst du die Gebühr erhöhen, um eine bessere Route zu finden. Wenn du On-Chain-Transaktionen durchführst, kannst du eine spezifische Gebühr einstellen, sodass deine Transaktion nicht lange im Mempool stecken bleibt, besonders in Phasen hoher Gebühren.


**3 - Invoice-Einstellungen**


In diesem Bereich findest du einige Optionen zur Erstellung von Invoices: 



- Standard-Memo festlegen: Gib eine Standardmeldung an, die in den von dir erstellten Invoices angezeigt wird.
- Ablaufzeit in Sekunden: Lege eine spezifische Zeit fest, die länger oder kürzer sein kann, damit deine Invoice bezahlt wird.
- Routing-Hinweise einbeziehen - Biete Informationen an, um nicht angekündigte oder private Kanäle zu finden. Dies ermöglicht das Routing von Zahlungen zu Nodes, die im Netzwerk nicht öffentlich sichtbar sind. Ein Route-Hinweis bietet eine Teilroute zwischen dem privaten Node des Empfängers und einem öffentlichen Node. Dieser Route-Hinweis wird dann in der vom Empfänger erstellten Invoice enthalten und dem Zahler bereitgestellt. Ich empfehle, diese Funktion standardmäßig zu aktivieren, da ansonsten eingehende Zahlungen fehlschlagen könnten (keine Route gefunden).
- AMP Invoice - Atomare Multi-Pfad-Zahlungen (AMP) sind ein neuer Typ von Lightning-Zahlungen, der von LND implementiert wurde und es ermöglicht, Sats ohne eine spezifische Invoice zu empfangen, indem man [keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend) verwendet. Es handelt sich praktisch um einen statischen Zahlungscode. [Mehr erfährst du hier](https://docs.lightning.engineering/lightning-network-tools/LND/amp).
- Benutzerdefiniertes Preimage-Feld anzeigen: Verwende diese Option nur in sehr spezifischen Fällen, wenn du wirklich benutzerdefinierte Felder im Preimage verwenden möchtest. [Mehr erfährst du hier](https://Bitcoin.stackexchange.com/questions/90797/how-can-i-generate-preimage-for-lightning-network-Invoice-should-i).


Eine weitere Option in diesem Bereich ist die Festlegung des Typs der On-Chain-Adresse, die du verwenden möchtest: segwit nested, segwit, taproot.


![Image](assets/en/04.webp)


Klicke auf das Zahnrad-Symbol oben, und es erscheint ein Popup-Fenster, in dem du den gewünschten Adresstyp auswählen kannst. Sobald du das gemacht hast, wird die nächste On-Chain-Transaktion, die du durchführst, die von dir ausgewählte Adressart verwenden. Du kannst diese Einstellung jederzeit ändern.


**4 - Kanaleinstellungen**


In diesem Bereich kannst du einige Funktionen für das Öffnen von Kanälen vorab einstellen, wie:



- Anzahl der Bestätigungen: Lege fest, wie viele Bestätigungen du für das Öffnen eines Kanals benötigst.
- Kanal ankündigen (standardmäßig deaktiviert): Das bedeutet, dass es sich um unangekündigte Kanäle handelt.
- Simple Taproot Kanäle: Diese Option bietet verbesserte On-Chain-Privatsphäre und niedrigere Gebühren beim Schließen des Kanals.
- Kanal-Kauf-Schaltfläche anzeigen: Aktiviere diese Option, um die Schaltfläche zum Kauf von Kanälen anzuzeigen.


**5 - Privatsphäre-Einstellungen**


Hier findest du einige grundlegende Einstellungen, um die Privatsphäre in der ZEUS-App zu erhöhen:

- Block-Explorer zum Öffnen von TX-Details (mempool.space, blockstream.info oder einem benutzerdefinierten persönlichen Explorer).
- Zwischenspeicher lesen - Schalte diese Option ein oder aus, je nachdem, ob du möchtest, dass ZEUS deinen Geräte-Zwischenspeicher liest.
- Lurker-Modus - Schalte diese Option ein oder aus, um spezifische sensible Informationen in deiner ZEUS-App zu verstecken. Das ist eine gute Option, wenn du Demos erstellst oder Screenshots machst.
- Mempool-Gebührenempfehlung - Aktiviere diese Option, wenn du die empfohlenen Gebührenniveaus von [Mempool.space](https://Mempool.space/) verwenden möchtest


**6 - Sicherheit**


Dieser Bereich bietet zwei Optionen, um die App beim Öffnen zu sichern: ein Passwort oder eine PIN festlegen.


Sobald du eine PIN zum Öffnen der App festgelegt hast, kannst du auch eine "Duress-PIN" einrichten. Diese geheime zusätzliche PIN wird NUR in einem Zwangsszenario verwendet, wenn du bedroht wirst. Wenn du diese PIN eingibst, wird die gesamte Konfiguration gelöscht. Daher ist es ratsam, deine Backups auf dem neuesten Stand zu halten. Automatische Backups sind standardmäßig aktiviert, aber es ist auch gut, eigene Backups außerhalb des Geräts zu haben.


**7 - Währung**


Aktiviere oder deaktiviere die Option, um eine Währungsumrechnung in Fiat-Währung in der ZEUS-App anzuzeigen. Derzeit werden über 30 Fiat-Währungen weltweit unterstützt.


**8 - Sprache**


Du kannst zwischen mehreren Übersetzungsoptionen wechseln, die von der ZEUS-Community mit Muttersprachlern überprüft wurden.


**9 - Anzeige**


In diesem Bereich kannst du deine ZEUS-Anzeige personalisieren, indem du verschiedene Farbthemen, den Standardbildschirm (Tastenfeld oder Guthaben), die Anzeige deines Node-Alias, die Aktivierung großer Tastenfeldschaltflächen und die Anzeige zusätzlicher Dezimalstellen auswählst.

**10 - Point of Sale**


Dies ist eine spezielle Funktion, um ein integriertes PoS-System in ZEUS zu aktivieren oder zu deaktivieren. Du kannst ein eigenständiges PoS oder ein mit einem Square PoS-System verbundenes PoS betreiben. Derzeit unterstützt es grundlegende PoS-Funktionen, die für einen guten Start ausreichen und kleinen Händlern (Bars/Restaurants, Lebensmittelgeschäfte) helfen können, BTC auf native Weise zu akzeptieren.


In diesen Einstellungen findest du verschiedene Optionen, um dein PoS einzurichten:



- Bestätigungstyp der Zahlung: Nur LN, 0-conf, 1-conf
- Trinkgeld für Mitarbeiter, die das PoS bedienen, aktivieren/deaktivieren
- Tastenfeld anzeigen/verstecken
- Steuerprozentsatz, der auf den Beleg angewendet wird
- Produkte und Produktkategorien erstellen
- Einfache Auflistung aller Verkäufe


Hier ist ein Live-Demo-Video zur Verwendung von Zeus PoS:


**B - Wallet Sicherung**


Der eingebettete Node in ZEUS basiert auf LND und verwendet das [aezeed seed Format](https://github.com/lightningnetwork/LND/blob/master/aezeed/README.md). Dies unterscheidet sich von dem typischen [BIP39-Format](https://github.com/Bitcoin/bips/blob/master/bip-0039.mediawiki), das in den meisten Bitcoin-Wallets zu sehen ist, obwohl es ähnlich erscheinen mag. Aezeed enthält zusätzliche Daten, einschließlich des Geburtsdatums der Wallet, die dazu beitragen, dass erneute Scans während der Wiederherstellung effizienter ablaufen.


Das aezeed-Schlüsselformat sollte mit den folgenden mobilen Wallets kompatibel sein: Blixt, BlueWallet und Breez. Beachte, dass der Seed allein nicht ausreicht, um alle Guthaben wiederherzustellen, falls du offene oder schließende Kanäle hast!


Erfahre mehr über den Sicherungs- und Wiederherstellungsprozess auf der [Zeus Docs page](https://docs.zeusln.app/for-users/embedded-node/backup-and-recovery).


WICHTIGER TIPP: Wenn du deinen Seed sicherst, speichere auch den Node-Pubkey! Manchmal ist es nützlich, diesen zusammen mit deinem Seed und SCB (Statische Kanalsicherung) griffbereit zu haben, falls du die Wiederherstellung überprüfen musst.


SCB ist nur erforderlich, wenn du LN-Kanäle geöffnet hast. Falls du nur On-Chain-Guthaben hast, ist SCB nicht notwendig.


Falls du bemerkst, dass nach langer Zeit die alten Transaktionsverläufe immer noch nicht angezeigt werden, gehe zu Eingebetteter Node - Peers und deaktiviere die Option, die Liste der ausgewählten Peers zu verwenden (standardmäßig ist es btcd.lnolymp.us). Das löst einen Neustart aus und verbindet sich mit dem ersten verfügbaren Neutrino-Node mit einer besseren Antwortzeit. Oder verwende die unten genannten anderen bekannten Neutrino-Peers.


Falls du mehr Wiederherstellungsoptionen für einen LND-Node sehen möchtest, [lies bitte meine vorherige Anleitung](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), in der du die Schritte findest, wie du einen aezeed Seed in die Sparrow-Wallet oder andere Methoden importieren kannst.


**C - Eingebetteter Node**


In diesem Abschnitt findest du grundlegende Werkzeuge zur Verwaltung des integrierten Nodes:

- _Katastrophenwiederherstellung:_ Automatische und manuelle Sicherungen für die LN-Kanäle. Lies mehr darüber, wie man dieses Feature auf der ZEUS-Dokumentationsseite verwendet.

- _Express Graph Sync:_ Die ZEUS-App lädt die LN-Gossip-Graphendaten von einem dedizierten Server herunter, für eine schnellere und bessere Synchronisation, die beste Zahlungspfade bietet. Du kannst auch auswählen, ob vorherige Graphendaten beim Start gelöscht werden sollen.

- _Peers:_ Abschnitt zur Verwaltung der Neutrino-Peers und 0-conf-Peers. Falls du Probleme mit der initialen Synchronisation oder Kanälen, die nicht online gehen, hast, liegt das daran, dass dein Gerät eine hohe Latenz mit dem konfigurierten Neutrino-Peer hat. Versuche, die Liste der bevorzugten Peers zu wechseln oder füge deinen spezifischen Peer hinzu, von dem du weißt, dass er eine bessere Latenz für die Synchronisation hat. Bekannte Neutrino-Server sind:



   - btcd1.lnolymp.us | btcd2.lnolymp.us - für die Region US
   - sg.lnolymp.us - für die Region Asien
   - btcd-Mainnet.lightning.computer - für die Region USA
   - uswest.blixtwallet.com (Seattle) - für die Region US
   - europe.blixtwallet.com (Deutschland) - für die EU-Region
   - asia.blixtwallet.com - für die Region Asien
   - node.eldamar.icu - für die Region US
   - noad.sathoarder.com - für die Region US
   - bb1.breez.technology | bb2.breez.technology - für die Region US
   - neutrino.shock.network - US-Region



- _LND logs_ - ein sehr nützliches Tool zur Fehlersuche in deinem LN-Nodes und zur detaillierten Kontrolle der Vorgänge auf technischer Ebene.
- _Erweiterte Einstellungen_ - weitere Tools zur Steuerung der Verwendung deines LND-Nodes:



  - _Pathfinding-Modus:_ bimodal oder apriori, Wege, um eine bessere Route für deine LN-Zahlungen zu finden, und das Zurücksetzen der vorherigen Routing-Informationen. Lies diese sehr guten Leitfäden über Pathfinding [Pathfinding](https://docs.lightning.engineering/lightning-network-tools/LND/pathfinding) - von Docs Lightning Engineering und [LN Payment Pathfinding](https://voltage.cloud/blog/lightning-network-faq/understanding-payment-pathfinding-between-nodes-on-lightning-network/) - von Voltage
   - _Persistent LND_ - Aktiviere diesen Modus, wenn du möchtest, dass der LND-Dienst kontinuierlich im Hintergrund läuft und deinen Node 24/7 online hält. Das ist sehr nützlich, wenn du ZEUS als PoS in einem kleinen Laden verwendest oder viele LN-Tipps über die LN-Adresse erhältst.
   - _Wallet neu scannen_ - Diese Option löst beim Neustart einen vollständigen Scan aller On-Chain-Transaktionen deiner Wallet aus. Aktiviere dies nur, falls du einige Transaktionen in deiner Wallet vermisst. Die Neuscann-Aufgabe wird Zeit in Anspruch nehmen, mehrere Minuten, also sei geduldig und überprüfe immer die Protokolle, um mehr Details über den Fortschritt zu sehen.
   - _Datenbank komprimieren_ - Diese Option ist sehr nützlich, wenn deine ZEUS-App viel Gerätespeicher belegt (siehe App-Details in den Geräteeinstellungen). Falls du viel Aktivität mit ZEUS hast, empfehle ich, diese Kompaktierung häufiger durchzuführen. Sobald du bemerkst, dass du mehr als 1-1,5 GB Daten für die ZEUS-App hast, führe die Kompaktierung durch. Es wird neu starten und etwas Zeit in Anspruch nehmen, also sei geduldig.
   - _Neutrino-Dateien löschen_ - Diese Option zum Löschen der Neutrino-Dateien (mit einem Neustart) verringert erheblich den Datenspeicherverbrauch. Die Verringerung des Datenverbrauchs hat auch einen großen Einfluss auf den Akkuverbrauch, besonders wenn du ZEUS im persistenten Modus verwendest.


**D - Node-Info**


In diesem Abschnitt findest du mehr Details zum Status deines ZEUS-Node, wie:

- Alias - kurze Node-ID
- Öffentlicher Schlüssel - der vollständige öffentliche Schlüssel für deinen Node, der von anderen Nodes benötigt wird, um den Pfad zu deinem Node zu finden. Beachte, dass dieser öffentliche Schlüssel NICHT auf den regulären LN-Explorern (Mempool, Amboss, 1ML usw.) sichtbar ist. Dieser öffentliche Schlüssel ist NUR über deine verbundenen LN-Peers und Kanäle erreichbar.
- LN-Implementierungsversion
- ZEUS-App-Version
- Synced to chain und Synced to graph Status - sehr wichtige, die den korrekten Status deines Nodes anzeigen. Falls diese beiden nicht "true" anzeigen, bedeutet das, dass dein Node noch synchronisiert oder Probleme bei der Synchronisation hat. Daher wird empfohlen, einen Blick in deine LND-Protokolle zu werfen oder etwas länger zu warten.
- Blockhöhe und Hash - zeigt den letzten Block und Hash an, den dein Node gesehen und synchronisiert hat.


**E - Netzwerkinfo**


Dieser Abschnitt zeigt mehr Details zum allgemeinen Status des Lightning-Netzwerks, extrahiert aus deinen Graphensynchronisationsdaten: Anzahl der verfügbaren öffentlichen Kanäle, Anzahl der Nodes, Anzahl der Zombie-Kanäle (offline oder tot), Graphendurchmesser, durchschnittlicher und maximaler Ausgrad des Graphen.

Diese Informationen könnten nützlich sein, um Probleme zu beheben oder einfach für Statistiken.


**F - Lightning-Adresse**


In diesem Abschnitt kann der Nutzer seine eigene selbstverwahrte LN-Adresse @zeuspay.com einrichten.

ZEUS PAY nutzt benutzergenerierte Preimage-Hashes, Hodl-Invoices und das Zaplocker Nostr-Bestätigungsschema, um es Benutzern, die nicht 24/7 online sind, zu ermöglichen, Zahlungen an eine statische Lightning-Adresse zu empfangen. Benutzer müssen sich einfach innerhalb von 24 Stunden in ihren ZEUS-Wallets anmelden, um die Zahlungen zu beanspruchen, andernfalls werden sie an den Absender zurückgesendet.

Falls du den "persistenten Modus" aktivierst, werden alle Zahlungen an deine LN-Adresse sofort empfangen.

Erfahre mehr darüber, wie [Zaplocker](https://github.com/supertestnet/zaplocker#how-it-works) Zahlungen funktionieren und mehr über [ZeusPay-Gebühren hier](https://docs.zeusln.app/lightning-Address/fees).


**G - Onchain-Adressen**


In diesem Abschnitt kannst du deine generierten On-Chain-Adressen einsehen, um eine bessere Coin-Kontrolle zu haben.


**H - Kontakte**


Ein neues Kontaktbuch wurde in ZEUS v 0.8.0 eingeführt, das du verwenden kannst, um schnell Zahlungen an Freunde und Familie zu senden, und du kannst auch deine Kontakte von Nostr importieren.

Gib einfach deine Nostr npub oder lesbare NIP-05-Adresse ein, und ZEUS wird Nostr nach allen deinen Kontakten durchsuchen. Von dort kannst du eine schnelle Zahlung an einen Kontakt senden oder alle oder ausgewählte Kontakte in dein lokales Kontaktbuch importieren./<

Hier ist ein kurzes Video, wie du deine ZEUS-Kontakte konfigurierst und verwendest:


**I - Tools**


Hier haben wir verschiedene Unterabschnitte mit mehr Werkzeugen:

- _Konten:_  Hier kannst du externe Konten/Wallets importieren, Cold Wallets, Hot Wallets, um sie als externe Finanzierungsquelle für deine ZEUS-Node-Kanäle zu steuern oder zu verwenden. Dieses Feature ist noch experimentell.
- _Transaktion beschleunigen:_ Dieses Feature könnte hilfreich sein, wenn du eine Transaktion im Mempool hast, die stecken geblieben ist, und du die Gebühr erhöhen möchtest. Du musst die Transaktionsausgabe aus den Transaktionsdetails bereitstellen und die gewünschte neue Gebühr auswählen, die du verwenden möchtest. Sie muss höher als die vorherige sein und erfordert, dass du mehr Mittel in deiner On-Chain-Wallet verfügbar hast.


![Image](assets/en/05.webp)


Du musst zu deiner ausstehenden Transaktion gehen und die txID Outpoint kopieren. Gehe dann in diesen Abschnitt und füge sie ein, wähle dann die neue Gebühr, die du verwenden möchtest, um sie zu erhöhen. Es wird ein neues Fenster mit den empfohlenen Gebühren in diesem Moment anzeigen, oder du kannst eine benutzerdefinierte Gebühr festlegen. Denke daran, sie MUSS höher als die vorherige sein.

Es ist immer besser, eine UTXO mit maximal 100k Sats in deiner ZEUS On-Chain-Wallet zu behalten, um sie verwenden zu können, um Gebühren zu erhöhen, wenn es notwendig ist.


- _Signieren oder verifizieren_ - Mit diesem Feature kannst du eine spezifische Nachricht mit deinen Wallet-Schlüsseln unterzeichnen. Es kann auch verwendet werden, um eine Nachricht zu überprüfen, um zu beweisen, dass sie von bestimmten Wallet-Schlüsseln stammt.
- _Währungsrechner_ - ein einfaches Tool zur Berechnung des Umrechnungskurses zwischen BTC und anderen Fiat-Währungen.


**J - Merch und Support**


Hier findest du mehr Informationen und Links zu ZEUS, Online-Shop, Sponsoren, sozialen Medien.


**K - Hilfe**


In diesem letzten Abschnitt findest du Links zur ZEUS-Dokumentationsseite, GitHub Issues (falls du einen Fehler melden oder eine Anfrage direkt an die App-Entwickler senden möchtest), E-Mail-Support.



### SCHRITT 2 - Starten des ZEUS NODE



Denke daran, dass ZEUS hauptsächlich als LN-Wallet verwendet wird, für einfache und schnelle Zahlungen über LN. Natürlich enthält es auch eine On-Chain-Wallet, aber diese sollte ausschließlich zum Öffnen/Schließen von LN-Kanälen und nicht für regelmäßige Zahlungen, wie zum Beispiel für einen Kaffee, verwendet werden.

Bitte lies meine andere Anleitung darüber, [wie du deine eigene Bank sein kannst, indem du die 3 Stufen der Stash-Nutzung anwendest](https://darth-coin.github.io/beginner/be-your-own-bank-en.html).


Momentan hast du 2 Möglichkeiten, um mit ZEUS zu beginnen:

- Sofort über LN, unter Verwendung des 0-conf-Kanals von Olympus LSP
- Zuerst auf die On-Chain-Wallet einzahlen und dann einen normalen LN-Kanal mit dem gewünschten Peer öffnen.


#### Methode A - Verwendung des Olympus LSP


Das ist eine sehr einfache und direkte Möglichkeit, einen neuen LN-Nutzer mit ZEUS einzubinden. Es könnte ein völlig neuer Bitcoin-Nutzer sein, der keine Sats hat, der von einem Freund eingebunden wird, oder ein neuer Händler, der mit seiner ersten LN-Zahlung beginnt.

Standardmäßig verwendet ZEUS seinen eigenen LSP, Olympus. Später kannst du auch zu anderen LSPs wechseln, die dieses 0-conf-Protokoll unterstützen, um Kanäle zu öffnen.

Indem du einfach eine Invoice in deinem ZEUS erstellst (gib den Betrag ein und klicke auf die "Anfordern"-Schaltfläche), kannst du diese Sats sofort empfangen.

Die von dir erstellte Invoice wird [verpackt](https://docs.zeusln.app/lsp/wrapped-invoices) und es werden die mit dem Service verbundenen Gebühren angezeigt, falls sie bezahlt werden. Diese Wrapped Invoice enthält Route-Hinweise zu deinem ZEUS-Node, sodass der LSP deinen neuen Node finden und einen Kanal mit den neuen Guthaben, die du einzahlst, zu deinem ZEUS-Node öffnen kann.


![Image](assets/en/06.webp)


![Image](assets/en/07.webp)


Sobald die Invoice in ZEUS erstellt ist, bezahle sie einfach mit einer anderen Lightning-Wallet, und dein Kanal wird sofort geöffnet. [Konsultiere die Zeus LSP-Gebühren](https://docs.zeusln.app/lsp/fees).


Ein weiterer Vorteil des Bezahlens für einen Kanal ist das "zero fee routing". Das bedeutet, dass der erste Hop durch OLYMPUS von ZEUS keine Routing-Gebühren verursacht. Beachte, dass Hops jenseits von OLYMPUS von ZEUS weiterhin Gebühren von dir verlangen.

Sobald der Kanal bereit ist, klicke auf die rechte Schaltfläche unten auf dem Bildschirm, die die ZEUS-Kanäle anzeigt.


![Image](assets/en/08.webp)


Und du wirst einen Kanal wie diesen sehen, der deine Kanalbilanz anzeigt:


![Image](assets/en/09.webp)


Für mehr, was du von diesem Kanal ausgibst, desto mehr eingehende Liquidität hast du. Für mehr Sats, die du in diesen Kanal empfängst, hast du weniger eingehenden Liquiditäts-Raum.

Hier ist eine nette einfache visuelle Demonstration (von Rene Pickhardt) darüber, wie LN-Kanäle funktionieren:

In diesem Moment, wenn du auf den Namen des Kanals klickst, siehst du mehr Details darüber.


Du hast einen einzelnen Kanal mit Olympus, mit einer Gesamtkapazität von 490.000 Sats, mit einem Guthaben von 378k Sats auf deiner Seite und 88k Sats auf der Seite von Olympus. Das bedeutet, dass du maximal 88k Sats mehr in demselben Kanal empfangen kannst.

Falls du mehr als 88k Sats (die verfügbare eingehende Liquidität in diesem Fall) empfangen musst, sagen wir weitere 500k Sats, indem du einfach eine neue LN-Invoice mit diesem Betrag erstellst, wird eine neue Kanalanfrage an den Olympus LSP ausgelöst. Also wirst du einen 2. Kanal erhalten.

Deshalb ist es empfehlenswert, beim ersten Mal einen größeren Kanal zu öffnen, sagen wir 1-2M Sats. Sobald er geöffnet ist, kannst du einen Teil dieser Sats, sagen wir 50%, auf die On-Chain-Wallet auslagern, indem du einen beliebigen externen Tauschdienst verwendest, der in dieser Anleitung beschrieben ist.

Sobald du einen Teil aus diesem Kanal ausgelagert hast, sagen wir 50%, und die Sats zurück in deine eigene ZEUS On-Chain-Wallet bringst, bist du bereit, zur nächsten Methode des Öffnens eines neuen Kanals - von der On-Chain-Bilanz - überzugehen.


#### Methode B - Verwendung deines Onchain-Guthabens


Mit dieser Methode kannst du Kanäle zu jedem anderen LN-Node öffnen, einschließlich desselben Olympus LSP. Aber falls du bereits einen Kanal mit Olympus hast, ist es empfehlenswert, auch einen mit einem anderen Node zu haben, für mehr Zuverlässigkeit, und du kannst auch MPP (multi-part payment) verwenden.


![Image](assets/en/10.webp)


Oben ist ein Beispiel dafür, wie eine LN-Invoice unter Verwendung von MPP bezahlt wird. Wie du unten auf dem Bildschirm siehst, hast du "Einstellungen" und es öffnet sich eine Dropdown-Seite mit mehr Details für die Zahlung, die du gleich tätigen wirst. In diesem Bildschirm, falls du mindestens 2 Kanäle geöffnet hast, wird das MPP-Feature standardmäßig aktiviert. Auch kannst du AMP (atomare Multi-Pfad-Zahlungen) aktivieren und spezifische Teile einstellen, die du möchtest. Das ist ein mächtiges Feature!


Für einen privaten Node wie ZEUS empfehle ich, 2-3 gute Kanäle (max. 4-5) zu haben, mit guten LSPs und guter Liquidität, um alle deine Bedürfnisse zum Senden oder Empfangen von Sats über LN zu decken. [Siehe mehr LN-Node-Liquiditäts-Ratschläge in dieser Anleitung](/nodes/managing-lightning-node-liquidity-de.html). Auch hier ein weiterer [allgemeiner Leitfaden über LN-Liquidität](https://Bitcoin.design/guide/how-it-works/liquidity/) vom Bitcoin-Designteam.


Die Wahl der richtigen Peers ist, wie ich weiß, keine einfache Aufgabe, sogar für erfahrene Benutzer. [Deshalb gebe ich dir einige Optionen, um zu beginnen,](https://github.com/ZeusLN/zeus/discussions/2265) dies sind Peer-Nodes, die ich selbst mit ZEUS getestet habe (ich habe versucht, nur mit LND-Nodes zu verbinden, um Inkompatibilitätsprobleme zu vermeiden).

Hier ist auch eine Liste von bestätigten Peer-Nodes für ZEUS. Falls du gute kennst, bist du herzlich eingeladen, sie zu dieser Liste hinzuzufügen.

Du kannst einen Kanal in ZEUS öffnen, indem du zur Kanalansicht gehst, indem du auf das Kanal-Symbol in der unteren rechten Ecke der Hauptansicht klickst, und dann auf das + Symbol in der oberen rechten Ecke klickst.


![Image](assets/en/11.webp)


Falls du einen Kanal mit einem bestimmten Node öffnen möchtest, klicke auf (A) oben, um den Node QR nodeID zu scannen (auf Mempool, Amboss, 1ML kannst du diesen QR erhalten) und alle Peer-Details werden automatisch ausgefüllt.


MERKE:


- ZEUS eingebetteter Node verwendet keinen Tor-Dienst! Also versuche bitte nicht, Kanäle mit Nodes zu öffnen, die unter Tor sind! Du richtest dir damit mehr Schaden an, als dass du mehr Privatsphäre erhältst. Tor für LN bietet keine zusätzliche Privatsphäre, sondern sorgt nur für zusätzliche Probleme.
- Wähle deine Peers weise aus, besser sind gute LSPs, gute Routing-Nodes, keine zufälligen Pleb-Nodes, die deine Kanäle schließen und keine gute Liquidität bieten könnten. [Hier habe ich einen speziellen Leitfaden](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) über Liquidität und Beispiele von Nodes geschrieben.


Falls du direkt auf die Schaltfläche "Kanal zu Olympus öffnen" klickst, werden die erforderlichen Felder zum Öffnen eines Kanals zu [OLYMPUS by ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581) ausgefüllt.


Im Gegensatz zu bezahlten LSP-Kanälen erfordert dein Kanal eine On-Chain-Bestätigung, unter Verwendung deiner On-Chain-Mittel (du kannst aus deinen UTXOs in der Kanalöffnungsansicht auswählen); er wird nicht sofort geöffnet. Bitte konsultiere zuerst die aktuellen Mempool-Gebühren und passe sie entsprechend an, je nachdem, wie schnell du diesen Kanal öffnen möchtest.

Bevor du auf die Schaltfläche zum Öffnen des Kanals klickst, ziehe die erweiterten Optionen nach unten:


![Image](assets/en/12.webp)


Du musst auch sicherstellen, dass der Kanal unangekündigt (privat) ist. Standardmäßig ist die Option für angekündigte Kanäle deaktiviert. Diese Option wird nur dann empfohlen, wenn du ZEUS mit deinem Remote-Node als öffentlichem Routing-Node verwendest, ist nützlich.


Im Gegensatz zu bezahlten LSP-Kanälen profitierst du nicht von Null-Gebühren-Routing, indem du Kanäle mit dieser Methode öffnest.

Und fertig, klicke einfach auf die Schaltfläche "Kanal öffnen", warte, bis die Transaktion von den Minern bestätigt wurde. Sobald der Kanal geöffnet ist, kannst du nach Belieben mit den Sats von deinen Kanälen transagieren.

Denke daran, dass diese Kanäle die gesamte Bilanz auf DEINER Seite haben, sodass du keine eingehende Liquidität hast. Wie ich bereits sagte, tausche einen Teil aus oder gib einige Sats aus, indem du über LN einkaufst, um "mehr Raum" zu schaffen, um zu empfangen.

Stelle dir deine LN-Kanäle wie ein Glas Wasser vor. Du gießt etwas Wasser (Sats) in ein leeres Glas (dein Kanal), bis du es füllst. Du kannst kein weiteres Wasser eingießen, bis du etwas trinkst (ausgibst/swap out). Wenn das Glas fast leer ist, gieße mehr Wasser (Sats) hinein, indem du einen Swap in verwendest. [Lies mehr über externe Swap-Dienste hier.](https://darth-coin.github.io/nodes/lightning-submarine-swaps-en.html).


Es gibt auch andere LSP-Dienste, die dir eingehende Kanäle verkaufen: LNBig oder Bitrefill. Ich denke, es gibt noch mehr solcher Dienste, aber ich kann mich gerade nicht daran erinnern.

Also, falls du praktisch einen leeren LN-Kanal (die Bilanz ist 100% auf der Peer-Seite von Anfang an) benötigst, um mehr Zahlungen zu empfangen, als du mit deinen bestehenden, gefüllten Kanälen handhaben kannst, könnte dies eine sehr gute Option sein. Du zahlst eine spezifische Gebühr für das Öffnen dieser Kanäle und erhältst viel eingehenden Raum.


## TIPPS UND TRICKS


### Eingehende Reservegrenzen


Derzeit ist es aufgrund einiger LN-Code-Beschränkungen nicht möglich, genau die in "Eingehend" angezeigte Menge zu empfangen. Beachte immer, dass du deine Invoices mit einem leicht geringeren Betrag erstellen solltest, entsprechend dem "Kanal-Lokalreserve"-Betrag.


![Image](assets/en/13.webp)


Wie du im obigen Bild sehen kannst, zeigt "Inbound" an, dass ich noch 5101 Sats empfangen kann, aber in Wirklichkeit ist es in diesem Moment unmöglich, mehr zu empfangen. Und du kannst beobachten, dass es die gleiche Menge wie die "Lokale Reserve" ist.


Beachte also, wenn du Invoices zum Empfangen erstellst, wirf auch einen Blick auf deine Kanal-Liquidität und ziehe die lokale Reserve von diesem Betrag ab, falls du den empfangbaren Betrag bis zum Maximum ausreizen möchtest.


### Kurzer Rat für neue Benutzer, die mit Zeus Node beginnen:



- Nutze deine neuen Kanäle richtig.


Zum Beispiel, falls du weißt, dass du in einer Woche etwa 1M Sats empfangen wirst, öffne einen 2M Sats Kanal und tausche 50-60% deiner ausgehenden Liquidität in die On-Chain-Wallet oder in ein (vorübergehendes) verwahrte LN-Konto aus. Sei immer auf mehr Liquidität vorbereitet. Falls du mehr Liquidität in deinen ZEUS-Kanälen benötigst, kannst du sie aus den custodial Accounts zurückholen.

- Falls du ein Händler bist und regelmäßig mehr empfangen wirst, als du ausgibst, kaufe einen dedizierten eingehenden Kanal. Das ist die kostengünstigste Möglichkeit. Du zahlst eine minimale Gebühr und erhältst einen "leeren" Kanal.

- Öffne keine kleinen, sinnlosen Kanäle von 50-100-300-500k Sats. Du wirst sie in Tagen füllen, selbst wenn du sie nur für Zaps verwendest. Öffne größere und verschiedene, NICHT nur einen Kanal.
Sobald du einen größeren Kanal geöffnet hast, kannst du immer externe submarine swaps verwenden, um Sats in deine On-Chain-Wallets (einschließlich zurück zu ZEUS On-Chain) zu bewegen. Es ist gut, eine Balance zwischen ein- und ausgehender Liquidität zu halten, und du kannst diese Sats auch "wiederverwenden", um mehr Kanäle zu öffnen, falls du möchtest.


### Wrapped Invoice


Falls du beim Empfangen mehr Privatsphäre wünschst, kannst du die "Wrapped Invoice" Methode verwenden. Beachte: Um dies zu können, benötigst du einen Kanal mit Olympus LSP. Wrapped Invoices "verstecken" das endgültige Ziel (deinen ZEUS-Node) und zeigen den LSP-Node als Empfänger für den Zahler an.

Um eine "Wrapped Invoice" zu erhalten, gehe auf den Haupt-Tastenfeld-Bildschirm, gib den Betrag ein und klicke auf "Anfordern". Es wird ein normaler QR-Code für deine Invoice angezeigt. Jetzt klicke auf die obere rechte "X"-Schaltfläche, und du wirst zu mehr Optionen für die Invoice weitergeleitet.

![Image](assets/en/14.webp)


Jetzt musst du die obere Option "LSP aktivieren" und dann auf die Schaltfläche "Invoice erstellen" klicken. Diese Option erstellt die wrapped invoice und beachte, dass sie eine kleine Gebühr erhebt.


### Invoices mit Route-Hinweisen


Das ist ein sehr nützliches Feature, falls du die eingehende Kanal-Liquidität mehrerer Kanäle verwalten möchtest. Praktisch kannst du angeben, in welchen eingehenden Kanal du die Sats von einer Invoice empfangen möchtest.

Dieses Feature kann auch für zirkuläre Rebalancing verwendet werden, wenn du Liquidität von einem gefüllten Kanal in einen leeren verschieben möchtest.

Wie erstellt man eine Invoice mit Route-Hinweisen?

- Auf dem Hauptbildschirm wische nach rechts, um das LN-Menü zu öffnen, und klicke auf "Empfangen".
- Gehe im Invoice-Setup zum unteren Teil und aktiviere die Schaltfläche "Route-Hinweise einfügen", dann wähle die "Benutzerdefiniert"-Registerkarte. Es wird ein Bildschirm mit allen deinen verfügbaren Kanälen geöffnet. Wähle den aus, in den du empfangen möchtest.
- Fülle alle anderen Invoice-Details aus, Betrag, Memo usw. und klicke auf "Invoice erstellen".
- Das Bezahlen dieser Invoice bringt die Sats in den angegebenen Kanal.

Falls du diese Invoice an dich selbst bezahlen möchtest (zirkuläres Rebalancing), wähle im Zahlungsbildschirm den ausgehenden Kanal (einer mit mehr Liquidität) aus, der als Zahlungssender verwendet werden soll.


### Bezahlen mit Keysend


Keysend ist ein sehr unterschätztes LN-Feature, und Benutzer sollten es häufiger verwenden.


[Keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend) ermöglicht es Benutzern im Lightning-Netzwerk, Zahlungen direkt an ihren öffentlichen Schlüssel zu senden, solange ihr Node öffentliche Kanäle hat und Keysend aktiviert ist. Keysend erfordert keine Invoice vom Empfänger.


Also, wie kannst du das mit ZEUS machen?

Einfach die Empfänger-NodeID scannen oder kopieren (oder ZEUS-Kontakte verwenden, um deine regelmäßigen Empfänger-Nodes als Kontakte zu speichern) und dann auf dem Haupt-ZEUS-Bildschirm auf die "Senden"-Schaltfläche klicken. In diesem Bildschirm dann den NodeID einfügen oder aus deinen Kontakten auswählen.

Gib den Betrag in Sats ein, eine Nachricht, falls notwendig (ja, du kannst es auch als geheimen Chat über LN verwenden) und klicke auf die "Senden"-Schaltfläche. Fertig!


![Image](assets/en/15.webp)


Falls du einen direkten Kanal mit dem Ziel-Peer hast, sind KEINE Gebühren involviert.

Falls du keinen direkten Kanal mit dem Ziel-Peer hast, wird die Keysend-Zahlung die Gebühren wie eine normale LN-Invoice bezahlen, geroutet auf einem regulären Pfad wie jede andere Zahlung. Nur dass, beachte, es bleibt KEINE Spur als eine LN-Invoice.


## Fazit


Ich empfehle die Lektüre des Leitfadens [Advanced usage of Zeus](https://darth-coin.github.io/wallets/zeus-node-advanced-usage-en.html) mit weiteren Anweisungen und Anwendungsfällen.


Und… das war's! Ab jetzt verwendest du einfach den ZEUS-Node als eine reguläre BTC/LN-Wallet auf deinem Mobilgerät. Die Benutzeroberfläche ist ziemlich intuitiv und einfach zu verwenden, intuitiv für jeden Benutzertyp, ich denke, ich muss nicht weiter ins Detail gehen, wie man Zahlungen macht und empfängt.

Zusammenfassend hier ein Vergleich der Privatsphäre:


![Image](assets/en/16.webp)
