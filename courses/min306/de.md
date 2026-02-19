---
name: Bitaxe Open Source Mining Mastery
goal: Beherrschen Sie das komplette Bitaxe-Ökosystem, vom Zusammenbau der Hardware bis zur fortgeschrittenen Anpassung und Leistungsoptimierung
objectives: 

  - Verstehen der Philosophie der quelloffenen Bitcoin mining Hardware
  - Bitaxe mining Geräte von Grund auf neu bauen
  - Konfigurieren und Optimieren der mining-Software einschließlich AxeOS und Public Pool
  - Implementierung erweiterter Leistungsoptimierungen, einschließlich Übertaktung und Benchmarking

---

# Ihr Bitaxe Mining Führer


Willkommen zum umfassenden Bitaxe-Kurs, in dem Sie die revolutionäre Open-Source-Hardware Bitcoin mining beherrschen werden, die den Zugang zur mining-Technologie demokratisiert. Dieser Kurs führt Sie vom Verständnis der philosophischen Grundlagen des dezentralen mining bis hin zu fortgeschrittenen Techniken zur Hardware-Anpassung und Leistungsoptimierung.


Das Bitaxe-Projekt stellt einen Paradigmenwechsel bei Bitcoin mining dar, indem es das Monopol der proprietären ASIC-Hersteller durch die Bereitstellung von vollständig quelloffenen Designs, Firmware und Software bricht. In diesen praxisnahen Kapiteln erwerben Sie praktische Fähigkeiten in den Bereichen Hardwaremontage, Softwarekonfiguration, PCB-Design und Leistungsoptimierung.


Es ist keine vorherige mining-Erfahrung erforderlich, obwohl grundlegende Elektronikkenntnisse und Vertrautheit mit GitHub hilfreich sind. Der Kurs wird Sie von einem neugierigen Beobachter in einen fähigen Bitaxe-Erbauer und Mitwirkenden verwandeln.


+++


# Einführung


<partId>6b3cd9f0-0063-40f0-a7bb-00a48f330d88</partId>


## Überblick über den Kurs


<chapterId>1fac9579-0e1c-48e3-9bc5-e7a2960018c8</chapterId>


Willkommen zum Kurs MIN 306 _**Bitaxe Open Source Mining Mastery**_, einer umfassenden Reise in die Welt von Bitaxe mining. Dieser Kurs ist für diejenigen gedacht, die ihre eigene Bitaxe mining Hardware verstehen, bauen und optimieren wollen, während sie die philosophischen und technischen Grundlagen erforschen, die dieses Projekt innerhalb des Bitcoin Ökosystems einzigartig machen.


### Bitaxe verstehen


Der erste Abschnitt legt die wesentlichen Grundlagen: Sie werden die Ursprünge des Bitaxe-Projekts, seine Entwicklung und die Werte der Dezentralisierung und Transparenz, die es definieren, entdecken. Sie erfahren, was eine Bitaxe eigentlich ist, wie sie sich von proprietären ASICs unterscheidet und wo Sie Community-Ressourcen finden, um Ihr Wissen zu vertiefen. Dieser Abschnitt liefert den nötigen Kontext, um zu verstehen, warum Bitaxe einen Wendepunkt in der Geschichte von Bitcoin mining darstellt.


### Software und Betrieb


Der zweite Abschnitt konzentriert sich auf die Softwareumgebung mit einer detaillierten Präsentation von *AxeOS*: dem Open-Source-Betriebssystem, das speziell für Bitaxe-Geräte entwickelt wurde. Sie lernen seine wichtigsten Funktionen kennen und erfahren, wie Sie Ihr Gerät konfigurieren und mit ihm interagieren, um Ihren ersten mining-Betrieb zu starten.


### Gemeinschaft und Zusammenarbeit


Der dritte Abschnitt beleuchtet den kollaborativen Aspekt des Projekts. Sie werden die Open-Source-Philosophie erkunden, die sowohl bei der Hardware- als auch bei der Software-Entwicklung von Bitaxe zur Anwendung kommt. Durch praktische Übungen werden Sie lernen, wie Sie direkt zum Quellcode beitragen können, und Sie werden auch _Public Pool_ kennenlernen, eine Gemeinschaftsplattform zur Bündelung von Rechenleistung. Sie werden auch lernen, wie man es auf einem Umbrel-Knoten für lokale und souveräne Integration installiert.


### Hardware-Montage und Fehlersuche


Im vierten Abschnitt geht es um die Hardware selbst. Sie werden lernen, wie man die Werkzeuge identifiziert, die für den Zusammenbau eines Bitaxe benötigt werden, Lötprobleme behebt und eine vollständige Diagnose mit *AxeOS* und USB-Tools durchführt. Dieser Abschnitt legt den Schwerpunkt auf praktische Übungen und ein tiefes Verständnis für das Zusammenspiel von Hardware- und Softwarekomponenten.


### Erweiterte Anpassung


Der fünfte Abschnitt ist der Anpassung gewidmet. Sie erfahren, wie Sie die Leiterplatte (PCB) modifizieren, eine Fabrikdatei erstellen und den _Bitaxe Web Flasher_ verwenden. Dieser Abschnitt richtet sich an diejenigen, die über den einfachen Zusammenbau hinausgehen und wirklich individuelle Versionen ihres eigenen Geräts entwerfen wollen.


### Optimierung der Leistung


Der sechste Abschnitt schließlich behandelt fortgeschrittene Optimierungstechniken. Sie lernen, wie Sie die Leistung Ihres Bitaxe mit Hilfe von Benchmarks bewerten können und wie Sie ihn effizient übertakten können. Diese Fähigkeiten helfen Ihnen, das Beste aus Ihrer Hardware herauszuholen und gleichzeitig ihre physikalischen Grenzen zu respektieren.


Wie bei allen Kursen der Plan ₿ Academy enthält der letzte Abschnitt eine Bewertung, um Ihr Wissen zu festigen.


Tauchen Sie ein in dieses technische Abenteuer - die Zukunft von Bitcoin mining liegt in Ihren Händen!


# Bitaxe verstehen

<partId>ba1cb4ea-6a77-54fd-916c-57285c8c2418</partId>


## Die Geschichte

<chapterId>73d928e5-72f0-5c17-a7a6-8b6ece7f9a30</chapterId>

:::video id=67d2529a-b7cb-4804-b02c-e56c12c9e66e:::

