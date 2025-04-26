---
term: MINISCRIPT
---

Framework designed to provide a framework for programming scripts securely on Bitcoin. The native language of Bitcoin is called script. It is quite complex to use in practice, especially for sophisticated and customized applications. Above all, it is very difficult to verify a script's limitations. Miniscript uses a subset of Bitcoin scripts to simplify their creation, analysis, and verification. Each miniscript is equivalent 1 for 1 with a native script. A user-friendly policy language is used, which is then compiled into miniscript, to finally correspond to a native script.

![](../../dictionnaire/assets/30.webp)

Miniscript thus allows developers to build sophisticated scripts in a safer and more reliable way. The essential properties of Miniscript are as follows:
* It allows for static analysis of the script, including the spending conditions it permits and its cost in terms of resources;
* It enables the creation of scripts that adhere to the consensus;
* It allows for the analysis of whether or not the different spending paths comply with the standard rules of the nodes;
* It establishes a general standard, understandable and composable, for all wallet software and hardware.

The Miniscript project was launched in 2018 by Peter Wuille, Andrew Poelstra, and Sanket Kanjalkar, through the company Blockstream. Miniscript was added to the Bitcoin Core wallet in watch-only mode in December 2022 with version 24.0, and then fully in May 2023 with version 25.0.