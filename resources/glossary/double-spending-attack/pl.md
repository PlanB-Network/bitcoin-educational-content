---
term: PODWÓJNE WYDATKI (ATAK)
---

Atak, w którym złośliwy użytkownik próbuje użyć tego samego UTXO (*Unspent Transaction Output*) więcej niż jeden raz, aby wzbogacić się kosztem stron zaangażowanych w transakcje. Zasadniczo, gdy transakcja zostanie potwierdzona w bloku i dodana do Blockchain, użycie tych bitcoinów jest trwale rejestrowane, zapobiegając dalszemu wydawaniu tych samych bitcoinów. Zapobieganie podwójnym wydatkom jest nawet podstawową użytecznością Blockchain.


W kontekście ataku double spending atakujący najpierw dokonuje legalnej transakcji ze sprzedawcą, a następnie tworzy drugą konkurencyjną transakcję, wydając te same monety, albo wysyłając je z powrotem do siebie w celu odzyskania kwoty, albo wykorzystując je do zakupu innego towaru lub usługi od innego sprzedawcy.


Istnieją dwa główne scenariusze, które mogą umożliwić ten atak. Pierwszy i najprostszy dla atakującego polega na wykonaniu oszukańczej transakcji, zanim legalna transakcja zostanie uwzględniona w bloku. Aby upewnić się, że oszukańcza transakcja zostanie potwierdzona jako pierwsza, atakujący wiąże z nią znacznie wyższe opłaty transakcyjne niż z legalną transakcją. Jest to rodzaj oszukańczego RBF. Ten scenariusz jest możliwy tylko wtedy, gdy sprzedawca zgodzi się sfinalizować sprzedaż w trybie "zeroconf", czyli bez żadnych potwierdzeń transakcji płatniczej. Dlatego zdecydowanie zaleca się odczekanie kilku potwierdzeń przed uznaniem transakcji za niezmienną. Drugim scenariuszem, znacznie bardziej złożonym, jest atak 51%. Jeśli atakujący kontroluje znaczną część mocy obliczeniowej sieci, może wydobyć łańcuch konkurencyjny do tego zawierającego legalną transakcję, ale zawierający jego oszukańczą transakcję. Gdy sprzedawca zaakceptuje sprzedaż, a atakującemu uda się utworzyć dłuższy łańcuch (z większą ilością zgromadzonej pracy) niż legalny łańcuch, może on następnie rozgłosić swój fałszywy łańcuch, który zostanie rozpoznany przez węzły sieci jako prawidłowy.