Das Bitaxe-Projekt stellt einen bahnbrechenden Wandel in der Bitcoin-[mining](https://planb.academy/resources/glossary/mining)-Hardwareentwicklung dar und bringt Open-Source-Prinzipien in eine Branche, die von proprietären Lösungen dominiert wird. Diese Bildungsreihe erforscht die umfassende Geschichte, die technischen Innovationen und die von der Gemeinschaft vorangetriebene Entwicklung von Bitaxe und gibt Einblicke, wie sich die Vision eines einzelnen Ingenieurs in ein florierendes Ökosystem dezentraler mining-Hardware verwandelte. Durch die Untersuchung der Ursprünge, Herausforderungen und Errungenschaften des Projekts gewinnen wir ein wertvolles Verständnis sowohl für die technische Komplexität der [ASIC](https://planb.academy/resources/glossary/asic)-Entwicklung als auch für die Macht der Open-Source-Zusammenarbeit im Bitcoin-Bereich.


### Die Entstehungsgeschichte: Von der Entdeckung der Seidenstraße zur Solar-Mining-Vision


Skot, der Gründer von Bitaxe, begann seine Reise in Bitcoin auf einer College-Party, wo er zum ersten Mal von Bitcoin durch jemanden erfuhr, der Gegenstände auf der Seidenstraße kaufte. Dieser erste Kontakt mit Bitcoin zu einem Preis von etwa 20 Dollar pro Münze weckte eine Neugier, die sich später zu einem revolutionären mining-Projekt entwickeln sollte. Die technische Grundlage für seine zukünftige Arbeit wurde während seiner Zeit an der Universität geschaffen, wo er Zugang zu umfangreichen FPGA-Ressourcen in einer Laborumgebung hatte. In Zusammenarbeit mit seinem Doktorvater begann Skot mit Open-Source-FPGA-Bitstreams für Bitcoin mining zu experimentieren, zunächst mit dem bescheidenen Ziel, mining genug Bitcoin zu geben, um eine Pizza für ihr Büro zu kaufen.


Der Übergang vom akademischen Experimentieren zur ernsthaften Entwicklung erfolgte Jahre später, als Skot an solarbetriebenen Gateways für die Ferndatenerfassung in Afrika arbeitete. Diese berufliche Erfahrung mit Solarenergiesystemen führte zu der Erkenntnis, dass Bitcoin mining ASICs, die grundsätzlich Niederspannungs-Gleichstromgeräte sind, perfekt mit Solarpanels zusammenpassen würden. Das Konzept schien natürlich und elegant. Als Skot jedoch begann, nach bestehenden Lösungen zu suchen, entdeckte er eine erhebliche Marktlücke: Im Gegensatz zu den Anfängen von Bitcoin mining, als FPGA-Designs offen zugänglich waren, hatte sich die Branche mit dem Aufkommen der ASICs in Richtung vollständig proprietärer, Closed-Source-Lösungen bewegt.


Der Mangel an quelloffener mining-Hardware wurde für Skot zu einer treibenden Frustration, insbesondere angesichts seines Hintergrunds in der Open-Source-Softwareentwicklung und seiner Überzeugung, dass der Open-Source-Charakter des Bitcoin auch für die mining-Infrastruktur gelten sollte. Diese philosophische Ausrichtung auf Open-Source-Prinzipien in Verbindung mit der technischen Herausforderung des Reverse-Engineering proprietärer ASIC-Designs bildete die Grundlage für das, was das Bitaxe-Projekt werden sollte. Die anfängliche Vision war ehrgeizig und doch praktisch: einen solarbetriebenen Bitcoin [Miner](https://planb.academy/resources/glossary/miner) zu entwickeln, der unabhängig arbeiten kann, ohne einen separaten Computer zur Steuerung zu benötigen, so dass er sich für den Einsatz an abgelegenen Orten unter Sonnenkollektoren eignet.


### Technische Herausforderungen und Durchbrüche beim Reverse Engineering


Die Entwicklung von Bitaxe erforderte die Überwindung erheblicher technischer Hindernisse, die sich vor allem auf das völlige Fehlen einer Dokumentation der ASIC-Chips von Bitmain konzentrierten. Skots Herangehensweise an diese Herausforderung ist ein Beispiel für die Entschlossenheit und den Einfallsreichtum, die für ein erfolgreiches Reverse Engineering erforderlich sind. Ohne Zugang zu offiziellen Datenblättern oder technischen Spezifikationen untersuchte er die Chips unter dem Mikroskop, maß die Pin-Abstände mit einem Messschieber und scannte sogar die Chips, um ihren genauen Platzbedarf zu bestimmen. Dieser mühsame Prozess führte zu mehreren gescheiterten Prototypen, wobei die ersten beiden Iterationen des "Day Miners" aufgrund falscher Footprint-Berechnungen nicht richtig funktionierten.


Der Durchbruch gelang mit der dritten Iteration im Mai 2022, als Skot erfolgreich ein funktionierendes Zwei-Chip-Design mit BM1387-Chips aus Antminer S9-Einheiten entwickelte. Diese Leistung war die Geburtsstunde des Namens Bitaxe, inspiriert vom Konzept einer Spitzhacke für Bitcoin mining. Der Erfolg dieses Entwurfs bestätigte den Reverse-Engineering-Ansatz und zeigte, dass unabhängige Entwickler funktionale mining-Hardware ohne Herstellerunterstützung entwickeln können. Die technischen Herausforderungen erstreckten sich jedoch nicht nur auf die Chip-Schnittstellen, sondern auch auf das komplexe Design der Stromversorgung, da die ASICs eine präzise Spannungsregelung bei hohen Strömen erforderten und oft mit Spannungen von nur 0,6 Volt arbeiteten, während sie gleichzeitig erhebliche Stromstärken aufnahmen.


Die Entwicklung der Firmware stellte eine weitere Komplexitätsebene dar, da das Projekt die Erstellung von mining-Software erforderte, die direkt auf einem ESP32-Mikrocontroller ausgeführt werden konnte, anstatt auf externe Computer mit Software wie CGMiner angewiesen zu sein. Dieser in sich geschlossene Ansatz war für Skots Vision von einsatzfähigen, unabhängigen mining-Einheiten unerlässlich. Die Kombination aus Hardware-Reverse-Engineering und eingebetteter Firmware-Entwicklung stellte eine umfassende technische Herausforderung dar, die Fachwissen aus mehreren Disziplinen erforderte, von Elektrotechnik und PCB-Design bis hin zu eingebetteter Programmierung und Netzwerkprotokollen.


### Bildung von Gemeinschaften und Open-Source-Zusammenarbeit


Die Umwandlung von Bitaxe von einem Einzelprojekt in eine florierende Gemeinschaftsinitiative ist einer der wichtigsten Aspekte des Erfolgs. Anfänglich stießen Skots Versuche, über Bitcoin-Foren und soziale Medien generate-Interesse zu wecken, auf begrenzte Resonanz und gelegentliche Skepsis. Der Durchbruch kam, als Mitglieder der Gemeinschaft wie SirVapesAlot das Potenzial von Open Source mining erkannten und den Open Source Miners United (OSMU) Discord-Server einrichteten. Diese Plattform sorgte für das kollaborative Umfeld, das für das Gedeihen des Projekts notwendig war, und zog Mitwirkende mit unterschiedlichem Hintergrund an, die ein gemeinsames Interesse an der Demokratisierung der Bitcoin mining-Technologie hatten.


Das von der Community betriebene Entwicklungsmodell erwies sich als bemerkenswert effektiv, da wichtige Mitwirkende wie johnny9 und Ben auftauchten, um spezifische technische Herausforderungen zu bewältigen. Johnny9s Expertise in der Firmware-Entwicklung löste kritische Software-Implementierungsprobleme, während Bens Fähigkeiten in der Front-End-Entwicklung das intuitive AxeOS-Dashboard schufen, das die Gerätekonfiguration und -überwachung vereinfachte. Zu Bens zusätzlichen Beiträgen gehörten die Einrichtung von Fertigungskapazitäten und die Schaffung von Public Pool, einem für Bitaxe-Geräte optimierten Open-Source-[mining-Pool](https://planb.academy/resources/glossary/pool-mining). Dieser kollaborative Ansatz zeigte, wie Open-Source-Prinzipien die Entwicklung über das hinaus beschleunigen können, was jeder einzelne Mitarbeiter allein erreichen könnte.


Die OSMU-Gemeinschaft förderte auch ein integratives Umfeld, in dem Neulinge unabhängig von ihren anfänglichen technischen Kenntnissen lernen und ihren Beitrag leisten konnten. Bens eigener Weg vom Lötanfänger zum großen Hersteller ist ein Beispiel für diesen einladenden Ansatz zur Entwicklung von Fähigkeiten. Das Engagement der Gemeinschaft für Bildung und gegenseitige Unterstützung schuf einen positiven Kreislauf, in dem erfahrene Mitglieder Neulinge anleiteten, die dann selbst zu Mitwirkenden wurden. Dieses Modell erwies sich als wesentlich, um das Projekt über seinen ursprünglichen Umfang hinaus zu erweitern und ein nachhaltiges Ökosystem für kontinuierliche Innovation und Wachstum zu schaffen.


### Vision für dezentrales Mining und zukünftige Auswirkungen


Skots langfristige Vision für Bitaxe geht weit über die Schaffung eines weiteren mining-Geräts hinaus: Sie ist eine grundlegende Umgestaltung der mining-Landschaft von Bitcoin. Das ehrgeizige Ziel, eine Million Ein-Terahash-Miner zu produzieren, würde eine Exahash von verteilter mining-Energie schaffen und einen bedeutenden Schritt in Richtung mining-Dezentralisierung darstellen. Diese Vision befasst sich mit kritischen Bedenken bezüglich der mining-Zentralisierung, bei der große Pools und Industrieunternehmen potenziell dem Druck der Regierung oder der Regulierung ausgesetzt sein könnten. Durch die Verteilung der mining-Energie auf zahllose private Bergleute wird das Netzwerk widerstandsfähiger und steht im Einklang mit den dezentralen Prinzipien von Bitcoin.


Das Wirtschaftsmodell, das diese Vision unterstützt, stützt sich auf die einzigartigen Eigenschaften von mining für den Heimgebrauch, wo die Infrastrukturkosten im Wesentlichen gleich Null sind und die Bergleute mit minimaler Aufsicht arbeiten können. Im Gegensatz zum industriellen mining-Betrieb, der massive Kapitalinvestitionen in Anlagen, Strominfrastruktur und Kühlsysteme erfordert, können Heimschürfer ihre Geräte einfach an vorhandene Steckdosen und Internetverbindungen anschließen. Dieser Ansatz könnte theoretisch eine beträchtliche [Hash-Rate](https://planb.academy/resources/glossary/hashrate) online bringen, ohne die traditionellen Eintrittsbarrieren, die für groß angelegte mining-Betriebe charakteristisch sind.


Der Erfolg des Projekts hat bereits begonnen, das breitere Bitcoin mining-Ökosystem zu beeinflussen, mit dem Potenzial, andere Hersteller zu inspirieren, Open-Source-Entwicklungsmodelle zu übernehmen. Die von den Bitaxe-Herstellern unter Beweis gestellte finanzielle Rentabilität beweist, dass Open-Source-Hardware kommerziell erfolgreich sein kann und gleichzeitig die Transparenz und die Beteiligung der Gemeinschaft aufrechterhalten wird. Während sich das Projekt mit neuen Chip-Integrationen, verbesserten Designs und erweiterten Fertigungspartnerschaften weiterentwickelt, dient es als Konzeptnachweis dafür, wie Bitcoin mining zu seinen dezentralen Wurzeln zurückkehren und gleichzeitig moderne ASIC Technologie einbeziehen kann. Das letztendliche Ziel geht über die bloße Verbreitung von Hash-Raten hinaus und umfasst auch eine erzieherische Wirkung, die mehr Menschen in direkten Kontakt mit dem grundlegenden Bitcoin mining-Prozess bringt und ein tieferes Verständnis für das Sicherheitsmodell des Netzwerks fördert.


## Was ist die Bitaxe?

<chapterId>6a56af56-35ce-51af-999b-4bc7305e6464</chapterId>

:::video id=12b26c7a-74b1-4ea9-afc0-e3ef90cf5837:::

### Hardware-Übersicht und -Funktionen


Das Bitaxe-Ökosystem umfasst mehrere Hardware-Iterationen, die jeweils darauf ausgelegt sind, verschiedene Aspekte des mining-Erlebnisses zu optimieren und gleichzeitig die Kernphilosophie der Open-Source-Zugänglichkeit zu wahren. Diese Geräte dienen nicht nur als funktionale mining-Hardware, sondern auch als Lehrmittel, die es den Benutzern ermöglichen, die komplizierte Beziehung zwischen ASIC-Chips, Mikrocontrollern und dem Bitcoin-mining-Prozess zu verstehen. Das Verständnis der Designphilosophie und der technischen Umsetzung der Bitaxe bietet wertvolle Einblicke in die Funktionsweise moderner mining-Hardware sowohl auf Komponenten- als auch auf Systemebene.



### Bitaxe Max, Implementierung der ersten Generation


Der Bitaxe Max stellt die grundlegende Implementierung des Bitaxe-Konzepts dar und nutzt den BM1397 ASIC Chip, der ursprünglich von Bitmain für ihre S17 mining Serie entwickelt wurde. Diese Chip-Integration zeigt, wie Open-Source-Hardware bestehende ASIC-Technologie wiederverwenden kann, um zugängliche mining-Lösungen zu schaffen. Der Bitaxe Max liefert eine geschätzte Hash-Rate von 300 bis 400 Gigahashes pro Sekunde, was ihn eher als eine pädagogische und experimentelle mining-Plattform denn als eine kommerzielle Lösung positioniert.


Die Integration des BM1397-Chips in den Bitaxe Max erforderte eine sorgfältige Berücksichtigung von Energiemanagement, Wärmeregelung und Kommunikationsprotokollen. Das Design des Boards berücksichtigt die spezifischen Anforderungen dieses ASIC und bietet gleichzeitig die notwendigen unterstützenden Schaltungen für einen stabilen Betrieb. Diese Implementierung zeigt, wie die Open-Source-Hardwareentwicklung bestehende Halbleitertechnologie nutzen kann, um neue Anwendungen und Lernmöglichkeiten innerhalb der mining-Gemeinschaft zu schaffen.


### Bitaxe Ultra, fortschrittliche Chip-Technologie


Die Bitaxe Ultra stellt die Weiterentwicklung der Bitaxe-Plattform dar und enthält den fortschrittlicheren BM1366 ASIC Chip aus der S19-Serie von Bitmain. Diese neuere Chiptechnologie bringt der Bitaxe-Plattform verbesserte Effizienz- und Leistungsmerkmale, während die grundlegende Designphilosophie beibehalten wird. Das Upgrade auf den BM1366-Chip demonstriert die Anpassungsfähigkeit der Plattform und das Engagement der Community, technologische Fortschritte in Open-Source-mining-Lösungen zu integrieren.


Der Übergang vom BM1397- zum BM1366-Chip erforderte Änderungen an den Stromversorgungssystemen, dem Wärmemanagement und den Steuerungsalgorithmen der Karte. Diese Änderungen verdeutlichen den iterativen Charakter der Hardwareentwicklung und die Bedeutung der Aufrechterhaltung der Kompatibilität bei gleichzeitiger Leistungssteigerung. Die Bitaxe-Ultra-Implementierung bietet den Nutzern Zugang zu neuerer ASIC-Technologie und bewahrt gleichzeitig den Lehr- und Experimentiercharakter der Plattform.


### Mikrocontroller und Kommunikationssysteme


Das Herzstück eines jeden Bitaxe-Geräts ist ein ESP-Mikrocontroller, der als primäre Schnittstelle zwischen dem Benutzer und dem ASIC-Chip dient. Auf diesem Mikrocontroller läuft eine spezielle Software, die von der Open Source Miners United (OSMU)-Gemeinschaft entwickelt wurde und eine präzise Kontrolle über die Betriebsparameter des ASIC ermöglicht. Die Kommunikation zwischen dem Mikrocontroller und dem ASIC erfolgt über sorgfältig entwickelte serielle Kommunikationsleitungen, die als sichtbare Leiterbahnen direkt auf die Leiterplatte geätzt sind.


Die Rolle des Mikrocontrollers geht über die einfache Steuerung des ASIC hinaus: Er umfasst Funktionen zur Energieverwaltung, Temperaturüberwachung und Benutzerschnittstelle. Über den integrierten Bildschirm können die Benutzer wichtige Betriebsparameter wie Temperatur, Hash-Rate, IP-Adresse und andere relevante mining-Statistiken überwachen. Dieses Echtzeit-Feedback-System bietet wertvolle Einblicke in die Leistung des Geräts und hilft den Benutzern, ihren mining-Betrieb zu optimieren und gleichzeitig etwas über das zugrunde liegende Hardwareverhalten zu lernen.


### Energiemanagement und Sicherheitsaspekte


Die Bitaxe-Plattform arbeitet mit einer strikten 5-Volt-Spannungsanforderung, so dass die richtige Wahl der Stromversorgung für die Langlebigkeit und Sicherheit des Geräts entscheidend ist. Das Power-Management-System auf den Bitaxe-Platinen umfasst hochentwickelte Schaltungen, die die Spannungsversorgung des ASIC-Chips regeln und gleichzeitig den Stromverbrauch in verschiedenen Betriebsmodi überwachen. Dank dieser Stromverwaltungsfunktion kann das Gerät über einen Bereich interner Frequenzen und Spannungen hinweg effizient arbeiten und verbraucht je nach Konfiguration typischerweise zwischen 5 und 25 Watt.


Das Verständnis des Strombedarfs ist entscheidend, wenn man bedenkt, dass eine falsche Spannungsanwendung das Gerät dauerhaft beschädigen kann. Die Beziehung zwischen Frequenz, Spannung, Stromverbrauch und Hash-Rate demonstriert grundlegende Prinzipien des ASIC-Betriebs, die für alle mining-Hardware gelten. Die Benutzer können mit verschiedenen Leistungseinstellungen experimentieren, um die dem mining-Betrieb innewohnenden Effizienzkonflikte zu verstehen und praktische Erfahrungen mit Konzepten zu sammeln, die für mining-Implementierungen in größerem Maßstab gelten.


### Solo Mining Fokus und Netzwerkbeteiligung


Die Bitaxe-Plattform zielt speziell auf mining-Einzelanwendungen ab, bei denen einzelne Schürfer versuchen, Bitcoin-[Blöcke](https://planb.academy/resources/glossary/block) unabhängig voneinander zu lösen, anstatt sich an großen mining-Pools zu beteiligen. Obwohl die Hash-Rate von Bitaxe-Geräten eine erfolgreiche Blockentdeckung statistisch gesehen unwahrscheinlich macht, dient dieser Ansatz wichtigen pädagogischen und philosophischen Zwecken innerhalb der Bitcoin-Gemeinschaft. Solo mining mit Bitaxe-Geräten hilft den Nutzern, die grundlegende Mechanik des Bitcoin [proof-of-work](https://planb.academy/resources/glossary/proof-of-work)-Systems zu verstehen und trägt gleichzeitig zur Dezentralisierung des Netzwerks bei.


Die Betonung des Solo-mining spiegelt das Engagement der OSMU-Gemeinschaft wider, die individuelle Beteiligung am Sicherheitsmodell des Bitcoin zu fördern. Durch die Bereitstellung zugänglicher Hardware, die unabhängig betrieben werden kann, ermöglicht die Bitaxe-Plattform den Nutzern, ihre eigenen mining-Operationen durchzuführen, ohne auf die Pool-Infrastruktur angewiesen zu sein. Dieser Ansatz fördert ein tieferes Verständnis des [Konsensmechanismus](https://planb.academy/resources/glossary/consensus) von Bitcoin und unterstützt gleichzeitig den dezentralen Charakter des Netzwerks durch eine größere Vielfalt an Minern.


### Hardware-Entwicklung und Produktionsverbesserungen


Die Bitaxe-Plattform wird durch das Feedback der Community und die Optimierung der Produktion ständig weiterentwickelt, wobei neuere Versionen Verbesserungen enthalten, die die Herstellbarkeit und das Benutzererlebnis verbessern. Versions-Updates konzentrieren sich in der Regel eher auf die Produktionseffizienz als auf grundlegende Leistungsänderungen, um sicherzustellen, dass bestehende Nutzer nicht unter Veralterungsdruck geraten. Funktionen wie der Übergang von Micro-USB- zu USB-C-Anschlüssen und verbesserte Stromanschlusssysteme spiegeln die Aufmerksamkeit der Community für praktische Verbesserungen der Benutzerfreundlichkeit wider.


Dieser evolutionäre Ansatz verdeutlicht die Vorteile der Open-Source-Hardwareentwicklung, bei der der Input der Community zu schrittweisen Verbesserungen führt, die allen Nutzern zugute kommen. Die Philosophie "wenn es hascht, dann hascht es" unterstreicht den Fokus der Plattform auf Funktionalität statt ständiger Upgrades und ermutigt die NutzerInnen, ihre Geräte zu warten und zu betreiben, anstatt nach den neuesten Versionen zu streben. Dieser Ansatz unterstützt nachhaltige Hardware-Praktiken und erhält gleichzeitig den pädagogischen Wert von Bitaxe.


## Wo kann ich mehr erfahren?

<chapterId>706f2fff-fa1c-5d8e-b14c-ece6e42c016f</chapterId>

:::video id=90088397-3a16-485f-bbd2-89cdbb844e4a:::

Das Bitaxe-Projekt stellt eine umfassende Open-Source-mining-Initiative dar, die weit über ein einzelnes Gerät hinausgeht. Für jeden, der sich in diesem Ökosystem engagieren möchte, ist es wichtig zu wissen, wo man verlässliche Informationen, technische Ressourcen und die Unterstützung der Gemeinschaft findet. Dieses Kapitel bietet einen vollständigen Leitfaden zu den wesentlichen Plattformen und Ressourcen, die die Grundlage der Bitaxe- und Open Source Miners United (OSMU)-Community bilden.


### Bitaxe.org, der zentrale Knotenpunkt


Die Website Bitaxe.org dient als primärer Zugang zu allen projektbezogenen Informationen und Ressourcen. Diese zentrale Plattform dient als erste Anlaufstelle, wenn Sie etwas über Bitaxe-Geräte erfahren oder andere Projekte innerhalb der OSMU-Community erkunden möchten. Das Design der Website legt den Schwerpunkt auf Zugänglichkeit und Organisation und präsentiert Besuchern sorgfältig kuratierte Links, die zu verschiedenen spezialisierten Ressourcen innerhalb des Ökosystems führen.


Die Bedeutung dieser zentralen Drehscheibe kann gar nicht hoch genug eingeschätzt werden, da sie die Verwirrung beseitigt, die oft mit dezentralen Open-Source-Projekten einhergeht. Anstatt mehrere Plattformen zu durchsuchen oder sich auf potenziell veraltete Informationen aus inoffiziellen Quellen zu verlassen, können die Nutzer darauf vertrauen, dass Bitaxe.org aktuelle, verifizierte Links zu allen wichtigen Ressourcen bereitstellt. Dieser Ansatz stellt sicher, dass sowohl Neulinge als auch erfahrene Community-Mitglieder effizient die spezifischen Informationen finden können, die sie für ihre Projekte benötigen.


### Technische Ressourcen und Entwicklungsmaterialien


Das Hardware Design Files Repository auf GitHub ist eine der wertvollsten Ressourcen für jeden, der daran interessiert ist, Bitaxe Geräte zu verstehen oder zu bauen. Dieses öffentliche Repository enthält eine umfassende Dokumentation, die jeden Aspekt des Hardware-Designprozesses abdeckt, von den ersten Konzepten bis zu den endgültigen Fertigungsspezifikationen. Das Repository enthält detaillierte Bilder, Projektziele, Funktionsbeschreibungen und Erklärungen zu eingebauten Komponenten, die sowohl technische Tiefe als auch praktische Anleitung bieten.


Für diejenigen, die ihre eigenen Geräte herstellen möchten, enthält das Repository spezielle Dokumentationsdateien wie building.md, die Schritt-für-Schritt-Anweisungen für den gesamten Produktionsprozess enthalten. Diese Dokumentation umfasst die für das PCB-Design erforderlichen Softwaretools, die Verfahren zum Senden von Dateien an die Hersteller und die Schritte zum Erhalt und zur Validierung der hergestellten PCBs. Dieser Detaillierungsgrad stellt sicher, dass Einzelpersonen oder kleine Unternehmen den Herstellungsprozess auch ohne umfangreiche Vorkenntnisse in der Hardware-Produktion erfolgreich bewältigen können.


Das ESP-Miner Repository dient als zentraler Ort für alle Firmware-bezogenen Codes und Dokumentationen. Dieses GitHub-Repository enthält jede Codezeile, die für die Bitaxe-Firmware geschrieben wurde, zusammen mit einer umfassenden Dokumentation, die die Systemanforderungen, Hardwarespezifikationen und Konfigurationsoptionen erläutert. Die Repository-Struktur ist so konzipiert, dass sowohl Benutzer, die vorkompilierte Binärdateien bevorzugen, als auch Entwickler, die die Firmware aus dem Quellcode erstellen möchten, auf ihre Kosten kommen.


Die Dokumentation in diesem Repository enthält detaillierte Abschnitte zu den Hardwareanforderungen, Vorkonfigurationsoptionen und empfohlenen Werten für verschiedene Einstellungen. Diese Informationen sind von unschätzbarem Wert für Benutzer, die ihre Geräte anpassen oder bestimmte Probleme beheben möchten. Darüber hinaus enthält das Repository Informationen über neuere Entwicklungen, wie z. B. die Integration des Raspberry Pi, wodurch sichergestellt wird, dass die Dokumentation mit der laufenden Entwicklung des Projekts auf dem neuesten Stand bleibt.


### Tools zur Geräteverwaltung und -wartung


Der Bitaxe Web Flasher ist eine praktische Lösung für die Wartung und Aktualisierung von Geräten. Mit diesem webbasierten Tool können Benutzer Firmware auf ihre Geräte flashen, ohne spezielle Software oder komplexe Befehlszeilenverfahren zu benötigen. Der Flasher unterstützt mehrere Gerätevarianten, darunter den Bitaxe Ultra mit verschiedenen Port-Versionen und die älteren Bitaxe Max-Modelle. Die Benutzer können wählen, ob sie die vorhandene Firmware über die Webschnittstelle aktualisieren oder über USB-Verbindungen einen kompletten Werksreset durchführen wollen.


Dieses Tool befasst sich mit einer der häufigsten Herausforderungen, mit denen Hardware-Enthusiasten konfrontiert sind: der Wartung und Aktualisierung der Geräte-Firmware. Durch die Bereitstellung einer benutzerfreundlichen Weboberfläche beseitigt der Flasher viele der technischen Hürden, die Benutzer andernfalls davon abhalten könnten, ihre Geräte mit den neuesten Firmware-Versionen auf dem neuesten Stand zu halten. Das Design des Tools legt den Schwerpunkt auf Einfachheit und bietet gleichzeitig die nötige Flexibilität für unterschiedliche Gerätekonfigurationen und Aktualisierungsszenarien.


### Gemeinschaftsplattformen und Kommunikationskanäle


Der Discord-Server ist das Herzstück der Echtzeit-Community-Interaktion und des Supports innerhalb des Bitaxe-Ökosystems. Die Organisation des Servers spiegelt die unterschiedlichen Interessen und Bedürfnisse der Community-Mitglieder wider, mit sorgfältig strukturierten Channels, die gezielte Diskussionen zu bestimmten Themen ermöglichen. Neue Mitglieder durchlaufen einen Verifizierungsprozess, der das Lesen und Akzeptieren der Community-Regeln erfordert, um sicherzustellen, dass alle Teilnehmer die Erwartungen an eine respektvolle und produktive Interaktion verstehen.


Die Channel-Struktur des Servers umfasst allgemeine Diskussionsbereiche, die Themen wie die Integration von Solarenergie, mining-Pools und Bitcoin-bezogene Diskussionen abdecken. Speziellere Bereiche konzentrieren sich auf bestimmte Geräte, einschließlich spezieller Kanäle für die Bitaxe Ultra-, Hex- und Supra-Varianten. Der Firmware-Kanal bietet einen konzentrierten Raum für technische Diskussionen über Softwareentwicklung und Fehlerbehebung, während der Kanal für offizielle Veröffentlichungen sicherstellt, dass die Community-Mitglieder rechtzeitig über neue Entwicklungen informiert werden.


Außerdem gibt es einen Abonnentenbereich, der zusätzliche Vorteile für Gemeindemitglieder bietet, die sich für eine finanzielle Unterstützung des Projekts entscheiden. Dieser mehrstufige Ansatz ermöglicht es der Community, erweiterte Dienste anzubieten und gleichzeitig den Zugang zu wichtigen Informationen und Supportkanälen offen zu halten. Der Hilfe-Kanal dient als spezieller Bereich für die Fehlersuche und technische Unterstützung, damit die Nutzer bei Schwierigkeiten sofort Hilfe erhalten.



Das Open Source Miners United-Wiki (osmu.wiki) bietet eine umfassende Dokumentation, die die Echtzeit-Diskussionen auf Discord ergänzt. Im Gegensatz zu Chat-basierten Plattformen bietet das Wiki eine strukturierte, durchsuchbare Dokumentation, die alle Aspekte des Bitaxe-Projekts und verwandter Initiativen abdeckt. Die Art und Weise, wie es organisiert ist, spiegelt die Struktur des Projekts wider, mit speziellen Abschnitten für verschiedene Geräteserien und umfassenden Anleitungen zur Einrichtung.


Der Open-Source-Charakter des Wikis ermöglicht es den Mitgliedern der Community, direkt zur Dokumentation beizutragen. Benutzer können Seiten bearbeiten, Korrekturen einreichen und neue Informationen über die GitHub-Integration hinzufügen, um sicherzustellen, dass die Wissensdatenbank aktuell und transparent bleibt. Dieser kollaborative Ansatz nutzt das kollektive Fachwissen der Community und gewährleistet gleichzeitig eine Qualitätskontrolle durch ein Prüfverfahren für eingereichte Änderungen.


Das Wiki enthält praktische Ressourcen wie z. B. PDF-Einrichtungsleitfäden, die Schritt-für-Schritt-Anweisungen für die Gerätekonfiguration und -nutzung enthalten. Diese Leitfäden dienen als wertvolle Referenz für neue Benutzer und erfahrene Community-Mitglieder, die einen schnellen Zugriff auf bestimmte Verfahren oder Konfigurationsdetails benötigen.


### Informationen für Einkäufer und Lieferanten


Die Bitaxe-Legitimationsliste adressiert ein kritisches Bedürfnis innerhalb der Open-Source-Hardware-Community: vertrauenswürdige Anbieter zu identifizieren und betrügerische Verkäufer zu vermeiden. Diese kuratierte Liste enthält verifizierte Wiederverkäufer und Hersteller, die bestimmte Kriterien für Legitimität und Community-Unterstützung erfüllen. Jede Auflistung enthält direkte Links zu den Websites der Anbieter, regionale Informationen und Unternehmensbeschreibungen, die den Benutzern helfen, fundierte Kaufentscheidungen zu treffen.


Wichtig ist, dass aus der Liste hervorgeht, ob die einzelnen Anbieter der OSMU-Gemeinschaft entweder finanziell oder durch andere Formen der Unterstützung helfen. Diese Transparenz hilft den Mitgliedern der Gemeinschaft zu verstehen, welche Anbieter die Entwicklung und Nachhaltigkeit des Projekts aktiv unterstützen. Die Liste dient auch als Schutzmaßnahme gegen gängige Betrügereien, wie z. B. nicht autorisierte Vorbestellungen für unveröffentlichte Produkte, die in der Vergangenheit zu Problemen innerhalb der Gemeinschaft geführt haben.


Die Betonung von nicht-verbundenen Links zeigt das Engagement der Community, unvoreingenommene Anbieterempfehlungen zu geben. Die Nutzer können darauf vertrauen, dass die Empfehlungen auf der Legitimität des Anbieters und dem Beitrag der Gemeinschaft beruhen und nicht auf finanziellen Anreizen, so dass Kaufentscheidungen sowohl den individuellen Bedarf als auch die Nachhaltigkeit der Gemeinschaft unterstützen.



# Software und Betrieb

<partId>04b302a9-42ba-5ad4-834c-6979950c2948</partId>


## Was ist AxeOS?

<chapterId>a0cdf10d-e007-58e2-a17b-b588fd393b5e</chapterId>

:::video id=de7bcbf2-f9ac-4057-ad40-29dc223b4798:::

AxeOS ist eine Firmware- und Webschnittstelle für Bitaxe mining-Geräte, die dem Benutzer über ein intuitives, browserbasiertes Dashboard vollständige Steuerungs- und Überwachungsmöglichkeiten bietet. Dieses System verwandelt die komplexe Aufgabe der ASIC-Verwaltung in eine zugängliche Erfahrung, die es Bergleuten ermöglicht, die Leistung zu überwachen, Einstellungen anzupassen und mehrere Geräte über eine einzige Schnittstelle zu verwalten. Das Verständnis von AxeOS ist für die Maximierung des Potenzials Ihres Bitaxe-Geräts und die Aufrechterhaltung eines optimalen mining-Betriebs unerlässlich.


### Übersicht über das Dashboard und die wichtigsten Metriken


Das AxeOS-Dashboard dient als Ihr primäres Fenster zur Leistung Ihres Bitaxe-Geräts und stellt wichtige mining-Metriken in einem organisierten Echtzeitformat dar. Wenn Sie zur IP-Adresse Ihres Bitaxe-Geräts navigieren, werden Ihnen sofort vier wichtige Leistungsindikatoren angezeigt, die den aktuellen Zustand Ihres mining-Betriebs definieren. Die Anzeige der Hash-Rate zeigt die tatsächliche Rechengeschwindigkeit, die Ihr ASIC-Chip bei der Verarbeitung der aktuellen Blockvorlage erzeugt, und liefert so ein unmittelbares Feedback zur Kernfunktionalität Ihres Geräts.


Neben der Hash-Rate verfolgt der Anteilszähler jede gültige Lösung, die Ihr Bitaxe-Gerät an den mining-Pool sendet. Er erhöht sich mit jeder erfolgreichen Übertragung und dient als direktes Maß für den Beitrag Ihres Geräts zu den mining-Bemühungen des Pools. Die Effizienzmetrik bietet einen entscheidenden Einblick in die Energieleistung Ihres Geräts, indem sie das Verhältnis zwischen Hash-Rate und Stromverbrauch berechnet und Ihnen hilft, die Rentabilität Ihres Betriebs zu optimieren. Der Indikator für den besten Schwierigkeitsgrad speichert den höchsten Schwierigkeitsgrad, den Ihr Gerät jemals erreicht hat, und behält diesen Wert auch bei Neustarts und Updates bei, wobei er nur zurückgesetzt wird, wenn Sie einen kompletten Werksflash durchführen.


Das erweiterbare Menüsystem des Dashboards, das über einen Toggle-Button gesteuert wird, ermöglicht den Zugriff auf alle AxeOS-Funktionen und bietet gleichzeitig eine übersichtliche Benutzeroberfläche. Eine der wertvollsten Funktionen ist die Live-Hash-Rate-Grafik, die Leistungsdaten in Echtzeit anzeigt, die umso genauer und informativer werden, je länger Sie Ihre Sitzung aufrechterhalten. Die Bereiche Strom, Wärme und Leistung bieten eine umfassende Überwachung des Betriebsstatus Ihres Geräts, einschließlich Eingangsspannungswarnungen, die Sie auf potenzielle Probleme mit der Stromversorgung hinweisen und gleichzeitig einen kontinuierlichen Betrieb innerhalb sicherer Parameter gewährleisten.


### Erweiterte Überwachung und Systeminformationen


Die Überwachungsfunktionen von AxeOS gehen weit über die grundlegende Hash-Rate-Verfolgung hinaus und bieten detaillierte Einblicke in jeden Aspekt des Betriebs Ihres Bitaxe-Geräts. Der Stromversorgungsbereich zeigt den berechneten Stromverbrauch an, der von den integrierten Schaltkreisen, den Eingangsspannungsmessungen von Ihrem Stromversorgungsanschluss und den angeforderten ASIC-Spannungspegeln abgeleitet wird. Bei Spannungseinbrüchen zeigt AxeOS sofort Warnmeldungen an, die sich jedoch in der Regel nicht auf den mining-Betrieb auswirken und lediglich auf mögliche Optimierungsmöglichkeiten der Stromversorgung hinweisen.


Die Temperaturüberwachung konzentriert sich auf das Wärmemanagement des ASIC-Chips. Die Messwerte werden an strategischen Stellen des Geräts entnommen, um genaue Wärmedaten mit entsprechenden Offsets für die Genauigkeit auf Chipebene zu liefern. Die Frequenz- und Spannungsanzeigen bieten Echtzeit-Feedback zu Ihren ASIC-Abstimmungsparametern, wobei die gemessene Spannung den genauesten verfügbaren Messwert darstellt, der direkt an der ASIC-Chipstelle gemessen wird. Diese Präzision ermöglicht eine Feinabstimmung der Leistungsparameter unter Beibehaltung sicherer Betriebsbedingungen.


Der Abschnitt "Verbindungsstatus" bietet einen unmittelbaren Einblick in Ihre mining-Pool-Konfiguration und zeigt die aktuelle Stratum-URL, den Port und die Benutzerkennung an. Für Geräte, die mit öffentlichen Pools verbunden sind, generiert AxeOS praktische Quick Links, die Sie direkt zur Weboberfläche Ihres Pools führen, wo Sie auf detaillierte Statistiken, Gerätelisten und historische Leistungsdaten zugreifen können. Diese Integration rationalisiert den Überwachungsprozess durch die Verbindung von Informationen auf Geräte- und Poolebene in einem nahtlosen Arbeitsablauf.


### Schwarm-Management und Multi-Device-Steuerung


Die Swarm-Funktionalität stellt die Lösung von AxeOS für die Komplexität der Verwaltung mehrerer Bitaxe-Geräte in einem Netzwerk dar und beseitigt die Notwendigkeit, sich zahlreiche IP-Adressen zu merken und zu navigieren. Dieses zentralisierte Managementsystem ermöglicht es Ihnen, Geräte hinzuzufügen, indem Sie einfach ihre IP-Adressen eingeben, aktive Bitaxe-Miner automatisch erkennen und sie in ein einheitliches Kontroll-Dashboard einbinden. Einmal konfiguriert, bietet Swarm umfassende Kontrolle über Ihren gesamten mining-Betrieb von einer einzigen Schnittstelle aus.


Über die Swarm-Schnittstelle können Sie wichtige Verwaltungsaufgaben für mehrere Geräte gleichzeitig oder einzeln durchführen, einschließlich Änderungen der Poolkonfiguration, Neustarts von Geräten, Frequenzanpassungen und Leistungsüberwachung. Dieser zentralisierte Ansatz reduziert den administrativen Aufwand für die Verwaltung großer mining-Operationen erheblich und gewährleistet gleichzeitig eine einheitliche Konfiguration für alle Geräte. Das System behält die Identität der einzelnen Geräte bei und bietet gleichzeitig kollektive Verwaltungsfunktionen, wodurch ein optimales Gleichgewicht zwischen granularer Kontrolle und betrieblicher Effizienz erreicht wird.


Das Swarm-Dashboard zeigt für jedes verwaltete Gerät den aktuellen Status, Leistungsmetriken und Schnellzugriffskontrollen an und ermöglicht eine schnelle Reaktion auf Leistungsprobleme oder Konfigurationsänderungen. Diese Funktionalität erweist sich als besonders wertvoll für Miner, die mehrere Geräte an verschiedenen Standorten betreiben oder die mining-Parameter häufig an die Marktbedingungen oder die Poolleistung anpassen.


### Konfigurationsmanagement und Systemeinstellungen


Der Abschnitt Einstellungen von AxeOS bietet umfassende Kontrolle über jeden konfigurierbaren Aspekt Ihres Bitaxe-Geräts, von der Netzwerkkonnektivität bis hin zu mining-Parametern und Hardware-Optimierung. Die Netzwerkkonfiguration beginnt mit der Wi-Fi-Einrichtung, bei der Sie Ihren Netzwerknamen und Ihr Kennwort angeben, wobei AxeOS Netzwerknamen mit nur einem Wort ohne Leerzeichen empfiehlt, um eine zuverlässige Verbindung zu gewährleisten. Das System wickelt den gesamten drahtlosen Konfigurationsprozess ab und ermöglicht die Fernverwaltung und -überwachung.


Die Mining-Konfiguration konzentriert sich auf die Stratum-Einstellungen, bei denen Sie die URL des gewählten mining-Pools ohne Protokollpräfixe oder Portnummern angeben, die in separaten Feldern behandelt werden. Das Stratum-Benutzerfeld passt sich verschiedenen Pool-Anforderungen an und unterstützt sowohl Bitcoin-Adressen für Solo-mining als auch Benutzernamen-Systeme für Pool-mining, mit der Möglichkeit, Gerätekennungen für Multi-Geräte-Operationen anzuhängen. Die kürzlich hinzugefügte Stratum-Passwortfunktion unterstützt Pools, die eine Authentifizierung erfordern, obwohl die meisten öffentlichen Pools ohne diese Anforderung arbeiten.


Die Hardware-Optimierung durch Frequenz- und Kernspannungsanpassung ist die leistungsstärkste Tuning-Funktion von AxeOS. Je nach Geräteversion und Browser erscheinen diese Einstellungen als Dropdown-Menüs mit voreingestellten Konfigurationen oder als offene Felder, die benutzerdefinierte Werte ermöglichen. Die Standardeinstellungen von 485 MHz Frequenz und 1200 mV Kernspannung bieten einen stabilen Betrieb für erste Tests, während fortgeschrittene Benutzer diese Parameter für maximale Leistung oder Effizienz basierend auf ihren spezifischen Anforderungen und Betriebsbedingungen optimieren können.


### Systemwartung und erweiterte Funktionen


AxeOS enthält ausgefeilte Systemwartungsfunktionen, die dafür sorgen, dass Ihr Bitaxe-Gerät stets mit maximaler Leistung arbeitet und gleichzeitig Diagnoseinformationen für die Fehlersuche und Optimierung bereitstellt. Das Update-System rationalisiert die Firmware-Verwaltung, indem es die neueste verfügbare Version direkt in der Benutzeroberfläche anzeigt und direkte Download-Links zu offiziellen Firmware-Dateien bereitstellt. Diese Integration macht das manuelle Navigieren in GitHub-Repositories oder das Verwalten von Dateidownloads überflüssig und vereinfacht den Aktualisierungsprozess auf ein paar Klicks.


Die Update-Schnittstelle akzeptiert korrekt benannte Firmware-Dateien, insbesondere esp-miner.bin und www.bin, um Kompatibilität zu gewährleisten und Installationsfehler zu vermeiden. Für Benutzer, die Schwierigkeiten mit dem Standard-Update-Prozess haben, bietet AxeOS Verweise auf umfassende Factory-Flash-Verfahren, die die ursprüngliche Funktionalität der Geräte wiederherstellen können. Dieser duale Ansatz eignet sich sowohl für Routine-Updates als auch für Wiederherstellungsszenarien.


Das Protokollierungssystem bietet Echtzeiteinblicke in den Gerätebetrieb und zeigt detaillierte Informationen zu ASIC-Chipmodellen, Systembetriebszeit, Wi-Fi-Verbindungsstatus, verfügbarem Speicher, Firmware-Versionen und Board-Revisionen an. Diese Protokolle sind von unschätzbarem Wert für Entwickler und fortgeschrittene Benutzer, die das Geräteverhalten verstehen, Probleme diagnostizieren oder die Leistung optimieren möchten. Der Echtzeit-Protokoll-Viewer zeigt Live-Betriebsdaten, einschließlich [Nonce](https://planb.academy/resources/glossary/nonce)-Verarbeitung, Schwierigkeitsberechnungen und mining-Übermittlungsparameter, und bietet so einen beispiellosen Einblick in den mining-Prozess selbst.


Zu den weiteren Systemfunktionen gehören die Steuerung der Bildschirmausrichtung für Geräte in kundenspezifischen Gehäusen, die Umkehrung der Lüfterpolarität für spezielle Kühlkonfigurationen und die automatische Lüftersteuerung, die die Kühlung auf der Grundlage der ASIC-Temperatur anpasst. Die manuelle Steuerung der Lüftergeschwindigkeit ermöglicht ein präzises Kühlungsmanagement, wenn die automatischen Systeme bestimmte Anforderungen nicht erfüllen. Alle Konfigurationsänderungen müssen gespeichert und das Gerät neu gestartet werden, um wirksam zu werden. So wird ein stabiler Betrieb gewährleistet und verhindert, dass Teilkonfigurationen die Leistung des mining beeinträchtigen.



# Gemeinschaft und Zusammenarbeit

<partId>eed1ce48-6752-5744-91f7-91e4e20ff6b2</partId>


## Überblick über Open-Source-Beiträge

<chapterId>715d026e-cebc-536e-a34e-728f5653b999</chapterId>

:::video id=7298ba19-28d2-4a7c-ac0b-44ad0c4770cf:::

### GitHub und seine Rolle in der Softwareentwicklung


GitHub stellt einen grundlegenden Wandel in der Art und Weise dar, wie Softwareentwicklungsprojekte verwaltet und von der globalen Programmiergemeinschaft gemeinsam genutzt werden. Als Cloud-basierte Plattform, auf der Softwareentwicklungsprojekte mit Git, einem verteilten Versionskontrollsystem, gehostet werden, ermöglicht GitHub Entwicklern die nahtlose Zusammenarbeit an Projekten unabhängig von ihrem physischen Standort. Die Plattform dient sowohl als technisches Werkzeug als auch als soziales Netzwerk für Programmierer, das es ihnen ermöglicht, Änderungen zu verfolgen, Updates zusammenzuführen, verschiedene Versionen ihres Codes zu pflegen und zu Open-Source-Initiativen wie dem BitX-Projekt von Open Source Miners United beizutragen.


Die Stärke von GitHub liegt in seiner Fähigkeit, den komplexen Prozess der gemeinschaftlichen Entwicklung zu vereinfachen. Wenn mehrere Entwickler an einem Projekt arbeiten, bietet GitHub die Infrastruktur, um Beiträge zu verwalten, Änderungen zu überprüfen, Projektprobleme zu bearbeiten und eine umfassende Dokumentation zu führen. Dieser kollaborative Ansatz hat GitHub zu einem unverzichtbaren Bestandteil moderner Softwareentwicklungs-Workflows gemacht und verändert die Art und Weise, wie sowohl einzelne Entwickler als auch große Unternehmen an Projektmanagement und Code-Sharing herangehen.


### Navigieren in der GitHub Interface und Repository-Struktur


Um die GitHub-Benutzeroberfläche zu verstehen, müssen Sie zunächst die Schlüsselelemente erkennen, aus denen eine Repository-Seite besteht. Die obere Navigationsleiste enthält mehrere wichtige Abschnitte, darunter Code, Issues, Pull Requests, Discussions, Actions, Projects, Security und Insights. Jeder Bereich dient einem bestimmten Zweck im Projektmanagement-Ökosystem, wobei der Code-Bereich die eigentlichen Dateien und Ordner anzeigt, aus denen das Projekt besteht.


Die Struktur des Repositorys selbst spiegelt den organisatorischen Ansatz der Projektbetreuer wider. Einige Repositories enthalten nur eine einzige Datei, vielleicht ein einfaches Shell-Skript, während andere wie das BitX-Hardware-Projekt zahlreiche Dateien enthalten, die in Verzeichnissen und Unterverzeichnissen organisiert sind. Der Name des Repositorys erscheint an prominenter Stelle und dient sowohl als Identifikator als auch als kurze Beschreibung des Projektzwecks. Zu den wesentlichen interaktiven Elementen gehören die Schaltfläche "Beobachten", um Benachrichtigungen über Aktualisierungen des Projektarchivs zu erhalten, die Schaltfläche "Fork", um persönliche Kopien des Projektarchivs zu erstellen, und die Schaltfläche "Stern", die ähnlich wie ein "Daumen hoch"-Feature als gemeinschaftliches Befürwortungssystem funktioniert.


Der Abschnitt "Über" enthält wichtige Projektinformationen in einem komprimierten Format, einschließlich einer einzeiligen Beschreibung, Lizenzinformationen und wichtige Projektdetails. Für das BitX-Projekt wird es in diesem Abschnitt als "Open Source ASIC Bitcoin Miner-Hardware" identifiziert und die GPL 3.0 Lizenz angegeben. Das Verständnis der Lizenzierung ist besonders wichtig, da GitHub als Open-Source-Plattform fungiert, auf der öffentliche Repositories für die gesamte Community zugänglich sind, die Inhalte aber nur gemäß den Regeln der jeweiligen Lizenz verwendet und verbreitet werden dürfen.


### Arbeiten mit Verzweigungen und Projektversionen


Das Konzept der Verzweigungen ist eine der leistungsstärksten Funktionen von GitHub für die Verwaltung verschiedener Versionen und Entwicklungsspuren innerhalb eines einzelnen Projekts. Eine Verzweigung erstellt im Wesentlichen eine Kopie oder eine geänderte Version der Hauptcodebasis und ermöglicht es den Entwicklern, an bestimmten Funktionen, Fehlerbehebungen oder experimentellen Änderungen zu arbeiten, ohne die primäre Entwicklungslinie zu beeinträchtigen. Der Master-Zweig dient in der Regel als Standard und stabilste Version des Projekts, während zusätzliche Zweige verschiedene Iterationen, Testphasen oder völlig unterschiedliche Produktvarianten aufnehmen.


Im BitX-Hardwareprojekt gibt es mehrere Zweige, um verschiedene Hardwareversionen und -konfigurationen zu verwalten. Zum Beispiel enthält der Ultra v2-Zweig Dateien, die speziell für diese Hardware-Iteration bestimmt sind, während der Super 401-Zweig sich auf Implementierungen konzentriert, die den S21 ASIC-Chip für eine verbesserte Effizienz verwenden. Jeder Zweig kann mehrere Commits vor oder hinter dem Master-Zweig liegen, was den Umfang der Änderungen und der Entwicklungsaktivitäten anzeigt. Bei der Untersuchung der verschiedenen Zweige werden die Benutzer völlig unterschiedliche Dateistrukturen, Dokumentationen und sogar visuelle Darstellungen feststellen, die die einzigartigen Anforderungen und Spezifikationen der einzelnen Hardwarevarianten widerspiegeln.


Das Zweigsystem verhindert Verwirrung unter den Mitwirkenden und Benutzern, indem es die verschiedenen Entwicklungsspuren klar voneinander trennt. Anstatt experimentelle Funktionen mit stabilen Versionen zu vermischen oder verschiedene Hardwareversionen an einem Ort zu kombinieren, sorgen Zweige für eine saubere Trennung, wobei die Möglichkeit erhalten bleibt, erfolgreiche Änderungen bei Bedarf wieder in die Hauptentwicklungslinie einzubringen. Dieser organisatorische Ansatz stellt sicher, dass die Benutzer leicht die spezifische Version finden können, die sie benötigen, während die Entwickler an Verbesserungen arbeiten können, ohne das Hauptprojekt zu unterbrechen.


### Beitrag durch Probleme


Der Bereich "Probleme" dient als primärer Kommunikationskanal zwischen Benutzern und Projektbetreuern, um Probleme zu melden, Verbesserungen vorzuschlagen und Fehler zu dokumentieren. Es ist jedoch wichtig zu verstehen, dass der Bereich Probleme speziell für legitime technische Probleme und nicht für allgemeine Fragen oder Supportanfragen gedacht ist. Wenn Benutzer auf tatsächliche Fehlfunktionen oder unerwartetes Verhalten stoßen oder Verbesserungsmöglichkeiten aufzeigen, hilft das Erstellen eines gut dokumentierten Problems der gesamten Gemeinschaft, indem es die Aufmerksamkeit auf Probleme lenkt, die möglicherweise mehrere Benutzer betreffen.


Eine effektive Meldung von Problemen erfordert eine detaillierte Dokumentation des Problems, einschließlich der Umstände, die zu dem Problem geführt haben, der Schritte zur Reproduktion des Problems und aller relevanten technischen Details. Das BitX-Projekt demonstriert dieses Prinzip anhand verschiedener abgeschlossener Probleme, die den Lösungsprozess von der anfänglichen Problemerkennung über die Diskussion in der Community bis hin zur endgültigen Lösung aufzeigen. Einige Probleme führen zu Hardware-Verbesserungen, wie z.B. das Hinzufügen von Montagelöchern zur Verbesserung der Kühlung, während andere durch Benutzerschulung oder Software-Updates gelöst werden können.


Die Unterscheidung zwischen Themen und Diskussionen ist wichtig für die Aufrechterhaltung einer organisierten Community-Interaktion. Während sich Issues auf spezifische technische Probleme konzentrieren, bietet der Discussions-Bereich eine forumähnliche Umgebung für Fragen, Ideen und allgemeines Engagement der Community. Obwohl der Discord-Server zum primären Kommunikationskanal für die BitX-Community geworden ist, bleibt der GitHub-Diskussionsbereich für formellere oder durchsuchbare Unterhaltungen verfügbar, die von einer permanenten Dokumentation und einfachen Referenz profitieren.


### Verstehen von Pull Requests


Pull-Requests sind der Mechanismus, mit dem externe Mitwirkende Änderungen an einem Projekt-Repository vorschlagen. Wenn jemand eine Verbesserung, Fehlerbehebung oder neue Funktion findet, die dem Projekt zugute kommen würde, kann er eine Pull-Anfrage erstellen, um seine Änderungen zur Überprüfung und möglichen Integration in die Haupt-Codebasis einzureichen. Dieser Prozess stellt sicher, dass alle Änderungen geprüft werden, bevor sie Teil des offiziellen Projekts werden, wodurch die Qualität des Codes und die Kohärenz des Projekts erhalten bleiben und gleichzeitig Beiträge der Gemeinschaft ermöglicht werden.


Der Arbeitsablauf einer Pull-Anfrage beginnt in der Regel damit, dass ein Mitwirkender das Repository forkt, seine eigene Kopie erstellt, in der er Änderungen vornehmen kann, und diese Änderungen dann per Pull-Anfrage an das ursprüngliche Projekt zurückschickt. Die Projektbetreuer können dann die vorgeschlagenen Änderungen überprüfen, die Modifikationen mit dem Mitwirkenden besprechen und schließlich entscheiden, ob die Änderungen in das Hauptprojekt übernommen werden sollen. Dieser kollaborative Überprüfungsprozess hilft dabei, die Projektstandards aufrechtzuerhalten und gleichzeitig die Beteiligung der Gemeinschaft und Verbesserungen zu fördern.


Das Verständnis von Tags und Versionen ist eine weitere Ebene des Projektmanagements und der Versionskontrolle. Tags dienen als Markierungen in der Entwicklungszeitachse, die bestimmte Punkte kennzeichnen, die für bestimmte Versionen oder Meilensteine stehen. In Hardware-Projekten wie BitX entsprechen Tags oft bestimmten Modellnummern oder Hardware-Revisionen und bieten klare Bezugspunkte für Benutzer, die nach bestimmten Versionen suchen. Releases, die häufiger in Software-Projekten verwendet werden, stellen formale Verteilungen von fertigen Funktionen und Fehlerbehebungen dar, oft begleitet von detaillierten Release Notes und herunterladbaren Paketen.


Das GitHub-Ökosystem schafft eine umfassende Umgebung für die Open-Source-Zusammenarbeit, die weit über den einfachen Austausch von Dateien hinausgeht. Wenn Sie diese verschiedenen Komponenten und ihre richtige Verwendung verstehen, können Sie sich effektiv an Projekten beteiligen, zur Verbesserung von Software- und Hardware-Designs beitragen und von dem kollektiven Wissen und den Bemühungen der globalen Entwicklergemeinschaft profitieren. Ob Sie nun Probleme melden, Verbesserungen vorschlagen oder Code beisteuern, GitHub bietet die Werkzeuge und die Struktur, die für eine sinnvolle Zusammenarbeit in der Open-Source-Welt erforderlich sind.


## Open-Source-Beitrag in der Praxis

<chapterId>84d033f5-7182-584f-b1a5-697172bc7a1c</chapterId>

:::video id=7d318fd0-6f0b-422a-9f30-2c470b56951d:::

Aufbauend auf der Grundlage des Erstellens von Issues und der Erkundung von Open-Source-Projekten, konzentriert sich dieses Kapitel auf die praktischen Aspekte der direkten Beiträge durch Pull-Requests und die Verwaltung von Repositories. Zu verstehen, wie man fork Repositories verwaltet, Änderungen vornimmt und Pull-Requests einreicht, ist eine wichtige Fähigkeit für jeden Entwickler, der einen sinnvollen Beitrag zu Open-Source-Projekten leisten möchte, egal ob es sich um Softwareentwicklung oder Hardwaredesign handelt.


Der Prozess des Einbringens von Codeänderungen folgt einem standardisierten Arbeitsablauf, der die Projektintegrität gewährleistet und gleichzeitig eine gemeinschaftliche Entwicklung ermöglicht. Dieser Arbeitsablauf umfasst das Erstellen einer eigenen Kopie eines Projekt-Repositorys, das Vornehmen von Änderungen in einer kontrollierten Umgebung und das anschließende Einbringen dieser Änderungen in das ursprüngliche Projekt im Rahmen eines formalen Überprüfungsprozesses. Die Beispiele in diesem Kapitel beziehen sich zwar in erster Linie auf Software-Beiträge, aber dieselben Prinzipien und Verfahren gelten auch für Hardware-Projekte, die PCB-Entwürfe, Schaltpläne und andere technische Dokumentationen umfassen.


### Verstehen von Gabeln und Repository-Struktur


Die Grundlage für die Mitwirkung an einem Open-Source-Projekt beginnt mit der Erstellung eines fork, der als Ihre persönliche Kopie des ursprünglichen Repositorys dient. Wenn Sie zu einem GitHub-Repository navigieren und auf die Schaltfläche "fork" klicken, erstellen Sie eine unabhängige Kopie unter Ihrem eigenen GitHub-Konto, die eine klare Verbindung zum ursprünglichen Quellcode aufrechterhält. Dieses "forked" Repository erscheint in Ihrem Konto mit einem klaren Hinweis auf seine Herkunft, indem unter dem Repository-Titel ein Text wie "forked from [original-owner]/[repository-name]" angezeigt wird.


Ihr geforktes Repository arbeitet unabhängig vom Original und ermöglicht es Ihnen, Änderungen vorzunehmen, ohne das Hauptprojekt zu beeinflussen. Durch die Synchronisierungsfunktionen von GitHub bleibt es jedoch über Aktualisierungen des ursprünglichen Repositorys informiert. Wenn das ursprüngliche Repository Aktualisierungen erhält, die Ihrem fork fehlen, zeigt GitHub Statusinformationen wie "Dieser Zweig liegt X Commits zurück" oder "X Commits voraus" an, wodurch die Beziehung zwischen Ihrem fork und dem Upstream-Repository klar ersichtlich wird. Sie können Ihr fork jederzeit mit dem ursprünglichen Repository synchronisieren, indem Sie auf die Schaltfläche "fork synchronisieren" klicken, wodurch die neuesten Änderungen aus der Upstream-Quelle übernommen werden.


Die Beziehung zwischen Ihrem fork und dem ursprünglichen Repository wird besonders wichtig, wenn Sie beginnen, Änderungen vorzunehmen. Wenn Sie Änderungen vornehmen und diese an Ihr fork übertragen, verfolgt GitHub diese Unterschiede und zeigt sie als Commits vor dem ursprünglichen Repository an. Dieses Nachverfolgungssystem ermöglicht den Pull-Request-Prozess, bei dem Sie Ihre Änderungen zur Aufnahme in das Hauptprojekt vorschlagen können, während Sie gleichzeitig einen klaren Überblick über die vorgenommenen Änderungen erhalten.


### Einrichten Ihrer Entwicklungsumgebung


Die Schaffung einer effektiven Entwicklungsumgebung erfordert ein sorgfältiges Augenmerk sowohl auf allgemeine Entwicklungswerkzeuge als auch auf projektspezifische Anforderungen. Visual Studio Code dient als hervorragende integrierte Entwicklungsumgebung (IDE) für die meisten Open-Source-Beiträge und bietet wesentliche Funktionen für die Codebearbeitung, die Integration der Versionskontrolle und die Projektverwaltung. Die erste wichtige Komponente ist die Installation und Konfiguration der Git-Erweiterung, die eine nahtlose Integration mit GitHub-Repositories direkt aus der Entwicklungsumgebung ermöglicht.


Moderne Versionen von Visual Studio Code enthalten in der Regel standardmäßig Git-Unterstützung, aber Sie müssen sich mit Ihrem GitHub-Konto authentifizieren, um die volle Funktionalität zu aktivieren. Dieser Authentifizierungsprozess beinhaltet die Anmeldung bei GitHub über die IDE, die es Ihnen dann ermöglicht, Repositories zu klonen, Änderungen zu übertragen und Updates direkt von Ihrer Entwicklungsumgebung aus zu pushen. Die GitHub-Integration wird als Symbol in der linken Seitenleiste angezeigt und ermöglicht den Zugriff auf das Klonen von Repositories, die Zweigverwaltung und die Synchronisierungsfunktionen, ohne dass Befehlszeilenoperationen erforderlich sind.


Für Projekte, die eingebettete Systeme oder spezielle Hardware-Plattformen beinhalten, werden zusätzliche Tools benötigt. Die ESP-IDF-Erweiterung ist eine wichtige Komponente für Projekte, die auf ESP32-Mikrocontroller abzielen, und erfordert eine spezielle Versionskompatibilität, um eine ordnungsgemäße Funktionalität zu gewährleisten. Der Installationsprozess umfasst die Auswahl der geeigneten ESP-IDF-Version, die Konfiguration der Werkzeugpfade und die Einrichtung der Entwicklungscontainerumgebung. Version 5.1.3 stellt derzeit die empfohlene Konfiguration für viele ESP32-basierte Projekte dar, obwohl sich diese Anforderungen ändern können, wenn Projekte ihre Abhängigkeiten und Toolchains aktualisieren.


### Änderungen vornehmen und Commits verwalten


Sobald Ihre Entwicklungsumgebung ordnungsgemäß konfiguriert ist, beginnt der Prozess, sinnvolle Beiträge zu leisten, mit dem Herunterladen oder Klonen Ihres Forked Repository auf Ihren lokalen Rechner. Dazu können Sie entweder eine ZIP-Datei mit dem Inhalt des Repositorys herunterladen oder die integrierte Klonfunktion von Visual Studio Code verwenden, die einen optimierten Workflow für die laufende Entwicklung bietet. Beim Klonen wird eine lokale Kopie Ihres Repositorys erstellt, die mit Ihrem GitHub fork synchronisiert bleibt, so dass Sie offline arbeiten und gleichzeitig die Versionskontrolle beibehalten können.


Wenn Sie mit dem lokalen Repository arbeiten, haben Sie Zugriff auf die gesamte Projektstruktur, einschließlich der Quellcodedateien, Konfigurationsdateien, Dokumentation und aller Hardware-Designdateien. Die meisten Firmware-Projekte verwenden Programmiersprachen wie C für die Kernfunktionalität, mit zusätzlichen Komponenten, die in TypeScript für Benutzeroberflächen oder Java für spezielle Dienstprogramme geschrieben sind. Die Kenntnis der Projektstruktur hilft Ihnen, die entsprechenden Dateien zu identifizieren, die Sie ändern müssen, und stellt sicher, dass Ihre Änderungen mit den Architekturmustern und Codierungsstandards des Projekts übereinstimmen.


Der Commit-Prozess ist ein grundlegender Aspekt der Versionskontrolle, bei dem sowohl auf technische Genauigkeit als auch auf eine klare Kommunikation geachtet werden muss. Bevor Sie Änderungen vornehmen, sollten Sie den bestehenden Code gründlich verstehen und alle Änderungen in Ihrer lokalen Umgebung testen. Die Kardinalregel für Open-Source-Beiträge besagt, dass Sie niemals ungetesteten Code veröffentlichen sollten, da dies zu Fehlern oder Sicherheitslücken führen kann, die die gesamte Projektgemeinschaft betreffen. Außerdem dürfen Sie niemals vertrauliche Informationen wie Passwörter, API-Tokens oder persönliche Anmeldedaten an öffentliche Repositories weitergeben, da diese Informationen für jeden, der Zugriff auf das Repository hat, dauerhaft zugänglich sind.


### Erstellen und Verwalten von Pull Requests


Die Krönung Ihres Beitrags ist die Erstellung einer Pull-Anfrage, die als formeller Vorschlag für die Zusammenführung Ihrer Änderungen mit dem ursprünglichen Projekt-Repository dient. Dieser Prozess beginnt in Ihrem GitHub fork, wo Sie die Unterschiede zwischen Ihrem Repository und dem Upstream-Quellcode überprüfen können. Die Oberfläche von GitHub zeigt deutlich die Anzahl der Commits an, die vor oder hinter Ihnen liegen, so dass Sie den Umfang der von Ihnen vorgeschlagenen Änderungen sofort erkennen können. Bevor Sie eine Pull-Anfrage erstellen, sollten Sie sicherstellen, dass Ihr fork mit den neuesten Upstream-Änderungen synchronisiert ist, um mögliche Konflikte zu minimieren.


Die Erstellung eines effektiven Pull-Requests erfordert mehr als nur das Einreichen Ihrer Codeänderungen. Die Beschreibung der Pull-Anfrage dient dazu, den Zweck, den Umfang und die Auswirkungen Ihrer Änderungen den Projektbetreuern und der Gemeinschaft mitzuteilen. Eine gut geschriebene Beschreibung erklärt, welche Probleme Ihre Änderungen angehen, wie Sie die Lösung implementiert haben, und welche Auswirkungen es auf andere Teile des Projekts haben könnte. Diese Dokumentation ist besonders wichtig, wenn es sich um komplexe Änderungen handelt, die nicht sofort ersichtlich sind, wenn man sich nur die Unterschiede im Code ansieht.


Der Überprüfungsprozess stellt einen gemeinschaftlichen Aspekt der Open-Source-Entwicklung dar, bei dem Projektbetreuer und erfahrene Mitwirkende Ihre vorgeschlagenen Änderungen bewerten. Sie können bestimmte Prüfer anfordern, die über Fachwissen in den Bereichen verfügen, die Ihre Änderungen betreffen, um sicherzustellen, dass sachkundige Mitglieder der Gemeinschaft Ihre Arbeit prüfen. Der Überprüfungsprozess kann mehrere Iterationen umfassen, wobei die Prüfer Rückmeldungen geben, Änderungen verlangen oder um zusätzliche Tests bitten. Dieser kollaborative Verfeinerungsprozess trägt dazu bei, die Qualität des Codes aufrechtzuerhalten und bietet gleichzeitig wertvolle Lernmöglichkeiten für Mitwirkende auf allen Erfahrungsebenen.


Zu verstehen, dass nicht alle Pull Requests angenommen werden, hilft dabei, angemessene Erwartungen für den Beitragsprozess zu setzen. Projektbetreuer können Pull-Requests aus verschiedenen Gründen ablehnen, unter anderem weil sie nicht mit den Projektzielen übereinstimmen, unzureichend getestet wurden oder weil es bereits alternative Lösungen in der Entwicklung gibt. Anstatt die Ablehnung als Scheitern zu betrachten, sollte sie als eine Gelegenheit betrachtet werden, aus dem Feedback zu lernen, den Ansatz zu verfeinern und möglicherweise alternative Lösungen beizusteuern, die den Bedürfnissen des Projekts besser entsprechen. Die Open-Source-Gemeinschaft lebt von diesem iterativen Prozess des Vorschlags, der Überprüfung und der Verfeinerung, der letztendlich Projekte durch kollektive Anstrengungen und gemeinsames Fachwissen vorantreibt.



## Was ist Public-Pool?

<chapterId>b461bf94-4a90-5bb8-ba3f-976d5d57be0d</chapterId>


:::video id=d4652496-1ed4-4415-8048-0b6871b9ed51:::

Public Pool stellt einen revolutionären Ansatz für Bitcoin mining dar, der viele der Bedenken, die Miner mit traditionellen mining-Pools haben, ausräumt. Als vollständig quelloffener Solo-Bitcoin-mining-Pool ändert Public Pool das Modell der Belohnungsverteilung, an das sich Miner gewöhnt haben, grundlegend. Im Gegensatz zu herkömmlichen mining-Pools, bei denen die Teilnehmer die Belohnungen teilen, wenn ein Schürfer im Pool einen Block findet, arbeitet Public Pool nach dem Solo-mining-Prinzip, bei dem die einzelnen Schürfer 100 % ihrer Blockbelohnungen behalten, wenn sie erfolgreich einen Block schürfen.


Das überzeugendste Merkmal von Public Pool ist seine gebührenfreie Struktur. Wenn Miner mit Hilfe von Public Pool erfolgreich einen Block finden, erhalten sie die komplette Blockbelohnung zusammen mit allen damit verbundenen [Transaktionsgebühren](https://planb.academy/resources/glossary/transaction-fees), ohne jegliche Abzüge für die Betriebskosten des Pools. Dies steht in krassem Gegensatz zu traditionellen mining-Pools, die in der Regel Gebühren in Höhe von 1-3% der mining-Rewards verlangen. Das Null-Gebühren-Modell macht Public Pool besonders attraktiv für Miner, die ihre potenziellen Erträge maximieren und gleichzeitig die volle Kontrolle über ihre mining-Operationen behalten wollen.


Um die einzigartige Position von Public Pool zu verstehen, ist es wichtig, den grundlegenden Unterschied zwischen Solo-mining und gepooltem mining zu begreifen. Echtes Solo-mining bedeutet, dass Sie unabhängig schürfen und die volle Blockbelohnung (derzeit 3,125 BTC + Gebühren) erhalten, wenn Sie einen Block finden, aber die Wahrscheinlichkeit ist proportional zu Ihrer Hash-Rate im Vergleich zum gesamten Netzwerk - was zu extremen Schwankungen führt, die Monate oder Jahre zwischen den Belohnungen liegen können. Traditionelle Pools kombinieren die Hash-Power, um häufiger Blöcke zu finden, verteilen die Belohnungen proportional und sorgen für ein stetiges, vorhersehbares Einkommen. Für Schürfer mit erheblichen Investitionen in Hardware und Betriebskosten ist ein reiner Solo-mining ungeachtet seiner philosophischen Vorteile in der Regel nicht praktikabel - die Varianz macht es fast unmöglich, die Stromkosten zu decken und die Investitionen zurückzugewinnen. Diese wirtschaftliche Realität bedeutet, dass sich die meisten Miner aus praktischen finanziellen Gründen für einen gepoolten mining entscheiden werden. Public Pool arbeitet als Solo-mining-Pool, was bedeutet, dass Sie immer noch mit der Varianz von Solo-mining konfrontiert sind (Sie werden nur belohnt, wenn Sie persönlich einen Block finden), aber Sie profitieren von der Infrastruktur des Pools und dem transparenten, gebührenfreien Betrieb.


### Der Vorteil von Open Source und die technische Umsetzung


Das Engagement von Public Pool für Open-Source-Entwicklung bietet Bergleuten eine beispiellose Transparenz und Kontrolle über ihre mining-Operationen. Die gesamte Codebasis ist auf GitHub verfügbar, so dass Bergleute genau untersuchen können, wie die Software funktioniert, sie nach ihren Bedürfnissen verändern und sogar zu ihrer Entwicklung beitragen können. Mit dieser Transparenz wird ein wichtiges Anliegen der mining-Gemeinschaft hinsichtlich der unbekannten Konfigurationen und Praktiken traditioneller mining-Pools erfüllt.


Die Software-Architektur umfasst sowohl die Kernfunktionalität von mining Pool als auch ein separates Repository für die Benutzeroberfläche, die beide frei zum Download und zur Modifikation verfügbar sind. Miner können Public Pool in verschiedenen Konfigurationen, einschließlich Docker-Containern, betreiben, wodurch er an unterschiedliche Hardware-Konfigurationen und technische Präferenzen angepasst werden kann. Die umfassende Dokumentation in den GitHub-Repositories bietet detaillierte Installationsanleitungen, Konfigurationsoptionen und Modifizierungsanweisungen, so dass sie für Miner mit unterschiedlichen technischen Kenntnissen zugänglich ist.


Die Verbindung zum Public Pool erfordert im Vergleich zu herkömmlichen mining-Einrichtungen nur eine minimale Konfiguration. Miner müssen lediglich ihre mining-Geräte mit den [Stratum](https://planb.academy/resources/glossary/stratum)-Verbindungsdetails konfigurieren und ihre Bitcoin-Adresse als Benutzernamen angeben. Zu organisatorischen Zwecken kann ein optionaler Arbeitername nach einem Punkttrennzeichen hinzugefügt werden.


### Gemeinschaftsmerkmale und Nachhaltigkeitsmodell


Public Pool enthält mehrere innovative Funktionen, die die Bitcoin mining-Community stärken und gleichzeitig den gebührenfreien Betrieb aufrechterhalten. Die Plattform zeigt umfassende Statistiken an, darunter die gesamte Hash-Rate der angeschlossenen Miner, die im Jahr 2024 typischerweise zwischen 1 und 2 PetaHash pro Sekunde und im November 2025 bei etwa 40 PH/s lag, und liefert detaillierte Informationen über angeschlossene mining-Geräte. Besonders erwähnenswert ist die Betonung der Plattform auf Open-Source-mining-Hardware, wobei die mit Sternen gekennzeichneten Geräte vollständig quelloffene Designs mit Links zu ihren jeweiligen GitHub-Repositories darstellen.


Die Nachhaltigkeit des gebührenfreien Betriebs von Public Pool beruht auf einer kreativen Partnerschaftsprogramm-Partnerschaft mit mining-Hardwareanbietern. Wenn Schürfer mit dem Rabattcode "SOLO" Ausrüstung von Partnerunternehmen kaufen, unterstützen fünfzig Prozent der Affiliate-Einnahmen die Betriebskosten von Public Pool, während die restlichen fünfzig Prozent als Belohnungen an Schürfer verteilt werden, die jeden Monat die höchsten Schwierigkeitsanteile erzielen. Dieses Modell schafft eine symbiotische Beziehung, bei der Miner Rabatte auf den Kauf von Ausrüstung erhalten, Anbieter Kunden gewinnen und Public Pool seinen Betrieb aufrechterhält, ohne direkte Gebühren zu verlangen.


### Philosophie und bewährte Praktiken der Dezentralisierung


Während Public Pool eine ausgezeichnete Alternative zu den traditionellen mining-Pools bietet, ist es wichtig, seine Rolle im breiteren Kontext der Bitcoin-Dezentralisierung zu verstehen. Die Plattform dient als Sprungbrett in Richtung des ultimativen Ziels, dass einzelne Miner ihre eigenen mining-Pools betreiben. Der Betrieb eines eigenen mining-Pools stellt die höchste Stufe der Dezentralisierung dar, da er die Abhängigkeit von der Infrastruktur oder Software Dritter beseitigt, unabhängig davon, wie transparent oder wohlmeinend diese Dritten sein mögen.


Der Open-Source-Charakter von Public Pool macht ihn zu einer idealen Lernplattform für Miner, die den Poolbetrieb verstehen wollen, bevor sie ihre eigenen Lösungen implementieren. Die Verfügbarkeit von Installationsanleitungen für mehrere Betriebssysteme und die umfassende Dokumentation vermitteln Bergleuten das Wissen, das sie für den Übergang von der Nutzung von Public Pool zum Betrieb ihrer eigenen mining-Infrastruktur benötigen. Dieser Bildungsaspekt steht im Einklang mit den Grundprinzipien von Bitcoin, nämlich Selbstbestimmung und Dezentralisierung, und befähigt die einzelnen Miner, die vollständige Kontrolle über ihren mining-Betrieb zu übernehmen und gleichzeitig zur allgemeinen Sicherheit und Dezentralisierung des Bitcoin-Netzwerks beizutragen.


Die Benutzeroberfläche der Plattform bietet Bergleuten detaillierte Überwachungsfunktionen, einschließlich des Status der Arbeiter, Hash-Raten-Statistiken und Leistungsmetriken. Diese Funktionen helfen den Schürfern, ihren Betrieb zu optimieren und gleichzeitig etwas über die Grundsätze der Poolverwaltung zu lernen, die sie später auf ihre eigenen mining-Pool-Implementierungen anwenden können.


## Wie installiert man Public-Pool auf Umbrel

<chapterId>7f6d0307-7715-5581-89ea-f13cf8754f9a</chapterId>


:::video id=3a4fe0a9-bbf5-458a-8ec1-52c3b83afd87:::

Das Betreiben eines eigenen Bitcoin mining-Pools zu Hause ist mit moderner Hardware und vereinfachten Softwarelösungen immer einfacher geworden. Dieses Kapitel befasst sich mit der praktischen Umsetzung eines öffentlichen Pools zu Hause mit erschwinglicher Mini-PC-Hardware und optimierter [Knotenverwaltungssoftware](https://planb.academy/resources/glossary/node). Am Ende dieses Leitfadens werden Sie die Hardwareanforderungen, den Softwareeinrichtungsprozess und die Grundkonfiguration verstehen, die für die Einrichtung Ihrer eigenen mining-Pool-Infrastruktur erforderlich sind.


### Hardware-Anforderungen und Einrichtung


Die Grundlage jeder mining-Pool-Einrichtung zu Hause beginnt mit der Auswahl geeigneter Hardware, die ein ausgewogenes Verhältnis zwischen Leistung, Kosten und Energieeffizienz bietet. Ein Mini-PC stellt eine ideale Lösung für diese Anwendung dar, da er ausreichend Rechenleistung bietet und gleichzeitig eine kompakte Stellfläche und einen angemessenen Stromverbrauch aufweist. Die empfohlene Konfiguration umfasst einen Intel N100-Prozessor, der ausreichende Rechenressourcen für den Poolbetrieb bietet, gepaart mit mindestens einem Terabyte NVMe-Speicher, um die Bitcoin-[Blockchain](https://planb.academy/resources/glossary/blockchain) und die zugehörigen Daten unterzubringen.


Der Speicherbedarf ist besonders kritisch, da der Betrieb eines mining-Pools die Aufrechterhaltung eines vollständig synchronisierten Bitcoin-Knotens voraussetzt. Das NVMe-Laufwerk mit einem Terabyte gewährleistet schnelle Lese-/Schreibvorgänge, die für die Blockchain-Synchronisierung und die laufende [Transaktionsverarbeitung](https://planb.academy/resources/glossary/transaction-tx) unerlässlich sind. Darüber hinaus unterstützt eine ausreichende RAM-Zuweisung den reibungslosen Betrieb sowohl des zugrunde liegenden Linux-Betriebssystems als auch der Knotenverwaltungssoftware, die die Pool-Aktivitäten koordinieren wird.


### Softwarearchitektur und Knotenverwaltung


Der Software-Stack für einen mining-Pool zu Hause baut auf einer Linux-Grundlage auf und bietet die für den Bitcoin-Betrieb erforderliche Stabilität und Sicherheit. Auf diesem Basissystem schafft eine spezialisierte Knotenverwaltungssoftware wie Umbrel eine intuitive Schnittstelle für die Verwaltung der Bitcoin-Infrastruktur. Dieser Ansatz abstrahiert einen Großteil der Komplexität, die traditionell mit dem Betrieb von Bitcoin-Knoten verbunden ist, und macht den Poolbetrieb auch für Benutzer ohne umfassende technische Kenntnisse zugänglich.


Umbrel dient als umfassende Knotenverwaltungsplattform, die die Installation von [Bitcoin Core](https://planb.academy/resources/glossary/bitcoin-core), die Synchronisierung und die laufende Wartung über eine webbasierte Schnittstelle abwickelt. Das App-Store-Modell der Plattform ermöglicht die einfache Installation zusätzlicher Dienste, einschließlich mining-Pool-Software, durch einfache Point-and-Click-Vorgänge. Diese Architektur stellt sicher, dass sich die Benutzer auf den Poolbetrieb und nicht auf die Systemverwaltung konzentrieren können, während sie weiterhin die volle Kontrolle über ihre Bitcoin-Infrastruktur behalten.


### Öffentliches Schwimmbad Installation und Konfiguration


Die Installation der Software für öffentliche Schwimmbäder über die Umbrel-Plattform demonstriert die rationelle Art der modernen Bitcoin-Infrastrukturbereitstellung. Der Prozess beginnt mit dem Zugriff auf den Umbrel-App-Store über die Weboberfläche, wo eine einfache Suche nach "Public Pool" die verfügbare mining-Pool-Software aufzeigt. Die Installation erfordert nur wenige Klicks: Auswahl der Anwendung, Bestätigung der Installation und Warten auf den Abschluss des automatischen Einrichtungsprozesses.


Der Installationsprozess konfiguriert automatisch die erforderlichen Verbindungen zwischen der öffentlichen Pool-Software und dem zugrunde liegenden Bitcoin-Knoten. Diese Integration stellt sicher, dass der Pool Transaktionen validieren, Blockvorlagen erstellen und die Arbeit an die angeschlossenen Miner verteilen kann, ohne dass eine manuelle Konfiguration komplexer Netzwerkparameter erforderlich ist. Nach Abschluss der Installation ist die Pool-Schnittstelle sofort über das lokale Netzwerk zugänglich und bietet Überwachungs- und Verwaltungsfunktionen in Echtzeit.


### Anschluss von Bergleuten und Überlegungen zum Netzwerk


Um mining-Hardware mit Ihrem neu eingerichteten Pool zu verbinden, müssen die Pool-Einstellungen des Miners so konfiguriert werden, dass sie auf Ihre lokale Infrastruktur verweisen. Dazu muss die Standard-Pooladresse durch Ihre lokale IP-Adresse und die entsprechende Portnummer ersetzt werden, die bei der Installation des öffentlichen Pools zugewiesen wurde. Die Konfigurationsänderung leitet die Rechenleistung Ihrer mining-Hardware von externen Pools auf Ihre heimische Infrastruktur um, so dass Sie die volle Kontrolle über den mining-Betrieb und mögliche Gewinne behalten.


Die Netzwerkkonfiguration spielt eine entscheidende Rolle für die Zugänglichkeit und Funktionalität des Pools. Die Einrichtung eines lokalen Netzwerks umfasst in der Regel eine Standard-IP-Adressierung, aber je nach Routerkonfiguration kann es zu Abweichungen bei der DNS-Auflösung kommen. Einige Router bieten lokale DNS-Dienste, die Friendly Names für lokale Dienste erstellen, während andere einen direkten IP-Adressenzugriff erfordern. Für eine breitere Zugänglichkeit über das lokale Netzwerk hinaus kann eine Portweiterleitungskonfiguration auf dem Router erforderlich sein, obwohl dies zusätzliche Sicherheitsüberlegungen mit sich bringt, die eine sorgfältige Abwägung der damit verbundenen Risiken und Vorteile erfordern.


Die erfolgreiche Einrichtung eines mining-Pools zu Hause stellt einen bedeutenden Schritt in Richtung einer dezentralisierten Bitcoin-Infrastruktur dar, die sowohl einen pädagogischen Wert als auch praktische mining-Fähigkeiten bietet und gleichzeitig die vollständige Kontrolle über Ihren Bitcoin-Betrieb behält.


# Hardware-Montage und Fehlersuche

<partId>f6987088-5ba4-52e2-b2d0-aa122080940c</partId>


## Welche Instrumente sind zu verwenden?

<chapterId>733935b5-0171-5a22-838c-e192df6f7ccf</chapterId>


:::video id=bddd0e47-7b43-4685-ba2e-bf3a8ff653c9:::

In der Welt des Lötens von oberflächenmontierten Bauteilen (SMD), insbesondere bei der Arbeit mit Bitaxe-Projekten, macht das richtige Werkzeug den Unterschied zwischen Frustration und Erfolg aus. Dieser umfassende Leitfaden deckt die wesentliche Ausrüstung ab, die benötigt wird, um SMD-Lötprojekte effektiv anzugehen, von grundlegenden Handwerkzeugen bis hin zu spezieller Ausrüstung, die Ihre Lötfähigkeiten verbessern wird.


Wenn Sie die Dokumentation zu den Schaltplänen nachlesen möchten, schauen Sie sich dieses [GitHub Repo](https://github.com/skot/bitaxe-doc/tree/main) an.


### Grundlegende Handwerkzeuge und Präzisionsinstrumente


Die Grundlage jeder SMD-Lötanlage beginnt mit einer hochwertigen Pinzette, die als primäres Werkzeug zur Platzierung der Bauteile dient. Zwei Arten von Pinzetten erweisen sich bei dieser Arbeit als besonders wertvoll: Standardpinzetten mit gerader Spitze und solche mit einer leichten Biegung an der Spitze. Die Pinzette mit gerader Spitze eignet sich für die meisten SMD-Bauteile, die in den typischen Bitaxe-Bausätzen enthalten sind, während die Pinzette mit gebogener Spitze besonders gut für die Arbeit mit extrem kleinen Bauteilen geeignet ist, die eine präzise Positionierung erfordern. Diese Werkzeuge sind oft in Reparatursätzen enthalten, wie z. B. in den iFixit-Sets für Telefonreparaturen, so dass sie für die meisten Bastler leicht zugänglich sind.


Neben der Pinzette ist eine gute Schere unverzichtbar für das Schneiden von Isolierband, das bei Elektronikprojekten mehrere Zwecke erfüllt. Isolierband ist für die Isolierung von Kabeln und Bauteilen unverzichtbar, und wenn man hochwertiges Klebeband zur Hand hat, kann man den Lötprozess optimieren. Diese Grundausstattung kann in Baumärkten oder Online-Händlern beschafft werden, ohne dass man einen spezialisierten Elektroniklieferanten benötigt.


### Anwendung und Verwaltung von Lötpaste


Das Auftragen von Lotpaste ist einer der kritischsten Aspekte des SMD-Lötens, und die richtigen Werkzeuge machen diesen Prozess sowohl präzise als auch angenehm. Kleine, nicht scharfe, mit Lötpaste gefüllte Spritzen bieten eine außergewöhnliche Kontrolle über die Pastenplatzierung. Diese Methode ermöglicht ein präzises Auftragen der exakten Menge an Lötpaste, die für jede Verbindung benötigt wird, und die meisten Menschen entwickeln durch praktische Übung schnell die richtige Technik zur Kontrolle von Druck und Durchflussmenge.


Die Wahl der Lötpaste selbst hat einen erheblichen Einfluss auf den Löterfolg. ChipQuik TS391SNL50 zeichnet sich als außergewöhnliche Lötpaste für Bitaxe-Projekte und allgemeine SMD-Arbeiten aus. Diese Paste weist eine angemessene Konsistenz und Schmelzeigenschaften auf und vermeidet die Probleme, die mit billigeren Alternativen verbunden sind, die einen zu niedrigen Schmelzpunkt haben. Bei minderwertigen Lötpasten kann es zu Problemen kommen, wenn zuvor gelötete Verbindungen beim Erhitzen benachbarter Bereiche wieder flüssig werden, was zu einer Verschiebung von Bauteilen und schlechten Verbindungen führt. Qualitativ hochwertige Lötpaste stellt zwar eine höhere Anfangsinvestition dar, aber die besseren Ergebnisse und die geringere Frustration rechtfertigen die Kosten.


### Problemlösungs- und Bereinigungstools


Selbst erfahrene Löter stoßen auf Probleme, die korrigiert werden müssen, so dass eine Entlötausrüstung für jedes vollständige Toolkit unerlässlich ist. Eine Entlötanlage, im Wesentlichen ein beheiztes Vakuumwerkzeug, entfernt überschüssiges Lot und korrigiert überbrückte Verbindungen zwischen Bauteilstiften. Diese Werkzeuge arbeiten am effektivsten, wenn sie mit Flussmittel kombiniert werden, das den Lötfluss verbessert und dazu beiträgt, dass der Entlötprozess effizienter abläuft.


Flussmittel gibt es in verschiedenen Formen, unter anderem in fester und flüssiger Form, und sie dienen nicht nur zur Unterstützung beim Entlöten. Wenn die Lötpaste während längerer Arbeitssitzungen ihre Wirksamkeit verliert, stellt das Auftragen von zusätzlichem Flussmittel die richtigen Fließeigenschaften wieder her und gewährleistet zuverlässige Verbindungen. Ein kleines löffelartiges Werkzeug, das häufig in Präzisionsreparatursätzen zu finden ist, erleichtert das genaue Auftragen von Flussmittel auf bestimmte Bereiche, ohne die umliegenden Bauteile zu verunreinigen.


Die Reinigung der Platine ist der letzte Schritt für eine professionelle Arbeit und erfordert Isopropanol und eine spezielle Reinigungsbürste. Eine alte Zahnbürste eignet sich hervorragend für diesen Zweck, und eine Squeeze-Flasche mit Isopropanol ermöglicht eine kontrollierte Anwendung der Reinigungslösung. Mit dieser Kombination werden Flussmittel- und Pastenreste entfernt, so dass die Leiterplatten ein sauberes, professionelles Aussehen erhalten, das auch die Inspektion der Lötstellen erleichtert.


### Spezialisierte Ausrüstung und fortschrittliche Werkzeuge


Bei Projekten mit komplexen integrierten Schaltungen, insbesondere ASICs, verwandeln Schablonen den Lötprozess von mühsamer Handarbeit in einen effizienten, präzisen Pastenauftrag. Diese präzisionsgeschnittenen Schablonen gewährleisten eine gleichmäßige Pastenstärke und -platzierung, wodurch sich der Zeitaufwand für komplexe Komponenten drastisch verringert und gleichzeitig die Zuverlässigkeit verbessert. Die Investition in Qualitätsschablonen zahlt sich durch Zeitersparnis und bessere Ergebnisse aus.


Das Wärmemanagement ist bei der Arbeit mit Leistungskomponenten von entscheidender Bedeutung, weshalb Wärmeleitpaste oder Wärmeleitfett unverzichtbare Hilfsmittel sind. Diese Materialien gewährleisten eine ordnungsgemäße Wärmeübertragung zwischen Kühlkörpern und integrierten Schaltkreisen, verhindern thermische Schäden und gewährleisten einen zuverlässigen Betrieb. Qualitativ hochwertige Wärmeleitmaterialien stellen eine kleine Investition dar, die wesentlich teurere Komponenten schützt.


Das Herzstück jeder SMD-Lötanlage ist die Heißluft-Rework-Station, die die für die Oberflächenmontage erforderliche kontrollierte Wärme liefert. Preisgünstige Stationen im Bereich von 30 bis 50 $ können zwar eine angemessene Leistung erbringen, doch fehlt ihnen oft die Zuverlässigkeit und Präzision von Geräten der oberen Preisklasse. Diese Einstiegsstationen arbeiten in der Regel effektiv bei 355 °C und verfügen über eine automatische Temperaturabsenkung, wenn das Handstück in die Halterung zurückgelegt wird. Ihre Zuverlässigkeit kann jedoch unbeständig sein, und manche Geräte fallen vorzeitig aus. Für ernsthafte Arbeiten bietet die Investition in höherwertige Geräte von spezialisierten Elektronikanbietern einen besseren langfristigen Wert durch höhere Zuverlässigkeit und präzisere Temperaturkontrolle.


Die Kombination dieser Werkzeuge ermöglicht ein komplettes SMD-Löten, das weit über Bitaxe-Projekte hinausgeht und auch für allgemeine Elektronikarbeiten geeignet ist. Wenn Sie die Rolle jedes einzelnen Werkzeugs verstehen und eine Qualitätsausrüstung auswählen, die Ihren Fähigkeiten und Projektanforderungen entspricht, können Sie erfolgreiche Ergebnisse und eine angenehme Löterfahrung erzielen.



## Lötprobleme beheben

<chapterId>96663744-b4f7-5154-930f-a68ba7954603</chapterId>


:::video id=9286c0dc-acd6-44d9-b34e-59cfb2da9748:::


Der Bitaxe-Transceiver-Bausatz stellt beim Zusammenbau besondere Herausforderungen dar, die eine sorgfältige Beachtung der Komponentenausrichtung, der Vermeidung von Lötbrücken und des richtigen Wärmemanagements erfordern. Das Verständnis dieser häufigen Probleme und ihrer Lösungen ist für den erfolgreichen Zusammenbau des Bausatzes und die Vermeidung kostspieliger Bauteilschäden unerlässlich. Dieses Kapitel befasst sich mit den häufigsten Lötproblemen, die bei der Bitaxe-Baugruppe auftreten, und bietet praktische Techniken, um diese zu erkennen und zu lösen.


### Orientierung und Identifizierung von Komponenten


Die korrekte Ausrichtung der Komponenten ist einer der wichtigsten Aspekte einer erfolgreichen Bitaxe-Montage, insbesondere bei den MOSFETs Q1 und Q2. Diese Komponenten weisen unverwechselbare Orientierungsmarkierungen auf, die beim Einbau sorgfältig beachtet werden müssen. Jeder MOSFET ist mit einer kleinen Punktmarkierung versehen, die einer bestimmten Pad-Anordnung auf der Leiterplatte entspricht. Der Schlüssel zur korrekten Ausrichtung liegt im Verständnis der physikalischen Struktur dieser Bauteile, die vier Stifte aufweisen, die mit einem großen Pad und drei kleineren Pads angeordnet sind, die keine Verbindung zum großen Pad haben.


Untersuchen Sie beim Einbau von Q1 und Q2 sowohl das Bauteil als auch die Leiterplatte sorgfältig. Das Platinenlayout zeigt die vorgesehene Ausrichtung durch die Pad-Konfiguration deutlich an, wobei vier Stifte so positioniert sind, dass sie der MOSFET-Struktur entsprechen. Bevor Sie ein großes Bauteil einlöten, überprüfen Sie immer die Ausrichtung, indem Sie die physischen Markierungen des Bauteils mit der Anordnung der Pads auf der Platine vergleichen. Dieser einfache Überprüfungsschritt vermeidet die Frustration des Auslötens und Wiedereinbaus von falsch ausgerichteten Komponenten.


Die Folgen einer falschen Ausrichtung gehen über einfache Funktionsprobleme hinaus. Falsch ausgerichtete MOSFETs können zu Schaltkreisfehlfunktionen führen, die schwer zu diagnostizieren sind und möglicherweise den kompletten Austausch von Komponenten erfordern. Wenn Sie sich die Zeit nehmen, die Ausrichtung zu überprüfen, bevor Sie Wärme zuführen, wird der ordnungsgemäße Betrieb der Schaltung sichergestellt und eine unnötige Fehlersuche im späteren Verlauf des Montageprozesses vermieden.


### Umgang mit Lötbrücken und überschüssigem Lötzinn


Lötbrücken sind eine weitere häufige Herausforderung bei der Bitaxe-Bestückung, insbesondere bei Fine-Pitch-Komponenten wie U10. Diese unerwünschten Verbindungen zwischen benachbarten Pins können zu Fehlfunktionen in der Schaltung führen und erfordern sorgfältige Entlöttechniken. Die effektivste Methode ist die Verwendung eines Entlötdochts, eines Kupfergeflechts, das bei Erwärmung überschüssiges Lot aufnimmt. Diese Technik erfordert Geduld und die richtige Auswahl des Werkzeugs, um die empfindlichen Bauteile nicht zu beschädigen.


Wenn Sie Lötbrücken auf integrierten Schaltungen behandeln, verwenden Sie einen Leiterplattenhalter oder eine Gelenkklemme, um das Bauteil während der Arbeit sicher zu halten. Wenden Sie sanfte Wärme auf den betroffenen Bereich an und ziehen Sie den Entlötdocht vorsichtig über die überbrückten Verbindungen. Das Kupfergeflecht absorbiert auf natürliche Weise das überschüssige Lot und trennt die unerwünschten Verbindungen. Dieser Vorgang kann mehrere Versuche erfordern, aber Ausdauer führt zu sauberen, richtig getrennten Verbindungen.


Vorbeugung ist nach wie vor der beste Ansatz für das Management von Lötbrücken. Die Verwendung einer angemessenen Menge an Lötpaste und die Beibehaltung einer ruhigen Hand bei der Platzierung der Komponenten reduziert die Brückenbildung erheblich. Wenn dennoch Brücken auftreten, sollten Sie diese sofort beseitigen, anstatt zu hoffen, dass sie den Betrieb der Schaltung nicht beeinträchtigen. Selbst scheinbar unbedeutende Brücken können zu erheblichen Funktionsproblemen führen, die schwer zu diagnostizieren sind, sobald die Leiterplatte fertig montiert ist.


### Kritische Komponenten und besondere Erwägungen


Der Abwärtswandler U9 verdient besondere Aufmerksamkeit, da er eine entscheidende Rolle bei der Umwandlung von 5 Volt in 1,2 Volt für den ASIC-Chip spielt. Dieses Bauteil stellt aufgrund seiner fünf kleinen Anschlüsse und seiner Neigung zum Versagen eine besondere Herausforderung dar. Die ordnungsgemäße Installation erfordert einen präzisen Auftrag von Lötpaste und ein sorgfältiges Wärmemanagement. Unzureichende Lötpaste unter U9 kann zu schlechten Verbindungen führen, die eine ordnungsgemäße Spannungsumwandlung verhindern, während überschüssige Paste zu Brücken führen kann, die eine Fehlfunktion der Schaltung verursachen.


U9 erzeugt bei Problemen mit der Lötbrücke eine charakteristische Audiosignatur, die ein hochfrequentes Rauschen erzeugt, das sich vom normalen Betrieb des ASIC unterscheidet. Diese auditive Diagnosetechnik kann bei der Identifizierung von Problemen helfen, erfordert jedoch ein gutes Gehör für hohe Frequenzen, um sie zu erkennen. Wenn eine akustische Diagnose nicht möglich ist, ist eine visuelle Inspektion unerlässlich. Untersuchen Sie alle Verbindungen sorgfältig auf Brücken oder unzureichende Lötstellen.


Wenn U9 nicht die erforderlichen 1,2 Volt ausgibt, obwohl es ordnungsgemäß verlötet zu sein scheint, ist die wahrscheinliche Ursache unzureichende Lötpaste. Entfernen Sie das Bauteil, tragen Sie eine kleine Menge zusätzlicher Lötpaste auf und bauen Sie es wieder ein. In Fällen, in denen einzelne Pins nicht ausreichend mit Lötmittel bedeckt sind, tragen Sie mit einer Pinzette vorsichtig kleine Mengen Lötpaste auf bestimmte Stellen auf. Die Lötpaste fließt bei Erwärmung von selbst unter das Bauteil und stellt durch Kapillarwirkung ordnungsgemäße Verbindungen her.


### Wärmemanagement und Bauteilschutz


Ein angemessenes Wärmemanagement schützt empfindliche Bauteile vor thermischen Schäden und gewährleistet gleichzeitig zuverlässige Lötstellen. Bauteile wie der Quarzoszillator Y1 und U1 sind besonders empfindlich gegenüber längerer Hitzeeinwirkung und erfordern eine sorgfältige Temperaturkontrolle. Halten Sie die Temperatur des Lötkolbens bei 350 Grad Celsius, aber minimieren Sie die Dauer der Wärmeeinwirkung, um eine Beschädigung der Bauteile zu vermeiden. Schnelle, effiziente Löttechniken schützen diese empfindlichen Bauteile und sorgen für zuverlässige Verbindungen.


Der ASIC-Chip erfordert aufgrund seiner komplexen Pin-Struktur und seiner Empfindlichkeit gegenüber mechanischer Beanspruchung besondere Handhabungsmethoden. Wenn Sie Schablonen zum Auftragen von Lotpaste verwenden, achten Sie darauf, dass alle Pins gleichmäßig bedeckt sind, um einen ungleichmäßigen Sitz der Komponenten zu vermeiden. Wenn zu viel Lotpaste dazu führt, dass das ASIC ungleichmäßig sitzt, lassen Sie die Baugruppe vollständig abkühlen, bevor Sie Korrekturen vornehmen. Üben Sie während des Aufheizens nur leichten Druck auf die beschrifteten Kanten des Bauteils aus, niemals auf den zentralen Chipbereich, um einen korrekten Sitz zu erreichen.


Das Bauteil U8 stellt aufgrund seiner zahlreichen Stifte und der Möglichkeit verbogener Leitungen eine besondere Herausforderung dar. Wenn Stifte bei der Handhabung verbogen werden, verwenden Sie einen Leiterplattenhalter oder eine Gelenkklemme, um das Bauteil zu sichern und die betroffenen Stifte vorsichtig zu richten. Arbeiten Sie langsam und geduldig, um ein Abbrechen der empfindlichen Anschlüsse zu vermeiden. Wenn Sie wissen, dass bestimmte Pin-Gruppen auf U8 intern verbunden sind, kann die Fehlersuche vereinfacht werden, da Brücken zwischen diesen spezifischen Pins den Betrieb der Schaltung nicht beeinträchtigen. Brücken zwischen anderen Stiften müssen jedoch vorsichtig entfernt werden, um die ordnungsgemäße Funktion sicherzustellen.


## Wie Sie Ihren Bitaxe mit AxeOS debuggen

<chapterId>603f5c0d-4b7c-51e1-9bad-318a8b8e9db7</chapterId>

:::video id=d23d748b-510e-4748-9617-b875da757031:::

Bei der Arbeit mit Bitaxe mining-Geräten können sich Hardware-Fehler auf verschiedene Weise bemerkbar machen, die möglicherweise nicht sofort offensichtlich sind. Wenn Sie wissen, wie Sie diese Probleme mit dem AxeOS-Betriebssystem systematisch diagnostizieren, können Sie viel Zeit sparen und den Austausch unnötiger Komponenten verhindern. In diesem Kapitel werden die Diagnosetechniken und Fehlerbehebungsmethoden untersucht, die erfahrene Techniker verwenden, um spezifische Hardwareprobleme durch Softwareanalyse zu identifizieren.


### Verstehen der Stromverbrauchsanzeigen


Der erste und wichtigste Diagnose-Indikator in AxeOS ist die Überwachung des Stromverbrauchs. Normale Bitaxe-Geräte, einschließlich der Bitaxe Ultra- und Bitaxe Supra-Modelle, verbrauchen im Normalbetrieb zwischen 10 und 17 Watt. Diese Basismessung dient als primärer Gesundheitsindikator für das gesamte System. Wenn der Stromverbrauch deutlich unter diesen Bereich fällt, insbesondere unter 3 Watt, deutet dies auf ein grundsätzliches Problem mit dem ASIC-Chip oder seiner unterstützenden Schaltung hin.


Szenarien mit niedrigem Stromverbrauch erfordern sofortige Aufmerksamkeit, da sie darauf hindeuten, dass der mining-Chip entweder völlig funktionsunfähig ist oder in einem stark degradierten Zustand arbeitet. Diese Messung allein kann Ihnen helfen, schnell zwischen Leistungsproblemen und kompletten Hardwareausfällen zu unterscheiden. Die Stromverbrauchsmessung in AxeOS liefert ein Echtzeit-Feedback, mit dem Sie die Wirksamkeit aller Reparaturversuche am Gerät überwachen können.


### Analyse der ASIC-Spannungsmessungen


Die Spannungsmessungsfunktion des ASIC in AxeOS liefert wichtige Diagnoseinformationen, die helfen, die genaue Art von Hardwareproblemen zu ermitteln. Bei der Untersuchung von Spannungsmesswerten müssen Sie die Beziehung zwischen der gemessenen Spannung und der angeforderten Spannung verstehen, um Probleme richtig zu diagnostizieren. Das System zeigt sowohl die Spannung an, die an den ASIC-Chip geliefert wird, als auch die Spannung, die der Chip vom Power-Management-System anfordert.


Wenn Sie eine ASIC-Spannungsmessung von genau 1,2 Volt in Verbindung mit einer Leistungsaufnahme von weniger als 3 Watt beobachten, deutet diese spezifische Kombination entweder auf ein Lötproblem mit dem ASIC-Chip oder auf einen vollständig ausgefallenen ASIC hin. Diese Spannungsmessung deutet darauf hin, dass der Chip zwar mit Strom versorgt wird, aber der Chip selbst nicht richtig funktioniert. Bei einer physischen Inspektion des ASIC-Chips können Risse oder andere sichtbare Schäden festgestellt werden, die dieses Verhaltensmuster erklären würden.


Ein anderes Diagnoseszenario ergibt sich, wenn eine geringe Leistungsaufnahme mit sehr niedrigen angeforderten Spannungswerten, wie 100 Millivolt oder 0,5 Volt, einhergeht. Dieses Muster deutet darauf hin, dass der ASIC-Chip nicht ausreichend mit Spannung versorgt wird, was in der Regel auf Probleme mit der Abwärtswandlerkomponente U9 hinweist. Der Abwärtswandler ist für die präzise Spannungsregelung verantwortlich, die ASIC-Chips für den ordnungsgemäßen Betrieb benötigen.


### Interpretation von Protokolldaten und ASIC-Kommunikation


Das AxeOS-Protokollierungssystem liefert wertvolle Informationen darüber, ob Ihr ASIC-Chip mit dem Kontrollsystem kommuniziert. Wenn Sie über die Funktion "show logs" auf die Protokolle zugreifen, bestätigt das Vorhandensein von "ASIC results"-Einträgen, dass der Chip nicht nur mit Strom versorgt wird, sondern auch aktiv Arbeit verarbeitet und Ergebnisse liefert. Diese Kommunikation deutet darauf hin, dass der ASIC ordnungsgemäß verlötet ist und seine Verbindung zum Steuerkreislauf aufrechterhält.


Das Fehlen von ASIC-Ergebnissen in den Protokollen, insbesondere in Verbindung mit anderen Symptomen, hilft, das Problem auf bestimmte Komponenten oder Verbindungsprobleme einzugrenzen. Dieser Diagnoseansatz ermöglicht es Ihnen, zwischen Chips zu unterscheiden, die überhaupt nicht reagieren, und solchen, bei denen es zu zeitweiligen Verbindungsproblemen kommen kann. Die Protokollanalyse ist besonders wertvoll bei der Behebung komplexer Probleme, bei denen mehrere Symptome auf unterschiedliche Ursachen hindeuten können.


### Systematischer Ansatz zur Fehlersuche


Bei der Diagnose von Bitaxe-Hardware-Problemen sollte man systematisch vorgehen, um zu verhindern, dass kritische Probleme übersehen werden, und um effiziente Reparaturprozesse zu gewährleisten. Beginnen Sie mit der Dokumentation des Stromverbrauchs und der Spannungsmesswerte und setzen Sie diese Messungen dann mit den Protokolldaten in Beziehung, um ein vollständiges Bild des Systemverhaltens zu erhalten. Mit diesem methodischen Ansatz lässt sich feststellen, ob die Probleme vom ASIC-Chip selbst, vom Stromversorgungssystem oder von den Kommunikationspfaden zwischen den Komponenten herrühren.


In Fällen, in denen der U9-Abwärtswandler das Problem zu sein scheint, kann eine physische Inspektion und ein mögliches Nachlöten erforderlich sein. Die U9-Komponente ist besonders anfällig für Lötprobleme, vor allem beim erstmaligen Zusammenbau. Wenn Probleme mit der Spannungsregulierung vermutet werden, kann mit einem Multimeter überprüft werden, ob an den ASIC-Pins tatsächlich 1,2 Volt anliegen, um die Probleme mit der Stromversorgung endgültig zu bestätigen. Wenn die Spannung an den Pins vorhanden ist, das ASIC aber immer noch nicht funktioniert und die physische Inspektion keine Schäden zeigt, ist der Austausch des ASIC-Chips der nächste logische Schritt. Sollten die Probleme auch nach dem Austausch des ASIC fortbestehen, muss als letztes Element der Fehlersuchsequenz möglicherweise die U2-Komponente, die den ASIC-Chip ansteuert, untersucht werden.


## Wie kann man mit USB debuggen?

<chapterId>f3182763-e1ef-5460-8bc0-f2ea53e3a410</chapterId>


:::video id=fe1b4b48-5f8a-4fd7-9417-ca03a36bce9f:::


Bei der Fehlersuche in Bitaxe mining-Geräten bietet der direkte Zugriff auf das interne Protokollierungssystem des Geräts unschätzbare Einblicke, die webbasierte Schnittstellen nicht bieten können. In diesem Kapitel wird untersucht, wie eine direkte serielle USB-Verbindung zu Ihrem Bitaxe-Gerät unter Verwendung des ESP-IDF-Frameworks hergestellt werden kann, was die Echtzeitüberwachung von Systemprotokollen, Bootsequenzen und Fehlermeldungen ermöglicht. Dieser Debugging-Ansatz ist besonders wichtig bei Geräten, die häufig neu gestartet werden oder bei denen es zu Hardwarefehlern kommt, da er alle Diagnoseinformationen erfasst, die bei einem Systemneustart verloren gehen könnten.


Der Debugging-Prozess erfordert Visual Studio Code mit der ESP-IDF-Erweiterung, obwohl jede kompatible IDE verwendet werden kann. Diese Methode funktioniert mit allen Bitaxe-Varianten, die über einen USB-Anschluss verfügen, einschließlich des Bitaxe Ultra 204 und anderer Modelle der Serie. Die direkte serielle Verbindung umgeht mögliche Einschränkungen der Webschnittstelle und bietet ungefilterten Zugriff auf die internen Statusinformationen des Geräts.


### Einrichten der seriellen Kommunikation


Der Aufbau der Kommunikation mit Ihrem Bitaxe-Gerät beginnt mit dem Anschluss des USB-Kabels und dem Öffnen des ESP-IDF-Terminals in Ihrer Entwicklungsumgebung. Der Befehl `idf.py monitor` initiiert den Verbindungsprozess und scannt automatisch die verfügbaren COM-Ports, um eine UART-Kommunikation mit dem ESP32-Chip auf Ihrem Bitaxe-Gerät herzustellen. Das System durchläuft in der Regel die verfügbaren Ports (COM3, COM4, COM16, etc.), bis es die richtige Verbindung findet.


Sobald die Verbindung hergestellt ist, zeigt das Terminal die komplette Boot-Sequenz und die laufenden Betriebsprotokolle an. Der anfängliche Verbindungsvorgang kann einige Augenblicke dauern, da das System den richtigen Kommunikationsanschluss identifiziert. Wenn die automatische Anschlusserkennung fehlschlägt, können Sie den COM-Anschluss manuell über die Anschlussauswahlschnittstelle des IDE festlegen. Dieser direkte Kommunikationskanal bleibt während des gesamten Betriebs des Geräts aktiv und bietet kontinuierlichen Zugang zu Systemdiagnosen und Leistungsmetriken.


### Interpretation der Bootsequenz und der Protokolle des Normalbetriebs


Die Startsequenz liefert wichtige Informationen über die Hardwarekonfiguration und den Initialisierungsprozess Ihres Bitaxe-Geräts. Normale Startprotokolle beginnen mit ESP-IDF Versionsinformationen, gefolgt von der unverwechselbaren "Welcome to the Bitaxe. Hack the planet", die das erfolgreiche Laden der Firmware bestätigt. Anschließend zeigt das System die ASIC-Frequenzkonfiguration, die Identifikation des Gerätemodells und die Details der Boardversion an.


Ein ordnungsgemäß funktionierendes Gerät zeigt eine erfolgreiche I2C-Initialisierung und eine auf 1,2 Volt eingestellte ASIC-Spannungsregelung. Die Protokolle zeigen GPIO-Statusinformationen und Wi-Fi-Initialisierungssequenzen an, gefolgt von der DHCP-Serverkonfiguration und der IP-Adresszuweisung. Einer der wichtigsten Indikatoren ist die ASIC-Chip-Erkennungsmeldung, die bei einem Ein-Chip-Gerät "einen ASIC-Chip erkannt" melden sollte. Diese Bestätigung bestätigt, dass die mining-Hardware ordnungsgemäß angeschlossen ist und mit dem ESP32-Steuergerät kommuniziert.


Aus den Betriebsprotokollen geht hervor, dass auf dem Gerät mehrere Aufgaben gleichzeitig ausgeführt werden, darunter die Kommunikation der Schicht API, die Koordination der Hauptaufgabe, die Verwaltung der ASIC-Aufgabe und die Verarbeitung der Schichtaufgabe. Diese verschiedenen Task-Kennungen helfen bei der Eingrenzung von Problemen auf bestimmte Systemkomponenten. Zum normalen Betrieb gehören der Aufbau von Pool-Verbindungen, Meldungen zur Anpassung der Schwierigkeit, das Einreihen in eine Warteschlange und das Entfernen aus einer Warteschlange sowie die Meldung der Nonce-Generierung. Erfolgreiche mining-Operationen zeigen ASIC-Ergebnisse mit Schwierigkeitsberechnungen und mining-Übermittlungsbestätigungen an, wenn die Anteile den erforderlichen Schwellenwert erreichen.


### Identifizierung von Hardwarefehlern und Fehlermustern


Hardware-Fehler manifestieren sich in den Protokollen durch spezifische Fehlermuster, die anzeigen, welche Komponenten fehlerhaft arbeiten. Der häufigste Fehlermodus sind I2C-Kommunikationsfehler mit bestimmten integrierten Schaltkreisen auf dem Bitaxe-Board. Beispielsweise erscheinen DS4432U-Kommunikationsfehler als "ESP_ERROR_CHECK failed"-Meldungen mit Timeout-Indikatoren, die auf Spannungsregulierungsprobleme oder Lötprobleme bei der für die Display-Kommunikation zuständigen U10-Komponente hinweisen.


Diese Fehlermeldungen enthalten detaillierte Debugging-Informationen wie die spezifische Quelldatei (main_ds4432u.c), den fehlgeschlagenen Funktionsaufruf und den Prozessorkern, der die Aufgabe bearbeitet. Die Backtrace-Informationen bieten zusätzlichen Kontext für die erweiterte Fehlersuche. Ähnliche Fehlermuster können mit dem EMC2101-Temperatur- und Lüftersteuerungs-Chip auftreten, die jeweils unverwechselbare Protokollsignaturen erzeugen, die zur Identifizierung der fehlerhaften Komponente beitragen.


Physikalische Hardware-Probleme äußern sich oft in wiederholten Fehlerzyklen, gefolgt von einem Neustart des Systems. Wenn Ihr Gerät während des Betriebs hörbare Geräusche erzeugt, deutet dies in der Regel auf Lötprobleme hin, z. B. Brücken zwischen Komponentenstiften oder unzureichende Lötstellen. Diese mechanischen Probleme führen zwar nicht immer zu generate spezifischen Protokolleinträgen, aber sie schaffen instabile Betriebsbedingungen, die sich in häufigen Abstürzen und Neustartzyklen in der Überwachungsausgabe manifestieren.


### Erweiterte Strategien zur Fehlerbehebung


Die serielle Überwachung bietet mehrere Vorteile gegenüber webbasierten Debugging-Schnittstellen, insbesondere bei intermittierenden Fehlern oder Geräten, die häufig neu gestartet werden. Die kontinuierliche Protokollierung stellt sicher, dass bei Systemneustarts keine Diagnoseinformationen verloren gehen, im Gegensatz zu Webschnittstellen, bei denen Daten bei Verbindungsabbrüchen verloren gehen können. Diese umfassende Protokollierungsfunktion ermöglicht es, Muster in Fehlern zu erkennen und bestimmte Fehlerbedingungen mit Hardware- oder Umgebungsfaktoren zu korrelieren.


Konzentrieren Sie sich bei der Analyse problematischer Geräte auf die Abfolge der Ereignisse, die zu Ausfällen führen, und nicht auf einzelne Fehlermeldungen. Eine erfolgreiche ASIC-Kommunikation sollte regelmäßige Auftragsverarbeitungs-, Nonce-Generierungs- und Share-Sendezyklen aufweisen. Fehlende ASIC-Ergebnisse in den Protokollen deuten auf Kommunikationsfehler zwischen dem ESP32 und dem mining-Chip hin, die häufig durch Probleme mit der Stromversorgung, beschädigte Leiterbahnen oder Komponentenausfälle verursacht werden.


Zur systematischen Fehlersuche sollten Sie Fehlermuster und komponentenspezifische Ausfälle dokumentieren, bevor Sie sich an die Community wenden. Die detaillierten Fehlerprotokolle, einschließlich spezifischer Chip-Identifikatoren und Fehlermodi, ermöglichen es erfahrenen Anwendern, gezielte Reparaturanleitungen zu geben, z. B. Verfahren zum Austausch von Komponenten oder Korrekturen beim Löten. Diese methodische Herangehensweise an die Hardware-Fehlersuche verbessert die Erfolgsquote bei der Reparatur erheblich und verkürzt die Zeit für die Fehlersuche bei komplexen Problemen.


# Erweiterte Anpassung

<partId>8d333102-ecb5-5f05-bfb5-03a27b2d0d70</partId>


## Ändern Sie die Leiterplatte

<chapterId>ca08d2a4-2b34-575b-aecc-7482a03c190e</chapterId>


:::video id=30fb0010-f560-4e96-a05b-c21dc172746e:::

KiCad ist eines der leistungsstärksten Open-Source-Tools für das Design und die Entflechtung von Leiterplatten (PCB). Diese professionelle Software ermöglicht es Ingenieuren und Bastlern, komplexe elektronische Designs zu erstellen, indem sie Komponenten auf virtuellen Leiterplatten platzieren und die komplizierten Leiterbahnen verlegen, die diese Komponenten miteinander verbinden. Was KiCad für Ausbildungs- und Entwicklungszwecke besonders wertvoll macht, ist sein vollständiger Open-Source-Charakter, der es den Benutzern ermöglicht, bestehende Designs ohne Lizenzbeschränkungen zu ändern, anzupassen und von ihnen zu lernen.


Das Bitaxe-Projekt ist ein Beispiel für die Leistungsfähigkeit der Open-Source-Hardwareentwicklung, da es ein komplettes PCB-Design bereitstellt, das die Benutzer untersuchen, verändern und an ihre spezifischen Bedürfnisse anpassen können. Diese Zugänglichkeit schafft eine hervorragende Lernumgebung, in der Studenten und Praktiker reale PCB-Designs erforschen können, während sie ihr Verständnis für elektronische Systeme entwickeln. Die Möglichkeit, visuelle Elemente wie Logos anzupassen, bietet einen einfachen Einstieg für Benutzer, die von der technischen Komplexität des Elektronikdesigns eingeschüchtert sind.


### Einrichten Ihrer KiCad-Umgebung


Bevor Sie mit den Anpassungen beginnen, ist die richtige Einrichtung Ihrer Entwicklungsumgebung unerlässlich. Das Bitaxe-Repository muss auf Ihren lokalen Rechner heruntergeladen werden, was in der Regel über die ZIP-Download-Funktion von GitHub geschieht. Dieses Repository enthält alle erforderlichen Projektdateien, einschließlich der KiCad-Projektdateien, Komponentenbibliotheken und der Konstruktionsdokumentation, die für eine erfolgreiche Änderung erforderlich sind.


Die KiCad-Installation sollte mit der offiziellen Distribution von der KiCad-Website durchgeführt werden, um die Kompatibilität mit den Projektdateien und den Zugriff auf die neuesten Funktionen sicherzustellen. Sobald sowohl das Repository als auch KiCad ordnungsgemäß installiert sind, muss zum Öffnen des Projekts zur Bitaxe Ultra KiCad-Projektdatei innerhalb der heruntergeladenen Repository-Struktur navigiert werden. Diese Projektdatei dient als zentraler Knotenpunkt, der alle zugehörigen Designdateien, Komponentenbibliotheken und Konfigurationseinstellungen verknüpft.


Der erste Blick auf ein komplexes PCB-Design kann überwältigend erscheinen, da zahlreiche Komponenten, Leiterbahnen und Ebenen eine dichte visuelle Landschaft bilden. Die 3D-Viewer-Funktionalität von KiCad ist jedoch ein unschätzbares Werkzeug, um das physikalische Layout und die räumlichen Beziehungen innerhalb des Designs zu verstehen. Diese dreidimensionale Perspektive verwandelt die abstrakte schematische Darstellung in eine realistische Visualisierung des fertigen Produkts, wodurch die Platzierung der Komponenten und die Gesamtästhetik des Designs leichter zu verstehen sind.


### Prozess der Logoanpassung


Das Anpassen von Logos auf Leiterplattenentwürfen ist eine der zugänglichsten Modifikationen für Benutzer, die neu in KiCad sind, da es nur minimale technische Kenntnisse erfordert und sofortige visuelle Ergebnisse liefert. Der Prozess beginnt mit dem Bildkonverter-Tool, das Standard-Bilddateien in Footprint-Formate umwandelt, die mit der PCB-Design-Software kompatibel sind. Dieser Konvertierungsprozess erfordert eine sorgfältige Beachtung der Größenparameter, die in der Regel in Millimetern gemessen werden, um eine korrekte Skalierung auf der fertigen Leiterplatte zu gewährleisten.


Der Bildkonvertierungs-Workflow umfasst mehrere kritische Schritte, die das endgültige Erscheinungsbild und die Platzierung der individuellen Logos bestimmen. Bei der Auswahl des Quellbildes sollte auf kontrastreiche Designs geachtet werden, die sich gut im Siebdruckverfahren der Leiterplattenherstellung verarbeiten lassen. Die Festlegung der Größe ist von entscheidender Bedeutung, da die Logos groß genug sein müssen, um nach der Herstellung lesbar zu bleiben, ohne die Platzierung der Komponenten oder die Funktionalität zu beeinträchtigen. Die Wahl zwischen vorderen und hinteren Siebdruckschichten wirkt sich sowohl auf die Sichtbarkeit als auch auf die Herstellung aus.


Die Verwaltung von Footprint-Bibliotheken ist ein grundlegender Aspekt der KiCad-Anpassung und erfordert, dass die Benutzer verstehen, wie die Software die Designelemente organisiert und darauf zugreift. Das Hinzufügen von benutzerdefinierten Logos beinhaltet das Erstellen neuer Footprint-Bibliotheken oder das Ändern bestehender Bibliotheken und das anschließende ordnungsgemäße Verknüpfen dieser Bibliotheken innerhalb der Projektstruktur. Dieser Prozess stellt sicher, dass benutzerdefinierte Elemente über verschiedene Entwurfssitzungen hinweg zugänglich bleiben und leicht mit anderen Teammitgliedern oder Mitarbeitern geteilt werden können.


### Erforschung und Verständnis von Design für Fortgeschrittene


Über die einfache Logoanpassung hinaus bietet KiCad leistungsstarke Werkzeuge zum Erforschen und Verstehen komplexer PCB-Designs. Das Ebenenverwaltungssystem ermöglicht es Benutzern, verschiedene Aspekte des Entwurfs selektiv zu betrachten, von der Komponentenplatzierung und dem Routing bis hin zu Fertigungsspezifikationen und Montageinformationen. Dieser schichtweise Ansatz ermöglicht eine detaillierte Analyse spezifischer Designelemente ohne visuelle Unordnung durch nicht verwandte Komponenten.


Die Analyse des Leiterbahnverlaufs ist einer der lehrreichsten Aspekte der Leiterplattenuntersuchung, denn sie zeigt, wie elektrische Verbindungen zwischen Komponenten und Subsystemen fließen. Durch die Verfolgung einzelner Leiterbahnen oder Gruppen zusammengehöriger Signale kann der Benutzer ein Verständnis für die Funktionalität von Schaltungen und Designentscheidungen entwickeln. Die Untersuchung von Stromverteilungsnetzen zeigt zum Beispiel, wie Spannungsregelung und Filterkomponenten zusammenarbeiten, um empfindliche elektronische Komponenten mit sauberer, stabiler Energie zu versorgen.


Die Beziehung zwischen Schaltplandesign und physischem Layout wird durch eine sorgfältige Untersuchung der Bauteilplatzierung und Routing-Entscheidungen deutlich. Wenn man versteht, warum bestimmte Komponenten an bestimmten Stellen positioniert werden, wie thermische Überlegungen die Layout-Entscheidungen beeinflussen und wie die Anforderungen an die Signalintegrität die Routing-Entscheidungen beeinflussen, erhält man wertvolle Einblicke in die professionelle PCB-Designpraxis. Dieses Wissen ist von unschätzbarem Wert für Benutzer, die ihre eigenen Designs entwickeln oder bestehende Designs für bestimmte Anwendungen modifizieren.


KiCad's umfassende Werkzeuge zur Überprüfung von Entwurfsregeln und zur Verifizierung stellen sicher, dass Änderungen die elektrische und fertigungstechnische Kompatibilität aufrechterhalten. Diese automatisierten Systeme helfen dabei, häufige Konstruktionsfehler zu vermeiden, während sie die Benutzer über Industriestandards und Best Practices aufklären. Die Integration von 3D-Visualisierung mit elektrischen Konstruktionsdaten schafft eine leistungsstarke Lernumgebung, in der theoretische Konzepte durch visuelle Darstellung und interaktive Erkundung greifbar werden.


## Wie erstellt man eine Fabrikdatei?

<chapterId>e9da631c-e6d1-50c1-bb59-bc8455c29d3e</chapterId>


:::video id=07f980bf-6052-4ed4-bf7b-75e8aba585df:::

Die Erstellung benutzerdefinierter Firmware für ESP-basierte mining-Geräte erfordert eine sorgfältige Beachtung der Konfiguration, der Abhängigkeiten und des richtigen Erstellungsprozesses. Dieser umfassende Leitfaden führt Sie durch den kompletten Prozess der Erstellung von Standard-Firmware-Binärdateien und Werksdateien mit vorkonfigurierten Einstellungen, die die Bereitstellung effizienter machen und die Einrichtungszeit für Endbenutzer verkürzen.


Beachten Sie, dass dieses Kapitel recht technisch ist und nur überflogen werden kann, wenn Sie neugierig darauf sind.


### Einrichten der Entwicklungsumgebung


Um mit der Entwicklung der ESP-Miner-Firmware zu beginnen, sollten Sie zunächst die richtige Entwicklungsumgebung in Visual Studio Code einrichten, idealerweise auf einer Linux-Distribution. Die ESP-IDF-Erweiterung dient als Eckpfeiler dieser Einrichtung und bietet die notwendigen Werkzeuge und die Integration des Frameworks für die ESP32-Entwicklung. Bei der erstmaligen Installation der ESP-IDF-Erweiterung wird der Benutzer durch einen Setup-Guide geführt, der den Konfigurationsprozess erleichtert.


Ein entscheidender Punkt bei der Einrichtung ist die Auswahl der geeigneten ESP-IDF-Version. Während früher die Version 5.1.3 empfohlen wurde, hat die praktische Erfahrung gezeigt, dass diese Version Probleme bei der Erstellung verursachen kann, die den Entwicklungsprozess erschweren. Die empfohlene Vorgehensweise besteht nun darin, ESP-IDF Version 5.3 Beta 1 zu verwenden, die nachweislich diese Komplikationen bei der Erstellung behebt und sicherstellt, dass Bitaxe-Geräte ordnungsgemäß funktionieren. Der Installationsprozess erfordert die Auswahl der Express-Installationsoption und insbesondere die Auswahl von Version 5.3 Beta 1 aus den verfügbaren Optionen.


Die Einrichtung der Entwicklungsumgebung geht über die ESP-IDF-Installation hinaus und umfasst auch die richtige Terminal-Konfiguration. Visual Studio Code bietet mehrere Methoden für den Zugriff auf die ESP-IDF-Funktionalität, einschließlich der Befehlspalettenoption zum Öffnen eines ESP-IDF-Terminals oder der Verwendung des speziellen Terminalsymbols in der Benutzeroberfläche. Diese spezielle Terminalumgebung stellt sicher, dass alle ESP-IDF-Befehle korrekt funktionieren und bietet Zugriff auf die komplette Toolchain.


### Konfigurieren der ESP-Miner-Einstellungen


Die Konfigurationsdatei ist das Herzstück des ESP-Miner-Anpassungsprozesses. Sie enthält alle wesentlichen Parameter, die festlegen, wie das Gerät in seiner Zielumgebung funktionieren soll. Diese Konfiguration umfasst Netzwerkeinstellungen, mining-Poolverbindungen und hardwarespezifische Parameter, die auf das jeweilige Einsatzszenario zugeschnitten werden müssen.


Die Netzwerkkonfiguration ist die wichtigste Komponente des Einrichtungsprozesses und erfordert die Angabe von Wi-Fi-Anmeldeinformationen, einschließlich SSID und Passwort. Anstatt Platzhalterwerte wie "Test" zu verwenden, sollten Produktionskonfigurationen die tatsächlichen Netzwerkanmeldeinformationen enthalten, die das Gerät in seiner Betriebsumgebung verwenden wird. Die Konfiguration berücksichtigt auch verschiedene mining-Pool-Konfigurationen, die sowohl private Pool-Konfigurationen mit spezifischen IP-Adressen als auch öffentliche Pools wie public-pool.io mit den entsprechenden Port-Einstellungen unterstützen.


Zu den Mining-spezifischen Konfigurationsparametern gehört die Stratum-Benutzereinstellung, die in der Regel der Bitcoin-Adresse entspricht, an die mining-Belohnungen gerichtet werden sollen. Zusätzliche Hardware-Parameter wie Frequenzeinstellungen, Spannungskonfigurationen und ASIC-Typ-Spezifikationen müssen mit der Ziel-Hardware-Plattform übereinstimmen. Das GitHub-Repository bietet vorkonfigurierte Beispiele für verschiedene Hardware-Varianten, wie die BM1368-Konfiguration für Super-Geräte und BM1366-Einstellungen für Ultra-Varianten. Spezifikationen für die Boardversion, wie z. B. die Einstellung der Portversion auf 401 für neuere Hardwareversionen, gewährleisten die Kompatibilität mit den spezifischen Eigenschaften des Zielgeräts.


### Erstellung des Web-Interface und der Kern-Firmware


Das ESP-Miner-Projekt umfasst eine hochentwickelte Webschnittstelle, die separat kompiliert werden muss, bevor der eigentliche Firmware-Erstellungsprozess beginnen kann. Diese als AxeOS-Firmware bezeichnete Webschnittstelle bietet den Benutzern eine umfassende Verwaltungsschnittstelle zur Überwachung und Steuerung ihrer mining-Geräte.


Der Erstellungsprozess für die Weboberfläche beginnt mit der Navigation zum HTTP-Server-Verzeichnis innerhalb der Haupt-Repository-Struktur, insbesondere zum Unterverzeichnis AxeOS. Dieses Verzeichnis enthält die Node.js-basierte Webanwendung, die mit dem Befehl npm install installiert werden muss. Das Build-System geht davon aus, dass Node.js ordnungsgemäß auf dem Entwicklungssystem installiert ist, da dies eine grundlegende Voraussetzung für den Kompilierungsprozess der Weboberfläche ist.


Nach der Installation der Abhängigkeiten kompiliert der npm run build-Befehl die Webinterface-Komponenten und erstellt die notwendigen Dateien, die in die ESP32-Firmware eingebettet werden. Dieser Kompilierungsprozess erzeugt optimierte Web-Assets, die die Funktionalität der Benutzeroberfläche bereitstellen und gleichzeitig eine effiziente Speichernutzung auf der eingeschränkten ESP32-Plattform gewährleisten. Der erfolgreiche Abschluss dieses Kompilierungsschritts ist wichtig, bevor mit der Hauptkompilierung der Firmware fortgefahren wird, da die ESP-Miner-Firmware diese Web-Interface-Komponenten als integrale Funktionalität enthält.


### Erstellen von Werksdateien mit eingebetteter Konfiguration


Die Erstellung von Werksdateien stellt eine fortschrittliche Bereitstellungsstrategie dar, bei der die Konfigurationseinstellungen direkt in die Firmware-Binärdatei eingebettet werden, so dass eine manuelle Konfiguration während der Einrichtung des Geräts nicht mehr erforderlich ist. Dieser Ansatz erweist sich als besonders wertvoll für groß angelegte Implementierungen oder Situationen, in denen eine konsistente Konfiguration über mehrere Geräte hinweg wichtig ist.


Der Prozess zur Erstellung der Werksdatei beginnt mit der Generierung einer binären Konfiguration aus der CSV-Konfigurationsdatei mithilfe des ESP-IDF-Tools NVS Partition Generator. Dieses Tool, das sich im ESP-IDF-Komponentenverzeichnis unter nvs-flash/nvs-partition-generator befindet, konvertiert die vom Menschen lesbare Konfiguration in ein Binärformat, das für die direkte Speicherung im Flash-Speicher geeignet ist. Das Skript nvs-partition-gen.py verarbeitet die Datei config.csv und erzeugt eine Datei config.binary, die auf den Speicheradressraum 0x6000 abzielt.


Für die abschließende Zusammenstellung der Factory-Dateien werden spezielle Merge-Skripte verwendet, die die Kern-Firmware-Binärdateien mit den Konfigurationsdaten kombinieren. Das Repository bietet mehrere Merge-Optionen, darunter ein Standard-Merge-Skript für einfache Werksdateien und ein Merge-Skript für umfassende Werksdateien, das die Konfiguration einschließt. Das merge-bin-with-config.sh-Skript erstellt Factory-Dateien, die sowohl die Firmware-Funktionalität als auch die vorkonfigurierten Einstellungen enthalten und somit ein vollständiges Bereitstellungspaket ergeben. Dieser Ansatz ermöglicht die Erstellung gerätespezifischer Werksdateien, wie z. B. Versionen, die auf Bitaxe-Ultra-Geräte mit bestimmten Board-Revisionen zugeschnitten sind, und bietet gleichzeitig die Flexibilität, generate generische Werksdateien ohne eingebettete Konfigurationen für Szenarien zu erstellen, die eine manuelle Einrichtungsflexibilität erfordern.


Mit den fertigen Werksdateien erhalten die Einsatzteams flashfertige Binärdateien, die alle erforderlichen Firmware-Komponenten und Konfigurationseinstellungen enthalten. Dadurch wird der Prozess der Gerätebereitstellung rationalisiert und es werden konsistente Betriebsparameter für alle eingesetzten mining-Geräte gewährleistet.


## Wie benutzt man den Bitaxe Web Flasher?

<chapterId>8c3e2d4c-c038-53ec-93cb-cc30a29e4394</chapterId>


:::video id=291757b9-f459-48f6-8766-56387f907859:::

Der Bitaxe Web Installer stellt einen rationalisierten Ansatz für die Firmware-Verwaltung von Bitaxe-Geräten dar und bietet den Benutzern mehrere Installationsoptionen über eine webbasierte Schnittstelle. Dieses umfassende Tool beseitigt die Komplexität, die traditionell mit Firmware-Updates und Neuinstallationen verbunden ist, und macht das Gerätemanagement für Benutzer unabhängig von deren technischen Kenntnissen zugänglich. Die richtige Verwendung dieses Installationsprogramms ist entscheidend für die Aufrechterhaltung einer optimalen Geräteleistung und die Vermeidung häufiger Fehler, die Geräte vorübergehend funktionsunfähig machen können.


### Anforderungen an den Zugriff und die Browser-Kompatibilität


Der Bitaxe Web Installer ist über die spezielle URL [https://bitaxeorg.github.io/bitaxe-web-flasher/](https://bitaxeorg.github.io/bitaxe-web-flasher/) zugänglich (die im Video vorgestellte URL ist inzwischen veraltet) und dient als zentraler Knotenpunkt für alle Firmware-Installationsaktivitäten. Der erfolgreiche Betrieb dieses webbasierten Tools erfordert jedoch die Kompatibilität des Browsers, da das Installationsprogramm auf bestimmten Webtechnologien basiert, die nicht von allen Browsern unterstützt werden. Chrome ist der primär empfohlene Browser für das Installationsprogramm und bietet volle Kompatibilität mit allen Funktionen. Andere Chromium-basierte Browser bieten zwar ähnliche Funktionen, aber beliebte Alternativen wie Brave und Firefox verfügen nicht über die erforderliche API-Web-Serienunterstützung, so dass sie mit den Kernfunktionen des Installationsprogramms nicht kompatibel sind.


Diese Browser-Beschränkung rührt daher, dass der Installateur auf die direkte serielle Kommunikation mit Bitaxe-Geräten über die Web-Schnittstelle angewiesen ist. Der serielle Webstandard API, der diese Kommunikation ermöglicht, ist ein relativ neuer Webstandard, der noch nicht von allen Browsern unterstützt wird. Benutzer, die versuchen, über nicht unterstützte Browser auf das Installationsprogramm zuzugreifen, werden auf Verbindungsfehler stoßen und können nicht mit ihren Geräten kommunizieren, was einen Wechsel zu einem kompatiblen Browser erforderlich macht, bevor sie mit der Installation fortfahren können.


### Stromanforderungen und Gerätevorbereitung


Bitaxe-Geräte haben je nach Modell und Version unterschiedliche Anforderungen an die Stromversorgung, so dass eine korrekte Energieverwaltung für eine erfolgreiche Firmware-Installation unerlässlich ist. Geräte, die mit Version 204 oder niedriger laufen, können ausschließlich mit USB-Strom betrieben werden und ziehen ausreichend Strom vom angeschlossenen Computer, um den Betrieb während des Flash-Prozesses aufrechtzuerhalten. Diese vereinfachte Stromversorgung macht diese früheren Versionen besonders geeignet für Firmware-Updates, da die Benutzer nur ein einziges USB-Kabel anschließen müssen, um den Installationsprozess zu starten.


Geräte mit der Version 205 und höher benötigen jedoch zusätzlich zur USB-Verbindung eine externe Stromquelle, was auf den geänderten Stromverbrauch und das Schaltungsdesign in neueren Hardwareversionen zurückzuführen ist. Diese Geräte können über USB allein nicht ausreichend mit Strom versorgt werden und müssen während der Firmware-Installation an ihre Standard-Netzteile angeschlossen werden. Wenn diese neueren Geräte nicht ausreichend mit Strom versorgt werden, führt dies zu Installationsfehlern und möglicherweise zu einer Beschädigung des Firmware-Aktualisierungsprozesses.


Der physische Verbindungsprozess erfordert ein bestimmtes Timing und eine bestimmte Tastenbedienung, um eine ordnungsgemäße Kommunikation zwischen dem Installationsprogramm und dem Gerät sicherzustellen. Benutzer müssen die Boot-Taste auf ihrem Bitaxe-Gerät drücken und halten, bevor sie das USB-C-Kabel an ihren Computer anschließen. Diese Sequenz versetzt das Gerät in den Bootloader-Modus und ermöglicht es dem Installationsprogramm, direkt mit dem Firmware-Speicher des Geräts zu kommunizieren. Das Anschließen des USB-Kabels vor dem Betätigen des Boot-Knopfes führt zum normalen Gerätebetrieb und nicht zum Bootloader-Modus, der für die Firmware-Installation erforderlich ist, und verhindert, dass der Installer den erforderlichen Kommunikationskanal aufbauen kann.


### Installationsoptionen und ihre Anwendungen


Der Bitaxe Web Installer bietet vier verschiedene Installationsoptionen, die jeweils für bestimmte Anwendungsfälle und Gerätekonfigurationen entwickelt wurden. Die Bitaxe Superboard Version 4.0.1 stellt die aktuellste Firmware für Super-Modell-Geräte dar, wobei Version 4.0.2 für eine zukünftige Veröffentlichung geplant ist. Diese Option umfasst sowohl die Werks- als auch die Update-Variante und bietet somit Flexibilität bei der Installation je nach Benutzeranforderungen und Gerätestatus.


Werksinstallationen sind vollständige Firmware-Ersetzungen, die den ursprünglichen Herstellungsprozess widerspiegeln, einschließlich umfassender Selbsttestverfahren, die die Gerätefunktionalität in allen Systemen überprüfen. Wenn Benutzer eine Werksinstallation wählen, führt der Installateur eine vollständige Löschung der vorhandenen Firmware und Konfigurationsdaten durch und ersetzt sie durch eine frische, saubere Installation, die mit der bei der Herstellung verwendeten identisch ist. Dieser Prozess beinhaltet einen automatischen Selbsttest, der den ordnungsgemäßen Betrieb der Hardware prüft, wobei die Benutzer ihre Geräte nach Abschluss der Installation neu starten müssen, bevor der normale Betrieb wieder aufgenommen werden kann. Werksinstallationen erweisen sich als besonders wertvoll, wenn bei Geräten anhaltende Probleme auftreten oder wenn Benutzer ihre Geräte auf die ursprünglichen Werksspezifikationen zurücksetzen möchten.


Update-Installationen bieten einen konservativeren Ansatz, bei dem die vorhandenen Konfigurationsdaten erhalten bleiben und nur die wichtigsten Firmware-Komponenten aktualisiert werden. Diese Option erweist sich als ideal für Benutzer, die ihre Geräteeinstellungen angepasst haben und ihre persönlichen Konfigurationen beibehalten und gleichzeitig von Firmware-Verbesserungen und Fehlerbehebungen profitieren möchten. Der Aktualisierungsprozess zielt nur auf die Firmware-Komponenten ab, die geändert werden müssen. Benutzerspezifische Einstellungen, WiFi-Anmeldedaten und Bitcoin-Adressen bleiben während des gesamten Installationsprozesses erhalten.


### Kritische Überlegungen zur Installation und zum Datenschutz


Die Unterscheidung zwischen Werks- und Update-Installationen hat erhebliche Auswirkungen auf die Gerätekonfiguration und die Erhaltung der Benutzerdaten. Bei der Werksinstallation wird das Gerät vollständig gelöscht, d. h. alle vom Benutzer konfigurierten Einstellungen, einschließlich WiFi-Anmeldeinformationen, Bitcoin-Adressen und personalisierte Geräteparameter, werden entfernt. Nach einer Werksinstallation müssen sich die Benutzer erneut mit dem Standard-WiFi-Netzwerk des Geräts verbinden und alle persönlichen Einstellungen von Grund auf neu konfigurieren, wodurch das Gerät im Wesentlichen so behandelt wird, als wäre es brandneu vom Hersteller.


Bei Update-Installationen muss die Option "Gerät löschen", die während des Installationsvorgangs angezeigt wird, sorgfältig beachtet werden. Das Installationsprogramm wird den Benutzer mit der Frage "Möchten Sie das Gerät vor der Installation von Bitaxe Flasher löschen?" auffordern, begleitet von einer Warnung, dass alle Daten auf dem Gerät verloren gehen. Benutzer, die Update-Installationen durchführen, müssen diese Option ablehnen, indem sie auf "Weiter" klicken, anstatt den Löschvorgang zu bestätigen. Wenn Sie die Löschoption während einer Update-Installation akzeptieren, wird die Konfigurationsdatei des Geräts gelöscht, wodurch das Gerät möglicherweise nicht mehr funktioniert, bis die richtige Konfiguration wiederhergestellt ist. Zwar wird das Gerät in diesem Fall nicht dauerhaft beschädigt, aber es entstehen unnötige Komplikationen und es sind zusätzliche Konfigurationsschritte erforderlich, um den normalen Betrieb wiederherzustellen.


Der Installationsprozess selbst läuft automatisch ab, sobald der Benutzer seine Auswahl getroffen und bestätigt hat. Das Installationsprogramm übernimmt alle technischen Aspekte der Firmware-Übertragung und -Überprüfung und liefert während des gesamten Prozesses Fortschrittsanzeigen und Statusaktualisierungen. Dank dieses automatisierten Ansatzes müssen sich die Benutzer nicht mit komplexen Firmware-Installationsverfahren auseinandersetzen, während gleichzeitig zuverlässige und konsistente Ergebnisse für verschiedene Gerätemodelle und Firmware-Versionen gewährleistet werden.


## Wie erstellt und bestellt man die Leiterplatte?

<chapterId>566f5e06-9ec9-55c0-84f6-101d6ca4c2ff</chapterId>


:::video id=9a56ad84-d9cf-4f85-ab98-301fb3101228:::

Dieses Kapitel befasst sich mit dem praktischen Prozess der Erstellung von Fertigungsdateien aus KiCad-Projekten und der Bestellung professioneller Leiterplatten bei Online-Herstellern. Am Beispiel des Bitaxe-Projekts werden wir den kompletten Arbeitsablauf von der Dateierstellung bis zur Bestellung bei einem Leiterplattenhersteller durchlaufen.


### Verständnis des PCB-Herstellungsprozesses


Der Weg von einem fertigen KiCad-Design zu einer physischen Leiterplatte umfasst mehrere kritische Schritte, die die Lücke zwischen dem digitalen Design und der physischen Fertigung schließen. Bei der Arbeit mit komplexen Projekten wie dem Bitaxe bietet der PCB-Editor in KiCad eine umfassende Ansicht Ihres Entwurfs und zeigt alle Komponenten und ihre Verbindungen durch farbige Leiterbahnen an. Die roten und blauen Linien, die Sie sehen, stellen die elektrischen Verbindungen zwischen verschiedenen integrierten Schaltungen und Komponenten auf der Platine dar. KiCads 3D-Viewer-Funktion ermöglicht es Ihnen, das Aussehen der fertig bestückten Platine zu visualisieren, was Ihnen wertvolle Einblicke in die Platzierung der Komponenten und mögliche mechanische Konflikte gibt.


Für den Herstellungsprozess sind bestimmte Dateiformate erforderlich, die von den Leiterplattenherstellern interpretiert und für die Fertigung Ihrer Leiterplatten verwendet werden können. Diese Dateien enthalten genaue Informationen über Kupferlagen, Bohrungen, die Platzierung von Bauteilen und andere Fertigungsspezifikationen. Ein Verständnis dieses Arbeitsablaufs ist unerlässlich, egal ob Sie mit dem Standard-Bitaxe-Design arbeiten oder Modifikationen vornehmen, wie z. B. das Hinzufügen von benutzerdefinierten Logos, das Ändern von Bauteilwerten oder das Anpassen des Platinenlayouts, um bestimmte Anforderungen zu erfüllen.


### Erzeugen von Gerberdateien für die Fertigung


Gerber-Dateien sind der Industriestandard für die Übermittlung von PCB-Designinformationen an Hersteller. Diese Dateien enthalten alle notwendigen Daten für die Herstellung Ihrer Leiterplatte, einschließlich Kupferlagenmuster, Lötmasken-Definitionen und Bohrlochpositionen. Um generate diese Dateien in KiCad zu erstellen, navigieren Sie zum PCB-Editor und rufen Sie die Fertigungsausgänge über das Menü Dateien auf. Die Software konfiguriert automatisch die entsprechenden Einstellungen für Standard-Fertigungsprozesse, einschließlich der richtigen Ausgabeverzeichnisstruktur, die normalerweise als "Fertigungsdateien/Gerber" organisiert ist


Beim Generierungsprozess werden mehrere Gerberdateien erstellt, die jeweils verschiedene Aspekte Ihres PCB-Designs darstellen. Diese Dateien arbeiten zusammen, um den Herstellern vollständige Fertigungsanweisungen zu liefern. Nach der Erstellung müssen diese Dateien in ein ZIP-Archiv komprimiert werden, da dies das von den meisten Leiterplattenherstellern erwartete Standardformat ist. Die ZIP-Datei enthält alle erforderlichen Fertigungsdaten und stellt sicher, dass beim Hochladen auf die Website des Herstellers keine Dateien verloren gehen oder beschädigt werden.


Es ist erwähnenswert, dass viele Open-Source-Projekte, einschließlich Bitaxe, oft vorgenerierte Fertigungsdateien in ihren Repositories enthalten. Das Wissen, wie man generate diese Dateien selbst erstellt, ist jedoch entscheidend, wenn man Designänderungen vornimmt oder mit verschiedenen Board-Versionen arbeitet. Dieses Wissen ist besonders wertvoll bei der Anpassung von Designs oder der Behebung von Fertigungsproblemen.


### Auswahl von PCB-Herstellern und Verständnis der Optionen


Im Bereich der Leiterplattenherstellung gibt es mehrere seriöse Anbieter, wobei JLCPCB und PCBWay zu den beliebtesten Anbietern sowohl für Hobby- als auch für professionelle Anwender gehören. Beide Hersteller bieten ähnliche Dienstleistungen mit wettbewerbsfähigen Preisen und zuverlässiger Qualität an, obwohl jeder von ihnen je nach Projektanforderungen spezifische Vorteile hat. JLCPCB lockt Erstanwender oft mit Sonderpreisen und benutzerfreundlichen Schnittstellen, während PCBWay verschiedene Materialoptionen oder spezielle Dienstleistungen anbietet.


Wenn Sie Ihre Gerber-Dateien auf die Website eines Herstellers hochladen, analysiert das System automatisch Ihren Entwurf und bietet verschiedene Fertigungsoptionen an. Die von diesen Plattformen bereitgestellten Standardeinstellungen sind in der Regel für die meisten Standarddesigns geeignet, und es wird im Allgemeinen empfohlen, diese Einstellungen beizubehalten, sofern Sie keine besonderen Anforderungen haben. Zu den wichtigsten Parametern gehören Leiterplattendicke, Kupfergewicht, Oberflächengüte und Mindestmengen. Die meisten Hersteller verlangen eine Mindestbestellmenge von fünf Platinen, was für Hobby-Projekte, bei denen es von Vorteil ist, Ersatzplatinen zu haben oder sie mit Freunden zu teilen, gut funktioniert.


Farboptionen sind eine der wenigen ästhetischen Möglichkeiten, die während des Herstellungsprozesses zur Verfügung stehen. Während Grün nach wie vor die traditionelle und kostengünstigste Option ist, bieten die Hersteller in der Regel Alternativen wie Blau, Rot, Gelb, Lila und Schwarz an. Die Farbwahl ist rein ästhetisch und hat keinen Einfluss auf die elektrische Leistung Ihrer Leiterplatte, obwohl einige Farben leichte Auswirkungen auf die Kosten oder längere Herstellungszeiten haben können.


### Erweiterte Fertigungsüberlegungen und Montageoptionen


Neben der grundlegenden Leiterplattenfertigung bieten moderne Hersteller zusätzliche Dienstleistungen an, die die Fertigstellung Ihres Projekts erheblich rationalisieren können. Schablonen sind eine der wertvollsten Zusatzleistungen, insbesondere für Designs mit Fine-Pitch-Komponenten wie den ASIC-Chips, die in Bitcoin mining-Projekten verwendet werden. Eine Schablone ist im Wesentlichen eine präzisionsgeschnittene Aluminiumschablone mit Öffnungen, die genau den Positionen der Lötpunkte auf Ihrer Leiterplatte entsprechen. Dieses Werkzeug ermöglicht ein konsistentes und genaues Auftragen von Lötpaste, was die Qualität der Bestückung erheblich verbessert und die Wahrscheinlichkeit von Lötfehlern verringert.


Zu den Schablonenoptionen gehören in der Regel einzelne Schablonen mit Ober- und Unterseite oder separate Schablonen für jede Seite der Platte. Für die meisten Projekte erweist sich eine kombinierte Schablone als praktischer und kostengünstiger. Die Schablonendicke wird sorgfältig berechnet, um die richtige Menge an Lotpaste für Ihre spezifischen Bauteiltypen und Padgrößen aufzubringen. Die Verwendung einer Schablone verwandelt einen mühsamen und fehleranfälligen manuellen Prozess in einen schnellen und professionellen Montageschritt.


Einige Hersteller bieten zwar Teil- oder Komplettmontageservices an, doch diese Optionen müssen bei komplexen Projekten wie dem Bitaxe sorgfältig abgewogen werden. Die Verfügbarkeit von Bauteilen, die Kosten und der pädagogische Wert der Selbstmontage spielen bei dieser Entscheidung eine Rolle. Viele spezielle Komponenten, die für Bitcoin mining-Projekte benötigt werden, sind möglicherweise nicht ohne Weiteres über Standard-Leiterplattenbestückungsdienste erhältlich, so dass die Beschaffung von Komponenten und die manuelle Montage der praktischere Ansatz sind. Künftige Folgen dieser Serie werden sich mit Strategien zur Beschaffung von Bauteilen und Montagetechniken befassen, die Ihnen helfen, Ihr Bitaxe-Projekt von der nackten Leiterplatte bis zum funktionsfähigen Gerät erfolgreich abzuschließen.


Der Fertigungs- und Montageprozess stellt eine entscheidende Brücke zwischen dem digitalen Entwurf und der physischen Umsetzung dar. Wenn Sie diese Arbeitsabläufe verstehen, können Sie die Kontrolle über Ihre Projekte übernehmen, Kosten senken und wertvolle praktische Erfahrungen mit professionellen Fertigungsprozessen sammeln. Ganz gleich, ob Sie einen einzelnen Prototyp bauen oder eine Kleinserie planen, die Beherrschung dieser Fertigkeiten eröffnet Ihnen neue Möglichkeiten, Ihre elektronischen Designs zum Leben zu erwecken.


# Optimierung der Leistung

<partId>87b8790f-b7a9-5286-a7f8-328176ef7cb5</partId>


## Benchmarking Ihrer Bitaxe

<chapterId>7259a4b1-93c1-5956-87d3-baaee58115af</chapterId>


:::video id=2491a783-9750-4ea5-a40c-1d1d611784d5:::

Das Streben nach optimaler mining-Leistung erfordert einen systematischen Ansatz für die Hardwarekonfiguration, der hashrate, Effizienz und Wärmemanagement in Einklang bringt. Die Bitaxe bieten zahlreiche Konfigurationsparameter, die sich erheblich auf die Leistung auswirken können, aber es wäre unpraktisch und zeitaufwändig, jede Kombination von Einstellungen manuell zu testen. In diesem Kapitel wird untersucht, wie automatisierte Benchmarking-Tools eingesetzt werden können, um die Leistung Ihres Bitaxe wissenschaftlich zu optimieren und gleichzeitig sichere Betriebsbedingungen aufrechtzuerhalten.


### Verstehen der Bitaxe Performance Metriken und Baseline Konfiguration


Bevor Sie sich mit Optimierungstechniken befassen, sollten Sie die wichtigsten Leistungsindikatoren kennen, die die Betriebseffizienz Ihres Bitaxe bestimmen. Zu den primären Messgrößen gehören hashrate, gemessen in Terahash pro Sekunde, Leistungseffizienz, ausgedrückt in Joule pro Terahash, ASIC-Frequenz in Megahertz und Kernspannung in Volt. Ein gut konfigurierter Bitaxe könnte etwa 1,1 Terahash mit einem Wirkungsgrad von etwa 17 Joule pro Terahash erreichen und bei 550 Megahertz mit einer gemessenen ASIC-Spannung von 1,14 Volt arbeiten. Diese Basiszahlen bieten einen Anhaltspunkt für das Verständnis der potenziellen Verbesserungen, die durch systematische Optimierung möglich sind.


Die Beziehung zwischen diesen Parametern ist komplex und voneinander abhängig. Höhere Frequenzen erhöhen in der Regel die hashrate, steigern aber auch den Stromverbrauch und die Wärmeentwicklung. In ähnlicher Weise wirken sich Spannungsanpassungen sowohl auf die Leistung als auch auf die thermischen Eigenschaften aus. Die Herausforderung besteht darin, das optimale Gleichgewicht zu finden, das entweder hashrate oder die Effizienz maximiert und gleichzeitig einen stabilen Betrieb innerhalb sicherer Temperaturgrenzen gewährleistet. Dieser Optimierungsprozess erfordert methodische Tests über mehrere Parameterkombinationen hinweg, so dass automatisierte Tools von unschätzbarem Wert sind, um optimale Ergebnisse zu erzielen.


### Die Architektur des Bitaxe Hashrate Benchmark-Tools


Das Tool [Bitaxe Hashrate Benchmark](https://github.com/mrv777/Bitaxe-Hashrate-Benchmark/) ist eine ausgeklügelte Python-basierte Lösung, die ursprünglich von WhiteCookie entwickelt und anschließend von mrv777 verbessert wurde. Dieses Open-Source-Tool, das unter der GPLv3-Lizenz vertrieben wird, automatisiert den komplexen Prozess des Testens mehrerer Konfigurationskombinationen, um die optimalen Einstellungen für Ihre spezifische Hardware zu ermitteln. Die Hauptstärke des Tools liegt in seinem systematischen Ansatz zum Testen von Parametern, bei dem die Frequenz- und Spannungseinstellungen schrittweise angepasst werden, während die Leistungsmetriken und thermischen Bedingungen kontinuierlich überwacht werden.


Der Benchmarking-Prozess dauert in der Regel 30 bis 40 Minuten, während derer das Tool methodisch verschiedene Kombinationen von ASIC-Frequenz- und Spannungseinstellungen testet. Das Tool beginnt mit konservativen Grundeinstellungen, in der Regel bei 1,15 Volt und 500 Megahertz, und erhöht dann schrittweise diese Parameter, während hashrate, Temperatur und Stabilität überwacht werden. Wichtig ist, dass das Tool dem sicheren Betrieb Vorrang vor maximaler Leistung einräumt und Einstellungen, die zu übermäßiger Wärmeentwicklung oder Instabilität führen, automatisch zurücknimmt. Dieser konservative Ansatz stellt sicher, dass der Optimierungsprozess die Langlebigkeit und Zuverlässigkeit der Hardware nicht beeinträchtigt.


### Installations- und Einrichtungsanforderungen


Die Implementierung des Bitaxe Hashrate Benchmark-Tools erfordert mehrere vorausgesetzte Softwarekomponenten auf Ihrem lokalen Computer. Zu den Hauptanforderungen gehören Python für die Ausführung der Benchmarking-Skripte, Git für die Repository-Verwaltung und optional Visual Studio Code für erweiterte Funktionen der Entwicklungsumgebung. Das Tool kann zwar über die Befehlszeilenschnittstelle bedient werden, aber die Verwendung einer integrierten Entwicklungsumgebung wie VS Code bietet einen besseren Einblick in den Benchmarking-Prozess und die Ergebnisanalyse.


Der Installationsprozess folgt den üblichen Python-Entwicklungspraktiken und beginnt mit dem Klonen des Repositorys von GitHub auf Ihren lokalen Rechner. Sobald das Repository heruntergeladen ist, müssen Sie eine virtuelle Umgebung erstellen, um die Abhängigkeiten des Tools von der Python-Installation Ihres Systems zu isolieren. Diese Isolierung verhindert mögliche Konflikte mit anderen Python-Anwendungen und gewährleistet einen konsistenten Betrieb. Nachdem Sie die virtuelle Umgebung aktiviert haben, installieren Sie die erforderlichen Abhängigkeiten mithilfe der mitgelieferten Anforderungsdatei, die automatisch alle notwendigen Bibliotheken und Module für den ordnungsgemäßen Betrieb des Tools konfiguriert.


### Durchführung von Benchmarks und Interpretation der Ergebnisse


Um den Benchmark auszuführen, muss ein einziger Python-Befehl ausgeführt werden, der die IP-Adresse Ihres Bitaxe als Parameter enthält. Das Tool verbindet sich automatisch mit der Webschnittstelle Ihres Miners und beginnt mit dem systematischen Testprozess. Während der Ausführung liefert das Tool detaillierte Protokollinformationen, die die aktuelle Testiteration, die angelegten Spannungs- und Frequenzeinstellungen, die resultierende hashrate, die Eingangsspannung, die Temperaturmesswerte und die thermischen Daten von kritischen Komponenten wie dem Abwärtswandler anzeigen. Dieses Echtzeit-Feedback ermöglicht es Ihnen, den Fortschritt des Benchmarking zu überwachen und zu verstehen, wie verschiedene Einstellungen die Leistung Ihres Miners beeinflussen.


Das intelligente Wärmemanagement des Geräts macht sich bemerkbar, wenn sich die Temperaturen dem Sicherheitsgrenzwert von 66 Grad Celsius nähern. Anstatt die sicheren Betriebsgrenzen zu überschreiten, reduziert der Benchmark automatisch die Einstellungen, um die thermische Stabilität zu erhalten. Dieser konservative Ansatz stellt sicher, dass der Optimierungsprozess der langfristigen Zuverlässigkeit der Hardware Vorrang vor kurzfristigen Leistungssteigerungen einräumt. Nach Abschluss generiert das Tool umfassende Ergebnisse im JSON-Format, die eine Rangliste der fünf besten Konfigurationen für maximale hashrate und optimale Effizienz enthalten. Diese Ergebnisse bieten eine klare Anleitung für die Auswahl der Konfiguration, die Ihren betrieblichen Prioritäten am besten entspricht, unabhängig davon, ob der Schwerpunkt auf maximaler Leistung oder Energieeffizienz liegt.


Das Benchmarking-Tool bietet auch Anpassungsoptionen für fortgeschrittene Benutzer, die die Testparameter ändern möchten. Mit Hilfe von Befehlszeilenargumenten können Sie benutzerdefinierte Startspannungen und -frequenzen angeben, die eine gezieltere Optimierung für bestimmte Anwendungsfälle ermöglichen. Wenn Sie beispielsweise bereits wissen, dass Ihre Hardware bei höheren Frequenzen gut funktioniert, können Sie den Benchmark mit höheren Einstellungen starten, anstatt mit den konservativen Standardwerten zu beginnen. Diese Flexibilität macht das Tool sowohl für Anfänger, die eine automatische Optimierung anstreben, als auch für erfahrene Miner, die eine Feinabstimmung bestimmter Leistungsmerkmale vornehmen möchten, wertvoll.


## Übertakten Sie Ihre Bitaxe

<chapterId>6b48c0c6-51c3-51a3-b317-850a374ae61e</chapterId>


:::video id=46c7a442-cd72-477c-8c91-b2c489ada1e6:::

Die Übertaktung eines Bitaxe-Gerätes erfordert eine sorgfältige Berücksichtigung sowohl der Hardware-Einschränkungen als auch der Kühlungsanforderungen. Während viele Benutzer es vorziehen, ihre Geräte für einen leiseren Betrieb zu untertakten, ist das Verständnis der richtigen Übertaktungstechniken für diejenigen, die maximale Leistung ohne Beschädigung ihrer Hardware suchen, unerlässlich. Der Prozess beinhaltet die Erhöhung der Frequenz und möglicherweise die Anpassung der Spannungseinstellungen über die Werksspezifikationen hinaus, was die Wärmeentwicklung und die Belastung der Komponenten erhöht.


Die Grundlage für eine erfolgreiche Übertaktung liegt in einer angemessenen Kühlungsinfrastruktur. Bevor Sie irgendwelche Frequenzänderungen vornehmen, müssen Sie sicherstellen, dass Ihr Bitaxe über eine angemessene Wärmeabfuhr verfügt. Ein Bitaxe Gamma mit einem hochwertigen Kühlkörper und Lüfter bietet das notwendige Wärmemanagement für eine sichere Übertaktung. Geräte mit kleinen Kühlkörpern und unzureichenden Lüftern sollten nicht übertaktet werden, da eine schlechte Kühlleistung zu thermischem Throttling und potenziellen Hardwareschäden führen wird. Die Beziehung zwischen Wärme und der Langlebigkeit von Komponenten ist von entscheidender Bedeutung - übermäßige Wärme erzeugt Stress, der elektronische Komponenten mit der Zeit verschlechtert und die Lebensdauer Ihres Geräts erheblich verkürzt.


### Strategische Platzierung des Kühlkörpers


Das kritischste Bauteil, das zusätzliche Kühlung benötigt, ist der Abwärtswandler, ein kleines schwarzes Bauteil, das sich auf der Rückseite des Bitaxe in der Nähe der großen Spule befindet. Dieses Bauteil wandelt die eingehende 5-V-Stromversorgung in die für den ASIC-Chip geeignete Spannung um, in der Regel etwa 1,2 V. Der Abwärtswandler, oft auch als TPS bezeichnet, erzeugt während des Betriebs erhebliche Wärme und stellt einen thermischen Engpass dar, der das Übertaktungspotenzial einschränkt. Die Installation eines kleinen, selbstklebenden Kühlkörpers auf dieser Komponente ermöglicht nicht nur eine höhere Übertaktungsleistung, sondern verbessert auch die Gesamteffizienz durch die Reduzierung der Wärmeverluste.


Die zusätzliche Platzierung von Kühlkörpern kann anderen Hochstrombereichen der Platine zugute kommen. Die Schaltung zur Spannungsregulierung ist einer erheblichen elektrischen Belastung ausgesetzt, da der Strom vom Eingangsbereich durch verschiedene Leiterbahnen auf der Platine nach unten fließt, um den ASIC-Chip zu versorgen. Viele erfahrene Übertakter installieren Kühlkörper auf der Vorderseite des Bitaxe in diesen Hochstrombereichen, um die Wärmeableitung weiter zu verbessern. Diese zusätzlichen Kühlmaßnahmen sind zwar bei moderater Übertaktung nicht unbedingt erforderlich, werden aber wichtig, wenn die Frequenzen auf ein extremes Niveau angehoben werden.


### Überlegungen und Einschränkungen des Kühlsystems


Der ESP32-Controller, der als silbernes Bauteil auf der Platine sichtbar ist, benötigt normalerweise keine zusätzliche Kühlung. Dieses Bauteil erzeugt selbst nur minimale Wärme und wird nur durch die Wärmeübertragung der umliegenden Komponenten warm. Die Installation von Kühlkörpern in der Nähe des ESP32 kann möglicherweise die benachbarte Wi-Fi-Antenne stören, was die drahtlose Verbindung und die Signalqualität verschlechtert. Konzentrieren Sie sich bei der Kühlung auf die Komponenten zur Leistungsregulierung und den ASIC-Bereich und nicht auf den Steuerschaltkreis.


Konfigurationen mit zwei Lüftern bieten sowohl Möglichkeiten als auch Einschränkungen. Während das Hinzufügen eines zweiten Lüfters, der Luft über die Rückseite des Bitaxe bläst, die Kühlleistung verbessern kann, kann die Firmware des Geräts nur einen Lüfter richtig steuern. Der Bitaxe hat zwei Lüfteranschlüsse, aber nur eine Lüftersteuerung, was bedeutet, dass der Anschluss von zwei Lüftern die Firmware verwirren wird, da sie widersprüchliche Drehzahlsignale erhält. Diese Konfiguration funktioniert zwar, kann aber zu unvorhersehbarem Verhalten der Lüftersteuerung führen.


### Grundlegende Leistungsbewertung


Bevor Sie Änderungen an der Übertaktung vornehmen, ermitteln Sie die Grunddaten der Leistung, indem Sie Ihr Bitaxe mehrere Stunden lang mit den Standardeinstellungen betreiben. Überwachen Sie die Temperatur des ASIC, die Temperatur des Spannungsreglers und die prozentuale Lüftergeschwindigkeit über das Webinterface. Optimale Betriebstemperaturen sollten das ASIC unter 60 °C und den Spannungsregler unter 60 °C unter normalen Bedingungen halten. Wenn Ihr Gerät bei den Standardeinstellungen bereits über 65 °C beim ASIC oder 70-80 °C beim Spannungsregler arbeitet, ist zusätzliche Kühlungshardware erforderlich, bevor Sie mit der Übertaktung fortfahren.


Der systematische Ansatz zur Frequenzerhöhung besteht aus schrittweisen Schritten unter Verwendung der vordefinierten Frequenzoptionen im Einstellungsmenü. Beginnen Sie mit der Auswahl des nächsten verfügbaren Frequenzschritts über Ihrer aktuellen Einstellung, während Sie die Standard-Kernspannung beibehalten. Dieser konservative Ansatz ermöglicht es Ihnen, die thermischen und stabilitätsbezogenen Auswirkungen zu bewerten, bevor Sie weitere Änderungen vornehmen. Lassen Sie das Gerät mindestens 30 Minuten bis eine Stunde lang mit jeder neuen Frequenzeinstellung arbeiten und beobachten Sie während des gesamten Bewertungszeitraums die Temperaturentwicklung und die Stabilität der Hash-Rate.


### Erweiterte benutzerdefinierte Konfiguration


Der Zugriff auf benutzerdefinierte Frequenz- und Spannungseinstellungen erfordert die Aktivierung der erweiterten Übertaktungsschnittstelle durch Anhängen von "?OC" an die URL der Webschnittstelle des Geräts. Dadurch werden manuelle Eingabefelder für eine präzise Frequenz- und Spannungssteuerung freigeschaltet, begleitet von entsprechenden Warnungen über die Risiken des Betriebs außerhalb der vorgesehenen Parameter. Die benutzerdefinierte Schnittstelle ermöglicht eine Feinabstimmung über die Standardfrequenzschritte hinaus, so dass erfahrene Benutzer die Leistung für ihre spezifischen Kühlkonfigurationen optimieren können.


Bei der Verwendung benutzerdefinierter Einstellungen sollten Sie konservative Schrittgrößen von 10-15 MHz pro Anpassungsschritt beibehalten. Dieser methodische Ansatz verhindert plötzliche Wärmespitzen und ermöglicht eine ordnungsgemäße Stabilitätsprüfung bei jeder Frequenzstufe. Einige erfahrene Benutzer erreichen Frequenzen um 700 MHz mit Kernspannungen von 1,175 V oder ähnlichen Werten, aber diese extremen Einstellungen erfordern umfangreiche Kühlungsmodifikationen und eine sorgfältige Überwachung. Der Spannungsregler kann bei Temperaturen von bis zu 100 °C arbeiten, ohne sofort Schaden zu nehmen, aber höhere Temperaturen verringern die Effizienz und langfristige Zuverlässigkeit. Erfolgreiches Übertakten erfordert Geduld, systematisches Testen und kontinuierliche Überwachung, um stabile Leistungsverbesserungen bei gleichzeitiger Wahrung der Hardware-Integrität zu erzielen.


# Letzter Abschnitt

<partId>33367393-17a7-58d4-8359-79fffc6221fb</partId>


## Bewerten Sie diesen Kurs

<chapterId>785f8b92-c8a6-5a65-aa39-e9753a7edf51</chapterId>

<isCourseReview>true</isCourseReview>

## Schlussfolgerung

<chapterId>758baee6-2404-56fb-b534-6a39e441ae29</chapterId>

<isCourseConclusion>true</isCourseConclusion>