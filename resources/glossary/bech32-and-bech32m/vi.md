---
term: BECH32 AND BECH32M

---
`Bech32` and `Bech32m` are two address encoding formats for receiving bitcoins. They are based on a slightly modified base 32. They incorporate a checksum based on an error-correcting algorithm called BCH (*Bose-Chaudhuri-Hocquenghem*). Compared to Legacy addresses, encoded in `Base58check`, the `Bech32` and `Bech32m` addresses have a more efficient checksum, allowing for the detection and potentially automatic correction of typos. Their format also offers better readability, with only lowercase characters. Here is the addition matrix for this format from base 10:

&nbsp;

| +   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |

| --- | --- | --- | --- | --- | --- | --- | --- | --- |

| 0   | q   | p   | z   | r   | y   | 9   | x   | 8   |

| 8   | g   | f   | 2   | t   | v   | d   | w   | 0   |

| 16  | s   | 3   | j   | n   | 5   | 4   | k   | h   |

| 24  | c   | e   | 6   | m   | u   | a   | 7   | l   |

&nbsp;

Bech32 and Bech32m are encoding formats used to represent SegWit addresses. Bech32 is an address encoding format introduced by BIP173 in 2017. It uses a specific set of characters, composed of numbers and lowercase letters, to minimize typing errors and facilitate reading. Bech32 addresses generally start with `bc1` to indicate that they are native to SegWit. This format is only used on SegWit V0 addresses, with the scripts P2WPKH (Pay to Witness Public Key Hash) and P2WSH (Pay to Witness Script Hash). However, there is a small, unexpected flaw specific to the Bech32 format. Whenever the last character of the address is a `p`, adding or removing any number of `q` characters immediately preceding it does not invalidate the checksum. This does not affect existing uses of SegWit V0 addresses (BIP173) due to their restriction to two defined lengths. However, this could affect future uses of the Bech32 encoding. The Bech32m format is simply a Bech32 format with this error corrected. It was introduced with BIP350 in 2020. Bech32m addresses also start with `bc1`, but they are specifically designed to be compatible with SegWit V1 (Taproot) and later versions, with the script P2TR (Pay to TapRoot).