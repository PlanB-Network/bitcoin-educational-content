---
name: Einfache Anmeldung
description: Mit Pseudonymen geschützte Identität
---
![cover](assets/cover.webp)

## Anmeldung = E-Mail = Verlust der Privatsphäre


In der digitalen Welt ist es üblich geworden, für jede Plattform, auf die man zugreifen möchte, ein Konto zu haben.

Für jeden dieser Dienste ist eine Anmeldung erforderlich, die in der Regel mit dem Paar _Benutzername_ und _Passwort_ verbunden ist. Oft ist der Benutzername die persönliche E-Mail-Adresse des Benutzers.


Wenn man seinen persönlichen E-Mail-Address für jede Anmeldung verwendet, kann man sich leicht die erste Folge vorstellen: den Verlust der Vertraulichkeit, der besonders schwerwiegend wird, wenn der Address aus _name.surname@serviceemail.com_ besteht.


Entwickler von Open-Source-Tools haben eine Reihe von Anwendungssuiten entwickelt, die den Nutzern ein Stück Privatsphäre zurückgeben sollen: Sie melden sich zwar weiterhin an, verwenden aber einen Alias anstelle des Tools, das ihre private Identität preisgibt.


Die einfachste von denen, die ich persönlich ausprobiert habe und immer noch teste, ist [Simple Login] (https://simplelogin.io/).


## Alias


Ein E-Mail-Alias ersetzt einfach den Teil _Name.Nachname_ Ihrer E-Mail Address durch einen fiktiven Namen. Für den Benutzer ändert sich nichts; der Alias-Dienst leitet die E-Mails ganz normal an den und vom normalen Address weiter. Jeder kann seinen Posteingang wie gewohnt nutzen, aber statt des echten Namens wird ein nicht erkennbarer Benutzer angezeigt. Dieser Dienst muss effizient sein, und bis jetzt hat sich Simple Login als genau das erwiesen.


Wenn Sie die Simple-Login-Website zum ersten Mal besuchen, müssen Sie ein Konto erstellen (auch hier!), indem Sie die "offizielle" E-Mail Address verwenden. Hier müssen Sie die E-Mail und ein Passwort eingeben und ein Captcha lösen.


![image](assets/it/02.webp)


Simple Login sendet eine Bestätigungsnachricht an die angegebene E-Mail Address. Anstatt auf die Verifizierungsschaltfläche zu klicken, ist es ratsam, den Link zu kopieren und ihn in die Address-Leiste einzufügen.


![image](assets/it/03.webp)


![image](assets/it/04.webp)


Das Dashboard für die einfache Anmeldung wird sofort geöffnet und enthält eine kurze Anleitung zur Navigation.


![image](assets/it/05.webp)


Es ist zu beachten, dass Simple Login automatisch das Abonnement des Newsletters aktiviert, das über den entsprechenden Befehl deaktiviert werden kann.


![image](assets/it/06.webp)


## Einstellungen


Sie können sofort einen Blick auf die _Einstellungen_ werfen, um die Funktionen des Dienstes zu entdecken. Beim Simple Login sind zunächst alle Optionen aktiv, auch die _Premium_, die 10 Tage lang nutzbar bleiben. Nach Ablauf der Testphase haben Sie die Möglichkeit, 10 Aliasnamen mit diesem Profil zu erstellen und Sie können Ihre Proton-E-Mail direkt verknüpfen, da Simple Login von dem Schweizer E-Mail-Anbieter übernommen wurde.


![image](assets/it/07.webp)


Sie können eine Reihe von Parametern festlegen oder überprüfen, ob Ihre E-Mail bereits in Bezug auf den Datenschutz gefährdet ist.


![image](assets/it/08.webp)


Schließlich können Sie ein Backup Ihres Profils exportieren oder von einem anderen Anbieter importieren.


![image](assets/it/09.webp)


### Arbeit E-Mail


Diejenigen, die E-Mails mit einer persönlichen Domain als Arbeits-E-Mail verwenden, können ihre private Domain einrichten.


![image](assets/it/10.webp)


Im Hauptfenster können Sie unter _Postfächer_ auch andere E-Mail-Adressen hinzufügen und die Aliase verwenden, die entsprechend erstellt werden. In diesem Lernprogramm habe ich mich zum Beispiel entschieden, das Profil mit einem _gmail.com_-Postfach zu erstellen und dann ein _proton.me_ Address zuzuordnen.


![image](assets/it/11.webp)


Beim Hinzufügen eines neuen Address, insbesondere wenn er zum Proton-Provider gehört, zeigt das geführte Verfahren die Möglichkeit, in den _sudo_-Modus, den Superuser, zu gelangen. Simple Login fordert zur Eingabe des Passworts dieser Mailbox auf, um die Legitimität des Ownership zu beweisen.


⚠️ **Ich persönlich rate davon ab**. ⚠️


![image](assets/it/12.webp)


**Es ist besser, auf das E-Mail-Postfach zuzugreifen -> den Link zur Verifizierung zu kopieren und in die URL-Leiste einzufügen -> und die Verifizierung zu erhalten, ohne das Passwort preiszugeben


![image](assets/it/13.webp)


Von den beiden eingegebenen Adressen wird eine zur Standard- und die andere zur Sekundäradresse, aber sie können leicht ausgetauscht werden, und die Einstellung ist im Dashboard leicht zu erkennen.


![image](assets/it/14.webp)


Nachdem wir eine zweite E-Mail Address (optional) hinzugefügt haben, wollen wir sehen, was wir mit Simple Login machen können.


## Erstellung von Aliasen


Im Panel ist die erste Menüoption mit _Alias_ beschriftet, wo Sie sie erstellen können. Sie haben die Möglichkeit, generate Aliase nach dem Zufallsprinzip zu erstellen, indem Sie auf die Schaltfläche "Zufälliger Alias" klicken, bei der es sich um die auf dem nächsten Foto gezeigte Schaltfläche Green handelt. Mit dieser Funktion können Sie eine einzigartige und faszinierende E-Mail Address erstellen.


![image](assets/it/24.webp)


Wenn Sie jedoch die Dienste durch unterschiedliche Namen unterscheiden möchten, müssen Sie _Neuer benutzerdefinierter Alias_ wählen. Auf diese Weise können Sie dem Alias den Namen des Dienstes geben, auf den Sie zugreifen möchten (soziale Medien, Dienstleister, Online-Events, Fremde, die Sie zufällig getroffen haben, usw.). Der Rest wird von Simple Login erledigt.

Aus Spaß (aber nicht wirklich, um die Wahrheit zu sagen) habe ich beschlossen, einen Alias für die Bank zu erstellen und ihn `BANK` zu nennen. Auch wenn es stimmt, dass meine Bank alles über mich weiß, finde ich es amüsant, mit ihr über eine E-Mail Address zu kommunizieren, die für sie unverständlich ist. Simple Login generiert tatsächlich einen zufälligen Namen, der von dem von uns gewählten durch ein `.` getrennt wird


Hier kann die neue E-Mail Address werden:


- bank.breeding123@aleeas.com
- bank.platter456@slmails.com
- bank.preoccupy789@8shield.net
- und so weiter


Es können mehrere Domains ausgewählt werden: Öffentliche Domains sind mit dem kostenlosen Tarif verfügbar, während andere, die als privat gekennzeichnet sind (einschließlich _@simplelogin.com_), die Auswahl für Nutzer, die sich für einen kostenpflichtigen Tarif entscheiden, erweitern.


![image](assets/it/15.webp)


Sobald die zufällige Endung und die Domäne ausgewählt wurden, können Sie festlegen, ob dieser neue (und bizarre) Address als Alias für nur eines der persönlichen E-Mail-Postfächer oder für alle dienen soll. Der Alias wird nach einem Klick auf _Erstellen_ fertig und aktiv


![image](assets/it/16.webp)


Die neue E-Mail Address wurde erstellt und ist nun sichtbar und kann durch einfaches Kopieren (an die Bank!) gesendet werden.


![image](assets/it/18.webp)


An diesem Punkt können Sie sich darauf konzentrieren, einen Alias für jeden Dienst oder jede Plattform zu erstellen, auf den/die Sie zugreifen möchten und bei dem/der die E-Mail als wesentlicher Parameter für die Erstellung eines Kontos erforderlich ist.


![image](assets/it/19.webp)


Für Liebhaber des Datenschutzes gibt es auch die Option, generate eine E-Mail Address auf der Grundlage des UUID-Protokolls (nicht auf identifizierbaren Namen) zu erstellen, das einen eindeutigen 128-Bit-Bezeichner erzeugt, der nicht von zentralen Parteien kontrolliert wird. Diese Funktion, die für sensible Konten nützlich ist, finden Sie im Menü _Zufälliger Alias_.


![image](assets/it/21.webp)

![image](assets/it/22.webp)


Wie Sie sehen, handelt es sich um einen E-Mail-Address, der eine angemessene Verwaltung erfordert.


Wenn Sie es sich anders überlegen und einen Alias nicht mehr verwenden möchten, klicken Sie einfach auf den Befehl _Mehr_ für jeden einzelnen Alias und wählen Sie _Löschen_.


![image](assets/it/23.webp)


## Alias-Verwaltung


Die Erstellung von Aliasen ist einfach, ebenso wie ihre Verwaltung, die nur ein wenig Sorgfalt und Disziplin erfordert. Der gesamte Datenverkehr läuft weiterhin über das E-Mail-Postfach, das wir zu Beginn als offizielles Postfach definiert haben. Benachrichtigungen und wichtige Mitteilungen von Plattformen werden weiterhin über Gmail, Proton oder den jeweiligen E-Mail-Anbieter verschickt.


Das Ergebnis ist jedoch, dass wir die Haupt-Address erhalten haben, die wir ab dem Zeitpunkt der Erstellung der Aliasnamen frei entscheiden können, wem wir sie offenlegen und wem nicht.


Ein Alias funktioniert sowohl für den Empfang als auch für das Senden: Ein anderer Benutzer wird die Antwort von alias.preoccupy789@8shield.net tatsächlich erhalten, wenn dies das für diesen bestimmten Empfänger gewählte Pseudonym ist.


## Profis


Insgesamt ist die Verwendung von Pseudonymen ein effektiver Weg, um Ihre Identität und Ihre Privatsphäre zu schützen. E-Mail-Adressen werden häufig von Datenmaklern und Websites gesammelt, um die Gewohnheiten und das Verhalten der Nutzer zu verfolgen. Ein Alias macht Sie zwar nicht völlig unauffindbar, aber die konsequente Verwendung eines Alias ist ein positiver Schritt zum Schutz Ihrer Daten. Außerdem ist es in unserem "globalen digitalen Dorf", in dem Hackerangriffe, Datenverkauf und Sicherheitsverletzungen nur allzu häufig vorkommen, sehr wahrscheinlich, dass die E-Mail, die Sie zur Registrierung auf verschiedenen Websites verwenden, bereits kompromittiert oder ins Visier genommen wurde.


Ein eindeutiges Pseudonym, das für jede Anmeldung verwendet wird, **ermöglicht es uns sofort zu verstehen, welche Plattform Spam (oder Schlimmeres) an unsere Mailbox sendet, da die E-Mail durch den damit verbundenen Alias identifiziert wird**. Sie haben keine Ahnung, wie viel Spam und Phishing von so genannten zuverlässigen, weil institutionellen Kanälen kommt, bis Sie anfangen, einen Alias für Banken, einen für Postdienste oder einen speziellen für einige obligatorische Regierungsdienste zu verwenden. Sobald der Absender der Spam (oder Schlimmeres) identifiziert ist, wissen Sie, dass diese Website kompromittiert wurde, und treffen alle Vorsichtsmaßnahmen, um alle Daten zu schützen, die Sie dieser speziellen Website zur Verfügung stellen (denken Sie an Kreditkarten!), die den Einbruch vielleicht erst Wochen später bemerkt.


Was die einfache Anmeldung betrifft, so verfügt dieses Tool über die folgenden Funktionen:



- mobile App (auch von F-Droid) und Browsererweiterung, um Aliase in jeder Situation zu verwalten;
- zwei-Faktor-Authentifizierung für jedes neue Pseudonym, was den Grad der Unabhängigkeit vom Dienst selbst erhöht;
- PGP-Unterstützung (für _Premium-Benutzer);
- einfache Erstellung aller Arten von Aliasen (benutzerdefiniert, zufällig und UUID);
- unter den kostenlosen Angeboten des Sektors die Möglichkeit, Aliase mit mehreren "offiziellen" E-Mail-Postfächern zu verwenden. Andere Konkurrenten beschränken sich auf nur einen.


## Nachteile


- 10 Aliasnamen sind vielleicht nicht genug, wenn Sie Simple Login ausgiebig nutzen wollen. In diesem Fall ist der kostenpflichtige Plan, der recht erschwinglich ist, nützlich, um die Anzahl der möglichen Aliase zu erhöhen.
- Es ist nicht möglich, einen Alias mit einem bestimmten Namen und einer bestimmten Domäne zu erstellen. Die zufällige Endung, die nach einem von uns gewählten Namen hinzugefügt wird, erzeugt einen Address, der bestenfalls als bizarr bezeichnet werden kann. Traditionelle soziale Medien weigern sich in der Regel, Konten mit dieser Art von E-Mail-Adressen zuzulassen. Nostr schafft hier Abhilfe!
- Wenn Sie ein Pseudonym verwenden, um eine Nachricht an jemanden zu senden, kann sie leicht im Spam-Ordner des Empfängers landen. In einem ersten Schritt ist es ratsam, das Pseudonym für den Empfang zu verwenden, genau wie bei der Einrichtung eines Kontos, der Anmeldung bei einer Mailingliste usw.