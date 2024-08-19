---
name: Einführung in die formale Kryptographie
goal: Eine tiefgehende Einführung in die Wissenschaft und Praxis der Kryptographie.
objectives:
  - Erforschung von Beale-Chiffren und modernen kryptografischen Methoden, um grundlegende und historische Konzepte der Kryptographie zu verstehen.
  - Vertiefung in Zahlentheorie, Gruppen und Felder, um die Schlüsselmathematischen Konzepte, die der Kryptographie zugrunde liegen, zu meistern.
  - Studium des RC4-Stream-Ciphers und AES mit einem 128-Bit-Schlüssel, um symmetrische kryptografische Algorithmen kennenzulernen.
  - Untersuchung des RSA-Kryptosystems, Schlüsselverteilung und Hash-Funktionen, um asymmetrische Kryptographie zu erkunden.

---
# Tiefgehender Einblick in die Kryptographie

Es ist schwierig, viele Materialien zu finden, die einen guten Mittelweg in der Kryptographieausbildung bieten.

Einerseits gibt es langwierige, formale Abhandlungen, die wirklich nur für diejenigen zugänglich sind, die eine starke Grundlage in Mathematik, Logik oder einer anderen formalen Disziplin haben. Andererseits gibt es sehr allgemeine Einführungen, die wirklich zu viele Details für jeden verbergen, der zumindest ein wenig neugierig ist.

Diese Einführung in die Kryptographie sucht den Mittelweg zu erfassen. Obwohl sie für jeden, der neu in der Kryptographie ist, relativ herausfordernd und detailliert sein sollte, ist es nicht das Kaninchenloch einer typischen grundlegenden Abhandlung.

+++

# Eine Einführung in die Kryptographie
<partId>bbed2f46-d64c-5fb5-b892-d726032f2494</partId>

## Kurzbeschreibung
<chapterId>bb8a8b73-7fb2-50da-bf4e-98996d79887b</chapterId>

Dieses Buch bietet eine tiefgehende Einführung in die Wissenschaft und Praxis der Kryptographie. Wo möglich, konzentriert es sich auf konzeptionelle, anstatt formale Darstellung des Materials.

