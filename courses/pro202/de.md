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

<partId>e545b7a7-b596-436e-86e9-d0ddceb72543</partId>


## Mathematik für die Bitcoin-Implementierung

<chapterId>790e5214-836b-40fe-bbd6-f4ccc920b778</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Elliptische Kurven Kryptographie

<chapterId>7d3d842e-ae88-472e-85ff-196d60655815</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin-Transaktion Innere Verflechtungen

<partId>774c0e80-d316-414a-bd59-0bbd185d3b58</partId>


## Bitcoin Transaktionsparsing und ECDSA-Signaturen

<chapterId>ae86fc27-2f27-4de9-b17c-351c00690144</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Bitcoin Skript- und Transaktionsvalidierung

<chapterId>8f0d4381-2b36-4c66-8bee-1100b2dfd8ed</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Transaktionsaufbau und Pay-to-Script Hash


<chapterId>1a6ca3fa-a71f-4b7e-9337-7c84a0b3f928</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Bitcoin Netzwerk-Innenleben

<partId>6af9d722-07da-487b-bf08-1b30bc3db3d4</partId>


## Bitcoin-Blöcke und Proof of Work

<chapterId>28a0f5d3-af1b-4093-be49-e3112e1d48a4</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Netzwerkkommunikation und Merkle-Bäume

<chapterId>dd8e23bc-ddd6-45a6-8d3a-16bc86ba49ac</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Erweiterte Knotenkommunikation und getrennter Zeuge

<chapterId>8d70c283-4609-46a8-ad24-83b04a68529a</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Letzter Abschnitt


<partId>f338e5f4-216e-4b38-bf56-8333e674c04c</partId>


## Rezensionen und Bewertungen


<chapterId>e149d14b-e99f-428a-a775-ed50cd0a6e9b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## Schlussfolgerung


<chapterId>247bcefb-b158-42a3-82f4-c58bcad4a47a</chapterId>

<isCourseConclusion>true</isCourseConclusion>
