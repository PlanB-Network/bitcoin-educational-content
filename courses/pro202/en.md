---
name: Programming Bitcoin
goal: Build a complete Bitcoin library from scratch and understand Bitcoin's cryptographic foundations
objectives: 
 - Implement finite field arithmetic and elliptic curve operations in Python
 - Construct and parse Bitcoin transactions programmatically
 - Create testnet addresses and broadcast transactions over the network
 - Master the mathematical foundations underlying Bitcoin's security model
---
# A Journey to Bitcoin's scripts and programs

This intensive two-day course, taught by Jimmy Song, takes you deep into Bitcoin's technical foundations by building a complete Bitcoin library from the ground up. Starting with the essential mathematics of finite fields and elliptic curves, you'll progress through transaction parsing, script execution, and network communication. Through hands-on coding exercises in Jupyter notebooks, you'll create your own testnet address, construct transactions manually, and broadcast them directly to the network—all while gaining a profound understanding of the cryptographic principles that make Bitcoin secure and trustless.

Enjoy your discovery!

+++

# Introduction

<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>

## Course Overview

<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>

Welcome to the course PRO 202 _**Programming Bitcoin**_, an intensive journey that takes you from finite field arithmetic all the way to building and broadcasting real transactions on Bitcoin’s Testnet.

In this course, you will progressively build a Bitcoin library in Python while acquiring the cryptographic, protocol, and software foundations necessary to reason precisely about Bitcoin’s security and inner workings. The PRO 202 approach is thoroughly hands-on: every concept is immediately implemented in Jupyter notebooks, ensuring that theory and code strengthen each other.

### Essential Mathematical Concepts for Bitcoin

This first section establishes the indispensable mathematical groundwork. You will implement finite field arithmetic and elliptic curve operations (group law, addition, doubling, scalar multiplication...) — the prerequisites for ECDSA. The goal is twofold: to understand the algebraic structure that makes cryptographic signatures possible and to build reliable Python tools for manipulating them.

You will then formalize the components of ECDSA: key generation, point formatting, hashing, signature creation, and verification. This section directly connects theory to practice, emphasizing implementation details and the robustness of the underlying security model.

### Bitcoin Transaction Innerworkings

In the second section, you will dissect the structure of a Bitcoin transaction: UTXOs, inputs/outputs, sequences, scripts, encodings, and more. You will write code to construct, sign, and verify transactions, gaining a precise understanding of what is committed by the hash and why.

Next, you will implement a minimal _Script_ executor, review key opcodes, and validate spending paths. The objective is to make you capable of auditing transaction behavior, diagnosing validation failures, and reasoning about the safety of spending policies.

### Bitcoin Network Innerworkings

In the third section, you will place the transaction within the broader system: block structure, headers, difficulty, and the Proof-of-Work mechanism. You will handle protocol messages, block headers, and Merkle trees.

Finally, you will study peer-to-peer node communication, message optimization, and the introduction of SegWit.

As with every course on Plan ₿ Academy, the final section includes an evaluation designed to consolidate your understanding. Ready to uncover the inner workings of Bitcoin and write the code that powers it? Let’s begin!









# Essential Mathematical Concepts for Bitcoin
<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>

## Mathematics for Bitcoin Implementation
<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>
![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)

## Elliptic Curve Cryptography
<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>
![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)

# Bitcoin Transaction Innerworkings
<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>

## Bitcoin Transaction Parsing and ECDSA Signatures
<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>
![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)

## Bitcoin Script and Transaction Validation
<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>
![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)

## Transaction Construction and Pay-to-Script Hash

<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>
![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)

# Bitcoin Network Innerworkings
<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>

## Bitcoin Blocks and Proof of Work
<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>
![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)

## Network Communication and Merkle Trees
<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>
![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)

## Advanced Node Communication and Segregated Witness
<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>
![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)


# Final Section

<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>

## Reviews & Ratings

<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>
<isCourseReview>true</isCourseReview>

## Conclusion


<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>

<isCourseConclusion>true</isCourseConclusion>
