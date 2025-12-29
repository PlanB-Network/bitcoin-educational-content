---
name: Vererbungsplan Bitcoin
description: Wie Sie Bitcoins an Ihre Lieben übertragen
---

![cover](assets/cover.webp)



Die Übertragung von Bitcoins stellt eine große technische Herausforderung dar, die viele Inhaber übersehen. Im Gegensatz zu traditionellen Bankguthaben, bei denen ein Finanzinstitut die Gelder an die rechtmäßigen Eigentümer überweisen kann, funktioniert Bitcoin ohne Vermittler. Ihre Angehörigen werden niemals in der Lage sein, ohne die erforderlichen technischen Informationen auf Ihre Gelder zuzugreifen, unabhängig von ihrer rechtlichen Legitimität.



Dieses Lernprogramm führt Sie durch die Erstellung eines technischen Nachlassplans. Sie erfahren, wie die on-chain-Mechanismen für die automatische Übertragung funktionieren, wie Sie Ihre Konfigurationen dokumentieren und wie Sie die richtigen Lösungen wählen, um sicherzustellen, dass Ihr Bitcoin-Erbe für Ihre Angehörigen zugänglich bleibt.



## Warum ein Plan für das technische Erbe unerlässlich ist



Bitcoin basiert auf einem grundlegenden kryptografischen Prinzip: Wer die privaten Schlüssel besitzt, kontrolliert das Geld. Diese Souveränität wird zu einer großen Schwachstelle, wenn der Inhaber verschwindet, ohne die erforderlichen Informationen übermittelt zu haben.



Ein Bitcoin-Erbschaftsplan muss zwei scheinbar widersprüchliche Ziele erfüllen: Er muss es Ihren Angehörigen ermöglichen, zu gegebener Zeit auf Ihr Vermögen zuzugreifen, und gleichzeitig verhindern, dass jemand anderes vorzeitig darauf zugreift. Dieses empfindliche Gleichgewicht beruht auf den nativen Programmierfähigkeiten von Bitcoin.



Die technische Komplexität stellt eine zusätzliche Schwierigkeit dar. Ihre Erben müssen Konzepte wie Wiederherstellungsphrasen, Portfoliodeskriptoren oder Ableitungspfade manipulieren. Ohne angemessene Vorbereitung riskiert selbst ein wohlmeinender Erbe, irreversible Fehler zu machen.



## Wie on-chain-Vererbung funktioniert



Bitcoin verwendet seine Skriptsprache, um Ausgabenbedingungen direkt in Transaktionen zu kodieren. Die on-chain-Vererbung macht sich diese Programmierbarkeit zunutze, um alternative Wiederherstellungspfade zu schaffen, die automatisch aktiviert werden.



### Timelocks



Timelocks sind der grundlegende Mechanismus der Bitcoin-Vererbung. Sie ermöglichen die Sperrung von Mitteln, bis eine Zeitbedingung erfüllt ist.



**CLTV (CheckLockTimeVerify)**: Diese absolute Zeitsperre überprüft, ob ein bestimmter Zeitpunkt (Datum oder Blockhöhe) erreicht wurde, bevor die Ausgabe genehmigt wird. Zum Beispiel: "Diese Mittel können erst nach Block 900000 ausgegeben werden" oder "nach dem 1. Januar 2026". Der Vorteil von CLTV besteht darin, dass lange Verzögerungen (mehrere Jahre) möglich sind, das Datum jedoch feststeht und für alle UTXOs im Portfolio identisch gilt. Um die Kontrolle über Ihre Mittel zu behalten, müssen Sie in regelmäßigen Abständen ein neues Portfolio mit einem verlängerten Verfallsdatum anlegen und Ihre Mittel dorthin übertragen.



