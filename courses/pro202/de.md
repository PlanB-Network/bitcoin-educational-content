---
name: Programmierung Bitcoin
goal: Erstellen einer vollständigen Bitcoin-Bibliothek von Grund auf und Verstehen der kryptografischen Grundlagen von Bitcoin
objectives: 

 - Implementierung der Arithmetik endlicher Felder und elliptischer Kurven in Python
 - Bitcoin-Transaktionen programmatisch konstruieren und parsen
 - Testnet-Adressen erstellen und Transaktionen über das Netz verbreiten
 - Beherrschung der mathematischen Grundlagen des Bitcoin-Sicherheitsmodells

---
# Eine Reise zu den Skripten und Programmen von Bitcoin


Dieser zweitägige Intensivkurs, der von Jimmy Song geleitet wird, führt Sie tief in die technischen Grundlagen von Bitcoin ein, indem er eine komplette Bitcoin-Bibliothek von Grund auf aufbaut. Beginnend mit der grundlegenden Mathematik der endlichen Felder und elliptischen Kurven, werden Sie durch Transaktionsparsing, Skriptausführung und Netzwerkkommunikation fortschreiten. Durch praktische Programmierübungen in Jupyter-Notizbüchern werden Sie Ihr eigenes Testnet Address erstellen, Transaktionen manuell konstruieren und sie direkt an das Netzwerk senden - und dabei ein tiefes Verständnis der kryptografischen Prinzipien erlangen, die Bitcoin und Trustless sicher machen.


Viel Spaß bei Ihrer Entdeckung!


+++

# Einführung

<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>

## Kursübersicht

<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>

Willkommen im Kurs PRO 202 _**Programming Bitcoin**_, einer intensiven Reise, die Sie von der endlichen Feldarithmetik bis hin zum Erstellen und Übertragen echter Transaktionen im Bitcoin-Testnetz führt.

In diesem Kurs werden Sie schrittweise eine Bitcoin-Bibliothek in Python erstellen und dabei die kryptografischen, protokollarischen und softwaretechnischen Grundlagen erwerben, die notwendig sind, um präzise über die Sicherheit und die inneren Abläufe von Bitcoin zu argumentieren. Der PRO 202-Ansatz ist vollständig praxisorientiert: jedes Konzept wird sofort in Jupyter-Notebooks implementiert, sodass Theorie und Code sich gegenseitig stärken.

### Wesentliche mathematische Konzepte für Bitcoin

Dieser erste Abschnitt legt das unverzichtbare mathematische Fundament. Sie werden die Arithmetik endlicher Körper und Operationen auf elliptischen Kurven implementieren (Gruppengesetz, Addition, Verdopplung, Skalarmultiplikation...) — die Voraussetzungen für ECDSA. Das Ziel ist zweifach: die algebraische Struktur zu verstehen, die kryptografische Signaturen ermöglicht, und zuverlässige Python-Werkzeuge zu entwickeln, um damit zu arbeiten.

Anschließend werden Sie die Komponenten von ECDSA formalisieren: Schlüsselgenerierung, Punktformatierung, Hashing, Signaturerstellung und -überprüfung. Dieser Abschnitt verbindet Theorie direkt mit Praxis und betont Implementierungsdetails sowie die Robustheit des zugrunde liegenden Sicherheitsmodells.

### Das Innenleben einer Bitcoin-Transaktion

Im zweiten Abschnitt werden Sie die Struktur einer Bitcoin-Transaktion analysieren: UTXOs, Eingaben/Ausgaben, Sequenzen, Skripte, Kodierungen und mehr. Sie werden Code schreiben, um Transaktionen zu erstellen, zu signieren und zu verifizieren, und dabei ein genaues Verständnis davon gewinnen, was durch den Hash festgelegt wird und warum.

Als Nächstes implementieren Sie einen minimalen _Script_-Interpreter, überprüfen wichtige Opcodes und validieren Ausgabepfade. Das Ziel ist, Sie in die Lage zu versetzen, das Transaktionsverhalten zu prüfen, Validierungsfehler zu diagnostizieren und über die Sicherheit von Ausgaberegeln zu urteilen.

### Das Innenleben des Bitcoin-Netzwerks

Im dritten Abschnitt werden Sie die Transaktion in das größere System einordnen: Blockstruktur, Header, Schwierigkeit und den Proof-of-Work-Mechanismus. Sie werden mit Protokollnachrichten, Block-Headern und Merkle-Bäumen arbeiten.

Abschließend werden Sie die Peer-to-Peer-Knotenkommunikation, Nachrichtenoptimierung und die Einführung von SegWit untersuchen.

Wie bei jedem Kurs an der Plan ₿ Academy enthält der letzte Abschnitt eine Bewertung, die darauf ausgelegt ist, Ihr Verständnis zu festigen. Bereit, die inneren Abläufe von Bitcoin zu entdecken und den Code zu schreiben, der es antreibt? Los geht’s!

# Grundlegende mathematische Konzepte für Bitcoin

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Mathematik für die Bitcoin-Implementierung

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Elliptische Kurven Kryptographie

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin-Transaktion Innere Verflechtungen

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Transaktionsparsing und ECDSA-Signaturen

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Skript- und Transaktionsvalidierung

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Transaktionsaufbau und Pay-to-Script Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Bitcoin Netzwerk-Innenleben

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bitcoin-Blöcke und Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Netzwerkkommunikation und Merkle-Bäume

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Erweiterte Knotenkommunikation und getrennter Zeuge

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Letzter Abschnitt


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Rezensionen und Bewertungen


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>


## Schlussfolgerung


<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>

<isCourseConclusion>true</isCourseConclusion>
