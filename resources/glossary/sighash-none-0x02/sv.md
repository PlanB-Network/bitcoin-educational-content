---
term: SIGHASH_NONE (0X02)
definition: SigHash-flagga där signaturen täcker alla inputs men ingen av transaktionens outputs.
---

Typ av SigHash-flagga som används i Bitcoin-transaktionssignaturer för att ange att signaturen gäller för alla inmatningar i transaktionen, men inte för någon av dess utmatningar. Användningen av `SIGHASH_NONE` innebär att undertecknaren endast förbinder sig till ingångarna och låter utgångarna förbli obestämda eller modifierbara efter undertecknandet. Denna typ av signatur är användbar i fall där undertecknaren vill bemyndiga andra parter att besluta hur bitcoins ska distribueras i transaktionen.