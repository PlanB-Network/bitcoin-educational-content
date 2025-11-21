---
term: SIGHASH_ALL/SIGHASH_ACP
---

Typ flagi SigHash (`0x81`) w połączeniu z modyfikatorem `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) używanym w podpisach transakcji Bitcoin. Ta kombinacja określa, że podpis ma zastosowanie do wszystkich wyjść i tylko do określonego wejścia transakcji. `SIGHASH_ALL | SIGHASH_ANYONECANPAY` pozwala innym uczestnikom na dodanie dodatkowych wejść do transakcji po jej początkowym podpisaniu. Jest to szczególnie przydatne w scenariuszach współpracy, takich jak transakcje crowdfundingowe, w których różni uczestnicy mogą dodawać własne dane wejściowe, zachowując integralność danych wyjściowych zatwierdzonych przez początkowego sygnatariusza.