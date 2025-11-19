---
name: Blixt Wallet
description: Wie können Sie einen leistungsstarken LN-Knoten auf Ihrem Mobiltelefon verwenden?
---
![cover](assets/cover.webp)


Dieser Leitfaden ist all jenen neuen Nutzern gewidmet, die Bitcoin Lightning Network (LN) in einer KOSTENLOSEN, VOLLSTÄNDIG NICHT KUNDENORIENTIERTEN Weise nutzen wollen.


Mit [Blixt Wallet] (https://blixtwallet.com/), einem vollständigen LN-Knoten auf Ihrem Handy, wo immer Sie sind.


Wenn Sie Bitcoin Lightning Network noch nie benutzt haben, lesen Sie bitte zunächst diese einfache Erklärung über Lightning Network (LN) (https://darth-coin.github.io/beginner/LN-airport-analogy-en.html).


## WICHTIGE ASPEKTE:



- Blixt ist ein privater Knoten, KEIN Routing-Knoten! Behalten Sie das im Hinterkopf: Das bedeutet, dass alle LN-Kanäle in Blixt dem LN-Graphen unangekündigt zur Verfügung stehen (so genannte private Kanäle). Das bedeutet, dass dieser Knoten KEIN ROUTING von anderen Zahlungen durch den Blixt-Knoten durchführt. Dieser Blixt-Knoten ist NICHT für das Routing, ich wiederhole. Er dient hauptsächlich dazu, Ihre eigenen LN-Kanäle zu verwalten und Ihre LN-Zahlungen privat abzuwickeln, wann immer Sie es brauchen. Dieser Blixt-Knoten muss online sein und synchronisiert werden, NUR BEVOR Sie Ihre Transaktionen durchführen. Aus diesem Grund sehen Sie oben ein Symbol, das den Synchronisierungsstatus anzeigt. Es dauert nur wenige Augenblicke, je nachdem, wie lange Sie ihn offline gehalten haben.



- Blixt verwendet LND (aezeed) als Wallet-Backend, versuchen Sie also nicht, andere Arten von Bitcoin-Geldbörsen in es zu importieren. [Hier haben Sie die Arten von Wallet Mnemonic Samen erklärt] (https://coldbit.com/what-types-of-Mnemonic-seeds-are-used-in-Bitcoin/). Und hier ist [eine ausführlichere Liste aller Arten von Geldbörsen](https://walletsrecovery.org/). Wenn du also vorher einen LND-Knoten hattest, kannst du die seed- und die backup.channels in Blixt importieren, [wie es in diesem Leitfaden erklärt wird](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html).



- Am Ende dieses Leitfadens finden Sie einen speziellen Abschnitt mit ["Tipps und Tricks"] (https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#tips)



- Blixt wichtige Links - siehe am Ende dieses Leitfadens, bitte bookmarken Sie sie.


---

## Blixt - Erster Kontakt


Also... Darths Mom hat beschlossen, LN mit Blixt zu verwenden. Hard Entscheidung, aber weise. Blixt ist nur für schlaue Leute und diejenigen, die wirklich mehr und tieferen Gebrauch von LN lernen wollen.


![blixt](assets/en/01.webp)


Darth warnt seine Mutter:


"*Mama, wenn du anfängst, Blixt LN Node zu benutzen, musst du zuerst wissen, was Lightning Network ist und wie es funktioniert, zumindest auf grundlegender Ebene. [Hier habe ich eine einfache Liste von Ressourcen über Lightning Network zusammengestellt (https://blixtwallet.github.io/faq#what-is-LN). Bitte lesen Sie diese zuerst.*"


Darth's Mom hat die Ressourcen gelesen und ihren ersten Schritt getan: Blixt auf ihrem brandneuen Android-Gerät installiert. Blixt ist auch für iOS und macOS (Desktop) verfügbar. Aber das ist nichts für Darths Mutter... Trotzdem wird empfohlen, eine neuere Version von Android zu verwenden, mindestens 9 oder 10 für bessere Kompatibilität und Erfahrung. Die Ausführung eines vollständigen LN-Knotens auf einem mobilen Gerät ist keine leichte Aufgabe und könnte etwas Platz (mindestens 600 MB) und Speicherplatz beanspruchen.


Wenn du Blixt öffnest, werden dir auf dem "Willkommen"-Bildschirm einige Optionen angezeigt:


![blixt](assets/en/02.webp)


In der rechten oberen Ecke sehen Sie 3 Punkte, die ein Menü mit aktivieren:



- "enable Tor" - Nutzer können mit dem Tor-Netzwerk starten, insbesondere wenn sie einen alten LND-Knoten wiederherstellen wollen, der nur mit Tor-Peers lief.
- "Bitcoin-Knoten einstellen" - wenn der Benutzer sich direkt mit seinem eigenen Knoten verbinden möchte, um die Blöcke über Neutrino zu synchronisieren, kann er dies direkt auf dem Willkommensbildschirm tun. Diese Option ist auch gut für den Fall, dass Ihre Internetverbindung oder Tor nicht so stabil ist, um sich mit dem Standard-Bitcoin-Knoten (node.blixtwallet.com) zu verbinden.
- Bald wird die Sprache dort hinzugefügt, so dass der Benutzer direkt mit einer Sprache beginnen kann, die ihm angenehm ist. Wenn Sie zu diesem Open-Source-Projekt mit Übersetzungen in anderen Sprachen beitragen möchten, [bitte hier](https://explore.transifex.com/blixt-Wallet/blixt-Wallet/).


### OPTION A - Neue Wallet erstellen


Wenn Sie "ein neues Wallet erstellen" wählen, werden Sie direkt zum Hauptbildschirm von Blixt Wallet weitergeleitet.


Dies ist Ihr "Cockpit" und auch der "Haupt-LN Wallet". Beachten Sie also, dass hier nur der Saldo Ihres LN Wallet angezeigt wird. Der angeschlossene Wallet wird separat angezeigt (siehe C).


![blixt](assets/en/03.webp)


A - Blixt blockiert das Symbol der Synchronisationsanzeige. Dies ist das Wichtigste für einen LN Knoten: mit dem Netzwerk synchronisiert zu sein. Wenn dieses Symbol noch funktioniert, bedeutet das, dass dein Knoten NICHT BEREIT ist! Haben Sie also Geduld, besonders bei der ersten Synchronisation. Es kann bis zu 6-8 Minuten dauern, abhängig von Ihrem Gerät und Ihrer Internetverbindung.


Sie können darauf klicken und den Status der Synchronisierung sehen:


![blixt](assets/en/04.webp)


Sie können auch auf die Schaltfläche "LND-Protokoll anzeigen" (A) klicken, wenn Sie weitere technische Details des LND-Protokolls in Echtzeit sehen und lesen möchten. Dies ist sehr nützlich für die Fehlersuche und um mehr über die Funktionsweise des LN zu erfahren.


B - Hier können Sie auf alle Blixt-Einstellungen zugreifen, und das sind eine Menge! Blixt bietet viele Funktionen und Optionen, um deinen LN-Knoten wie ein Profi zu verwalten. Alle diese Optionen werden im Detail auf der "[Blixt Features Page](https://blixtwallet.github.io/features#blixt-options) - Options Menu" erklärt.


C - Hier haben Sie das "Magic Drawer"-Menü, [auch hier im Detail erklärt] (https://blixtwallet.github.io/features#blixt-drawer). Hier ist die "Onchain Wallet" (B), Lightning Channels (C), Kontakte, Channels Status Symbol (A), Keysend (D).


![blixt](assets/en/05.webp)


D - Ist das Hilfe-Menü, mit Links zu FAQ / Guides Seite, Kontakt Entwickler, Github Seite und Telegram Support Gruppe.


E - Geben Sie Ihre ersten BTC Address an, wo Sie Ihre ersten Tests Sats einzahlen können. DIES IST OPTIONAL! Wenn Sie direkt in diesen Address einzahlen, wird ein LN-Kanal zum Blixt Node geöffnet. Das bedeutet, dass Ihr eingezahltes Sats in eine andere Onchain-Transaktion (tx) geht, um diesen LN-Kanal zu öffnen. Sie können das in Blixt onchain Wallet überprüfen (siehe Punkt C), indem Sie auf das TX-Menü oben rechts klicken.


![blixt](assets/en/06.webp)


Wie Sie im Onchain-Transaktionsprotokoll sehen können, sind die Schritte sehr detailliert und geben an, wohin die Sats gehen (einzahlen, Kanal öffnen, schließen).


EMPFEHLUNG:


Nachdem wir mehrere Situationen getestet haben, sind wir zu dem Schluss gekommen, dass es viel effizienter ist, Kanäle zwischen 1 und 5 Mio. Sats zu öffnen. Kleinere Kanäle neigen dazu, schnell erschöpft zu sein und einen höheren Prozentsatz an Gebühren im Vergleich zu größeren Kanälen zu zahlen.


F - Zeigt Ihren Haupt-Wallet-Saldo in Lightning an. Dies ist NICHT Ihr gesamter Blixt Wallet Saldo, sondern nur der Sats, den Sie in Lightning Channels haben und der zum Senden verfügbar ist. Wie bereits erwähnt, ist der Onchain-Wallet separat. Behalten Sie diesen Aspekt im Auge. Das Onchain-Wallet ist aus einem wichtigen Grund separat: Es wird hauptsächlich zum Öffnen/Schließen von LN-Kanälen verwendet.


Ok, jetzt hat Darth's Mom etwas Sats in das auf dem Hauptbildschirm angezeigte onchain Address eingezahlt. Es wird empfohlen, dass Sie, wenn Sie das tun, Ihre Blixt-App online und aktiv für eine Weile zu halten, bis die BTC tx von den Minern in den ersten Block genommen wird.


Danach kann es bis zu 20-30 Minuten dauern, bis der Kanal vollständig bestätigt ist und Sie ihn im Magic Drawer - Lightning Channels als aktiv sehen. Auch der kleine farbige Punkt oben in der Schublade, wenn Green ist, zeigt an, dass Ihr LN-Kanal online ist und bereit ist, Sats über LN zu senden.


Der Address und die angezeigte Willkommensnachricht verschwinden. Es ist nun nicht mehr notwendig, einen automatischen Kanal zu öffnen. Sie können die Option auch im Menü Einstellungen deaktivieren.


Es ist an der Zeit, weiterzugehen und andere Funktionen und Optionen zu testen, um LN-Kanäle zu öffnen.


Nun wollen wir einen weiteren Kanal mit einem anderen Node-Peer öffnen. Die Blixt-Community hat [eine Liste guter Nodes für die Nutzung von Blixt] (https://github.com/hsjoberg/blixt-Wallet/issues/1033) zusammengestellt.


**Vorgehensweise zum Öffnen eines LN-Kanals in Blixt**


Das ist ganz einfach, man braucht nur ein paar Schritte und ein bisschen Geduld:



- Aufnahme in die [Blixt Community](https://github.com/hsjoberg/blixt-Wallet/issues/1033) Liste der Gleichgestellten
- Wählen Sie einen Knoten aus und klicken Sie auf den Link mit dem Namen des Knotens, um dessen Amboss-Seite zu öffnen
- Klicken Sie auf , um den QR-Code für den Knoten URI Address anzuzeigen


![blixt](assets/en/07.webp)


Öffnen Sie Blixt und gehen Sie zur obersten Schublade - Lightning Channels und klicken Sie auf die Schaltfläche "+"


![blixt](assets/en/08.webp)


Klicken Sie nun auf die Kamera (A), um den QR-Code von der Amboss-Seite zu scannen, und die Daten des Knotens werden ausgefüllt. Fügen Sie den Betrag des Sats für den gewünschten Kanal hinzu und wählen Sie dann den Gebührensatz für den Sender. Für eine schnellere Bestätigung können Sie die Einstellung auf Auto (B) belassen oder sie manuell durch Schieben der Taste anpassen. Sie können auch lange auf die Nummer drücken und sie nach Belieben bearbeiten.


Setzen Sie nicht weniger als 1 sat/vbyte ein! In der Regel ist es besser, die [Mempool Gebühren] (https://Mempool.space/) zu konsultieren, bevor Sie einen Kanal öffnen, und eine günstige Gebühr zu wählen.


Fertig, jetzt nur noch auf den Button "Kanal öffnen" klicken und auf 3 Bestätigungen warten, das dauert in der Regel 30 min (1 Block ca. alle 10min).


Sobald dies bestätigt ist, wird der Kanal in Ihrem Bereich "Blitzkanäle" als aktiv angezeigt.


---

## Blixt - Zweiter Kontakt


Jetzt haben wir also einen LN-Kanal mit nur OUTBOUND-Liquidität. Das bedeutet, dass wir nur SENDEN können, wir können immer noch nicht Sats über LN EMPFANGEN.


![blixt](assets/en/09.webp)


Warum? Haben Sie die eingangs erwähnten Leitfäden gelesen? Nein? Gehen Sie zurück und lesen Sie sie. Es ist sehr wichtig zu verstehen, wie LN-Kanäle funktionieren.


![blixt](assets/en/10.webp)


Wie Sie in diesem Beispiel sehen können, hat der Kanal, der mit der ersten Einzahlung geöffnet wurde, nicht allzu viel INBOUND-Liquidität ("Kann empfangen"), aber viel OUTBOUND-Liquidität ("Kann senden").


Welche Möglichkeiten haben Sie also, wenn Sie mehr Sats als LN erhalten möchten?



- Geben Sie einige Sats aus bestehenden Kanälen aus. Ja, LN ist ein Zahlungsnetzwerk von Bitcoin, das hauptsächlich dazu dient, Ihre Sats schneller, billiger, privat und einfach auszugeben. LN ist KEIN Hodling-Weg, dafür gibt es das onchain Wallet.



- Tauschen Sie einige Sats mit Hilfe eines U-Boot-Tauschdienstes zurück in Ihr Onchain-Wallet. Auf diese Weise geben Sie Ihr Sats nicht aus, sondern geben es Ihrem eigenen Onchain-Wallet zurück. Hier können Sie einige Methoden im Detail sehen, in der [Blixt Guides Page] (https://blixtwallet.github.io/guides).



- Öffnen Sie einen INBOUND-Kanal von einem beliebigen LSP-Anbieter. Hier ist eine Video-Demo über die Verwendung von LNBig LSP zur Eröffnung eines Inbound-Kanals. Das heißt, Sie zahlen eine kleine Gebühr für einen LEEREN Kanal (auf Ihrer Seite) und können mehr Sats in diesem Kanal empfangen. Wenn Sie ein Händler sind, der mehr einnimmt als ausgibt, ist das eine gute Option. Auch wenn Sie Sats über LN kaufen, Robosats oder einen anderen LN Exchange verwenden.



- Eröffnen Sie einen Dunder-Kanal mit dem Blixt-Knoten oder einem anderen Dunder-LSP-Anbieter. Ein Dunder-Kanal ist ein einfacher Weg, um etwas INBOUND-Liquidität zu erhalten, aber gleichzeitig zahlen Sie etwas Sats in diesen Kanal ein. Das ist auch deshalb gut, weil der Kanal mit einem [UTXO](https://en.Bitcoin.it/wiki/UTXO) geöffnet wird, das nicht von Ihrem Blixt Wallet stammt. Das sorgt für etwas mehr Privatsphäre. Es ist auch gut, weil, wenn Sie keine Sats in einem onchain Wallet haben, um einen normalen LN Kanal zu öffnen, aber Sie haben sie in einem anderen LN Wallet, können Sie einfach von diesem anderen Wallet durch LN die Öffnung und die Kaution (auf Ihrer Seite) dieses Dunder Kanals bezahlen. [Weitere Details, wie Dunder funktioniert und wie Sie Ihren eigenen Server betreiben können, finden Sie hier](https://github.com/hsjoberg/dunder-lsp).


![blixt](assets/en/11.webp)


Hier sind die Schritte zur Aktivierung der Öffnung eines Dunder-Kanals:



- Gehen Sie zu Einstellungen, aktivieren Sie im Abschnitt "Experimente" das Kästchen "Dunder LSP aktivieren".
- Sobald Sie das getan haben, gehen Sie zurück zum Abschnitt "Lightning Network" und Sie werden sehen, dass die Option "Set Dunder LSP Server" erscheint. Dort ist standardmäßig "https://dunder.blixtwallet.com" eingestellt, aber Sie können es mit jedem anderen Dunder LSP Provider Address ändern. [Hier ist eine Blixt-Community-Liste](https://github.com/hsjoberg/blixt-Wallet/issues/1033) mit Knoten, die Dudner LSP-Kanäle für Ihr Blixt bereitstellen können.
- Jetzt können Sie zum Hauptbildschirm gehen und auf die Schaltfläche "Empfangen" klicken. Gehen Sie dann wie folgt vor [wie in dieser Anleitung erklärt] (https://blixtwallet.github.io/guides#guide-lsp).


OK, nachdem der Dunder-Kanal bestätigt wurde (das dauert ein paar Minuten), haben Sie am Ende zwei LN-Kanäle: einen, der zunächst mit Autopilot geöffnet wurde (Kanal A), und einen mit mehr eingehender Liquidität, geöffnet mit Dunder (Kanal B).


![blixt](assets/en/12.webp)


Gut, jetzt sind Sie startklar, um genügend Sats über LN zu senden und zu empfangen!


GLÜCKLICHE Bitcoin BLITZ!


---

## Blixt - Dritter Kontakt


Erinnern Sie sich, im ersten Kapitel "Erster Kontakt" gab es 2 Optionen auf dem Willkommensbildschirm:


- [Option A](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#option-a) - Neues Wallet erstellen
- Option B - Wiederherstellung von Wallet


Lassen Sie uns nun besprechen, wie man einen abgestürzten Blixt Wallet oder einen anderen LND Knoten wiederherstellt. Dies ist etwas technischer, aber bitte passen Sie auf. Das ist nicht der Hard.


### OPTION B - Wiederherstellung von Wallet


In der Vergangenheit habe ich eine spezielle Anleitung über [wie man einen abgestürzten Umbrel-Knoten wiederherstellt] (https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html) geschrieben, in der ich auch die Methode der Verwendung von Blixt als Schnellwiederherstellungsprozess unter Verwendung der seed + channel.backup-Datei von Umbrel erwähnt habe.


Ich habe auch eine Anleitung geschrieben, wie du deinen Blixt-Knoten wiederherstellen oder dein Blixt auf ein anderes Gerät migrieren kannst, [hier](https://blixtwallet.github.io/faq#blixt-restore).


![blixt](assets/en/13.webp)


Aber lassen Sie uns diesen Prozess in einfachen Schritten erklären. Wie Sie auf dem Bild oben sehen können, gibt es 2 Dinge, die Sie tun sollten, um Ihren vorherigen Blixt/LND-Knoten wiederherzustellen:



- in das obere Feld müssen Sie alle 24 Wörter aus Ihrem seed (alter/toter Knoten) eintragen
- unten gibt es zwei Schaltflächen zum Einfügen/Hochladen der channel.backup-Datei, die zuvor von Ihrem alten Blixt/LND-Knoten gespeichert wurde. Es kann von einer lokalen Datei (Sie laden es in Ihr Gerät zuvor) oder kann von einem Google-Laufwerk / iCloud Remote-Speicherort sein. Blixt bietet die Möglichkeit, das Backup Ihrer Kanäle direkt in einem Google- oder iCloud-Laufwerk zu speichern. Weitere Details finden Sie auf der [Blixt Features Page] (https://blixtwallet.github.io/features#blixt-options).


Wenn Sie vorher keine offenen LN-Kanäle hatten, müssen Sie keine channels.backup-Datei hochladen. Fügen Sie einfach die 24 Wörter seed ein und klicken Sie auf die Schaltfläche Wiederherstellen.


Vergessen Sie nicht, Tor zu aktivieren, und zwar über das Menü mit den 3 Punkten oben, wie wir im Abschnitt Option A erklärt haben. Das ist der Fall, wenn Sie NUR Tor-Peers hatten und nicht über Clearnet (Domain/IP) kontaktiert werden konnten. Ansonsten ist das nicht notwendig.


Eine weitere nützliche Funktion ist die Einstellung eines bestimmten Bitcoin-Knotens in diesem oberen Menü. Standardmäßig werden Blöcke von node.blixtwallet.com synchronisiert (Neutrino-Modus), aber Sie können jeden anderen Bitcoin-Knoten einstellen, der Neutrino-Synchronisation bietet.


Wenn du diese Optionen ausfüllst und auf die Schaltfläche Wiederherstellen klickst, beginnt Blixt zunächst damit, die Blöcke über Neutrino zu synchronisieren, wie wir es im Kapitel Erster Kontakt erklärt haben. Sei also geduldig und beobachte den Wiederherstellungsprozess auf dem Hauptbildschirm, indem du auf das Sync-Symbol klickst.


![blixt](assets/en/14.webp)


Wie Sie in diesem Beispiel sehen können, zeigt es, dass die Bitcoin Blöcke zu 100% synchronisiert sind (A) und der Wiederherstellungsprozess im Gange ist (B). Das bedeutet, dass die LN-Kanäle, die Sie zuvor hatten, geschlossen werden und die Mittel in Ihrem Blixt onchain Wallet wiederhergestellt werden.


Dieser Prozess braucht Zeit! Bitte haben Sie also Geduld und versuchen Sie, Ihr Blixt aktiv und online zu halten. Die erste Synchronisierung kann bis zu 6-8 Minuten dauern und das Schließen der Kanäle kann bis zu 10-15 Minuten dauern. Es ist also besser, wenn du das Gerät gut aufgeladen hast.


Sobald dieser Prozess gestartet wurde, können Sie im Magic Drawer - Lightning Channels den Status jedes Ihrer vorherigen Kanäle überprüfen, der den Status "zum Schließen anstehend" hat. Sobald jeder Kanal geschlossen ist, können Sie im Onchain Wallet (siehe Magic Drawer - Onchain) die schließenden TX sehen und das TX-Menüprotokoll öffnen.


![blixt](assets/en/15.webp)


Außerdem sollten Sie überprüfen, ob Ihre früheren Peers, die Sie in Ihrem alten LN-Knoten hatten, noch nicht vorhanden sind, und diese hinzufügen. Gehen Sie also in das Menü "Einstellungen", gehen Sie zu "Lightning Network" und geben Sie die Option "Lightning Peers anzeigen" ein.


![blixt](assets/en/16.webp)


In diesem Abschnitt sehen Sie die Peers, mit denen Sie zu diesem Zeitpunkt verbunden sind, und Sie können weitere hinzufügen, am besten solche, mit denen Sie zuvor Kanäle hatten. Gehen Sie einfach auf die [Amboss-Seite] (https://amboss.space/), suchen Sie nach den Aliasen oder der NodeID Ihrer Peer-Knoten und scannen Sie deren Node-URI.


![blixt](assets/en/17.webp)


Wie Sie auf dem Bild oben sehen können, gibt es 3 Aspekte:


A - steht für den Clearnetzknoten Address URI (Domäne/IP)


B - steht für den Tor-Zwiebelknoten Address URI (.onion)


C - ist der QR-Code zum Scannen mit Ihrer Blixt-Kamera oder die Kopierschaltfläche.


Diesen Knoten Address URI müssen Sie in Ihre Peers-Liste aufnehmen. Beachten Sie also, dass es nicht ausreicht, nur den Knotenaliasnamen oder die Knoten-ID anzugeben.


Jetzt können Sie auf Magic Drawer (Menü oben links) - Lightning Channels gehen und sehen, bei welcher Höhe des Fälligkeitsblocks die Gelder in Ihre Onchain Address zurückgegeben werden.


![blixt](assets/en/18.webp)


Die Blocknummer 764272 ist der Zeitpunkt, an dem die Gelder in Ihrem Bitcoin auf der Kette Address verwendet werden können. Und es könnte bis zu 144 Blöcke ab dem 1. Bestätigungsblock dauern, bis sie freigegeben werden. [Überprüfen Sie das also im Mempool] (https://Mempool.space/).


Und das war's. Warten Sie einfach geduldig, bis alle Kanäle geschlossen sind und das Geld zurück in Ihr Wallet fließt.


👉 **Geheime Wiederherstellungsmethode :**


Es gibt eine weitere Methode, um Ihren Blixt LND Knoten wiederherzustellen, ohne die Kanäle zu schließen. Aber es ist vor den üblichen Noob-Benutzern versteckt, weil diese Methode NUR für diejenigen ist, die wissen, was sie tun.


Wenn Sie Ihren bestehenden (funktionierenden) Blixt-Knoten auf ein anderes neues Gerät migrieren möchten, ohne die bestehenden LN-Kanäle zu schließen, müssen Sie die folgenden Schritte ausführen:



- Wir gehen davon aus, dass Sie bereits den Blixt Wallet seed (24 Wörter aezeed) gespeichert haben
- Gehen Sie auf dem alten Gerät zu "Einstellungen" - Abschnitt Debug - "LND-Datenbank kompaktieren". Dieser Schritt ist optional, wird aber empfohlen, wenn Sie eine kleinere Größe der channel.db-Datei wünschen. Normalerweise ist sie ziemlich groß, abhängig von der Aktivität Ihres Knotens. Dadurch wird Blixt neu gestartet und die Größe der db-Datei reduziert.
- Gehen Sie nach dem Neustart zu "Einstellungen" und ändern Sie Ihren normalen Alias-Namen in "Hampus". Dadurch werden die versteckten Optionen aktiviert, die nur für fortgeschrittene Benutzer gelten.
- Gehen Sie ganz nach unten zum Abschnitt "Debug" und Sie werden eine neue Option "Export channel.db file" sehen. WARNUNG! Sobald Sie diesen Export durchführen, wird der bestehende Blixt LN-Knoten auf diesem alten Gerät deaktiviert und die gesamte Knotendatenbank (channel.db) wird exportiert, damit sie in ein neues Gerät importiert werden kann.
- Diese db-Datei wird in einem bestimmten Ordner auf Ihrem alten Gerät gespeichert (Dokumente oder Downloads) und von dort aus müssen Sie sie unverändert auf Ihr neues Gerät übertragen. Sie können zum Beispiel [LocalSend FOSS app] (https://github.com/localsend/localsend) verwenden, um die Datei direkt zwischen den Geräten zu übertragen.
- In diesem Moment MUSS Ihr altes Blixt ausgeschaltet bleiben. ÖFFNE ES NICHT WIEDER!
- Sobald Sie die Datei channel.db auf das neue Gerät übertragen haben, starten Sie die Neuinstallation von Blixt und wählen Sie auf dem ersten Bildschirm "Wallet wiederherstellen".
- Auf die Schaltfläche, wo es heißt "Select SCB file" lange drücken (NICHT einfach klicken!) und dann sehen Sie die Möglichkeit, eine channel.db Datei zu wählen, wo Sie es lokal in das neue Gerät zu speichern. Wenn Sie nur einfach auf diese Schaltfläche drücken, wird standardmäßig eine SCB-Datei (mit geschlossenen Kanälen) verwendet, es funktioniert nicht für vollständige Backup-Live-Kanäle.
- Geben Sie die 24 Wörter seed ein und klicken Sie dann auf "Wiederherstellen"
- Sie werden sehen, dass Blixt die Synchronisierung mit Neutrino beginnt. Du kannst auch die Synchronisationsprotokolle sehen.
- BEHALTEN SIE DAS IM HINTERKOPF! Versuchen Sie, Blixt in dieser Phase ständig geöffnet zu halten! Lass es nicht in den Ruhezustand gehen oder den Bildschirm der App schließen. Das könnte die anfängliche Synchronisierung stören und du musst sie erneut durchführen. Warten Sie geduldig, es dauert nicht länger als ein paar Minuten.
- Sobald die anfängliche Blocksynchronisierung abgeschlossen ist, werden Ihre früheren Wallet-Adressen schnell gescannt, und Ihre Kanäle sind wieder online, lebendig und gesund.
- Leider ist es (noch) nicht möglich, den bisherigen Zahlungsverlauf und die Kontakte wiederherzustellen. Aber das ist ja auch nicht so wichtig.


Und FERTIG! Jetzt haben Sie einen vollständig wiederhergestellten Blixt LN Knoten. Es könnte auch mit anderen LND-Backups (Umbrel, Raspiblitz usw.) funktionieren, wenn Sie vorher die channel.db-Datei korrekt gespeichert haben. Blixt kann also buchstäblich jeden toten LND-Knoten retten.


---

## Blixt - Vierter Kontakt


In diesem Kapitel geht es um die Anpassung und das bessere Kennenlernen von Blixt Node. Ich werde nicht alle verfügbaren Funktionen beschreiben, es sind zu viele und wurden bereits in der [Blixt Features Page] (https://blixtwallet.github.io/features) erklärt.


Aber ich werde auf einige dieser Punkte hinweisen, die notwendig sind, um mit Blixt voranzukommen und eine gute Erfahrung zu machen.


### A - Name (NameDesc)


![blixt](assets/en/19.webp)


[NamDesc] (https://github.com/lightning/blips/blob/master/blip-0011.md) ist ein Standard für die Übermittlung des "Empfängernamens" in BOLT11-Rechnungen.


Dies kann ein beliebiger Name sein, der jederzeit geändert werden kann.


Diese Option ist in verschiedenen Fällen sehr nützlich, wenn Sie einen Namen zusammen mit der Invoice-Beschreibung senden möchten, so dass der Empfänger einen Hinweis darauf erhalten kann, wer diese Sats erhalten hat. Dies ist völlig optional und auch im Zahlungsbildschirm muss der Benutzer das Kästchen ankreuzen, das angibt, dass der Aliasname gesendet werden soll.


Hier ist ein Beispiel für die Verwendung von [chat.blixtwallet.com](https://chat.blixtwallet.com/)


![blixt](assets/en/20.webp)


Dies ist ein weiteres Beispiel für das Senden an eine andere Wallet-Anwendung, die NameDesc unterstützt:


![blixt](assets/en/21.webp)


### B - Blitzableiter


Mit der neuen Version 0.6.9-420 [kürzlich angekündigt] (https://github.com/hsjoberg/blixt-Wallet/releases/tag/v0.6.9-420) hat Blixt eine neue leistungsstarke Funktion für Lightning Address in Blixt eingeführt.


Diese neue Funktion ist eine optionale Option, die nicht standardmäßig aktiviert ist!


Im Moment wird die Standard-LN-Box von Blixt-Server betrieben und bietet ein @blixtwallet.com LN Address. Aber JEDER mit einem LND öffentlichen Knoten kann die Lightning Box Server laufen und bieten LN Address für seine eigene Domain, self-custody.


Im Moment leitet der Blixt-Server die an LN-Adressen @blixtwallet.com gesendeten Zahlungen nur an die Blixt-Benutzer weiter, die ihren LN auf Address gesetzt haben. Benutzer müssen ihren Blixt-Knoten Wallet in den "dauerhaften Modus" versetzen, um diese Zahlungen an ihre LN-Adressen @blixtwallet.com zu erhalten.


In den Versionshinweisen finden Sie eine Video-Demo, wie Sie Ihren LN Address in Blixt einrichten.


Dieses LN Address in Blixt Wallet App implementiert, ist wie ein Chat über LN, sofort und Spaß, auch die Unterstützung [LUD-18] (https://github.com/lnurl/luds/blob/luds/18.md) (Hinzufügen eines Alias-Namen zu einer Zahlung). Sie können in der Kontaktliste all Ihre regulären LN-Adressen hinzufügen, die Sie häufig verwenden, und haben sie zum Chatten zur Hand. Jetzt kann Blixt als vollwertige LN Chat-App betrachtet werden 😂😂.


Eine weitere nützliche Funktion ist die volle Unterstützung von LUD-18 (die auch [Stacker.News](https://stacker.news/r/DarthCoin) und andere unterstützen).


![blixt](assets/en/22.webp)


Wie Sie auf dem Screenshot oben sehen können, wird beim Senden von einem Stacker News-Konto das Logo + LN Address + Nachricht angezeigt. Das Gleiche gilt für das Senden von Blixt. Sie können Ihren Blixt LN Address anhängen oder einfach den Alias-Namen hinzufügen (zuvor in den Blixt-Einstellungen festgelegt) oder sogar beides.


Diese Option von LUD-18 könnte auch für Abonnementdienste nützlich sein, bei denen der Benutzer einen bestimmten Aliasnamen (NICHT seinen Knotenalias oder seinen echten Namen!) senden kann, auf dessen Grundlage er registriert werden kann oder eine bestimmte Nachricht zurückerhält oder was auch immer. Das Anhängen eines Alias-Namens ([LUD-18](https://github.com/lnurl/luds/blob/luds/18.md))+ eines Kommentars ([LUD-12](https://github.com/lnurl/luds/blob/luds/12.md)) an eine LN-Zahlung kann mehrere Anwendungsfälle haben!


Hier ist der Code für [Lightning Box] (https://github.com/hsjoberg/lightning-box), wenn Sie es für sich selbst, für Ihre Familie und Freunde, auf Ihrem eigenen Knotenpunkt ausführen.


Hier können Sie auch den [LSP Dunder Server](https://github.com/hsjoberg/dunder-lsp) für Blixt-Mobilknoten betreiben und Liquidität für Blixt-Nutzer anbieten, wenn Sie einen guten öffentlichen LN-Knoten haben (funktioniert nur mit LND).


### C - Sicherung von LN-Kanälen und seed-Wörtern


Dies ist ein sehr wichtiges Merkmal!


Nach dem Öffnen oder Schließen eines LN-Kanals sollten Sie ein Backup erstellen. Dies kann manuell erfolgen, indem Sie eine kleine Datei auf dem lokalen Gerät (normalerweise im Download-Ordner) oder über ein Google Drive- oder iCloud-Konto speichern.


![blixt](assets/en/23.webp)


Gehen Sie zum Abschnitt Blixt-Einstellungen - Wallet. Dort haben Sie die Möglichkeit, alle wichtigen Daten für Ihr Blixt Wallet zu speichern:



- "Mnemonic anzeigen" - zeigt die 24 Wörter seed an, um sie aufzuschreiben
- "Mnemonic vom Gerät entfernen" - diese Option ist optional und sollte nur verwendet werden, wenn Sie die seed-Wörter wirklich von Ihrem Gerät entfernen möchten. Dadurch wird Ihr Wallet NICHT gelöscht, sondern nur das seed. Aber Achtung! Es gibt keine Möglichkeit, sie wiederherzustellen, wenn Sie sie nicht vorher aufgeschrieben haben.
- "Kanalsicherung exportieren" - diese Option speichert eine kleine Datei auf Ihrem lokalen Gerät, normalerweise im Ordner "Downloads", von wo aus Sie sie zur sicheren Aufbewahrung außerhalb Ihres Geräts verschieben können.
- "Kanal-Backup überprüfen" - eine gute Option, wenn Sie Google Drive oder iCloud verwenden, um die Integrität des Backups aus der Ferne zu überprüfen.
- " Google drive channel backup" - speichert die Sicherungsdatei in Ihrem persönlichen Google-Laufwerk. Die Datei ist verschlüsselt und wird in einem anderen Speicherort als Ihre üblichen Google-Dateien gespeichert. Es gibt also keine Bedenken, dass sie von jemandem gelesen werden kann. Außerdem ist diese Datei ohne die seed-Wörter völlig nutzlos, so dass niemand Ihr Geld nur aus dieser Datei nehmen kann.


Ich würde für diesen Abschnitt Folgendes empfehlen:



- verwenden Sie einen Passwort-Manager, um Ihre seed und die Backup-Datei sicher zu speichern. KeePass oder Bitwarden sind sehr gut dafür geeignet und können auf mehreren Plattformen und selbst gehostet oder offline verwendet werden.
- Machen Sie JEDESMAL, wenn Sie einen Kanal öffnen oder schließen, eine Sicherungskopie. Diese Datei wird mit den Informationen über die Kanäle aktualisiert. Es ist nicht nötig, dies nach jeder Transaktion, die Sie im LN durchgeführt haben, zu tun. Die Kanalsicherung speichert diese Informationen nicht, sondern nur den Status des Kanals.


![blixt](assets/en/24.webp)


---

## Blixt - Tipps und Tricks


### FALL 1 - SYNCHRONISIERUNGSPROBLEME


"Mein Blixt wird nicht synchronisiert... Mein Blixt zeigt den Kontostand nicht an... Mein Blixt kann keine Kanäle öffnen... Ich habe versucht, es auf einem anderen Gerät wiederherzustellen... etc_"


All diese Probleme beginnen damit, dass IHR GERÄT NICHT RICHTIG SYNCHRONISIERT. Bitte verstehen Sie diesen wichtigen Aspekt: Blixt ist ein mobiler LND-Knoten, der Neutrino zum Synchronisieren/Lesen der Blöcke verwendet.



- Hier ist eine weniger technische Erklärung aus dem [Bitcoin Magazin] (https://bitcoinmagazine.com/technical/why-Bitcoin-wallets-need-block-filters)
- Hier finden Sie weitere technische Ressourcen von [Bitcoin Optech] (https://bitcoinops.org/en/topics/compact-block-filters/)
- Hier sehen Sie, wie Sie Neutrino auf Ihrem eigenen Heimknoten aktivieren und Blockfilter für Ihren mobilen Knoten bereitstellen können, aus [Docs Lightning Engineering] (https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core)


ERINNERUNG: Die Verwendung von Neutrino über das Clearnetz ist absolut sicher, Ihre IP oder xpub werden nicht weitergegeben. Sie lesen lediglich Blöcke von einem entfernten Knoten mit Neutrino. Das ist alles. Der ganze Rest wird auf Ihrem lokalen Gerät erledigt.


Es gibt also KEINE Notwendigkeit, es mit Tor zu benutzen. Tor führt zu einer enormen Latenz bei der Synchronisierung und macht dein Blixt sehr instabil. Wenn du Blixt wirklich über Tor benutzen willst, solltest du dir sicher sein, was du tust und eine gute Verbindung und Geduld haben. Dasselbe gilt für die Verwendung eines VPN. Sei vorsichtig, was für eine Latenz dir von diesem VPN gegeben wird.


Sie können die Latenzzeit eines Neutrino-Servers testen, indem Sie ihn einfach anpingen, von einem PC oder von Ihrem Handy aus.


![blixt](assets/en/25.webp)


Dies ist ein gewöhnlicher Ping zum Neutrino-Server europe.blixtwallet.com, der zeigt, dass die Verbindung mit einer Antwortzeit von durchschnittlich 50 ms und einer TTL von 51 sehr gut ist. Die Antwortzeit kann variieren, aber nicht zu sehr. Die TTL muss stabil sein.


Wenn diese Werte höher als 100-150ms sind, dann wird Ihr Synchronisierungsprozess stocken oder noch schlimmer, es könnte zu geschlossenen Kanälen bei den Peers führen! Ignorieren Sie diesen Aspekt nicht.


Ohne eine ordnungsgemäße Synchronisierung können Sie auch nicht die richtige Balance sehen oder Ihre LN-Kanäle werden nicht online und betriebsbereit. Es spielt keine Rolle, wie viele Giga-Ultra-Terraps Sie die Download-Geschwindigkeit haben, es spielt keine Rolle. Es kommt auf das Zeitverhalten und die TTL (time to live) an.


Dies ist wie ein allgemeiner Fall für LATAM Benutzer. Ich weiß nicht, was dort passiert, aber ihr habt eine schreckliche Verbindung mit Pings von über 200ms, die jede Synchronisation stören können.


Was ist also die Lösung für diese verzweifelten Nutzer?



- blixt nicht mehr mit Tor benutzen. Ist völlig nutzlos
- sie können ein VPN verwenden, aber wählen Sie es mit Bedacht aus und überwachen Sie die ganze Zeit den Ping. Verwenden Sie eines, das näher an Ihrem geografischen Standort liegt. Entfernung bedeutet mehr ms Antwortzeit, denken Sie daran.
- wählen Sie Ihre Neutrino-Peers mit Bedacht aus. Hier finden Sie eine Liste bekannter öffentlicher Neutrino-Server:


```txt
For US region
btcd1.lnolymp.us | btcd2.lnolymp.us
btcd-mainnet.lightning.computer
swest.blixtwallet.com (Seattle)
node.eldamar.icu
noad.sathoarder.com
bb1.breez.technology | bb2.breez.technology
neutrino.shock.network
For EU region
europe.blixtwallet.com (Germany)
For Asia region
sg.lnolymp.us
asia.blixtwallet.com
```


Eine andere Möglichkeit ist, einen Knoten aus dieser Liste auszuwählen, der die "Kompaktfilter" (BIP157 / Neutrino) ankündigt - [Bitnodes Page Neutrino filter](https://bitnodes.io/nodes/?q=NODE_COMPACT_FILTERS). Wählen Sie einen, der näher an Ihrem geografischen Standort liegt.


Eine andere Möglichkeit (die beste) besteht darin, sich mit einem lokalen Gemeinschaftsknoten zu verbinden, der von einem Freund oder einer Gruppe betrieben wird, die Sie kennen, und der eine Neutrino-Verbindung anbietet. (https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) Ihr Knoten wird in keiner Weise beeinträchtigt, sie brauchen nur eine stabile und öffentliche Verbindung.


Es besteht ein Bedarf an mehr Neutrino-Servern in der LATAM-Region, um eine bessere und schnelle Synchronisierung zu ermöglichen. Also organisieren Sie sich bitte mit Ihrer lokalen Bitcoin-Community und entscheiden Sie, wer und wo einen Bitcoin Core + Neutrino für Ihren eigenen Gebrauch betreibt. Eine öffentliche IP reicht aus. Wenn Sie keinen Zugang zu einer öffentlichen IP haben, können Sie eine VPS-IP verwenden und einen Wireguard-Tunnel zu Ihrem Home-Node einrichten. Auf diese Weise leiten Sie den gesamten Datenverkehr zu Ihrer lokalen VPS-IP um, ohne private Informationen über Ihren Heimatknoten preiszugeben.


### FALL 2 - SYNCHRONISIERUNG NIE BEENDEN


"_Mein Blixt hat eine gute Verbindung mit dem Neutrino-Server, aber die Synchronisierung bleibt stecken."


#### Zeit-Server


Manchmal benutzen Leute verschiedene alte Geräte oder sind nicht richtig mit einem Zeitserver verbunden. Neutrino synchronisiert so lange, bis es die aktuellen Blöcke erreicht, die nicht der realen Ortszeit entsprechen. In den Blixt LND Protokollen werden Sie einen Fehler sehen, der besagt, dass "der Zeitstempel des Blocks weit von der Zukunft entfernt ist" oder etwas, das mit "der Header hat die Plausibilitätsprüfung nicht bestanden" zu tun hat.


Schnelle Lösung: Stellen Sie die richtige Uhrzeit und das richtige Datum für Ihr Gerät ein und starten Sie Blixt neu.


#### Wenig Platz auf dem Gerät


Manchmal kann bei der Verwendung eines alten Geräts mit wenig Speicherplatz ein Schwellenwert erreicht werden, an dem es hängen bleibt. Je mehr Sie diesen mobilen LND-Knoten verwenden, desto größer werden die Neutrinodateien und auch die channel.db-Datei.


Schnelle Lösung: Gehen Sie zu Blixt Optionen - Abschnitt Debug - Wählen Sie "LND stoppen und Neutrino-Dateien löschen". Dadurch wird die App neu gestartet und eine neue, frische Synchronisierung durchgeführt. Manchmal kann diese schnelle Lösung auch beschädigte Daten reparieren. Denken Sie daran, dass die vollständige Neusynchronisierung zwischen 1 und 3 Minuten dauern wird. Vorhandene Fonds oder Kanäle werden NICHT gelöscht, aber ja, nach der Neusynchronisierung könnte ein erneuter Scan der Bitcoin-Adressen ausgelöst werden, was mehr Zeit in Anspruch nehmen könnte.


Der nächste Schritt besteht darin, zu prüfen, wie viele Daten noch belegt sind. Sie können dies in Android App Info - Daten sehen. Wenn die Datenmenge immer noch größer als 400-500MB ist, können Sie die LND Dateien komprimieren. Gehen Sie dazu in die Blixt-Optionen - Abschnitt Debug - Wählen Sie "Compact DB LND". Starten Sie die Blixt-App neu, falls dies nicht automatisch geschieht. Die Komprimierung findet beim Start statt und wird nur einmal durchgeführt. Jetzt werden Sie sehen, dass die Blixt-Daten mehr oder weniger belegt sind.


#### Dauermodus


Manchmal öffnen die Leute Blixt lange Zeit nicht, so dass die Synchronisierung viel zu alt ist. Aber sie erwarten, dass sie sofort synchronisiert werden, wenn sie es öffnen.


Bitte haben Sie Geduld und sehen Sie sich das sich drehende Rad an. Optional können Sie auf Optionen - Knoteninfo anzeigen gehen und sehen, ob "wahr" als "mit Kette synchronisiert" und "mit Diagramm synchronisiert" markiert ist. Ohne diese "true"-Angabe können Sie Blixt nicht richtig nutzen, Sie können den Kontostand nicht richtig sehen, Sie können die LN-Kanäle nicht online sehen, Sie können keine Zahlungen vornehmen.


Schnelle Lösung: Es gibt eine leistungsstarke Option, um Ihren Blixt-Knoten "am Leben zu erhalten". Gehen Sie zu Optionen - Experimente - Wählen Sie "Persistenten Modus aktivieren". Dadurch wird Ihr Blixt neu gestartet und der LND-Dienst in den persistenten Modus versetzt, d. h. er bleibt immer aktiv und hält Ihre Synchronisierung online, auch wenn Sie zu einer anderen Anwendung wechseln oder Blixt einfach schließen (nicht zwangsweise schließen oder die Aufgabe beenden). Das kann den ganzen Tag so bleiben, wenn Sie eine stabile Verbindung haben und Blixt mehrmals verwenden müssen. Es wird nicht zu viel Akku verbrauchen.


### FALL 3 - ICH MÖCHTE AUF EIN ANDERES GERÄT MIGRIEREN


OK, zu diesem Szenario habe ich eine ausführliche Anleitung auf der [FAQ-Seite] (https://blixtwallet.github.io/faq#blixt-restore) geschrieben: mit 2 Optionen, schnell (kooperatives Schließen der Kanäle vor der Migration) und langsam (erzwungenes Schließen der Kanäle, weil das alte Gerät tot ist).


Ich möchte hier jedoch einige wichtige Aspekte wiederholen und ein neues "geheimes" Verfahren hinzufügen.


ERINNERUNG:



- Erstellen Sie immer eine Sicherungskopie des Status Ihrer Kanäle (SCB), NACHDEM Sie einen Kanal geöffnet oder geschlossen haben. Dies dauert nur wenige Sekunden.
- Bewahren Sie die alten SCB-Dateien nicht auf, um sie nicht zu verwechseln und wiederherzustellen. Sie sind völlig nutzlos und könnten ein Strafverfahren auslösen, wenn Sie sie wiederherstellen. Verwenden Sie immer die letzte Version der SCB-Datei, wenn Sie zur Wiederherstellung fortfahren.
- Speichern Sie die SCB-Datei (es handelt sich um einen verschlüsselten Text mit der Erweiterung .bin) außerhalb Ihres Geräts an einem sicheren Ort. Sie können [LocalSend](https://github.com/localsend/localsend) verwenden, um diese Datei auf einen PC oder ein anderes Gerät zu übertragen.
- Speichern Sie auch den seed Ihres Blixt Wallet an einem sicheren Ort, z. B. in einem Offline-Passwortmanager/verschlüsselten USB.


Geheime Methode: Wie man den Blixt-Knoten migriert, ohne die bestehenden Kanäle zu schließen. Dazu müssen Sie den vorherigen Abschnitt "Dritter Kontakt" in diesem Leitfaden über "Wallet wiederherstellen" sorgfältig lesen.


Dieses Verfahren ist nicht für Anfänger, sondern nur für fortgeschrittene Benutzer! Deshalb ist es nicht allgemein zugänglich und ich empfehle, es nur mit Hilfe der Blixt-Entwickler oder meines Supports durchzuführen. Bitte ignorieren Sie diesen Rat nicht.


### FALL 4 - WELCHE PEERS SOLLEN DIE KANÄLE ÖFFNEN?


Wie ich in [Blixt guides page] (https://blixtwallet.github.io/guides) geschrieben habe, gibt es viele Möglichkeiten, Kanäle mit diesem mobilen LND Knoten zu öffnen. Aber einige wichtige Aspekte möchte ich Ihnen hier in Erinnerung rufen:



- offen mit bekannten LSP-Knoten und mit von der Gemeinschaft verbürgten Gleichrangigen. [Siehe hier eine Liste](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- öffnen Sie nicht mit zufälligen Tor-Nodes. Diese sind wertlos und du wirst nur Probleme bekommen, weil du keine Zahlungen tätigen kannst. Egal wie gut dein Freund "the node runner" mit einem schäbigen Tor-Knoten im Dschungel ist, er wird dir niemals die besten Routen für einen mobilen privaten Knoten geben. Du öffnest keine Kanäle mit jemandem, weil er dein Freund ist. Wir sind hier nicht bei Facebook! Du öffnest einen Kanal für: gute Routen, geringe Gebühren, Verfügbarkeit.
- es gibt keine Notwendigkeit, eine Scheiße Tonne von kleinen Kanälen zu öffnen, 2-3 oder max 4, aber mit einer guten Menge von Sats. Öffnen Sie nicht kleine Kanäle, sind völlig nutzlos. Kleiner als 200k für eine mobile haben nicht viel nutzen.
- denken Sie an die LSPs, die Inbound-Kanäle und JIT-Kanäle (just in time) anbieten. Diese sind sehr nützlich, weil Sie keine Ihrer UTXOs verwenden müssen. Sie können den Eröffnungskanal mit Geldern bezahlen, die Sie bereits in anderen LN-Geldbörsen haben, und diese stapeln und für die Eröffnung eines größeren Kanals vorbereiten. Sie sollten diese JIT-Kanäle zu Ihren Gunsten nutzen. [Ich habe in diesem Leitfaden](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) mehr Optionen für Peers für private Nodes wie Blixt erklärt. Außerdem habe ich [hier in diesem Leitfaden auf SN](https://stacker.news/items/679242/r/DarthCoin) erklärt, wie man die Liquidität der privaten mobilen Nodes verwaltet.


---

## Schlussfolgerung


OK, es gibt noch viele andere erstaunliche Funktionen, die Blixt bietet. Ich werde sie dir nach und nach zeigen und dir viel Spaß dabei wünschen.


Diese App wird wirklich unterschätzt, vor allem, weil sie nicht von VCs finanziert wird, sondern von der Community betrieben wird und mit Liebe und Leidenschaft für Bitcoin und Lightning Network entwickelt wurde.


Dieser mobile LN-Knoten, Blixt, ist ein sehr leistungsfähiges Werkzeug in den Händen vieler Nutzer, wenn sie wissen, wie man es richtig einsetzt. Stellen Sie sich vor, Sie laufen mit einem LN-Knoten in Ihrer Tasche durch die Welt und niemand wird es bemerken.


Ganz zu schweigen von den vielen anderen Funktionen, die nur wenige oder gar keine anderen Wallet-Anwendungen bieten können.


In der Zwischenzeit finden Sie hier alle Links zu diesem erstaunlichen Bitcoin Lightning Node:



- [Offizielle Blixt-Webseite](https://blixtwallet.com/)
- [Blixt Github-Seite](https://github.com/hsjoberg/blixt-Wallet/)
- [Blixt Features page](https://blixtwallet.github.io/features) - erklärt jedes einzelne Feature und jede einzelne Funktion.
- [Blixt-FAQ-Seite](https://blixtwallet.github.io/faq) - Liste der Fragen und Antworten und der Fehlerbehebung bei Blixt
- [Blixt Guides page](https://blixtwallet.github.io/guides) - Demos, Video-Tutorials, zusätzliche Anleitungen und Anwendungsfälle für Blixt
- Download: [Android Play Store](https://play.google.com/store/apps/details?id=com.blixtwallet) | [iOS](https://testflight.apple.com/join/EXvGhRzS) | [APK direkt herunterladen](https://github.com/hsjoberg/blixt-Wallet/releases)
- [Telegrammgruppe für direkte Unterstützung] (https://t.me/blixtwallet)
- [Twitter] (https://twitter.com/BlixtWallet)
- [Geyser Crowdfunding-Seite](https://geyser.fund/project/blixt) - spenden Sie Sats, um das Projekt zu unterstützen
- [LNURL Chat Blixt](https://chat.blixtwallet.com/) - anonymer LN Chat
- [Blixt presentation - promo video](https://lightning.video/06fdf68f99e246a6ec6ba1470677b9e632faaad4aa0ca9773c38714b682a4ac1)
- [Blixt Girls Calendar](https://lightning.video/eeb744202ad3f14c18bf6d719970ebd9c53f0f13b79c94d299c6be623fba64b6) - Promo-Video (Sie können Ihre 1. Verwendung von LN testen)
- [Druckbarer A4-Flyer mit ersten Schritten mit Blixt, in verschiedenen Sprachen] (https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer).
- [Blixt bietet auch eine voll funktionsfähige Demoversion (https://blixt-Wallet-git-master-hsjoberg.vercel.app/) direkt auf der Website oder auf einer speziellen Webversion an, mit der Sie alle Funktionen testen können, bevor Sie sie in der realen Welt einsetzen.


---
**DISCLAIMER:**


*Ich werde von den Entwicklern dieser App weder bezahlt noch in irgendeiner Weise unterstützt. Ich habe diesen Leitfaden geschrieben, weil ich gesehen habe, dass das Interesse an dieser Wallet-App zunimmt und neue Benutzer immer noch nicht verstehen, wie sie damit anfangen sollen. Außerdem möchte ich Hampus (dem Hauptentwickler) mit der Dokumentation über die Verwendung dieses Knotens Wallet.* helfen


*Ich habe kein anderes Interesse daran, diese LN-App zu fördern, als die Einführung von Bitcoin und LN voranzutreiben. Das ist der einzige Weg!*


---