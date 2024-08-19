---
term: SCHWIERIGKEIT
---

Ein anpassbarer Parameter, der die Komplexität des erforderlichen Arbeitsnachweises (Proof of Work) bestimmt, um einen neuen Block zur Blockchain hinzuzufügen und die damit verbundene Belohnung zu verdienen. Diese Schwierigkeit wird durch das Schwierigkeitsziel dargestellt, einen 256-Bit-Wert, der das obere Limit festlegt, das der Hash des Blockheaders erfüllen muss, um als gültig betrachtet zu werden. Das Ziel ist, dass der Hash, erreicht durch eine doppelte Ausführung von SHA256 (SHA256d), kleiner oder gleich diesem Ziel ist. Um diesen Hash zu erreichen, manipulieren Miner den `nonce` im Blockheader. Die Schwierigkeit passt sich alle 2016 Blöcke oder ungefähr alle zwei Wochen an, um die durchschnittliche Blockerstellungszeit bei etwa 10 Minuten zu halten.