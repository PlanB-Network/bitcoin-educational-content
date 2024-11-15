---
name: Introduction to the Cryptographic Algorithms of Bitcoin
goal: Understand the creation of a Bitcoin wallet from a cryptographic perspective
objectives:
  - Demystify cryptography terminology related to Bitcoin.
  - Master the creation of a Bitcoin wallet.
  - Understand the structure of a Bitcoin wallet.
  - Understand addresses and derivation paths.
---

# A Journey into Cryptography

Are you fascinated by Bitcoin? Wondering how a Bitcoin wallet works? Get ready to embark on a captivating journey into cryptography! Loïc, our expert, will guide you through the intricacies of creating a Bitcoin wallet, unraveling the mysteries behind intimidating technical terms such as hashing, key derivation, and elliptic curves.

This training will not only equip you with the knowledge to understand the structure of a Bitcoin wallet but also prepare you to delve deeper into the exciting world of cryptography. So, are you ready to embark on this journey? Join us and turn your curiosity into expertise!

+++

# Introduction
<partId>32960669-d13a-592f-a053-37f70b997cbf</partId>

## Introduction to Cryptography
<chapterId>fb4e8857-ea35-5a8a-ae8a-5300234e0104</chapterId>

### Is this training for you? YES!

We are delighted to welcome you to the new training course titled "Crypto 301: Introduction to Cryptography and HD Wallet", led by the expert in the field, Loïc Morel. This course will immerse you in the fascinating world of cryptography, the fundamental discipline of mathematics that ensures the encryption and security of your data.

In our daily lives, and particularly in the realm of Bitcoin, cryptography plays a crucial role. Concepts related to cryptography, such as private keys, public keys, addresses, derivation paths, seed, and entropy, are at the core of using and creating a Bitcoin wallet. Throughout this course, Loïc will explain in detail how private keys are generated and how they are linked to addresses. Loïc will also dedicate an hour to explaining the mathematical details of elliptic curves. Additionally, you will understand why the use of HMAC SHA512 is important for securing your wallet and what the difference is between a seed and a mnemonic phrase.
The ultimate goal of this training is to enable you to understand the technical processes involved in creating an HD wallet and the cryptographic methods used. Over the years, Bitcoin wallets have evolved to become easier to use, more secure, and standardized thanks to specific BIPs. Loïc will help you understand these BIPs to grasp the choices made by Bitcoin developers and cryptographers. Like all the trainings offered by our university, this one is completely free and open source. This means that you are free to take it and use it as you wish. We look forward to receiving your feedback at the end of this exciting course.

### The floor is yours, professor!

Hello everyone, I'm Loïc Morel, your guide through this technical exploration of the cryptography used in Bitcoin wallets.

Our journey begins with a dive into the depths of cryptographic hash functions. Together, we will dissect the inner workings of the essential SHA256 and explore various algorithms dedicated to derivation.

We will continue our adventure by deciphering the mysterious world of digital signatures. You will discover how the magic of elliptic curves applies to these signatures, and we will shed light on how to calculate the public key from the private key. And of course, we will delve into the process of digital signature.

Next, we will go back in time to see the evolution of Bitcoin wallets, and we will venture into the concepts of entropy and random numbers. We will review the famous mnemonic phrase, while also touching on the passphrase. You will even have the opportunity to experience something unique by creating a seed from 128 dice rolls!

With these solid foundations, we will be ready for the crucial part: creating a Bitcoin wallet. From the birth of the seed and the master key, to the study of extended keys, and the derivation of child key pairs, each step will be dissected. We will also discuss the structure of the wallet and derivation paths.

To top it all off, we will conclude our journey by examining Bitcoin addresses. We will explain how they are created and how they play an essential role in the functioning of Bitcoin wallets.

Join me on this captivating journey, and get ready to explore the world of cryptography like never before. Leave your preconceptions at the door and open your mind to a new way of understanding Bitcoin and its fundamental structure.

# Hash Functions
<partId>3713fee1-2ec2-512e-9e97-b6da9e4d2f17</partId>

## Introduction to cryptographic hash functions related to Bitcoin
<chapterId>dba011f5-1805-5a48-ac2b-4bd637c93703</chapterId>

Welcome to today's session dedicated to an in-depth immersion into the cryptographic world of hash functions, a crucial cornerstone of Bitcoin protocol security. Imagine a hash function as an ultra-efficient cryptographic deciphering robot that transforms information of any size into a unique and fixed-size digital fingerprint, called a "hash," "digest," or "checksum."
In summary, a hash function takes an input message of arbitrary size and converts it into a fixed-size output fingerprint.

Describing the profile of cryptographic hash functions requires understanding two essential qualities: their irreversibility and their resistance to forgery.

Irreversibility, or resistance to preimage, means that calculating the output given the input can be done easily, but calculating the input from the output is impossible.
It is a one-way function.

![image](assets/image/section1/0.webp)

Resistance to forgery comes from the fact that even the slightest modification of the input will result in a profoundly different output.
These functions allow for verifying the integrity of downloaded software.

![image](assets/image/section1/1.webp)

Another crucial characteristic they possess is their resistance to collisions and second preimage. A collision occurs when two distinct inputs produce the same output.
Certainly, in the hashing universe, collisions are inevitable, but an excellent cryptographic hash function minimizes them significantly. The risk must be so low that it can be considered negligible. It's as if each hash were a house in a vast city; despite the enormous number of houses, a good hash function ensures that each house has a unique address.

Resistance to second preimage depends on resistance to collisions; if there is resistance to collisions, then there is resistance to second preimage.
Given an input information that is imposed on us, we must find a second input, different from the first, that produces a collision in the output hash of the function. Resistance to second preimage is similar to resistance to collisions, except that the input is imposed.
Let us now navigate the tumultuous waters of outdated hash functions. SHA0, SHA1, and MD5 are now considered rusty shells in the ocean of cryptographic hashing. They are often discouraged as they have lost their resistance to collisions. The pigeonhole principle explains why, despite our best efforts, collision avoidance is impossible due to the limitation of the output size. To truly be considered secure, a hash function must resist collisions, second preimages, and preimages.

A key element in the Bitcoin protocol, the SHA-256 hash function is the captain of the ship. Other functions, such as SHA-512, are used for derivation with HMAC and PBKDF. Additionally, RIPMD160 is used to reduce a fingerprint to 160 bits. When we refer to HASH256 and HASH160, we are referring to the use of double hashing with SHA-256 and RIPMD.

For HASH256, it is a double hash of the message using the SHA256 function.
$$
SHA256(SHA256(message))
$$
For HASH160, it is a double hash of the message using SHA256 first, then RIPMD160.
$$
RIPMD160(SHA256(message))
$$
The use of HASH160 is particularly advantageous as it allows for the security of SHA-256 while reducing the size of the fingerprint.

In summary, the ultimate goal of a cryptographic hash function is to transform arbitrary-sized information into a fixed-size fingerprint. To be recognized as secure, it must have several strengths: irreversibility, resistance to tampering, resistance to collisions, and resistance to second preimages.

![image](assets/image/section1/2.webp)

