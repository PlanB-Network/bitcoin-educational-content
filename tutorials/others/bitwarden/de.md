---
name: BITWARDEN
description: Wie richtet man einen Passwort-Manager ein?
---
![cover](assets/cover.webp)

Im digitalen Zeitalter müssen wir eine Vielzahl von Online-Konten verwalten, die verschiedene Aspekte unseres täglichen Lebens abdecken, einschließlich Bankwesen, Finanzplattformen, E-Mails, Dateispeicherung, Gesundheit, Verwaltung, soziale Netzwerke, Videospiele usw.

Um uns bei jedem dieser Konten zu authentifizieren, verwenden wir einen Identifikator, oft eine E-Mail-Adresse, begleitet von einem Passwort. Angesichts der Unmöglichkeit, sich eine große Anzahl einzigartiger Passwörter zu merken, könnte man versucht sein, dasselbe Passwort wiederzuverwenden oder eine gemeinsame Basis leicht zu modifizieren, um es sich leicht merken zu können. Diese Praktiken gefährden jedoch ernsthaft die Sicherheit Ihrer Konten.

Das erste Prinzip, das man bei Passwörtern befolgen sollte, ist, sie nicht wiederzuverwenden. Jedes Online-Konto sollte durch ein einzigartiges und völlig unterschiedliches Passwort geschützt sein. Dies ist wichtig, denn wenn ein Angreifer eines Ihrer Passwörter kompromittieren kann, möchten Sie nicht, dass er Zugang zu all Ihren Konten hat. Ein einzigartiges Passwort für jedes Konto zu haben, isoliert potenzielle Angriffe und begrenzt deren Reichweite. Wenn Sie beispielsweise dasselbe Passwort für eine Videospieleplattform und für Ihre E-Mail verwenden und dieses Passwort über eine mit der Spieleplattform verknüpfte Phishing-Seite kompromittiert wird, könnte der Angreifer dann leicht auf Ihre E-Mail zugreifen und die Kontrolle über alle Ihre anderen Online-Konten übernehmen.

Das zweite wesentliche Prinzip ist die Stärke des Passworts. Ein Passwort gilt als stark, wenn es schwer durch Brute-Force, also durch Ausprobieren, zu erraten ist. Das bedeutet, dass Ihre Passwörter so zufällig wie möglich, lang und mit einer Vielfalt von Zeichen (Kleinbuchstaben, Großbuchstaben, Zahlen und Symbole) sein müssen.

Diese beiden Sicherheitsprinzipien für Passwörter (Einzigartigkeit und Robustheit) im Alltag anzuwenden, kann schwierig sein, da es fast unmöglich ist, sich ein einzigartiges, zufälliges und starkes Passwort für all unsere Konten zu merken. Hier kommt der Passwort-Manager ins Spiel.

Ein Passwort-Manager generiert und speichert sicher starke Passwörter, sodass Sie auf alle Ihre Online-Konten zugreifen können, ohne sich diese einzeln merken zu müssen. Sie müssen sich nur ein Passwort merken, das Master-Passwort, das Ihnen Zugang zu allen Ihren im Manager gespeicherten Passwörtern gibt. Die Verwendung eines Passwort-Managers verbessert Ihre Online-Sicherheit, da sie die Wiederverwendung von Passwörtern verhindert und systematisch zufällige Passwörter generiert. Aber es vereinfacht auch Ihre tägliche Nutzung Ihrer Konten, indem es den Zugang zu Ihren sensiblen Informationen zentralisiert.
In diesem Tutorial werden wir erkunden, wie man einen Passwort-Manager einrichtet und verwendet, um die Online-Sicherheit zu verbessern. Ich werde Ihnen Bitwarden vorstellen, und in einem anderen Tutorial werden wir uns eine andere Lösung namens KeePass ansehen.
https://planb.network/tutorials/others/keepass

