---
term: MTP (median time past)
definition: Medianen av tidsstämplarna för de senaste 11 blocken, som fungerar som tidsreferens för nätverket.
---

Detta koncept används i Bitcoin-protokollet för att bestämma en marginal på nätverkets konsensus Timestamp. MTP definieras som medianen av tidsstämplarna för de senaste 11 blocken. Användningen av denna indikator hjälper till att undvika meningsskiljaktigheter mellan noder om den exakta tiden vid avvikelser. MTP användes ursprungligen för att verifiera giltigheten hos blockens tidsstämplar mot det förflutna. Sedan BIP113 har den också använts som referens för nätverkstiden för att verifiera giltigheten av tidslåsningstransaktioner (`nLockTime`, `OP_CHECKLOCKTIMEVERIFY`, `nSequence` och `OP_CHECKSEQUENCEVERIFY`).