At the end of this exploration, we have demystified cryptographic hash functions, highlighted their uses in the Bitcoin protocol, and dissected their specific objectives. We have learned that for hash functions to be considered secure, they must be resistant to preimages, second preimages, collisions, and tampering. We have also covered the range of different hash functions used in the Bitcoin protocol. In our next session, we will delve into the core of the SHA256 hash function and discover the fascinating mathematics that give it its unique characteristics.

## The Inner Workings of SHA256
<chapterId>905eb320-f15b-5fb6-8d2d-5bb447337deb</chapterId>

Welcome to the continuation of our fascinating journey through the cryptographic mazes of the hash function. Today, we unveil the mysteries of SHA256, a complex yet ingenious process that we introduced earlier.
As a skilled professional translator, my primary task is to accurately translate technical content from French into English while adhering to the provided guidelines. Here is the translation of the text:

As a reminder, the purpose of the SHA256 hash function is to take an input message of any size and generate a 256-bit hash as output.

### Pre-processing

Let's take a step further in this labyrinth by starting with the pre-processing of SHA256.

#### Padding Bits

The objective of this first step is to have a message that is equalized to a multiple of 512 bits. To achieve this, we will add padding bits to the message.

Let M be the initial message size.
Let 1 be a bit reserved for the separator.
Let P be the number of bits used for padding, and 64 be the number of bits set aside for the second pre-processing phase.
The total should be a multiple of 512 bits, which is represented by n.

![image](assets/image/section1/3.webp)

Example with an input message of 950 bits:

```
Step 1: Determine the size; the final desired number of bits.
The first multiple of 512 > (M + 64 + 1) (with M = 950) is 1024.
1024 = 2 * 512
So n = 2.

Step 2: Determine P, the number of padding bits needed to reach the final desired number of bits.
-> M + 1 + P + 64 = n * 512
-> M + 1 + P + 64 = 2 * 512
-> 950 + 1 + P + 64 = 1024
-> P = 1024 - 1 - 64 - 950
-> P = 9

Therefore, 9 padding bits need to be added to have a message equalized to a multiple of 512.
```

And now?
Right after the initial message, the separator 1 followed by P, which in our example is nine 0s, needs to be added.

```
message + 1 000 000 000
```

#### Size Padding

We now move on to the second phase of pre-processing, which involves adding the binary representation of the size of the initial message in bits.

Let's revisit the example with an input of 950 bits:

```
The binary representation of the number 950 is: 11 1011 0110

We use our 64 reserved bits from the previous step. We add zeros to round our 64 bits to our equalized input. Then, we merge the initial message, the padding bits, and the size padding to obtain our equalized input.
```

Here is the result:

![image](assets/image/section1/4.webp)

### Processing

#### Understanding Prerequisites

##### Constants and Initialization Vectors

Now, we are preparing for the initial steps of processing the SHA-256 function. Just like in any good recipe, we need some basic ingredients, which we call constants and initialization vectors.

The initialization vectors, from A to H, are the first 32 bits of the decimal parts of the square roots of the first 8 prime numbers. They will serve as base values in the initial processing steps. Their values are in hexadecimal format.

The constants K, from 0 to 63, represent the first 32 bits of the decimal parts of the cubic roots of the first 64 prime numbers. They are used in each round of the compression function. Their values are also in hexadecimal format.

![image](assets/image/section1/5.webp)

##### Used Operations

Within the compression function, we use specific operators such as XOR, AND, and NOT. We process the bits one by one according to their position, using the XOR operator and a truth table. The AND operator is used to return 1 only if both operands are equal to 1, and the NOT operator is used to return the opposite value of an operand. We also use the SHR operation to shift the bits to the right by a chosen number.

The truth table:

![image](assets/image/section1/6.webp)

Bit shift operations:

![image](assets/image/section1/7.webp)

#### The Compression Function

Before applying the compression function, we divide the input into blocks of 512 bits. Each block will be processed independently of the others.

Each 512-bit block is then further divided into 32-bit chunks called W. In this way, W(0) represents the first 32 bits of the 512-bit block. W(1) represents the next 32 bits, and so on, until we reach the 512 bits of the block.

Once all the constants K and the chunks W are defined, we can perform the following calculations for each chunk W in each round.

We perform 64 rounds of calculations in the compression function. In the last round, at the "Output of the function" level, we will have an intermediate state that will be added to the initial state of the compression function.

Then, we repeat all these steps of the compression function on the next 512-bit block, until the last block.

All additions in the compression function are modulo 2^32 additions to always keep a 32-bit sum.

![image](assets/image/section1/9.webp)

![image](assets/image/section1/8.webp)

##### One Round of the Compression Function

![image](assets/image/section1/11.webp)

![image](assets/image/section1/10.webp)

The compression function will be performed 64 times. We have our pieces W and our previously defined constants K as input.
The red squares/crosses correspond to a modulo 2^32-bit addition.

The inputs A, B, C, D, E, F, G, H will be associated with a 32-bit value to make a total of 32 * 8 = 256 bits.
We also have a new sequence A, B, C, D, E, F, G, H as output. This output will then be used as input for the next round and so on until the end of the 64th round.

The values of the input sequence for the first round of the compression function correspond to the predefined initialization vectors mentioned earlier.
As a reminder, the initialization vectors represent the first 32 bits of the decimal parts of the square roots of the first 8 prime numbers.

Here is an example of a round:

![image](assets/image/section1/12.1.webp)

##### Intermediate State

As a reminder, the message is divided into blocks of 512 bits, which are then divided into 32-bit pieces. For each 512-bit block, we apply the 64 rounds of the compression function.
The intermediate state corresponds to the end of the 64 rounds of a block. The values of the output sequence from this 64th round are used as initial values for the input sequence of the first round of the next block.

![image](assets/image/section1/12.2.webp)

#### Overview of the hash function

![image](assets/image/section1/13.webp)

We can notice that the output of the first 512-bit message piece corresponds to our initialization vectors as input for the second 512-bit message piece, and so on.

The output of the last round, of the last piece, corresponds to the final result of the SHA256 function.

In conclusion, we would like to emphasize the crucial role of the calculations performed in the CH, MAJ, σ0, and σ1 boxes. These operations, among others, are the guardians that ensure the robustness of the SHA256 hash function against attacks, making it a preferred choice for securing many digital systems, especially within the Bitcoin protocol. It is evident that, although complex, the beauty of SHA256 lies in its ability to find the input from the hash, while verifying the hash for a given input is a mechanically simple action.

## The algorithms used for derivation
<chapterId>cc668121-7789-5e99-bf5e-1ba085f4f5f2</chapterId>

The HMAC and PBKDF2 derivation algorithms are key components in the security mechanism of the Bitcoin protocol. They prevent a variety of potential attacks and ensure the integrity of Bitcoin wallets.
HMAC and PBKDF2 are cryptographic tools used for various tasks in Bitcoin. HMAC is primarily used to counter length extension attacks when deriving Hierarchical Deterministic (HD) wallets, while PBKDF2 is used to convert a mnemonic phrase into a seed.

#### HMAC-SHA512

The HMAC-SHA512 pair has two inputs: a message m (Input 1) and a key K arbitrarily chosen by the user (Input 2). It also has a fixed-size output: 512 bits.


