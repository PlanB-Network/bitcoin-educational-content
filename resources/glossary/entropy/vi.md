---
term: ENTROPY

---
Entropy, in the context of cryptography and information, is a quantitative measure of the uncertainty or unpredictability associated with a data source or a random process. Entropy plays a crucial role in the security of cryptographic systems, especially in the generation of keys and random numbers. High entropy ensures that the generated keys are sufficiently unpredictable and resistant to brute-force attacks, where an attacker tries all possible combinations to guess the key.

In the context of Bitcoin, entropy is used to generate private keys or seeds. When creating a deterministic and hierarchical wallet, the construction of the mnemonic phrase is done from a random number, itself derived from an entropy source. The phrase is then used to generate multiple private keys, in a deterministic and hierarchical manner, in order to create spending conditions on UTXOs.

It is essential to have a quality source of entropy to ensure the security of cryptographic systems. Entropy sources can be physical processes, such as electronic noise or thermal variations, or software processes, such as pseudo-random number generators.