**CSV (CheckSequenceVerify)**: Diese relative Zeitsperre prüft, ob eine bestimmte Anzahl von Blöcken seit der Erstellung des UTXO verstrichen ist. Zum Beispiel: "Diese Mittel können nur 52560 Blöcke (~1 Jahr) nach Erhalt ausgegeben werden". Der Vorteil von CSV ist, dass jeder UTXO seinen eigenen unabhängigen Zähler hat. Jedes Mal, wenn Sie eine Transaktion durchführen, setzen die neu erstellten UTXOs ihr eigenes Zeitlimit zurück. Allerdings schränkt die technische Grenze von 65535 Blöcken (~15 Monate maximal) die möglichen Zeiträume ein. Dieser Ansatz ist für den täglichen Gebrauch natürlicher, da Ihre normale Tätigkeit die Fristen automatisch nach hinten verschiebt.



### Mehrere Ausgabenwege



Ein Vererbungsportfolio kombiniert mehrere Ausgabenwege in jeder Adresse:





- Hauptweg** : Der Eigentümer kann sein Geld jederzeit mit seinem Hauptschlüssel ausgeben, ohne zeitliche Begrenzung.
- Wiederherstellungspfad(e)**: Ein oder mehrere alternative Schlüssel können erst nach Ablauf einer bestimmten Zeit Mittel ausgeben.



Jede vom Eigentümer durchgeführte Transaktion "frischt" den UTXO auf und erzeugt neue Ausgänge mit zurückgesetzten Zeitschaltern. Dieser Mechanismus stellt sicher, dass die Wiederherstellungspfade niemals aktiviert werden, solange der Eigentümer aktiv bleibt.



### Miniscript und Taproot



**Miniscript** ist eine von Andrew Poelstra, Pieter Wuille und Sanket Kanjalkar entwickelte strukturierte Sprache, die das Schreiben und Analysieren komplexer Bitcoin-Skripte erleichtert. Sie ermöglicht es Ihnen, lesbare und überprüfbare Ausgabebedingungen zusammenzustellen, die für Vererbungskonfigurationen mit mehreren Schlüsseln und Zeitgebern unerlässlich sind.



**Taproot** (aktiviert im November 2021) verbessert die on-chain-Vererbung erheblich. Dank seiner Baumstruktur (MAST) wird nur die verwendete Ausgabebedingung in der Blockchain offengelegt. Wenn der Eigentümer seine Mittel normal ausgibt, bleiben die Vererbungsbedingungen unsichtbar. Diese Vertraulichkeit verringert auch die Transaktionskosten für komplexe Pfade.



## Die entscheidende Bedeutung von Deskriptoren



Bei Altbeständen reicht die Rückforderungsphrase (seed) nicht aus, um den Zugang zu den Mitteln wiederherzustellen. Der **Deskriptor** wird zum entscheidenden Element.



Ein Deskriptor ist eine Zeichenfolge, die die Struktur eines Portfolios ausführlich beschreibt: die beteiligten öffentlichen Schlüssel, die Ausgabebedingungen, die Ableitungspfade und die konfigurierten Zeitsperren. Hier ist ein vereinfachtes Beispiel:



```
wsh(or_d(pk([fingerprint/path]xpub...),and_v(v:pkh([fingerprint/path]xpub...),older(52560))))
```



Dieser Deskriptor besagt, dass entweder der Hauptschlüssel sofort oder der Wiederherstellungsschlüssel nach 52560 Blöcken ausgegeben werden kann.



Lassen Sie uns dieses Beispiel auspacken:




- wsh() : Witness Script Hash, gibt den Adresstyp an (P2WSH)
- or_d()`: "oder"-Bedingung mit einer Standardverzweigung
- pk([Fingerabdruck/Pfad]xpub...)`: Der öffentliche Hauptschlüssel mit seinem Fingerabdruck und dem Ableitungspfad
- und_v()`: "und"-Bedingung, die den Wiederherstellungsschlüssel mit der Zeitsperre kombiniert
- älter(52560)`: Die relative Zeitsperre von 52560 Blöcken



