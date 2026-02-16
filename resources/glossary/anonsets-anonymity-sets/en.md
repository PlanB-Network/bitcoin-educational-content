---
term: Anonsets (anonymity sets)
definition: Indicators measuring the degree of privacy of a UTXO by counting the number of indistinguishable UTXOs in a set, typically after a coinjoin.
---
Anonsets serve as indicators to assess the degree of privacy of a particular UTXO. More specifically, they measure the number of indistinguishable UTXOs within the set that includes the coin under study. Since a group of identical UTXOs is required, anonsets are generally calculated within a cycle of coinjoins. They make it possible, where applicable, to assess the quality of coinjoins. A large anonset implies a higher level of anonymity, as it becomes difficult to distinguish a specific UTXO within the set.

Two types of anonsets exist: the forward anonset (forward-looking metrics); and the backward anonset (backward-looking metrics). The term "*score*" is also sometimes used to refer to anonsets.

The first indicates the size of the group within which the studied output UTXO is hidden, given the input UTXO. This indicator makes it possible to measure the robustness of the coin’s privacy against a past-to-present analysis (input to output). The second indicates the number of possible sources for a given coin, given the output UTXO. This indicator makes it possible to measure the robustness of the coin’s privacy against a present-to-past analysis (output to input).









