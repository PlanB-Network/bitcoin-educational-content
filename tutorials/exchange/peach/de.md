---
name: Peach
description: Vollständiger Leitfaden zur Verwendung von Peach und zum Handel mit Bitcoins in P2P
---

![cover](assets/cover.webp)





## Einführung



KYC-freie Peer-to-Peer-Börsen (P2P) sind für die Wahrung der Vertraulichkeit und der finanziellen Autonomie der Nutzer unerlässlich. Sie ermöglichen direkte Transaktionen zwischen Einzelpersonen, ohne dass eine Identitätsüberprüfung erforderlich ist, was für diejenigen, die Wert auf ihre Privatsphäre legen, entscheidend ist. Für ein tiefergehendes Verständnis der theoretischen Konzepte siehe den Kurs BTC204:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### 1. Was ist Peach?



Peach ist eine P2P-Austauschplattform, die es Benutzern ermöglicht, Bitcoins ohne KYC zu kaufen und zu verkaufen. Sie bietet eine intuitive Schnittstelle und erweiterte Sicherheitsfunktionen. Im Vergleich zu anderen Lösungen wie Bisq, HodlHodl und Robosat zeichnet sich Peach durch seine Benutzerfreundlichkeit aus.


Ein multisignature-Treuhandsystem (2-2) garantiert die Sicherheit der Gelder während der Transaktionen. Peach unterstützt verschiedene Zahlungsmethoden und verfügt über ein Reputationssystem, das den Händlern bei ihren Handlungen hilft. Wie bei P2P-Plattformen üblich, ist es daher wichtig, einen guten Ruf zu pflegen, um die Glaubwürdigkeit bei anderen Händlern zu erhalten.



### 2. Datenschutz und gesammelte Daten



**Welche Informationen sammelt Peach?



Peach ist bestrebt, ein absolutes Minimum an Daten über seine Nutzer zu speichern. Hier finden Sie einen Überblick über die auf unseren Servern gespeicherten Daten:





- Eine hash Ihrer eindeutigen Antragskennung (AdID)
- Eine hash Ihrer Zahlungsdaten
- Ihre verschlüsselten Unterhaltungen
- Transaktionsdaten, um sicherzustellen, dass anonyme Nutzer das Handelslimit nicht überschreiten (Art der verwendeten Zahlungsmittel, Kauf- und Verkaufsbeträge)
- Addresses, die zum Senden und Empfangen vom Treuhandkonto verwendet werden
- Nutzungsdaten (Firebase & Google Analytics), nur mit Ihrer Zustimmung



Zur Erinnerung: Ein hash ist ein unkenntlich gemachter Datensatz, ähnlich wie bei einer Verschlüsselung. Dieselben Daten erzeugen immer dasselbe hash, wodurch es möglich ist, Duplikate zu erkennen, ohne die Originaldaten zu kennen.



*Eine ausführlichere Erklärung des hashing finden Sie in diesem Kurs:*



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

**Wer kann meine Zahlungsdaten einsehen?





- Nur Ihr Vertragspartner kann Ihre Zahlungsdaten einsehen
- Die Daten werden über Peach-Server übertragen, sind aber von Anfang bis Ende vollständig verschlüsselt
- Im Falle einer Streitigkeit sind Ihre Zahlungsdaten und Ihr Gesprächsverlauf für den beauftragten Peach-Vermittler sichtbar



## Installation und Konfiguration



### 1. Peach-Anwendung installieren



![Installation de Peach](assets/fr/01.webp)