> Dieser Kurs basiert auf [JWBurgers's Repo](https://github.com/JWBurgers/An_Introduction_to_Cryptography). Alle Rechte bei ihm. Der Inhalt ist noch nicht fertig und dient nur dazu zu zeigen, wie wir es integrieren könnten, wenn JWburger zustimmt.

### Motivation und Ziele

Es ist schwierig, viele Materialien zu finden, die einen guten Mittelweg in der Kryptographieausbildung bieten.

Einerseits gibt es langwierige, formale Abhandlungen, die wirklich nur für diejenigen zugänglich sind, die eine starke Grundlage in Mathematik, Logik oder einer anderen formalen Disziplin haben. Andererseits gibt es sehr allgemeine Einführungen, die wirklich zu viele Details für jeden verbergen, der zumindest ein wenig neugierig ist.

Diese Einführung in die Kryptographie sucht den Mittelweg zu erfassen. Obwohl sie für jeden, der neu in der Kryptographie ist, relativ herausfordernd und detailliert sein sollte, ist es nicht das Kaninchenloch einer typischen grundlegenden Abhandlung.


### Zielgruppe

Von Entwicklern bis zu intellektuell Neugierigen ist dieses Buch nützlich für jeden, der mehr als ein oberflächliches Verständnis der Kryptographie wünscht. Wenn Ihr Ziel ist, das Feld der Kryptographie zu meistern, dann ist dieses Buch auch ein guter Ausgangspunkt.


### Leseanleitungen

Das Buch enthält derzeit sieben Kapitel: "Was ist Kryptographie?" (Kapitel 1), "Mathematische Grundlagen der Kryptographie I" (Kapitel 2), "Mathematische Grundlagen der Kryptographie II" (Kapitel 3), "Symmetrische Kryptographie" (Kapitel 4), "RC4 und AES" (Kapitel 5), "Asymmetrische Kryptographie" (Kapitel 6) und "Das RSA-Kryptosystem" (Kapitel 7). Ein abschließendes Kapitel, "Kryptographie in der Praxis", wird noch hinzugefügt. Es konzentriert sich auf verschiedene kryptografische Anwendungen, einschließlich Transportschichtsicherheit, Onion-Routing und dem Wertaustauschsystem von Bitcoin.
Sofern Sie nicht über fundierte Kenntnisse in Mathematik verfügen, ist die Zahlentheorie wahrscheinlich das schwierigste Thema in diesem Buch. Ich biete einen Überblick darüber in Kapitel 3, und sie erscheint auch in der Darstellung von AES in Kapitel 5 und dem RSA-Kryptosystem in Kapitel 7.
Wenn Sie wirklich mit den formalen Details in diesen Teilen des Buches zu kämpfen haben, empfehle ich Ihnen, sich beim ersten Mal auf eine hochrangige Lektüre zu beschränken.

### Danksagungen

Das einflussreichste Buch bei der Gestaltung dieses Werkes war Jonathan Katz und Yehuda Lindells _Einführung in die moderne Kryptographie_, CRC Press (Boca Raton, FL), 2015. Ein begleitender Kurs ist auf Coursera unter dem Titel "Kryptographie" verfügbar.

Die wichtigsten zusätzlichen Quellen, die bei der Erstellung des Überblicks in diesem Buch hilfreich waren, sind Simon Singh, _Das Geheimnis der Codes_, Fourth Estate (London, 1999); Christof Paar und Jan Pelzl, _Verständnis der Kryptographie_, Springer (Heidelberg, 2010) und ein auf dem Buch von Paar basierender Kurs mit dem Titel „Einführung in die Kryptographie“ (verfügbar unter https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg); und Bruce Schneier, Angewandte Kryptographie, 2. Aufl., 2015 (Indianapolis, IN: John Wiley & Sons).

Ich werde nur sehr spezifische Informationen und Ergebnisse aus diesen Quellen zitieren, möchte aber hier meine allgemeine Dankbarkeit ihnen gegenüber zum Ausdruck bringen.

Für diejenigen Leser, die nach dieser Einführung tiefergehendes Wissen über Kryptographie suchen, empfehle ich dringend das Buch von Katz und Lindell. Katzs Kurs auf Coursera ist etwas zugänglicher als das Buch.

### Beiträge

Bitte werfen Sie einen Blick auf die Beitragsdatei im Repository für einige Richtlinien, wie Sie das Projekt unterstützen können.

# Was ist Kryptographie?
<partId>48e4d6d5-cd00-5c00-8adb-ae8477ff47c4</partId>

Beginnen wir unsere Untersuchung des Feldes der Kryptographie mit einer der charmantesten und unterhaltsamsten Episoden in ihrer Geschichte: der der Beale-Chiffren.<sup>[1](#footnote1)</sup>

Die Geschichte der Beale-Chiffren ist meiner Meinung nach eher Fiktion als Realität. Aber sie soll sich folgendermaßen zugetragen haben.

## Die Beale-Chiffren
<chapterId>ae674346-4789-5ab1-9b6f-c8989d83be89</chapterId>

Sowohl im Winter 1820 als auch 1822 übernachtete ein Mann namens Thomas J. Beale in einer Herberge, die Robert Morriss in Lynchburg (Virginia) gehörte. Am Ende von Beales zweitem Aufenthalt übergab er Morriss eine eiserne Kiste mit wertvollen Papieren zur Aufbewahrung.

Einige Monate später erhielt Morriss einen Brief von Beale, datiert auf den 9. Mai 1822. Darin betonte er den großen Wert des Inhalts der eisernen Kiste und teilte Morriss einige Anweisungen mit: Falls weder Beale noch einer seiner Gefährten jemals kämen, um die Kiste zu beanspruchen, sollte er sie genau zehn Jahre nach dem Datum des Briefes (also am 9. Mai 1832) öffnen. Einige der Papiere im Inneren würden in regulärem Text geschrieben sein. Mehrere andere jedoch wären „ohne die Hilfe eines Schlüssels unverständlich“. Dieser „Schlüssel“ würde dann im Juni 1832 von einem nicht genannten Freund Beales an Morriss übergeben werden.
Trotz der klaren Anweisungen öffnete Morriss die Kiste im Mai 1832 nicht, und der geheimnisvolle Freund von Beale erschien auch im Juni jenes Jahres nicht. Erst 1845 entschied sich der Gastwirt schließlich dazu, die Kiste zu öffnen. Darin fand Morriss einen Zettel, der erklärte, wie Beale und seine Gefährten im Westen Gold und Silber entdeckten und es zusammen mit einigen Schmuckstücken zur sicheren Aufbewahrung vergruben. Zusätzlich enthielt die Kiste drei **Geheimtexte**: das heißt, in Code geschriebene Texte, die einen **kryptografischen Schlüssel** oder ein Geheimnis und einen begleitenden Algorithmus zur Entschlüsselung benötigen. Dieser Prozess des Entriegelns eines Geheimtextes ist als **Entschlüsselung** bekannt, während der Verriegelungsprozess als **Verschlüsselung** bekannt ist. (Wie in Kapitel 3 erklärt, kann der Begriff Chiffre verschiedene Bedeutungen annehmen. Im Namen "Beale-Chiffren" steht er kurz für Geheimtexte.)
Die drei Geheimtexte, die Morriss in der eisernen Kiste fand, bestehen jeweils aus einer Reihe von durch Kommas getrennten Zahlen. Laut Beales Notiz geben diese Geheimtexte separat den Standort des Schatzes, den Inhalt des Schatzes und eine Liste von Namen mit rechtmäßigen Erben des Schatzes und ihren Anteilen an (die letztere Information ist relevant, falls Beale und seine Gefährten die Kiste nie beanspruchen würden).

Morris versuchte zwanzig Jahre lang, die drei Geheimtexte zu entschlüsseln. Dies wäre mit dem Schlüssel einfach gewesen. Aber Morriss hatte den Schlüssel nicht und war erfolglos in seinen Versuchen, die Originaltexte oder **Klartexte**, wie sie in der Kryptografie typischerweise genannt werden, wiederherzustellen.

Gegen Ende seines Lebens übergab Morriss die Kiste 1862 an einen Freund. Dieser Freund veröffentlichte anschließend 1885 unter dem Pseudonym J.B. Ward ein Pamphlet. Es enthielt eine Beschreibung der (angeblichen) Geschichte der Kiste, die drei Geheimtexte und eine Lösung, die er für den zweiten Geheimtext gefunden hatte. (Anscheinend gibt es einen Schlüssel für jeden Geheimtext und nicht einen Schlüssel, der auf alle drei Geheimtexte funktioniert, wie Beale ursprünglich in seinem Brief an Morriss zu suggerieren schien.)

Sie können den zweiten Geheimtext in *Abbildung 2* unten sehen.<sup>[2](#footnote2)</sup> Der Schlüssel zu diesem Geheimtext ist die Unabhängigkeitserklärung der Vereinigten Staaten. Das Entschlüsselungsverfahren kommt auf die Anwendung der folgenden zwei Regeln herunter:

* Für jede Zahl n im Geheimtext, finde das n-te Wort in der Unabhängigkeitserklärung der Vereinigten Staaten
* Ersetze die Zahl n mit dem ersten Buchstaben des gefundenen Wortes

*Abbildung 1: Beale-Chiffre Nr. 2*

![Abbildung 1: Beale-Chiffre Nr. 2](assets/Figure1-1.webp "Abbildung 1: Beale-Chiffre Nr. 2")

Zum Beispiel ist die erste Zahl des zweiten Geheimtextes 115. Das 115. Wort der Unabhängigkeitserklärung ist „instituted“, also ist der erste Buchstabe des Klartextes „i“. Der Geheimtext gibt Wortabstände und Großschreibung nicht direkt an. Aber nachdem die ersten paar Wörter entschlüsselt wurden, kann man logisch ableiten, dass das erste Wort des Klartextes einfach „I“ war. (Der Klartext beginnt mit der Phrase „I have deposited in the county of Bedford.“)
Nach der Entschlüsselung liefert die zweite Nachricht detaillierte Inhalte über den Schatz (Gold, Silber und Juwelen) und deutet darauf hin, dass er in eisernen Töpfen begraben und mit Steinen in Bedford County (Virginia) bedeckt wurde. Menschen lieben ein gutes Geheimnis, daher wurden große Anstrengungen unternommen, um die anderen beiden Beale-Chiffren zu entschlüsseln, insbesondere die, die den Standort des Schatzes beschreibt. Selbst verschiedene prominente Kryptographen haben sich daran versucht. Bisher konnte jedoch niemand die anderen beiden Chiffretexte entschlüsseln.

## Moderne Kryptographie
<chapterId>d07d576f-8a4b-5890-b182-2e5763f550f4</chapterId>

Bunte Geschichten wie die der Beale-Chiffren sind das, was die meisten von uns mit Kryptographie verbinden. Doch die moderne Kryptographie unterscheidet sich in mindestens vier wichtigen Punkten von diesen Arten historischer Beispiele.

Erstens war die Kryptographie historisch gesehen nur mit **Geheimhaltung** (oder Vertraulichkeit) beschäftigt. Chiffretexte wurden erstellt, um sicherzustellen, dass nur bestimmte Parteien Zugang zu den Informationen in den Klartexten hatten, wie im Fall der Beale-Chiffren. Damit ein Verschlüsselungsschema diesen Zweck gut erfüllt, sollte die Entschlüsselung des Chiffretexts nur möglich sein, wenn man den Schlüssel hat.

Die moderne Kryptographie beschäftigt sich mit einem breiteren Spektrum an Themen als nur Geheimhaltung. Diese Themen umfassen hauptsächlich (1) **Nachrichtenintegrität** – das heißt, die Sicherstellung, dass eine Nachricht nicht verändert wurde; (2) **Nachrichtenauthentizität** – das heißt, die Sicherstellung, dass eine Nachricht wirklich von einem bestimmten Absender stammt; und (3) **Nichtabstreitbarkeit** – das heißt, die Sicherstellung, dass ein Absender später nicht fälschlicherweise leugnen kann, dass er eine Nachricht gesendet hat.

Ein wichtiger Unterschied, den man im Kopf behalten sollte, ist also zwischen einem **Verschlüsselungsschema** und einem **kryptographischen Schema**. Ein Verschlüsselungsschema beschäftigt sich nur mit Geheimhaltung. Während ein Verschlüsselungsschema ein kryptographisches Schema ist, ist das Umgekehrte nicht wahr. Ein kryptographisches Schema kann auch den anderen Hauptthemen der Kryptographie dienen, einschließlich Integrität, Authentizität und Nichtabstreitbarkeit.

Die Themen Integrität und Authentizität sind genauso wichtig wie Geheimhaltung. Unsere modernen Kommunikationssysteme könnten ohne Garantien bezüglich der Integrität und Authentizität von Kommunikationen nicht funktionieren. Nichtabstreitbarkeit ist ebenfalls ein wichtiges Anliegen, wie bei digitalen Verträgen, aber in kryptographischen Anwendungen weniger allgegenwärtig benötigt als Geheimhaltung, Integrität und Authentizität.

Zweitens involvieren klassische Verschlüsselungsschemata wie die Beale-Chiffren immer einen Schlüssel, der unter allen relevanten Parteien geteilt wurde. Viele moderne kryptographische Schemata beinhalten jedoch nicht nur einen, sondern zwei Schlüssel: einen **privaten** und einen **öffentlichen Schlüssel**. Während ersterer in allen Anwendungen privat bleiben sollte, ist letzterer typischerweise öffentlich bekannt (daher ihre jeweiligen Namen). Im Bereich der Verschlüsselung kann der öffentliche Schlüssel verwendet werden, um die Nachricht zu verschlüsseln, während der private Schlüssel zur Entschlüsselung verwendet werden kann.

Der Zweig der Kryptographie, der sich mit Schemata befasst, bei denen alle Parteien einen Schlüssel teilen, ist als **symmetrische Kryptographie** bekannt. Der einzelne Schlüssel in einem solchen Schema wird üblicherweise als **privater Schlüssel** (oder Geheimschlüssel) bezeichnet. Der Zweig der Kryptographie, der sich mit Schemata befasst, die ein privates-öffentliches Schlüsselpaar erfordern, ist als **asymmetrische Kryptographie** bekannt. Diese Zweige werden manchmal auch als **Private-Key-Kryptographie** und **Public-Key-Kryptographie** bezeichnet, obwohl dies Verwirrung stiften kann, da öffentliche Schlüsselkryptographieschemata auch private Schlüssel haben.
Das Aufkommen der asymmetrischen Kryptografie Ende der 1970er Jahre war eines der wichtigsten Ereignisse in der Geschichte der Kryptografie. Ohne sie wären die meisten unserer modernen Kommunikationssysteme, einschließlich Bitcoin, nicht möglich oder zumindest sehr unpraktisch.
Wichtig ist, dass die moderne Kryptografie nicht ausschließlich das Studium von symmetrischen und asymmetrischen Schlüsselkryptografieschemata ist (obwohl das einen Großteil des Feldes abdeckt). Beispielsweise befasst sich die Kryptografie auch mit Hash-Funktionen und Pseudozufallszahlengeneratoren, und man kann auf diesen Primitiven Anwendungen aufbauen, die nicht mit symmetrischer oder asymmetrischer Schlüsselkryptografie zusammenhängen.

Drittens waren klassische Verschlüsselungsschemata, wie die in den Beale-Chiffren verwendeten, mehr Kunst als Wissenschaft. Ihre wahrgenommene Sicherheit basierte weitgehend auf Intuitionen bezüglich ihrer Komplexität. Typischerweise wurden sie gepatcht, wenn ein neuer Angriff auf sie bekannt wurde, oder ganz fallen gelassen, wenn der Angriff besonders schwerwiegend war. Die moderne Kryptografie hingegen ist eine strenge Wissenschaft mit einem formalen, mathematischen Ansatz sowohl für die Entwicklung als auch für die Analyse kryptografischer Schemata.<sup>[5](#footnote5)</sup>

Insbesondere konzentriert sich die moderne Kryptografie auf formale **Beweise der Sicherheit**. Jeder Sicherheitsbeweis für ein kryptografisches Schema erfolgt in drei Schritten:

1. Die Aussage einer **kryptografischen Definition von Sicherheit**, das heißt, ein Satz von Sicherheitszielen und die durch den Angreifer dargestellte Bedrohung.
2. Die Aussage aller mathematischen Annahmen hinsichtlich der Rechenkomplexität des Schemas. Beispielsweise kann ein kryptografisches Schema einen Pseudozufallszahlengenerator enthalten. Obwohl wir nicht beweisen können, dass diese existieren, können wir annehmen, dass sie es tun.
3. Die Darlegung eines mathematischen **Sicherheitsbeweises** des Schemas auf der Grundlage des formalen Sicherheitsbegriffs und aller mathematischen Annahmen.

Viertens, während Kryptografie historisch gesehen hauptsächlich in militärischen Einstellungen genutzt wurde, hat sie in unserem täglichen Leben im digitalen Zeitalter allgegenwärtig geworden. Ob Sie online Bankgeschäfte tätigen, in sozialen Medien posten, ein Produkt bei Amazon mit Ihrer Kreditkarte kaufen oder einem Freund Bitcoin zukommen lassen, Kryptografie ist das sine qua non unseres digitalen Zeitalters.

Angesichts dieser vier Aspekte der modernen Kryptografie könnten wir die moderne **Kryptografie** als die Wissenschaft charakterisieren, die sich mit der formalen Entwicklung und Analyse kryptografischer Schemata zur Sicherung digitaler Informationen gegen feindliche Angriffe befasst.<sup>[6](#footnote6)</sup> Sicherheit sollte hier im weitesten Sinne verstanden werden als die Verhinderung von Angriffen, die die Geheimhaltung, Integrität, Authentifizierung und/oder Nichtabstreitbarkeit in der Kommunikation beschädigen.

Kryptografie wird am besten als eine Teildisziplin der **Cybersicherheit** gesehen, die sich mit der Verhinderung von Diebstahl, Beschädigung und Missbrauch von Computersystemen befasst. Beachten Sie, dass viele Cybersicherheitsbedenken wenig oder nur teilweise mit Kryptografie zu tun haben.

Beispielsweise, wenn ein Unternehmen teure Server lokal beherbergt, könnte es darum besorgt sein, diese Hardware vor Diebstahl und Beschädigung zu sichern. Während dies ein Cybersicherheitsanliegen ist, hat es wenig mit Kryptografie zu tun.

Als weiteres Beispiel sind **Phishing-Angriffe** ein häufiges Problem in unserem modernen Zeitalter. Diese Angriffe versuchen, Menschen über eine E-Mail oder ein anderes Nachrichtenmedium zu täuschen, um sensible Informationen wie Passwörter oder Kreditkartennummern preiszugeben. Obwohl Kryptografie bis zu einem gewissen Grad bei der Bekämpfung von Phishing-Angriffen helfen kann, erfordert ein umfassender Ansatz mehr als nur die Verwendung von etwas Kryptografie.

## Offene Kommunikation
<chapterId>cb23d0a6-ba9a-5dc6-a55a-258405ae4117</chapterId>

Die moderne Kryptografie ist darauf ausgelegt, Sicherheitsgarantien in einer **offenen Kommunikations**umgebung zu bieten. Wenn unser Kommunikationskanal so gut geschützt ist, dass Lauscher keine Chance haben, unsere Nachrichten zu manipulieren oder auch nur zu beobachten, dann ist Kryptografie überflüssig. Die meisten unserer Kommunikationskanäle sind jedoch kaum so gut geschützt.
Das Rückgrat der Kommunikation in der modernen Welt ist ein riesiges Netzwerk aus Glasfaserkabeln. Telefonate führen, Fernsehen schauen und im Web surfen in einem modernen Haushalt hängen in der Regel von diesem Netzwerk aus Glasfaserkabeln ab (ein kleiner Prozentsatz könnte sich rein auf Satelliten verlassen). Es stimmt, dass Sie in Ihrem Zuhause verschiedene Datenverbindungen haben könnten, wie Koaxialkabel, (asymmetrische) digitale Teilnehmeranschlussleitung und Glasfaserkabel. Aber zumindest in der entwickelten Welt verbinden sich diese verschiedenen Datenmedien schnell außerhalb Ihres Hauses zu einem Knotenpunkt in einem riesigen Netzwerk aus Glasfaserkabeln, das den gesamten Globus verbindet. Ausnahmen sind einige abgelegene Gebiete der entwickelten Welt, wie in den Vereinigten Staaten und Australien, wo der Datenverkehr immer noch auch über traditionelle Kupfertelefonleitungen erhebliche Entfernungen zurücklegen könnte.

Es wäre unmöglich, potenziellen Angreifern den physischen Zugang zu diesem Netzwerk von Kabeln und seiner unterstützenden Infrastruktur zu verwehren. Tatsächlich wissen wir bereits, dass die meisten unserer Daten an entscheidenden Schnittpunkten des Internets von verschiedenen nationalen Nachrichtendiensten abgefangen werden. Dies umfasst alles von Facebook-Nachrichten bis zu den Webadressen, die Sie besuchen.

Obwohl die Überwachung von Daten in großem Maßstab einen mächtigen Gegner, wie eine nationale Nachrichtenagentur, erfordert, können Angreifer mit nur wenigen Ressourcen leicht versuchen, auf lokaler Ebene zu schnüffeln. Obwohl dies auf der Ebene des Abhörens von Leitungen geschehen kann, ist es weitaus einfacher, drahtlose Kommunikation abzufangen.

Die meisten unserer lokalen Netzwerkdaten – ob in unseren Häusern, im Büro oder in einem Café – reisen jetzt über Funkwellen zu drahtlosen Zugangspunkten auf All-in-One-Routern, anstatt durch physische Kabel. Ein Angreifer benötigt also wenig Ressourcen, um Ihren lokalen Verkehr abzufangen. Dies ist besonders besorgniserregend, da die meisten Menschen sehr wenig tun, um die Daten zu schützen, die über ihre lokalen Netzwerke reisen. Darüber hinaus können potenzielle Angreifer auch unsere mobilen Breitbandverbindungen, wie 3G, 4G und 5G, ins Visier nehmen. All diese drahtlosen Kommunikationen sind ein leichtes Ziel für Angreifer.

Daher ist die Idee, Kommunikation geheim zu halten, indem der Kommunikationskanal geschützt wird, für einen großen Teil der modernen Welt eine hoffnungslos illusorische Vorstellung. Alles, was wir wissen, rechtfertigt schwere Paranoia: Sie sollten immer davon ausgehen, dass jemand zuhört. Und Kryptographie ist das Hauptwerkzeug, das wir haben, um in dieser modernen Umgebung irgendeine Art von Sicherheit zu erlangen.

### Anmerkungen
[^1]: Für eine gute Zusammenfassung der Geschichte siehe Simon Singh, *The Code Book*, Fourth Estate (London, 1999), S. 82-99. Ein Kurzfilm der Geschichte wurde 2010 von Andrew Allen gemacht. Den Film, „The Thomas Beale Cipher“, finden Sie auf dessen Website [^1].

[^2]: Dieses Bild ist auf der Wikipedia-Seite für die Beale-Chiffren verfügbar [^2].

[^3]: Um genau zu sein, waren die wichtigen Anwendungen von kryptographischen Schemata mit Geheimhaltung beschäftigt. Kinder verwenden beispielsweise häufig einfache kryptographische Schemata zum „Spaß“. Geheimhaltung ist in diesen Fällen nicht wirklich ein Anliegen [^3].

[^4]: Bruce Schneier, *Applied Cryptography*, 2. Aufl., 2015 (Indianapolis, IN: John Wiley & Sons), S. 2 [^4].

[^5]: Siehe Jonathan Katz und Yehuda Lindell, *Introduction to Modern Cryptography*, CRC Press (Boca Raton, FL: 2015), insbes. S. 16–23, für eine gute Beschreibung [^5].

[^6]: Vgl. Katz und Lindell, ebenda, S. 3. Ich denke, ihre Charakterisierung hat einige Probleme, daher präsentiere ich hier eine leicht abweichende Version ihrer Aussage [^6].
[^7]: Siehe zum Beispiel Olga Khazan, „The creepy, long-standing practice of undersea cable tapping“, *The Atlantic*, 16. Juli 2013 (verfügbar unter [The Atlantic](https://www.theatlantic.com/international/archive/2013/07/the-creepy-long-standing-practice-of-undersea-cable-tapping/277855/)) [^7].

# Mathematische Grundlagen der Kryptographie I
<partId>1bf9f0aa-0f68-5493-83fb-2167238ff9de</partId>

Die Kryptographie basiert auf Mathematik. Und wenn man ein mehr als oberflächliches Verständnis von Kryptographie aufbauen möchte, muss man mit dieser Mathematik vertraut sein.

Dieses Kapitel führt die meisten der grundlegenden mathematischen Konzepte ein, auf die man beim Erlernen der Kryptographie stößt. Die Themen umfassen Zufallsvariablen, Modulo-Operationen, XOR-Operationen und Pseudozufälligkeit. Man sollte das Material in diesen Abschnitten beherrschen, um ein nicht-oberflächliches Verständnis von Kryptographie zu erlangen.

Das nächste Kapitel befasst sich mit der Zahlentheorie, die wesentlich herausfordernder ist.

## Zufallsvariablen
<chapterId>b623a7d0-3dff-5803-bd4e-8257ff73dd69</chapterId>

Eine Zufallsvariable wird typischerweise durch einen nicht fettgedruckten, Großbuchstaben dargestellt. So könnten wir beispielsweise von einer Zufallsvariablen X, einer Zufallsvariablen Y oder einer Zufallsvariablen Z sprechen. Dies ist die Notation, die ich auch von nun an verwenden werde.

Eine **Zufallsvariable** kann zwei oder mehr mögliche Werte annehmen, jeder mit einer bestimmten positiven Wahrscheinlichkeit. Die möglichen Werte sind im **Ergebnisset** aufgelistet.

Jedes Mal, wenn man eine **Zufallsvariable** abfragt, zieht man einen bestimmten Wert aus ihrem Ergebnisset gemäß den definierten Wahrscheinlichkeiten.

Wenden wir uns einem einfachen Beispiel zu. Nehmen wir an, eine Variable X ist wie folgt definiert:

* X hat das Ergebnisset {1,2}
* Pr [X = 1] = 0,5
* Pr [X = 2] = 0,5

Es ist leicht zu erkennen, dass X eine Zufallsvariable ist. Erstens gibt es zwei oder mehr mögliche Werte, die X annehmen kann, nämlich 1 und 2. Zweitens hat jeder mögliche Wert eine positive Wahrscheinlichkeit, aufzutreten, wenn man X abfragt, nämlich 0,5.

Alles, was eine Zufallsvariable benötigt, ist ein Ergebnisset mit zwei oder mehr Möglichkeiten, wobei jede Möglichkeit eine positive Wahrscheinlichkeit hat, bei der Abfrage aufzutreten. Im Prinzip kann eine Zufallsvariable also abstrakt definiert werden, losgelöst von jedem Kontext. In diesem Fall könnte man sich das „Abfragen“ als Durchführung eines natürlichen Experiments vorstellen, um den Wert der Zufallsvariablen zu bestimmen.

Die Variable X oben wurde abstrakt definiert. Man könnte also denken, das Abfragen der Variablen X oben als das Werfen einer fairen Münze und das Zuweisen von „2“ im Fall von Kopf und „1“ im Fall von Zahl zu betrachten. Bei jeder Abfrage von X wirft man die Münze erneut.

Alternativ könnte man sich auch vorstellen, X abzufragen, indem man einen fairen Würfel wirft und „2“ zuweist, falls der Würfel auf 1, 3 oder 4 landet, und „1“ zuweist, falls der Würfel auf 2, 5 oder 6 landet. Jedes Mal, wenn man X abfragt, wirft man den Würfel erneut.

Tatsächlich kann jedes natürliche Experiment, das es erlauben würde, die Wahrscheinlichkeiten der möglichen Werte von X oben zu definieren, im Hinblick auf die Zeichnung vorgestellt werden.
Häufig werden Zufallsvariablen jedoch nicht nur abstrakt eingeführt. Stattdessen hat die Menge der möglichen Ausgangswerte eine explizite reale Bedeutung (anstatt nur als Zahlen). Darüber hinaus könnten diese Ausgangswerte gegen einen bestimmten Typ von Experiment definiert sein (anstatt als jedes natürliche Experiment mit diesen Werten).
Betrachten wir nun ein Beispiel einer Variablen X, die nicht abstrakt definiert ist. X wird wie folgt definiert, um zu bestimmen, welches von zwei Teams ein Fußballspiel beginnt:

* X hat die Ausgangsmenge {rot beginnt, blau beginnt}
* Werfen einer bestimmten Münze C: Zahl = „rot beginnt“; Kopf = „blau beginnt“
* Pr [X = rot beginnt] = 0,5
* Pr [X = blau beginnt] = 0,5

In diesem Fall wird der Ausgangsmenge von X eine konkrete Bedeutung verliehen, nämlich welches Team in einem Fußballspiel beginnt. Darüber hinaus werden die möglichen Ausgänge und ihre zugehörigen Wahrscheinlichkeiten durch ein konkretes Experiment bestimmt, nämlich das Werfen einer bestimmten Münze C.

In Diskussionen über Kryptographie werden Zufallsvariablen normalerweise gegen eine Ausgangsmenge mit realer Bedeutung eingeführt. Es könnte die Menge aller Nachrichten sein, die verschlüsselt werden könnten, bekannt als der Nachrichtenraum, oder die Menge aller Schlüssel, die die Parteien, die die Verschlüsselung verwenden, auswählen können, bekannt als der Schlüsselraum.

Zufallsvariablen in Diskussionen über Kryptographie werden jedoch normalerweise nicht gegen ein bestimmtes natürliches Experiment definiert, sondern gegen jedes Experiment, das die richtigen Wahrscheinlichkeitsverteilungen liefern könnte.

Zufallsvariablen können diskrete oder kontinuierliche Wahrscheinlichkeitsverteilungen haben. Zufallsvariablen mit einer **diskreten Wahrscheinlichkeitsverteilung** – das heißt, diskrete Zufallsvariablen – haben eine endliche Anzahl möglicher Ausgänge. Die Zufallsvariable X in beiden bisher gegebenen Beispielen war diskret.

**Kontinuierliche Zufallsvariablen** können stattdessen Werte in einem oder mehreren Intervallen annehmen. Man könnte zum Beispiel sagen, dass eine Zufallsvariable bei der Stichprobe jeden reellen Wert zwischen 0 und 1 annimmt und dass jede reelle Zahl in diesem Intervall gleich wahrscheinlich ist. Innerhalb dieses Intervalls gibt es unendlich viele mögliche Werte.

Für kryptografische Diskussionen müssen Sie nur diskrete Zufallsvariablen verstehen. Jede Diskussion über Zufallsvariablen sollte daher als Bezugnahme auf diskrete Zufallsvariablen verstanden werden, sofern nicht ausdrücklich anders angegeben.

### Grafische Darstellung von Zufallsvariablen

Die möglichen Werte und zugehörigen Wahrscheinlichkeiten für eine Zufallsvariable können leicht durch ein Diagramm visualisiert werden. Betrachten Sie zum Beispiel die Zufallsvariable X aus dem vorherigen Abschnitt mit einer Ausgangsmenge von {1,2} und Pr [X = 1] = 0,5 und Pr [X = 2] = 0,5. Typischerweise würden wir eine solche Zufallsvariable in Form eines Balkendiagramms darstellen, wie in *Abbildung 1*.

*Abbildung 1: Zufallsvariable X*

![Abbildung 1: Zufallsvariable X.](assets/Figure2-1.webp)

Die breiten Balken in *Abbildung 1* sollen natürlich nicht suggerieren, dass die Zufallsvariable X tatsächlich kontinuierlich ist. Stattdessen werden die Balken breit gemacht, um visuell ansprechender zu sein (nur eine gerade Linie nach oben bietet eine weniger intuitive Visualisierung).

### Gleichverteilte Variablen

Im Ausdruck „Zufallsvariable“ bedeutet der Begriff „zufällig“ einfach „probabilistisch“. Mit anderen Worten, es bedeutet einfach, dass zwei oder mehr mögliche Ausgänge der Variablen mit bestimmten Wahrscheinlichkeiten auftreten. Diese Ausgänge müssen jedoch *nicht notwendigerweise* gleich wahrscheinlich sein (obwohl der Begriff „zufällig“ in anderen Kontexten diese Bedeutung haben kann).
Eine **gleichverteilte Variable** ist ein spezieller Fall einer Zufallsvariable. Sie kann zwei oder mehr Werte annehmen, alle mit gleicher Wahrscheinlichkeit. Die Zufallsvariable X, dargestellt in *Abbildung 1*, ist eindeutig eine gleichverteilte Variable, da beide möglichen Ergebnisse mit einer Wahrscheinlichkeit von 0,5 auftreten. Es gibt jedoch viele Zufallsvariablen, die keine Beispiele für gleichverteilte Variablen sind.
Betrachten Sie zum Beispiel die Zufallsvariable Y. Sie hat die Ergebnismenge {1,2,3,8,10} und die folgende Wahrscheinlichkeitsverteilung: Pr [Y = 1] = 0,25; Pr [Y = 2] = 0,35; Pr [Y = 3] = 0,1; Pr [Y = 8] = 0,25; Pr [Y = 10] = 0,05.

Während zwei mögliche Ergebnisse tatsächlich eine gleiche Wahrscheinlichkeit des Auftretens haben, nämlich 1 und 8, kann Y auch bestimmte Werte mit anderen Wahrscheinlichkeiten als 0,25 bei der Stichprobenziehung annehmen. Daher ist Y zwar tatsächlich eine Zufallsvariable, aber keine gleichverteilte Variable.

Eine grafische Darstellung von Y wird in *Abbildung 2* bereitgestellt.

*Abbildung 2: Zufallsvariable Y*

![Abbildung 2: Zufallsvariable Y.](assets/Figure2-2.webp "Abbildung 2: Zufallsvariable Y")

Als letztes Beispiel betrachten Sie die Zufallsvariable Z. Sie hat die Ergebnismenge {1,3,7,11,12} und die folgende Wahrscheinlichkeitsverteilung: Pr (2) = 0,2; Pr (3) = 0,2; Pr (9) = 0,2; Pr (11) = 0,2; Pr (12) = 0,2. Sie können sie in Abbildung 3 sehen. Die Zufallsvariable Z ist im Gegensatz zu Y tatsächlich eine gleichverteilte Variable, da alle Wahrscheinlichkeiten für die möglichen Werte bei der Stichprobenziehung gleich sind.

*Abbildung 3: Zufallsvariable Z*

![Abbildung 3: Zufallsvariable Z.](assets/Figure2-3.webp "Abbildung 3: Zufallsvariable Z")


### Bedingte Wahrscheinlichkeit

Nehmen wir an, Bob beabsichtigt, zufällig einen Tag aus dem letzten Kalenderjahr auszuwählen. Was sollten wir schlussfolgern, ist die Wahrscheinlichkeit, dass der ausgewählte Tag im Sommer liegt?

Solange wir denken, dass Bobs Prozess tatsächlich wirklich gleichmäßig sein wird, sollten wir schlussfolgern, dass es eine 1/4 Wahrscheinlichkeit gibt, dass Bob einen Tag im Sommer auswählt. Dies ist die **unbedingte Wahrscheinlichkeit** des zufällig ausgewählten Tages, im Sommer zu sein.

Nehmen wir jetzt an, dass Bob statt eines Kalendertages zufällig nur aus jenen Tagen auswählt, an denen die Mittagstemperatur am Crystal Lake (New Jersey) 21 Grad Celsius oder höher war. Angesichts dieser zusätzlichen Information, was können wir über die Wahrscheinlichkeit schlussfolgern, dass Bob einen Tag im Sommer auswählt?

Wir sollten wirklich eine andere Schlussfolgerung ziehen als zuvor, auch ohne weitere spezifische Informationen (z.B. die Temperatur zu Mittag jeden Tag im letzten Kalenderjahr).

Da bekannt ist, dass Crystal Lake in New Jersey liegt, würden wir sicherlich nicht erwarten, dass die Mittagstemperatur im Winter 21 Grad Celsius oder höher ist. Stattdessen ist es viel wahrscheinlicher, dass es ein warmer Tag im Frühling oder Herbst oder ein Tag irgendwo im Sommer ist. Daher wird, wenn bekannt ist, dass die Mittagstemperatur am Crystal Lake am ausgewählten Tag 21 Grad Celsius oder höher war, die Wahrscheinlichkeit, dass der von Bob ausgewählte Tag im Sommer liegt, viel höher. Dies ist die **bedingte Wahrscheinlichkeit** des zufällig ausgewählten Tages, im Sommer zu sein, gegeben, dass die Mittagstemperatur am Crystal Lake 21 Grad Celsius oder höher war.
Im Gegensatz zum vorherigen Beispiel können die Wahrscheinlichkeiten zweier Ereignisse auch völlig unabhängig voneinander sein. In diesem Fall sagen wir, dass sie **unabhängig** sind.
Nehmen wir zum Beispiel an, dass eine bestimmte faire Münze Kopf gelandet ist. Angesichts dieser Tatsache, was ist dann die Wahrscheinlichkeit, dass es morgen regnen wird? Die bedingte Wahrscheinlichkeit in diesem Fall sollte die gleiche sein wie die unbedingte Wahrscheinlichkeit, dass es morgen regnen wird, da ein Münzwurf im Allgemeinen keinen Einfluss auf das Wetter hat.

Wir verwenden ein „|“ Symbol, um bedingte Wahrscheinlichkeitsaussagen zu schreiben. Zum Beispiel kann die Wahrscheinlichkeit des Ereignisses A, gegeben dass Ereignis B eingetreten ist, wie folgt geschrieben werden: Pr[A|B]. Wenn also zwei Ereignisse, A und B, unabhängig sind, dann gilt Pr[A|B] = Pr[A] und Pr[B|A] = Pr[B]. Die Bedingung für Unabhängigkeit kann wie folgt vereinfacht werden: Pr[A,B] = Pr[A]*Pr[B].

Ein Schlüsselergebnis in der Wahrscheinlichkeitstheorie ist als **Bayessches Theorem** bekannt. Es besagt im Grunde, dass Pr[A|B] wie folgt umgeschrieben werden kann:

Pr[A|B] = (Pr[B|A] • Pr[A]) / Pr[B]

Anstatt bedingte Wahrscheinlichkeiten mit spezifischen Ereignissen zu verwenden, können wir uns auch die bedingten Wahrscheinlichkeiten ansehen, die mit zwei oder mehr Zufallsvariablen über eine Menge möglicher Ereignisse beteiligt sind. Nehmen wir zwei Zufallsvariablen, X und Y. Wir können jeden möglichen Wert für X mit x und jeden möglichen Wert für Y mit y bezeichnen. Wir könnten dann sagen, dass zwei Zufallsvariablen unabhängig sind, wenn die folgende Aussage zutrifft:

Pr[X = x,Y = y] = Pr[X = x] • Pr[Y = y] für alle x und y

Lassen Sie uns etwas expliziter darüber sein, was diese Aussage bedeutet.

Nehmen wir an, dass die Ergebnismengen für X und Y wie folgt definiert sind: **X** = {x<sub>1</sub>,x<sub>2</sub>….,x<sub>i</sub>,….x<sub>n</sub>} und **Y** = {y<sub>1</sub>,y<sub>2</sub>….,y<sub>i</sub>,….y<sub>m</sub>}. (Es ist üblich, Mengen von Werten durch fettgedruckte, großgeschriebene Buchstaben anzugeben.)

Nehmen wir nun an, Sie beproben Y und beobachten y<sub>1</sub>. Die obige Aussage sagt uns, dass die Wahrscheinlichkeit, nun x<sub>1</sub> durch Beprobung von X zu erhalten, genau die gleiche ist, als hätten wir y<sub>1</sub> nie beobachtet. Dies gilt für jedes y<sub>i</sub>, das wir aus unserer anfänglichen Beprobung von Y hätten ziehen können. Schließlich gilt dies nicht nur für x<sub>1</sub>. Für jedes x<sub>i</sub> wird die Wahrscheinlichkeit des Auftretens nicht durch das Ergebnis einer Beprobung von Y beeinflusst. All dies gilt auch für den Fall, dass X zuerst beprobt wird.

Lassen Sie uns unsere Diskussion mit einem etwas philosophischeren Punkt beenden. In jeder realen Situation wird die Wahrscheinlichkeit eines Ereignisses immer gegen einen bestimmten Satz von Informationen abgewogen. Es gibt keine „unbedingte Wahrscheinlichkeit“ im sehr strengen Sinne des Wortes.

Nehmen wir zum Beispiel an, ich frage Sie nach der Wahrscheinlichkeit, dass Schweine bis 2030 fliegen werden. Obwohl ich Ihnen keine weiteren Informationen gebe, wissen Sie deutlich viel über die Welt, das Ihr Urteil beeinflussen kann. Sie haben noch nie gesehen, dass Schweine fliegen. Sie wissen, dass die meisten Menschen nicht erwarten, dass sie fliegen. Sie wissen, dass sie nicht wirklich zum Fliegen gebaut sind. Und so weiter.
Wenn wir also von einer "unbedingten Wahrscheinlichkeit" eines Ereignisses im realen Kontext sprechen, kann dieser Begriff wirklich nur eine Bedeutung haben, wenn wir ihn als "die Wahrscheinlichkeit ohne weitere explizite Informationen" verstehen. Jedes Verständnis einer "bedingten Wahrscheinlichkeit" sollte dann immer gegen ein spezifisches Stück Information verstanden werden.
Ich könnte Ihnen zum Beispiel die Wahrscheinlichkeit fragen, dass Schweine bis 2030 fliegen werden, nachdem ich Ihnen Beweise gegeben habe, dass einige Ziegen in Neuseeland nach einigen Jahren des Trainings gelernt haben zu fliegen. In diesem Fall werden Sie wahrscheinlich Ihr Urteil über die Wahrscheinlichkeit, dass Schweine bis 2030 fliegen werden, anpassen. Also ist die Wahrscheinlichkeit, dass Schweine bis 2030 fliegen werden, bedingt durch diese Beweise über Ziegen in Neuseeland.

## Die Modulo-Operation
<chapterId>709b34e5-b155-53d2-abbd-97d67e56db00</chapterId>

Der grundlegendste Ausdruck mit der **Modulo-Operation** ist folgender: x mod y.

Die Variable x wird als Dividend und die Variable y als Divisor bezeichnet. Um eine Modulo-Operation mit einem positiven Dividend und einem positiven Divisor durchzuführen, bestimmen Sie einfach den Rest der Division.

Betrachten Sie zum Beispiel den Ausdruck 25 mod 4. Die Zahl 4 geht insgesamt 6 Mal in die Zahl 25 ein. Der Rest dieser Division ist 1. Daher ist 25 mod 4 gleich 1. Auf ähnliche Weise können wir die untenstehenden Ausdrücke bewerten:

* 29 mod 30 = 29 (da 30 insgesamt 0 Mal in 29 geht und der Rest 29 ist)
* 42 mod 2 = 0 (da 2 insgesamt 21 Mal in 42 geht und der Rest 0 ist)
* 12 mod 5 = 2 (da 5 insgesamt 2 Mal in 12 geht und der Rest 2 ist)
* 20 mod 8 = 4 (da 8 insgesamt 2 Mal in 20 geht und der Rest 4 ist)

Wenn der Dividend oder Divisor negativ ist, können Modulo-Operationen von Programmiersprachen unterschiedlich gehandhabt werden.

Sie werden definitiv auf Fälle mit einem negativen Dividend in der Kryptographie stoßen. In diesen Fällen ist der typische Ansatz wie folgt:

* Bestimmen Sie zuerst den nächstniedrigeren Wert *kleiner oder gleich* dem Dividend, in den der Divisor mit einem Rest von Null teilt. Nennen Sie diesen Wert p.
* Wenn der Dividend x ist, dann ist das Ergebnis der Modulo-Operation der Wert von x – p.

Nehmen wir zum Beispiel an, der Dividend ist – 20 und der Divisor 3. Der nächstniedrigere Wert kleiner oder gleich – 20, in den 3 gleichmäßig teilt, ist – 21. Der Wert von x – p in diesem Fall ist – 20 – – 21. Das ergibt 1 und daher ist – 20 mod 3 gleich 1. Auf ähnliche Weise können wir die untenstehenden Ausdrücke bewerten:

* – 8 mod 5 = 2
* – 19 mod 16 = 13
* – 14 mod 6 = 4

Bezüglich der Notation werden Sie typischerweise folgende Arten von Ausdrücken sehen: x = [y mod z]. Aufgrund der Klammern gilt die Modulo-Operation in diesem Fall nur für die rechte Seite des Ausdrucks. Wenn y gleich 25 und z gleich 4 ist, zum Beispiel, dann wird x zu 1 bewertet.
Ohne Klammern wirkt die Modulo-Operation auf *beide Seiten* eines Ausdrucks. Nehmen wir zum Beispiel den folgenden Ausdruck: x = y mod z. Wenn y gleich 25 und z gleich 4 ist, dann wissen wir nur, dass x mod 4 den Wert 1 ergibt. Dies ist konsistent mit jedem Wert für x aus der Menge {….– 7, – 3, 1, 5, 9….}. 
Der Bereich der Mathematik, der Modulo-Operationen mit Zahlen und Ausdrücken umfasst, wird als **modulare Arithmetik** bezeichnet. Man kann sich diesen Bereich als Arithmetik für Fälle vorstellen, in denen die Zahlengerade nicht unendlich lang ist. Obwohl wir typischerweise auf Modulo-Operationen für (positive) ganze Zahlen innerhalb der Kryptographie stoßen, können Modulo-Operationen auch mit beliebigen reellen Zahlen durchgeführt werden.

### Der Verschiebechiffre

Die Modulo-Operation wird häufig innerhalb der Kryptographie angetroffen. Um dies zu veranschaulichen, betrachten wir eines der berühmtesten historischen Verschlüsselungsschemata: den Verschiebechiffre.

Definieren wir ihn zunächst. Nehmen wir ein Wörterbuch *D*, das alle Buchstaben des englischen Alphabets in der Reihenfolge den Zahlen {0,1,2…,25} zuordnet. Nehmen wir einen Nachrichtenraum **M** an. Der **Verschiebechiffre** ist dann ein Verschlüsselungsschema, das wie folgt definiert ist:

- Wähle gleichmäßig einen Schlüssel k aus dem Schlüsselraum **K**, wobei **K** = {0,1,2,…,25}<sup>[1](#footnote1)</sup>
- Verschlüssele eine Nachricht m є **M**, wie folgt:
    - Trenne m in seine einzelnen Buchstaben m<sub>0</sub>, m<sub>1</sub>,….m<sub>i</sub>….,m<sub>l</sub>
    - Konvertiere jeden m<sub>i</sub> in eine Zahl gemäß *D*
    - Für jeden m<sub>i</sub>, c<sub>i</sub> = [(m<sub>i</sub> + k) mod 26]
    - Konvertiere jeden c<sub>i</sub> in einen Buchstaben gemäß *D*
    - Kombiniere dann c<sub>0</sub>, c<sub>1</sub>,….,c<sub>l</sub>, um den Chiffretext c zu erhalten
- Entschlüssele einen Chiffretext c wie folgt:
    -- Konvertiere jeden c<sub>i</sub> in eine Zahl gemäß *D*
    -- Für jeden c<sub>i</sub>, m<sub>i</sub> = [(c<sub>i</sub> – k) mod 26]
    -- Konvertiere jeden m<sub>i</sub> in einen Buchstaben gemäß *D*
    -- Kombiniere dann m<sub>0</sub>, m<sub>1</sub>,….,m<sub>l</sub>, um die ursprüngliche Nachricht m zu erhalten

Der Modulo-Operator im Verschiebechiffre stellt sicher, dass Buchstaben umlaufen, sodass alle Chiffretextbuchstaben definiert sind. Um dies zu veranschaulichen, betrachten wir die Anwendung des Verschiebechiffres auf das Wort „DOG“.

Nehmen wir an, dass du gleichmäßig einen Schlüssel mit dem Wert 17 ausgewählt hast. Der Buchstabe „O“ entspricht 15. Ohne die Modulo-Operation würde die Addition dieser Klartextzahl mit dem Schlüssel zu einer Chiffretextzahl von 32 führen. Diese Chiffretextzahl könnte jedoch nicht in einen Chiffretextbuchstaben umgewandelt werden, da das englische Alphabet nur 26 Buchstaben hat. Die Modulo-Operation stellt sicher, dass die Chiffretextzahl tatsächlich 6 ist (das Ergebnis von 32 mod 26), was dem Chiffretextbuchstaben „G“ entspricht.

Die gesamte Verschlüsselung des Wortes „DOG“ mit einem Schlüsselwert von 17 ist wie folgt:
* Nachricht = HUND = H,U,N,D = 3,15,6* c<sub>0</sub> = [(3 + 17) Mod 26] = [(20) Mod 26] = 20 = U
* c<sub>1</sub> = [(15 + 17) Mod 26] = [(32) Mod 26] = 6 = G
* c<sub>2</sub> = [(6 + 17) Mod 26] = [(23) Mod 26] = 23 = X
* c = UGX

Jeder kann intuitiv verstehen, wie die Verschiebechiffre funktioniert und sie wahrscheinlich selbst anwenden. Um jedoch Ihr Wissen über Kryptographie zu erweitern, ist es wichtig, sich mit der Formalisierung vertraut zu machen, da die Schemata wesentlich komplizierter werden. Daher wurden die Schritte für die Verschiebechiffre formalisiert.

## Die XOR-Operation
<chapterId>22f185cc-c516-5b33-950b-0908f2f881fe</chapterId>

Alle Computerdaten werden auf Bit-Ebene verarbeitet, gespeichert und über Netzwerke gesendet. Alle kryptographischen Schemata, die auf Computerdaten angewendet werden, operieren ebenfalls auf der Bit-Ebene.

Nehmen wir an, Sie haben eine E-Mail in Ihre E-Mail-Anwendung getippt. Jede Verschlüsselung, die Sie anwenden, erfolgt nicht direkt auf den ASCII-Zeichen Ihrer E-Mail. Stattdessen wird sie auf die Bit-Darstellung der Buchstaben und anderen Symbole in Ihrer E-Mail angewendet.

Eine wichtige mathematische Operation, die für die moderne Kryptographie neben der Modulo-Operation verstanden werden muss, ist die **XOR-Operation** oder „exklusives Oder“. Diese Operation nimmt zwei Bits als Eingabe und liefert ein weiteres Bit als Ausgabe. Die XOR-Operation wird einfach als "XOR" bezeichnet. Sie ergibt 0, wenn die beiden Bits gleich sind, und 1, wenn die beiden Bits unterschiedlich sind. Sie können die vier Möglichkeiten unten sehen.

* 0 XOR 0 = 0
* 0 XOR 1 = 1
* 1 XOR 0 = 1
* 1 XOR 1 = 0

Sie können eine XOR-Operation auf zwei Nachrichten ausführen, die länger als ein einzelnes Bit sind, indem Sie die Bits dieser beiden Nachrichten ausrichten und die XOR-Operation auf jedes einzelne Paar von Bits durchführen.

Um zu veranschaulichen, nehmen wir an, Sie haben eine Nachricht m<sub>1</sub> (01111001) und eine Nachricht m<sub>2</sub> (01011001). Die XOR-Operation dieser beiden Nachrichten kann unten gesehen werden.

* m<sub>1</sub> XOR m<sub>2</sub> = 01111001 XOR 01011001 = 00100000

Der Prozess ist unkompliziert. Zuerst führen Sie die XOR-Operation auf die am weitesten links stehenden Bits von m<sub>1</sub> und m<sub>2</sub> durch. In diesem Fall ist das 0 XOR 0 = 0. Dann führen Sie die XOR-Operation auf das zweite Paar von Bits von links durch. In diesem Fall ist das 1 XOR 1 = 0. Sie setzen diesen Prozess fort, bis Sie die XOR-Operation auf die am weitesten rechts stehenden Bits durchgeführt haben.
Es ist leicht zu erkennen, dass die XOR-Operation kommutativ ist, nämlich dass m<sub>1</sub> XOR m<sub>2</sub> = m<sub>2</sub> XOR m<sub>1</sub>. Zusätzlich ist die XOR-Operation auch assoziativ. Das heißt, (m<sub>1</sub> XOR m<sub>2</sub>) XOR m<sub>3</sub> = m<sub>1</sub> XOR (m<sub>2</sub> XOR m<sub>3</sub>).
Eine XOR-Operation auf zwei Zeichenketten unterschiedlicher Länge kann je nach Kontext unterschiedlich interpretiert werden. Wir werden uns hier nicht mit XOR-Operationen auf Zeichenketten unterschiedlicher Längen beschäftigen.

Eine XOR-Operation entspricht dem Spezialfall der Durchführung einer Modulo-Operation auf die Addition von Bits, wenn der Divisor 2 ist. Die Äquivalenz können Sie in den folgenden Ergebnissen sehen:

* (0 + 0) mod 2 = 0 XOR 0 = 0
* (1 + 0) mod 2 = 1 XOR 0 = 1
* (0 + 1) mod 2 = 0 XOR 1 = 1
* (1 + 1) mod 2 = 1 XOR 1 = 0

## Pseudorandomness
<chapterId>20463fc5-3e92-581f-a1b7-3151279bd95e</chapterId>

In unserer Diskussion über zufällige und gleichverteilte Variablen haben wir eine spezifische Unterscheidung zwischen „zufällig“ und „gleichverteilt“ gemacht. Diese Unterscheidung wird in der Praxis typischerweise beibehalten, wenn es um die Beschreibung von Zufallsvariablen geht. Jedoch muss in unserem aktuellen Kontext diese Unterscheidung fallen gelassen werden und „zufällig“ und „gleichverteilt“ werden synonym verwendet. Ich werde am Ende des Abschnitts erklären, warum.

Zunächst können wir eine binäre Zeichenkette der Länge n **zufällig** (oder **gleichverteilt**) nennen, wenn sie das Ergebnis der Stichprobe einer gleichverteilten Variablen S war, die jeder binären Zeichenkette dieser Länge n eine gleiche Wahrscheinlichkeit der Auswahl gibt.

Nehmen wir zum Beispiel die Menge aller binären Zeichenketten der Länge 8: {0000 0000, 0000 0001, …, 1111 1111}. (Es ist üblich, eine 8-Bit-Zeichenkette in zwei Quartette zu schreiben, jedes wird als **Nibble** bezeichnet.) Nennen wir diese Menge von Zeichenketten **S<sub>8</sub>**.

Gemäß der obigen Definition können wir dann eine bestimmte binäre Zeichenkette der Länge 8 als zufällig (oder gleichverteilt) bezeichnen, wenn sie das Ergebnis der Stichprobe einer gleichverteilten Variablen S war, die jeder Zeichenkette in **S<sub>8</sub>** eine gleiche Wahrscheinlichkeit der Auswahl gibt. Da die Menge **S<sub>8</sub>** 2<sup>8</sup> Elemente umfasst, müsste die Wahrscheinlichkeit der Auswahl bei der Stichprobe für jede Zeichenkette in der Menge 1/2<sup>8</sup> sein.

Ein Schlüsselaspekt für die Zufälligkeit einer binären Zeichenkette ist, dass sie in Bezug auf den Prozess definiert wird, durch den sie ausgewählt wurde. Die Form einer bestimmten binären Zeichenkette an sich verrät daher nichts über ihre Zufälligkeit bei der Auswahl.

Zum Beispiel haben viele Menschen intuitiv die Idee, dass eine Zeichenkette wie 1111 1111 nicht zufällig ausgewählt worden sein könnte. Aber das ist offensichtlich falsch.
Definieren einer einheitlichen Variablen S über alle Binärstrings der Länge 8, ist die Wahrscheinlichkeit, 1111 1111 aus der Menge **S<sub>8</sub>** auszuwählen, dieselbe wie die eines Strings wie 0111 01001. Daher kann man über die Zufälligkeit eines Strings nichts aussagen, nur indem man den String selbst analysiert.
Wir können auch von zufälligen Strings sprechen, ohne speziell Binärstrings zu meinen. Wir könnten zum Beispiel von einem zufälligen Hex-String AF 02 82 sprechen. In diesem Fall wäre der String zufällig aus der Menge aller Hex-Strings der Länge 6 ausgewählt worden. Dies entspricht der zufälligen Auswahl eines Binärstrings der Länge 24, da jede Hex-Ziffer 4 Bits repräsentiert.

Typischerweise bezieht sich der Ausdruck „ein zufälliger String“, ohne weitere Qualifikation, auf einen String, der zufällig aus der Menge aller Strings derselben Länge ausgewählt wurde. So habe ich es oben beschrieben. Ein String der Länge n kann natürlich auch zufällig aus einer anderen Menge ausgewählt werden. Eine, die zum Beispiel nur eine Teilmenge aller Strings der Länge n bildet, oder vielleicht eine Menge, die Strings unterschiedlicher Länge umfasst. In diesen Fällen würden wir jedoch nicht von einem „zufälligen String“ sprechen, sondern eher von „einem String, der zufällig aus irgendeiner Menge **S** ausgewählt wurde“.

Ein Schlüsselkonzept innerhalb der Kryptografie ist das der Pseudozufälligkeit. Ein **pseudorandom String** der Länge n erscheint *als ob* er das Ergebnis der Stichprobe einer einheitlichen Variablen S wäre, die jedem String in **S<sub>n</sub>** eine gleiche Wahrscheinlichkeit der Auswahl gibt. Tatsächlich ist der String jedoch das Ergebnis der Stichprobe einer einheitlichen Variablen S', die nur eine Wahrscheinlichkeitsverteilung definiert – nicht notwendigerweise eine mit gleichen Wahrscheinlichkeiten für alle möglichen Ergebnisse – auf einer Teilmenge von **S<sub>n</sub>**. Der entscheidende Punkt hier ist, dass niemand wirklich zwischen Stichproben von S und S' unterscheiden kann, selbst wenn man viele davon nimmt.

Nehmen wir zum Beispiel eine Zufallsvariable S. Ihre Ergebnismenge ist **S<sub>256</sub>**, dies ist die Menge aller Binärstrings der Länge 256. Diese Menge hat 2<sup>256</sup> Elemente. Jedes Element hat bei der Stichprobe eine gleiche Wahrscheinlichkeit der Auswahl, 1/2<sup>256</sup>.

Nehmen wir zusätzlich eine Zufallsvariable S’. Ihre Ergebnismenge umfasst nur 2<sup>128</sup> Binärstrings der Länge 256. Sie hat eine gewisse Wahrscheinlichkeitsverteilung über diese Strings, aber diese Verteilung ist nicht notwendigerweise gleichmäßig.

Nehmen wir an, ich hätte jetzt 1000er Stichproben von S und 1000er Stichproben von S' genommen und Ihnen die beiden Ergebnismengen gegeben. Ich sage Ihnen, welche Ergebnismenge mit welcher Zufallsvariablen verbunden ist. Als Nächstes nehme ich eine Stichprobe von einer der beiden Zufallsvariablen. Aber dieses Mal sage ich Ihnen nicht, von welcher Zufallsvariablen ich die Stichprobe nehme. Wenn S' pseudorandom wäre, dann ist die Idee, dass Ihre Wahrscheinlichkeit, die richtige Vermutung anzustellen, welche Zufallsvariable ich beprobt habe, praktisch nicht besser als 1/2 ist.

Typischerweise wird ein pseudorandom String der Länge n erzeugt, indem zufällig ein String der Größe n – x ausgewählt wird, wobei x eine positive ganze Zahl ist, und dieser als Eingabe für einen expansionsfähigen Algorithmus verwendet wird. Dieser zufällige String der Größe n – x ist als der **Seed** bekannt.
Pseudorandom-Zeichenfolgen sind ein Schlüsselkonzept, um Kryptografie praktikabel zu machen. Betrachten Sie zum Beispiel Stromchiffren. Bei einer Stromchiffre wird ein zufällig ausgewählter Schlüssel in einen Expansionsalgorithmus eingespeist, um eine viel größere pseudorandom-Zeichenfolge zu erzeugen. Diese pseudorandom-Zeichenfolge wird dann mittels einer XOR-Operation mit dem Klartext kombiniert, um einen Chiffretext zu erzeugen.
Wenn wir nicht in der Lage wären, diese Art von pseudorandom-Zeichenfolge für eine Stromchiffre zu erzeugen, dann bräuchten wir einen Schlüssel, der so lang wie die Nachricht ist, um deren Sicherheit zu gewährleisten. Dies ist in den meisten Fällen keine sehr praktikable Option.

Die in diesem Abschnitt diskutierte Vorstellung von Pseudorandomität kann formaler definiert werden. Sie erstreckt sich auch auf andere Kontexte. Aber wir müssen hier nicht tiefer in diese Diskussion eintauchen. Alles, was Sie für einen Großteil der Kryptografie intuitiv verstehen müssen, ist der Unterschied zwischen einer zufälligen und einer pseudorandom-Zeichenfolge.<sup>[2](#footnote2)</sup>

Der Grund für das Weglassen der Unterscheidung zwischen „zufällig“ und „gleichverteilt“ in unserer Diskussion sollte nun auch klar sein. In der Praxis verwendet jeder den Begriff pseudorandom, um eine Zeichenfolge zu bezeichnen, die **als ob** sie das Ergebnis des Samplings einer gleichverteilten Variablen S wäre. Streng genommen sollten wir eine solche Zeichenfolge „pseudo-gleichverteilt“ nennen, indem wir unsere Sprache von früher übernehmen. Da der Begriff „pseudo-gleichverteilt“ jedoch umständlich ist und von niemandem verwendet wird, werden wir ihn hier der Klarheit halber nicht einführen. Stattdessen lassen wir einfach die Unterscheidung zwischen „zufällig“ und „gleichverteilt“ im aktuellen Kontext fallen.

## Anmerkungen
<chapterId>7cccd92c-15bc-5394-9024-af126988ecd7</chapterId>

[^1]: Wir können diese Aussage genau definieren, indem wir die Terminologie aus dem vorherigen Abschnitt verwenden. Lassen Sie eine gleichverteilte Variable K **K** als ihre Menge möglicher Ergebnisse haben. Also Pr [K = 0] = 1/26, Pr [K = 1] = 1/26, und so weiter. Sample die gleichverteilte Variable K einmal, um einen bestimmten Schlüssel zu ergeben [^1].

[^2]: Wenn Sie an einer formaleren Ausführung zu diesen Themen interessiert sind, können Sie Katz und Lindells *Einführung in die moderne Kryptografie* konsultieren, insbesondere Kapitel 3 [^2].

# Mathematische Grundlagen der Kryptografie II
<partId>d7245cc9-bb6d-5403-b3d5-9c703d9a2f81</partId>

Dieses Kapitel behandelt ein fortgeschritteneres Thema zu den mathematischen Grundlagen der Kryptografie: Zahlentheorie. Obwohl die Zahlentheorie wichtig für die symmetrische Kryptografie ist (wie beim Rijndael Cipher), ist sie besonders wichtig im Kontext der Public-Key-Kryptografie.

Wenn Sie die Details der Zahlentheorie als mühsam empfinden, würde ich Ihnen empfehlen, beim ersten Mal eine hochrangige Lektüre vorzunehmen. Sie können jederzeit zu einem späteren Zeitpunkt darauf zurückkommen.

## Was ist Zahlentheorie?
<chapterId>c0051c34-fd5d-539c-93e2-5c6dfd4c3355</chapterId>

Man könnte die **Zahlentheorie** als die Untersuchung der Eigenschaften von Ganzzahlen und mathematischen Funktionen, die mit Ganzzahlen arbeiten, charakterisieren.

Betrachten Sie zum Beispiel, dass zwei Zahlen a und N **teilerfremd** (oder **relativ prim**) sind, wenn ihr größter gemeinsamer Teiler 1 beträgt. Nehmen wir nun eine bestimmte ganze Zahl N an. Wie viele Ganzzahlen, die kleiner als N sind, sind teilerfremd zu N? Können wir allgemeine Aussagen über die Antworten auf diese Frage machen? Dies sind die typischen Arten von Fragen, die die Zahlentheorie zu beantworten sucht.
Die moderne Zahlentheorie stützt sich auf die Werkzeuge der abstrakten Algebra. Das Gebiet der **abstrakten Algebra** ist eine Unterdisziplin der Mathematik, in der die Hauptanalyseobjekte abstrakte Objekte sind, die als algebraische Strukturen bekannt sind. Eine **algebraische Struktur** ist eine Menge von Elementen, die mit einer oder mehreren Operationen verbunden sind, welche bestimmte Axiome erfüllen. Durch algebraische Strukturen können Mathematiker Einblicke in spezifische mathematische Probleme gewinnen, indem sie von deren Details abstrahieren.
Das Gebiet der abstrakten Algebra wird manchmal auch als moderne Algebra bezeichnet. Sie könnten auch auf den Begriff **abstrakte Mathematik** (oder **reine Mathematik**) stoßen. Dieser letztere Begriff bezieht sich nicht auf abstrakte Algebra, sondern bedeutet das Studium der Mathematik um ihrer selbst willen und nicht nur mit Blick auf potenzielle Anwendungen.

Die Mengen aus der abstrakten Algebra können sich mit vielen Arten von Objekten befassen, von den formbewahrenden Transformationen an einem gleichseitigen Dreieck bis hin zu Tapetenmustern. Für die Zahlentheorie betrachten wir nur Mengen von Elementen, die ganze Zahlen enthalten oder Funktionen, die mit ganzen Zahlen arbeiten.

## Gruppen
<chapterId>3209b270-f9cd-5224-803e-0ed19fbf7826</chapterId>

Ein grundlegendes Konzept in der Mathematik ist das einer Menge von Elementen. Eine Menge wird üblicherweise durch geschweifte Klammern dargestellt, wobei die Elemente durch Kommas getrennt sind.

Beispielsweise ist die Menge aller ganzen Zahlen {…,-2,-1,0,1,2,…}. Die Ellipsen bedeuten hier, dass ein bestimmtes Muster in eine bestimmte Richtung fortgesetzt wird. So enthält die Menge aller ganzen Zahlen auch 3,4,5,6 und so weiter, sowie -3,-4,-5,-6 und so weiter. Diese Menge aller ganzen Zahlen wird typischerweise durch ℤ dargestellt.

Ein weiteres Beispiel für eine Menge ist ℤ mod 11, oder die Menge aller ganzen Zahlen modulo 11. Im Gegensatz zur gesamten Menge ℤ enthält diese Menge nur eine endliche Anzahl von Elementen, nämlich {0,1,…,9,10}.

Ein häufiger Fehler ist zu denken, dass die Menge ℤ mod 11 tatsächlich {-10,-9,….,0,….,9,10} ist. Aber das ist nicht der Fall, wenn man die Art und Weise betrachtet, wie wir die Modulo-Operation früher definiert haben. Alle negativen ganzen Zahlen, die durch Modulo 11 reduziert werden, wickeln sich auf {0,1,….,9,10} um. Beispielsweise wickelt sich der Ausdruck -2 mod 11 auf 9 um, während sich der Ausdruck -27 mod 11 auf 5 umwickelt.

Ein weiteres grundlegendes Konzept in der Mathematik ist das einer binären Operation. Dies ist jede Operation, die zwei Elemente nimmt, um ein drittes zu produzieren. Beispielsweise wären Sie aus der Grundrechenarten und Algebra mit vier grundlegenden binären Operationen vertraut: Addition, Subtraktion, Multiplikation und Division.

Diese beiden grundlegenden mathematischen Konzepte, Mengen und binäre Operationen, werden verwendet, um den Begriff einer Gruppe zu definieren, die wesentlichste Struktur in der abstrakten Algebra.

Speziell nehmen wir an, es gibt eine binäre Operation ◌. Zusätzlich nehmen wir an, es gibt eine Menge von Elementen **S**, die mit dieser Operation ausgestattet ist. „Ausgestattet“ bedeutet hier nur, dass die Operation ◌ zwischen beliebigen zwei Elementen in der Menge **S** durchgeführt werden kann.

Die Kombination 〈**S**, ◌〉 ist dann eine **Gruppe**, wenn sie vier spezifische Bedingungen erfüllt, die als Gruppenaxiome bekannt sind.

1. Für beliebige a und b, die Elemente von **S** sind, ist a ◌ b ebenfalls ein Element von **S**. Dies ist als die **Abgeschlossenheitsbedingung** bekannt.
2. Für beliebige a, b und c, die Elemente von **S** sind, gilt, dass (a ◌ b) ◌ c = a ◌ (b ◌ c). Dies wird als die **Assoziativitätsbedingung** bezeichnet. 3. Es gibt ein einzigartiges Element e in **S**, sodass für jedes Element a in **S** die folgende Gleichung gilt: e ◌ a = a ◌ e = a. Da es nur ein solches Element e gibt, wird es als das **neutrale Element** bezeichnet. Diese Bedingung ist bekannt als die **Neutralitätsbedingung**.
4. Für jedes Element a in **S** existiert ein Element b in **S**, sodass die folgende Gleichung gilt: a ◌ b = b ◌ a = e, wobei e das neutrale Element ist. Element b wird hier als das **inverse Element** bezeichnet und üblicherweise als a<sup>-1</sup> dargestellt. Diese Bedingung ist bekannt als die **Inversitätsbedingung** oder die **Umkehrbarkeitsbedingung**.

Lassen Sie uns Gruppen etwas weiter erforschen. Bezeichnen wir die Menge aller ganzen Zahlen mit ℤ. Diese Menge in Kombination mit der Standardaddition, oder 〈ℤ, +〉, erfüllt eindeutig die Definition einer Gruppe, da sie die vier oben genannten Axiome erfüllt.

1. Für beliebige x und y, die Elemente von ℤ sind, ist auch x + y ein Element von ℤ. Also erfüllt 〈ℤ, +〉 die Abgeschlossenheitsbedingung.
2. Für beliebige x, y und z, die Elemente von ℤ sind, gilt: (x + y) + z = x + (y + z). Also erfüllt 〈ℤ, +〉 die Assoziativitätsbedingung.
3. Es gibt ein neutrales Element in 〈ℤ, +〉, nämlich 0. Für jedes x in ℤ gilt nämlich: 0 + x = x + 0 = x. Also erfüllt 〈ℤ, +〉 die Neutralitätsbedingung.
4. Schließlich gibt es für jedes Element x in ℤ ein y, sodass x + y = y + x = 0. Wenn x beispielsweise 10 wäre, wäre y –10 (falls x 0 ist, ist y ebenfalls 0). Also erfüllt 〈ℤ, +〉 die Inversitätsbedingung.

Wichtig ist, dass die Menge der ganzen Zahlen mit Addition eine Gruppe bildet, was jedoch nicht bedeutet, dass sie auch mit Multiplikation eine Gruppe bildet. Sie können dies überprüfen, indem Sie 〈ℤ, •〉 gegen die vier Gruppenaxiome testen (wobei • die Standardmultiplikation bedeutet).

Die ersten beiden Axiome gelten offensichtlich. Darüber hinaus kann unter der Multiplikation das Element 1 als neutrales Element dienen. Jede ganze Zahl x multipliziert mit 1 ergibt nämlich x. Allerdings erfüllt 〈ℤ, •〉 nicht die Inversitätsbedingung. Das heißt, es gibt kein einzigartiges Element y in ℤ für jedes x in ℤ, sodass x • y = 1.

Nehmen wir an, x = 22. Welcher Wert y aus der Menge ℤ multipliziert mit x würde das neutrale Element 1 ergeben? Der Wert 1/22 würde funktionieren, aber dieser ist nicht in der Menge ℤ enthalten. Tatsächlich stößt man bei jedem ganzen Wert x, außer bei den Werten 1 und -1 (wo y 1 bzw. -1 sein müsste), auf dieses Problem.
Wenn wir reelle Zahlen für unsere Menge zulassen würden, dann würden unsere Probleme größtenteils verschwinden. Für jedes Element x in der Menge führt die Multiplikation mit 1/x zu 1. Da Brüche in der Menge der reellen Zahlen enthalten sind, kann für jede reelle Zahl ein Inverses gefunden werden. Die Ausnahme ist die Null, da jede Multiplikation mit Null niemals das Identitätselement 1 ergibt. Daher ist die Menge der von Null verschiedenen reellen Zahlen, ausgestattet mit der Multiplikation, tatsächlich eine Gruppe.

Einige Gruppen erfüllen eine fünfte allgemeine Bedingung, bekannt als die **Kommutativitätsbedingung**. Diese Bedingung lautet wie folgt:

* Nehmen wir eine Gruppe G mit einer Menge **S** und einem binären Operator ◌ an. Nehmen wir an, dass a und b Elemente von **S** sind. Wenn gilt, dass a ◌ b = b ◌ a für beliebige zwei Elemente a und b in **S**, dann erfüllt G die Kommutativitätsbedingung.

Jede Gruppe, die die Kommutativitätsbedingung erfüllt, ist als **kommutative Gruppe** oder **abelsche Gruppe** (nach Niels Henrik Abel) bekannt. Es ist leicht zu überprüfen, dass sowohl die Menge der reellen Zahlen über Addition als auch die Menge der ganzen Zahlen über Addition abelsche Gruppen sind. Die Menge der ganzen Zahlen über Multiplikation ist überhaupt keine Gruppe, kann also de facto keine abelsche Gruppe sein. Die Menge der von Null verschiedenen reellen Zahlen über Multiplikation ist hingegen ebenfalls eine abelsche Gruppe.

Zwei wichtige Konventionen zur Notation sollten beachtet werden. Erstens werden die Zeichen “+” oder “x” häufig verwendet, um Gruppenoperationen zu symbolisieren, auch wenn die Elemente tatsächlich keine Zahlen sind. In diesen Fällen sollten Sie diese Zeichen nicht als standardmäßige arithmetische Addition oder Multiplikation interpretieren. Stattdessen handelt es sich um Operationen, die nur eine abstrakte Ähnlichkeit mit diesen arithmetischen Operationen haben.

Sofern Sie sich nicht speziell auf arithmetische Addition oder Multiplikation beziehen, ist es einfacher, Symbole wie ◌ und ◊ für Gruppenoperationen zu verwenden, da diese keine kulturell tief verwurzelten Konnotationen haben.

Zweitens, aus demselben Grund, warum “+” und “x” oft verwendet werden, um nicht-arithmetische Operationen anzuzeigen, werden die Identitätselemente von Gruppen häufig durch “0” und “1” symbolisiert, auch wenn die Elemente in diesen Gruppen keine Zahlen sind. Sofern Sie sich nicht auf das Identitätselement einer Gruppe mit Zahlen beziehen, ist es einfacher, ein neutraleres Symbol wie “e” zu verwenden, um das Identitätselement anzugeben.

Viele verschiedene und sehr wichtige Mengen von Werten in der Mathematik, ausgestattet mit bestimmten binären Operationen, sind Gruppen. Kryptographische Anwendungen arbeiten jedoch nur mit Mengen von ganzen Zahlen oder zumindest Elementen, die durch ganze Zahlen beschrieben werden, das heißt, im Bereich der Zahlentheorie. Daher werden Mengen mit reellen Zahlen außer ganzen Zahlen in kryptographischen Anwendungen nicht verwendet.

Lassen Sie uns abschließend ein Beispiel für Elemente geben, die „durch ganze Zahlen beschrieben werden können“, obwohl sie keine ganzen Zahlen sind. Ein gutes Beispiel sind die Punkte auf elliptischen Kurven. Obwohl ein Punkt auf einer elliptischen Kurve klar keine ganze Zahl ist, wird ein solcher Punkt tatsächlich durch zwei ganze Zahlen beschrieben.

Elliptische Kurven sind beispielsweise entscheidend für Bitcoin. Jedes Standard-Bitcoin-Private- und Public-Key-Paar wird aus der Menge von Punkten ausgewählt, die durch die folgende elliptische Kurve definiert ist: x<sup>3</sup> + 7 = y<sup>2</sup> mod 2<sup>256</sup> – 232 – 29 – 28 – 27 – 26 - 24 - 1 (die größte Primzahl kleiner als 2<sup>256</sup>). Die x-Koordinate ist der private Schlüssel und die y-Koordinate ist Ihr öffentlicher Schlüssel.
Transaktionen in Bitcoin beinhalten typischerweise das Sperren von Ausgaben für einen oder mehrere öffentliche Schlüssel auf irgendeine Weise. Der Wert aus diesen Transaktionen kann dann durch die Erstellung digitaler Signaturen mit den entsprechenden privaten Schlüsseln entsperrt werden.

## Zyklische Gruppen
<chapterId>bfa5c714-7952-5fef-88b1-ca5b07edd886</chapterId>

Ein wichtiger Unterschied, den wir machen können, ist zwischen einer **endlichen** und einer **unendlichen Gruppe**. Erstere hat eine endliche Anzahl von Elementen, während letztere eine unendliche Anzahl von Elementen hat. Die Anzahl der Elemente in jeder endlichen Gruppe ist als die **Ordnung der Gruppe** bekannt. Alle praktischen Kryptographien, die die Verwendung von Gruppen beinhalten, stützen sich auf endliche (zahlentheoretische) Gruppen.

Innerhalb der Public-Key-Kryptographie ist eine bestimmte Klasse von endlichen abelschen Gruppen, bekannt als zyklische Gruppen, besonders wichtig. Um zyklische Gruppen zu verstehen, müssen wir zuerst das Konzept der Exponentiation von Gruppenelementen verstehen.

Nehmen wir an, eine Gruppe G mit einer Gruppenoperation ◌, und dass a ein Element von G ist. Der Ausdruck a<sup>n</sup> sollte dann als das Element a interpretiert werden, das insgesamt n – 1 Mal mit sich selbst kombiniert wird. Zum Beispiel bedeutet a<sup>2</sup> a ◌ a, a<sup>3</sup> bedeutet a ◌ a ◌ a, und so weiter. (Beachten Sie, dass die Exponentiation hier nicht notwendigerweise Exponentiation im standardmäßigen arithmetischen Sinne ist.)

Wenden wir uns einem Beispiel zu. Nehmen wir an, dass G = 〈ℤ mod 7,+〉 ist, und dass unser Wert für a gleich 4 ist. In diesem Fall wäre a<sup>2</sup> = [4 + 4 mod 7] = [8 mod 7] = 1 mod 7. Alternativ würde a<sup>4</sup> darstellen [4 + 4 + 4 + 4 mod 7] = [16 mod 7] = 2 mod 7.

Einige abelsche Gruppen haben ein oder mehrere Elemente, die durch fortgesetzte Exponentiation alle anderen Gruppenelemente erzeugen können. Diese Elemente werden **Generatoren** oder **primitive Elemente** genannt.

Eine wichtige Klasse solcher Gruppen ist 〈ℤ* mod N, •〉, wobei N eine Primzahl ist. Die Notation ℤ* bedeutet hier, dass die Gruppe alle nicht-null, positiven Ganzzahlen kleiner als N enthält. Eine solche Gruppe hat daher immer N – 1 Elemente.

Betrachten wir zum Beispiel G = 〈ℤ* mod 11, •〉. Diese Gruppe hat die folgenden Elemente: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}. Die Ordnung dieser Gruppe ist 10 (was tatsächlich gleich 11 – 1 ist).

Lassen Sie uns das Exponentieren des Elements 2 aus dieser Gruppe erkunden. Die Berechnungen bis zu 2<sup>12</sup> werden unten gezeigt. Beachten Sie, dass auf der linken Seite der Gleichung der Exponent auf die Exponentiation von Gruppenelementen verweist. In unserem speziellen Beispiel beinhaltet dies tatsächlich arithmetische Exponentiation auf der rechten Seite der Gleichung (es hätte aber auch zum Beispiel Addition beinhalten können). Zur Klarstellung habe ich die wiederholte Operation ausgeschrieben, anstatt die Exponentenform auf der rechten Seite.

* 2<sup>1</sup> = 2 mod 11
* 2<sup>2</sup> = 2 · 2 mod 11 = 4 mod 11
* 2<sup>3</sup> = 2 · 2 · 2 mod 11 = 8 mod 11
* 2<sup>4</sup> = 2 · 2 · 2 · 2 mod 11 = 16 mod 11 = 5 mod 11
* 2<sup>5</sup> = 2 · 2 · 2 · 2 · 2 mod 11 = 32 mod 11 = 10 mod 11
* 2<sup>6</sup> = 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 64 mod 11 = 9 mod 11
* 2<sup>7</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 128 mod 11 = 7 mod 11
* 2<sup>8</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 256 mod 11 = 3 mod 11
* 2<sup>9</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 512 mod 11 = 6 mod 11
* 2<sup>10</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 1024 mod 11 = 1 mod 11
* 2<sup>11</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 2048 mod 11 = 2 mod 11
* 2<sup>12</sup> = 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 · 2 mod 11 = 4096 mod 11 = 4 mod 11

Wenn Sie genau hinsehen, können Sie erkennen, dass die Potenzierung des Elements 2 durch alle Elemente von 〈ℤ* mod 11, •〉 in folgender Reihenfolge zyklisch verläuft: 2, 4, 8, 5, 10, 9, 7, 3, 6, 1. Nach 2<sup>10</sup> zyklisiert die fortgesetzte Potenzierung des Elements 2 erneut durch alle Elemente und in derselben Reihenfolge. Daher ist das Element 2 ein Generator in 〈ℤ* mod 11, •〉.

Obwohl 〈ℤ* mod 11, •〉 mehrere Generatoren hat, sind nicht alle Elemente dieser Gruppe Generatoren. Betrachten Sie zum Beispiel das Element 3. Die Durchführung der ersten 10 Potenzierungen, ohne die umständlichen Berechnungen zu zeigen, ergibt folgende Ergebnisse:

* 3<sup>1</sup> = 3 mod 11
* 3<sup>2</sup> = 9 mod 11
* 3<sup>3</sup> = 5 mod 11
* 3<sup>4</sup> = 4 mod 11
* 3<sup>5</sup> = 1 mod 11
* 3<sup>6</sup> = 3 mod 11
* 3<sup>7</sup> = 9 mod 11
* 3<sup>8</sup> = 5 mod 11
* 3<sup>9</sup> = 4 mod 11
* 3<sup>10</sup> = 1 mod 11

Anstatt alle Werte in 〈ℤ* mod 11, •〉 zu durchlaufen, führt die Exponentiation des Elements 3 nur zu einer Teilmenge dieser Werte: 3, 9, 5, 4 und 1. Nach der fünften Exponentiation beginnen diese Werte sich zu wiederholen.

Wir können nun eine **zyklische Gruppe** als jede Gruppe definieren, die mindestens einen Generator hat. Das heißt, es gibt mindestens ein Gruppenelement, aus dem man durch Exponentiation alle anderen Gruppenelemente erzeugen kann.

Vielleicht ist Ihnen in unserem Beispiel oben aufgefallen, dass sowohl 2<sup>10</sup> als auch 3<sup>10</sup> gleich 1 mod 11 sind. Tatsächlich, obwohl wir die Berechnungen nicht durchführen werden, führt die Exponentiation durch 10 jedes Elements in der Gruppe 〈ℤ* mod 11, •〉 zu 1 mod 11. Warum ist das so?

Dies ist eine wichtige Frage, aber es bedarf einiger Arbeit, um sie zu beantworten.

Beginnen wir mit der Annahme von zwei positiven Ganzzahlen a und N. Ein wichtiges Theorem in der Zahlentheorie besagt, dass a ein multiplikatives Inverses modulo N hat (das heißt, eine ganze Zahl b, so dass a • b = 1 mod N), wenn und nur wenn der größte gemeinsame Teiler zwischen a und N gleich 1 ist. Das heißt, wenn a und N teilerfremd sind.

Also sind in jeder Gruppe von Ganzzahlen, die mit der Multiplikation modulo N ausgestattet ist, nur die kleineren Teilerfremden mit N in der Menge enthalten. Wir können diese Menge mit ℤ<sup>c</sup> mod N bezeichnen.

Nehmen wir zum Beispiel an, dass N 10 ist. Nur die Ganzzahlen 1, 3, 7 und 9 sind teilerfremd zu 10. Also enthält die Menge ℤ<sup>c</sup> mod 10 nur {1, 3, 7, 9}. Man kann keine Gruppe mit Ganzzahlmultiplikation modulo 10 unter Verwendung anderer Ganzzahlen zwischen 1 und 10 bilden. Für diese spezielle Gruppe sind die Inversen die Paare 1 und 9 sowie 3 und 7.

Im Fall, dass N selbst eine Primzahl ist, sind alle Ganzzahlen von 1 bis N – 1 teilerfremd zu N. Eine solche Gruppe hat daher eine Ordnung von N – 1. Unter Verwendung unserer früheren Notation entspricht ℤ<sup>c</sup> mod N gleich ℤ* mod N, wenn N eine Primzahl ist. Die Gruppe, die wir für unser früheres Beispiel ausgewählt haben, 〈ℤ* mod 11, •〉, ist ein spezielles Beispiel dieser Klasse von Gruppen.

Als Nächstes berechnet die Funktion φ(N) die Anzahl der Teilerfremden bis zu einer Zahl N und ist als **Eulersche Phi-Funktion** bekannt.<sup>[1](#footnote1)</sup> Gemäß **Eulers Theorem** gilt, wann immer zwei Ganzzahlen a und N teilerfremd sind, folgendes:

* a<sup>φ(N)</sup> mod N = 1 mod N
Dies hat eine wichtige Implikation für die Klasse der Gruppen 〈ℤ* mod N, •〉, wobei N eine Primzahl ist. Für diese Gruppen stellt die Exponentiation von Gruppenelementen die arithmetische Exponentiation dar. Das heißt, a<sup>φ(N)</sup> mod N repräsentiert die arithmetische Operation a<sup>φ(N)</sup> mod N. Da jedes Element a in diesen multiplikativen Gruppen teilerfremd mit N ist, bedeutet dies, dass a<sup>φ(N)</sup> mod N = a<sup>N – 1</sup> mod N = 1 mod N.

Der Satz von Euler ist ein wirklich wichtiges Ergebnis. Zunächst impliziert er, dass alle Elemente in 〈ℤ* mod N, •〉 nur durch eine Anzahl von Werten durch Exponentiation zyklisch verlaufen können, die in N – 1 teilt. Im Fall von 〈ℤ* mod 11, •〉 bedeutet dies, dass jedes Element nur durch 2, 5 oder 10 Elemente zyklisch verlaufen kann. Die Gruppenwerte, durch die jedes Element bei der Exponentiation zyklisch verläuft, sind als die **Ordnung des Elements** bekannt. Ein Element mit einer Ordnung, die der Ordnung einer Gruppe entspricht, ist ein Generator.

Darüber hinaus impliziert der Satz von Euler, dass wir immer das Ergebnis von a<sup>N – 1</sup> mod N für jede Gruppe 〈ℤ* mod N, •〉 kennen können, wobei N eine Primzahl ist. Dies gilt unabhängig davon, wie kompliziert die tatsächlichen Berechnungen sein mögen.

Nehmen wir zum Beispiel an, unsere Gruppe ist ℤ* mod 160,481,182 (wo 160,481,182 tatsächlich eine Primzahl ist). Wir wissen, dass alle ganzen Zahlen von 1 bis 160,481,181 Elemente dieser Gruppe sein müssen, und dass φ(n) = 160,481,181. Obwohl wir nicht alle Schritte in den Berechnungen durchführen können, wissen wir, dass Ausdrücke wie 514<sup>160,481,181</sup>, 2,005<sup>160,481,181</sup> und 256,212<sup>160,481,181</sup> alle zu 1 mod 160,481,182 auswerten müssen.

## Felder
<chapterId>fad52d86-3a22-5c9f-979e-3bec9eaa008e</chapterId>

Eine Gruppe ist die grundlegende algebraische Struktur in der abstrakten Algebra, aber es gibt noch viele mehr. Die einzige andere algebraische Struktur, mit der Sie vertraut sein müssen, ist die eines Feldes, speziell die eines endlichen Feldes. Diese Art von algebraischer Struktur wird häufig in der Kryptographie verwendet, wie zum Beispiel im Advanced Encryption Standard. Letzterer ist das Hauptverfahren der symmetrischen Verschlüsselung, auf das Sie in der Praxis stoßen werden.

Ein Feld leitet sich aus der Vorstellung einer Gruppe ab. Speziell ist ein **Feld** eine Menge von Elementen **S** ausgestattet mit zwei binären Operatoren ◌ und ◊, die die folgenden Bedingungen erfüllen:

1. Die Menge **S** ausgestattet mit ◌ ist eine Abelsche Gruppe.
2. Die Menge **S** ausgestattet mit ◊ ist eine Abelsche Gruppe für die „nicht-null“ Elemente.
3. Die Menge **S** ausgestattet mit den beiden Operatoren erfüllt die sogenannte distributive Bedingung: Angenommen, a, b und c sind Elemente von **S**. Dann erfüllt **S** ausgestattet mit den beiden Operatoren die distributive Eigenschaft, wenn a ◌ (b ◊ c) = a ◌ b ◊ a ◌ c.
Beachten Sie, dass die Definition eines Feldes, ähnlich wie bei Gruppen, sehr abstrakt ist. Es werden keine Aussagen über die Arten von Elementen in **S** oder über die Operationen ◌ und ◊ gemacht. Es wird lediglich festgestellt, dass ein Feld jede Menge von Elementen mit zwei Operationen ist, für die die drei oben genannten Bedingungen gelten. (Das "Null"-Element in der zweiten abelschen Gruppe kann abstrakt interpretiert werden.)
Was könnte also ein Beispiel für ein Feld sein? Ein gutes Beispiel ist die Menge ℤ mod 7, oder {0,1,…,7}, definiert über die Standardaddition (anstelle von ◌ oben) und die Standardmultiplikation (anstelle von ◊ oben).

Erstens erfüllt ℤ mod 7 die Bedingung, eine abelsche Gruppe über Addition zu sein, und es erfüllt die Bedingung, eine abelsche Gruppe über Multiplikation zu sein, wenn man nur die Nicht-Null-Elemente betrachtet. Zweitens erfüllt die Kombination der Menge mit den zwei Operatoren die distributive Bedingung.

Es ist didaktisch wertvoll, diese Behauptungen zu erkunden, indem man einige spezielle Werte verwendet. Nehmen wir die experimentellen Werte 5, 2 und 3, einige zufällig ausgewählte Elemente aus der Menge ℤ mod 7, um das Feld 〈ℤ mod 7, +, •〉 zu untersuchen. Wir werden diese drei Werte in der Reihenfolge verwenden, wie sie benötigt werden, um bestimmte Bedingungen zu erkunden.

Lassen Sie uns zuerst erkunden, ob ℤ mod 7 ausgestattet mit Addition eine abelsche Gruppe ist.

1. Abgeschlossenheitsbedingung: Nehmen wir 5 und 2 als unsere Werte. In diesem Fall ist [5 + 2] mod 7 = 7 mod 7 = 0. Dies ist tatsächlich ein Element von ℤ mod 7, also ist das Ergebnis konsistent mit der Abgeschlossenheitsbedingung.
2. Assoziativitätsbedingung: Nehmen wir 5, 2 und 3 als unsere Werte. In diesem Fall ist [(5 + 2) + 3] mod 7 = [5 + (2 + 3)] mod 7 = 10 mod 7 = 3. Dies ist konsistent mit der Assoziativitätsbedingung.
3. Identitätsbedingung: Nehmen wir 5 als unseren Wert. In diesem Fall ist [5 + 0] mod 7 = [0 + 5] mod 7 = 5. Also scheint 0 das Identitätselement für die Addition zu sein.
4. Inversitätsbedingung: Betrachten wir das Inverse von 5. Es muss gelten, dass [5 + d] mod 7 = 0, für einen bestimmten Wert von d. In diesem Fall ist der einzigartige Wert aus ℤ mod 7, der diese Bedingung erfüllt, 2.
5. Kommutativitätsbedingung: Nehmen wir 5 und 3 als unsere Werte. In diesem Fall ist [5 + 3] mod 7 = [3 + 5] mod 7 = 1. Dies ist konsistent mit der Kommutativitätsbedingung.

Die Menge ℤ mod 7 ausgestattet mit Addition erscheint eindeutig als eine abelsche Gruppe. Lassen Sie uns nun erkunden, ob ℤ mod 7 ausgestattet mit Multiplikation eine abelsche Gruppe für alle Nicht-Null-Elemente ist.

1. Abgeschlossenheitsbedingung: Nehmen wir 5 und 2 als unsere Werte. In diesem Fall ist [5 • 2] mod 7 = 10 mod 7 = 3. Dies ist ebenfalls ein Element von ℤ mod 7, also ist das Ergebnis konsistent mit der Abgeschlossenheitsbedingung.
2. Assoziativgesetz: Nehmen wir 5, 2 und 3 als unsere Werte. In diesem Fall ist [(5 • 2) • 3] mod 7 = [5 • (2 • 3)] mod 7 = 30 mod 7 = 2. Dies ist konsistent mit dem Assoziativgesetz.
3. Identitätsgesetz: Nehmen wir 5 als unseren Wert. In diesem Fall ist [5 • 1] mod 7 = [1 • 5] mod 7 = 5. Also scheint 1 das Identitätselement für die Multiplikation zu sein.
4. Inverses Gesetz: Betrachten wir das Inverse von 5. Es muss gelten, dass [5 • d] mod 7 = 1, für einen bestimmten Wert von d. Der einzigartige Wert aus ℤ mod 7, der diese Bedingung erfüllt, ist 3. Dies ist konsistent mit dem inversen Gesetz.
5. Kommutativgesetz: Nehmen wir 5 und 3 als unsere Werte. In diesem Fall ist [5 • 3] mod 7 = [3 • 5] mod 7 = 15 mod 7 = 1. Dies ist konsistent mit dem Kommutativgesetz.

Die Menge ℤ mod 7 scheint offensichtlich die Regeln für eine abelsche Gruppe zu erfüllen, wenn sie mit entweder Addition oder Multiplikation über den Nicht-Null-Elementen verbunden wird.

Schließlich scheint diese Menge in Kombination mit beiden Operatoren die distributive Bedingung zu erfüllen. Nehmen wir 5, 2 und 3 als unsere Werte. Wir können sehen, dass [5 • (2 + 3)] mod 7 = [5 • 2 + 5 • 3] mod 7 = 25 mod 7 = 4.

Wir haben nun gesehen, dass ℤ mod 7 ausgestattet mit Addition und Multiplikation die Axiome für ein endliches Feld erfüllt, wenn es mit bestimmten Werten getestet wird. Natürlich können wir das auch allgemein zeigen, werden dies hier aber nicht tun.

Ein Schlüsselunterschied besteht zwischen zwei Arten von Feldern: endliche und unendliche Felder.

Ein **unendliches Feld** beinhaltet ein Feld, bei dem die Menge **S** unendlich groß ist. Die Menge der reellen Zahlen ℝ ausgestattet mit Addition und Multiplikation ist ein Beispiel für ein unendliches Feld. Ein **endliches Feld**, auch bekannt als **Galois-Feld**, ist ein Feld, bei dem die Menge **S** endlich ist. Unser obiges Beispiel von 〈ℤ mod 7, +, •〉 ist ein endliches Feld.

In der Kryptographie sind wir hauptsächlich an endlichen Feldern interessiert. Allgemein kann gezeigt werden, dass ein endliches Feld für eine Menge von Elementen **S** existiert, wenn und nur wenn es p<sup>m</sup> Elemente hat, wobei p eine Primzahl und m eine positive ganze Zahl größer oder gleich eins ist. Mit anderen Worten, wenn die Ordnung einer Menge **S** eine Primzahl (p<sup>m</sup> wo m = 1) oder eine Primzahlpotenz (p<sup>m</sup> wo m > 1) ist, dann können Sie zwei Operatoren ◌ und ◊ finden, sodass die Bedingungen für ein Feld erfüllt sind.

Wenn ein endliches Feld eine Primzahl von Elementen hat, dann wird es als **Primfeld** bezeichnet. Wenn die Anzahl der Elemente im endlichen Feld eine Primzahlpotenz ist, dann wird das Feld als **Erweiterungsfeld** bezeichnet. In der Kryptographie sind wir an beiden, Prim- und Erweiterungsfeldern, interessiert.<sup>[2](#footnote2)</sup>
Die Hauptinteressensgebiete in der Kryptographie sind jene, bei denen die Menge aller ganzen Zahlen durch eine Primzahl moduliert wird und die Operatoren die Standardaddition und -multiplikation sind. Diese Klasse von endlichen Feldern würde ℤ mod 2, ℤ mod 3, ℤ mod 5, ℤ mod 7, ℤ mod 11, ℤ mod 13 und so weiter umfassen. Für jedes Primfeld ℤ mod p ist die Menge der Zahlen des Feldes wie folgt: {0,1,….,p – 2, p – 1}.
In der Kryptographie interessieren wir uns auch für Erweiterungsfelder, insbesondere für alle Felder mit 2<sup>m</sup> Elementen, wobei m > 1 ist. Solche endlichen Felder werden beispielsweise im Rijndael Cipher verwendet, der die Grundlage des Advanced Encryption Standard bildet. Während Primfelder relativ intuitiv sind, sind diese Basis-2-Erweiterungsfelder wahrscheinlich nicht für jemanden verständlich, der mit abstrakter Algebra nicht vertraut ist.

Zunächst ist es tatsächlich wahr, dass jeder Menge von ganzen Zahlen mit 2<sup>m</sup> Elementen zwei Operatoren zugewiesen werden können, die ihre Kombination zu einem Feld machen (solange m eine positive ganze Zahl ist). Doch nur weil ein Feld existiert, bedeutet das nicht unbedingt, dass es leicht zu entdecken oder für bestimmte Anwendungen besonders praktisch ist.

Es stellt sich heraus, dass insbesondere anwendbare Erweiterungsfelder von 2<sup>m</sup> in der Kryptographie jene sind, die über bestimmte Mengen von Polynomausdrücken definiert sind, anstatt über irgendeine Menge von ganzen Zahlen.

Nehmen wir zum Beispiel an, wir wollten ein Erweiterungsfeld mit 2<sup>3</sup> (d.h., 8) Elementen in der Menge. Obwohl es viele verschiedene Mengen geben könnte, die für Felder dieser Größe verwendet werden können, umfasst eine solche Menge alle einzigartigen Polynome der Form a<sub>2</sub>x<sup>2</sup> + a<sub>1</sub>x + a<sub>0</sub>, wobei jeder Koeffizient a<sub>i</sub> entweder 0 oder 1 ist. Daher umfasst diese Menge **S** die folgenden Elemente:

1. 0: Der Fall, bei dem a<sub>2</sub> = 0, a<sub>1</sub> = 0 und a<sub>0</sub> = 0 ist.
2. 1: Der Fall, bei dem a<sub>2</sub> = 0, a<sub>1</sub> = 0 und a<sub>0</sub> = 1 ist.
3. x: Der Fall, bei dem a<sub>2</sub> = 0, a<sub>1</sub> = 1 und a<sub>0</sub> = 0 ist.
4. x + 1: Der Fall, bei dem a<sub>2</sub> = 0, a<sub>1</sub> = 1 und a<sub>0</sub> = 1 ist.
5. x<sup>2</sup>: Der Fall, bei dem a<sub>2</sub>= 1, a<sub>1</sub> = 0 und a<sub>0</sub> = 0 ist.
6. x<sup>2</sup> + 1: Der Fall, bei dem a<sub>2</sub> = 1, a<sub>1</sub> = 0 und a<sub>0</sub> = 1 ist.
7. \(x^2 + x\): Der Fall, bei dem \(a_2 = 1\), \(a_1 = 1\) und \(a_0 = 0\). 8. \(x^2 + x + 1\): Der Fall, bei dem \(a_2 = 1\), \(a_1 = 1\) und \(a_0 = 1\).

Also wäre **S** die Menge \(\{0,1,x,x + 1, x^2,x^2 + 1, x^2 + x, x^2 + x + 1\}\). Welche zwei Operationen können über dieser Menge von Elementen definiert werden, um sicherzustellen, dass ihre Kombination ein Feld ist?

Die erste Operation auf der Menge S (◌) kann als Standardpolynomaddition modulo 2 definiert werden. Alles, was Sie tun müssen, ist, die Polynome wie gewohnt zu addieren und dann das Modulo 2 auf jeden der Koeffizienten des resultierenden Polynoms anzuwenden. Hier sind einige Beispiele:

* \([(x^2) + (x^2 + x + 1)] \mod 2 = [2x^2 + x + 1] \mod 2 = x + 1\)
* \([(x^2 + x) + (x)] \mod 2 = [x^2 + 2x] \mod 2 = x^2\)
* \([(x + 1) + (x^2 + x + 1)] \mod 2 = [x^2 + 2x + 2] \mod 2 = x^2 + 1\)

Die zweite Operation auf der Menge S (◌), die für die Erstellung des Feldes benötigt wird, ist komplizierter. Es handelt sich um eine Art der Multiplikation, aber nicht um die Standardmultiplikation aus der Arithmetik. Stattdessen müssen Sie jedes Element als Vektor betrachten und die Operation als die Multiplikation dieser beiden Vektoren modulo eines irreduziblen Polynoms verstehen.

Wenden wir uns zunächst der Idee eines irreduziblen Polynoms zu. Ein **irreduzibles Polynom** ist eines, das nicht faktorisiert werden kann (genauso wie eine Primzahl nicht in Komponenten außer 1 und der Primzahl selbst faktorisiert werden kann). Für unsere Zwecke interessieren wir uns für Polynome, die in Bezug auf die Menge aller ganzen Zahlen irreduzibel sind. (Beachten Sie, dass Sie bestimmte Polynome möglicherweise faktorisieren können, zum Beispiel durch die reellen oder komplexen Zahlen, auch wenn Sie sie nicht mit ganzen Zahlen faktorisieren können.)

Betrachten Sie zum Beispiel das Polynom \(x^2 - 3x + 2\). Dies kann als \((x – 1)(x – 2)\) umgeschrieben werden. Daher ist dies nicht irreduzibel. Betrachten Sie nun das Polynom \(x^2 + 1\). Unter Verwendung von nur ganzen Zahlen gibt es keine Möglichkeit, diesen Ausdruck weiter zu faktorisieren. Daher ist dies ein irreduzibles Polynom in Bezug auf die ganzen Zahlen.
Als Nächstes wenden wir uns dem Konzept der Vektormultiplikation zu. Wir werden dieses Thema nicht in die Tiefe erforschen, Sie müssen nur eine grundlegende Regel verstehen: Eine Vektordivision kann stattfinden, solange der Dividend einen höheren oder gleich hohen Grad wie der Divisor hat. Hat der Dividend einen niedrigeren Grad als der Divisor, dann kann der Dividend nicht mehr durch den Divisor geteilt werden.  
Betrachten Sie zum Beispiel den Ausdruck x<sup>6</sup> + x + 1 mod x<sup>5</sup> + x<sup>2</sup>. Dies reduziert sich weiter, da der Grad des Dividenden, 6, höher ist als der Grad des Divisors, 5. Betrachten Sie nun den Ausdruck x<sup>5</sup> + x + 1 mod x<sup>5</sup> + x<sup>2</sup>. Dies reduziert sich ebenfalls weiter, da der Grad des Dividenden, 5, und des Divisors, 5, gleich sind.

Betrachten Sie jedoch jetzt den Ausdruck x<sup>4</sup> + x + 1 mod x<sup>5</sup> + x<sup>2</sup>. Dies reduziert sich nicht weiter, da der Grad des Dividenden, 4, niedriger ist als der Grad des Divisors, 5.

Auf der Grundlage dieser Informationen sind wir jetzt bereit, unsere zweite Operation für die Menge {0,1,x,x + 1,x<sup>2</sup>,x<sup>2</sup> + 1,x<sup>2</sup> + x,x<sup>2</sup> + x + 1} zu finden.

Ich habe bereits gesagt, dass die zweite Operation als Vektormultiplikation modulo eines irreduziblen Polynoms verstanden werden sollte. Dieses irreduzible Polynom sollte sicherstellen, dass die zweite Operation eine abelsche Gruppe über **S** definiert und mit der distributiven Bedingung konsistent ist. Welches sollte also dieses irreduzible Polynom sein?

Da alle Vektoren in der Menge einen Grad von 2 oder niedriger haben, sollte das irreduzible Polynom einen Grad von 3 haben. Wenn eine Multiplikation von zwei Vektoren in der Menge ein Polynom vom Grad 3 oder höher ergibt, wissen wir, dass modulo eines Polynoms vom Grad 3 immer ein Polynom vom Grad 2 oder niedriger ergibt. Dies ist der Fall, weil jedes Polynom vom Grad 3 oder höher immer durch ein Polynom vom Grad 3 teilbar ist. Zusätzlich muss das Polynom, das als Divisor fungiert, irreduzibel sein.

Es stellt sich heraus, dass es mehrere irreduzible Polynome vom Grad 3 gibt, die wir als unseren Divisor verwenden könnten. Jedes dieser Polynome definiert in Verbindung mit unserer Menge S und Addition modulo 2 ein unterschiedliches Feld. Das bedeutet, Sie haben mehrere Optionen, wenn Sie Erweiterungsfelder 2<sup>m</sup> in der Kryptographie verwenden.

Für unser Beispiel nehmen wir an, dass wir das Polynom x<sup>3</sup> + x + 1 wählen. Dies ist tatsächlich irreduzibel, weil es sich nicht mit ganzen Zahlen faktorisieren lässt. Zusätzlich wird es sicherstellen, dass jede Multiplikation von zwei Elementen ein Polynom vom Grad 2 oder weniger ergibt.
Lassen Sie uns anhand eines Beispiels der zweiten Operation durchgehen, wobei das Polynom x<sup>3</sup> + x + 1 als Divisor verwendet wird, um zu veranschaulichen, wie es funktioniert. Nehmen wir an, Sie multiplizieren die Elemente x<sup>2</sup> + 1 mit x<sup>2</sup> + x in unserer Menge **S**. Wir müssen dann den Ausdruck [(x<sup>2</sup> + 1) • (x<sup>2</sup> + x)] mod x<sup>3</sup> + x + 1 berechnen. Dies kann wie folgt vereinfacht werden:
* [(x<sup>2</sup> + 1) • (x<sup>2</sup> + x)] mod x<sup>3</sup> + x + 1 =
* [x<sup>2</sup> • x<sup>2</sup> + x<sup>2</sup> • x + 1 • x<sup>2</sup> + 1 • x] mod x<sup>3</sup> + x + 1 = 
* [x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x] mod x<sup>3</sup> + x + 1
    
Wir wissen, dass [x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x] mod x<sup>3</sup> + x + 1 reduziert werden kann, da der Dividend einen höheren Grad (4) als der Divisor (3) hat.

Zum Start können Sie sehen, dass der Ausdruck x<sup>3</sup> + x + 1 insgesamt x Mal in x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x geht. Sie können dies überprüfen, indem Sie x<sup>3</sup> + x + 1 mit x multiplizieren, was x<sup>4</sup> + x<sup>2</sup> + x ergibt. Da der letztere Term denselben Grad wie der Dividend hat, nämlich 4, wissen wir, dass dies funktioniert. Sie können den Rest dieser Division durch x wie folgt berechnen:

* [(x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x) – (x<sup>4</sup> + x<sup>2</sup> + x)] mod x<sup>3</sup> + x + 1 = 
* [x<sup>3</sup>] mod x<sup>3</sup> + x + 1 =
* x<sup>3</sup>

Also, nachdem x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x insgesamt x Mal durch x<sup>3</sup> + x + 1 geteilt wurde, haben wir einen Rest von x<sup>3</sup>. Kann dies weiter durch x<sup>3</sup> + x + 1 geteilt werden?
Intuitiv mag es ansprechend erscheinen zu sagen, dass x<sup>3</sup> nicht länger durch x<sup>3</sup> + x + 1 geteilt werden kann, weil der letztere Term größer zu sein scheint. Jedoch erinnern Sie sich an unsere Diskussion über die Vektordivision zuvor. Solange der Dividend einen Grad hat, der größer oder gleich dem des Divisors ist, kann der Ausdruck weiter reduziert werden. Speziell kann der Ausdruck x<sup>3</sup> + x + 1 genau 1 Mal in x<sup>3</sup> eingehen. Der Rest wird wie folgt berechnet:
[(x<sup>3</sup>) – (x<sup>3</sup> + x + 1)] mod x<sup>3</sup> + x + 1 = 
[x + 1] mod x<sup>3</sup> + x + 1 = 
x + 1

Sie fragen sich vielleicht, warum (x<sup>3</sup>) – (x<sup>3</sup> + x + 1) zu x + 1 und nicht zu – x – 1 evaluiert wird. Erinnern Sie sich daran, dass die erste Operation unseres Feldes modulo 2 definiert ist. Daher ergibt die Subtraktion zweier Vektoren genau das gleiche Ergebnis wie die Addition zweier Vektoren.

Zusammenfassend zur Multiplikation von x<sup>2</sup> + 1 und x<sup>2</sup> + x: Wenn Sie diese beiden Terme multiplizieren, erhalten Sie ein Polynom vierten Grades, x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x, das modulo x<sup>3</sup> + x + 1 reduziert werden muss. Das Polynom vierten Grades ist durch x<sup>3</sup> + x + 1 genau x + 1 Mal teilbar. Der Rest nach der Teilung von x<sup>4</sup> + x<sup>3</sup> + x<sup>2</sup> + x durch x<sup>3</sup> + x + 1 genau x + 1 Mal ist x + 1. Dies ist tatsächlich ein Element in unserem Set {0,1,x,x + 1,x<sup>2</sup>,x<sup>2</sup> + 1,x<sup>2</sup> + x,x<sup>2</sup> + x + 1}.

Warum wären Erweiterungskörper mit Basis 2 über Mengen von Polynomen, wie im obigen Beispiel, nützlich für die Kryptographie? Der Grund ist, dass man die Koeffizienten in den Polynomen solcher Mengen, entweder 0 oder 1, als Elemente von Binärstrings mit einer bestimmten Länge betrachten kann. Das Set **S** in unserem Beispiel oben könnte stattdessen als ein Set S betrachtet werden, das alle Binärstrings der Länge 3 (000 bis 111) umfasst. Die Operationen auf **S** können dann auch verwendet werden, um Operationen auf diesen Binärstrings durchzuführen und einen Binärstring derselben Länge zu erzeugen.

## Abstrakte Algebra in der Praxis
<chapterId>ed35b98d-18b4-5790-9911-1078e0f84f92</chapterId>
Trotz der formellen Sprache und der Abstraktheit der Diskussion sollte das Konzept einer Gruppe nicht allzu schwer zu verstehen sein. Es handelt sich lediglich um eine Menge von Elementen zusammen mit einer binären Operation, bei der die Ausführung dieser binären Operation auf diesen Elementen vier allgemeinen Bedingungen genügt. Eine abelsche Gruppe hat lediglich eine zusätzliche Bedingung, die als Kommutativität bekannt ist. Eine zyklische Gruppe wiederum ist eine spezielle Art von abelscher Gruppe, nämlich eine, die einen Generator hat. Ein Körper ist lediglich ein komplexeres Konstrukt aus der grundlegenden Gruppenvorstellung.
Aber wenn Sie praktisch veranlagt sind, könnten Sie sich an diesem Punkt fragen: Wen interessiert das? Hat das Wissen, dass eine Menge von Elementen mit einem Operator eine Gruppe, oder sogar eine abelsche oder zyklische Gruppe ist, irgendeine Relevanz in der realen Welt? Hat das Wissen, dass etwas ein Körper ist?

Ohne zu sehr ins Detail zu gehen, lautet die Antwort „ja“. Gruppen wurden erstmals im 19. Jahrhundert vom französischen Mathematiker Evariste Galois geschaffen. Er verwendete sie, um Schlussfolgerungen über das Lösen von Polynomgleichungen eines Grades höher als fünf zu ziehen.

Seitdem hat das Konzept der Gruppe geholfen, eine Reihe von Problemen in der Mathematik und anderswo zu beleuchten. Auf ihrer Basis konnte beispielsweise der Physiker Murray-Gellman die Existenz eines Teilchens vorhersagen, bevor es tatsächlich in Experimenten beobachtet wurde. Als weiteres Beispiel verwenden Chemiker die Gruppentheorie, um die Formen von Molekülen zu klassifizieren. Mathematiker haben sogar das Konzept einer Gruppe verwendet, um Schlussfolgerungen über etwas so Konkretes wie Tapeten zu ziehen!

Im Wesentlichen zu zeigen, dass eine Menge von Elementen mit einem Operator eine Gruppe ist, bedeutet, dass das, was Sie beschreiben, eine bestimmte Symmetrie hat. Nicht eine Symmetrie im üblichen Sinne des Wortes, sondern in einer abstrakteren Form. Und dies kann erhebliche Einblicke in bestimmte Systeme und Probleme bieten. Die komplexeren Vorstellungen aus der abstrakten Algebra geben uns nur zusätzliche Informationen.

Am wichtigsten ist, dass Sie die Bedeutung von zahlentheoretischen Gruppen und Körpern in der Praxis durch ihre Anwendung in der Kryptographie, insbesondere der Public-Key-Kryptographie, sehen werden. Wir haben bereits in unserer Diskussion über Körper gesehen, wie beispielsweise Erweiterungskörper im Rijndael-Chiffre verwendet werden. Wir werden dieses Beispiel in *Kapitel 5* ausarbeiten.

## Weiterführende Erkundungen
<chapterId>ab51038d-82bd-5c5d-a759-276cfbf7fbce</chapterId>

Für weitere Diskussionen über abstrakte Algebra würde ich die ausgezeichnete Videoserie über abstrakte Algebra von Socratica empfehlen. Ich würde insbesondere die folgenden Videos empfehlen: „Was ist abstrakte Algebra?“, „Gruppendefinition (erweitert)“, „Ringdefinition (erweitert)“ und „Körperdefinition (erweitert)“. Diese vier Videos geben Ihnen einige zusätzliche Einblicke in einen Großteil der oben geführten Diskussion. (Wir haben nicht über Ringe gesprochen, aber ein Körper ist nur eine spezielle Art von Ring.)

Für weitere Diskussionen über moderne Zahlentheorie können Sie viele fortgeschrittene Diskussionen über Kryptographie konsultieren. Ich würde als Vorschläge Jonathan Katz und Yehuda Lindells Einführung in die moderne Kryptographie oder Christof Paar und Jan Pelzls Verständnis der Kryptographie für weitere Diskussionen anbieten.
[^1]: Die Funktion funktioniert wie folgt. Jede ganze Zahl N kann in ein Produkt von Primzahlen zerlegt werden. Nehmen wir an, dass ein bestimmtes N in folgender Weise zerlegt wird: p<sub>1</sub><sup>e1</sup> • p<sub>2</sub><sup>e2</sup> …. • p<sub>m</sub><sup>em</sup>, wobei alle p's Primzahlen sind und alle e's ganze Zahlen größer oder gleich 1 sind. Dann ist φ(N) = Summe<sub>i=1…m</sub>[p<sub>i</sub><sup>ei</sup> – p<sub>i</sub><sup>ei - 1</sup>] [^1].
[^2]: Erweiterungskörper werden sehr kontraintuitiv. Anstatt Elemente von ganzen Zahlen zu haben, haben sie Mengen von Polynomen. Außerdem werden alle Operationen modulo eines irreduziblen Polynoms durchgeführt [^2].

[^3]: Siehe [YouTube-Video](https://www.youtube.com/watch?v=NOMUnMuxDZY&feature=youtu.be) [^3].

[^4]: Socratica, [Abstrakte Algebra](https://www.socratica.com/subject/abstract-algebra) [^4].

[^5]: Katz und Lindell, *Einführung in die moderne Kryptographie*, 2. Auflage, 2015 (CRC Press: Boca Raton, FL). Paar und Pelzl, *Verständnis der Kryptographie*, 2010 (Springer-Verlag: Berlin) [^5].


# Symmetrische Kryptographie
<partId>ef768d0e-fe7b-510c-87d6-6febb3de1039</partId>

Eine der beiden Hauptzweige der Kryptographie ist die symmetrische Kryptographie. Sie umfasst Verschlüsselungsschemata sowie Schemata, die sich mit Authentifizierung und Integrität befassen. Bis in die 1970er Jahre hätte die gesamte Kryptographie aus symmetrischen Verschlüsselungsschemata bestanden.

Die Hauptdiskussion beginnt mit einem Blick auf symmetrische Verschlüsselungsschemata und macht die entscheidende Unterscheidung zwischen Stromchiffren und Blockchiffren. Dann wenden wir uns den Nachrichtenauthentifizierungscodes zu, die Schemata zur Sicherstellung der Nachrichtenintegrität und -authentizität sind. Schließlich erkunden wir, wie symmetrische Verschlüsselungsschemata und Nachrichtenauthentifizierungscodes kombiniert werden können, um sichere Kommunikation zu gewährleisten.

Dieses Kapitel diskutiert verschiedene symmetrische kryptographische Schemata aus der Praxis im Vorbeigehen. Das nächste Kapitel bietet eine detaillierte Darstellung der Verschlüsselung mit einer Stromchiffre und einer Blockchiffre aus der Praxis, nämlich RC4 und AES.

Bevor wir unsere Diskussion über symmetrische Kryptographie beginnen, möchte ich kurz einige Bemerkungen zu den Alice-und-Bob-Illustrationen in diesem und den folgenden Kapiteln machen.


## Alice und Bob
<chapterId>47345330-be2d-5faf-afd0-d289a8d21bf1</chapterId>

Bei der Veranschaulichung der Prinzipien der Kryptographie verlassen sich die Menschen oft auf Beispiele, die Alice und Bob einbeziehen. Ich werde dies ebenfalls tun.

Besonders wenn Sie neu in der Kryptographie sind, ist es wichtig zu realisieren, dass diese Beispiele von Alice und Bob nur dazu dienen, die Prinzipien und Konstruktionen der Kryptographie in einer vereinfachten Umgebung zu illustrieren. Die Prinzipien und Konstruktionen sind jedoch auf eine viel breitere Palette von realen Kontexten anwendbar.

Folgendes sind fünf Schlüsselpunkte, die man bei Beispielen mit Alice und Bob in der Kryptographie im Kopf behalten sollte:

1. Sie können leicht in Beispiele mit anderen Arten von Akteuren wie Unternehmen oder Regierungsorganisationen übersetzt werden.
2. Sie können leicht erweitert werden, um drei oder mehr Akteure einzubeziehen.
3. In den Beispielen sind Bob und Alice typischerweise aktive Teilnehmer bei der Erstellung jeder Nachricht und bei der Anwendung kryptografischer Verfahren auf diese Nachricht. In der Realität ist die elektronische Kommunikation jedoch weitgehend automatisiert. Wenn Sie beispielsweise eine Website mit Transport Layer Security besuchen, wird die Kryptografie typischerweise vollständig von Ihrem Computer und dem Webserver gehandhabt. 4. Im Kontext der elektronischen Kommunikation sind die „Nachrichten“, die über einen Kommunikationskanal gesendet werden, normalerweise TCP/IP-Pakete. Diese können zu einer E-Mail, einer Facebook-Nachricht, einem Telefongespräch, einer Dateiübertragung, einer Website, einem Software-Upload und so weiter gehören. Es handelt sich nicht um Nachrichten im traditionellen Sinne. Dennoch vereinfachen Kryptografen diese Realität oft, indem sie sagen, dass die Nachricht beispielsweise eine E-Mail ist.
5. Die Beispiele konzentrieren sich typischerweise auf elektronische Kommunikation, können aber auch auf traditionelle Kommunikationsformen wie Briefe ausgeweitet werden.

## Symmetrische Verschlüsselungsverfahren
<chapterId>41bfdbe1-6d41-5272-98bb-81f24b2fd6af</chapterId>

Wir können ein **symmetrisches Verschlüsselungsverfahren** locker als jedes kryptografische Verfahren mit drei Algorithmen definieren:

1. Ein **Schlüsselgenerierungsalgorithmus**, der einen privaten Schlüssel generiert.
2. Ein **Verschlüsselungsalgorithmus**, der den privaten Schlüssel und einen Klartext als Eingaben nimmt und einen Geheimtext ausgibt.
3. Ein **Entschlüsselungsalgorithmus**, der den privaten Schlüssel und den Geheimtext als Eingaben nimmt und den ursprünglichen Klartext ausgibt.

Typischerweise bietet ein Verschlüsselungsverfahren – ob symmetrisch oder asymmetrisch – eine Vorlage für die Verschlüsselung basierend auf einem Kernalgorithmus, anstatt einer exakten Spezifikation.

Betrachten wir zum Beispiel Salsa20, ein symmetrisches Verschlüsselungsverfahren. Es kann sowohl mit 128- als auch mit 256-Bit-Schlüssellängen verwendet werden. Die Wahl der Schlüssellänge beeinflusst einige kleinere Details des Algorithmus (genau genommen die Anzahl der Durchläufe im Algorithmus).

Aber man würde nicht sagen, dass die Verwendung von Salsa20 mit einem 128-Bit-Schlüssel ein anderes Verschlüsselungsverfahren ist als Salsa20 mit einem 256-Bit-Schlüssel. Der Kernalgorithmus bleibt derselbe. Nur wenn sich der Kernalgorithmus ändert, würden wir wirklich von zwei verschiedenen Verschlüsselungsverfahren sprechen.

Symmetrische Verschlüsselungsverfahren sind typischerweise in zwei Arten von Fällen nützlich: (1) Solche, in denen zwei oder mehr Agenten aus der Ferne kommunizieren und den Inhalt ihrer Kommunikation geheim halten wollen; und (2) solche, in denen ein Agent den Inhalt einer Nachricht über die Zeit geheim halten möchte.

Sie können eine Darstellung der Situation (1) in *Abbildung 1* unten sehen. Bob möchte eine Nachricht M an Alice über eine Distanz senden, möchte aber nicht, dass andere diese Nachricht lesen können.

Bob verschlüsselt zuerst die Nachricht M mit dem privaten Schlüssel K. Dann sendet er den Geheimtext C an Alice. Sobald Alice den Geheimtext erhalten hat, kann sie ihn mit dem Schlüssel K entschlüsseln und den Klartext lesen. Mit einem guten Verschlüsselungsverfahren sollte jeder Angreifer, der den Geheimtext C abfängt, nichts wirklich Bedeutendes über die Nachricht M erfahren können.

Sie können eine Darstellung der Situation (2) in *Abbildung 2* unten sehen. Bob möchte verhindern, dass andere bestimmte Informationen einsehen. Eine typische Situation könnte sein, dass Bob ein Mitarbeiter ist, der sensible Daten auf seinem Computer speichert, die weder Außenstehende noch seine Kollegen lesen sollen.
Bob verschlüsselt die Nachricht M zum Zeitpunkt T<sub>0</sub> mit dem Schlüssel K, um den Chiffretext C zu erzeugen. Zum Zeitpunkt T<sub>1</sub> benötigt er die Nachricht erneut und entschlüsselt den Chiffretext C mit dem Schlüssel K. Jeder Angreifer, der in der Zwischenzeit auf den Chiffretext C gestoßen sein könnte, sollte nicht in der Lage gewesen sein, etwas Bedeutendes über M daraus abzuleiten.
*Abbildung 1: Geheimhaltung über den Raum*

![Abbildung 1: Geheimhaltung über den Raum](assets/Figure4-1.webp "Abbildung 1: Geheimhaltung über den Raum")

*Abbildung 2: Geheimhaltung über die Zeit*

![Abbildung 2: Geheimhaltung über die Zeit](assets/Figure4-2.webp "Abbildung 2: Geheimhaltung über die Zeit")

## Ein Beispiel: Die Verschiebechiffre
<chapterId>7b179ae8-8d15-5e80-a43f-22c970d87b5e</chapterId>

In Kapitel 2 sind wir auf die Verschiebechiffre gestoßen, die ein Beispiel für ein sehr einfaches symmetrisches Verschlüsselungsverfahren ist. Lassen Sie uns hier noch einmal darauf schauen.

Nehmen wir ein Wörterbuch *D* an, das alle Buchstaben des englischen Alphabets der Reihe nach den Zahlen {0,1,2…,25} zuordnet. Nehmen wir eine Menge möglicher Nachrichten **M** an. Die Verschiebechiffre ist dann ein Verschlüsselungsverfahren, das wie folgt definiert ist:

- Wähle zufällig einen Schlüssel k aus der Menge der möglichen Schlüssel **K**, wobei **K** = {0,1,2,…,25}
- Verschlüssle eine Nachricht m є **M**, wie folgt:
    - Trenne m in seine einzelnen Buchstaben m<sub>0</sub>, m<sub>1</sub>,….m<sub>i</sub>….,m<sub>l</sub>
    - Konvertiere jeden m<sub>i</sub> in eine Zahl gemäß *D*
    - Für jeden m<sub>i</sub>, c<sub>i</sub> = [(m<sub>i</sub> + k) mod 26]
    - Konvertiere jeden c<sub>i</sub> in einen Buchstaben gemäß *D*
    - Kombiniere dann c<sub>0</sub>, c<sub>1</sub>,….,c<sub>l</sub>, um den Chiffretext c zu erhalten
- Entschlüssle einen Chiffretext c wie folgt:
    - Konvertiere jeden c<sub>i</sub> in eine Zahl gemäß *D*
    - Für jeden c<sub>i</sub>, m<sub>i</sub> = [(c<sub>i</sub> – k) mod 26]
    - Konvertiere jeden m<sub>i</sub> in einen Buchstaben gemäß *D*
    - Kombiniere dann m<sub>0</sub>, m<sub>1</sub>,….,m<sub>l</sub>, um die ursprüngliche Nachricht m zu erhalten

Was die Verschiebechiffre zu einem symmetrischen Verschlüsselungsverfahren macht, ist, dass derselbe Schlüssel sowohl für den Verschlüsselungs- als auch für den Entschlüsselungsprozess verwendet wird. Angenommen, Sie möchten die Nachricht „DOG“ mit der Verschiebechiffre verschlüsseln und haben zufällig „24“ als Schlüssel ausgewählt. Die Verschlüsselung der Nachricht mit diesem Schlüssel würde „BME“ ergeben. Die einzige Möglichkeit, die ursprüngliche Nachricht wiederherzustellen, besteht darin, denselben Schlüssel „24“ für den Entschlüsselungsprozess zu verwenden.
Der Shift-Ziffer ist ein Beispiel für eine **monoalphabetische Substitutionschiffre**: ein Verschlüsselungsschema, bei dem das Chiffre-Alphabet festgelegt ist (d.h., es wird nur ein Alphabet verwendet). Unter der Annahme, dass der Entschlüsselungsalgorithmus deterministisch ist, kann jedes Symbol in der Substitutionschiffre höchstens einem Symbol im Klartext entsprechen.
Bis ins 18. Jahrhundert stützten sich viele Anwendungen der Verschlüsselung stark auf monoalphabetische Substitutionschiffren, obwohl diese oft viel komplexer waren als die Shift-Ziffer. Man könnte zum Beispiel zufällig einen Buchstaben aus dem Alphabet für jeden Buchstaben des Originaltexts auswählen, unter der Bedingung, dass jeder Buchstabe nur einmal im Chiffre-Alphabet vorkommt. Das bedeutet, dass man faktoriell 26 mögliche private Schlüssel hätte, was in der Zeit vor Computern enorm war.

Beachten Sie, dass Sie in der Kryptographie oft auf den Begriff **cipher** (Chiffre) stoßen werden. Seien Sie sich bewusst, dass dieser Begriff verschiedene Bedeutungen hat. Tatsächlich kenne ich mindestens fünf unterschiedliche Bedeutungen des Begriffs innerhalb der Kryptographie.

In einigen Fällen bezieht er sich auf ein Verschlüsselungsschema, wie es bei der Shift-Ziffer und der monoalphabetischen Substitutionschiffre der Fall ist. Der Begriff kann sich jedoch auch speziell auf den Verschlüsselungsalgorithmus, den privaten Schlüssel oder einfach auf den Chiffretext eines solchen Verschlüsselungsschemas beziehen.

Zuletzt kann der Begriff Chiffre auch auf einen Kernalgorithmus verweisen, aus dem man kryptographische Schemata konstruieren kann. Dazu können verschiedene Verschlüsselungsalgorithmen gehören, aber auch andere Arten von kryptographischen Schemata. Diese Bedeutung des Begriffs wird im Kontext von Blockchiffren (siehe den Abschnitt „Blockchiffren“ unten) relevant.

Sie werden auch auf die Begriffe **encipher** (verschlüsseln) oder **decipher** (entschlüsseln) stoßen. Diese Begriffe sind einfach Synonyme für Verschlüsselung und Entschlüsselung.

## Brute-Force-Angriffe und Kerckhoffs Prinzip
<chapterId>2d73ef97-26c5-5d11-8815-0ddbe89c8003</chapterId>

Die Shift-Ziffer ist ein sehr unsicheres symmetrisches Verschlüsselungsschema, zumindest in der modernen Welt.<sup>[1](#footnote1)</sup> Ein Angreifer könnte einfach versuchen, jeden Chiffretext mit allen 26 möglichen Schlüsseln zu entschlüsseln, um zu sehen, welches Ergebnis Sinn macht. Diese Art von Angriff, bei der der Angreifer einfach durch Schlüssel zyklisiert, um zu sehen, was funktioniert, ist als **Brute-Force-Angriff** oder **erschöpfende Schlüsselsuche** bekannt.

Damit ein Verschlüsselungsschema eine minimale Vorstellung von Sicherheit erfüllt, muss es eine Menge möglicher Schlüssel oder **Schlüsselraum** haben, der so groß ist, dass Brute-Force-Angriffe unpraktikabel sind. Alle modernen Verschlüsselungsschemata erfüllen diesen Standard. Dies ist als das **Prinzip des ausreichenden Schlüsselraums** bekannt. Ein ähnliches Prinzip gilt typischerweise auch in verschiedenen Arten von kryptographischen Schemata.

Um ein Gefühl für die massive Größe des Schlüsselraums in modernen Verschlüsselungsschemata zu bekommen, nehmen wir an, dass eine Datei mit einem 128-Bit-Schlüssel unter Verwendung des Advanced Encryption Standard verschlüsselt wurde. Das bedeutet, dass ein Angreifer eine Menge von 2<sup>128</sup> Schlüsseln durchlaufen muss, um einen Brute-Force-Angriff durchzuführen. Eine Erfolgschance von 0,78 % mit dieser Strategie würde erfordern, dass der Angreifer ungefähr 2,65 x 10<sup>36</sup> Schlüssel durchläuft.
Angenommen, wir nehmen optimistisch an, dass ein Angreifer 10 Billiarden Schlüssel pro Sekunde (d.h. 10<sup>16</sup> Schlüssel pro Sekunde) ausprobieren kann. Um 0,78% aller Schlüssel im Schlüsselraum zu testen, müsste ihr Angriff 2,65 x 10<sup>20</sup> Sekunden dauern. Das sind etwa 8,4 Billionen Jahre. Selbst ein Brute-Force-Angriff durch einen absurd mächtigen Gegner ist also mit einem modernen 128-Bit-Verschlüsselungsschema nicht realistisch. Dies ist das Prinzip des ausreichenden Schlüsselraums in Aktion.
Ist die Verschiebungschiffre sicherer, wenn der Angreifer den Verschlüsselungsalgorithmus nicht kennt? Vielleicht, aber nicht viel.

In jedem Fall geht die moderne Kryptographie immer davon aus, dass die Sicherheit eines jeden symmetrischen Verschlüsselungsschemas nur auf der Geheimhaltung des privaten Schlüssels beruht. Es wird immer angenommen, dass der Angreifer alle anderen Details kennt, einschließlich des Nachrichtenraums, des Schlüsselraums, des Chiffretext-Raums, des Schlüsselauswahlalgorithmus, des Verschlüsselungsalgorithmus und des Entschlüsselungsalgorithmus.

Die Idee, dass die Sicherheit eines symmetrischen Verschlüsselungsschemas nur auf der Geheimhaltung des privaten Schlüssels beruhen kann, ist als **Kerckhoffs’ Prinzip** bekannt.

Wie ursprünglich von Kerckhoffs beabsichtigt, gilt das Prinzip nur für symmetrische Verschlüsselungsschemata. Eine allgemeinere Version des Prinzips gilt jedoch auch für alle anderen modernen Arten von kryptographischen Schemata: Das Design eines kryptographischen Schemas darf nicht geheim sein müssen, damit es sicher ist; die Geheimhaltung kann sich nur auf einige Informationsstränge, typischerweise einen privaten Schlüssel, erstrecken.

Kerckhoffs’ Prinzip ist aus vier Gründen zentral für die moderne Kryptographie.<sup>[2](#footnote2)</sup> Erstens gibt es nur eine begrenzte Anzahl von kryptographischen Schemata für bestimmte Arten von Anwendungen. Zum Beispiel verwenden die meisten modernen symmetrischen Verschlüsselungsanwendungen den Rijndael-Zypher. Die Geheimhaltung bezüglich des Designs eines Schemas ist also nur sehr begrenzt. Es gibt jedoch viel mehr Flexibilität, einen privaten Schlüssel für den Rijndael-Zypher geheim zu halten.

Zweitens ist es einfacher, einige Informationsstränge zu ersetzen als ein ganzes kryptographisches Schema. Angenommen, alle Mitarbeiter eines Unternehmens verwenden die gleiche Verschlüsselungssoftware und jeder zwei Mitarbeiter haben einen privaten Schlüssel, um vertraulich zu kommunizieren. Schlüsselkompromisse sind in diesem Szenario ein Ärgernis, aber zumindest könnte das Unternehmen die Software bei solchen Sicherheitsverletzungen behalten. Wenn das Unternehmen auf die Geheimhaltung des Schemas angewiesen wäre, würde jede Verletzung dieser Geheimhaltung den Ersatz aller Software erfordern.

Drittens ermöglicht Kerckhoffs’ Prinzip die Standardisierung und Kompatibilität zwischen Benutzern von kryptographischen Schemata. Dies hat massive Vorteile für die Effizienz. Es ist zum Beispiel schwer vorstellbar, wie Millionen von Menschen jeden Tag sicher mit den Webservern von Google verbinden könnten, wenn diese Sicherheit die Geheimhaltung kryptographischer Schemata erfordern würde.

Viertens ermöglicht Kerckhoffs’ Prinzip die öffentliche Überprüfung von kryptographischen Schemata. Diese Art der Überprüfung ist absolut notwendig, um sichere kryptographische Schemata zu erreichen. Veranschaulichend war der Hauptalgorithmus in der symmetrischen Kryptographie, der Rijndael-Zypher, das Ergebnis eines Wettbewerbs, der zwischen 1997 und 2000 vom National Institute of Standards and Technology organisiert wurde.

Jedes System, das versucht, **Sicherheit durch Obskurität** zu erreichen, ist eines, das darauf angewiesen ist, die Details seines Designs und/oder seiner Implementierung geheim zu halten. In der Kryptographie wäre dies speziell ein System, das darauf angewiesen ist, die Designdetails des kryptographischen Schemas geheim zu halten. Sicherheit durch Obskurität steht also im direkten Gegensatz zu Kerckhoffs’ Prinzip.
Die Fähigkeit der Offenheit, Qualität und Sicherheit zu stärken, erstreckt sich auch weit über die Kryptographie hinaus auf die digitale Welt. Freie und Open-Source-Linux-Distributionen wie Debian haben beispielsweise im Vergleich zu ihren Windows- und MacOS-Pendants in Bezug auf Privatsphäre, Stabilität, Sicherheit und Flexibilität mehrere Vorteile. Obwohl dies mehrere Ursachen haben kann, ist das wahrscheinlich wichtigste Prinzip, wie Eric Raymond es in seinem berühmten Essay "The Cathedral and the Bazaar" formulierte, dass "[b]ei genügend Augenpaaren alle Fehler oberflächlich sind."<sup>[3](#footnote3)</sup> Es ist dieses Prinzip der Weisheit der Menge, das Linux seinen bedeutendsten Erfolg bescherte.
Man kann nie eindeutig sagen, dass ein kryptographisches Schema "sicher" oder "unsicher" ist. Stattdessen gibt es verschiedene Sicherheitsbegriffe für kryptographische Schemata. Jede **Definition kryptographischer Sicherheit** muss (1) Sicherheitsziele sowie (2) die Fähigkeiten eines Angreifers spezifizieren. Die Analyse kryptographischer Schemata gegenüber einer oder mehreren spezifischen Sicherheitsbegriffen bietet Einblicke in ihre Anwendungen und Einschränkungen.

Obwohl wir nicht auf alle Details der verschiedenen Sicherheitsbegriffe der Kryptographie eingehen werden, sollten Sie wissen, dass zwei Annahmen allen modernen kryptographischen Sicherheitsbegriffen bezüglich symmetrischer und asymmetrischer Schemata (und in gewisser Form auch anderen kryptographischen Primitiven) allgegenwärtig sind:

* Das Wissen des Angreifers über das Schema entspricht dem Kerckhoffs’schen Prinzip.
* Der Angreifer kann keinen Brute-Force-Angriff auf das Schema durchführbar ausführen. Insbesondere erlauben die Bedrohungsmodelle kryptographischer Sicherheitsbegriffe typischerweise nicht einmal Brute-Force-Angriffe, da sie davon ausgehen, dass diese keine relevante Überlegung sind.

## Stromchiffren
<chapterId>479aa6f4-45c4-59ca-8616-8cf8e61fc871</chapterId>

Symmetrische Verschlüsselungsschemata werden üblicherweise in zwei Typen unterteilt: Stromchiffren und Blockchiffren. Diese Unterscheidung ist jedoch etwas problematisch, da die Begriffe auf inkonsistente Weise verwendet werden. In den nächsten Abschnitten werde ich die Unterscheidung so darlegen, wie ich sie für am besten halte. Sie sollten jedoch wissen, dass viele Menschen diese Begriffe etwas anders verwenden werden, als ich es darlege.

Beginnen wir zunächst mit Stromchiffren. Eine **Stromchiffre** ist ein symmetrisches Verschlüsselungsschema, bei dem die Verschlüsselung aus zwei Schritten besteht.

Zuerst wird über einen privaten Schlüssel eine Zeichenfolge in der Länge des Klartextes erzeugt. Diese Zeichenfolge wird als **Schlüsselstrom** bezeichnet.

Anschließend wird der Schlüsselstrom mathematisch mit dem Klartext kombiniert, um einen Chiffretext zu erzeugen. Diese Kombination ist typischerweise eine XOR-Operation. Für die Entschlüsselung können Sie einfach die Operation umkehren. (Beachten Sie, dass A XOR B = B XOR A, falls A und B Bitfolgen sind. Die Reihenfolge einer XOR-Operation in einer Stromchiffre ist also für das Ergebnis nicht relevant. Diese Eigenschaft ist als Kommutativität bekannt.)

Eine typische XOR-Stromchiffre ist in *Abbildung 3* dargestellt. Zuerst nehmen Sie einen privaten Schlüssel K und verwenden ihn, um einen Schlüsselstrom zu erzeugen. Der Schlüsselstrom wird dann über eine XOR-Operation mit dem Klartext kombiniert, um den Chiffretext zu erzeugen. Jeder Agent, der den Chiffretext erhält, kann ihn leicht entschlüsseln, wenn er den Schlüssel K hat. Alles, was sie tun muss, ist, einen Schlüsselstrom zu erstellen, der so lang wie der Chiffretext ist, gemäß dem angegebenen Verfahren des Schemas und ihn mit dem Chiffretext zu XOR-en.

*Abbildung 3: Eine XOR-Stromchiffre*

![Abbildung 3: Eine XOR-Stromchiffre](assets/Figure4-3.webp "Abbildung 3: Eine XOR-Stromchiffre")
Bitte denken Sie daran, dass ein Verschlüsselungsschema typischerweise eine Vorlage für die Verschlüsselung mit demselben Kernalgorithmus ist, anstatt eine exakte Spezifikation. Entsprechend ist ein Stromchiffre in der Regel eine Vorlage für die Verschlüsselung, bei der Sie Schlüssel unterschiedlicher Länge verwenden können. Obwohl die Schlüssellänge einige kleinere Details des Schemas beeinflussen kann, wird sie dessen wesentliche Form nicht beeinträchtigen.
Das Verschiebechiffre ist ein Beispiel für ein sehr einfaches und unsicheres Stromchiffre. Mit einem einzigen Buchstaben (dem privaten Schlüssel) können Sie eine Buchstabenfolge erzeugen, die so lang wie die Nachricht ist (der Schlüsselstrom). Dieser Schlüsselstrom wird dann mit dem Klartext über eine Modulo-Operation kombiniert, um einen Geheimtext zu erzeugen. (Diese Modulo-Operation kann zu einer XOR-Operation vereinfacht werden, wenn die Buchstaben in Bits dargestellt werden).

Ein weiteres berühmtes Beispiel für ein Stromchiffre ist das **Vigenère-Chiffre**, nach Blaise de Vigenère, der es Ende des 16. Jahrhunderts vollständig entwickelte (obwohl andere zuvor bereits viel Vorarbeit geleistet hatten). Es ist ein Beispiel für ein **polyalphabetisches Substitutionschiffre**: ein Verschlüsselungsschema, bei dem das Geheimtextalphabet für ein Klartextsymbol je nach seiner Position im Text wechselt. Im Gegensatz zu einem monoalphabetischen Substitutionschiffre können Geheimtextsymbole mit mehr als einem Klartextsymbol in Verbindung gebracht werden.

Als die Verschlüsselung in der Renaissance in Europa an Popularität gewann, tat dies auch die **Kryptoanalyse** – das heißt, das Brechen von Geheimtexten – insbesondere unter Verwendung der **Frequenzanalyse**. Letztere nutzt statistische Regelmäßigkeiten in unserer Sprache, um Geheimtexte zu brechen, und wurde bereits im neunten Jahrhundert von arabischen Gelehrten entdeckt. Es ist eine Technik, die besonders gut bei längeren Texten funktioniert. Und selbst die ausgefeiltesten monoalphabetischen Substitutionschiffren waren im 18. Jahrhundert in Europa, insbesondere im militärischen und sicherheitstechnischen Bereich, der Frequenzanalyse nicht mehr gewachsen. Da das Vigenère-Chiffre einen signifikanten Fortschritt in der Sicherheit bot, wurde es in dieser Zeit beliebt und war bis Ende des 18. Jahrhunderts weit verbreitet.

Umgangssprachlich funktioniert das Verschlüsselungsschema wie folgt:

1. Wählen Sie ein Wort mit mehreren Buchstaben als privaten Schlüssel
2. Wenden Sie für jede Nachricht das Verschiebechiffre auf jeden Buchstaben der Nachricht an, indem Sie den entsprechenden Buchstaben im Schlüsselwort als Verschiebung verwenden
3. Wenn Sie das Schlüsselwort durchlaufen haben, aber den Klartext noch nicht vollständig verschlüsselt haben, wenden Sie erneut die Buchstaben des Schlüsselworts als Verschiebechiffre auf die entsprechenden Buchstaben im Rest des Textes an
4. Fahren Sie mit diesem Prozess fort, bis die gesamte Nachricht verschlüsselt wurde

Um zu veranschaulichen, nehmen wir an, Ihr privater Schlüssel ist GOLD und Sie möchten die Nachricht "CRYPTOGRAPHY" verschlüsseln. In diesem Fall würden Sie gemäß dem Vigenère-Chiffre wie folgt vorgehen:

- c<sub>0</sub> = [(2 + 6) Mod 26] = 8 = I
- c<sub>1</sub> = [(17 + 14) Mod 26] = 5 = F
- c<sub>2</sub> = [(24 + 11) Mod 26] = 9 = J
- c<sub>3</sub> = [(15 + 3) Mod 26] = 18 = S
- c<sub>4</sub> = [(19 + 6) Mod 26] = 25 = Z
- c<sub>5</sub> = [(14 + 14) Mod 26] = 2 = C
- c<sub>6</sub> = [(6 + 11) Mod 26] = 17 = R
- c<sub>7</sub> = [(17 + 3) Mod 26] = 20 = U
- c<sub>8</sub> = [(0 + 6) Mod 26] = 6 = G
- c<sub>9</sub> = [(15 + 14) Mod 26] = 3 = D
- c<sub>10</sub> = [(7 + 11) Mod 26] = 18 = S
- c<sub>11</sub> = [(24 + 3) Mod 26] = 1 = B
- c = "IFJSZCRUGDSB"

Ein weiteres berühmtes Beispiel für eine Stromchiffre ist das **One-Time-Pad**. Beim One-Time-Pad erstellt man einfach eine Zeichenfolge aus zufälligen Bits, die so lang wie die Klartextnachricht ist, und erzeugt den Geheimtext über die XOR-Operation. Daher sind der private Schlüssel und der Schlüsselstrom bei einem One-Time-Pad identisch.

Während die Verschiebechiffre und die Vigenère-Chiffre in der heutigen Zeit sehr unsicher sind, ist das One-Time-Pad sehr sicher, wenn es korrekt verwendet wird. Wahrscheinlich die bekannteste Anwendung des One-Time-Pads war, zumindest bis in die 1980er Jahre, für die **Washington-Moskau-Hotline**.<sup>[4](#footnote4)</sup>

Die Hotline ist eine direkte Kommunikationsverbindung zwischen Washington und Moskau für dringende Angelegenheiten, die nach der Kubakrise eingerichtet wurde. Die Technologie dafür hat sich im Laufe der Jahre gewandelt. Derzeit umfasst sie ein direktes Glasfaserkabel sowie zwei Satellitenverbindungen (für Redundanz), die E-Mail- und Textnachrichten ermöglichen. Die Verbindung endet an verschiedenen Orten in den USA. Das Pentagon, das Weiße Haus und der Raven Rock Mountain sind bekannte Endpunkte. Entgegen der landläufigen Meinung waren Telefone nie Teil der Hotline.

Im Wesentlichen funktionierte das One-Time-Pad-System wie folgt. Sowohl Washington als auch Moskau hätten zwei Sätze zufälliger Zahlen. Ein Satz zufälliger Zahlen, erstellt von den Russen, bezog sich auf die Verschlüsselung und Entschlüsselung von Nachrichten in russischer Sprache. Ein Satz zufälliger Zahlen, erstellt von den Amerikanern, bezog sich auf die Verschlüsselung und Entschlüsselung von Nachrichten in englischer Sprache. Von Zeit zu Zeit würden weitere zufällige Zahlen durch vertrauenswürdige Kuriere an die andere Seite geliefert.

Washington und Moskau konnten dann geheim kommunizieren, indem sie diese zufälligen Zahlen zur Erstellung von One-Time-Pads verwendeten. Jedes Mal, wenn man kommunizieren musste, würde man den nächsten Teil der zufälligen Zahlen für die Nachricht verwenden.

Obwohl sehr sicher, hat das One-Time-Pad signifikante praktische Einschränkungen: Der Schlüssel muss so lang wie die Nachricht sein und kein Teil eines One-Time-Pads darf wiederverwendet werden. Das bedeutet, dass man den Überblick behalten muss, wo man im One-Time-Pad ist, eine massive Anzahl von Bits speichern und von Zeit zu Zeit zufällige Bits mit seinen Gegenparteien austauschen muss. Als Konsequenz wird das One-Time-Pad in der Praxis nicht häufig verwendet.

Stattdessen sind **pseudorandomisierte Stromchiffren** die in der Praxis vorherrschenden Stromchiffren. Salsa20 und eine eng verwandte Variante namens ChaCha sind Beispiele für häufig verwendete pseudorandomisierte Stromchiffren.

Bei diesen pseudorandomisierten Stromchiffren wählt man zuerst zufällig einen Schlüssel K, der kürzer als die Länge des Klartextes ist. Ein solcher zufälliger Schlüssel K wird üblicherweise von unserem Computer auf der Basis von unvorhersehbaren Daten erstellt, die er im Laufe der Zeit sammelt, wie die Zeit zwischen Netzwerknachrichten, Mausbewegungen und so weiter.
Dieser zufällige Schlüssel K wird dann in einen Expansionsalgorithmus eingesetzt, der einen pseudozufälligen Schlüsselstrom erzeugt, der so lang wie die Nachricht ist. Sie können genau festlegen, wie lang der Schlüsselstrom sein muss (z.B. 500 Bits, 1000 Bits, 1200 Bits, 29.117 Bits usw.). Ein pseudozufälliger Schlüsselstrom erscheint *als ob* er vollständig zufällig aus der Menge aller Zeichenfolgen mit derselben Länge ausgewählt wurde. Daher erscheint die Verschlüsselung mit einem pseudozufälligen Schlüsselstrom so, als wäre sie mit einem Einmalschlüssel durchgeführt worden. Aber das ist natürlich nicht der Fall.

Da unser privater Schlüssel kürzer als der Schlüsselstrom ist und unser Expansionsalgorithmus deterministisch sein muss, damit der Verschlüsselungs-/Entschlüsselungsprozess funktioniert, könnte nicht jeder Schlüsselstrom dieser bestimmten Länge als Ausgabe aus unserer Expansionsoperation resultieren.

Nehmen wir beispielsweise an, dass unser privater Schlüssel eine Länge von 128 Bits hat und dass wir ihn in einen Expansionsalgorithmus einsetzen können, um einen viel längeren Schlüsselstrom zu erzeugen, sagen wir von 2.500 Bits. Da unser Expansionsalgorithmus deterministisch sein muss, kann unser Algorithmus höchstens 1/2<sup>128</sup> Zeichenfolgen mit einer Länge von 2.500 Bits auswählen. Ein solcher Schlüsselstrom könnte also nie vollständig zufällig aus allen Zeichenfolgen derselben Länge ausgewählt werden.

Unsere Definition eines Stromchiffre hat zwei Aspekte: (1) ein Schlüsselstrom, der so lang wie der Klartext ist, wird mit Hilfe eines privaten Schlüssels erzeugt; und (2) dieser Schlüsselstrom wird mit dem Klartext kombiniert, typischerweise über eine XOR-Operation, um den Chiffretext zu erzeugen.

Manchmal definieren Menschen Bedingung (1) strenger, indem sie behaupten, dass der Schlüsselstrom spezifisch pseudozufällig sein muss. Das bedeutet, dass weder die Verschiebechiffre noch der Einmalschlüssel als Stromchiffren betrachtet würden.

Meiner Meinung nach bietet die breitere Definition von Bedingung (1) eine einfachere Möglichkeit, Verschlüsselungsschemata zu organisieren. Darüber hinaus bedeutet es, dass wir nicht aufhören müssen, ein bestimmtes Verschlüsselungsschema als Stromchiffre zu bezeichnen, nur weil wir erfahren, dass es tatsächlich nicht auf pseudozufälligen Schlüsselströmen basiert.

## Blockchiffren
<chapterId>2df52d51-943d-5df7-9d49-333e4c5d97b7</chapterId>

Die erste Art, wie eine **Blockchiffre** allgemein verstanden wird, ist als etwas Primitiveres als eine Stromchiffre: Ein Kernalgorithmus, der eine längenerhaltende Transformation an einer Zeichenfolge geeigneter Länge mit Hilfe eines Schlüssels durchführt. Dieser Algorithmus kann für die Erstellung von Verschlüsselungsschemata und vielleicht anderen Arten von kryptografischen Schemata verwendet werden.

Häufig kann eine Blockchiffre Eingabezeichenfolgen unterschiedlicher Längen wie 64, 128 oder 256 Bits sowie Schlüssel unterschiedlicher Längen wie 128, 192 oder 256 Bits aufnehmen. Obwohl sich einige Details des Algorithmus je nach diesen Variablen ändern können, ändert sich der Kernalgorithmus nicht. Wenn dies der Fall wäre, würden wir von zwei verschiedenen Blockchiffren sprechen. Beachten Sie, dass die Verwendung der Terminologie des Kernalgorithmus hier dieselbe ist wie für Verschlüsselungsschemata.

Eine Darstellung, wie eine Blockchiffre funktioniert, kann in *Abbildung 4* unten gesehen werden. Eine Nachricht M der Länge L und ein Schlüssel K dienen als Eingaben für die Blockchiffre. Sie gibt eine Nachricht M’ der Länge L aus. Der Schlüssel muss nicht unbedingt dieselbe Länge wie M und M’ für die meisten Blockchiffren haben.

*Abbildung 4: Eine Blockchiffre*

![Abbildung 4: Eine Blockchiffre](assets/Figure4-4.webp "Abbildung 4: Eine Blockchiffre")
Ein Blockchiffre allein ist kein Verschlüsselungsschema. Aber ein Blockchiffre kann mit verschiedenen **Betriebsmodi** verwendet werden, um unterschiedliche Verschlüsselungsschemata zu erzeugen. Ein Betriebsmodus fügt einfach einige zusätzliche Operationen außerhalb des Blockchiffres hinzu.

Um zu veranschaulichen, wie das funktioniert, nehmen wir an, ein Blockchiffre (BC), der eine 128-Bit-Eingabezeichenfolge und einen 128-Bit-privaten Schlüssel benötigt. Abbildung 5 unten zeigt, wie dieser Blockchiffre mit dem **Electronic Code Book Modus** (**ECB-Modus**) verwendet werden kann, um ein Verschlüsselungsschema zu erstellen. (Die Ellipsen auf der rechten Seite deuten an, dass Sie dieses Muster so lange wiederholen können, wie es nötig ist).

*Abbildung 5: Ein Blockchiffre mit ECB-Modus*

![Abbildung 5: Ein Blockchiffre mit ECB-Modus](assets/Figure4-5.webp "Abbildung 5: Ein Blockchiffre mit ECB-Modus")

Der Prozess für die Electronic Code Book-Verschlüsselung mit dem Blockchiffre ist wie folgt. Sehen Sie, ob Sie Ihre Klartextnachricht in 128-Bit-Blöcke unterteilen können. Wenn nicht, fügen Sie der Nachricht **Padding** hinzu, sodass das Ergebnis gleichmäßig durch die Blockgröße von 128 Bits geteilt werden kann. Das sind Ihre Daten, die für den Verschlüsselungsprozess verwendet werden.

Teilen Sie nun die Daten in 128-Bit-Zeichenfolgen (M<sub>1</sub>, M<sub>2</sub>, M<sub>3</sub> usw.) auf. Führen Sie jede 128-Bit-Zeichenfolge durch den Blockchiffre mit Ihrem 128-Bit-Schlüssel, um 128-Bit-Blöcke von Ciphertext (C<sub>1</sub>, C<sub>2</sub>, C<sub>3</sub> usw.) zu erzeugen. Diese Blöcke, wieder zusammengesetzt, bilden den vollständigen Ciphertext.

Die Entschlüsselung ist einfach der umgekehrte Prozess, obwohl der Empfänger eine erkennbare Methode benötigt, um jedes Padding aus den entschlüsselten Daten zu entfernen und die ursprüngliche Klartextnachricht zu produzieren.

Obwohl relativ unkompliziert, mangelt es einem Blockchiffre mit Electronic Code Book-Modus an Sicherheit. Dies liegt daran, dass es zu **deterministischer Verschlüsselung** führt. Zwei identische 128-Bit-Datenstrings werden genau auf die gleiche Weise verschlüsselt. Diese Information kann ausgenutzt werden.

Stattdessen sollte jedes aus einem Blockchiffre konstruierte Verschlüsselungsschema **probabilistisch** sein: das heißt, die Verschlüsselung einer beliebigen Nachricht M oder eines spezifischen Teils von M sollte im Allgemeinen jedes Mal ein anderes Ergebnis liefern.<sup>[5](#footnote5)</sup>

Der **Cipher Block Chaining Modus** (**CBC-Modus**) ist wahrscheinlich der am häufigsten verwendete Modus mit einem Blockchiffre. Die Kombination, wenn richtig durchgeführt, erzeugt ein probabilistisches Verschlüsselungsschema. Sie können eine Darstellung dieses Betriebsmodus in Abbildung 6 unten sehen.

*Abbildung 6: Ein Blockchiffre mit CBC-Modus*

![Abbildung 6: Ein Blockchiffre mit CBC-Modus](assets/Figure4-6.webp "Abbildung 6: Ein Blockchiffre mit CBC-Modus")

Nehmen wir an, die Blockgröße beträgt wieder 128 Bits. Also, um zu beginnen, müssten Sie erneut sicherstellen, dass Ihre ursprüngliche Klartextnachricht das notwendige Padding erhält.

Dann XOR-en Sie den ersten 128-Bit-Teil Ihres Klartexts mit einem **Initialisierungsvektor** von 128 Bits. Das Ergebnis wird in den Blockchiffre eingegeben, um einen Ciphertext für den ersten Block zu erzeugen. Für den zweiten Block von 128 Bits XOR-en Sie zuerst den Klartext mit dem Ciphertext aus dem ersten Block, bevor Sie ihn in den Blockchiffre einfügen. Sie setzen diesen Prozess fort, bis Sie Ihre gesamte Klartextnachricht verschlüsselt haben.

Wenn Sie fertig sind, senden Sie die verschlüsselte Nachricht zusammen mit dem unverschlüsselten Initialisierungsvektor an den Empfänger. Der Empfänger muss den Initialisierungsvektor kennen, sonst kann er den Ciphertext nicht entschlüsseln.
Diese Konstruktion ist viel sicherer als der Modus des elektronischen Codebuchs, wenn sie korrekt verwendet wird. Sie sollten zunächst sicherstellen, dass der Initialisierungsvektor eine zufällige oder pseudozufällige Zeichenfolge ist. Darüber hinaus sollten Sie jedes Mal, wenn Sie dieses Verschlüsselungsschema verwenden, einen anderen Initialisierungsvektor verwenden.
Mit anderen Worten, Ihr Initialisierungsvektor sollte ein zufälliger oder pseudozufälliger Nonce sein, wobei ein **Nonce** für "eine Zahl, die nur einmal verwendet wird" steht. Wenn Sie diese Praxis beibehalten, dann stellt der CBC-Modus mit einem Blockchiffre sicher, dass zwei identische Klartextblöcke im Allgemeinen jedes Mal unterschiedlich verschlüsselt werden.

Schließlich wenden wir unsere Aufmerksamkeit dem **Output Feedback Modus** (**OFB-Modus**) zu. Sie können eine Darstellung dieses Modus in *Abbildung 7* sehen.

*Abbildung 7: Ein Blockchiffre mit OFB-Modus*

![Abbildung 7: Ein Blockchiffre mit OFB-Modus](assets/Figure4-7.webp "Abbildung 7: Ein Blockchiffre mit OFB-Modus")

Mit dem OFB-Modus wählen Sie ebenfalls einen Initialisierungsvektor. Aber hier wird für den ersten Block der Initialisierungsvektor direkt in das Blockchiffre mit Ihrem Schlüssel eingesetzt. Die resultierenden 128-Bit werden dann als Keystream behandelt. Dieser Keystream wird mit dem Klartext XOR-verknüpft, um den Chiffretext für den Block zu erzeugen. Für nachfolgende Blöcke verwenden Sie den Keystream aus dem vorherigen Block als Eingabe in das Blockchiffre und wiederholen die Schritte.

Wenn Sie genau hinsehen, was hier tatsächlich mit dem Blockchiffre im OFB-Modus erstellt wurde, ist ein Stromchiffre. Sie erzeugen Keystream-Teile von 128-Bit, bis Sie die Länge des Klartextes haben (wobei die Bits, die Sie vom letzten 128-Bit-Keystream-Teil nicht benötigen, verworfen werden). Dann XOR-verknüpfen Sie den Keystream mit Ihrer Klartextnachricht, um den Chiffretext zu erhalten.

Im vorherigen Abschnitt über Stromchiffren habe ich gesagt, dass Sie einen Keystream mit Hilfe eines privaten Schlüssels erzeugen. Um genau zu sein, muss er nicht nur mit einem privaten Schlüssel erstellt werden. Wie Sie im OFB-Modus sehen können, wird der Keystream mit Unterstützung sowohl eines privaten Schlüssels als auch eines Initialisierungsvektors erzeugt.

Beachten Sie, dass wie beim CBC-Modus, es wichtig ist, jedes Mal, wenn Sie ein Blockchiffre im OFB-Modus verwenden, einen pseudozufälligen oder zufälligen Nonce für den Initialisierungsvektor auszuwählen. Andernfalls wird die gleiche 128-Bit-Nachrichtenfolge, die in verschiedenen Kommunikationen gesendet wird, auf die gleiche Weise verschlüsselt. Dies ist eine Möglichkeit, probabilistische Verschlüsselung mit einem Stromchiffre zu erstellen.

Einige Stromchiffren verwenden nur einen privaten Schlüssel, um einen Keystream zu erstellen. Für diese Stromchiffren ist es wichtig, dass Sie einen zufälligen Nonce verwenden, um den privaten Schlüssel für jede Kommunikationsinstanz auszuwählen. Andernfalls werden auch die Ergebnisse der Verschlüsselung mit diesen Stromchiffren deterministisch sein, was zu Sicherheitsproblemen führt.

Der beliebteste moderne Blockchiffre ist der **Rijndael-Chiffre**. Er war der Gewinner aus fünfzehn Einreichungen zu einem Wettbewerb, der vom National Institute of Standards and Technology (NIST) zwischen 1997 und 2000 abgehalten wurde, um einen älteren Verschlüsselungsstandard, den **Data Encryption Standard** (**DES**), zu ersetzen.
Der Rijndael-Algorithmus kann mit verschiedenen Spezifikationen für Schlüssellängen und Blockgrößen sowie in unterschiedlichen Betriebsmodi verwendet werden. Das Komitee für den NIST-Wettbewerb hat eine eingeschränkte Version des Rijndael-Algorithmus angenommen – nämlich eine, die 128-Bit-Blockgrößen und Schlüssellängen von entweder 128 Bits, 192 Bits oder 256 Bits erfordert – als Teil des **Advanced Encryption Standard** (**AES**). Dies ist wirklich der Hauptstandard für symmetrische Verschlüsselungsanwendungen. Er ist so sicher, dass sogar die NSA bereit zu sein scheint, ihn mit 256-Bit-Schlüsseln für streng geheime Dokumente zu verwenden.<sup>[6](#footnote6)</sup>
Der AES-Blockchiffre wird in *Kapitel 5* detailliert erklärt.

## Klärung der Verwirrung
<chapterId>121c1858-27e3-5862-b0ce-4ff2f70f9f0f</chapterId>

Die Verwirrung über den Unterschied zwischen Blockchiffren und Stromchiffren entsteht, weil manchmal der Begriff Blockchiffre speziell als eine *Blockchiffre mit einem Blockmodus der Verschlüsselung* verstanden wird.

Betrachten Sie die ECB- und CBC-Modi im vorherigen Abschnitt. Diese erfordern speziell, dass die Daten zur Verschlüsselung durch die Blockgröße teilbar sind (was bedeutet, dass Sie möglicherweise Padding für die ursprüngliche Nachricht verwenden müssen). Darüber hinaus werden die Daten in diesen Modi auch direkt von der Blockchiffre bearbeitet (und nicht nur mit dem Ergebnis einer Blockchiffre-Operation kombiniert, wie im OFB-Modus).

Daher können Sie alternativ eine **Blockchiffre** als jedes Verschlüsselungsschema definieren, das auf festen Blocklängen der Nachricht auf einmal operiert (wobei jeder Block länger als ein Byte sein muss, sonst wird es zu einer Stromchiffre). Sowohl die Daten zur Verschlüsselung als auch der Chiffretext müssen sich gleichmäßig in diese Blockgröße teilen. Typischerweise ist die Blockgröße 64, 128, 192 oder 256 Bits lang. Im Gegensatz dazu kann eine Stromchiffre Nachrichten in Stücken von einem Bit oder Byte auf einmal verschlüsseln.

Mit diesem spezifischeren Verständnis von Blockchiffre können Sie tatsächlich behaupten, dass moderne Verschlüsselungsschemata entweder Strom- oder Blockchiffren sind. Von nun an werde ich den Begriff Blockchiffre im allgemeineren Sinne verwenden, sofern nicht anders angegeben.

Die Diskussion über den OFB-Modus im vorherigen Abschnitt wirft auch einen weiteren interessanten Punkt auf. Einige Stromchiffren werden aus Blockchiffren gebaut, wie Rijndael mit OFB. Einige, wie Salsa20 und ChaCha, werden nicht aus Blockchiffren erstellt. Man könnte letztere **primitive Stromchiffren** nennen. (Es gibt wirklich keinen standardisierten Begriff, um solche Stromchiffren zu bezeichnen.)

Wenn Leute über die Vor- und Nachteile von Stromchiffren und Blockchiffren sprechen, vergleichen sie typischerweise primitive Stromchiffren mit Verschlüsselungsschemata, die auf Blockchiffren basieren.

Während Sie immer leicht eine Stromchiffre aus einer Blockchiffre konstruieren können, ist es typischerweise sehr schwierig, irgendeine Art von Konstrukt mit einem Blockmodus der Verschlüsselung (wie mit dem CBC-Modus) aus einer primitiven Stromchiffre zu bauen.

Aus dieser Diskussion sollten Sie nun *Abbildung 8* verstehen. Sie bietet einen Überblick über symmetrische Verschlüsselungsschemata. Wir verwenden drei Arten von Verschlüsselungsschemata: primitive Stromchiffren, Blockchiffre-Stromchiffren und Blockchiffren in einem Blockmodus (auch „Blockchiffren“ im Diagramm genannt).

*Abbildung 8: Überblick über symmetrische Verschlüsselungsschemata*

![Abbildung 8: Überblick über symmetrische Verschlüsselungsschemata](assets/Figure4-8.webp "Abbildung 8: Überblick über symmetrische Verschlüsselungsschemata")

## Nachrichtenauthentifizierungscodes
<chapterId>19fa7c00-db59-56a0-9654-5350a137939d</chapterId>
Verschlüsselung beschäftigt sich mit Geheimhaltung. Aber Kryptografie befasst sich auch mit breiteren Themen, wie Nachrichtenintegrität, Authentizität und Nichtabstreitbarkeit. Sogenannte **Message Authentication Codes** (MACs) sind symmetrische kryptografische Verfahren, die Authentizität und Integrität in der Kommunikation unterstützen.

Warum ist etwas anderes als Geheimhaltung in der Kommunikation notwendig? Nehmen wir an, Bob sendet Alice eine Nachricht mit praktisch unknackbarer Verschlüsselung. Jeder Angreifer, der diese Nachricht abfängt, wird keine bedeutenden Einblicke in den Inhalt erhalten können. Dennoch hat der Angreifer mindestens zwei andere Angriffsvektoren zur Verfügung:

1. Sie könnte den Ciphertext abfangen, dessen Inhalt ändern und den veränderten Ciphertext an Alice weiterleiten.
2. Sie könnte Bobs Nachricht vollständig blockieren und ihren eigenen erstellten Ciphertext senden.

In beiden Fällen könnte der Angreifer keine Einblicke in die Inhalte aus den Ciphertexts (1) und (2) haben. Aber sie könnte auf diese Weise immer noch erheblichen Schaden anrichten. Hier werden Message Authentication Codes wichtig.

Message Authentication Codes werden locker als symmetrische kryptografische Verfahren mit drei Algorithmen definiert: einem Schlüsselerzeugungsalgorithmus, einem Tag-Erzeugungsalgorithmus und einem Verifizierungsalgorithmus. Ein sicherer MAC stellt sicher, dass Tags für jeden Angreifer **existenziell unfälschbar** sind – das heißt, sie können keinen Tag für die Nachricht erfolgreich erstellen, der verifiziert, es sei denn, sie haben den privaten Schlüssel.

Bob und Alice können die Manipulation einer bestimmten Nachricht mit einem MAC bekämpfen. Nehmen wir für den Moment an, dass sie sich nicht um Geheimhaltung kümmern. Sie möchten nur sicherstellen, dass die Nachricht, die Alice erhält, tatsächlich von Bob stammt und in keiner Weise verändert wurde.

Der Prozess ist in *Abbildung 9* dargestellt. Um einen MAC zu verwenden, würden sie zunächst einen privaten Schlüssel K generieren, der zwischen ihnen beiden geteilt wird. Bob erstellt einen Tag T für die Nachricht mit dem privaten Schlüssel K. Er sendet dann die Nachricht sowie den Nachrichtentag an Alice. Sie kann dann verifizieren, dass Bob tatsächlich den Tag erstellt hat, indem sie den privaten Schlüssel, die Nachricht und den Tag durch einen Verifizierungsalgorithmus laufen lässt.

*Abbildung 9: Übersicht über symmetrische Verschlüsselungsverfahren*

![Abbildung 9: Übersicht über symmetrische Verschlüsselungsverfahren](assets/Figure4-9.webp "Abbildung 9: Übersicht über symmetrische Verschlüsselungsverfahren")

Aufgrund der existenziellen Unfälschbarkeit kann ein Angreifer die Nachricht M in keiner Weise ändern oder eine eigene Nachricht mit einem gültigen Tag erstellen. Dies gilt selbst dann, wenn der Angreifer die Tags vieler Nachrichten zwischen Bob und Alice beobachtet, die denselben privaten Schlüssel verwenden. Höchstens könnte ein Angreifer verhindern, dass Alice die Nachricht M erhält (ein Problem, das die Kryptografie nicht adressieren kann).

Ein MAC garantiert, dass eine Nachricht tatsächlich von Bob erstellt wurde. Diese Authentizität impliziert automatisch Nachrichtenintegrität – das heißt, wenn Bob eine Nachricht erstellt hat, dann wurde sie in keiner Weise von einem Angreifer verändert. Von hier an sollte jede Sorge um Authentifizierung automatisch als eine Sorge um Integrität verstanden werden.

Während ich eine Unterscheidung zwischen Nachrichtenauthentizität und -integrität in meiner Diskussion gezogen habe, ist es auch üblich, diese Begriffe als Synonyme zu verwenden. Sie beziehen sich dann auf die Idee von Nachrichten, die sowohl von einem bestimmten Absender erstellt wurden als auch in keiner Weise verändert wurden. In diesem Sinne werden Message Authentication Codes häufig auch als **Message Integrity Codes** bezeichnet.

## Authentifizierte Verschlüsselung
<chapterId>33f2ec9b-9fb4-5c61-8fb4-50836270a144</chapterId>
Typischerweise möchte man sowohl Geheimhaltung als auch Authentizität in der Kommunikation garantieren, und daher werden Verschlüsselungsverfahren und MAC-Verfahren normalerweise zusammen verwendet.
Ein **authentifiziertes Verschlüsselungsverfahren** ist ein Schema, das Verschlüsselung mit einem MAC auf hochsichere Weise kombiniert. Speziell muss es die Standards für existenzielle Unfälschbarkeit sowie eine sehr starke Vorstellung von Geheimhaltung erfüllen, nämlich eine, die widerstandsfähig gegen **Angriffe mit gewählten Chiffretexten** ist.<sup>[7](#footnote7)</sup>

Damit ein Verschlüsselungsverfahren widerstandsfähig gegen Angriffe mit gewählten Chiffretexten ist, muss es die Standards für **Nicht-Verformbarkeit** erfüllen: das heißt, jede Modifikation eines Chiffretexts durch einen Angreifer sollte entweder einen ungültigen Chiffretext ergeben oder einen, der zu einem Klartext entschlüsselt wird, der keine Beziehung zum ursprünglichen hat.<sup>[8](#footnote8)</sup>

Da ein authentifiziertes Verschlüsselungsverfahren sicherstellt, dass ein von einem Angreifer erstellter Chiffretext immer ungültig ist (da das Tag nicht verifiziert wird), erfüllt es die Standards für Widerstandsfähigkeit gegen Angriffe mit gewählten Chiffretexten. Interessanterweise kann man beweisen, dass ein authentifiziertes Verschlüsselungsverfahren immer aus der Kombination eines existenziell unfälschbaren MAC und eines Verschlüsselungsverfahrens, das eine weniger starke Sicherheitsvorstellung erfüllt, bekannt als **Sicherheit gegen Angriffe mit gewählten Klartexten**, erstellt werden kann.

Wir werden nicht in alle Details der Konstruktion authentifizierter Verschlüsselungsverfahren eintauchen. Aber es ist wichtig, zwei Details ihrer Konstruktion zu kennen.

Erstens, ein authentifiziertes Verschlüsselungsverfahren behandelt zuerst die Verschlüsselung und erstellt dann ein Nachrichtentag auf dem Chiffretext. Es stellt sich heraus, dass andere Ansätze – wie die Kombination des Chiffretexts mit einem Tag auf dem Klartext oder zuerst ein Tag zu erstellen und dann sowohl den Klartext als auch das Tag zu verschlüsseln – unsicher sind. Zusätzlich haben beide Operationen ihren eigenen zufällig ausgewählten privaten Schlüssel, sonst ist Ihre Sicherheit stark gefährdet.

Das oben genannte Prinzip gilt allgemeiner: *Sie sollten immer unterschiedliche Schlüssel verwenden, wenn Sie grundlegende kryptografische Schemata kombinieren*.

Ein authentifiziertes Verschlüsselungsverfahren wird in *Abbildung 10* dargestellt. Bob erstellt zuerst einen Chiffretext C aus der Nachricht M mit einem zufällig ausgewählten Schlüssel K<sub>C</sub>. Dann erstellt er ein Nachrichtentag T, indem er den Chiffretext und einen anderen zufällig ausgewählten Schlüssel K<sub>T</sub> durch den Tag-Generierungsalgorithmus laufen lässt. Sowohl der Chiffretext als auch das Nachrichtentag werden an Alice gesendet.

Alice überprüft nun zuerst, ob das Tag gültig ist, gegeben den Chiffretext C und den Schlüssel K<sub>T</sub>. Wenn gültig, kann sie dann die Nachricht mit dem Schlüssel K<sub>C</sub> entschlüsseln. Sie ist nicht nur von einer sehr starken Vorstellung von Geheimhaltung in ihrer Kommunikation versichert, sondern weiß auch, dass die Nachricht von Bob erstellt wurde.

*Abbildung 10: Ein authentifiziertes Verschlüsselungsverfahren*

![Abbildung 10: Ein authentifiziertes Verschlüsselungsverfahren](assets/Figure4-10.webp "Abbildung 10: Ein authentifiziertes Verschlüsselungsverfahren")

Wie werden MACs erstellt? Obwohl MACs auf mehrere Methoden erstellt werden können, ist eine gängige und effiziente Methode, sie über kryptografische Hash-Funktionen zu erstellen.

Wir werden kryptografische Hash-Funktionen in *Kapitel 6* ausführlicher einführen. Für jetzt genügt es zu wissen, dass eine **Hash-Funktion** eine effizient berechenbare Funktion ist, die Eingaben beliebiger Größe nimmt und Ausgaben fester Länge liefert. Zum Beispiel erzeugt die beliebte Hash-Funktion **SHA-256** (Secure Hash Algorithm 256) immer eine 256-Bit-Ausgabe, unabhängig von der Größe des Eingabewerts. Einige Hash-Funktionen, wie SHA-256, haben nützliche Anwendungen in der Kryptografie.
Der am häufigsten produzierte Typ eines Tags mit einer kryptografischen Hash-Funktion ist der **hash-basierte Nachrichtenauthentifizierungscode** (HMAC). Der Prozess wird in *Abbildung 11* dargestellt. Eine Partei erzeugt zwei unterschiedliche Schlüssel aus einem privaten Schlüssel K, den inneren Schlüssel K<sub>1</sub> und den äußeren Schlüssel K<sub>2</sub>. Der Klartext M oder der Chiffretext C wird dann zusammen mit dem inneren Schlüssel gehasht. Das Ergebnis T' wird dann mit dem äußeren Schlüssel gehasht, um den Nachrichtentag T zu erzeugen.
Es gibt eine Palette von Hash-Funktionen, die zur Erstellung eines HMAC verwendet werden können. Die am häufigsten verwendete Hash-Funktion ist SHA-256.

*Abbildung 11: HMAC*

![Abbildung 11: HMAC](assets/Figure4-11.webp "Abbildung 11: HMAC")

## Sichere Kommunikationssitzungen
<chapterId>c7f7dcd3-bbed-53ed-a43d-039da0f180c5</chapterId>

Nehmen wir an, dass zwei Parteien in einer Kommunikationssitzung sind, sodass sie mehrere Nachrichten hin und her senden.

Ein Authentifizierungsschema für Verschlüsselung ermöglicht es einem Empfänger einer Nachricht zu überprüfen, ob sie von seinem Partner in der Kommunikationssitzung erstellt wurde (solange der private Schlüssel nicht durchgesickert ist). Dies funktioniert gut genug für eine einzelne Nachricht. Typischerweise senden jedoch zwei Parteien Nachrichten hin und her in einer Kommunikationssitzung. Und in diesem Setting bietet ein einfaches Authentifizierungsschema für Verschlüsselung, wie im vorherigen Abschnitt beschrieben, keinen ausreichenden Schutz.

Der Hauptgrund ist, dass ein Authentifizierungsschema für Verschlüsselung keine Garantien dafür bietet, dass die Nachricht tatsächlich auch von dem Agenten gesendet wurde, der sie innerhalb einer Kommunikationssitzung erstellt hat. Betrachten Sie die folgenden drei Angriffsvektoren:

1. **Replay-Angriff**: Ein Angreifer sendet einen Chiffretext und einen Tag, den er zu einem früheren Zeitpunkt zwischen zwei Parteien abgefangen hat, erneut.
2. **Reihenfolge-Angriff**: Ein Angreifer fängt zwei Nachrichten zu unterschiedlichen Zeiten ab und sendet sie in umgekehrter Reihenfolge an den Empfänger.
3. **Reflexionsangriff**: Ein Angreifer beobachtet eine Nachricht, die von A nach B gesendet wurde, und sendet diese Nachricht auch an A.

Obwohl der Angreifer keine Kenntnis vom Chiffretext hat und keine gefälschten Chiffretexte erstellen kann, können die oben genannten Angriffe dennoch erheblichen Schaden in der Kommunikation verursachen.

Nehmen wir zum Beispiel an, dass eine bestimmte Nachricht zwischen den beiden Parteien die Übertragung von finanziellen Mitteln beinhaltet. Ein Replay-Angriff könnte die Mittel ein zweites Mal übertragen. Ein einfaches Authentifizierungsschema für Verschlüsselung bietet keine Verteidigung gegen solche Angriffe.

Glücklicherweise können diese Arten von Angriffen in einer Kommunikationssitzung leicht durch die Verwendung von **Identifikatoren** und **relativen Zeitindikatoren** gemildert werden.

Identifikatoren können der Klartextnachricht vor der Verschlüsselung hinzugefügt werden. Dies würde jegliche Reflexionsangriffe verhindern. Ein relativer Zeitindikator kann zum Beispiel eine Sequenznummer in einer bestimmten Kommunikationssitzung sein. Jede Partei fügt einer Nachricht vor der Verschlüsselung eine Sequenznummer hinzu, sodass der Empfänger weiß, in welcher Reihenfolge die Nachrichten gesendet wurden. Dies eliminiert die Möglichkeit von Reihenfolge-Angriffen. Es eliminiert auch Replay-Angriffe. Jede Nachricht, die ein Angreifer weiterleitet, wird eine alte Sequenznummer haben, und der Empfänger wird wissen, dass er die Nachricht nicht noch einmal verarbeiten soll.

Um zu veranschaulichen, wie sichere Kommunikationssitzungen funktionieren, nehmen wir wieder Alice und Bob an. Sie senden insgesamt vier Nachrichten hin und her. Sie können sehen, wie ein Authentifizierungsschema für Verschlüsselung mit Identifikatoren und Sequenznummern unten in *Abbildung 11* funktionieren würde.
Die Kommunikationssitzung beginnt damit, dass Bob eine verschlüsselte Nachricht C<sub>0,B</sub> an Alice sendet, die eine Nachrichtenmarkierung T<sub>0,B</sub> enthält. Die verschlüsselte Nachricht beinhaltet die Nachricht selbst, sowie einen Identifikator (BOB) und eine Sequenznummer (0). Die Markierung T<sub>0,B</sub> wird über die gesamte verschlüsselte Nachricht erstellt. In ihren nachfolgenden Kommunikationen halten Alice und Bob dieses Protokoll aufrecht und aktualisieren bei Bedarf die Felder.
*Abbildung 12: Eine sichere Kommunikationssitzung*

![Abbildung 12: Eine sichere Kommunikationssitzung](assets/Figure4-12.webp "Abbildung 12: Eine sichere Kommunikationssitzung")


## Notizen
<chapterId>b96d38dd-c9cb-56a7-8764-4af8526bc63f</chapterId>

[^1]: Laut Seutonius wurde von Julius Caesar in seiner militärischen Kommunikation ein Verschiebechiffre mit einem konstanten Schlüsselwert von 3 verwendet. So würde A immer zu D, B immer zu E, C immer zu F und so weiter. Diese spezielle Version der Verschiebechiffre ist daher als **Caesar-Chiffre** bekannt geworden (obwohl sie im modernen Sinne des Wortes nicht wirklich eine Chiffre ist, da der Schlüsselwert konstant ist). Die Caesar-Chiffre mag im ersten Jahrhundert v. Chr. sicher gewesen sein, wenn die Feinde Roms sehr unvertraut mit Verschlüsselung waren. Aber in modernen Zeiten wäre es klarerweise kein sehr sicheres Verfahren [^1].

[^2]: Jonathan Katz und Yehuda Lindell, *Einführung in die moderne Kryptographie*, CRC Press (Boca Raton, FL: 2015), S. 7f [^2].

[^3]: Eric Raymond, „Der Kathedralen- und der Basar“, Vortrag gehalten auf dem Linux Kongress, Würzburg, Deutschland (27. Mai 1997). Es gibt eine Reihe von nachfolgenden Versionen sowie ein Buch. Meine Zitate stammen von Seite 30 im Buch: Eric Raymond, *Der Kathedralen- und der Basar: Gedanken über Linux und Open Source von einem unfreiwilligen Revolutionär*, überarbeitete Ausgabe. (2001), O’Reilly: Sebastopol, CA [^3].

[^4]: Crypto Museum, "Washington-Moskau-Hotline," 2013, verfügbar unter [Crypto Museum](https://www.cryptomuseum.com/crypto/hotline/index.htm) [^4].

[^5]: Die Bedeutung der probabilistischen Verschlüsselung wurde erstmals von Shafi Goldwasser und Silvio Micali hervorgehoben, „Probabilistische Verschlüsselung“, *Journal of Co [^5].



# RC4 und AES
<partId>a48c4a7d-0a41-523f-a4ab-1305b4430324</partId>

In diesem Kapitel werden wir die Details eines Verschlüsselungsschemas mit einem modernen primitiven Stromchiffre, RC4 (oder "Rivest-Chiffre 4"), und einem modernen Blockchiffre, AES, besprechen. Während der RC4-Chiffre als Verschlüsselungsmethode in Ungnade gefallen ist, ist AES der Standard für moderne symmetrische Verschlüsselung. Diese beiden Beispiele sollten eine bessere Vorstellung davon vermitteln, wie symmetrische Verschlüsselung unter der Haube funktioniert. 


## Der RC4-Stromchiffre
<chapterId>5caec5bd-5a77-56c9-b5e6-1e86f0d294aa</chapterId>
Um ein Gefühl dafür zu bekommen, wie moderne Pseudozufalls-Stream-Chiffren funktionieren, werde ich mich auf die RC4-Stream-Chiffre konzentrieren. Es handelt sich um eine Pseudozufalls-Stream-Chiffre, die in den Sicherheitsprotokollen für WEP- und WAP-Wireless-Access-Points sowie in TLS verwendet wurde. Da RC4 viele nachgewiesene Schwächen hat, ist sie in Ungnade gefallen. Tatsächlich verbietet die Internet Engineering Task Force nun die Verwendung von RC4-Suites durch Client- und Serveranwendungen in allen Instanzen von TLS.<sup>[3](#footnote3)</sup> Dennoch funktioniert sie gut als Beispiel, um zu veranschaulichen, wie eine primitive Stream-Chiffre funktioniert.
Zu Beginn werde ich zeigen, wie man eine Klartextnachricht mit einer Baby-RC4-Chiffre verschlüsselt. Nehmen wir an, unsere Klartextnachricht lautet „SOUP“. Die Verschlüsselung mit unserer Baby-RC4-Chiffre erfolgt dann in vier Schritten.

### Schritt 1

Zuerst definieren Sie ein Array S mit S[0] = 0 bis S[7] = 7. Ein Array bedeutet hier einfach eine veränderbare Sammlung von Werten, die durch einen Index organisiert sind, auch Liste in einigen Programmiersprachen genannt (z.B. Python). In diesem Fall läuft der Index von 0 bis 7, und die Werte laufen ebenfalls von 0 bis 7. So sieht S wie folgt aus:

- S = [0,1,2,3,4,5,6,7]

Die Werte hier sind keine ASCII-Zahlen, sondern die Dezimalwertdarstellungen von 1-Byte-Strings. So würde der Wert 2 gleich 0000 0011 sein. Die Länge des Arrays S beträgt also 8 Bytes.

### Schritt 2

Zweitens definieren Sie ein Schlüsselarray K mit einer Länge von 8 Bytes, indem Sie einen Schlüssel zwischen 1 und 8 Bytes wählen (Bruchteile von Bytes sind nicht zulässig). Da jedes Byte 8 Bits hat, können Sie für jedes Byte Ihres Schlüssels eine beliebige Zahl zwischen 0 und 255 auswählen.

Nehmen wir an, wir wählen unseren Schlüssel k als [14,48,9], sodass er eine Länge von 3 Bytes hat. Jeder Index unseres Schlüsselarrays wird dann entsprechend dem Dezimalwert für das jeweilige Element des Schlüssels in Reihenfolge gesetzt. Wenn Sie den gesamten Schlüssel durchlaufen haben, beginnen Sie wieder am Anfang, bis Sie die 8 Plätze des Schlüsselarrays gefüllt haben. Daher sieht unser Schlüsselarray wie folgt aus

- K = [14,48,9,14,48,9,14,48]

### Schritt 3

Drittens werden wir das Array S mit dem Schlüsselarray K transformieren, in einem Prozess, der als Schlüsselplanung bekannt ist. Der Prozess ist wie folgt in Pseudocode:

- Erstellen Sie Variablen j und i
- Setzen Sie die Variable j = 0
- Für jedes i von 0 bis 7:
	- Setzen Sie j = j + S[i] + K[i] mod 8
	- Tauschen Sie S[i] und S[j]

Die Transformation des Arrays S wird durch *Tabelle 1* erfasst.

Zu Beginn können Sie den Anfangszustand von S als [0,1,2,3,4,5,6,7] mit einem Anfangswert von 0 für j sehen. Dies wird mit dem Schlüsselarray [14,48,9,14,48,9,14,48] transformiert.
Die for-Schleife beginnt mit i = 0. Gemäß unserem Pseudocode oben wird der neue Wert von j zu 6 (j = j + S[0] + K[0] mod 8 = 0 + 0 + 14 mod 8 = 6 mod 8). Durch das Vertauschen von S[0] und S[6] wird der Zustand von S nach 1 Runde zu [6,1,2,3,4,5,0,7]. 
In der nächsten Zeile ist i = 1. Wenn wir die for-Schleife erneut durchlaufen, erhält j einen Wert von 7 (j = j + S[1] + K[1] mod 8 = 6 + 1 + 48 mod 8 = 55 mod 8 = 7 mod 8). Das Vertauschen von S[1] und S[7] vom aktuellen Zustand von S, [6,1,2,3,4,5,0,7], ergibt nach Runde 2 [6,7,2,3,4,5,0,1].

Wir setzen diesen Prozess fort, bis wir die letzte Zeile unten für das Array S produzieren, [6,4,1,0,3,7,5,2].

*Tabelle 1: Schlüsselplanungstabelle*

![Tabelle 1: Schlüsselplanungstabelle](assets/Table5-1.webp "Tabelle 1: Schlüsselplanungstabelle")

### Schritt 4

Als vierter Schritt erzeugen wir den Schlüsselstrom. Dies ist die pseudozufällige Zeichenfolge einer Länge, die der Nachricht entspricht, die wir senden möchten. Dies wird verwendet, um die ursprüngliche Nachricht „SOUP“ zu verschlüsseln. Da der Schlüsselstrom so lang wie die Nachricht sein muss, benötigen wir einen, der 4 Bytes lang ist.

Der Schlüsselstrom wird durch den folgenden Pseudocode erzeugt:

- Erstelle die Variablen j, i und t
- Setze j = 0
- Für jedes i des Klartextes, beginnend mit i = 1 und bis i = 4 gehend, wird jedes Byte des Schlüsselstroms wie folgt produziert:
    - j = j + S[i] mod 8
	- Tausche S[i] und S[j]
	- t = S[i] + S[j] mod 8
	- Das i-te Byte des Schlüsselstroms = S[t]

Die Berechnungen können in *Tabelle 2* verfolgt werden.

Der anfängliche Zustand von S = S = [6,4,1,0,3,7,5,2]. Wenn i = 1 gesetzt wird, wird der Wert j zu 4 (j = j + S[i] mod 8 = 0 + 4 mod 8 = 4). Wir tauschen dann S[1] und S[4], um die Transformation von S in der zweiten Zeile zu erzeugen, [6,3,1,0,4,7,5,2]. Der Wert t wird dann zu 7 (t = S[i] + S[j] mod 8 = 3 + 4 mod 8 = 7). Schließlich ist das Byte für den Schlüsselstrom dann S[7] oder 2.

Wir können dann fortfahren, die anderen Bytes zu produzieren, bis wir die folgenden vier Bytes haben: 2, 6, 3 und 7. Jedes dieser Bytes kann dann verwendet werden, um jeden Buchstaben des Klartextes, "SOUP", zu verschlüsseln.
Um zu beginnen, können wir mithilfe einer ASCII-Tabelle sehen, dass „SOUP“, kodiert durch die Dezimalwerte der zugrundeliegenden Byte-Strings, „83 79 85 80“ ist. Die Kombination mit dem Schlüsselstrom „2 6 3 2“ ergibt „85 85 88 82“, was nach einer Modulo-256-Operation gleich bleibt. In ASCII entspricht der Chiffretext „85 85 88 82“ „UUXR“. 
Was passiert, wenn das zu verschlüsselnde Wort länger als das Array S wäre? In diesem Fall transformiert sich das Array S einfach in der oben dargestellten Weise für jedes Byte i des Klartextes, bis wir eine Anzahl von Bytes im Schlüsselstrom haben, die der Anzahl der Buchstaben im Klartext entspricht.

*Tabelle 2: Generierung des Schlüsselstroms*

![Tabelle 2: Generierung des Schlüsselstroms](assets/Table5-2.webp "Tabelle 2: Generierung des Schlüsselstroms")

Das Beispiel, das wir gerade besprochen haben, ist nur eine vereinfachte Version des RC4-Stream-Ciphers. Der eigentliche RC4-Stream-Cipher hat ein S-Array von 256 Bytes Länge, nicht 8 Bytes, und einen Schlüssel, der zwischen 1 und 256 Bytes lang sein kann, nicht zwischen 1 und 8 Bytes. Das Schlüsselarray und die Schlüsselströme werden dann alle unter Berücksichtigung der 256-Byte-Länge des S-Arrays produziert. Die Berechnungen werden immens komplexer, aber die Prinzipien bleiben die gleichen. Unter Verwendung desselben Schlüssels, [14,48,9], wird die Klartextnachricht "SOUP" mit dem Standard-RC4-Cipher als 67 02 ed df im hexadezimalen Format verschlüsselt.

Ein Stream-Cipher, bei dem sich der Schlüsselstrom unabhängig von der Klartextnachricht oder dem Chiffretext aktualisiert, ist ein **synchroner Stream-Cipher**. Der Schlüsselstrom hängt nur vom Schlüssel ab. Offensichtlich ist RC4 ein Beispiel für einen synchronen Stream-Cipher, da der Schlüsselstrom keine Beziehung zum Klartext oder Chiffretext hat. Alle unsere primitiven Stream-Ciphers, die im vorherigen Kapitel erwähnt wurden, einschließlich des Shift-Ciphers, des Vigenère-Ciphers und des One-Time-Pads, waren ebenfalls von der synchronen Sorte.

Im Gegensatz dazu wird bei einem **asynchronen Stream-Cipher** der Schlüsselstrom sowohl durch den Schlüssel als auch durch vorherige Elemente des Chiffretexts erzeugt. Diese Art von Cipher wird auch als **selbstsynchronisierender Cipher** bezeichnet.

Wichtig ist, dass der mit RC4 erzeugte Schlüsselstrom wie ein One-Time-Pad behandelt werden sollte, und man kann den Schlüsselstrom nicht genau auf die gleiche Weise das nächste Mal erzeugen. Anstatt jedes Mal den Schlüssel zu ändern, ist die praktische Lösung, den Schlüssel mit einem Nonce zu kombinieren, um den Bytestrom zu erzeugen.

## AES mit einem 128-Bit-Schlüssel
<chapterId>0b30886f-e620-5b8d-807b-9d84685ca8ff</chapterId>

Wie im vorherigen Kapitel erwähnt, veranstaltete das National Institute of Standards and Technology (NIST) zwischen 1997 und 2000 einen Wettbewerb, um einen neuen symmetrischen Verschlüsselungsstandard zu bestimmen. Der Rijndael-Cipher erwies sich als der Gewinner. Der Name ist ein Wortspiel mit den Namen der belgischen Erfinder, Vincent Rijmen en Joan Daemen.

Der Rijndael-Cipher ist ein Block-Cipher, was bedeutet, dass es einen Kernalgorithmus gibt, der mit verschiedenen Spezifikationen für Schlüssellängen und Blockgrößen verwendet werden kann. Man kann ihn dann mit verschiedenen Betriebsmodi verwenden, um Verschlüsselungsschemata zu konstruieren.
Das Komitee für den NIST-Wettbewerb hat eine eingeschränkte Version des Rijndael-Verschlüsselungsverfahrens angenommen – nämlich eine, die 128-Bit-Blockgrößen und Schlüssellängen von entweder 128 Bits, 192 Bits oder 256 Bits erfordert – als Teil des Advanced Encryption Standard (AES). Diese eingeschränkte Version des Rijndael-Verschlüsselungsverfahrens kann auch unter mehreren Betriebsmodi verwendet werden. Die Spezifikation für den Standard ist bekannt als der Advanced Encryption Standard (AES).

Um zu zeigen, wie das Rijndael-Verschlüsselungsverfahren funktioniert, den Kern von AES, werde ich den Prozess für die Verschlüsselung mit einem 128-Bit-Schlüssel illustrieren. Die Schlüsselgröße hat einen Einfluss auf die Anzahl der Runden, die für jeden Block der Verschlüsselung gehalten werden. Für 128-Bit-Schlüssel sind 10 Runden erforderlich. Mit 192 Bits und 256 Bits wären es jeweils 12 und 14 Runden gewesen.

Zusätzlich werde ich annehmen, dass AES im ECB-Modus verwendet wird. Das macht die Darstellung etwas einfacher und spielt für das Rijndael-Algorithmus keine Rolle. Sicher ist der ECB-Modus in der Praxis nicht sicher, da er zu deterministischer Verschlüsselung führt. Der am häufigsten verwendete sichere Modus mit AES ist CBC.

Nennen wir den Schlüssel K<sub>0</sub>. Die Konstruktion mit den oben genannten Parametern sieht dann aus wie in Abbildung 1, wo M<sub>i</sub> für einen Teil der Klartextnachricht von 128 Bits und C<sub>i</sub> für einen Teil des Chiffretexts von 128 Bits steht. Padding wird dem Klartext für den letzten Block hinzugefügt, wenn der Klartext nicht gleichmäßig durch die Blockgröße geteilt werden kann.

*Abbildung 1: AES-ECB mit einem 128-Bit-Schlüssel*

![Abbildung 1: AES-ECB mit einem 128-Bit-Schlüssel](assets/Figure5-1.webp "Abbildung 1: AES-ECB mit einem 128-Bit-Schlüssel")

Jeder 128-Bit-Block des Textes durchläuft zehn Runden im Rijndael-Verschlüsselungsschema. Dies erfordert einen separaten Rundenschlüssel für jede Runde (K<sub>1</sub> bis K<sub>10</sub>). Diese werden für jede Runde aus dem ursprünglichen 128-Bit-Schlüssel K<sub>0</sub> mittels eines Schlüsselerweiterungsalgorithmus produziert. Daher werden wir für jeden zu verschlüsselnden Textblock den ursprünglichen Schlüssel K<sub>0</sub> sowie zehn separate Rundenschlüssel verwenden. Beachten Sie, dass diese gleichen 11 Schlüssel für jeden 128-Bit-Block des Klartextes verwendet werden, der verschlüsselt werden muss.

Der Schlüsselerweiterungsalgorithmus ist lang und komplex. Sich damit zu beschäftigen, hat wenig didaktischen Nutzen. Sie können sich den Schlüsselerweiterungsalgorithmus selbst ansehen, wenn Sie möchten. Sobald die Rundenschlüssel produziert sind, wird das Rijndael-Verschlüsselungsverfahren den ersten 128-Bit-Block des Klartextes, M<sub>1</sub>, manipulieren, wie in Abbildung 2 zu sehen ist. Wir werden nun diese Schritte durchgehen.

*Abbildung 2: Die Manipulation von M<sub>1</sub> mit dem Rijndael-Verschlüsselungsverfahren*

![Abbildung 2: AES-ECB mit einem 128-Bit-Schlüssel](assets/Figure5-2.webp "Abbildung 2: AES-ECB mit einem 128-Bit-Schlüssel")

### Runde 0

Runde 0 des Rijndael-Verschlüsselungsverfahrens ist unkompliziert. Ein Array S<sub>0</sub> wird durch eine XOR-Operation zwischen dem 128-Bit-Klartext und dem privaten Schlüssel erzeugt. Das heißt,

- S<sub>0</sub> = M<sub>1</sub> XOR K<sub>0</sub>

### Runde 1
In Runde 1 wird das Array S<sub>0</sub> zunächst mit dem Rundenschlüssel K<sub>1</sub> mittels einer XOR-Operation kombiniert. Dies führt zu einem neuen Zustand von S. 
Zweitens wird die Byte-Substitutionsoperation auf dem aktuellen Zustand von S durchgeführt. Dabei wird jedes Byte des 16-Byte großen S-Arrays genommen und durch ein Byte eines Arrays ersetzt, das **Rijndael’s S-Box** genannt wird. Jedes Byte erfährt eine einzigartige Transformation, und als Ergebnis wird ein neuer Zustand von S erzeugt. Rijndael's S-Box wird in *Abbildung 3* dargestellt.

*Abbildung 3: Rijndael's S-Box*

![Abbildung 3: Rijndael's S-Box](assets/Figure5-3.webp "Abbildung 3: Rijndael's S-Box")

Diese S-Box ist eine Stelle, an der abstrakte Algebra im Rijndael-Chiffre zum Einsatz kommt, speziell Galois-Felder.

Zunächst definiert man jedes mögliche Byte-Element von 00 bis FF als einen 8-Bit-Vektor. Jeder solche Vektor ist ein Element des Galois-Feldes GF(2<sup>8</sup>), wobei das irreduzible Polynom für die Modulo-Operation x<sup>8</sup> + x<sup>4</sup> + x<sup>3</sup> + x + 1 ist. Das Galois-Feld mit diesen Spezifikationen wird auch Rijndael’s Endliches Feld genannt.

Als Nächstes erstellen wir für jedes mögliche Element im Feld das, was als **Nyberg S-Box** bezeichnet wird. In dieser Box wird jedes Byte auf sein multiplikatives Inverses abgebildet (d.h., so dass ihr Produkt gleich 1 ist). Dann werden diese Werte aus der Nyberg S-Box mittels der affinen Transformation auf Rijndael’s S-Box abgebildet.

Die dritte Operation am S-Array ist die Zeilenverschiebungsoperation. Sie nimmt den Zustand von S und listet alle sechzehn Bytes in einer Matrix auf. Das Befüllen der Matrix beginnt oben links und arbeitet sich durch, indem von oben nach unten gegangen wird und dann, jedes Mal wenn eine Spalte gefüllt ist, eine Spalte nach rechts und nach oben verschoben wird.

Sobald die Matrix von S konstruiert wurde, werden die vier Reihen verschoben. Die erste Reihe bleibt gleich. Die zweite Reihe bewegt sich eins nach links. Die dritte bewegt sich zwei nach links. Die vierte bewegt sich drei nach links. Ein Beispiel des Prozesses wird in *Abbildung 4* gegeben. Der ursprüngliche Zustand von S wird oben gezeigt, der resultierende Zustand nach der Zeilenverschiebungsoperation wird darunter gezeigt.

*Abbildung 4: Zeilenverschiebungsoperation*

![Abbildung 4: Zeilenverschiebungsoperation](assets/Figure5-4.webp "Abbildung 4: Zeilenverschiebungsoperation")

Im vierten Schritt kommen Galois-Felder wieder ins Spiel. Zunächst wird jede Spalte der S-Matrix mit der Spalte der 4 x 4 Matrix, die in *Abbildung 5* zu sehen ist, multipliziert. Aber anstatt einer regulären Matrixmultiplikation handelt es sich um eine Vektormultiplikation modulo eines irreduziblen Polynoms, x<sup>8</sup> + x<sup>4</sup> + x<sup>3</sup> + x + 1. Die resultierenden Vektorkoeffizienten repräsentieren die einzelnen Bits eines Bytes.

*Abbildung 5: Mix-Spalten-Matrix*

![Abbildung 5: Mix-Spalten-Matrix](assets/Figure5-5.webp "Abbildung 5: Mix-Spalten-Matrix")

Die Multiplikation der ersten Spalte der S-Matrix mit der oben genannten 4 x 4 Matrix ergibt das Ergebnis in *Abbildung 6*.
*Abbildung 6: Multiplikation der ersten Spalte*
![Abbildung 6: Multiplikation der ersten Spalte](assets/Figure5-6.webp "Abbildung 6: Multiplikation der ersten Spalte")

Als nächster Schritt müssen alle Terme in der Matrix in Polynome umgewandelt werden. Zum Beispiel repräsentiert F1 1 Byte und würde zu x<sup>7</sup> + x<sup>6</sup> + x<sup>5</sup> + x<sup>4</sup> + 1 werden und 03 repräsentiert 1 Byte und würde zu x + 1 werden.

Alle Multiplikationen werden dann modulo x<sup>8</sup> + x<sup>4</sup> + x<sup>3</sup> + x + 1 durchgeführt. Dies führt zur Addition von vier Polynomen in jeder der vier Zellen der Spalte. Nachdem diese Additionen modulo 2 durchgeführt wurden, erhält man vier Polynome. Jedes dieser Polynome repräsentiert eine 8-Bit-Zeichenfolge oder 1 Byte von S. Wir werden diese Berechnungen hier in *Abbildung 6* nicht durchführen, da sie umfangreich sind.

Sobald die erste Spalte verarbeitet wurde, werden die anderen drei Spalten der S-Matrix auf die gleiche Weise verarbeitet. Letztendlich ergibt dies eine Matrix mit sechzehn Bytes, die in ein Array umgewandelt werden kann.

Als letzter Schritt wird das Array S erneut mit dem Rundenschlüssel in einer XOR-Operation kombiniert. Dies erzeugt den Zustand S<sub>1</sub>. Das heißt,

- S<sub>1</sub> = S XOR K<sub>0</sub>

### Runden 2 bis 10

Die Runden 2 bis 9 sind lediglich eine Wiederholung der ersten Runde, *mutatis mutandis*. Die letzte Runde ähnelt den vorherigen Runden, außer dass der Schritt "Spalten mischen" entfällt. Das heißt, Runde 10 wird wie folgt ausgeführt:

- S<sub>9</sub> XOR K<sub>10</sub>
- Byte-Substitution
- Zeilen verschieben
- S<sub>10</sub> = S XOR K<sub>10</sub>

Der Zustand S<sub>10</sub> ist nun auf C<sub>1</sub> gesetzt, die ersten 128 Bits des Chiffretexts. Die Bearbeitung der verbleibenden 128-Bit-Plaintextblöcke ergibt den vollständigen Chiffretext C.

### Die Operationen des Rijndael-Chiffre

Was ist die Begründung für die verschiedenen Operationen im Rijndael-Chiffre?

Ohne auf Details einzugehen, werden Verschlüsselungsschemata auf der Grundlage bewertet, inwieweit sie Verwirrung und Streuung erzeugen. Wenn das Verschlüsselungsschema einen hohen Grad an **Verwirrung** aufweist, bedeutet dies, dass der Chiffretext drastisch anders aussieht als der Plaintext. Wenn das Verschlüsselungsschema einen hohen Grad an **Streuung** aufweist, bedeutet dies, dass jede kleine Änderung am Plaintext einen drastisch anderen Chiffretext erzeugt.

Die Begründung für die Operationen hinter dem Rijndael-Chiffre ist, dass sie sowohl einen hohen Grad an Verwirrung als auch an Streuung erzeugen. Die Verwirrung wird durch die Byte-Substitutionsoperation erzeugt, während die Streuung durch die Operationen "Zeilen verschieben" und "Spalten mischen" erzeugt wird.

# Asymmetrische Kryptographie
<partId>868bd9dd-6e1c-5ea9-9ece-54affc13ba05</partId>

Wie bei der symmetrischen Kryptographie können asymmetrische Schemata sowohl zur Gewährleistung von Geheimhaltung als auch von Authentizität verwendet werden. Im Gegensatz dazu verwenden diese Schemata jedoch zwei Schlüssel anstatt eines: einen privaten und einen öffentlichen Schlüssel.
Wir beginnen unsere Untersuchung mit der Entdeckung der asymmetrischen Kryptografie, insbesondere den Problemen, die sie vorangetrieben haben. Als Nächstes diskutieren wir, wie asymmetrische Verschlüsselungs- und Authentifizierungsschemata auf hoher Ebene funktionieren. Dann führen wir Hash-Funktionen ein, die für das Verständnis asymmetrischer Authentifizierungsschemata entscheidend sind und auch in anderen kryptografischen Kontexten relevant sind, wie zum Beispiel für die hash-basierten Nachrichtenauthentifizierungscodes, die wir in Kapitel 4 besprochen haben.

## Das Problem der Schlüsselverteilung und -verwaltung
<chapterId>1bb651ba-689a-5a89-a7d3-0b9cc3b694f7</chapterId>

Nehmen wir an, Bob möchte einen neuen Regenmantel von Jim’s Sporting Goods, einem Online-Sportartikelhändler mit Millionen von Kunden in Nordamerika, kaufen. Dies wäre sein erster Kauf bei ihnen, und er möchte seine Kreditkarte verwenden. Also muss Bob zunächst ein Konto bei Jim’s Sporting Goods erstellen, was das Senden persönlicher Details wie seiner Adresse und Kreditkarteninformationen erfordert. Dann kann er die notwendigen Schritte durchgehen, um den Regenmantel zu kaufen.

Bob und Jim’s Sporting Goods möchten sicherstellen, dass ihre Kommunikation während dieses Prozesses sicher ist, in Anbetracht dessen, dass das Internet ein offenes Kommunikationssystem ist. Sie möchten zum Beispiel sicherstellen, dass kein potenzieller Angreifer Bobs Kreditkarten- und Adressdetails herausfinden kann und dass kein potenzieller Angreifer seine Käufe wiederholen oder gefälschte in seinem Namen erstellen kann.

Ein fortgeschrittenes authentifiziertes Verschlüsselungsschema, wie im vorherigen Kapitel besprochen, könnte die Kommunikation zwischen Bob und Jim’s Sporting Goods sicherlich sichern. Aber es gibt offensichtlich praktische Hindernisse bei der Implementierung eines solchen Schemas.

Um diese praktischen Hindernisse zu veranschaulichen, nehmen wir an, wir lebten in einer Welt, in der nur die Werkzeuge der symmetrischen Kryptografie existierten. Was könnten Jim’s Sporting Goods und Bob dann tun, um eine sichere Kommunikation zu gewährleisten?

Unter diesen Umständen würden sie erhebliche Kosten für die sichere Kommunikation tragen. Da das Internet ein offenes Kommunikationssystem ist, können sie nicht einfach einen Satz Schlüssel darüber austauschen. Daher müssten Bob und ein Vertreter von Jim’s Sporting Goods einen Schlüsselaustausch persönlich durchführen.

Eine Möglichkeit ist, dass Jim’s Sporting Goods spezielle Schlüsselaustauschorte erstellt, wo Bob und andere neue Kunden einen Satz Schlüssel für sichere Kommunikation abholen können. Dies würde offensichtlich erhebliche organisatorische Kosten verursachen und die Effizienz, mit der neue Kunden Einkäufe tätigen können, stark reduzieren.

Alternativ könnte Jim’s Sporting Goods Bob ein Paar Schlüssel mit einem hochvertrauenswürdigen Kurier senden. Dies ist wahrscheinlich effizienter als die Organisation von Schlüsselaustauschorten. Aber dies würde immer noch erhebliche Kosten verursachen, insbesondere wenn viele Kunden nur ein oder wenige Käufe tätigen.

Weiterhin zwingt ein symmetrisches Schema für authentifizierte Verschlüsselung Jim’s Sporting Goods dazu, separate Sätze von Schlüsseln für all ihre Kunden zu speichern. Dies wäre eine signifikante praktische Herausforderung für Tausende von Kunden, geschweige denn Millionen.

Um diesen letzten Punkt zu verstehen, nehmen wir an, Jim’s Sporting Goods würde jedem Kunden dasselbe Paar Schlüssel zur Verfügung stellen. Dies würde jedem Kunden – oder jedem anderen, der dieses Paar Schlüssel erhalten könnte – ermöglichen, alle Kommunikationen zwischen Jim’s Sporting Goods und seinen Kunden zu lesen und sogar zu manipulieren. Man könnte dann genauso gut auf Kryptografie in der Kommunikation verzichten.

Sogar die Wiederholung eines Satzes von Schlüsseln für nur einige Kunden ist eine schreckliche Sicherheitspraxis. Jeder potenzielle Angreifer könnte versuchen, diese Eigenschaft des Schemas auszunutzen (denken Sie daran, dass Angreifer gemäß dem Prinzip von Kerckhoffs alles über ein Schema außer den Schlüsseln wissen).

Also müsste Jim’s Sporting Goods ein Paar Schlüssel für jeden Kunden speichern, unabhängig davon, wie diese Schlüsselpaare verteilt werden. Dies stellt offensichtlich mehrere praktische Probleme dar.

- Jim’s Sporting Goods müsste Millionen von Schlüsselpaaren speichern, einen Satz für jeden Kunden.
- Diese Schlüssel müssten ordnungsgemäß gesichert werden, da sie ein sicheres Ziel für Hacker darstellen würden. Jede Sicherheitsverletzung würde die Wiederholung kostspieliger Schlüsselaustausche erfordern, entweder an speziellen Schlüsselaustauschorten oder per Kurier. - Jeder Kunde von Jim’s Sporting Goods müsste zu Hause ein Paar Schlüssel sicher aufbewahren. Verluste und Diebstähle werden auftreten, was eine Wiederholung des Schlüsselaustauschs erforderlich macht. Kunden müssten diesen Prozess auch für alle anderen Online-Shops oder andere Arten von Entitäten durchlaufen, mit denen sie über das Internet kommunizieren und Transaktionen durchführen möchten.

Diese beiden gerade beschriebenen Hauptprobleme waren bis Ende der 1970er Jahre sehr grundlegende Bedenken. Sie waren bekannt als das **Schlüsselverteilungsproblem** und das **Schlüsselverwaltungsproblem**.

Diese Probleme hatten natürlich immer existiert und in der Vergangenheit oft Kopfschmerzen bereitet. Militärische Kräfte beispielsweise mussten ständig Bücher mit Schlüsseln für sichere Kommunikation an Personal im Feld unter großen Risiken und Kosten verteilen. Aber diese Probleme verschlimmerten sich, da die Welt zunehmend in eine Ära der Fernkommunikation, insbesondere für nichtstaatliche Entitäten, überging.

Hätten diese Probleme in den 1970er Jahren nicht gelöst werden können, wäre ein effizientes und sicheres Einkaufen bei Jim’s Sporting Goods wahrscheinlich nicht existent gewesen. Tatsächlich wäre unsere moderne Welt mit praktischem und sicherem E-Mail-Verkehr, Online-Banking und Einkaufen wahrscheinlich nur eine ferne Fantasie gewesen. Etwas, das auch nur entfernt Bitcoin ähnelt, hätte überhaupt nicht existieren können.

Was also geschah in den 1970er Jahren? Wie ist es möglich, dass wir heute sofort online Einkäufe tätigen und sicher im World Wide Web surfen können? Wie ist es möglich, dass wir augenblicklich Bitcoins von unseren Smartphones aus in die ganze Welt senden können?

## Neue Richtungen in der Kryptographie
<chapterId>7a9dd9a3-496e-5f9d-93e0-b5028a7dd0f1</chapterId>

In den 1970er Jahren hatten die Probleme der Schlüsselverteilung und Schlüsselverwaltung die Aufmerksamkeit einer Gruppe amerikanischer akademischer Kryptographen erregt: Whitfield Diffie, Martin Hellman und Ralph Merkle. Trotz erheblicher Skepsis von der Mehrheit ihrer Kollegen wagten sie es, eine Lösung dafür zu finden.

Mindestens eine primäre Motivation für ihr Vorhaben war die Weitsicht, dass offene Computerkommunikation unsere Welt tiefgreifend beeinflussen würde. Wie Diffie und Hellman 1976 anmerkten,

> Die Entwicklung von computergesteuerten Kommunikationsnetzwerken verspricht mühelosen und kostengünstigen Kontakt zwischen Menschen oder Computern auf gegenüberliegenden Seiten der Welt und ersetzt die meisten Briefe und viele Ausflüge durch Telekommunikation. Für viele Anwendungen müssen diese Kontakte sowohl gegen Lauschangriffe als auch gegen die Einspeisung illegitimer Nachrichten gesichert werden. Derzeit hinkt jedoch die Lösung von Sicherheitsproblemen weit hinter anderen Bereichen der Kommunikationstechnologie hinterher. *Die zeitgenössische Kryptographie kann die Anforderungen nicht erfüllen, da ihre Nutzung solch schwere Unannehmlichkeiten für die Systemnutzer mit sich bringen würde, dass viele Vorteile der Televerarbeitung eliminiert würden.*<sup>[1](#footnote1)</sup>

Die Hartnäckigkeit von Diffie, Hellman und Merkle zahlte sich aus. Die erste Veröffentlichung ihrer Ergebnisse war ein Artikel von Diffie und Hellman im Jahr 1976 mit dem Titel „New Directions in Cryptography“. Darin präsentierten sie zwei originelle Wege, um die Probleme der Schlüsselverteilung und der Schlüsselverwaltung anzugehen.
Die erste Lösung, die sie anboten, war ein entferntes *Schlüsselaustauschprotokoll*, das heißt, ein Satz von Regeln für den Austausch von einem oder mehreren symmetrischen Schlüsseln über einen unsicheren Kommunikationskanal. Dieses Protokoll ist heute als *Diffie-Helmann-Schlüsselaustausch* oder *Diffie-Helmann-Merkle-Schlüsselaustausch* bekannt.<sup>[2](#footnote2)</sup>
Mit dem Diffie-Helmann-Schlüsselaustausch tauschen zwei Parteien zunächst einige Informationen öffentlich über einen unsicheren Kanal wie das Internet aus. Auf der Grundlage dieser Informationen erstellen sie dann unabhängig voneinander einen symmetrischen Schlüssel (oder ein Paar symmetrischer Schlüssel) für die sichere Kommunikation. Obwohl beide Parteien ihre Schlüssel unabhängig voneinander erstellen, stellt die öffentlich geteilte Information sicher, dass dieser Schlüsselerstellungsprozess für beide das gleiche Ergebnis liefert.

Wichtig ist, dass, obwohl jeder die Informationen beobachten kann, die von den Parteien über den unsicheren Kanal öffentlich ausgetauscht werden, nur die beiden am Informationsaustausch beteiligten Parteien symmetrische Schlüssel daraus erstellen können.

Das klingt natürlich völlig kontraintuitiv. Wie könnten zwei Parteien einige Informationen öffentlich austauschen, die es nur ihnen ermöglichen, symmetrische Schlüssel daraus zu erstellen? Warum sollte jemand anderes, der den Informationsaustausch beobachtet, nicht in der Lage sein, die gleichen Schlüssel zu erstellen?

Es beruht natürlich auf einiger schöner Mathematik. Der Diffie-Helmann-Schlüsselaustausch funktioniert über eine Einwegfunktion mit einer Falltür. Lassen Sie uns die Bedeutung dieser beiden Begriffe der Reihe nach besprechen.

Nehmen wir an, Ihnen wird eine Funktion f(x) und das Ergebnis f(a) = y gegeben, wobei a ein bestimmter Wert für x ist. Wir sagen, dass f(x) eine **Einwegfunktion** ist, wenn es einfach ist, den Wert y zu berechnen, wenn a und f(x) gegeben sind, aber es rechnerisch nicht machbar ist, den Wert a zu berechnen, wenn y und f(x) gegeben sind. Der Name Einwegfunktion stammt natürlich daher, dass eine solche Funktion nur praktisch in eine Richtung zu berechnen ist.

Einige Einwegfunktionen haben das, was als Falltür bekannt ist. Während es praktisch unmöglich ist, a zu berechnen, wenn nur y und f(x) gegeben sind, gibt es ein bestimmtes Stück Information Z, das es rechnerisch machbar macht, a aus y zu berechnen. Dieses Stück Information Z ist als die **Falltür** bekannt. Einwegfunktionen, die eine Falltür haben, sind als **Falltürfunktionen** bekannt.

Wir werden hier nicht auf die Details des Diffie-Helmann-Schlüsselaustauschs eingehen. Aber im Wesentlichen erstellt jeder Teilnehmer einige Informationen, von denen ein Teil öffentlich geteilt und von denen einige geheim bleiben. Jede Partei nimmt dann ihr geheimes Stück Information und die von der anderen Partei geteilten öffentlichen Informationen, um einen privaten Schlüssel zu erstellen. Und irgendwie wie durch ein Wunder enden beide Parteien mit demselben privaten Schlüssel.

Jede Partei, die nur die öffentlich geteilten Informationen zwischen den beiden Parteien in einem Diffie-Helmann-Schlüsselaustausch beobachtet, ist nicht in der Lage, diese Berechnungen zu replizieren. Sie würden die privaten Informationen von einer der beiden Parteien benötigen, um dies zu tun.

Obwohl die Basisversion des Diffie-Helmann-Schlüsselaustauschs, die im Jahr 1976 vorgestellt wurde, nicht sehr sicher ist, sind ausgefeilte Versionen des Basisprotokolls heute sicherlich noch in Gebrauch. Am wichtigsten ist, dass jedes Schlüsselaustauschprotokoll in der neuesten Version des Transport Layer Security-Protokolls (Version 1.3) im Wesentlichen eine bereicherte Version des Protokolls ist, das von Diffie und Hellman im Jahr 1976 vorgestellt wurde. Das Transport Layer Security-Protokoll ist das vorherrschende Protokoll für den sicheren Austausch von Informationen, die gemäß dem Hypertext Transfer Protocol (http) formatiert sind, dem Standard für den Austausch von Webinhalten.
Wichtig ist, dass der Diffie-Hellman-Schlüsselaustausch kein asymmetrisches Schema ist. Streng genommen gehört er wohl eher in den Bereich der symmetrischen Schlüsselkryptografie. Da jedoch sowohl der Diffie-Hellman-Schlüsselaustausch als auch die asymmetrische Kryptografie auf einseitigen zahlentheoretischen Funktionen mit Falltüren basieren, werden sie typischerweise gemeinsam diskutiert.
Der zweite Weg, den Diffie und Hellman in ihrem Paper von 1976 vorschlugen, um das Problem der Schlüsselverteilung und -verwaltung anzugehen, war natürlich durch asymmetrische Kryptografie.

Im Gegensatz zu ihrer Darstellung des Diffie-Hellman-Schlüsselaustauschs lieferten sie nur die allgemeinen Umrisse, wie asymmetrische kryptografische Schemata plausibel konstruiert werden könnten. Sie boten keine spezifische Einwegfunktion an, die die Bedingungen für eine vernünftige Sicherheit in solchen Schemata speziell erfüllen könnte.

Eine praktische Implementierung eines asymmetrischen Schemas wurde jedoch ein Jahr später von drei verschiedenen akademischen Kryptografen und Mathematikern gefunden: Ronald Rivest, Adi Shamir und Leonard Adleman. Das von ihnen eingeführte Kryptosystem wurde als das **RSA-Kryptosystem** bekannt (nach ihren Nachnamen).

Die in der asymmetrischen Kryptografie (und dem Diffie-Hellman-Schlüsselaustausch) verwendeten Falltürfunktionen stehen alle in Zusammenhang mit zwei Hauptproblemen, die **rechnerisch schwer** sind: die Primfaktorzerlegung und die Berechnung diskreter Logarithmen.

**Primfaktorzerlegung** erfordert, wie der Name schon sagt, das Zerlegen einer ganzen Zahl in ihre Primfaktoren. Das RSA-Problem ist bei weitem das bekannteste Beispiel für ein Kryptosystem, das mit der Primfaktorzerlegung zusammenhängt.

Das **Problem des diskreten Logarithmus** tritt in zyklischen Gruppen auf. Gegeben sei ein Generator in einer bestimmten zyklischen Gruppe, erfordert es die Berechnung des einzigartigen Exponenten, der benötigt wird, um ein anderes Element in der Gruppe aus dem Generator zu erzeugen.

Auf dem diskreten Logarithmus basierende Schemata stützen sich auf zwei Hauptarten von zyklischen Gruppen: multiplikative Gruppen von ganzen Zahlen und Gruppen, die die Punkte auf elliptischen Kurven umfassen. Der ursprüngliche Diffie-Hellman-Schlüsselaustausch, wie er in „New Directions in Cryptography“ vorgestellt wurde, arbeitet mit einer zyklischen multiplikativen Gruppe von ganzen Zahlen. Bitcoins digitales Signaturverfahren und das kürzlich eingeführte Schnorr-Signaturschema (2021) basieren beide auf dem Problem des diskreten Logarithmus für eine bestimmte elliptische Kurvenzyklusgruppe.

Als Nächstes werden wir uns einen Überblick über Geheimhaltung und Authentifizierung im asymmetrischen Kontext verschaffen. Zuvor müssen wir jedoch eine kurze historische Anmerkung machen.

Es scheint nun plausibel, dass eine Gruppe britischer Kryptografen und Mathematiker, die für das Government Communications Headquarters (GCHQ) arbeiteten, die oben genannten Entdeckungen einige Jahre zuvor unabhängig gemacht hatte. Diese Gruppe bestand aus James Ellis, Clifford Cocks und Malcolm Williamson.

Nach ihren eigenen Angaben und denen des GCHQ war es James Ellis, der 1969 das Konzept der Public-Key-Kryptografie entwickelte. Angeblich entdeckte Clifford Cocks dann 1973 das RSA-Kryptosystem und Malcolm Williamson 1974 das Konzept des Diffie-Hellman-Schlüsselaustauschs. Ihre Entdeckungen wurden jedoch angeblich erst 1997 bekannt gegeben, angesichts der geheimen Natur der Arbeit, die beim GCHQ geleistet wurde.

## Asymmetrische Verschlüsselung und Authentifizierung
<chapterId>2f6f0f03-3c3d-5025-90f0-5211139bc0cc</chapterId>

Ein Überblick über die asymmetrische Verschlüsselung mit Hilfe von Bob und Alice wird in *Abbildung 1* gegeben.
Alice erstellt zunächst ein Schlüsselpaar, bestehend aus einem öffentlichen Schlüssel (K<sub>P</sub>) und einem privaten Schlüssel (K<sub>S</sub>), wobei das „P“ in K<sub>P</sub> für „public“ (öffentlich) und das „S“ in K<sub>S</sub> für „secret“ (geheim) steht. Anschließend verteilt sie diesen öffentlichen Schlüssel frei an andere. Wir werden später auf die Details dieses Verteilungsprozesses zurückkommen. Aber nehmen wir vorerst an, dass jeder, einschließlich Bob, den öffentlichen Schlüssel K<sub>P</sub> von Alice sicher erhalten kann.
Zu einem späteren Zeitpunkt möchte Bob eine Nachricht M an Alice schreiben. Da sie sensible Informationen enthält, möchte er jedoch, dass der Inhalt für alle außer Alice geheim bleibt. Also verschlüsselt Bob zuerst seine Nachricht M mit K<sub>P</sub>. Dann sendet er den resultierenden Chiffretext C an Alice, die C mit K<sub>S</sub> entschlüsselt, um die ursprüngliche Nachricht M zu reproduzieren.

*Abbildung 1: Asymmetrische Verschlüsselung*

![Abbildung 1: Asymmetrische Verschlüsselung](assets/Figure6-1.webp "Abbildung 1: Asymmetrische Verschlüsselung")

Jeder Gegner, der Bobs und Alices Kommunikation abhört, kann C beobachten. Sie kennt auch K<sub>P</sub> und den Verschlüsselungsalgorithmus E(·). Wichtig ist jedoch, dass diese Informationen es dem Angreifer nicht ermöglichen, den Chiffretext C realistisch zu entschlüsseln. Zum Entschlüsseln wird spezifisch K<sub>S</sub> benötigt, welches der Angreifer nicht besitzt.

Symmetrische Verschlüsselungsverfahren müssen im Allgemeinen sicher gegen einen Angreifer sein, der gültige Klartextnachrichten verschlüsseln kann (bekannt als Sicherheit gegen Angriffe mit gewähltem Chiffretext). Sie sind jedoch nicht explizit dafür ausgelegt, die Erstellung solcher gültigen Chiffretexte durch einen Angreifer oder jemand anderen zu ermöglichen.

Dies steht im starken Kontrast zu einem asymmetrischen Verschlüsselungsverfahren, dessen ganzer Zweck es ist, jedem, einschließlich Angreifern, zu ermöglichen, gültige Chiffretexte zu produzieren. Asymmetrische Verschlüsselungsverfahren können daher als **Mehrfachzugriffs-Chiffren** bezeichnet werden.

Um besser zu verstehen, was passiert, stellen Sie sich vor, dass Bob statt eine Nachricht elektronisch zu senden, einen physischen Brief in Geheimhaltung senden wollte. Eine Möglichkeit, die Geheimhaltung zu gewährleisten, wäre, dass Alice ein sicheres Vorhängeschloss an Bob sendet, aber den Schlüssel dazu behält. Nachdem er seinen Brief geschrieben hat, könnte Bob den Brief in eine Kiste legen und diese mit Alices Vorhängeschloss verschließen. Dann könnte er die verschlossene Kiste mit der Nachricht an Alice senden, die den Schlüssel hat, um sie zu öffnen.

Während Bob in der Lage ist, das Vorhängeschloss zu verschließen, kann weder er noch eine andere Person, die die Kiste abfängt, das Vorhängeschloss öffnen, wenn es tatsächlich sicher ist. Nur Alice kann es aufschließen und den Inhalt von Bobs Brief sehen, weil sie den Schlüssel hat.

Ein asymmetrisches Verschlüsselungsverfahren ist, grob gesagt, eine digitale Version dieses Prozesses. Das Vorhängeschloss entspricht dem öffentlichen Schlüssel und der Schlüssel des Vorhängeschlosses dem privaten Schlüssel. Da das Vorhängeschloss digital ist, ist es jedoch viel einfacher und nicht so kostspielig für Alice, es an jeden zu verteilen, der ihr geheime Nachrichten senden möchte.

Für die Authentifizierung im asymmetrischen Kontext verwenden wir **digitale Signaturen**. Diese haben somit die gleiche Funktion wie Nachrichtenauthentifizierungscodes im symmetrischen Kontext. Ein Überblick über digitale Signaturen wird in *Abbildung 2* bereitgestellt.
Bob erstellt zunächst ein Schlüsselpaar, bestehend aus dem öffentlichen Schlüssel (K<sub>P</sub>) und dem privaten Schlüssel (K<sub>S</sub>), und verteilt seinen öffentlichen Schlüssel. Wenn er Alice eine authentifizierte Nachricht senden möchte, nimmt er zuerst seine Nachricht M und seinen privaten Schlüssel, um eine digitale Signatur D zu erstellen. Bob sendet dann Alice seine Nachricht zusammen mit der digitalen Signatur. Alice gibt die Nachricht, den öffentlichen Schlüssel und die digitale Signatur in einen Verifizierungsalgorithmus ein. Dieser Algorithmus liefert entweder true für eine gültige Signatur oder false für eine ungültige Signatur. 
Eine digitale Signatur ist, wie der Name klar impliziert, das digitale Äquivalent einer handschriftlichen Unterschrift auf Briefen, Verträgen und so weiter. Tatsächlich ist eine digitale Signatur in der Regel viel sicherer. Mit einigem Aufwand kann man eine handschriftliche Unterschrift fälschen; ein Prozess, der dadurch erleichtert wird, dass handschriftliche Unterschriften häufig nicht genau überprüft werden. Eine sichere digitale Signatur ist jedoch, genau wie ein sicherer Nachrichtenauthentifizierungscode, **existenziell unfälschbar**: das heißt, mit einem sicheren digitalen Signaturschema kann niemand eine Signatur für eine Nachricht erstellen, die das Verifizierungsverfahren besteht, es sei denn, sie besitzen den privaten Schlüssel.

*Abbildung 2: Asymmetrische Authentifizierung*

![Abbildung 2: Asymmetrische Authentifizierung](assets/Figure6-2.webp "Abbildung 2: Asymmetrische Authentifizierung")

Wie bei der asymmetrischen Verschlüsselung sehen wir einen interessanten Kontrast zwischen digitalen Signaturen und Nachrichtenauthentifizierungscodes. Bei letzteren kann der Verifizierungsalgorithmus nur von einer der Parteien verwendet werden, die an der sicheren Kommunikation beteiligt sind. Dies liegt daran, dass er einen privaten Schlüssel erfordert. Im asymmetrischen Setting kann jedoch jeder eine von Bob erstellte digitale Signatur S verifizieren.

All dies macht digitale Signaturen zu einem äußerst mächtigen Werkzeug. Sie bilden beispielsweise die Grundlage für das Erstellen von Signaturen auf Verträgen, die zu rechtlichen Zwecken verifiziert werden können. Wenn Bob in dem oben genannten Austausch eine Signatur auf einem Vertrag gemacht hätte, könnte Alice die Nachricht M, den Vertrag und die Signatur S einem Gericht vorlegen. Das Gericht kann dann die Signatur mit Bobs öffentlichem Schlüssel verifizieren.

Als weiteres Beispiel sind digitale Signaturen ein wichtiger Aspekt, um Software und Software-Updates sicher zu verteilen. Diese Art der öffentlichen Überprüfbarkeit könnte niemals allein mit Nachrichtenauthentifizierungscodes geschaffen werden.

Als letztes Beispiel für die Macht digitaler Signaturen betrachten Sie Bitcoin. Eines der häufigsten Missverständnisse über Bitcoin, insbesondere in den Medien, ist, dass Transaktionen verschlüsselt sind: das sind sie nicht. Stattdessen arbeiten Bitcoin-Transaktionen mit digitalen Signaturen, um Sicherheit zu gewährleisten.

Bitcoins existieren in Chargen, die als unverbrauchte Transaktionsausgänge (oder UTXOs) bezeichnet werden. Nehmen wir an, Sie erhalten drei Zahlungen auf eine bestimmte Bitcoin-Adresse von jeweils 2 Bitcoins. Technisch gesehen haben Sie jetzt nicht 6 Bitcoins auf dieser Adresse. Stattdessen haben Sie drei Chargen von 2 Bitcoins, die durch ein kryptografisches Problem, das mit dieser Adresse verbunden ist, gesperrt sind. Für jede Zahlung, die Sie leisten, können Sie eine, zwei oder alle drei dieser Chargen verwenden, je nachdem, wie viel Sie für die Transaktion benötigen.

Der Nachweis des Eigentums über unverbrauchte Transaktionsausgänge wird in der Regel über eine oder mehrere digitale Signaturen geführt. Bitcoin funktioniert genau deshalb, weil gültige digitale Signaturen auf unverbrauchten Transaktionsausgängen rechnerisch unmöglich zu erstellen sind, es sei denn, man besitzt die geheimen Informationen, die dafür benötigt werden.
Derzeit beinhalten Bitcoin-Transaktionen transparent alle Informationen, die von den Teilnehmern im Netzwerk verifiziert werden müssen, wie zum Beispiel die Herkunft der unverbrauchten Transaktionsausgänge, die in der Transaktion verwendet werden. Obwohl es möglich ist, einige dieser Informationen zu verbergen und trotzdem eine Verifizierung zu ermöglichen (wie es einige alternative Kryptowährungen wie Monero tun), entstehen dadurch auch besondere Sicherheitsrisiken.
Verwirrung entsteht manchmal über digitale Signaturen und schriftliche Signaturen, die digital erfasst werden. Im letzteren Fall erfassen Sie ein Bild Ihrer schriftlichen Signatur und fügen es an ein elektronisches Dokument, wie einen Arbeitsvertrag, an. Dies ist jedoch keine digitale Signatur im kryptografischen Sinne. Letztere ist nur eine lange Zahl, die nur durch den Besitz eines privaten Schlüssels erzeugt werden kann.

Wie im symmetrischen Schlüssel-Setting können Sie auch asymmetrische Verschlüsselungs- und Authentifizierungsschemata zusammen verwenden. Ähnliche Prinzipien gelten. Zuerst sollten Sie unterschiedliche private-öffentliche Schlüsselpaare für die Verschlüsselung und das Erstellen digitaler Signaturen verwenden. Zusätzlich sollten Sie zuerst eine Nachricht verschlüsseln und dann authentifizieren.

Wichtig ist, dass in vielen Anwendungen asymmetrische Kryptografie nicht während des gesamten Kommunikationsprozesses verwendet wird. Stattdessen wird sie typischerweise nur verwendet, um *symmetrische Schlüssel* zwischen den Parteien auszutauschen, mit denen sie tatsächlich kommunizieren werden.

Dies ist beispielsweise der Fall, wenn Sie Waren online kaufen. Wenn Sie den öffentlichen Schlüssel des Verkäufers kennen, kann er Ihnen digital signierte Nachrichten senden, deren Authentizität Sie überprüfen können. Auf dieser Basis können Sie einem von mehreren Protokollen folgen, um symmetrische Schlüssel auszutauschen, um sicher zu kommunizieren.

Der Hauptgrund für die Häufigkeit des oben genannten Ansatzes ist, dass asymmetrische Kryptografie viel weniger effizient als symmetrische Kryptografie ist, um ein bestimmtes Sicherheitsniveau zu erzeugen. Dies ist einer der Gründe, warum wir neben der öffentlichen Kryptografie immer noch symmetrische Schlüsselkryptografie benötigen. Darüber hinaus ist symmetrische Schlüsselkryptografie in bestimmten Anwendungen, wie einem Computerbenutzer, der seine eigenen Daten verschlüsselt, viel natürlicher.

Wie genau adressieren also digitale Signaturen und öffentliche Schlüsselverschlüsselung die Probleme der Schlüsselverteilung und des Schlüsselmanagements?

Es gibt hier nicht eine Antwort. Asymmetrische Kryptografie ist ein Werkzeug und es gibt nicht nur eine Möglichkeit, dieses Werkzeug zu verwenden. Aber nehmen wir unser früheres Beispiel von Jims Sportgeschäft, um zu zeigen, wie die Probleme typischerweise in diesem Beispiel angegangen würden.

Zu Beginn würde Jims Sportgeschäft wahrscheinlich eine **Zertifizierungsstelle** ansprechen, eine Organisation, die bei der Verteilung öffentlicher Schlüssel unterstützt. Die Zertifizierungsstelle würde einige Details über Jims Sportgeschäft registrieren und ihm einen öffentlichen Schlüssel gewähren. Dann würde sie Jims Sportgeschäft ein Zertifikat, bekannt als **TLS/SSL-Zertifikat**, mit dem öffentlichen Schlüssel von Jims Sportgeschäft digital signiert mit dem eigenen öffentlichen Schlüssel der Zertifizierungsstelle, senden. Auf diese Weise bestätigt die Zertifizierungsstelle, dass ein bestimmter öffentlicher Schlüssel tatsächlich zu Jims Sportgeschäft gehört.

Der Schlüssel zum Verständnis dieses Prozesses mit TLS/SSL-Zertifikaten ist, dass Sie den öffentlichen Schlüssel von Jims Sportgeschäft im Allgemeinen nirgendwo auf Ihrem Computer gespeichert haben werden, die öffentlichen Schlüssel anerkannter Zertifizierungsstellen jedoch tatsächlich in Ihrem Browser oder in Ihrem Betriebssystem gespeichert sind. Diese sind in dem, was man **Root-Zertifikate** nennt, gespeichert.

Daher, wenn Jims Sportgeschäft Ihnen sein TLS/SSL-Zertifikat zur Verfügung stellt, können Sie die digitale Signatur der Zertifizierungsstelle über ein Root-Zertifikat in Ihrem Browser oder Betriebssystem überprüfen. Wenn die Signatur gültig ist, können Sie relativ sicher sein, dass der öffentliche Schlüssel auf dem Zertifikat tatsächlich zu Jims Sportgeschäft gehört. Auf dieser Basis ist es einfach, ein Protokoll für sichere Kommunikation mit Jims Sportgeschäft einzurichten.
Die Schlüsselverteilung ist für Jim’s Sporting Goods nun wesentlich einfacher geworden. Es ist nicht schwer zu erkennen, dass auch das Schlüsselmanagement erheblich vereinfacht wurde. Anstatt Tausende von Schlüsseln speichern zu müssen, muss Jim’s Sporting Goods lediglich einen privaten Schlüssel speichern, der es ermöglicht, Signaturen für den öffentlichen Schlüssel seines SSL-Zertifikats zu erstellen. Jedes Mal, wenn ein Kunde die Seite von Jim’s Sporting Goods besucht, kann er eine sichere Kommunikationssitzung über diesen öffentlichen Schlüssel aufbauen. Kunden müssen auch keine Informationen speichern (außer den öffentlichen Schlüsseln anerkannter Zertifizierungsstellen in ihrem Betriebssystem und Browser).

## Hash-Funktionen
<chapterId>ea8327ab-b0e3-5635-941c-4b51f396a648</chapterId>

Hash-Funktionen sind allgegenwärtig in der Kryptographie. Sie sind weder symmetrische noch asymmetrische Schemata, sondern fallen in ihre eigene kryptographische Kategorie.

Wir sind bereits in Kapitel 4 auf Hash-Funktionen gestoßen, bei der Erstellung von hash-basierten Authentifizierungsnachrichten. Sie sind auch im Kontext digitaler Signaturen wichtig, allerdings aus einem etwas anderen Grund: Digitale Signaturen werden nämlich typischerweise über den Hash-Wert einer (verschlüsselten) Nachricht gemacht, anstatt über die eigentliche (verschlüsselte) Nachricht. In diesem Abschnitt werde ich eine gründlichere Einführung in Hash-Funktionen bieten.

Beginnen wir mit der Definition einer Hash-Funktion. Eine **Hash-Funktion** ist jede effizient berechenbare Funktion, die Eingaben beliebiger Größe nimmt und Ausgaben fester Länge liefert.

Eine **kryptographische Hash-Funktion** ist einfach eine Hash-Funktion, die für Anwendungen in der Kryptographie nützlich ist. Die Ausgabe einer kryptographischen Hash-Funktion wird typischerweise als **Hash**, **Hash-Wert** oder **Nachrichten-Hashwert** bezeichnet.

Im Kontext der Kryptographie bezieht sich „Hash-Funktion“ typischerweise auf eine kryptographische Hash-Funktion. Ich werde diese Praxis von nun an übernehmen.

Ein Beispiel für eine beliebte Hash-Funktion ist **SHA-256** (Secure Hash Algorithm 256). Unabhängig von der Größe der Eingabe (z.B. 15 Bits, 100 Bits oder 10.000 Bits) liefert diese Funktion einen 256-Bit-Hash-Wert. Unten können Sie einige Beispiel-Ausgaben der SHA-256-Funktion sehen.

* „Hello“: 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
* „52398“: a3b14d2bf378c1bd47e7f8eaec63b445150a3d7a80465af16dd9fd319454ba90
* „Kryptographie macht Spaß“: 3cee2a5c7d2cc1d62db4893564c34ae553cc88623992d994e114e344359b146c

Alle Ausgaben sind genau 256 Bits lang und im hexadezimalen Format geschrieben (jede Hexadezimalziffer kann durch vier Binärziffern dargestellt werden). Selbst wenn Sie das Buch *Der Herr der Ringe* von Tolkien in die SHA-256-Funktion eingegeben hätten, wäre die Ausgabe immer noch 256 Bits lang.

Hash-Funktionen wie SHA-256 werden in der Kryptographie zu verschiedenen Zwecken eingesetzt. Welche Eigenschaften von einer Hash-Funktion gefordert werden, hängt wirklich vom Kontext einer bestimmten Anwendung ab. Es gibt zwei Hauptmerkmale, die allgemein von Hash-Funktionen in der Kryptographie gewünscht werden:<sup>[6](#footnote6)</sup>

1.	Kollisionsresistenz
2.	Verbergung

Eine Hash-Funktion H wird als **kollisionsresistent** bezeichnet, wenn es unpraktikabel ist, zwei Werte x und y zu finden, sodass x ≠ y, aber H(x) = H(y).
Kollisionsresistente Hashfunktionen sind beispielsweise bei der Verifizierung von Software wichtig. Nehmen wir an, Sie möchten die Windows-Version von Bitcoin Core 0.21.0 (eine Serveranwendung zur Verarbeitung von Bitcoin-Netzwerkverkehr) herunterladen. Die Hauptschritte, die Sie unternehmen müssen, um die Legitimität der Software zu überprüfen, sind wie folgt:
1. Zuerst müssen Sie die öffentlichen Schlüssel eines oder mehrerer Bitcoin Core-Beitragenden herunterladen und in Software importieren, die digitale Signaturen verifizieren kann (z.B. Kleopetra). Diese öffentlichen Schlüssel finden Sie [hier](https://github.com/bitcoin/bitcoin/blob/master/contrib/builder-keys/keys.txt). Es wird empfohlen, die Bitcoin Core-Software mit den öffentlichen Schlüsseln mehrerer Beitragender zu verifizieren.
2. Als Nächstes müssen Sie die importierten öffentlichen Schlüssel verifizieren. Ein Schritt, den Sie mindestens unternehmen sollten, ist zu überprüfen, ob die öffentlichen Schlüssel, die Sie gefunden haben, mit denen übereinstimmen, die an verschiedenen anderen Orten veröffentlicht wurden. Sie könnten beispielsweise die persönlichen Webseiten, Twitter-Seiten oder Github-Seiten der Personen konsultieren, deren öffentliche Schlüssel Sie importiert haben. Typischerweise wird dieser Vergleich der öffentlichen Schlüssel durch Vergleichen eines kurzen Hashs des öffentlichen Schlüssels, bekannt als Fingerabdruck, durchgeführt.
3. Als Nächstes müssen Sie das ausführbare Programm für Bitcoin Core von deren [Website](www.bitcoincore.org) herunterladen. Es werden Pakete für Linux-, Windows- und MAC-Betriebssysteme verfügbar sein.
4. Als Nächstes müssen Sie zwei Release-Dateien lokalisieren. Die erste enthält den offiziellen SHA-256-Hash für das heruntergeladene ausführbare Programm zusammen mit den Hashes über alle anderen veröffentlichten Pakete. Eine andere Release-Datei wird die Signaturen verschiedener Beitragender über die Release-Datei mit den Pakethashes enthalten. Beide Release-Dateien sollten auf der Bitcoin Core-Website zu finden sein.
5. Als Nächstes müssten Sie den SHA-256-Hash des von der Bitcoin Core-Website heruntergeladenen ausführbaren Programms auf Ihrem eigenen Computer berechnen. Sie vergleichen dann dieses Ergebnis mit dem des offiziellen Pakethashs für das ausführbare Programm. Sie sollten identisch sein.
6. Schließlich müssten Sie verifizieren, dass eine oder mehrere der digitalen Signaturen über die Release-Datei mit den offiziellen Pakethashes tatsächlich einem oder mehreren öffentlichen Schlüsseln entsprechen, die Sie importiert haben (Veröffentlichungen von Bitcoin Core sind nicht immer von allen signiert). Dies können Sie mit einer Anwendung wie Kleopetra tun.

Dieser Prozess der Softwareverifizierung hat zwei Hauptvorteile. Erstens stellt er sicher, dass beim Herunterladen von der Bitcoin Core-Website keine Übertragungsfehler aufgetreten sind. Zweitens stellt er sicher, dass kein Angreifer Sie dazu bringen konnte, modifizierten, bösartigen Code herunterzuladen, entweder durch Hacking der Bitcoin Core-Website oder durch Abfangen des Verkehrs.

Wie genau schützt der oben beschriebene Softwareverifizierungsprozess vor diesen Problemen?

Wenn Sie die importierten öffentlichen Schlüssel sorgfältig verifiziert haben, können Sie ziemlich sicher sein, dass diese Schlüssel tatsächlich ihnen gehören und nicht kompromittiert wurden. Da digitale Signaturen existenzielle Unfälschbarkeit aufweisen, wissen Sie, dass nur diese Beitragenden eine digitale Signatur über die offiziellen Pakethashes auf der Release-Datei erstellt haben könnten.

Angenommen, die Signaturen auf der heruntergeladenen Release-Datei stimmen überein. Sie können nun den Hashwert, den Sie lokal für das Windows ausführbare Programm berechnet haben, das Sie heruntergeladen haben, mit dem im ordnungsgemäß signierten Release-Dokument enthaltenen vergleichen. Da Sie wissen, dass die SHA-256-Hashfunktion kollisionsresistent ist, bedeutet eine Übereinstimmung, dass Ihr ausführbares Programm genau dasselbe ist wie das offizielle ausführbare Programm.

Wenden wir uns nun der zweiten gemeinsamen Eigenschaft von Hashfunktionen zu: Verbergen. Jede Hashfunktion H wird als verbergend bezeichnet, wenn es für ein zufällig ausgewähltes x aus einem sehr großen Bereich unpraktikabel ist, x zu finden, wenn nur H(x) gegeben ist.
Unten können Sie den SHA-256-Output einer Nachricht sehen, die ich geschrieben habe. Um ausreichende Zufälligkeit zu gewährleisten, enthielt die Nachricht am Ende eine zufällig generierte Zeichenfolge. Da SHA-256 die Verbergungseigenschaft besitzt, wäre es niemandem möglich, diese Nachricht zu entschlüsseln.
* b194221b37fa4cd1cfce15aaef90351d70de17a98ee6225088b523b586c32ded

Aber ich werde Sie nicht in Spannung lassen, bis SHA-256 schwächer wird. Die ursprüngliche Nachricht, die ich geschrieben habe, lautete wie folgt:

* „Dies ist eine sehr zufällige Nachricht, oder naja, irgendwie zufällig. Dieser Anfangsteil ist es nicht, aber ich werde mit einigen relativ zufälligen Zeichen enden, um eine sehr unvorhersehbare Nachricht zu gewährleisten. XLWz4dVG3BxUWm7zQ9qS“.

Eine gängige Art und Weise, wie Hash-Funktionen mit der Verbergungseigenschaft verwendet werden, ist im Passwortmanagement (Kollisionsresistenz ist auch für diese Anwendung wichtig). Jeder anständige Online-Kontodienst wie Facebook oder Google wird Ihre Passwörter nicht direkt speichern, um den Zugang zu Ihrem Konto zu verwalten. Stattdessen speichern sie nur einen Hash Ihres Passworts. Jedes Mal, wenn Sie Ihr Passwort in einem Browser eingeben, wird zuerst ein Hash berechnet. Nur dieser Hash wird an den Server des Dienstanbieters gesendet und mit dem Hash verglichen, der in der Backend-Datenbank gespeichert ist. Die Verbergungseigenschaft kann dabei helfen sicherzustellen, dass Angreifer es nicht aus dem Hash-Wert wiederherstellen können.

Passwortmanagement über Hashes funktioniert natürlich nur, wenn Benutzer tatsächlich schwierige Passwörter wählen. Die Verbergungseigenschaft setzt voraus, dass x zufällig aus einem sehr großen Bereich gewählt wird. Die Auswahl von Passwörtern wie „1234“, „meinpasswort“ oder Ihr Geburtsdatum bietet keine echte Sicherheit. Lange Listen von gängigen Passwörtern und ihren Hashes existieren, die Angreifer nutzen können, wenn sie jemals den Hash Ihres Passworts erhalten. Diese Arten von Angriffen sind als **Wörterbuchangriffe** bekannt. Wenn Angreifer einige Ihrer persönlichen Details kennen, könnten sie auch einige informierte Vermutungen anstellen. Daher benötigen Sie immer lange, sichere Passwörter (vorzugsweise lange, zufällige Zeichenfolgen aus einem Passwortmanager).

Manchmal könnte eine Anwendung eine Hash-Funktion benötigen, die sowohl kollisionsresistent als auch verborgen ist. Aber sicherlich nicht immer. Der Software-Verifizierungsprozess, den wir besprochen haben, erfordert zum Beispiel nur, dass die Hash-Funktion Kollisionsresistenz aufweist, Verbergung ist nicht wichtig.

Während Kollisionsresistenz und Verbergung die Hauptmerkmale sind, die von Hash-Funktionen in der Kryptographie gesucht werden, könnten in bestimmten Anwendungen auch andere Arten von Eigenschaften wünschenswert sein.


### Anmerkungen
[^1]: Whitfield Diffie und Martin Hellman, „New directions in cryptography“, *IEEE Transactions on Information Theory* IT-22 (1976), S. 644–654, auf S. 644 [^1].

[^2]: Ralph Merkle diskutiert auch ein Schlüsselaustauschprotokoll in „Secure communications over insecure channels“, *Communications of the Association for Computing Machinery*, 21 (1978), 294–99. Obwohl Merkle dieses Papier vor dem von Diffie und Hellman einreichte, wurde es später veröffentlicht. Merkles Lösung ist nicht exponentiell sicher, im Gegensatz zu Diffie-Hellman [^2].

[^3]: Ron Rivest, Adi Shamir und Leonard Adleman, „A method for obtaining digital signatures and public-key cryptosystems“, *Communications of the Association for Computing Machinery*, 21 (1978), S. 120–26 [^3].

[^4]: Eine gute Geschichte dieser Entdeckungen wird von Simon Singh in *The Code Book*, Fourth Estate (London, 1999), Kapitel 6, bereitgestellt [^4].
[^5]: Alle Schemata, die Nichtabstreitbarkeit erreichen wollen, ein anderes Thema, das wir in *Kapitel 1* besprochen haben, müssen grundsätzlich digitale Signaturen einbeziehen [^5].
[^6]: Die Terminologie des „Verbergens“ ist keine allgemeine Sprache, sondern speziell entnommen aus Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller und Steven Goldfeder, *Bitcoin und Kryptowährungstechnologien*, Princeton University Press (Princeton, 2016), Kapitel 1 [^6].

# Das RSA-Kryptosystem
<partId>864dca42-2a8d-530f-bb94-2e1f68b3f411</partId>

Während symmetrische Kryptographie für die meisten Menschen in der Regel recht intuitiv ist, ist dies typischerweise nicht der Fall bei asymmetrischer Kryptographie. Obwohl Sie wahrscheinlich mit der hochrangigen Beschreibung, die in den vorherigen Abschnitten angeboten wurde, vertraut sind, fragen Sie sich wahrscheinlich, was genau Einwegfunktionen sind und wie genau sie verwendet werden, um asymmetrische Schemata zu konstruieren.

In diesem Kapitel werde ich etwas von dem Geheimnis um die asymmetrische Kryptographie lüften, indem ich tiefer in ein spezifisches Beispiel eintauche, nämlich das RSA-Kryptosystem. Im ersten Abschnitt werde ich das Faktorisierungsproblem vorstellen, auf dem das RSA-Problem basiert. Dann werde ich eine Reihe von Schlüsselergebnissen aus der Zahlentheorie abdecken. Im letzten Abschnitt werden wir diese Informationen zusammenführen, um das RSA-Problem zu erklären und wie dies für die Erstellung asymmetrischer kryptographischer Schemata verwendet werden kann.

Diese Tiefe unserer Diskussion hinzuzufügen, ist keine leichte Aufgabe. Es erfordert die Einführung von ziemlich vielen zahlentheoretischen Theoremen und Propositionen. Aber lassen Sie sich nicht von der Mathematik abschrecken. Sich durch diese Diskussion zu arbeiten, wird Ihr Verständnis von dem, was der asymmetrischen Kryptographie zugrunde liegt, erheblich verbessern und ist eine lohnende Investition.

Lassen Sie uns nun zuerst zum Faktorisierungsproblem kommen.

## Das Faktorisierungsproblem
<chapterId>a31a66e4-52ea-539c-9953-4769ad565d7e</chapterId>

Wann immer Sie zwei Zahlen multiplizieren, sagen wir a und b, bezeichnen wir die Zahlen a und b als **Faktoren** und das Ergebnis als das **Produkt**. Den Versuch, eine Zahl N in die Multiplikation von zwei oder mehr Faktoren zu schreiben, nennt man **Faktorisierung** oder **Faktorisieren**.<sup>[1](#footnote1)</sup> Jedes Problem, das dies erfordert, können Sie als **Faktorisierungsproblem** bezeichnen.

Vor etwa 2.500 Jahren entdeckte der griechische Mathematiker Euklid von Alexandria einen Schlüsselsatz über die Faktorisierung von Ganzzahlen. Er wird allgemein als **Satz von der eindeutigen Faktorisierung** bezeichnet und besagt Folgendes:

*Theorem 1*. Jede Ganzzahl N, die größer als 1 ist, ist entweder eine Primzahl oder kann als Produkt von Primfaktoren ausgedrückt werden.

Der letztere Teil dieser Aussage bedeutet einfach, dass Sie jede nicht-primäre Ganzzahl N, die größer als 1 ist, als Multiplikation von Primzahlen aufschreiben können. Unten sind mehrere Beispiele von nicht-primären Ganzzahlen aufgeführt, die als Produkt von Primfaktoren geschrieben sind.

* 18 = 2 • 3 • 3 = 2 • 3<sup>2</sup>
* 84 = 2 • 2 • 3 • 7 = 2<sup>2</sup> • 3 • 7
* 144 = 2 • 2 • 2 • 2 • 3 • 3 = 2<sup>4</sup> • 3<sup>2</sup>
Für alle drei der oben genannten ganzen Zahlen ist das Berechnen ihrer Primfaktoren relativ einfach, selbst wenn Ihnen nur N gegeben ist. Sie beginnen mit der kleinsten Primzahl, nämlich 2, und sehen, wie oft die ganze Zahl N durch sie teilbar ist. Dann gehen Sie dazu über, die Teilbarkeit von N durch 3, 5, 7 und so weiter zu testen. Sie setzen diesen Prozess fort, bis Ihre ganze Zahl N als Produkt von nur Primzahlen geschrieben ist.
Nehmen wir zum Beispiel die ganze Zahl 84. Unten können Sie den Prozess zur Bestimmung ihrer Primfaktoren sehen. Bei jedem Schritt nehmen wir den kleinsten verbleibenden Primfaktor heraus (links) und bestimmen den verbleibenden Term, der faktorisiert werden soll. Wir fahren fort, bis der verbleibende Term ebenfalls eine Primzahl ist. Bei jedem Schritt wird die aktuelle Faktorisierung von 84 ganz rechts angezeigt.

* Primfaktor = 2: verbleibender Term = 42 	(84 = 2 • 42)
* Primfaktor = 2: verbleibender Term = 21 	(84 = 2 • 2 • 21)
* Primfaktor = 3: verbleibender Term = 7 		(84 = 2 • 2 • 3 • 7)
* Da 7 eine Primzahl ist, ist das Ergebnis 2 • 2 • 3 • 7 oder 2<sup>2</sup> • 3 • 7.

Angenommen, N ist jetzt sehr groß. Wie schwierig wäre es, N in seine Primfaktoren zu zerlegen?

Das hängt wirklich von N ab. Nehmen wir zum Beispiel an, N ist 50.450.400. Obwohl diese Zahl einschüchternd aussieht, sind die Berechnungen nicht so kompliziert und können leicht von Hand durchgeführt werden. Wie oben beginnen Sie einfach mit 2 und arbeiten sich weiter vor. Unten können Sie das Ergebnis dieses Prozesses in ähnlicher Weise wie oben sehen.

* 2: 25.225.200 	(50.450.400 = 2 • 25.225.200)  
* 2: 12.612.600 	(50.450.400 = 2<sup>2</sup> • 12.612.600)  
* 2: 6.306.300 		(50.450.400 = 2<sup>3</sup> • 6.306.300)  
* 2: 3.153.150 		(50.450.400 = 2<sup>4</sup> • 3.153.150)  
* 2: 1.576.575 		(50.450.400 = 2<sup>5</sup> • 1.576.575)  
* 3: 525.525 		(50.450.400 = 2<sup>5</sup> • 3 • 525.525)
* 3: 175.175 		(50.450.400 = 2<sup>5</sup> • 3<sup>2</sup> • 175.175)
* 5: 35.035 		(50.450.400 = 2<sup>5</sup> • 3<sup>2</sup> • 5 • 35.035)
* 5: 7.007		    (50.450.400 = 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7.007)
* 7: 1.001 (50.450.400 = 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7 • 1.001)
* 7: 143 (50.450.400 = 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7<sup>2</sup> • 143)
* 11: 13 (50.450.400 = 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7<sup>2</sup> • 11 • 13)
* Da 13 eine Primzahl ist, ist das Ergebnis 2<sup>5</sup> • 3<sup>2</sup> • 5<sup>2</sup> • 7<sup>2</sup> • 11 • 13.

Dieses Problem von Hand zu lösen, dauert eine Weile. Ein Computer könnte all dies natürlich in einem Bruchteil einer Sekunde erledigen. Tatsächlich kann ein Computer häufig sogar extrem große ganze Zahlen in einem Bruchteil einer Sekunde faktorisieren.

Es gibt jedoch bestimmte Ausnahmen. Nehmen wir an, wir wählen zuerst zwei sehr große Primzahlen zufällig aus. Es ist üblich, diese mit p und q zu bezeichnen, und ich werde diese Konvention hier übernehmen.

Um konkret zu sein, sagen wir, dass p und q beide 1024-Bit-Primzahlen sind und dass sie tatsächlich mindestens 1024 Bits zur Darstellung benötigen (also muss das erste Bit eine 1 sein). So könnte zum Beispiel 37 nicht eine der Primzahlen sein. Man kann 37 sicherlich mit 1024 Bits darstellen. Aber klarerweise *braucht man* nicht so viele Bits, um sie darzustellen. Man kann 37 durch jede Zeichenfolge darstellen, die 6 Bits oder mehr hat. (In 6 Bits würde 37 als 100101 dargestellt).

Es ist wichtig zu würdigen, wie groß p und q sind, wenn sie unter den oben genannten Bedingungen ausgewählt werden. Als Beispiel habe ich eine zufällige Primzahl ausgewählt, die mindestens 1024 Bits zur Darstellung benötigt, siehe unten.

* 14.752.173.874.503.595.484.930.006.383.670.759.559.764.562.721.397.166.747.289.220.945.457.932.666.751.048.198.854.920.097.085.690.793.755.254.946.188.163.753.506.778.089.706.699.671.722.089.715.624.760.049.594.106.189.662.669.156.149.028.900.805.928.183.585.427.782.974.951.355.515.394.807.209.836.870.484.558.332.897.443.152.653.214.483.870.992.618.171.825.921.582.253.023.974.514.209.142.520.026.807.636.589

Nehmen wir nun an, nachdem wir zufällig die Primzahlen p und q ausgewählt haben, multiplizieren wir sie, um eine ganze Zahl N zu erhalten. Diese letztere Zahl ist daher eine 2048-Bit-Zahl, die mindestens 2048 Bits zu ihrer Darstellung benötigt. Sie ist viel, viel größer als entweder p oder q.
Angenommen, Sie geben einem Computer nur N und bitten ihn, die beiden 1024-Bit-Primfaktoren von N zu finden. Die Wahrscheinlichkeit, dass der Computer p und q entdeckt, ist extrem gering. Man kann sagen, es ist für alle praktischen Zwecke unmöglich. Das gilt selbst dann, wenn Sie einen Supercomputer oder sogar ein Netzwerk von Supercomputern einsetzen würden.

Zunächst nehmen wir an, dass der Computer versucht, das Problem zu lösen, indem er durch 1024-Bit-Zahlen zyklisch durchgeht und in jedem Fall testet, ob sie prim sind und ob sie Faktoren von N sind. Die Menge der zu testenden Primzahlen beträgt dann ungefähr 1,265 • 10<sup>305</sup>.<sup>[2](#footnote2)</sup>

Selbst wenn Sie alle Computer auf dem Planeten nehmen und sie versuchen lassen, 1024-Bit-Primzahlen auf diese Weise zu finden und zu testen, würde eine Chance von eins zu einer Milliarde, einen Primfaktor von N erfolgreich zu finden, eine Rechenzeit erfordern, die viel länger ist als das Alter des Universums.

In der Praxis kann ein Computer jedoch besser abschneiden als das gerade beschriebene grobe Verfahren. Es gibt mehrere Algorithmen, die der Computer anwenden kann, um schneller zu einer Faktorisierung zu kommen. Der Punkt ist jedoch, dass selbst unter Verwendung dieser effizienteren Algorithmen die Aufgabe für den Computer immer noch rechnerisch nicht machbar ist.<sup>[3](#footnote3)</sup>

Wichtig ist, dass die Schwierigkeit der Faktorisierung unter den gerade beschriebenen Bedingungen auf der Annahme beruht, dass es keine rechnerisch effizienten Algorithmen zur Berechnung von Primfaktoren gibt. Wir können tatsächlich nicht beweisen, dass ein effizienter Algorithmus nicht existiert. Dennoch ist diese Annahme sehr plausibel: Trotz umfangreicher Bemühungen über Hunderte von Jahren haben wir noch keinen solchen rechnerisch effizienten Algorithmus gefunden.

Daher kann das Faktorisierungsproblem unter bestimmten Umständen plausiblerweise als ein schwieriges Problem angesehen werden. Insbesondere, wenn p und q sehr große Primzahlen sind, ist ihr Produkt N nicht schwer zu berechnen; aber die Faktorisierung, nur gegeben N, ist praktisch unmöglich.

## Zahlentheoretische Ergebnisse
<chapterId>23cd2186-8d97-5709-a4a7-b984f1eb9999</chapterId>

Leider kann das Faktorisierungsproblem nicht direkt für asymmetrische kryptografische Schemata verwendet werden. Wir können jedoch ein komplexeres, aber damit zusammenhängendes Problem zu diesem Zweck nutzen: das RSA-Problem.

Um das RSA-Problem zu verstehen, müssen wir eine Reihe von Theoremen und Aussagen aus der Zahlentheorie verstehen. Diese werden in diesem Abschnitt in drei Unterabschnitten vorgestellt: (1) die Ordnung von N, (2) die Invertierbarkeit modulo N und (3) Eulers Theorem.

Einige der Materialien in den drei Unterabschnitten wurden bereits in *Kapitel 3* eingeführt. Aber ich werde hier das Material zur Bequemlichkeit noch einmal darstellen.

### Die Ordnung von N

Eine ganze Zahl a ist **teilerfremd** oder ein **relativer Prim** zu einer ganzen Zahl N, wenn der größte gemeinsame Teiler zwischen ihnen 1 ist. Obwohl 1 konventionell keine Primzahl ist, ist sie ein Teilerfremder jeder ganzen Zahl (wie auch – 1).

Betrachten Sie zum Beispiel den Fall, wenn a = 18 und N = 37 ist. Diese sind eindeutig teilerfremd. Die größte Zahl, die sowohl in 18 als auch in 37 teilt, ist 1. Im Gegensatz dazu betrachten Sie den Fall, wenn a = 42 und N = 16 ist. Diese sind eindeutig nicht teilerfremd. Beide Zahlen sind durch 2 teilbar, was größer als 1 ist.
Wir können nun die Ordnung von N wie folgt definieren. Nehmen wir an, dass N eine ganze Zahl größer als 1 ist. Die **Ordnung von N** ist dann die Anzahl aller zu N teilerfremden Zahlen, so dass für jede teilerfremde Zahl a die folgende Bedingung erfüllt ist: 1 ≤ a < N.
Zum Beispiel, wenn N = 12 ist, dann sind 1, 5, 7 und 11 die einzigen Teilerfremden, die die oben genannte Anforderung erfüllen. Daher ist die Ordnung von 12 gleich 4.

Nehmen wir an, dass N eine Primzahl ist. Dann ist jede ganze Zahl kleiner als N, aber größer oder gleich 1, teilerfremd zu ihr. Dies schließt alle Elemente in der folgenden Menge ein: {1,2,3….,N – 1}. Daher ist, wenn N eine Primzahl ist, die Ordnung von N N – 1. Dies wird in Proposition 1 ausgedrückt, wo φ(N) die Ordnung von N bezeichnet.

**Proposition 1**. φ(N) = N – 1, wenn N eine Primzahl ist

Nehmen wir an, dass N keine Primzahl ist. Dann können Sie seine Ordnung mit **Eulers Phi-Funktion** berechnen. Während die Berechnung der Ordnung einer kleinen ganzen Zahl relativ einfach ist, wird Eulers Phi-Funktion besonders wichtig für größere ganze Zahlen. Die Proposition von Eulers Phi-Funktion wird unten angegeben.

*Theorem 2*. Sei N gleich p<sub>1</sub><sup>e_1</sup> • p<sub>2</sub><sup>e_2</sup> • … • p<sub>i</sub><sup>e_i</sup> • … • p<sub>n</sub><sup>e_n</sup>, wobei die Menge {p<sub>i</sub>} aus allen verschiedenen Primfaktoren von N besteht und jedes e_i angibt, wie oft der Primfaktor p<sub>i</sub> für N vorkommt. Dann ist φ(N) = p<sub>1</sub><sup>e_1 - 1</sup> • (p<sub>1</sub> - 1) • p<sub>2</sub><sup>e_2 - 1</sup> • (p<sub>2</sub> - 1) • … • p<sub>n</sub><sup>e_n - 1</sup> • (p<sub>n</sub> - 1).

*Theorem 2* zeigt, dass es einfach ist, die Ordnung von N zu berechnen, sobald Sie ein nicht-primäres N in seine verschiedenen Primfaktoren zerlegt haben.

Zum Beispiel, nehmen wir an, dass N = 270 ist. Dies ist eindeutig keine Primzahl. Die Zerlegung von N in seine Primfaktoren ergibt den Ausdruck: 2 • 3<sup>3</sup> • 5. Gemäß Eulers Phi-Funktion ist die Ordnung von N dann wie folgt:

* φ(N) = 2<sup>1 – 1</sup> (2 – 1) + 3<sup>3 – 1</sup> (3 – 1) + 5<sup>1 – 1</sup> (5 – 1) = 1 (1) + 9 (2) + 1 (4) = 1 + 18 + 4 = 23
Nehmen wir als nächstes an, dass N ein Produkt von zwei Primzahlen, p und q, ist. *Theorem 2* besagt dann, dass die Ordnung von N wie folgt ist: p<sup>1 – 1</sup> (p – 1) x q<sup>1 – 1</sup> (q – 1) = (p – 1) x (q – 1). Dies ist ein Schlüsselergebnis für das RSA-Problem im Besonderen und wird in *Proposition 2* unten dargestellt.
*Proposition 2*. Wenn N das Produkt von zwei Primzahlen, p und q, ist, dann ist die Ordnung von N das Produkt (p – 1) x (q – 1).

Um dies zu veranschaulichen, nehmen wir an, dass N = 119 ist. Diese ganze Zahl kann in zwei Primzahlen zerlegt werden, nämlich 7 und 17. Daher legt die Eulersche Phi-Funktion nahe, dass die Ordnung von 119 wie folgt ist:

* φ(119) = (7 – 1) • (17 – 1) = 6 • 16 = 96.

Mit anderen Worten, die ganze Zahl 119 hat 96 teilerfremde Zahlen im Bereich von 1 bis 119. Tatsächlich umfasst diese Menge alle ganzen Zahlen von 1 bis 119, die keine Vielfachen von entweder 7 oder 17 sind.

Von hier an bezeichnen wir die Menge der teilerfremden Zahlen, die die Ordnung von N bestimmt, als **C<sub>N</sub>**. Für unser Beispiel, wo N = 119 ist, ist die Menge **C<sub>119</sub>** viel zu groß, um sie vollständig aufzulisten. Aber einige der Elemente sind wie folgt: **C<sub>119</sub>** = {1,2,….6,8….13,15,16,18,….,33,35….,96}.

### Invertierbarkeit modulo N

Wir können sagen, dass eine ganze Zahl a **invertierbar modulo N** ist, wenn es mindestens eine ganze Zahl b gibt, so dass a x b modulo N = 1 modulo N ist. Jede solche ganze Zahl b wird als ein **Inverses** (oder **multiplikatives Inverses**) einer gegebenen Reduktion durch modulo N bezeichnet.

Nehmen wir zum Beispiel an, dass a = 5 und N = 11 ist. Es gibt viele ganze Zahlen, mit denen Sie 5 multiplizieren können, so dass 5 x b mod 11 = 1 mod 11. Betrachten Sie zum Beispiel die ganzen Zahlen 20 und 31. Es ist leicht zu sehen, dass beide diese ganzen Zahlen Inverse von 5 für die Reduktion modulo 11 sind.

* 5 x 20 mod 11 = 100 mod 11 = 1 mod 11
* 5 x 31 mod 11 = 155 mod 11 = 1 mod 11

Obwohl 5 viele Inverse bei der Reduktion modulo 11 hat, kann man zeigen, dass genau ein positives Inverses von 5 existiert, das kleiner als 11 ist. Tatsächlich ist dies nicht nur auf unser spezielles Beispiel beschränkt, sondern ein allgemeines Ergebnis.

*Proposition 3*. Wenn die ganze Zahl a invertierbar modulo N ist, muss es der Fall sein, dass genau ein positives Inverses von a kleiner als N ist. (Also muss dieses einzigartige Inverse von a aus der Menge {1,…,N – 1} stammen).
Lassen Sie uns das eindeutige Inverse von a aus Proposition 3 als a<sup>-1</sup> bezeichnen. Für den Fall, dass a = 5 und N = 11 ist, können Sie sehen, dass a<sup>-1</sup> = 9 ist, gegeben dass 5 x 9 mod 11 = 45 mod 11 = 1 mod 11. 
Beachten Sie, dass Sie den Wert 9 für a<sup>-1</sup> in unserem Beispiel auch einfach erhalten können, indem Sie jedes andere Inverse von a modulo 11 reduzieren. Zum Beispiel, 20 mod 11 = 31 mod 11 = 9 mod 11. Also, wann immer eine ganze Zahl a > N modulo N invertierbar ist, dann muss auch a mod N modulo N invertierbar sein.

Es ist nicht notwendigerweise der Fall, dass ein Inverses von a bei Reduktion modulo N existiert. Nehmen wir zum Beispiel an, dass a = 2 und N = 8 ist. Es gibt kein b, oder spezifisch kein a<sup>-1</sup>, so dass 2 x b mod 8 = 1 mod 8. Dies liegt daran, dass jeder Wert von b immer ein Vielfaches von 2 produzieren wird, so dass keine Division durch 8 jemals einen Rest ergeben kann, der 1 entspricht.

Wie genau wissen wir, ob eine ganze Zahl a ein Inverses für ein gegebenes N hat? Wie Sie vielleicht im obigen Beispiel bemerkt haben, ist der größte gemeinsame Teiler zwischen 2 und 8 höher als 1, nämlich 2. Und dies ist tatsächlich illustrativ für das folgende allgemeine Ergebnis:

*Proposition 4*. Ein Inverses existiert von einer ganzen Zahl a gegeben Reduktion modulo N, und spezifisch ein einzigartiges positives Inverses kleiner als N, wenn und nur wenn der größte gemeinsame Teiler zwischen a und N 1 ist (das heißt, wenn sie teilerfremd sind).

Für den Fall, dass a = 5 und N = 11 ist, kamen wir zu dem Schluss, dass a<sup>-1</sup> = 9, gegeben dass 5 x 9 mod 11 = 45 mod 11 = 1 mod 11. Es ist wichtig zu beachten, dass das Umgekehrte auch wahr ist. Das heißt, wenn a = 9 und N = 11 ist, ist es der Fall, dass a<sup>-1</sup> = 5.

### Eulers Theorem

Bevor wir zum RSA-Problem übergehen, müssen wir ein weiteres entscheidendes Theorem verstehen, nämlich **Eulers Theorem**. Es besagt Folgendes:

*Theorem 3*. Angenommen, zwei ganze Zahlen a und N sind teilerfremd. Dann ist a<sup>φ(N)</sup> mod N = 1 mod N.

Dies ist ein bemerkenswertes Ergebnis, aber zunächst ein wenig verwirrend. Lassen Sie uns anhand eines Beispiels darauf eingehen, um es zu verstehen.

Nehmen wir an, dass a = 5 und N = 7 ist. Diese sind in der Tat teilerfremd, wie Eulers Theorem es verlangt. Wir wissen, dass die Ordnung von 7 gleich 6 ist, da 7 eine Primzahl ist (siehe **Proposition 1**).

Was Eulers Theorem nun besagt, ist, dass 5<sup>6</sup> mod 7 gleich 1 mod 7 sein muss. Unten sind die Berechnungen, um zu zeigen, dass dies tatsächlich wahr ist.

* 5<sup>6</sup> mod 7 = 15.625 mod 7 = 1 mod N

Die ganze Zahl 7 teilt sich in 15.624 insgesamt 2.233 Mal. Daher ist der Rest der Division von 16.625 durch 7 1.

Als Nächstes können Sie mit Eulers Phi-Funktion, *Theorem 2*, die *Proposition 5* unten ableiten.
*Behauptung 5*. φ(a • b) = φ(a) • φ(b) für alle positiven ganzen Zahlen a und b.
Wir werden nicht zeigen, warum dies der Fall ist. Aber wir merken nur an, dass Sie bereits Beweise für diese Behauptung gesehen haben, durch die Tatsache, dass φ(p • q) = φ(p) • φ(q) = (p – 1) • (q – 1) ist, wenn p und q Primzahlen sind, wie in *Behauptung 2* angegeben.

Der Satz von Euler in Verbindung mit *Behauptung 5* hat wichtige Implikationen. Sehen Sie, was zum Beispiel in den folgenden Ausdrücken passiert, wo a und N teilerfremd sind.

* a<sup>2 • φ(N)</sup> mod N = a<sup>φ(N)</sup> • a<sup>φ(N)</sup> mod N = 1 • 1 mod N = 1 mod N
* a<sup>φ(N) + 1</sup> mod N = a<sup>φ(N)</sup> • a<sup>1</sup> mod N = 1 • a<sup>1</sup> mod N = a mod N
* a<sup>8 • φ(N) + 3</sup> mod N = a<sup>8 • φ(N)</sup> • a<sup>3</sup>  mod N = 1 • a<sup>3</sup>  mod N = a<sup>3</sup>  mod N

Daher ermöglicht uns die Kombination des Satzes von Euler und *Behauptung 5*, eine Reihe von Ausdrücken einfach zu berechnen. Allgemein können wir die Einsicht wie in *Behauptung 6* zusammenfassen.

*Behauptung 6*. a<sup>x</sup> mod N = a<sup>x mod φ(N)</sup>

Nun müssen wir alles in einem kniffligen letzten Schritt zusammenführen.

So wie N eine Ordnung φ(N) hat, die die Elemente der Menge **C<sub>N</sub>** umfasst, wissen wir, dass die ganze Zahl φ(N) ihrerseits auch eine Ordnung und eine Menge von Teilerfremden haben muss. Setzen wir φ(N) = R. Dann wissen wir, dass es auch einen Wert für φ(R) und eine Menge von Teilerfremden **C<sub>R</sub>** gibt.

Nehmen wir an, dass wir nun eine ganze Zahl e aus der Menge **C<sub>R</sub>** auswählen. Wir wissen aus *Behauptung 3*, dass diese ganze Zahl e nur ein einziges positives Inverses kleiner als R hat. Das heißt, e hat ein einziges Inverses aus der Menge **C<sub>R</sub>**. Nennen wir dieses Inverse d. Angesichts der Definition eines Inversen bedeutet dies, dass e • d = 1 mod R.

Wir können dieses Ergebnis verwenden, um eine Aussage über unsere ursprüngliche ganze Zahl N zu machen. Dies wird in *Behauptung 7* zusammengefasst.

*Behauptung 7*. Angenommen, e • d mod φ(N) = 1 mod φ(N). Dann muss für jedes Element a der Menge **C<sub>N</sub>** gelten, dass a<sup>e • d mod φ(N)</sup> = a<sup>1 mod φ(N)</sup> = a mod N.

Wir haben nun alle zahlentheoretischen Ergebnisse, die benötigt werden, um das RSA-Problem klar zu formulieren.


## Das RSA-Kryptosystem
<chapterId>0253c2f7-b8a4-5d0e-bd60-812ed6b6c7a9</chapterId>
Wir sind nun bereit, das RSA-Problem zu formulieren. Nehmen wir an, Sie erstellen eine Menge von Variablen bestehend aus p, q, N, φ(N), e, d und y. Nennen wir diese Menge Π. Sie wird wie folgt erstellt:
1. Generiere zwei zufällige Primzahlen p und q gleicher Größe und berechne ihr Produkt N.
2. Berechne die Ordnung von N, φ(N), durch das folgende Produkt: (p – 1) • (q – 1).
3. Wähle ein e > 2, sodass es kleiner und teilerfremd zu φ(N) ist.
4. Berechne d, indem e • d mod φ(N) = 1 gesetzt wird.
5. Wähle einen zufälligen Wert y, der kleiner und teilerfremd zu N ist.

Das RSA-Problem besteht darin, ein x zu finden, sodass x<sup>e</sup> = y, während nur eine Teilmenge der Informationen bezüglich Π gegeben ist, nämlich die Variablen N, e und y. Wenn p und q sehr groß sind, typischerweise wird empfohlen, dass sie 1024 Bits groß sind, gilt das RSA-Problem als schwierig. Jetzt können Sie sehen, warum dies der Fall ist, angesichts der vorangegangenen Diskussion.

Eine einfache Methode, x zu berechnen, wenn x<sup>e</sup> mod N = y mod N ist, ist einfach durch Berechnung von y<sup>d</sup> mod N. Wir wissen, dass y<sup>d</sup> mod N = x mod N durch die folgenden Berechnungen:

* y<sup>d</sup> mod N = x<sup>e • d</sup> mod N = x<sup>e • d mod φ(N)</sup> mod N = x<sup>1 mod φ(N)</sup> mod N = x mod N.

Das Problem ist, dass wir den Wert d nicht kennen, da er im Problem nicht gegeben ist. Daher können wir y<sup>d</sup> mod N nicht direkt berechnen, um x mod N zu erzeugen.

Wir könnten jedoch in der Lage sein, d indirekt aus der Ordnung von N, φ(n), zu berechnen, da wir wissen, dass e • d mod φ(N) = 1 mod φ(N). Aber nach Annahme gibt das Problem auch keinen Wert für φ(N) an.

Schließlich könnte die Ordnung indirekt mit den Primfaktoren p und q berechnet werden, sodass wir letztendlich d berechnen können. Aber nach Annahme wurden uns auch die Werte p und q nicht zur Verfügung gestellt.

Streng genommen, selbst wenn das Faktorisierungsproblem innerhalb eines RSA-Problems schwierig ist, können wir nicht beweisen, dass das RSA-Problem ebenfalls schwierig ist. Es könnte nämlich andere Wege geben, das RSA-Problem zu lösen als durch Faktorisierung. Es wird jedoch allgemein akzeptiert und angenommen, dass, wenn das Faktorisierungsproblem innerhalb des RSA-Problems schwierig ist, das RSA-Problem selbst ebenfalls schwierig ist.

Wenn das RSA-Problem tatsächlich schwierig ist, dann erzeugt es eine Einwegfunktion mit einer Falltür. Die Funktion hier ist f(g) = g<sup>e</sup> mod N. Mit Kenntnis von f(g) könnte jeder leicht einen Wert y für ein bestimmtes g = x berechnen. Es ist jedoch praktisch unmöglich, einen bestimmten Wert x nur aus der Kenntnis des Wertes y und der Funktion f(g) zu berechnen. Die Ausnahme ist, wenn Ihnen ein Stück Information d, die Falltür, gegeben wird. In diesem Fall können Sie einfach y<sup>d</sup> berechnen, um x zu geben.

Lassen Sie uns anhand eines spezifischen Beispiels das RSA-Problem veranschaulichen. Ich kann kein RSA-Problem auswählen, das unter den oben genannten Bedingungen als schwierig angesehen würde, da die Zahlen unhandlich wären. Stattdessen dient dieses Beispiel nur dazu zu veranschaulichen, wie das RSA-Problem im Allgemeinen funktioniert.
Um zu beginnen, nehmen wir an, Sie wählen zwei zufällige Primzahlen 13 und 31. Also ist p = 13 und q = 31. Das Produkt N dieser beiden Primzahlen beträgt 403. Wir können leicht die Ordnung von 403 berechnen. Sie entspricht (13 – 1) • (31 – 1) = 360.
Als nächstes müssen wir, wie in Schritt 3 des RSA-Problems vorgegeben, einen teilerfremden Wert zu 360 wählen, der größer als 2 und kleiner als 360 ist. Wir müssen diesen Wert nicht zufällig auswählen. Nehmen wir an, wir wählen 103. Dies ist ein teilerfremder Wert zu 360, da sein größter gemeinsamer Teiler mit 103 gleich 1 ist.

Schritt 4 erfordert nun, dass wir einen Wert d berechnen, sodass 103 • d mod 360 = 1. Dies ist keine leichte Aufgabe von Hand, wenn der Wert für N groß ist. Es erfordert, dass wir ein Verfahren namens **erweiterter Euklidischer Algorithmus** verwenden.

Obwohl ich das Verfahren hier nicht zeige, ergibt es den Wert 7, wenn e = 103. Sie können überprüfen, dass das Wertepaar 103 und 7 tatsächlich die allgemeine Bedingung e • d mod φ(n) = 1 durch die untenstehenden Berechnungen erfüllt.

* 103 • 7 mod 360 = 721 mod 360 = 1 mod 360

Wichtig ist, dass wir aufgrund von *Proposition 4* wissen, dass kein anderer ganzer Wert zwischen 1 und 360 für d das Ergebnis produzieren wird, dass 103 • d = 1 mod 360. Zusätzlich impliziert die Proposition, dass die Auswahl eines anderen Wertes für e einen anderen einzigartigen Wert für d ergeben wird.

In Schritt 5 des RSA-Problems müssen wir eine positive ganze Zahl y auswählen, die ein kleinerer teilerfremder Wert zu 403 ist. Nehmen wir an, wir setzen y = 2<sup>103</sup>. Die Exponentiation von 2 mit 103 ergibt das untenstehende Ergebnis.

* 2<sup>103</sup> mod 403 = 10.141.204.801.825.835.211.973.625.643.008 mod 403 = 349 mod 403

Das RSA-Problem in diesem speziellen Beispiel lautet nun wie folgt: Ihnen wird N = 403, e = 103 und y = 349 mod 403 gegeben. Sie müssen nun x berechnen, sodass x<sup>103</sup> = 349 mod 403. Das heißt, Sie müssen herausfinden, dass der ursprüngliche Wert vor der Exponentiation durch 103 gleich 2 war.

Es wäre einfach (zumindest für einen Computer), x zu berechnen, wenn wir wüssten, dass d = 7. In diesem Fall könnten Sie x wie unten bestimmen.

* x = y<sup>7</sup> mod 403 = 349<sup>7</sup> mod 403 = 630.634.881.591.804.949 mod 403 = 2 mod 403

Das Problem ist, dass Ihnen die Information, dass d = 7 ist, nicht gegeben wurde. Natürlich könnten Sie d aus der Tatsache berechnen, dass 103 • d = 1 mod 360. Das Problem ist, dass Ihnen auch nicht die Information gegeben wurde, dass die Ordnung von N = 360 ist. Schließlich könnten Sie auch die Ordnung von 403 berechnen, indem Sie das folgende Produkt berechnen: (p – 1) • (q – 1). Aber Ihnen wurde auch nicht gesagt, dass p = 13 und q = 31 ist.
Natürlich könnte ein Computer das RSA-Problem in diesem Beispiel immer noch relativ leicht lösen, da die beteiligten Primzahlen nicht groß sind. Aber wenn die Primzahlen sehr groß werden, steht er vor einer praktisch unmöglichen Aufgabe.
Wir haben nun das RSA-Problem vorgestellt, eine Reihe von Bedingungen, unter denen es schwierig ist, und die zugrundeliegende Mathematik. Wie hilft uns das bei der asymmetrischen Kryptografie? Speziell, wie können wir die Schwierigkeit des RSA-Problems unter bestimmten Bedingungen in ein Verschlüsselungsschema oder ein digitales Signaturschema umwandeln?

Ein Ansatz besteht darin, das RSA-Problem zu nehmen und Schemata auf eine direkte Weise zu erstellen. Angenommen, Sie haben eine Reihe von Variablen Π erzeugt, wie im RSA-Problem beschrieben, und stellen sicher, dass p und q ausreichend groß sind. Sie setzen Ihren öffentlichen Schlüssel gleich (N, e) und teilen diese Informationen mit der Welt. Wie oben beschrieben, halten Sie die Werte für p, q, φ(n) und d geheim. Tatsächlich ist d Ihr privater Schlüssel.

Jeder, der Ihnen eine Nachricht m, die ein Element von **C<sub>N</sub>** ist, senden möchte, könnte sie einfach wie folgt verschlüsseln: c = m<sup>e</sup> mod N. (Der Chiffretext c hier entspricht dem Wert y im RSA-Problem.) Sie können diese Nachricht leicht entschlüsseln, indem Sie einfach c<sup>d</sup> mod N berechnen.

Sie könnten versuchen, auf die gleiche Weise ein digitales Signaturschema zu erstellen. Angenommen, Sie möchten jemandem eine Nachricht m mit einer digitalen Signatur S senden. Sie könnten einfach S = m<sup>d</sup> mod N setzen und das Paar (m,S) an den Empfänger senden. Jeder kann die digitale Signatur einfach überprüfen, indem er prüft, ob S<sup>e</sup> mod N = m mod N. Ein Angreifer hätte jedoch große Schwierigkeiten, ein gültiges S für eine Nachricht zu erstellen, da er d nicht besitzt.

Leider ist es nicht so einfach, aus einem an sich schwierigen Problem, dem RSA-Problem, ein kryptografisches Schema zu machen. Für das direkte Verschlüsselungsschema können Sie nur teilerfremde von N als Ihre Nachrichten auswählen. Das lässt uns nicht viele mögliche Nachrichten, sicherlich nicht genug für eine Standardkommunikation. Zusätzlich müssen diese Nachrichten zufällig ausgewählt werden. Das scheint etwas unpraktisch. Schließlich wird jede Nachricht, die zweimal ausgewählt wird, genau denselben Chiffretext ergeben. Das ist in jedem Verschlüsselungsschema äußerst unerwünscht und erfüllt keine rigorose moderne Standardvorstellung von Sicherheit in der Verschlüsselung.

Die Probleme werden sogar noch schlimmer für unser direktes digitales Signaturschema. Wie es derzeit steht, kann jeder Angreifer leicht digitale Signaturen fälschen, indem er zuerst ein Teilerfremdes von N als die Signatur auswählt und dann die entsprechende ursprüngliche Nachricht berechnet. Dies bricht eindeutig die Anforderung der existenziellen Unfälschbarkeit.

Dennoch kann das RSA-Problem mit ein wenig cleverer Komplexität verwendet werden, um ein sicheres öffentliches Schlüsselverschlüsselungsschema sowie ein sicheres digitales Signaturschema zu erstellen. Wir werden hier nicht auf die Details solcher Konstruktionen eingehen.<sup>[4](#footnote4)</sup> Wichtig ist jedoch, dass diese zusätzliche Komplexität das grundlegende zugrundeliegende RSA-Problem, auf dem diese Schemata basieren, nicht ändert.

### Anmerkungen

[^1]: Die Faktorisierung kann auch für den Umgang mit anderen Arten mathematischer Objekte als Zahlen wichtig sein. Beispielsweise kann es nützlich sein, polynomiale Ausdrücke wie x^2 – 2x + 1 zu faktorisieren. In unserer Diskussion werden wir uns jedoch nur auf die Faktorisierung von Zahlen, speziell ganzen Zahlen, konzentrieren [^1].
[^2]: Gemäß dem Primzahlsatz ist die Anzahl der Primzahlen kleiner oder gleich N ungefähr N/ln(N). Das bedeutet, dass man die Anzahl der Primzahlen der Länge 1024 Bits annähern kann durch 2^1024/ln(2^1024) - 2^1023/ln(2^1023), was ungefähr 1,265 x 10^305 entspricht [^2].

# Beiträge
<partId>4556aab1-4876-552a-b6db-df6837bbf27a</partId>

## Über
<chapterId>ff08a57b-740f-5d7e-8cf2-81db0908166e</chapterId>

Jeder Beitrag ist herzlich willkommen. Bevor Sie dies tun, schauen Sie bitte unten nach Hintergrundinformationen zu meinen eigenen Plänen für das Buch sowie den Richtlinien für Beiträge.

### Aktuelle Pläne

Meine aktuellen Pläne für die weitere Entwicklung des Buches sind wie folgt:

- Ein abschließendes Kapitel erstellen, das sich mit den Details praktischer kryptografischer Anwendungen befasst, wie Transport Layer Security, Onion Routing und Werttausch in Bitcoin
- Bessere und mehr Abbildungen und Diagramme erstellen, um die schriftliche Diskussion zu unterstützen
- LaTeX Math oder eine andere Satzanwendung für die formale Notation verwenden (anstatt nur Markdown)

### Richtlinien für Beiträge

Wenn Sie kleinere Korrekturen oder Vorschläge bezüglich des bestehenden Textes haben, können Sie einen Pull-Request erstellen oder ein Issue eröffnen. Wenn Sie einen Pull-Request erstellen, beachten Sie bitte die folgenden Richtlinien:

- Erstellen Sie die Commits auf einem separaten Branch in Ihrem Fork des Repositories
- Beschriften Sie die Commits klar
- Erstellen Sie separate Commits für logisch unterschiedliche Probleme, um den Überprüfungsprozess zu erleichtern

Wenn Sie substantiellere Vorschläge bezüglich des Buches haben, eröffnen Sie bitte ein Issue oder kontaktieren Sie mich direkt unter **jaburgers@protonmail.com**.

### Lizenz

Die Arbeit in diesem Repository ist lizenziert unter der Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0).

Eine kurze Beschreibung der Lizenz finden Sie [hier](https://creativecommons.org/licenses/by-nc-nd/4.0/).

Eine vollständige Version der Lizenz finden Sie [hier](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode).

## Notation
<chapterId>07250f8d-ad7c-5531-a70c-4417d6d1b865</chapterId>

### Schlüsselbegriffe

Schlüsselbegriffe in den Grundlagen werden durch Fettdruck eingeführt. Zum Beispiel würde die Einführung des Rijndael-Chiffre als Schlüsselbegriff folgendermaßen aussehen: **Rijndael-Chiffre**.

Schlüsselbegriffe werden explizit definiert, es sei denn, es handelt sich um Eigennamen oder ihre Bedeutung ist aus der Diskussion offensichtlich.

Eine Definition wird normalerweise bei der Einführung eines Schlüsselbegriffs gegeben, obwohl es manchmal bequemer ist, die Definition bis zu einem späteren Zeitpunkt zu verschieben.

### Hervorgehobene Wörter und Phrasen

Wörter und Phrasen werden durch Kursivschrift hervorgehoben. Zum Beispiel würde die Phrase "Merke dir dein Passwort" folgendermaßen aussehen: *Merke dir dein Passwort*.

### Formale Notation

Die formale Notation betrifft hauptsächlich Variablen, Zufallsvariablen und Mengen.

* Variablen: Diese werden normalerweise einfach durch einen Kleinbuchstaben angezeigt (z.B. "x" oder "y"). Manchmal werden sie zur Klarheit großgeschrieben (z.B. "M" oder "K").
* Zufallsvariablen: Diese werden immer durch einen Großbuchstaben angezeigt (z.B. "X" oder "Y").
* Mengen: Diese werden immer durch fettgedruckte, Großbuchstaben angezeigt (z. B. **S**)