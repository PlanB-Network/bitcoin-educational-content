---
term: BIP0085

definition: Phương pháp cho phép tạo ra nhiều cụm từ ghi nhớ cho các ví khác nhau từ một hạt giống chính (master seed) duy nhất.
---
Solution to unify the derivation of different Bitcoin wallets using a single master seed for all. This proposal allows for the derivation of entropy from root information to generate multiple mnemonic phrases for multiple wallets, without compromising security. The goal of BIP85 is to facilitate the management and backup of multiple Bitcoin wallets. Instead of having to secure multiple phrases, a single piece of information suffices for all others.