**Ohne den Deskriptor sind Ihre Erben trotz aller Wiederherstellungsphrasen nicht in der Lage, das Portfolio wiederherzustellen.** Ein Standardportfolio kann nur aus seed wiederhergestellt werden, da es standardisierten Ableitungspfaden folgt (BIP44, BIP84). Ein Legacy-Portfolio hingegen verwendet angepasste Skripte, die nicht erraten werden können. Das Deskriptor-Backup (oder die von Ihrer Software exportierte Konfigurationsdatei) muss die Wiederherstellungsphrasen in Ihrem Vererbungsplan begleiten.



## Dokumentarische Bestandteile eines Nachlassplans



Abgesehen von den technischen Mechanismen stützt sich ein wirksamer Legacy-Plan auf drei Säulen der Dokumentation.



### Der Erbschaftsbrief



Dieses persönliche Schreiben ist der Einstieg in Ihren Plan. Er ist für Ihre Erben bestimmt und erläutert den Kontext und die zu treffenden Vorkehrungen.



Ihr Schreiben muss ausdrückliche Sicherheitsvorschriften enthalten:




- Überstürzen Sie nichts, nehmen Sie sich Zeit zum Lernen, bevor Sie Geld einzahlen
- Übermitteln Sie einer einzelnen Person niemals eine vollständige Wiederherstellungsphrase
- Geben Sie niemals eine Wiederherstellungsphrase in ein ungeprüftes Softwareprogramm oder einen Computer ein
- Hüten Sie sich vor Betrügern und Menschen, die unaufgefordert Hilfe anbieten
- Holen Sie den Rat von mindestens zwei Personen Ihres Vertrauens ein, bevor Sie eine Entscheidung treffen



Dieses Schreiben enthält auch die Kontaktdaten Ihres Notars und den Ort, an dem sich Ihr Testament befindet. Es sollte niemals Wiederherstellungsphrasen oder Passwörter enthalten.



### Das Verzeichnis der vertrauenswürdigen Kontakte



Kein Erbe sollte mit der Bitcoin-Wiederbeschaffung allein sein. In diesem Verzeichnis sind Personen aufgeführt, die technische oder rechtliche Unterstützung leisten können.



Dokumentieren Sie für jeden Kontakt: vollständiger Name, Beziehung zu Ihnen, Rolle in dem Plan, Grad des Vertrauens, Bitcoin-Fähigkeiten und vollständige Kontaktangaben. Die Grundregel: Ihre Erben sollten immer mindestens zwei verschiedene Personen konsultieren, bevor sie eine wichtige Entscheidung treffen.



### Bitcoin Anlageninventar



In diesem Abschnitt finden Sie alle Ihre Bitcoins mit den technischen Informationen, die Sie benötigen, um sie wiederzuerlangen.



Dokumentieren Sie für jedes Portfolio :




- Portfoliotyp**: Hardware, Software, Konfiguration (Single-Sig, Multisig, Legacy)
- Gerätestandort**: physischer Standort der wallet-Hardware
- Speicherort der Descriptor/Konfigurationsdatei**: wichtig für fortgeschrittene Portfolios
- Ort der Rückgewinnungsphrase**: getrennt vom Deskriptor
- Zugangscodes**: wo PINs und Passphrasen gespeichert werden
- Konfigurierte Verzögerungen**: wenn Wiederherstellungspfade aktiviert werden



## Technische Lösungen verfügbar



Mehrere Softwarepakete implementieren on-chain-Vererbungsmechanismen. Jedes hat seine eigenen technischen Merkmale.



### Liana



Liana ist eine Desktop-Software (Linux, macOS, Windows), die Miniscript verwendet, um Portfolios mit zeitlich festgelegten Wiederherstellungspfaden zu erstellen. Das Projekt wird von Wizardsardine entwickelt, das von Antoine Poinsot (Bitcoin Core contributor) mitbegründet wurde.



**Technische Architektur**: Liana erstellt standardmäßig P2WSH-Portfolios (SegWit nativ), wobei Taproot-Unterstützung je nach Kompatibilität Ihrer wallet-Hardware verfügbar ist. Die Architektur basiert auf einem Hauptpfad und einem oder mehreren Wiederherstellungspfaden. Der generierte Deskriptor kodiert alle Bedingungen und muss gespeichert werden.



