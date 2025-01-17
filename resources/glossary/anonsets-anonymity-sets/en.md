---
term: ANONSETS (ANONYMITY SETS)
---

Anonsets serve as indicators to assess the privacy level of a particular UTXO. More specifically, they measure the number of indistinguishable UTXOs within the set that includes the coin under study. Since a group of identical UTXOs is required, anonsets are generally calculated within a cycle of coinjoins. They allow, where appropriate, to judge the quality of the coinjoins. A large anonset means an increased level of anonymity, as it becomes difficult to distinguish a specific UTXO within the set. There are two types of anonsets:
* The prospective anonymity set;
* The retrospective anonymity set.

The first indicates the size of the group among which the studied UTXO is hidden, knowing the UTXO at input. This indicator allows measuring the resistance of the coin's privacy against an analysis from past to present (input to output). In English, the name of this indicator is “*forward anonset*,” or “*forward-looking metrics*.”

![](../../dictionnaire/assets/39.webp)

The second indicates the number of possible sources for a given coin, knowing the UTXO at output. This indicator allows measuring the resistance of the coin's privacy against an analysis from present to past (output to input). In English, the name of this indicator is “*backward anonset*,” or “*backward-looking metrics*.”

![](../../dictionnaire/assets/40.webp)

> ► *In French, it is generally accepted to use the term “anonset.” However, it could be translated as “ensemble d'anonymat” or “potentiel d'anonymat.” In both English and French, the term “score” is also sometimes used to refer to anonsets (prospective score and retrospective score).*