---
name: Introduction to Cryptography
goal: Understand the creation of a Bitcoin wallet from a cryptographic perspective
objectives:
  - Demystify the terminology of cryptography related to Bitcoin.
  - Master the creation of a Bitcoin wallet.
  - Understand the structure of a Bitcoin wallet.
  - Understand addresses and derivation paths.
---

# A journey into cryptography

Are you fascinated by Bitcoin? Wondering how a Bitcoin wallet works? Get ready to embark on a captivating journey into cryptography! Loïc, our expert, will guide you through the intricacies of creating a Bitcoin wallet, unveiling the mysteries behind intimidating technical terms such as hashing, key derivation, and elliptic curves.

This training will not only equip you with the knowledge to understand the structure of a Bitcoin wallet, but also prepare you to delve deeper into the exciting world of cryptography. So, are you ready to embark on this journey? Join us and turn your curiosity into expertise!

+++

# Introduction

## Introduction to Cryptography

### Is this training for you? YES!

![introduction by Rogzy](https://youtu.be/ul8zU5QWIXg)

We are delighted to welcome you to the new training course titled "Crypto 301: Introduction to Cryptography and HD Wallet", orchestrated by the expert himself, Loïc Morel. This course will immerse you in the fascinating world of cryptography, the fundamental discipline of mathematics that ensures the encryption and security of your data.

In our daily lives, and particularly in the realm of Bitcoin, cryptography plays a crucial role. Concepts related to cryptography such as private keys, public keys, addresses, derivation paths, seed, and entropy are at the heart of using and creating a Bitcoin wallet. Throughout this course, Loïc will explain in detail how private keys are generated and how they are linked to addresses. Loïc will also dedicate an hour to explaining the mathematical details of elliptic curves, this complex mathematical curve. Additionally, you will understand why the use of HMAC SHA512 is important for securing your wallet and what the difference is between seed and mnemonic phrase.

The ultimate goal of this training is to enable you to understand the technical processes of creating an HD wallet and the cryptographic methods used. Over the years, Bitcoin wallets have evolved to become easier to use, more secure, and standardized thanks to specific BIPs. Loïc will help you understand these BIPs to grasp the choices made by Bitcoin developers and cryptographers. Like all the trainings offered by our university, this one is completely free and open source. This means that you can freely take it and use it as you wish. We look forward to receiving your feedback at the end of this exciting course.

### The floor is yours, professor!

![intro by loïc](https://youtu.be/mwuxXLk4Kws)

Hello everyone, I'm Loïc Morel, your guide through this technical exploration of the cryptography used in Bitcoin wallets.

Our journey begins with a dive into the depths of cryptographic hash functions. Together, we will dissect the inner workings of the essential SHA256 and explore various algorithms dedicated to derivation.

We will continue our adventure by deciphering the mysterious world of digital signatures. You will discover how the magic of elliptic curves applies to these signatures, and we will shed light on how to calculate the public key from the private key. And of course, we will address the act of signing with the private key.

Next, we will go back in time to see the evolution of Bitcoin wallets, and we will venture into the concepts of entropy and random numbers. We will review the famous mnemonic phrase, while also delving into the topic of passphrases. You will even have the opportunity to experience something unique by creating a seed from 128 dice rolls!

With these solid foundations, we will be ready for the crucial part: creating a Bitcoin wallet. From the birth of the seed and the master key, to the study of extended keys, and the derivation of child key pairs, each step will be dissected. We will also discuss the structure of the wallet and derivation paths.

To top it all off, we will conclude our journey by examining Bitcoin addresses. We will explain how they are created and how they play an essential role in the functioning of Bitcoin wallets.

Join me on this captivating journey, and get ready to explore the world of cryptography like never before. Leave your preconceptions at the door and open your mind to a new way of understanding Bitcoin and its fundamental structure.

# Hash Functions

## Introduction to cryptographic hash functions related to Bitcoin

![2.1 - Cryptographic Hash Functions](https://youtu.be/dvnGArYvVr8)

Welcome to today's session dedicated to an in-depth immersion into the cryptographic world of hash functions, an essential cornerstone of Bitcoin protocol security. Imagine a hash function as an ultra-efficient cryptographic deciphering robot that transforms information of all sizes into a unique and fixed-size digital fingerprint called a "hash". Throughout our exploration, we will depict the profile of cryptographic hash functions, highlighting their use in the Bitcoin protocol, and defining the specific objectives that these cryptographic functions must achieve.

![image](assets/image/section1/0.JPG)

Depicting the profile of cryptographic hash functions requires understanding two essential qualities: their irreversibility and their resistance to falsification. Each cryptographic hash function is like a unique artist, producing a distinct "hash" for each input. Even a slightly deviating brush significantly alters the final painting, i.e., the hash. These functions act as digital sentinels, verifying the integrity of downloaded software. Another crucial characteristic they possess is their resistance to collisions. Certainly, in the hashing universe, collisions are inevitable, but an excellent cryptographic hash function minimizes them significantly. It's as if each hash were a house in a vast city; despite the enormous number of houses, a good hash function ensures that each house has a unique address.

![image](assets/image/section1/1.JPG)

Let's now navigate the turbulent waters of outdated hash functions. SHA0, SHA1, and MD5 are now considered rusty relics in the ocean of cryptographic hashing. They are often discouraged as they have lost their resistance to collisions. The principle of drawers explains why, despite our best efforts, collision avoidance is impossible due to the limitation of output size. It is also important to note that resistance to second preimage is dependent on resistance to collisions. To be truly considered secure, a hash function must resist collisions, second preimage, and preimage.

Key element in the Bitcoin protocol, the SHA-256 hash function is the captain of the ship. Other functions, like SHA-512, are used for derivation with HMAC and PBKDF. In addition, RIPMD160 is used to reduce a fingerprint to 160 bits. When we talk about HASH256 and HASH160, we are referring to the use of double hashing with SHA-256 and RIPMD. The use of HASH160 is particularly advantageous as it allows for the security of SHA-256 while reducing the size of the fingerprint.

To summarize, the ultimate goal of a cryptographic hash function is to transform arbitrary-sized information into a fixed-size fingerprint. To be recognized as secure, it must have several strengths: irreversibility, resistance to forgery, resistance to collisions, and resistance to second preimage.

![image](assets/image/section1/2.JPG)

At the end of this exploration, we have demystified cryptographic hash functions, highlighted their use in the Bitcoin protocol, and dissected their specific objectives. We have learned that in order to be considered secure, hash functions must be resistant to preimage, second preimage, collisions, and forgery. We have also covered the range of different hash functions used in the Bitcoin protocol. In our next session, we will delve into the core of the SHA256 hash function and discover the fascinating mathematics that give it its unique characteristics.

## The Inner Workings of SHA256

![The Inner Workings of SHA256](https://youtu.be/74SWg_ZbUj4)

Welcome to the continuation of our fascinating journey through the cryptographic mazes of the hash function. Today, we unveil the mysteries of SHA256, a complex yet ingenious process that we introduced in our previous discussion on hash functions. Let's take another step into this maze, starting with the preprocessing of SHA256. Imagine preprocessing as the preparation of a delicious dish, where we add "padding bits" to make the size of our main ingredient, the input, reach a perfect multiple of 512 bits. All of this with the ultimate goal of generating a succulent 256-bit hash from a variable-sized ingredient.

![image](assets/image/section1/3.JPG)
![image](assets/image/section1/4.JPG)

In this cryptographic recipe, we play with bits, having an initial message size that we will call M. One bit is reserved for the separator, while P bits are used for padding. Additionally, we set aside 64 bits for the second preprocessing phase. The total must be a multiple of 512 bits. It's a bit like making sure all the ingredients blend perfectly in our dish.

![image](assets/image/section1/5.JPG)

We now move on to the second phase of preprocessing, which involves adding the binary representation of the initial message size, in bits. For this, we use our 64 reserved bits from the previous step. We add zeros to round our 64 bits to our balanced input. Then, we merge the initial message, the padding bits, and the size padding, like ingredients in a blender, to obtain our balanced input.

![image](assets/image/section1/6.JPG)

Now, we prepare for the first steps of the SHA-256 function processing. Like in any good recipe, we need some basic ingredients, which we call constants and initialization vectors. The initialization vectors, from A to H, are the first 32 bits of the decimal parts of the square roots of the first 8 prime numbers. The constants K, from 0 to 63, represent the first 32 bits of the decimal parts of the cubic roots of the first 64 prime numbers.

![image](assets/image/section1/7.JPG)

Within the compression function, we use specific operators such as XOR, AND, and NOT. We process the bits one by one according to their rank, using the XOR operator and a truth table. The AND operator is used to return 1 only if both operands are equal to 1, and the NOT operator to return the opposite value of an operand. We also use the SHR operation to shift the bits to the right by a chosen number.

![image](assets/image/section1/8.JPG)
![image](assets/image/section1/9.JPG)

Finally, after separating the balanced input into different blocks of 512-bit messages, we perform 64 rounds of calculation in the compression function. Like in a cycling race, each lap improves our position. We add modulo 2^32 the intermediate state to the initial state of the compression function. The additions in the compression function are modulo 2^32 additions to contain the size of the sums to 32 bits.

![image](assets/image/section1/10.JPG)
![image](assets/image/section1/11.JPG)
![image](assets/image/section1/12.JPG)
![image](assets/image/section1/13.JPG)

To conclude, we would like to emphasize the crucial role of the calculations performed in the CH, MAJ, σ0, and σ1 boxes. These operations, among others, are the guardians that ensure the robustness of the SHA256 hash function against attacks, making it a preferred choice for securing numerous digital systems, especially within the Bitcoin protocol. It is evident that, although complex, the beauty of SHA256 lies in its robustness to find the input from the hash, while verifying the hash for a given input is a mechanically simple action.

## The algorithms used for derivation

![The algorithms used for derivation](https://youtu.be/ZF1_BMsOJXc)

The HMAC and PBKDF2 derivation algorithms are key components in the security mechanism of the Bitcoin protocol. They prevent a variety of potential attacks and ensure the integrity of Bitcoin wallets.

HMAC and PBKDF2 are cryptographic tools used for different tasks in Bitcoin. HMAC is primarily used to counter length extension attacks when deriving hierarchically deterministic (HD) wallets, while PBKDF2 is used to convert a mnemonic phrase into a seed.

![image](assets/image/section1/14.JPG)

HMAC, which takes a message and a key as inputs, generates a fixed-size output. To ensure uniformity, the key is adjusted based on the block size used in the hash function. In the context of HD wallet derivation, HMAC-SHA-512 is used. The latter operates with 1024-bit (128-byte) blocks and adjusts the key accordingly. It uses the constants OPAD (0x5c) and IPAD (0x36), repeated as necessary to enhance security.

The HMAC-SHA-512 process involves concatenating the result of SHA-512 applied to the key XOR OPAD and the key XOR IPAD with the message. When used with 1024-bit (128-byte) blocks, the input key is padded with zeros if necessary, then XORed with IPAD and OPAD. The modified key is then concatenated with the message.

![image](assets/image/section1/15.JPG)

The use of a salt, by incorporating an additional source of entropy, increases the security of derived keys. Without it, an attack could compromise the entire wallet and steal all the bitcoins.

PBKDF2 is used to convert a mnemonic phrase into a seed. This algorithm performs 2048 rounds using HMAC SHA512. Thanks to these derivation algorithms, two different inputs can produce a unique and fixed output, which mitigates the problem of possible length extension attacks on SHA-2 family functions. A length extension attack exploits a specific property of certain cryptographic hash functions. In such an attack, an attacker who already has the hash of an unknown message can use it to calculate the hash of a longer message, which is an extension of the original message. This is often possible without knowing the content of the original message, which can lead to significant security vulnerabilities if this type of hash function is used for tasks such as integrity verification.

![image](assets/image/section1/16.JPG)

In conclusion, the HMAC and PBKDF2 algorithms play essential roles in the security of HD wallet derivation in the Bitcoin protocol. HMAC-SHA-512 is used to protect against length extension attacks, while PBKDF2 allows the conversion of the mnemonic phrase into a seed. The chain code adds an additional source of entropy in key derivation, ensuring the robustness of the system.

# Digital Signatures

## Digital Signatures and Elliptic Curves

![Digital Signatures and Elliptic Curves](https://youtu.be/gOjYiPkx4z8)

In the world of cryptocurrencies, transaction security is paramount. At the core of the Bitcoin protocol, digital signatures are used as mathematical proofs demonstrating the possession of a private key associated with a specific public key. This data protection technique is essentially based on a fascinating field of cryptography called elliptic curve cryptography (ECC).

![image](assets/image/section2/0.JPG)

Elliptic curve cryptography is the backbone of Bitcoin transaction security. These elliptic curves, reminiscent of the mathematical curves we studied in school, are useful in a variety of cryptographic applications, ranging from key exchanges to asymmetric encryption to digital signature creation. An interesting detail that distinguishes elliptic curves is their symmetry: any non-vertical line intersecting two points on the curve will intersect a third point.

Now let's dig a little deeper: the Bitcoin protocol uses a specific elliptic curve called SecP256K1 to perform its cryptographic operations. This curve, defined on a finite set of positive integers modulo a prime number of 256 bits, can be visualized as a cloud of points rather than a traditional curve. It is this unique design that allows Bitcoin to effectively secure its transactions.

![image](assets/image/section2/1.JPG)

As for the choice of the secp256k1 curve for Bitcoin, it is interesting to note that it was preferred over the secp256r1 curve. This curve is defined by the parameters a=0 and b=7, and its equation is y² = x³ + 7 modulo n, where n represents the prime number that determines the order of the curve.

When we talk about the constants used in the Bitcoin system, we generally refer to the specific parameters of the Elliptic Curve Digital Signature Algorithm (ECDSA) and the elliptic curve system used by Bitcoin, which is the secp256k1 curve. Here are these parameters:

- prime field (p): Bitcoin uses a curve over a prime field, so p is the first number used to define this field. For the secp256k1 curve, p is equal to `p = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE FFFFFC2F` in hexadecimal or p = 2^256 - 2^32 - 2^9 - 2^8 - 2^7 - 2^6 - 2^4 -1 in decimal.
- curve order (n): This is the number of points on the curve, including the point at infinity. For secp256k1, n is equal to `n = FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE BAAEDCE6 AF48A03B BFD25E8C D0364141` in hexadecimal or n = 2^256 - 432420386565659656852420866394968145599 in decimal.
- generator point (G): The base point, or generator, is the point on the curve from which all other public keys are generated. It has specific x and y coordinates, usually represented in hexadecimal. For secp256k1, the coordinates G are, in hexadecimal:
  - `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
  - `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8`

![image](assets/image/section2/2.JPG)

Note that all hexadecimal values are generally represented in base 16, while decimal values are in base 10. In addition, all operations on these constants are performed modulo p for point coordinates on the curve and modulo n for key and signature operations.

So, where are these famous bitcoins stored? Not in a Bitcoin wallet, as one might think. In reality, a Bitcoin wallet stores the private keys necessary to prove ownership of the bitcoins. The bitcoins themselves are recorded on the blockchain, a decentralized database that archives all transactions.

In the Bitcoin system, the unit of account is the bitcoin (note the lowercase "b"). It is divisible up to eight decimal places, with the smallest unit being the satoshi. UTXOs, or "Unspent Transaction Outputs," represent the unspent transaction outputs belonging to a user. To spend these bitcoins, one must demonstrate ownership of the private key corresponding to the public key linked to each UTXO.

To ensure transaction security, Bitcoin relies on two digital signature protocols: ECDSA (Elliptic Curve Digital Signature Algorithm) and Schnorr. ECDSA is a signature protocol integrated into Bitcoin since its launch in 2009, while Schnorr signatures were added more recently in November 2021. Although both protocols are based on elliptic curve cryptography and use similar mathematical mechanisms, they differ mainly in terms of signature structure.

Before delving deeper into these signature mechanisms, it is important to understand what an elliptic curve is. An elliptic curve is defined by the equation y² = x³ + ax + b. Every point on this curve has a distinctive symmetry that is key to its usefulness in cryptography.

Ultimately, various elliptic curves are recognized as secure for cryptographic use. Perhaps the most well-known is the secp256r1 curve. However, for Bitcoin, Satoshi Nakamoto opted for a different curve: secp256k1.

In the next section of this course, we will take a closer look at the public key and private key for a thorough understanding of cryptography on elliptic curves and the digital signature algorithm. This will be the time to consolidate your knowledge and understand how all this information comes together to ensure the security of the Bitcoin protocol.

## Calculating the public key from the private key

![Calculating the public key from the private key](https://youtu.be/NJENwFU889Y)

In the following section of this course, we will delve into the mechanisms of public and private keys, two crucial elements of the Bitcoin protocol. These keys are intrinsically linked by the Elliptic Curve Digital Signature Algorithm (ECDSA). Understanding them will give us a deep insight into how Bitcoin secures transactions on its platform.

![image](assets/image/section2/3.JPG)
![image](assets/image/section2/4.JPG)

To begin, let's dive into the world of the ECDSA algorithm. Bitcoin utilizes this digital signature algorithm to link private and public keys. In this system, the private key is a random or pseudo-random 256-bit number. The total number of possibilities for a private key is theoretically 2^256, but in reality, it is slightly less than that. To be precise, some 256-bit private keys are not valid for Bitcoin.

![image](assets/image/section2/5.JPG)

To be compatible with Bitcoin, a private key must be between 1 and n-1, where n represents the order of the elliptic curve. This means that the total number of possibilities for a Bitcoin private key is almost equal to 1.158 x 10^77. To put this into perspective, it is roughly the same number of atoms present in the observable universe. The unique private key is then used to derive a 512-bit public key.

![image](assets/image/section2/6.JPG)

The public key, denoted as K, is a point on the elliptic curve that is derived from the private key using point operations on the curve. It is important to note that the ECDSA function is irreversible, meaning it is impossible to retrieve the private key from the public key. This irreversibility is the cornerstone of Bitcoin wallet security.

The public key consists of two 256-bit points, totaling 512 bits. However, it can be compressed into a 264-bit number. The point G is the starting point for calculating all the public keys of users in the system.

![image](assets/image/section2/7.JPG)

One remarkable property of elliptic curves is that a line intersecting the curve at two points will also intersect a third point, called point O. This property is used to determine point U, which is the opposite of point O. Adding a point to itself is done by drawing a tangent to the curve at that point, resulting in a new unique point called j. The scalar multiplication of a point by n is equivalent to adding that point to itself n times.

![image](assets/image/section2/8.JPG)

These operations on points of an elliptic curve are the basis for calculating public keys. Knowing the private key, it is easy to calculate the public key. However, knowing the public key does not allow for the calculation of the private key, thus ensuring the security of the Bitcoin system. In fact, the security of public and private keys relies on the discrete logarithm problem, a complex mathematical question.

![image](assets/image/section2/9.JPG)

In our next lesson, we will explore how a digital signature is achieved using the ECDSA algorithm with a private key to unlock bitcoins. Stay tuned for this exciting exploration of the world of cryptocurrencies and cryptography.

## Signing with the private key

![Signing with the private key](https://youtu.be/h2hIyGgPqkM)

The process of digital signature is a key method to prove that you are the holder of a private key without revealing it. This is achieved using the ECDSA algorithm, which involves determining a unique nonce, calculating a specific number V, and creating a digital signature composed of two parts, S1 and S2. It is crucial to always use a unique nonce to avoid security attacks. A notorious example of what can happen when this rule is not followed is the case of the PlayStation 3 hack, which was compromised due to nonce reuse.

Specifically, to validate a digital signature using the ECDSA (Elliptic Curve Digital Signature Algorithm) algorithm, the following steps are typically involved:

1. Verify that the signature values, S1 and S2, are in the range [1, n-1]. If not, the signature is invalid.
2. Calculate the inverse of S2 mod n. We will call this u. It is often calculated as follows: u = (S2)^-1 mod n.
3. Calculate H, which is the hash value of the signed message.
4. Calculate u1 = H _ u mod n and u2 = S1 _ u mod n.
5. Calculate the point P on the elliptic curve using u1, u2, and the public key K: P = u1*G + u2*K, where G is the curve's generator point.
6. If P is the point at infinity, the signature is invalid.
7. Calculate I = x-coordinate of P mod n.
8. The signature is valid if I is equal to S1.

![image](assets/image/section2/10.JPG)
![image](assets/image/section2/11.JPG)

It is important to note that each software may use different notations and some steps may be combined or rearranged, but the basic logic remains the same. Also note that all arithmetic operations are performed in the finite field defined by the elliptic curve (mod n, where n is the order of the curve). As a reminder, the secp256k1 curve (used in Bitcoin) has n = 2^256 - 432420386565659656852420866394968145599.
When it comes to generating public and private keys, it is essential to familiarize yourself with the elliptic curve and the generator point. To obtain a public key, a random number must be chosen as the private key, often called a `nonce`, and used in the equation of the elliptic curve.

The elliptic curve is a powerful tool for generating secure public and private keys. For example, to obtain the public key 3G, you draw a tangent to the point G, calculate the opposite of -G to obtain 2G, and then add G and 2G. To perform a transaction, you must prove that you know the number 3 by unlocking the bitcoins associated with the public key 3G.

To create a digital signature and prove that you know the private key associated with the public key 3G, you first calculate a nonce, then the point V associated with this nonce (in the given example, it is 4G). Then, you calculate the point T by adding the public key 3G and the point V, which gives 7G.

![image](assets/image/section2/12.JPG)

Verifying a digital signature is a crucial step in using the ECDSA algorithm, which allows confirming the authenticity of a signed message without needing the sender's private key. Here is how it works in detail:

In our example, we have two important values: T and V. T is a numerical value (7 in this example), and V is a point on the elliptic curve (represented by 4G here). These values are produced during the creation of the digital signature and are then sent along with the message to enable verification.

When the verifier receives the message, they will also receive these two values, T and V.

Here are the steps the verifier will follow to validate the signature:

1. They will first compute the hash of the message, which we will call H.
2. Then, they will calculate u1 and u2. To do this, they will use the following formulas:
   - u1 = H \* (S2)^-1 mod n
   - u2 = T \* (S2)^-1 mod n'

# The mnemonic phrase

## Evolution of Bitcoin wallets

![Evolution of Bitcoin wallets](https://youtu.be/6tmu1R9cXyk)

The Hierarchical Deterministic Wallet, or more commonly known as the HD wallet, plays a prominent role in the cryptocurrency ecosystem. The term "wallet" may seem misleading to those new to the field, as it does not imply the holding of money or currency. Rather, it refers to a collection of private cryptographic keys derived from a single master key, thanks to an ingenious process of algorithmic arithmetic. These private keys, which are a fixed length of 256 bits, are the very essence of crypto-currency ownership, and are sometimes referred to by the slightly cruder name of "Just a Bunch Of Keys" (JBOC).

![image](assets/image/section3/0.JPG)

However, the complexity of managing these keys is offset by a set of protocols, known as Bitcoin Improvement Proposals (BIPs). These upgrade proposals are at the heart of the functionality and security of HD wallets. For example, [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), launched in 2012, revolutionized the way these keys are generated and stored, introducing the concept of deterministically and hierarchically derived keys. This greatly simplifies the process of saving these keys, while maintaining their level of security.

![image](assets/image/section3/1.JPG)

Subsequently, [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) introduced a landmark innovation: the 24-word mnemonic phrase. This system made it possible to transform a complex, hard-to-remember sequence of digits into a series of ordinary words, much easier to memorize and store. In addition, [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) proposed adding an additional passphrase to reinforce the security of individual keys. These successive improvements led to BIP43 and BIP44, which standardized the structure and hierarchy of HD wallets, making them more accessible and easier to use for the general public.

In the following sections, we'll take a deeper dive into how HD portfolios work. We'll cover the principles of key derivation, and examine the fundamental concepts of entropy and random number generation, which are essential to guaranteeing the security of your HD portfolio.
The Hierarchical Deterministic Wallet, or more commonly known as the HD wallet, plays a prominent role in the cryptocurrency ecosystem. The term "wallet" may seem misleading to those new to the field, as it does not imply the holding of money or currency. Rather, it refers to a collection of private cryptographic keys derived from a single master key, thanks to an ingenious process of algorithmic arithmetic. These private keys, which are a fixed length of 256 bits, are the very essence of crypto-currency ownership, and are sometimes referred to by the slightly cruder name of "Just a Bunch Of Keys" (JBOC).

![image](assets/image/section3/0.JPG)

However, the complexity of managing these keys is offset by a set of protocols, known as Bitcoin Improvement Proposals (BIPs). These upgrade proposals are at the heart of the functionality and security of HD wallets. For example, [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), launched in 2012, revolutionized the way these keys are generated and stored, introducing the concept of deterministically and hierarchically derived keys. This greatly simplifies the process of saving these keys, while maintaining their level of security.![image](assets/image/section3/1.JPG)

In summary, it is essential to highlight the central role of BIP32 and BIP39 in the design and security of HD wallets. These protocols allow for the generation of multiple keys from a single seed, which is supposed to be a random or pseudo-random number. Today, these standards are adopted by the majority of cryptocurrency wallets, whether they are dedicated to a single cryptocurrency or support multiple types of currencies.

I hope this introduction has helped you better understand the foundations of HD wallets and their various characteristics. Our goal is to help you master these essential concepts and navigate more efficiently in the complex world of cryptocurrencies. So, stay with us as we continue to explore the intricacies and nuances of this fascinating world in the upcoming lessons.

## Entropy and Random Number

![Entropy and Random Number](https://youtu.be/k18yH18w2TE)

The importance of private key security in the Bitcoin ecosystem is undeniable. They are indeed the cornerstone that ensures the security of Bitcoin transactions. To avoid any vulnerability associated with predictability, these keys must be generated in a truly random manner, which can quickly become a laborious exercise for the user. One solution to this puzzle is the Hierarchical Deterministic Wallet, or HD wallet. This method allows for the deterministic and hierarchical generation of child key pairs from a single piece of information at the base of the wallet. This is where randomness becomes essential to guarantee the security of derived keys.

![image](assets/image/section3/2.JPG)

The generation of random numbers is indeed a crucial element in cryptography, to ensure the integrity of private keys. To prevent any vulnerability related to predictability, a private key must be produced randomly. The use of a new key pair for each transaction further enhances security, although it complicates their backup and only partially preserves confidentiality. In summary, the security of private keys is an absolute priority, requiring rigorous and random generation. HD wallets offer a solution to facilitate the generation and management of keys while maintaining a high level of security.

However, generating random numbers on computers poses a significant challenge, as the results obtained are not truly random. That is why it is essential to use a Random Number Generator (RNG). The types of RNG vary, ranging from Pseudo-Random Number Generators (PRNG) to True Random Number Generators (TRNG), as well as PRNGs that incorporate an entropy source.

![image](assets/image/section3/3.JPG)

In the case of Bitcoin, private keys are generated from a single piece of information at the base of the wallet. This information allows for deterministic and hierarchical derivation of child key pairs. Entropy is the foundation of any HD wallet, although there is no standard for generating this random number. Therefore, generating random numbers is a major concern for securing Bitcoin transactions.

The verification phase of key generation is crucial to ensure the security and authenticity of random number generation, a fundamental step in preventing any vulnerability associated with predictability. It is strongly recommended to use open-source wallets to enable this verification.

However, it is important to note that some hardware wallets may be "closed source," making it impossible to verify the generation of the random number. A possible workaround would be to generate one's own mnemonic phrase using dice, although this approach may present certain risks.

![image](assets/image/section3/4.JPG)

Using a randomly generated passphrase can help mitigate these risks.

An example of applying this method is the "dice roll" option offered by CoinKit to generate mnemonic phrases. Another possibility would be to use a very large initial piece of information and reduce this information to 256 bits with the SHA-256 hash function, capable of generating a good random number. It is important to mention that the SHA-256 hash function resists collisions, falsification, and pre-image and second pre-image attacks.

Ultimately, randomness plays a central role in cryptography and computer science, and the ability to generate randomness securely is crucial to ensuring the security of private keys and Bitcoin transactions. Entropy, which is at the heart of the Bitcoin HD wallet, is essential for its security. In our next lesson, we will continue to explore this topic, delving into how entropy contributes to the security of HD wallets.

## The mnemonic phrase

![The mnemonic phrase](https://youtu.be/uJERqH9Xp7I)

The security of a Bitcoin wallet is a major concern for all its users. An essential way to ensure the backup of the wallet is to generate a mnemonic phrase based on entropy and checksum.

![image](assets/image/section3/5.JPG)

Entropy is the cornerstone of HD wallet security. Several methods exist to generate this entropy, including through pseudo-random number generators (PRNGs), true random number generators (TRNGs), or manually. It is crucial that this entropy be random or pseudo-random to guarantee the security of the wallet.

![image](assets/image/section3/6.JPG)

On the other hand, the checksum ensures the verification of the accuracy of the recovery phrase. Without this checksum, an error in the phrase could result in the creation of a different wallet and therefore the loss of funds. The checksum is obtained by passing the entropy through the SHA256 function and retrieving the first 8 bits of the hash.

Different standards exist for the mnemonic phrase depending on the size of the entropy. The most commonly used standard for a 24-word recovery phrase is an entropy of 256 bits. The size of the checksum is determined by dividing the size of the entropy by 32.

For example, a 256-bit entropy generates an 8-bit checksum. The concatenation of the entropy and the checksum then leads to respective sizes of 128 bits, 160 bits, etc. Depending on the size of the entropy, the recovery phrase will consist of 12 words for 128 bits, 15 words for 160 bits, and 24 words for 256 bits.

![image](assets/image/section3/7.JPG)

To transform the bits into phrases, each segment is associated with a word from a list of 2048 words. It is important to note that no word has the same order of the first four letters.

It is essential to backup the 24-word recovery phrase to preserve the integrity of the Bitcoin wallet. The two most commonly used standards are based on an entropy of 128 or 256 bits and a concatenation of 12 or 24 words. Adding a passphrase is an additional option to enhance the security of the wallet.

In conclusion, generating a mnemonic phrase to secure a Bitcoin wallet is a crucial process. It is important to adhere to the standards of the mnemonic phrase depending on the size of the entropy. Backing up the 24-word recovery phrase is essential to prevent any loss of funds. Thank you for your attention and we look forward to our next cryptocurrency course.

## The passphrase

![The passphrase](https://youtu.be/dZkOYO7MXwc)

The passphrase is an additional password that can be integrated into a Bitcoin wallet to increase its security. Its use is optional and is at the discretion of the user. By adding arbitrary information that, together with the mnemonic phrase, allows the calculation of the wallet's seed, the passphrase enhances its security.

![image](assets/image/section3/8.JPG)

To derive the keys of an HD wallet, both the mnemonic phrase and the passphrase are necessary. The passphrase is free and can reach an almost infinite size. It is not included in the mnemonic phrase, which is standardized and must follow certain constraints of size, checksum, and encoding. An attacker cannot access a user's bitcoins without knowing the passphrase. The passphrase plays a role in the construction and calculation of all the wallet's keys.

The pbkdf2 function is used to generate the seed from the passphrase. This seed allows the derivation of all the child key pairs of the wallet. If the passphrase is changed, the Bitcoin wallet becomes completely different.

The passphrase is an essential tool to enhance the security of Bitcoin wallets. It can enable the application of various security strategies. For example, it can be used to create duplicates and facilitate backups of the mnemonic phrase. It can also improve the wallet's security by mitigating the risks associated with random generation of the mnemonic phrase.

An effective passphrase should be long (20 to 40 characters) and diversified (using uppercase letters, lowercase letters, numbers, and symbols). It should not be directly related to the user or their environment. It is safer to use a random sequence of characters rather than a simple word as a passphrase.

![image](assets/image/section3/9.JPG)

A passphrase is more secure than a simple password. The ideal passphrase is long, varied, and random. It can enhance the security of a wallet or hot software. It can also be used to create redundant and secure backups.

It is crucial to take care of passphrase backups to avoid losing access to the wallet. A passphrase is an option for an HD wallet. It can be randomly generated with dice or another pseudo-random number generator. It is not recommended to memorize a passphrase or mnemonic phrase.

In our next lesson, we will examine in detail the functioning of the seed and the first pair of keys generated from it. Feel free to follow this course to continue your learning. We look forward to seeing you very soon.

# Creation of Bitcoin Wallets

## Creation of the seed and master key

![Creation of the seed and master key](https://youtu.be/56yAt_JDWhY)

In this part of the course, we will explore the steps of deriving a Hierarchical Deterministic Wallet (HD Wallet), which allows for the creation and management of private and public keys in a hierarchical manner.

![image](assets/image/section4/0.JPG)

The foundation of the HD Wallet relies on two essential elements: the mnemonic phrase and the passphrase (optional additional password). Together, they constitute the seed, a 512-bit alphanumeric sequence that serves as the basis for deriving the wallet's keys. From this seed, it is possible to derive all the child key pairs of the Bitcoin wallet. The seed is the key that grants access to all the bitcoins associated with the wallet, whether you use a passphrase or not.

To obtain the seed, the pbkdf2 function (Password-Based Key Derivation Function 2) is used with the mnemonic phrase and the passphrase. The output of pbkdf2 is a 512-bit seed. The master private key and the master chain code are determined using the HMAC SHA-512 (Hash-based Message Authentication Code Secure Hash Algorithm 512) algorithm. This algorithm requires a message and a key to generate a result. The master private key is calculated from the seed and the phrase "Bitcoin SEED". This phrase is identical for all HD wallet derivations, ensuring consistency across wallets.

![image](assets/image/section4/1.JPG)

Initially, the SHA-512 function was not implemented in the Bitcoin protocol, which is why HMAC SHA-512 is used. The use of HMAC SHA-512 with the phrase "Bitcoin SEED" constrains the user to generate a wallet specific to Bitcoin. The result of HMAC SHA-512 is a 512-bit number, divided into two parts: the leftmost 256 bits represent the master private key, while the rightmost 256 bits represent the master chain code.

The master private key is the parent key of all future keys in the wallet, while the master chain code is involved in the derivation of child keys. It is important to note that it is impossible to derive a child key pair without knowing the corresponding chain code of the parent pair. The chain code adds a source of entropy to the derivation process.

A key pair in the wallet consists of a private key, a public key, and a chain code. The chain code allows for the introduction of randomness in the derivation of child keys and isolates each key pair to prevent any information leakage.

![image](assets/image/section4/2.JPG)

It is important to emphasize that the master private key is the first private key derived from the seed and has no connection to the extended keys of the wallet. Therefore, the seed is the fundamental element for deriving all the keys of the wallet. It differs from the mnemonic phrase and passphrase, which are used for seed creation.

In the next lesson, we will explore in detail the extended keys, such as xPub, xPRV, zPub, and understand why they are used and how they are constructed.

## Extended Keys

![Extended Keys](https://youtu.be/TRz760E_zUY)

In this part of the lesson, we will study the extended keys (xPub, zPub, yPub) and their prefixes, which play an important role in deriving child keys in an HD (Hierarchical Deterministic Wallet) wallet.

![image](assets/image/section4/3.JPG)

Extended keys are distinguished from master keys. An HD wallet generates a mnemonic phrase and a seed to obtain the master key and master chain code. Extended keys are used to derive child keys and require both the parent key and the corresponding chain code. An extended key combines these two pieces of information to simplify the derivation process.

Extended keys are identified by specific prefixes (XPRV, XPUB, YPUB, ZPUB) that indicate whether it is an extended private or public key, as well as its specific purpose. The metadata associated with an extended key includes the version (prefix), depth, public key fingerprint, index, and payload (chain code and parent key).

![image](assets/image/section4/4.JPG)

The payload consists of the chain code (32 bytes) and the parent key (33 bytes). These elements are essential for deriving child keys. A private key is generated from a random or pseudo-random number, while a public key is generated using the ECDSA (Elliptic Curve Digital Signature Algorithm) algorithm.

Each pair of extended keys is associated with a unique chain code, which allows for specific derivations. By concatenating the parent key with the chain code, an extended private or public key is obtained.

![image](assets/image/section4/5.JPG)

Extended public keys can only be derived from normal child public keys, while extended private keys can be derived from both public and private child keys, whether through normal or hardened derivation. Using extended keys with the XPUB prefix allows for deriving new addresses without going back to the corresponding private keys, thus providing better security. The metadata associated with extended keys provides important information about their role and position in the key hierarchy.

Compressed public keys have a size of 33 bytes, while uncompressed public keys are 512 bits. Compressed public keys retain the same information as uncompressed keys, but with a reduced size. Extended keys have a size of 82 bytes and their prefix is represented in base 58 through hexadecimal conversion. The checksum is calculated using the HASH256 hash function.

![image](assets/image/section4/6.JPG)

Hardened derivations start from indexes that are powers of 2 (2^31). Extended public keys only allow derivation of normal child public keys, while extended private keys allow derivation of any child key. It is worth noting that the most commonly used prefixes are xpub and zpub, which correspond to legacy and segwit v1 and segwit v0 standards, respectively.

In our next lesson, we will explore the derivation of child key pairs using the knowledge gained about extended keys and the wallet's master key.

In conclusion, extended keys play an essential role in cryptography and the operation of HD wallets. Understanding their use and calculation is crucial to ensure transaction security and the protection of digital assets. The prefixes and metadata associated with extended keys allow for efficient use and accurate derivation of necessary child keys.

## Derivation of Child Key Pairs

![Derivation of Child Key Pairs](https://youtu.be/FXhI-GmE9Aw)

Next, we will discuss the calculation of the seed and the master key, which are the first essential elements for the hierarchical organization and derivation of the HD wallet (Hierarchical Deterministic Wallet). The seed, with a length of 128 to 256 bits, is generated randomly or from a secret phrase. It plays a deterministic role in the derivation of all other keys. The master key is the first key derived from the seed, and it allows for the derivation of all other child key pairs.

The master chain code plays an important role in recovering the portfolio from the seed. It should be noted that all keys derived from the same seed will have the same master chain code.

![image](assets/image/section4/7.JPG)

The hierarchical and deterministic wallet (HD wallet) provides more efficient management of keys and wallet structures. Extended keys allow the derivation of a child key pair from a parent key pair using mathematical calculations and specific algorithms.

There are different types of child key pairs, including hardened keys and normal keys. The extended public key only allows the derivation of normal child public keys, while the extended private key allows the derivation of all child keys, both public and private, whether in normal or hardened mode. Each key pair has an index that distinguishes them from each other.

![image](assets/image/section4/8.JPG)

The derivation of child keys uses the HMAC-SHA512 function using the parent key concatenated with the index and the chain code associated with the key pair. Normal child keys have an index ranging from 0 to 2 to the power of 31 minus 1, while hardened child keys have an index ranging from 2 to the power of 31 to 2 to the power of 32 minus 1.

![image](assets/image/section4/9.JPG)
![image](assets/image/section4/10.JPG)

There are two types of child key pairs: hardened pairs and normal pairs. The process of deriving child keys uses the public keys to generate spending conditions, while the private keys are used for signing. The extended public key only allows the derivation of normal child public keys, while the extended private key allows the derivation of all child keys, both public and private, in normal or hardened mode.

![image](assets/image/section4/11.JPG)
![image](assets/image/section4/12.JPG)

Hardened derivation uses the parent private key, while normal derivation uses the parent public key. The HMAC-SHA512 function is used for hardened derivation, while normal derivation uses a 512-bit hash. The child public key is obtained by multiplying the child private key by the generator of the elliptic curve.

![image](assets/image/section4/13.JPG)
![image](assets/image/section4/14.JPG)

## Wallet Structure and Derivation Paths

![Wallet Structure and Derivation Paths](https://youtu.be/etO9UxwyE2I)

In this chapter, we will study the structure of the derivation tree in a Hierarchical Deterministic Wallet (HD Wallet). We have already explored the calculation of the seed, the master key, and the derivation of child key pairs. Now, we will focus on the organization of keys within the wallet.

The HD Wallet uses depth layers to organize the keys. Each derivation from a parent pair to a child pair corresponds to a depth layer. Depth 0 corresponds to the master key and the master chain code.

![image](assets/image/section4/15.JPG)

- Depth 1 is used to derive child keys for a specific purpose, which is determined by the index. The purposes are compliant with BIP 84 and Segwit v0/v1 standards.

- Depth 2 allows differentiation of accounts for different cryptocurrencies or networks. This allows organizing the wallet based on different sources of funds.

- Depth 3 is used to organize the wallet into different accounts, providing a clearer and more organized structure.

- Depth 4 corresponds to the external and internal chains, which are used for addresses intended to be publicly communicated. Index 0 is associated with the external chain, while index 1 is associated with the internal chain. Each account has two chains: the external chain (0) and the internal chain (1). Depth 4 is also used to manage script types in the case of multi-signature wallets.

- Depth 5 is used for receiving addresses in a standard wallet. In the next section, we will examine the derivation of child key pairs in more detail.

![image](assets/image/section4/16.JPG)

For each depth layer, we use indexes to differentiate the child key pairs. Hardened indexes are used with an apostrophe for certain derivations. The public key per year is used as input for the HMAC function. The index in a derivation path indicates the value used in the HMAC function.
The index without an apostrophe corresponds to the actual index used, while the index with an apostrophe corresponds to the actual index + 2^31. Reinforced derivations use indexes from 2^31 to 2^32-1. For example, index 44' corresponds to the actual index 2^31 + 44.
To generate a specific receiving address, we derive a pair of child keys from the master key and the master chain code. Then, we use the index to differentiate between different pairs of child keys at the same depth.

Extended keys, such as XPUB, allow you to share your wallet with multiple people. The derivation path is used to differentiate between the external chain (addresses intended to be communicated) and the internal chain (change addresses).

It is important to note that different depths are used in an HD wallet depending on different standards. Deriving parent keys to child keys allows for transitioning from one depth to another. The use of different branches in the HD wallet indicates the different standards followed.

In the next chapter, we will study receiving addresses, their advantages of use, and the steps involved in their construction.

# What is a Bitcoin address?

## Bitcoin addresses

![Bitcoin addresses](https://youtu.be/nqGBMjPtFNI)

In this chapter, we will explore receiving addresses, which play a crucial role in the Bitcoin system. They allow for receiving funds on a coin and are generated from pairs of private and public keys. Although there is a script type called Pay2PublicKey that allows for locking bitcoins to a public key, users generally prefer to use receiving addresses instead of this script.

![image](assets/image/section5/0.JPG)

When a recipient wants to receive bitcoins, they provide a receiving address to the sender instead of their public key. An address is actually a hash of a public key, with a specific format. The public key is derived from the child private key using mathematical operations such as point addition and doubling on elliptic curves.

![image](assets/image/section5/1.JPG)

It is important to note that it is not possible to reverse from an address to the public key, nor from the public key to the private key. Using an address helps reduce the size of the public key information, which initially is 512 bits. It is possible to compress a public key by only keeping the x value and adding a prefix, but this technique was not known at the time of Bitcoin's creation. Therefore, using an address does not save space in the blocks.

## How to create a Bitcoin address?

![How to create a Bitcoin address?](https://youtu.be/ewMGTN8dKjI)

In this chapter, we will discuss the construction of a receiving address for Bitcoin transactions. A receiving address is an alphanumeric representation of a compressed public key. The conversion of a public key into a receiving address goes through several steps.

![image](assets/image/section5/3.JPG)

One advantageous feature of receiving addresses is the presence of a checksum, which allows for error detection. For this, we use BCH (Bose-Chaudhuri-Hocquenghem) checksum technology, which ensures accurate error detection. This technology also contributes to reducing the number of characters required to represent an address, making it easier to use.

To start building an address, we need to compress the corresponding public key. A raw public key occupies 520 bits, but thanks to the symmetry of the elliptic curve used, an elliptic curve can have an x-coordinate associated with two possible values for y: positive or negative. On the Bitcoin network, we work with a finite set of positive integers rather than the set of real numbers. To represent a public key from x, we add a prefix indicating the value of y (even or odd). Compressing a public key reduces its size from 520 to 264 bits. The parity of y in a finite set of positive integers corresponds to the parity of y in the set of real numbers.

![image](assets/image/section5/4.JPG)
![image](assets/image/section5/5.JPG)

Let's take the example of the public key belonging to Satoshi Nakamoto, with a prefix 0,3 indicating an odd value of y. We can then move on to the second step of constructing an address from compressed public keys. It is possible to calculate two addresses for each public key. To do this, we use the SHA256 function to obtain the hash of the public key. Then, we apply the ripemd160 function to the result of SHA256 to obtain a string of characters. This string is then encoded in binary format in groups of 5 bits, to which metadata is added for checksum calculation using the BCH program.

![image](assets/image/section5/6.JPG)

In the case of legacy addresses, we use double SHA256 hashing to generate the address checksum. However, for Segwit V0 and V1 addresses, we rely on BCH checksum technology to ensure error detection. The BCH program is capable of suggesting and correcting errors with an extremely low probability of error. Currently, the BCH program is used to detect and suggest modifications, but it does not automatically make them on behalf of the user. The calculation of the checksum with the BCH code is based on polynomial Chien-Chauffage arithmetic.

![image](assets/image/section5/7.JPG)

The BCH program requires several input information, including the HRP (Human Readable Part) that needs to be expanded. Expanding the HRP involves encoding each letter in base 2, taking the first three bits of each character by inserting a separator 0, and then concatenating the last five bits of each character. The blue characters converted to base 10 correspond to 3 and 3 in decimal, while the other five orange characters correspond to 2 and 3 in base 10. The extension of the HRP in base 10 allows isolating the last five bits of each character, thus reinforcing the checksum.

![image](assets/image/section5/8.JPG)

The Segwit V0 version is represented by the code 00 and the "payload" is in black, in base 10. This is followed by six characters reserved for the checksum. The input containing the metadata is then submitted to the BCH program to obtain the checksum in base 10. The concatenation of the version, payload, and checksum allows building the address. The base 10 characters are then converted to bech32 characters using a mapping table. The bech32 alphabet includes all alphanumeric characters, except 1, b, i, and o, to avoid confusion.

![image](assets/image/section5/9.JPG)
![image](assets/image/section5/10.JPG)

To build an address starting with bc1q, we need to apply a hash function (H160) to a compressed public key, then add the checksum, the version (q), the HRP (bc), and the separator (1). Taproot addresses, on the other hand, start with bc1p because their version (Segwit V1) corresponds to 0+1=1, hence the use of the character p. All these elements are then converted to BCH32, a Bitcoin-specific variant of base 32.

Thus, we have gone through the steps of constructing a receiving address, the use of BCH checksum technology, as well as the construction of an address starting with bc1q or bc1p using the BCH32 variant of Bitcoin-specific base 32.

## Summary of Cryptography for Bitcoin Wallets

![training summary](https://youtu.be/NkAYoVUMvOs)

Throughout this training, we have studied in depth the Hierarchical Deterministic (HD) wallet with BIP32. Entropy plays a central role in this type of wallet, as it is used to generate a mnemonic phrase from a random number. With the list of 2048 words provided in BIP39, this mnemonic phrase can be encoded into a series of easy-to-remember words. The mnemonic phrase, along with an optional passphrase, is necessary to generate the wallet's seed. The passphrase acts as a cryptographic salt that adds an extra layer of protection to the wallet.

![image](assets/image/section5/11.JPG)

The pbkdf2 function is used to generate the seed from the mnemonic phrase and passphrase, using hmacha512 and 2048 iterations. The master key and master chain code are then derived from this seed using the hmacha512 function again with the phrase "bitcoin seed". The master private key and master chain code are the highest elements in the HD wallet hierarchy.

![image](assets/image/section5/12.JPG)

The derivation of a child key depends on several factors, including the parent key and the corresponding chain code. An extended key is obtained by concatenating a parent key with its chain code, while a master key is a separate key. To derive an address, the compressed public key is first hashed using SHA256 and RIPMD160, and then a checksum is calculated. Double SHA256 hashing is used to calculate the checksum in the case of a legacy standard, while the BCH (Bose-Chaudhuri-Hocquenghem) program is used to calculate the checksum in the case of a segwit standard. Then, a base 58 format representation is used for a legacy standard, while the bech32 format is used for a segwit standard, to obtain the HD wallet address.

![image](assets/image/section5/13.JPG)

In summary, we have explored in detail the hash functions and their characteristics, as well as digital signatures and elliptic curves. We then delved into the world of Hierarchical Deterministic (HD) wallets with BIP32, using entropy and passphrase to generate the wallet seed. We also learned how to derive child keys and obtain the HD wallet address. I hope this information has been helpful to you, and I now encourage you to proceed to the assessment to test your knowledge gained during the Crypto 301 course. Thank you for your attention.

# Go further

## Creating a seed from 128 dice rolls!

![Creating a seed from 128 dice rolls!](https://youtu.be/lUw-1kk75Ok)

The creation of a mnemonic phrase is a crucial step in securing your cryptocurrency portfolio. There are several methods to generate a mnemonic phrase, however, we will focus on the manual generation method using dice. It is important to note that this method is not suitable for a high-value wallet. It is recommended to use open-source software or a hardware wallet to generate the mnemonic phrase. To create a mnemonic phrase, we will use dice to generate binary information. The goal is to understand the process of creating the mnemonic phrase.

**Step 1 - Preparation:**
Make sure you have an amnesic Linux distribution, such as Tails OS, installed on a USB drive for added security. Note that this tutorial should not be used to create a primary wallet.

**Step 2 - Generating a random binary number:**
We will use dice to generate binary information. Roll a die 128 times and note each result (1 for odd, 0 for even).

**Step 3 - Organizing the binary numbers:**
Organize the obtained binary numbers into rows of 11 digits to facilitate further calculations. The twelfth row should only have 7 digits.

**Step 4 - Calculating the checksum:**
The last 4 digits for the twelfth row correspond to the checksum. To calculate this checksum, we need to use a terminal from a Linux distribution. It is recommended to use [TailOs](https://tails.boum.org/index.fr.html), which is a memoryless distribution bootable from a USB drive. Once on your terminal, enter the command `echo <binary number> | shasum -a 254 -0`. Replace `<binary number>` with your list of 128 zeros and ones. The output is a hexadecimal hash. Take note of the first character of this hash and convert it to binary. You can use this [table](https://www.educative.io/answers/decimal-binary-and-hex-conversion-table) for assistance. Add the binary checksum (4 digits) to the twelfth row of your sheet.

**Step 5 - Conversion to decimal:**
To find the words associated with each of your lines, you first need to convert each series of 11 bits into decimal. Here you cannot use an online converter because these bits represent your mnemonic phrase. So you will need to convert using a calculator and a trick as follows: each bit is associated with a power of 2, so from left to right we have 11 ranks corresponding to 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1. To convert your series of 11 bits into decimal, you just need to add up the ranks that contain a 1. For example, for the series 00110111011, this corresponds to the following addition: 256 + 128 + 32 + 16 + 8 + 2 + 1 = 443. You can now convert each line to decimal. And before moving on to encoding into words, you need to add +1 to all the lines because the index of the BIP39 word list starts from 1 and not 0.

**Step 8 - Generation of the mnemonic phrase:**
Start by printing the [list of 2048 words](https://seedxor.com/files/wordlist.pdf) to convert between your decimal numbers and the BIP39 words. The peculiarity of this list is that no word has the same first 4 letters in common with all the other words in this dictionary. Then, for each of your lines, look for the word associated with the decimal number.

**Step 9 - Testing the mnemonic phrase:**
Immediately test your mnemonic phrase on Sparrow Wallet by creating a wallet from it. If you get an invalid checksum error, it is likely that you made a calculation error. Correct this error by going back to step 4 and test again on Sparrow Wallet. There you go! You have just created a new Bitcoin wallet from 128 dice rolls.

Generating a mnemonic phrase is an important process for securing your cryptocurrency wallet. It is recommended to use more secure methods, such as the use of open source software or hardware wallets, to generate the mnemonic phrase. However, completing this workshop helps to better understand how we can create a Bitcoin wallet from a random number.

## Conclusion and end

### Acknowledgments and keep digging the rabbit hole

We would like to sincerely thank you for attending the Crypto 301 training. We hope that this experience has been enriching and educational for you. We have covered many exciting topics, ranging from mathematics to cryptography to the workings of the Bitcoin protocol.

If you wish to delve further into the subject, we have an additional resource to offer you. We have conducted an exclusive interview with Théo Pantamis and Loïc Morel, two renowned experts in the field of cryptography. This interview delves deep into various aspects of the subject and offers interesting perspectives.

Feel free to watch this interview to continue exploring the fascinating field of cryptography. We hope that it will be useful and inspiring in your journey. Once again, thank you for your participation and commitment throughout this training.

### Support Us

This course, along with all the content available on this university, has been provided to you for free by our community. To support us, you can share it with others, become a member of the university, and even contribute to its development via GitHub. On behalf of the entire team, thank you!

### Rate the Training

A rating system for the training will soon be integrated into this new E-learning platform! In the meantime, thank you very much for taking the course, and if you enjoyed it, please consider sharing it with others.