**Verwendete Timelocks**: Liana verwendet relative Zeitsperren (CSV), begrenzt auf 65535 Blöcke (~15 Monate). Um die Kontrolle zu behalten, müssen Sie eine Auffrischungstransaktion durchführen, bevor das Timelock abläuft.



**Hardware wallet-Integration**: BitBox02, Blockstream Jade, Coldcard, Ledger, Specter DIY und andere Geräte sind zum Signieren von Transaktionen kompatibel.



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

### Bitcoin Keeper



Bitcoin Keeper ist eine mobile Anwendung (iOS, Android), die Multisig und Timelocks über ihre "Enhanced Vaults" kombiniert. Der mobile Ansatz mit integrierter Anleitung macht sie auch für technisch weniger versierte Nutzer zugänglich.



**Technische Architektur**: Erweiterte Tresore verwenden Miniscript, um Multisig-Konfigurationen zu erstellen, bei denen zusätzliche Schlüssel nach bestimmten Verzögerungen aktiviert werden. Der Vererbungsschlüssel ergänzt das bestehende Quorum, während der Notfallschlüssel die Multisig-Konfiguration vollständig umgehen kann.



**Verwendete Timelocks**: Bitcoin Keeper verwendet absolute Timelocks (CLTV), die Vorlaufzeiten von mehr als 15 Monaten ermöglichen. Das Aktivierungsdatum wird bei der Erstellung von wallet festgelegt und gilt für alle UTXOs. Die Anwendung verfügt über eine "Wiederauffrischungsfunktion", die die Auffrischung automatisch verwaltet: Der Benutzer folgt einfach den geführten Schritten, ohne manuell ein neues wallet erstellen zu müssen.



**Zusätzliche Funktionen**: Integrierte Vererbungsdokumente, Canary Wallets zur Erkennung von Schlüsselkompromittierungen und Aktualisierungserinnerungen.



https://planb.academy/tutorials/wallet/mobile/bitcoin-keeper-7f2a160b-10b6-4cc5-8820-514ee2eb1599

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

### Erbe



Heritage ist eine Desktop-Anwendung, die Taproot-Skripte zur Kodierung von Vererbungsbedingungen verwendet. Die Verwendung von Taproot bietet eine verbesserte Vertraulichkeit, da ungenutzte Pfade in der Blockchain unsichtbar bleiben.



**Technische Architektur**: Jede Erbenadresse umfasst einen Hauptpfad und alternative Pfade für jeden Erben, mit progressiven Zeitrahmen. Die hierarchische Struktur ermöglicht es, ein persönliches Backup mit 6 Monaten und Familienerben mit 12-15 Monaten zu definieren.



**Nutzungsmodi**: Eigenständige Version mit eigenem Knotenpunkt (kostenlos) oder verwalteter Dienst, der Erinnerungen und Benachrichtigungen an Erben hinzufügt (0,05%/Jahr).



https://planb.academy/tutorials/wallet/desktop/heritage-0549701f-2619-4037-ad05-44982be73ef4

## Der Genesungsprozess des Erben



Ein Verständnis des Einziehungsprozesses hilft bei der Erstellung eines wirksamen Plans. Hier sind die technischen Schritte, die ein Erbe befolgen muss.



### Anforderungen an die Einziehung



Der Erbe braucht :


1. **Der Deskriptor oder die Konfigurationsdatei** des ursprünglichen Portfolios (JSON oder Textformat, je nach Software)


2. **Seine Wiederherstellungsphrase** (die mit seinem Vererbungsschlüssel verbundene Phrase, normalerweise 12 oder 24 Wörter)


3. **Kompatible Software** (Liana, Bitcoin Keeper, Heritage oder Sparrow/Specter für Standarddeskriptoren)


