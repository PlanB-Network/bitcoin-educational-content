---
term: MINISCRIPT

---
Framework für die sichere Programmierung von Skripten auf Bitcoin. Die native Sprache von Bitcoin heißt Script. Sie ist in der Praxis recht kompliziert zu verwenden, insbesondere für anspruchsvolle und angepasste Anwendungen. Vor allem ist es sehr schwierig, die Grenzen eines Skripts zu verifizieren. Miniscript verwendet eine Teilmenge von Bitcoin-Skripten, um deren Erstellung, Analyse und Überprüfung zu vereinfachen. Jedes Miniscript ist 1:1 mit einem nativen Skript gleichwertig. Es wird eine benutzerfreundliche Policy-Sprache verwendet, die dann in Miniscript kompiliert wird, um schließlich einem nativen Skript zu entsprechen.

![](../../dictionnaire/assets/30.webp)

Miniscript ermöglicht es Entwicklern, anspruchsvolle Skripte auf eine sicherere und zuverlässigere Weise zu erstellen. Die wesentlichen Eigenschaften von Miniscript sind wie folgt:


- Es ermöglicht eine statische Analyse des Skripts, einschließlich der zulässigen Ausgabenbedingungen und der Kosten für die Ressourcen;
- Sie ermöglicht die Erstellung von Skripten, die sich an den Konsens halten;
- Es ermöglicht die Analyse, ob die verschiedenen Ausgabenwege den Standardregeln der Knotenpunkte entsprechen oder nicht;
- Es wird ein allgemeiner, verständlicher und kompatibler Standard für alle Wallet-Software und -Hardware festgelegt.

Das Miniscript-Projekt wurde 2018 von Peter Wuille, Andrew Poelstra und Sanket Kanjalkar über das Unternehmen Blockstream gestartet. Miniscript wurde der Bitcoin Core Wallet im Dezember 2022 mit Version 24.0 im Watch-Only-Modus hinzugefügt und dann im Mai 2023 mit Version 25.0 vollständig.