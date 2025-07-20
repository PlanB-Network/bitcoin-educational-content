---
term: SIGHASH_SINGLE/SIGHASH_ACP
---

Typ flagi SigHash (`0x83`) w połączeniu z modyfikatorem `SIGHASH_ANYONECANPAY` (`SIGHASH_ACP`) używanym w podpisach transakcji Bitcoin. Ta kombinacja określa, że podpis dotyczy tylko określonego pojedynczego wejścia i tylko wyjścia o tym samym indeksie co to wejście. Inne wejścia i wyjścia mogą być dodawane lub modyfikowane przez inne strony. Ta konfiguracja jest przydatna w przypadku transakcji opartych na współpracy, w których uczestnicy mogą dodawać własne dane wejściowe w celu sfinansowania określonego wyjścia.