4. **Eine Verbindung zu einem Bitcoin**-Knoten, um den Timelock-Status zu prüfen und die Transaktion zu übertragen



### Schritte zur Wiederherstellung



1. **Installieren Sie die Software** auf einem sicheren Gerät und konfigurieren Sie die Verbindung zum Bitcoin-Netzwerk (persönlicher Knoten oder Electrum-Server)


2. **Importieren Sie den Deskriptor**, um die Portfoliostruktur zu rekonstruieren. Die Software wird automatisch generate alle verwendeten Adressen


3. **Wiederherstellung des Vererbungsschlüssels** aus der Wiederherstellungsphrase. Die Software prüft, ob dieser Schlüssel mit einem der im Deskriptor autorisierten Schlüssel übereinstimmt


4. **Portfolio synchronisieren**, um alle UTXOs und ihre Ausgabenbedingungen zu ermitteln


5. **Überprüfen des Ablaufs der Zeitsperre**: Die Software zeigt für jedes UTXO an, ob der Wiederherstellungspfad aktiv ist


6. **Erstellen der Wiederherstellungstransaktion** an eine Adresse, die ausschließlich vom Erben kontrolliert wird (idealerweise ein neuer einzelner wallet)


7. **Unterzeichnung und Verbreitung** der Transaktion im Bitcoin-Netz



Wenn die Zeitsperre noch nicht abgelaufen ist, muss der Erbe warten. Die Software zeigt das Datum oder den Block an, ab dem eine Rückgabe möglich ist. Während dieser Wartezeit bleiben die Gelder auf der Blockchain sicher.



### Zu beachtende Punkte für den Erben



Der Erbe muss besonders darauf achten, dass :




- Prüfen Sie die Echtheit der heruntergeladenen Software** (Prüfsummen, Signaturen)
- Teilen Sie niemals Ihre Genesungsphrase** mit jemandem, der Ihnen Hilfe anbietet
- Konsultieren Sie mindestens zwei Personen Ihres Vertrauens**, bevor Sie eine Rückforderung durchführen
- Übertragen Sie die Mittel in ein einfaches Portfolio**, das er nach der Genesung vollständig kontrolliert



## Bewährte Praktiken



### Trennung von Informationen



Speichern Sie niemals alle Informationen an einem Ort. Der Deskriptor muss von den Wiederherstellungsphrasen getrennt sein, die wiederum von den PIN-Codes getrennt sind. Diese Aufteilung erschwert einem Angreifer den Zugang, während sie für Ihre rechtmäßigen Erben rekonstruierbar bleibt.



### Wiederherstellungstests



Bevor Sie größere Beträge einzahlen, sollten Sie den gesamten Wiederherstellungsprozess mit einem kleinen Betrag testen. Vergewissern Sie sich, dass Sie das Portfolio anhand des Deskriptors und der Wiederherstellungsphrasen auf einem leeren Gerät wiederherstellen können. Dokumentieren Sie die Schritte für Ihre Erben.



### Timelock-Wartung



Planen Sie die Auffrischung Ihrer Zeitsperren lange vor deren Ablauf. Bei einem 12-Monats-Timelock sollten Sie alle 9-10 Monate eine Transaktion durchführen. Die Software bietet in der Regel Erinnerungsfunktionen oder automatische Aktualisierungsfunktionen.



### Aktualisierung des Plans



Ihre Bitcoin-Konfiguration entwickelt sich weiter. Jede wesentliche Änderung (neues Portfolio, Änderung der Fristen, Hinzufügung eines Erben) muss in Ihrer Dokumentation festgehalten werden. Legen Sie eine jährliche Überprüfungsroutine fest.



## Wählen Sie Ihren Ansatz



Die Wahl zwischen den verschiedenen Lösungen hängt von Ihrem technischen Profil und Ihren spezifischen Bedürfnissen ab.



