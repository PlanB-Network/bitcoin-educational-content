---
name: Bitcoin Development Accelerator
goal: Acquire all the bases to start developing on Bitcoin
objectives:
  - Understand the core concepts and technology underpinning Bitcoin.
  - Gain practical skills in Bitcoin security, software development, and network governance.
  - Develop a mastery of the Lightning Network and its associated protocols.
---

# Introduction and preparatory courses

## Introduction to CUBO+ courses

![Video](https://youtu.be/4VuI9we_XYM)

Filippo and Mario provide an introductory talk on CUBO+, setting the stage for the comprehensive learning journey that awaits. They discuss the structure of the courses, the learning outcomes, and how these will empower students in the Bitcoin development space.

### Objectives

The course aims to equip participants with a deep understanding of Bitcoin's underlying principles, practical development skills, and the ability to navigate and contribute to the Bitcoin ecosystem effectively. Through a blend of theoretical knowledge and practical exercises, students will master the essentials of Bitcoin security, the intricacies of its software stack, and the mechanisms of its governance.

### Prerequisite

Participants are expected to bring a strong sense of curiosity, an eagerness to learn at a professional level, and some foundational knowledge in development. While a detailed background in Bitcoin is not required, a basic understanding of coding principles and an openness to engaging with complex technical concepts are essential for making the most of the accelerator.

## Module 1 - Why Bitcoin

### Why El salvador needs Bitcoin

![video](https://www.youtube.com/live/In8BJ3VlaM8?feature=share)

The first lecture ‘Why El Salvador needs Bitcoin’ provides an overview of: the Bitcoin protocol and its roots, the cypherpunk movement, and the importance of Bitcoin as a tool of freedom (uncensored money, financial inclusion, and other related topics). 

### Cyperpunk movement and austrian economics

![video](https://youtube.com/live/KIaC31YQLBA)

In our second lecture 'Cypherpunk movement and Austrian Economics', we delved deeper into the Cypherpunk philosophy introduced by Rikki in the previous lecture. 

Also, our discussion centered on the Austrian School of Economics, which distinguishes itself from the current financial system (Keynesian Economics). 
We explored concepts such as scarcity, time preference, durability and saving, which Saifedean will delve into further. To prepare for his lecture, I recommend reading The Bitcoin Standard (you can find it in 'Additional Resources'), or at least a few chapters. 

It is important to note that the first module, 'Why Bitcoin', was necessary to comprehend the roots and goals before moving on to 'How Bitcoin', where we will discover the Bitcoin's technological stack and tradeoffs early developers made in the protocol.
Here is the link, enjoy! 

## Module 2 - How Bitcoin 

### Bitcoin's Technology Stack

![video](https://youtube.com/live/OKanfSTLlW0)

In the first lecture of 'How Bitcoin' course, we began exploring the technology stack that underpins the Bitcoin network. We covered a range of topics, including Hashcash, transactions, the blockchain, Lightning Network and other key components of the Bitcoin protocol.

### Bitcoin's Technological Stack

![video](https://www.youtube.com/live/VT2nuXaYnHk?feature=share)

During the second lecture of 'How Bitcoin', we conducted a more in-depth examination of Bitcoin's technology stack. 

## Module 3 - Debunk Bitcoin

### Cut the FUD

![video](https://www.youtube.com/watch?v=P0reZe6pMpo)

Debunking blockchains and shitcoin and Debunking myths and misconceptions about Bitcoin’s energy waste, and criminal usage 

## Module 4 - Running Bitcoin 

### Installation of Bitcoin Core

![Video](https://youtube.com/live/K0meE5pldmI)

In the first lecture of the 4th module we explored the Bitcoin's architecture and installation of a Bitcoin Core node

### Installation of C-lightning

![video](https://youtube.com/live/p6SgjtplAAM)

During our second lecture, we delved into the process of installing c-lightning

### Security and Hardware devices

![video](https://www.youtube.com/live/_0N4EC9Veuw?feature=share)

In third lecture, we covered topics related to security, hardware devices, and the configuration of Specter

## Module 5 - Imrpoving Bitcoin

### Open Problems in the Bitcoin ecosystem

![video](https://youtube.com/live/BVYKeTXMtzQ)

Hey guys, here is the link for the last lecture of the preparatory period about Bitcoin problems and potential solutions


# Bitcoin Fundamentals

## Security Thinking in Bitcoin

![Video](https://youtu.be/2f_rK74MB3U)

Peter Todd delves into the security considerations unique to Bitcoin, teaching developers how to adopt a security-first mindset. The lecture aims to instill a strong foundation in recognizing and mitigating potential threats in Bitcoin development based on a pratical exercice of expliciting the Threat Model of software for timestamping election. 

## Free and Open Source Software (FLOSS) in Bitcoin

![Video](https://youtu.be/GM-ho5M5_mQ)

The use of Free and Open Source Software (FLOSS) is critical in Bitcoin's ecosystem. Peter Todd explores the importance of FLOSS for Bitcoin, exploring the history of FLOSS and examining how Github allow us to collaboratively build open-source software like Bitcoin.

## Cryptography in Bitcoin

![Video](https://youtu.be/4Fw9xS7JlVU)

Adam Gibson takes participants through the cryptographic underpinnings of Bitcoin from a mathematical perspective. The session covers the essential cryptographic functions that are present in Bitcoin, like hashes and their security, merkle trees, identity protocols and signature, discrete logs and elliptic curves. 

## Bitcoin's Governance Model

![Video](https://youtu.be/KSpKwTFSOdc)

Peter Todd discusses Bitcoin's governance model, providing insights into how decisions are made within the Bitcoin community and how this decentralized approach influences the protocol's development and stability. Notably he explores how different type of changes can lead to Soft or Hard Forks, how the governance difference between policy change and consensus rules, and what is the game of politics of change in Bitcoin.  

# Layer One Concepts

## Node Components in Bitcoin

![Video](https://youtu.be/jdHc-pbDI9E)

Adam Gibson breaks down the various components of a Bitcoin node. The chapter focuses on the role each component plays in maintaining the network's functionality and integrity. In particularly he focuses on why we should run a bitcoin node, what does a bitcoin node do, and how the different components of a bitcoin node function. 

## Bitcoin's Data Structures

![video](https://youtu.be/SJnaDPZmVsE?si=5h048qponlVi-iQM)

Alekos Filini presents an in-depth look at Bitcoin's data structures. This covers the organization of data within the blockchain and how it enables the robustness and efficiency of the network. 

## Bitcoin L1 Software Stack

![Video](https://youtu.be/L6FkntRwkOU)

Daniela Brozzoni offers a comprehensive overview of the Bitcoin Layer 1 software stack, explaining the layers that comprise the foundation of Bitcoin's protocol (ie. Bitcoin nodes and Bitcoin wallets) and how to build Bitcoin software with an introduction to Bitcoin librairies and a deep dive into Bitcoin Development Kit (BDK). 

# Lightning Network

## History of Payment Channels

![Video](https://youtu.be/0ZgE-LjHWvI)

Gabriel Comte provides a historical perspective on the development of payment channels, which are fundamental to the Lightning Network. This chapter explores the evolution of payment channels and their significance in scaling Bitcoin transactions, from Satoshi's payment channels to bi-directional payment channel solutions like Duplex Micropayment Channels or Lightning payment channels.

## History of Atomic Routing

![Video](https://youtu.be/RaMeYgSBJQ0)

Gabriel Comte recounts the history of atomic routing, detailing several  techniques that have been on the foundation of the routing layer of lightning network like Hub-and-Spokes model, Ripple model and Hashed TimeLocked Contracts (HTLCs). This history has been pivotal in enabling secure, trustless transactions across the Lightning Network.

## BOLT Review

![Video](https://youtu.be/Fy5W_ryWrCY)

asi0 reviews BOLT, the Basis of Lightning Technology, explaining the specifications that any Lightning Network implements must respect. This will be a first deep dive into the different layers of the Lightning Network. 

## Major LN Clients

![Video](https://youtu.be/a0Q_5dzpqKw)

asi0 introduces the major Lightning Network (LN) clients, providing an analysis of their features, strengths based on a 2x2 matrix that evaluates the level of custody and liquidity management that the user has with LN clients. 

# The Challenges of LN

## Practical Challenges to LN

(the video will be available soon)

asi0 addresses the practical challenges faced when working with the Lightning Network. This includes a discussion about the current limitations and the ongoing efforts to overcome them based on 4 main challenges (liquidity management, L1/L2 abstraction, receiving offline, and backup management) that are explored from the point of view of the user and from the point of view of the developper

## LN Future Evolution

![Video](https://youtu.be/TIrAMFK6Peg)

Gabriel Comte speculates on the future evolution of the Lightning Network, examining potential developments -- like dual-funded channels eltoo, BOLT 12, PTLCs, Watchtowers and LSP standards -- and how they could transform the landscape of Bitcoin transactions.

## Protocols on top of LN

![Video](https://youtu.be/OLTQLtQyoZE)

Alekos Filini examines the protocols built on top of the Lightning Network, explaining how they contribute to the scalability and functionality of Bitcoin.

# Bonus

## Bitcoin Mining Essentials

![Video](https://youtu.be/22LadAWEMQo)

Ajelex focuses on the business aspect of Bitcoin mining, examining strategies for maintaining profitability in a competitive market. The discussion includes an analysis of operational costs, efficiency measures, and the economics driving the mining industry. 


## Understanding Joinmarket

![Video](https://youtu.be/VFjccozVwc8)

Adam Gibson offers insight into Joinmarket, detailing how this CoinJoin implementation enhances Bitcoin's privacy and fungibility. He discusses how Joinmarket facilitates collaborative, trustless, and anonymous transactions within the Bitcoin ecosystem. Then in a second part, he show how to run Joinmarket in Signet. 

## Cubo+ first year Hackathon

### Groupe 1 Hackathon - The Satoshi Legacy

![Video](https://youtu.be/NiaahH57N1w)

The Satoshi Legacy's group presents their work on building a Lightning e-commerce with Shopify, React JS and Hydrogen and the IBEX payment gateway. 

### Groupe 2 Hackathon - Honey Badger

![Video](https://youtu.be/dds0-SV8ltE)

Honey Badger's group presents her solution for a blog with Lightning Powered Micropayments built-in with the use of LnBits and Next.js, Node.js and Hydrogen.

### Groupe 3 Hackathon

![Video](https://youtu.be/2YjrrDMGU9c)

The third group presents a Lightning Network Node Dashboard via a customed API, LND, vue.js, node.js, Bootstrap.


### Groupe 4 Hackathon - Satoshi Fellowship

![Video](https://youtu.be/mxLKiHa0mes#)

Satoshi's Fellowship's group presents a LN gaming app using LnBits and MongoDB, Poetry, Node.js. 

### Groupe 5 Hackathon - Lighting Walker

![Video](https://youtu.be/IiY5PmkGNVo)

Lightning Walker's group presents their solution for Remittances Service using MySQL, JavaScript and ZDB's API. 

## Acknowledgments

We'd like to acknowledge the contributions of our educators:

- Peter Todd
- Adam Gibson
- Alekos Filini
- Daniela Brozzoni
- Ajelex
- asi0
- Gabriel Comte

Their expertise has been invaluable to the success of this course. This has been the first course based on the 1st edition of the Cubo+ initiative, conducted in July 2023. Thank you to all participants and educators for being a part of this pioneering educational journey. It marks the beginning of what we hope will be a long and fruitful journey into the world of Bitcoin development. As the first cohort, your participation has set the standard for future classes.

Continue to explore, learn, and contribute to the Bitcoin ecosystem. The knowledge gained here is just a starting point. Keep digging the rabbit hole, and you'll discover an ever-expanding world of opportunities.
