---
name: Boltzmann Calculator
description: Understand the concept of entropy and how to use Boltzmann
---
![cover](assets/cover.webp)

The Boltzmann Calculator is a tool for analyzing a Bitcoin transaction by measuring its level of entropy along with other advanced metrics. It provides insights into the connections between the inputs and outputs of a transaction. These indicators offer a quantified assessment of a transaction's privacy and help identify potential errors.

This Python tool was developed by the teams at Samourai Wallet and OXT, but it can be used on any Bitcoin transaction.

## How to use the Boltzmann Calculator?
To use the Boltzmann Calculator, two options are available to you. The first is to install the [Python tool](https://code.samourai.io/oxt/boltzmann) directly on your machine. Alternatively, you can opt for the [KYCP.org](https://kycp.org/#/) (_Know Your Coin Privacy_) website, which offers a simplified usage platform. For [RoninDojo](https://planb.network/tutorials/node/ronin-dojo-v2) users, note that this tool is already integrated into your node.

Using the KYCP site is quite easy: just enter the transaction identifier (TXID) you wish to analyze in the search bar and press `ENTER`.
![KYCP](assets/1.webp)
You will then find different information about the transaction, including the links between the inputs and outputs. Click on `deterministic links`.
![KYCP](assets/2.webp)
You will arrive at the page dedicated to the Boltzmann Calculator indicators.
![KYCP](assets/3.webp)
For those who prefer to use the tool directly from their RoninDojo node, it is accessible via `RoninCLI > Samourai Toolkit > Boltzmann Calculator`.

For local use on your computer, specific instructions for your system are available at this address: [https://code.samourai.io/oxt/boltzmann](https://code.samourai.io/oxt/boltzmann)

As with the KYCP.org site, once the Python tool is installed, you will simply need to paste the TXID of the transaction you wish to analyze.

![KYCP](assets/7.webp)

Then, press the `ENTER` key to get the results.

![KYCP](assets/8.webp)

## What are the indicators of the Boltzmann Calculator?
### Combinations / Interpretations:
The first indicator that the software calculates is the total number of possible combinations, indicated under `nb combinations` or `interpretations` in the tool.

Taking into account the values of the UTXOs involved in the transaction, this indicator calculates the number of ways in which the inputs can be associated with the outputs. In other words, it determines the number of plausible interpretations that a transaction can elicit from the perspective of an external observer analyzing it.
For example, a coinjoin structured according to the Whirlpool 5x5 model presents `1,496` possible combinations: ![KYCP](assets/4.webp)
A Whirlpool Surge Cycle 8x8 coinjoin, on the other hand, presents `9,934,563` possible interpretations: ![KYCP](assets/5.webp)
In contrast, a more traditional transaction with 1 input and 2 outputs will only present a single interpretation: ![KYCP](assets/6.webp)

### Entropy:
The second indicator calculated is the entropy of a transaction, designated by `Entropy`.

In the general context of cryptography and information, entropy is a quantitative measure of the uncertainty or unpredictability associated with a data source or a random process. In other words, entropy is a way of measuring how difficult information is to predict or guess.

In the specific context of chain analysis, entropy is also the name of an indicator, derived from Shannon entropy and [invented by LaurentMT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf), which is calculated with the Boltzmann tool.

When a transaction presents a high number of possible combinations, it is often more relevant to refer to its entropy. This indicator allows measuring the lack of knowledge of analysts about the exact configuration of the transaction. In other words, the higher the entropy, the more difficult the task of identifying bitcoin movements between inputs and outputs becomes for analysts.

In practice, entropy reveals whether, from the perspective of an external observer, a transaction presents multiple possible interpretations, based solely on the amounts of inputs and outputs, without considering other external or internal patterns and heuristics. High entropy is then synonymous with better confidentiality for the transaction.

Entropy is defined as the binary logarithm of the number of possible combinations. Here is the formula used:
```bash
E: the entropy of the transaction
C: the number of possible combinations for the transaction

E = log2(C)
```

In mathematics, the binary logarithm (base-2 logarithm) corresponds to the inverse operation of exponentiating 2. In other words, the binary logarithm of `x` is the exponent to which `2` must be raised to obtain `x`. This indicator is thus expressed in bits.

Let's take the example of calculating the entropy for a coinjoin transaction structured according to the Whirlpool 5x5 model, which, as mentioned earlier, offers a number of possible combinations of `1,496`:
```bash
C = 1,496
E = log2(1,496)
E = 10.5469 bits
```
Thus, this coinjoin transaction displays an entropy of `10.5469 bits`, which is considered very satisfactory. The higher this value, the more different interpretations the transaction admits, thereby strengthening its level of privacy.
For a 8x8 coinjoin transaction presenting `9,934,563` interpretations, the entropy would be:
```bash
C = 9,934,563
E = log2(9,934,563)
E = 23.244 bits
```

Let's take another example with a more conventional transaction, featuring one input and two outputs: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://mempool.space/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce) In the case of this transaction, the only possible interpretation is: `(In.0) > (Out.0 ; Out.1)`. Consequently, its entropy is established at `0`:
```bash
C = 1
E = log2(1)
E = 0 bits
```

### Efficiency:
The third indicator provided by the Boltzmann Calculator is named `Wallet Efficiency`. This indicator assesses the efficiency of the transaction by comparing it to the optimal transaction conceivable in an identical configuration.

This leads us to discuss the concept of maximum entropy, which corresponds to the highest entropy a specific transaction structure could theoretically achieve. The transaction's efficiency is then calculated by confronting this maximum entropy with the actual entropy of the analyzed transaction.

The formula used is as follows:
```bash
ER: the actual entropy of the transaction expressed in bits
EM: the maximum possible entropy for a given transaction structure expressed in bits
Ef: the efficiency of the transaction in bits

Ef = ER - EM
```

For example, for a Whirlpool 5x5 type coinjoin structure, the maximum entropy is set at `10.5469`:
```bash
ER = 10.5469
EM = 10.5469
Ef = 10.5469 - 10.5469 = 0 bits
```

This indicator is also expressed as a percentage, its formula is then:
```bash
CR: the actual number of possible combinations
CM: the maximum number of possible combinations with the same structure
Ef: the efficiency expressed as a percentage

Ef = CR / CM
Ef = 1,496 / 1,496
Ef = 100%
```

An efficiency of `100%` thus indicates that the transaction maximizes its potential for privacy according to its structure.

### Entropy Density:
The fourth indicator is the entropy density, noted on the tool `Entropy Density`. It provides a perspective on the entropy relative to each input or output of the transaction. This indicator proves useful for evaluating and comparing the efficiency of transactions of different sizes. To calculate it, simply divide the total entropy of the transaction by the total number of inputs and outputs involved:
```bash
ED: the entropy density expressed in bits
E: the entropy of the transaction expressed in bits
T: the total number of inputs and outputs in the transaction

ED = E / T
```

Let's take the example of a Whirlpool 5x5 coinjoin:
```bash
T = 5 + 5 = 10
E = 10.5469
ED = 10.5469 / 10 = 1.054 bits
```

Let's also calculate the entropy density for a Whirlpool 8x8 coinjoin:
```bash
T = 8 + 8 = 16
E = 23.244
ED = 23.244 / 16 = 1.453 bits
```

### Boltzmann Score:
The fifth piece of information delivered by the Boltzmann Calculator is the table of matching probabilities between the inputs and outputs. This table indicates, through the Boltzmann score, the conditional probability that a specific input is related to a given output.

It is thus a quantitative measure of the conditional probability that an association between an input and an output in a transaction occurs, based on the ratio of the number of favorable occurrences of this event to the total number of possible occurrences, in a set of interpretations.

Taking the example of a Whirlpool coinjoin again, the table of conditional probabilities would highlight the chances of linkage between each input and output, providing a quantitative measure of the ambiguity of associations in the transaction:

| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
| ------- | -------- | -------- | -------- | -------- | -------- |
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |

Here, we can clearly see that each input has an equal chance of being associated with any output, which enhances the confidentiality of the transaction.
Calculating the Boltzmann score involves dividing the number of interpretations in which a certain event occurs by the total number of available interpretations. Thus, to determine the score associating input No. 0 with output No. 3 (`512` interpretations), the following procedure is used:
```bash
Interpretations (IN.0 > OUT.3) = 512
Total Interpretations = 1496
Score = 512 / 1496 = 34%
```

Taking the example of a Whirlpool 8x8 coinjoin (surge cycle), the Boltzmann table would look like this:

|       | OUT.0 | OUT.1 | OUT.2 | OUT.3 | OUT.4 | OUT.5 | OUT.6 | OUT.7 |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| IN.0  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.1  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.2  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.3  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.4  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.5  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.6  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.7  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |

However, in the case of a simple transaction with a single input and two outputs, the situation is different:

| %       | Output 0 | Output 1 |
|---------|----------|----------|
| Input 0 | 100%     | 100%     |

Here, it is observed that the probability for each output to originate from input No. 0 is `100%`. A lower probability thus translates to greater privacy by diluting the direct links between inputs and outputs.

### Deterministic Links:
The sixth piece of information provided is the number of deterministic links, complemented by the ratio of these links. This indicator reveals how many connections between the inputs and outputs in the analyzed transaction are indisputable, with a probability of `100%`. The ratio, on the other hand, offers a perspective on the weight of these deterministic links within the entire set of transaction links.
For example, a Whirlpool-type coinjoin transaction has no deterministic links, and therefore displays an indicator and a ratio of `0%`. Conversely, in our second simple transaction examined (with one input and two outputs), the indicator is set at `2` and the ratio reaches `100%`. Thus, a null indicator signals excellent confidentiality due to the absence of direct and indisputable links between inputs and outputs.

**External Resources:**

- [Boltzmann Code on Samourai](https://code.samourai.io/oxt/boltzmann) 
- [Bitcoin Transactions & Privacy (Part I) by Laurent MT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [Bitcoin Transactions & Privacy (Part II) by Laurent MT](https://gist.github.com/LaurentMT/d361bca6dc52868573a2)
- [Bitcoin Transactions & Privacy (Part III) by Laurent MT](https://gist.github.com/LaurentMT/e8644d5bc903f02613c6)
- [KYCP Website](https://kycp.org/#/)
- [Medium Article on an Introduction to Boltzmann Script by Laurent MT](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)