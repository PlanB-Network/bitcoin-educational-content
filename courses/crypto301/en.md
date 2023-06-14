---
name: Introduction to Cryptography
goal: Understanding the creation of a Bitcoin wallet from a cryptographic perspective
objectives:
  - Demystify the terminology of cryptography related to Bitcoin.
  - Master the creation of a Bitcoin wallet.
  - Understand the structure of a Bitcoin wallet.
  - Understand addresses and derivation paths
---

# A journey to the heart of cryptography

Are you fascinated by Bitcoin? Wondering how a Bitcoin wallet works? Get ready to embark on a captivating journey to the heart of cryptography! Loïc, our expert, will guide you through the intricacies of creating a Bitcoin wallet, unveiling the mysteries behind intimidating technical terms such as hashing, key derivation, and elliptic curves.

This training will not only equip you with the knowledge to understand the structure of a Bitcoin wallet, but also prepare you to dive deeper into the exciting world of cryptography. So, are you ready to undertake this journey? Join us and turn your curiosity into a skill!

+++

# Introduction to Cryptography

![Introduction by Rogzy](https://youtu.be/ul8zU5QWIXg)

We are pleased to welcome you to the new training course entitled "Crypto 301: Introduction to Cryptography and HD Wallet", orchestrated by the expert in the field, Loïc Morel. This course will immerse you in the fascinating world of cryptography, the fundamental discipline of mathematics that ensures the encryption and security of your data. In our daily lives, and particularly in the field of Bitcoins, cryptography plays a crucial role. Concepts related to it such as private keys, public keys, addresses, derivation paths, seed and entropy, are at the heart of the use and creation of a Bitcoin wallet. Through this course, Loïc will explain in detail how private keys are created and how they are linked to addresses. Loïc will also devote an hour to explaining the mathematical details of the elliptic curve, this complex mathematical curve. In addition, you will understand why the use of HMAC SHA512 is important to secure your wallet and what the difference is between seed and mnemonic phrase.

The ultimate goal of this training is to enable you to technically understand the processes involved in creating an HD wallet and the cryptographic methods used. Over the years, Bitcoin wallets have evolved to become easier to use, more secure, and standardized thanks to specific BIPs. Loïc will help you understand these BIPs to grasp the choices made by Bitcoin developers and cryptographers. Like all the courses offered by our university, this one is completely free and open source. This means that you can freely take it and use it as you wish. We look forward to receiving your feedback at the end of this exciting course.

![intro by Loïc](https://youtu.be/mwuxXLk4Kws)

Hello everyone, I'm Loïc Morel, your guide through this technical exploration of the cryptography used in Bitcoin wallets.

Our journey begins with a dive into the depths of cryptographic hash functions. Together, we will dismantle the workings of the essential SHA256 and explore various algorithms dedicated to derivation.

We will continue our adventure by deciphering the mysterious world of digital signatures. You will discover how the magic of elliptic curves applies to these signatures, and we will shed light on how to calculate the public key from the private key. And of course, we will address the act of signing with the private key.

Next, we will go back in time to see the evolution of Bitcoin wallets, and we will venture into the concepts of entropy and random numbers. We will review the famous mnemonic phrase, while opening a parenthesis on the passphrase. You will even have the opportunity to experience a unique experience by creating a seed from 128 dice rolls!

With these solid foundations, we will be ready for the crucial part: creating a Bitcoin wallet. From the birth of the seed and the master key, through the study of extended keys, to the derivation of child key pairs, each step will be dissected. We will also discuss the structure of the wallet and the derivation paths.

To top it all off, we will end our journey by examining Bitcoin addresses. We will explain how they are created and how they play an essential role in the functioning of Bitcoin wallets.

Join me on this captivating journey, and get ready to explore the world of cryptography like never before. Leave your preconceptions at the door and open your mind to a new way of understanding Bitcoin and its fundamental structure.

# Hash Functions

## Introduction to Cryptographic Hash Functions in Bitcoin

![2.1 - Cryptographic Hash Functions](https://youtu.be/dvnGArYvVr8)

Welcome to today's session dedicated to an in-depth immersion into the cryptographic world of hash functions, an essential cornerstone to the security of the Bitcoin protocol. Imagine a hash function as an ultra-efficient cryptographic deciphering robot that transforms information of all sizes into a unique and fixed-size digital fingerprint, called a "hash". Throughout our exploration, we will depict the profile of cryptographic hash functions, highlighting their use in the Bitcoin protocol, and defining the specific objectives that these cryptographic functions must achieve.

Depicting the profile of cryptographic hash functions requires understanding two essential qualities: their irreversibility and their resistance to falsification. Each cryptographic hash function is like a unique artist, producing a distinct "hash" for each input. Even a slightly deviating brush significantly alters the final picture, i.e., the hash. These functions act as digital sentinels, verifying the integrity of downloaded software. Another crucial characteristic they possess is their resistance to collisions. Certainly, in the world of hashing, collisions are inevitable, but an excellent cryptographic hash function minimizes them considerably. It's like each hash is a house in a vast city; despite the enormous number of houses, a good hash function ensures that each house has a unique address.

Let's now navigate the turbulent waters of outdated hash functions. SHA0, SHA1, and MD5 are now considered rusty shells in the ocean of cryptographic hashing. They are often discouraged because they have lost their resistance to collisions. The principle of drawers explains why, despite our best efforts, collision avoidance is impossible due to the limitation of the output size. It is also important to note that resistance to the second preimage is dependent on resistance to collisions. To be truly considered safe, a hash function must resist collisions, second preimage, and preimage.

## Cryptographic Hash Functions and SHA256

An essential element in the Bitcoin protocol, the SHA-256 hash function is the captain of the ship. Other functions, such as SHA-512, are used for derivation with HMAC and PBKDF. Additionally, RIPMD160 is used to reduce a fingerprint to 160 bits. When we talk about HASH256 and HASH160, we refer to the use of double hashing with SHA-256 and RIPMD. The use of HASH160 is particularly advantageous because it allows for the security of SHA-256 while reducing the size of the fingerprint.

In summary, the ultimate goal of a cryptographic hash function is to transform information of arbitrary size into a fixed-size fingerprint. To be recognized as secure, it must have several strings to its bow: irreversibility, resistance to falsification, resistance to collisions, and resistance to the second preimage.

At the end of this exploration, we have demystified cryptographic hash functions, highlighted their use in the Bitcoin protocol, and dissected their specific objectives. We have learned that to be considered safe, hash functions must be resistant to preimage, second preimage, collisions, and falsification. We have also explored the range of different hash functions used in the Bitcoin protocol. In our next session, we will delve into the heart of the SHA256 hash function and discover the fascinating mathematics that give it its unique characteristics.

## The Inner Workings of SHA256

![The Inner Workings of SHA256](https://youtu.be/74SWg_ZbUj4)

Welcome to the next part of our fascinating journey through the cryptographic labyrinths of the hash function. Today, we unveil the mysteries of SHA256, a complex but ingenious process that we introduced in our previous discussion on hash functions. Let's take another step into this labyrinth, starting with the pre-processing of SHA256. Imagine pre-processing as preparing a delicious dish, where we add "padding bits" so that the size of our main ingredient, the input, reaches a perfect multiple of 512 bits. All of this with the ultimate goal of generating a succulent 256-bit hash from an ingredient of varying size.

In this cryptographic recipe, we play with bits, having an initial message size that we will call M. One bit is reserved for the separator, while P bits are used for padding. Additionally, we set aside 64 bits for the second phase of pre-processing. The total must be a multiple of 512 bits. A bit like making sure all the ingredients harmonize perfectly in our dish.
We now move on to the second phase of preprocessing, which involves adding the binary representation of the initial message size in bits. To do this, we use the 64 bits reserved in the previous step. We add zeros to round our 64 bits to our balanced input. Then, we merge the initial message, bit padding, and size padding, like ingredients in a blender, to obtain our balanced input.

Now, we prepare for the first steps of processing the SHA-256 function. As in any good recipe, we need some basic ingredients, which we call constants and initialization vectors. The initialization vectors, from A to H, are the first 32 bits of the decimal parts of the square roots of the first 8 prime numbers. The constants K, from 0 to 63, represent the first 32 bits of the decimal parts of the cubic roots of the first 64 prime numbers.

Within the compression function, we use specific operators such as XOR, AND, and NOT. We process the bits one by one according to their rank, using the XOR operator and a truth table. The AND operator is used to return 1 only if both operands are equal to 1, and the NOT operator to return the opposite value of an operand. We also use the SHR operation to shift the bits to the right by a chosen number.

Finally, after separating the balanced input into different message blocks of 512 bits, we perform 64 rounds of calculation in the compression function. Like in a cycling race, each lap improves our position. We add modulo 2^32 the intermediate state to the initial state of the compression function. The additions in the compression function are modulo 2^32 additions to contain the size of the sums to 32 bits.

In conclusion, we would like to emphasize the crucial role of the calculations performed in the CH, MAJ, σ0, and σ1 boxes. These operations, among others, are the guardians that ensure the robustness of the SHA256 hash function against attacks, making it a preferred choice for securing many digital systems, particularly within the Bitcoin protocol. It is therefore evident that although complex, the beauty of SHA256 lies in its robustness in finding the input from the hash, while verifying the hash for a given input is a mechanically simple action.

## The algorithms used for derivation

![The algorithms used for derivation](https://youtu.be/ZF1_BMsOJXc)
The HMAC and PBKDF2 derivation algorithms are key components in the security mechanism of the Bitcoin protocol. They prevent a variety of potential attacks and ensure the integrity of Bitcoin wallets.

HMAC and PBKDF2 are cryptographic tools used for different tasks in Bitcoin. HMAC is mainly used to counter length extension attacks during the derivation of hierarchically deterministic (HD) wallets, while PBKDF2 is used to convert a mnemonic phrase into a seed.

HMAC, which takes a message and a key as inputs, generates a fixed-size output. To ensure uniformity, the key is adjusted according to the block size used in the hash function. In the context of HD wallet derivation, HMAC-SHA-512 is used. The latter works with 1024-bit (128-byte) blocks and adjusts the key accordingly. It uses the constants OPAD (0x5c) and IPAD (0x36), repeated as many times as necessary to strengthen security.

The HMAC-SHA-512 process involves concatenating the result of SHA-512 applied to the key XOR OPAD and the key XOR IPAD with the message. When used with 1024-bit (128-byte) blocks, the input key is padded with zeros if necessary, then XORed with IPAD and OPAD. The modified key is then concatenated with the message.

The chain code, by integrating an additional source of entropy, increases the security of derived keys. Without it, an attack could compromise the entire wallet and steal all bitcoins.

PBKDF2 is used to convert a mnemonic phrase into a seed. This algorithm performs 2048 rounds using HMAC SHA512. Thanks to these derivation algorithms, two different inputs can give a unique and fixed output, which addresses the problem of possible length extension attacks on SHA-2 family functions.

A length extension attack exploits a specific property of certain cryptographic hash functions. In such an attack, an attacker who already has the hash of an unknown message can use it to calculate the hash of a longer message, which is an extension of the original message. This is often possible without knowing the content of the original message, which can lead to significant security vulnerabilities if this type of hash function is used for tasks such as integrity verification.
In conclusion, HMAC and PBKDF2 algorithms play essential roles in the security of HD wallet derivation in the Bitcoin protocol. HMAC-SHA-512 is used to protect against length extension attacks, while PBKDF2 allows for the conversion of the mnemonic phrase into a seed. The chain code adds an additional source of entropy in key derivation, ensuring the robustness of the system.

# Digital Signatures

## Digital Signatures and Elliptic Curves

![Digital Signatures and Elliptic Curves](https://youtu.be/gOjYiPkx4z8)

In the world of cryptocurrencies, transaction security is paramount. At the heart of the Bitcoin protocol is the use of digital signatures, which serve as mathematical proofs demonstrating the possession of a private key associated with a specific public key. This data protection technique is essentially based on a fascinating field of cryptography called elliptic curve cryptography (ECC).

Elliptic curve cryptography is the backbone of Bitcoin transaction security. These elliptic curves, which are reminiscent of the mathematical curves we may have studied in school, are useful in a variety of cryptographic applications, ranging from key exchanges to asymmetric encryption to digital signature creation. An interesting detail that distinguishes elliptic curves is their symmetry: any non-vertical line intersecting two points on the curve will intersect a third point.

Now, let's dig a little deeper: the Bitcoin protocol uses a particular elliptic curve called SecP256K1 to perform its cryptographic operations. This curve, defined on a finite set of positive integers modulo a 256-bit prime number, can be visualized as a cloud of points rather than a traditional curve. It is this unique design that allows Bitcoin to effectively secure its transactions.

As for the choice of the secp256k1 curve for Bitcoin, it is interesting to note that it was preferred over the secp256r1 curve. This curve is defined by the parameters a=0 and b=7, and its equation is y² = x³ + 7 modulo n, with n representing the prime number that determines the order of the curve.

When we talk about the constants used in the Bitcoin system, we generally refer to the specific parameters of the Elliptic Curve Digital Signature Algorithm (ECDSA) and the elliptic curve system used by Bitcoin, which is the secp256k1 curve. Here are these parameters:

- Primary field (p): Bitcoin uses a curve over a primary field, where p is the first number used to define this field. For the secp256k1 curve, p is equal to `p = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE FFFFFC2F` in hexadecimal or p = 2^256 - 2^32 - 2^9 - 2^8 - 2^7 - 2^6 - 2^4 -1 in decimal.
- Curve order (n): This is the number of points on the curve, including the point at infinity. For secp256k1, n is equal to `n = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE BAAEDCE6 AF48A03B BFD25E8C D0364141` in hexadecimal or n = 2^256 - 432420386565659656852420866394968145599 in decimal.
- Generator point (G): The base point, or generator, is the point on the curve from which all other public keys are generated. It has specific x and y coordinates, usually represented in hexadecimal. For secp256k1, the coordinates of G are, in hexadecimal:
  - `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
  - `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8`

Note that all hexadecimal values are usually represented in base 16, while decimal values are in base 10. In addition, all operations on these constants are performed modulo p for point coordinates on the curve and modulo n for key and signature operations.

So where are these famous bitcoins stored? Not in a Bitcoin wallet, as one might think. In reality, a Bitcoin wallet stores the private keys necessary to prove ownership of the bitcoins. The bitcoins themselves are recorded on the blockchain, a decentralized database that archives all transactions.

In the Bitcoin system, the unit of account is the bitcoin (note the lowercase "b"). It is divisible up to eight decimal places, with the smallest unit being the satoshi. UTXOs, or "Unspent Transaction Outputs," represent the unspent transaction outputs belonging to a user. To spend these bitcoins, one must demonstrate ownership of the private key corresponding to the public key linked to each UTXO.
To ensure the security of transactions, Bitcoin uses two digital signature protocols: ECDSA (Elliptic Curve Digital Signature Algorithm) and Schnorr. ECDSA is a signature protocol integrated into Bitcoin since its launch in 2009, while Schnorr signatures were added more recently in November 2021. Although both protocols rely on elliptic curve cryptography and use similar mathematical mechanisms, they differ mainly in terms of signature structure.

Before delving deeper into these signature mechanisms, it is important to understand what an elliptic curve is. An elliptic curve is defined by the equation y² = x³ + ax + b. Every point on this curve has a distinctive symmetry that is key to its usefulness in cryptography.

Ultimately, various elliptic curves are recognized as secure for cryptographic use. The most well-known is perhaps the secp256r1 curve. However, for Bitcoin, Satoshi Nakamoto opted for a different curve: secp256k1.

In the next section of this course, we will take a closer look at the public and private keys for a deeper understanding of elliptic curve cryptography and the digital signature algorithm. This will be the time to consolidate your knowledge and understand how all this information fits together to ensure the security of the Bitcoin protocol.

## Calculating the public key from the private key

![Calculating the public key from the private key](https://youtu.be/NJENwFU889Y)

In the rest of this course, we will delve into the mechanisms of public and private keys, two crucial elements of the Bitcoin protocol. These keys are intrinsically linked by the Elliptic Curve Digital Signature Algorithm (ECDSA). Understanding them will give us a deep insight into how Bitcoin secures transactions on its platform.

To begin, let's dive into the world of the ECDSA algorithm. Bitcoin exploits this digital signature algorithm to link private and public keys. In this system, the private key is a random or pseudo-random 256-bit number. The total number of possibilities for a private key is theoretically 2^256, but it is slightly less than that in reality. To be precise, some 256-bit private keys are not valid for Bitcoin.
To be compatible with Bitcoin, a private key must be between 1 and n-1, where n represents the order of the elliptic curve. This means that the total number of possibilities for a Bitcoin private key is almost equal to 1.158 x 10^77. To put this into perspective, it's roughly the same number of atoms present in the observable universe. The unique private key is then used to determine a 512-bit public key.

The public key, denoted as K, is a point on the elliptic curve that is derived from the private key using point operations on the curve. It is important to note that the ECDSA function is irreversible, meaning it is impossible to retrieve the private key from the public key. This irreversibility is the cornerstone of Bitcoin wallet security.

The public key consists of two 256-bit points, totaling 512 bits. However, it can be compressed into a 264-bit number. The point G is the starting point for calculating all users' public keys in the system.

One remarkable property of elliptic curves is that a line intersecting the curve at two points will also intersect a third point, called point O. This property is used to determine point U, which is the opposite of point O. Adding a point to itself is done by drawing a tangent to the curve at that point, which gives a new unique point called j. The scalar product of a point by n is equivalent to adding that point to itself n times.

These operations on the points of an elliptic curve are the basis for calculating public keys. Knowing the private key makes it easy to calculate the public key. However, knowing the public key does not allow for the calculation of the private key, thus ensuring the security of the Bitcoin system. In fact, the security of public and private keys relies on the discrete logarithm problem, a complex mathematical question.

In our next lesson, we will explore how a digital signature is made using the ECDSA algorithm with a private key to unlock bitcoins. Stay tuned for this exciting exploration of the world of cryptocurrencies and cryptography.

## Signing with the private key

![Signing with the private key](https://youtu.be/h2hIyGgPqkM)
The process of digital signature is a key method for proving that you are the holder of a private key without revealing it. This is achieved using the ECDSA algorithm, which involves determining a unique nonce, calculating a specific number, V, and creating a digital signature composed of two parts, S1 and S2. It is crucial to always use a unique nonce to avoid security attacks. A notorious example of what can happen when this rule is not followed is the case of the PlayStation 3 hack, which was compromised due to nonce reuse.

To validate a digital signature using the ECDSA (Elliptic Curve Digital Signature Algorithm) algorithm, the following steps are generally involved:

1. Verify that the signature values, S1 and S2, are in the range [1, n-1]. If not, the signature is invalid.
2. Calculate the inverse of S2 mod n. We will call this u. It is often calculated as follows: u = (S2)^-1 mod n.
3. Calculate H, which is the hash value of the signed message.
4. Calculate u1 = H _ u mod n and u2 = S1 _ u mod n.
5. Calculate the point P on the elliptic curve using u1, u2, and the public key K: P = u1*G + u2*K, where G is the curve's generator point.
6. If P is the point at infinity, the signature is invalid.
7. Calculate I = x-coordinate of P mod n.
8. The signature is valid if I is equal to S1.

It is important to note that different software may use different notations and some steps may be combined or rearranged, but the basic logic is the same. Also note that all arithmetic operations are performed in the finite field defined by the elliptic curve (mod n, where n is the curve's order). As a reminder, the secp256k1 curve (used in Bitcoin) has n = 2^256 - 432420386565659656852420866394968145599.

Regarding the generation of public and private keys, it is essential to become familiar with the elliptic curve and the generator point. To obtain a public key, a random number must be chosen as the private key, often called a `nonce`, and used in the elliptic curve equation.
The elliptic curve is a powerful tool for generating secure public and private keys. For example, to obtain the public key 3G, you draw a tangent to point G, calculate the opposite of -G to obtain 2G, and then add G and 2G. To perform a transaction, you must prove that you know the number 3 by unlocking the bitcoins associated with the public key 3G.

To create a digital signature and prove that you know the private key associated with the public key 3G, you first calculate a nonce, then the point V associated with this nonce (in the example given, it is 4G). Then, you calculate the point T by adding the public key 3G and the point V, which gives 7G.

Verifying a digital signature is a crucial step in using the ECDSA algorithm, which allows you to confirm the authenticity of a signed message without needing the sender's private key. Here's how it works in detail:

In our example, we have two important values: T and V. T is a numerical value (7 in this example), and V is a point on the elliptic curve (represented by 4G here). These values are produced when creating the digital signature and are then sent with the message to allow verification.

When the verifier receives the message, they will also receive these two values, T and V.

Here are the steps the verifier will follow to validate the signature:

1. They will first calculate the hash of the message, which we will call H.
2. Then, they will calculate u1 and u2. To do this, they will use the following formulas:
   - u1 = H \* (S2)^-1 mod n
   - u2 = T \* (S2)^-1 mod n
     Where S2 is the second part of the digital signature, n is the order of the elliptic curve, and (S2)^-1 is the inverse of S2 mod n.
3. The verifier will then calculate a point P' on the elliptic curve using the formula: P' = u1 _ G + u2 _ K
   - G is the generation point of the curve
   - K is the sender's public key
4. The verifier will then calculate I', which is simply the x-coordinate of point P' modulo n.
5. Finally, the verifier will confirm that I' is equal to T. If this is the case, the signature is considered valid. If not, the signature is invalid.

This procedure ensures that only the sender possessing the corresponding private key could have produced a signature that passes this verification process.
In conclusion, verifying an ECDSA digital signature is an essential procedure in Bitcoin transactions. It ensures that the signed message has not been altered during transmission and that the sender is indeed the holder of the private key. This digital authentication technique is based on complex mathematical principles, including elliptic curve arithmetic, while maintaining the confidentiality of the private key. It provides a solid security foundation for cryptographic transactions.

That being said, managing these keys, as well as their creation, is another essential question in Bitcoin. How to generate a new key pair? How to organize a multitude of keys securely and efficiently? How to recover them if necessary?

To answer these questions and deepen your understanding of cryptography security, our next course will focus on the concept of Hierarchical Deterministic Wallets (HD wallets) and the use of mnemonic phrases. These mechanisms offer elegant ways to efficiently manage your cryptocurrency keys while enhancing security and recoverability.

# Mnemonic Phrase

## Evolution of Bitcoin Wallets

![Evolution of Bitcoin Wallets](https://youtu.be/6tmu1R9cXyk)

The Hierarchical Deterministic Wallet, or more commonly known as HD wallet, plays a prominent role in the cryptocurrency ecosystem. The term "wallet" may seem misleading to those who are new to this field, as it does not involve holding money or currencies. It rather refers to a collection of private cryptographic keys derived from a single master key, through a clever algorithmic arithmetic process. These private keys, which are of a fixed length of 256 bits, are the essence of cryptocurrency ownership and are sometimes referred to as "Just a Bunch Of Keys" (JBOC).

However, the complexity of managing these keys is offset by a set of protocols, called Bitcoin Improvement Proposals (BIP). These upgrade proposals are at the heart of the functionality and security of HD wallets. For example, [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), launched in 2012, revolutionized the way these keys are generated and stored, by introducing the concept of deterministically and hierarchically derived keys. Thus, the process of backing up these keys is greatly simplified, while maintaining their level of security.
Subsequently, [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) introduced a significant innovation: the 24-word mnemonic phrase. This system transformed a complex and difficult-to-remember string of numbers into a series of ordinary words, making it much easier to memorize and store. Additionally, [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) proposed adding an additional password phrase to enhance the security of individual keys. These successive improvements led to the BIP43 and BIP44 standards, which standardized the structure and hierarchy of HD wallets, making these wallets more accessible and easier to use for the general public.

In the following sections, we will delve deeper into the workings of HD wallets. We will discuss key derivation principles and examine the fundamental concepts of entropy and random number generation, which are essential for ensuring the security of your HD wallet.

As a summary, it is essential to highlight the central role of BIP32 and BIP39 in the design and security of HD wallets. These protocols allow for the generation of multiple keys from a single seed, which is supposed to be a random or pseudo-random number. Today, these standards are adopted by the majority of cryptocurrency wallets, whether they are dedicated to a single cryptocurrency or support multiple types of currencies.

We hope this introduction has helped you better understand the foundations of HD wallets and their various characteristics. Our goal is to help you master these essential concepts and navigate more efficiently in the complex world of cryptocurrencies. So, stay with us as we continue to explore the subtleties and nuances of this fascinating world in the upcoming lessons.

## Entropy and Random Number

![Entropy and Random Number](https://youtu.be/k18yH18w2TE)

The security of private keys in the Bitcoin ecosystem is crucial for ensuring the safety of transactions. To avoid vulnerabilities associated with predictability, private keys must be generated truly randomly, which can be a laborious task for users. One solution to this problem is the Hierarchical Deterministic Wallet, or HD wallet. This method allows for the deterministic and hierarchical generation of child key pairs from a single piece of information at the base of the wallet. Randomness is essential here to ensure the security of derived keys.

Random number generation is a crucial element in cryptography to ensure the integrity of private keys. To prevent vulnerabilities associated with predictability, a private key must be produced randomly. Using a new key pair for each transaction further enhances security, although it complicates backup and only partially preserves confidentiality. In summary, the security of private keys is an absolute priority, requiring rigorous and random generation. HD wallets offer a solution to facilitate key generation and management while maintaining a high level of security.

However, generating random numbers on computers poses a significant challenge since the results obtained are not truly random. Therefore, it is essential to use a Random Number Generator (RNG). The types of RNG vary, ranging from Pseudo-Random Number Generators (PRNG) to True Random Number Generators (TRNG), as well as PRNGs that incorporate an entropy source.

In the case of Bitcoin, private keys are generated from a single piece of information at the base of the wallet. This information allows for deterministic and hierarchical derivation of child key pairs. Entropy is the foundation of any HD wallet, although there is no standard for generating this random number. Therefore, random number generation is a major issue in securing Bitcoin transactions.

The verification phase of key generation is crucial to ensure the security and authenticity of random number generation, a fundamental step in preventing vulnerabilities associated with predictability. It is strongly recommended to use open-source wallets to enable this verification.
However, it is important to note that some hardware wallets may be "closed source", making it impossible to verify the generation of the random number. A possible workaround would be to generate one's own mnemonic phrase using dice, although this approach may present some risks. Using a randomly generated passphrase can help mitigate these risks.

An example of applying this method is the "dice roll" option offered by CoinKit to generate mnemonic phrases. Another possibility would be to use very large initial information and reduce this information to 256 bits with the SHA-256 hash function, capable of generating a good random number. It is important to mention that the SHA-256 hash function is resistant to collisions, falsification, and pre-image and second pre-image attacks.

Ultimately, randomness plays a central role in cryptography and computer science, and the ability to generate randomness securely is crucial to ensuring the security of private keys and Bitcoin transactions. Entropy, which is at the heart of the Bitcoin HD wallet, is essential for its security. In our next lesson, we will continue to explore this topic, delving more deeply into how entropy contributes to the security of HD wallets.

### Support Us

This course, as well as all the content on this university, has been offered to you for free by our community. To support us, you can share it around you, become a member of the university, and even contribute to its development via GitHub. On behalf of the entire team, thank you!

### Rate the Course

A rating system for the course will soon be integrated into this new E-learning platform! In the meantime, thank you very much for taking the course and if you enjoyed it, please consider sharing it around you.

## The Mnemonic Phrase

![The Mnemonic Phrase](https://youtu.be/uJERqH9Xp7I)

The security of a Bitcoin wallet is a major concern for all its users. An essential way to ensure the backup of the wallet is to generate a mnemonic phrase based on entropy and checksum.

Entropy is the cornerstone of HD wallet security. Several methods exist to generate this entropy, including through pseudo-random number generators (PRNGs), true random number generators (TRNGs), or manually. It is crucial that this entropy be random or pseudo-random to ensure the security of the wallet.
On the other hand, the checksum ensures the verification of the accuracy of the recovery phrase. Without this checksum, an error in the phrase could lead to the creation of a different wallet and therefore the loss of funds. The checksum is obtained by passing the entropy through the SHA256 function and retrieving the first 8 bits of the hash.

Different standards exist for the mnemonic phrase depending on the size of the entropy. The most commonly used standard for a 24-word recovery phrase is an entropy of 256 bits. The size of the checksum is determined by dividing the size of the entropy by 32.

For example, an entropy of 256 bits generates an 8-bit checksum. The concatenation of the entropy and the checksum then leads to respective sizes of 128 bits, 160 bits, etc. Depending on the size of the entropy, the recovery phrase will consist of 12 words for 128 bits, 15 words for 160 bits, and 24 words for 256 bits.

To convert bits into phrases, each segment is associated with a word from a list of 2048 words. It is important to note that no word has the same first four letters in the same order.

It is essential to save the 24-word recovery phrase to preserve the integrity of the Bitcoin wallet. The two most commonly used standards are based on an entropy of 128 or 256 bits and a concatenation of 12 or 24 words. Adding a passphrase is an additional option to strengthen the security of the wallet.

In conclusion, generating a mnemonic phrase to secure a Bitcoin wallet is a crucial process. It is important to respect the standards of the mnemonic phrase depending on the size of the entropy. Saving the 24-word recovery phrase is essential to prevent any loss of funds. Thank you for your attention and we look forward to our next course on cryptocurrency.

## The passphrase

![The passphrase](https://youtu.be/dZkOYO7MXwc)

The passphrase is an additional password that can be integrated into a Bitcoin wallet to increase its security. Its use is optional and is at the discretion of the user. By adding arbitrary information that, together with the mnemonic phrase, allows the wallet seed to be calculated, the passphrase strengthens its security.
To derive the keys of an HD wallet, both the mnemonic phrase and the passphrase are necessary. The passphrase is free and can reach an almost infinite size. It is not included in the mnemonic phrase, which is standardized and must follow certain constraints of size, checksum, and encoding. An attacker cannot access a user's bitcoins without knowing the passphrase. The passphrase plays a role in the construction and calculation of all the keys in the wallet.

The pbkdf2 function is used to generate the seed from the passphrase. This seed allows for the derivation of all the child key pairs of the wallet. If the passphrase is changed, the Bitcoin wallet becomes completely different.

The passphrase is an essential tool for enhancing the security of Bitcoin wallets. It can allow for the application of various security strategies. For example, it can be used to create duplicates and facilitate backups of the mnemonic phrase. It can also improve the security of the wallet by mitigating the risks associated with the random generation of the mnemonic phrase.

An effective passphrase should be long (20 to 40 characters) and diversified (using uppercase and lowercase letters, numbers, and symbols). It should not be directly related to the user or their environment. It is safer to use a random sequence of characters rather than a simple word as a passphrase.

A passphrase is more secure than a simple password. The ideal passphrase is long, varied, and random. It can enhance the security of an HD wallet or hot software. It can also be used to create redundant and secure backups.

It is crucial to take care of passphrase backups to avoid losing access to the wallet. A passphrase is an option for an HD wallet. It can be randomly generated with dice or another pseudo-random number generator. It is not recommended to memorize a passphrase or mnemonic phrase.

In our next course, we will examine in detail the functioning of the seed and the first key pair generated from it. Feel free to follow this course to continue your learning. We look forward to seeing you soon.

## Creating a seed from 128 dice rolls!

![Creating a seed from 128 dice rolls!](https://youtu.be/lUw-1kk75Ok)
The creation of a mnemonic phrase is a crucial step in securing your cryptocurrency portfolio. There are several methods for generating a mnemonic phrase, however, we will focus on the manual generation method using dice. It is important to note that this method is not suitable for a high-value portfolio. It is recommended to use open-source software or a hardware wallet to generate the mnemonic phrase. To create a mnemonic phrase, we will use dice to generate binary information. The goal is to understand the process of creating the mnemonic phrase.

**Step 1 - Preparation:**
Make sure you have an amnesic Linux distribution, such as Tails OS, installed on a USB key for added security. Note that this tutorial should not be used to create a primary wallet.

**Step 2 - Generating a random binary number:**
We will use dice to generate binary information. Roll a die 128 times and record each result (1 for odd, 0 for even).

**Step 3 - Organizing binary numbers:**
Organize the obtained binary numbers into rows of 11 digits to facilitate further calculations. The twelfth row should only have 7 digits.

**Step 4 - Calculating the checksum:**

The last 4 digits for the twelfth row correspond to the checksum. To calculate this checksum, we need to use a terminal from a Linux distribution. It is recommended to use [TailOs](https://tails.boum.org/index.fr.html), which is a bootable memoryless distribution from a USB key. Once on your terminal, enter the command `echo <binary number> | shasum -a 254 -0`. Replace `<binary number>` with your list of 128 zeros and ones. The output is a hexadecimal hash. Record the first character of this hash and convert it to binary. You can use this [table](https://www.educative.io/answers/decimal-binary-and-hex-conversion-table) for help. Add the binary checksum (4 digits) to the twelfth row of your sheet.

**Step 5 - Conversion to decimal:**
To find the words associated with each of your lines, you must first convert each series of 11 bits into decimal. Here, you cannot use an online converter because these bits represent your mnemonic phrase. Therefore, you will need to convert using a calculator and a trick as follows: each bit is associated with a power of 2, so from left to right, we have 11 ranks that correspond to 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1. To convert your series of 11 bits into decimal, you only need to add the ranks that contain a 1. For example, for the series 00110111011, this corresponds to the following addition: 256 + 128 + 32 + 16 + 8 + 2 + 1 = 443. You can now convert each line into decimal. And before moving on to encoding into words, you need to add +1 to all lines because the index of the BIP39 word list starts from 1 and not 0.

**Step 8 - Mnemonic phrase generation:**

Start by printing the [list of 2048 words](https://seedxor.com/files/wordlist.pdf) to convert between your decimal numbers and the BIP39 words. The particularity of this list is that no word has these first 4 letters in common with all the other words in this dictionary. Then, for each of your lines, look for the word associated with the decimal number.

**Step 9 - Mnemonic phrase test:**

Immediately test your mnemonic phrase on Sparrow Wallet by creating a wallet from it. If you get an invalid checksum error, you probably made a calculation error. Correct this error by going back to step 4 and testing again on Sparrow Wallet. Voila! You have just created a new Bitcoin wallet from 128 dice rolls.

Generating a mnemonic phrase is an important process for securing your cryptocurrency wallet. It is recommended to use more secure methods, such as the use of open source software or hardware wallets, to generate the mnemonic phrase. However, completing this workshop helps to better understand how we can create a Bitcoin wallet from a random number.

# Creating a Bitcoin wallet

## Creating the seed and master key

![Creating the seed and master key](https://youtu.be/56yAt_JDWhY)

In this part of the course, we will explore the steps of deriving an HD (Hierarchical Deterministic Wallet) wallet, which allows for hierarchical creation and management of private and public keys.
The foundation of the HD wallet relies on two essential elements: the mnemonic phrase and the passphrase (optional additional password). Together, they constitute the seed, an alphanumeric sequence of 512 bits that serves as the basis for deriving the keys of the wallet. From this seed, it is possible to derive all the child key pairs of the Bitcoin wallet. The seed is the key that allows access to all the bitcoins associated with the wallet, whether you use a passphrase or not.

To obtain the seed, the pbkdf2 function (Password-Based Key Derivation Function 2) is used with the mnemonic phrase and passphrase. The output of pbkdf2 is a 512-bit seed. The master private key and the master chain code are determined using the HMAC SHA-512 algorithm (Hash-based Message Authentication Code Secure Hash Algorithm 512). This algorithm requires a message and a key to generate a result. The master private key is calculated from the seed and the phrase "Bitcoin SEED". This phrase is identical for all HD wallet derivations, thus ensuring consistency between wallets.

Initially, the SHA-512 function was not implemented in the Bitcoin protocol, which is why HMAC SHA-512 is used. The use of HMAC SHA-512 with the phrase "Bitcoin SEED" constrains the user to generate a wallet specific to Bitcoin. The result of HMAC SHA-512 is a 512-bit number, divided into two parts: the left 256 bits represent the master private key, while the right 256 bits represent the master chain code.

The master private key is the parent key of all future keys in the wallet, while the master chain code is involved in the derivation of child keys. It is important to note that it is impossible to derive a child key pair without knowing the corresponding chain code of the parent pair. The chain code adds a source of entropy to the derivation process.

A key pair in the wallet includes a private key, a public key, and a chain code. The chain code allows for the introduction of randomness in the derivation of child keys and isolates each key pair to prevent information leakage.

It is important to emphasize that the master private key is the first private key derived from the seed and has no connection to the extended keys of the wallet. The seed is therefore the fundamental element for deriving all the keys of the wallet. It differs from the mnemonic phrase and passphrase, which are used for the creation of the seed.
In the next lesson, we will explore in detail extended keys, such as xPub, xPRV, zPub, and understand why they are used and how they are constructed.

## Extended Keys

![Extended Keys](https://youtu.be/TRz760E_zUY)

In this part of the lesson, we will study extended keys (xPub, zPub, yPub) and their prefixes, which play an important role in deriving child keys in a Hierarchical Deterministic Wallet (HD Wallet).

Extended keys differ from master keys. An HD wallet generates a mnemonic phrase and a seed to obtain the master key and master chain code. Extended keys are used to derive child keys and require both the parent key and the corresponding chain code. An extended key combines these two pieces of information to simplify the derivation process.

Extended keys are identified by specific prefixes (XPRV, XPUB, YPUB, ZPUB) that indicate whether it is an extended private or public key, as well as its specific purpose. The metadata associated with an extended key includes the version (prefix), depth, public key fingerprint, index, and payload (chain code and parent key).

The payload is composed of the chain code (32 bytes) and the parent key (33 bytes). These elements are essential for deriving child keys. A private key is generated from a random or pseudo-random number, while a public key is generated using the Elliptic Curve Digital Signature Algorithm (ECDSA) algorithm.

Each pair of extended keys is associated with a unique chain code, which allows for specific derivations. By concatenating the parent key with the chain code, an extended private or public key is obtained.

Extended public keys can only derive from normal child public keys, while extended private keys can derive from both public and private child keys, whether on a normal or hardened derivation. The use of extended keys with the XPUB prefix allows for deriving new addresses without going back to the corresponding private keys, thus providing better security. The metadata associated with extended keys provides important information about their role and position in the key hierarchy.
Compressed public keys have a size of 33 bytes, while uncompressed public keys are 512 bits. Compressed public keys retain the same information as uncompressed keys, but with a reduced size. Extended keys have a size of 82 bytes and their prefix is represented in base 58 through a conversion to hexadecimal. The checksum is calculated using the HASH256 hash function.

Hardened derivations start from indexes that are powers of 2 (2^31). Extended public keys only allow for the derivation of normal child public keys, while extended private keys allow for the derivation of any child key. It is interesting to note that the most commonly used prefixes are xpub and zpub, which correspond respectively to legacy standards and segwit v1 and segwit v0.

In our next lesson, we will look at the derivation of child key pairs using the knowledge gained about extended keys and the master key of the wallet.

In conclusion, extended keys play an essential role in cryptography and the operation of HD wallets. Understanding their use and calculation is crucial to ensure the security of transactions and the protection of digital assets. The prefixes and metadata associated with extended keys allow for efficient use and accurate derivation of necessary child keys.

## Derivation of Child Key Pairs

![Derivation of Child Key Pairs](https://youtu.be/FXhI-GmE9Aw)

Next, we will discuss the calculation of the seed and master key, which are the first essential elements for the hierarchy and derivation of the HD wallet (Hierarchical Deterministic Wallet). The seed, which is 128 to 256 bits long, is generated randomly or from a secret phrase. It plays a deterministic role in the derivation of all other keys. The master key is the first key derived from the seed, and it allows for the derivation of all other child key pairs.

The master chain code plays an important role in wallet recovery from the seed. It should be noted that all keys derived from the same seed will have the same master chain code.

The hierarchy and derivation of the HD wallet offer more efficient management of keys and wallet structures. Extended keys allow for the derivation of a child key pair from a parent pair using specific mathematical calculations and algorithms.

## Types of child key pairs

There are different types of child key pairs, including enhanced keys and normal keys. The extended public key allows only the derivation of normal public child keys, while the extended private key allows the derivation of all child keys, both public and private, whether in normal or enhanced mode. Each key pair has an index to distinguish it from the others.

Child key derivation uses the HMAC-SHA512 function, using the parent key concatenated with the index and string code associated with the key pair. Normal child keys have an index between 0 and 2 to the 31st power minus 1, while strengthened child keys have an index between 2 to the 31st power and 2 to the 32nd power minus 1.

## Child key derivation process

There are two types of child key pairs: reinforced pairs and normal pairs. The child key derivation process uses the public keys to generate the expenditure conditions, while the private keys are used for signing. The extended public key allows only the derivation of normal child public keys, while the extended private key allows the derivation of all child keys, both public and private, in normal or enhanced mode.

Enhanced derivation uses the parent private key, while normal derivation uses the parent public key. The HMAC-SHA512 function is used for enhanced derivation, while normal derivation uses a 512-bit condensate. The child public key is obtained by multiplying the child private key by the elliptic curve generator.

## Hierarchization and derivation of multiple key pairs

Hierarchizing and deriving many key pairs deterministically creates a family tree scheme for hierarchical derivation. In the next lesson of this course, we'll look at HD portfolio structure and derivation paths, with particular emphasis on derivation path notations.

## Portfolio structure and derivation paths

![Portfolio structure and derivation paths](https://youtu.be/etO9UxwyE2I)

In this chapter, we will study the structure of the derivation tree in an HD (Hierarchical Deterministic Wallet) portfolio. We have already explored the computation of the seed, the master key and the derivation of child key pairs. Now we'll concentrate on the organization of keys within the wallet.

Translated with www.DeepL.com/Translator (free version)
The HD wallet uses depth layers to organize keys. Each derivation from a parent pair to a child pair corresponds to a depth layer. Depth 0 corresponds to the master key and master chain code.

Depth 1 is used to derive child keys for a specific purpose, which is determined by the index. The purposes conform to BIP 84 and Segwit v0/v1 standards.

Depth 2 allows for differentiation of accounts for different cryptocurrencies or networks. This allows for organization of the wallet based on different sources of funds.

Depth 3 is used to organize the wallet into different accounts, providing a clearer and more organized structure.

Depth 4 corresponds to the internal and external chains, which are used for addresses intended to be publicly communicated. Index 0 is associated with the external chain, while index 1 is associated with the internal chain. Each account has two chains: the external chain (0) and the internal chain (1). Depth 4 is also used to manage script types in the case of multi-signature wallets.

Depth 5 is used for receiving addresses on a standard wallet. In the next section, we will examine in more detail the derivation of child key pairs.

For each depth layer, we use indexes to differentiate child key pairs. Hardened indexes are used with an apostrophe for certain derivations. The public key per year is used as input for the HMAC function. The index in a derivation path indicates the value used in the HMAC function.

The index without an apostrophe corresponds to the actual index used, while the index with an apostrophe corresponds to the actual index + 2^31. Hardened derivations use indexes from 2^31 to 2^32-1. For example, index 44' corresponds to the actual index 2^31 + 44.

To generate a specific receiving address, we derive a child key pair from the master key and master chain code. Then, we use the index to differentiate between different child key pairs at the same depth.

Extended keys, such as XPUB, allow for sharing your wallet with multiple people. The derivation path is used to differentiate between the external chain (addresses intended to be communicated) and the internal chain (change addresses).
It is important to note that different depths are used in an HD wallet depending on different standards. Deriving parent keys to child keys allows for moving from one depth to another. The use of different branches in the HD wallet indicates the different standards being followed.

In the next chapter, we will study Bitcoin addresses, their advantages of use, and the steps involved in their construction.

# What is a Bitcoin Address?

## Bitcoin Addresses

![Bitcoin Addresses](https://youtu.be/nqGBMjPtFNI)

In this chapter, we will explore receiving addresses, which play a crucial role in the Bitcoin system. They allow for receiving funds on a coin and are generated from pairs of private and public keys. Although there is a type of script called Pay2PublicKey that allows for locking bitcoins on a public key, users generally prefer to use receiving addresses instead of this script.

When a recipient wants to receive bitcoins, they provide a receiving address to the sender rather than their public key. An address is actually a hash of a public key, with a specific format. The public key is derived from the child private key using mathematical operations such as point addition and doubling on elliptic curves.

It is important to note that it is not possible to go back from the address to the public key, nor from the public key to the private key. Using an address reduces the size of the public key information, which initially is 512 bits. It is possible to compress a public key by only keeping the value of x and adding a prefix, but this technique was not known at the time of Bitcoin's creation. Using an address therefore does not save space in blocks.

Bitcoin addresses have been reduced in size to facilitate their use. They have a checksum, which allows for detecting typos and reducing the risk of losing bitcoins. On the other hand, public keys do not have a checksum, which means that typos can lead to the loss of corresponding funds.

Addresses also offer a second layer of security between public and private information, making it more difficult to take control of the private key. The hash functions used allow for key pairs to be resistant to potential attacks by quantum computers. Indeed, these computers can potentially break ECDSA (Elliptic Curve Digital Signature Algorithm), but they cannot break a hash function.
It is essential to emphasize that each address is for one-time use, which contributes to security and confidentiality. Reusing the same address poses serious privacy issues and should be avoided. Additionally, each address is a hash of a public key, accompanied by a checksum to reduce the risk of losing bitcoins.

Different prefixes are used for Bitcoin addresses. For example, BC1Q corresponds to a Segwit V0 address, BC1P to a Taproot/Segwit V1 address, and prefixes 1 and 3 are associated with Pay2PublicKeyH/Pay2ScriptH (legacy) addresses. In the next lesson, we will explain step by step how to derive an address from a public key.

In summary, receiving addresses are an essential element of the Bitcoin system. They are generated from pairs of private and public keys and are used to receive funds on a coin. Addresses integrate a checksum to reduce the risks of losing bitcoins and are designed to be used uniquely, ensuring security and confidentiality. Different types of addresses are used in the Bitcoin system, offering enhanced privacy and security.

## How to create a Bitcoin address?

![How to create a Bitcoin address?](https://youtu.be/ewMGTN8dKjI)

In this chapter, we will discuss the construction of a receiving address for Bitcoin transactions. A receiving address is an alphanumeric representation of a compressed public key. The conversion of a public key into a receiving address goes through several steps.

One of the advantageous features of receiving addresses is the presence of a checksum, which allows for error detection. For this, we use BCH (Bose-Chaudhuri-Hocquenghem) checksum technology, which ensures accurate error detection. This technology also contributes to reducing the number of characters required to represent an address, making it easier to use.

To start building an address, we must compress the corresponding public key. A raw public key occupies 520 bits, but thanks to the symmetry of the elliptic curve used, an elliptic curve can have an x-coordinate associated with two possible values for y: positive or negative. On the Bitcoin network, we work with a finite set of positive integers rather than the set of real numbers. To represent a public key from x, we add a prefix indicating the value of y (even or odd). Compressing a public key reduces its size from 520 to 264 bits. The parity of y in a finite set of positive integers corresponds to the parity of y in the set of real numbers.
Let's take the example of the public key belonging to Satoshi Nakamoto, with a prefix of 0,3 indicating an odd value of y. We can then move on to the second step of constructing an address from compressed public keys. It is possible to calculate two addresses for each public key. To do this, we use the SHA256 function to obtain the hash of the public key. Then, we apply the ripemd160 function to the result of SHA256 to obtain a string of characters. This string is then encoded in binary format in groups of 5 bits, to which metadata is added for the checksum calculation using the BCH program.

In the case of legacy addresses, we use double SHA256 hashing to generate the address checksum. However, for Segwit V0 and V1 addresses, we use BCH checksum technology to ensure error detection. The BCH program is capable of suggesting and correcting errors with an extremely low error probability. Currently, the BCH program is used to detect and suggest changes to be made, but it does not automatically make them for the user. The calculation of the checksum with the BCH code is based on polynomial Chien-Chauffage arithmetic.

The BCH program requires several input information, including the HRP (Human Readable Part) which must be extended. The extension of the HRP consists of encoding each letter in base 2, taking the first three bits of each character, inserting a separator 0, and then concatenating the last five bits of each character. The blue characters converted to base 10 correspond to 3 and 3 in decimal, while the other five orange characters correspond to 2 and 3 in base 10. The extension of the HRP in base 10 allows the isolation of the last five bits of each character, thus reinforcing the checksum.

The Segwit V0 version is represented by the code 00 and the "payload" is in black, in base 10. This is followed by six characters reserved for the checksum. The input containing the metadata is then submitted to the BCH program to obtain the checksum in base 10. The concatenation of the version, payload, and checksum allows the construction of the address. The base 10 characters are then converted to bech32 characters using a correspondence table. The bech32 alphabet includes all alphanumeric characters, except for 1, b, i, and o, to avoid confusion.
To build an address starting with bc1q, we must apply a hash function (H160) to a compressed public key, then add the checksum, version (q), HRP (bc), and separator (1). Taproot addresses, on the other hand, start with bc1p because their version (Segwit V1) corresponds to 0+1=1, hence the use of the character p. All of these elements are then converted to BCH32, a variant of base 32 specific to Bitcoin.

Thus, we have gone through the steps of constructing a receiving address, using BCH checksum technology, as well as constructing an address starting with bc1q or bc1p using the BCH32 variant of base 32 specific to Bitcoin.

## Cryptography Recap for Bitcoin Wallets

![training summary](https://youtu.be/NkAYoVUMvOs)

Throughout this training, we have studied in depth the Hierarchical Deterministic (HD) wallet with BIP32. Entropy plays a central role in this type of wallet, as it is used to generate a mnemonic phrase from a random number. With the list of 2048 words provided in BIP39, this mnemonic phrase can be encoded into a series of easy-to-remember words. The mnemonic phrase, along with an optional passphrase, is necessary to generate the wallet seed. The passphrase acts as a cryptographic salt that adds an extra layer of protection to the wallet.

The pbkdf2 function is used to generate the seed from the mnemonic phrase and passphrase, using an hmacha512 and 2048 iterations. The master key and master chain code are then derived from this seed using the hmacha512 function again with the phrase "bitcoin seed". The master private key and master chain code are the highest elements in the HD wallet hierarchy.
The derivation of a child key depends on several factors, including the parent key and the corresponding chain code. An extended key is obtained by concatenating a parent key with its chain code, while a master key is a distinct key. To derive an address, the compressed public key is first hashed using SHA256 and RIPMD160, and then a checksum is calculated. The double SHA256 hash is used to calculate the checksum in the case of a legacy standard, while the BCH (Bose-Chaudhuri-Hocquenghem) program is used to calculate the checksum in the case of a segwit standard. Then, a base 58 format representation is used for a legacy standard, while the bech32 format is used for a segwit standard, in order to obtain the HD wallet address.

In summary, we have explored in detail the hash functions and their characteristics, as well as digital signatures and elliptic curves. We then delved into the world of hierarchical deterministic (HD) wallets with BIP32, using entropy and passphrase to generate the wallet seed. We also learned how to derive child keys and obtain the HD wallet address. I hope this information has been useful to you, and I now encourage you to take the evaluation to test your acquired knowledge in the Crypto 301 course. Thank you for your attention.

# Acknowledgments and Keep Digging the Rabbit Hole

We would like to sincerely thank you for taking the Crypto 301 course. We hope this experience has been enriching and informative for you. We have covered many exciting topics, ranging from mathematics to cryptography to the workings of the Bitcoin protocol.

If you would like to further explore the subject, we have an additional resource to offer you. We conducted an exclusive interview with Théo Pantamis and Loïc Morel, two renowned experts in the field of cryptography. This interview delves deep into various aspects of the subject and offers interesting perspectives.

Feel free to watch this interview to continue exploring the fascinating field of cryptography. We hope it will be useful and inspiring in your journey. Once again, thank you for your participation and commitment throughout this course.

## Interview with Théo Pantamis

![Interview with Théo Pantamis](https://youtu.be/c9MvtGJsEvY)

Here is a summary of the interview:

In this interview, Théo Pantamys, specializing in mathematics and passionate about Bitcoin, Lightning Network, and protocols, shares his journey and thoughts on various topics.
Théo discovered Bitcoin in 2009, but his interest developed further in 2015-2016 thanks to scientific popularizers on YouTube. He focused on the mathematics and cryptography of Bitcoin, as well as on comparison with other protocols.

He emphasizes the importance of decentralization in Bitcoin and how it goes against the authority of the State, offering an opening of the register. Bitcoin also effectively solves the problem of regulation.

Théo also addresses the issue of privacy in Bitcoin. He explains the importance of CoinJoin to preserve users' privacy and avoid the disclosure of personal information. He recommends the use of Wasabi and Whirlpool to improve transaction anonymity.

Next, Théo discusses RGB, a complex protocol that solves Bitcoin's technical problems. He explains how RGB uses discrete contracts to create tokens and financial products while maintaining contract state validation on the Bitcoin blockchain.

The discussion continues on the threat of quantum computing to Bitcoin. Théo mentions that it would take about a hundred qubits to break most algorithms, and for now, quantum computers have not yet reached this level of power.

Regarding the checksum of Bitcoin addresses, Théo explains how BCH codes are used to detect and potentially correct typing errors. He emphasizes the importance of the checksum to avoid the loss of bitcoins and optimize address size.

In conclusion, Théo shares resources to deepen understanding of Bitcoin, including YouTube channels for mathematical popularization, recommended books, and Twitter spaces where developers discuss their work.