Let's note:
- m: arbitrary-sized message chosen by the user (input 1)
- K: arbitrary key chosen by the user (input 2)
- K': equalized key K. It has been adjusted to the size B of the blocks.
- ||: concatenation operation.
- opad: constant defined by the byte 0x5c repeated B times.
- ipad: constant defined by the byte 0x36 repeated B times.
- B: The size of the blocks of the hash function used.


![image](assets/image/section1/14.webp)

HMAC-SHA512, which takes a message and a key as inputs, generates a fixed-size output. To ensure uniformity, the key is adjusted based on the size of the blocks used in the hash function. In the context of HD wallet derivation, HMAC-SHA-512 is used. It operates with 1024-bit (128-byte) blocks and adjusts the key accordingly. It uses the constants OPAD (0x5c) and IPAD (0x36), repeated as necessary to enhance security.

The HMAC-SHA-512 process involves concatenating the result of SHA-512 applied to the key XOR OPAD and the key XOR IPAD with the message. When used with 1024-bit (128-byte) blocks, the input key is padded with zeros if necessary, then XORed with IPAD and OPAD. The modified key is then concatenated with the message.

![image](assets/image/section1/15.webp)

The inclusion of a salt in the string code increases the security of derived keys. Without it, an attack could compromise the entire wallet and steal all bitcoins.

PBKDF2 is used to convert a mnemonic phrase into a seed. This algorithm performs 2048 rounds using HMAC SHA512. Through these derivation algorithms, different inputs can produce a unique and fixed output, which mitigates the issue of possible length extension attacks on SHA-2 family functions.
A length extension attack exploits a specific property of certain cryptographic hash functions. In such an attack, an attacker who already possesses the hash of an unknown message can use it to calculate the hash of a longer message, which is an extension of the original message. This is often possible without knowing the content of the original message, which can lead to significant security vulnerabilities if this type of hash function is used for tasks such as integrity verification.

![image](assets/image/section1/16.webp)

In conclusion, HMAC and PBKDF2 algorithms play essential roles in the security of HD wallet derivation in the Bitcoin protocol. HMAC-SHA-512 is used to protect against length extension attacks, while PBKDF2 allows the conversion of the mnemonic phrase into a seed. The string code adds an additional source of entropy in key derivation, ensuring the robustness of the system.

# Digital Signatures
<partId>76b58a00-0c18-54b9-870d-6b7e34029db8</partId>

## Digital Signatures and Elliptic Curves
<chapterId>c9dd9672-6da1-57f8-9871-8b28994d4c1a</chapterId>

Where are these famous bitcoins stored? Not in a Bitcoin wallet, as one might think. In reality, a Bitcoin wallet stores the private keys necessary to prove ownership of the bitcoins. The bitcoins themselves are recorded on the blockchain, a decentralized database that archives all transactions.

In the Bitcoin system, the unit of account is the bitcoin (note the lowercase "b"). It is divisible up to eight decimal places, with the smallest unit being the satoshi. UTXOs, or "Unspent Transaction Outputs," represent the unspent transaction outputs belonging to a public key that is mathematically linked to a private key. To spend these bitcoins, one must be able to satisfy the spending condition of the transaction. A typical spending condition involves proving to the rest of the network that the user is the legitimate owner of the public key associated with the UTXO. To do this, the user must demonstrate possession of the private key corresponding to the public key linked to each UTXO without revealing the private key.

This is where the digital signature comes in. It serves as mathematical proof of possession of a private key associated with a specific public key. This data protection technique is primarily based on a fascinating field of cryptography called elliptic curve cryptography (ECC).

The signature can be mathematically verified by other participants in the Bitcoin network.

![image](assets/image/section2/0.webp)

To ensure the security of transactions, Bitcoin relies on two digital signature protocols: ECDSA (Elliptic Curve Digital Signature Algorithm) and Schnorr. ECDSA has been a signature protocol integrated into Bitcoin since its launch in 2009, while Schnorr signatures were added more recently in November 2021. Although both protocols are based on elliptic curve cryptography and use similar mathematical mechanisms, they mainly differ in terms of signature structure.

In this course, we will present the ECDSA algorithm.

### What is an elliptic curve?

Elliptic curve cryptography is a set of algorithms that use an elliptic curve for its various geometric and mathematical properties in a cryptographic context, with security based on the difficulty of calculating the discrete logarithm.

Elliptic curves are useful in a variety of cryptographic applications in the Bitcoin protocol, ranging from key exchanges to asymmetric encryption and digital signatures.

Elliptic curves have interesting properties:

- Symmetry: Any non-vertical line intersecting two points on the elliptic curve will intersect the curve at a third point.
- Any non-vertical line tangent to the curve at a point will always intersect the curve at a unique second point.

The Bitcoin protocol uses a specific elliptic curve called Secp256k1 for its cryptographic operations.

Before delving deeper into these signature mechanisms, it is important to understand what an elliptic curve is. An elliptic curve is defined by the equation y² = x³ + ax + b. Every point on this curve has a distinctive symmetry that is key to its usefulness in cryptography.

![image](assets/image/section2/1.webp)

Ultimately, various elliptic curves are recognized as secure for cryptographic use. The most well-known may be the secp256r1 curve. However, for Bitcoin, Satoshi Nakamoto opted for a different curve: secp256k1.

This curve is defined by the parameters a=0 and b=7, and its equation is y² = x³ + 7 modulo n, where n represents the prime number that determines the curve's order.

![image](assets/image/section2/2.webp)

The first image represents the secp256k1 curve over the real field and its equation.
The second image is a representation of the secp256k1 curve over the field ZP, the field of positive natural numbers, modulo p where p is a prime number. It looks like a cloud of points. We use this field of positive natural numbers to avoid approximations.
p is a prime number, and it is the order of the curve that is used.
Finally, the equation used in the Bitcoin protocol is:$$
y^2 = (x^3 + 7) mod(p) $$
The equation of the elliptic curve in Bitcoin corresponds to the last equation in the previous image.

In the next section of this course, we will use curves that are on the real field simply to facilitate understanding.

## Calculating the public key from the private key
<chapterId>fcb2bd58-5dda-5ecf-bb8f-ad1a0561ab4a</chapterId>

To begin, let's delve into the world of the Elliptic Curve Digital Signature Algorithm (ECDSA). Bitcoin utilizes this digital signature algorithm to link private and public keys. In this system, the private key is a random or pseudo-random 256-bit number. The total number of possibilities for a private key is theoretically 2^256, but in reality, it is slightly less than that. To be precise, some 256-bit private keys are not valid for Bitcoin.

To be compatible with Bitcoin, a private key must be between 1 and n-1, where n represents the order of the elliptic curve. This means that the total number of possibilities for a Bitcoin private key is almost equal to 1.158 x 10^77. To put this into perspective, it's roughly the same number of atoms present in the observable universe.

![image](assets/image/section2/3.webp)

The unique private key, denoted as k, is then used to determine a public key.