**Liana** ist für Desktop-Benutzer geeignet, die eine Open-Source-Software mit voller Kontrolle über ihren eigenen Knoten bevorzugen. Die Konfiguration bleibt dank der geführten Schnittstelle zugänglich. Relative Timelocks (CSV) vereinfachen die Wartung, da Ihre normale Tätigkeit die Fristen automatisch nach hinten verschiebt. Begrenzung: maximale Verzögerung von ca. 15 Monaten (65535 Blöcke).



**Bitcoin Keeper** richtet sich an mobile Nutzer, die eine intuitive Benutzeroberfläche mit integrierten Begleitdokumenten suchen. Die Anwendung bietet zwei Arten von Sonderschlüsseln: den Erbschaftsschlüssel (der zum Quorum beiträgt) und den Notfallschlüssel (der es vollständig umgeht). Absolute Timelocks (CLTV) ermöglichen Vorlaufzeiten von über 15 Monaten, wobei eine integrierte Auffrischungsfunktion die Auffrischung vereinfacht. Der Diamond Hands Plan schaltet erweiterte Legacy-Funktionen frei.



**Vererbung** richtet sich an technische Benutzer, die Taproot-Vertraulichkeit und hierarchische Vererbung mit progressiven Verzögerungen schätzen. Die Taproot-Baumstruktur verbirgt die Vererbungsbedingungen während normaler Transaktionen und gibt nur die bei der Wiederherstellung verwendete Bedingung preis.



Alle drei Lösungen haben eines gemeinsam: Sie müssen regelmäßig aktualisiert werden, um eine vorzeitige Aktivierung der Wiederherstellungspfade zu verhindern. Diese Einschränkung ist sowohl der Preis als auch die Garantie für das nicht vertrauenswürdige Erbe von on-chain. Planen Sie regelmäßige Erinnerungen ein und machen Sie diese Wartung zum Bestandteil Ihrer Bitcoin-Verwaltungsroutine.



## Schlussfolgerung



Ein technischer Bitcoin-Legacy-Plan kombiniert kryptographische Mechanismen (Timelocks, Miniscript, Taproot) mit strenger Dokumentation. Fortgeschrittene Wallets ermöglichen es Ihnen, Ihre Bitcoins nach einer gewissen Zeit der Inaktivität automatisch zu übertragen, ohne dass ein Dritter eingreifen muss.



Die wichtigsten Elemente, die Sie an Ihre Erben weitergeben sollten, sind: die Deskriptor- oder Konfigurationsdatei, die Wiederherstellungsphrase, detaillierte Wiederherstellungsanweisungen und die Kontaktdaten von kompetenten Personen, die ihnen helfen können.



Wählen Sie zunächst eine technische Lösung, die zu Ihrem Profil passt, testen Sie sie mit einer kleinen Menge und dokumentieren Sie das Ganze in einem strukturierten Plan. Die anfängliche Komplexität garantiert, dass Ihr Bitcoin-Vermögen in vollem Vertrauen weitergegeben wird.



## Ressourcen



### Vorlage Erbschaftsplan





- [Bitcoin Vorlage für einen Erbschaftsplan (PDF)](https://github.com/PlanB-Network/bitcoin-educational-content/blob/dev/resources/bet/seed-management-tools/assets/Bitcoin-Inheritance-Plan-Template.pdf) - Plan ₿ Network Dokumentationsvorlage



### Technische Referenzen





- [BIP-65 : OP_CHECKLOCKTIMEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki) - Spezifikation von absoluten Zeitgebern (CLTV)
- [BIP-112 : OP_CHECKSEQUENCEVERIFY](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki) - Angabe von relativen Timelocks (CSV)
- [Miniscript-Referenz](https://bitcoin.sipa.be/miniscript/) - Offizielle Miniscript-Dokumentation von Pieter Wuille



### Offizielle Webseiten zur Lösung





- [Liana Wallet](https://wizardsardine.com/liana/) - Wizardsardine
- [Bitcoin Keeper](https://bitcoinkeeper.app/) - Bithyve
- [Erbe Wallet](https://btc-heritage.com/) - Crypto7