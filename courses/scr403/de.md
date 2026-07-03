---
name: Eintauchen in Simplicity
goal: Beherrsche die Designphilosophie, das Typsystem und den vollständigen Lebenszyklus von Simplicity
objectives:
  - Verstehe die drei fundamentalen Kompositionsmethoden und die neun Kombinatoren, die eine vollständige Sprache bilden
  - Baue Boolesche Logik, Arithmetik und SHA-256 aus Simplicitys minimalem Typsystem auf
  - Erfasse, wie die Seiteneffekte Failure und Reader echte Blockchain-Interaktion ermöglichen
  - Lerne, wie Simplicity-Programme zu Taproot-Adressen werden und mit Witness-Daten eingelöst werden
---

# Eintauchen in Simplicity

Ein tiefer Einblick in die Theorie und die Designentscheidungen hinter der Sprache Simplicity, basierend auf der vollständigen fünfteiligen Artikelserie ["Delving Simplicity"](https://delvingbitcoin.org/t/delving-simplicity-part-three-fundamental-ways-of-combining-computations/1902) von [Dr. Russell O'Connor](https://r6.ca/), dem Schöpfer von Simplicity bei Blockstream Research. Dieser Kurs erklärt *warum* Simplicity so entworfen wurde, wie es entworfen wurde, nicht wie man es schreibt.

Der Kurs folgt Dr. O'Connors Artikeln durch die drei fundamentalen Wege der Kombination von Berechnungen, das minimale Typsystem und dessen Vollständigkeitssatz, den Aufbau praktischer Datentypen und Arithmetik aus ersten Prinzipien, die sorgfältige Einführung von Seiteneffekten für die Blockchain-Interaktion und schließlich, wie Programme zu Adressen committet und on-chain eingelöst werden.

+++

# Einführung

<partId>c362889b-c630-435f-911b-724c4eca505b</partId>

## Kursübersicht

<chapterId>cdcc40b6-c985-45b4-9bee-6f931e984476</chapterId>

Willkommen zu SCR403 — Eintauchen in Simplicity!

Dieser Kurs basiert auf der Artikelserie **"Delving Simplicity"**, geschrieben von [Dr. Russell O'Connor](https://r6.ca/), einem Infrastructure Tech Developer bei [Blockstream](https://blockstream.com/) und dem Schöpfer von Simplicity. Die ursprünglichen Artikel wurden im Forum [Delving Bitcoin](https://delvingbitcoin.org/u/roconnor-blockstream/summary) veröffentlicht und bilden das primäre Quellmaterial für diesen Kurs. Wir sind dankbar für seine Pionierarbeit, die diesen Lerninhalt möglich gemacht hat.

### Was du lernen wirst

Dieser Kurs erforscht die Designphilosophie und die mathematischen Grundlagen hinter Simplicity, der Skriptsprache der nächsten Generation, die im Juli 2025 im [Liquid Network](https://blockstream.com/press-releases/2025-07-31-blockstream-launches-simplicity/) aktiviert wurde. Er folgt der vollständigen fünfteiligen Artikelserie und ist in zwei Hauptinhaltsabschnitte gegliedert:

1. **Grundlagen von Simplicity** — Warum Blockchain-Berechnung eine fundamental andere Sprache erfordert, die drei Wege, Operationen zu kombinieren (sequentiell, parallel, bedingt), und die neun Kern-Kombinatoren, die eine mathematisch vollständige Sprache bilden
2. **Von Datentypen zu Programmen** — Aufbau von Boolescher Logik, Arithmetik und SHA-256 aus ersten Prinzipien; Verständnis der Seiteneffekte Failure und Reader, die Blockchain-Interaktion ermöglichen; und wie Programme über Commitment-Merkle-Roots zu Taproot-Adressen committet und mit Witness-Daten eingelöst werden

### Voraussetzungen

Dies ist ein Kurs auf **Expertenniveau** (etwa 10 Stunden). Du solltest vertraut sein mit:
- Grundlegenden Bitcoin-Scripting-Konzepten (was Transaktionsvalidierung bewirkt)
- Fundamentalen Programmierkonzepten (Typen, Funktionen, Komposition)
- Eine gewisse Vertrautheit mit mathematischer Notation ist hilfreich, aber nicht erforderlich. Wir führen alles im Verlauf ein

### Wichtige Ressourcen

- **Originalartikel**: ["Delving Simplicity"](https://delvingbitcoin.org/u/roconnor-blockstream/summary) von Dr. Russell O'Connor auf Delving Bitcoin
- **Simplicity-Repository**: [BlockstreamResearch/simplicity](https://github.com/BlockstreamResearch/simplicity) — Quellcode und formale Rocq-Beweise
- **Offizielle Website**: [simplicity-lang.org](https://simplicity-lang.org/) — Dokumentation und SimplicityHL-Referenz
- **Blockstream-Blog**: [Simplicity on GitHub](https://blog.blockstream.com/en-simplicity-github/) — technischer Überblick

Bereit, in eines der elegantesten Stücke Bitcoin-Ingenieurskunst einzutauchen? Los geht's!

## Was ist Simplicity?

<chapterId>d04f3960-d7fb-44e1-b5a3-25b33d03fd38</chapterId>

Wenn du diesen Kurs ohne Vorwissen zu Simplicity beginnst, wird dich dieses Kapitel orientieren, bevor wir ins tiefe Wasser springen.

### Simplicity in Kürze

Simplicity ist eine **Bitcoin-native Smart-Contract-Sprache**, die heute live auf dem Liquid Network läuft. Erstmals um 2012 von Dr. Russell O'Connor konzipiert und in seinem 2017er-Paper *Simplicity: A New Language for Blockchains* detailliert beschrieben, wurde sie im Juli 2025 nach Jahren formaler Verifikation und Entwicklung auf dem Liquid Network aktiviert.

Im Gegensatz zu Ethereums Solidity, einer Turing-vollständigen High-Level-Vertragssprache, ist Simplicity absichtlich minimal. Sie besitzt:
- **Drei Typkonstruktoren** (Unit, Summe, Produkt)
- **Neun Kombinatoren** (Grundoperationen und Kompositionsregeln)
- **Keine Schleifen, keine Rekursion, keinen dynamischen Speicher**

Aus genau diesen Primitiven lässt sich jede Berechnung aufbauen, die für die Transaktionsvalidierung benötigt wird, von Boolescher Logik bis zum vollständigen SHA-256-Hashing.

### Was kann man heute mit Simplicity machen?

Simplicity treibt bereits echte Anwendungen auf dem Liquid Network an. Am bemerkenswertesten ist die [Simplicity DEX](https://docs.simplicity-lang.org/use-cases/simplicity-dex/), ein orakelfreier Optionsmarktplatz, auf dem Nutzer Call-Optionen auf L-BTC mit USDt als Sicherheit handeln (der zugrunde liegende Vertrag unterstützt auch Puts). Weitere aktive Simplicity-Projekte sind [Swaption](https://swaption.io/) von SideSwap (Optionen) und das quelloffene [Deadcat](https://github.com/Resolvr-io/deadcat) von Resolvr (Prognosemärkte). Über DeFi hinaus ermöglicht Simplicity fortgeschrittene Ausgabebedingungen wie Vaults, Covenants und komplexe Multisig-Schemata, die in Bitcoin Script unmöglich oder unsicher wären.

### Was dieser Kurs ist — und was nicht

Dies ist **kein** praktisches Coding-Tutorial. Du wirst hier keine Simplicity-Programme schreiben. Wenn du danach suchst, schau dir an:
- [simplicity-lang.org](https://simplicity-lang.org/) — offizielle Dokumentation und die High-Level-Sprache SimplicityHL
- Das [Simplicity-GitHub-Repository](https://github.com/BlockstreamResearch/simplicity) — Referenzimplementierung, Beispiele und Rocq-Beweise
- Den [Blockstream-Blogbeitrag](https://blog.blockstream.com/en-simplicity-github/) zum Einstieg

Worum es in diesem Kurs **geht**: die **philosophischen und technischen Entscheidungen** hinter Simplicitys Design. Warum wurde diese Sprache so geschaffen? Warum nur neun Kombinatoren? Warum keine Rekursion? Warum ist es wichtig, dass das Typsystem an Gentzens Sequenzenkalkül anknüpft?

Stell es dir so vor: verstehen, **warum der Motor so gebaut wurde**, anstatt zu lernen, das Auto zu fahren.

### Für wen ist dieser Kurs?

Dieser Kurs ist ideal für:
- **Protokollentwickler**, die Simplicitys Grundlagen verstehen wollen, bevor sie Code schreiben
- **Bitcoin-Forscher**, die sich für den formalen Verifikations- und typentheoretischen Ansatz interessieren
- **Informatiker**, die neugierig auf die Verbindung zwischen Sequenzenkalkül und Blockchain-Berechnung sind
- **Fortgeschrittene Bitcoiner**, die über das oberflächliche Verständnis der Scripting-Fähigkeiten von Liquid hinausgehen wollen

Wenn dir Begriffe wie "Summentypen", "Kombinatoren" oder "Sequenzenkalkül" völlig neu sind, keine Sorge, wir erklären alles von Grund auf. Aber sei auf eine dichte, mathematische Reise vorbereitet.

### Von Artikeln zum Kurs

Die ursprüngliche Artikelserie "Delving Simplicity" von Dr. O'Connor ist in fünf technische Artikel gegliedert. Dieser Kurs reorganisiert und kommentiert dieses Material zu einem progressiven Lernpfad mit Quiz, um dein Verständnis unterwegs zu testen. Die Ideen, Definitionen und Beweise stammen von ihm, und wir haben das Format für strukturierte Bildung angepasst.

# Grundlagen von Simplicity

<partId>a5976618-94ab-4b29-b9aa-040d35c68e5d</partId>

## Fundamentale Wege der Kombination von Berechnungen

<chapterId>6d46e77a-7e60-473b-b230-418da5ae44eb</chapterId>

Nachdem Simplicity nun auf dem Liquid Network aktiviert wurde, möchte ich einen tiefen Einblick in die Philosophie und das Design der Sprache Simplicity geben.

Bitcoins Transaktionsvalidierung ist eine deutlich andere Anwendung als reguläres Programmiersprachendesign. Blockplatz ist teuer, daher müssen Programme kompakt sein. Die Programme in Bitcoin-Transaktionen werden nur jemals auf einem einzigen Input ausgeführt, und jeder führt das Programm auf demselben Input aus. Außerdem kennt der die Transaktion autorisierende Akteur das Ergebnis der Berechnung bereits im Voraus: dass die Transaktion gültig ist.

Typischerweise führt der autorisierende Akteur deutlich teurere Berechnungen aus, um Witness-Daten abzuleiten, die die Gültigkeit der Transaktion bezeugen, während Programme, die auf der Blockchain laufen, die Witness-Daten nur auf Gültigkeit prüfen müssen. Gültigkeit zu prüfen ist oft deutlich billiger als Gültigkeit zu beweisen.

Wir haben Simplicity mit diesen Arten einzigartiger Sprachdesign-Herausforderungen im Hinterkopf entworfen. Zum Beispiel verlangt Simplicity, dass nicht ausgeführte Zweige entfernt werden, sodass sie nicht auf der Blockchain erscheinen. Vorverarbeitungsschritte sind sorgfältig so gestaltet, dass sie (quasi-)lineare Zeitkomplexität in der Größe des Simplicity-Programms aufweisen. Statische Analyse wird anstelle von "Gas" verwendet, das nicht berechnet werden kann, ohne Code auf eine vorgeschriebene Weise auszuführen, sodass die Details des Ausführungsmodells nicht konsensrelevant werden. Keine dynamische Speicherzuweisung während der Ausführung. Und so weiter.

Bevor wir in die Designdetails von Simplicity eintauchen, möchte ich diese Serie mit etwas Programmierphilosophie über die allgemeinen Wege beginnen, Grundbausteine zu kombinieren, um neue Funktionalität zu schaffen.

### Komposition

Angenommen, jemand entwirft eine Sprache für programmierbare Transaktionen für eine Blockchain wie Bitcoin. Insbesondere haben Programme nur Zugriff auf die Transaktionsdaten und die UTXO-Daten der Inputs, und die Ausführung bestimmt nur die Transaktionsgültigkeit (was es erlaubt, das Ergebnis der Ausführung zu cachen). Nehmen wir an, man beginnt mit einer Menge grundlegender Operationen, die verschiedene Aufgaben ausführen können, wie grundlegende Berechnungen, das Lesen und/oder Verarbeiten von Daten aus der Transaktion und Signaturverifikation. Jede Operation konsumiert einen bestimmten Eingabetyp (möglicherweise leer) und liefert einen bestimmten Ausgabetyp zurück. Welche Möglichkeiten gibt es, diese Grundoperationen zu komplexeren Operationen zu kombinieren?

### Sequentielle Komposition

![Sequentielle Komposition](assets/en/001.webp)

Die grundlegendste Kompositionsmethode ist die sequentielle Komposition. Wenn wir zwei Grundoperationen haben, wobei der Ausgabetyp der einen dem Eingabetyp der anderen entspricht, können wir diese beiden Operationen zu einer neuen zusammengesetzten Operation kombinieren. Diese neue Operation führt diese beiden Grundoperationen nacheinander aus, nimmt als Eingabe die Eingabe der ersten Operation, gibt die Ausgabe dieser ersten Operation in die Eingabe der zweiten Operation und liefert schließlich die Ausgabe dieser zweiten Operation zurück.

Natürlich müssen wir uns nicht darauf beschränken, nur Grundoperationen zu kombinieren. Da wir nun einige zusammengesetzte Operationen haben, können wir diese ebenfalls per funktionaler Komposition kombinieren.

In der Mathematik wird diese sequentielle Komposition oft einfach "Komposition" genannt, und man könnte denken, dass dies die einzige Möglichkeit ist, Dinge zu komponieren. Wir haben jedoch weitere Möglichkeiten, Operationen zu komponieren.

### Parallele Komposition

![Parallele Komposition](assets/en/002.webp)

Angenommen, wir haben zwei Operationen — sie können grundlegend oder komplex sein — und beide nehmen denselben Eingabetyp an. Ein zweiter fundamentaler Weg, diese beiden Operationen zu komponieren, besteht darin, sie beide auf derselben Eingabe auszuführen. Dies nennt man parallele Komposition, und der Ausgabetyp ist das "Produkt" der Ausgabetypen der ursprünglichen Operationen und enthält das Paar der beiden Ausgaben.

Obwohl dies "parallele" Komposition genannt wird und die beiden Operationen im Prinzip parallel ausgeführt werden könnten, ist die parallele Ausführung keine operative Anforderung. Wir können parallele Komposition "sequentiell" implementieren, indem wir zuerst die eine und dann die andere Operation ausführen. Uns ist es egal, wie parallele Komposition im Detail implementiert wird, solange die Ausgabe dieselbe ist.

### Bedingte Komposition

![Bedingte Komposition](assets/en/003.webp)

Bedingte Komposition ist das Duale zur parallelen Komposition. In diesem Fall haben wir zwei Operationen, die dieselbe Ausgabe erzeugen, und wir komponieren sie, indem wir eine von ihnen zur Ausführung auswählen. Die Eingabe dieser zusammengesetzten Operation ist die "Summe" oder "getaggte Vereinigung" der Eingabetypen der ursprünglichen Operationen. In diesem Fall ist der Tag, "Left" oder "Right", ein einzelnes Bit in den Daten der Eingabe, das bestimmt, welche Art von Daten transportiert wird, und damit, welche der beiden Operationen ausgeführt werden kann.

Bedingte Komposition funktioniert auf dieselbe Weise, selbst wenn die Eingabe die Summe zweier identischer Typen ist. Der Summentyp enthält weiterhin einen Tag, und der Wert dieses Tags bestimmt, welche der beiden Operationen ausgeführt werden soll.

### Komposition in Bitcoin Script

Es gibt viele Wege, diese drei Arten von Komposition in verschiedenen Programmiersprachen zu realisieren. In Bitcoin Script wird sequentielle Komposition (näherungsweise) durch die Verkettung zweier Routinen realisiert (deshalb wird Bitcoin Script eine konkatenative Programmiersprache genannt), da die Ausgabe einer Routine auf dem Stack verbleibt, um von der nachfolgenden Routine konsumiert zu werden. Parallele Komposition wird durch den Einsatz von Duplizier- und Vertauschoperationen erreicht, die den Stack so manipulieren, dass zwei Routinen auf derselben Eingabe laufen können. Ganz so einfach ist es nicht, da das, was wir das "Produkt" von Typen nennen, typischerweise durch die Nutzung mehrerer Stack-Einträge realisiert wird. Hoffentlich erkennst du die allgemeine Idee.

Bedingte Komposition wird natürlich durch `OP_IF` realisiert, das anhand des Werts auf dem Stack verzweigt. In diesem Fall spielt der oberste Stack-Eintrag die Rolle eines Tags, und üblicherweise sind der nächste Eintrag oder die nächsten Einträge auf dem Stack von unterschiedlichem "Typ", abhängig vom Wert des Tags. Für jeden Fall dürfen die Stack-Eintragstypen nur für die Verarbeitung durch einen der Zweige in `OP_IF` geeignet sein. Nach Erreichen von `OP_ENDIF` müssen die Stack-Einträge jedoch von konsistentem "Typ" sein, sodass das übrige Script unabhängig davon fortfahren kann, welcher Zweig zuvor genommen wurde.

### Komposition in Simplicity

Wir haben Simplicity mit Kombinatoren entworfen, die diese drei Formen der Komposition direkt implementieren. Zusammen mit ein paar weiteren Kombinatoren zur Unterstützung anderer Grundoperationen im Zusammenhang mit Produkt- und Summentypen besteht die Simplicity-Kernsprache letztlich aus neun Kombinatoren, die ausreichen, um jede endliche Berechnung auszudrücken. Wir werden dies im nächsten Kapitel ausführlicher besprechen.

### Eine vierte Art der Komposition

Bevor wir schließen, sollten wir erwähnen, dass es in der Informatik mindestens eine weitere Art der Komposition gibt: die "rekursive Komposition". Bei der rekursiven Komposition wird eine Operation mehrfach iteriert.

Beachte, dass Bitcoin Script keine rekursive Komposition unterstützt, und ähnlich haben wir unbegrenzte Rekursion explizit aus Simplicitys Design ausgeschlossen. Unsere These ist, dass unbegrenzte iterative Berechnung besser mithilfe rekursiver Covenants implementiert wird, die über mehrere Transaktionen hinweg rechnen. Dies ermöglicht es Nutzern, Blockplatz- und Standardness-Beschränkungen zu vermeiden und Transaktionskosten besser vorherzusagen.

Trotzdem gibt es Möglichkeiten, Simplicitys Delegationsfunktion zu missbrauchen, um so etwas wie unbegrenzte rekursive Komposition bereitzustellen, was wir vielleicht später in dieser Serie besprechen.

### Fazit

Wir haben die drei wichtigsten Formen der Komposition betrachtet, um Grundoperationen in komplexe Operationen umzuwandeln:

- sequentielle Komposition
- parallele Komposition
- bedingte Komposition

Wir haben besprochen, wie diese Kompositionsformen in Bitcoin Script realisiert werden, und angedeutet, wie sie das Design der Sprache Simplicity beeinflusst haben. Wir haben festgestellt, dass die vierte Art der Komposition, die rekursive Komposition, sowohl aus Simplicity als auch aus Bitcoin Script gezielt ausgeschlossen ist.

Im nächsten Kapitel beschreiben wir die neun Kombinatoren, die den Kern der Sprache Simplicity bilden, wie sie diese drei Formen der Komposition direkt realisieren, und wie dies eine vollständige Sprache zur Beschreibung jeder endlichen Berechnung ergibt.

## Kombinatoren-Vollständigkeit von Simplicity

<chapterId>2a10a6ba-fada-4556-a673-3ae8c0794bf0</chapterId>

In diesem Kapitel führen wir die Kernsprache von Simplicity ein und zeigen, dass die Sprache vollständig ist, das heißt, dass jede endliche Berechnung in ihr ausgedrückt werden kann.

### Simplicity-Typen

Simplicity unterstützt drei fundamentale Typkonstruktoren. Der Produkttyp `A × B` repräsentiert Ausgaben paralleler Komposition, während der Summentyp `A + B` (getaggte Vereinigung) Eingaben bedingter Komposition behandelt. Der dritte Typ ist der Unit-Typ.

### Unit-Typ

Der Unit-Typ, bezeichnet mit `𝟙` oder `ONE`, enthält genau einen Wert: das leere Tupel `⟨⟩` bzw. `()`. Dieser Nullbit-Datentyp trägt keinerlei Information.

### Summentyp

Ein Summentyp `A + B` kombiniert zwei Typen mit Tags, die "links" oder "rechts" anzeigen. Werte werden als `σᴸ(a)` bzw. `inl(a)` für links-getaggte Werte und `σᴿ(b)` bzw. `inr(b)` für rechts-getaggte Werte geschrieben. Die Tags bleiben auch bei identischen Typen unterscheidbar.

#### Boolescher Typ

Der Typ `𝟙 + 𝟙`, bezeichnet mit `𝟚` oder `TWO`, repräsentiert einen Ein-Bit-Typ mit zwei Werten. Per Konvention repräsentiert `σᴸ⟨⟩` falsch/null, während `σᴿ⟨⟩` wahr/eins repräsentiert.

### Produkttyp

Produkttypen `A × B` enthalten Wertepaare, geschrieben als `⟨a, b⟩` bzw. `(a, b)`. Der Typ `𝟚 × 𝟚` hat vier Werte, verschieden von den vier Werten in `𝟚 + 𝟚`.

### Simplicity-Kernausdrücke

Operationen werden als `f : A ⊢ B` bezeichnet, was Eingabetyp `A` und Ausgabetyp `B` bedeutet. Simplicity ist "erststufig" — es besitzt keine Funktionstypen.

### Zwei Grundoperationen

Die Kernsprache bietet zwei Grundoperationen:

**Identität (`iden`).** Die Identitätsoperation gibt ihre Eingabe unverändert durch:

```
iden : A ⊢ A
⟦iden⟧(a) = a
```

**Unit (`unit`).** Die Unit-Operation verwirft ihre Eingabe und liefert das leere Tupel zurück:

```
unit : A ⊢ 𝟙
⟦unit⟧(a) = ⟨⟩
```

Diese bilden Familien mit einer Operation pro Typ.

### Drei Kompositions-Kombinatoren

Sequentielle Komposition verwendet `comp f g` (geschrieben `f ⨾ g` oder `f >>> g`):

```
If f : A ⊢ B and g : B ⊢ C, then
comp f g : A ⊢ C
⟦f ⨾ g⟧(a) = ⟦g⟧(⟦f⟧(a))
```

Parallele Komposition verwendet `pair f g` (geschrieben `f ▵ g` oder `f &&& g`):

```
If f : A ⊢ B and g : A ⊢ C, then
pair f g : A ⊢ B × C
⟦f ▵ g⟧(a) = ⟨⟦f⟧(a), ⟦g⟧(a)⟩
```

Bedingte Komposition verwendet `case f g : (A + B) × C ⊢ D`, was den Zweigen Zugriff auf eine gemeinsame Umgebung `C` verschafft:

```
If f : A × C ⊢ D and g : B × C ⊢ D, then
case f g : (A + B) × C ⊢ D
⟦case f g⟧⟨σᴸ(a), c⟩ = ⟦f⟧⟨a, c⟩
⟦case f g⟧⟨σᴿ(b), c⟩ = ⟦g⟧⟨b, c⟩
```

Warum hat die bedingte Komposition diese Form — eine Summe gepaart mit einer gemeinsamen Umgebung `C` — statt eines einfacheren `copair f g : A + B ⊢ C`, das lediglich einen Zweig auswählt? Weil ein bloßes `copair` **Distribution** nicht ausdrücken kann: die Funktion `dist : (A + B) × C ⊢ A × C + B × C`, die eine gemeinsame Eingabe in den jeweils genommenen Zweig hineinschiebt. Indem die Umgebung `C` direkt in `case` eingebaut wird, erhält Simplicity bedingte Komposition *und* Distribution aus einem einzigen Kombinator — eine der zentralen Designentscheidungen, die die Kernsprache auf neun Kombinatoren begrenzt.

### Vier weitere Kombinatoren

Die Produktkonsumierung verwendet `take` und `drop`:

**take** extrahiert das linke Element:

```
If f : A ⊢ C, then
take f : A × B ⊢ C
⟦take f⟧⟨a, b⟩ = ⟦f⟧(a)
```

**drop** extrahiert das rechte Element:

```
If f : B ⊢ C, then
drop f : A × B ⊢ C
⟦drop f⟧⟨a, b⟩ = ⟦f⟧(b)
```

Die Summenerzeugung verwendet `injl` und `injr`:

**injl** verpackt mit einem Links-Tag:

```
If f : A ⊢ B, then
injl f : A ⊢ B + C
⟦injl f⟧(a) = σᴸ(⟦f⟧(a))
```

**injr** verpackt mit einem Rechts-Tag:

```
If f : A ⊢ C, then
injr f : A ⊢ B + C
⟦injr f⟧(a) = σᴿ(⟦f⟧(a))
```

### Die neun Kern-Kombinatoren

Insgesamt hat Simplicity genau neun Kern-Kombinatoren:

| Combinator | Purpose |
|---|---|
| `iden` | Pass input through |
| `unit` | Discard input |
| `comp` | Sequential composition |
| `pair` | Parallel composition |
| `case` | Conditional composition |
| `take` | Extract left from product |
| `drop` | Extract right from product |
| `injl` | Inject into left of sum |
| `injr` | Inject into right of sum |

### Simplicity und der Sequenzenkalkül

Simplicitys Design leitet sich aus dem konjunktiv-disjunktiven Fragment von Gentzens Sequenzenkalkül ab. Genauer gesagt handelt es sich um eine Variante der *funktionalen Interpretation* des Sequenzenkalküls, die selbst analog zur Curry-Howard-Korrespondenz zwischen natürlicher Deduktion und Lambda-Kalkül ist. Die Kombinatorregeln weisen "kleinere Typen in den Prämissen als in den Konklusionen" auf, was es der Bit Machine — Simplicitys abstrakter Stack-Maschinen-Interpreter — ermöglicht, das Kopieren von Daten während der Ausführung zu minimieren.

### Werte sind keine Ausdrücke

Simplicity-Ausdrücke bezeichnen Operationen, keine Werte. Die Notation `scribe b : A ⊢ B` repräsentiert einen eindeutigen Ausdruck, der stets den Wert `b` zurückgibt, und dient als notationelle Bequemlichkeit statt als Kombinator. Dies spiegelt Bitcoin Script wider, wo Operationen wie `OP_1` Werte auf den Stack legen, statt sie direkt auszudrücken.

### Simplicitys Vollständigkeitssatz

Mit allen neun Kombinatoren zur Hand — woher wissen wir, dass uns nichts fehlt, dass diese neun wirklich genügen? Der Simplicity-Vollständigkeitssatz beantwortet dies: Für jede Funktion zwischen (endlichen) Simplicity-Typen bezeichnet ein Simplicity-Ausdruck diese Funktion. Der Beweis ist konstruktiv — er zeigt, wie man den Ausdruck aufbaut:

1. **Die Eingabe zerlegen**: Mithilfe verschachtelter `case`-Ausdrücke jede Eingabe jedes Typs vollständig in ihre einzelnen Bits zerlegen
2. **Eine Nachschlagetabelle aufbauen**: Für jede mögliche Eingabe mit `scribe` die entsprechende Ausgabe erzeugen
3. **Zusammensetzen**: Die verschachtelten Cases und Scribes bilden zusammen eine riesige Nachschlagetabelle, die die Funktion implementiert

Dieser Satz ist im Beweisassistenten Rocq (früher Coq) formal verifiziert. Der Beweis ist Teil des offiziellen Simplicity-Repositorys und wurde maschinell auf Korrektheit geprüft.

Während der Vollständigkeitssatz garantiert, dass Simplicitys neun Kombinatoren jede Funktion zwischen (endlichen) Simplicity-Typen ausdrücken können, sind die aus der Nachschlagetabellenkonstruktion resultierenden Ausdrücke unpraktisch groß. Eine Funktion mit 256-Bit-Eingaben würde eine Nachschlagetabelle mit 2²⁵⁶ Einträgen erfordern. Deshalb konzentrieren sich die nächsten Kapitel darauf, effiziente Ausdrücke zu bauen, die die Struktur der Berechnungen ausnutzen, statt alles per Brute-Force über Nachschlagetabellen zu lösen.

### Fazit

Simplicitys Kernsprache umfasst ein Typsystem und Kombinatoren, die jede endliche Berechnung ermöglichen. Während der Vollständigkeitssatz Ausdrucksstärke garantiert, sind die aus der generischen Konstruktion resultierenden Ausdrücke unpraktisch groß. Praktische Simplicity-Entwicklung besteht darin, die Struktur der Berechnung für prägnante Ausdrücke auszunutzen. Die nächsten Kapitel erforschen Datenstrukturen, Transaktionsinteraktionen und weitere Kombinatoren.

# Von Datentypen zu Programmen

<partId>08528a6f-d310-4675-b8cd-4e9b93b3c009</partId>

## Datentypen aufbauen

<chapterId>9981ae62-ae50-4770-adf2-b253d1e08de3</chapterId>

In den vorherigen Kapiteln haben wir gezeigt, wie Simplicitys Kernmenge von Kombinatoren ausreicht, um jede endliche reine Berechnung zu implementieren. Dieses Kapitel zeigt, wie man aus diesen Primitiven praktische Datenstrukturen und Berechnungen aufbaut — auf dieselbe Weise, wie Computer aus Logikgattern aufgebaut werden.

### Boolesche Logik

Der Boolesche Typ, bezeichnet mit `𝟚`, ist gleich `𝟙 + 𝟙` und hat zwei Werte: `σᴸ⟨⟩` (falsch) und `σᴿ⟨⟩` (wahr). Mithilfe der Kernkombinatoren lassen sich Boolesche Logikoperatoren konstruieren.

#### And-Operation

Die logische `and : 𝟚 × 𝟚 ⊢ 𝟚`-Operation nimmt zwei Bits und liefert ein Bit zurück. Die Implementierung verzweigt anhand des ersten Bits: wenn falsch, wird falsch zurückgegeben; andernfalls wird das zweite Bit zurückgegeben.

```
and ≔ case (injl unit) (drop iden) : 𝟚 × 𝟚 ⊢ 𝟚
```

Test mit `⟨false, false⟩`:

```
⟦and⟧⟨false, false⟩
 = {expand the notation for false}
⟦and⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {expand the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴸ⟨⟩, σᴸ⟨⟩⟩
 = {evaluate case for σᴸ}
⟦injl unit⟧⟨⟨⟩, σᴸ⟨⟩⟩
 = {evaluate injl}
σᴸ(⟦unit⟧⟨⟨⟩, σᴸ⟨⟩⟩)
 = {evaluate unit}
σᴸ⟨⟩
 = {by the notation for false}
false
```

Test mit `⟨true, true⟩`:

```
⟦and⟧⟨true, true⟩
 = {expand the notation for true and the definition of and}
⟦case (injl unit) (drop iden)⟧⟨σᴿ⟨⟩, σᴿ⟨⟩⟩
 = {evaluate case for σᴿ}
⟦drop iden⟧⟨⟨⟩, σᴿ⟨⟩⟩
 = {evaluate drop}
⟦iden⟧(σᴿ⟨⟩)
 = {evaluate iden}
σᴿ⟨⟩
 = {by the notation for true}
true
```

#### Weitere Logikoperationen

Die `not`-Operation benötigt einen Hilfskombinator:

```
                   f : A ⊢ C    g : B ⊢ C
--------------------------------------------------------------
copair f g ≔ iden ▵ unit ⨾ case (take f) (take g) : A + B ⊢ C
```

Das anfängliche `iden ▵ unit : A ⊢ A × 𝟙` fügt der Eingabe eine leere "Umgebung" hinzu, damit der `case`-Kombinator angewendet werden kann. Die Verwendung von `take` in beiden Zweigen verwirft diese leere Umgebung, um `f` bzw. `g` auszuführen.

Weitere Boolesche Logikoperationen:

- `or ≔ case (drop iden) (injr unit) : 𝟚 × 𝟚 ⊢ 𝟚`
- `not ≔ copair (injr unit) (injl unit) : 𝟚 ⊢ 𝟚`
- `xor ≔ case (drop iden) (drop not) : 𝟚 × 𝟚 ⊢ 𝟚`

### Bit-Addierer

Ein "Halbaddierer" nimmt zwei Bits und addiert sie, was eine Zwei-Bit-Ausgabe erzeugt: ein Carry-Bit und ein Summen-Bit.

```
half-adder ≔ and ▵ xor : 𝟚 × 𝟚 ⊢ 𝟚 × 𝟚
```

Ein "Volladdierer" addiert drei Bits und erzeugt eine Zwei-Bit-Ausgabe. Die Eingabe verwendet das verschachtelte Tupel `(𝟚 × 𝟚) × 𝟚`.

Für verschachtelte Tupel wird eine kompakte Notation verwendet:

- `O f` bezeichnet `take f`
- `I f` bezeichnet `drop f`
- `H` bezeichnet `iden`

Zum Beispiel bedeutet `I O H` `drop (take iden) : A × (B × C) ⊢ B`, was den mittleren Wert extrahiert. Die Notation erinnert an Binärziffern: Wenn man verschachtelte Tupel als Binärbäume betrachtet, repräsentiert die Notation umgekehrte Binärziffern der Baumpositionen. Diese Ausdrücke bilden De-Bruijn-Indizes für Simplicity.

**Hinweis:** Die Notation `I`, `O` und `H` gilt nur für Teilausdrücke, die ausschließlich aus `take`, `drop` und `iden` bestehen.

Der Volladdierer setzt zwei Halbaddierer zusammen und bildet das logische `or` der Carry-Bits:

```
full-adder ≔ take half-adder ▵ I H
           ⨾ O O H ▵ (O I H ▵ I H ⨾ half-adder)
           ⨾ (O H ▵ I O H ⨾ or) ▵ I I H
           : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × 𝟚
```

In der ersten Zeile führt `take half-adder ▵ I H : (𝟚 × 𝟚) × 𝟚 ⊢ (𝟚 × 𝟚) × 𝟚` den Halbaddierer auf den ersten beiden Bits aus und behält das letzte Bit bei.

In der zweiten Zeile behält `O O H ▵ (O I H ▵ I H ⨾ half-adder) : (𝟚 × 𝟚) × 𝟚 ⊢ 𝟚 × (𝟚 × 𝟚)` das erste Bit (den Carry-Out des ersten Halbaddierers) bei und führt den Halbaddierer auf den letzten beiden Bits aus.

In der letzten Zeile bildet `(O H ▵ I O H ⨾ or) ▵ I I H: 𝟚 × (𝟚 × 𝟚) ⊢ 𝟚 × 𝟚` das logische OR der ersten beiden Bits (Carry-Outs beider Halbaddierer) und liefert das Summen-Out-Bit des zweiten Halbaddierers zurück.

Dies zeigt Simplicity-Programmierung: die `I`-, `O`- und `H`-Notation wird verwendet, um Datenbits zu referenzieren und geeignete "Umgebungen" für den Aufruf anderer Funktionen via sequentieller Komposition zu bilden.

Nutzer definieren keine Low-Level-Operationen direkt. Später in dieser Serie werden Standardbibliotheks-Jets besprochen, die gängige Funktionen implementieren. Von Endnutzern wird nicht erwartet, direkt in Simplicity zu programmieren, ähnlich wie bei Bitcoin Script. Stattdessen erzeugen High-Level-Sprachen wie SimplicityHL Simplicity-Code, verwalten "Umgebungen" von Teilausdrücken und übersetzen benannte Variablen in geeignete `take`- und `drop`-Sequenzen.

### Vektoren

Vektoren fester Länge werden gebildet, indem man iterierte Produkte des Typs `A` bildet:

- `A² ≔ A × A`
- `A⁴ ≔ A² × A²`
- `A⁸ ≔ A⁴ × A⁴`
- `…`

Diese können auch als `A^2`, `A^4`, `A^8` usw. geschrieben werden.

Vektoren sind nur für Längen definiert, die Zweierpotenzen sind. Andere Längen erfordern die Wahl von Klammerungskonventionen.

Gegeben ein Ausdruck `f : A ⊢ B`, "mappt" wiederholtes Paaren ihn über Vektoren fester Länge:

- `f² ≔ f ▵ f : A² ⊢ B²`
- `f⁴ ≔ f² ▵ f² : A⁴ ⊢ B⁴`
- `f⁸ ≔ f⁴ ▵ f⁴ : A⁸ ⊢ B⁸`

Gegeben eine Funktion `f : A × B ⊢ B`, Iteration bzw. "Falten" über Vektoren fester Länge:

- `fold-right-2 f ≔ O O H ▵ (O I H ▵ I H ⨾ f) ⨾ f : A² × B ⊢ B`
- `fold-right-4 f ≔ fold-right-2 (fold-right-2 f) : A⁴ × B ⊢ B`
- `fold-right-8 f ≔ fold-right-2 (fold-right-4 f) : A⁸ × B ⊢ B`

Es gibt viele Varianten. Gegeben `f : A × B ⊢ C`, "zippe" über gepaarte Vektoren mit `zip-n f : (Aⁿ × Bⁿ) ⊢ Cⁿ`. Gegeben `f : (A × B) × C ⊢ C`, falte über gepaarte Vektoren mit `bifold-right-n f : (Aⁿ × Bⁿ) ⊢ C`. Die Kombination von `map` und `fold-right` erzeugt akkumulierende Kombinatoren: `f : A × C ⊢ C × B` ergibt `map-accum-right-n f : Aⁿ × C ⊢ C × Bⁿ`. Viele weitere Varianten sind möglich.

#### Mehrbit-Wörter

Ein Bitvektor ergibt Mehrbit-Ganzzahlen. Zum Beispiel ist `𝟚³²` ein 32-Bit-Worttyp. `𝟚²⁵⁶` ist ein 256-Bit-Worttyp, geeignet für Hashes und kryptografische Operationen.

Mithilfe des Volladdierers definiert eine Variante von Vektoroperationen einen "Ripple-Carry-Addierer" über Mehrbit-Wörtern:

```
full-adder-n ≔ zip-accum-right-n full-adder : (𝟚ⁿ × 𝟚ⁿ) × 𝟚 ⊢ 𝟚 × 𝟚ⁿ
```

`full-adder-n` nimmt zwei n-Bit-Binärzahlen und ein Ein-Bit-Carry-In und liefert ein Ein-Bit-Carry-Out-Flag sowie eine n-Bit-Summe zurück.

#### SHA-256

Durch die rekursive Definition arithmetischer Operationen auf Mehrbit-Wörtern — Subtraktion, Multiplikation, Division — und bitweiser logischer Operationen wie logisches AND, OR, XOR, und deren wiederholte Kombination, lässt sich sogar die Blockkompressionsfunktion von SHA-256 aufbauen:

```
sha256-hash-block ≔ … : 𝟚²⁵⁶ × 𝟚⁵¹² ⊢ 𝟚²⁵⁶
```

Die SHA-256-Kompression ist formal mithilfe von Simplicity im Beweisassistenten Rocq (früher Coq) definiert, mit einem formalen Beweis, dass die `sha256-hash-block`-Implementierung korrekt ist.

Die Kompression läuft als reines Simplicity zu langsam. Jets führen gängige Funktionen wie die SHA-256-Kompression nativ aus. Reine Simplicity-Implementierungen dienen als formale Spezifikationen für Jets.

### Optionstypen

Optionstypen entstehen, indem man eine Summe mit dem Unit-Typ bildet:

```
Option A ≔ 𝟙 + A
```

Der Typ `Option A` kann als `A?` oder `𝕊 A` geschrieben werden (wobei `𝕊` für "Nachfolger" steht). Funktionen können über Optionstypen gemappt werden:

```
                 f : A ⊢ B
------------------------------------------
f? ≔ copair (injl unit) (injr f) : A? ⊢ B?
```

Monadische Kombinatoren wie bind lassen sich definieren:

```
              f : A ⊢ B?
---------------------------------------
bind f ≔ copair (injl unit) f : A? ⊢ B?
```

### Puffer variabler Länge

"Puffer" sind Typen für teilweise gefüllte Vektoren:

- `Aᑉ² ≔ A?`
- `Aᑉ⁴ ≔ A²? × Aᑉ²`
- `Aᑉ⁸ ≔ A⁴? × Aᑉ⁴`
- `…`

Der Typ `Xᑉ⁸` expandiert zu `(1 + X⁴) × ((1 + X²) × (1 + X))`. Betrachtet man dies als Polynom und expandiert es, ergibt sich `1 + X + X² + X³ + X⁴ + X⁵ + X⁶ + X⁷`. Als Typ interpretiert repräsentiert dies die Summe aller möglichen Tupel von X bis zur Länge 7, einschließlich des leeren Tupels. Dies ist genau der Typ von Listen mit einer Länge strikt kleiner als 8.

Wie bei Vektoren lassen sich Map- und Fold-Operationen auch über Puffer definieren. Stack-Operationen umfassen `push-<n : Aᑉⁿ × A ⊢ Aⁿ + Aᑉⁿ` und `pop-<n : Aᑉⁿ ⊢ (Aᑉⁿ × A)?`. `push-<n` fügt dem Puffer ein Element hinzu und liefert bei Überlauf einen vollen Vektor zurück. `pop-<n` entfernt ein Element und liefert den kleineren Puffer sowie das entfernte Element zurück, wobei optional nichts zurückgegeben wird, wenn der ursprüngliche Puffer leer war.

Die `push-<n`-Definition, rekursiv:

```
push-<2 ≔ case (drop (injr (injr iden))) (injl iden)

push-<4 ≔ ((O I H ▵ IH) ⨾ push-<2) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ injl unit)) (injl iden))
               (injr (I H ▵ O H))

push-<8 ≔ ((O I H ▵ IH) ⨾ push-<4) ▵ O O H
        ⨾ case (I H ▵ O H ⨾ case (injr (injr (I H) ▵ (injl unit ▵ injl unit))) (injl iden))
               (injr (I H ▵ O H))

…
```

Rohes Simplicity wird jenseits gewisser Komplexitätsgrade schwer nachvollziehbar. Endnutzer verwenden High-Level-Sprachen wie SimplicityHL, die diese idiomatischen Ausdrücke erzeugen.

### Fazit

Dieses Kapitel zeigte, wie sich logische Operationen aus Bits aufbauen lassen. Daraus entstand Bit-Ebenen-Arithmetik, die das Schließen über Ausführung ermöglicht. Vektortypen wurden entwickelt, was die Iteration über Mehrbit-Wörter zur Definition von Arithmetik demonstriert. Fortsetzend lassen sich kryptografische Operationen wie SHA-256 und Schnorr-Signaturvalidierung allein mit Simplicity-Kombinatoren definieren — alle tatsächlich mit Simplicity definiert.

Dieses Kapitel ist kein umfassender Leitfaden für alle möglichen Datentypen und Operationen, die in Simplicity gebaut werden können, sondern veranschaulicht, wie praktische Funktionalität innerhalb der Beschränkungen von Simplicity erreicht wird. Trotz endlich begrenzter Typen lassen sich nützliche Vektoren, Puffertypen und Operationen zur Iteration über diese Strukturen definieren.

Tatsächliche Standardbibliotheks-Operationsspezifikationen weichen leicht von den hier gegebenen Definitionen ab. Zum Beispiel verwendet der Volladdierer ein 3-fach-XOR und eine "Mehrheits"-Logikfunktion anstelle zweier Halbaddierer.

In der Praxis verwenden Simplicity-Programme Jets für arithmetische und kryptografische Operationen. Jets ersetzen jedoch nur Ausdrücke. Kombinatoren, die über Puffer und Vektoren iterieren, können nicht durch Jets ersetzt werden und erscheinen in tatsächlichen Simplicity-Programmen. Statt diese jedoch direkt zu verwenden, setzen Endnutzer High-Level-Sprachen wie SimplicityHL ein, die solche Ausdrücke erzeugen.

Rekursiv definierte Kombinatoren scheinen exponentiell in der Ausdrucksgröße zu wachsen. Das ist kein Problem. Bei der Serialisierung werden Ausdrücke als DAGs (gerichtete azyklische Graphen) statt als Bäume kodiert. Die tatsächliche Darstellung wächst nur linear.

Bisher wurden nur reine Berechnungen betrachtet. Die Interaktion mit Transaktionsdaten für Aufgaben wie das Signieren von Transaktionen erfordert eine Möglichkeit für Programme, bei ungültigen Signaturen fehlzuschlagen. Das nächste Kapitel behandelt Seiteneffekte in Simplicity.

## Zwei Seiteneffekte

<chapterId>9eafe498-0765-419a-a69d-a74a9cdf3713</chapterId>

In den vorherigen Kapiteln haben wir gezeigt, wie man mit Simplicitys Kernmenge von Kombinatoren einige Datenstrukturen und Berechnungen aufbaut. Wie wir festgestellt haben, reichen die Kernkombinatoren aus, um jede endliche reine Berechnung zu implementieren. Dies wirft die Frage auf: Was lässt sich darüber hinaus erreichen? Wir können unseren Ausdrücken zusätzliche Seiteneffekte hinzufügen.

Es gibt verschiedene Arten möglicher Seiteneffekte für Ausdrücke: Zustandsaktualisierung, Schreiben in ein Log, Auslösen einer Ausnahme, Lesen aus einer Umgebung, Aufrufen einer Continuation usw. Die in Simplicity verfügbaren Seiteneffekte hängen von der Anwendung ab.

Für Bitcoin- und Liquid-Anwendungen haben wir derzeit zwei Seiteneffekte: den Failure-Effekt, ein Ausnahme-Effekt, bei dem die Ausnahme den Typ `𝟙` hat, und den Reader-Effekt, der es erlaubt, auf Daten aus der Transaktionsumgebung zuzugreifen. Unsere Kernkombinatoren sind "rein"; sie haben keine Seiteneffekte. Jets können jedoch neue Primitive einführen, die Seiteneffekte haben.

### Jets mit Effekten

Wir werden später in diesem Kurs mehr über Jets sprechen, aber hier führen wir ein paar Beispiel-Jets ein, um ihre Seiteneffekte zu veranschaulichen.

#### Bip0340-verify

`bip0340-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚⁵¹² ⊢ 𝟙` ist ein Jet für einen Ausdruck, der einen x-only Pubkey, eine 256-Bit-Nachricht und eine Schnorr-Signatur nimmt und nichts zurückgibt! Laut seinem Typ sollte er sich wie `unit` verhalten. Der Unterschied liegt im Seiteneffekt des Jets: Wenn die Signaturverifikation fehlschlägt, wird die gesamte Berechnung abgebrochen, indem eine Ausnahme (vom Unit-Typ) geworfen wird. Dies ist der Failure-Effekt.

#### Verify

`verify : 𝟚 ⊢ 𝟙` ist ein bloßer Jet zum Ausdrücken des Failure-Effekts. Wenn `verify`s Eingabe `false` ist, wird die gesamte Berechnung abgebrochen, indem eine Ausnahme geworfen wird. Ist die Eingabe `true`, wird nichts zurückgegeben, aber die Berechnung kann fortgesetzt werden.

#### Transaktions-Hashes

`sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` scheint eine konstante Funktion zu sein, da es nur einen möglichen Eingabewert gibt: das leere Tupel. Dieser Jet liest jedoch aus der Transaktionsumgebung und erzeugt einen Hash der Transaktionsdaten, der dem `SIGHASH_ALL`-Message-Digest analog ist, der bei der Signaturverifikation von Bitcoin Script verwendet wird. Dies ist ein Beispiel für den Reader-Effekt: Der zurückgegebene Wert hängt von der Transaktionsumgebung ab, in der der Jet ausgeführt wird. Es gibt mehrere weitere Hashing-Jets, die verschiedene Teilmengen der Transaktionsumgebungsdaten hashen, um benutzerdefinierte Message-Digests für Signaturen zu erstellen.

#### Introspektions-Jets

`input-sequence : 𝟚³² ⊢ 𝟚³²?` ist eine Funktion, die einen Input-Index nimmt und die Sequenznummer der Transaktion für diesen Input zurückgibt, wobei optional nichts zurückgegeben wird, wenn der Index außerhalb des gültigen Bereichs liegt. Auch hier ist der Ausgabewert keine reine Funktion des Eingabeindex, sondern die Operation verwendet den Reader-Effekt, um auf die Transaktionsumgebung zuzugreifen und den Ausgabewert zu bestimmen. Es gibt mehrere weitere Introspektions-Jets, die verschiedene Ausschnitte der Transaktionsumgebungsdaten zurückgeben.

### Effekte klassifizieren

Nicht alle Seiteneffekte sind gleich. Manche Seiteneffekte verhalten sich besser als andere. Wir können Effekte danach klassifizieren, wie zugänglich sie für Programmtransformationen sind.

#### Kommutative Effekte

Ein kommutativer Effekt liegt vor, wenn man die Ausgaben zweier Ausdrücke vertauschen kann und die Ausdrücke selbst sicher vertauschen kann, ohne den Effekt des Ausdrucks zu ändern. Betrachte `swap = I H ▵ O H : A × B ⊢ B × A`. Wenn `f ▵ g ⨾ swap = g ▵ f` für jeden Ausdruck `f` und `g` mit Seiteneffekten gilt, dann sind die Effekte kommutativ.

Das Lesen von Transaktionsdaten aus der Umgebung ist ein kommutativer Effekt, weil das Ergebnis des Lesens aus der Umgebung immer dasselbe ist, unabhängig davon, in welcher Reihenfolge wir lesen.

Im Allgemeinen ist das Auslösen einer Ausnahme kein kommutativer Effekt. Wenn `f` eine Ausnahme `e₁` und `g` eine andere Ausnahme `e₂` auslöst, dann hängt es von der Ausführungsreihenfolge ab, welche Ausnahme vom Paar `f` und `g` ausgelöst wird.

Im speziellen Fall des Failure-Effekts jedoch, bei dem nur eine Ausnahme vom Unit-Typ ausgelöst werden kann, ist der Effekt kommutativ. Egal, ob `f` oder `g` eine Ausnahme auslöst, die resultierende Ausnahme wird dieselbe sein, da es nur einen möglichen Ausnahmewert gibt.

#### Idempotente Effekte

Ein idempotenter Effekt liegt vor, wenn man die Ausgabe eines Ausdrucks duplizieren kann und den Ausdruck selbst sicher duplizieren kann, ohne den Effekt des Ausdrucks zu ändern. Betrachte `dup = iden ▵ iden : A ⊢ A × A`. Wenn `f ⨾ dup = dup ⨾ f ▵ f` für jedes `f` mit Seiteneffekten gilt, dann sind die Effekte idempotent.

Das Lesen von Transaktionsdaten aus der Umgebung ist ein idempotenter Effekt. Das Auslösen einer Ausnahme ist ebenfalls ein idempotenter Effekt. Obwohl nur einer der beiden duplizierten Ausdrücke ausgeführt wird, ist jede von `dup ⨾ f ▵ f` ausgelöste Ausnahme dieselbe wie die von `f ⨾ dup` ausgelöste.

Das Schreiben in ein Log ist jedoch möglicherweise nicht idempotent, da das Duplizieren des Effekts dazu führen würde, dass die Log-Nachricht zweimal erscheint. Besteht das Log jedoch aus einer _Menge_ von Nachrichten statt aus einer _Liste_ von Nachrichten, dann wäre der Effekt idempotent (und kommutativ), da Mengeneinfügung selbst eine idempotente Operation ist.

#### Unitäre Effekte

Ein unitärer Effekt liegt vor, wenn man die Ausgabe eines Ausdrucks verwerfen kann und den Ausdruck selbst sicher verwerfen kann, ohne die Effekte des Ausdrucks zu ändern. Wenn stets `f ⨾ unit = unit` für jedes `f` mit Seiteneffekten gilt, dann sind die Effekte unitär.

Das Lesen von Daten aus der Umgebung ist einer der wenigen Typen unitärer Effekte. Wird das Ergebnis des Lesens von Transaktionsdaten aus der Umgebung verworfen, kann der gesamte Ausdruck, der die Leseoperation ausführt, verworfen werden.

Der Failure-Effekt ist nicht unitär. Wenn `f` eine Ausnahme auslöst, tut dies auch `f ⨾ unit`; die Ausführung erreicht den `unit`-Kombinator nicht einmal, bevor die Berechnung abgebrochen wird. Andererseits würde `unit` offensichtlich keine Ausnahme auslösen, sodass sich die Effekte von `f ⨾ unit` und `unit` unterscheiden würden.

Zusammenfassend, hier ist, wie sich die oben besprochenen Effekte in Bezug auf diese drei Eigenschaften verhalten:

| Effect | Commutative | Idempotent | Unitary |
| --- | :---: | :---: | :---: |
| Reader (transaction environment) | ✓ | ✓ | ✓ |
| Failure (unit-typed exception) | ✓ | ✓ | ✗ |
| Writer (log as a set) | ✓ | ✓ | ✗ |
| General exceptions (arbitrary type) | ✗ | ✓ | ✗ |

### In Simplicity erlaubte Effekte

Je besser sich ein Effekttyp verhält, desto mehr Spielraum hat ein Simplicity-Optimierer, um Programme zu transformieren, die diese Effekte verwenden. Idealerweise würden wir nur Effekte erlauben, die alle drei Eigenschaften besitzen: kommutativ, idempotent und unitär. Dies würde es einem Optimierer erlauben, jede beliebige Art von Programmtransformation vorzunehmen. Das Lesen aus einer Umgebung ist jedoch der einzige Effekt, der alle drei Eigenschaften erfüllt.

Stattdessen verlangen wir, dass Simplicity-Effekte kommutativ und idempotent sind. Beide in Simplicity verwendeten Effekte, der Failure-Effekt und der Reader-Effekt, sind kommutativ und idempotent. Dies ermöglicht eine große Klasse von Optimierungen an Simplicity-Code.

Die oben beschriebene "Verwerfen"-Transformation, die versucht, `f ⨾ unit` durch `unit` zu ersetzen, oder eine ähnliche Transformation ist jedoch nicht erlaubt, wenn `f` einen Failure-Effekt erzeugen kann. Stell dir vor, `f` enthielte eine `bip0340-verify`-Assertion. Es wäre katastrophal, diese Prüfung wegzuoptimieren.

### Warum überhaupt Seiteneffekte erlauben?

Warum erlaubt Simplicity überhaupt Seiteneffekte? Wäre es nicht besser, wenn jedes Programm die gesamte Transaktion als Eingabe nähme und eine Boolesche Ausgabe zurückgäbe, die entscheidet, ob eine Transaktion gültig ist oder nicht?

#### Batch-Verifikation

Ein Grund, warum wir den Failure-Effekt haben, ist die Unterstützung der [Batch-Verifikation](https://github.com/bitcoin/bips/blob/c9a6ca6297eb8de850f6b64dafb8e60ee9b64d66/bip-0340.mediawiki#batch-verification) von Schnorr-Signaturen. Bei der Batch-Verifikation werden viele einzelne Schnorr-Signaturprüfungen so gebündelt, dass, wenn eine einzelne Signaturprüfung fehlschlägt, der gesamte Batch fehlschlägt.

Dieses Batching-Verfahren verbessert die Effizienz gegenüber der individuellen Verifikation jeder Signatur. Der Nachteil ist, dass wir, wenn die Batch-Verifikation fehlschlägt, nicht erfahren, welche spezifische Signaturprüfung oder -prüfungen fehlgeschlagen sind.

Durch die Verwendung des Failure-Seiteneffekts stellt `bip0340-verify` sicher, dass, wenn eine Signaturprüfung fehlschlägt, die gesamte Transaktion fehlschlägt. Würde `bip0340-verify` stattdessen `𝟚`, einen Booleschen Typ, für Erfolg oder Misserfolg zurückgeben, könnte eine fehlgeschlagene Signaturprüfung dennoch zu einem Zweig führen, in dem das Script erfolgreich ist. In einem solchen Fall müssten wir wissen, ob die jeweilige Signatur gültig ist oder nicht, und könnten somit nicht von der Batch-Verifikation profitieren.

#### Vorberechnete Transaktionsdaten

Ein Problem in frühem Bitcoin Script war, dass die Hashfunktion, die zur Erstellung von Message-Digests für Signaturen verwendet wurde, linear in der Größe der Transaktion war. Typischerweise erzeugt jeder Input mindestens einen Message-Digest für die Signaturverifikation, sodass die Gesamtmenge an Hashing quadratisch in der Transaktionsgröße war.

Dieses Problem wurde in Segwit und späteren Iterationen von Bitcoin Script behoben, indem die Message-Digests so neu definiert wurden, dass sie pro Signaturprüfung in konstanter Zeit berechnet werden können. Dies stützt sich auf `PrecomputedTransactionData`, das Hashes von Transaktionsdaten einmal vorberechnet und diese dann von den Sighash-Berechnungen jedes Inputs gemeinsam genutzt werden. Simplicitys Transaktions-Hashing-Jets stützen sich auf dieselbe Art vorberechneter Transaktionsdaten, um sicherzustellen, dass die Jets in konstanter Zeit laufen.

Angenommen, `sig-all-hash` verwendete nicht den Reader-Effekt. Angenommen, wir hätten es irgendwie geschafft, einen Simplicity-Typ für die Transaktionsumgebung zu bauen. Nennen wir ihn `TxEnv`, sodass `sig-all-hash : TxEnv ⊢ 𝟚²⁵⁶` der Typ des Jets wäre. Eine solche Definition würde erfordern, dass der `sig-all-hash`-Jet den Hash jeder beliebigen Transaktion berechnen kann, nicht nur der Transaktion, an der er beteiligt ist. Simplicity-Programme könnten das gegebene `TxEnv` kopieren und eine modifizierte Kopie davon an `sig-all-hash` übergeben. In einem solchen Fall könnte sich `sig-all-hash` nicht auf `PrecomputedTransactionData` verlassen, und wir wären wieder bei linearer Zeit bezüglich der Transaktionsdaten, die an diese Version von `sig-all-hash` übergeben werden.

Da `sig-all-hash : 𝟙 ⊢ 𝟚²⁵⁶` den Reader-Effekt verwendet, um auf die Transaktionsdaten zuzugreifen, erhält er _nur_ Zugriff auf eine feste Transaktionsumgebung. Aus diesem Grund kann die Implementierung des Jets sicher `PrecomputedTransactionData` verwenden und in konstanter Zeit operieren.

### Cross-Input-Signaturaggregation

Obwohl weder Liquid noch Bitcoin derzeit [Cross-Input-Signaturaggregation](https://hrf.org/latest/cisa-research-paper/) unterstützen, möchten wir sicherstellen, dass Simplicity damit kompatibel sein kann, wenn es soweit ist.

Auch wenn die Details noch nicht ausgearbeitet sind, stellen wir uns vor, dass Halbaggregation mithilfe eines Writer-Effekts implementiert wird. Das heißt, ein neuer Jet mit einem Typ wie `half-agg-verify : (𝟚²⁵⁶ × 𝟚²⁵⁶) × 𝟚²⁵⁶ ⊢ 𝟙` würde einen öffentlichen Schlüssel, einen Message-Digest und die `r`-Komponente einer Schnorr-Signatur (eine Schnorr-Signatur besteht aus einer `r`-Komponente und einer `s`-Komponente) nehmen und in ein Transaktionslog schreiben, bevor die Ausführung fortgesetzt wird. Anschließend würde an anderer Stelle in der Transaktion oder mit der Transaktion eine aggregierte `s`-Komponente für alle halbaggregierten Schnorr-Signaturen bereitgestellt. Die Transaktion wäre nur gültig, wenn eine solche aggregierte `s`-Komponente für alle protokollierten Schlüssel, Nachrichten und `r`-Komponenten bereitgestellt wird.

Um Simplicitys Anforderungen zu erfüllen, muss dieser Writer-Effekt idempotent und kommutativ sein. Dies lässt sich sicherstellen, indem das Writer-Log als eine Menge von Schlüssel-, Nachrichten-, `r`-Komponenten-Tupeln behandelt wird. Dies funktioniert, weil Mengenoperationen idempotent und kommutativ sind. Das Log als eine Menge von Werten zu behandeln wäre mit dem Halbaggregations-Verifikationsalgorithmus kompatibel.

### Fazit

In diesem Kapitel haben wir betrachtet, wie man den Berechnungen, die Simplicity ausführen kann, Seiteneffekte hinzufügt. Wir haben verschiedene Arten von Effekten danach klassifiziert, wie gut sie sich gegenüber verschiedenen Arten von Programmtransformationen verhalten. Wir haben entschieden, Simplicitys Effekte auf solche zu beschränken, die kommutativ und idempotent sind.

Die beiden Effekte, die wir für Bitcoin- und Liquid-Anwendungen verwenden, sind der Reader-Effekt für den Zugriff auf die Transaktionsumgebung und der Failure-Effekt für den Abbruch und das Fehlschlagen des Programms. Manche Jets nutzen primitive Operationen, bei denen diese Art von Seiteneffekten auftreten kann.

Der Failure-Effekt bestimmt die Ausgabe eines Simplicity-Programms: Das Programm schlägt entweder fehl, wodurch die Transaktion ungültig wird, oder das Programm gelingt. Der Reader-Effekt liefert eine Art von Eingabe für ein Simplicity-Programm: die Umgebung, die Transaktionsdaten enthält. Wir müssen aber auch andere Eingaben, wie digitale Signaturen, an Simplicity-Programme liefern.

Im nächsten Kapitel betrachten wir, was Simplicity-Programme sind, wie sie zu Adressen werden, und wie wir andere Eingaben, wie Signaturen, zu Simplicity-Programmen hinzufügen.

## Programme und Adressen

<chapterId>961652e3-8f7d-4c2a-8b55-9a990b91a0dd</chapterId>

Im vorherigen Kapitel haben wir zwei in Simplicity verwendete Seiteneffekte beschrieben: den Failure-Effekt, der über Erfolg oder Misserfolg eines Programms entscheidet, und den Reader-Effekt, der Zugriff auf die Transaktionsumgebung liefert. Nun wenden wir uns der praktischen Frage zu: Was genau ist ein Simplicity-Programm, und wie wird es zu einer Adresse auf der Blockchain?

### Simplicity-Programme

Ein Simplicity-Programm ist als Simplicity-Ausdruck vom Typ `𝟙 ⊢ 𝟙` definiert. Diese Typsignatur bedeutet, dass das Programm keine bedeutungsvolle Eingabe nimmt (nur den Unit-Wert) und keine bedeutungsvolle Ausgabe liefert (nur den Unit-Wert). Der Reader-Effekt erfasst die Eingabe der Transaktionsumgebung, während der Failure-Effekt Erfolg oder Misserfolg anzeigt. Diese Effekte handhaben I/O statt Simplicity-Typen selbst.

### Commitment-Merkle-Root

Anstatt vollständige Programme on-chain zu speichern, setzt Bitcoin auf Commitments — eine Praxis, die sich von Pay-to-Script-Hash (P2SH) fortsetzt. Simplicity verwendet einen Commitment-Merkle-Root (CMR).

Jeder Kombinator erhält einen SHA-256-Tag, der aus dem Muster `Simplicity␟Commitment␟[identifier]` abgeleitet ist, wobei `␟` den ASCII-Code 31 (den Unit Separator) darstellt.

Jeder Tag ist der SHA-256-Hash der entsprechenden Pre-Image-Zeichenkette, die unten aufgeführt ist:

| Combinator | Tag pre-image (ASCII string) |
|---|---|
| `iden` | `Simplicity␟Commitment␟iden` |
| `unit` | `Simplicity␟Commitment␟unit` |
| `comp` | `Simplicity␟Commitment␟comp` |
| `pair` | `Simplicity␟Commitment␟pair` |
| `case` | `Simplicity␟Commitment␟case` |
| `take` | `Simplicity␟Commitment␟take` |
| `drop` | `Simplicity␟Commitment␟drop` |
| `injl` | `Simplicity␟Commitment␟injl` |
| `injr` | `Simplicity␟Commitment␟injr` |

Ein Simplicity-Ausdruck wird dann rekursiv zu einem 256-Bit-CMR gehasht, indem für jeden Kombinator zusammen mit den CMRs seiner Argumente ein getaggter SHA-256-Midstate berechnet wird (schreibe `#ᶜ(e)` für den CMR des Ausdrucks `e`, und `∥` für Byte-Konkatenation):

| Combinator | CMR rule |
|---|---|
| `iden` | `#ᶜ(iden) = SHA-256-midstate(tag_iden ∥ tag_iden)` |
| `unit` | `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)` |
| `comp f g` | `#ᶜ(comp f g) = SHA-256-midstate(tag_comp ∥ tag_comp ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `pair f g` | `#ᶜ(pair f g) = SHA-256-midstate(tag_pair ∥ tag_pair ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `case f g` | `#ᶜ(case f g) = SHA-256-midstate(tag_case ∥ tag_case ∥ #ᶜ(f) ∥ #ᶜ(g))` |
| `take f` | `#ᶜ(take f) = SHA-256-midstate(tag_take ∥ tag_take ∥ 32·0x00 ∥ #ᶜ(f))` |
| `drop f` | `#ᶜ(drop f) = SHA-256-midstate(tag_drop ∥ tag_drop ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injl f` | `#ᶜ(injl f) = SHA-256-midstate(tag_injl ∥ tag_injl ∥ 32·0x00 ∥ #ᶜ(f))` |
| `injr f` | `#ᶜ(injr f) = SHA-256-midstate(tag_injr ∥ tag_injr ∥ 32·0x00 ∥ #ᶜ(f))` |

Binäre Kombinatoren (`comp`, `pair`, `case`) verketten die CMRs beider Kinder; unäre Kombinatoren (`take`, `drop`, `injl`, `injr`) verketten den CMR ihres einzigen Kindes nach 32 Bytes `0x00`-Padding; und die nullstelligen Blätter (`iden`, `unit`) hashen ihren Tag allein. Zwei Konventionen halten dies kostengünstig zu berechnen: SHA-256-Midstates werden verwendet, sodass **jeder Ausdruck höchstens einen Aufruf der SHA-256-Kompressionsfunktion erfordert** (vorausgesetzt, der Midstate bis zu den konstanten Tags ist vorberechnet), und die einargumentigen Konstruktoren stellen ihrem Argument 32 Bytes `0x00`-Padding voran, was etwas zusätzliche Vorberechnung für Implementierungen erlaubt, die dies wünschen.

Für den `unit`-Kombinator — einen nullstelligen Konstruktor ohne Argument-Teilausdrücke — spezialisiert sich diese Regel zu `#ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)`, wobei `tag_unit = SHA-256(Simplicity␟Commitment␟unit)` (der Tag wird zweimal eingespeist). Der resultierende CMR für das triviale `unit`-Programm ist:

```
0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

Entscheidend ist, dass der CMR sich nicht auf die Typen von Simplicity-Ausdrücken committet, sondern sich stattdessen auf Typinferenz bei der Einlösung stützt.

### Adressen

Adressen verwenden den Taproot-Mechanismus von BIP-0341, wobei CMRs unter der TapLeaf-Version `0xbe` committet werden. Der Prozess umfasst:

1. Berechnung eines TapLeaf-getaggten Hashes, der das Versionsbyte, die CMR-Länge und den CMR selbst kombiniert
2. Tweaken eines internen öffentlichen Schlüssels (unter Verwendung eines NUMS-Punkts, wenn kein Key-Spend-Pfad gewünscht ist)
3. Umwandlung ins Bech32m-Format
4. Hinzufügen geeigneter Prüfsummen

Wenn kein Key-Spend-Pfad gewünscht ist, wird der interne öffentliche Schlüssel auf einen **NUMS**-Punkt ("Nothing-Up-My-Sleeve") gesetzt: ein Kurvenpunkt, der absichtlich so gewählt wurde, dass niemand seinen diskreten Logarithmus kennt — mit anderen Worten, ein Punkt ohne zugehörigen privaten Schlüssel. Da niemand jemals eine Signatur für ihn erzeugen kann, ist der Key-Spend-Pfad nachweislich unbenutzbar, und der Output kann *nur* über den committeten Simplicity-Skriptpfad ausgegeben werden. In einer echten Anwendung sollte dieser NUMS-Punkt, wie in BIP-0341 empfohlen, randomisiert werden, sodass Outputs ohne Key-Spend-Pfad von gewöhnlichen Taproot-Outputs nicht unterscheidbar sind (ein Datenschutzvorteil).

#### Von Simplicity zur Adresse

Gehen wir die vollständige Ableitung für das einfachstmögliche Programm durch: `unit : 𝟙 ⊢ 𝟙`, ein No-Op, das immer erfolgreich ist.

**1. Kombinator-Tag.** Zuerst den `unit`-Tag berechnen:

```
tag_unit = SHA-256(Simplicity␟Commitment␟unit)
         = 0xd723083cff3c75e29f296707ecf2750338f100591c86e0c71717f807ff3cf69d
```

**2. CMR.** Den Tag zweimal einspeisen, um den CMR des Programms zu erhalten:

```
CMR = #ᶜ(unit) = SHA-256-midstate(tag_unit ∥ tag_unit)
    = 0xc40a10263f7436b4160acbef1c36fba4be4d95df181a968afeab5eac247adff7
```

**3. TapLeaf-Hash.** Dem CMR die TapLeaf-Version von Simplicity `0xbe` und die CMR-Länge `0x20` (32 Bytes) voranstellen, dann den getaggten Elements-TapLeaf-Hash bilden (ein getaggter Hash ist `hash_str(x) = SHA-256(SHA-256(str) ∥ SHA-256(str) ∥ x)`):

```
hash_TapLeaf/elements(0xbe ∥ 0x20 ∥ CMR)
  = 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c
```

Da es nur dieses eine Blatt gibt, gibt es keine TapBranches, sodass dieser Hash bereits die TapTree-Wurzel ist.

**4. TapTweak.** Da wir keinen Key-Spend-Pfad wollen, verwenden wir den BIP-0341-NUMS-Punkt als internen Schlüssel und tweaken ihn mit der TapTree-Wurzel:

```
internal_pk = 0x50929b74c1a04954b78b4b6035e97a5e078a5a0f28ec96d547bfee9ace803ac0
t = hash_TapTweak/elements(internal_pk ∥ 0x44cc38311ec7e5dfb7b573baf38449496ecd334eb5509cfed1b4fd30da8dd41c)
  = 0xb3bef172389b0937d7e5a8b15cfa41e776777f13f2f659cb06220a6ff0658285
```

**5. Output-Schlüssel.** Den internen Schlüssel auf der Kurve tweaken, `output_pk = lift_x(internal_pk) ⊕ t·G` (die elliptische-Kurven-Arithmetik ist hier zusammengefasst), was den x-only Output-Schlüssel `0x2cb0c20acd7340b4d4b65f6a60e2888d0d64e3267261f3b3cf7290e5af3f9e09` ergibt.

**6. Bech32m-Adresse.** Den x-only Output-Schlüssel kodieren, ein `p` voranstellen (das SegWit-v1-Witness-Versionszeichen), das Liquid-Testnet-Human-Readable-Präfix `tex1` hinzufügen und die Bech32m-Prüfsumme anhängen. Die endgültige Adresse lautet:

```
tex1p9jcvyzkdwdqtf49kta4xpc5g35xkfcexwfsl8v70w2gwttelncyshxjk56
```

Das war viel Arbeit — aber der Großteil davon wird durch Taproot selbst vorgeschrieben, nicht durch Simplicity.

### Witness-Ausdrücke

Ein neuer Kombinatortyp adressiert das Fehlen von Eingaben für Simplicity-Programme: der Witness-Ausdruck. Der `witness`-Kombinator erlaubt es, Signaturdaten und anderes Witness-Material in Programme zu integrieren.

```
      w : B
-----------------
witness w : A ⊢ B
```

Die Semantik des Witness-Ausdrucks ist einfach: Er ignoriert seine Eingabe und gibt einfach den Wert `w` zurück (der von jedem beliebigen Simplicity-Typ sein kann), d. h. `⟦witness w⟧(a) = w`. Dies fügt **keine neue Ausdrucksstärke** hinzu — laut dem Vollständigkeitssatz kann Simplicity bereits jede solche konstante Funktion bauen (erinnere dich an das `scribe`-Makro aus den vorherigen Kapiteln). Der Sinn des `witness`-Kombinators liegt vollständig in seinem **CMR**: Der Wert `w` ist **aus dem CMR des Ausdrucks ausgeschlossen**, sodass die Adresse berechnet werden kann, bevor `w` bekannt ist, und `w` bei der Einlösung geliefert wird.

Diese Designentscheidung unterstützt das Pruning — nicht ausgeführte bedingte Zweige müssen on-chain nicht offengelegt werden, einschließlich ihrer zugehörigen Witness-Ausdrücke. Wenn ein Zweig abgeschnitten wird, benötigt der Verifizierer nur den CMR des abgeschnittenen Teilbaums, nicht seinen tatsächlichen Inhalt.

### Witness-Werte

Es mag wie eine Einschränkung wirken, dass ein Witness-Ausdruck nur einen *Wert* enthalten kann und nicht einen allgemeineren Simplicity-Ausdruck. Aber Programme für UTXO-basierte Blockchains werden nur einmal ausgeführt. Es besteht keine Notwendigkeit, einen ganzen Teilausdruck in einen Witness-Knoten zu übergeben: Der Nutzer kann diesen Teilausdruck einfach selbst, off-chain, ausführen und dessen Ausgabe in den Witness-Wert übertragen, um dasselbe Ergebnis zu erhalten.

(Später in diesem Kurs begegnen wir dem `disconnect`-Kombinator, der sich sehr ähnlich wie ein Witness-Ausdruck verhält, der aber *tatsächlich* einen ganzen Simplicity-Ausdruck als sein Argument nimmt.)

Ein alternatives Design würde alle Witness-Daten als Argument in das Top-Level-Simplicity-Programm einspeisen. Witness-Ausdrücke werden aus zwei Gründen bevorzugt. Erstens **Pruning**: Nicht ausgeführte Zweige von `case`-Ausdrücken werden nie on-chain offengelegt, und alle Witness-Ausdrücke innerhalb dieser Zweige werden zusammen mit ihnen abgeschnitten. Zweitens **Lokalität**: Witness-Ausdrücke erlauben es uns, jeden Witness-Wert genau dort zu platzieren, wo er verwendet wird, anstatt ihn vom Top-Level-Input des Programms nach unten durchzureichen.

### Typinferenz

Da CMRs sich nicht auf Typen committen, wird das Typsystem bei der Einlösung rekonstruiert. Simplicitys Typinferenzalgorithmus bestimmt die minimalen Typen für jeden Teilausdruck basierend auf der Kombinatorstruktur. Genauer gesagt berechnet die Inferenz den *principal*-Typ (den allgemeinsten Typ) jedes Teilausdrucks; alle verbleibenden freien Typvariablen werden dann mit dem Unit-Typ `𝟙` instanziiert, was einen eindeutigen, minimalen Typ für das Programm ergibt.

### Fazit

In diesem Kapitel haben wir festgestellt, dass Simplicity-Programme Ausdrücke vom Typ `𝟙 ⊢ 𝟙` sind, erklärt, wie Commitment-Merkle-Roots aus getaggten SHA-256-Hashes jedes Kombinators konstruiert werden, und gezeigt, wie CMRs über BIP-0341-Taproot in On-Chain-Adressen umgewandelt werden. Wir haben Witness-Ausdrücke als den Mechanismus eingeführt, um Signaturdaten und andere Eingaben zum Zeitpunkt der Ausgabe zu liefern, ohne sich bei der Adresserstellung auf ihre Werte zu committen.

# Abschlussteil

<partId>96952535-4aa6-4e78-91e2-d12e9df895d4</partId>

## Bewertungen & Rezensionen

<chapterId>fb0b0133-39ea-497b-bd36-198be42c4fab</chapterId>
<isCourseReview>true</isCourseReview>

## Abschlussprüfung

<chapterId>2cc5e818-abcb-4a0a-9991-7a492c572e2d</chapterId>
<isCourseExam>true</isCourseExam>

## Fazit

<chapterId>8ade24bd-a84f-4d25-8f64-bdfa8b58926c</chapterId>
<isCourseConclusion>true</isCourseConclusion>
</content>
