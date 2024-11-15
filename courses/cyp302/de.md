---
name: Einführung in die formale Kryptographie
goal: Eine tiefgehende Einführung in die Wissenschaft und Praxis der Kryptographie.
objectives:
  - Erkundung von Beale-Chiffren und modernen kryptografischen Methoden, um grundlegende und historische Konzepte der Kryptographie zu verstehen.
  - Vertiefung in Zahlentheorie, Gruppen und Felder, um Schlüsselkonzepte der Mathematik, die der Kryptographie zugrunde liegen, zu meistern.
  - Studium des RC4-Stream-Ciphers und AES mit einem 128-Bit-Schlüssel, um symmetrische kryptografische Algorithmen kennenzulernen.
  - Untersuchung des RSA-Kryptosystems, Schlüsselverteilung und Hash-Funktionen, um asymmetrische Kryptographie zu erkunden.

---
# Tiefgehender Einblick in die Kryptographie

Es ist schwierig, viele Materialien zu finden, die einen guten Mittelweg in der Kryptographieausbildung bieten.

Einerseits gibt es umfangreiche, formale Abhandlungen, die wirklich nur für diejenigen zugänglich sind, die eine starke Grundlage in Mathematik, Logik oder einer anderen formalen Disziplin haben. Andererseits gibt es sehr allgemeine Einführungen, die wirklich zu viele Details für jeden verbergen, der zumindest ein wenig neugierig ist.

Diese Einführung in die Kryptographie sucht den Mittelweg zu erfassen. Obwohl sie für jeden, der neu in der Kryptographie ist, relativ herausfordernd und detailliert sein sollte, ist es nicht das Kaninchenloch einer typischen grundlegenden Abhandlung.

+++

# Einführung
<partId>bbed2f46-d64c-5fb5-b892-d726032f2494</partId>

## Kurzbeschreibung
<chapterId>bb8a8b73-7fb2-50da-bf4e-98996d79887b</chapterId>

Dieses Buch bietet eine tiefgehende Einführung in die Wissenschaft und Praxis der Kryptographie. Wo möglich konzentriert es sich auf konzeptionelle, anstatt formale Darstellung des Materials.

