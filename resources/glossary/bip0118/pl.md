---
term: BIP0118
definition: Propozycja ANYPREVOUT wprowadzająca nowe SigHash Flags umożliwiające ponowne użycie podpisów między transakcjami, przydatna dla Eltoo.
---

Propozycja ulepszenia Bitcoin miała na celu wprowadzenie dwóch nowych modyfikatorów SigHash Flag: `SIGHASH_ANYPREVOUT` i `SIGHASH_ANYPREVOUTANYSCRIPT`. Funkcje te rozszerzają możliwości transakcji Bitcoin, szczególnie w zakresie inteligentnych kontraktów i rozwiązań nakładkowych, takich jak Lightning Network. BIP118 umożliwiłby w szczególności korzystanie z Eltoo. Główną zaletą `SIGHASH_ANYPREVOUT` jest umożliwienie ponownego wykorzystania podpisów w wielu transakcjach, co zapewnia większą elastyczność. W szczególności te SigHashes pozwalają na podpis, który nie obejmuje żadnego z wejść transakcji.