Warnung: Ein Passwort-Manager ist großartig für die Speicherung von Passwörtern, aber **Sie sollten niemals die mnemonische Phrase Ihres Bitcoin-Wallets darin speichern!** Denken Sie daran, eine mnemonische Phrase sollte ausschließlich in einem physischen Format gespeichert werden, wie einem Stück Papier oder Metall.

## Einführung in Bitwarden

Bitwarden ist ein Passwort-Manager, der sowohl für Anfänger als auch für fortgeschrittene Benutzer geeignet ist. Er bietet zahlreiche Vorteile. Zunächst einmal ist Bitwarden eine Multi-Plattform-Lösung, was bedeutet, dass Sie es als mobile App, Webanwendung, Browsererweiterung und Desktop-Software verwenden können.
![BITWARDEN](assets/notext/01.webp)
Bitwarden ermöglicht es Ihnen, Ihre Passwörter online zu speichern und sie über alle Ihre Geräte hinweg zu synchronisieren, während durch Ihr Master-Passwort eine Ende-zu-Ende-Verschlüsselung gewährleistet wird. Dies ermöglicht es Ihnen beispielsweise, auf Ihre Passwörter sowohl auf Ihrem Computer als auch auf Ihrem Smartphone zuzugreifen, mit Synchronisation zwischen den beiden. Da Ihre Passwörter verschlüsselt sind, bleiben sie für jeden, einschließlich Bitwarden, ohne den Entschlüsselungsschlüssel, der Ihr Master-Passwort ist, unzugänglich.
Darüber hinaus ist Bitwarden Open-Source, was bedeutet, dass die Software von unabhängigen Experten geprüft werden kann. Bezüglich der Preisgestaltung bietet Bitwarden drei Tarife an:
- Eine kostenlose Version, die wir in diesem Tutorial erkunden werden. Obwohl sie kostenlos ist, bietet sie ein Sicherheitsniveau, das den bezahlten Versionen entspricht. Sie können eine unbegrenzte Anzahl von Passwörtern speichern und so viele Geräte synchronisieren, wie Sie möchten;
- Eine Premium-Version für 10 Dollar pro Jahr, die zusätzliche Funktionen wie Dateispeicherung, Kreditkarten-Backup, die Möglichkeit, 2FA mit einem physischen Sicherheitsschlüssel zu konfigurieren, und Zugang zur TOTP 2FA-Authentifizierung direkt mit Bitwarden umfasst;
- Und ein Familienplan für 40 Dollar pro Jahr, der die Vorteile der Premium-Version auf sechs verschiedene Benutzer erweitert.
![BITWARDEN](assets/notext/02.webp)
Meiner Meinung nach sind diese Preise fair. Die kostenlose Version ist eine ausgezeichnete Option für Anfänger, und die Premium-Version bietet im Vergleich zu anderen Passwort-Managern auf dem Markt ein sehr gutes Preis-Leistungs-Verhältnis, während sie mehr Funktionen bietet. Darüber hinaus ist der Umstand, dass Bitwarden Open-Source ist, ein großer Vorteil. Daher ist es ein interessanter Kompromiss, insbesondere für Anfänger.
Eine weitere Funktion von Bitwarden ist die Möglichkeit, Ihren Passwort-Manager selbst zu hosten, wenn Sie beispielsweise ein NAS zu Hause besitzen. Durch das Einrichten dieser Konfiguration werden Ihre Passwörter nicht auf den Servern von Bitwarden gespeichert, sondern auf Ihren eigenen Servern. Dies gibt Ihnen die vollständige Kontrolle über die Verfügbarkeit Ihrer Passwörter. Diese Option erfordert jedoch ein rigoroses Management von Backups, um jeglichen Zugriffsverlust zu vermeiden. Daher ist das Selbsthosting von Bitwarden eher für fortgeschrittene Benutzer geeignet, und wir werden es in einem anderen Tutorial besprechen.
## Wie erstellt man ein Bitwarden-Konto?