> Dieser Kurs basiert auf [JWBurgers's Repo](https://github.com/JWBurgers/An_Introduction_to_Cryptography). Alle Rechte bei ihm. Der Inhalt ist noch nicht fertig und dient nur dazu zu zeigen, wie wir ihn integrieren könnten, wenn JWburger zustimmt.

### Motivation und Ziele

Es ist schwierig, viele Materialien zu finden, die einen guten Mittelweg in der Kryptographieausbildung bieten.

Einerseits gibt es umfangreiche, formale Abhandlungen, die wirklich nur für diejenigen zugänglich sind, die eine starke Grundlage in Mathematik, Logik oder einer anderen formalen Disziplin haben. Andererseits gibt es sehr allgemeine Einführungen, die wirklich zu viele Details für jeden verbergen, der zumindest ein wenig neugierig ist.

Diese Einführung in die Kryptographie sucht den Mittelweg zu erfassen. Obwohl sie für jeden, der neu in der Kryptographie ist, relativ herausfordernd und detailliert sein sollte, ist es nicht das Kaninchenloch einer typischen grundlegenden Abhandlung.

### Zielgruppe

Von Entwicklern bis zu intellektuell Neugierigen ist dieses Buch für jeden nützlich, der mehr als ein oberflächliches Verständnis der Kryptographie wünscht. Wenn Ihr Ziel ist, das Feld der Kryptographie zu meistern, dann ist dieses Buch auch ein guter Ausgangspunkt.

### Leseanleitung

Das Buch enthält derzeit sieben Kapitel: "Was ist Kryptographie?" (Kapitel 1), "Mathematische Grundlagen der Kryptographie I" (Kapitel 2), "Mathematische Grundlagen der Kryptographie II" (Kapitel 3), "Symmetrische Kryptographie" (Kapitel 4), "RC4 und AES" (Kapitel 5), "Asymmetrische Kryptographie" (Kapitel 6) und "Das RSA-Kryptosystem" (Kapitel 7). Ein abschließendes Kapitel, "Kryptographie in der Praxis", wird noch hinzugefügt. Es konzentriert sich auf verschiedene kryptografische Anwendungen, einschließlich Transportschichtsicherheit, Onion-Routing und dem Wertaustauschsystem von Bitcoin.
Sofern Sie keinen starken Hintergrund in Mathematik haben, ist die Zahlentheorie wahrscheinlich das schwierigste Thema in diesem Buch. Ich biete einen Überblick darüber in Kapitel 3, und sie erscheint auch in der Darstellung von AES in Kapitel 5 und dem RSA-Kryptosystem in Kapitel 7.
Wenn Sie wirklich mit den formalen Details in diesen Teilen des Buches kämpfen, empfehle ich Ihnen, sich beim ersten Mal mit einer hochrangigen Lektüre zufriedenzugeben.

### Danksagungen

Das einflussreichste Buch bei der Gestaltung dieses Werkes war Jonathan Katz und Yehuda Lindells _Einführung in die moderne Kryptographie_, CRC Press (Boca Raton, FL), 2015. Ein begleitender Kurs ist auf Coursera verfügbar und heißt "Kryptographie".

Die wichtigsten zusätzlichen Quellen, die bei der Erstellung des Überblicks in diesem Buch hilfreich waren, sind Simon Singh, _Das Geheimnis der Codes_, Fourth Estate (London, 1999); Christof Paar und Jan Pelzl, _Verständnis der Kryptographie_, Springer (Heidelberg, 2010) und [ein auf dem Buch von Paar basierender Kurs namens „Einführung in die Kryptographie“](https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg); sowie Bruce Schneier, Angewandte Kryptographie, 2. Aufl., 2015 (Indianapolis, IN: John Wiley & Sons).

Ich werde nur sehr spezifische Informationen und Ergebnisse aus diesen Quellen zitieren, möchte aber hier meine allgemeine Dankbarkeit ihnen gegenüber zum Ausdruck bringen.

Für diejenigen Leser, die nach dieser Einführung weiterführendes Wissen über Kryptographie suchen, empfehle ich dringend das Buch von Katz und Lindell. Katzs Kurs auf Coursera ist etwas zugänglicher als das Buch.

### Beiträge

Bitte werfen Sie einen Blick auf [die Beitragsdatei im Repository](https://github.com/JWBurgers/An_Introduction_to_Cryptography/blob/master/Contributions.md) für einige Richtlinien, wie Sie das Projekt unterstützen können.

### Notation

**Schlüsselbegriffe:**

Schlüsselbegriffe in den Grundlagen werden durch Fettdruck eingeführt. Zum Beispiel würde die Einführung des Rijndael-Ziphers als Schlüsselbegriff folgendermaßen aussehen: **Rijndael-Zipher**.

Schlüsselbegriffe werden explizit definiert, es sei denn, es handelt sich um Eigennamen oder ihre Bedeutung ist aus der Diskussion offensichtlich.

Eine Definition wird normalerweise bei der Einführung eines Schlüsselbegriffs gegeben, obwohl es manchmal bequemer ist, die Definition bis zu einem späteren Zeitpunkt aufzuschieben.

**Hervorgehobene Wörter und Phrasen:**

Wörter und Phrasen werden durch Kursivschrift hervorgehoben. Zum Beispiel würde die Phrase "Merke dir dein Passwort" folgendermaßen aussehen: *Merke dir dein Passwort*.

**Formale Notation:**

Die formale Notation betrifft hauptsächlich Variablen, Zufallsvariablen und Mengen.

* Variablen: Diese werden normalerweise einfach durch einen Kleinbuchstaben angezeigt (z.B. "x" oder "y"). Manchmal werden sie zur Klarheit großgeschrieben (z.B. "M" oder "K").
* Zufallsvariablen: Diese werden immer durch einen Großbuchstaben angezeigt (z.B. "X" oder "Y")
* Mengen: Diese werden immer durch fette, großgeschriebene Buchstaben angezeigt (z.B. **S**)

# Was ist Kryptographie?
<partId>48e4d6d5-cd00-5c00-8adb-ae8477ff47c4</partId>

## Die Beale-Chiffren
<chapterId>ae674346-4789-5ab1-9b6f-c8989d83be89</chapterId>
Lassen Sie uns unsere Untersuchung im Bereich der Kryptographie mit einer der charmantesten und unterhaltsamsten Episoden ihrer Geschichte beginnen: der der Beale-Chiffren. [1]
Die Geschichte der Beale-Chiffren ist meiner Meinung nach eher Fiktion als Realität. Aber sie soll sich folgendermaßen zugetragen haben.

Sowohl im Winter 1820 als auch 1822 übernachtete ein Mann namens Thomas J. Beale in einer Herberge, die Robert Morriss in Lynchburg (Virginia) gehörte. Am Ende von Beales zweitem Aufenthalt übergab er Morriss eine eiserne Kiste mit wertvollen Papieren zur Aufbewahrung.

Einige Monate später erhielt Morriss einen Brief von Beale, datiert auf den 9. Mai 1822. Darin betonte er den großen Wert des Inhalts der eisernen Kiste und erteilte Morriss einige Anweisungen: Falls weder Beale noch einer seiner Gefährten jemals kämen, um die Kiste zu beanspruchen, sollte er sie genau zehn Jahre nach dem Datum des Briefes (also am 9. Mai 1832) öffnen. Einige der Papiere im Inneren wären in normalem Text geschrieben. Mehrere andere jedoch wären „unverständlich ohne die Hilfe eines Schlüssels“. Dieser „Schlüssel“ würde dann im Juni 1832 von einem ungenannten Freund Beales an Morriss übergeben werden.

Trotz der klaren Anweisungen öffnete Morriss die Kiste im Mai 1832 nicht und der geheimnisvolle Freund Beales tauchte im Juni jenes Jahres nicht auf. Erst 1845 entschied sich der Gastwirt schließlich, die Kiste zu öffnen. Darin fand Morriss einen Zettel, der erklärte, wie Beale und seine Gefährten im Westen Gold und Silber entdeckt und es zusammen mit einigen Schmuckstücken zur sicheren Aufbewahrung vergraben hatten. Zusätzlich enthielt die Kiste drei **Chiffretexte**: das heißt, Texte, die in einem Code geschrieben sind und einen **kryptographischen Schlüssel** oder ein Geheimnis sowie einen begleitenden Algorithmus zur Entschlüsselung benötigen. Dieser Prozess des Entsperrens eines Chiffretexts ist als **Entschlüsselung** bekannt, während der Verschlüsselungsprozess als **Verschlüsselung** bezeichnet wird. (Wie in Kapitel 3 erklärt, kann der Begriff Chiffre verschiedene Bedeutungen annehmen. Im Namen "Beale-Chiffren" steht er kurz für Chiffretexte.)

Die drei Chiffretexte, die Morriss in der eisernen Kiste fand, bestehen jeweils aus einer Reihe von Zahlen, getrennt durch Kommas. Laut Beales Notiz geben diese Chiffretexte separat den Standort des Schatzes, den Inhalt des Schatzes und eine Liste von Namen mit rechtmäßigen Erben des Schatzes und ihren Anteilen an (letztere Information ist relevant, falls Beale und seine Gefährten die Kiste nie beanspruchen würden).

Morris versuchte zwanzig Jahre lang, die drei Chiffretexte zu entschlüsseln. Dies wäre mit dem Schlüssel einfach gewesen. Aber Morriss hatte den Schlüssel nicht und scheiterte bei seinen Versuchen, die Originaltexte oder **Klartexte**, wie sie in der Kryptographie typischerweise genannt werden, wiederherzustellen.

Gegen Ende seines Lebens übergab Morriss die Kiste 1862 an einen Freund. Dieser Freund veröffentlichte anschließend 1885 unter dem Pseudonym J.B. Ward eine Broschüre. Sie enthielt eine Beschreibung der (angeblichen) Geschichte der Kiste, der drei Chiffretexte und einer Lösung, die er für den zweiten Chiffretext gefunden hatte. (Anscheinend gibt es einen Schlüssel für jeden Chiffretext und nicht einen Schlüssel, der auf alle drei Chiffretexte funktioniert, wie Beale in seinem Brief an Morriss ursprünglich zu suggerieren schien.)

Sie können den zweiten Chiffretext in *Abbildung 2* unten sehen. [2] Der Schlüssel zu diesem Chiffretext ist die Unabhängigkeitserklärung der Vereinigten Staaten. Das Entschlüsselungsverfahren basiert auf der Anwendung der folgenden zwei Regeln:
* Für jede Zahl n im Chiffretext, suchen Sie das n-te Wort in der Unabhängigkeitserklärung der Vereinigten Staaten* Ersetzen Sie die Zahl n durch den ersten Buchstaben des gefundenen Wortes

*Abbildung 1: Beale-Chiffre Nr. 2*

![Abbildung 1: Beale-Chiffre Nr. 2](assets/Figure1-1.webp "Abbildung 1: Beale-Chiffre Nr. 2")

Zum Beispiel ist die erste Zahl des zweiten Chiffretexts 115. Das 115. Wort der Unabhängigkeitserklärung ist „instituted“, also ist der erste Buchstabe des Klartextes „i“. Der Chiffretext gibt Wortabstände und Großschreibung nicht direkt an. Aber nachdem die ersten paar Wörter entschlüsselt wurden, kann man logisch ableiten, dass das erste Wort des Klartextes einfach „I“ war. (Der Klartext beginnt mit der Phrase „I have deposited in the county of Bedford.“)

Nach der Entschlüsselung liefert die zweite Nachricht detaillierte Inhalte über den Schatz (Gold, Silber und Juwelen) und deutet darauf hin, dass er in eisernen Töpfen begraben und mit Steinen in Bedford County (Virginia) bedeckt wurde. Menschen lieben ein gutes Mysterium, daher wurden große Anstrengungen unternommen, um die anderen beiden Beale-Chiffren zu entschlüsseln, insbesondere die, die den Standort des Schatzes beschreibt. Selbst verschiedene prominente Kryptographen haben sich daran versucht. Bis jetzt konnte jedoch niemand die anderen beiden Chiffretexte entschlüsseln.

**Anmerkungen:**

[1] Für eine gute Zusammenfassung der Geschichte siehe Simon Singh, *Das Buch der Codes*, Fourth Estate (London, 1999), S. 82-99. Ein Kurzfilm der Geschichte wurde 2010 von Andrew Allen gemacht. Den Film, „The Thomas Beale Cipher“, finden Sie [auf seiner Webseite](http://www.thomasbealecipher.com/).

[2] Dieses Bild ist auf der Wikipedia-Seite für die Beale-Chiffren verfügbar.

## Moderne Kryptographie
<chapterId>d07d576f-8a4b-5890-b182-2e5763f550f4</chapterId>

Farbenfrohe Geschichten wie die der Beale-Chiffren sind das, was die meisten von uns mit Kryptographie verbinden. Doch die moderne Kryptographie unterscheidet sich in mindestens vier wichtigen Punkten von diesen Arten historischer Beispiele.

Erstens war die Kryptographie historisch gesehen nur mit **Geheimhaltung** (oder Vertraulichkeit) beschäftigt. [3] Chiffretexte wurden erstellt, um sicherzustellen, dass nur bestimmte Parteien Zugang zu den Informationen in den Klartexten hatten, wie im Fall der Beale-Chiffren. Damit ein Verschlüsselungsschema diesen Zweck gut erfüllt, sollte das Entschlüsseln des Chiffretexts nur möglich sein, wenn man den Schlüssel hat.

Die moderne Kryptographie beschäftigt sich mit einem breiteren Spektrum an Themen als nur Geheimhaltung. Diese Themen umfassen primär (1) **Nachrichtenintegrität**—das heißt, die Sicherstellung, dass eine Nachricht nicht verändert wurde; (2) **Nachrichtenauthentizität**—das heißt, die Sicherstellung, dass eine Nachricht wirklich von einem bestimmten Sender stammt; und (3) **Nichtabstreitbarkeit**—das heißt, die Sicherstellung, dass ein Sender später nicht fälschlicherweise leugnen kann, eine Nachricht gesendet zu haben. [4]

Ein wichtiger Unterschied, den man im Kopf behalten sollte, ist also zwischen einem **Verschlüsselungsschema** und einem **kryptographischen Schema**. Ein Verschlüsselungsschema beschäftigt sich nur mit Geheimhaltung. Während ein Verschlüsselungsschema ein kryptographisches Schema ist, ist das Gegenteil nicht wahr. Ein kryptographisches Schema kann auch den anderen Hauptthemen der Kryptographie dienen, einschließlich Integrität, Authentizität und Nichtabstreitbarkeit.
Die Themen Integrität und Authentizität sind genauso wichtig wie Geheimhaltung. Unsere modernen Kommunikationssysteme könnten ohne Garantien bezüglich der Integrität und Authentizität von Kommunikationen nicht funktionieren. Auch die Nichtabstreitbarkeit ist eine wichtige Sorge, wie zum Beispiel bei digitalen Verträgen, aber weniger allgegenwärtig benötigt in kryptografischen Anwendungen als Geheimhaltung, Integrität und Authentizität.

Zweitens beinhalten klassische Verschlüsselungsschemata wie die Beale-Chiffren immer einen Schlüssel, der unter allen relevanten Parteien geteilt wurde. Viele moderne kryptografische Schemata beinhalten jedoch nicht nur einen, sondern zwei Schlüssel: einen **privaten** und einen **öffentlichen Schlüssel**. Während der erstere in allen Anwendungen privat bleiben sollte, ist der letztere typischerweise öffentlich bekannt (daher ihre jeweiligen Namen). Im Bereich der Verschlüsselung kann der öffentliche Schlüssel zur Verschlüsselung der Nachricht verwendet werden, während der private Schlüssel zur Entschlüsselung verwendet werden kann.

Der Zweig der Kryptografie, der sich mit Schemata befasst, bei denen alle Parteien einen Schlüssel teilen, ist als **symmetrische Kryptografie** bekannt. Der einzelne Schlüssel in einem solchen Schema wird üblicherweise als **privater Schlüssel** (oder Geheimschlüssel) bezeichnet. Der Zweig der Kryptografie, der sich mit Schemata befasst, die ein privates-öffentliches Schlüsselpaar erfordern, ist als **asymmetrische Kryptografie** bekannt. Diese Zweige werden manchmal auch als **Private-Key-Kryptografie** und **Public-Key-Kryptografie** bezeichnet, obwohl dies Verwirrung stiften kann, da öffentliche Schlüsselkryptografieschemata auch private Schlüssel haben.

Das Aufkommen der asymmetrischen Kryptografie Ende der 1970er Jahre war eines der wichtigsten Ereignisse in der Geschichte der Kryptografie. Ohne sie wären die meisten unserer modernen Kommunikationssysteme, einschließlich Bitcoin, nicht möglich oder zumindest sehr unpraktisch.

Wichtig ist, dass die moderne Kryptografie nicht ausschließlich das Studium von symmetrischen und asymmetrischen Schlüsselkryptografieschemata ist (obwohl das einen Großteil des Feldes abdeckt). Zum Beispiel befasst sich die Kryptografie auch mit Hash-Funktionen und Pseudozufallszahlgeneratoren, und man kann Anwendungen auf diesen Primitiven aufbauen, die nicht mit symmetrischer oder asymmetrischer Schlüsselkryptografie zusammenhängen.

Drittens waren klassische Verschlüsselungsschemata, wie die bei den Beale-Chiffren verwendeten, mehr Kunst als Wissenschaft. Ihre wahrgenommene Sicherheit basierte weitgehend auf Intuitionen bezüglich ihrer Komplexität. Typischerweise wurden sie gepatcht, wenn ein neuer Angriff auf sie gelernt wurde, oder ganz fallen gelassen, wenn der Angriff besonders schwerwiegend war. Die moderne Kryptografie hingegen ist eine strenge Wissenschaft mit einem formalen, mathematischen Ansatz sowohl für die Entwicklung als auch für die Analyse kryptografischer Schemata.

Insbesondere konzentriert sich die moderne Kryptografie auf formale **Sicherheitsbeweise**. Jeder Sicherheitsbeweis für ein kryptografisches Schema erfolgt in drei Schritten:

1. Die Aussage einer **kryptografischen Definition von Sicherheit**, das heißt, ein Satz von Sicherheitszielen und die durch den Angreifer dargestellte Bedrohung.
2. Die Aussage aller mathematischen Annahmen in Bezug auf die Rechenkomplexität des Schemas. Zum Beispiel kann ein kryptografisches Schema einen Pseudozufallszahlgenerator enthalten. Obwohl wir nicht beweisen können, dass diese existieren, können wir annehmen, dass sie es tun.
3. Die Darstellung eines mathematischen **Sicherheitsbeweises** des Schemas auf der Grundlage der formalen Sicherheitsvorstellung und aller mathematischen Annahmen.

Viertens, während Kryptografie historisch gesehen hauptsächlich in militärischen Einstellungen genutzt wurde, hat sie in unserem täglichen Leben im digitalen Zeitalter allgegenwärtig geworden. Ob Sie online Bankgeschäfte tätigen, in sozialen Medien posten, ein Produkt bei Amazon mit Ihrer Kreditkarte kaufen oder einem Freund Bitcoin geben, Kryptografie ist das sine qua non unseres digitalen Zeitalters.

Angesichts dieser vier Aspekte der modernen Kryptografie könnten wir die moderne **Kryptografie** als die Wissenschaft charakterisieren, die sich mit der formalen Entwicklung und Analyse kryptografischer Schemata zur Sicherung digitaler Informationen gegen feindliche Angriffe befasst. Sicherheit sollte hier im weitesten Sinne verstanden werden als die Verhinderung von Angriffen, die Geheimhaltung, Integrität, Authentifizierung und/oder Nichtabstreitbarkeit in Kommunikationen schädigen.
Kryptografie wird am besten als eine Unterdisziplin der **Cybersicherheit** angesehen, die sich mit der Verhinderung von Diebstahl, Beschädigung und Missbrauch von Computersystemen befasst. Beachten Sie, dass viele Bedenken hinsichtlich der Cybersicherheit wenig oder nur teilweise mit Kryptografie zusammenhängen.
Wenn beispielsweise ein Unternehmen teure Server lokal vorhält, könnte es darum besorgt sein, diese Hardware vor Diebstahl und Beschädigung zu sichern. Obwohl dies ein Anliegen der Cybersicherheit ist, hat es wenig mit Kryptografie zu tun.

Als weiteres Beispiel sind **Phishing-Angriffe** ein häufiges Problem in unserer modernen Zeit. Diese Angriffe versuchen, Menschen über eine E-Mail oder ein anderes Nachrichtenmedium zu täuschen, um sensible Informationen wie Passwörter oder Kreditkartennummern preiszugeben. Obwohl Kryptografie dazu beitragen kann, Phishing-Angriffe bis zu einem gewissen Grad anzugehen, erfordert ein umfassender Ansatz mehr als nur die Verwendung von etwas Kryptografie.

**Notizen:**

[3] Um genau zu sein, waren die wichtigen Anwendungen kryptografischer Schemata mit Geheimhaltung beschäftigt. Kinder verwenden beispielsweise häufig einfache kryptografische Schemata zum „Spaß“. Geheimhaltung ist in diesen Fällen eigentlich kein Anliegen.

[4] Bruce Schneier, *Applied Cryptography*, 2. Auflage, 2015 (Indianapolis, IN: John Wiley & Sons), S. 2.

[5] Siehe Jonathan Katz und Yehuda Lindell, *Introduction to Modern Cryptography*, CRC Press (Boca Raton, FL: 2015), insbes. S. 16–23, für eine gute Beschreibung.

[6] Vgl. Katz und Lindell, ebenda, S. 3. Ich denke, ihre Charakterisierung hat einige Probleme, daher präsentiere ich hier eine leicht abweichende Version ihrer Aussage.

## Offene Kommunikation
<chapterId>cb23d0a6-ba9a-5dc6-a55a-258405ae4117</chapterId>

Die moderne Kryptografie ist darauf ausgelegt, Sicherheitszusagen in einer **offenen Kommunikations**umgebung zu bieten. Wenn unser Kommunikationskanal so gut geschützt ist, dass Lauscher keine Chance haben, unsere Nachrichten zu manipulieren oder auch nur zu beobachten, dann ist Kryptografie überflüssig. Die meisten unserer Kommunikationskanäle sind jedoch kaum so gut bewacht.

Das Rückgrat der Kommunikation in der modernen Welt ist ein riesiges Netzwerk aus Glasfaserkabeln. Telefonate führen, Fernsehen schauen und im Web surfen in einem modernen Haushalt basiert im Allgemeinen auf diesem Netzwerk aus Glasfaserkabeln (ein kleiner Prozentsatz könnte rein auf Satelliten basieren). Es ist wahr, dass Sie in Ihrem Zuhause unterschiedliche Datenverbindungen haben könnten, wie Koaxialkabel, (asymmetrische) digitale Teilnehmeranschlussleitung und Glasfaserkabel. Aber zumindest in der entwickelten Welt schließen sich diese verschiedenen Datenmedien schnell außerhalb Ihres Hauses an einem Knotenpunkt in einem riesigen Netzwerk aus Glasfaserkabeln an, das den gesamten Globus verbindet. Ausnahmen sind einige abgelegene Gebiete der entwickelten Welt, wie in den Vereinigten Staaten und Australien, wo der Datenverkehr immer noch auch über erhebliche Entfernungen über traditionelle Kupfertelefonleitungen reisen könnte.

Es wäre unmöglich, potenziellen Angreifern den physischen Zugang zu diesem Netzwerk von Kabeln und seiner unterstützenden Infrastruktur zu verwehren. Tatsächlich wissen wir bereits, dass die meisten unserer Daten von verschiedenen nationalen Geheimdiensten an entscheidenden Schnittstellen des Internets abgefangen werden.[7] Dies umfasst alles von Facebook-Nachrichten bis zu den Website-Adressen, die Sie besuchen.

Obwohl die Überwachung von Daten in großem Maßstab einen mächtigen Gegner, wie eine nationale Geheimdienstbehörde, erfordert, können Angreifer mit nur wenigen Ressourcen leicht versuchen, auf lokaler Ebene zu schnüffeln. Obwohl dies auf der Ebene des Abhörens von Leitungen geschehen kann, ist es weitaus einfacher, einfach drahtlose Kommunikation abzufangen.
Die meisten unserer lokalen Netzwerkdaten – ob zu Hause, im Büro oder in einem Café – reisen jetzt über Funkwellen zu drahtlosen Zugangspunkten auf All-in-One-Routern, anstatt durch physische Kabel. Ein Angreifer benötigt daher nur wenig Ressourcen, um jeglichen lokalen Datenverkehr abzufangen. Dies ist besonders besorgniserregend, da die meisten Menschen sehr wenig tun, um die Daten zu schützen, die über ihre lokalen Netzwerke reisen. Darüber hinaus können potenzielle Angreifer auch unsere mobilen Breitbandverbindungen, wie 3G, 4G und 5G, ins Visier nehmen. All diese drahtlosen Kommunikationen sind ein leichtes Ziel für Angreifer.

Daher ist die Idee, die Kommunikation geheim zu halten, indem der Kommunikationskanal geschützt wird, für einen großen Teil der modernen Welt eine hoffnungslos illusorische Vorstellung. Alles, was wir wissen, rechtfertigt schwere Paranoia: Man sollte immer davon ausgehen, dass jemand zuhört. Und Kryptographie ist das Hauptwerkzeug, das wir haben, um in dieser modernen Umgebung irgendeine Art von Sicherheit zu erlangen.

**Notizen:**

[7] Siehe zum Beispiel Olga Khazan, „Die gruselige, langjährige Praxis des Abhörens von Unterseekabeln“, *The Atlantic*, 16. Juli 2013 (verfügbar unter [The Atlantic](https://www.theatlantic.com/international/archive/2013/07/the-creepy-long-standing-practice-of-undersea-cable-tapping/277855/)).

# Mathematische Grundlagen der Kryptographie 1
<partId>1bf9f0aa-0f68-5493-83fb-2167238ff9de</partId>

## Zufallsvariablen
<chapterId>b623a7d0-3dff-5803-bd4e-8257ff73dd69</chapterId>

Die Kryptographie stützt sich auf Mathematik. Und wenn man mehr als ein oberflächliches Verständnis von Kryptographie aufbauen möchte, muss man mit dieser Mathematik vertraut sein.

Dieses Kapitel führt die meisten der grundlegenden Mathematik ein, auf die man beim Erlernen der Kryptographie stoßen wird. Die Themen umfassen Zufallsvariablen, Modulo-Operationen, XOR-Operationen und Pseudozufälligkeit. Man sollte das Material in diesen Abschnitten beherrschen, um ein nicht-oberflächliches Verständnis der Kryptographie zu erlangen.

Der nächste Abschnitt befasst sich mit der Zahlentheorie, die viel herausfordernder ist.

### Zufallsvariablen

Eine Zufallsvariable wird typischerweise durch einen nicht fettgedruckten, Großbuchstaben dargestellt. So könnten wir beispielsweise von einer Zufallsvariablen $X$, einer Zufallsvariablen $Y$ oder einer Zufallsvariablen $Z$ sprechen. Diese Notation werde ich auch von hier an verwenden.

Eine **Zufallsvariable** kann zwei oder mehr mögliche Werte annehmen, jeder mit einer bestimmten positiven Wahrscheinlichkeit. Die möglichen Werte sind im **Ergebnisset** aufgelistet.

Jedes Mal, wenn man **eine Probe** einer Zufallsvariablen entnimmt, zieht man einen bestimmten Wert aus ihrem Ergebnisset gemäß den definierten Wahrscheinlichkeiten.

Wenden wir uns einem einfachen Beispiel zu. Nehmen wir an, eine Variable $X$ ist wie folgt definiert:

- $X$ hat das Ergebnisset $\{1,2\}$

$$
Pr[X = 1] = 0.5
$$

$$
Pr[X = 2] = 0.5
$$

Es ist leicht zu erkennen, dass $X$ eine Zufallsvariable ist. Erstens gibt es zwei oder mehr mögliche Werte, die $X$ annehmen kann, nämlich $1$ und $2$. Zweitens hat jeder mögliche Wert eine positive Wahrscheinlichkeit aufzutreten, wann immer man $X$ entnimmt, nämlich $0.5$.
Alles, was eine Zufallsvariable benötigt, ist eine Ergebnismenge mit zwei oder mehr Möglichkeiten, wobei jede Möglichkeit eine positive Wahrscheinlichkeit hat, bei der Stichprobe aufzutreten. Prinzipiell kann dann eine Zufallsvariable abstrakt definiert werden, losgelöst von jedem Kontext. In diesem Fall könnten Sie an "Stichprobenziehung" als das Durchführen eines natürlichen Experiments denken, um den Wert der Zufallsvariablen zu bestimmen.
Die Variable $X$ oben wurde abstrakt definiert. Sie könnten also daran denken, die Variable $X$ zu beproben, indem Sie eine faire Münze werfen und „2“ im Falle von Kopf und „1“ im Falle von Zahl zuweisen. Bei jeder Stichprobe von $X$ werfen Sie die Münze erneut.

Alternativ könnten Sie auch daran denken, $X$ zu beproben, indem Sie einen fairen Würfel werfen und „2“ zuweisen, falls der Würfel $1$, $3$ oder $4$ zeigt, und „1“ zuweisen, falls der Würfel $2$, $5$ oder $6$ zeigt. Jedes Mal, wenn Sie $X$ beproben, werfen Sie den Würfel erneut.

Tatsächlich kann jedes natürliche Experiment, das es Ihnen erlauben würde, die Wahrscheinlichkeiten der möglichen Werte von $X$ zu definieren, im Hinblick auf die Zeichnung vorgestellt werden.

Häufig werden Zufallsvariablen jedoch nicht nur abstrakt eingeführt. Stattdessen hat die Menge der möglichen Ausgangswerte eine explizite reale Bedeutung (anstatt nur als Zahlen). Darüber hinaus könnten diese Ausgangswerte gegen einen bestimmten Typ von Experiment definiert sein (anstatt als jedes natürliche Experiment mit diesen Werten).

Betrachten wir nun ein Beispiel einer Variablen $X$, die nicht abstrakt definiert ist. X ist wie folgt definiert, um zu bestimmen, welches von zwei Teams ein Fußballspiel beginnt:

- $X$ hat die Ergebnismenge {rot stößt an, blau stößt an}
- Werfen Sie eine bestimmte Münze $C$: Zahl = „rot stößt an“; Kopf = „blau stößt an“

$$
Pr [X = \text{rot stößt an}] = 0.5
$$

$$
Pr [X = \text{blau stößt an}] = 0.5
$$

In diesem Fall wird der Ergebnismenge von X eine konkrete Bedeutung verliehen, nämlich welches Team in einem Fußballspiel beginnt. Darüber hinaus werden die möglichen Ausgänge und ihre zugehörigen Wahrscheinlichkeiten durch ein konkretes Experiment bestimmt, nämlich das Werfen einer bestimmten Münze $C$.

In Diskussionen über Kryptographie werden Zufallsvariablen normalerweise gegen eine Ergebnismenge mit realer Bedeutung eingeführt. Es könnte die Menge aller Nachrichten sein, die verschlüsselt werden könnten, bekannt als der Nachrichtenraum, oder die Menge aller Schlüssel, die die Parteien, die die Verschlüsselung verwenden, auswählen können, bekannt als der Schlüsselraum.

Zufallsvariablen in Diskussionen über Kryptographie werden jedoch normalerweise nicht gegen ein bestimmtes natürliches Experiment definiert, sondern gegen jedes Experiment, das die richtigen Wahrscheinlichkeitsverteilungen liefern könnte.

Zufallsvariablen können diskrete oder kontinuierliche Wahrscheinlichkeitsverteilungen haben. Zufallsvariablen mit einer **diskreten Wahrscheinlichkeitsverteilung** – das heißt, diskrete Zufallsvariablen – haben eine endliche Anzahl möglicher Ausgänge. Die Zufallsvariable $X$ in beiden bisher gegebenen Beispielen war diskret.

**Kontinuierliche Zufallsvariablen** können stattdessen Werte in einem oder mehreren Intervallen annehmen. Man könnte zum Beispiel sagen, dass eine Zufallsvariable bei der Stichprobenziehung jeden reellen Wert zwischen 0 und 1 annimmt und dass jede reelle Zahl in diesem Intervall gleich wahrscheinlich ist. Innerhalb dieses Intervalls gibt es unendlich viele mögliche Werte.

Für kryptographische Diskussionen müssen Sie nur diskrete Zufallsvariablen verstehen. Jede Diskussion über Zufallsvariablen sollte daher als Bezugnahme auf diskrete Zufallsvariablen verstanden werden, sofern nicht ausdrücklich anders angegeben.

### Graphen von Zufallsvariablen
Die möglichen Werte und zugehörigen Wahrscheinlichkeiten einer Zufallsvariablen können leicht durch ein Diagramm visualisiert werden. Betrachten Sie zum Beispiel die Zufallsvariable $X$ aus dem vorherigen Abschnitt mit einer Ergebnismenge von $\{1, 2\}$, und $Pr [X = 1] = 0,5$ und $Pr [X = 2] = 0,5$. Typischerweise würden wir eine solche Zufallsvariable in Form eines Balkendiagramms darstellen, wie in *Abbildung 1*.
*Abbildung 1: Zufallsvariable X*

![Abbildung 1: Zufallsvariable X.](assets/Figure2-1.webp)

Die breiten Balken in *Abbildung 1* sollen keineswegs suggerieren, dass die Zufallsvariable $X$ tatsächlich kontinuierlich ist. Stattdessen werden die Balken breit gemacht, um optisch ansprechender zu sein (nur eine gerade Linie nach oben bietet eine weniger intuitive Visualisierung).

### Gleichverteilte Variablen

Im Ausdruck „Zufallsvariable“ bedeutet der Begriff „zufällig“ einfach „probabilistisch“. Mit anderen Worten, es bedeutet einfach, dass zwei oder mehr mögliche Ergebnisse der Variablen mit bestimmten Wahrscheinlichkeiten auftreten. Diese Ergebnisse müssen jedoch *nicht notwendigerweise* gleich wahrscheinlich sein (obwohl der Begriff „zufällig“ in anderen Kontexten diese Bedeutung haben kann).

Eine **gleichverteilte Variable** ist ein Spezialfall einer Zufallsvariablen. Sie kann zwei oder mehr Werte annehmen, alle mit gleicher Wahrscheinlichkeit. Die Zufallsvariable $X$, dargestellt in *Abbildung 1*, ist eindeutig eine gleichverteilte Variable, da beide möglichen Ergebnisse mit einer Wahrscheinlichkeit von $0,5$ auftreten. Es gibt jedoch viele Zufallsvariablen, die keine Beispiele für gleichverteilte Variablen sind.

Betrachten Sie zum Beispiel die Zufallsvariable $Y$. Sie hat eine Ergebnismenge $\{1, 2, 3, 8, 10\}$ und die folgende Wahrscheinlichkeitsverteilung:

$$
\Pr[Y = 1] = 0,25
$$

$$
\Pr[Y = 2] = 0,35
$$

$$
\Pr[Y = 3] = 0,1
$$

$$
\Pr[Y = 8] = 0,25
$$

$$
\Pr[Y = 10] = 0,05
$$

Während zwei mögliche Ergebnisse tatsächlich eine gleiche Wahrscheinlichkeit des Auftretens haben, nämlich $1$ und $8$, kann $Y$ auch bestimmte Werte mit anderen Wahrscheinlichkeiten als $0,25$ bei der Stichprobenentnahme annehmen. Daher ist $Y$ zwar eine Zufallsvariable, aber keine gleichverteilte Variable.

Eine grafische Darstellung von $Y$ wird in *Abbildung 2* bereitgestellt.

*Abbildung 2: Zufallsvariable Y*

![Abbildung 2: Zufallsvariable Y.](assets/Figure2-2.webp "Abbildung 2: Zufallsvariable Y")

Als letztes Beispiel betrachten Sie die Zufallsvariable Z. Sie hat die Ergebnismenge {1,3,7,11,12} und die folgende Wahrscheinlichkeitsverteilung:

$$
\Pr[Z = 2] = 0,2
$$

$$
\Pr[Z = 3] = 0,2
$$

$$
\Pr[Z = 9] = 0,2
$$

$$
\Pr[Z = 11] = 0,2
$$

$$
\Pr[Z = 12] = 0,2
$$

Sie können sie in *Abbildung 3* dargestellt sehen. Die Zufallsvariable Z ist im Gegensatz zu Y eine gleichverteilte Variable, da alle Wahrscheinlichkeiten für die möglichen Werte bei der Stichprobenentnahme gleich sind.

*Abbildung 3: Zufallsvariable Z*
![Abbildung 3: Zufallsvariable Z.](assets/Figure2-3.webp "Abbildung 3: Zufallsvariable Z")

### Bedingte Wahrscheinlichkeit

Nehmen wir an, Bob beabsichtigt, zufällig einen Tag aus dem letzten Kalenderjahr auszuwählen. Zu welchem Schluss sollten wir kommen bezüglich der Wahrscheinlichkeit, dass der ausgewählte Tag im Sommer liegt?

Solange wir davon ausgehen, dass Bobs Prozess tatsächlich völlig gleichmäßig ist, sollten wir schlussfolgern, dass die Wahrscheinlichkeit, dass Bob einen Tag im Sommer auswählt, 1/4 beträgt. Dies ist die **unbedingte Wahrscheinlichkeit**, dass der zufällig ausgewählte Tag im Sommer liegt.

Nehmen wir nun an, dass Bob statt eines beliebigen Kalendertags nur aus jenen Tagen gleichmäßig auswählt, an denen die Mittagstemperatur am Crystal Lake (New Jersey) 21 Grad Celsius oder höher war. Angesichts dieser zusätzlichen Information, zu welchem Schluss können wir bezüglich der Wahrscheinlichkeit kommen, dass Bob einen Tag im Sommer auswählt?

Wir sollten wirklich zu einem anderen Schluss kommen als zuvor, selbst ohne weitere spezifische Informationen (z.B. die Temperatur zu Mittag an jedem Tag des letzten Kalenderjahres).

Da bekannt ist, dass der Crystal Lake in New Jersey liegt, würden wir sicherlich nicht erwarten, dass die Mittagstemperatur im Winter 21 Grad Celsius oder höher ist. Stattdessen ist es viel wahrscheinlicher, dass es sich um einen warmen Tag im Frühling oder Herbst handelt, oder um einen Tag irgendwo im Sommer. Daher wird, wenn bekannt ist, dass die Mittagstemperatur am Crystal Lake am ausgewählten Tag 21 Grad Celsius oder höher war, die Wahrscheinlichkeit, dass der von Bob ausgewählte Tag im Sommer liegt, viel höher. Dies ist die **bedingte Wahrscheinlichkeit**, dass der zufällig ausgewählte Tag im Sommer liegt, vorausgesetzt, dass die Mittagstemperatur am Crystal Lake 21 Grad Celsius oder höher war.

Im Gegensatz zum vorherigen Beispiel können die Wahrscheinlichkeiten zweier Ereignisse auch völlig unabhängig voneinander sein. In diesem Fall sagen wir, dass sie **unabhängig** sind.

Nehmen wir zum Beispiel an, dass eine bestimmte faire Münze auf Kopf gelandet ist. Angesichts dieser Tatsache, was ist dann die Wahrscheinlichkeit, dass es morgen regnen wird? Die bedingte Wahrscheinlichkeit in diesem Fall sollte gleich der unbedingten Wahrscheinlichkeit sein, dass es morgen regnen wird, da ein Münzwurf im Allgemeinen keinen Einfluss auf das Wetter hat.

Wir verwenden ein "|" Symbol, um Aussagen über bedingte Wahrscheinlichkeiten zu schreiben. Beispielsweise kann die Wahrscheinlichkeit des Ereignisses $A$ unter der Bedingung, dass Ereignis $B$ eingetreten ist, wie folgt geschrieben werden:

$$
Pr[A|B]
$$

Wenn also zwei Ereignisse, $A$ und $B$, unabhängig sind, dann gilt:

$$
Pr[A|B] = Pr[A] \text{ und } Pr[B|A] = Pr[B]
$$

Die Bedingung für Unabhängigkeit kann wie folgt vereinfacht werden:

$$
Pr[A, B] = Pr[A] \cdot Pr[B]
$$

Ein Schlüsselergebnis in der Wahrscheinlichkeitstheorie ist als **Bayessches Theorem** bekannt. Es besagt im Grunde, dass $Pr[A|B]$ wie folgt umgeschrieben werden kann:

$$
Pr[A|B] = \frac{Pr[B|A] \cdot Pr[A]}{Pr[B]}
$$

Anstatt bedingte Wahrscheinlichkeiten mit spezifischen Ereignissen zu verwenden, können wir uns auch die bedingten Wahrscheinlichkeiten ansehen, die mit zwei oder mehr Zufallsvariablen über eine Reihe möglicher Ereignisse verbunden sind. Nehmen wir zwei Zufallsvariablen, $X$ und $Y$. Wir können jeden möglichen Wert für $X$ mit $x$ und jeden möglichen Wert für $Y$ mit $y$ bezeichnen. Wir könnten dann sagen, dass zwei Zufallsvariablen unabhängig sind, wenn die folgende Aussage zutrifft:

$$
Pr[X = x, Y = y] = Pr[X = x] \cdot Pr[Y = y]
$$

für alle $x$ und $y$.

Lassen Sie uns etwas expliziter darüber sein, was diese Aussage bedeutet.
Nehmen wir an, die Ergebnismengen für $X$ und $Y$ sind wie folgt definiert: **X** = $\{x_1, x_2, \ldots, x_i, \ldots, x_n\}$ und **Y** = $\{y_1, y_2, \ldots, y_i, \ldots, y_m\}$. (Es ist üblich, Mengen von Werten durch fettgedruckte, großgeschriebene Buchstaben zu kennzeichnen.)
Nehmen wir nun an, Sie ziehen eine Stichprobe von $Y$ und beobachten $y_1$. Die obige Aussage sagt uns, dass die Wahrscheinlichkeit, nun $x_1$ durch eine Stichprobe von $X$ zu erhalten, genau dieselbe ist, als hätten wir $y_1$ nie beobachtet. Dies gilt für jedes $y_i$, das wir aus unserer anfänglichen Stichprobe von $Y$ gezogen haben könnten. Schließlich gilt dies nicht nur für $x_1$. Für jedes $x_i$ wird die Wahrscheinlichkeit des Auftretens nicht durch das Ergebnis einer Stichprobe von $Y$ beeinflusst. All dies gilt auch für den Fall, dass $X$ zuerst gezogen wird.

Lassen Sie uns unsere Diskussion mit einem etwas philosophischeren Punkt beenden. In jeder realen Situation wird die Wahrscheinlichkeit eines Ereignisses immer gegen einen bestimmten Satz von Informationen abgewogen. Es gibt keine „unbedingte Wahrscheinlichkeit“ im sehr strengen Sinne des Wortes.

Nehmen wir zum Beispiel an, ich frage Sie nach der Wahrscheinlichkeit, dass Schweine bis 2030 fliegen können. Obwohl ich Ihnen keine weiteren Informationen gebe, wissen Sie offensichtlich viel über die Welt, das Ihr Urteil beeinflussen kann. Sie haben noch nie gesehen, dass Schweine fliegen. Sie wissen, dass die meisten Menschen nicht erwarten, dass sie fliegen können. Sie wissen, dass sie nicht wirklich zum Fliegen gebaut sind. Und so weiter.

Daher, wenn wir von einer „unbedingten Wahrscheinlichkeit“ eines Ereignisses in einem realen Kontext sprechen, kann dieser Begriff wirklich nur eine Bedeutung haben, wenn wir ihn als „die Wahrscheinlichkeit ohne weitere explizite Informationen“ verstehen. Jedes Verständnis einer „bedingten Wahrscheinlichkeit“ sollte dann immer gegen ein spezifisches Informationsstück verstanden werden.

Ich könnte Sie zum Beispiel nach der Wahrscheinlichkeit fragen, dass Schweine bis 2030 fliegen können, nachdem ich Ihnen Beweise gegeben habe, dass einige Ziegen in Neuseeland nach einigen Jahren des Trainings gelernt haben zu fliegen. In diesem Fall werden Sie wahrscheinlich Ihr Urteil über die Wahrscheinlichkeit, dass Schweine bis 2030 fliegen können, anpassen. Also ist die Wahrscheinlichkeit, dass Schweine bis 2030 fliegen können, bedingt durch diese Beweise über Ziegen in Neuseeland.

## Die Modulo-Operation
<chapterId>709b34e5-b155-53d2-abbd-97d67e56db00</chapterId>

### Modulo

Der grundlegendste Ausdruck mit der **Modulo-Operation** hat die folgende Form: $x \mod y$.

Die Variable $x$ wird als Dividend und die Variable $y$ als Divisor bezeichnet. Um eine Modulo-Operation mit einem positiven Dividenden und einem positiven Divisor durchzuführen, bestimmen Sie einfach den Rest der Division.

Betrachten Sie zum Beispiel den Ausdruck $25 \mod 4$. Die Zahl 4 geht insgesamt 6 Mal in die Zahl 25 ein. Der Rest dieser Division ist 1. Daher entspricht $25 \mod 4$ der Zahl 1. Auf ähnliche Weise können wir die folgenden Ausdrücke bewerten:

* $29 \mod 30 = 29$ (da 30 insgesamt 0 Mal in 29 geht und der Rest 29 ist)
* $42 \mod 2 = 0$ (da 2 insgesamt 21 Mal in 42 geht und der Rest 0 ist)
* $12 \mod 5 = 2$ (da 5 insgesamt 2 Mal in 12 passt und der Rest 2 ist)
* $20 \mod 8 = 4$ (da 8 insgesamt 2 Mal in 20 passt und der Rest 4 ist)

Wenn der Dividend oder Divisor negativ ist, können Modulo-Operationen von Programmiersprachen unterschiedlich gehandhabt werden.

Sie werden definitiv auf Fälle mit einem negativen Dividend in der Kryptographie stoßen. In diesen Fällen ist der typische Ansatz wie folgt:

* Bestimmen Sie zuerst den nächstniedrigeren Wert *kleiner oder gleich* dem Dividend, in den der Divisor ohne Rest passt. Nennen wir diesen Wert $p$.
* Wenn der Dividend $x$ ist, dann ist das Ergebnis der Modulo-Operation der Wert von $x – p$.

Nehmen wir an, der Dividend ist $–20$ und der Divisor 3. Der nächstniedrigere Wert, kleiner oder gleich $–20$, in den 3 ohne Rest passt, ist $–21$. Der Wert von $x – p$ in diesem Fall ist $–20 – (–21)$. Das ergibt 1 und somit ist $–20 \mod 3$ gleich 1. Auf ähnliche Weise können wir die folgenden Ausdrücke bewerten:

* $–8 \mod 5 = 2$
* $–19 \mod 16 = 13$
* $–14 \mod 6 = 4$

Bezüglich der Notation sehen Sie typischerweise die folgenden Arten von Ausdrücken: $x = [y \mod z]$. Aufgrund der Klammern gilt die Modulo-Operation in diesem Fall nur für die rechte Seite des Ausdrucks. Wenn $y$ zum Beispiel 25 und $z$ 4 ist, dann ergibt $x$ den Wert 1.

Ohne Klammern wirkt die Modulo-Operation auf *beide Seiten* eines Ausdrucks. Nehmen wir zum Beispiel den folgenden Ausdruck: $x = y \mod z$. Wenn $y$ 25 und $z$ 4 ist, dann wissen wir nur, dass $x \mod 4$ den Wert 1 ergibt. Dies ist konsistent mit jedem Wert für $x$ aus der Menge $\{\ldots,–7, –3, 1, 5, 9,\ldots\}$.

Der Bereich der Mathematik, der Modulo-Operationen an Zahlen und Ausdrücken umfasst, wird als **modulare Arithmetik** bezeichnet. Sie können sich diesen Bereich als Arithmetik für Fälle vorstellen, in denen die Zahlengerade nicht unendlich lang ist. Obwohl wir typischerweise auf Modulo-Operationen für (positive) ganze Zahlen innerhalb der Kryptographie stoßen, können Sie auch Modulo-Operationen mit beliebigen reellen Zahlen durchführen.

### Der Verschiebechiffre

Die Modulo-Operation wird häufig in der Kryptographie angetroffen. Um dies zu veranschaulichen, betrachten wir eines der berühmtesten historischen Verschlüsselungsschemata: den Verschiebechiffre.

Definieren wir ihn zuerst. Nehmen wir ein Wörterbuch *D*, das alle Buchstaben des englischen Alphabets in der Reihenfolge mit der Menge der Zahlen $\{0, 1, 2, \ldots, 25\}$ gleichsetzt. Nehmen wir einen Nachrichtenraum **M** an. Der **Verschiebechiffre** ist dann ein Verschlüsselungsschema, das wie folgt definiert ist:

- Wählen Sie gleichmäßig einen Schlüssel $k$ aus dem Schlüsselraum **K**, wo **K** = $\{0, 1, 2, \ldots, 25\}$ [1]
- Verschlüsseln Sie eine Nachricht $m \in \mathbf{M}$ wie folgt:
    - Trennen Sie $m$ in seine einzelnen Buchstaben $m_0, m_1, \ldots, m_i, \ldots, m_l$
- Konvertieren Sie jedes $m_i$ in eine Zahl gemäß *D*
    - Für jedes $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Konvertieren Sie jedes $c_i$ in einen Buchstaben gemäß *D*
    - Kombinieren Sie dann $c_0, c_1, \ldots, c_l$, um den Chiffretext $c$ zu erhalten
- Entschlüsseln Sie einen Chiffretext $c$ wie folgt:
    - Konvertieren Sie jedes $c_i$ in eine Zahl gemäß *D*
    - Für jedes $c_i$, $m_i = [(c_i – k) \mod 26]$
    - Konvertieren Sie jedes $m_i$ in einen Buchstaben gemäß *D*
    - Kombinieren Sie dann $m_0, m_1, \ldots, m_l$, um die ursprüngliche Nachricht $m$ zu erhalten

Der Modulo-Operator im Verschiebechiffre stellt sicher, dass Buchstaben umlaufen, sodass alle Chiffrebuchstaben definiert sind. Um dies zu veranschaulichen, betrachten Sie die Anwendung des Verschiebechiffres auf das Wort „HUND“.

Nehmen wir an, Sie haben einheitlich einen Schlüssel mit dem Wert 17 ausgewählt. Der Buchstabe „U“ entspricht 21. Ohne die Modulo-Operation würde die Addition dieser Klartextzahl mit dem Schlüssel zu einer Chiffretextzahl von 38 führen. Diese Chiffretextzahl könnte jedoch nicht in einen Chiffrebuchstaben umgewandelt werden, da das englische Alphabet nur 26 Buchstaben hat. Die Modulo-Operation stellt sicher, dass die Chiffretextzahl tatsächlich 12 (das Ergebnis von $38 \mod 26$) ist, was dem Chiffrebuchstaben „M“ entspricht.

Die gesamte Verschlüsselung des Wortes „HUND“ mit einem Schlüsselwert von 17 ist wie folgt:

* Nachricht = HUND = H,U,N,D = 8,21,14,4
* $c_0 = [(8 + 17) \mod 26] = [(25) \mod 26] = 25 = Y$
* $c_1 = [(21 + 17) \mod 26] = [(38) \mod 26] = 12 = M$
* $c_2 = [(14 + 17) \mod 26] = [(31) \mod 26] = 5 = F$
* $c_3 = [(4 + 17) \mod 26] = [(21) \mod 26] = 21 = V$
* $c = YMFV$

Jeder kann intuitiv verstehen, wie das Verschiebechiffre funktioniert und es wahrscheinlich selbst verwenden. Um jedoch Ihr Wissen über Kryptographie zu erweitern, ist es wichtig, mit der Formalisierung vertrauter zu werden, da die Schemata viel komplizierter werden. Daher wurde die Vorgehensweise für das Verschiebechiffre formalisiert.

**Anmerkungen:**

[1] Wir können diese Aussage genau definieren, indem wir die Terminologie aus dem vorherigen Abschnitt verwenden. Lassen Sie eine gleichförmige Variable $K$ $K$ als ihre Menge möglicher Ergebnisse haben. So:

$$
Pr[K = 0] = \frac{1}{26}
$$

$$
Pr[K = 1] = \frac{1}{26}
$$

...und so weiter. Wählen Sie die gleichförmige Variable $K$ einmal aus, um einen bestimmten Schlüssel zu erhalten.

## Die XOR-Operation
<chapterId>22f185cc-c516-5b33-950b-0908f2f881fe</chapterId>

Alle Computerdaten werden auf Bit-Ebene verarbeitet, gespeichert und über Netzwerke gesendet. Alle kryptografischen Schemata, die auf Computerdaten angewendet werden, operieren ebenfalls auf der Bit-Ebene.

Nehmen wir an, Sie haben eine E-Mail in Ihre E-Mail-Anwendung getippt. Jede Verschlüsselung, die Sie anwenden, erfolgt nicht direkt auf den ASCII-Zeichen Ihrer E-Mail. Stattdessen wird sie auf die Bit-Darstellung der Buchstaben und anderen Symbole in Ihrer E-Mail angewendet.
Eine Schlüsseloperation in der modernen Kryptographie, neben der Modulo-Operation, ist die **XOR-Operation** oder "exklusives Oder". Diese Operation nimmt zwei Bits als Eingabe und liefert ein weiteres Bit als Ausgabe. Die XOR-Operation wird einfach als "XOR" bezeichnet. Sie ergibt 0, wenn die beiden Bits gleich sind, und 1, wenn die beiden Bits unterschiedlich sind. Unten sehen Sie die vier Möglichkeiten. Das Symbol $\oplus$ steht für "XOR":
* $0 \oplus 0 = 0$
* $0 \oplus 1 = 1$
* $1 \oplus 0 = 1$
* $1 \oplus 1 = 0$

Um dies zu veranschaulichen, nehmen wir an, dass Sie eine Nachricht $m_1$ (01111001) und eine Nachricht $m_2$ (01011001) haben. Die XOR-Operation dieser beiden Nachrichten kann unten gesehen werden.

* $m_1 \oplus m_2 = 01111001 \oplus 01011001 = 00100000$

Der Prozess ist unkompliziert. Zuerst führen Sie die XOR-Operation für die am weitesten links stehenden Bits von $m_1$ und $m_2$ durch. In diesem Fall ist das $0 \oplus 0 = 0$. Dann führen Sie die XOR-Operation für das zweite Paar von Bits von links durch. In diesem Fall ist das $1 \oplus 1 = 0$. Sie setzen diesen Prozess fort, bis Sie die XOR-Operation für die am weitesten rechts stehenden Bits durchgeführt haben.

Es ist leicht zu erkennen, dass die XOR-Operation kommutativ ist, nämlich dass $m_1 \oplus m_2 = m_2 \oplus m_1$. Darüber hinaus ist die XOR-Operation auch assoziativ. Das heißt, $(m_1 \oplus m_2) \oplus m_3 = m_1 \oplus (m_2 \oplus m_3)$.

Eine XOR-Operation an zwei Zeichenketten unterschiedlicher Länge kann je nach Kontext unterschiedlich interpretiert werden. Wir werden uns hier nicht mit XOR-Operationen an Zeichenketten unterschiedlicher Länge beschäftigen.

Eine XOR-Operation entspricht dem Spezialfall der Durchführung einer Modulo-Operation auf die Addition von Bits, wenn der Divisor 2 ist. Die Äquivalenz können Sie in den folgenden Ergebnissen sehen:

* $(0 + 0) \mod 2 = 0 \oplus 0 = 0$
* $(1 + 0) \mod 2 = 1 \oplus 0 = 1$
* $(0 + 1) \mod 2 = 0 \oplus 1 = 1$
* $(1 + 1) \mod 2 = 1 \oplus 1 = 0$

## Pseudorandomness
<chapterId>20463fc5-3e92-581f-a1b7-3151279bd95e</chapterId>

In unserer Diskussion über zufällige und gleichverteilte Variablen haben wir eine spezifische Unterscheidung zwischen „zufällig“ und „gleichverteilt“ gemacht. Diese Unterscheidung wird in der Praxis typischerweise beibehalten, wenn es um die Beschreibung von Zufallsvariablen geht. Jedoch muss in unserem aktuellen Kontext diese Unterscheidung fallen gelassen werden und „zufällig“ und „gleichverteilt“ werden synonym verwendet. Ich werde am Ende des Abschnitts erklären, warum.

Zu Beginn können wir eine binäre Zeichenkette der Länge $n$ **zufällig** (oder **gleichverteilt**) nennen, wenn sie das Ergebnis der Stichprobenziehung einer gleichverteilten Variablen $S$ ist, die jeder binären Zeichenkette dieser Länge $n$ eine gleiche Wahrscheinlichkeit der Auswahl gibt.
Nehmen wir zum Beispiel die Menge aller Binärstrings der Länge 8: $\{0000\ 0000, 0000\ 0001, \ldots, 1111\ 1111\}$. (Es ist üblich, einen 8-Bit-String in zwei Quartette zu schreiben, jedes wird als **Nibble** bezeichnet.) Nennen wir diese Menge von Strings **$S_8$**.
Gemäß der obigen Definition können wir dann einen bestimmten Binärstring der Länge 8 als zufällig (oder gleichverteilt) bezeichnen, wenn er das Ergebnis der Stichprobenziehung einer gleichverteilten Variablen $S$ war, die jedem String in **$S_8$** eine gleiche Wahrscheinlichkeit der Auswahl gibt. Da die Menge **$S_8$** $2^8$ Elemente umfasst, müsste die Wahrscheinlichkeit der Auswahl bei der Stichprobenziehung für jeden String in der Menge $1/2^8$ betragen.

Ein Schlüsselaspekt für die Zufälligkeit eines Binärstrings ist, dass sie in Bezug auf den Prozess definiert wird, durch den er ausgewählt wurde. Die Form eines bestimmten Binärstrings an sich verrät daher nichts über seine Zufälligkeit bei der Auswahl.

Zum Beispiel haben viele Menschen intuitiv die Vorstellung, dass ein String wie $1111\ 1111$ nicht zufällig ausgewählt worden sein könnte. Aber das ist eindeutig falsch.

Definiert man eine gleichverteilte Variable $S$ über alle Binärstrings der Länge 8, ist die Wahrscheinlichkeit, $1111\ 1111$ aus der Menge **$S_8$** auszuwählen, dieselbe wie die eines Strings wie $0111\ 0100$. Somit kann man nichts über die Zufälligkeit eines Strings sagen, nur indem man den String selbst analysiert.

Wir können auch von zufälligen Strings sprechen, ohne speziell Binärstrings zu meinen. Wir könnten zum Beispiel von einem zufälligen Hex-String $AF\ 02\ 82$ sprechen. In diesem Fall wäre der String zufällig aus der Menge aller Hex-Strings der Länge 6 ausgewählt worden. Dies entspricht der zufälligen Auswahl eines Binärstrings der Länge 24, da jede Hex-Ziffer 4 Bits repräsentiert.

Typischerweise bezieht sich der Ausdruck „ein zufälliger String“, ohne Qualifikation, auf einen String, der zufällig aus der Menge aller Strings derselben Länge ausgewählt wurde. So habe ich es oben beschrieben. Ein String der Länge $n$ kann natürlich auch aus einer anderen Menge zufällig ausgewählt werden. Eine, die zum Beispiel nur eine Teilmenge aller Strings der Länge $n$ umfasst, oder vielleicht eine Menge, die Strings unterschiedlicher Länge einschließt. In diesen Fällen würden wir jedoch nicht von einem „zufälligen String“ sprechen, sondern von „einem String, der zufällig aus irgendeiner Menge **S** ausgewählt wurde“.

Ein Schlüsselkonzept innerhalb der Kryptografie ist das der Pseudorandomität. Ein **pseudorandomer String** der Länge $n$ erscheint *als ob* er das Ergebnis der Stichprobenziehung einer gleichverteilten Variablen $S$ wäre, die jedem String in **$S_n$** eine gleiche Wahrscheinlichkeit der Auswahl gibt. Tatsächlich jedoch ist der String das Ergebnis der Stichprobenziehung einer gleichverteilten Variablen $S'$, die nur eine Wahrscheinlichkeitsverteilung definiert – nicht notwendigerweise eine mit gleichen Wahrscheinlichkeiten für alle möglichen Ergebnisse – auf einer Teilmenge von **$S_n$**. Der entscheidende Punkt hierbei ist, dass niemand wirklich zwischen Stichproben von $S$ und $S'$ unterscheiden kann, selbst wenn man viele davon nimmt.
Nehmen wir zum Beispiel eine Zufallsvariable $S$. Ihr Ergebnisset ist **$S_{256}$**, dies ist die Menge aller Binärstrings der Länge 256. Diese Menge hat $2^{256}$ Elemente. Jedes Element hat bei der Auswahl eine gleiche Wahrscheinlichkeit von $1/2^{256}$.

Zusätzlich nehmen wir an, es gibt eine Zufallsvariable $S'$. Ihr Ergebnisset umfasst nur $2^{128}$ Binärstrings der Länge 256. Sie hat eine gewisse Wahrscheinlichkeitsverteilung über diese Strings, aber diese Verteilung ist nicht notwendigerweise gleichmäßig.

Angenommen, ich habe nun 1000er Proben von $S$ und 1000er Proben von $S'$ genommen und gebe Ihnen die zwei Ergebnismengen. Ich sage Ihnen, welche Menge von Ergebnissen mit welcher Zufallsvariablen verbunden ist. Als Nächstes nehme ich eine Probe von einer der beiden Zufallsvariablen. Aber dieses Mal sage ich Ihnen nicht, von welcher Zufallsvariablen ich die Probe nehme. Wenn $S'$ pseudorandom wäre, dann ist die Idee, dass Ihre Wahrscheinlichkeit, die richtige Vermutung anzustellen, von welcher Zufallsvariablen ich die Probe genommen habe, praktisch nicht besser als $1/2$ ist.

Typischerweise wird ein pseudorandomer String der Länge $n$ erzeugt, indem zufällig ein String der Größe $n – x$ ausgewählt wird, wobei $x$ eine positive ganze Zahl ist, und dieser als Eingabe für einen Expansionalgorithmus verwendet wird. Dieser zufällige String der Größe $n – x$ ist als der **Seed** bekannt.

Pseudorandom-Strings sind ein Schlüsselkonzept, um Kryptographie praktikabel zu machen. Betrachten Sie zum Beispiel Stromchiffren. Bei einer Stromchiffre wird ein zufällig ausgewählter Schlüssel in einen Expansionalgorithmus eingespeist, um einen viel größeren pseudorandomen String zu erzeugen. Dieser pseudorandome String wird dann mit dem Klartext über eine XOR-Operation kombiniert, um einen Chiffretext zu erzeugen.

Wenn wir diesen Typ von pseudorandomem String für eine Stromchiffre nicht erzeugen könnten, dann bräuchten wir einen Schlüssel, der so lang wie die Nachricht ist, für deren Sicherheit. Das ist in den meisten Fällen keine sehr praktikable Option.

Die hier diskutierte Vorstellung von Pseudorandomheit kann formaler definiert werden. Sie erstreckt sich auch auf andere Kontexte. Aber wir müssen diese Diskussion hier nicht vertiefen. Alles, was Sie für einen Großteil der Kryptographie intuitiv verstehen müssen, ist der Unterschied zwischen einem zufälligen und einem pseudorandomen String.

Der Grund für das Weglassen der Unterscheidung zwischen „zufällig“ und „gleichmäßig“ in unserer Diskussion sollte nun auch klar sein. In der Praxis verwendet jeder den Begriff pseudorandom, um einen String zu bezeichnen, der **als ob** er das Ergebnis der Stichprobe einer gleichmäßigen Variablen $S$ wäre. Streng genommen sollten wir einen solchen String „pseudo-gleichmäßig“ nennen, indem wir unsere Sprache von früher übernehmen. Da der Begriff „pseudo-gleichmäßig“ jedoch sowohl umständlich als auch von niemandem verwendet wird, werden wir ihn hier der Klarheit halber nicht einführen. Stattdessen lassen wir die Unterscheidung zwischen „zufällig“ und „gleichmäßig“ im aktuellen Kontext einfach fallen.

**Anmerkungen**

[2] Wenn Sie an einer formaleren Darstellung dieser Themen interessiert sind, können Sie Katz und Lindells *Einführung in die moderne Kryptographie*, insbesondere Kapitel 3, konsultieren.


# Mathematische Grundlagen der Kryptographie 2
<partId>d7245cc9-bb6d-5403-b3d5-9c703d9a2f81</partId>




## Was ist Zahlentheorie?
<chapterId>c0051c34-fd5d-539c-93e2-5c6dfd4c3355</chapterId>
Dieses Kapitel behandelt ein fortgeschritteneres Thema über die mathematischen Grundlagen der Kryptographie: die Zahlentheorie. Obwohl die Zahlentheorie für die symmetrische Kryptographie wichtig ist (wie beim Rijndael Cipher), ist sie besonders wichtig im Kontext der Public-Key-Kryptographie.

Wenn Sie die Details der Zahlentheorie als mühsam empfinden, würde ich Ihnen empfehlen, beim ersten Mal eine hochrangige Lektüre vorzunehmen. Sie können jederzeit später darauf zurückkommen.

___

Man könnte die **Zahlentheorie** als das Studium der Eigenschaften von ganzen Zahlen und mathematischen Funktionen, die mit ganzen Zahlen arbeiten, charakterisieren.

Betrachten Sie zum Beispiel, dass zwei Zahlen $a$ und $N$ **teilerfremd** (oder **relativ prim**) sind, wenn ihr größter gemeinsamer Teiler gleich 1 ist. Nehmen wir nun eine bestimmte ganze Zahl $N$ an. Wie viele ganze Zahlen, die kleiner als $N$ sind, sind teilerfremd zu $N$? Können wir allgemeine Aussagen über die Antworten auf diese Frage machen? Dies sind die typischen Arten von Fragen, die die Zahlentheorie zu beantworten sucht.

Die moderne Zahlentheorie stützt sich auf die Werkzeuge der abstrakten Algebra. Das Gebiet der **abstrakten Algebra** ist eine Unterdisziplin der Mathematik, bei der die Hauptobjekte der Analyse abstrakte Objekte sind, die als algebraische Strukturen bekannt sind. Eine **algebraische Struktur** ist eine Menge von Elementen, die mit einer oder mehreren Operationen verbunden sind, welche bestimmte Axiome erfüllen. Durch algebraische Strukturen können Mathematiker Einblicke in spezifische mathematische Probleme gewinnen, indem sie von deren Details abstrahieren.

Das Gebiet der abstrakten Algebra wird manchmal auch als moderne Algebra bezeichnet. Sie können auch auf den Begriff **abstrakte Mathematik** (oder **reine Mathematik**) stoßen. Dieser letztere Begriff bezieht sich nicht auf abstrakte Algebra, sondern bedeutet das Studium der Mathematik um ihrer selbst willen und nicht nur mit Blick auf potenzielle Anwendungen.

Die Mengen aus der abstrakten Algebra können sich mit vielen Arten von Objekten befassen, von den formbewahrenden Transformationen an einem gleichseitigen Dreieck bis hin zu Tapetenmustern. Für die Zahlentheorie betrachten wir nur Mengen von Elementen, die ganze Zahlen enthalten oder Funktionen, die mit ganzen Zahlen arbeiten.

## Gruppen
<chapterId>3209b270-f9cd-5224-803e-0ed19fbf7826</chapterId>

Ein grundlegendes Konzept in der Mathematik ist das einer Menge von Elementen. Eine Menge wird üblicherweise durch geschweifte Klammern dargestellt, wobei die Elemente durch Kommas getrennt sind.

Beispielsweise ist die Menge aller ganzen Zahlen $\{\ldots, -2, -1, 0, 1, 2, \ldots\}$. Die Ellipsen bedeuten hier, dass ein bestimmtes Muster in eine bestimmte Richtung fortgesetzt wird. So enthält die Menge aller ganzen Zahlen auch $3, 4, 5, 6$ und so weiter, sowie $-3, -4, -5, -6$ und so weiter. Diese Menge aller ganzen Zahlen wird typischerweise durch $\mathbb{Z}$ dargestellt.

Ein weiteres Beispiel für eine Menge ist $\mathbb{Z} \mod 11$, oder die Menge aller ganzen Zahlen modulo 11. Im Gegensatz zur gesamten Menge $\mathbb{Z}$ enthält diese Menge nur eine endliche Anzahl von Elementen, nämlich $\{0, 1, \ldots, 9, 10\}$.
Ein häufiger Fehler ist zu denken, dass die Menge $\mathbb{Z} \mod 11$ tatsächlich $\{-10, -9, \ldots, 0, \ldots, 9, 10\}$ ist. Aber das ist nicht der Fall, wenn man die Art und Weise betrachtet, wie wir die Modulo-Operation zuvor definiert haben. Alle negativen Ganzzahlen, die durch Modulo 11 reduziert werden, wickeln sich auf $\{0, 1, \ldots, 9, 10\}$ auf. Zum Beispiel wickelt sich der Ausdruck $-2 \mod 11$ auf $9$ auf, während sich der Ausdruck $-27 \mod 11$ auf $5$ aufwickelt.

Ein weiteres grundlegendes Konzept in der Mathematik ist das einer binären Operation. Das ist jede Operation, die zwei Elemente nimmt, um ein drittes zu produzieren. Zum Beispiel wären Sie aus der Grundrechenart und Algebra mit vier grundlegenden binären Operationen vertraut: Addition, Subtraktion, Multiplikation und Division.

Diese zwei grundlegenden mathematischen Konzepte, Mengen und binäre Operationen, werden verwendet, um die Vorstellung einer Gruppe zu definieren, die wesentlichste Struktur in der abstrakten Algebra.

Speziell nehmen wir an, es gibt eine binäre Operation $\circ$. Zusätzlich nehmen wir an, es gibt eine Menge von Elementen **S**, die mit dieser Operation ausgestattet ist. Alles, was „ausgestattet“ hier bedeutet, ist, dass die Operation $\circ$ zwischen beliebigen zwei Elementen in der Menge **S** durchgeführt werden kann.

Die Kombination $\langle \mathbf{S}, \circ \rangle$ ist dann eine **Gruppe**, wenn sie vier spezifische Bedingungen erfüllt, die als Gruppenaxiome bekannt sind.

1. Für beliebige $a$ und $b$, die Elemente von $\mathbf{S}$ sind, ist $a \circ b$ ebenfalls ein Element von $\mathbf{S}$. Dies ist als die **Abgeschlossenheitsbedingung** bekannt.
2. Für beliebige $a$, $b$ und $c$, die Elemente von $\mathbf{S}$ sind, gilt, dass $(a \circ b) \circ c = a \circ (b \circ c)$. Dies ist als die **Assoziativitätsbedingung** bekannt.
3. Es gibt ein einzigartiges Element $e$ in $\mathbf{S}$, sodass für jedes Element $a$ in $\mathbf{S}$ die folgende Gleichung gilt: $e \circ a = a \circ e = a$. Da es nur ein solches Element $e$ gibt, wird es das **neutrale Element** genannt. Diese Bedingung ist als die **Neutralitätsbedingung** bekannt.
4. Für jedes Element $a$ in $\mathbf{S}$ existiert ein Element $b$ in $\mathbf{S}$, sodass die folgende Gleichung gilt: $a \circ b = b \circ a = e$, wobei $e$ das neutrale Element ist. Element $b$ wird hier als das **inverse Element** bezeichnet und wird üblicherweise als $a^{-1}$ notiert. Diese Bedingung ist als die **Inversitätsbedingung** bekannt.

Lassen Sie uns Gruppen ein wenig weiter erkunden. Bezeichnen wir die Menge aller Ganzzahlen mit $\mathbb{Z}$. Diese Menge in Kombination mit der Standardaddition, oder $\langle \mathbb{Z}, + \rangle$, passt eindeutig zur Definition einer Gruppe, da sie die vier oben genannten Axiome erfüllt.

1. Für beliebige $x$ und $y$, die Elemente von $\mathbb{Z}$ sind, ist $x + y$ ebenfalls ein Element von $\mathbb{Z}$. Also erfüllt $\langle \mathbb{Z}, + \rangle$ die Abgeschlossenheitsbedingung.
2. Für jedes $x$, $y$ und $z$, die Elemente von $\mathbb{Z}$ sind, gilt $(x + y) + z = x + (y + z)$. Somit erfüllt $\langle \mathbb{Z}, + \rangle$ die Assoziativitätsbedingung. 3. Es gibt ein neutrales Element in $\langle \mathbb{Z}, + \rangle$, nämlich 0. Für jedes $x$ in $\mathbb{Z}$ gilt nämlich: $0 + x = x + 0 = x$. Somit erfüllt $\langle \mathbb{Z}, + \rangle$ die Neutralitätsbedingung. 4. Schließlich gibt es für jedes Element $x$ in $\mathbb{Z}$ ein $y$, sodass $x + y = y + x = 0$. Wenn $x$ beispielsweise 10 wäre, wäre $y$ $-10$ (falls $x$ 0 ist, ist $y$ ebenfalls 0). Somit erfüllt $\langle \mathbb{Z}, + \rangle$ die Inversitätsbedingung.

Wichtig ist, dass die Tatsache, dass die Menge der ganzen Zahlen mit Addition eine Gruppe bildet, nicht bedeutet, dass sie auch mit Multiplikation eine Gruppe bildet. Dies können Sie überprüfen, indem Sie $\langle \mathbb{Z}, \cdot \rangle$ gegen die vier Gruppenaxiome testen (wobei $\cdot$ die Standardmultiplikation bedeutet).

Die ersten beiden Axiome gelten offensichtlich. Darüber hinaus kann unter der Multiplikation das Element 1 als neutrales Element dienen. Jede ganze Zahl $x$, multipliziert mit 1, ergibt nämlich $x$. Jedoch erfüllt $\langle \mathbb{Z}, \cdot \rangle$ nicht die Inversitätsbedingung. Das heißt, es gibt kein eindeutiges Element $y$ in $\mathbb{Z}$ für jedes $x$ in $\mathbb{Z}$, sodass $x \cdot y = 1$.

Nehmen wir an, $x = 22$. Welcher Wert $y$ aus der Menge $\mathbb{Z}$, multipliziert mit $x$, würde das neutrale Element 1 ergeben? Der Wert von $1/22$ würde funktionieren, aber dieser ist nicht in der Menge $\mathbb{Z}$. Tatsächlich stößt man auf dieses Problem bei jeder ganzen Zahl $x$, außer bei den Werten 1 und -1 (wo $y$ jeweils 1 und -1 sein müsste).

Wenn wir reelle Zahlen für unsere Menge zulassen würden, dann verschwinden unsere Probleme größtenteils. Für jedes Element $x$ in der Menge führt die Multiplikation mit $1/x$ zu 1. Da Brüche in der Menge der reellen Zahlen enthalten sind, kann für jede reelle Zahl ein Inverses gefunden werden. Die Ausnahme bildet die Null, da jede Multiplikation mit Null niemals das neutrale Element 1 ergibt. Daher ist die Menge der nicht-null reellen Zahlen, ausgestattet mit der Multiplikation, tatsächlich eine Gruppe.

Einige Gruppen erfüllen eine fünfte allgemeine Bedingung, bekannt als die **Kommutativitätsbedingung**. Diese Bedingung lautet wie folgt:

* Angenommen, eine Gruppe $G$ mit einer Menge **S** und einem binären Operator $\circ$. Angenommen, $a$ und $b$ sind Elemente von **S**. Wenn es der Fall ist, dass $a \circ b = b \circ a$ für beliebige zwei Elemente $a$ und $b$ in **S**, dann erfüllt $G$ die Kommutativitätsbedingung.
Jede Gruppe, die die Kommutativitätsbedingung erfüllt, ist als **kommutative Gruppe** oder **abelsche Gruppe** (nach Niels Henrik Abel) bekannt. Es ist leicht zu überprüfen, dass sowohl die Menge der reellen Zahlen über Addition als auch die Menge der ganzen Zahlen über Addition abelsche Gruppen sind. Die Menge der ganzen Zahlen über Multiplikation ist überhaupt keine Gruppe und kann daher ipso facto keine abelsche Gruppe sein. Im Gegensatz dazu ist die Menge der von null verschiedenen reellen Zahlen über Multiplikation auch eine abelsche Gruppe.

Zwei wichtige Konventionen zur Notation sollten beachtet werden. Erstens werden die Zeichen „+“ oder „×“ häufig verwendet, um Gruppenoperationen zu symbolisieren, auch wenn die Elemente tatsächlich keine Zahlen sind. In diesen Fällen sollten Sie diese Zeichen nicht als standardmäßige arithmetische Addition oder Multiplikation interpretieren. Stattdessen handelt es sich um Operationen, die nur eine abstrakte Ähnlichkeit mit diesen arithmetischen Operationen haben.

Sofern Sie sich nicht speziell auf arithmetische Addition oder Multiplikation beziehen, ist es einfacher, Symbole wie $\circ$ und $\diamond$ für Gruppenoperationen zu verwenden, da diese keine sehr kulturell tief verwurzelten Konnotationen haben.

Zweitens, aus demselben Grund, warum „+“ und „×“ oft verwendet werden, um nicht-arithmetische Operationen anzuzeigen, werden die Identitätselemente von Gruppen häufig durch „0“ und „1“ symbolisiert, auch wenn die Elemente in diesen Gruppen keine Zahlen sind. Sofern Sie sich nicht auf das Identitätselement einer Gruppe mit Zahlen beziehen, ist es einfacher, ein neutraleres Symbol wie „$e$“ zu verwenden, um das Identitätselement anzugeben.

Viele verschiedene und sehr wichtige Mengen von Werten in der Mathematik, die mit bestimmten binären Operationen ausgestattet sind, sind Gruppen. Kryptografische Anwendungen arbeiten jedoch nur mit Mengen von ganzen Zahlen oder zumindest Elementen, die durch ganze Zahlen beschrieben werden, das heißt, im Bereich der Zahlentheorie. Daher werden Mengen mit reellen Zahlen außer ganzen Zahlen in kryptografischen Anwendungen nicht verwendet.

Lassen Sie uns abschließend ein Beispiel für Elemente geben, die „durch ganze Zahlen beschrieben werden können“, obwohl sie keine ganzen Zahlen sind. Ein gutes Beispiel sind die Punkte auf elliptischen Kurven. Obwohl jeder Punkt auf einer elliptischen Kurve klar keine ganze Zahl ist, wird ein solcher Punkt tatsächlich durch zwei ganze Zahlen beschrieben.

Elliptische Kurven sind beispielsweise entscheidend für Bitcoin. Jedes Standard-Bitcoin-Private- und Public-Key-Paar wird aus der Menge von Punkten ausgewählt, die durch die folgende elliptische Kurve definiert ist:

$$
x^3 + 7 = y^2 \mod 2^{256} – 2^{32} – 29 – 28 – 27 – 26 - 24 - 1
$$

(die größte Primzahl kleiner als $2^{256}$). Die $x$-Koordinate ist der private Schlüssel und die $y$-Koordinate ist Ihr öffentlicher Schlüssel.

Transaktionen in Bitcoin beinhalten typischerweise das Sperren von Ausgaben an einen oder mehrere öffentliche Schlüssel auf irgendeine Weise. Der Wert aus diesen Transaktionen kann dann durch Erstellen digitaler Signaturen mit den entsprechenden privaten Schlüsseln entsperrt werden.

## Zyklische Gruppen
<chapterId>bfa5c714-7952-5fef-88b1-ca5b07edd886</chapterId>

Ein wichtiger Unterschied, den wir machen können, ist zwischen einer **endlichen** und einer **unendlichen Gruppe**. Erstere hat eine endliche Anzahl von Elementen, während letztere eine unendliche Anzahl von Elementen hat. Die Anzahl der Elemente in jeder endlichen Gruppe ist als die **Ordnung der Gruppe** bekannt. Alle praktischen kryptografischen Anwendungen, die Gruppen verwenden, stützen sich auf endliche (zahlentheoretische) Gruppen.

Innerhalb der Public-Key-Kryptografie ist eine bestimmte Klasse von endlichen abelschen Gruppen, bekannt als zyklische Gruppen, besonders wichtig. Um zyklische Gruppen zu verstehen, müssen wir zunächst das Konzept der Exponentiation von Gruppenelementen verstehen.
Nehmen wir an, eine Gruppe $G$ mit einer Gruppenoperation $\circ$, und dass $a$ ein Element von $G$ ist. Der Ausdruck $a^n$ sollte dann als das Element $a$ interpretiert werden, das insgesamt $n – 1$ Mal mit sich selbst kombiniert wird. Zum Beispiel bedeutet $a^2$ $a \circ a$, $a^3$ bedeutet $a \circ a \circ a$ und so weiter. (Beachten Sie, dass die Exponentiation hier nicht notwendigerweise Exponentiation im üblichen arithmetischen Sinne ist.)

Wenden wir uns einem Beispiel zu. Nehmen wir an, dass $G = \langle \mathbb{Z} \mod 7, + \rangle$ ist, und dass unser Wert für $a$ gleich 4 ist. In diesem Fall ist $a^2 = [4 + 4 \mod 7] = [8 \mod 7] = 1 \mod 7$. Alternativ würde $a^4$ $[4 + 4 + 4 + 4 \mod 7] = [16 \mod 7] = 2 \mod 7$ darstellen.

Einige Abelsche Gruppen haben ein oder mehrere Elemente, die durch fortgesetzte Exponentiation alle anderen Gruppenelemente erzeugen können. Diese Elemente werden **Generatoren** oder **primitive Elemente** genannt.

Eine wichtige Klasse solcher Gruppen ist $\langle \mathbb{Z}^* \mod N, \cdot \rangle$, wobei $N$ eine Primzahl ist. Die Notation $\mathbb{Z}^*$ bedeutet hier, dass die Gruppe alle nicht-null, positiven ganzen Zahlen kleiner als $N$ enthält. Eine solche Gruppe hat daher immer $N – 1$ Elemente.

Betrachten wir zum Beispiel $G = \langle \mathbb{Z}^* \mod 11, \cdot \rangle$. Diese Gruppe hat die folgenden Elemente: $\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$. Die Ordnung dieser Gruppe ist 10 (was tatsächlich $11 – 1$ entspricht).

Lassen Sie uns das Exponentieren des Elements 2 aus dieser Gruppe erkunden. Die Berechnungen bis zu $2^{12}$ werden unten gezeigt. Beachten Sie, dass auf der linken Seite der Gleichung der Exponent auf die Exponentiation von Gruppenelementen verweist. In unserem speziellen Beispiel beinhaltet dies tatsächlich arithmetische Exponentiation auf der rechten Seite der Gleichung (es hätte aber auch zum Beispiel Addition beinhalten können). Zur Klarstellung habe ich die wiederholte Operation ausgeschrieben, anstatt die Exponentenform auf der rechten Seite.

* $2^1 = 2 \mod 11$
* $2^2 = 2 \cdot 2 \mod 11 = 4 \mod 11$
* $2^3 = 2 \cdot 2 \cdot 2 \mod 11 = 8 \mod 11$
* $2^4 = 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 16 \mod 11 = 5 \mod 11$
* $2^5 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 32 \mod 11 = 10 \mod 11$
* $2^6 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 64 \mod 11 = 9 \mod 11$
* $2^7 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 128 \mod 11 = 7 \mod 11$
* $2^8 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 256 \mod 11 = 3 \mod 11$
* $2^9 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 512 \mod 11 = 6 \mod 11$
* $2^{10} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 1024 \mod 11 = 1 \mod 11$
* $2^{11} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 2048 \mod 11 = 2 \mod 11$
* $2^{12} = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 \mod 11 = 4096 \mod 11 = 4 \mod 11$

Wenn Sie genau hinsehen, können Sie erkennen, dass die Potenzierung des Elements 2 in der folgenden Reihenfolge durch alle Elemente von $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ zyklisch verläuft: 2, 4, 8, 5, 10, 9, 7, 3, 6, 1. Nach $2^{10}$ zyklisiert die fortgesetzte Potenzierung des Elements 2 erneut durch alle Elemente und in derselben Reihenfolge. Daher ist das Element 2 ein Generator in $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$.

Obwohl $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ mehrere Generatoren hat, sind nicht alle Elemente dieser Gruppe Generatoren. Betrachten Sie zum Beispiel das Element 3. Die Durchführung der ersten 10 Potenzierungen, ohne die umständlichen Berechnungen zu zeigen, ergibt die folgenden Ergebnisse:

* $3^1 = 3 \mod 11$
* $3^2 = 9 \mod 11$
* $3^3 = 5 \mod 11$
* $3^4 = 4 \mod 11$
* $3^5 = 1 \mod 11$
* $3^6 = 3 \mod 11$
* $3^7 = 9 \mod 11$
* $3^8 = 5 \mod 11$
* $3^9 = 4 \mod 11$
* $3^{10} = 1 \mod 11$
Anstatt alle Werte in $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ zu durchlaufen, führt die Exponentiation des Elements 3 nur zu einer Teilmenge dieser Werte: 3, 9, 5, 4 und 1. Nach der fünften Exponentiation beginnen diese Werte sich zu wiederholen.
Wir können nun eine **zyklische Gruppe** als jede Gruppe definieren, die mindestens einen Generator hat. Das heißt, es gibt mindestens ein Gruppenelement, aus dem man durch Exponentiation alle anderen Gruppenelemente erzeugen kann.

Vielleicht haben Sie in unserem Beispiel oben bemerkt, dass sowohl $2^{10}$ als auch $3^{10}$ gleich $1 \mod 11$ sind. Tatsächlich, obwohl wir die Berechnungen nicht durchführen werden, führt die Exponentiation mit 10 jedes Elements in der Gruppe $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ zu $1 \mod 11$. Warum ist das so?

Dies ist eine wichtige Frage, aber es bedarf einiger Arbeit, um sie zu beantworten.

Beginnen wir damit, zwei positive ganze Zahlen $a$ und $N$ anzunehmen. Ein wichtiges Theorem in der Zahlentheorie besagt, dass $a$ ein multiplikatives Inverses modulo $N$ hat (das heißt, eine ganze Zahl $b$, so dass $a \cdot b = 1 \mod N$), wenn und nur wenn der größte gemeinsame Teiler zwischen $a$ und $N$ gleich 1 ist. Das heißt, wenn $a$ und $N$ teilerfremd sind.

Also, für jede Gruppe von ganzen Zahlen, die mit der Multiplikation modulo $N$ ausgestattet ist, sind nur die kleineren Teilerfremden mit $N$ in der Menge enthalten. Wir können diese Menge mit $\mathbb{Z}^c \mod N$ bezeichnen.

Nehmen wir zum Beispiel an, dass $N$ 10 ist. Nur die ganzen Zahlen 1, 3, 7 und 9 sind teilerfremd mit 10. Also enthält die Menge $\mathbb{Z}^c \mod 10$ nur $\{1, 3, 7, 9\}$. Man kann keine Gruppe mit ganzzahliger Multiplikation modulo 10 unter Verwendung anderer ganzer Zahlen zwischen 1 und 10 erstellen. Für diese spezielle Gruppe sind die Inversen die Paare 1 und 9 sowie 3 und 7.

Im Fall, dass $N$ selbst eine Primzahl ist, sind alle ganzen Zahlen von 1 bis $N – 1$ teilerfremd mit $N$. Eine solche Gruppe hat also eine Ordnung von $N – 1$. Unter Verwendung unserer früheren Notation entspricht $\mathbb{Z}^c \mod N$ $\mathbb{Z}^* \mod N$, wenn $N$ eine Primzahl ist. Die Gruppe, die wir für unser früheres Beispiel ausgewählt haben, $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$, ist ein spezielles Beispiel dieser Klasse von Gruppen.

Als Nächstes berechnet die Funktion $\phi(N)$ die Anzahl der Teilerfremden bis zu einer Zahl $N$ und ist als **Eulersche Phi-Funktion** bekannt. [1] Gemäß dem **Eulerschen Theorem** gilt, wann immer zwei ganze Zahlen $a$ und $N$ teilerfremd sind, folgendes:

* $a^{\phi(N)} \mod N = 1 \mod N$
Dies hat eine wichtige Implikation für die Klasse der Gruppen $\langle \mathbb{Z}^* \mod N, \cdot \rangle$, wobei $N$ eine Primzahl ist. Für diese Gruppen repräsentiert die Exponentiation von Gruppenelementen die arithmetische Exponentiation. Das heißt, $a^{\phi(N)} \mod N$ stellt die arithmetische Operation $a^{\phi(N)} \mod N$ dar. Da jedes Element $a$ in diesen multiplikativen Gruppen teilerfremd mit $N$ ist, bedeutet dies, dass $a^{\phi(N)} \mod N = a^{N – 1} \mod N = 1 \mod N$.

Eulers Theorem ist ein wirklich wichtiges Ergebnis. Zunächst impliziert es, dass alle Elemente in $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ nur durch eine Anzahl von Werten durch Exponentiation zyklisch verlaufen können, die in $N – 1$ teilt. Im Fall von $\langle \mathbb{Z}^* \mod 11, \cdot \rangle$ bedeutet dies, dass jedes Element nur durch 2, 5 oder 10 Elemente zyklisch verlaufen kann. Die Gruppenwerte, durch die jedes Element bei der Exponentiation zyklisch verläuft, sind als die **Ordnung des Elements** bekannt. Ein Element mit einer Ordnung, die der Ordnung einer Gruppe entspricht, ist ein Generator.

Darüber hinaus impliziert Eulers Theorem, dass wir immer das Ergebnis von $a^{N – 1} \mod N$ für jede Gruppe $\langle \mathbb{Z}^* \mod N, \cdot \rangle$ kennen können, bei der $N$ eine Primzahl ist. Dies gilt unabhängig davon, wie kompliziert die tatsächlichen Berechnungen sein mögen.

Nehmen wir zum Beispiel an, unsere Gruppe ist $\mathbb{Z}^* \mod 160,481,182$ (wo 160,481,182 tatsächlich eine Primzahl ist). Wir wissen, dass alle ganzen Zahlen von 1 bis 160,481,181 Elemente dieser Gruppe sein müssen und dass $\phi(n) = 160,481,181$. Obwohl wir nicht alle Schritte in den Berechnungen durchführen können, wissen wir, dass Ausdrücke wie $514^{160,481,181}$, $2,005^{160,481,181}$ und $256,212^{160,481,181}$ alle zu $1 \mod 160,481,182$ auswerten müssen.

**Notizen:**

[1] Die Funktion funktioniert wie folgt. Jede ganze Zahl $N$ kann in ein Produkt von Primzahlen zerlegt werden. Nehmen wir an, dass ein bestimmtes $N$ wie folgt zerlegt wird: $p_1^{e1} \cdot p_2^{e2} \cdot \ldots \cdot p_m^{em}$, wobei alle $p$’s Primzahlen und alle $e$’s ganze Zahlen größer oder gleich 1 sind. Dann:

$$
\phi(N) = \sum_{i=1}^m \left[p_i^{e_i} - p_i^{e_i - 1}\right]
$$

Eulers Phi-Funktion Formel für die Primfaktorzerlegung von $N$.

## Felder
<chapterId>fad52d86-3a22-5c9f-979e-3bec9eaa008e</chapterId>

Eine Gruppe ist die grundlegende algebraische Struktur in der abstrakten Algebra, aber es gibt noch viele mehr. Die einzige andere algebraische Struktur, die Sie kennen müssen, ist die eines **Feldes**, speziell die eines **endlichen Feldes**. Diese Art von algebraischer Struktur wird häufig in der Kryptographie verwendet, wie zum Beispiel im Advanced Encryption Standard. Letzterer ist das Hauptverfahren der symmetrischen Verschlüsselung, auf das Sie in der Praxis stoßen werden.
Ein Feld leitet sich von der Vorstellung einer Gruppe ab. Speziell ist ein **Feld** eine Menge von Elementen **S** ausgestattet mit zwei binären Operatoren $\circ$ und $\diamond$, welche die folgenden Bedingungen erfüllen:
1. Die Menge **S** ausgestattet mit $\circ$ ist eine Abelsche Gruppe.
2. Die Menge **S** ausgestattet mit $\diamond$ ist eine Abelsche Gruppe für die "nicht-null" Elemente.
3. Die Menge **S** ausgestattet mit den beiden Operatoren erfüllt die sogenannte distributive Bedingung: Angenommen, $a$, $b$ und $c$ sind Elemente von **S**. Dann erfüllt **S** ausgestattet mit den beiden Operatoren die distributive Eigenschaft, wenn $a \circ (b \diamond c) = (a \circ b) \diamond (a \circ c)$.

Beachten Sie, dass, wie bei Gruppen, die Definition eines Feldes sehr abstrakt ist. Es werden keine Aussagen über die Arten von Elementen in **S** oder über die Operationen $\circ$ und $\diamond$ gemacht. Es wird lediglich festgestellt, dass ein Feld jede Menge von Elementen mit zwei Operationen ist, für die die drei oben genannten Bedingungen gelten. (Das "Null"-Element in der zweiten Abelschen Gruppe kann abstrakt interpretiert werden.)

Was könnte also ein Beispiel für ein Feld sein? Ein gutes Beispiel ist die Menge $\mathbb{Z} \mod 7$, oder $\{0, 1, \ldots, 7\}$ definiert über die Standardaddition (anstelle von $\circ$ oben) und die Standardmultiplikation (anstelle von $\diamond$ oben).

Zuerst erfüllt $\mathbb{Z} \mod 7$ die Bedingung, eine Abelsche Gruppe über Addition zu sein, und es erfüllt die Bedingung, eine Abelsche Gruppe über Multiplikation zu sein, wenn man nur die nicht-null Elemente betrachtet. Zweitens erfüllt die Kombination der Menge mit den beiden Operatoren die distributive Bedingung.

Es ist didaktisch wertvoll, diese Behauptungen zu erkunden, indem man einige spezielle Werte verwendet. Nehmen wir die experimentellen Werte 5, 2 und 3, einige zufällig ausgewählte Elemente aus der Menge $\mathbb{Z} \mod 7$, um das Feld $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$ zu untersuchen. Wir werden diese drei Werte der Reihe nach verwenden, wie benötigt, um spezielle Bedingungen zu erkunden.

Lassen Sie uns zuerst erkunden, ob $\mathbb{Z} \mod 7$ ausgestattet mit Addition eine Abelsche Gruppe ist.

1. **Abgeschlossenheitsbedingung**: Nehmen wir 5 und 2 als unsere Werte. In diesem Fall ist $[5 + 2] \mod 7 = 7 \mod 7 = 0$. Dies ist tatsächlich ein Element von $\mathbb{Z} \mod 7$, also ist das Ergebnis konsistent mit der Abgeschlossenheitsbedingung.
2. **Assoziativitätsbedingung**: Nehmen wir 5, 2 und 3 als unsere Werte. In diesem Fall ist $[(5 + 2) + 3] \mod 7 = [5 + (2 + 3)] \mod 7 = 10 \mod 7 = 3$. Dies ist konsistent mit der Assoziativitätsbedingung.
3. **Identitätsbedingung**: Nehmen wir 5 als unseren Wert. In diesem Fall ist $[5 + 0] \mod 7 = [0 + 5] \mod 7 = 5$. Also scheint 0 das Identitätselement für die Addition zu sein.
4. **Inverse Bedingung**: Betrachten wir das Inverse von 5. Es muss gelten, dass $[5 + d] \mod 7 = 0$ für einen bestimmten Wert von $d$. In diesem Fall ist der einzigartige Wert aus $\mathbb{Z} \mod 7$, der diese Bedingung erfüllt, 2,5. **Kommutativitätsbedingung**: Nehmen wir 5 und 3 als unsere Werte. In diesem Fall ist $[5 + 3] \mod 7 = [3 + 5] \mod 7 = 1$. Dies ist konsistent mit der Kommutativitätsbedingung.

Die Menge $\mathbb{Z} \mod 7$ ausgestattet mit Addition erscheint klar als eine Abelsche Gruppe. Lassen Sie uns nun erkunden, ob $\mathbb{Z} \mod 7$ ausgestattet mit Multiplikation für alle Nicht-Null-Elemente eine Abelsche Gruppe ist.

1. **Abgeschlossenheitsbedingung**: Nehmen wir 5 und 2 als unsere Werte. In diesem Fall ist $[5 \cdot 2] \mod 7 = 10 \mod 7 = 3$. Dies ist ebenfalls ein Element von $\mathbb{Z} \mod 7$, also ist das Ergebnis konsistent mit der Abgeschlossenheitsbedingung.
2. **Assoziativitätsbedingung**: Nehmen wir 5, 2 und 3 als unsere Werte. In diesem Fall ist $[(5 \cdot 2) \cdot 3] \mod 7 = [5 \cdot (2 \cdot 3)] \mod 7 = 30 \mod 7 = 2$. Dies ist konsistent mit der Assoziativitätsbedingung.
3. **Identitätsbedingung**: Nehmen wir 5 als unseren Wert. In diesem Fall ist $[5 \cdot 1] \mod 7 = [1 \cdot 5] \mod 7 = 5$. Also scheint 1 das Identitätselement für die Multiplikation zu sein.
4. **Inverse Bedingung**: Betrachten wir das Inverse von 5. Es muss gelten, dass $[5 \cdot d] \mod 7 = 1$ für einen bestimmten Wert von $d$. Der einzigartige Wert aus $\mathbb{Z} \mod 7$, der diese Bedingung erfüllt, ist 3. Dies ist konsistent mit der Inversen Bedingung.
5. **Kommutativitätsbedingung**: Nehmen wir 5 und 3 als unsere Werte. In diesem Fall ist $[5 \cdot 3] \mod 7 = [3 \cdot 5] \mod 7 = 15 \mod 7 = 1$. Dies ist konsistent mit der Kommutativitätsbedingung.

Die Menge $\mathbb{Z} \mod 7$ scheint eindeutig die Regeln für eine Abelsche Gruppe zu erfüllen, wenn sie entweder mit Addition oder Multiplikation über die Nicht-Null-Elemente verbunden wird.

Schließlich scheint diese Menge kombiniert mit beiden Operatoren die distributive Bedingung zu erfüllen. Nehmen wir 5, 2 und 3 als unsere Werte. Wir können sehen, dass $[5 \cdot (2 + 3)] \mod 7 = [5 \cdot 2 + 5 \cdot 3] \mod 7 = 25 \mod 7 = 4$.

Wir haben nun gesehen, dass $\mathbb{Z} \mod 7$ ausgestattet mit Addition und Multiplikation die Axiome für ein endliches Feld erfüllt, wenn es mit bestimmten Werten getestet wird. Natürlich können wir das auch allgemein zeigen, werden dies hier aber nicht tun.

Ein Schlüsselunterschied besteht zwischen zwei Arten von Feldern: endliche und unendliche Felder.
Ein **unendliches Feld** bezieht sich auf ein Feld, bei dem die Menge **S** unendlich groß ist. Die Menge der reellen Zahlen $\mathbb{R}$, ausgestattet mit Addition und Multiplikation, ist ein Beispiel für ein unendliches Feld. Ein **endliches Feld**, auch bekannt als **Galois-Feld**, ist ein Feld, bei dem die Menge **S** endlich ist. Unser obiges Beispiel von $\langle \mathbb{Z} \mod 7, +, \cdot \rangle$ ist ein endliches Feld.
In der Kryptographie sind wir hauptsächlich an endlichen Feldern interessiert. Allgemein lässt sich zeigen, dass ein endliches Feld für eine Menge von Elementen **S** existiert, wenn und nur wenn es $p^m$ Elemente hat, wobei $p$ eine Primzahl und $m$ eine positive ganze Zahl größer oder gleich eins ist. Mit anderen Worten, wenn die Ordnung einer Menge **S** eine Primzahl ($p^m$ wobei $m = 1$) oder eine Primzahlpotenz ($p^m$ wobei $m > 1$) ist, dann können Sie zwei Operatoren $\circ$ und $\diamond$ finden, sodass die Bedingungen für ein Feld erfüllt sind.

Wenn ein endliches Feld eine Primzahl von Elementen hat, dann wird es als **Primfeld** bezeichnet. Wenn die Anzahl der Elemente im endlichen Feld eine Primzahlpotenz ist, dann wird das Feld als **Erweiterungsfeld** bezeichnet. In der Kryptographie sind wir an beiden, Prim- und Erweiterungsfeldern, interessiert. [2]

Die Hauptprimfelder von Interesse in der Kryptographie sind solche, bei denen die Menge aller ganzen Zahlen durch eine Primzahl moduliert wird und die Operatoren die Standardaddition und -multiplikation sind. Diese Klasse von endlichen Feldern würde $\mathbb{Z} \mod 2$, $\mathbb{Z} \mod 3$, $\mathbb{Z} \mod 5$, $\mathbb{Z} \mod 7$, $\mathbb{Z} \mod 11$, $\mathbb{Z} \mod 13$ und so weiter einschließen. Für jedes Primfeld $\mathbb{Z} \mod p$ ist die Menge der ganzen Zahlen des Feldes wie folgt: $\{0, 1, \ldots, p – 2, p – 1\}$.

In der Kryptographie sind wir auch an Erweiterungsfeldern interessiert, insbesondere an solchen Feldern mit $2^m$ Elementen, wobei $m > 1$. Solche endlichen Felder werden beispielsweise im Rijndael Cipher verwendet, der die Grundlage des Advanced Encryption Standard bildet. Während Primfelder relativ intuitiv sind, sind diese Basis-2-Erweiterungsfelder wahrscheinlich nicht für jeden verständlich, der nicht mit abstrakter Algebra vertraut ist.

Zunächst ist es tatsächlich wahr, dass jeder Menge von ganzen Zahlen mit $2^m$ Elementen zwei Operatoren zugewiesen werden können, die ihre Kombination zu einem Feld machen würden (solange $m$ eine positive ganze Zahl ist). Doch nur weil ein Feld existiert, bedeutet das nicht unbedingt, dass es leicht zu entdecken oder besonders praktisch für bestimmte Anwendungen ist.

Wie sich herausstellt, sind besonders anwendbare Erweiterungsfelder von $2^m$ in der Kryptographie solche, die über bestimmte Mengen von Polynomausdrücken definiert sind, anstatt über eine Menge von ganzen Zahlen.

Nehmen wir an, wir wollten ein Erweiterungsfeld mit $2^3$ (d.h., 8) Elementen in der Menge. Während es viele verschiedene Mengen geben könnte, die für Felder dieser Größe verwendet werden können, umfasst eine solche Menge alle einzigartigen Polynome der Form $a_2x^2 + a_1x + a_0$, wobei jeder Koeffizient $a_i$ entweder 0 oder 1 ist. Daher umfasst diese Menge **S** die folgenden Elemente:
1. $0$: Der Fall, bei dem $a_2 = 0$, $a_1 = 0$ und $a_0 = 0$ ist.
2. $1$: Der Fall, bei dem $a_2 = 0$, $a_1 = 0$ und $a_0 = 1$ ist.
3. $x$: Der Fall, bei dem $a_2 = 0$, $a_1 = 1$ und $a_0 = 0$ ist.
4. $x + 1$: Der Fall, bei dem $a_2 = 0$, $a_1 = 1$ und $a_0 = 1$ ist.
5. $x^2$: Der Fall, bei dem $a_2 = 1$, $a_1 = 0$ und $a_0 = 0$ ist.
6. $x^2 + 1$: Der Fall, bei dem $a_2 = 1$, $a_1 = 0$ und $a_0 = 1$ ist.
7. $x^2 + x$: Der Fall, bei dem $a_2 = 1$, $a_1 = 1$ und $a_0 = 0$ ist.
8. $x^2 + x + 1$: Der Fall, bei dem $a_2 = 1$, $a_1 = 1$ und $a_0 = 1$ ist.

Somit wäre **S** die Menge $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$. Welche zwei Operationen können über dieser Menge von Elementen definiert werden, um sicherzustellen, dass ihre Kombination ein Feld bildet?

Die erste Operation auf der Menge **S** ($\circ$) kann als Standardpolynomaddition modulo 2 definiert werden. Alles, was Sie tun müssen, ist, die Polynome wie gewohnt zu addieren und dann das Modulo 2 auf jeden der Koeffizienten des resultierenden Polynoms anzuwenden. Hier sind einige Beispiele:

* $[(x^2) + (x^2 + x + 1)] \mod 2 = [2x^2 + x + 1] \mod 2 = x + 1$
* $[(x^2 + x) + (x)] \mod 2 = [x^2 + 2x] \mod 2 = x^2$
* $[(x + 1) + (x^2 + x + 1)] \mod 2 = [x^2 + 2x + 2] \mod 2 = x^2 + 1$

Die zweite Operation auf der Menge **S** ($\diamond$), die für die Erstellung des Feldes benötigt wird, ist komplizierter. Es handelt sich um eine Art der Multiplikation, aber nicht um die Standardmultiplikation aus der Arithmetik. Stattdessen muss man jedes Element als einen Vektor betrachten und die Operation als die Multiplikation dieser beiden Vektoren modulo eines irreduziblen Polynoms verstehen.

Wenden wir uns zunächst der Idee eines irreduziblen Polynoms zu. Ein **irreduzibles Polynom** ist eines, das nicht faktorisiert werden kann (genauso wie eine Primzahl nicht in andere Komponenten als 1 und die Primzahl selbst faktorisiert werden kann). Für unsere Zwecke interessieren wir uns für Polynome, die in Bezug auf die Menge aller ganzen Zahlen irreduzibel sind. (Beachten Sie, dass Sie bestimmte Polynome möglicherweise faktorisieren können, zum Beispiel durch die reellen oder komplexen Zahlen, auch wenn Sie sie nicht mit ganzen Zahlen faktorisieren können.)
Zum Beispiel betrachten Sie das Polynom $x^2 - 3x + 2$. Dies kann umgeschrieben werden als $(x – 1)(x – 2)$. Daher ist dieses Polynom nicht irreduzibel. Betrachten Sie nun das Polynom $x^2 + 1$. Unter Verwendung von nur ganzen Zahlen gibt es keine Möglichkeit, diesen Ausdruck weiter zu faktorisieren. Daher ist dies ein irreduzibles Polynom in Bezug auf die ganzen Zahlen.

Als Nächstes wenden wir uns dem Konzept der Vektor-Multiplikation zu. Wir werden dieses Thema nicht in der Tiefe erkunden, aber Sie müssen nur eine grundlegende Regel verstehen: Eine Vektor-Division kann stattfinden, solange der Dividend einen höheren oder gleich hohen Grad wie der Divisor hat. Wenn der Dividend einen niedrigeren Grad als der Divisor hat, kann der Dividend nicht länger durch den Divisor geteilt werden.

Zum Beispiel betrachten Sie den Ausdruck $x^6 + x + 1 \mod x^5 + x^2$. Dies reduziert sich weiter, da der Grad des Dividenden, 6, höher ist als der Grad des Divisors, 5. Betrachten Sie nun den Ausdruck $x^5 + x + 1 \mod x^5 + x^2$. Dies reduziert sich ebenfalls weiter, da der Grad des Dividenden, 5, und des Divisors, 5, gleich sind.

Betrachten Sie jedoch jetzt den Ausdruck $x^4 + x + 1 \mod x^5 + x^2$. Dies reduziert sich nicht weiter, da der Grad des Dividenden, 4, niedriger ist als der Grad des Divisors, 5.

Auf der Grundlage dieser Informationen sind wir nun bereit, unsere zweite Operation für die Menge $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$ zu finden.

Ich habe bereits gesagt, dass die zweite Operation als Vektor-Multiplikation modulo eines irreduziblen Polynoms verstanden werden sollte. Dieses irreduzible Polynom sollte sicherstellen, dass die zweite Operation eine Abelsche Gruppe über **S** definiert und mit der distributiven Bedingung konsistent ist. Welches sollte also dieses irreduzible Polynom sein?

Da alle Vektoren in der Menge einen Grad von 2 oder niedriger haben, sollte das irreduzible Polynom einen Grad von 3 haben. Wenn eine Multiplikation von zwei Vektoren in der Menge ein Polynom vom Grad 3 oder höher ergibt, wissen wir, dass modulo eines Polynoms vom Grad 3 immer ein Polynom vom Grad 2 oder niedriger ergibt. Dies ist der Fall, weil jedes Polynom vom Grad 3 oder höher immer durch ein Polynom vom Grad 3 teilbar ist. Zusätzlich muss das Polynom, das als Divisor fungiert, irreduzibel sein.

Es stellt sich heraus, dass es mehrere irreduzible Polynome vom Grad 3 gibt, die wir als unseren Divisor verwenden könnten. Jedes dieser Polynome definiert in Verbindung mit unserer Menge **S** und Addition modulo 2 ein unterschiedliches Feld. Das bedeutet, Sie haben mehrere Optionen, wenn Sie Erweiterungskörper $2^m$ in der Kryptographie verwenden.

Für unser Beispiel nehmen wir an, dass wir das Polynom $x^3 + x + 1$ auswählen. Dies ist tatsächlich irreduzibel, da Sie es nicht unter Verwendung von ganzen Zahlen faktorisieren können. Zusätzlich wird es sicherstellen, dass jede Multiplikation von zwei Elementen ein Polynom vom Grad 2 oder weniger ergibt.
Lassen Sie uns anhand eines Beispiels der zweiten Operation durchgehen, indem wir das Polynom $x^3 + x + 1$ als Divisor verwenden, um zu veranschaulichen, wie es funktioniert. Nehmen wir an, dass Sie die Elemente $x^2 + 1$ mit $x^2 + x$ in unserer Menge **S** multiplizieren. Dann müssen wir den Ausdruck $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1$ berechnen. Dies kann wie folgt vereinfacht werden:
* $[(x^2 + 1) \cdot (x^2 + x)] \mod x^3 + x + 1 =$
* $[x^2 \cdot x^2 + x^2 \cdot x + 1 \cdot x^2 + 1 \cdot x] \mod x^3 + x + 1 =$
* $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$

Wir wissen, dass $[x^4 + x^3 + x^2 + x] \mod x^3 + x + 1$ reduziert werden kann, da der Dividend einen höheren Grad (4) als der Divisor (3) hat.

Um zu beginnen, können Sie sehen, dass der Ausdruck $x^3 + x + 1$ insgesamt $x$-mal in $x^4 + x^3 + x^2 + x$ geht. Sie können dies überprüfen, indem Sie $x^3 + x + 1$ mit $x$ multiplizieren, was $x^4 + x^2 + x$ ergibt. Da der letztere Term denselben Grad wie der Dividend hat, nämlich 4, wissen wir, dass dies funktioniert. Sie können den Rest dieser Division durch $x$ wie folgt berechnen:

* $[(x^4 + x^3 + x^2 + x) - (x^4 + x^2 + x)] \mod x^3 + x + 1 =$
* $[x^3] \mod x^3 + x + 1 =$
* $x^3$

Also, nachdem wir $x^4 + x^3 + x^2 + x$ insgesamt $x$-mal durch $x^3 + x + 1$ geteilt haben, haben wir einen Rest von $x^3$. Kann dies weiter durch $x^3 + x + 1$ geteilt werden?

Intuitiv könnte man sagen, dass $x^3$ nicht weiter durch $x^3 + x + 1$ geteilt werden kann, weil der letztere Term größer erscheint. Erinnern Sie sich jedoch an unsere Diskussion über die Vektordivision zuvor. Solange der Dividend einen Grad hat, der größer oder gleich dem des Divisors ist, kann der Ausdruck weiter reduziert werden. Speziell kann der Ausdruck $x^3 + x + 1$ genau 1 Mal in $x^3$ gehen. Der Rest wird wie folgt berechnet:

$$
[(x^3) - (x^3 + x + 1)] \mod x^3 + x + 1 = [x + 1] \mod x^3 + x + 1 = x + 1
$$

Sie fragen sich vielleicht, warum $(x^3) - (x^3 + x + 1)$ zu $x + 1$ und nicht zu $-x - 1$ ausgewertet wird. Erinnern Sie sich daran, dass die erste Operation unseres Feldes modulo 2 definiert ist. Daher ergibt die Subtraktion zweier Vektoren genau dasselbe Ergebnis wie die Addition zweier Vektoren.
Zusammenfassend zur Multiplikation von $x^2 + 1$ und $x^2 + x$: Wenn man diese beiden Terme multipliziert, erhält man ein Polynom vierten Grades, $x^4 + x^3 + x^2 + x$, das modulo $x^3 + x + 1$ reduziert werden muss. Das Polynom vierten Grades ist durch $x^3 + x + 1$ genau $x + 1$ Mal teilbar. Der Rest nach der Division von $x^4 + x^3 + x^2 + x$ durch $x^3 + x + 1$ genau $x + 1$ Mal ist $x + 1$. Dies ist tatsächlich ein Element in unserem Set $\{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$.

Warum sind Erweiterungskörper mit Basis 2 über Mengen von Polynomen, wie im obigen Beispiel, für die Kryptographie nützlich? Der Grund ist, dass man die Koeffizienten in den Polynomen solcher Mengen, entweder 0 oder 1, als Elemente von Binärstrings mit einer bestimmten Länge betrachten kann. Das Set **S** in unserem Beispiel oben könnte stattdessen als ein Set **S** betrachtet werden, das alle Binärstrings der Länge 3 (000 bis 111) umfasst. Die Operationen auf **S** können dann auch verwendet werden, um Operationen auf diesen Binärstrings durchzuführen und einen Binärstring derselben Länge zu erzeugen.

**Notizen:**

[2] Erweiterungskörper werden sehr kontraintuitiv. Anstatt Elemente von Ganzzahlen zu haben, haben sie Mengen von Polynomen. Darüber hinaus werden alle Operationen modulo eines irreduziblen Polynoms durchgeführt.

## Abstrakte Algebra in der Praxis
<chapterId>ed35b98d-18b4-5790-9911-1078e0f84f92</chapterId>

Trotz der formalen Sprache und Abstraktheit der Diskussion sollte das Konzept einer Gruppe nicht zu schwierig zu verstehen sein. Es ist einfach eine Menge von Elementen zusammen mit einer binären Operation, bei der die Ausführung dieser binären Operation auf diesen Elementen vier allgemeinen Bedingungen genügt. Eine abelsche Gruppe hat nur eine zusätzliche Bedingung, die als Kommutativität bekannt ist. Eine zyklische Gruppe wiederum ist eine spezielle Art von abelscher Gruppe, nämlich eine, die einen Generator hat. Ein Feld ist lediglich eine komplexere Konstruktion aus der grundlegenden Gruppenvorstellung.

Aber wenn Sie praktisch veranlagt sind, fragen Sie sich vielleicht an diesem Punkt: Wen interessiert das? Hat das Wissen, dass eine Menge von Elementen mit einem Operator eine Gruppe ist, oder sogar eine abelsche oder zyklische Gruppe, irgendeine Relevanz in der realen Welt? Hat das Wissen, dass etwas ein Feld ist?

Ohne zu sehr ins Detail zu gehen, lautet die Antwort „ja“. Gruppen wurden im 19. Jahrhundert vom französischen Mathematiker Evariste Galois erstellt. Er verwendete sie, um Schlussfolgerungen über das Lösen von Polynomgleichungen eines Grades höher als fünf zu ziehen.

Seitdem hat das Konzept der Gruppe geholfen, eine Reihe von Problemen in der Mathematik und anderswo zu beleuchten. Auf ihrer Basis konnte beispielsweise der Physiker Murray-Gellman die Existenz eines Teilchens vorhersagen, bevor es tatsächlich in Experimenten beobachtet wurde. [3] Als weiteres Beispiel verwenden Chemiker die Gruppentheorie, um die Formen von Molekülen zu klassifizieren. Mathematiker haben sogar das Konzept einer Gruppe verwendet, um Schlussfolgerungen über etwas so Konkretes wie Tapeten zu ziehen!
Im Wesentlichen zu zeigen, dass eine Menge von Elementen mit einer bestimmten Operation eine Gruppe bildet, bedeutet, dass das, was Sie beschreiben, eine bestimmte Symmetrie aufweist. Nicht eine Symmetrie im allgemeinen Sinne des Wortes, sondern in einer abstrakteren Form. Und dies kann erhebliche Einblicke in bestimmte Systeme und Probleme bieten. Die komplexeren Begriffe aus der abstrakten Algebra geben uns zusätzliche Informationen.
Am wichtigsten ist, dass Sie die Bedeutung von zahlentheoretischen Gruppen und Körpern in der Praxis durch ihre Anwendung in der Kryptographie, insbesondere der Public-Key-Kryptographie, sehen werden. Wir haben bereits in unserer Diskussion über Körper gesehen, zum Beispiel, wie Erweiterungskörper im Rijndael Cipher verwendet werden. Wir werden dieses Beispiel in *Kapitel 5* ausarbeiten.

Für weitere Diskussionen über abstrakte Algebra würde ich die ausgezeichnete Videoserie über abstrakte Algebra von Socratica empfehlen. [4] Ich würde insbesondere die folgenden Videos empfehlen: „What is abstract algebra?“, „Group definition (expanded)“, „Ring definition (expanded)“, und „Field definition (expanded)“. Diese vier Videos werden Ihnen einige zusätzliche Einblicke in einen Großteil der oben geführten Diskussion geben. (Wir haben nicht über Ringe gesprochen, aber ein Körper ist nur eine spezielle Art von Ring.)

Für weitere Diskussionen über moderne Zahlentheorie können Sie viele fortgeschrittene Diskussionen über Kryptographie konsultieren. Als Vorschläge würde ich Jonathan Katz und Yehuda Lindells Einführung in die moderne Kryptographie oder Christof Paar und Jan Pelzls Verständnis der Kryptographie für weitere Diskussionen anbieten. [5]

**Anmerkungen:**

[3] Siehe [YouTube-Video](https://www.youtube.com/watch?v=NOMUnMuxDZY&feature=youtu.be)

[4] Socratica, [Abstrakte Algebra](https://www.socratica.com/subject/abstract-algebra)

[5] Katz und Lindell, *Einführung in die moderne Kryptographie*, 2. Auflage, 2015 (CRC Press: Boca Raton, FL). Paar und Pelzl, *Verständnis der Kryptographie*, 2010 (Springer-Verlag: Berlin).

# Symmetrische Kryptographie
<partId>ef768d0e-fe7b-510c-87d6-6febb3de1039</partId>

## Alice und Bob
<chapterId>47345330-be2d-5faf-afd0-d289a8d21bf1</chapterId>

Einer der beiden Hauptzweige der Kryptographie ist die symmetrische Kryptographie. Sie umfasst Verschlüsselungsschemata sowie Schemata, die sich mit Authentifizierung und Integrität befassen. Bis in die 1970er Jahre hätte die gesamte Kryptographie aus symmetrischen Verschlüsselungsschemata bestanden.

Die Hauptdiskussion beginnt mit der Betrachtung symmetrischer Verschlüsselungsschemata und macht die entscheidende Unterscheidung zwischen Stromchiffren und Blockchiffren. Dann wenden wir uns den Nachrichtenauthentifizierungscodes zu, die Schemata zur Sicherstellung der Nachrichtenintegrität und -authentizität sind. Schließlich erkunden wir, wie symmetrische Verschlüsselungsschemata und Nachrichtenauthentifizierungscodes kombiniert werden können, um eine sichere Kommunikation zu gewährleisten.

Dieses Kapitel diskutiert verschiedene symmetrische kryptographische Schemata aus der Praxis im Vorbeigehen. Das nächste Kapitel bietet eine detaillierte Darstellung der Verschlüsselung mit einer Stromchiffre und einer Blockchiffre aus der Praxis, nämlich RC4 und AES.

Bevor wir unsere Diskussion über symmetrische Kryptographie beginnen, möchte ich kurz einige Bemerkungen zu den Illustrationen von Alice und Bob in diesem und den folgenden Kapiteln machen.

___

Bei der Veranschaulichung der Prinzipien der Kryptographie verlassen sich die Menschen oft auf Beispiele, die Alice und Bob involvieren. Ich werde dies ebenfalls tun.

Besonders wenn Sie neu in der Kryptographie sind, ist es wichtig zu realisieren, dass diese Beispiele von Alice und Bob nur dazu dienen, die Prinzipien und Konstruktionen der Kryptographie in einer vereinfachten Umgebung zu illustrieren. Die Prinzipien und Konstruktionen sind jedoch auf eine viel breitere Palette von realen Kontexten anwendbar.
Im Folgenden finden Sie fünf wichtige Punkte, die Sie bei Beispielen mit Alice und Bob in der Kryptographie beachten sollten:
1. Sie können leicht in Beispiele mit anderen Arten von Akteuren wie Unternehmen oder Regierungsorganisationen übersetzt werden.
2. Sie können leicht erweitert werden, um drei oder mehr Akteure einzubeziehen.
3. In den Beispielen sind Bob und Alice typischerweise aktive Teilnehmer beim Erstellen jeder Nachricht und bei der Anwendung kryptografischer Schemata auf diese Nachricht. In der Realität sind elektronische Kommunikationen jedoch weitgehend automatisiert. Wenn Sie beispielsweise eine Website mit Transport Layer Security besuchen, wird die Kryptographie typischerweise vollständig von Ihrem Computer und dem Webserver gehandhabt.
4. Im Kontext der elektronischen Kommunikation sind die „Nachrichten“, die über einen Kommunikationskanal gesendet werden, normalerweise TCP/IP-Pakete. Diese können zu einer E-Mail, einer Facebook-Nachricht, einem Telefongespräch, einer Dateiübertragung, einer Website, einem Software-Upload und so weiter gehören. Es handelt sich nicht um Nachrichten im traditionellen Sinne. Dennoch vereinfachen Kryptographen diese Realität oft, indem sie sagen, dass die Nachricht beispielsweise eine E-Mail ist.
5. Die Beispiele konzentrieren sich in der Regel auf elektronische Kommunikation, können aber auch auf traditionelle Kommunikationsformen wie Briefe erweitert werden.

## Symmetrische Verschlüsselungsschemata
<chapterId>41bfdbe1-6d41-5272-98bb-81f24b2fd6af</chapterId>

Wir können ein **symmetrisches Verschlüsselungsschema** locker als jedes kryptografische Schema mit drei Algorithmen definieren:

1. Ein **Schlüsselgenerierungsalgorithmus**, der einen privaten Schlüssel generiert.
2. Ein **Verschlüsselungsalgorithmus**, der den privaten Schlüssel und einen Klartext als Eingaben nimmt und einen Chiffretext ausgibt.
3. Ein **Entschlüsselungsalgorithmus**, der den privaten Schlüssel und den Chiffretext als Eingaben nimmt und den ursprünglichen Klartext ausgibt.

Typischerweise bietet ein Verschlüsselungsschema – ob symmetrisch oder asymmetrisch – eine Vorlage für die Verschlüsselung basierend auf einem Kernalgorithmus, anstatt einer exakten Spezifikation.

Betrachten Sie zum Beispiel Salsa20, ein symmetrisches Verschlüsselungsschema. Es kann sowohl mit 128-Bit- als auch mit 256-Bit-Schlüssellängen verwendet werden. Die Wahl der Schlüssellänge beeinflusst einige kleinere Details des Algorithmus (genau genommen die Anzahl der Durchläufe im Algorithmus).

Aber man würde nicht sagen, dass die Verwendung von Salsa20 mit einem 128-Bit-Schlüssel ein anderes Verschlüsselungsschema ist als Salsa20 mit einem 256-Bit-Schlüssel. Der Kernalgorithmus bleibt derselbe. Nur wenn sich der Kernalgorithmus ändert, würden wir wirklich von zwei verschiedenen Verschlüsselungsschemata sprechen.

Symmetrische Verschlüsselungsschemata sind typischerweise in zwei Arten von Fällen nützlich: (1) Solche, in denen zwei oder mehr Agenten aus der Ferne kommunizieren und den Inhalt ihrer Kommunikation geheim halten wollen; und (2) solche, in denen ein Agent den Inhalt einer Nachricht über die Zeit geheim halten möchte.

Sie können eine Darstellung der Situation (1) in *Abbildung 1* unten sehen. Bob möchte eine Nachricht $M$ über eine Distanz an Alice senden, möchte aber nicht, dass andere diese Nachricht lesen können.

Bob verschlüsselt zuerst die Nachricht $M$ mit dem privaten Schlüssel $K$. Dann sendet er den Chiffretext $C$ an Alice. Sobald Alice den Chiffretext erhalten hat, kann sie ihn mit dem Schlüssel $K$ entschlüsseln und den Klartext lesen. Mit einem guten Verschlüsselungsschema sollte jeder Angreifer, der den Chiffretext $C$ abfängt, nichts von wirklicher Bedeutung über die Nachricht $M$ erfahren können.

Sie können eine Darstellung der Situation (2) in *Abbildung 2* unten sehen. Bob möchte verhindern, dass andere bestimmte Informationen einsehen. Eine typische Situation könnte sein, dass Bob ein Mitarbeiter ist, der sensible Daten auf seinem Computer speichert, die weder Außenstehende noch seine Kollegen lesen sollen.
Bob verschlüsselt die Nachricht $M$ zum Zeitpunkt $T_0$ mit dem Schlüssel $K$, um den Geheimtext $C$ zu erzeugen. Zum Zeitpunkt $T_1$ benötigt er die Nachricht erneut und entschlüsselt den Geheimtext $C$ mit dem Schlüssel $K$. Jeder Angreifer, der in der Zwischenzeit auf den Geheimtext $C$ gestoßen sein könnte, sollte nicht in der Lage gewesen sein, etwas Bedeutendes über $M$ daraus abzuleiten.

*Abbildung 1: Geheimhaltung über den Raum*

![Abbildung 1: Geheimhaltung über den Raum](assets/Figure4-1.webp "Abbildung 1: Geheimhaltung über den Raum")

*Abbildung 2: Geheimhaltung über die Zeit*

![Abbildung 2: Geheimhaltung über die Zeit](assets/Figure4-2.webp "Abbildung 2: Geheimhaltung über die Zeit")

## Ein Beispiel: Die Verschiebechiffre
<chapterId>7b179ae8-8d15-5e80-a43f-22c970d87b5e</chapterId>

In Kapitel 2 sind wir auf die Verschiebechiffre gestoßen, die ein Beispiel für ein sehr einfaches symmetrisches Verschlüsselungsverfahren ist. Lassen Sie uns hier noch einmal darauf schauen.

Nehmen wir ein Wörterbuch *D*, das alle Buchstaben des englischen Alphabets der Reihe nach den Zahlen $\{0,1,2,\dots,25\}$ zuordnet. Nehmen wir eine Menge möglicher Nachrichten **M** an. Die Verschiebechiffre ist dann ein Verschlüsselungsverfahren, das wie folgt definiert ist:

- Wähle zufällig einen Schlüssel $k$ aus der Menge der möglichen Schlüssel **K**, wobei **K** = $\{0,1,2,\dots,25\}$
- Verschlüssle eine Nachricht $m \in$ **M**, wie folgt:
    - Trenne $m$ in seine einzelnen Buchstaben $m_0, m_1,\dots, m_i, \dots, m_l$
    - Konvertiere jedes $m_i$ in eine Zahl gemäß *D*
    - Für jedes $m_i$, $c_i = [(m_i + k) \mod 26]$
    - Konvertiere jedes $c_i$ in einen Buchstaben gemäß *D*
    - Kombiniere dann $c_0, c_1,\dots, c_l$, um den Geheimtext $c$ zu erhalten
- Entschlüssle einen Geheimtext $c$ wie folgt:
    - Konvertiere jedes $c_i$ in eine Zahl gemäß *D*
    - Für jedes $c_i$, $m_i = [(c_i - k) \mod 26]$
    - Konvertiere jedes $m_i$ in einen Buchstaben gemäß *D*
    - Kombiniere dann $m_0, m_1,\dots, m_l$, um die ursprüngliche Nachricht $m$ zu erhalten

Was die Verschiebechiffre zu einem symmetrischen Verschlüsselungsverfahren macht, ist, dass derselbe Schlüssel sowohl für den Verschlüsselungs- als auch für den Entschlüsselungsprozess verwendet wird. Angenommen, Sie möchten die Nachricht „DOG“ mit der Verschiebechiffre verschlüsseln und haben zufällig „24“ als Schlüssel ausgewählt. Die Verschlüsselung der Nachricht mit diesem Schlüssel würde „BME“ ergeben. Die einzige Möglichkeit, die ursprüngliche Nachricht wiederherzustellen, besteht darin, denselben Schlüssel, „24“, für den Entschlüsselungsprozess zu verwenden.

Diese Verschiebechiffre ist ein Beispiel für eine **monoalphabetische Substitutionschiffre**: ein Verschlüsselungsverfahren, bei dem das Geheimtextalphabet festgelegt ist (d.h., es wird nur ein Alphabet verwendet). Unter der Annahme, dass der Entschlüsselungsalgorithmus deterministisch ist, kann jedes Symbol im Substitutionstext höchstens einem Symbol im Klartext entsprechen.
Bis ins 18. Jahrhundert basierten viele Anwendungen der Verschlüsselung stark auf monoalphabetischen Substitutionschiffren, obwohl diese oft viel komplexer waren als die Verschiebungschiffre. Man könnte beispielsweise zufällig einen Buchstaben des Alphabets für jeden Buchstaben des Originaltexts auswählen, unter der Bedingung, dass jeder Buchstabe im Chiffre-Alphabet nur einmal vorkommt. Das bedeutet, dass man faktoriell 26 mögliche private Schlüssel hätte, was in der Zeit vor Computern enorm war.
Beachten Sie, dass Ihnen der Begriff **Chiffre** in der Kryptographie häufig begegnen wird. Seien Sie sich bewusst, dass dieser Begriff verschiedene Bedeutungen hat. Tatsächlich kenne ich mindestens fünf unterschiedliche Bedeutungen des Begriffs innerhalb der Kryptographie.

In einigen Fällen bezieht er sich auf ein Verschlüsselungsschema, wie es bei der Verschiebungschiffre und der monoalphabetischen Substitutionschiffre der Fall ist. Der Begriff kann sich jedoch auch speziell auf den Verschlüsselungsalgorithmus, den privaten Schlüssel oder einfach den Chiffretext eines solchen Verschlüsselungsschemas beziehen.

Zuletzt kann der Begriff Chiffre auch auf einen Kernalgorithmus verweisen, aus dem man kryptographische Schemata konstruieren kann. Dazu können verschiedene Verschlüsselungsalgorithmen gehören, aber auch andere Arten von kryptographischen Schemata. Diese Bedeutung des Begriffs wird im Kontext von Blockchiffren relevant (siehe den Abschnitt „Blockchiffren“ unten).

Sie werden auch auf die Begriffe **verschlüsseln** oder **entschlüsseln** stoßen. Diese Begriffe sind einfach Synonyme für Verschlüsselung und Entschlüsselung.

## Brute-Force-Angriffe und Kerckhoffs Prinzip
<chapterId>2d73ef97-26c5-5d11-8815-0ddbe89c8003</chapterId>

Die Verschiebungschiffre ist ein sehr unsicheres symmetrisches Verschlüsselungsschema, zumindest in der modernen Welt. [1] Ein Angreifer könnte einfach versuchen, jeden Chiffretext mit allen 26 möglichen Schlüsseln zu entschlüsseln, um zu sehen, welches Ergebnis Sinn macht. Diese Art von Angriff, bei der der Angreifer einfach durch Schlüssel zyklisiert, um zu sehen, was funktioniert, ist als **Brute-Force-Angriff** oder **exhaustive Schlüsselsuche** bekannt.

Damit ein Verschlüsselungsschema eine minimale Vorstellung von Sicherheit erfüllt, muss es eine Menge möglicher Schlüssel oder **Schlüsselraum** haben, der so groß ist, dass Brute-Force-Angriffe nicht machbar sind. Alle modernen Verschlüsselungsschemata erfüllen diesen Standard. Dies ist als das **Prinzip des ausreichenden Schlüsselraums** bekannt. Ein ähnliches Prinzip gilt typischerweise in verschiedenen Arten von kryptographischen Schemata.

Um ein Gefühl für die massive Größe des Schlüsselraums in modernen Verschlüsselungsschemata zu bekommen, nehmen wir an, dass eine Datei mit einem 128-Bit-Schlüssel unter Verwendung des Advanced Encryption Standard verschlüsselt wurde. Das bedeutet, dass ein Angreifer eine Menge von $2^{128}$ Schlüsseln durchgehen muss, um einen Brute-Force-Angriff durchzuführen. Eine Erfolgschance von 0,78 % mit dieser Strategie würde erfordern, dass der Angreifer etwa $2.65 \times 10^{36}$ Schlüssel durchprobiert.

Nehmen wir optimistisch an, dass ein Angreifer $10^{16}$ Schlüssel pro Sekunde (d.h. 10 Billiarden Schlüssel pro Sekunde) versuchen kann. Um 0,78 % aller Schlüssel im Schlüsselraum zu testen, müsste ihr Angriff $2.65 \times 10^{20}$ Sekunden dauern. Das sind etwa 8,4 Billionen Jahre. Also ist selbst ein Brute-Force-Angriff durch einen absurd mächtigen Gegner mit einem modernen 128-Bit-Verschlüsselungsschema nicht realistisch. Dies ist das Prinzip des ausreichenden Schlüsselraums in Aktion.

Ist die Verschiebungschiffre sicherer, wenn der Angreifer den Verschlüsselungsalgorithmus nicht kennt? Vielleicht, aber nicht viel.
In jedem Fall geht die moderne Kryptografie immer davon aus, dass die Sicherheit eines jeden symmetrischen Verschlüsselungsverfahrens nur darauf beruht, den privaten Schlüssel geheim zu halten. Es wird immer angenommen, dass der Angreifer alle anderen Details kennt, einschließlich des Nachrichtenraums, des Schlüsselraums, des Chiffretext-Raums, des Schlüsselauswahlalgorithmus, des Verschlüsselungsalgorithmus und des Entschlüsselungsalgorithmus.
Die Idee, dass die Sicherheit eines symmetrischen Verschlüsselungsverfahrens nur auf der Geheimhaltung des privaten Schlüssels beruhen kann, ist als **Kerckhoffs’ Prinzip** bekannt.

Wie ursprünglich von Kerckhoffs beabsichtigt, gilt das Prinzip nur für symmetrische Verschlüsselungsverfahren. Eine allgemeinere Version des Prinzips gilt jedoch auch für alle anderen modernen Arten von kryptografischen Verfahren: Das Design eines kryptografischen Verfahrens darf nicht geheim sein, damit es sicher ist; die Geheimhaltung kann sich nur auf einige Informationsstränge, typischerweise einen privaten Schlüssel, erstrecken.

Kerckhoffs’ Prinzip ist aus vier Gründen zentral für die moderne Kryptografie. [2] Erstens gibt es nur eine begrenzte Anzahl von kryptografischen Verfahren für bestimmte Arten von Anwendungen. Zum Beispiel verwenden die meisten modernen symmetrischen Verschlüsselungsanwendungen den Rijndael-Zypher. Die Geheimhaltung bezüglich des Designs eines Verfahrens ist also sehr begrenzt. Es gibt jedoch viel mehr Flexibilität, einen privaten Schlüssel für den Rijndael-Zypher geheim zu halten.

Zweitens ist es einfacher, einige Informationsstränge zu ersetzen als ein ganzes kryptografisches Verfahren. Nehmen wir an, dass alle Mitarbeiter eines Unternehmens die gleiche Verschlüsselungssoftware haben und dass jeweils zwei Mitarbeiter einen privaten Schlüssel haben, um vertraulich zu kommunizieren. Kompromisse bei Schlüsseln sind in diesem Szenario ein Problem, aber zumindest könnte das Unternehmen die Software bei solchen Sicherheitsverletzungen behalten. Wenn das Unternehmen auf die Geheimhaltung des Verfahrens angewiesen wäre, würde jede Verletzung dieser Geheimhaltung den Ersatz aller Software erfordern.

Drittens ermöglicht Kerckhoffs’ Prinzip die Standardisierung und Kompatibilität zwischen Benutzern kryptografischer Verfahren. Dies hat massive Vorteile für die Effizienz. Es ist zum Beispiel schwer vorstellbar, wie Millionen von Menschen jeden Tag sicher mit den Webservern von Google verbinden könnten, wenn diese Sicherheit die Geheimhaltung kryptografischer Verfahren erfordern würde.

Viertens ermöglicht Kerckhoffs’ Prinzip die öffentliche Überprüfung kryptografischer Verfahren. Diese Art der Überprüfung ist absolut notwendig, um sichere kryptografische Verfahren zu erreichen. Veranschaulichend war der Hauptalgorithmus in der symmetrischen Kryptografie, der Rijndael-Zypher, das Ergebnis eines Wettbewerbs, der zwischen 1997 und 2000 vom National Institute of Standards and Technology organisiert wurde.

Jedes System, das versucht, **Sicherheit durch Obskurität** zu erreichen, ist eines, das darauf angewiesen ist, die Details seines Designs und/oder seiner Implementierung geheim zu halten. In der Kryptografie wäre dies speziell ein System, das darauf angewiesen ist, die Designdetails des kryptografischen Verfahrens geheim zu halten. Sicherheit durch Obskurität steht also im direkten Gegensatz zu Kerckhoffs’ Prinzip.

Die Fähigkeit der Offenheit, Qualität und Sicherheit zu stärken, erstreckt sich auch breiter auf die digitale Welt als nur auf die Kryptografie. Freie und Open-Source-Linux-Distributionen wie Debian haben beispielsweise im Vergleich zu ihren Windows- und MacOS-Pendants mehrere Vorteile in Bezug auf Privatsphäre, Stabilität, Sicherheit und Flexibilität. Während das mehrere Ursachen haben mag, ist das wichtigste Prinzip wahrscheinlich, wie Eric Raymond es in seinem berühmten Essay "Die Kathedrale und der Basar" formulierte, dass "bei genügend Augenpaaren alle Fehler oberflächlich sind." [3] Es ist dieses Weisheit-der-Vielen-Prinzip, das Linux seinen größten Erfolg bescherte.
Man kann nie eindeutig sagen, dass ein kryptografisches Schema "sicher" oder "unsicher" ist. Stattdessen gibt es verschiedene Sicherheitsbegriffe für kryptografische Schemata. Jede **Definition von kryptografischer Sicherheit** muss (1) Sicherheitsziele sowie (2) die Fähigkeiten eines Angreifers spezifizieren. Die Analyse kryptografischer Schemata anhand einer oder mehrerer spezifischer Sicherheitsbegriffe bietet Einblicke in ihre Anwendungen und Grenzen.
Obwohl wir nicht alle Details der verschiedenen Sicherheitsbegriffe der Kryptografie erörtern werden, sollten Sie wissen, dass zwei Annahmen allen modernen kryptografischen Sicherheitsbegriffen bezüglich symmetrischer und asymmetrischer Schemata (und in gewisser Form auch anderen kryptografischen Primitiven) allgegenwärtig sind:

* Das Wissen des Angreifers über das Schema entspricht dem Kerckhoffs’schen Prinzip.
* Der Angreifer kann keinen Brute-Force-Angriff auf das Schema durchführbar ausführen. Insbesondere erlauben die Bedrohungsmodelle kryptografischer Sicherheitsbegriffe normalerweise nicht einmal Brute-Force-Angriffe, da sie annehmen, dass diese keine relevante Überlegung sind.

**Notizen:**

[1] Nach Seutonius wurde von Julius Caesar in seiner militärischen Kommunikation ein Verschiebechiffre mit einem konstanten Schlüsselwert von 3 verwendet. So würde A immer zu D, B immer zu E, C immer zu F und so weiter. Diese besondere Version des Verschiebechiffres ist daher als **Caesar-Chiffre** bekannt geworden (obwohl es im modernen Sinne des Wortes nicht wirklich eine Chiffre ist, da der Schlüsselwert konstant ist). Die Caesar-Chiffre mag im ersten Jahrhundert v. Chr. sicher gewesen sein, wenn Roms Feinde sehr unvertraut mit Verschlüsselung waren. Aber in der modernen Zeit wäre es klarerweise kein sehr sicheres Schema.

[2] Jonathan Katz und Yehuda Lindell, _Einführung in die moderne Kryptografie_, CRC Press (Boca Raton, FL: 2015), S. 7f.

[3] Eric Raymond, „Die Kathedrale und der Basar“, Vortrag gehalten auf dem Linux Kongress, Würzburg, Deutschland (27. Mai 1997). Es gibt eine Reihe von nachfolgenden Versionen sowie ein Buch. Meine Zitate stammen von Seite 30 im Buch: Eric Raymond, _Die Kathedrale und der Basar: Gedanken zu Linux und Open Source von einem unfreiwilligen Revolutionär_, überarbeitete Ausg. (2001), O’Reilly: Sebastopol, CA.

## Stromchiffren
<chapterId>479aa6f4-45c4-59ca-8616-8cf8e61fc871</chapterId>

Symmetrische Verschlüsselungsschemata werden üblicherweise in zwei Typen unterteilt: **Stromchiffren** und **Blockchiffren**. Diese Unterscheidung ist jedoch etwas problematisch, da die Begriffe auf inkonsistente Weise verwendet werden. In den nächsten Abschnitten werde ich die Unterscheidung so darlegen, wie ich sie für am besten halte. Sie sollten sich jedoch bewusst sein, dass viele Menschen diese Begriffe etwas anders verwenden werden, als ich es darlege.

Beginnen wir zunächst mit Stromchiffren. Eine **Stromchiffre** ist ein symmetrisches Verschlüsselungsschema, bei dem die Verschlüsselung aus zwei Schritten besteht.

Zuerst wird über einen privaten Schlüssel eine Zeichenfolge erzeugt, die so lang wie der Klartext ist. Diese Zeichenfolge wird als **Schlüsselstrom** bezeichnet.

Anschließend wird der Schlüsselstrom mathematisch mit dem Klartext kombiniert, um einen Chiffretext zu erzeugen. Diese Kombination ist typischerweise eine XOR-Operation. Für die Entschlüsselung können Sie einfach die Operation umkehren. (Beachten Sie, dass $A \oplus B = B \oplus A$ im Fall, dass $A$ und $B$ Bitfolgen sind. Die Reihenfolge einer XOR-Operation in einer Stromchiffre spielt also für das Ergebnis keine Rolle. Diese Eigenschaft ist als **Kommutativität** bekannt.)
Ein typisches XOR-Stream-Chiffre wird in *Abbildung 3* dargestellt. Zuerst nehmen Sie einen privaten Schlüssel $K$ und verwenden ihn, um einen Schlüsselstrom zu generieren. Der Schlüsselstrom wird dann mit dem Klartext über eine XOR-Operation kombiniert, um den Chiffretext zu erzeugen. Jeder Agent, der den Chiffretext erhält, kann ihn leicht entschlüsseln, wenn er den Schlüssel $K$ hat. Alles, was sie tun muss, ist, einen Schlüsselstrom zu erstellen, der so lang wie der Chiffretext ist, gemäß dem spezifizierten Verfahren des Schemas und ihn mit dem Chiffretext zu XOR-en.

*Abbildung 3: Ein XOR-Stream-Chiffre*

![Abbildung 3: Ein XOR-Stream-Chiffre](assets/Figure4-3.webp "Abbildung 3: Ein XOR-Stream-Chiffre")

Es sei daran erinnert, dass ein Verschlüsselungsschema typischerweise eine Vorlage für die Verschlüsselung mit demselben Kernalgorithmus ist, anstatt eine exakte Spezifikation. Entsprechend ist ein Stream-Chiffre typischerweise eine Vorlage für die Verschlüsselung, bei der Sie Schlüssel unterschiedlicher Länge verwenden können. Obwohl die Schlüssellänge einige kleinere Details des Schemas beeinflussen kann, wird sie seine wesentliche Form nicht beeinflussen.

Das Shift-Chiffre ist ein Beispiel für ein sehr einfaches und unsicheres Stream-Chiffre. Mit einem einzigen Buchstaben (dem privaten Schlüssel) können Sie eine Reihe von Buchstaben in der Länge der Nachricht (den Schlüsselstrom) produzieren. Dieser Schlüsselstrom wird dann mit dem Klartext über eine Modulo-Operation kombiniert, um den Chiffretext zu erzeugen. (Diese Modulo-Operation kann zu einer XOR-Operation vereinfacht werden, wenn die Buchstaben in Bits dargestellt werden).

Ein weiteres berühmtes Beispiel für ein Stream-Chiffre ist das **Vigenère-Chiffre**, nach Blaise de Vigenère, der es am Ende des 16. Jahrhunderts vollständig entwickelte (obwohl andere bereits viel Vorarbeit geleistet hatten). Es ist ein Beispiel für ein **polyalphabetisches Substitutionschiffre**: ein Verschlüsselungsschema, bei dem das Chiffretext-Alphabet für ein Klartextsymbol je nach seiner Position im Text wechselt. Im Gegensatz zu einem monoalphabetischen Substitutionschiffre können Chiffretextsymbole mit mehr als einem Klartextsymbol in Verbindung gebracht werden.

Als die Verschlüsselung im Renaissance-Europa an Popularität gewann, tat dies auch die **Kryptoanalyse** – das heißt, das Brechen von Chiffretexten – insbesondere unter Verwendung der **Frequenzanalyse**. Letztere verwendet statistische Regelmäßigkeiten in unserer Sprache, um Chiffretexte zu brechen, und wurde bereits im neunten Jahrhundert von arabischen Gelehrten entdeckt. Es ist eine Technik, die besonders gut bei längeren Texten funktioniert. Und selbst die ausgefeiltesten monoalphabetischen Substitutionschiffren waren im Europa des 18. Jahrhunderts, insbesondere im militärischen und sicherheitstechnischen Bereich, nicht mehr ausreichend gegen die Frequenzanalyse. Da das Vigenère-Chiffre einen signifikanten Fortschritt in der Sicherheit bot, wurde es in dieser Zeit beliebt und war bis zum späten 18. Jahrhundert weit verbreitet.

Informell gesprochen funktioniert das Verschlüsselungsschema wie folgt:

1. Wählen Sie ein Mehrbuchstabenwort als privaten Schlüssel.
2. Wenden Sie für jede Nachricht das Shift-Chiffre auf jeden Buchstaben der Nachricht an, indem Sie den entsprechenden Buchstaben im Schlüsselwort als Verschiebung verwenden.
3. Wenn Sie das Schlüsselwort durchlaufen haben, aber den Klartext noch nicht vollständig verschlüsselt haben, wenden Sie erneut die Buchstaben des Schlüsselworts als Shift-Chiffre auf die entsprechenden Buchstaben im Rest des Textes an.
4. Fahren Sie mit diesem Prozess fort, bis die gesamte Nachricht verschlüsselt wurde.

Um zu veranschaulichen, nehmen wir an, Ihr privater Schlüssel ist "GOLD" und Sie möchten die Nachricht "CRYPTOGRAPHY" verschlüsseln. In diesem Fall würden Sie wie folgt nach dem Vigenère-Chiffre vorgehen:

- $c_0  = [(2 + 6) \mod 26] = 8 = I$
- $c_1  = [(17 + 14) \mod 26] = 5 = F$
- $c_2  = [(24 + 11) \mod 26] = 9 = J$
- $c_3 = [(15 + 3) \mod 26] = 18 = S$
- $c_4 = [(19 + 6) \mod 26] = 25 = Z$
- $c_5 = [(14 + 14) \mod 26] = 2 = C$
- $c_6 = [(6 + 11) \mod 26] = 17 = R$
- $c_7 = [(17 + 3) \mod 26] = 20 = U$
- $c_8 = [(0 + 6) \mod 26] = 6 = G$
- $c_9 = [(15 + 14) \mod 26] = 3 = D$
- $c_{10} = [(7 + 11) \mod 26] = 18 = S$
- $c_{11} = [(24 + 3) \mod 26] = 1 = B$

Somit ist der Geheimtext $c$ = "IFJSZCRUGDSB".

Ein weiteres berühmtes Beispiel für eine Stromchiffre ist das **One-Time-Pad**. Beim One-Time-Pad erstellt man einfach eine Zeichenfolge aus zufälligen Bits, die so lang wie die Klartextnachricht ist, und erzeugt den Geheimtext über die XOR-Operation. Daher sind der private Schlüssel und der Schlüsselstrom bei einem One-Time-Pad identisch.

Während die Verschiebechiffre und die Vigenère-Chiffre in der heutigen Zeit sehr unsicher sind, ist das One-Time-Pad sehr sicher, wenn es korrekt verwendet wird. Wahrscheinlich die berühmteste Anwendung des One-Time-Pads war, zumindest bis in die 1980er Jahre, für die **Washington-Moskau-Hotline**. [4]

Die Hotline ist eine direkte Kommunikationsverbindung zwischen Washington und Moskau für dringende Angelegenheiten, die nach der Kubakrise eingerichtet wurde. Die Technologie dafür hat sich im Laufe der Jahre gewandelt. Derzeit umfasst sie ein direktes Glasfaserkabel sowie zwei Satellitenverbindungen (zur Redundanz), die E-Mail und Textnachrichten ermöglichen. Die Verbindung endet an verschiedenen Orten in den USA. Das Pentagon, das Weiße Haus und der Raven Rock Mountain sind bekannte Endpunkte. Entgegen der landläufigen Meinung hat die Hotline nie Telefone involviert.

Im Wesentlichen funktionierte das One-Time-Pad-System wie folgt. Sowohl Washington als auch Moskau hätten zwei Sätze von Zufallszahlen. Ein Satz von Zufallszahlen, erstellt von den Russen, bezog sich auf die Verschlüsselung und Entschlüsselung von Nachrichten in russischer Sprache. Ein Satz von Zufallszahlen, erstellt von den Amerikanern, bezog sich auf die Verschlüsselung und Entschlüsselung von Nachrichten in englischer Sprache. Von Zeit zu Zeit würden weitere Zufallszahlen durch vertrauenswürdige Kuriere an die andere Seite geliefert.

Washington und Moskau konnten dann geheim kommunizieren, indem sie diese Zufallszahlen zur Erstellung von One-Time-Pads verwendeten. Jedes Mal, wenn Sie kommunizieren mussten, würden Sie den nächsten Teil der Zufallszahlen für Ihre Nachricht verwenden.

Obwohl sehr sicher, sieht sich das One-Time-Pad signifikanten praktischen Einschränkungen gegenüber: Der Schlüssel muss so lang wie die Nachricht sein und kein Teil eines One-Time-Pads darf wiederverwendet werden. Das bedeutet, dass Sie den Überblick behalten müssen, wo Sie im One-Time-Pad sind, eine massive Anzahl von Bits speichern und von Zeit zu Zeit zufällige Bits mit Ihren Gegenparteien austauschen müssen. Als Konsequenz wird das One-Time-Pad in der Praxis nicht häufig verwendet.

Stattdessen sind **pseudorandomisierte Stromchiffren** die in der Praxis vorherrschenden Stromchiffren. Salsa20 und eine eng verwandte Variante namens ChaCha sind Beispiele für häufig verwendete pseudorandomisierte Stromchiffren.
Bei diesen Pseudozufallsstromchiffren wählen Sie zunächst zufällig einen Schlüssel K aus, der kürzer als die Länge des Klartextes ist. Ein solcher zufälliger Schlüssel K wird üblicherweise von unserem Computer auf der Basis von unvorhersehbaren Daten erstellt, die er im Laufe der Zeit sammelt, wie die Zeit zwischen Netzwerknachrichten, Mausbewegungen und so weiter.
Dieser zufällige Schlüssel $K$ wird dann in einen Expansionsalgorithmus eingesetzt, der einen pseudozufälligen Schlüsselstrom erzeugt, der so lang wie die Nachricht ist. Sie können genau festlegen, wie lang der Schlüsselstrom sein muss (z.B. 500 Bits, 1000 Bits, 1200 Bits, 29.117 Bits und so weiter).

Ein pseudozufälliger Schlüsselstrom erscheint *als ob* er vollständig zufällig aus der Menge aller Strings gleicher Länge ausgewählt wurde. Daher erscheint die Verschlüsselung mit einem pseudozufälligen Schlüsselstrom, als wäre sie mit einem Einmalschlüssel durchgeführt worden. Aber das ist natürlich nicht der Fall.

Da unser privater Schlüssel kürzer als der Schlüsselstrom ist und unser Expansionsalgorithmus deterministisch sein muss, damit der Verschlüsselungs-/Entschlüsselungsprozess funktioniert, könnte nicht jeder Schlüsselstrom dieser bestimmten Länge als Ausgabe aus unserer Expansionsoperation resultiert haben.

Nehmen wir beispielsweise an, dass unser privater Schlüssel eine Länge von 128 Bits hat und dass wir ihn in einen Expansionsalgorithmus einsetzen können, um einen viel längeren Schlüsselstrom zu erzeugen, sagen wir von 2.500 Bits. Da unser Expansionsalgorithmus deterministisch sein muss, kann unser Algorithmus höchstens $1/2^{128}$ Strings mit einer Länge von 2.500 Bits auswählen. Ein solcher Schlüsselstrom könnte also niemals vollständig zufällig aus allen Strings derselben Länge ausgewählt werden.

Unsere Definition einer Stromchiffre hat zwei Aspekte: (1) ein Schlüsselstrom, der so lang wie der Klartext ist, wird mit Hilfe eines privaten Schlüssels erzeugt; und (2) dieser Schlüsselstrom wird mit dem Klartext kombiniert, typischerweise über eine XOR-Operation, um den Chiffretext zu erzeugen.

Manchmal definieren Leute Bedingung (1) strenger, indem sie behaupten, dass der Schlüsselstrom spezifisch pseudozufällig sein muss. Das bedeutet, dass weder die Verschiebechiffre noch der Einmalschlüssel als Stromchiffren betrachtet würden.

Meiner Ansicht nach bietet die breitere Definition von Bedingung (1) eine einfachere Möglichkeit, Verschlüsselungsschemata zu organisieren. Darüber hinaus bedeutet es, dass wir nicht aufhören müssen, ein bestimmtes Verschlüsselungsschema als Stromchiffre zu bezeichnen, nur weil wir erfahren, dass es tatsächlich nicht auf pseudozufälligen Schlüsselströmen basiert.

**Notizen:**

[4] Crypto Museum, "Washington-Moskau-Hotline," 2013, verfügbar unter [https://www.cryptomuseum.com/crypto/hotline/index.htm](https://www.cryptomuseum.com/crypto/hotline/index.htm).

## Blockchiffren
<chapterId>2df52d51-943d-5df7-9d49-333e4c5d97b7</chapterId>

Die erste Art, wie eine **Blockchiffre** allgemein verstanden wird, ist als etwas Primitiveres als eine Stromchiffre: Ein Kernalgorithmus, der eine längenerhaltende Transformation an einem String einer geeigneten Länge mit Hilfe eines Schlüssels durchführt. Dieser Algorithmus kann für die Erstellung von Verschlüsselungsschemata und vielleicht anderen Arten von kryptografischen Schemata verwendet werden.
Häufig kann ein Blockchiffre Eingabestrings unterschiedlicher Länge wie 64, 128 oder 256 Bits sowie Schlüssel unterschiedlicher Länge wie 128, 192 oder 256 Bits verarbeiten. Obwohl sich einige Details des Algorithmus je nach diesen Variablen ändern können, ändert sich der Kernalgorithmus nicht. Würde er sich ändern, sprächen wir von zwei verschiedenen Blockchiffren. Beachten Sie, dass die Verwendung der Terminologie des Kernalgorithmus hier dieselbe ist wie bei Verschlüsselungsschemata.
Eine Darstellung, wie ein Blockchiffre funktioniert, kann in *Abbildung 4* unten gesehen werden. Eine Nachricht $M$ der Länge $L$ und ein Schlüssel $K$ dienen als Eingaben für den Blockchiffre. Er gibt eine Nachricht $M'$ der Länge $L$ aus. Der Schlüssel muss nicht unbedingt dieselbe Länge wie $M$ und $M'$ haben, bei den meisten Blockchiffren.

*Abbildung 4: Ein Blockchiffre*

![Abbildung 4: Ein Blockchiffre](assets/Figure4-4.webp "Abbildung 4: Ein Blockchiffre")

Ein Blockchiffre allein ist kein Verschlüsselungsschema. Aber ein Blockchiffre kann mit verschiedenen **Betriebsmodi** verwendet werden, um unterschiedliche Verschlüsselungsschemata zu erzeugen. Ein Betriebsmodus fügt einfach einige zusätzliche Operationen außerhalb des Blockchiffres hinzu.

Um zu veranschaulichen, wie das funktioniert, nehmen wir an, ein Blockchiffre (BC), der einen 128-Bit-Eingabestring und einen 128-Bit-Privatschlüssel benötigt. Abbildung 5 unten zeigt, wie dieser Blockchiffre mit dem **Electronic Code Book Modus** (**ECB-Modus**) verwendet werden kann, um ein Verschlüsselungsschema zu erstellen. (Die Ellipsen auf der rechten Seite deuten an, dass Sie dieses Muster so lange wiederholen können, wie es benötigt wird).

*Abbildung 5: Ein Blockchiffre mit ECB-Modus*

![Abbildung 5: Ein Blockchiffre mit ECB-Modus](assets/Figure4-5.webp "Abbildung 5: Ein Blockchiffre mit ECB-Modus")

Der Prozess für die Electronic Code Book-Verschlüsselung mit dem Blockchiffre ist wie folgt. Sehen Sie, ob Sie Ihre Klartextnachricht in 128-Bit-Blöcke aufteilen können. Wenn nicht, fügen Sie der Nachricht **Padding** hinzu, sodass das Ergebnis gleichmäßig durch die Blockgröße von 128 Bits geteilt werden kann. Das sind Ihre Daten, die für den Verschlüsselungsprozess verwendet werden.

Teilen Sie nun die Daten in 128-Bit-Strings ($M_1$, $M_2$, $M_3$ und so weiter) auf. Führen Sie jeden 128-Bit-String durch den Blockchiffre mit Ihrem 128-Bit-Schlüssel, um 128-Bit-Blöcke von Ciphertext ($C_1$, $C_2$, $C_3$ und so weiter) zu erzeugen. Diese Blöcke, wenn sie wieder zusammengesetzt werden, bilden den vollständigen Ciphertext.

Die Entschlüsselung ist einfach der umgekehrte Prozess, obwohl der Empfänger eine erkennbare Möglichkeit benötigt, um jedes Padding aus den entschlüsselten Daten zu entfernen und die ursprüngliche Klartextnachricht zu produzieren.

Obwohl relativ einfach, mangelt es einem Blockchiffre mit Electronic Code Book-Modus an Sicherheit. Dies liegt daran, dass es zu **deterministischer Verschlüsselung** führt. Zwei identische 128-Bit-Strings von Daten werden genau auf die gleiche Weise verschlüsselt. Diese Information kann ausgenutzt werden.

Stattdessen sollte jedes aus einem Blockchiffre konstruierte Verschlüsselungsschema **probabilistisch** sein: das heißt, die Verschlüsselung einer beliebigen Nachricht $M$ oder eines bestimmten Teils von $M$ sollte im Allgemeinen jedes Mal ein anderes Ergebnis liefern. [5]

Der **Cipher Block Chaining-Modus** (**CBC-Modus**) ist wahrscheinlich der am häufigsten verwendete Modus mit einem Blockchiffre. Die Kombination, wenn richtig durchgeführt, erzeugt ein probabilistisches Verschlüsselungsschema. Sie können eine Darstellung dieses Betriebsmodus in *Abbildung 6* unten sehen.

*Abbildung 6: Ein Blockchiffre mit CBC-Modus*
![Abbildung 6: Ein Blockverschlüsselungsalgorithmus im CBC-Modus](assets/Figure4-6.webp "Abbildung 6: Ein Blockverschlüsselungsalgorithmus im CBC-Modus")
Nehmen wir an, die Blockgröße beträgt erneut 128 Bit. Um zu beginnen, müssen Sie also erneut sicherstellen, dass Ihre ursprüngliche Klartextnachricht das notwendige Padding erhält.

Dann XOR-verknüpfen Sie den ersten 128-Bit-Teil Ihres Klartextes mit einem **Initialisierungsvektor** von 128 Bit. Das Ergebnis wird in den Blockverschlüsselungsalgorithmus eingespeist, um einen Chiffretext für den ersten Block zu erzeugen. Für den zweiten Block von 128 Bit XOR-verknüpfen Sie zuerst den Klartext mit dem Chiffretext aus dem ersten Block, bevor Sie ihn in den Blockverschlüsselungsalgorithmus einfügen. Diesen Prozess setzen Sie fort, bis Sie Ihre gesamte Klartextnachricht verschlüsselt haben.

Wenn Sie fertig sind, senden Sie die verschlüsselte Nachricht zusammen mit dem unverschlüsselten Initialisierungsvektor an den Empfänger. Der Empfänger muss den Initialisierungsvektor kennen, sonst kann er den Chiffretext nicht entschlüsseln.

Diese Konstruktion ist viel sicherer als der elektronische Codebuch-Modus, wenn sie korrekt verwendet wird. Sie sollten zunächst sicherstellen, dass der Initialisierungsvektor eine zufällige oder pseudozufällige Zeichenfolge ist. Darüber hinaus sollten Sie jedes Mal, wenn Sie dieses Verschlüsselungsschema verwenden, einen anderen Initialisierungsvektor verwenden.

Mit anderen Worten, Ihr Initialisierungsvektor sollte ein zufälliger oder pseudozufälliger Nonce sein, wobei ein **Nonce** für "eine Zahl, die nur einmal verwendet wird", steht. Wenn Sie diese Praxis beibehalten, dann gewährleistet der CBC-Modus mit einem Blockverschlüsselungsalgorithmus, dass zwei identische Klartextblöcke im Allgemeinen jedes Mal unterschiedlich verschlüsselt werden.

Schließlich wenden wir uns dem **Output Feedback-Modus** (**OFB-Modus**) zu. Sie können eine Darstellung dieses Modus in *Abbildung 7* sehen.

*Abbildung 7: Ein Blockverschlüsselungsalgorithmus im OFB-Modus*

![Abbildung 7: Ein Blockverschlüsselungsalgorithmus im OFB-Modus](assets/Figure4-7.webp "Abbildung 7: Ein Blockverschlüsselungsalgorithmus im OFB-Modus")

Im OFB-Modus wählen Sie ebenfalls einen Initialisierungsvektor. Aber hier wird für den ersten Block der Initialisierungsvektor direkt mit Ihrem Schlüssel in den Blockverschlüsselungsalgorithmus eingespeist. Die resultierenden 128 Bit werden dann als Keystream behandelt. Dieser Keystream wird mit dem Klartext XOR-verknüpft, um den Chiffretext für den Block zu erzeugen. Für nachfolgende Blöcke verwenden Sie den Keystream aus dem vorherigen Block als Eingabe in den Blockverschlüsselungsalgorithmus und wiederholen die Schritte.

Wenn Sie genau hinsehen, was hier tatsächlich mit dem Blockverschlüsselungsalgorithmus im OFB-Modus geschaffen wurde, ist ein Stromverschlüsselungsalgorithmus. Sie erzeugen Keystream-Teile von 128 Bit, bis Sie die Länge des Klartextes erreicht haben (wobei Sie die Bits, die Sie vom letzten 128-Bit-Keystream-Teil nicht benötigen, verwerfen). Dann XOR-verknüpfen Sie den Keystream mit Ihrer Klartextnachricht, um den Chiffretext zu erhalten.

Im vorherigen Abschnitt über Stromverschlüsselungsalgorithmen habe ich erwähnt, dass Sie einen Keystream mit Hilfe eines privaten Schlüssels erzeugen. Um genau zu sein, muss er nicht nur mit einem privaten Schlüssel erstellt werden. Wie Sie im OFB-Modus sehen können, wird der Keystream mit Unterstützung sowohl eines privaten Schlüssels als auch eines Initialisierungsvektors erzeugt.

Beachten Sie, dass es wie im CBC-Modus wichtig ist, jedes Mal, wenn Sie einen Blockverschlüsselungsalgorithmus im OFB-Modus verwenden, einen pseudozufälligen oder zufälligen Nonce für den Initialisierungsvektor auszuwählen. Andernfalls wird die gleiche 128-Bit-Nachrichtenfolge, die in verschiedenen Kommunikationen gesendet wird, auf die gleiche Weise verschlüsselt. Dies ist eine Möglichkeit, probabilistische Verschlüsselung mit einem Stromverschlüsselungsalgorithmus zu erstellen.
Einige Stromchiffren verwenden ausschließlich einen privaten Schlüssel, um einen Schlüsselstrom zu erzeugen. Für diese Stromchiffren ist es wichtig, dass Sie einen zufälligen Nonce verwenden, um den privaten Schlüssel für jede Kommunikationsinstanz auszuwählen. Andernfalls werden die Ergebnisse der Verschlüsselung mit diesen Stromchiffren ebenfalls deterministisch sein, was zu Sicherheitsproblemen führt. 
Der beliebteste moderne Blockchiffre ist der **Rijndael-Chiffre**. Er war der Gewinner aus fünfzehn Einreichungen eines Wettbewerbs, der vom National Institute of Standards and Technology (NIST) zwischen 1997 und 2000 abgehalten wurde, um einen älteren Verschlüsselungsstandard, den **Data Encryption Standard** (**DES**), zu ersetzen.

Der Rijndael-Chiffre kann mit verschiedenen Spezifikationen für Schlüssellängen und Blockgrößen sowie in verschiedenen Betriebsmodi verwendet werden. Das Komitee für den NIST-Wettbewerb hat eine eingeschränkte Version des Rijndael-Chiffres angenommen – nämlich eine, die 128-Bit-Blockgrößen und Schlüssellängen von entweder 128 Bits, 192 Bits oder 256 Bits erfordert – als Teil des **Advanced Encryption Standard** (**AES**). Dies ist wirklich der Hauptstandard für symmetrische Verschlüsselungsanwendungen. Er ist so sicher, dass sogar die NSA bereit zu sein scheint, ihn mit 256-Bit-Schlüsseln für streng geheime Dokumente zu verwenden. [6]

Der AES-Blockchiffre wird in *Kapitel 5* detailliert erklärt.


**Anmerkungen:**

[5] Die Bedeutung der probabilistischen Verschlüsselung wurde erstmals von Shafi Goldwasser und Silvio Micali hervorgehoben, „Probabilistic encryption“, _Journal of Computer and System Sciences_, 28 (1984), 270–99.

[6] Siehe NSA, "Commercial National Security Algorithm Suite", [https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm](https://apps.nsa.gov/iaarchive/programs/iad-initiatives/cnsa-suite.cfm).



## Klärung der Verwirrung
<chapterId>121c1858-27e3-5862-b0ce-4ff2f70f9f0f</chapterId>

Die Verwirrung über den Unterschied zwischen Blockchiffren und Stromchiffren entsteht, weil manchmal der Begriff Blockchiffre speziell als Bezeichnung für einen *Blockchiffre mit einem Blockmodus der Verschlüsselung* verstanden wird.

Betrachten Sie die ECB- und CBC-Modi im vorherigen Abschnitt. Diese erfordern speziell, dass die Daten für die Verschlüsselung durch die Blockgröße teilbar sind (was bedeutet, dass Sie möglicherweise Padding für die ursprüngliche Nachricht verwenden müssen). Darüber hinaus werden die Daten in diesen Modi auch direkt vom Blockchiffre bearbeitet (und nicht nur mit dem Ergebnis einer Blockchiffre-Operation kombiniert, wie im OFB-Modus).

Daher können Sie alternativ einen **Blockchiffre** als jedes Verschlüsselungsschema definieren, das auf festen Blocklängen der Nachricht auf einmal operiert (wobei jeder Block länger als ein Byte sein muss, sonst fällt es in einen Stromchiffre). Sowohl die Daten für die Verschlüsselung als auch der Chiffretext müssen sich gleichmäßig in diese Blockgröße teilen. Typischerweise ist die Blockgröße 64, 128, 192 oder 256 Bits lang. Im Gegensatz dazu kann ein Stromchiffre Nachrichten in Stücken von einem Bit oder Byte auf einmal verschlüsseln.

Mit diesem spezifischeren Verständnis von Blockchiffre können Sie tatsächlich behaupten, dass moderne Verschlüsselungsschemata entweder Strom- oder Blockchiffren sind. Von nun an werde ich den Begriff Blockchiffre im allgemeineren Sinne verwenden, sofern nicht anders angegeben.
Die Diskussion über den OFB-Modus im vorherigen Abschnitt wirft auch einen weiteren interessanten Punkt auf. Einige Stromchiffren werden aus Blockchiffren gebaut, wie Rijndael mit OFB. Andere, wie Salsa20 und ChaCha, werden nicht aus Blockchiffren erstellt. Man könnte die letzteren als **primitive Stromchiffren** bezeichnen. (Es gibt eigentlich keinen standardisierten Begriff, um solche Stromchiffren zu bezeichnen.)
Wenn Leute über die Vor- und Nachteile von Stromchiffren und Blockchiffren sprechen, vergleichen sie typischerweise primitive Stromchiffren mit Verschlüsselungsschemata, die auf Blockchiffren basieren.

Während man immer leicht eine Stromchiffre aus einer Blockchiffre konstruieren kann, ist es typischerweise sehr schwierig, irgendeine Art von Konstrukt mit einem Blockmodus der Verschlüsselung (wie mit CBC-Modus) aus einer primitiven Stromchiffre zu bauen.

Aus dieser Diskussion sollten Sie nun *Abbildung 8* verstehen. Sie bietet einen Überblick über symmetrische Verschlüsselungsschemata. Wir verwenden drei Arten von Verschlüsselungsschemata: primitive Stromchiffren, Blockchiffre-Stromchiffren und Blockchiffren im Blockmodus (auch „Blockchiffren“ im Diagramm genannt).

*Abbildung 8: Überblick über symmetrische Verschlüsselungsschemata*

![Abbildung 8: Überblick über symmetrische Verschlüsselungsschemata](assets/Figure4-8.webp "Abbildung 8: Überblick über symmetrische Verschlüsselungsschemata")

## Nachrichtenauthentifizierungscodes
<chapterId>19fa7c00-db59-56a0-9654-5350a137939d</chapterId>

Verschlüsselung befasst sich mit Geheimhaltung. Aber Kryptographie befasst sich auch mit breiteren Themen, wie Nachrichtenintegrität, Authentizität und Nichtabstreitbarkeit. Sogenannte **Nachrichtenauthentifizierungscodes** (MACs) sind symmetrische kryptographische Schemata, die Authentizität und Integrität in der Kommunikation unterstützen.

Warum ist etwas anderes als Geheimhaltung in der Kommunikation notwendig? Nehmen wir an, Bob sendet Alice eine Nachricht mit praktisch unknackbarer Verschlüsselung. Jeder Angreifer, der diese Nachricht abfängt, wird keine signifikanten Einblicke in den Inhalt erhalten können. Dennoch hat der Angreifer mindestens zwei andere Angriffsvektoren zur Verfügung:

1. Sie könnte den Ciphertext abfangen, dessen Inhalt ändern und den veränderten Ciphertext an Alice weiterleiten.
2. Sie könnte Bobs Nachricht vollständig blockieren und ihren eigenen erstellten Ciphertext senden.

In beiden Fällen könnte der Angreifer möglicherweise keine Einblicke in die Inhalte aus den Ciphertexts (1) und (2) haben. Aber sie könnte auf diese Weise immer noch erheblichen Schaden anrichten. Hier werden Nachrichtenauthentifizierungscodes wichtig.

Nachrichtenauthentifizierungscodes werden locker als symmetrische kryptographische Schemata mit drei Algorithmen definiert: einem Schlüsselgenerierungsalgorithmus, einem Tag-Generierungsalgorithmus und einem Verifizierungsalgorithmus. Ein sicherer MAC stellt sicher, dass Tags für jeden Angreifer **existenziell unfälschbar** sind – das heißt, sie können keinen Tag für die Nachricht erfolgreich erstellen, der verifiziert, es sei denn, sie haben den privaten Schlüssel.

Bob und Alice können die Manipulation einer bestimmten Nachricht mit einem MAC bekämpfen. Nehmen wir für den Moment an, dass sie sich nicht um die Geheimhaltung kümmern. Sie wollen nur sicherstellen, dass die von Alice empfangene Nachricht tatsächlich von Bob stammt und in keiner Weise verändert wurde.

Der Prozess ist in *Abbildung 9* dargestellt. Um einen **MAC** (Message Authentication Code) zu verwenden, würden sie zuerst einen privaten Schlüssel $K$ generieren, der zwischen ihnen beiden geteilt wird. Bob erstellt einen Tag $T$ für die Nachricht mit dem privaten Schlüssel $K$. Dann sendet er die Nachricht sowie den Nachrichtentag an Alice. Sie kann dann verifizieren, dass Bob tatsächlich den Tag erstellt hat, indem sie den privaten Schlüssel, die Nachricht und den Tag durch einen Verifizierungsalgorithmus laufen lässt.

*Abbildung 9: Überblick über symmetrische Verschlüsselungsschemata*
![Abbildung 9: Übersicht über symmetrische Verschlüsselungsverfahren](assets/Figure4-9.webp "Abbildung 9: Übersicht über symmetrische Verschlüsselungsverfahren")
Aufgrund der **existenziellen Unfälschbarkeit** kann ein Angreifer die Nachricht $M$ in keiner Weise verändern oder eine eigene Nachricht mit einem gültigen Tag erstellen. Dies gilt selbst dann, wenn der Angreifer die Tags vieler Nachrichten zwischen Bob und Alice beobachtet, die denselben privaten Schlüssel verwenden. Höchstens könnte ein Angreifer verhindern, dass Alice die Nachricht $M$ erhält (ein Problem, das die Kryptographie nicht adressieren kann).

Ein MAC garantiert, dass eine Nachricht tatsächlich von Bob erstellt wurde. Diese Authentizität impliziert automatisch die Integrität der Nachricht – das heißt, wenn Bob eine Nachricht erstellt hat, dann wurde sie faktisch in keiner Weise von einem Angreifer verändert. Von hier an sollte jede Sorge um Authentifizierung automatisch als Sorge um Integrität verstanden werden.

Obwohl ich in meiner Diskussion eine Unterscheidung zwischen Nachrichtenauthentizität und -integrität getroffen habe, ist es auch üblich, diese Begriffe synonym zu verwenden. Sie beziehen sich dann auf die Idee von Nachrichten, die sowohl von einem bestimmten Absender erstellt wurden als auch in keiner Weise verändert wurden. In diesem Sinne werden Nachrichtenauthentifizierungscodes häufig auch als **Nachrichtenintegritätscodes** bezeichnet.

## Authentifizierte Verschlüsselung
<chapterId>33f2ec9b-9fb4-5c61-8fb4-50836270a144</chapterId>

Typischerweise möchte man sowohl Geheimhaltung als auch Authentizität in der Kommunikation garantieren, und daher werden Verschlüsselungsverfahren und MAC-Verfahren in der Regel zusammen verwendet.

Ein **authentifiziertes Verschlüsselungsverfahren** ist ein Verfahren, das Verschlüsselung mit einem MAC auf hochsichere Weise kombiniert. Insbesondere muss es den Standards für existenzielle Unfälschbarkeit sowie einer sehr starken Vorstellung von Geheimhaltung genügen, nämlich einer, die resistent gegen **Angriffe mit gewählten Chiffretexten** ist. [7]

Damit ein Verschlüsselungsverfahren resistent gegen Angriffe mit gewählten Chiffretexten ist, muss es den Standards für **Nicht-Verformbarkeit** entsprechen: das heißt, jede Modifikation eines Chiffretexts durch einen Angreifer sollte entweder einen ungültigen Chiffretext ergeben oder einen, der zu einem Klartext entschlüsselt wird, der in keiner Beziehung zum ursprünglichen steht. [8]

Da ein authentifiziertes Verschlüsselungsverfahren sicherstellt, dass ein von einem Angreifer erstellter Chiffretext immer ungültig ist (da der Tag nicht verifiziert wird), erfüllt es die Standards für Resistenz gegen Angriffe mit gewählten Chiffretexten. Interessanterweise kann man beweisen, dass ein authentifiziertes Verschlüsselungsverfahren immer aus der Kombination eines existenziell unfälschbaren MAC und eines Verschlüsselungsverfahrens, das eine weniger starke Sicherheitsvorstellung erfüllt, bekannt als **Sicherheit gegen Angriffe mit gewählten Klartexten**, erstellt werden kann.

Wir werden nicht in alle Details der Konstruktion authentifizierter Verschlüsselungsverfahren eintauchen. Aber es ist wichtig, zwei Details ihrer Konstruktion zu kennen.

Zuerst behandelt ein authentifiziertes Verschlüsselungsverfahren die Verschlüsselung und erstellt dann einen Nachrichtentag auf dem Chiffretext. Es stellt sich heraus, dass andere Ansätze – wie die Kombination des Chiffretexts mit einem Tag auf dem Klartext oder zuerst das Erstellen eines Tags und dann das Verschlüsseln sowohl des Klartexts als auch des Tags – unsicher sind. Zusätzlich haben beide Operationen ihren eigenen zufällig ausgewählten privaten Schlüssel, sonst ist Ihre Sicherheit stark beeinträchtigt.

Das oben genannte Prinzip gilt allgemeiner: *Sie sollten immer unterschiedliche Schlüssel verwenden, wenn Sie grundlegende kryptografische Verfahren kombinieren*.

Ein authentifiziertes Verschlüsselungsverfahren wird in *Abbildung 10* dargestellt. Bob erstellt zuerst einen Chiffretext $C$ aus der Nachricht $M$ unter Verwendung eines zufällig ausgewählten Schlüssels $K_C$. Dann erstellt er einen Nachrichtentag $T$, indem er den Chiffretext und einen anderen zufällig ausgewählten Schlüssel $K_T$ durch den Tag-Generierungsalgorithmus laufen lässt. Sowohl der Chiffretext als auch der Nachrichtentag werden an Alice gesendet.
Alice prüft nun zuerst, ob das Tag angesichts des Ciphertexts $C$ und des Schlüssels $K_T$ gültig ist. Wenn es gültig ist, kann sie dann die Nachricht mit dem Schlüssel $K_C$ entschlüsseln. Sie ist sich nicht nur einer sehr starken Vorstellung von Geheimhaltung in ihrer Kommunikation sicher, sondern sie weiß auch, dass die Nachricht von Bob erstellt wurde.
*Abbildung 10: Ein authentifiziertes Verschlüsselungsschema*

![Abbildung 10: Ein authentifiziertes Verschlüsselungsschema](assets/Figure4-10.webp "Abbildung 10: Ein authentifiziertes Verschlüsselungsschema")

Wie werden MACs erstellt? Obwohl MACs auf verschiedene Weisen erstellt werden können, ist ein gängiger und effizienter Weg, sie mittels **kryptografischer Hash-Funktionen** zu erstellen.

Wir werden kryptografische Hash-Funktionen in *Kapitel 6* ausführlicher einführen. Für den Moment genügt es zu wissen, dass eine **Hash-Funktion** eine effizient berechenbare Funktion ist, die Eingaben beliebiger Größe nimmt und Ausgaben fester Länge liefert. Zum Beispiel erzeugt die beliebte Hash-Funktion **SHA-256** (Secure Hash Algorithm 256) immer eine 256-Bit-Ausgabe, unabhängig von der Größe der Eingabe. Einige Hash-Funktionen, wie SHA-256, haben nützliche Anwendungen in der Kryptografie.

Die am häufigsten produzierte Art von Tag mit einer kryptografischen Hash-Funktion ist der **hash-basierte Message Authentication Code** (HMAC). Der Prozess ist in *Abbildung 11* dargestellt. Eine Partei erzeugt zwei unterschiedliche Schlüssel aus einem privaten Schlüssel $K$, den inneren Schlüssel $K_1$ und den äußeren Schlüssel $K_2$. Der Klartext $M$ oder Ciphertext $C$ wird dann zusammen mit dem inneren Schlüssel gehasht. Das Ergebnis $T'$ wird dann mit dem äußeren Schlüssel gehasht, um das Nachrichten-Tag $T$ zu produzieren.

Es gibt eine Palette von Hash-Funktionen, die zur Erstellung eines HMAC verwendet werden können. Die am häufigsten verwendete Hash-Funktion ist SHA-256.

*Abbildung 11: HMAC*

![Abbildung 11: HMAC](assets/Figure4-11.webp "Abbildung 11: HMAC")

**Anmerkungen:**

[7] Die spezifischen Ergebnisse, die in diesem Abschnitt diskutiert werden, stammen von Katz und Lindell, S. 131–47.

[8] Technisch gesehen ist die Definition von Angriffen mit gewähltem Ciphertext anders als der Begriff der Nicht-Manipulierbarkeit. Aber man kann zeigen, dass diese beiden Sicherheitskonzepte äquivalent sind.

## Sichere Kommunikationssitzungen
<chapterId>c7f7dcd3-bbed-53ed-a43d-039da0f180c5</chapterId>

Nehmen wir an, zwei Parteien befinden sich in einer Kommunikationssitzung, sodass sie mehrere Nachrichten hin und her senden.

Ein authentifiziertes Verschlüsselungsschema ermöglicht es dem Empfänger einer Nachricht zu überprüfen, dass sie von seinem Partner in der Kommunikationssitzung erstellt wurde (solange der private Schlüssel nicht durchgesickert ist). Das funktioniert gut genug für eine einzelne Nachricht. Typischerweise senden jedoch zwei Parteien in einer Kommunikationssitzung Nachrichten hin und her. Und in diesem Setting kommt ein einfaches authentifiziertes Verschlüsselungsschema, wie im vorherigen Abschnitt beschrieben, zu kurz, um Sicherheit zu bieten.

Der Hauptgrund ist, dass ein authentifiziertes Verschlüsselungsschema keine Garantie dafür bietet, dass die Nachricht tatsächlich auch von dem Agenten gesendet wurde, der sie innerhalb einer Kommunikationssitzung erstellt hat. Betrachten Sie die folgenden drei Angriffsvektoren:

1. **Replay-Angriff**: Ein Angreifer sendet einen Ciphertext und ein Tag, die er zu einem früheren Zeitpunkt zwischen zwei Parteien abgefangen hat, erneut.
2. **Reihenfolge-Angriff**: Ein Angreifer fängt zwei Nachrichten zu unterschiedlichen Zeiten ab und sendet sie in umgekehrter Reihenfolge an den Empfänger.
3. **Reflexionsangriff**: Ein Angreifer beobachtet eine Nachricht, die von A nach B gesendet wurde, und sendet diese Nachricht auch an A.

Obwohl der Angreifer keine Kenntnis vom Ciphertext hat und keine gefälschten Ciphertexts erstellen kann, können die oben genannten Angriffe dennoch erheblichen Schaden in der Kommunikation verursachen.
Angenommen, zum Beispiel, dass eine bestimmte Nachricht zwischen zwei Parteien den Transfer von finanziellen Mitteln beinhaltet. Ein Replay-Angriff könnte die Mittel ein zweites Mal übertragen. Ein einfaches authentifiziertes Verschlüsselungsschema bietet keine Abwehr gegen solche Angriffe.
Glücklicherweise können diese Arten von Angriffen in einer Kommunikationssitzung leicht durch **Identifikatoren** und **relative Zeitindikatoren** gemildert werden.

Identifikatoren können der Klartextnachricht vor der Verschlüsselung hinzugefügt werden. Dies würde jegliche Reflexionsangriffe verhindern. Ein relativer Zeitindikator kann zum Beispiel eine Sequenznummer in einer bestimmten Kommunikationssitzung sein. Jede Partei fügt einer Nachricht vor der Verschlüsselung eine Sequenznummer hinzu, sodass der Empfänger weiß, in welcher Reihenfolge die Nachrichten gesendet wurden. Dies eliminiert die Möglichkeit von Neuordnungsangriffen. Es eliminiert auch Replay-Angriffe. Jede Nachricht, die ein Angreifer weiterleitet, wird eine alte Sequenznummer haben, und der Empfänger wird wissen, dass er die Nachricht nicht noch einmal verarbeiten soll.

Um zu veranschaulichen, wie sichere Kommunikationssitzungen funktionieren, nehmen wir wieder Alice und Bob an. Sie senden insgesamt vier Nachrichten hin und her. Sie können sehen, wie ein authentifiziertes Verschlüsselungsschema mit Identifikatoren und Sequenznummern unten in *Abbildung 11* funktionieren würde.

Die Kommunikationssitzung beginnt damit, dass Bob einen Chiffretext $C_{0,B}$ an Alice sendet mit einem Nachrichtentag $T_{0,B}$. Der Chiffretext enthält die Nachricht sowie einen Identifikator (BOB) und eine Sequenznummer (0). Der Tag $T_{0,B}$ wird über den gesamten Chiffretext erstellt. In ihren nachfolgenden Kommunikationen halten Alice und Bob dieses Protokoll aufrecht und aktualisieren die Felder nach Bedarf.

*Abbildung 12: Eine sichere Kommunikationssitzung*

![Abbildung 12: Eine sichere Kommunikationssitzung](assets/Figure4-12.webp "Abbildung 12: Eine sichere Kommunikationssitzung")

# RC4 und AES
<partId>a48c4a7d-0a41-523f-a4ab-1305b4430324</partId>

## Der RC4-Stream-Cipher
<chapterId>5caec5bd-5a77-56c9-b5e6-1e86f0d294aa</chapterId>

In diesem Kapitel werden wir die Details eines Verschlüsselungsschemas mit einem modernen primitiven Stream-Cipher, RC4 (oder "Rivest Cipher 4"), und einem modernen Block-Cipher, AES, besprechen. Während der RC4-Cipher als Verschlüsselungsmethode in Ungnade gefallen ist, ist AES der Standard für moderne symmetrische Verschlüsselung. Diese beiden Beispiele sollten eine bessere Vorstellung davon geben, wie symmetrische Verschlüsselung unter der Haube funktioniert.

___

Um ein Gefühl dafür zu bekommen, wie moderne pseudorandom Stream-Cipher funktionieren, werde ich mich auf den RC4-Stream-Cipher konzentrieren. Es handelt sich um einen pseudorandom Stream-Cipher, der in den WEP- und WAP-Wireless-Access-Point-Sicherheitsprotokollen sowie in TLS verwendet wurde. Da RC4 viele bewiesene Schwächen hat, ist er in Ungnade gefallen. Tatsächlich verbietet die Internet Engineering Task Force nun die Verwendung von RC4-Suites durch Client- und Serveranwendungen in allen Instanzen von TLS. Dennoch dient er gut als Beispiel, um zu illustrieren, wie ein primitiver Stream-Cipher funktioniert.

Zu Beginn werde ich zunächst zeigen, wie man eine Klartextnachricht mit einem Baby-RC4-Cipher verschlüsselt. Nehmen wir an, unsere Klartextnachricht ist „SOUP“. Die Verschlüsselung mit unserem Baby-RC4-Cipher erfolgt dann in vier Schritten.

### Schritt 1
Zuerst definieren Sie ein Array **S** mit $S[0] = 0$ bis $S[7] = 7$. Ein Array bedeutet hier einfach eine veränderbare Sammlung von Werten, die durch einen Index organisiert sind, auch Liste in einigen Programmiersprachen genannt (z.B. Python). In diesem Fall läuft der Index von 0 bis 7, und die Werte laufen ebenfalls von 0 bis 7. Also ist **S** wie folgt:
- $S = [0, 1, 2, 3, 4, 5, 6, 7]$

Die Werte hier sind keine ASCII-Zahlen, sondern die Dezimalwertdarstellungen von 1-Byte-Strings. Also würde der Wert 2 gleich $0000 \ 0011$ sein. Die Länge des Arrays **S** beträgt somit 8 Bytes.

### Schritt 2

Als Zweites definieren Sie ein Schlüsselarray **K** mit einer Länge von 8 Bytes, indem Sie einen Schlüssel zwischen 1 und 8 Bytes wählen (Bruchteile von Bytes sind nicht zulässig). Da jedes Byte 8 Bits hat, können Sie jede Zahl zwischen 0 und 255 für jedes Byte Ihres Schlüssels auswählen.

Nehmen wir an, wir wählen unseren Schlüssel **k** als $[14, 48, 9]$, sodass er eine Länge von 3 Bytes hat. Jeder Index unseres Schlüsselarrays wird dann gemäß dem Dezimalwert für das jeweilige Element des Schlüssels in Reihenfolge gesetzt. Wenn Sie den gesamten Schlüssel durchlaufen, beginnen Sie wieder am Anfang, bis Sie die 8 Plätze des Schlüsselarrays gefüllt haben. Daher ist unser Schlüsselarray wie folgt:

- $K = [14, 48, 9, 14, 48, 9, 14, 48]$

### Schritt 3

Drittens werden wir das Array **S** unter Verwendung des Schlüsselarrays **K** transformieren, in einem Prozess, der als **Schlüsselplanung** bekannt ist. Der Prozess ist wie folgt in Pseudocode:

- Erstellen Sie Variablen **j** und **i**
- Setzen Sie die Variable $j = 0$
- Für jedes $i$ von 0 bis 7:
    - Setzen Sie $j = (j + S[i] + K[i]) \mod 8$
    - Tauschen Sie $S[i]$ und $S[j]$

Die Transformation des Arrays **S** wird durch *Tabelle 1* erfasst.

Zu Beginn können Sie den Anfangszustand von **S** als $[0, 1, 2, 3, 4, 5, 6, 7]$ mit einem Anfangswert von 0 für **j** sehen. Dies wird unter Verwendung des Schlüsselarrays $[14, 48, 9, 14, 48, 9, 14, 48]$ transformiert.

Die For-Schleife beginnt mit $i = 0$. Gemäß unserem Pseudocode oben wird der neue Wert von **j** zu 6 ($j = (j + S[0] + K[0]) \mod 8 = (0 + 0 + 14) \mod 8 = 6 \mod 8$). Durch Tauschen von $S[0]$ und $S[6]$, wird der Zustand von **S** nach 1 Runde zu $[6, 1, 2, 3, 4, 5, 0, 7]$.
In der nächsten Zeile ist $i = 1$. Wenn wir die for-Schleife erneut durchlaufen, erhält **j** einen Wert von 7 ($j = (j + S[1] + K[1]) \mod 8 = (6 + 1 + 48) \mod 8 = 55 \mod 8 = 7 \mod 8$). Durch das Vertauschen von $S[1]$ und $S[7]$ im aktuellen Zustand von **S**, $[6, 1, 2, 3, 4, 5, 0, 7]$, ergibt sich nach Runde 2 $[6, 7, 2, 3, 4, 5, 0, 1]$.
Wir setzen diesen Prozess fort, bis wir die letzte Zeile unten für das Array **S** erzeugen, $[6, 4, 1, 0, 3, 7, 5, 2]$.

*Tabelle 1: Schlüsselplanungstabelle*

| Runde   | i   | j   |     | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| ------- | --- | --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|         |     |     |     |      |      |      |      |      |      |      |      |
| Anfang  |     | 0   |     | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    |
| 1       | 0   | 6   |     | 6    | 1    | 2    | 3    | 4    | 5    | 0    | 7    |
| 2       | 1   | 7   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 3       | 2   | 2   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 4       | 3   | 3   |     | 6    | 7    | 2    | 3    | 4    | 5    | 0    | 1    |
| 5       | 4   | 3   |     | 6    | 7    | 2    | 0    | 3    | 5    | 4    | 1    |
| 6       | 5   | 6   |     | 6    | 4    | 2    | 0    | 3    | 7    | 5    | 1    |
| 7       | 6   | 1   |     | 6    | 4    | 2    | 0    | 3    | 7    | 5    | 2    |
| 8       | 7   | 2   |     | 6    | 4    | 1    | 0    | 3    | 7    | 5    | 2    |

### Schritt 4
Als vierter Schritt erzeugen wir den **Keystream**. Dies ist die pseudozufällige Zeichenfolge, deren Länge gleich der Länge der Nachricht ist, die wir senden möchten. Diese wird verwendet, um die ursprüngliche Nachricht „SOUP“ zu verschlüsseln. Da der Keystream genauso lang sein muss wie die Nachricht, benötigen wir einen, der 4 Bytes lang ist.
Der Keystream wird durch den folgenden Pseudocode erzeugt:

- Erstelle die Variablen **j**, **i** und **t**.
- Setze $j = 0$.
- Für jedes $i$ des Klartextes, beginnend mit $i = 1$ und fortlaufend bis $i = 4$, wird jedes Byte des Keystreams wie folgt erzeugt:
    - $j = (j + S[i]) \mod 8$
    - Tausche $S[i]$ und $S[j]$.
    - $t = (S[i] + S[j]) \mod 8$
    - Das $i^{te}$ Byte des Keystreams = $S[t]$

Die Berechnungen können in *Tabelle 2* nachvollzogen werden.

Der Anfangszustand von **S** ist $S = [6, 4, 1, 0, 3, 7, 5, 2]$. Wenn $i = 1$ gesetzt wird, wird der Wert von **j** zu 4 ($j = (j + S[i]) \mod 8 = (0 + 4) \mod 8 = 4$). Dann tauschen wir $S[1]$ und $S[4]$, um die Transformation von **S** in der zweiten Zeile zu erzeugen, $[6, 3, 1, 0, 4, 7, 5, 2]$. Der Wert von **t** wird dann 7 ($t = (S[i] + S[j]) \mod 8 = (3 + 4) \mod 8 = 7$). Schließlich ist das Byte für den Keystream $S[7]$, oder 2.

Wir fahren dann fort, die anderen Bytes zu erzeugen, bis wir die folgenden vier Bytes haben: 2, 6, 3 und 7. Jedes dieser Bytes kann dann verwendet werden, um jeden Buchstaben des Klartextes, "SOUP", zu verschlüsseln.

Um zu beginnen, können wir mithilfe einer ASCII-Tabelle sehen, dass „SOUP“ kodiert durch die Dezimalwerte der zugrundeliegenden Byte-Strings „83 79 85 80“ ist. Die Kombination mit dem Keystream „2 6 3 7“ ergibt „85 85 88 87“, was nach einer Modulo-256-Operation gleich bleibt. In ASCII entspricht der Chiffretext „85 85 88 87“ „UUXW“.

Was passiert, wenn das zu verschlüsselnde Wort länger als das Array **S** wäre? In diesem Fall würde sich das Array **S** einfach in der oben dargestellten Weise für jedes Byte **i** des Klartextes weiter transformieren, bis wir eine Anzahl von Bytes im Keystream haben, die der Anzahl der Buchstaben im Klartext entspricht.


*Tabelle 2: Keystream-Erzeugung*

| i   | j   | t   | Keystream | S[0] | S[1] | S[2] | S[3] | S[4] | S[5] | S[6] | S[7] |
| --- | --- | --- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|     | 0   |     |           | 6    | 4    | 1    | 0    | 3    | 7    | 5    | 2    || 1   | 4   | 7   | 2         | 6    | 3    | 1    | 0    | 4    | 7    | 5    | 2    |
| 2   | 5   | 0   | 6         | 6    | 3    | 7    | 0    | 4    | 1    | 5    | 2    |
| 3   | 5   | 1   | 3         | 6    | 3    | 7    | 1    | 4    | 0    | 5    | 2    |
| 4   | 1   | 7   | 2         | 6    | 4    | 7    | 1    | 3    | 0    | 5    | 2    |

Das Beispiel, das wir gerade besprochen haben, ist nur eine vereinfachte Version des **RC4 Stream Cipher**. Der eigentliche RC4 Stream Cipher hat ein **S**-Array mit einer Länge von 256 Bytes, nicht 8 Bytes, und einen Schlüssel, der zwischen 1 und 256 Bytes lang sein kann, nicht zwischen 1 und 8 Bytes. Das Schlüsselarray und die Keystreams werden dann alle unter Berücksichtigung der 256-Byte-Länge des **S**-Arrays produziert. Die Berechnungen werden immens komplexer, aber die Prinzipien bleiben die gleichen. Unter Verwendung desselben Schlüssels, [14,48,9], wird die Klartextnachricht "SOUP" mit dem Standard-RC4-Cipher als 67 02 ed df im hexadezimalen Format verschlüsselt.

Ein Stream Cipher, bei dem der Keystream unabhängig von der Klartextnachricht oder dem Ciphertext aktualisiert wird, ist ein **synchroner Stream Cipher**. Der Keystream hängt nur vom Schlüssel ab. Offensichtlich ist RC4 ein Beispiel für einen synchronen Stream Cipher, da der Keystream keine Beziehung zum Klartext oder Ciphertext hat. Alle unsere primitiven Stream Ciphers, die im vorherigen Kapitel erwähnt wurden, einschließlich des Shift Cipher, des Vigenère Cipher und des One-Time Pad, waren ebenfalls von der synchronen Sorte.

Im Gegensatz dazu wird bei einem **asynchronen Stream Cipher** der Keystream sowohl durch den Schlüssel als auch durch vorherige Elemente des Ciphertexts erzeugt. Diese Art von Cipher wird auch als **selbstsynchronisierender Cipher** bezeichnet.

Wichtig ist, dass der mit RC4 erzeugte Keystream wie ein One-Time Pad behandelt werden sollte, und man kann den Keystream nicht genau auf die gleiche Weise ein nächstes Mal produzieren. Anstatt jedes Mal den Schlüssel zu ändern, ist die praktische Lösung, den Schlüssel mit einem **Nonce** zu kombinieren, um den Bytestream zu erzeugen.

## AES mit einem 128-Bit-Schlüssel
<chapterId>0b30886f-e620-5b8d-807b-9d84685ca8ff</chapterId>

Wie im vorherigen Kapitel erwähnt, veranstaltete das National Institute of Standards and Technology (NIST) zwischen 1997 und 2000 einen Wettbewerb, um einen neuen symmetrischen Verschlüsselungsstandard zu bestimmen. Der **Rijndael Cipher** stellte sich als der Gewinner heraus. Der Name ist ein Wortspiel mit den Namen der belgischen Erfinder, Vincent Rijmen und Joan Daemen.
Der Rijndael-Algorithmus ist ein **Blockchiffre**, was bedeutet, dass es einen Kernalgorithmus gibt, der mit verschiedenen Spezifikationen für Schlüssellängen und Blockgrößen verwendet werden kann. Sie können ihn dann mit verschiedenen Betriebsmodi verwenden, um Verschlüsselungsschemata zu konstruieren.
Das Komitee für den NIST-Wettbewerb hat eine eingeschränkte Version des Rijndael-Algorithmus angenommen – nämlich eine, die 128-Bit-Blockgrößen und Schlüssellängen von entweder 128 Bits, 192 Bits oder 256 Bits erfordert – als Teil des **Advanced Encryption Standard (AES)**. Diese eingeschränkte Version des Rijndael-Algorithmus kann auch unter mehreren Betriebsmodi verwendet werden. Die Spezifikation für den Standard ist bekannt als der **Advanced Encryption Standard (AES)**.

Um zu zeigen, wie der Rijndael-Algorithmus funktioniert, den Kern von AES, werde ich den Prozess für die Verschlüsselung mit einem 128-Bit-Schlüssel illustrieren. Die Schlüsselgröße hat einen Einfluss auf die Anzahl der Runden, die für jeden Block der Verschlüsselung gehalten werden. Für 128-Bit-Schlüssel sind 10 Runden erforderlich. Mit 192 Bits und 256 Bits wären es 12 bzw. 14 Runden gewesen.

Zusätzlich werde ich annehmen, dass AES im **ECB-Modus** verwendet wird. Das macht die Darstellung etwas einfacher und spielt für den Rijndael-Algorithmus keine Rolle. Sicher ist der ECB-Modus in der Praxis nicht, da er zu deterministischer Verschlüsselung führt. Der am häufigsten verwendete sichere Modus mit AES ist **CBC** (Cipher Block Chaining).

Nennen wir den Schlüssel $K_0$. Die Konstruktion mit den oben genannten Parametern sieht dann aus wie in *Abbildung 1*, wo $M_i$ für einen Teil der Klartextnachricht von 128 Bits steht und $C_i$ für einen Teil des Chiffretexts von 128 Bits. Padding wird dem Klartext für den letzten Block hinzugefügt, wenn der Klartext nicht gleichmäßig durch die Blockgröße geteilt werden kann.

*Abbildung 1: AES-ECB mit einem 128-Bit-Schlüssel*

![Abbildung 1: AES-ECB mit einem 128-Bit-Schlüssel](assets/Figure5-1.webp "Abbildung 1: AES-ECB mit einem 128-Bit-Schlüssel")

Jeder 128-Bit-Block des Textes durchläuft zehn Runden im Rijndael-Verschlüsselungsschema. Dies erfordert einen separaten Rundenschlüssel für jede Runde ($K_1$ bis $K_{10}$). Diese werden für jede Runde aus dem ursprünglichen 128-Bit-Schlüssel $K_0$ mit einem **Schlüsselexpansionsalgorithmus** erzeugt. Daher werden wir für jeden zu verschlüsselnden Textblock den ursprünglichen Schlüssel $K_0$ sowie zehn separate Rundenschlüssel verwenden. Beachten Sie, dass diese gleichen 11 Schlüssel für jeden 128-Bit-Block des Klartextes verwendet werden, der verschlüsselt werden muss.

Der Schlüsselexpansionsalgorithmus ist lang und komplex. Sich damit zu beschäftigen, bringt wenig didaktischen Nutzen. Sie können sich den Schlüsselexpansionsalgorithmus selbst ansehen, wenn Sie möchten. Sobald die Rundenschlüssel produziert sind, wird der Rijndael-Algorithmus den ersten 128-Bit-Block des Klartextes, $M_1$, manipulieren, wie in *Abbildung 2* zu sehen. Wir werden nun diese Schritte durchgehen.

*Abbildung 2: Die Manipulation von $M_1$ mit dem Rijndael-Algorithmus:*

**Runde 0:**
- XOR $M_1$ und $K_0$ um $S_0$ zu erzeugen

---

**Runde n für n = {1,...,9}:**
- XOR $S_{n-1}$ und $K_n$
- Byte-Substitution
- Zeilen verschieben
- Spalten mischen
- XOR $S$ und $K_n$ um $S_n$ zu erzeugen

---

**Runde 10:**
- XOR $S_9$ und $K_{10}$ - Byte-Substitution
- Zeilen verschieben
- XOR $S$ und $K_{10}$, um $S_{10}$ zu erzeugen
- $S_{10}$ = $C_1$

### Runde 0

Runde 0 des Rijndael-Verschlüsselungsverfahrens ist unkompliziert. Ein Array $S_0$ wird durch eine XOR-Operation zwischen dem 128-Bit-Klartext und dem privaten Schlüssel erzeugt. Das heißt,

- $S_0 = M_1 \oplus K_0$

### Runde 1

In Runde 1 wird das Array $S_0$ zunächst mit dem Rundenschlüssel $K_1$ mittels einer XOR-Operation kombiniert. Dies erzeugt einen neuen Zustand von $S$.

Zweitens wird die **Byte-Substitution**-Operation auf dem aktuellen Zustand von $S$ durchgeführt. Dabei wird jedes Byte des 16-Byte $S$-Arrays genommen und durch ein Byte aus einem Array ersetzt, das **Rijndael’s S-Box** genannt wird. Jedes Byte hat eine einzigartige Transformation, und ein neuer Zustand von $S$ wird als Ergebnis erzeugt. Rijndael's S-Box wird in *Abbildung 3* dargestellt.

*Abbildung 3: Rijndael's S-Box*

|     | 00  | 01  | 02  | 03  | 04  | 05  | 06  | 07  | 08  | 09  | 0A  | 0B  | 0C  | 0D  | 0E  | 0F  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00  | 63  | 7C  | 77  | 7B  | F2  | 6B  | 6F  | C5  | 30  | 01  | 67  | 2B  | FE  | D7  | AB  | 76  |
| 10  | CA  | 82  | C9  | 7D  | FA  | 59  | 47  | F0  | AD  | D4  | A2  | AF  | 9C  | A4  | 72  | C0  |
| 20  | B7  | FD  | 93  | 26  | 36  | 3F  | F7  | CC  | 34  | A5  | E5  | F1  | 71  | D8  | 31  | 15  |
| 30  | 04  | C7  | 23  | C3  | 18  | 96  | 05  | 9A  | 07  | 12  | 80  | E2  | EB  | 27  | B2  | 75  |
| 40  | 09  | 83  | 2C  | 1A  | 1B  | 6E  | 5A  | A0  | 52  | 3B  | D6  | B3  | 29  | E3  | 2F  | 84  |
| 50  | 53  | D1  | 00  | ED  | 20  | FC  | B1  | 5B  | 6A  | CB  | BE  | 39  | 4A  | 4C  | 58  | CF  || 60  | D0  | EF  | AA  | FB  | 43  | 4D  | 33  | 85  | 45  | F9  | 02  | 7F  | 50  | 3C  | 9F  | A8  |
| 70  | 51  | A3  | 40  | 8F  | 92  | 9D  | 38  | F5  | BC  | B6  | DA  | 21  | 10  | FF  | F3  | D2  |
| 80  | CD  | 0C  | 13  | EC  | 5F  | 97  | 44  | 17  | C4  | A7  | 7E  | 3D  | 64  | 5D  | 19  | 73  |
| 90  | 60  | 81  | 4F  | DC  | 22  | 2A  | 90  | 88  | 46  | EE  | B8  | 14  | DE  | 5E  | 0B  | DB  |
| A0  | E0  | 32  | 3A  | 0A  | 49  | 06  | 24  | 5C  | C2  | D3  | AC  | 62  | 91  | 95  | E4  | 79  |
| B0  | E7  | C8  | 37  | 6D  | 8D  | D5  | 4E  | A9  | 6C  | 56  | F4  | EA  | 65  | 7A  | AE  | 08  |
| C0  | BA  | 78  | 25  | 2E  | 1C  | A6  | B4  | C6  | E8  | DD  | 74  | 1F  | 4B  | BD  | 8B  | 8A  |
| D0  | 70  | 3E  | B5  | 66  | 48  | 03  | F6  | 0E  | 61  | 35  | 57  | B9  | 86  | C1  | 1D  | 9E  |
| E0  | E1  | F8  | 98  | 11  | 69  | D9  | 8E  | 94  | 9B  | 1E  | 87  | E9  | CE  | 55  | 28  | DF  |
| F0  | 8C  | A1  | 89  | 0D  | BF  | E6  | 42  | 68  | 41  | 99  | 2D  | 0F  | B0  | 54  | BB  | 16  |

Diese S-Box ist einer der Punkte, an denen abstrakte Algebra im Rijndael-Verschlüsselungsverfahren zum Einsatz kommt, speziell **Galois-Felder**.

Zunächst definieren Sie jedes mögliche Byte-Element von 00 bis FF als einen 8-Bit-Vektor. Jeder solche Vektor ist ein Element des **Galois-Feldes GF(2^8)**, wobei das irreduzible Polynom für die Modulo-Operation $x^8 + x^4 + x^3 + x + 1$ ist. Das Galois-Feld mit diesen Spezifikationen wird auch **Rijndaels endliches Feld** genannt.

Als Nächstes erstellen wir für jedes mögliche Element im Feld, was als **Nyberg S-Box** bezeichnet wird. In dieser Box wird jedes Byte auf sein **multiplikatives Inverses** abgebildet (d.h., so dass ihr Produkt 1 ergibt). Dann werden diese Werte aus der Nyberg S-Box mithilfe der **affinen Transformation** auf Rijndaels S-Box abgebildet.

Die dritte Operation am **S**-Array ist die **Zeilenverschiebung**. Sie nimmt den Zustand von **S** und listet alle sechzehn Bytes in einer Matrix auf. Das Füllen der Matrix beginnt oben links und arbeitet sich durch, indem von oben nach unten gegangen wird und dann, jedes Mal wenn eine Spalte gefüllt ist, eine Spalte nach rechts und nach oben verschoben wird.

Sobald die Matrix von **S** konstruiert wurde, werden die vier Reihen verschoben. Die erste Reihe bleibt gleich. Die zweite Reihe bewegt sich eins nach links. Die dritte bewegt sich zwei nach links. Die vierte bewegt sich drei nach links. Ein Beispiel für den Prozess wird in *Abbildung 4* gezeigt. Der ursprüngliche Zustand von **S** wird oben gezeigt, und der resultierende Zustand nach der Zeilenverschiebung wird darunter gezeigt.

*Abbildung 4: Zeilenverschiebungsoperation*

| F1   | A0   | B1   | 23   |
|------|------|------|------|
| 59   | EF   | 09   | 82   |
| 97   | 01   | B0   | CC   |
| D4   | 72   | 04   | 21   |

| F1   | A0   | B1   | 23   |
|------|------|------|------|
| EF   | 09   | 82   | 59   |
| B0   | CC   | 97   | 01   |
| 21   | D4   | 72   | 04   |


Im vierten Schritt kommen **Galois-Felder** erneut zum Einsatz. Zunächst wird jede Spalte der **S**-Matrix mit der Spalte der 4 x 4 Matrix multipliziert, die in *Abbildung 5* zu sehen ist. Aber anstatt einer regulären Matrixmultiplikation handelt es sich um eine Vektormultiplikation **modulo eines irreduziblen Polynoms**, $x^8 + x^4 + x^3 + x + 1$. Die resultierenden Vektorkoeffizienten repräsentieren die einzelnen Bits eines Bytes.

*Abbildung 5: Spalten mischen Matrix*

| 02   | 03   | 01   | 01   |
|------|------|------|------|
| 01   | 02   | 03   | 01   |
| 01   | 01   | 02   | 03   || 03   | 01   | 01   | 02   |

Die Multiplikation der ersten Spalte der **S**-Matrix mit der oben stehenden 4 x 4 Matrix ergibt das Ergebnis in *Abbildung 6*.

*Abbildung 6: Multiplikation der ersten Spalte:*

$$
\begin{matrix}
02 \cdot F1 + 03 \cdot EF + 01 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 02 \cdot EF + 03 \cdot B0 + 01 \cdot 21 \\
01 \cdot F1 + 01 \cdot EF + 02 \cdot B0 + 03 \cdot 21 \\
03 \cdot F1 + 01 \cdot EF + 01 \cdot B0 + 02 \cdot 21
\end{matrix}
$$

Als nächster Schritt müssen alle Terme in der Matrix in Polynome umgewandelt werden. Zum Beispiel steht F1 für 1 Byte und würde zu $x^7 + x^6 + x^5 + x^4 + 1$ werden, und 03 steht für 1 Byte und würde zu $x + 1$ werden.

Alle Multiplikationen werden dann **modulo** $x^8 + x^4 + x^3 + x + 1$ durchgeführt. Dies führt zur Addition von vier Polynomen in jeder der vier Zellen der Spalte. Nachdem diese Additionen **modulo 2** durchgeführt wurden, erhält man vier Polynome. Jedes dieser Polynome repräsentiert eine 8-Bit-Zeichenfolge oder 1 Byte von **S**. Wir werden all diese Berechnungen hier in der Matrix in *Abbildung 6* nicht durchführen, da sie umfangreich sind.

Sobald die erste Spalte verarbeitet wurde, werden die anderen drei Spalten der **S**-Matrix auf die gleiche Weise verarbeitet. Letztendlich ergibt dies eine Matrix mit sechzehn Bytes, die in ein Array umgewandelt werden kann.

Als letzter Schritt wird das Array **S** erneut in einer **XOR**-Operation mit dem Rundenschlüssel kombiniert. Dies produziert den Zustand $S_1$. Das heißt,

- $S_1 = S \oplus K_0$

### Runden 2 bis 10

Die Runden 2 bis 9 sind lediglich eine Wiederholung der Runde 1, *mutatis mutandis*. Die letzte Runde ähnelt den vorherigen Runden, außer dass der Schritt **Spalten mischen** weggelassen wird. Das heißt, Runde 10 wird wie folgt ausgeführt:

- $S_9 \oplus K_{10}$
- Byte-Substitution
- Zeilen verschieben
- $S_{10} = S \oplus K_{10}$

Der Zustand $S_{10}$ ist nun auf $C_1$ gesetzt, die ersten 128 Bits des Chiffretexts. Das Fortfahren durch die verbleibenden 128-Bit-Plaintextblöcke ergibt den vollständigen Chiffretext **C**.

### Die Operationen des Rijndael-Chiffre

Was ist die Begründung hinter den verschiedenen Operationen, die im Rijndael-Chiffre gesehen werden?

Ohne auf die Details einzugehen, werden Verschlüsselungsschemata auf der Grundlage bewertet, inwieweit sie Verwirrung und Streuung erzeugen. Wenn das Verschlüsselungsschema einen hohen Grad an **Verwirrung** aufweist, bedeutet dies, dass der Chiffretext drastisch anders aussieht als der Plaintext. Wenn das Verschlüsselungsschema einen hohen Grad an **Streuung** aufweist, bedeutet dies, dass jede kleine Änderung am Plaintext einen drastisch anderen Chiffretext produziert.
Die Begründung für die Operationen hinter dem Rijndael-Verschlüsselungsverfahren ist, dass sie sowohl ein hohes Maß an Verwirrung als auch an Streuung erzeugen. Die Verwirrung wird durch die Byte-Substitutionsoperation erzeugt, während die Streuung durch die Operationen "Zeilen verschieben" und "Spalten mischen" erzeugt wird.
# Asymmetrische Kryptographie
<partId>868bd9dd-6e1c-5ea9-9ece-54affc13ba05</partId>

## Das Problem der Schlüsselverteilung und -verwaltung
<chapterId>1bb651ba-689a-5a89-a7d3-0b9cc3b694f7</chapterId>

Wie bei der symmetrischen Kryptographie können asymmetrische Verfahren sowohl zur Gewährleistung von Geheimhaltung als auch von Authentizität verwendet werden. Im Gegensatz dazu verwenden diese Verfahren jedoch zwei Schlüssel anstelle von einem: einen privaten und einen öffentlichen Schlüssel.

Wir beginnen unsere Untersuchung mit der Entdeckung der asymmetrischen Kryptographie, insbesondere den Problemen, die sie hervorgerufen hat. Als Nächstes diskutieren wir, wie asymmetrische Verfahren für Verschlüsselung und Authentifizierung auf hoher Ebene funktionieren. Dann führen wir Hash-Funktionen ein, die für das Verständnis asymmetrischer Authentifizierungsschemata von entscheidender Bedeutung sind und auch in anderen kryptographischen Kontexten relevant sind, wie zum Beispiel für die hash-basierten Nachrichtenauthentifizierungscodes, die wir in Kapitel 4 besprochen haben.

___

Nehmen wir an, Bob möchte einen neuen Regenmantel von Jim’s Sporting Goods, einem Online-Sportartikelhändler mit Millionen von Kunden in Nordamerika, kaufen. Dies wird sein erster Kauf bei ihnen sein, und er möchte seine Kreditkarte verwenden. Also muss Bob zunächst ein Konto bei Jim’s Sporting Goods erstellen, was das Senden persönlicher Details wie seiner Adresse und Kreditkarteninformationen erfordert. Dann kann er die notwendigen Schritte durchgehen, um den Regenmantel zu kaufen.

Bob und Jim’s Sporting Goods werden sicherstellen wollen, dass ihre Kommunikation während dieses Prozesses sicher ist, in Anbetracht dessen, dass das Internet ein offenes Kommunikationssystem ist. Sie werden zum Beispiel sicherstellen wollen, dass kein potenzieller Angreifer Bobs Kreditkarten- und Adressdetails herausfinden kann und dass kein potenzieller Angreifer seine Käufe wiederholen oder gefälschte in seinem Namen erstellen kann.

Ein fortgeschrittenes authentifiziertes Verschlüsselungsschema, wie im vorherigen Kapitel besprochen, könnte die Kommunikation zwischen Bob und Jim’s Sporting Goods sicherlich sichern. Aber es gibt offensichtlich praktische Hindernisse für die Implementierung eines solchen Schemas.

Um diese praktischen Hindernisse zu veranschaulichen, nehmen wir an, wir lebten in einer Welt, in der nur die Werkzeuge der symmetrischen Kryptographie existierten. Was könnten Jim’s Sporting Goods und Bob dann tun, um eine sichere Kommunikation zu gewährleisten?

Unter diesen Umständen würden sie erhebliche Kosten für eine sichere Kommunikation tragen. Da das Internet ein offenes Kommunikationssystem ist, können sie nicht einfach einen Satz von Schlüsseln darüber austauschen. Daher müssten Bob und ein Vertreter von Jim’s Sporting Goods einen Schlüsselaustausch persönlich durchführen.

Eine Möglichkeit ist, dass Jim’s Sporting Goods spezielle Schlüsselaustauschstellen einrichtet, wo Bob und andere neue Kunden einen Satz von Schlüsseln für eine sichere Kommunikation abholen können. Dies würde offensichtlich erhebliche organisatorische Kosten verursachen und die Effizienz, mit der neue Kunden Einkäufe tätigen können, stark reduzieren.

Alternativ kann Jim’s Sporting Goods Bob ein Paar Schlüssel mit einem hochvertrauenswürdigen Kurier senden. Dies ist wahrscheinlich effizienter als die Organisation von Schlüsselaustauschstellen. Aber dies würde immer noch erhebliche Kosten verursachen, insbesondere wenn viele Kunden nur ein oder wenige Käufe tätigen.

Weiterhin zwingt ein symmetrisches Schema für authentifizierte Verschlüsselung Jim’s Sporting Goods dazu, separate Sätze von Schlüsseln für all ihre Kunden zu speichern. Dies wäre eine signifikante praktische Herausforderung für Tausende von Kunden, geschweige denn Millionen.
Um diesen letzten Punkt zu verstehen, nehmen wir an, dass Jim’s Sporting Goods jedem Kunden dasselbe Paar Schlüssel zur Verfügung stellt. Dies würde jedem Kunden – oder jeder anderen Person, die dieses Paar Schlüssel erhalten könnte – ermöglichen, alle Kommunikationen zwischen Jim’s Sporting Goods und seinen Kunden zu lesen und sogar zu manipulieren. Man könnte dann genauso gut auf Kryptografie in der Kommunikation verzichten.

Selbst die Wiederholung eines Satzes von Schlüsseln für nur einige Kunden ist eine schreckliche Sicherheitspraxis. Ein potenzieller Angreifer könnte versuchen, diese Eigenschaft des Systems auszunutzen (denken Sie daran, dass Angreifer gemäß dem Prinzip von Kerckhoffs alles über ein System wissen, außer den Schlüsseln).

Also müsste Jim’s Sporting Goods für jeden Kunden ein Paar Schlüssel speichern, unabhängig davon, wie diese Schlüsselpaare verteilt werden. Dies stellt offensichtlich mehrere praktische Probleme dar.

- Jim’s Sporting Goods müsste Millionen von Schlüsselpaaren speichern, ein Satz für jeden Kunden.
- Diese Schlüssel müssten ordnungsgemäß gesichert werden, da sie ein sicheres Ziel für Hacker wären. Jede Sicherheitsverletzung würde die Wiederholung kostspieliger Schlüsselaustausche erfordern, entweder an speziellen Schlüsselaustauschorten oder per Kurier.
- Jeder Kunde von Jim’s Sporting Goods müsste zu Hause ein Paar Schlüssel sicher aufbewahren. Verluste und Diebstähle werden vorkommen, was eine Wiederholung des Schlüsselaustauschs erfordert. Kunden müssten diesen Prozess auch für alle anderen Online-Shops oder andere Arten von Entitäten durchlaufen, mit denen sie über das Internet kommunizieren und Transaktionen durchführen möchten.

Diese beiden gerade beschriebenen Hauptprobleme waren bis Ende der 1970er Jahre sehr grundlegende Bedenken. Sie waren bekannt als das **Schlüsselverteilungsproblem** und das **Schlüsselverwaltungsproblem**.

Diese Probleme hatten natürlich immer existiert und oft Kopfschmerzen in der Vergangenheit verursacht. Militärische Kräfte mussten beispielsweise ständig Bücher mit Schlüsseln für sichere Kommunikation an Personal im Feld unter großen Risiken und Kosten verteilen. Aber diese Probleme verschlimmerten sich, da die Welt zunehmend in eine Ära der Fernkommunikation, insbesondere für nichtstaatliche Entitäten, überging.

Hätten diese Probleme in den 1970er Jahren nicht gelöst werden können, wäre effizientes und sicheres Einkaufen bei Jim’s Sporting Goods wahrscheinlich nicht existent gewesen. Tatsächlich wäre unsere moderne Welt mit praktischer und sicherer E-Mail-Kommunikation, Online-Banking und Einkaufen wahrscheinlich nur eine ferne Fantasie gewesen. Etwas, das auch nur entfernt Bitcoin ähnelt, hätte überhaupt nicht existieren können.

Was also geschah in den 1970er Jahren? Wie ist es möglich, dass wir heute sofort online Einkäufe tätigen und sicher im World Wide Web surfen können? Wie ist es möglich, dass wir augenblicklich Bitcoins von unseren Smartphones aus überall auf der Welt versenden können?

## Neue Richtungen in der Kryptografie
<chapterId>7a9dd9a3-496e-5f9d-93e0-b5028a7dd0f1</chapterId>

In den 1970er Jahren hatten die Probleme der Schlüsselverteilung und Schlüsselverwaltung die Aufmerksamkeit einer Gruppe amerikanischer akademischer Kryptografen erregt: Whitfield Diffie, Martin Hellman und Ralph Merkle. Trotz erheblicher Skepsis von der Mehrheit ihrer Kollegen wagten sie es, eine Lösung dafür zu finden.

Mindestens eine primäre Motivation für ihr Vorhaben war die Voraussicht, dass offene Computerkommunikation unsere Welt tiefgreifend beeinflussen würde. Wie Diffie und Hellman 1976 feststellten,
Die Entwicklung von computergesteuerten Kommunikationsnetzwerken verspricht mühelosen und kostengünstigen Kontakt zwischen Menschen oder Computern auf gegenüberliegenden Seiten der Welt und ersetzt die meisten Briefe und viele Reisen durch Telekommunikation. Für viele Anwendungen müssen diese Kontakte sowohl gegen Lauschangriffe als auch gegen das Einspeisen von illegitimen Nachrichten gesichert werden. Derzeit hinkt jedoch die Lösung von Sicherheitsproblemen anderen Bereichen der Kommunikationstechnologie weit hinterher. *Die zeitgenössische Kryptographie kann die Anforderungen nicht erfüllen, da ihre Nutzung solch schwere Unannehmlichkeiten für die Systemnutzer mit sich bringen würde, dass viele der Vorteile der Televerarbeitung zunichte gemacht würden.* [1]

Die Hartnäckigkeit von Diffie, Hellman und Merkle zahlte sich aus. Die erste Veröffentlichung ihrer Ergebnisse war ein Papier von Diffie und Hellman im Jahr 1976 mit dem Titel „New Directions in Cryptography“. Darin präsentierten sie zwei originelle Wege zur Adresse der Schlüsselverteilung und des Schlüsselmanagements.

Die erste Lösung, die sie anboten, war ein *Schlüsselaustauschprotokoll* für die Ferne, das heißt, ein Satz von Regeln für den Austausch von einem oder mehreren symmetrischen Schlüsseln über einen unsicheren Kommunikationskanal. Dieses Protokoll ist heute als *Diffie-Hellman-Schlüsselaustausch* oder *Diffie-Hellman-Merkle-Schlüsselaustausch* bekannt. [2]

Mit dem Diffie-Hellman-Schlüsselaustausch tauschen zwei Parteien zunächst einige Informationen öffentlich über einen unsicheren Kanal wie das Internet aus. Auf der Grundlage dieser Informationen erstellen sie dann unabhängig voneinander einen symmetrischen Schlüssel (oder ein Paar symmetrischer Schlüssel) für die sichere Kommunikation. Obwohl beide Parteien ihre Schlüssel unabhängig voneinander erstellen, stellt die öffentlich geteilte Information sicher, dass dieser Schlüsselerstellungsprozess für beide das gleiche Ergebnis liefert.

Wichtig ist, dass, während jeder die Informationen beobachten kann, die von den Parteien über den unsicheren Kanal öffentlich ausgetauscht werden, nur die beiden Parteien, die am Informationsaustausch teilnehmen, symmetrische Schlüssel daraus erstellen können.

Das klingt natürlich völlig kontraintuitiv. Wie könnten zwei Parteien einige Informationen öffentlich austauschen, die es nur ihnen ermöglichen, symmetrische Schlüssel daraus zu erstellen? Warum sollte jeder andere, der den Informationsaustausch beobachtet, nicht in der Lage sein, die gleichen Schlüssel zu erstellen?

Es beruht natürlich auf einiger schöner Mathematik. Der Diffie-Hellman-Schlüsselaustausch funktioniert über eine Einwegfunktion mit einer Falltür. Lassen Sie uns die Bedeutung dieser beiden Begriffe der Reihe nach besprechen.

Angenommen, Ihnen wird eine Funktion $f(x)$ und das Ergebnis $f(a) = y$ gegeben, wobei $a$ ein bestimmter Wert für $x$ ist. Wir sagen, dass $f(x)$ eine **Einwegfunktion** ist, wenn es einfach ist, den Wert $y$ zu berechnen, wenn $a$ und $f(x)$ gegeben sind, aber es rechnerisch unpraktikabel ist, den Wert $a$ zu berechnen, wenn $y$ und $f(x)$ gegeben sind. Der Name **Einwegfunktion** stammt natürlich von der Tatsache, dass eine solche Funktion nur in eine Richtung praktisch zu berechnen ist.

Einige Einwegfunktionen haben das, was als **Falltür** bekannt ist. Während es praktisch unmöglich ist, $a$ zu berechnen, wenn nur $y$ und $f(x)$ gegeben sind, gibt es ein bestimmtes Stück Information $Z$, das das Berechnen von $a$ aus $y$ rechnerisch machbar macht. Dieses Stück Information $Z$ ist als die **Falltür** bekannt. Einwegfunktionen, die eine Falltür haben, sind als **Falltürfunktionen** bekannt.
Wir werden hier nicht ins Detail des Diffie-Hellman-Schlüsselaustauschs gehen. Aber im Wesentlichen erstellt jeder Teilnehmer einige Informationen, von denen ein Teil öffentlich geteilt und ein Teil geheim gehalten wird. Jede Partei nimmt dann ihr geheimes Informationsstück und die von der anderen Partei öffentlich geteilten Informationen, um einen privaten Schlüssel zu erstellen. Und etwas wunderbarerweise enden beide Parteien mit demselben privaten Schlüssel.
Jede Partei, die nur die öffentlich geteilten Informationen zwischen den beiden Parteien in einem Diffie-Hellman-Schlüsselaustausch beobachtet, ist nicht in der Lage, diese Berechnungen zu replizieren. Sie würden die privaten Informationen von einer der beiden Parteien benötigen, um dies zu tun.

Obwohl die Basisversion des Diffie-Hellman-Schlüsselaustauschs, die im Papier von 1976 vorgestellt wurde, nicht sehr sicher ist, sind ausgefeiltere Versionen des Basisprotokolls heute sicherlich noch in Gebrauch. Am wichtigsten ist, dass jedes Schlüsselaustauschprotokoll in der neuesten Version des Transport Layer Security Protokolls (Version 1.3) im Wesentlichen eine angereicherte Version des Protokolls ist, das von Diffie und Hellman im Jahr 1976 vorgestellt wurde. Das Transport Layer Security Protokoll ist das vorherrschende Protokoll für den sicheren Austausch von Informationen, die gemäß dem Hypertext Transfer Protocol (http) formatiert sind, dem Standard für den Austausch von Webinhalten.

Wichtig ist, dass der Diffie-Hellman-Schlüsselaustausch kein asymmetrisches Schema ist. Streng genommen gehört er wohl eher in den Bereich der symmetrischen Schlüsselkryptografie. Aber da sowohl der Diffie-Hellman-Schlüsselaustausch als auch die asymmetrische Kryptografie auf einseitigen zahlentheoretischen Funktionen mit Falltüren basieren, werden sie typischerweise zusammen diskutiert.

Der zweite Weg, den Diffie und Hellman anboten, um das Problem der Schlüsselverteilung und -verwaltung in ihrem Papier von 1976 anzugehen, war natürlich über die asymmetrische Kryptografie.

Im Gegensatz zu ihrer Darstellung des Diffie-Hellman-Schlüsselaustauschs lieferten sie nur die allgemeinen Umrisse, wie asymmetrische kryptografische Schemata plausibel konstruiert werden könnten. Sie boten keine spezifische Einwegfunktion an, die die Bedingungen für eine vernünftige Sicherheit in solchen Schemata speziell erfüllen könnte.

Eine praktische Implementierung eines asymmetrischen Schemas wurde jedoch ein Jahr später von drei verschiedenen akademischen Kryptografen und Mathematikern gefunden: Ronald Rivest, Adi Shamir und Leonard Adleman. [3] Das von ihnen eingeführte Kryptosystem wurde als **RSA-Kryptosystem** (nach ihren Nachnamen) bekannt.

Die Falltürfunktionen, die in der asymmetrischen Kryptografie (und dem Diffie-Hellman-Schlüsselaustausch) verwendet werden, sind alle mit zwei Hauptarten von **rechnerisch schwierigen Problemen** verbunden: der Primfaktorzerlegung und der Berechnung diskreter Logarithmen.

**Primfaktorzerlegung** erfordert, wie der Name schon sagt, eine Zahl in ihre Primfaktoren zu zerlegen. Das RSA-Problem ist bei weitem das bekannteste Beispiel für ein Kryptosystem, das mit der Primfaktorzerlegung zusammenhängt.

Das **Problem des diskreten Logarithmus** tritt in zyklischen Gruppen auf. Gegeben ein Generator in einer bestimmten zyklischen Gruppe, erfordert es die Berechnung des einzigartigen Exponenten, der benötigt wird, um ein anderes Element in der Gruppe aus dem Generator zu erzeugen.

Auf dem diskreten Logarithmus basierende Schemata stützen sich auf zwei Hauptarten von zyklischen Gruppen: multiplikative Gruppen von Ganzzahlen und Gruppen, die die Punkte auf elliptischen Kurven einschließen. Der ursprüngliche Diffie-Hellman-Schlüsselaustausch, wie er in „New Directions in Cryptography“ vorgestellt wurde, arbeitet mit einer zyklischen multiplikativen Gruppe von Ganzzahlen. Bitcoins digitales Signaturverfahren und das kürzlich eingeführte Schnorr-Signaturschema (2021) basieren beide auf dem Problem des diskreten Logarithmus für eine bestimmte elliptische Kurvenzyklusgruppe.

Als Nächstes werden wir uns einen Überblick über Geheimhaltung und Authentifizierung im asymmetrischen Kontext verschaffen. Bevor wir dies jedoch tun, müssen wir eine kurze historische Anmerkung machen.
Es scheint nun plausibel, dass eine Gruppe britischer Kryptografen und Mathematiker, die für das Government Communications Headquarters (GCHQ) arbeiteten, die oben genannten Entdeckungen einige Jahre früher unabhängig gemacht hatten. Diese Gruppe bestand aus James Ellis, Clifford Cocks und Malcolm Williamson.
Nach ihren eigenen Aussagen und denen des GCHQ war es James Ellis, der 1969 das Konzept der Public-Key-Kryptografie erstmals entwickelte. Angeblich entdeckte daraufhin Clifford Cocks 1973 das RSA-Kryptographiesystem und Malcolm Williamson 1974 das Konzept des Diffie-Hellman-Schlüsselaustauschs. [4] Ihre Entdeckungen wurden jedoch angeblich erst 1997 bekannt gegeben, angesichts der geheimen Natur der Arbeit beim GCHQ.

**Notizen:**

[1] Whitfield Diffie und Martin Hellman, „Neue Richtungen in der Kryptografie“, _IEEE Transactions on Information Theory_ IT-22 (1976), S. 644–654, auf S. 644.

[2] Ralph Merkle diskutiert ebenfalls ein Schlüsselaustauschprotokoll in „Sichere Kommunikation über unsichere Kanäle“, _Communications of the Association for Computing Machinery_, 21 (1978), 294–99. Obwohl Merkle dieses Papier vor dem von Diffie und Hellman einreichte, wurde es später veröffentlicht. Merkles Lösung ist nicht exponentiell sicher, im Gegensatz zu Diffie-Hellman.

[3] Ron Rivest, Adi Shamir und Leonard Adleman, „Eine Methode zur Erlangung digitaler Signaturen und Public-Key-Kryptosysteme“, _Communications of the Association for Computing Machinery_, 21 (1978), S. 120–26.

[4] Eine gute Geschichte dieser Entdeckungen wird von Simon Singh in _The Code Book_, Fourth Estate (London, 1999), Kapitel 6, bereitgestellt.

## Asymmetrische Verschlüsselung und Authentifizierung
<chapterId>2f6f0f03-3c3d-5025-90f0-5211139bc0cc</chapterId>

Ein Überblick über **asymmetrische Verschlüsselung** mit Hilfe von Bob und Alice wird in *Abbildung 1* dargestellt.

Alice erstellt zunächst ein Paar von Schlüsseln, bestehend aus einem öffentlichen Schlüssel ($K_P$) und einem privaten Schlüssel ($K_S$), wobei das „P“ in $K_P$ für „public“ (öffentlich) und das „S“ in $K_S$ für „secret“ (geheim) steht. Sie verteilt diesen öffentlichen Schlüssel dann frei an andere. Wir werden später auf die Details dieses Verteilungsprozesses zurückkommen. Aber zunächst nehmen wir an, dass jeder, einschließlich Bob, den öffentlichen Schlüssel $K_P$ von Alice sicher erhalten kann.

Zu einem späteren Zeitpunkt möchte Bob eine Nachricht $M$ an Alice schreiben. Da sie sensible Informationen enthält, möchte er, dass der Inhalt für jeden außer Alice geheim bleibt. Also verschlüsselt Bob seine Nachricht $M$ zunächst mit $K_P$. Anschließend sendet er den resultierenden Chiffretext $C$ an Alice, die $C$ mit $K_S$ entschlüsselt, um die ursprüngliche Nachricht $M$ zu erhalten.

*Abbildung 1: Asymmetrische Verschlüsselung*

![Abbildung 1: Asymmetrische Verschlüsselung](assets/Figure6-1.webp "Abbildung 1: Asymmetrische Verschlüsselung")

Jeder Gegner, der die Kommunikation zwischen Bob und Alice abhört, kann $C$ beobachten. Sie kennt auch $K_P$ und den Verschlüsselungsalgorithmus $E(\cdot)$. Wichtig ist jedoch, dass diese Informationen es dem Angreifer nicht ermöglichen, den Chiffretext $C$ praktikabel zu entschlüsseln. Zum Entschlüsseln wird speziell $K_S$ benötigt, welches der Angreifer nicht besitzt.
Symmetrische Verschlüsselungsverfahren müssen in der Regel sicher gegenüber einem Angreifer sein, der gültige Klartextnachrichten verschlüsseln kann (bekannt als Sicherheit gegenüber Angriffen mit gewähltem Chiffretext). Sie sind jedoch nicht explizit dafür ausgelegt, die Erstellung solcher gültigen Chiffretexte durch einen Angreifer oder jemand anderen zu ermöglichen.
Dies steht im starken Kontrast zu einem asymmetrischen Verschlüsselungsverfahren, dessen ganzer Zweck es ist, jedem, einschließlich Angreifern, zu ermöglichen, gültige Chiffretexte zu erzeugen. Asymmetrische Verschlüsselungsverfahren können daher als **Mehrfachzugriffs-Chiffren** bezeichnet werden.

Um besser zu verstehen, was passiert, stellen Sie sich vor, dass Bob anstelle einer elektronischen Nachricht einen physischen Brief im Geheimen senden wollte. Eine Möglichkeit, die Geheimhaltung zu gewährleisten, wäre, dass Alice Bob ein sicheres Vorhängeschloss zusendet, aber den Schlüssel dafür behält. Nachdem er seinen Brief geschrieben hat, könnte Bob den Brief in eine Kiste legen und diese mit Alices Vorhängeschloss verschließen. Anschließend könnte er die verschlossene Kiste mit der Nachricht an Alice senden, die den Schlüssel hat, um sie zu öffnen.

Obwohl Bob in der Lage ist, das Vorhängeschloss zu verschließen, kann weder er noch eine andere Person, die die Kiste abfängt, das Vorhängeschloss öffnen, wenn es tatsächlich sicher ist. Nur Alice kann es öffnen und den Inhalt von Bobs Brief sehen, weil sie den Schlüssel hat.

Ein asymmetrisches Verschlüsselungsverfahren ist, grob gesagt, eine digitale Version dieses Prozesses. Das Vorhängeschloss entspricht dem öffentlichen Schlüssel und der Schlüssel des Vorhängeschlosses dem privaten Schlüssel. Da das Vorhängeschloss digital ist, ist es jedoch viel einfacher und nicht so kostspielig für Alice, es an jeden zu verteilen, der ihr geheime Nachrichten senden möchte.

Für die Authentifizierung im asymmetrischen Kontext verwenden wir **digitale Signaturen**. Diese haben somit die gleiche Funktion wie Nachrichtenauthentifizierungscodes im symmetrischen Kontext. Ein Überblick über digitale Signaturen wird in *Abbildung 2* gegeben.

Bob erstellt zunächst ein Paar von Schlüsseln, bestehend aus dem öffentlichen Schlüssel ($K_P$) und dem privaten Schlüssel ($K_S$), und verteilt seinen öffentlichen Schlüssel. Wenn er Alice eine authentifizierte Nachricht senden möchte, nimmt er zuerst seine Nachricht $M$ und seinen privaten Schlüssel, um eine **digitale Signatur** $D$ zu erstellen. Bob sendet dann Alice seine Nachricht zusammen mit der digitalen Signatur.

Alice fügt die Nachricht, den öffentlichen Schlüssel und die digitale Signatur in einen **Verifizierungsalgorithmus** ein. Dieser Algorithmus liefert entweder **wahr** für eine gültige Signatur oder **falsch** für eine ungültige Signatur.

Eine digitale Signatur ist, wie der Name klar impliziert, das digitale Äquivalent einer handschriftlichen Unterschrift auf Briefen, Verträgen und so weiter. Tatsächlich ist eine digitale Signatur in der Regel viel sicherer. Mit einigem Aufwand kann man eine handschriftliche Unterschrift fälschen; ein Prozess, der dadurch erleichtert wird, dass handschriftliche Unterschriften häufig nicht genau überprüft werden. Eine sichere digitale Signatur ist jedoch, genau wie ein sicherer Nachrichtenauthentifizierungsscode, **existenziell unfälschbar**: das heißt, mit einem sicheren digitalen Signaturschema kann niemand eine Signatur für eine Nachricht erstellen, die das Verifizierungsverfahren besteht, es sei denn, er hat den privaten Schlüssel.

*Abbildung 2: Asymmetrische Authentifizierung*

![Abbildung 2: Asymmetrische Authentifizierung](assets/Figure6-2.webp "Abbildung 2: Asymmetrische Authentifizierung")

Wie bei der asymmetrischen Verschlüsselung sehen wir einen interessanten Kontrast zwischen digitalen Signaturen und Nachrichtenauthentifizierungscodes. Bei letzteren kann der Verifizierungsalgorithmus nur von einer der Parteien verwendet werden, die an der sicheren Kommunikation beteiligt sind. Dies liegt daran, dass er einen privaten Schlüssel benötigt. Im asymmetrischen Kontext kann jedoch jeder eine digitale Signatur $S$, die von Bob erstellt wurde, überprüfen.
All dies macht digitale Signaturen zu einem äußerst mächtigen Werkzeug. Sie bilden die Grundlage, beispielsweise für das Erstellen von Signaturen auf Verträgen, die aus rechtlicher Sicht verifiziert werden können. Wenn Bob eine Signatur auf einem Vertrag in dem oben genannten Austausch gemacht hätte, könnte Alice die Nachricht $M$, den Vertrag und die Signatur $S$ einem Gericht vorlegen. Das Gericht kann dann die Signatur mit Bobs öffentlichem Schlüssel verifizieren. [5]
Als weiteres Beispiel sind digitale Signaturen ein wichtiger Aspekt der sicheren Software und der Verteilung von Software-Updates. Diese Art der öffentlichen Überprüfbarkeit könnte niemals allein mit Nachrichtenauthentifizierungscodes geschaffen werden.

Als letztes Beispiel für die Macht digitaler Signaturen betrachten Sie Bitcoin. Eines der häufigsten Missverständnisse über Bitcoin, insbesondere in den Medien, ist, dass Transaktionen verschlüsselt sind: Das sind sie nicht. Stattdessen arbeiten Bitcoin-Transaktionen mit digitalen Signaturen, um Sicherheit zu gewährleisten.

Bitcoins existieren in Bündeln, die als unverbrauchte Transaktionsausgänge (oder **UTXO’s**) bezeichnet werden. Nehmen wir an, Sie erhalten drei Zahlungen auf eine bestimmte Bitcoin-Adresse von jeweils 2 Bitcoins. Technisch gesehen haben Sie jetzt nicht 6 Bitcoins auf dieser Adresse. Stattdessen haben Sie drei Bündel von 2 Bitcoins, die durch ein kryptografisches Problem, das mit dieser Adresse verbunden ist, gesperrt sind. Für jede Zahlung, die Sie tätigen, können Sie eines, zwei oder alle drei dieser Bündel verwenden, je nachdem, wie viel Sie für die Transaktion benötigen.

Der Nachweis des Eigentums über unverbrauchte Transaktionsausgänge wird normalerweise über eine oder mehrere digitale Signaturen gezeigt. Bitcoin funktioniert genau deshalb, weil gültige digitale Signaturen auf unverbrauchten Transaktionsausgängen rechnerisch unmöglich zu erstellen sind, es sei denn, man besitzt die geheimen Informationen, die dafür benötigt werden.

Derzeit beinhalten Bitcoin-Transaktionen transparent alle Informationen, die von den Teilnehmern im Netzwerk verifiziert werden müssen, wie die Herkunft der in der Transaktion verwendeten unverbrauchten Transaktionsausgänge. Während es möglich ist, einige dieser Informationen zu verbergen und dennoch eine Verifizierung zu ermöglichen (wie es einige alternative Kryptowährungen wie Monero tun), schafft dies auch bestimmte Sicherheitsrisiken.

Verwirrung entsteht manchmal über digitale Signaturen und schriftlich erfasste Signaturen digital. Im letzteren Fall erfassen Sie ein Bild Ihrer schriftlichen Signatur und fügen es einem elektronischen Dokument wie einem Arbeitsvertrag bei. Dies ist jedoch keine digitale Signatur im kryptografischen Sinne. Letzteres ist nur eine lange Zahl, die nur durch den Besitz eines privaten Schlüssels erzeugt werden kann.

Wie im symmetrischen Schlüssel-Setting können Sie auch asymmetrische Verschlüsselungs- und Authentifizierungsschemata zusammen verwenden. Ähnliche Prinzipien gelten. Zunächst sollten Sie unterschiedliche private-öffentliche Schlüsselpaare für die Verschlüsselung und das Erstellen digitaler Signaturen verwenden. Zusätzlich sollten Sie zuerst eine Nachricht verschlüsseln und dann authentifizieren.

Wichtig ist, dass in vielen Anwendungen asymmetrische Kryptografie nicht während des gesamten Kommunikationsprozesses verwendet wird. Stattdessen wird sie typischerweise nur verwendet, um *symmetrische Schlüssel* zwischen den Parteien auszutauschen, mit denen sie tatsächlich kommunizieren werden.

Dies ist beispielsweise der Fall, wenn Sie Waren online kaufen. Wenn Sie den öffentlichen Schlüssel des Verkäufers kennen, kann sie Ihnen digital signierte Nachrichten senden, deren Authentizität Sie überprüfen können. Auf dieser Grundlage können Sie einem von mehreren Protokollen folgen, um symmetrische Schlüssel auszutauschen, um sicher zu kommunizieren.

Der Hauptgrund für die Häufigkeit des oben genannten Ansatzes ist, dass asymmetrische Kryptografie viel weniger effizient als symmetrische Kryptografie ist, um ein bestimmtes Sicherheitsniveau zu erzeugen. Dies ist ein Grund, warum wir neben der öffentlichen Kryptografie immer noch symmetrische Schlüsselkryptografie benötigen. Darüber hinaus ist symmetrische Schlüsselkryptografie in bestimmten Anwendungen, wie einem Computerbenutzer, der seine eigenen Daten verschlüsselt, viel natürlicher.

Wie genau adressieren also digitale Signaturen und öffentliche Schlüsselverschlüsselung die Probleme der Schlüsselverteilung und des Schlüsselmanagements?
Es gibt nicht nur eine Antwort hier. Asymmetrische Kryptografie ist ein Werkzeug, und es gibt nicht nur eine Art, dieses Werkzeug zu verwenden. Aber nehmen wir unser früheres Beispiel von Jim’s Sporting Goods, um zu zeigen, wie die Probleme in diesem Beispiel typischerweise angegangen würden.
Zu Beginn würde Jim’s Sporting Goods sich wahrscheinlich an eine **Zertifizierungsstelle** wenden, eine Organisation, die bei der Verteilung öffentlicher Schlüssel unterstützt. Die Zertifizierungsstelle würde einige Details über Jim’s Sporting Goods registrieren und ihm einen öffentlichen Schlüssel gewähren. Dann würde sie Jim’s Sporting Goods ein Zertifikat, bekannt als **TLS/SSL-Zertifikat**, mit dem öffentlichen Schlüssel von Jim’s Sporting Goods digital signiert mit dem eigenen öffentlichen Schlüssel der Zertifizierungsstelle, zusenden. Auf diese Weise bestätigt die Zertifizierungsstelle, dass ein bestimmter öffentlicher Schlüssel tatsächlich zu Jim’s Sporting Goods gehört.

Der Schlüssel zum Verständnis dieses Prozesses mit TLS/SSL-Zertifikaten ist, dass, obwohl Sie den öffentlichen Schlüssel von Jim’s Sporting Goods im Allgemeinen nirgendwo auf Ihrem Computer gespeichert haben werden, die öffentlichen Schlüssel anerkannter Zertifizierungsstellen tatsächlich in Ihrem Browser oder in Ihrem Betriebssystem gespeichert sind. Diese sind in sogenannten **Root-Zertifikaten** gespeichert.

Daher, wenn Jim’s Sporting Goods Ihnen sein TLS/SSL-Zertifikat zur Verfügung stellt, können Sie die digitale Signatur der Zertifizierungsstelle über ein Root-Zertifikat in Ihrem Browser oder Betriebssystem verifizieren. Wenn die Signatur gültig ist, können Sie relativ sicher sein, dass der öffentliche Schlüssel auf dem Zertifikat tatsächlich zu Jim’s Sporting Goods gehört. Auf dieser Grundlage ist es einfach, ein Protokoll für sichere Kommunikation mit Jim’s Sporting Goods einzurichten.

Die Schlüsselverteilung ist nun für Jim’s Sporting Goods wesentlich einfacher geworden. Es ist nicht schwer zu erkennen, dass auch das Schlüsselmanagement erheblich vereinfacht wurde. Anstatt tausende von Schlüsseln speichern zu müssen, muss Jim’s Sporting Goods lediglich einen privaten Schlüssel speichern, der es ihm ermöglicht, Signaturen für den öffentlichen Schlüssel auf seinem SSL-Zertifikat zu erstellen. Jedes Mal, wenn ein Kunde die Seite von Jim’s Sporting Goods besucht, können sie eine sichere Kommunikationssitzung von diesem öffentlichen Schlüssel aus etablieren. Kunden müssen auch keine Informationen speichern (außer den öffentlichen Schlüsseln anerkannter Zertifizierungsstellen in ihrem Betriebssystem und Browser).

**Notizen:**

[5] Jedes Schema, das versucht, Nichtabstreitbarkeit zu erreichen, das andere Thema, das wir in Kapitel 1 besprochen haben, muss auf digitalen Signaturen basieren.

## Hash-Funktionen
<chapterId>ea8327ab-b0e3-5635-941c-4b51f396a648</chapterId>

Hash-Funktionen sind allgegenwärtig in der Kryptografie. Sie sind weder symmetrische noch asymmetrische Schemata, sondern fallen in ihre eigene kryptografische Kategorie.

Wir sind bereits in Kapitel 4 auf Hash-Funktionen gestoßen bei der Erstellung von hash-basierten Authentifizierungsnachrichten. Sie sind auch wichtig im Kontext von digitalen Signaturen, allerdings aus einem etwas anderen Grund: Digitale Signaturen werden nämlich typischerweise über den Hash-Wert einer (verschlüsselten) Nachricht gemacht, anstatt über die eigentliche (verschlüsselte) Nachricht. In diesem Abschnitt werde ich eine gründlichere Einführung in Hash-Funktionen bieten.

Lassen Sie uns mit der Definition einer Hash-Funktion beginnen. Eine **Hash-Funktion** ist jede effizient berechenbare Funktion, die Eingaben beliebiger Größe nimmt und Ausgaben fester Länge liefert.

Eine **kryptografische Hash-Funktion** ist einfach eine Hash-Funktion, die für Anwendungen in der Kryptografie nützlich ist. Die Ausgabe einer kryptografischen Hash-Funktion wird typischerweise als **Hash**, **Hash-Wert** oder **Nachrichten-Hash** bezeichnet.

Im Kontext der Kryptografie bezieht sich „Hash-Funktion“ typischerweise auf eine kryptografische Hash-Funktion. Ich werde diese Praxis von nun an übernehmen.
Ein Beispiel für eine beliebte Hash-Funktion ist **SHA-256** (Secure Hash Algorithm 256). Unabhängig von der Größe der Eingabe (z.B. 15 Bits, 100 Bits oder 10.000 Bits) liefert diese Funktion einen 256-Bit-Hashwert. Unten können Sie einige Beispieloutputs der SHA-256-Funktion sehen.
„Hello“: `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`

„52398“: `a3b14d2bf378c1bd47e7f8eaec63b445150a3d7a80465af16dd9fd319454ba90`

„Kryptografie macht Spaß“: `3cee2a5c7d2cc1d62db4893564c34ae553cc88623992d994e114e344359b146c`

Alle Outputs sind genau 256 Bits lang und im hexadezimalen Format geschrieben (jede Hexadezimalziffer kann durch vier Binärziffern dargestellt werden). Selbst wenn Sie das Buch *Der Herr der Ringe* von Tolkien in die SHA-256-Funktion eingegeben hätten, wäre der Output immer noch 256 Bits lang.

Hash-Funktionen wie SHA-256 werden zu verschiedenen Zwecken in der Kryptografie eingesetzt. Welche Eigenschaften von einer Hash-Funktion gefordert werden, hängt wirklich vom Kontext einer bestimmten Anwendung ab. Es gibt zwei Hauptmerkmale, die allgemein von Hash-Funktionen in der Kryptografie gewünscht werden: [6]

1.	Kollisionsresistenz
2.	Verbergen

Eine Hash-Funktion $H$ gilt als **kollisionsresistent**, wenn es unpraktikabel ist, zwei Werte $x$ und $y$ zu finden, sodass $x \neq y$, aber $H(x) = H(y)$.

Kollisionsresistente Hash-Funktionen sind beispielsweise bei der Verifizierung von Software wichtig. Nehmen wir an, Sie möchten die Windows-Version von Bitcoin Core 0.21.0 (eine Serveranwendung zur Verarbeitung von Bitcoin-Netzwerkverkehr) herunterladen. Die Hauptschritte, die Sie zur Überprüfung der Legitimität der Software unternehmen müssten, sind wie folgt:

1.	Zuerst müssen Sie die öffentlichen Schlüssel eines oder mehrerer Bitcoin Core-Beitragenden herunterladen und in eine Software importieren, die digitale Signaturen verifizieren kann (z.B. Kleopetra). Diese öffentlichen Schlüssel finden Sie [hier](https://github.com/bitcoin/bitcoin/blob/master/contrib/builder-keys/keys.txt). Es wird empfohlen, die Bitcoin Core-Software mit den öffentlichen Schlüsseln mehrerer Beitragender zu verifizieren.
2.	Als Nächstes müssen Sie die importierten öffentlichen Schlüssel verifizieren. Ein Schritt, den Sie mindestens unternehmen sollten, ist zu überprüfen, ob die öffentlichen Schlüssel, die Sie gefunden haben, mit denen übereinstimmen, die an verschiedenen anderen Orten veröffentlicht wurden. Sie könnten beispielsweise die persönlichen Webseiten, Twitter-Seiten oder Github-Seiten der Personen konsultieren, deren öffentliche Schlüssel Sie importiert haben. Typischerweise wird dieser Vergleich der öffentlichen Schlüssel durch Vergleichen eines kurzen Hashs des öffentlichen Schlüssels, bekannt als Fingerabdruck, durchgeführt.
3.	Als Nächstes müssen Sie das ausführbare Programm von Bitcoin Core von deren [Website](www.bitcoincore.org) herunterladen. Es werden Pakete für Linux-, Windows- und MAC-Betriebssysteme verfügbar sein.
4.	Danach müssen Sie zwei Release-Dateien lokalisieren. Die erste enthält den offiziellen SHA-256-Hash für das heruntergeladene ausführbare Programm zusammen mit den Hashes über alle anderen veröffentlichten Pakete. Eine andere Release-Datei wird die Signaturen verschiedener Beitragender über die Release-Datei mit den Pakethashes enthalten. Beide Release-Dateien sollten auf der Bitcoin Core-Website zu finden sein.
5. Als Nächstes müssten Sie den SHA-256-Hash des ausführbaren Programms berechnen, das Sie von der Bitcoin Core-Website auf Ihren eigenen Computer heruntergeladen haben. Dann vergleichen Sie dieses Ergebnis mit dem des offiziellen Paket-Hashs für das ausführbare Programm. Sie sollten identisch sein. 6. Schließlich müssten Sie überprüfen, ob eine oder mehrere der digitalen Signaturen über der Release-Datei mit den offiziellen Paket-Hashs tatsächlich einer oder mehreren öffentlichen Schlüsseln entsprechen, die Sie importiert haben (Releases von Bitcoin Core sind nicht immer von jedem signiert). Dies können Sie mit einer Anwendung wie Kleopetra tun.

Dieser Prozess der Softwareverifizierung hat zwei Hauptvorteile. Erstens stellt er sicher, dass beim Herunterladen von der Bitcoin Core-Website keine Übertragungsfehler aufgetreten sind. Zweitens stellt er sicher, dass kein Angreifer Sie dazu bringen konnte, modifizierten, bösartigen Code herunterzuladen, entweder durch Hacking der Bitcoin Core-Website oder durch Abfangen des Datenverkehrs.

Wie genau schützt der oben beschriebene Softwareverifizierungsprozess vor diesen Problemen?

Wenn Sie die öffentlichen Schlüssel, die Sie importiert haben, sorgfältig verifiziert haben, dann können Sie ziemlich sicher sein, dass diese Schlüssel tatsächlich ihnen gehören und nicht kompromittiert wurden. Da digitale Signaturen existenzielle Unfälschbarkeit aufweisen, wissen Sie, dass nur diese Beitragenden eine digitale Signatur über den offiziellen Paket-Hashs auf der Release-Datei gemacht haben könnten.

Angenommen, die Signaturen auf der heruntergeladenen Release-Datei stimmen überein. Sie können nun den Hash-Wert, den Sie lokal für das Windows ausführbare Programm berechnet haben, das Sie heruntergeladen haben, mit dem im ordnungsgemäß signierten Release-Dokument enthaltenen vergleichen. Da Sie wissen, dass die SHA-256-Hashfunktion kollisionsresistent ist, bedeutet eine Übereinstimmung, dass Ihr ausführbares Programm genau dasselbe ist wie das offizielle ausführbare Programm.

Wenden wir uns nun der zweiten gemeinsamen Eigenschaft von Hash-Funktionen zu: **Verbergen**. Eine Hash-Funktion $H$ wird als verbergend bezeichnet, wenn es für ein zufällig ausgewähltes $x$ aus einem sehr großen Bereich unpraktikabel ist, $x$ zu finden, wenn nur $H(x)$ gegeben ist.

Unten können Sie den SHA-256-Output einer Nachricht sehen, die ich geschrieben habe. Um ausreichende Zufälligkeit zu gewährleisten, enthielt die Nachricht am Ende eine zufällig generierte Zeichenfolge. Da SHA-256 die Eigenschaft des Verbergens hat, wäre es niemandem möglich, diese Nachricht zu entschlüsseln.

- `b194221b37fa4cd1cfce15aaef90351d70de17a98ee6225088b523b586c32ded`

Aber ich werde Sie nicht in Spannung lassen, bis SHA-256 schwächer wird. Die ursprüngliche Nachricht, die ich geschrieben habe, lautete wie folgt:

* „Dies ist eine sehr zufällige Nachricht, oder naja, irgendwie zufällig. Dieser Anfangsteil ist es nicht, aber ich werde mit einigen relativ zufälligen Zeichen enden, um eine sehr unvorhersehbare Nachricht zu gewährleisten. XLWz4dVG3BxUWm7zQ9qS“.

Eine gängige Art und Weise, wie Hash-Funktionen mit der Eigenschaft des Verbergens verwendet werden, ist im Passwortmanagement (Kollisionsresistenz ist auch für diese Anwendung wichtig). Jeder anständige Online-Kontodienst wie Facebook oder Google wird Ihre Passwörter nicht direkt speichern, um den Zugang zu Ihrem Konto zu verwalten. Stattdessen speichern sie nur einen Hash Ihres Passworts. Jedes Mal, wenn Sie Ihr Passwort in einem Browser eingeben, wird zuerst ein Hash berechnet. Nur dieser Hash wird an den Server des Dienstanbieters gesendet und mit dem Hash verglichen, der in der Backend-Datenbank gespeichert ist. Die Eigenschaft des Verbergens kann helfen sicherzustellen, dass Angreifer es nicht aus dem Hash-Wert wiederherstellen können.
Passwortverwaltung durch Hashes funktioniert natürlich nur, wenn Benutzer tatsächlich schwierige Passwörter wählen. Die Verbergungseigenschaft setzt voraus, dass x zufällig aus einem sehr großen Bereich ausgewählt wird. Die Auswahl von Passwörtern wie „1234“, „meinpasswort“ oder Ihr Geburtsdatum bietet keine echte Sicherheit. Lange Listen von gängigen Passwörtern und deren Hashes existieren, welche Angreifer nutzen können, falls sie jemals den Hash Ihres Passworts erhalten. Diese Arten von Angriffen sind als **Wörterbuchangriffe** bekannt. Wenn Angreifer einige Ihrer persönlichen Details kennen, könnten sie auch einige informierte Vermutungen anstellen. Daher benötigen Sie immer lange, sichere Passwörter (vorzugsweise lange, zufällige Zeichenfolgen aus einem Passwortmanager).

Manchmal könnte eine Anwendung eine Hash-Funktion benötigen, die sowohl Kollisionsresistenz als auch Verbergung aufweist. Aber sicherlich nicht immer. Der Software-Verifizierungsprozess, den wir besprochen haben, erfordert zum Beispiel nur, dass die Hash-Funktion Kollisionsresistenz aufzeigt, Verbergung ist nicht wichtig.

Während Kollisionsresistenz und Verbergung die Hauptmerkmale sind, die von Hash-Funktionen in der Kryptographie gesucht werden, könnten in bestimmten Anwendungen auch andere Arten von Eigenschaften wünschenswert sein.

**Notizen:**

[6] Die Terminologie „Verbergung“ ist keine allgemeine Sprache, sondern speziell entnommen aus Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller und Steven Goldfeder, *Bitcoin und Kryptowährungstechnologien*, Princeton University Press (Princeton, 2016), Kapitel 1.

# Das RSA-Kryptosystem
<partId>864dca42-2a8d-530f-bb94-2e1f68b3f411</partId>

## Das Faktorisierungsproblem
<chapterId>a31a66e4-52ea-539c-9953-4769ad565d7e</chapterId>

Während symmetrische Kryptographie für die meisten Menschen in der Regel recht intuitiv ist, ist dies typischerweise nicht der Fall bei asymmetrischer Kryptographie. Obwohl Sie wahrscheinlich mit der hochrangigen Beschreibung, die in den vorherigen Abschnitten angeboten wurde, vertraut sind, fragen Sie sich wahrscheinlich, was genau Einwegfunktionen sind und wie genau sie verwendet werden, um asymmetrische Schemata zu konstruieren.

In diesem Kapitel werde ich etwas von dem Geheimnis um die asymmetrische Kryptographie lüften, indem ich tiefer in ein spezifisches Beispiel eintauche, nämlich das RSA-Kryptosystem. Im ersten Abschnitt werde ich das Faktorisierungsproblem vorstellen, auf dem das RSA-Problem basiert. Dann werde ich eine Reihe von Schlüsselergebnissen aus der Zahlentheorie abdecken. Im letzten Abschnitt werden wir diese Informationen zusammenführen, um das RSA-Problem zu erklären und wie dies für die Erstellung asymmetrischer kryptographischer Schemata verwendet werden kann.

Diese Tiefe unserer Diskussion hinzuzufügen, ist keine leichte Aufgabe. Es erfordert die Einführung von ziemlich vielen zahlentheoretischen Theoremen und Propositionen. Aber lassen Sie sich nicht von der Mathematik abschrecken. Sich durch diese Diskussion zu arbeiten, wird Ihr Verständnis von dem, was der asymmetrischen Kryptographie zugrunde liegt, erheblich verbessern und ist eine lohnende Investition.

Lassen Sie uns nun zuerst zum Faktorisierungsproblem kommen.

___

Wann immer Sie zwei Zahlen multiplizieren, sagen wir $a$ und $b$, bezeichnen wir die Zahlen $a$ und $b$ als **Faktoren** und das Ergebnis als das **Produkt**. Den Versuch, eine Zahl $N$ in die Multiplikation von zwei oder mehr Faktoren zu schreiben, nennt man **Faktorisierung** oder **Faktorisieren**. [1] Jedes Problem, das dies erfordert, können Sie ein **Faktorisierungsproblem** nennen.

Vor etwa 2.500 Jahren entdeckte der griechische Mathematiker Euklid von Alexandria einen Schlüsselsatz über die Faktorisierung von Ganzzahlen. Er wird allgemein als **Eindeutiger Faktorisierungssatz** bezeichnet und besagt Folgendes:

**Theorem 1**. Jede Ganzzahl $N$, die größer als 1 ist, ist entweder eine Primzahl oder kann als Produkt von Primfaktoren ausgedrückt werden.
Der letzte Teil dieser Aussage bedeutet lediglich, dass Sie jede nicht-prime ganze Zahl $N$, die größer als 1 ist, als Multiplikation von Primzahlen darstellen können. Unten finden Sie mehrere Beispiele für nicht-prime ganze Zahlen, die als Produkt von Primfaktoren geschrieben sind.
* $18 = 2 \cdot 3 \cdot 3 = 2 \cdot 3^2$
* $84 = 2 \cdot 2 \cdot 3 \cdot 7 = 2^2 \cdot 3 \cdot 7$
* $144 = 2 \cdot 2 \cdot 2 \cdot 2 \cdot 3 \cdot 3 = 2^4 \cdot 3^2$

Für alle drei der oben genannten ganzen Zahlen ist die Berechnung ihrer Primfaktoren relativ einfach, selbst wenn Ihnen nur $N$ gegeben ist. Sie beginnen mit der kleinsten Primzahl, nämlich 2, und sehen, wie oft die ganze Zahl $N$ durch sie teilbar ist. Dann gehen Sie dazu über, die Teilbarkeit von $N$ durch 3, 5, 7 und so weiter zu testen. Sie setzen diesen Prozess fort, bis Ihre ganze Zahl $N$ als Produkt von nur Primzahlen geschrieben ist.

Nehmen wir zum Beispiel die ganze Zahl 84. Unten können Sie den Prozess zur Bestimmung ihrer Primfaktoren sehen. Bei jedem Schritt nehmen wir den kleinsten verbleibenden Primfaktor (links) heraus und bestimmen den verbleibenden Term, der faktorisiert werden soll. Wir fahren fort, bis der verbleibende Term ebenfalls eine Primzahl ist. Bei jedem Schritt wird die aktuelle Faktorisierung von 84 ganz rechts angezeigt.

* Primfaktor = 2: verbleibender Term = 42 	($84 = 2 \cdot 42$)
* Primfaktor = 2: verbleibender Term = 21 	($84 = 2 \cdot 2 \cdot 21$)
* Primfaktor = 3: verbleibender Term = 7 	($84 = 2 \cdot 2 \cdot 3 \cdot 7$)
* Da 7 eine Primzahl ist, ist das Ergebnis $2 \cdot 2 \cdot 3 \cdot 7$ oder $2^2 \cdot 3 \cdot 7$.

Angenommen, $N$ ist sehr groß. Wie schwierig wäre es, $N$ in seine Primfaktoren zu zerlegen?

Das hängt wirklich von $N$ ab. Nehmen wir zum Beispiel an, dass $N$ 50,450,400 ist. Obwohl diese Zahl einschüchternd aussieht, sind die Berechnungen nicht so kompliziert und können leicht von Hand durchgeführt werden. Wie oben beginnen Sie einfach mit 2 und arbeiten sich weiter vor. Unten können Sie das Ergebnis dieses Prozesses in ähnlicher Weise wie oben sehen.

* 2: 25,225,200 	($50,450,400 = 2 \cdot 25,225,200$)  
* 2: 12,612,600 	($50,450,400 = 2^2 \cdot 12,612,600$)  
* 2: 6,306,300 	($50,450,400 = 2^3 \cdot 6,306,300$)  
* 2: 3,153,150 	($50,450,400 = 2^4 \cdot 3,153,150$)  
* 2: 1,576,575 	($50,450,400 = 2^5 \cdot 1,576,575$)
* 3: 525.525 ($50.450.400 = 2^5 \cdot 3 \cdot 525.525$)
* 3: 175.175 ($50.450.400 = 2^5 \cdot 3^2 \cdot 175.175$)
* 5: 35.035 ($50.450.400 = 2^5 \cdot 3^2 \cdot 5 \cdot 35.035$)
* 5: 7.007 ($50.450.400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7.007$)
* 7: 1.001 ($50.450.400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7 \cdot 1.001$)
* 7: 143 ($50.450.400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 143$)
* 11: 13 ($50.450.400 = 2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$)
* Da 13 eine Primzahl ist, ist das Ergebnis $2^5 \cdot 3^2 \cdot 5^2 \cdot 7^2 \cdot 11 \cdot 13$.

Dieses Problem von Hand zu lösen, dauert einige Zeit. Ein Computer kann all dies natürlich in einem Bruchteil einer Sekunde erledigen. Tatsächlich kann ein Computer häufig sogar extrem große ganze Zahlen in einem Bruchteil einer Sekunde faktorisieren.

Es gibt jedoch bestimmte Ausnahmen. Nehmen wir an, wir wählen zuerst zwei sehr große Primzahlen zufällig aus. Es ist üblich, diese mit $p$ und $q$ zu bezeichnen, und ich werde diese Konvention hier übernehmen.

Um konkret zu sein, sagen wir, dass $p$ und $q$ beide 1024-Bit-Primzahlen sind und dass sie tatsächlich mindestens 1024 Bits zur Darstellung benötigen (also muss das erste Bit eine 1 sein). So könnte zum Beispiel 37 nicht eine der Primzahlen sein. Man kann sicherlich 37 mit 1024 Bits darstellen. Aber offensichtlich *benötigt man* nicht so viele Bits, um sie darzustellen. Man kann 37 mit jeder Zeichenfolge darstellen, die 6 Bits oder mehr hat. (In 6 Bits würde 37 als $100101$ dargestellt).

Es ist wichtig zu verstehen, wie groß $p$ und $q$ sind, wenn sie unter den oben genannten Bedingungen ausgewählt werden. Als Beispiel habe ich eine zufällige Primzahl ausgewählt, die mindestens 1024 Bits zur Darstellung benötigt.
* 14.752.173.874.503.595.484.930.006.383.670.759.559.764.562.721.397.166.747.289.220.945.457.932.666.751.048.198.854.920.097.085.690.793.755.254.946.188.163.753.506.778.089.706.699.671.722.089.715.624.760.049.594.106.189.662.669.156.149.028.900.805.928.183.585.427.782.974.951.355.515.394.807.209.836.870.484.558.332.897.443.152.653.214.483.870.992.618.171.825.921.582.253.023.974.514.209.142.520.026.807.636.589

Angenommen, nachdem zufällig Primzahlen $p$ und $q$ ausgewählt wurden, multiplizieren wir sie, um eine ganze Zahl $N$ zu erhalten. Diese ganze Zahl ist daher eine 2048-Bit-Zahl, die mindestens 2048 Bits zu ihrer Darstellung benötigt. Sie ist viel, viel größer als $p$ oder $q$.

Angenommen, Sie geben einem Computer nur $N$ und bitten ihn, die beiden 1024-Bit-Primfaktoren von $N$ zu finden. Die Wahrscheinlichkeit, dass der Computer $p$ und $q$ entdeckt, ist extrem gering. Man kann sagen, es ist für alle praktischen Zwecke unmöglich. Dies gilt selbst dann, wenn Sie einen Supercomputer oder sogar ein Netzwerk von Supercomputern einsetzen würden.

Zunächst einmal, nehmen wir an, dass der Computer versucht, das Problem zu lösen, indem er durch 1024-Bit-Zahlen zyklisch geht und in jedem Fall testet, ob sie prim sind und ob sie Faktoren von $N$ sind. Die Menge der zu testenden Primzahlen ist dann ungefähr $1,265 \cdot 10^{305}$. [2]

Selbst wenn Sie alle Computer auf dem Planeten nehmen und sie versuchen lassen, 1024-Bit-Primzahlen auf diese Weise zu finden und zu testen, würde eine Chance von 1 zu einer Milliarde, erfolgreich einen Primfaktor von $N$ zu finden, eine Rechenzeit erfordern, die viel länger ist als das Alter des Universums.

In der Praxis kann ein Computer jedoch besser als das gerade beschriebene grobe Verfahren abschneiden. Es gibt mehrere Algorithmen, die der Computer anwenden kann, um schneller zu einer Faktorisierung zu kommen. Der Punkt ist jedoch, dass selbst unter Verwendung dieser effizienteren Algorithmen die Aufgabe des Computers immer noch rechnerisch nicht machbar ist. [3]

Wichtig ist, dass die Schwierigkeit der Faktorisierung unter den gerade beschriebenen Bedingungen auf der Annahme beruht, dass es keine rechnerisch effizienten Algorithmen zur Berechnung von Primfaktoren gibt. Wir können tatsächlich nicht beweisen, dass ein effizienter Algorithmus nicht existiert. Dennoch ist diese Annahme sehr plausibel: Trotz umfangreicher Bemühungen über Hunderte von Jahren haben wir bisher keinen solchen rechnerisch effizienten Algorithmus gefunden.

Daher kann das Faktorisierungsproblem unter bestimmten Umständen plausiblerweise als ein schwieriges Problem angesehen werden. Insbesondere, wenn $p$ und $q$ sehr große Primzahlen sind, ist ihr Produkt $N$ nicht schwer zu berechnen; aber die Faktorisierung, nur gegeben $N$, ist praktisch unmöglich.


**Anmerkungen:**

[1] Die Faktorisierung kann auch wichtig sein, um mit anderen Arten mathematischer Objekte als Zahlen zu arbeiten. Zum Beispiel kann es nützlich sein, polynomiale Ausdrücke wie $x^2 - 2x + 1$ zu faktorisieren. In unserer Diskussion werden wir uns jedoch nur auf die Faktorisierung von Zahlen, speziell ganzen Zahlen, konzentrieren.
[2] Gemäß dem **Primzahlsatz** ist die Anzahl der Primzahlen kleiner oder gleich $N$ ungefähr $N/\ln(N)$. Das bedeutet, dass man die Anzahl der Primzahlen der Länge 1024 Bits annähern kann durch:
$$ \frac{2^{1024}}{\ln(2^{1024})} - \frac{2^{1023}}{\ln(2^{1023})} $$

...was ungefähr $1.265 \times 10^{305}$ entspricht.

[3] Das Gleiche gilt für Probleme des diskreten Logarithmus. Daher funktionieren asymmetrische Konstruktionen mit viel größeren Schlüsseln als symmetrische kryptografische Konstruktionen.

## Zahlentheoretische Ergebnisse
<chapterId>23cd2186-8d97-5709-a4a7-b984f1eb9999</chapterId>

Leider kann das Faktorisierungsproblem nicht direkt für asymmetrische kryptografische Schemata verwendet werden. Wir können jedoch ein komplexeres, aber damit zusammenhängendes Problem zu diesem Zweck nutzen: das RSA-Problem.

Um das RSA-Problem zu verstehen, müssen wir eine Reihe von Theoremen und Aussagen aus der Zahlentheorie verstehen. Diese werden in diesem Abschnitt in drei Unterabschnitten präsentiert: (1) die Ordnung von N, (2) die Invertierbarkeit modulo N und (3) der Satz von Euler.

Einige der Materialien in den drei Unterabschnitten wurden bereits in *Kapitel 3* eingeführt. Ich werde hier jedoch das Material zur Bequemlichkeit noch einmal darstellen.

### Die Ordnung von N

Eine ganze Zahl $a$ ist **teilerfremd** oder ein **relativer Prim** zu einer ganzen Zahl $N$, wenn der größte gemeinsame Teiler zwischen ihnen 1 ist. Obwohl 1 konventionell keine Primzahl ist, ist sie ein Teilerfremder jeder ganzen Zahl (wie auch $-1$).

Betrachten Sie zum Beispiel den Fall, wenn $a = 18$ und $N = 37$ ist. Diese sind eindeutig teilerfremd. Die größte Zahl, die sowohl in 18 als auch in 37 aufgeht, ist 1. Im Gegensatz dazu betrachten Sie den Fall, wenn $a = 42$ und $N = 16$ ist. Diese sind eindeutig nicht teilerfremd. Beide Zahlen sind durch 2 teilbar, was größer als 1 ist.

Wir können nun die Ordnung von $N$ wie folgt definieren. Angenommen, $N$ ist eine ganze Zahl größer als 1. Die **Ordnung von N** ist dann die Anzahl aller Teilerfremden mit $N$, so dass für jeden Teilerfremden $a$ die folgende Bedingung gilt: $1 \leq a < N$.

Zum Beispiel, wenn $N = 12$, dann sind 1, 5, 7 und 11 die einzigen Teilerfremden, die die oben genannte Anforderung erfüllen. Daher ist die Ordnung von 12 gleich 4.

Angenommen, $N$ ist eine Primzahl. Dann ist jede ganze Zahl kleiner als $N$, aber größer oder gleich 1, teilerfremd zu ihr. Dies umfasst alle Elemente in der folgenden Menge: $\{1,2,3,….,N - 1\}$. Daher ist, wenn $N$ eine Primzahl ist, die Ordnung von $N$ $N - 1$. Dies wird in Aussage 1 dargestellt, wobei $\phi(N)$ die Ordnung von $N$ bezeichnet.

**Aussage 1**. $\phi(N) = N - 1$, wenn $N$ eine Primzahl ist
Angenommen, $N$ ist keine Primzahl. Dann können Sie dessen Ordnung mit Hilfe der **Eulerschen Phi-Funktion** berechnen. Während die Berechnung der Ordnung einer kleinen Zahl relativ einfach ist, wird die Eulersche Phi-Funktion besonders wichtig für größere Zahlen. Die Aussage der Eulerschen Phi-Funktion ist unten angegeben.

**Theorem 2**. Sei $N = p_1^{e_1} \cdot p_2^{e_2} \cdot \ldots \cdot p_i^{e_i} \cdot \ldots \cdot p_n^{e_n}$, wobei die Menge $\{p_i\}$ aus allen unterschiedlichen Primfaktoren von $N$ besteht und jedes $e_i$ angibt, wie oft der Primfaktor $p_i$ für $N$ vorkommt. Dann gilt

$$\phi(N) = p_1^{e_1 - 1} \cdot (p_1 - 1) \cdot p_2^{e_2 - 1} \cdot (p_2 - 1) \cdot \ldots \cdot p_n^{e_n - 1} \cdot (p_n - 1)$$

**Theorem 2** zeigt, dass es einfach ist, die Ordnung von $N$ zu berechnen, sobald Sie ein nicht-primäres $N$ in seine unterschiedlichen Primfaktoren zerlegt haben.

Nehmen wir zum Beispiel an, dass $N = 270$. Dies ist offensichtlich keine Primzahl. Die Zerlegung von $N$ in seine Primfaktoren ergibt den Ausdruck: $2 \cdot 3^3 \cdot 5$. Gemäß der Eulerschen Phi-Funktion ist die Ordnung von $N$ dann wie folgt:

$$\phi(N) = 2^{1 - 1} \cdot (2 - 1) + 3^{3 - 1} \cdot (3 - 1) + 5^{1 - 1} \cdot (5 - 1) = 1 \cdot 1 + 9 \cdot 2 + 1 \cdot 4 = 1 + 18 + 4 = 23$$

Nehmen wir als Nächstes an, dass $N$ ein Produkt von zwei Primzahlen, $p$ und $q$, ist. **Theorem 2** oben besagt dann, dass die Ordnung von $N$ wie folgt ist:

$$p^{1 - 1} \cdot (p - 1) \cdot q^{1 - 1} \cdot (q - 1) = (p - 1) \cdot (q - 1)$$

Dies ist ein Schlüsselergebnis insbesondere für das RSA-Problem und wird in **Proposition 2** unten angegeben.

**Proposition 2**. Wenn $N$ das Produkt von zwei Primzahlen, $p$ und $q$, ist, dann ist die Ordnung von $N$ das Produkt $(p - 1) \cdot (q - 1)$.

Um zu veranschaulichen, nehmen wir an, dass $N = 119$. Diese Zahl kann in zwei Primzahlen zerlegt werden, nämlich 7 und 17. Daher legt die Eulersche Phi-Funktion nahe, dass die Ordnung von 119 wie folgt ist:

$$\phi(119) = (7 - 1) \cdot (17 - 1) = 6 \cdot 16 = 96$$

Mit anderen Worten, die Zahl 119 hat 96 teilerfremde Zahlen im Bereich von 1 bis 119. Tatsächlich umfasst diese Menge alle Zahlen von 1 bis 119, die keine Vielfachen von entweder 7 oder 17 sind.
Von hier an bezeichnen wir die Menge der teilerfremden Zahlen, die die Ordnung von $N$ bestimmen, als $C_N$. Für unser Beispiel, bei dem $N = 119$ ist, ist die Menge $C_{119}$ viel zu groß, um sie vollständig aufzulisten. Aber einige der Elemente sind wie folgt:
$$C_{119} = \{1, 2, \dots 6, 8 \dots 13, 15, 16, 18, \dots 33, 35 \dots 96\}$$

### Invertierbarkeit modulo N

Wir können sagen, dass eine ganze Zahl $a$ **invertierbar modulo N** ist, wenn es mindestens eine ganze Zahl $b$ gibt, so dass $a \cdot b \mod N = 1 \mod N$. Jede solche ganze Zahl $b$ wird als ein **Inverses** (oder **multiplikatives Inverses**) von $a$ bezeichnet, gegeben durch Reduktion modulo $N$.

Nehmen wir zum Beispiel an, dass $a = 5$ und $N = 11$ ist. Es gibt viele ganze Zahlen, mit denen man 5 multiplizieren kann, so dass $5 \cdot b \mod 11 = 1 \mod 11$. Betrachten Sie zum Beispiel die ganzen Zahlen 20 und 31. Es ist leicht zu sehen, dass beide diese Zahlen Inverse von 5 bei der Reduktion modulo 11 sind.

* $5 \cdot 20 \mod 11 = 100 \mod 11 = 1 \mod 11$
* $5 \cdot 31 \mod 11 = 155 \mod 11 = 1 \mod 11$

Obwohl 5 viele Inverse bei der Reduktion modulo 11 hat, kann man zeigen, dass nur ein einziges positives Inverses von 5 existiert, das kleiner als 11 ist. Tatsächlich ist dies nicht einzigartig für unser spezielles Beispiel, sondern ein allgemeines Ergebnis.

**Proposition 3**. Wenn die ganze Zahl $a$ invertierbar modulo $N$ ist, muss es der Fall sein, dass genau ein positives Inverses von $a$ kleiner als $N$ ist. (Also muss dieses einzigartige Inverse von $a$ aus der Menge $\{1, \dots, N - 1\}$ stammen).

Bezeichnen wir das einzigartige Inverse von $a$ aus **Proposition 3** als $a^{-1}$. Für den Fall, dass $a = 5$ und $N = 11$ ist, können Sie sehen, dass $a^{-1} = 9$ ist, gegeben dass $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$.

Beachten Sie, dass Sie den Wert 9 für $a^{-1}$ in unserem Beispiel auch einfach erhalten können, indem Sie jedes andere Inverse von $a$ modulo 11 reduzieren. Zum Beispiel $20 \mod 11 = 31 \mod 11 = 9 \mod 11$. Also, wann immer eine ganze Zahl $a > N$ invertierbar modulo $N$ ist, dann muss $a \mod N$ auch invertierbar modulo $N$ sein.

Es ist nicht notwendigerweise der Fall, dass ein Inverses von $a$ bei der Reduktion modulo $N$ existiert. Nehmen wir zum Beispiel an, dass $a = 2$ und $N = 8$ ist. Es gibt kein $b$, oder speziell kein $a^{-1}$, so dass $2 \cdot b \mod 8 = 1 \mod 8$. Dies liegt daran, dass jeder Wert von $b$ immer ein Vielfaches von 2 produzieren wird, so dass keine Division durch 8 jemals einen Rest ergeben kann, der 1 entspricht.
Wie genau wissen wir, ob eine ganze Zahl $a$ ein Inverses bezüglich einer gegebenen Zahl $N$ hat? Wie Sie vielleicht im obigen Beispiel bemerkt haben, ist der größte gemeinsame Teiler (ggT) zwischen 2 und 8 größer als 1, nämlich 2. Und dies veranschaulicht tatsächlich das folgende allgemeine Ergebnis:
**Proposition 4**. Ein Inverses einer ganzen Zahl $a$ bezüglich der Reduktion modulo $N$ existiert, und speziell ein eindeutiges positives Inverses kleiner als $N$, wenn und nur wenn der größte gemeinsame Teiler zwischen $a$ und $N$ 1 ist (das heißt, wenn sie teilerfremd sind).

Für den Fall, dass $a = 5$ und $N = 11$ ist, kamen wir zu dem Schluss, dass $a^{-1} = 9$, da $5 \cdot 9 \mod 11 = 45 \mod 11 = 1 \mod 11$. Es ist wichtig zu beachten, dass das Umgekehrte auch wahr ist. Das heißt, wenn $a = 9$ und $N = 11$ ist, gilt, dass $a^{-1} = 5$.

### Eulers Theorem

Bevor wir zum RSA-Problem übergehen, müssen wir ein weiteres entscheidendes Theorem verstehen, nämlich **Eulers Theorem**. Es besagt Folgendes:

**Theorem 3**. Angenommen, zwei ganze Zahlen $a$ und $N$ sind teilerfremd. Dann gilt $a^{\phi(N)} \mod N = 1 \mod N$.

Dies ist ein bemerkenswertes Ergebnis, aber zunächst ein wenig verwirrend. Lassen Sie uns ein Beispiel betrachten, um es zu verstehen.

Nehmen wir an, dass $a = 5$ und $N = 7$ ist. Diese sind in der Tat teilerfremd, wie es Eulers Theorem erfordert. Wir wissen, dass die Ordnung von 7 gleich 6 ist, da 7 eine Primzahl ist (siehe **Proposition 1**).

Was Eulers Theorem nun besagt, ist, dass $5^6 \mod 7$ gleich $1 \mod 7$ sein muss. Unten sind die Berechnungen, die zeigen, dass dies tatsächlich wahr ist.

* $5^6 \mod 7 = 15.625 \mod 7 = 1 \mod N$

Die ganze Zahl 7 teilt 15.624 insgesamt 2.233 Mal. Daher ist der Rest der Division von 16.625 durch 7 gleich 1.

Als Nächstes können Sie mit Eulers Phi-Funktion, **Theorem 2**, die **Proposition 5** unten ableiten.

**Proposition 5**. $\phi(a \cdot b) = \phi(a) \cdot \phi(b)$ für beliebige positive ganze Zahlen $a$ und $b$.

Wir werden nicht zeigen, warum dies der Fall ist. Aber beachten Sie lediglich, dass Sie bereits Beweise für diese Proposition gesehen haben, durch die Tatsache, dass $\phi(p \cdot q) = \phi(p) \cdot \phi(q) = (p - 1) \cdot (q - 1)$, wenn $p$ und $q$ Primzahlen sind, wie in **Proposition 2** angegeben.

Eulers Theorem in Verbindung mit **Proposition 5** hat wichtige Implikationen. Sehen Sie, was beispielsweise in den untenstehenden Ausdrücken passiert, wo $a$ und $N$ teilerfremd sind.

* $a^{2 \cdot \phi(N)} \mod N = a^{\phi(N)} \cdot a^{\phi(N)} \mod N = 1 \cdot 1 \mod N = 1 \mod N$
* $a^{\phi(N) + 1} \mod N = a^{\phi(N)} \cdot a^1 \mod N = 1 \cdot a^1 \mod N = a \mod N$* $a^{8 \cdot \phi(N) + 3} \mod N = a^{8 \cdot \phi(N)} \cdot a^3 \mod N = 1 \cdot a^3 \mod N = a^3 \mod N$

Daher erlaubt uns die Kombination des Satzes von Euler und **Proposition 5**, eine Reihe von Ausdrücken einfach zu berechnen. Allgemein können wir die Einsicht wie in **Proposition 6** zusammenfassen.

**Proposition 6**. $a^x \mod N = a^{x \mod \phi(N)}$

Nun müssen wir alles in einem kniffligen letzten Schritt zusammenführen.

So wie $N$ eine Ordnung $\phi(N)$ hat, die die Elemente der Menge $C_N$ einschließt, wissen wir, dass die ganze Zahl $\phi(N)$ wiederum auch eine Ordnung und eine Menge von teilerfremden Zahlen haben muss. Setzen wir $\phi(N) = R$. Dann wissen wir, dass es auch einen Wert für $\phi(R)$ und eine Menge von teilerfremden Zahlen $C_R$ gibt.

Nehmen wir an, dass wir nun eine ganze Zahl $e$ aus der Menge $C_R$ auswählen. Wir wissen aus **Proposition 3**, dass diese ganze Zahl $e$ nur ein einziges positives Inverses kleiner als $R$ hat. Das heißt, $e$ hat ein einziges Inverses aus der Menge $C_R$. Nennen wir dieses Inverse $d$. Angesichts der Definition eines Inversen bedeutet dies, dass $e \cdot d = 1 \mod R$.

Wir können dieses Ergebnis nutzen, um eine Aussage über unsere ursprüngliche ganze Zahl $N$ zu machen. Dies wird in **Proposition 7** zusammengefasst.

**Proposition 7**. Angenommen, $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Dann muss für jedes Element $a$ der Menge $C_N$ gelten, dass $a^{e \cdot d \mod \phi(N)} = a^{1 \mod \phi(N)} = a \mod N$.

Nun haben wir alle zahlentheoretischen Ergebnisse, die benötigt werden, um das RSA-Problem klar zu formulieren.


## Das RSA-Kryptosystem
<chapterId>0253c2f7-b8a4-5d0e-bd60-812ed6b6c7a9</chapterId>

Wir sind nun bereit, das RSA-Problem zu formulieren. Nehmen Sie an, Sie erstellen eine Menge von Variablen, bestehend aus $p$, $q$, $N$, $\phi(N)$, $e$, $d$ und $y$. Nennen Sie diese Menge $\Pi$. Sie wird wie folgt erstellt:

1. Generieren Sie zwei zufällige Primzahlen $p$ und $q$ gleicher Größe und berechnen Sie ihr Produkt $N$.
2. Berechnen Sie die Ordnung von $N$, $\phi(N)$, durch das folgende Produkt: $(p - 1) \cdot (q - 1)$.
3. Wählen Sie ein $e > 2$, das kleiner und teilerfremd zu $\phi(N)$ ist.
4. Berechnen Sie $d$, indem Sie $e \cdot d \mod \phi(N) = 1$ setzen.
5. Wählen Sie einen zufälligen Wert $y$, der kleiner und teilerfremd zu $N$ ist.
Das RSA-Problem besteht darin, ein $x$ zu finden, so dass $x^e = y$, während nur ein Teil der Informationen bezüglich $\Pi$ gegeben ist, nämlich die Variablen $N$, $e$ und $y$. Wenn $p$ und $q$ sehr groß sind, typischerweise wird empfohlen, dass sie 1024 Bits groß sind, gilt das RSA-Problem als schwierig. Jetzt kann man sehen, warum das der Fall ist, angesichts der vorangegangenen Diskussion.

Eine einfache Methode, um $x$ zu berechnen, wenn $x^e \mod N = y \mod N$ ist, besteht einfach darin, $y^d \mod N$ zu berechnen. Wir wissen, dass $y^d \mod N = x \mod N$ durch die folgenden Berechnungen ist:

$$ y^d \mod N = x^{e \cdot d} \mod N = x^{e \cdot d \mod \phi(N)} \mod N = x^{1 \mod \phi(N)} \mod N = x \mod N. $$

Das Problem ist, dass wir den Wert $d$ nicht kennen, da er im Problem nicht gegeben ist. Daher können wir $y^d \mod N$ nicht direkt berechnen, um $x \mod N$ zu produzieren.

Wir könnten jedoch in der Lage sein, $d$ indirekt aus der Ordnung von $N$, $\phi(N)$, zu berechnen, da wir wissen, dass $e \cdot d \mod \phi(N) = 1 \mod \phi(N)$. Aber nach Annahme gibt das Problem auch keinen Wert für $\phi(N)$ an.

Schließlich könnte die Ordnung indirekt mit den Primfaktoren $p$ und $q$ berechnet werden, so dass wir schließlich $d$ berechnen können. Aber nach Annahme wurden uns auch die Werte $p$ und $q$ nicht gegeben.

Streng genommen, selbst wenn das Faktorisierungsproblem innerhalb eines RSA-Problems schwierig ist, können wir nicht beweisen, dass das RSA-Problem ebenfalls schwierig ist. Es könnte nämlich andere Wege geben, das RSA-Problem zu lösen, als durch Faktorisierung. Es wird jedoch allgemein akzeptiert und angenommen, dass, wenn das Faktorisierungsproblem innerhalb des RSA-Problems schwierig ist, das RSA-Problem selbst ebenfalls schwierig ist.

Wenn das RSA-Problem tatsächlich schwierig ist, dann erzeugt es eine Einwegfunktion mit einer Falltür. Die Funktion hier ist $f(g) = g^e \mod N$. Mit Kenntnis von $f(g)$ könnte jeder leicht einen Wert $y$ für ein bestimmtes $g = x$ berechnen. Es ist jedoch praktisch unmöglich, einen bestimmten Wert $x$ nur aus der Kenntnis des Wertes $y$ und der Funktion $f(g)$ zu berechnen. Die Ausnahme ist, wenn man ein Stück Information $d$, die Falltür, gegeben bekommt. In diesem Fall kann man einfach $y^d$ berechnen, um $x$ zu geben.

Lassen Sie uns anhand eines spezifischen Beispiels das RSA-Problem veranschaulichen. Ich kann kein RSA-Problem auswählen, das unter den oben genannten Bedingungen als schwierig angesehen würde, da die Zahlen unhandlich wären. Stattdessen soll dieses Beispiel nur veranschaulichen, wie das RSA-Problem im Allgemeinen funktioniert.

Um zu beginnen, nehmen wir an, Sie wählen zwei zufällige Primzahlen 13 und 31. Also $p = 13$ und $q = 31$. Das Produkt $N$ dieser beiden Primzahlen ergibt 403. Wir können leicht die Ordnung von 403 berechnen. Sie entspricht $(13 - 1) \cdot (31 - 1) = 360$.
Als nächstes, wie in Schritt 3 des RSA-Problems vorgegeben, müssen wir einen Teilerfremden für 360 auswählen, der größer als 2 und kleiner als 360 ist. Wir müssen diesen Wert nicht zufällig auswählen. Nehmen wir an, wir wählen 103. Dies ist ein teilerfremder Wert zu 360, da sein größter gemeinsamer Teiler mit 103 gleich 1 ist.
Schritt 4 erfordert nun, dass wir einen Wert $d$ berechnen, so dass $103 \cdot d \mod 360 = 1$. Dies ist keine leichte Aufgabe von Hand, wenn der Wert für $N$ groß ist. Es erfordert, dass wir ein Verfahren namens **erweiterter Euklidischer Algorithmus** verwenden.

Obwohl ich das Verfahren hier nicht zeige, ergibt es den Wert 7, wenn $e = 103$. Sie können überprüfen, dass das Wertepaar 103 und 7 tatsächlich die allgemeine Bedingung $e \cdot d \mod \phi(n) = 1$ durch die untenstehenden Berechnungen erfüllt.

* $103 \cdot 7 \mod 360 = 721 \mod 360 = 1 \mod 360$

Wichtig ist, dass wir aufgrund von *Proposition 4* wissen, dass kein anderer ganzer Wert zwischen 1 und 360 für $d$ das Ergebnis erzeugen wird, dass $103 \cdot d = 1 \mod 360$. Zusätzlich impliziert die Proposition, dass die Auswahl eines anderen Wertes für $e$ einen anderen einzigartigen Wert für $d$ ergibt.

In Schritt 5 des RSA-Problems müssen wir eine positive ganze Zahl $y$ auswählen, die ein kleinerer Teilerfremder von 403 ist. Nehmen wir an, wir setzen $y = 2^{103}$. Die Exponentiation von 2 mit 103 ergibt das folgende Ergebnis.

* $2^{103} \mod 403 = 10.141.204.801.825.835.211.973.625.643.008 \mod 403 = 349 \mod 403$

Das RSA-Problem in diesem speziellen Beispiel ist nun wie folgt: Ihnen wird $N = 403$, $e = 103$ und $y = 349 \mod 403$ gegeben. Sie müssen nun $x$ berechnen, so dass $x^{103} = 349 \mod 403$. Das heißt, Sie müssen herausfinden, dass der ursprüngliche Wert vor der Exponentiation durch 103 gleich 2 war.

Es wäre einfach (zumindest für einen Computer), $x$ zu berechnen, wenn wir wüssten, dass $d = 7$. In diesem Fall könnten Sie einfach $x$ wie folgt bestimmen.

* $x = y^7 \mod 403 = 349^7 \mod 403 = 630.634.881.591.804.949 \mod 403 = 2 \mod 403$

Das Problem ist, dass Ihnen die Information, dass $d = 7$ ist, nicht gegeben wurde. Natürlich könnten Sie $d$ aus der Tatsache berechnen, dass $103 \cdot d = 1 \mod 360$. Das Problem ist, dass Ihnen auch nicht die Information gegeben wurde, dass die Ordnung von $N = 360$ ist. Schließlich könnten Sie auch die Ordnung von 403 berechnen, indem Sie das folgende Produkt berechnen: $(p - 1) \cdot (q - 1)$. Aber auch hier wurde Ihnen nicht gesagt, dass $p = 13$ und $q = 31$ ist.

Natürlich könnte ein Computer das RSA-Problem für dieses Beispiel relativ leicht lösen, da die beteiligten Primzahlen nicht groß sind. Aber wenn die Primzahlen sehr groß werden, steht er vor einer praktisch unmöglichen Aufgabe.
Wir haben nun das RSA-Problem vorgestellt, eine Reihe von Bedingungen, unter denen es schwierig ist, und die zugrundeliegende Mathematik. Wie hilft uns all das bei der asymmetrischen Kryptografie? Speziell, wie können wir die Schwierigkeit des RSA-Problems unter bestimmten Bedingungen in ein Verschlüsselungsschema oder ein digitales Signaturschema umwandeln?
Ein Ansatz besteht darin, das RSA-Problem zu nehmen und Schemata auf eine direkte Weise zu erstellen. Nehmen wir zum Beispiel an, dass Sie eine Reihe von Variablen $\Pi$ wie im RSA-Problem beschrieben generiert haben und sicherstellen, dass $p$ und $q$ ausreichend groß sind. Sie setzen Ihren öffentlichen Schlüssel gleich $(N, e)$ und teilen diese Information mit der Welt. Wie oben beschrieben, halten Sie die Werte für $p$, $q$, $\phi(n)$ und $d$ geheim. Tatsächlich ist $d$ Ihr privater Schlüssel.

Jeder, der Ihnen eine Nachricht $m$ senden möchte, die ein Element von $C_N$ ist, könnte sie einfach wie folgt verschlüsseln: $c = m^e \mod N$. (Der Chiffretext $c$ hier entspricht dem Wert $y$ im RSA-Problem.) Sie können diese Nachricht leicht entschlüsseln, indem Sie einfach $c^d \mod N$ berechnen.

Sie könnten versuchen, auf die gleiche Weise ein digitales Signaturschema zu erstellen. Nehmen wir an, Sie möchten jemandem eine Nachricht $m$ mit einer digitalen Signatur $S$ senden. Sie könnten einfach $S = m^d \mod N$ setzen und das Paar $(m,S)$ an den Empfänger senden. Jeder kann die digitale Signatur einfach überprüfen, indem er prüft, ob $S^e \mod N = m \mod N$ ist. Ein Angreifer hätte jedoch große Schwierigkeiten, ein gültiges $S$ für eine Nachricht zu erstellen, da er $d$ nicht besitzt.

Leider ist es nicht so einfach, das an sich schwierige RSA-Problem in ein kryptografisches Schema umzuwandeln. Bei dem direkten Verschlüsselungsschema können Sie nur teilerfremde Zahlen von $N$ als Ihre Nachrichten auswählen. Das lässt uns nicht viele mögliche Nachrichten, sicherlich nicht genug für eine Standardkommunikation. Außerdem müssen diese Nachrichten zufällig ausgewählt werden. Das scheint etwas unpraktisch. Schließlich wird jede Nachricht, die zweimal ausgewählt wird, genau denselben Chiffretext ergeben. Das ist in jedem Verschlüsselungsschema äußerst unerwünscht und erfüllt keinen rigorosen modernen Sicherheitsstandard bei der Verschlüsselung.

Die Probleme werden noch schlimmer bei unserem direkten digitalen Signaturschema. Wie es derzeit steht, kann jeder Angreifer leicht digitale Signaturen fälschen, indem er zuerst eine teilerfremde Zahl von $N$ als Signatur auswählt und dann die entsprechende ursprüngliche Nachricht berechnet. Dies bricht eindeutig die Anforderung der existenziellen Unfälschbarkeit.

Dennoch kann mit dem Hinzufügen eines bisschen cleverer Komplexität das RSA-Problem verwendet werden, um ein sicheres öffentliches Schlüsselverschlüsselungsschema sowie ein sicheres digitales Signaturschema zu erstellen. Wir werden hier nicht auf die Details solcher Konstruktionen eingehen. [4] Wichtig ist jedoch, dass diese zusätzliche Komplexität das grundlegende zugrundeliegende RSA-Problem, auf dem diese Schemata basieren, nicht ändert.

**Anmerkungen:**

[4] Siehe zum Beispiel Jonathan Katz und Yehuda Lindell, _Einführung in die moderne Kryptografie_, CRC Press (Boca Raton, FL: 2015), S. 410–32 über RSA-Verschlüsselung und S. 444–41 für RSA-digitale Signaturen.

## Kurs bewerten
<chapterId>f1905f78-8cf7-5031-949a-dfa8b76079b4</chapterId>
<isCourseReview>true</isCourseReview>