- Laden Sie die Anwendung von [Peach Bitcoin] (https://peachbitcoin.com/fr/quick-start/) herunter. Unter iOS müssen Sie zunächst die App [testflight](https://apps.apple.com/us/app/testflight/id899247664) installieren.
- Befolgen Sie die Installationsanweisungen auf Ihrem Gerät.
- Während der Installation werden Sie gefragt, ob Sie bestimmte Daten freigeben möchten, um die Peach-Anwendung zu verbessern. (Bild 1)
- Auf dem nächsten Bildschirm (Abbildung 2) haben Sie zwei Möglichkeiten:
 - Wenn Sie ein neuer Benutzer sind, klicken Sie auf "Neuer Benutzer", um ein neues Profil zu erstellen
 - Wenn Sie bereits ein Konto haben, verwenden Sie "Wiederherstellen", um Ihr bestehendes Profil wiederherzustellen
- Wenn Sie einen Empfehlungscode haben, können Sie ihn hier eingeben.
- Um ein bestehendes Konto wiederherzustellen (Bild 3), benötigen Sie :
 - Ihre Sicherungsdatei
 - Das Passwort zur Entschlüsselung dieser Datei



### 2. Übersicht der Hauptbildschirme



Die Anwendung Peach ist in vier Hauptbildschirme unterteilt, die über die untere Navigationsleiste zugänglich sind:



![Navigation dans l'application](assets/fr/02.webp)





- Startseite (4)** : Der Hauptbildschirm, von dem aus Sie wählen können, ob Sie kaufen oder verkaufen, neue Transaktionen erstellen und auf verfügbare Angebote zugreifen:
 - angebote mit den beiden Schaltflächen unten erstellen (Kaufen / Verkaufen erstellen)
 - mit den beiden Schaltflächen unten ("Kaufen"/"Verkaufen") die von anderen Nutzern erstellten Angebote nutzen.





- Wallet (5)** : Ihr integrierter bitcoin wallet, der es Ihnen ermöglicht, :
 - Prüfen Sie Ihr Guthaben
 - Bitcoins erhalten
 - Envoyer Bitcoins (mit Münzkontrolle)
 - Ihre Transaktionshistorie einsehen
 - Finanzierung Ihrer Verkäufe





- Trades (6)**: Ihre aktuellen und vergangenen Verträge, auf drei Registerkarten:
 - Laufende Käufe
 - Laufende Verkäufe
 - Die Geschichte Ihres Austausches





- Einstellungen (7)** : Das Konfigurationszentrum für
 - Ihr Profil einsehen (Ruf, Abzeichen, Grenzen usw.)
 - Verwaltung der Sicherheit (Backup, Pin)
 - Verwalten Sie Ihre Zahlungsmittel
 - Kontakt zum Support
 - Sprache ändern
 - usw.



### 3. Konfigurieren Sie Ihre Zahlungsarten



![Accès aux paramètres de paiement](assets/fr/03.webp)



Sie können Ihre Zahlungsarten in den Einstellungen verwalten (Abbildung 8)



Peach bietet Online-Zahlungen und persönliche Zahlungen (nur bei registrierten Treffen).



**Online-Zahlungen



**Wichtig:**


um die Nutzer zu schützen, verlangt die Peach, dass die Herkunft der Gelder mit der angegebenen übereinstimmt. Die Händler müssen zu ihrem eigenen Schutz sicherstellen, dass dies der Fall ist.



![Configuration des paiements en ligne](assets/fr/04.webp)



So fügen Sie eine Methode hinzu:




- Klicken Sie auf der Registerkarte "Online" auf "Eine Währung/Methode hinzufügen"
- Wählen Sie Ihre Währung
- Wählen Sie Ihre bevorzugte Zahlungsmethode



*Verfügbare Zahlungsarten:*



***Für Banküberweisungen: ***




- SEPA (Standard oder Sofort)
- Geben Sie Ihre SEPA-Bankverbindung ein.



***Online wallet akzeptiert :***




- Je nach Land stehen mehrere Optionen zur Verfügung (Revolut, Paypal, Wise, Strike, usw.)
- Folgen Sie den Anweisungen, um Ihre Anmeldedaten hinzuzufügen



*geschenkkarte verwendbar:*** Geschenkkarte verwendbar:*** Geschenkkarte verwendbar:*** Geschenkkarte verwendbar:*** Geschenkkarte verwendbar:*** Geschenkkarte verwendbar:***




- Amazon, Steam, etc.
- Geben Sie das Land, in dem die Karte ausgestellt wurde, und andere erforderliche Informationen ein



***Nationale Zahlungsmöglichkeiten:***


Länderspezifische Zahlungssysteme :




- Satispay (Italien)
- MB Way (Portugal)
- Bizum (Spanien)
- Faster Payments (Vereinigtes Königreich)
- usw.



***Für persönliche Zahlungen: ***



![Configuration des paiements en personne](assets/fr/05.webp)





- Wählen Sie "Meetup" (Bild 12)
- Wählen Sie dann Ihr Treffen aus der Liste aus (Abbildung 13)



### Gebrauchsanweisung





- Sie können mehrere Zahlungsarten hinzufügen
- Je mehr Methoden Sie hinzufügen, desto breiter ist die Palette der Angebote, die Sie nutzen können
- Überprüfen Sie die Richtigkeit Ihrer Angaben vor der Anmeldung
- Sie können Ihre Zahlungsarten jederzeit ändern oder löschen



**Sicherheitshinweis**: Ihre Zahlungsinformationen sind verschlüsselt und werden nur während einer Transaktion an Ihren Tauschpartner weitergegeben, es sei denn, es handelt sich um einen Streitfall, zu dem auch ein Peach-Vermittler Zugang hat.



### 4. Wie Sie Ihr Portfolio sichern können



**Verstehen Sie Ihr Peach-Konto



Ein Peach-Konto hat keinen Benutzernamen und kein Passwort. Es handelt sich um eine Datei, die lokal auf Ihrem Telefon gespeichert ist, was bedeutet, dass Peach Ihre Daten nicht speichern muss und Ihre Identität nicht kennt: Sie haben die Kontrolle. Diese Datei enthält alle Ihre Daten: einschließlich der 12 Bitcoin-Wiederherstellungswörter, PGP-Schlüssel, Zahlungsdetails und so weiter. Es ist also wichtig, diese Datei zu speichern und sie mit einem __robusten__ Passwort zu schützen.



Dieser Ansatz garantiert ein gewisses Maß an Vertraulichkeit und überlässt die Verantwortung für die Daten- und Backup-Verwaltung dem Benutzer. Wenn Sie Ihr Telefon ohne Backup verlieren, haben Sie keinen Zugriff mehr auf Ihr Peach-Konto und Ihr Geld.



**Sicherungen erstellen**






- Zugriff auf die Einstellungen über die Registerkarte unten rechts auf dem Startbildschirm
- Wählen Sie im Einstellungsmenü die Option "Backups"



![Processus de sauvegarde](assets/fr/06.webp)



Es sind zwei Arten der Sicherung verfügbar:



**Kontodatei speichern (Bild 14)**




- Klicken Sie auf "Neue Sicherung erstellen"
- Erstellen Sie ein **starkes** Passwort, um Ihre Sicherungsdatei zu verschlüsseln
- Senden Sie diese Datei an einen Ort, der ihre Redundanz im Falle des Verlusts des Telefons gewährleistet.



Die Dateisicherung stellt Ihr komplettes Peach-Konto wieder her, einschließlich :




- Ihr Portfolio
- Ihre Zahlungsmodalitäten
- Zahlungsdaten
- Transaktionshistorie mit Angaben zu Gegenparteien und Gesprächen mit ihnen



**Speichern des Wiederherstellungssatzes (Bild 15)**




- Folgen Sie den Anweisungen, um Ihre Wiederherstellungsphrase anzuzeigen
- Schreiben Sie die Wörter sorgfältig in der richtigen Reihenfolge auf
- Speichern Sie diese Sicherungskopie an einem sicheren Ort, idealerweise an einem anderen Ort als die Kontodatei



Die Wiederherstellungsphrase ermöglicht die Wiederherstellung von :




- Ihr Ruf, Ihre Berufe
- Ihr Bitcoin-Guthaben



Aber **NICHT** die folgenden:




- Ihre aktuellen und vergangenen Unterhaltungen
- Zahlungsdaten
- Kontrahenteninformationen in der Transaktionshistorie




## Kauf und Verkauf von Bitcoins



### 1.a Wie man Bitcoins kauft: Nehmen Sie ein Verkaufsangebot an



Der erste Reflex eines Käufers sollte sein, sich die Verkaufsangebote anzuschauen, die bereits mit Bitcoin finanziert sind.



![Vue des offres de vente et filtres](assets/fr/07.webp)





- Klicken Sie auf dem Startbildschirm auf die Schaltfläche "Kaufen" (Abbildung 16)
- Sie können dann eine Liste der Bitcoins einsehen, die im Treuhandsystem hinterlegt wurden und zum Verkauf bereitstehen (Abbildung 17). Sie können den Betrag, den Preis (in % im Vergleich zum KYC-Markt), die Zahlungsarten und die akzeptierten Währungen sehen.
- Verwenden Sie Filter zum Sortieren und Ordnen der Angebote (Abbildung 18).
- Hinweis: Über die Schaltfläche am unteren Rand der Filterseite können Sie sich benachrichtigen lassen, wenn ein Angebot, das Ihren Filtern entspricht, veröffentlicht wurde; über die Schaltfläche "Zurücksetzen" werden einfach alle Filter gelöscht (Abbildung 18).



![Sélection et confirmation d'achat](assets/fr/08.webp)





- Sehen Sie sich das für Sie passende Angebot an und senden Sie eine Umtauschanfrage (Bild 19)
- Sie können mehrere Umtauschanträge stellen, und das erste positive Angebot wird Ihre anderen Anträge stornieren.
- Bezahlen Sie nach der vereinbarten Methode.


**Erinnerung:** Die Geldquelle muss mit der übereinstimmen, die Sie beim Hinzufügen der Zahlungsmethode angegeben haben.




- Bestätigen Sie Ihre Zahlung in der Anwendung, sobald sie erfolgt ist**.
- Warten Sie, bis der Verkäufer die Zahlung erhalten hat, und melden Sie sie als solche (Bild 20)
- Und schließlich bewerten Sie Ihre Erfahrungen mit dem Verkäufer (Abbildung 21)



![Réception des bitcoins](assets/fr/09.webp)





- Verfolgen Sie den Status Ihrer Transaktion
- Bestätigung des Empfangs von Bitcoins prüfen
- Die Mittel werden in Ihrem Peach-Portfolio verfügbar sein (Abbildung 22 und 23)



### 1.b Wie man Bitcoins kauft: Ein Gebot erstellen



Wenn Sie kein passendes Angebot zum Verkauf finden, können Sie ein Kaufangebot erstellen. Da Sie in diesem Stadium noch keine Bitcoins einsetzen, haben Sie weniger Chancen, einen Tauschpartner zu finden, vor allem, wenn Ihre Erfolgsbilanz und Ihr Ruf schlecht oder gar nicht vorhanden sind. Um hier Abhilfe zu schaffen, ist es wichtig, bei der Erstellung des Angebots ein *hochpreisiges Angebot* zu machen, um die Verkäufer zu motivieren, Ihr Angebot zu wählen. Lassen Sie uns fortfahren:



![Creation d'ordre d'achat](assets/fr/10.webp)





- Klicken Sie auf dem Startbildschirm auf die Schaltfläche "Kaufangebot erstellen" (Abbildung 24)
- Fügen Sie eine Zahlungsmethode hinzu, falls Sie dies noch nicht getan haben, und geben Sie Ihre Präferenzen ein (Menge, Prämie usw.) (Abbildung 25).


Mit der Option "Sofort" können Sie eine Handelsanfrage automatisch annehmen.




 - Klicken Sie erneut auf "Angebot erstellen", um fortzufahren
- Nach der Erstellung ist der Verkäufer an der Reihe, sich mit einer Tauschanfrage an Sie zu wenden. Sie können die App ohne Bedenken schließen und verlassen.
- Sie können die Prämie ändern, wenn Sie keine Anfragen erhalten. Denken Sie daran: Eine höhere Prämie motiviert die Verkäufer, Ihr Angebot zu suchen (Abbildung 26).
- Sie finden Ihr Angebot auf der Registerkarte "Kaufen", die sich wiederum im Fenster "Exchange" befindet (Abb. 27)



![Reception d'une demande de vente, messagerie](assets/fr/11.webp)





- Wenn Sie eine Kaufanfrage (Abb. 28) erhalten (und wenn Sie den Soforthandel in Abb. 25 nicht deaktiviert haben), akzeptieren Sie den Handel, nachdem Sie den Ruf des Verkäufers überprüft haben. Wenn der Soforthandel aktiviert ist, springen Sie direkt zu Abbildung 29.
- Der Verkäufer muss dann die Bitcoin in das Treuhandsystem einzahlen ("den Safe finanzieren"). (Bild 29)
- Bezahlen Sie den Verkäufer dann über Ihr persönliches Banksystem an dem in Abb. 30 angegebenen Ort. Ziehen Sie den Cursor "Ich habe die Zahlung getätigt" nicht, bevor Sie dies getan haben!
- Sie können mit dem Verkäufer über das Nachrichtensystem (P2P verschlüsselt) kommunizieren. Im Falle eines Problems können Sie einen Streitfall eröffnen, indem Sie auf das Symbol in der rechten oberen Ecke klicken (Abbildung 31). Ein Peach-Vermittler wird sich dann in die Diskussion einschalten.



![Offre de vente completée](assets/fr/12.webp)





- Sobald der Verkäufer das Geld erhalten hat, meldet er es, und das Treuhandsystem gibt den Bitcoin frei, der dann auf dem Weg zu Ihrem wallet ist (standardmäßig über GroupHug, das Transaktionsgruppierungssystem von Peach, das einmal am Tag läuft),
- Bewerten Sie Ihre Erfahrungen mit dem Verkäufer



Das war's!



**Hinweis für neue Käufer:** Verkäufer richten sich bei ihren Angeboten nach dem Ruf des Käufers und neigen dazu, Gebote von Käufern zu vermeiden, die noch keine Geschäfte abgeschlossen haben. Es ist zunächst einfacher, sich einen Ruf zu verschaffen, indem man bereits vorhandene Verkaufsangebote annimmt.




### 2.a Wie man Bitcoins verkauft: Einen Verkauf erstellen



Der schnellste und einfachste Weg, auf Peach zu verkaufen, ist die **Erstellung eines Verkaufsangebots**.



![Création d'un ordre de vente](assets/fr/13.webp)





- Klicken Sie auf der Startseite auf "Verkaufsangebot erstellen" (Abbildung 32)
- Richten Sie Ihr Angebot ein und stellen Sie sicher, dass Sie eine Zahlungsmethode und die richtigen Parameter eingeben


sie können auch :




  - mehrere identische Angebote erstellen
  - aktivieren Sie den "Sofortigen Austausch", damit der erste Käufer, der sich meldet, den Vertrag (ohne Ihre Bestätigung) annehmen und mit der Zahlung fortfahren kann.
  - wählen Sie eine Erstattungsadresse
  - finanzieren Sie den Kofferraum Ihres wallet Peach
- Finanzieren Sie die Transaktion, indem Sie die Bitcoins an die angegebene Adresse senden (Bild 34)
- Warten Sie auf die Bestätigung der Transaktion. Sobald dies geschehen ist, wird Ihr Angebot auf dem Markt sichtbar sein.



![Attente du paiement](assets/fr/14.webp)





- Warten Sie auf einen Käufer, der Ihr Angebot annimmt. Erwägen Sie eine Erhöhung der Prämie (%), wenn Sie die Dinge beschleunigen wollen (Abbildung 36)
- Sobald Sie eine Tauschanfrage erhalten haben, prüfen Sie den Ruf des Käufers. Beurteilen Sie selbst, ob das Profil für Sie geeignet ist, und klicken Sie auf "Akzeptieren", wenn dies der Fall ist. (37)
- Jetzt ist der Käufer an der Reihe, die Zahlung von seiner Bank an Ihre zu überweisen. Er wird dann die Zahlung an Sie weiterleiten. Zögern Sie nicht, den Käufer im Chat zu kontaktieren.
- nachdem Sie sich vergewissert haben, dass der Betrag bei Ihrer Bank* eingegangen ist, geben Sie den Betrag frei, indem Sie auf die Schaltfläche "Ich habe die Zahlung erhalten" klicken (Abbildung 38). Bestätigen Sie niemals den Erhalt einer Zahlung, bevor Sie nicht geprüft haben, ob sie auf Ihrem Konto eingegangen ist.
- Bewerten Sie die Transaktion
- Bitcoin werden automatisch für den Käufer freigegeben,



Na also!



**Sicherheitshinweise und Tipps für eine erfolgreiche Transaktion:**




 - Achten Sie auf die Angaben des Käufers und prüfen Sie, ob die Herkunft des Geldes mit der auf Peach beschriebenen übereinstimmt. Wenn die Herkunft des Geldes nicht mit der angegebenen übereinstimmt, gehen Sie zum Chat und eröffnen Sie einen Streit (Bild 39), und schicken Sie das Geld an seinen Ursprung zurück.
 - Folgen Sie den Anweisungen in der gelben Katze.
 - Reagieren Sie schnell auf Nachrichten von Ihrem Geschäftspartner
 - achten Sie auf die Einstellung des Käufers, insbesondere wenn es sich um ein Profil mit wenig Erfahrung handelt
 - Zögern Sie nicht, den Mediationsdienst in Anspruch zu nehmen, wenn Sie ein Problem haben



### 2.b Wie man Bitcoins verkauft: ein Gebot abgeben



Es ist auch möglich, Kaufangebote anzusehen und auszuwählen. Hier müssen Sie besonders vorsichtig sein, da hier die meisten Betrüger zu finden sind.



![Prendre une offre d'achat](assets/fr/15.webp)





- Klicken Sie auf der Startseite auf "Vertrieb" (Abbildung 40)
- Verwenden Sie die Filter, um die attraktivsten Angebote anzuzeigen und auszuwählen (Abbildung 41)



![vérification de la réputation](assets/fr/16.webp)





- wir empfehlen Ihnen, das Profil des Käufers auf seine Eignung hin zu überprüfen, bevor Sie ein Angebot machen. Sie können auf ein Angebot und dann auf die ID des Nutzers klicken, um sein Profil zu sehen. Das Angebot in Abbildung 42 könnte zum Beispiel als "riskant" eingestuft werden (neuer Nutzer, relativ hoher Betrag). Das "Risiko", das Sie eingehen, wenn Sie dieses Angebot annehmen, besteht lediglich darin, Zeit zu verschwenden, solange Sie nicht den Fehler machen, die Bitcoins freizugeben, ohne das Geld erhalten zu haben. Sie können die Bitcoins immer noch im Tresor deponieren.


Das in Abbildung 43 gezeigte Angebot stammt dagegen von einem erfahrenen Händler (Abbildung 44), bei dem es in der Vergangenheit keine Streitigkeiten gab. Es handelt sich also um ein weniger riskantes Angebot.



![Match avec vendeur](assets/fr/17.webp)





- Sobald das Angebot angefordert wurde und der Käufer Ihre Anfrage annimmt, werden Sie zu Bild 34 weitergeleitet, wo Sie den Handel wie unten beschrieben fortsetzen können.




## Vorteile und Nachteile



### Peach Vorteile





- Keine KYC erforderlich**: Bewahrt die Vertraulichkeit der Nutzer.
- Kein Zugang zu Bankdaten**: Die Peach hat keinen Zugriff auf Ihre Bankdaten oder Ihre Identität.
- Interface intuitiv**: Einfach zu bedienen für fortgeschrittene Benutzer.
- Offener Quellcode** : Der Quellcode ist öffentlich und von der Gemeinschaft überprüfbar.



### Peach Nachteile





- Begrenzte Liquidity**: Geringeres Handelsvolumen als bei etablierteren Plattformen.
- Regulatorisches Risiko** : Die Anwendung wird von einem Schweizer Unternehmen verwaltet. Sie unterliegt daher den Schweizer Vorschriften, die sich weiterentwickeln und die Anwendung möglicherweise zensieren könnten.



## Nützliche Ressourcen





- Französisches Erklärungsvideo: [YouTube](https://youtu.be/ziwhv9KqVkM)
- Schnellstart-Anleitung: [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/)
- [Support telegram](t.me/peachtopeach) (Vorsicht vor Betrügern, die Administratoren werden Sie niemals zuerst per privater Nachricht anschreiben)