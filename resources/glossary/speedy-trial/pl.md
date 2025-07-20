---
term: SZYBKA PRÓBA
---

Metoda aktywacji Soft Fork początkowo opracowana dla Taproot na początku 2021 roku przez Davida A. Hardinga w oparciu o pomysł Russella O'Connora. Jej zasadą jest użycie metody BIP8 z parametrem `LOT` ustawionym na `false`, przy jednoczesnym skróceniu okresu aktywacji do zaledwie 3 miesięcy. Ten skrócony okres głosowania pozwala na szybką weryfikację zatwierdzenia Miner. Jeśli wymagany próg zatwierdzenia zostanie osiągnięty w jednym z okresów, Soft Fork zostanie zablokowany. Zostanie on aktywowany kilka miesięcy później, dając górnikom niezbędny czas na aktualizację oprogramowania.


Sukces tej metody dla Taproot, która cieszyła się szerokim konsensusem w społeczności Bitcoin, nie gwarantuje jednak jej skuteczności dla wszystkich aktualizacji. Chociaż metoda Speedy Trial pozwala na szybszą aktywację, niektórzy deweloperzy wyrażają obawy co do jej przyszłego zastosowania. Obawiają się oni, że może ona prowadzić do zbyt szybkiej sukcesji forków Soft, co mogłoby potencjalnie zagrozić stabilności i bezpieczeństwu protokołu Bitcoin. W porównaniu do BIP8 z parametrem `LOT=true`, metoda Speedy Trial jest znacznie mniej groźna dla górników. Automatycznie nie jest planowana aktywacja UASF. Ta metoda aktywacji nie została jeszcze sformalizowana w ramach BIP.


> termin "przyspieszony proces" został zapożyczony z terminologii prawniczej oznaczającej "przyspieszony proces" Odnosi się to do faktu, że propozycja ulepszeń jest szybko przedstawiana przed sądem górniczym w celu ustalenia ich intencji. Ogólnie przyjęte jest używanie angielskiego terminu bezpośrednio w języku francuskim