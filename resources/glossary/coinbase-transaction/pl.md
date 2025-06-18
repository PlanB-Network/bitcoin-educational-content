---
term: COINBASE (TRANSAKCJA)
---

Coinbase Transaction jest specjalną i unikalną transakcją zawartą w każdym bloku Bitcoin Blockchain. Reprezentuje pierwszą transakcję bloku i jest tworzona przez Miner, który pomyślnie znalazł nagłówek potwierdzający Proof of Work (*Proof-of-Work*), czyli mniejszy lub równy celowi.


Coinbase Transaction służy przede wszystkim dwóm celom: przyznaniu Block reward do Miner i dodaniu nowych jednostek bitcoinów do pieniądza obiegowego Supply. Block reward, który jest zachętą ekonomiczną dla górników do angażowania się w Proof of Work, obejmuje skumulowane opłaty za transakcje zawarte w bloku oraz określoną ilość nowo utworzonych bitcoinów ex-nihilo (dotacja blokowa). Kwota ta, początkowo ustalona na 50 bitcoinów na blok w 2009 roku, jest zmniejszana o połowę co 210 000 bloków (mniej więcej co 4 lata) podczas wydarzenia zwanego "Halving"


Coinbase Transaction różni się od zwykłych transakcji na kilka sposobów. Po pierwsze, nie ma wejścia, co oznacza, że żadne istniejące wyjście transakcji (UTXO) nie jest przez nią wykorzystywane. Następnie skrypt podpisu (`scriptSig`) dla Coinbase Transaction zazwyczaj zawiera dowolne pole umożliwiające włączenie dodatkowych danych, takich jak niestandardowe wiadomości lub informacje o wersji oprogramowania Mining. Wreszcie, bitcoiny wygenerowane przez Coinbase Transaction podlegają okresowi zapadalności wynoszącemu 100 bloków (101 potwierdzeń), zanim będą mogły zostać wydane, aby zapobiec potencjalnemu wydaniu nieistniejących bitcoinów w przypadku reorganizacji łańcucha.


> nie istnieje tłumaczenie "Coinbase" na język francuski. Dlatego akceptowane jest używanie tego terminu bezpośrednio