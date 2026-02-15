---
name: Introduction to Bitcoin mining
goal: Understanding Bitcoin mining and proof-of-work from scratch
objectives: 

  - Understand proof-of-work and its role in Bitcoin.
  - Analyze the difficulty adjustment mechanism.
  - Know what the technical terms associated with mining actually mean.
  - Describe the steps involved in building a Bitcoin block and its components.
  - Identify major developments in the mining industry.

---

# Discover the fundamentals of Bitcoin mining


To understand the proof of work is to understand how Bitcoin works. Without this invention and its ingenious use, Bitcoin simply couldn't have existed. This course provides you with all the mining theory you need for your bitcoin journey.


MIN 101 is primarily aimed at beginners, as it explains all the concepts precisely from scratch. However, if you already have an intermediate level of knowledge, this course will enable you to consolidate your understanding, correct some approximate intuitions and explore details often missing from mainstream explanations.


By the end of this course, you'll be able to explain how proof-of-work works in a simple and rigorous way. MIN 101 is also an ideal introduction to all the other more advanced courses devoted to Bitcoin mining on Plan ₿ Academy, whether theoretical or practical.


+++


# Introduction

<partId>041ff0fa-53c3-4d55-9888-d7840de283e9</partId>


## Course overview

<chapterId>a82d49dc-d68a-4e3f-985e-bcef6643677e</chapterId>


Welcome to the MIN 101 course, in which you'll discover the fundamental theoretical concepts of mining and Proof-of-Work within the Bitcoin system. This course is the first step in your bitcoiner journey to understand how mining works. Once you've completed it, you'll be able to move on to more advanced theory courses, or get hands-on and become a bitcoin miner yourself!


In this MIN 101 course, we won't be going back over the basic concepts of Bitcoin, as we'll be getting straight to the heart of the matter: mining. If you've never heard of Bitcoin, or if its fundamentals are still a little unclear to you, I strongly recommend that you start with our introductory BTC 101 course. Once you have acquired these fundamentals, you'll be able to tackle MIN 101 with confidence:


https://planb.academy/courses/2b7dc507-81e3-4b70-88e6-41ed44239966


### Part 1 - Introduction


We're going to start this course with an optional first chapter, in which I offer a very simplified explanation of mining, to give you a clear mental picture before getting into the technical mechanisms.


