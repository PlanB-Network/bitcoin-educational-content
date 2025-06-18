---
term: KONSOLIDACJA
---

Określona transakcja, w której wiele małych UTXO jest łączonych w jedno wejście w celu utworzenia pojedynczego, większego UTXO jako wyjścia. Ta operacja jest transakcją wykonywaną na własnym Wallet. Celem konsolidacji jest wykorzystanie okresów, w których opłaty w sieci Bitcoin są niskie, aby połączyć kilka małych UTXO w jedno o większej wartości. W ten sposób przewiduje się obowiązkowe wydatki w przypadku wzrostu opłat, co pozwala zaoszczędzić na przyszłych opłatach transakcyjnych.


Rzeczywiście, transakcje z wieloma danymi wejściowymi są cięższe, a co za tym idzie, droższe. Oprócz oszczędności na opłatach transakcyjnych, konsolidacja jest również formą długoterminowego planowania. Jeśli Wallet zawiera bardzo małe UTXO, mogą one stać się bezużyteczne, jeśli sieć Bitcoin wejdzie w przedłużający się okres wysokich opłat. Na przykład, jeśli musisz wydać UTXO w wysokości 10 000 Sats, ale minimalne opłaty Mining wynoszą 15 000 Sats, wydatek ten przekroczyłby wartość samego UTXO. Te małe UTXO stają się wtedy ekonomicznie nieracjonalne w użyciu i pozostają bezużyteczne tak długo, jak opłaty nie spadają. Te UTXO są powszechnie określane jako "Dust" Regularna konsolidacja małych UTXO zmniejsza ryzyko związane ze wzrostem opłat.


Należy jednak zauważyć, że transakcje konsolidacyjne są rozpoznawalne podczas analizy łańcucha. Taka transakcja wskazuje na Common Input Ownership Heuristic (CIOH), co oznacza, że dane wejściowe transakcji konsolidacyjnej są własnością jednego podmiotu. Może to mieć wpływ na prywatność użytkownika.


![](../../dictionnaire/assets/7.webp)