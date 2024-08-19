---
term: MINISCRIPT
---

Framework, das darauf ausgelegt ist, ein Framework für das sichere Programmieren von Skripten auf Bitcoin bereitzustellen. Die native Sprache von Bitcoin wird als Skript bezeichnet. Sie ist in der Praxis besonders für anspruchsvolle und maßgeschneiderte Anwendungen recht komplex in der Nutzung. Vor allem ist es sehr schwierig, die Grenzen eines Skripts zu verifizieren. Miniscript verwendet eine Teilmenge von Bitcoin-Skripten, um deren Erstellung, Analyse und Verifizierung zu vereinfachen. Jedes Miniscript entspricht 1:1 einem nativen Skript. Es wird eine benutzerfreundliche Richtliniensprache verwendet, die dann in Miniscript kompiliert wird, um schließlich einem nativen Skript zu entsprechen.

![](../../dictionnaire/assets/30.png)

Miniscript ermöglicht es Entwicklern somit, anspruchsvolle Skripte auf eine sicherere und zuverlässigere Weise zu erstellen. Die wesentlichen Eigenschaften von Miniscript sind wie folgt:
* Es ermöglicht die statische Analyse des Skripts, einschließlich der Bedingungen für das Ausgeben und seiner Kosten in Bezug auf Ressourcen;
* Es ermöglicht die Erstellung von Skripten, die dem Konsens entsprechen;
* Es ermöglicht die Analyse, ob die verschiedenen Ausgabepfade den Standardregeln der Knoten entsprechen oder nicht;
* Es etabliert einen allgemeinen Standard, der verständlich und komponierbar ist, für alle Wallet-Software und -Hardware.

Das Miniscript-Projekt wurde 2018 von Peter Wuille, Andrew Poelstra und Sanket Kanjalkar durch das Unternehmen Blockstream ins Leben gerufen. Miniscript wurde im Dezember 2022 mit Version 24.0 im Nur-Lese-Modus in das Bitcoin Core Wallet aufgenommen und dann vollständig im Mai 2023 mit Version 25.0.