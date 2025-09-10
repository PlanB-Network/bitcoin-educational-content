---
term: ANONSETS (ANONYMITY SETS)
---

Anonsets are indicators used to assess the privacy level of a specific UTXO. More precisely, they measure how many indistinguishable UTXOs exist within the set that includes the coin under study. Since a group of identical UTXOs is required, anonsets are generally calculated within a coinjoins round. They are helpful in evaluating the quality of a CoinJoin, with larger anonymity sets indicating greater anonymity, making it harder to trace or isolate a specific UTXO within the group. There are two types of anonsets:
* Forward Anonset
* Backward Anonset

The first indicates the size of the group among which the analyzed output UTXO is hidden, given the input UTXO. It evaluates the coin's privacy against analysis that moves from past to present (input → output). In English, the name of this indicator is “*forward anonset*,” or “*forward-looking metrics*.”

![](../../dictionnaire/assets/39.webp)

The second indicates the number of possible sources for a given coin, given the output UTXO. It assesses privacy against analysis that moves from present to past (output → input). In English, the name of this indicator is “*backward anonset*,” or “*backward-looking metrics*.”

![](../../dictionnaire/assets/40.webp)

> ► *In French, it is generally accepted to use the term “anonset.” However, it could be translated as “ensemble d'anonymat” or “potentiel d'anonymat.” In both English and French, the term “score” is also sometimes used to refer to anonsets (prospective score and retrospective score).*