The public key, denoted as K, is a point on the elliptic curve that is derived from the private key using irreversible algorithms like ECDSA. When we have knowledge of the private key, it is very easy to retrieve the public key, but when we only have the public key, it is impossible to retrieve the private key. This irreversibility is the cornerstone of Bitcoin wallet security.

The public key is 512 bits long as it corresponds to a point on the curve with an x-coordinate of 256 bits and a y-coordinate of 256 bits. However, it can be compressed into a 264-bit number.

![image](assets/image/section2/4.webp)

The generator point (G) is the point on the curve from which all public keys are generated in the Bitcoin protocol. It has specific x and y coordinates, usually represented in hexadecimal. For secp256k1, the coordinates of G are, in hexadecimal:

- `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
- `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8`
This point is useful for deriving all public keys. To calculate the public key K, simply multiply point G by the private key k, such that: K = k.G

We will now study how to add and multiply points on elliptic curves.

#### Addition and doubling of points on elliptic curves

##### Adding two points M + L

One of the remarkable properties of elliptic curves is that a non-vertical line intersecting the curve at two points will also intersect it at a third point, called point O in our example. This property is used to determine point U, which is the opposite of point O.

M + L = U

![image](assets/image/section2/5.webp)

##### Adding a point to itself = Point doubling

Adding a point G to itself is done by drawing a tangent to the curve at that point. This tangent, according to the properties of elliptic curves, will intersect the curve at a second unique point -J. The opposite of this point, J, is the result of adding point G to itself.
G + G = J

In fact, point G is the starting point for calculating all public keys of Bitcoin system users.

![image](assets/image/section2/6.webp)

#### Scalar multiplication on elliptic curves

Scalar multiplication of a point by n is equivalent to adding that point to itself n times.

Similar to point doubling, scalar multiplication of point G by a point n is done by drawing a tangent to the curve at point G. This tangent, according to the properties of elliptic curves, will intersect the curve at a second unique point -2G. The opposite of this point, 2G, is the result of adding point G to itself.

If n = 4, then the operation is repeated until reaching 4G.

![image](assets/image/section2/7.webp)

Here is an example calculation for 3G:

![image](assets/image/section2/8.webp)

These operations on points of an elliptic curve are the basis for calculating public keys. Deriving a public key knowing the private key is very easy.
A public key is a point on the elliptic curve, it is the result of our addition and doubling of point G k times. With k = private key.

In this example:

- The private key k = 4
- The public key K = kG = 4G

![image](assets/image/section2/9.webp)

Knowing the private key k, it is easy to calculate the public key K. However, it is impossible to retrieve the private key based on the public key. Is this the result of an addition or a doubling of points?

In our next lesson, we will explore how a digital signature is created using the ECDSA algorithm with a private key to spend bitcoins.

## Signing with the private key
<chapterId>bb07826f-826e-5905-b307-3d82001fb778</chapterId>

The process of digital signature is a key method to prove that you are the holder of a private key without revealing it. This is achieved using the ECDSA algorithm, which involves determining a unique nonce, calculating a specific number V, and creating a digital signature composed of two parts, S1 and S2.
It is crucial to always use a unique nonce to avoid security attacks. A notorious example of what can happen when this rule is not followed is the hacking of the PlayStation 3, which was compromised due to nonce reuse.

![](assets/image/section2/10.webp)

Steps:

- Determine a nonce v, which is a unique random number.
  Nonce = Number Only Used Once.
  It is determined by the one performing the signature.
- Calculate by adding and doubling points on an elliptic curve from point G, the position of V on the elliptic curve.
  Such that V = v.G
  x and y are the coordinates of V on the plane.
- Calculate S1.
  S1 = x mod n with n = the order of the curve and x a coordinate of V on the plane.
  Note: The number of possible public keys is greater than the number of points on the elliptic curve in the finite field of positive integers used in Bitcoin.
  The order of the curve corresponds only to the possibilities that the public key can take on the curve.
- Calculate S2.
  H(Tx) = Hash of the transaction
  k = the private key
- Calculate the signature: the concatenation of S1 + S2.
- Calculate P, the signature verification calculation.
  K = the public key

For example, to obtain the public key 3G, you draw a tangent to point G, calculate the opposite of -G to obtain 2G, and then add G and 2G. To perform a transaction, you must prove that you know the number 3 by unlocking the bitcoins associated with the public key 3G.

To create a digital signature and prove that you know the private key associated with the public key 3G, you first calculate a nonce, then the point V associated with this nonce (in the given example, it is 4G). Then, you calculate the point T by adding the public key 3G and the point V, which gives 7G.

![image](assets/image/section2/11.webp)

Let's simplify the process of digital signature.
In the previous image, the private key k = 3.
We can easily calculate the public key K associated with this private key: K = 3G.
Then, we generate a nonce pseudo-randomly: v = 4.
From this nonce, it is possible to calculate V such that: V = v.G = 4G.

From this point V, we calculate the point T such that:
T = t.G = 7G (with t = 7).

Now it's time to proceed with the verification of the digital signature.

Verifying a digital signature is a crucial step in using the ECDSA algorithm, which allows confirming the authenticity of a signed message without needing the sender's private key. Here's how it works in detail:

In our example, we have two important values: t and V.
t is a numerical value (7 in this example), and V is a point on the elliptic curve (represented by 4G here). These values are generated during the creation of the digital signature and are then sent along with the message to enable verification.

When the verifier receives the message, they will also receive these two values, t and V.

Here are the steps that the verifier will follow to validate the signature:

1. First, they will calculate the hash of the message, which we will call H.
2. Then, they will calculate u1 and u2. To do this, they will use the following formulas:
   - u1 = H /\* (S2)^-1 mod n
   - u2 = T /\* (S2)^-1 mod n
     Where S2 is the second part of the digital signature, n is the order of the elliptic curve, and (S2)^-1 is the inverse of S2 mod n.
3. The verifier will then calculate a point P' on the elliptic curve using the formula: P' = u1 _ G + u2 _ K
   - G is the generator point of the curve
   - K is the sender's public key
4. The verifier will then calculate I', which is simply the x-coordinate of the point P' modulo n.
5. Finally, the verifier will confirm that I' is equal to t. If this is the case, the signature is considered valid. If not, the signature is invalid.
This procedure ensures that only the sender possessing the corresponding private key could have produced a signature that passes this verification process.

![image](assets/image/section2/12.webp)

In simpler terms:
The person producing the signature will provide the number t (in our example, t = 7) and the point V to the person verifying it.

It is impossible to determine the public key or private key from the number 7 and the number V.

The steps for verifying the digital signature are as follows:

- On the curve, the verifier adds the point of the public key to the point V to retrieve the point T'.
- The verifier calculates the number t.G.
- The verifier checks that the result of t.G is indeed equal to the number T'.

In conclusion, verifying a digital signature is an essential procedure in Bitcoin transactions. It ensures that the signed message has not been altered during transmission and that the sender is indeed the holder of the private key. This digital authentication technique is based on complex mathematical principles, including elliptic curve arithmetic, while maintaining the confidentiality of the private key. It provides a solid security foundation for cryptographic transactions.

That being said, the management of these keys, as well as their creation, is another essential question in Bitcoin. How to generate a new key pair? How to securely and efficiently organize a multitude of keys? How to recover them if necessary?

To answer these questions and deepen your understanding of cryptography security, our next course will focus on the concept of Hierarchical Deterministic Wallets (HD wallets) and the use of mnemonic phrases. These mechanisms offer elegant ways to effectively manage your cryptocurrency keys while enhancing security.

# The mnemonic phrase
<partId>4070af16-c8a2-58b5-9871-a22c86c07458</partId>

## Evolution of Bitcoin wallets
<chapterId>9d9acd5d-a0e5-5dfd-b544-f043fae8840f</chapterId>

The Hierarchical Deterministic Wallet, more commonly known as HD wallet, plays a prominent role in the cryptocurrency ecosystem. The term "wallet" may seem misleading to those who are new to this field, as it does not involve holding money or currencies. Instead, it refers to a collection of cryptographic private keys.

The early wallets were software that grouped privately determined keys in a pseudo-random manner but had no connection between them. These wallets are called "Just a Bunch Of Keys" (JBOK).

Since the keys have no connection between them, the user is required to make a new backup for every new pair of keys generated.
Whether the user always uses the same key pair and compromises confidentiality, or generates a new key pair randomly and therefore needs to make a new backup of these keys.

However, the complexity of managing these keys is offset by a set of protocols called Bitcoin Improvement Proposals (BIPs). These upgrade proposals are at the core of the functionality and security of HD wallets. For example, [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), launched in 2012, revolutionized the way these keys are generated and stored by introducing the concept of deterministically and hierarchically derived keys. The idea is to derive all keys deterministically and hierarchically from a unique piece of information: the seed. This greatly simplifies the process of backing up these keys while maintaining their level of security.

Subsequently, [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) introduced a significant innovation: the 24-word mnemonic phrase. This system transformed a complex and hard-to-remember sequence of numbers into a series of ordinary words, making it much easier to memorize and store. Additionally, [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) proposed adding an additional passphrase to enhance the security of individual keys. These successive improvements led to the BIP43 and BIP44 standards, which standardized the structure and hierarchization of HD wallets, making them more accessible and user-friendly for the general public.

In the following sections, we will delve deeper into the workings of HD wallets. We will discuss key derivation principles and examine the fundamental concepts of entropy and random number generation, which are essential for ensuring the security of your HD wallet.

In summary, it is essential to highlight the central role of BIP32 and BIP39 in the design and security of HD wallets. These protocols allow for the generation of multiple keys from a single seed, which is supposed to be a random or pseudo-random number. Today, these standards are adopted by the majority of cryptocurrency wallets, whether they are dedicated to a single cryptocurrency or support multiple types of currencies.

## Entropy and Random Number
<chapterId>b43c715d-affb-56d8-a697-ad5bc2fffd63</chapterId>

The importance of private key security in the Bitcoin ecosystem is undeniable. They are indeed the cornerstone that ensures the security of Bitcoin transactions. To avoid any vulnerability associated with predictability, these keys must be generated in a truly random manner, which can quickly become a laborious exercise. The problem is that in computer science, it is impossible to generate a truly random number since it is necessarily derived from a deterministic process; a code. That is why it is essential to learn about the different Random Number Generators (RNG). The types of RNG vary, ranging from Pseudo-Random Number Generators (PRNG) to True Random Number Generators (TRNG), as well as PRNGs that incorporate a source of entropy.

Entropy refers to the "disorder" state of a system. From an external entropy, that is, an external source of information, it is possible to use a random number generator to obtain a random number.

![image](assets/image/section3/2.webp)

Let's take a look at how a Pseudo-Random Number Generator (PRNG) works.

It takes a seed as input, which corresponds to the internal state 0.
On this internal state, a transformation function is applied, and the result, which is a pseudo-random number, corresponds to the internal state 1.
On this internal state 1, again, a transformation function is applied, resulting in a new random number = internal state 2.
And so on.

The main drawback is that any identical seed will always produce the same output. Also, if we know the result of the initial transformation functions, we will be able to retrieve the random number at the output of the process.

An example of a transformation function is the PBKDF2 function.

**In summary, a cryptographically secure PRNG must:**

- be statistically random
- be unpredictable
- be resistant even if the results are revealed
- have a sufficiently long period

![image](assets/image/section3/3.webp)

In the case of Bitcoin, private keys are generated from a single piece of information at the base of the wallet. This information allows for deterministic and hierarchical derivation of child key pairs. Entropy is the foundation of every HD wallet, although there is no standard for generating this random number. Therefore, random number generation is a major challenge in securing Bitcoin transactions.

## The mnemonic phrase
<chapterId>8f9340c1-e6dc-5557-a2f2-26c9669987d5</chapterId>

The security of a Bitcoin wallet is a major concern for all its users. One essential way to ensure the backup of the wallet is to generate a mnemonic phrase based on entropy and checksum.

![image](assets/image/section3/5.webp)

To convert entropy into a mnemonic phrase, simply calculate the checksum of the entropy and concatenate the entropy and checksum.

Once the entropy is generated, the SHA256 function is used on the entropy to create a hash. 
The first 8 bits of the hash are retrieved, which is the checksum.
The mnemonic phrase is the result of the entropy added to the checksum.

The checksum ensures the verification of the accuracy of the recovery phrase. Without this checksum, an error in the phrase could result in the creation of a different wallet and therefore the loss of funds. The checksum is obtained by passing the entropy through the SHA256 function and retrieving the first 8 bits of the hash.

![image](assets/image/section3/6.webp)

Different standards exist for the mnemonic phrase depending on the size of the entropy. The most commonly used standard for a 24-word recovery phrase is an entropy of 256 bits. The size of the checksum is determined by dividing the size of the entropy by 32.

For example, an entropy of 256 bits generates an 8-bit checksum. The concatenation of the entropy and checksum then leads to respective sizes of 128 bits, 160 bits, etc. Depending on the size of the entropy, the recovery phrase will consist of 12 words for 128 bits, 15 words for 160 bits, and 24 words for 256 bits.

**Encoding of the mnemonic phrase:**

![image](assets/image/section3/7.webp)

The last 8 bits correspond to the checksum.
Each 11-bit segment is converted into decimal.
Each decimal corresponds to a word from a list of 2048 words on BIP39. It is important to note that no word has the same order of the first four letters.

It is essential to backup the 24-word recovery phrase to preserve the integrity of the Bitcoin wallet. The two most commonly used standards are based on an entropy of 128 or 256 bits and a concatenation of 12 or 24 words. Adding a passphrase is an additional option to enhance the security of the wallet.

In conclusion, generating a mnemonic phrase to secure a Bitcoin wallet is a crucial process. It is important to adhere to the standards of the mnemonic phrase based on the size of the entropy. Backing up the 24-word recovery phrase is essential to prevent any loss of funds.

## The passphrase
<chapterId>6a51b397-f3b5-5084-b151-cef94bc9b93f</chapterId>

The passphrase is an additional password that can be integrated into a Bitcoin wallet to increase its security. Its use is optional and is at the discretion of the user. By adding arbitrary information that, together with the mnemonic phrase, allows the calculation of the wallet's seed, the passphrase enhances its security.

![image](assets/image/section3/8.webp)

The passphrase is an optional cryptographic salt of a size chosen by the user. It improves the security of an HD wallet by adding arbitrary information that, when combined with the mnemonic phrase, will allow the calculation of the seed.

Once established during the creation of a wallet, it is necessary for the derivation of all the keys of the wallet. The pbkdf2 function is used to generate the seed from the passphrase. This seed allows the derivation of all the child key pairs of the wallet. If the passphrase is changed, the Bitcoin wallet becomes completely different.

The passphrase is an essential tool for enhancing the security of Bitcoin wallets. It can enable the implementation of various security strategies. For example, it can be used to create duplicates and facilitate backups of the mnemonic phrase. It can also improve the security of the wallet by mitigating the risks associated with random generation of the mnemonic phrase.

An effective passphrase should be long (20 to 40 characters) and diverse (using uppercase letters, lowercase letters, numbers, and symbols). It should not be directly related to the user or their environment. It is safer to use a random sequence of characters rather than a simple word as a passphrase.

![image](assets/image/section3/9.webp)

A passphrase is more secure than a simple password. The ideal passphrase is long, varied, and random. It can enhance the security of a wallet or hot software. It can also be used to create redundant and secure backups.

It is crucial to take care of passphrase backups to avoid losing access to the wallet. A passphrase is an option for an HD wallet. It can be generated randomly with dice or another pseudo-random number generator. It is not recommended to memorize a passphrase or mnemonic phrase.

In our next lesson, we will examine in detail the functioning of the seed and the first key pair generated from it. Feel free to follow this course to continue your learning. We look forward to seeing you again very soon.

# Creation of Bitcoin Wallets
<partId>9c25e767-7eae-50b8-8c5f-679d8fc83bab</partId>

## Creation of the Seed and Master Key
<chapterId>63093760-2010-5691-8d0e-9a04732ae557</chapterId>

In this part of the course, we will explore the steps for deriving a Hierarchical Deterministic Wallet (HD Wallet), which allows for the hierarchical and deterministic creation and management of private and public keys.

![image](assets/image/section4/0.webp)

The foundation of the HD Wallet relies on two essential elements: the mnemonic phrase and the passphrase (optional additional password). Together, they constitute the seed, an alphanumeric sequence of 512 bits that serves as the basis for deriving the wallet's keys. From this seed, it is possible to derive all the child key pairs of the Bitcoin wallet. The seed is the key that grants access to all the bitcoins associated with the wallet, whether you use a passphrase or not.

![image](assets/image/section4/1.webp)

To obtain the seed, the pbkdf2 function (Password-Based Key Derivation Function 2) is used with the mnemonic phrase and the passphrase. The output of pbkdf2 is a 512-bit seed.

From the seed, it is possible to determine the master private key and the chain code using the HMAC SHA-512 (Hash-based Message Authentication Code Secure Hash Algorithm 512) algorithm. This algorithm requires a message and a key as input to generate a result. The master private key is calculated from the seed and the phrase "Bitcoin SEED". This phrase is identical for all derivations of all HD wallets, ensuring consistency across wallets.

Initially, the SHA-512 function was not implemented in the Bitcoin protocol, which is why HMAC SHA-512 is used. The use of HMAC SHA-512 with the phrase "Bitcoin SEED" constrains the user to generate a wallet specific to Bitcoin. The result of HMAC SHA-512 is a 512-bit number, divided into two parts: the leftmost 256 bits represent the master private key, while the rightmost 256 bits represent the master chain code.

![image](assets/image/section4/2.webp)

The master private key is the parent key of all future keys in the wallet, while the master chain code is involved in the derivation of child keys. It is important to note that it is impossible to derive a child key pair without knowing the corresponding chain code of the parent pair.

A key pair in the wallet consists of a private key, a public key, and a chain code. The chain code introduces a source of randomness in the derivation of child keys and isolates each key pair to prevent any information leakage.
It is important to note that the master private key is the first private key derived from the seed and has no connection to the extended keys of the wallet.

In the next lesson, we will explore extended keys in detail, such as xPub, xPRV, zPub, and understand why they are used and how they are constructed.

## Extended Keys
<chapterId>8dcffce1-31bd-5e0b-965b-735f5f9e4602</chapterId>

In this part of the lesson, we will study extended keys (xPub, zPub, yPub) and their prefixes, which play an important role in deriving child keys in a Hierarchical Deterministic Wallet (HD Wallet).

![image](assets/image/section4/3.webp)

Extended keys are distinct from master keys. An HD wallet generates a mnemonic phrase and a seed to obtain the master key and master chain code. Extended keys are used to derive child keys and require both the parent key and the corresponding chain code. An extended key combines these two pieces of information to simplify the derivation process.

![image](assets/image/section4/4.webp)

Extended public keys can only derive normal child public keys, while extended private keys can derive both child public and private keys, whether through normal or hardened derivation. Hardened derivation is derivation from the parent private key, while normal derivation corresponds to derivation from the parent public key.

Using extended keys with the XPUB prefix allows for the derivation of new addresses without going back to the corresponding private keys, thus providing better security. The metadata associated with extended keys provides important information about their role and position in the key hierarchy.

Extended keys are identified by specific prefixes (XPRV, XPUB, YPUB, ZPUB) that indicate whether it is an extended private or public key, as well as its specific purpose. The metadata associated with an extended key includes the version (prefix), depth, parent key fingerprint, index, and payload (chain code and parent key).

![image](assets/image/section4/5.webp)

The version corresponds to the type of key: xpub, xprv, ...

The depth corresponds to the number of derivations between parent and child keys since the master key.

The parent fingerprint is the first 4 bytes of the hash 160 of the parent key.
The index is the number of the pair that is used to generate the extended key among its siblings. (siblings = keys of the same depth) For example, if we want to derive the xpub of our 3rd account, its index will be 2 (because the index starts at 0).

The payload is composed of the chain code (32 bytes) and the parent key (33 bytes).

Compressed public keys have a size of 33 bytes, while raw public keys are 512 bits. Compressed public keys retain the same information as raw keys, but with a reduced size. Extended keys have a size of 82 bytes and their prefix is represented in base 58 through a conversion to hexadecimal. The checksum is calculated using the HASH256 hash function.

![image](assets/image/section4/6.webp)

Enhanced derivations start from indexes that are powers of 2 (2^31). It is interesting to note that the most commonly used prefixes are xpub and zpub, which correspond respectively to legacy standards and segwit v1 and segwit v0.

In our next lesson, we will focus on the derivation of child key pairs using the knowledge acquired about extended keys and the master key of the wallet.

## Derivation of child key pairs
<chapterId>61c0807c-845b-5076-ad06-7f395b36adfd</chapterId>

As a reminder, we have discussed the calculation of the seed and the master key, which are the first essential elements for the hierarchical organization and derivation of the HD (Hierarchical Deterministic) wallet. The seed, with a length of 128 to 256 bits, is generated randomly or from a secret phrase. It plays a deterministic role in the derivation of all other keys. The master key is the first key derived from the seed, and it allows the derivation of all other child key pairs.

The master chain code plays an important role in wallet recovery from the seed. It should be noted that all keys derived from the same seed will have the same master chain code.

![image](assets/image/section4/7.webp)

The hierarchical organization and derivation of the HD wallet offer more efficient management of keys and wallet structures. Extended keys allow the derivation of a child key pair from a parent key pair using mathematical calculations and specific algorithms.
There are different types of child key pairs, including reinforced keys and normal keys. The extended public key only allows the derivation of normal child public keys, while the extended private key allows the derivation of all child keys, both public and private, whether they are in normal or reinforced mode. Each key pair has an index that allows them to be differentiated from each other.

![image](assets/image/section4/8.webp)

The derivation of child keys uses the HMAC-SHA512 function using the parent key concatenated with the index and the chain code associated with the key pair. Normal child keys have an index ranging from 0 to 2 to the power of 31 minus 1, while reinforced child keys have an index ranging from 2 to the power of 31 to 2 to the power of 32 minus 1.

![image](assets/image/section4/9.webp)

![image](assets/image/section4/10.webp)

There are two types of child key pairs: reinforced pairs and normal pairs. The process of deriving child keys uses public keys to generate spending conditions, while private keys are used for signing. The extended public key only allows the derivation of normal child public keys, while the extended private key allows the derivation of all child keys, both public and private, in normal or reinforced mode.

![image](assets/image/section4/11.webp)
![image](assets/image/section4/12.webp)

Reinforced derivation uses the parent private key, while normal derivation uses the parent public key. The HMAC-SHA512 function is used for reinforced derivation, while normal derivation uses a 512-bit digest. The child public key is obtained by multiplying the child private key by the elliptic curve generator.

![image](assets/image/section4/13.webp)
![image](assets/image/section4/14.webp)

Hierarchically deriving and deriving many key pairs deterministically allows for the creation of a tree structure for hierarchical derivation. In the next lesson of this training, we will study the structure of the HD wallet as well as derivation paths, with a particular focus on derivation path notations.

## Wallet Structure and Derivation Paths
<chapterId>34e1bbda-67de-5493-b268-1fded8d67689</chapterId>

In this chapter, we will study the structure of the derivation tree in a Hierarchical Deterministic Wallet (HD Wallet). We have already explored seed calculation, the master key, and the derivation of child key pairs. Now, we will focus on organizing keys within the wallet.

The HD Wallet uses depth layers to organize keys. Each derivation from a parent pair to a child pair corresponds to a depth layer.

![image](assets/image/section4/15.webp)

- Depth 0 corresponds to the master key and the master chain code.

- Depth 1 is used to derive child keys for a specific purpose, determined by the index. The purposes comply with BIP 84 and Segwit v0/v1 standards.

- Depth 2 allows differentiation of accounts for different cryptocurrencies or networks. This allows organizing the wallet based on different sources of funds. For bitcoin, the index will be 0.

- Depth 3 is used to organize the wallet into different accounts, providing a clearer and more organized structure.

- Depth 4 corresponds to the external and internal chains, which are used for addresses intended to be publicly communicated. Index 0 is associated with the external chain, while index 1 is associated with the internal chain. Each account has two chains: the external chain (0) and the internal chain (1). Depth 4 is also used to manage script types in the case of multi-signature wallets.

- Depth 5 is used for receiving addresses in a standard wallet. In the next section, we will examine the derivation of child key pairs in more detail.

![image](assets/image/section4/16.webp)

For each depth layer, we use indexes to differentiate child key pairs.

The index without an apostrophe corresponds to the actual used index, while the index with an apostrophe corresponds to the actual index + 2^31. Hardened derivations use indexes from 2^31 to 2^32-1. For example, index 44' corresponds to the actual index 2^31 + 44.

To generate a specific receiving address, we derive a child key pair from the master key and the master chain code. Then, we use the index to differentiate between different child key pairs at the same depth.

Extended keys, such as XPUB, allow you to share your wallet with multiple people. The derivation path is used to differentiate between the external chain (addresses intended to be shared) and the internal chain (change addresses).

In the next chapter, we will study receiving addresses, their advantages of use, and the steps involved in their construction.

# What is a Bitcoin address?
<partId>81ec8d17-f8ee-5aeb-8035-d370866f4281</partId>

## Bitcoin addresses
<chapterId>0a887ed8-3424-5a52-98e1-e4b406150475</chapterId>

In this chapter, we will explore receiving addresses, which play a crucial role in the Bitcoin system. They allow funds to be received on a transaction and are generated from pairs of private and public keys. Although there is a script type called Pay2PublicKey that allows bitcoins to be locked to a public key, users generally prefer to use receiving addresses instead of this script.

![image](assets/image/section5/0.webp)

When a recipient wants to receive bitcoins, they provide a receiving address to the sender instead of their public key. An address is actually a hash of a public key, with a specific format. The public key is derived from the child private key using mathematical operations such as point addition and doubling on elliptic curves.

![image](assets/image/section5/1.webp)

It is important to note that it is not possible to reverse from an address to the public key, nor from the public key to the private key. Using an address reduces the size of the public key information, which initially is 512 bits.

Bitcoin addresses have been reduced in size to facilitate their use. They have a checksum, which allows for detecting typos and reducing the risk of losing bitcoins. On the other hand, public keys do not have a checksum, which means that typos can result in the loss of corresponding funds.

Addresses also provide a second layer of security between public and private information, making it more difficult to take control of the private key.

It is essential to emphasize that each address should be used only once. Reusing the same address poses privacy issues and should be avoided.

Different prefixes are used for Bitcoin addresses. For example, BC1Q corresponds to a Segwit V0 address, BC1P to a Taproot/Segwit V1 address, and prefixes 1 and 3 are associated with Pay2PublicKeyH/Pay2ScriptH (legacy) addresses. In the next lesson, we will explain step by step how to derive an address from a public key.

## How to create a Bitcoin address?
<chapterId>6dee7bf3-7767-5f8d-a01b-659b95cfe0a5</chapterId>

In this chapter, we will discuss the construction of a receiving address for Bitcoin transactions. A receiving address is an alphanumeric representation of a compressed public key. The conversion of a public key into a receiving address involves several steps.

### Step 1: Compression of the public key

![image](assets/image/section5/14.webp)

An address is derived from a child public key.

A public key is a point on the elliptic curve. Thanks to the symmetry of the elliptic curve, a point on the elliptic curve will have an x-coordinate associated with only two possible values for y: positive or negative. 
However, in the Bitcoin protocol, we work with a finite set of positive integers rather than with the set of real numbers. To distinguish between the two possible values of y, it is sufficient to indicate whether y is even or odd.

The compression of a public key reduces its size from 520 bits to 264 bits.

We use the prefix 0x02 for an even y and 0x03 for an odd y. This is the compressed form of the public key.

### Step 2: Hashing of the compressed public key

![image](assets/image/section5/3.webp)

The hashing of the compressed public key is performed using the SHA256 function. The RIPEMD160 function is then applied to the digest.

### Step 3: The payload = Address payload

![image](assets/image/section5/4.webp)

The binary digest of RIPEMD160(SHA256(K)) is used to form groups of 5 bits. Each group is transformed into base16 (Hexadecimal) and/or base 10.

### Step 4: Adding metadata for checksum calculation with the BCH program

![image](assets/image/section5/5.webp)

In the case of legacy addresses, we use double SHA256 hashing to generate the address checksum. However, for Segwit V0 and V1 addresses, we rely on the BCH checksum technology to ensure error detection. The BCH program is capable of suggesting and correcting errors with an extremely low probability of error. Currently, the BCH program is used to detect and suggest modifications to be made, but it does not automatically perform them on behalf of the user.

The BCH program requires several input information, including the HRP (Human Readable Part) that needs to be extended. Extending the HRP involves encoding each letter in base 2 according to their ASCII code. Then, by taking the first 3 bits of the result for each letter and converting them to base 10 (in blue in the image). Insert a separator 0. Then concatenate the following 5 bits of each letter previously converted to base 10 (in yellow in the image).

Extending the HRP in base 10 allows isolating the last five bits of each character, thus reinforcing the checksum.

Segwit V0 version is represented by the code 00 and the "payload" is in black, in base 10. This is followed by six reserved characters for the checksum.

### Step 5: Calculating the checksum with the BCH program

![image](assets/image/section5/6.webp)

The input containing the metadata is then submitted to the BCH program to obtain the checksum in base 10.

Here we have the checksum.

### Step 6: Address construction and conversion to Bech32

![image](assets/image/section5/7.webp)

The concatenation of the version, payload, and checksum allows building the address. The base 10 characters are then converted to Bech32 characters using a correspondence table. The Bech32 alphabet includes all alphanumeric characters, except for 1, b, i, and o, to avoid any confusion.

### Step 7: Adding the HRP and separator

![image](assets/image/section5/8.webp)

In pink, the checksum.
In black, the payload = the hash of the public key.
In blue, the version.

Everything is converted to Bech32, then 'bc' is added for bitcoin and '1' as a separator, and here is the address.

# Go further
<partId>58111408-b734-54db-9ea7-0d5b67f99f99</partId>

## Creating a seed from 128 dice rolls!
<chapterId>0f4d40a7-cf0e-5faf-bc4d-691486771ac1</chapterId>

Creating a mnemonic phrase is a crucial step in securing your cryptocurrency wallet. There are several methods to generate a mnemonic phrase, however, we will focus on the manual generation method using dice. It is important to note that this method is not suitable for a high-value wallet. It is recommended to use open-source software or a hardware wallet to generate the mnemonic phrase. To create a mnemonic phrase, we will use dice to generate binary information. The goal is to understand the process of creating the mnemonic phrase.

**Step 1 - Preparation:**
Make sure you have an amnesic Linux distribution, such as Tails OS, installed on a USB key for added security. Note that this tutorial should not be used to create a main wallet.
**Step 2 - Generating a random binary number:**
We will use dice to generate binary information. Roll a die 128 times and record each result (1 for odd, 0 for even).

**Step 3 - Organizing binary numbers:**
Organize the obtained binary numbers into rows of 11 digits to facilitate further calculations. The twelfth row should only have 7 digits.

**Step 4 - Calculating the checksum:**
The last 4 digits for the twelfth row correspond to the checksum. To calculate this checksum, we need to use a terminal from a Linux distribution. It is recommended to use [TailOs](https://tails.boum.org/index.fr.html), which is a bootable memoryless distribution from a USB key. Once on your terminal, enter the command `echo <binary number> | shasum -a 254 -0`. Replace `<binary number>` with your list of 128 zeros and ones. The output is a hexadecimal hash. Take note of the first character of this hash and convert it to binary. You can use this [table](https://www.educative.io/answers/decimal-binary-and-hex-conversion-table) for assistance. Add the binary checksum (4 digits) to the twelfth row of your sheet.

**Step 5 - Conversion to decimal:**
To find the words associated with each of your rows, you first need to convert each series of 11 bits to decimal. Here, you cannot use an online converter because these bits represent your mnemonic phrase. Therefore, you will need to convert using a calculator and a trick as follows: each bit is associated with a power of 2, so from left to right, we have 11 ranks corresponding to 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1. To convert your series of 11 bits to decimal, simply add up only the ranks that contain a 1. For example, for the series 00110111011, this corresponds to the following addition: 256 + 128 + 32 + 16 + 8 + 2 + 1 = 443. You can now convert each row to decimal. And before moving on to encoding into words, add +1 to all the rows because the index of the BIP39 word list starts from 1, not 0.

**Step 8 - Generating the mnemonic phrase:**
Start by printing the [list of 2048 words](https://seedxor.com/files/wordlist.pdf) to convert between your decimal numbers and the BIP39 words. The uniqueness of this list is that no word shares the first 4 letters with any other word in this dictionary. Then, search for the word associated with each of your lines' decimal number.
**Step 9 - Mnemonic Phrase Test:**
Immediately test your mnemonic phrase on Sparrow Wallet by creating a wallet from it. If you receive an invalid checksum error, it is likely that you made a calculation error. Correct this error by going back to step 4 and test again on Sparrow Wallet. Voilà! You have just created a new Bitcoin wallet from 128 dice rolls.

Generating a mnemonic phrase is an important process to secure your cryptocurrency wallet. It is recommended to use more secure methods, such as using open-source software or a hardware wallet, to generate the mnemonic phrase. However, completing this workshop helps to better understand how we can create a Bitcoin wallet from a random number.

## BONUS: Interview with Théo Pantamis
<chapterId>39f0ec5a-e258-55cb-9789-bc46d314d816</chapterId>

Another widely used cryptographic method on the Bitcoin protocol is the method of digital signatures.

![video](https://youtu.be/c9MvtGJsEvY?si=bQ1N5NCd6op0G6nW)



## Evaluate the course
<chapterId>0cd71541-a7fd-53db-b66a-8611b6a28b04</chapterId>
<isCourseReview>true</isCourseReview>

## Final Exam
<chapterId>a53ea27d-0f84-56cd-b37c-a66210a4b31d</chapterId>
<isCourseExam>true</isCourseExam>


## Conclusion and End
<chapterId>d291428b-3cfa-5394-930e-4b514be82d5a</chapterId>

### Thanks and keep digging the rabbit hole

We would like to sincerely thank you for completing the Crypto 301 course. We hope this experience has been enriching and educational for you. We have covered many exciting topics, ranging from mathematics to cryptography to the workings of the Bitcoin protocol.

If you would like to delve deeper into the subject, we have an additional resource to offer you. We conducted an exclusive interview with Théo Pantamis and Loïc Morel, two renowned experts in the field of cryptography. This interview explores various aspects of the subject in depth and provides interesting perspectives.

Feel free to watch this interview to continue exploring the fascinating field of cryptography. We hope it will be useful and inspiring in your journey. Once again, thank you for your participation and commitment throughout this course.

### Support Us

This course, along with all the content on this university, has been provided to you for free by our community. To support us, you can share it with others, become a member of the university, and even contribute to its development via GitHub. On behalf of the entire team, thank you!

### Rate the course

A grading system for the training will soon be integrated into this new E-learning platform! In the meantime, thank you very much for taking the course, and if you enjoyed it, please consider sharing it with others.
