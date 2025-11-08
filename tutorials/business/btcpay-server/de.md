---
name: BTCPay-Server
description: Annahme von BTC-Zahlungen ohne Zwischenhändler
---

![cover](assets/cover.webp)



![video](https://youtu.be/KqsM-n-e4aY)



BTCPay Server ist ein kostenloses, von Nicolas Dorier entwickeltes Open-Source-Softwarepaket, das die Annahme von Bitcoin-Zahlungen ohne Zwischenhändler ermöglicht. Es wurde entwickelt, um Autonomie und finanzielle Souveränität zu bieten. Es wird auf einem eigenen Server installiert und bietet ein vollständiges Transaktionsmanagement, von der Rechnungsstellung über die Validierung von on-chain- oder Lightning Network-Zahlungen bis hin zur Buchhaltung. Es lässt sich leicht in E-Commerce-Websites (WooComerce, Shopify usw.) integrieren oder kann als Zahlungsterminal für physische Geschäfte (*POS*) verwendet werden.



BTCPay Server ist ohne Zweifel die fortschrittlichste Lösung für Händler, die Bitcoin akzeptieren möchten. Es ist die umfassendste und robusteste Software in Bezug auf Sicherheit, Souveränität und Vertraulichkeit. Auf der anderen Seite ist sie aber auch am kompliziertesten zu installieren und zu warten. Es gibt auch einfachere Alternativen: einige sind vollständig verwahrend, wie OpenNode, während andere einen interessanten Kompromiss zwischen Benutzerfreundlichkeit und Souveränität bieten, wie Swiss Bitcoin Pay :



https://planb.academy/tutorials/business/point-of-sale/swiss-bitcoin-pay-2-a78b057e-ed11-47ac-860c-71019fcb451a

Das Ziel dieses Tutorials ist es, Sie Schritt für Schritt durch die Installation, Konfiguration und Verwendung von BTCPay Server zu führen, damit Sie eine sichere, unabhängige Zahlungsinfrastruktur im Einklang mit dem Bitcoin Ethos einrichten können.



## BTCPay Server Merkmale



Zentralisierte Bitcoin-Verkaufsstellenlösungen, wie z. B. *OpenNode*, sind zwar benutzerfreundlich, aber auf ein Drittunternehmen angewiesen, da sie nicht selbst gehostet werden können und in den meisten Fällen proprietär sind. Sie vereinfachen zwar die Einrichtung von Zahlungen, sind aber mit Gebühren verbunden und setzen ihre Nutzer mehr Risiken aus als eine Lösung wie BTCPay Server, sowohl in Bezug auf die Verwahrung der Gelder als auch auf die Vertraulichkeit.



BTCPay Server richtet sich an Online- oder physische Händler, Vereine und gemeinnützige Organisationen, die Spenden in Bitcoins erhalten möchten. Es ist auch eine ideale Lösung für Projektbesitzer und Entwickler, die eine direkte Unterstützung durch ihre Community wünschen.



Zu den besonderen Merkmalen von BTCPay Server gehören:




- seine **vollständige Autonomie**,
- das Fehlen eines **KYC**-Verfahrens,
- volle Kontrolle über die Mittel**,
- die **Abschaffung der Plattformgebühren**.



Indem Sie Ihr eigener Zahlungsabwickler werden, beseitigen Sie jede Abhängigkeit von einer zentralen dritten Partei zwischen Ihnen und Ihren Kunden. Sie können Zahlungen direkt in Bitcoins und generate-Zahlungsrechnungen akzeptieren. Dadurch wird sichergestellt, dass weder Sie noch Ihr Unternehmen von jemand anderem verboten werden können. Sie spielen sowohl die Rolle der Bank als auch die des Zahlungsabwicklers, ohne dass Sie für jede Transaktion Provisionen an einen Vermittler zahlen müssen.



Die Transaktionsgebühren für **on-chain** bleiben bestehen, können aber durch die Nutzung des **Liquid**- oder **Lightning**-Netzwerks reduziert werden.



Darüber hinaus :




- Vollständig anpassbare Schnittstelle und Rechnungen;
- Native **Tor**-Unterstützung für erhöhte Vertraulichkeit;
- Unterstützung für **Crowdfunding**, **POS** und **Zahlungsschaltflächen**;
- Kompatibel mit vielen Währungen;
- Bitcoin Direkt- und Peer-to-Peer-Zahlungen ;
- Vollständige Kontrolle über Ihre privaten Schlüssel;
- Verbesserter Datenschutz ;
- Erhöhte Sicherheit ;
- Selbstgehostete Software ;
- Unterstützung für **SegWit** und **Lightning network** ;
- Internes, knotenbasiertes Portfolio, mit Integration von Hardware-Portfolios.



## Installieren und Konfigurieren von BTCPay Server



### Auswahl des Hosting-Modus



BTCPay Server kann auf verschiedene Arten installiert werden. Je nach Ihren Bedürfnissen und Ressourcen gibt es drei Hauptoptionen:




- BTCPay Server hosted by a third party**: Sie nutzen eine Plattform, die den Dienst für Sie hostet. Es ist einfach, aber normalerweise nicht kostenlos.
- BTCPay-Server selbst gehostet auf einem Cloud-Server** (z. B. über [btcpayprovider](https://btcpayprovider.com/), [Bitcoin People](http://bitcoinpeople.it/) oder einen anderen Anbieter). Dies ist die empfohlene Lösung für die meisten unerfahrenen Händler.
- BTCPay Server installiert auf Ihrer eigenen Hardware (lokal)** : auf einem Computer, Mini-PC oder Umbrel. Diese Methode ist technisch aufwendiger, bietet aber völlige Unabhängigkeit.



https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

Für ein Start-up-Unternehmen ist die **Bereitstellung auf einem Cloud-Server** der beste Kompromiss zwischen Autonomie, Einfachheit und Sicherheit, ohne die gesamte technische Infrastruktur verwalten zu müssen.



BTCPay Server kann schnell von einer Reihe von Hosting-Anbietern bereitgestellt werden. Unter ihnen hebt sich **Voltage** als Benchmark-Lösung für Benutzer hervor, die eine **zuverlässige**, **professionelle** und **ausländische** Infrastruktur benötigen.



### Erstellen Sie eine BTCPay Server-Instanz auf Voltage



**Voltage** ist eine schlüsselfertige Bitcoin- und Lightning-Hosting-Plattform, mit der Sie sofort Ihren eigenen BTCPay-Server einsetzen können, ohne komplexe Konfiguration oder Serverwartung.



Besuchen Sie die [offizielle Website von Voltage](https://voltage.cloud).



![capture](assets/fr/03.webp)



Erstellen Sie ein **Benutzerkonto** mit einer gültigen E-Mail-Adresse und einem sicheren Passwort.



![capture](assets/fr/04.webp)



Voltage bietet eine **kostenlose 7-Tage-Testversion**. Bitte beachten Sie, dass Sie nach der 7-tägigen kostenlosen Testphase eingeladen werden, ein festes Abonnement für **25$ pro Monat** abzuschließen, um Ihre Knoten weiterhin **aktiv zu halten**.



Nachdem Sie Ihr Voltage-Konto erstellt und sich zum ersten Mal angemeldet haben, werden Sie zur Startseite weitergeleitet, die aus zwei Hauptbereichen besteht:




- Ein **Infrastruktur**-Bereich zur Verwaltung von Lightning-Knoten, Bitcoin Core, BTCPay Server und anderen Bitcoin-Diensten in der Cloud;
- und einen Abschnitt **Zahlungen**, über den Sie auf API Lightning von Voltage zugreifen können, um Bitcoin-Zahlungen in kundenspezifische Anwendungen zu integrieren.



Um Ihre **BTCPay Server**-Instanz einzurichten, klicken Sie auf **Zugangsinfrastruktur**. Hier können Sie alle Ihre Dienste erstellen, verwalten und überwachen, einschließlich Ihres Bitcoin-Knotens und des BTCPay-Servers.



#### Eine Gruppe erstellen



Bevor Sie einen Dienst bereitstellen können, werden Sie von der Plattform aufgefordert, eine **Gruppe** zu erstellen. Eine **Gruppe** (Arbeitsbereich) ist ein Arbeitsbereich, in dem alle Ihre Bitcoin- und Lightning-Dienste zusammengefasst sind (z. B. ein Knoten, ein BTCPay-Server, ein Explorer usw.). Es ist so etwas wie ein Ordner, der Ihre verschiedenen Projekte enthält.



![capture](assets/fr/05.webp)



Für die Zwecke dieses Tutorials wird die von uns erstellte Gruppe **Genesis** genannt. Sie können ein Profilbild hinzufügen, wenn Sie möchten. Klicken Sie anschließend auf die Schaltfläche **Erstellen**. Sie können andere Benutzer einladen, der Gruppe beizutreten, und sogar den Gruppennamen ändern, wenn Sie möchten.



Auf der Startseite der Gruppe werden mehrere Optionen angezeigt:




- Lightning-Knoten**: zur Bereitstellung eines vollständigen Lightning-Knotens (LND) ;
- Bitcoin-Kernknoten** : um einen kompletten Bitcoin-Knoten zu starten;
- BTCPay Server** : zum Hosten einer einsatzbereiten BTCPay-Instanz;
- Nostr-Konten**: zur Verwaltung von Nostr-Identitäten.



Aktivieren Sie die **Doppelauthentifizierung (2FA)**, um Ihr Konto und Ihre Dienste zu sichern (die Schaltfläche ist in rot sichtbar, wenn sie deaktiviert ist).



![capture](assets/fr/06.webp)



Klicken Sie unter den Optionen auf **BTCPay-Server** und dann auf **BTCPay-Shop eröffnen**.



![capture](assets/fr/07.webp)



Voltage fordert Sie dann auf, Ihre BTCPay-Server-Instanz **zu erstellen und zu konfigurieren**, indem Sie einen **Servicenamen** (1) wählen und Lightning-Zahlungen aktivieren (2).



Sie benötigen einen Lightning-Knoten, wenn Sie Lightning-Zahlungen akzeptieren möchten.



Wenn Sie noch keinen Bitcoin- oder Lightning-Knoten haben, schlägt Voltage Ihnen vor, automatisch einen zu erstellen.



Klicken Sie auf **Einen Blitzknoten erstellen** (3) .



![capture](assets/fr/08.webp)



Auf der Oberfläche zur Knotenerstellung werden Sie aufgefordert, zwischen den Layouts **Standard** und **Professional** zu wählen.



Sie können einen echten Knoten (**Mainnet**) oder einen Testknoten (**Testnet**) erstellen. Klicken Sie dann auf die Schaltfläche **Fortfahren**.



![capture](assets/fr/09.webp)



Für dieses Lernprogramm verwenden wir den Standardplan. Geben Sie den **Knotennamen** und ein **Passwort** ein und drücken Sie die Schaltfläche **Erstellen**.



![capture](assets/fr/10.webp)



Nach wenigen Augenblicken ist Ihr Knoten betriebsbereit und Sie können einen freien Kanal mit einer Empfangskapazität von 500.000 sats öffnen.



![capture](assets/fr/11.webp)



Etwas weiter unten auf der rechten Seite finden Sie alle Informationen, die Sie über Ihren Knoten benötigen!



![capture](assets/fr/12.webp)



Nachdem wir nun unseren Lightning-Knoten zum Laufen gebracht haben, können wir uns wieder der Installation unseres BTCPay-Servers widmen. Sie können nun auf die Schaltfläche **BTCPay erstellen** klicken.



![capture](assets/fr/13.webp)



Es öffnet sich eine Seite mit Ihren Standard-Anmeldedaten und einer Meldung, die Sie auffordert, Ihr ursprüngliches Passwort zu ändern. Sobald Sie dies getan haben, klicken Sie auf die Schaltfläche **Jetzt anmelden**, um auf Ihre Schnittstelle zuzugreifen.



![capture](assets/fr/14.webp)



Das war's! Ihr BTCPay-Server ist jetzt einsatzbereit. Sie werden direkt zur Anmeldeseite Ihres BTCPay-Servers weitergeleitet.



![capture](assets/fr/15.webp)



Sobald Sie eingeloggt sind, konfigurieren Sie Ihren ersten **Speicher**:





- Geben Sie ihm einen **Namen**.





- Wählen Sie die **Standardwährung** (EUR, USD, CFA, usw.).





- Wählen Sie einen **Wechselkursanbieter** (z.B. CoinGecko).



![capture](assets/fr/16.webp)



Sie werden dann zum Dashboard Ihres Shops weitergeleitet. Auf der Dashboard-Oberfläche werden Sie feststellen, dass die Schaltfläche **Shop erstellen** grün markiert ist, da dieser Schritt bereits abgeschlossen ist.



![capture](assets/fr/17.webp)



Ein Stück weiter unten finden Sie die Schaltflächen **wallet konfigurieren** und **Lightning-Knoten konfigurieren**. In unserem Fall haben wir bereits eine Verbindung zu einem Lightning-Knoten hergestellt, der unter Spannung steht. Also müssen wir das hier nicht tun.



Gehen wir nun zur Konfiguration eines Portfolios über. Klicken Sie auf die Schaltfläche **Portfolio konfigurieren**.



Da wir gerade erst mit BTCPay Server anfangen, wollen wir ein bestehendes wallet verbinden. Drücken Sie also **Verbinden Sie ein bestehendes Portfolio**.



![capture](assets/fr/18.webp)



Anschließend müssen Sie Ihre **Importmethode** wählen. Wählen Sie unter den verfügbaren Optionen **Erweiterten öffentlichen Schlüssel eingeben**.



![capture](assets/fr/19.webp)



Durch die Verknüpfung eines bestehenden wallet können Sie Ihre Zahlungen **direkt auf diesem externen wallet** empfangen, ohne dass der BTCPay-Server Zugriff auf Ihren privaten Schlüssel hat. Selbst wenn der Server gehackt oder der öffentliche Schlüssel (`xpub`) kompromittiert würde, könnte ein Angreifer Ihre Transaktionshistorie einsehen, hätte aber **keinen Zugriff auf Ihr Geld**.



Sobald Sie auf die Schaltfläche **Erweiterten öffentlichen Schlüssel eingeben** klicken, werden Sie auf die Seite **geleitet**, auf der Sie diesen Schlüssel angeben müssen.



Lassen Sie uns nun den **erweiterten öffentlichen Schlüssel** abrufen.



### Anschließen eines Bitcoin wallet



Um Ihre Zahlungen zu empfangen, müssen Sie ein Bitcoin wallet an Ihr Geschäft anschließen. Hierfür haben Sie mehrere Möglichkeiten:





- Hardware-Portfolio** (Ledger, Trezor, Coldcard...) ;





- Software-Portfolio** (Blockstream App, Ashigaru, Electrum, Sparrow...)





- BTCPay Server** internes wallet (nicht empfohlen, da es weniger sicher ist und Ihre Gelder im Falle eines Server-Hackings stärker gefährdet sind).



In diesem Lernprogramm verwenden wir ein **Softwareportfolio**, das für die Erstkonfiguration leichter zugänglich ist. Sie können aus einer Reihe von kompatiblen Anwendungen wählen: **Electrum**, **Phoenix**, **Zeus**, **Muun**, usw.



Für die Demonstration verwenden wir **Electrum**. Öffnen Sie **Electrum**, klicken Sie auf **Portfolio**, dann auf **Informationen**:



![capture](assets/fr/20.webp)



Kopieren Sie dann den **öffentlichen Hauptschlüssel (xpub)**.



![capture](assets/fr/21.webp)



Sobald Sie den öffentlichen Hauptschlüssel kopiert haben, fügen Sie ihn in das dafür vorgesehene Feld auf der BTCPay-Server-Seite ein.



![capture](assets/fr/22.webp)



Nach der Überprüfung werden Sie zum Dashboard Ihres Shops weitergeleitet.



![capture](assets/fr/23.webp)



### Erzeugen eines Point of Sale (PoS)



Nachdem Sie Ihren Shop und Ihr Portfolio eingerichtet haben, können Sie nun einen **Point of Sale (PoS)** einrichten, um Bitcoin-Zahlungen direkt von Ihren Kunden zu erhalten.



Diese integrierte Funktion von **BTCPay Server** ist ideal für **Händler, Handwerker, Gastronomen oder Dienstleister**, die Bitcoin **ohne eigene Website** oder besondere technische Kenntnisse akzeptieren möchten.



### Was ist der Ort des Verkaufs?



Der **PoS** ist eine **vereinfachte POS-Schnittstelle**, die als **Bitcoin-Zahlungsterminal** fungiert.


Sie ermöglicht es Ihnen, :




- Erstellen Sie ein **Menü von Produkten oder Dienstleistungen** mit festen Preisen.
- Generieren Sie eine **Sofortrechnung mit QR-Code** zum Scannen.
- Geben Sie eine **Zahlungs-URL** frei, die über Smartphone, Tablet oder Computer zugänglich ist.



Mit anderen Worten: PoS verwandelt Ihren BTCPay-Server in eine **Direktverkaufsschnittstelle**, bei der jede Zahlung **in Ihrem eigenen Bitcoin wallet** empfangen wird, ohne Zwischenhändler.



### PoS konfigurieren



Klicken Sie im BTCPay-Dashboard auf **PLUGINS**, dann auf **Verkaufsstelle**.



Klicken Sie dann auf **Eine neue PoS-Anwendung erstellen**. Diese Aktion fügt eine **neue Anwendung** zu Ihrem BTCPay-Shop hinzu, als ob Sie eine interne Mini-Verkaufsseite installieren würden.



Es öffnet sich eine Seite zum Erstellen Ihrer Anwendung. Legen Sie einen **Anwendungsnamen** fest: Dies ist ein interner Name, der nur in Ihrem Dashboard sichtbar ist (z. B. _Shoe Shop_).



Klicken Sie zum Bestätigen auf **Erstellen**.



![capture](assets/fr/24.webp)



Nach der Erstellung werden Sie auf die **Detaillierte Konfigurationsseite** des Point of Sale weitergeleitet.



### Passen Sie Ihre Vertriebsoberfläche an



Auf dieser Seite können Sie die wesentlichen Elemente Ihres PoS festlegen:





- Anwendungsname** (interner Verwaltungsname, kann jederzeit geändert werden).





- Anzeigetitel** (was Ihre Kunden oben auf der Seite sehen).





- Verkaufsstellenstil** (der Modus **Beschreibung** eignet sich für Dienstleistungen wie Haarschnitte oder Mahlzeiten, während der Modus **Produktkatalog** ideal für Geschäfte ist, die mehrere Artikel anbieten).





- Währung anzeigen** (wählen Sie **XOF**, **EUR** oder **USD** entsprechend Ihren üblichen Preisen).





- Produktliste** (fügen Sie hier Ihre Produkte, Beschreibungen und Preise ein).



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



### Speichern und testen Sie Ihren PoS



Wenn Sie mit der Konfiguration fertig sind, klicken Sie auf **Speichern**, um Ihre Einstellungen zu speichern, und dann auf **Anzeigen**, um eine Vorschau Ihres PoS zu erhalten.



Sie sehen eine Seite, auf der Ihre Produkte vorgestellt werden, wobei jede Schaltfläche einem Artikel oder einer Dienstleistung entspricht.



Sobald ein Kunde ein Produkt auswählt:



1. BTCPay erstellt automatisch eine Bitcoin- oder Lightning**-Rechnung.



2. Auf dem Bildschirm erscheint ein **QR-Code**.



3. Die Kunden können mit ihrem Bitcoin wallet direkt **scannen und bezahlen**.




![capture](assets/fr/27.webp)



### Endgültiges Ergebnis



Sie haben jetzt einen kompletten **Bitcoin Point of Sale**, den Sie :





- Öffnen Sie von einem Smartphone oder Tablet in Ihrem Geschäft;





- Anzeige auf einem Bildschirm, den der Kunde scannen kann;





- Oder geben Sie sie über eine öffentliche **URL** weiter, z. B. eine vereinfachte Bestellseite.



Bei jeder Zahlung wird der Betrag automatisch auf **Ihrem eigenen BTCPay wallet** gutgeschrieben, ohne Zwischenhändler oder Gebühren Dritter.


Dadurch wird Ihr PoS zu einem **autonomen Bitcoin-Zahlungsterminal**.




## Alltäglicher Gebrauch



Bevor Sie sich echte Zahlungen auszahlen lassen, empfehlen wir Ihnen, einen **Test** durchzuführen, um zu prüfen, ob alles richtig funktioniert.



### Testen Sie eine Zahlung





- Erstellen Sie eine Rechnung** über Ihre PoS-Schnittstelle (z. B. ein 1 satoshi-Produkt oder einen kleinen Betrag).





- Scannen Sie den auf dem Bildschirm angezeigten QR-Code** mit einem Bitcoin oder Lightning wallet (z. B. **Phoenix**, **Muun** oder **Wallet von Satoshi**).




![capture](assets/fr/28.webp)





- Bestätigen Sie die Zahlung** in Ihrem wallet: Die Transaktion wird sofort gesendet.





- Rückkehr zum BTCPay-Server**: Die Rechnung wird in der Liste als **bezahlt** angezeigt.



![capture](assets/fr/29.webp)



Herzlichen Glückwunsch! Ihr Point of Sale ist jetzt **funktional**. Sie können nun Bitcoin-Zahlungen von Ihren Kunden empfangen, einfach, schnell und ohne Zwischenhändler.



### Eine Rechnung für einen Kunden erstellen



Klicken Sie im Menü **Rechnungen** auf **Neue Rechnung**.



![capture](assets/fr/30.webp)



Geben Sie den **Betrag** und die **Landeswährung** ein (BTCPay errechnet automatisch den Gegenwert in BTC), sowie weitere Informationen zum Produkt.



![capture](assets/fr/31.webp)



Teilen Sie dem Kunden den **QR-Code** oder die **URL** mit.



![capture](assets/fr/32.webp)



### Erhaltene Zahlungen verfolgen



Im Menü **Rechnungen** sehen Sie weiterhin eine Liste aller Ihrer Transaktionen.


Die möglichen Zustände sind:





- Ausstehend**: Die Zahlung wurde noch nicht bestätigt.





- Bezahlt**: Zahlung bestätigt.





- Abgelaufen**: Rechnung, die nicht bis zum Fälligkeitsdatum bezahlt wurde.



### Rückerstattung an einen Kunden



Wählen Sie im Menü **Rechnungen** die Rechnung aus, die erstattet werden soll.



![capture](assets/fr/33.webp)



Klicken Sie auf **Rückerstattung** und geben Sie die vom Kunden angegebene Bitcoin-Adresse ein.



![capture](assets/fr/34.webp)



![capture](assets/fr/35.webp)



### Berichte und Datenexport



Mit BTCPay Server können Sie Ihre Transaktionen **exportieren** (im CSV- oder Excel-Format). Dies ist sehr praktisch für Ihre Buchhaltung und Kassen-Nachbearbeitung.



![capture](assets/fr/36.webp)



Klicken Sie im Menü **Bericht** auf **Exportieren**: Alle Ihre Transaktionen werden in einer CSV-Datei gespeichert, die Sie dann lokal einsehen können.



## Sicherheit und bewährte Praktiken



Die vom BTCPay Server gewährte Autonomie (volle Souveränität über Ihr Geld) ist eine echte Stärke. Aber mit dieser Freiheit kommt auch eine größere Verantwortung in Bezug auf die Sicherheit. Indem Sie Ihre eigenen Zahlungen verwalten, übernehmen Sie die Rolle Ihrer eigenen Bank. Deshalb ist es unerlässlich, bewährte Verfahren zum Schutz Ihrer Gelder, Ihrer Daten und Ihrer Infrastruktur anzuwenden. Hier sind die wichtigsten Punkte, die Sie beachten sollten.



### Sicherer Zugang zu Ihrem Server





- Verwenden Sie ein sicheres Passwort: kombinieren Sie Groß- und Kleinbuchstaben, Zahlen und Sonderzeichen. Vermeiden Sie die Wiederverwendung eines bestehenden Passworts.
- Aktivieren Sie die Zwei-Faktor-Authentifizierung (2FA) für den Zugriff auf Ihre BTCPay-Schnittstelle.
- Aktualisieren Sie regelmäßig Ihr Betriebssystem, Ihre BTCPay-Server-Instanz und Ihre Abhängigkeiten (Docker, Bitcoin-Knoten, Lightning-Knoten...). Updates beheben häufig Sicherheitslücken.



### Verwalten und Sichern privater Schlüssel





- Speichern Sie Ihre privaten Schlüssel und Seedphrases offline auf physischen Medien (Papier oder Metall).
- Verwenden Sie vorzugsweise einen wallet Hardware wallet.
- Bewahren Sie mehrere Kopien Ihrer Backups an getrennten, geschützten Orten auf.



### Sichere Zahlungen und Vertraulichkeit





- Verwenden Sie das Tor-Netzwerk oder ein VPN, um die IP-Adresse Ihres Servers zu verbergen und Ihre Privatsphäre zu schützen.
- Deaktivieren Sie unnötige Ports auf Ihrem Server und beschränken Sie SSH-Verbindungen nur auf vertrauenswürdige Adressen.
- Aktivieren Sie HTTPS (SSL-Zertifikat) für alle Verbindungen zu Ihrem BTCPay-Webinterface.
- Geben Sie Ihre Verwaltungsschnittstelle niemals an Personal weiter, das nicht in der Bitcoin-Portfolioverwaltung geschult ist.



### Umsetzung bewährter Verfahren für das Lightning-Netzwerk



Ihr Geschäft ist mit einem **Lightning-Knoten, der auf Voltage** gehostet wird, verbunden, was die technische Verwaltung des Netzes erheblich vereinfacht. Dennoch bleibt es wichtig, **gute Überwachungs- und Sicherheitspraktiken** anzuwenden:





- Speichern Sie den API**-Login und die Zugriffsschlüssel Ihres Voltage-Knotens (die die Verbindung zu BTCPay ermöglichen).
- Schützen Sie Ihr Voltage-Konto** mit Zwei-Faktor-Authentifizierung und einem sicheren Passwort.
- Überwachen Sie den Status von Knoten und Kanälen** über Ihr Voltage Dashboard: So können Sie Anomalien oder Desynchronisationen erkennen.
- Vermeiden Sie es, Ihre API**-Anmeldedaten weiterzugeben oder sie öffentlich preiszugeben (z. B. in Website-Code).
- Im Falle einer Migration muss lediglich **die Verbindung zwischen BTCPay und Voltage** neu konfiguriert werden: kein Kanal muss manuell geschlossen werden.



Mit Voltage profitieren Sie von einer **sicheren, hochverfügbaren** und **automatisch gesicherten** Infrastruktur, während Sie die **vollständige Hoheit über Ihre Lightning-Zahlungen** behalten.



### Interne Abläufe organisieren und strukturieren





- Definieren Sie eine klare Zugriffsregelung: wer darf eine Rechnung erstellen, Zahlungen einsehen, auf den Knoten zugreifen usw.
- Dokumentieren Sie Ihre Sicherungs- und Wiederherstellungsverfahren, damit Sie im Falle eines Vorfalls schnell reagieren können.
- Testen Sie regelmäßig die Wiederherstellung Ihrer Backups, um sicherzustellen, dass sie ordnungsgemäß funktionieren.
- Schulen Sie Ihr Personal oder Ihre Mitarbeiter in der grundlegenden Betriebssicherheit: Wachsamkeit gegenüber Phishing, Verwendung sicherer Passwörter, Wahrung der Vertraulichkeit.



### Beaufsichtigung und Festlegung der laufenden Wartung





- Überwachen Sie die Aktivität Ihres Servers kontinuierlich mit Hilfe von Protokollierungs- oder Überwachungswerkzeugen.
- Planen Sie eine regelmäßige Sicherheitsüberprüfung: Überprüfen Sie Updates, Zugriff, Backups und die Konsistenz von Transaktionen.



Herzlichen Glückwunsch! Sie haben das Ende dieses Tutorials erreicht. Sie können sich nun selbständig mit BTCPay Server auseinandersetzen, was Ihnen die Verwaltung Ihres Shops erleichtert.



Um mehr darüber zu erfahren, empfehle ich Ihnen unseren vollständigen Schulungskurs zur Integration von Bitcoin in Ihr Unternehmen:



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a