The aim here is not to give you all the technical details (they'll come later in the course), but to give you a guiding thread. Once this framework is in place, each more advanced concept introduced afterward will naturally fit into this structure.


### Part 2 - How proof of work works


After the introduction, Part 2 is the technical foundation of the training program. Its aim is to explain, step by step, how Bitcoin produces valid blocks. We'll start by discovering the structure of a block, before going into the proof-of-work mechanism: the role of the target, the nonce and the hash function. Finally, we'll see how Bitcoin manages to maintain a stable block production rate despite variations in hash power, thanks to the difficulty adjustment mechanism. At the end of this section, you'll have a complete understanding of the fundamental principles of Bitcoin's proof-of-work.


### Part 3 - The Bitcoin mining incentive system


In the third part, we'll look at why miners are encouraged to participate honestly in mining. We'll detail the principle of block reward, its composition and calculation method, its evolution over time through halvings, and the specific role of the coinbase transaction.


### Part 4 - The Bitcoin mining industry


The fourth part puts mining back into its operational reality. It traces the evolution of mining machines, from the beginning of Bitcoin to the modern ASIC, in order to understand current hardware constraints. We also look at the basics of mining pools, to understand how miners manage to reduce the variance of their income.


### Part 5 - Final section


In the final part of the course, you can test your knowledge of mining by taking your diploma.


The aim of this MIN 101 course is therefore to enable you to leave with a clear, structured and lasting understanding of Bitcoin mining, both technically and economically.


Ready to discover Bitcoin mining? Let's get started!



## Bitcoin mining made easy

<chapterId>278577a6-98bb-4659-86c7-f6c4f6d5fa3e</chapterId>


Before moving on to a detailed and more technical explanation of Bitcoin mining, I'd like to give you an overview of the principle, which is deliberately simple and schematic. If you already have some basic knowledge, you can go straight to the heart of the matter in the next chapter, after answering the quiz questions. This chapter is aimed primarily at beginners, to give you a gentle start.


Imagine Bitcoin as a large public notebook, shared by everyone, where we write down who sent bitcoins to whom. This notebook is called the blockchain. It can't be held by just one person, otherwise it would have to be trusted. Instead, Bitcoin works collectively: thousands of computers verify and maintain the same version of this notebook.


![Image](assets/fr/049.webp)


In Bitcoin, when you make a payment, you create a transaction. This transaction is not instantly added to the notebook. It is first sent to the network, then waits to be integrated into the next transaction packet. This packet is called a block.


![Image](assets/fr/050.webp)


A block is simply a set of transactions grouped together. When a block is ready, it's not enough to publish it. You have to prove to the network that the block is worthy of being added to the pool. This is where mining comes in.


Mining is the work of validating a block by consuming energy. Actors called miners use specialized computers. These machines consume electricity to carry out a very large number of tests, in a loop, until they find a proof that the network accepts. When a miner finds this proof, his block is considered valid.


Once the block has been validated, it is broadcast to the network. The other nodes quickly check that it complies with the rules, then add it to the sequence of previous blocks. This is why it's called a "blockchain": each new block comes after the others, in sequential order, and this chain grows little by little.


![Image](assets/fr/051.webp)


To sum up, transactions are first created. Then, they are grouped together in a block. Then, a miner validates this block by consuming electricity. Finally, this block is added to the blockchain, and the transactions it contains become confirmed.


If miners consume electricity, it's not because they're volunteers. They do it because there's a reward. When a miner validates a block, he receives two types of income. On the one hand, he receives newly created bitcoins. On the other, he collects the fees paid by users for the transactions included in the block. In other words, the miner is compensated both through programmed monetary issuance, and by transaction fees determined by a market.


At this stage, you're deliberately given a very simple view of mining. It doesn't yet explain how the block is constructed in detail, or how exactly the proof miners are looking for works, or how Bitcoin keeps a steady pace, or how the reward is calculated precisely, or how it's claimed. That's okay, that's all we're going to see in the rest of this MIN 101 course!


The aim of this chapter was simply to give you a clear mental structure: transactions → blocks → mining → blockchain → reward. Keep this chain of ideas in mind. In the rest of the course, each chapter will add a layer of technical detail on one of these elements, until you understand not only what's going on, but how and why it works reliably, at scale, without a boss, and without needing trust.


# How proof of work works

<partId>e917e8e3-37f2-46fb-91b2-6a5ce6f0f5c3</partId>


## The Bitcoin transaction path

<chapterId>3b7a3502-4814-4554-8de1-86ac961a2958</chapterId>


To understand what Bitcoin mining is all about, we first need to follow the path of a typical Bitcoin transaction. This will show you exactly where the block comes into play, and why it's at the heart of the system. That's what I'd like you to discover in this first chapter.


In Bitcoin, a transaction is a data structure that transfers ownership of bitcoins from one user to another. In concrete terms, it consumes `outputs` from past transactions (so-called UTXOs), referring to them as `inputs`, and then creates new `outputs` that define to whom these bitcoins now belong and under what conditions they can be spent later.


![Image](assets/fr/001.webp)


An important point about Bitcoin is the authorization to spend. Bitcoins are not in an account, as your money in the bank might be, but are locked by spending conditions. When a wallet wants to use a UTXO as an input, it must provide cryptographic proof that it has the right to unlock it. This proof often takes the form of a digital signature generated from a private key. That's why bitcoiners insist on securing your private keys: it's these that unlock access to your bitcoins and, consequently, enable you to spend them.


![Image](assets/fr/002.webp)


The digital signature in Bitcoin plays two important roles:


- Authorize expenditure: this proves that the user possesses the private key expected by the UTXO expenditure condition;
- Integrity protection: links authorization to the precise details of the transaction (recipients, amounts, fees, etc.). If someone alters the transaction afterward, the signature will no longer be valid.


Once the transaction has been correctly constructed and signed by the user's Bitcoin wallet, it must be broadcast on the Bitcoin network.


### The role of the Bitcoin node in distribution


Bitcoin is a peer-to-peer network: there is no central server that receives and processes all transactions. This role is played collectively by the nodes. A Bitcoin node is a piece of software (e.g. Bitcoin Core) connected to other nodes in the Bitcoin network, whose main mission is to verify, store and relay transactions and blocks.


When you send a transaction from a wallet, the wallet forwards it to a node (your own, or that of a service). This node will first check that the transaction complies with various rules, such as:


- signatures are valid;
- the inputs reference existing UTXOs (i.e. bitcoins that exist);
- these UTXO have not already been spent elsewhere;
- the amount of outputs is less than or equal to the amount of inputs (bitcoins are not created from nothing);
- etc.


If the transaction passes all these checks, the node propagates it to the other nodes in the network with which it is connected. They in turn check it and relay it, and so on. In a matter of seconds, the transaction is propagated and becomes known to the whole, or at least to a large part, of the Bitcoin network.


![Image](assets/fr/003.webp)


### The mempool: the transaction waiting room


Between the moment a transaction is broadcast and the moment it is confirmed in a block, it must wait. This waiting area is called **the mempool** (contraction of `memory` and `pool`). A mempool is therefore a temporary storage space for valid, but still unconfirmed, transactions.


Important point: there's no such thing as a single mempool, only mempools. Each node maintains its own mempool, with its own local constraints. This means that at any given moment, two nodes may have slightly different mempool contents (depending on what they have received, what they have rejected, or what they have purged).


![Image](assets/fr/004.webp)


At this stage, the network knows about the transaction, has verified it and is holding it in memory until it is confirmed. But confirmation of this transaction will only come when a miner inserts it into a block, and this block is accepted by the network.


### Blockchain: a public time-stamping register


As bitcoin is an intangible currency, it has to address one problem: preventing double spending without a central authority. If two transactions attempt to spend the same UTXO, everyone must be able to converge on a single, coherent state. Satoshi Nakamoto sums up this issue with this famous sentence:


> The only way to confirm the absence of a transaction is to be aware of all transactions.

In other words, to know that a bitcoin hasn't already been spent, you need a common record of past spending.


This is the role of the blockchain: a public register containing the history of transactions. But rather than writing each transaction as it happens, Bitcoin groups them into blocks. Each block acts as a history page, and the system thus functions like a time-stamp server: it orders transactions over time in a verifiable way.


This register cannot be rewritten, thanks to a simple principle: each block includes the cryptographic fingerprint (hash) of the previous block. Thus, blocks are linked: if you modify a block from the past, its hash changes, which breaks the link with the next block, which breaks the link with the block after that, and so on. It's this chain of dependencies that gives the "*blockchain*" its name.


![Image](assets/fr/005.webp)


Once we've understood these basic principles of Bitcoin, we can describe a miner's objective in more concrete terms: to build a new block that extends the existing chain, by inscribing pending transactions, and then attempt to make it valid (this is the famous "proof of work" that we'll study in a later chapter). But first, let's discover together in the next chapter how a candidate block is constructed.


## Building a Bitcoin block

<chapterId>2b5cd04b-d400-4865-b0a0-e70fa7e67c17</chapterId>


You've now understood how a Bitcoin transaction works, and the role of the blockchain. However, before we look in more detail at how proof-of-work works, there's still one essential step that the miner must perform: the construction of a candidate block. Let's find out together what a candidate block is and how the miner constructs it, before embarking on the search for a valid proof.


### The candidate block


Miners have to build their blocks themselves before trying to mine them. Each miner, in turn, constructs what is known as a candidate block from the transactions pending in his mempool. Building a candidate block therefore consists of:


- choose which transactions to include;
- organize these transactions in a way that is compatible with Bitcoin rules;
- produce the block's metadata, stored in its header.


The choice of transactions follows a simple economic logic: a block has a capacity limited by the Bitcoin protocol, so the miner seeks to maximize what he earns for this space. He selects as a priority the transactions offering the highest fees relative to the space they occupy in the block (this is known as the "fee rate", expressed in sats/vB). The details of fees will be dealt with later; just remember the idea of sorting by space efficiency.


A Bitcoin block therefore consists of two main parts:


- a list of transactions;
- a block header, which serves, in a way, as block's identity card.


![Image](assets/fr/006.webp)


The header is essential, as it is used as the basis for the proof-of-work: in Bitcoin, you don't mine an entire block directly; you mine only the header of a block, which summarizes the information needed to link the block to the chain and commit its contents. To enable the header to represent all transactions, Bitcoin uses a cryptographic tool: the Merkle tree.


### The Merkle tree: summarizing a large set of transactions


Listing all the transactions in the header would be impossible: a block can contain thousands of transactions, while the header has a fixed size (80 bytes). The solution is therefore to calculate a unique hash that depends on all the transactions in the block: this is the Merkle root.


The principle is as follows:


- the cryptographic fingerprint (hash) of each transaction is calculated;
- these hashes are paired, concatenated, and then hashed again to form a new layer of hashes;
- this process is repeated until a single final hash is obtained: the Merkle root.


![Image](assets/fr/007.webp)


So, if a single transaction changes, even by a single bit, the result is a modification of its fingerprint, which propagates to the Merkle root. This root is included in the block header. So modifying a past transaction means modifying the block header in which it is included, and therefore the block footprint, and then the link with subsequent blocks.


Since SegWit, we've separated the signatures from the rest. So, in reality, there are 2 Merkle trees nested within each block. This separation has consequences for the way we count the size of a block and for certain cryptographic commitments, but the basic idea remains the same: the header must commit, in a compact way, all the contents of the block.


### Block header


The block header is 80 bytes long and contains exactly 6 fields. It is these six elements that will be hashed when searching for a proof of work (see next chapter):



- The version (`version`): This indicates which rules or update signals the block adheres to. It serves as a mechanism for maintaining protocol compatibility and evolution.


- Previous block hash (`previousblockhash`): This is the hash of the previous block's header. This is what links the blocks together. Without this field, we'd have independent blocks. By including the hash of the previous block's header, we obtain a chain, where each new block builds on the previous one.



- Merkle root (`merkleroot`): This is the fingerprint of all the transactions in the block (via the Merkle tree). It links the header to the content: if the miner modifies the selection or order of transactions, the root changes.



- Time stamp: This is a timestamp (Unix time) chosen by the miner (with validity constraints), which must indicate when the block was mined. It doesn't have to be perfectly accurate to the second, but it must meet certain conditions to remain acceptable to the network.



- Encoded difficulty target (`nbits`): This field encodes the current difficulty target. We'll go into more detail in the chapter on difficulty, but remember that this parameter is part of the header.



- Nonce (`nonce`): This is a value that the miner can freely modify. It serves as an adjustable variable during proof-of-work. I'll explain its role in more detail in the next chapter, but it's important to understand that the nonce is part of the block header and is designed to allow successive attempts.


To make this easier to visualize, here's an example of a block header in hexadecimal format (80 bytes):


```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```


Here is a field-by-field breakdown:


```text
version: 00e0ff3f
previousblockhash: 5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
merkleroot: 206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
time: bcb13a64
nbits: b2e00517
nonce: 43f09a40
```


This candidate block header, constructed by the miner, forms the basis of their work. When searching for a valid proof-of-work, it's not the entire list of transactions that is directly hashed in a loop, but rather this 80-byte block, which contains everything needed to link the block to the past and commit its contents, while also including the parameters necessary for the mining mechanism, which we'll explore in the next chapter.


## The hash, the target and the nonce

<chapterId>d054323b-16bd-4556-bac5-4878654e59a3</chapterId>


In the previous chapters, you followed the path of a Bitcoin transaction: created and signed by a wallet, relayed by nodes, stored in mempools, then confirmed when a miner includes it in a block accepted by the network. But we haven't yet seen how a miner can add his block to the blockchain. What's the process behind mining?


Understanding the mining process is pretty straightforward. It boils down to 3 concepts that go hand in hand: a hash function, a target value and a variable that the miner can modify. Let's take a look at how it all works.


### The hash function


A hash function is a tool that takes a message as input and produces an output of fixed size, called "*fingerprint*" or "*hash*".


![Image](assets/fr/010.webp)


The hash function is interesting in computer systems because it has certain properties:



- If you change a single bit of the input, the resulting output hash changes completely and unpredictably;


![Image](assets/fr/011.webp)



- It is impossible to go from the output to the input: the function is irreversible;


![Image](assets/fr/012.webp)



- It's impossible to find two different messages that give exactly the same hash.


![Image](assets/fr/013.webp)


The hash function used in Bitcoin for mining is `SHA256`, applied twice in succession. This is known as double SHA256, or `SHA256d`. It is this double hashing that produces the block's fingerprint.


```text
hash = SHA256(SHA256(message))
```


In our case, the `message` corresponds in fact to the block header, which you saw in the previous chapter. As a reminder, the header is a small structure that summarizes everything in the block.


![Image](assets/fr/014.webp)


### Proof of work: finding a hash smaller than the target


Proof-of-Work is often described as solving a complex problem. In reality, it's not so much a problem as a trial-and-error search: the miner must find a version of the header whose hash (after passing through the `SHA256d` hash function) respects a simple condition: it must be smaller than a certain target.


This condition is formulated as follows:


- the block header’s hash is computed using a hash function;
- we interpret this hash as a number;
- for the block to be valid, this number must be less than or equal to a value called "*difficulty target*".


In other words, a block is valid if:


```text
SHA256d(block_header) <= target
```


![Image](assets/fr/015.webp)


The target is a 256-bit number. As the hash produced by `SHA256d` is also 256 bits, they can be compared as two numbers. The lower the target, the more difficult the condition, as there are fewer possible results below this threshold. Conversely, the higher the target, the easier the condition is to satisfy, and the easier it becomes to mine a block. We'll be taking a closer look at how this target is determined in later chapters.


In this system, the hash function is interesting. Remember that it's easy to calculate the output from the input, but impossible to find an input by knowing only the function's output. In mining, miners are not asked to find a precise hash, but rather to find a hash below a target value. The only way to achieve this is to make a very large number of attempts, until a particular header of their candidate block, when hashed, produces a hash smaller than this target.


Once the target is sufficiently low, this process becomes costly. The miner calculates the hash of its candidate block's header, checks the result and, if the condition is not met, modifies the header and repeats the calculation. This loop is repeated until a valid header is found. When the hash of the header finally satisfies the condition, the proof of work is established, the block is considered valid and can be broadcast on the Bitcoin network for nodes to add to their blockchain. The winning miner then receives the associated reward (we'll detail its composition later), while all the miners immediately set off in search of a new, valid header for the next block.


The fundamental advantage of this mechanism lies in its asymmetry. Producing a proof of work is costly for miners, as it requires a large number of hash calculations. On the other hand, for verifiers, i.e. network nodes, verification is extremely simple: all they have to do is hash the block header supplied by the miner and check that the resulting hash is indeed lower than the target. Finding a proof therefore requires a lot of work and resources, whereas verifying its validity is quick and inexpensive. It is precisely this property that defines an efficient proof-of-work system.


### The nonce


A practical question remains: if the candidate block's header constructed by the miner doesn't give a valid hash, how can the miner try again? He needs to modify something in the header to obtain a different hash. This is precisely the role of the nonce.


Remember the first property of a hash function: changing a single bit of the input is enough to produce a totally different and unpredictable output hash. Each hash calculation is therefore akin to a random draw.


![Image](assets/fr/016.webp)


To try his luck again, the miner doesn't need to modify the entire header of his candidate block: he just needs to change a tiny part of it, because even a single different bit will result in a completely new hash, potentially valid if it's smaller than the target.


This is precisely why the block header contains a nonce. The nonce is a 32-bit value, used once and then replaced. In practical terms, for the same candidate block, a miner can test some 4.29 billion possible values (from `0` to `2^32 - 1`). Each variation of the nonce modifies the block header and, consequently, completely changes the hash produced after applying the `SHA256d` hash function.


The mining process is very simple:


- the miner builds a candidate block (transactions + header);
- then calculates the hash of the `SHA256d(header)`;
- if the result is greater than the target, it changes the nonce;
- starts again;
- etc.


![Image](assets/fr/017.webp)


In fact, the nonce is not the only field that can be modified. Any modification within the transactions of a block results in a change to the root of the Merkle tree, and therefore a modification to the header of that block. With modern computing power, going through the 4.29 billion possible values of the nonce can be done relatively quickly. That's why there's another field, generally referred to as "*extra-nonce*", which further multiplies the possibilities of header variation. We'll come back to this mechanism in more detail in a later chapter.


### What's the point of proof of work?


We call it "proof" because the result is immediately verifiable: once a block has been produced, any node can check, in a fraction of a second, that the cryptographic hash of its header is indeed below the required target. We call it "work" because achieving this hash requires a multitude of attempts, and therefore a real cost in terms of computation and energy.


In the Bitcoin White Paper, Satoshi Nakamoto puts forward two advantages in using a proof-of-work system in Bitcoin:



- **Sealing the economic history:**


Once the computational load has been spent, the block is locked: modifying it would require redoing that block’s proof of work. And as the blocks are chained together, altering an old block would also mean recalculating all the subsequent blocks, and then catching up to and surpassing the ongoing work of the honest chain.


In other words, the proof-of-work serves as the backbone of the time-stamping system, making it increasingly costly to falsify the past as blocks accumulate. When a new block is mined, the security provided by the proof of work is applied simultaneously and uniformly to all existing UTXOs. With each block added, each UTXO thus accumulates an additional amount of security from the Proof-of-Work.



- **Define majority rule (consensus) and neutralize Sybil:**


Proof-of-Work also allows Bitcoin to reach consensus without relying on the "one ID = one vote" voting rule, which could be easily fudged by the massive creation of identities (IPs, nodes, keys...).


In Bitcoin, the "*majority*" is not the greatest number of participants, but the **chain that accumulates the most work**. As Satoshi puts it, this is a "one CPU = one vote" principle, i.e. a vote weighted by the actual computing power spent to produce valid blocks. So deploying thousands of nodes brings no advantage in itself over Bitcoin. Without additional computing power, no more proofs of work are accumulated, and the Sybil attack becomes useless, while the decision rule remains objective and requires no identification of participants.


![Image](assets/fr/018.webp)


[Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System.*](https://bitcoin.org/bitcoin.pdf)


The principles relating to the usefulness and powers of minors are a highly complex subject, which I won't go into in greater detail in this course. However, we will return to this subject in depth in future MIN 201 training courses.


For the moment, you can summarize how mining works like this: miners build a candidate block with the transactions pending in the mempools, then look for a hash of its header (via `SHA256d`) that is less than or equal to a target. They achieve this by testing nonces through trial and error.


In the next chapter, we'll take a brief historical detour into the proof-of-work principle to understand its background, and then look at how the difficulty target is determined by the system.


## The history of proof of work

<chapterId>919d9f3e-8b3b-41d9-b45a-54df4f3c31a3</chapterId>


Proof-of-work was not invented for Bitcoin. Satoshi Nakamoto took up and assembled several older ideas, already explored in different contexts.


### Hashcash


In the late 1990s, the problem of e-mail spam became significant. Indeed, if sending an e-mail costs almost nothing, a spammer can send millions. But if each message requires a small computational effort, sending a single legitimate message remains easy for a normal user, whereas sending millions of messages becomes very expensive.


This is the aim of Hashcash, proposed by Adam Back in 1997, which is considered to be the invention of the proof-of-work principle. The Hashcash principle is very similar to mining: produce a hash that respects a condition (having a certain number of zeros at the beginning of the hash). The proof then accompanies the message and can be verified very quickly by the recipient. If an e-mail is received that does not contain this proof, it can be immediately considered as spam, and therefore filtered. Spammers are then forced to expend a considerable amount of energy to send millions of messages, which drastically reduces (or even completely nullifies) the profitability of this type of operation, whether marketing or fraudulent.


Nowadays, Hashcash is not used for e-mail. Spam filtering is now largely based on centralized systems. Hashcash's advantage over current solutions lies in the fact that it doesn't require centralized filtering: anyone can adjust the parameters according to their own criteria. Nor does it require identification, since a hash search can be performed anonymously. Above all, it does not rely on a reputation system, which tends to introduce subjective forms of filtering.


Hashcash wasn't about creating money. It sought to impose a marginal cost on an easily automatable digital action.


![Image](assets/fr/008.webp)


### Bit Gold


In the late 1990s and early 2000s, Nick Szabo explored the idea of digital scarcity based on proof of work. His conceptual project, called Bit Gold, envisions the creation of units of value by solving a costly proof of work, then recording these proofs in a register to establish a form of ownership.


Bit Gold didn't result in a deployed system like Bitcoin, but it does contain several important insights: the idea that computation can produce scarcity, and the idea of timestamping elements over time to create a history that is difficult to rewrite.


### RPOW


In 2004, Hal Finney proposed RPOW (*Reusable Proofs of Work*). The idea was to produce proofs of work that could then be exchanged, rather than simply consumed. RPOW aimed to create digital tokens based on proof of work, with a system for verifying and transferring these tokens without duplicating them. RPOW, again, did not satisfactorily solve the problem of a totally decentralized registry as Bitcoin would later do, but it remains one of the great precursors of Bitcoin.


![Image](assets/fr/009.webp)


Hashcash, Bit Gold and RPOW use proof-of-work to impose a cost and create a form of scarcity. Bitcoin takes up this mechanism, but gives it a central and collective role: proof-of-work is not only used to create something, it is also used to decide who has the right to write the next page of the register (the next block), and to make this register costly to falsify.


## Adjusting the difficulty target

<chapterId>528bcaa8-351e-4eae-887a-426a78a223e3</chapterId>


In previous chapters, you saw the heart of proof-of-work: miners hash the header of their candidate block with `SHA256d`, and the block is only considered valid if the resulting hash is numerically less than or equal to a reference value called the target. The question then remains: where does this target come from, and how does the system ensure that it remains consistent over time?


Bitcoin is aiming for an average rate of one block found every 10 minutes. Obviously, this pace isn’t guaranteed to the second. In practice, some blocks are found a few seconds after the previous one, while others are found after more than an hour. What matters here is the average over a sufficiently long period.


![Image](assets/fr/019.webp)


This variability stems from the probabilistic nature of mining: each hash is an independent attempt, with a constant probability (assuming the target remains unchanged) of producing a result below the target. It can therefore be compared to a lottery with a continuous draw: the more hashes miners make per second, the shorter the expected delay before the appearance of a valid block, but without ever eliminating the randomness from one draw to the next.


### Why aim for 10 minutes between blocks?


Although there is no evidence of this, Satoshi Nakamoto surely chose 10 minutes as a practical compromise between efficiency and security. A shorter interval would give more frequent confirmations, but would cause more temporary network splits. To understand this point, we need to go back to the way a block propagates.


When a miner finds a valid block, he immediately distributes it to his peers. The nodes that receive it check its validity (transactions, proof of work, consensus rules, etc.), then relay it in turn. This propagation takes a certain amount of time, limited by internet latency, bandwidth and the ability of each node to verify the block.


![Image](assets/fr/020.webp)


If, during this diffusion delay, another miner also discovers a valid block at the same height, the network may be temporarily split: one part of the nodes and miners rely on block A, while the other rely on block B. This is a temporary division of the network.


![Image](assets/fr/021.webp)


These divisions are not catastrophic. The Nakamoto consensus predicts that, in the long term, only one branch will prevail: the one that accumulates the most work. Indeed, as soon as a new block is mined on top of block A, for example, the whole network resynchronizes on this branch and abandons block B, which then becomes a "*stale block*", sometimes erroneously called an "*orphan block*" in everyday language.


![Image](assets/fr/022.webp)


On the other hand, they have a cost: for a few minutes, a fraction of the miners work on a branch that will be abandoned. This work is then wasted from the point of view of overall security, as it has not contributed to the final chain. The faster the interval between each block, the greater the probability of such splits, since the propagation time represents a larger proportion of the time between each block.


The 10-minute interval generally allows enough time for the winning block to propagate widely before a competing block at the same height is found. It's a compromise that limits splits, reduces wasted computing power, and helps the network stay synchronized on a global scale.


### Understanding hashrate


*"Hashrate*" refers to the amount of hash computation produced per second, whether by a single miner, a group of miners, or all miners in Bitcoin. It is expressed in `H/s` (hashes per second), with multiples such as `TH/s` (terahashes per second) or `EH/s` (exahashes per second). This represents the number of attempts miners can make each second to try to get a hash lower than the target.


If the target remains fixed, then:


- each attempt has a fixed probability of success;
- making more attempts per second increases the likelihood that a winning attempt will appear quickly

In other words, if tomorrow's Bitcoin network doubles its computing power by connecting twice as many mining machines, without a corrective mechanism, blocks would be found on average twice as fast. The target must therefore be adjusted to compensate for hashrate variations.


### Adjusting the difficulty target


Bitcoin solves this problem with a periodic target adjustment mechanism, which adjusts the difficulty of mining. The principle is as follows: every 2016 blocks (approximately every 2 weeks), each node recalculates the difficulty target by observing how much time was actually needed to produce these 2016 blocks.


The aim of this mechanism is to reduce the average production time of a block to around 10 minutes, while the overall hashrate of the network is constantly changing, due to machines being disconnected or, on the contrary, new machines being added.


![Image](assets/fr/023.webp)


The calculation is based on the observed time for the period elapsed:


- if the last 2016 blocks were found too quickly, this means that hashrate increased during this period; Bitcoin then makes the condition more difficult by lowering the target for the next period;
- if the 2016 blocks were found too slowly, this means that hashrate has decreased; Bitcoin eases the condition by increasing the target.


The formula is as follows:


```txt
Tn = To * (Ta / Tt)
```


With:


- `tn`: new target
- `to`: old target
- `Ta`: elapsed real time for the last 2016 blocks
- `Tt`: target time (in seconds)


With a target time of two weeks, i.e. `Tt = 1,209,600` seconds:


```txt
Tn = To * (Ta / 1 209 600)
```


To understand how to adjust the difficulty of Bitcoin mining, here's an example with fictitious values:


```txt
Tn = To * (Ta / 1 209 600)
Tn = 18 045 755 102 * (1 000 000 / 1 209 600)
Tn = 14 918 779 020
```

With:

- `**To = 18,045,755,102**`: Old target, i.e. the reference value before adjustment.
- `**ta = 1,000,000 seconds**`: Time actually spent producing the last 2016 blocks. Since this time is less than the target time, the network has mined too quickly.
- `**1,209,600 seconds**`: Target time corresponding to 10 minutes per block for 2016 blocks, used as a reference for adjustment.
- `**tn = 14,918,779,020**`: New target calculated after difficulty adjustment.


Here, the new target is lower than the old one, which means mining becomes harder in order to slow down block production in the next period.

*The target values in this example are simplified and scaled for teaching purposes; the actual target used in Bitcoin is a 256-bit integer of a completely different order of magnitude.*


This calculation is performed locally by each node, based on the timestamps entered in the blocks. As all nodes apply the same rules, they arrive at the same result, and the new target becomes the common reference for the next 2016 blocks.


There's an important detail to note about this adjustment: **it is limited**. Bitcoin limits the variation in difficulty per period in order to avoid too abrupt changes that could block it. In fact, the actual time taken into account is constrained to remain within a range equivalent to a factor of 4 (minimum one quarter of the old target, maximum four times the old target). This prevents extreme retargeting if timestamps are highly atypical or manipulated.


### Target representation


In the block header, the target does not appear in its full 256-bit form, as this would take up too much space. Instead, the 32-bit `nBits` field encodes the target in a compact format, comparable to base 256 scientific notation: an exponent (1 byte) and a coefficient (3 bytes). The complete target is then reconstructed from these two values. We won't go into detail here, as the subject is relatively complex and adds nothing to the understanding of mining. Just remember that the target is not stored in raw form in the block header, but in compact form.


With this final chapter of Part I, we have taken a tour of how proof-of-work works in Bitcoin: the miner builds a candidate block by selecting transactions from its mempool, calculates the candidate block header, hashes it, compares the resulting hash with the period target, then starts again by modifying the nonce until a valid hash is obtained. Finally, every 2016 blocks, the network recalculates a new target in order to maintain an average time of around 10 minutes per block, despite the constant variations in hashrate.



# The Bitcoin mining incentive system

<partId>27fb10c1-d53b-4dc2-90fa-3cb0309b74c1</partId>


## Block reward

<chapterId>b316fb89-9c18-417e-917b-ab98f1722646</chapterId>


As you can imagine, Bitcoin mining is not an altruistic activity. Miners have real costs: electricity to run their mining computers, the purchase of specialized equipment, payroll for maintenance, sometimes premises and cooling systems. For the Bitcoin system to work, the private interests of the miners must be aligned with the collective interests of the network. This is exactly the role of the mining reward. It encourages miners to invest in proof of work, to include valid transactions, and to respect the rules of the protocol rather than trying to corrupt it.


This logic is based on game theory: the protocol makes honesty rational. A miner earns money when he produces a valid block accepted by the nodes. Conversely, if he tries to cheat, his block will be rejected by the nodes, and he will get nothing. Since producing a block has a cost, a rejected block represents a direct loss. In a competitive environment where thousands of players are simultaneously searching for a valid block, the most profitable strategy, most of the time, is therefore to follow the rules strictly and maximize your income honestly.


To achieve this, the Bitcoin protocol stipulates that the miner who finds a valid block wins the right to include a particular transaction in it, which awards the miner a certain sum of BTC. This is known as **block reward**. In this first chapter of this section, the aim is to understand what it's made up of and how it's determined. Later, we'll see how the money creation part evolves over time (with halvings) and how it is actually collected technically (via the coinbase transaction).


### What does the block reward consist of?


In previous chapters, we saw how miners manage to find a valid block. Once a miner has found a header whose hash is smaller than the target, his candidate block is considered valid. He can then distribute it to the entire Bitcoin network. The block is added to the rest of the blockchain, confirming the transactions it contains.


It is precisely this event (the actual addition of the block to the blockchain) that triggers giving a reward to the winning miner. This reward is made up of two distinct elements that are added together:


- **block subsidy**;
- **transaction fees**.


![Image](assets/fr/024.webp)


Let's take a look at what these two parts of the reward correspond to.


### Block subsidy


The block subsidy corresponds to the monetary creation part of the reward. When a miner produces a valid block, the protocol authorizes him to create a certain number of new bitcoins and to allocate them to himself as a reward. These bitcoins are created ex nihilo. They did not exist before.


However, the quantity of newly created bitcoins is by no means arbitrary. It is strictly defined by the Bitcoin protocol rules and is identical for all miners. We'll take a closer look at this mechanism in the next chapter, as the subsidy is not a fixed value indefinitely: it is divided up periodically according to a precise schedule. For now, just remember that:


- the block subsidy is one of the two components of the block reward;
- it is capped and determined by the protocol, not by the miner (even though the miner can technically request less than the maximum amount);
- it creates bitcoins out of thin air.


This subsidy plays two main roles within the Bitcoin protocol. The first is to encourage players to participate in mining. In the early years of Bitcoin (and sometimes still today), transaction fees were very low. The subsidy therefore has guaranteed sufficient compensation to attract miners and maintain a level of security for the system.


The second role relates to currency distribution. Any new currency faces the question of how to distribute monetary units fairly to the population. The block subsidy provides an answer to this problem. By creating bitcoins via mining, it enables their initial distribution in an open and neutral way: anyone can obtain them, provided they participate in the mining, with no prior authorization or identification required.


On the other hand, since these bitcoins are created out of nothing, their value is not without a basis. By increasing the amount of money in circulation, the subsidy mechanically dilutes the value of existing bitcoins. It therefore introduces a form of monetary inflation. However, we'll see in the next chapter that this subsidy is destined to disappear gradually, and that inflation will eventually cease.


![Image](assets/fr/025.webp)


### Transaction fees


The second component of the block reward is linked to system usage: when a user posts a transaction, he wants it to be confirmed. However, block space is limited, and blocks appears on average only every 10 minutes or so. Block space is therefore a scarce resource. When demand exceeds supply, the price rises: this is the transaction fee market. Each miner who manages to produce a valid block obtains the right to collect, for his own account, the full transaction fees associated with all the transactions he has included in his block.


You can think of it as an auction system: each transaction proposes a fee amount, and miners prioritize those that maximize their income, under space constraints. This mechanism naturally aligns interests:


- users in a hurry pay more to be included quickly;
- miners are encouraged to include transactions that pay the highest fees for block space.
- the network avoids spam, because publishing a transaction has a cost.


#### How are transaction fees calculated?


Contrary to popular belief, fees are not an output in a Bitcoin transaction. In fact, a transaction spends inputs and creates outputs. Inputs represent the source of bitcoins used, while outputs represent the destination of payments. Transaction fees are simply **the difference between total inputs and total outputs**.


In other words, the user's bitcoin inputs, which belong to them, create outputs for the recipients, but do not reproduce the full amount consumed by the inputs. The difference between the two represents the transaction fees that the miner can collect.


Let's take an example. A transaction consumes two inputs, one of `100,000 sats` and the other of `150,000 sats`, and creates three outputs of `35,000 sats`, `42,000 sats` and `170,000 sats`.


![Image](assets/fr/027.webp)


The sum of inputs is therefore `250,000 sats`, while the sum of outputs is `247,000 sats`. This means that `3,000 sats` have been consumed in inputs without being recreated in outputs: this amount corresponds to the fees proposed by this transaction.


![Image](assets/fr/028.webp)


If a miner includes this transaction in a valid block, he will be entitled to recover these `3,000 sats`, in addition to the fees of all other transactions included in the block. However, there is no direct on-chain link between the transaction that pays the fee and the sats actually collected by the miner. Technically, the `3,000 sats` in fees are destroyed, and, in return, the miner obtains the right to recreate the same amount for himself.


#### The fee ratio


A block is not limited by the number of transactions, but by its total capacity (today, in practice, by the weight of the block). Some transactions take up more space than others: a transaction with many inputs and outputs will be larger than a simple transaction with a single input and two outputs. The scripts used will also influence size.


![Image](assets/fr/026.webp)


Two transactions may therefore pay the same amount of fees in absolute terms, but not be economically equivalent from the miner's point of view. If one is twice as big, it costs twice as much space in the block. Space is scarce, so the miner seeks to maximize his revenue per unit of space.


This is why, in practice, we express the competitiveness of a transaction with a fee ratio, usually in `sats/vB` (satoshis per virtual byte). Calculating this ratio is straightforward:


```text
fee rate = fee / weight (in vB)
```


For example, if we have a transaction weighing `141 vB` and allocating `1,974 sats` in fees, it will have a fee rate of `14 sats/vB`.


```text
1 974 / 141 ≈ 14 sats/vB
```


This ratio explains the economic choices made by miners: at fixed capacity, including high-rate transactions maximizes the block’s total fees, and therefore the miner's compensation. It also explains why low-cost transactions remain queued in mempools for long periods: they compete with other transactions that pay more per unit of space.


### Network protection against spam


Fees also serve an operational security purpose: they introduce a cost to the multiplication of transactions. If publishing a transaction were free, it would be easy to flood the network with useless transactions and saturate mempools, increasing the load on nodes.


In practice, nodes apply local relay policies (mempool rules) and often set a minimum fee threshold below which they will not relay a transaction (by default, `0.1 sat/vB` in Bitcoin Core via `minRelayTxFee`). A transaction may be valid in the strict sense of the consensus rules, but not relayed by most nodes if its fees are too low. As a result, it doesn't circulate, doesn't reach the miners, and has very little chance of being confirmed.


At this point, you've got the gist of the block reward: it corresponds to the compensation for the winning miner and is made up of two distinct elements. On the one hand, a block subsidy, defined by the protocol rules, which creates new bitcoins ex nihilo. And on the other hand, the fees of transactions included in the mined block.


In the next chapter, we'll focus in more detail on the block subsidy, to understand precisely how it is calculated and how it evolves over time according to the rules of the Bitcoin protocol.


## Halving

<chapterId>7cdca211-7300-48f8-a1e4-53e5c2678cd8</chapterId>


In the previous chapter, we saw that miners who produce a valid block receive a reward consisting of the fees for the transactions included in the block, plus a block subsidy. However, we haven't yet explained how the amount of this subsidy is determined. The mechanism that sets and evolves this value is known as ***halving***.


### What is halving?


Halving is an event programmed into the Bitcoin protocol that halves the block subsidy, i.e. the maximum amount of new bitcoins that the winning miner is allowed to create with each block. It does not affect transaction fees: fees exist independently and remain determined by user activity and competition for block space.


When Bitcoin was launched in 2009, the block subsidy was set at 50 BTC for each mined block. Since then, this subsidy has been halved several times for each halving.


![Image](assets/fr/029.webp)


Halving is not triggered by a date, but by block height. It is executed **every 210,000 blocks**. Since Bitcoin targets an average interval of around 10 minutes per block, 210,000 blocks corresponds to roughly four years.


```cpp
CAmount GetBlockSubsidy(int nHeight, const Consensus::Params& consensusParams)
{
int halvings = nHeight / consensusParams.nSubsidyHalvingInterval;
// Force block reward to zero when right shift is undefined.
if (halvings >= 64)
return 0;

CAmount nSubsidy = 50 * COIN;
// Subsidy is cut in half every 210,000 blocks which will occur approximately every 4 years.
nSubsidy >>= halvings;
return nSubsidy;
}
```


Thus, if we note `n` the number of halvings already occurred, the block subsidy in BTC can be calculated as follows:


```text
subsidy(n) = 50 / 2^n
```


### Past halvings


Here is a summary table of halvings that have already occurred, with their block height, date and the new block subsidy applicable after the event:


| Event               |   Height  | Date                        | Subsidy    |
| ------------------- | --------: | --------------------------- | ---------: |
| Halving 1           |   210 000 | 28 novembre 2012            |     25 BTC |
| Halving 2           |   420 000 | 9 july 2016                 |   12,5 BTC |
| Halving 3           |   630 000 | 11 may 2020                 |   6,25 BTC |
| Halving 4           |   840 000 | 20 april 2024               |  3,125 BTC |
| Halving 5 (upcoming) | 1 050 000 | Spring   2028 (estimation) | 1,5625 BTC |

### When and how does the subsidy end?


Halving is repeated as long as the subsidy can be expressed in the system's minimum unit: satoshi.


```text
1 BTC = 100 000 000 sats
```


As the subsidy is halved, we eventually reach fractions of a bitcoin so small that they become less than 1 satoshi. At this point, it is no longer possible to create half a unit of satoshi. The creation of money through the block subsidy stops, and miners are compensated solely on the basis of transaction fees. From this point on, all bitcoins will be in circulation, and it will no longer be possible to produce new units.


The definitive end to block subsidies will come at block level 6,930,000, i.e. at the 33rd and final halving. This event is expected to take place around the year 2140, although it is impossible to give an exact date, as it will depend on the actual speed at which blocks are found between now and then.


Since the block subsidy follows a geometric sequence with a ratio of 1/2 at each halving, money creation was extremely high in Bitcoin’s early days, and then decreases very quickly. By the 7th halving, over 99% of bitcoins will have already been put into circulation. The 99% threshold is expected to be crossed between 2032 and 2036. This means that it will then take over 100 years to mine the last remaining 1% of bitcoins. While monetary inflation was very high when Bitcoin was launched, to enable widespread distribution of the currency, it is now very low and will continue to fall, until it reaches the level of a true hard currency, whose circulating supply can no longer increase.


![Image](assets/fr/030.webp)


### Why will there never be 21 million BTCs?


Bitcoin's maximum monetary supply is often presented as 21 million BTC. This is a good approximation for understanding its monetary policy, but from a strictly technical point of view, the total supply will never actually reach exactly 21,000,000 bitcoins.


The main reason is mechanical. Through successive halvings, the block subsidy eventually falls below the minimum value of 1 sat, which ends issuance before reaching the exact theoretical total. As a result of this minimum granularity and the rounding rules, the total number of bitcoins created by the subsidy is slightly less than 21 million.


In addition, marginal protocol-related deviations can also add to this. For example, in rare cases, some miners may not have claimed their full subsidy, which definitively reduces the quantity of bitcoins actually issued. We can also mention the genesis block, produced by Satoshi on January 3, 2009, whose bitcoins created are not part of the UTXO set, as well as certain historical events linked to bugs, such as duplicate coinbase transaction identifiers.


Finally, we must also take into account all the bitcoins that have been destroyed or blocked:


- bitcoins locked in unsolvable scripts;
- those deliberately destroyed by `OP_RETURN` scripts;
- or loss of private keys at application level.


In theory, Bitcoin's supply is therefore limited to 21 million. In practice, however, there will never actually be 21 million bitcoins in circulation.


## The coinbase transaction

<chapterId>69476700-3616-4aab-b006-367aba059de9</chapterId>


In the previous chapters, we presented two important points. Firstly, the miner who succeeds in producing and distributing a valid block receives a reward. On the other hand, we saw that this reward is made up of two distinct elements:


- a block subsidy (bitcoins created ex nihilo, the maximum amount of which is set by the protocol and gradually reduced via halvings);
- all transaction fees paid by users whose transactions have been included in the block.


One question remains, however: by what mechanism does the miner collect this reward in Bitcoin? This is precisely the role of a particular transaction called a "coinbase".


### How the coinbase transaction works


As we saw in the first part of the course, each Bitcoin block contains a list of pending transactions that it will confirm. The very first of these is always the coinbase transaction. It is what allows the winning miner to receive their reward.


![Image](assets/fr/031.webp)


At first glance, it looks like a classic Bitcoin transaction: it has a TXID, outputs, and is included in the block's Merkle tree. However, it differs in one important respect: it doesn't spend any existing UTXO.


In a classic Bitcoin transaction, `inputs` reference previous unspent outputs (UTXOs), which provide the input value. Outputs then redistribute this value to new UTXOs, with new spending conditions. In other words, to send bitcoins, you must already own them. The coinbase transaction, on the other hand, consumes no bitcoins in input: it creates bitcoins in output directly from scratch.


It is precisely this mechanism that enables new bitcoins to be introduced into circulation via the block subsidy, and credits the miner with the fees associated with the transactions included in the block. The coinbase transaction cannot reference a real existing UTXO (in fact, it references a fictitious UTXO), since its role is precisely to create part of the value (the subsidy) and recover the other part (the fees), without receiving them from a previous transaction. For the whole system to remain consistent, the portion corresponding to fees must exactly equal the sum of bitcoins consumed in inputs but not recreated in outputs in the other transactions of the block.


![Image](assets/fr/032.webp)


This transaction is not optional. A block that does not contain a coinbase transaction is invalid and will be systematically rejected by network nodes.


⚠️ Please note: the term "*coinbase*" has no connection with the exchange platform of the same name. In Bitcoin, "*coinbase*" historically refers to the transaction that creates the block reward. The company has simply adopted this term for its name.


The coinbase transaction actually fulfils several roles simultaneously:


- The first is the one we have just detailed: it assigns to the miner the reward they are entitled to for having produced a valid block.
- Its second, more technical, role is to anchor the cryptographic commitment to the witnesses (signatures) of the SegWit transactions included in the block.
- A third role, this time not directly protocol-related but linked to the modern industrialization of mining, is that the coinbase is now frequently used to anchor arbitrary technical data. This data is generally linked to the operation of mining pools and their internal organization.


To help you understand these different uses, we'll now take a closer look at the structure of the coinbase transaction.


### The basic structure of the coinbase transaction


A coinbase transaction must contain exactly one input. For simplicity's sake, we sometimes say that it has no input, because this input spends no real UTXO. In reality, there is an input with a referenced source, but it deliberately points to a non-existent UTXO.


As we have already seen, every Bitcoin transaction must consume UTXOs as input in order to create valid outputs. In the Bitcoin transaction, this consumption takes the form of referencing an existing UTXO as input. This referencing is done simply by indicating the identifier of the previous transaction (the one in which the UTXO was created), as well as its index among the outputs of this transaction. In concrete terms, a UTXO is defined by a hash (the previous TXID) and an index.


But in the case of the coinbase transaction, instead of referencing a real existing UTXO, the input must necessarily point to this particular fake UTXO, with a TXID full of zeros, which does not correspond to any real TXID:


```text
0000000000000000000000000000000000000000000000000000000000000000
```

Directly followed by the false index:

```text
0xffffffff
```

![Image](assets/fr/033.webp)


In the basic Bitcoin protocol, as described in Satoshi Nakamoto, this false input is the only constraint imposed on the coinbase transaction.


Like any UTXO referenced in a transaction's input, it is associated with a `scriptSig` field. In a conventional transaction, this `scriptSig` field contains the elements needed to satisfy the `scriptPubKey` and thus unlock the spent UTXO. But in the particular case of coinbase, since the UTXO referenced is deliberately fictitious, the `scriptSig` field is entirely free. Miners can therefore enter any data they like. We’ll look later at how this freedom is used.

In addition to this false input, there are one or more perfectly standard outputs, which enable the miner to collect the bitcoins from the reward on one of their Bitcoin addresses. These outputs are UTXOs locked by a `scriptPubKey` (e.g. a script pointing to an address controlled by the miner or the pool). The only peculiarity here lies in the rule for calculating their value: the total sum of the coinbase's outputs must never exceed the maximum subsidy allowed, to which the block fees are added.


Historically, then, the coinbase transaction is boiled down to this simple scheme: a fake input referencing a non-existent UTXO, and one or more outputs designed to distribute the block reward to the winning miner. Today, however, the coinbase is no longer limited to this distribution role. Its special position in the block and the great flexibility of its structure have led to new uses, both in the protocol itself and in mining pool management mechanisms.


### Other coinbase uses


Over time, the coinbase transaction has become a particularly convenient insertion point for integrating a variety of information useful for mining and for the block structure itself. Let's take a look at them to better understand the overall coinbase organization.


#### The BIP-34


BIP-34 is a fork soft deployed in March 2013, starting with block 227,930, which introduced version 2 of Bitcoin blocks. This new version requires each block to include, in the `scriptSig` of the coinbase transaction, the height of the block being created.


On the one hand, this evolution clarifies the way in which the network agrees to evolve block structure and consensus rules. Secondly, it ensures the uniqueness of each block and coinbase transaction.


Thus, the coinbase's `scriptSig` is not totally free. Since the activation of BIP-34, it is simply constrained to start with the height of the block in which this coinbase transaction is included.


![Image](assets/fr/035.webp)


#### The extra-nonce


As we saw in the first chapters of this course, the miner has a 32-bit nonce field in the block header, which they modify by trial and error to find a hash less than or equal to the target. This 32-bit space already allows a very large number of combinations to be explored, but when mining difficulty is high, this range can be fully exhausted in a relatively short time and thus may yield no combination that produces a valid hash. If all possible values of the `nonce` have been tested without success, the miner must then modify another element to change the block header and start a new series of attempts.


As the coinbase transaction offers a free field via the `scriptSig` of its input, the solution used to extend the nonce's space is to exploit part of this `scriptSig`. This is generally referred to as the extra-nonce. By modifying the extra-nonce, the miner modifies the coinbase's `scriptSig`, i.e. the transaction identifier, then the Merkle root of the block, and finally the block header itself. In this way, they obtain a new search space of hashes to explore, without having to modify the other components of their candidate block.


![Image](assets/fr/036.webp)


#### Identifying pools and miners


Today, a very large proportion of the world's hashrate is organized in mining pools. These structures bring together individual miners to combine their work and reduce the variance of their income.


For operational reasons, mining pools also exploit the free field of the coinbase input's `scriptSig` to insert various pieces of information. These vary from pool to pool and from network protocol to network protocol, but generally include a unique identifier (often an extra nonce structured into several sub-parts) assigned to each miner, to avoid duplication of work within the pool. A pool identification tag is usually added, used for public attribution of found blocks, mining statistics and other tracking purposes.


![Image](assets/fr/037.webp)


#### SegWit's commitment


Since the SegWit soft fork was enabled in 2017, witness data (i.e. generally signatures) has been separated from transaction master data, notably to correct the malleability problem of Bitcoin transactions. This separation therefore introduces a new element to be committed in the block.


To do this, the witnesses are grouped together in another dedicated Merkle tree, whose root is then committed to the coinbase transaction via a `OP_RETURN` output.


![Image](assets/fr/038.webp)


I won't go into more detail on this mechanism in this course, as it's beyond the scope of this article, but just remember that since the introduction of SegWit, the coinbase transaction serves as a vehicle to anchor in the block a fingerprint summarizing all SegWit witnesses. The witnesses are placed in an independent Merkle tree, the root of this tree is written to an output of the coinbase transaction, and this coinbase transaction is itself included in the main Merkle tree along with all the other transactions, whose root appears in the block header. This is how the witnesses, stored separately from the main transaction data, are still committed to the block header.


![Image](assets/fr/039.webp)


#### Arbitrary messages


Since the `scriptSig` allows free insertion of arbitrary information chosen by the miner, some have taken advantage of the opportunity to add messages of a more personal nature, rather than technical ones. The most famous case is of course Satoshi Nakamoto, with his now-iconic message:


> The Times 03/Jan/2009 Chancellor on brink of second bailout for banks

This message, present in the Genesis block (the very first block of Bitcoin) is actually encoded in hexadecimal in the `scriptSig` of the coinbase transaction:


```text
5468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73
```

![Image](assets/fr/034.webp)


### The maturity period

Once the block has been mined and distributed, the coinbase transaction appears on the blockchain like any other transaction. It creates UTXOs for the winning miner, enabling them to collect their reward. However, these UTXOs are not immediately spendable: they are subject to a maturity period. This maturity is set at 100 blocks after the block containing the coinbase. In concrete terms, the coinbase transaction must therefore total 101 confirmations for its outputs to become spendable by the winning miner.

![Image](assets/fr/040.webp)

The aim of this rule is to limit the impact of chain reorganizations on the economy. As we have seen in previous chapters, it can happen that at the same height, two distinct valid blocks are found almost simultaneously by different miners. For a brief moment, the network may split: some nodes receive block A first, while others see block B first. Then, over the course of subsequent blocks, one of the two branches accumulates more work and becomes the reference branch. The other branch is abandoned and its blocks become obsolete. The transactions it contained can then, in theory, return to the mempools awaiting confirmation.


In practice, this rarely happens, because the fee market often results in nearly the same transactions appearing in two competing blocks at the same height. This is one of the reasons why a Bitcoin transaction is commonly considered to become immutable after six confirmations: reorganizations of more than six blocks are so unlikely that they can reasonably be considered impossible.


![Image](assets/fr/041.webp)


The problem with these reorganizations in the case of the coinbase transaction is that it is no ordinary transaction. It introduces brand-new bitcoins into circulation. If the block reward could be spent immediately, a problematic cascade situation could arise:


- a miner spends bitcoins from a coinbase,
- these bitcoins circulate in the economy,
- then the original block was finally abandoned during a reorganization.


The bitcoins in circulation would then never have existed in the final chain, and a series of transactions that were valid at the time of issue would become invalid a posteriori.


The maturity period imposes a timeframe long enough to make this scenario unrealistic. A reorganization of 101 blocks is considered, in practice, impossible (even if there remains an infinitesimal probability). We don't know exactly why Satoshi chose such a high value for maturity, but it is likely that it was chosen so that the mechanism would remain functional, even in the event of major network malfunctions.


This rule prevents newly-created block-reward money from starting to circulate before the block that generated it has been securely buried under a large amount of accumulated work.


---

We've now come to the end of our explanation of how Bitcoin mining works. You should now have a clear picture of the basic mechanisms involved.


In the last part of the course, we'll return to more concrete aspects, to show you how Bitcoin mining materializes in the real world: its industrialization, the machines used, the grouping of players, and so on. The aim will be to give you an overall view of Bitcoin mining, both from the theoretical and protocol perspective we've just seen, and also from its practical and operational side.


# The Bitcoin mining industry

<partId>906a6e18-4718-4a1f-85f5-18854cebdf7c</partId>


## The evolution of mining machines

<chapterId>2d2f9055-75fd-4630-b493-a577d708a39f</chapterId>


In the early days of Bitcoin, mining was not an industrial activity. It was part of the Bitcoin software, launched on a personal computer, often out of curiosity, sometimes to support the network, and secondarily to obtain bitcoins which then had virtually no market value.


Over the years, this activity has undergone a transformation: the machines have changed, the difficulty has exploded, and mining has become an industry in its own right. Let's take a look at the operational aspects of Bitcoin mining.


### Getting started: mining with a CPU


In 2009 and in the early years, mining was mainly carried out using the CPU of a conventional computer. Bitcoin was then just a simple piece of software, serving as a wallet, a node, and a miner. Simply launching the Satoshi Nakamoto's software on your personal computer was enough to participate in the mining process and, in many cases, to find blocks.


A CPU can do everything, but it's not optimized for anything. It executes very general instructions, with complex logic. For a task like repetitive hashing of block headers, it's not the ideal tool, but at network start-up, the difficulty is so low that it's more than enough to find blocks.


This period is important, because it reminds us of an important point: proof of work does not depend on a particular category of equipment. What counts is the ability to calculate hashes faster than others, at a given cost. As soon as a technical advantage appears, it is automatically transformed into an economic advantage. But in absolute terms, it's still possible today to attempt to find Bitcoin blocks using a conventional CPU. This is the approach adopted by the NerdMiner project, for example. The chances of finding a block are virtually nil, but there is still an infinitesimal probability.


https://planb.academy/tutorials/mining/hardware/nerdminer-c9826fd9-c2b4-4d1e-8c78-809122de1654

### Switching to GPUs


Soon enough, miners realized that the bottleneck was not power, but the ability to perform a huge number of similar operations in parallel. This was exactly what graphics processing units (GPUs) could do. Originally, a GPU had been designed to perform the same operations on large quantities of data. This architecture was perfectly suited for a task like repeated hashing: instead of having a few highly versatile cores, you have hundreds, then thousands of units capable of executing the same instructions simultaneously.


With comparable power consumption, a GPU can produce far more hashes per second than a CPU. At the same time, bitcoin had an exchange rate against the dollar, its value was increasing, and exchange platforms were appearing. From then on, the nature of mining began to change. It was no longer just about participating, but about making money. Dedicated configurations appeared: machines built around several graphics cards, sometimes without screens, with a minimal system and specialized software, whose sole purpose was to mine.


It was at this point that the difficulty of mining began to explode. Between mid-2010 and mid-2011, it even increased by a factor of 1,000. Mechanically, specialization begins, just like the early forms of industrialization, and ordinary users—who are content to run the Bitcoin software on their personal computers—now have only a very small chance of finding a valid block.


![Image](assets/fr/044.webp)


*Source: [CoinWarz.com](https://www.coinwarz.com/mining/bitcoin/hashrate-chart)*


Between the GPU era and the modern ASIC era, there was an intermediate phase: the use of FPGAs. An FPGA is a reprogrammable component: it can be configured to directly implement a logic circuit dedicated to a particular calculation, in this case `SHA256d`. The idea was to move even further away from general-purpose hardware (CPU/GPU) to gain in energy efficiency. But soon, the improvements made virtually on FPGAs would be applied physically to the chips themselves: that's the arrival of ASIC.


### The arrival of ASIC


The final stage in the specialization of mining hardware was the appearance of ASICs (*Application-Specific Integrated Circuits*). An ASIC is a chip designed for a single task. In the case of Bitcoin mining, this task is precisely the execution of `SHA256d` at maximum speed and with optimum energy efficiency. Unlike a GPU, a ASIC isn't used to run games, 3D rendering or AI. It's for hashing, and that's all.


![Image](assets/fr/045.webp)


*ASIC S21 XP manufactured by Bitmain*


This specialization has two major consequences:


- The first is a leap in performance and efficiency. For devices of comparable generation, an ASIC produces a far more of hashes per second than a GPU, while consuming less power. Mining with a GPU quickly became uncompetitive: even though it worked technically, the electricity cost far outweighed the expected revenue in most contexts;
- The second is a change of model: investment mainly shifted to industrial-grade hardware. Mining now involves buying machines designed for this purpose, powering them continuously, cooling them, maintaining them, and absorbing their obsolescence. Because an ASIC is not economically eternal: when a new, more efficient generation comes onto the market, the old machines become progressively less profitable, even if they remain functional.


From that point on, we're no longer just talking about a hobby. We're talking about a sector where competitiveness depends on an equation:


- cost of electricity;
- cost of equipment and depreciation;
- ability to cool and operate on a large scale;
- machine availability and reliability;
- speed of communications;
- etc.


### Mining farms


An isolated machine can mine, but by grouping hundreds, then thousands of ASICs in a single location, we share fixed costs, optimize logistics, and move closer to a specialized data center model.


A mining farm, in its simplest form, is a building (or set of containers) filled with ASICs running 24/7. The challenge now is to maintain stable operating conditions:


- supply large amounts of low-cost, stable electrical power;
- manage heat to avoid throttling, as the energy density is considerable;
- filter dust, control humidity, clean;
- real-time monitoring of machine performance (temperatures, hardware errors, hashrate drops, etc.).


![Image](assets/fr/043.webp)


*One of the seven buildings dedicated to Bitcoin mining at Riot Platforms' Rockdale site, near Austin, Texas. This one is specifically dedicated to immersion mining*


Mining is now driven by industrial players, some of them listed on the stock exchange, who are building and operating very large-scale farms. These include MARA Holdings (Nasdaq: `MARA`) and Riot Platforms (Nasdaq: `RIOT`).


![Image](assets/fr/042.webp)


Even without going into the details of profitability models, it's important to understand why mining has taken this form. Proof-of-work is a competitive mechanism: the probability of finding a block, and therefore making money, is proportional to the share of hashrate you deploy. As a result, there is constant pressure to increase computing power, reduce the cost per unit of computation and limit losses. As a result, environments that offer cheaper electricity, a climate conducive to cooling, or an abundant energy infrastructure, naturally become more attractive.


Mining Bitcoin has thus evolved from an activity accessible to anyone in its early days, to one dominated by specialized equipment and professional operations. This does not change the rules of the protocol. In theory, anyone can mine with any machine. But in practice, the level of difficulty and efficiency of ASIC has made domestic mining largely uncompetitive in most contexts.


Of course, there are still situations in which home mining can be of interest, for example if you benefit from very cheap electricity, or if you use the heat generated by your miner to heat your home in winter. But in any case, you'll still need to buy a machine equipped with an ASIC chip. What's more, since your mining power will remain extremely small relative to the Bitcoin network, you'll need to find a way of reducing the variance of your income: this is precisely the role of mining pools, which we'll be discussing in the next chapter.


If you'd like to explore home mining solutions with heat recovery, we have tutorials on various tools, both ready-to-use and DIY:


https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

https://planb.academy/tutorials/mining/hardware/attakai-0d177e6b-e167-4b25-8e38-4ec74213d1fb

## Grouping into mining pools

<chapterId>c871bece-eebe-4ef4-9789-d47251f16c8b</chapterId>


Mining Bitcoin involves ongoing and unavoidable costs, foremost among which is machine power consumption. These expenses are incurred independently of any results, even though revenues from mining are, by their very nature, rare and random. The discovery of a block depends exclusively on the miner's share of hashrate, which makes earnings all the more unpredictable the smaller that share is. It is precisely this practical problem that rapidly led to the widespread use of mining pools. In this final chapter of the MIN 101 course, I offer an introduction to the principles and operation of mining pools in Bitcoin.


### What's a mining pool?


A mining pool is an organization (often an online service) that aggregates the computing power of many independent miners, in order to increase the frequency with which their group finds blocks. When the pool finds a block, the block reward is then redistributed among the participants according to internal pool rules (which will be covered in the MIN 201 course, as they are too complex for MIN 101).


Participants in a mining pool are then often referred to as "hashers", rather than as "miners", as they no longer carry out all the mining work, but simply hash the data transmitted to them by the pool.


Be careful not to confuse the mining pool with the mining farm. These are two different concepts. As we saw in the previous chapter, a farm is a physical site where a single entity operates numerous mining machines. A pool, on the other hand, is above all a virtual grouping: thousands of machines, often geographically dispersed, work under a common coordination. However, a farm can, and often does, participate in a pool.


![Image](assets/fr/048.webp)


### Reducing income variance


So why join a pool? Quite simply because the result of mining activity is probabilistic: with each hash attempt, there is a very small chance that it will meet the difficulty target and therefore produce a valid block.


Over the very long term, your average earnings should be proportional to your share of the overall hashrate. This principle follows directly from the laws of probability: each hash calculation constitutes an independent random draw, and, by the law of large numbers, the frequency with which you discover blocks converges mathematically towards your fraction of the network's total hashrate. In the short to medium term, however, your actual earnings can be extremely irregular. It's this discrepancy between theoretical average and random reality that we call **variance** in mathematics.


Here's a simple example to illustrate the principle:


- The Bitcoin network produces an average of 144 blocks per day (approximately one block every 10 minutes);
- If you have `0.0001 %` of the total hashrate, your expectation is `144 × 0.000001`, or `0.000144` block/day;
- In other words, you should find a block on average every `1 / 0.000144` days, i.e. every 6,944 days, or around 19 years.


But this value corresponds only to a mathematical expectation: the distribution of discovery times follows a random law, so it's perfectly possible, in practice, never to discover a single block, even over a very long period. You can be unlucky and find nothing for a very long time, while paying recurring costs (electricity, maintenance, equipment depreciation...).


The mining pool changes the nature of this problem: by combining hashrates, the pool finds blocks more often. Each participant then agrees to receive only a fraction of each block found, but much more frequently. It's a transformation from a highly volatile, widely-spaced income to a more regular one, at the cost of sharing the rewards and paying service fees.


### Why does variance drop when you group together?


The higher your computing power, the higher your expected frequency of found blocks. More importantly, the more frequent the events, the closer the observed results are to the statistical average over a given period.


On a solo basis, a small-scale miner may go for years without a single block, then get a big payout one day, then nothing. In a pool, the same probabilistic reality still applies, but it's smoothed out at the collective scale: the pool finds blocks more often, and redistribution converts these events into more regular payouts for each participant. **The mining pool therefore sells predictability on the mining activity**.


### Historical landmarks


As we saw in the previous chapter, at the very beginning, mining could be done solo with a conventional computer, as the difficulty was very low. But as the global hashrate exploded (GPU, then ASIC), solo mining became a very time-consuming gamble for most participants.


The first pools were created precisely in response to this new reality. Braiins Pool (formerly Slush Pool / Bitcoin.cz) is the first Bitcoin mining pool: it mined its first block on December 16, 2010. The success of this first mining pool was rapid, as in just a few days it captured nearly 3.5% of the global hashrate.


![Image](assets/fr/047.webp)


On the technical side, pools were then structured around specialized communication protocols between the pool and the miners (e.g. Stratum, then Stratum V2), in order to efficiently orchestrate distributed work. We'll be taking a closer look at these concepts in our MIN 201 training course.


### The modern situation


At the time of writing (early 2026), the global Bitcoin hashrate is at an order of magnitude of zetta-hash per second (= 1,000 EH/s = 1,000,000,000,000,000,000 hashes per second), and almost all the blocks found come from mining pools.


Here is a ranking, to date, of the main mining pools and their respective share of hashrate. This ranking is likely to change by the time you read this course. For up-to-date data, please visit [mempool.space](https://mempool.space/graphs/mining/pools).


![Image](assets/fr/046.webp)


| Ranking    | Pool           | Blocks found  | Hashrate share   |
| ---------: | -------------- | ------------: | ---------------: |
|          1 | Foundry USA    |          1297 |           29.57% |
|          2 | AntPool        |           755 |           17.21% |
|          3 | ViaBTC         |           514 |           11.72% |
|          4 | F2Pool         |           467 |           10.65% |
|          5 | SpiderPool     |           349 |            7.96% |
|          6 | MARA Pool      |           229 |            5.22% |
|          7 | SECPOOL        |           197 |            4.49% |
|          8 | Luxor          |           128 |            2.92% |
|          9 | Binance Pool   |           105 |            2.39% |
|         10 | OCEAN          |            78 |            1.78% |
|         11 | SBI Crypto     |            70 |            1.60% |
|         12 | Braiins Pool   |            54 |            1.23% |
|         13 | WhitePool      |            33 |            0.75% |
|         14 | Mining Squared |            26 |            0.59% |
|         15 | BTC.com        |            16 |            0.36% |
|         16 | Poolin         |            14 |            0.32% |
|         17 | ULTIMUSPOOL    |            14 |            0.32% |
|         18 | GDPool         |            12 |            0.27% |
|         19 | Innopolis Tech |            11 |            0.25% |
|         20 | NiceHash       |             8 |            0.18% |
|         21 | RedRock Pool   |             8 |            0.18% |
|         22 | Unknown        |             2 |            0.05% |
|         23 | Public Pool    |             1 |            0.02% |

*Source [mempool.space](https://mempool.space/graphs/mining/pools), one-month data, December 16, 2025 to January 16, 2025.*


In a more advanced course, we'll go further into the internal workings of the pools (shares, network protocols, payment methods...), because this is where the details that determine both the miner's profitability and the potential implications for Bitcoin come into play.


---

We've now come to the end of MIN 101. Thank you for following it through to the end. If you'd like to assess the skills you've acquired throughout the course, a final exam awaits you in the next section.


With the basic knowledge you've just acquired, you can now take more advanced courses on mining on Plan ₿ Academy, whether in theory, like this one, or more practical courses, so that you too can start participating in Bitcoin mining!


# Final part

<partId>eced8ca1-971d-4a22-9254-dbf8bce15d1b</partId>


## Reviews & Ratings

<chapterId>dc005a96-f4b4-42be-ab72-d4624c110716</chapterId>

<isCourseReview>true</isCourseReview>

## Final examination

<chapterId>959f06cf-fd66-4f29-b7ee-665bfedfea0d</chapterId>

<isCourseExam>true</isCourseExam>

## Conclusion

<chapterId>f16a4e42-c16e-466b-ad16-f42b5360f510</chapterId>

<isCourseConclusion>true</isCourseConclusion>