Besuchen Sie [die Bitwarden-Website](https://bitwarden.com/) und klicken Sie auf "*Get Started*".
![BITWARDEN](assets/notext/03.webp)
Beginnen Sie, indem Sie Ihre E-Mail-Adresse und Ihren Namen oder Spitznamen eingeben.
![BITWARDEN](assets/notext/04.webp)
Als Nächstes müssen Sie Ihr Master-Passwort einrichten. Wie wir in der Einleitung gesehen haben, ist dieses Passwort sehr wichtig, da es Ihnen Zugang zu allen Ihren anderen gespeicherten Passwörtern im Manager gibt. Es birgt zwei Hauptgefahren: Verlust und Kompromittierung. Wenn Sie den Zugang zu diesem Passwort verlieren, können Sie nicht mehr auf alle Ihre Anmeldedaten zugreifen. Wird Ihr Passwort gestohlen, kann der Angreifer auf alle Ihre Konten zugreifen.

Um das Risiko eines Verlustes zu minimieren, empfehle ich, eine physische Sicherung Ihres Master-Passworts auf Papier zu machen und an einem sicheren Ort aufzubewahren. Wenn möglich, versiegeln Sie diese Sicherung in einem sicheren Umschlag, um regelmäßig sicherzustellen, dass niemand anderes darauf zugegriffen hat.

Um die Kompromittierung Ihres Master-Passworts zu verhindern, muss es extrem robust sein. Es sollte so lang wie möglich sein, eine breite Vielfalt von Zeichen verwenden und zufällig gewählt werden. Im Jahr 2024 lauten die Mindestempfehlungen für ein sicheres Passwort 13 Zeichen, einschließlich Zahlen, Klein- und Großbuchstaben sowie Symbole, vorausgesetzt, das Passwort ist wirklich zufällig. Ich empfehle jedoch, ein Passwort von mindestens 20 Zeichen zu wählen, das alle möglichen Arten von Zeichen umfasst, um seine Sicherheit länger zu gewährleisten.

Geben Sie Ihr Master-Passwort in das dafür vorgesehene Feld ein und bestätigen Sie es im folgenden Feld.
![BITWARDEN](assets/notext/05.webp)
Wenn Sie möchten, können Sie einen Hinweis für Ihr Master-Passwort hinzufügen. Ich rate jedoch davon ab, da der Hinweis keine zuverlässige Methode zur Wiederherstellung im Falle eines Passwortverlustes bietet und sogar Angreifern, die versuchen, Ihr Passwort zu erraten oder per Brute-Force anzugreifen, nützlich sein könnte. Als allgemeine Regel gilt, öffentliche Hinweise zu vermeiden, die die Sicherheit Ihres Master-Passworts gefährden könnten.
![BITWARDEN](assets/notext/06.webp)Klicken Sie dann auf den Button "*Konto erstellen*".
![BITWARDEN](assets/notext/07.webp)
Sie können sich jetzt in Ihr neues Bitwarden-Konto einloggen. Geben Sie Ihre E-Mail-Adresse ein.
![BITWARDEN](assets/notext/08.webp)
Geben Sie dann Ihr Hauptpasswort ein.
![BITWARDEN](assets/notext/09.webp)
Sie befinden sich jetzt in der Web-Oberfläche Ihres Passwort-Managers.
![BITWARDEN](assets/notext/10.webp)
## Wie richtet man Bitwarden ein?

Zunächst werden wir unsere E-Mail-Adresse bestätigen. Klicken Sie auf "*E-Mail senden*".
![BITWARDEN](assets/notext/11.webp)
Klicken Sie dann auf den Button, den Sie per E-Mail erhalten haben.
![BITWARDEN](assets/notext/12.webp)
Loggen Sie sich abschließend erneut ein.
![BITWARDEN](assets/notext/13.webp)
Zuallererst rate ich Ihnen dringend, die Zwei-Faktor-Authentifizierung (2FA) einzurichten, um Ihren Passwort-Manager zu sichern. Sie haben die Wahl zwischen der Verwendung einer TOTP-Anwendung oder eines physischen Sicherheitsschlüssels. Durch die Aktivierung der 2FA wird bei jedem Einloggen in Ihr Bitwarden-Konto nicht nur Ihr Hauptpasswort, sondern auch ein Nachweis Ihres zweiten Authentifizierungsfaktors angefordert. Dies ist eine zusätzliche Sicherheitsebene, die besonders nützlich ist, falls Ihre Papierkopie des Hauptpassworts kompromittiert wird.

Wenn Sie unsicher sind, wie Sie diese 2FA-Geräte einrichten und verwenden, empfehle ich, diesen 2 anderen Tutorials zu folgen:

https://planb.network/tutorials/others/authy

https://planb.network/tutorials/others/security-key

Gehen Sie hierfür zum Reiter "*Sicherheit*" im Menü "*Einstellungen*".
![BITWARDEN](assets/notext/14.webp)
Klicken Sie dann auf den Tab "*Zwei-Schritt-Anmeldung*".
![BITWARDEN](assets/notext/15.webp)
Hier können Sie die 2FA-Methode wählen, die Sie bevorzugen. Ich werde zum Beispiel 2FA mit einer TOTP-Anwendung wählen, indem ich auf den Button "*Verwalten*" klicke.
![BITWARDEN](assets/notext/16.webp)
Bestätigen Sie Ihr Hauptpasswort.
![BITWARDEN](assets/notext/17.webp)
Scannen Sie dann den QR-Code mit Ihrer 2FA-Anwendung.
![BITWARDEN](assets/notext/18.webp)
Geben Sie den 6-stelligen Code ein, den Sie auf Ihrer 2FA-Anwendung notiert haben, und klicken Sie dann auf den Button "*Aktivieren*". ![BITWARDEN](assets/notext/19.webp)
Die Zwei-Faktor-Authentifizierung wurde erfolgreich auf Ihrem Konto eingerichtet.
![BITWARDEN](assets/notext/20.webp)
Wenn Sie nun versuchen, sich erneut in Ihren Manager einzuloggen, müssen Sie zuerst Ihr Hauptpasswort eingeben und dann den 6-stelligen dynamischen Code, der von Ihrer 2FA-Anwendung generiert wurde. Stellen Sie sicher, dass Sie immer Zugang zu diesem dynamischen Code haben; ohne ihn können Sie Ihre Passwörter nicht wiederherstellen.
![BITWARDEN](assets/notext/21.webp)
In den Einstellungen haben Sie auch die Möglichkeit, Ihren Manager im Tab "*Präferenzen*" anzupassen. Hier können Sie die Dauer ändern, bevor Ihr Manager automatisch sperrt, sowie die Sprache und das Thema der Oberfläche.
![BITWARDEN](assets/notext/22.webp)
Ich empfehle dringend, die Länge der von Bitwarden generierten Passwörter anzupassen. Standardmäßig ist die Länge auf 14 Zeichen festgelegt, was für optimale Sicherheit unzureichend sein könnte. Jetzt, da Sie einen Manager haben, der sich all Ihre Passwörter merkt, sollten Sie dies nutzen, um sehr starke Passwörter zu verwenden.
Um dies zu tun, gehen Sie zum Menü "*Generator*". ![BITWARDEN](assets/notext/23.webp)
Hier können Sie den Wert der Passwortlänge auf 40 erhöhen und das Kästchen aktivieren, um Symbole einzuschließen.
![BITWARDEN](assets/notext/24.webp)
## Wie sichern Sie Ihre Konten mit Bitwarden?

Jetzt, wo Ihr Passwort-Manager eingerichtet ist, können Sie beginnen, die Anmeldedaten für Ihre Online-Konten zu speichern. Um einen neuen Eintrag hinzuzufügen, klicken Sie direkt auf den Button "*Neuer Eintrag*" oder auf den Button "*Neu*", der oben rechts auf dem Bildschirm zu finden ist, und dann auf "*Eintrag*".
![BITWARDEN](assets/notext/25.webp)
In dem sich öffnenden Formular beginnen Sie damit, die Art des zu speichernden Eintrags zu bestimmen. Um Anmeldedaten zu speichern, wählen Sie die Option "*Anmeldung*" aus dem Dropdown-Menü.
![BITWARDEN](assets/notext/26.webp)
Im Feld "*Name*" geben Sie einen beschreibenden Namen für Ihre Anmeldedaten ein. Dies erleichtert die Suche und Organisation Ihrer Passwörter, besonders wenn Sie eine große Anzahl haben. Wenn Sie beispielsweise Ihre Anmeldedaten für die PlanB Network-Seite speichern möchten, können Sie diesen Eintrag so benennen, dass er bei zukünftigen Suchen sofort erkennbar ist.
![BITWARDEN](assets/notext/27.webp)
Das Feld "*Ordner*" ermöglicht es Ihnen, Ihre Anmeldedaten in Ordner zu klassifizieren. Im Moment haben wir noch keine erstellt, aber ich werde Ihnen später zeigen, wie das geht.
![BITWARDEN](assets/notext/28.webp)
Im Feld "*Benutzername*" geben Sie Ihren Benutzernamen ein, der in der Regel Ihre E-Mail-Adresse ist. ![BITWARDEN](assets/notext/29.webp)
Als Nächstes können Sie im Feld "*Passwort*" Ihr Passwort eingeben. Ich empfehle jedoch dringend, Bitwarden ein langes, zufälliges und einzigartiges Passwort für Sie generieren zu lassen. Dies stellt sicher, dass Sie ein starkes Passwort haben. Um diese Funktion zu nutzen, klicken Sie auf das Doppelpfeil-Symbol über dem auszufüllenden Feld.
![BITWARDEN](assets/notext/30.webp)
Sie können sehen, dass Ihr Passwort generiert wurde.
![BITWARDEN](assets/notext/31.webp)
Im Feld "*URI 1*" können Sie den Domainnamen der Webseite eingeben.
![BITWARDEN](assets/notext/32.webp)
Und schließlich können Sie im Feld "*Notizen*" bei Bedarf zusätzliche Details hinzufügen.
![BITWARDEN](assets/notext/33.webp)
Wenn Sie alle diese Felder ausgefüllt haben, klicken Sie auf den Button "*Speichern*".
![BITWARDEN](assets/notext/34.webp)
Ihre Anmeldedaten erscheinen nun in Ihrem Bitwarden-Manager.
![BITWARDEN](assets/notext/35.webp)
Durch Anklicken können Sie auf die Details zugreifen und diese ändern.
![BITWARDEN](assets/notext/36.webp)
Durch Klicken auf die drei kleinen Punkte rechts haben Sie schnellen Zugriff, um das Passwort oder den Benutzernamen zu kopieren.
![BITWARDEN](assets/notext/37.webp)
Herzlichen Glückwunsch, Sie haben erfolgreich Ihr erstes Passwort in Ihrem Manager gespeichert! Wenn Sie Ihre Anmeldedaten besser organisieren möchten, können Sie spezifische Ordner erstellen. Dazu klicken Sie auf den Button "*Neu*", der oben rechts auf dem Bildschirm zu finden ist, und wählen dann "*Ordner*".
![BITWARDEN](assets/notext/38.webp)
Geben Sie einen Namen für Ihren Ordner ein.
![BITWARDEN](assets/notext/39.webp)
Dann klicken Sie auf "*Speichern*".
![BITWARDEN](assets/notext/40.webp)
Ihr Ordner erscheint nun in Ihrem Manager.
![BITWARDEN](assets/notext/41.webp) Sie können einem Anmeldeinformation einen Ordner zuweisen, wenn Sie ihn erstellen, wie wir es zuvor getan haben, oder indem Sie eine vorhandene Anmeldeinformation ändern. Zum Beispiel kann ich, indem ich auf meine Anmeldeinformation für das PlanB Network klicke, dann wählen, sie im Ordner "*Bitcoin*" zu klassifizieren.
![BITWARDEN](assets/notext/42.webp)
Auf diese Weise können Sie Ihren Passwort-Manager strukturieren, um es einfacher zu machen, Ihre Anmeldeinformationen zu finden. Sie können sie mit Ordnern wie persönlich, beruflich, Banken, E-Mails, soziale Netzwerke, Abonnements, Einkaufen, Verwaltung, Streaming, Speicherung, Reisen, Gesundheit usw. organisieren.
Wenn Sie es vorziehen, nur die Webversion von Bitwarden zu verwenden, ist es durchaus möglich, dabei zu bleiben. Ich empfehle dann, Ihren Passwort-Manager zu den Favoriten Ihres Browsers hinzuzufügen, um einen einfachen Zugang zu ermöglichen und Phishing-Risiken zu vermeiden. Bitwarden bietet jedoch auch eine vollständige Palette von Clients an, die es Ihnen ermöglichen, Ihren Manager auf verschiedenen Geräten zu verwenden und seine tägliche Nutzung zu vereinfachen. Sie bieten insbesondere eine mobile App, eine Browsererweiterung und Desktop-Software an. Lassen Sie uns sehen, wie wir diese einrichten.

![BITWARDEN](assets/notext/43.webp)
## Wie verwendet man die Bitwarden-Browsererweiterung?

Zuerst können Sie die Browsererweiterung einrichten, wenn Sie möchten. Diese Erweiterung funktioniert als reduzierte Version Ihres Managers und bietet Ihnen die Möglichkeit, automatisch neue Passwörter zu speichern, sichere Passwortvorschläge zu generieren und Ihre Anmeldeinformationen in Anmeldeformularen auf Webseiten automatisch auszufüllen.

Die Verwendung dieser Erweiterung im täglichen Gebrauch ist äußerst praktisch, kann aber auch neue Angriffsvektoren öffnen. Daher raten einige Cybersicherheitsexperten von der Verwendung von Browsererweiterungen für Passwort-Manager ab. Wenn Sie sich jedoch entscheiden, die Bitwarden-Erweiterung zu verwenden, gehen Sie folgendermaßen vor:

Beginnen Sie damit, die [offizielle Bitwarden-Downloadseite](https://bitwarden.com/download/#downloads-web-browser) zu besuchen.
![BITWARDEN](assets/notext/44.webp)
Wählen Sie Ihren Browser aus der bereitgestellten Liste. Für dieses Beispiel verwende ich Firefox, also werde ich zur offiziellen Bitwarden-Erweiterung im Firefox Add-ons Store weitergeleitet. Das Verfahren ist für andere Browser recht ähnlich.
![BITWARDEN](assets/notext/45.webp)
Klicken Sie auf den Button "*Zu Firefox hinzufügen*".
![BITWARDEN](assets/notext/46.webp)
Sie können dann Bitwarden an Ihre Erweiterungsleiste für einen einfachen Zugang anheften. Klicken Sie auf die Erweiterung, um sich anzumelden.
![BITWARDEN](assets/notext/47.webp)
Geben Sie Ihre E-Mail-Adresse ein.
![BITWARDEN](assets/notext/48.webp)
Dann Ihr Master-Passwort.
![BITWARDEN](assets/notext/49.webp)
Und schließlich geben Sie den 6-stelligen Code aus Ihrer Authentifizierungs-App ein.
![BITWARDEN](assets/notext/50.webp)
Sie sind jetzt über die Browsererweiterung mit Ihrem Bitwarden-Manager verbunden.
![BITWARDEN](assets/notext/51.webp)
Wenn ich zum Beispiel zur PlanB Network-Seite zurückgehe und versuche, mich in meinem Konto anzumelden, können Sie sehen, dass die in den Browser integrierte Bitwarden-Erweiterung die Anmeldefelder erkennt und mir automatisch anbietet, den zuvor gespeicherten Identifikator auszuwählen.
![BITWARDEN](assets/notext/52.webp)
Wenn ich diesen Identifikator auswähle, füllt Bitwarden die Anmeldefelder für mich aus. Diese Funktion der Erweiterung ermöglicht eine schnelle Verbindung zu Websites, ohne die Anmeldeinformationen aus der Bitwarden-Webanwendung oder Software kopieren und einfügen zu müssen. ![BITWARDEN](assets/notext/53.webp) Die Erweiterung ist auch darauf ausgelegt, die Erstellung neuer Konten zu erkennen. Zum Beispiel, wenn ein neues Konto im PlanB-Netzwerk erstellt wird, schlägt Bitwarden automatisch vor, den neuen Identifikator zu speichern. ![BITWARDEN](assets/notext/54.webp) Durch Klicken auf diesen Vorschlag, der erscheint, öffnet sich die Erweiterung. Sie ermöglicht es mir, die Details des neuen Identifikators einzugeben und ein starkes, einzigartiges Passwort zu generieren. ![BITWARDEN](assets/notext/55.webp) Nachdem die Informationen vervollständigt und auf "*Speichern*" geklickt wurde, speichert die Erweiterung die Anmeldeinformationen. ![BITWARDEN](assets/notext/56.webp) Anschließend fügt die Erweiterung automatisch unsere Anmeldeinformationen in die entsprechenden Felder auf der Website ein. ![BITWARDEN](assets/notext/57.webp) ## Wie verwendet man die Bitwarden-Software?
Um die Bitwarden-Desktopsoftware zu installieren, beginnen Sie damit, [die Download-Seite](https://bitwarden.com/download/#downloads-desktop) zu besuchen. Wählen und laden Sie die Version herunter, die Ihrem Betriebssystem entspricht. ![BITWARDEN](assets/notext/58.webp) Sobald der Download abgeschlossen ist, fahren Sie mit der Installation der Software auf Ihrem Computer fort. Beim ersten Start der Bitwarden-Software müssen Sie Ihre Anmeldeinformationen eingeben, um Ihren Passwortmanager freizuschalten. ![BITWARDEN](assets/notext/59.webp) Dann gelangen Sie zur Startseite Ihres Managers. Die Schnittstelle ist fast identisch mit der der Webanwendung. ![BITWARDEN](assets/notext/60.webp) ## Wie verwendet man die Bitwarden-App?

Um auf Ihre Passwörter von Ihrem Telefon aus zuzugreifen, können Sie die Bitwarden-Mobil-App installieren. Beginnen Sie damit, [die Download-Seite](https://bitwarden.com/download/#downloads-mobile) zu besuchen und verwenden Sie Ihr Smartphone, um den QR-Code zu scannen, der Ihrem Betriebssystem entspricht. ![BITWARDEN](assets/notext/61.webp) Laden Sie die offizielle Bitwarden-Mobil-App herunter und installieren Sie sie. Beim ersten Öffnen der App geben Sie Ihre Anmeldeinformationen ein, um den Zugang zu Ihrem Passwortmanager freizuschalten. ![BITWARDEN](assets/notext/62.webp) Einmal verbunden, können Sie alle Ihre Passwörter direkt aus der App heraus konsultieren und verwalten. ![BITWARDEN](assets/notext/63.webp) Um die Sicherheit Ihrer App zu erhöhen, rate ich dazu, in den Einstellungen den PIN-Schutz zu aktivieren. Dies fügt eine zusätzliche Sicherheitsebene im Falle eines Verlusts oder Diebstahls Ihres Telefons hinzu. ![BITWARDEN](assets/notext/64.webp) ## Wie sichert man Bitwarden?
Um sicherzustellen, dass Sie niemals den Zugang zu Ihren Passwörtern verlieren, selbst im Falle des Verlusts Ihres Hauptpassworts oder eines Desasters, das Bitwardens Server betrifft, rate ich Ihnen, regelmäßig ein verschlüsseltes Backup Ihres Managers auf einem externen Medium durchzuführen.

Die Idee ist, alle Ihre Bitwarden-Anmeldeinformationen mit einem Passwort zu verschlüsseln, das sich von Ihrem Hauptpasswort unterscheidet, und dieses verschlüsselte Backup auf einem USB-Stick oder einer Festplatte zu speichern, die Sie beispielsweise zu Hause aufbewahren. Sie können dann eine physische Kopie des Entschlüsselungspassworts an einem separaten Ort aufbewahren, wo das Backup-Medium gelagert ist. Beispielsweise könnten Sie den USB-Stick zu Hause aufbewahren und die physische Kopie des Verschlüsselungspassworts einem vertrauenswürdigen Freund anvertrauen.

Diese Methode stellt sicher, dass selbst wenn Ihr Backup-Medium gestohlen wird, Ihre Daten ohne das Entschlüsselungspasswort unzugänglich bleiben. Ebenso wird Ihr Freund ohne das physische Medium nicht auf Ihre Daten zugreifen können.
Sollten Sie jedoch auf ein Problem stoßen, können Sie das Passwort und das externe Medium nutzen, um unabhängig von Bitwarden wieder Zugang zu Ihren Anmeldeinformationen zu erhalten. Selbst wenn die Server von Bitwarden zerstört werden sollten, hätten Sie immer noch die Möglichkeit, Ihre Passwörter wiederherzustellen.
Daher rate ich Ihnen, diese Backups regelmäßig durchzuführen, damit sie stets Ihre neuesten Anmeldeinformationen enthalten. Um Ihren Freund, der eine Kopie des Verschlüsselungspassworts besitzt, bei jedem neuen Backup nicht zu belästigen, können Sie dieses Passwort in Ihrem Passwortmanager speichern. Dies ist nicht als Backup gedacht, da Ihr Freund bereits eine physische Kopie besitzt, sondern soll Ihre zukünftigen Exportverfahren vereinfachen.

Um mit dem Export fortzufahren, ist es ganz einfach: Gehen Sie zum Abschnitt "*Tools*" Ihres Bitwarden-Managers und wählen Sie "*Export vault*".
![BITWARDEN](assets/notext/65.webp)
Wählen Sie als Format "*.json (Verschlüsselt)*".
![BITWARDEN](assets/notext/66.webp)
Wählen Sie dann die Option "*Passwortgeschützt*".
![BITWARDEN](assets/notext/67.webp)
Hier ist es wichtig, ein starkes, einzigartiges und zufällig generiertes Passwort zur Verschlüsselung des Backups zu wählen. Dies stellt sicher, dass es selbst im Falle eines Diebstahls Ihres verschlüsselten Backups für einen Angreifer unmöglich wäre, es durch Brute-Force zu entschlüsseln.
![BITWARDEN](assets/notext/68.webp)
Klicken Sie auf "*Format bestätigen*" und geben Sie Ihr Hauptpasswort ein, um mit dem Export fortzufahren.
![BITWARDEN](assets/notext/69.webp)
Sobald der Export abgeschlossen ist, finden Sie Ihre verschlüsselte Backup-Datei in Ihren Downloads. Übertragen Sie sie auf ein sicheres externes Speichermedium, wie einen USB-Stick oder eine Festplatte. Wiederholen Sie diesen Vorgang regelmäßig, je nach Ihrem Bedarf. Sie können beispielsweise das Backup jede Woche oder jeden Monat erneuern, je nach Ihren Bedürfnissen.