---
term: BECH32 AND BECH32M
---

`Bech32` and `Bech32m` are two Bitcoin address encoding formats. They are based on a slightly modified version of base 32 and include a checksum based derived from an error-detecting algorithm known as BCH (*Bose-Chaudhuri-Hocquenghem*). Compared to Legacy addresses, encoded in `Base58check`, the `Bech32` and `Bech32m` addresses feature a more efficient checksum, which enables improved error detection and, in some cases, the possibility of automatic typo correction. These formats also offers better readability, as they use only lowercase characters. Here is the addition matrix for this format from base 10:

| +   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | q   | p   | z   | r   | y   | 9   | x   | 8   |
| 8   | g   | f   | 2   | t   | v   | d   | w   | 0   |
| 16  | s   | 3   | j   | n   | 5   | 4   | k   | h   |
| 24  | c   | e   | 6   | m   | u   | a   | 7   | l   |

Bech32 was introduced by BIP173 in 2017 as an address format specifically designed for SegWit.  It uses a restricted set of characters, consisting of digits and lowercase letters, to minimize transcription errors and improve readability. Bech32 addresses typically start with bc1 and are used exclusively for SegWit V0 scripts, namely P2WPKH (Pay to Witness Public Key Hash) and P2WSH (Pay to Witness Script Hash).

However, there is a small, unexpected flaw specific to the Bech32 format. Whenever the last character of the address is a `p`, adding or removing any number of `q` characters immediately preceding it does not invalidate the checksum. This quirk does not affect SegWit V0 addresses defined by BIP173 because their lengths are fixed to two specific sizes, but it could impact future applications of Bech32 encoding. 

To address this, Bech32m was introduced by BIP350 in 2020. Bech32m addresses also begin with bc1 but are specifically designed for SegWit V1 (Taproot) and future script versions, most notably P2TR (Pay to Taproot).