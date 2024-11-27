---
name: Introduction to Bitcoin Mining
goal: Understand the functioning of the mining industry through a practical exercise of reusing ASICs.
objectives:
  - Understand the theory behind mining
  - Understand the mining industry
  - Transform an S9 into a heater
  - Mine your first satoshi
---

# Your first steps in mining!

In this training, we will delve into the mining industry to demystify this complex subject! The training is accessible to everyone and does not require any initial investment.

The first section will be theoretical, where Ajelex and I will have an in-depth discussion on various topics related to mining. This will help us better understand this industry and the economic and geopolitical issues associated with it.
In the second section, we will tackle a practical case. Indeed, we will learn how to transform a used S9 miner into a home heating system! Through written guides and videos, we will show and explain all the steps to achieve this at your home :)

Through this video, we hope to show you that the mining industry is more complex than it seems, and studying it helps to nuance the ecological debate that is linked to it!
If you need help with your setup, a Telegram group has been created for students, and all the necessary components can be found on our e-commerce platform!

+++

# Introduction

<partId>a99dc130-3650-563f-8d42-a0b5160af0ab</partId>

## Welcome!

<chapterId>7ad1abeb-a190-5c85-8bff-44df71331e4d</chapterId>

Welcome to MINING 201: an introduction to mining. Ajelex, Jim & Rogzy are excited to accompany you in your first concrete steps in this new industry. We hope you enjoy the course and join the adventure of home mining!

### Course Overview

In this course, the first section will focus on the theory of mining with Ajelex. We will have in-depth discussions on various topics related to mining, which will help us better understand this industry and the economic and geopolitical issues associated with it.

In the second section, we will embark on a fascinating practical case, learning how to transform a used S9 miner into a home heating system. Through written guides and videos, all the necessary steps will be meticulously explained, ensuring your success in this innovative project.

This learning journey will show you that the mining industry is more complex than it appears, offering a balanced perspective on the ecological debate associated with it. Ongoing assistance will be available through a dedicated Telegram group for students, and all the necessary components will be easily accessible on our e-commerce platform.

### Curriculum:

Theoretical Section:

- Explanation of mining.
- The mining industry.
- Nuances of the mining industry.
- Mining in the Bitcoin protocol.
- Bitcoin Price and Hashrate, a Correlation? Sovereignty and Regulation
- Interview with a Mining Industry Professional

Practical Section: Attakai

- Introduction to Attakai.
- Buying Guide.
- Modifying the Software of an Antminer S9.
- Replacing Fans to Reduce Noise.
- Pool Configuration.
- Configuring Antminer S9 with Braiins OS+.

Ready to embark on this captivating adventure? Let's dive together into the fascinating world of home mining!

# Everything You Need to Know About Mining

<partId>aa99ef2c-da29-5317-a533-2ffa4f66f674</partId>

## Explanation of Mining

<chapterId>36a82de7-87ee-5e7a-b69e-48fc30030447</chapterId>

### Mining explained: the puzzle analogy

To explain the concept of mining in a simplified way, a relevant analogy can be used: that of a puzzle. Just like a puzzle, mining is a complex task to perform but easy to verify once completed. In the context of Bitcoin mining, miners strive to quickly solve a digital puzzle. The first miner to solve the puzzle presents their solution to the entire network, which can then easily verify its validity. This successful verification allows the miner to validate a new block and add it to the Bitcoin Timechain. In recognition of their work, which involves significant costs, the miner is rewarded with a certain number of bitcoins. This reward serves as a financial incentive for miners to continue their work of validating transactions and securing the Bitcoin network.

![image](assets/en/01.webp)

Initially in the Bitcoin network, the awarded reward was 50 bitcoins every ten minutes, parallel to the discovery of a block every ten minutes on average by miners. This reward undergoes a halving every 210,000 blocks, approximately every four years. This remuneration serves as a powerful incentive to encourage miners to participate in the mining process despite its energy cost. Without a reward, the electricity-intensive mining would be abandoned, compromising the security and stability of the entire Bitcoin network.
The current mining reward is twofold. On one hand, it includes the creation of new bitcoins, which has decreased from 50 bitcoins every ten minutes initially to 6.25 bitcoins today (2023). On the other hand, it includes transaction fees, or mining fees, from the transactions that the miner chooses to include in their block. When a bitcoin transaction is made, transaction fees are paid. These fees function as a sort of auction where users indicate how much they are willing to pay to have their transaction included in the next block. To maximize their reward, miners, acting in their own interest, select the most profitable transactions to include in their block, considering the limited available space. Thus, the mining reward consists of both the generation of new bitcoins and transaction fees, ensuring a continuous incentive for miners and ensuring the longevity and security of the Bitcoin network.

### Miners and their tools: mining

The mining process involves finding a valid hash that is acceptable to the Bitcoin network. Once calculated and found, this hash is irreversible, similar to potatoes being turned into mashed potatoes. It verifies a certain function without the possibility of going back. Miners, in competition, use machines to calculate these hashes. Although it is theoretically possible to find this hash manually, the complexity of the operation makes this option unfeasible. Computers, capable of performing these calculations quickly, are therefore used, consuming a significant amount of electricity.

In the beginning, the CPU era dominated, where miners used their personal computers for Bitcoin mining. The discovery of the advantages of GPUs (graphics cards) for this task marked a turning point, substantially increasing the hashrate and reducing energy consumption. The progress did not stop there, with the subsequent introduction of FPGAs (field-programmable gate arrays). FPGAs served as a platform for the development of ASICs (application-specific integrated circuits).

![image](assets/en/02.webp)

ASICs are chips, comparable to a CPU chip, however, they are developed to perform only one specific type of calculation in the most efficient way possible. In other words, a CPU is capable of performing a multitude of different types of calculations without being particularly optimized for one type of calculation or another, whereas an ASIC will be able to perform only one type of calculation, but very efficiently. In the case of Bitcoin ASICs, they are designed for the calculation of the SHA256 algorithm.
Nowadays, miners exclusively use ASICs dedicated to this operation, optimized to test the maximum number of combinations with the smallest possible energy consumption and as quickly as possible. These computers, incapable of performing tasks other than Bitcoin mining, are a tangible testament to the continuous evolution and increasing specialization of the Bitcoin mining industry. This constant evolution reflects the intrinsic dynamics of Bitcoin, where a difficulty adjustment ensures the production of a block every ten minutes despite the exponential increase in mining capacity.

To illustrate the intensity of this process, consider a typical miner capable of achieving 14 TeraHash per second, or 14 trillion attempts every second to find the correct hash. At the scale of the Bitcoin network, we now reach approximately 300 HexaHash per second, highlighting the collective power mobilized in Bitcoin mining.

### Difficulty adjustment:

Difficulty adjustment is a crucial mechanism in the operation of the Bitcoin network, ensuring that blocks are mined on average every 10 minutes. This duration is an average because the mining process is actually a game of probabilities, similar to rolling dice in the hope of getting a number lower than the number defined by the difficulty. Every 2016 blocks, the network adjusts the mining difficulty based on the average time required to mine the previous blocks. If the average time is greater than 10 minutes, the difficulty is reduced, and conversely, if the average time is lower, the difficulty is increased. This adjustment mechanism ensures that the mining time for new blocks remains constant over time, regardless of the number of miners or the overall computing power of the network. This is why the Bitcoin Blockchain is also called the Timechain.

![image](assets/en/03.webp)

- Example from China:
  The case of China perfectly illustrates this difficulty adjustment mechanism. With abundant and cheap energy, China was the main global hub for Bitcoin mining. In 2021, the country suddenly banned Bitcoin mining on its territory, resulting in a massive drop in the global Bitcoin network's hashrate, around 50%. This rapid decrease in mining power could have severely disrupted the Bitcoin network by increasing the average block mining time. However, the difficulty adjustment mechanism kicked in, reducing the mining difficulty to ensure that the block mining frequency remains at an average of 10 minutes. This case demonstrates the efficiency and resilience of Bitcoin's difficulty adjustment mechanism, which ensures the stability and predictability of the network, even in the face of sudden and significant changes in the global mining landscape.

### Evolution of Bitcoin mining machines

Regarding the evolution of Bitcoin mining machines, it is important to note that the context is more oriented towards a traditional business model. Miners earn their income from block validation, a task with a relatively low probability of success. The current model in use, the Antminer S9, although an older model launched around 2016, is still in circulation in the second-hand market, trading for around €100 to €200. However, the price of mining machines varies based on the value of Bitcoin, and a newer model, the Antminer S19, is currently estimated at around €3000.

Faced with constant technological advancements in the mining field, professionals must strategically position themselves. The mining industry is subject to continuous innovations, as demonstrated by the recent release of the J version of the S19 and the anticipated release of the S19 XP, offering significantly higher mining capabilities. Furthermore, improvements are not only related to the raw performance of the machines. For example, the new S19 XP model uses a liquid cooling system, a technical modification that allows for a significant improvement in energy efficiency. Although innovation remains a constant, future efficiency gains will likely be smaller compared to those observed so far, due to reaching a certain threshold of technological innovation.

![image](assets/en/04.webp)

In conclusion, the Bitcoin mining industry continues to adapt and develop, and industry players must anticipate diminishing efficiency gains in the future and adjust their strategies accordingly. Future technological advancements, although still present, are likely to occur on a smaller scale, reflecting the growing maturity of the sector.

## The mining industry

<chapterId>0896dfc1-c97e-5bec-9bf1-8c20b3388a2c</chapterId>

### Mining pools

Currently, Bitcoin mining has evolved into a serious and substantial industry, with many players now publicly known and an increasing number of significant miners. This evolution has made mining almost inaccessible for small players due to the high cost associated with acquiring new mining machines. This raises the question of the distribution of hashrate among various market players. The situation is complex because it is essential to examine both the distribution of hashrate among different companies and among different mining pools.

![image](assets/en/05.webp)

A mining pool is a group of miners who combine their computing resources to increase their chances of mining. This cooperation is necessary because an isolated small mining machine is competing against industry giants, reducing its chances of success to a negligible level. Mining works on a lottery principle, and the chances of winning a block (and therefore the Bitcoin reward) every ten minutes are extremely low for an individual small miner. By pooling together, miners can combine their computing power, find blocks more frequently, and then distribute the rewards proportionally to each miner's contribution to the pool.

For example, if a pool finds a block and wins 6.25 bitcoins, a miner contributing 1% of the total computing power of the pool would receive 1% of the 6.25 bitcoins earned. However, it should be noted that mining pools generally take a small commission (usually around 2%) to cover the operating costs of the cooperative.

### Software used by the industry

In the context of Bitcoin mining, the role of software is just as crucial as hardware. An example of this is illustrated by the role of Bitmain, a prolific manufacturer that developed the Antminer S9. In addition to mining hardware, the industry heavily relies on collaborative mining pools, such as Brainspool, which controls approximately 5% of the global hashrate of the Bitcoin network.
The actors in this industry are constantly seeking to increase efficiency through hardware and software. For example, a popular software used in this context is BrainsOS Plus. This software replaces the original operating system of the mining machine, allowing the same operations to be performed more efficiently. With such software, a miner can increase the efficiency of their machine by 25%. This means that for an equivalent amount of electricity, the machine can produce an additional 25% of hashrate, thereby increasing the rewards received by the miner. This software optimization is an essential element of competitiveness in Bitcoin mining, demonstrating the importance of an integrated approach that combines both hardware and software improvements to maximize efficiency and returns.

### Regulation and electricity tariffs

As observed in China and elsewhere, regulation has a significant influence on mining. Although there are no significant miners in France, regulation and high electricity tariffs in Europe are major obstacles. Miners are constantly searching for low-cost electricity to maximize their profits. Therefore, the high cost of electricity in Europe and France does not attract miners to these regions.

Miners tend to gravitate towards regions with low electricity tariffs, often in emerging countries or countries with energy surpluses. For example, a large portion of the global hashrate is located in Texas, United States. Texas has an independent power grid that does not share its energy resources with other states. This uniqueness often leads Texas to produce more electricity than necessary to avoid shortages, creating a surplus. Bitcoin miners take advantage of this overproduction by setting up operations in Texas, where they can mine bitcoins at very low electricity rates during periods of energy surplus. This situation demonstrates the significant influence of regulations and electricity tariffs on Bitcoin mining, highlighting the importance of these factors in miners' decision-making regarding the location of their mining operations.

### Where do miners go and energy management?

By highlighting the impact of Bitcoin miners in the world of energy, the trajectory is clear: these actors are constantly seeking sources of cheap electricity, often those that are wasted or untapped. This phenomenon is evident in regions with new electrical infrastructure, such as those equipped with recent hydroelectric dams.

Let's take an example. In a country that is in the process of building a dam, electricity production often starts before the distribution lines are fully operational. This time gap can result in significant costs and discourage investment in such infrastructure projects. However, bitcoin miners can act as a flexible demand source, ready to consume this "orphaned" electricity, thus helping to offset infrastructure costs. The implication here is that new installations can be immediately profitable, promoting the creation of new sources of electricity. This principle also applies on smaller scales. Whether it's an individual using a hydroelectric generator on a small river or a household equipped with solar panels, the excess electricity produced can be used to power bitcoin mining operations.

In France, for example, surplus electricity from solar panels is injected back into the grid and producers are compensated with a consumption credit from EDF. Similarly, one can imagine a miner operating on this surplus electricity, shutting down when local demand equals supply. Although this may seem selfish, prioritizing bitcoin production over supporting the local power grid, it presents another angle: stabilizing the power grid. The complex management of surplus electricity, sometimes even with associated costs for disposal, can be greatly simplified. Bitcoin miners can absorb these surpluses, acting as a flexible buffer, adjusting demand rather than supply. In a world where electricity production from renewable (non-controllable) sources is constantly increasing, miners can play a key role in ensuring the balance of our power grids, while benefiting from cheap or surplus electricity to power their mining operations.

### Mining centralization

Mining centralization is addressed as a major challenge. Large players, such as Foundry, dominate the market, which can potentially lead to transaction censorship. This centralization can also make the network vulnerable to attacks, including the 51% attack, where an actor or group controls more than 50% of the network's hashing power, allowing them to control and manipulate the network.

Regulation Risk It is emphasized that if a country like the United States were to decide to regulate or ban certain Bitcoin transactions, it could have a significant impact on the network, especially if a large portion of the hashing power is centralized in that country.

![image](assets/en/06.webp)

To combat this centralization, different strategies are discussed:

- Home Mining: The idea of Home Mining is based on the decentralization of mining activity. It encourages individuals to participate in mining from their homes, thus distributing the hashrate more widely.
- Stratum V2: The Stratum V2 protocol offers another approach. Unlike its predecessor, Stratum V2 allows miners to choose which transactions to include in the blocks they mine. This ability strengthens resistance to censorship and reduces the ability of large mining pools to dominate the network. By giving more power to individual miners, the Stratum V2 protocol can play a decisive role in the fight against hashrate centralization.
  Open-Sourcing Mining Software
- Open-sourcing mining software: This is another potentially effective strategy. By making mining software accessible to everyone, small miners would have the same opportunities as large mining companies to participate and contribute to the blockchain network. This approach would encourage a broader distribution of hashrate, thus contributing to network decentralization.
- Diversification of Actors and Geography: Encouraging the participation of diverse actors from different geographical regions in cryptocurrency mining can also prove effective. By diversifying the hashrate geographically, it becomes more difficult for a single actor or country to exert disproportionate control or influence over the network. This approach can help protect the network against potential attacks and strengthen its decentralization.

The general conclusion is that decentralization is crucial for the security and resilience of the Bitcoin network. Although centralization can offer efficiency benefits, it exposes the network to significant risks, including censorship and 51% attacks. Initiatives like Takai and the adoption of new protocols like Stratum V2 are important steps towards decentralization and protecting the Bitcoin network against these threats.

## Nuances of the Mining Industry

<chapterId>7b9ee427-316a-54e3-a2d4-4ea97839a31b</chapterId>

### The principle of Attakai

In the current context, Bitcoin mining with the S9 model may seem complex, but a deeper analysis opens the door to innovative alternatives. The Attakai principle is based on considering the use of mining installations in various types of buildings, such as schools or hospitals. The main idea is to place a few mining machines in different locations, thus reusing the heat emitted by these machines to heat the establishments. By opting for more efficient models such as the S19, it would be possible to distribute mining activity, thereby enhancing overall performance while also contributing usefully to society. This initiative aims to compete with large centralized mining operations by using the heat generated by mining machines in a productive and efficient way.

The Attakai initiative stems from a personal home-mining experiment conducted by two friends eager to actively participate in the Bitcoin network. They faced major obstacles, such as the high noise levels of mining equipment, designed for industrial rather than domestic use. To address this issue, hardware modifications were made to the mining machines. More efficient and quieter fans replaced the original equipment, making home mining more accessible and less disruptive. Additionally, the inclusion of a Wi-Fi adapter eliminated the need for a wired Ethernet connection, further simplifying the home-mining process. In winter, these modified miners were used as a heating source, turning a nuisance into a benefit.

After presenting their project to the Bitcoin community and seeing the interest it generated, the inventors of Attakai decided to publish detailed guides on the Découvre Bitcoin platform, allowing anyone to replicate their home-mining experience. They now plan to extend this concept beyond the domestic setting. The goal is to demonstrate how a modified miner can be transformed into a quiet auxiliary heater usable during the winter, offering a smooth transition to a second part of the training, focused on the practical implementation of these modifications, illustrated by explanatory videos. However, the question remains whether this initiative can be expanded on a larger scale, offering a realistic and sustainable alternative to current centralized mining structures.

![image](assets/en/07.webp)

### The limit of this decentralization?

Although the idea of decentralizing mining through the productive use of generated heat seems promising, it has certain limitations and questions remain. Energy-intensive establishments such as saunas and pools could benefit from this concept by using the heat produced by miners to warm the water in their facilities. This practice is already being implemented by some members of the Bitcoin community, who are exploring different methods to efficiently utilize the heat generated by mining equipment. For example, a banquet hall could theoretically be heated by three or four S19 miners, each consuming 3000 watts and producing an equivalent amount of heat.

However, it should be noted that energy consumption and heat production are equivalent, whether the energy is used by an electric heater or a miner. For every kilowatt of electricity used, the amount of heat produced will be the same in both cases. The difference lies in the fact that the miner not only provides heat but also a bitcoin reward, thus offering an economic incentive to use a miner instead of a simple electric heater. This additional reward could help alleviate concerns about the high energy consumption of miners.

The question of the long-term efficiency and feasibility of using bitcoin miners for heating remains open. Ongoing innovations in mining hardware and heating technologies may potentially open up new avenues for more efficient use of the heat generated by mining, thereby contributing to the viability of this approach in the future.

### Why have BTC rewards?

The question of rewarding in bitcoin rather than another currency is essential in the system envisioned by Satoshi Nakamoto. The creation of Bitcoin is characterized by a fixed cap of 21 million units. The goal was to find a fair way to distribute these newly created units. Miners, by providing their computing power to secure the network and make any attack increasingly costly, effectively protect the Bitcoin network. In return for this crucial contribution, they are rewarded with newly created bitcoins, facilitating the distribution of coins within the ecosystem.

It is a win-win system. Miners are rewarded for both securing the network and approving transactions. The newly created bitcoins are given as an incentive to strengthen security, and transaction fees are an additional income for approving transactions. These two elements combined make up the total reward for mining. The question of the future of mining arises due to the programmed reduction of mining rewards, halving every four years, an event known as "halving". By 2032, the block reward will be less than one bitcoin, and by 2140, no new bitcoins will be created. At this point, miners will rely solely on transaction fees for compensation. The Bitcoin network will need to support a large number of transactions, with sufficiently high fees, to ensure mining profitability.

The rise of the Lightning Network, which allows for fast and low-cost transactions outside of the main Bitcoin chain, raises questions about the future of mining. The Lightning Network has the potential to significantly reduce transaction fees, thereby impacting miners' income. However, this will depend on the adoption and use of the Lightning Network compared to the main Bitcoin network. In a pessimistic scenario, miners may find it profitable to mine even at a loss if they have amortized their costs and have access to cheap electricity. In a more optimistic scenario, transaction fees on the main Bitcoin network could remain high enough to maintain mining profitability.

### What should be included in a Bitcoin block?

Regarding the question of what should be included in a Bitcoin block, it is crucial to consider the complementary nature of the different layers of the Bitcoin network. Although the Lightning Network can enable faster and cheaper transactions, it still relies on the base layer of Bitcoin, often referred to as the "settlement layer," for opening and closing payment channels.

With the expected growth of the Lightning Network and the consequent increase in channel openings and closings, space in Bitcoin blocks will become increasingly valuable. The Bitcoin community already tends to value the preservation of this space, recognizing its intrinsic limitation. This awareness has led to discussions about the legitimate use of block space, with concerns about "spam" on the blockchain from transactions considered non-essential.

![image](assets/en/08.webp)

Speculation surrounds the future use of block space, but it is generally accepted that it is a scarce resource that should be used wisely. Even though there is a desire to fill it, it is essential to preserve it to ensure the long-term viability of the Bitcoin network, anticipating a future increase in demand for block space. As in any free market, supply and demand will regulate the use of block space. With limited supply, stakeholders will need to make informed choices about the use of this valuable space to ensure the long-term efficiency and security of the Bitcoin network.

## Bitcoin Mining in the Bitcoin Protocol

<chapterId>879a66b0-c20a-56b5-aad0-8a21be61e338</chapterId>

The role of miners in the Bitcoin network has been a subject of intense debate during the block size wars. Although essential for the security and functionality of the network, miners do not necessarily hold the ultimate power in the Bitcoin ecosystem. The balance between miners, nodes, and end-users ensures the integrity and distribution of the network.

### The Block Size Wars

During the block size wars, many miners were opposed to certain developments in the network, highlighting the tension between different actors in the ecosystem. The question remains on how to balance power among miners, nodes, and users to ensure the long-term security of Bitcoin.

![image](assets/en/09.webp)

The security dilemma of Bitcoin rests on a delicate balance. While miners play a crucial role in validating and creating blocks, nodes maintain integrity by verifying and validating transactions and blocks. An incorrect or fraudulent block will be rejected by the nodes, thus censoring the miner and preserving the security of the network. Power is also held by the nodes and users of the Bitcoin network. Nodes have the power of verification and validation, while users have the power to choose which blockchain to use. This distribution of power ensures the distribution and integrity of the Bitcoin network.

The block size wars revealed the uncertainty and tension inherent in managing the Bitcoin network. Although Bitcoin Core is currently the dominant chain, the debate over governance and network management continues.

Ultimately, responsibility is shared among all actors in the Bitcoin network. A decrease in the number of users, nodes, or miners could weaken the network, increasing the risk of centralization and vulnerability to attacks. Each actor contributes to the robustness and security of the network, reinforcing the importance of maintaining a balance of power and responsibility.

### The power of miners

Satoshi Nakamoto's elegant game theory established a situation where each actor in the Bitcoin network is incentivized to act correctly to protect both their own interests and those of other participants. This creates a balance where bad behavior can be reprimanded, thus enhancing the security and stability of the entire system. Despite this balance, states remain a potential threat. As indicated in the presentation at Surfing Bitcoin 2022, states can attempt to attack the mining industry, exposing the Bitcoin network to risks of centralization and attack. Hypothetical scenarios such as a military attack targeting mining hardware production facilities highlight the importance of geographical and industrial diversification for the resilience of the Bitcoin network.

![image](assets/en/10.webp)

The centralization of mining hardware production in China poses another risk. A refusal to export mining machines or an accumulation of hashrate for a potential 51% attack by China underscores the need for diversified mining hardware production. In response to these risks, the Bitcoin community is actively exploring solutions. Companies like Intel are considering producing mining equipment in the United States, contributing to the distribution of production. Other initiatives, such as Block's open-source Mining Development Kit (MDK), aim to decrease the monopoly of mining hardware design and production, allowing for a broader distribution of hashrate. At the heart of these discussions lies Bitcoin's fundamental mission: to be a censorship-resistant value exchange network. The Bitcoin community is constantly striving to strengthen distribution, resistance to censorship, and network anti-fragility, rejecting proposals such as the transition to proof of stake, which do not align with these fundamental principles.

### The physical link of Proof of Work vs Proof of Stake

Proof of Work (PoW) is essential because it represents the physical link between the real world and Bitcoin. Although bitcoins are intangible, their production requires tangible energy, thus establishing a direct connection with the physical and real world. This connection ensures that the production and validation of bitcoins and blocks have a real energy cost, thereby anchoring the Bitcoin network in physical reality and preventing its complete domination by powerful entities. PoW acts as a bulwark against centralization, ensuring that participation in the network and validation of transactions require an investment in tangible resources. This prevents the monopolization of the network by entities that could otherwise take control without any significant entry barrier, thus ensuring a more equitable distribution of power and influence within the Bitcoin network.

![image](assets/en/11.webp)

### The limitations of Proof of Stake

On the other hand, Proof of Stake (PoS), although it allows for small-scale participation, does not guarantee equivalent protection against centralization. In a PoS network, those who already hold a large amount of the currency have disproportionate power, reflecting existing power inequalities in society at large. This dynamic could potentially perpetuate centralization and the concentration of power in the hands of a few, contrary to the fundamental distribution objectives of the Bitcoin network. The argument that everyone can participate in PoS, even on a small scale, by joining pools, is not necessarily robust. In a PoW network, even a small contributor, with modest equipment, can actively participate and contribute to the security and distribution of the network.

### Recap

To recap, miners fortify the Bitcoin network against censorship by using electricity to compute Bitcoin's proof of work, and are rewarded with new bitcoins and transaction fees. With the professionalization of the industry, various players emerge, playing different roles, from chip creation to the management of mining farms. Additionally, finance also plays a role, exerting control by deciding who survives during different market phases. The issue of centralization persists, with the wealthiest entities potentially dominating the market. However, alternatives are being developed at both the hardware and software levels. It is up to each individual to act and contribute to the distribution of the network. Bitcoin represents an extraordinary opportunity not only in terms of freedom but also energy independence. Despite controversies surrounding its electricity consumption, Bitcoin offers an economic incentive for a transition towards a more rational and abundant use of energy, realizing what was previously an ecological ideal.

## Bitcoin Price and Hashrate, a Correlation?

<chapterId>e6676214-007c-5181-968e-c27536231bd6</chapterId>

### Hashrate, price, and profitability

The current hash rate, despite Bitcoin's price being at $30,000 compared to its previous peak of $69,000, highlights the tangible link between mining and the real world. Bull market periods lead to a high demand for Bitcoin mining and an increase in machine orders from manufacturers such as Avalon and Bitmain. However, production and delivery are not instantaneous, creating a mismatch between increased demand and later availability. This can lead to machines ordered during a bull market being delivered in a bear market, highlighting a notable asymmetry between a low price and a high hash rate.

This situation also illustrates the resilience of Bitcoin, often assessed based on its price. However, a deeper analysis of Bitcoin's health requires examining its hash rate, which measures the calculations per second in the Bitcoin network. While the price of Bitcoin fluctuates, its cost, linked to the electricity needed to operate mining machines, remains essential for understanding market dynamics. By focusing on cost rather than price, a more consistent perspective on Bitcoin's stability and long-term viability is obtained. Generally, the cost of Bitcoin is proportional to its price, providing a better understanding of price fluctuations and future outlooks.

![image](assets/en/12.webp)

### Hash rate and reward

Mining may establish a floor price for Bitcoin, below which miners would sell at a loss. The cost of mining significantly influences the price, as illustrated by the ban on mining in China, where the hash rate and price dropped significantly but were quickly recovered. Focusing solely on the price can be misleading. Studying the cost, via profitability calculators, offers a more balanced perspective. However, the market can behave irrationally, with miners potentially being forced to sell at a loss, potentially lowering the price below the mining cost. To assess the health of Bitcoin and its decentralization, an equation incorporating various factors, such as the number of nodes and the price, could be developed. This approach could provide a more nuanced analysis of Bitcoin compared to discussions based solely on price.

### Mining for profit or for the network?

The question is profound and encompasses several dimensions of Bitcoin mining. The balance between seeking profit and contributing to the security and distribution of the Bitcoin network is a constant dilemma for miners. The debate continues in the Bitcoin community, with strong arguments on each side.

- Mining for profit:

* For: Miners are naturally attracted to the potential earnings from Bitcoin mining. Investing in expensive mining equipment can be offset by mining rewards and transaction fees, especially when the price of Bitcoin is high.
* Against: The pursuit of profit can lead to the centralization of hashing power if only a few large companies can afford to invest in high-end mining equipment. Additionally, mining for profit can have a significant environmental impact.

- Mining for the network:

* For: Mining to contribute to the security and decentralization of the Bitcoin network is a noble initiative. It helps strengthen the network's resilience and resist censorship and attacks.
* Against: Without sufficient financial incentive, it may be difficult for miners to continue supporting the network, especially if they operate at a loss.

The Attakai initiative highlights the importance of contributing to the network while offering solutions to make mining more accessible and less harmful. The possibility of mining at home, with more affordable equipment and solutions to reduce noise pollution, can help democratize Bitcoin mining. It encourages those interested in Bitcoin not only to invest and hold bitcoins but also to actively participate in securing the network. By providing tested equipment and guides for assembly and installation, Attakai makes it easier to enter the world of Bitcoin mining. It also encourages innovation and continuous improvements, inviting the community to contribute and share their ideas and experiences to enhance home mining. The Attakai model is an answer to the question of mining for profit or for the network. It's not just about making profits, but also about strengthening the distribution and security of the Bitcoin network, while enabling more people to participate in mining, learn, and understand this crucial industry. The challenge of a potential mining ban in Europe remains an open question. This raises concerns about the future of Bitcoin mining in the region and the need for balanced regulation that recognizes the importance of mining for the security and viability of the Bitcoin network while addressing environmental issues. Attakai and other similar initiatives can play a crucial role in this debate, showing that it is possible to mine in a more sustainable and responsible manner, while positively contributing to the Bitcoin network.

## Sovereignty and Regulation

<chapterId>9d9a5908-2acc-501e-906b-a6fce9ecfebd</chapterId>

### Sovereignty before profit?

To address the crucial issue of wealth through mining, it is important to consider various perspectives and approaches. Questions about the profitability of mining are common, with inquiries surrounding the purchase of shares in companies like Riot or the leasing of mining machines in countries with low energy costs such as Iceland or Russia. Before venturing into mining, a key consideration would be to compare the profitability of mining to the direct purchase of Bitcoin. If the cost of mining a Bitcoin exceeds the cost of buying it directly, it is generally wiser to purchase the Bitcoin directly. This avoids the multiple challenges and costs associated with the mining process.

However, mining offers unique avenues to get involved in the Bitcoin ecosystem. For example, mining Bitcoin in winter can be a clever way to heat your home while generating Bitcoin revenue. Another option is to invest in companies that sell mining equipment and store and manage the machines in locations with low energy costs, thus providing access to favorable electricity rates without the hassle of managing the equipment.

Despite these options, mining presents significant challenges. The well-known adage in the world of cryptocurrencies, "Not your keys, not your Bitcoins," finds a similar resonance in the world of mining: "Not your hashrate, not your reward." Stories of disappointments and disconnected machines are common, with many players promising exceptional results but failing to deliver. Issues with electricity supply and machine breakdowns can leave investors powerless, with expensive equipment they do not control. In this context, caution and a deep understanding of the mining sector are crucial before venturing into it. While opportunities for gains exist, the risks are significant, and an informed and thoughtful approach is essential for navigating this complex and often unpredictable field. It is therefore vital to conduct thorough research and carefully weigh the pros and cons before engaging in Bitcoin mining.

![image](assets/en/13.webp)

### Virgin Bitcoins

The aspiration to own one's own hashrate appears as a promising path in the world of mining. However, navigating this complex ecosystem requires a cautious approach. The field of cloud mining is marked by a large number of scams, fueled by a lack of understanding of mining from many investors. Attractive offers, packaged in various ways, can easily mislead those who are not sufficiently informed. On the other hand, owning your own mining equipment offers considerable advantages. Besides the personal satisfaction of actively contributing to the security of the Bitcoin network and seeing rewards fall into your wallet, there is the appealing aspect of "virgin bitcoins." These are freshly mined bitcoins, which have never been spent and have no history attached to them. These bitcoins are often considered more valuable because they have never been "tainted," offering a certain guarantee against rejection by regulators or major exchange platforms.

The possibility of mining virgin bitcoins while avoiding Know Your Customer (KYC) procedures is another added value. Many mining pools do not require the identity of miners, thus allowing the acquisition of bitcoins without undergoing tedious identity checks. Virgin bitcoins are perceived as "clean," bearing no past history or association. They are particularly sought after by large institutional players who can guarantee the legitimacy of their digital assets in the face of regulatory authorities. However, despite these advantages, it is crucial to recognize that the mining industry remains extremely competitive and volatile, and unforeseen incidents can disrupt mining operations.

In this context, choosing an autonomous and educated approach to mining appears wise. Acquiring one's own hashrate and investing in personal mining equipment, while remaining aware of the risks and challenges, can potentially offer a safer and more satisfying path to acquiring virgin bitcoins, thus enhancing the financial sovereignty of the individual while supporting the Bitcoin ecosystem as a whole.

### Is mining banned in Europe?

With the issue of the potential ban on mining in Europe, discussions about regulation are becoming increasingly relevant. The fluctuating regulatory landscape can indeed significantly influence the Bitcoin mining industry. The ban on mining in Europe is a conceivable scenario, especially considering precedents in China. Although mining operations continue in China despite the ban, Europe could follow a similar path. A broader distribution of the hashrate across different regions could help strengthen the mining community in Europe, enabling them to effectively counter misunderstandings and misconceptions about mining, its environmental impact, and its footprint on the electrical grid.

![image](assets/en/14.webp)

Faced with campaigns like those of Greenpeace and the often misleading figures from some studies, the best weapon remains truthful information. It is essential to inform the general public and decision-makers about the reality of mining, its complexity, and its nuances, rather than letting them rely on stereotypes and inaccurate information. The more people are informed and aware of what mining truly is, the better the industry can defend itself against potential restrictive regulations.

In conclusion, despite the regulatory risk and the possibility of a mining ban in Europe, the most powerful weapon remains education and information. A clear and precise understanding of mining, how it works, and its impact can help demystify the industry and fight against misinformation, thus offering better resistance to potentially damaging regulations. The initiative to train and inform people about mining, as this discussion does, is a step in the right direction to ensure the sustainability and growth of mining in Europe, and around the world. Continuous efforts to educate and inform are essential to ensure a safe and prosperous future for the Bitcoin mining industry.

# Home Mining and Heat Reuse

<partId>78d22d06-2c4a-573f-86bb-1027115dad3a</partId>

## Attakai - Making Home Mining Possible and Accessible!

<chapterId>1f5d1b74-2f99-5f31-a088-a73d36491ebf</chapterId>

Attakai, which means "the ideal temperature" in Japanese, is the name of the initiative aimed at discovering bitcoin mining through heat reuse launched by @ajelexBTC and @jimzap21 with Découvre Bitcoin.
This ASIC retrofitting guide will serve as a basis for learning more about mining, its operation, and the underlying economy by demonstrating the possibility of adapting a Bitcoin miner for use as radiators in homes. This offers more comfort and savings, allowing participants to receive non-KYC BTC cash back on their electric heating bill.

Bitcoin automatically adjusts the mining difficulty and rewards miners for their participation. However, the concentration of hashrate can pose risks to the neutrality of the network. Using Bitcoin's computing power for heating solutions directly benefits the network itself by increasing the distribution of computing power.

### Why reuse the heat from an ASIC?

It is important to understand the relationship between energy and heat production in an electrical system.

For an investment of 1 kW of electrical energy, an electric radiator produces 1 kW of heat, no more, no less. New radiators are not more efficient than traditional radiators. Their advantage lies in their ability to continuously and evenly distribute heat in a room, providing more comfort compared to traditional radiators that alternate between high heating power and no heating, thus generating regular temperature variations and discomfort.

A computer, or more broadly an electronic board, does not consume energy to perform calculations, it simply needs energy to flow through its components to function. Energy consumption is due to the electrical resistance of the components, which produces losses and generates heat, known as the Joule effect.

Some companies have come up with the idea of combining computing power needs with heating needs through radiator/servers. The idea is to distribute a company's servers into small units that could be placed in homes or offices. However, this idea faces several problems. The need for servers is not related to the need for heating, and companies cannot use the computing capabilities of their servers flexibly. There are also limits to the bandwidth that individuals can have. All these constraints prevent the company from making these expensive installations profitable or providing a stable online server offering without data centers that can take over when heating is not needed.

> The heat generated by your computer is not wasted if you need to heat your home. If you use electric heating where you live, then the heat from your computer is not wasted. It costs the same to generate this heat with your computer. If you have a cheaper heating system than electric heating, then the waste is only in the cost difference. If it's summer and you use air conditioning, then it's double the waste. Bitcoin mining should take place where it is cheaper. Maybe it will be where the climate is cold and where heating is electric, where mining will become free.  
>  
> Satoshi Nakamoto - August 8, 2010  

Bitcoin and its proof of work stand out because they automatically adjust the mining difficulty based on the amount of computation performed by the entire network. This amount is called the hashrate and is expressed in hashes per second. Today it is estimated at 380 exahashes per second, which is 380 billion billion hashes per second. This hashrate represents work and therefore an amount of energy expended. The higher the hashrate, the higher the difficulty, and vice versa. Thus, a Bitcoin miner can be activated or deactivated at any time without affecting the network, unlike radiators/servers that need to remain stable to provide their service. The miner is rewarded for their participation, relative to others, no matter how small it may be.

In summary, an electric radiator and a Bitcoin miner both produce 1 kW of heat for 1 kW of electricity consumed. However, the miner also receives bitcoins as a reward. Regardless of the price of electricity, the price of bitcoin, or the competition in Bitcoin mining activity on the network, it is economically more advantageous to heat with a miner rather than an electric radiator.

### The added value for Bitcoin

What is important to understand is how mining contributes to the decentralization of Bitcoin.
Several existing technologies have been ingeniously combined to bring Nakamoto's consensus to life. This consensus economically rewards honest participants for their contribution to the operation of the Bitcoin network, while discouraging dishonest participants. This is one of the key points that allows the network to exist sustainably.
Honest actors, those who mine according to the rules, are all competing with each other to obtain the largest possible share of the reward for producing new blocks. This economic incentive naturally leads to a form of centralization as companies choose to specialize in this lucrative activity by reducing their costs through economies of scale. These industrial actors have an advantageous position for purchasing and maintaining machines, as well as negotiating wholesale electricity rates.

> At first, most users would run network nodes, but as the network grows beyond a certain point, it would be left more and more to specialists with server farms of specialized hardware. A server farm would only need to have one node on the network and the rest of the LAN connects to that node.  
>  
> Satoshi Nakamoto - November 2, 2008  

Certain entities hold a considerable percentage of the total hashrate in large mining farms. We can observe the recent cold wave in the United States where a significant portion of the hashrate was taken offline to redirect energy to households with an exceptional need for electricity. For several days, miners were economically incentivized to shut down their farms, and this exceptional weather can be seen on the Bitcoin hashrate curve.

This issue could become problematic and poses a significant risk to the neutrality of the network. An actor with more than 51% of the hashrate could more easily censor transactions if they wished. That is why it is important to distribute the hashrate among multiple actors rather than centralized entities that could be more easily seized by a government, for example.

**If miners are distributed in thousands, or even millions, of households around the world, it becomes very difficult for a state to take control of them.**

When it comes out of the factory, a miner is not suitable for use as a heater in a home, due to two main problems: excessive noise and lack of adjustment. However, these problems can be easily solved through hardware and software modifications, allowing for a much quieter miner that can be configured and automated like modern electric heaters.

**Attakaï is an educational initiative that teaches you how to retrofit the Antminer S9 in the most cost-effective way.**

This is an excellent opportunity to learn by practicing while being rewarded for your participation with KYC-free satoshis.

## Buying Guide for a Used ASIC

<chapterId>3b0b3bf0-859b-57f2-b92f-843ac70b7e68</chapterId>

In this section, we will discuss best practices for purchasing a used Bitmain Antminer S9, the machine on which this radiator retrofitting tutorial will be based. This guide also applies to other models of ASICs as it is a general buying guide for used mining hardware.

The Antminer S9 is a device offered by Bitmain since May 2016. It consumes 1400W of electricity and produces 13.5 TH/s. Although it is considered old, it remains an excellent option for starting mining. Since it has been produced in large quantities, it is easy to find spare parts abundantly in many regions of the world. It can generally be acquired peer-to-peer on sites such as eBay or LeBonCoin, as professional resellers no longer offer it due to its lower competitiveness compared to newer machines. It is less efficient than ASICs like the Antminer S19, offered since March 2020, but this makes it an affordable used hardware and more suitable for the modifications we will make.

The Antminer S9 comes in several variations (i, j) that make minor modifications to the first-generation hardware. We do not believe that this should influence your purchasing decision, and this guide works for all these variations.

The price of ASICs varies depending on many factors such as the price of bitcoin, network difficulty, machine efficiency, and electricity cost. Therefore, it is difficult to give an accurate estimate for the purchase of a used machine. In February 2023, the expected price in France generally ranges from €100 to €200, but these prices are subject to change rapidly.

![image](assets/en/15.webp)

The Antminer S9 is composed of the following parts:

- 3 hashboards that contain the chips that produce the hashing power.

![image](assets/en/16.webp)

- A control board that includes a slot for an SD card, an Ethernet port, and connectors for the hashboards and fans. This is the brain of your ASIC.

![image](assets/en/17.webp)

- 3 data cables that connect the hashboards to the control board.

![image](assets/en/18.webp)

- The power supply, which operates on 220V and can be plugged in like a regular household appliance.

![image](assets/en/19.webp)

- 2 120mm fans.

![image](assets/en/20.webp)

- A male C13 cable.

![image](assets/en/21.webp)

When buying a used machine, it is important to check that all parts are included and functional. During the exchange, you should ask the seller to turn on the machine to check its proper functioning. It is important to verify that the device turns on correctly, and then check the internet connectivity by plugging in an Ethernet cable and accessing the Bitmain login interface via a web browser on the same local network. You can find this IP address by connecting to your internet router interface and looking for connected devices. This address should have the following format: 192.168.x.x

![image](assets/en/22.webp)

Also, check that the default credentials work (username: root, password: root). If the default credentials do not work, you will need to reset the machine.

![image](assets/en/23.webp)

Once connected, you should be able to see the status of each hashboard on the dashboard. If the miner is connected to a pool, you should see all the hashboards functioning. It is important to note that miners make a lot of noise, which is normal. Also, make sure the fans are working properly.

You can then remove the previous owner's mining pool to set up your own later. If you wish, you can also inspect the hashboards by disassembling the machine. However, this step is more complex and requires more time and some tools. If you want to proceed with this disassembly, you can refer to the next part of this tutorial that details how to do it. It is important to note that miners collect a lot of dust and require regular maintenance. You can observe this dust accumulation and the quality of maintenance by disassembling the machine.
After reviewing all these points, you can buy your machine with a high degree of confidence. If in doubt, consult the community.

To summarize this guide in one sentence: **"Don't trust, verify."**

[You can also turn to professionals in the reconditioning of mining machines, such as our partner 21energy. They offer tested S9 machines, cleaned and with BraiiinOS+ software already installed. With the affiliate code "decouvre," you will receive a 10% discount on the purchase of an S9 while supporting the Attakai project.](https://21energy.io/en/produkt/bitmain-antminer-s9-bundle/)

## Guide for Purchasing Hardware Modifications for the S9

<chapterId>fa5f5eca-bcbf-5a83-9b03-98ecbadbabd6</chapterId>

Owner of an Antminer S9, you probably know how loud and bulky this equipment can be. However, it is possible to transform it into a silent and connected heater by following a few simple steps. In this section, we will present the necessary equipment to make the modifications.

If you are a skilled handyman and are looking to transform a miner into a heater, this tutorial is for you. We want to warn you that modifications made to an electronic device can present electrical risks. It is therefore essential to take all necessary precautions to avoid any damage or injury.

1. Replace the fans

The original fans of the Antminer S9 are too noisy to use your Antminer as a heater. The solution is to replace them with quieter fans. Our team has tested several models from the Noctua brand and has selected the Noctua NF-A14 iPPC-2000 PWM as the best compromise. Be sure to choose the 12V version of the fans. This 140mm fan can produce up to 1200W of heating while maintaining a theoretical noise level of 31 dB. To install these 140mm fans, you will need to use a 140mm to 120mm adapter, which you can find on the DécouvreBitcoin store. We will also add 140mm protective grilles.

![image](assets/en/24.webp)
![image](assets/en/25.webp)
![image](assets/en/26.webp)

The power supply fan is also quite noisy and needs to be replaced. We recommend the Noctua NF-A6x25 PWM. Note that the connectors of the Noctua fans are not the same as the original ones, so you will need a connector adapter to connect them. Two will be enough. Again, make sure to choose the 12V version of the fan.

![image](assets/en/27.webp)
![image](assets/en/28.webp)

2. Add a WIFI/Ethernet bridge

Instead of using an Ethernet cable, you can connect your Antminer via WIFI by adding a WIFI/Ethernet bridge. We have selected the vonets vap11g-300 because it easily allows you to retrieve the WIFI signal from your Internet box and transmit it to your Antminer via Ethernet without creating a subnet. If you have electrical skills, you can power it directly with the Antminer's power supply without the need to add a USB charger. For this, you will need a female 5.5mmx2.1mm jack.

![image](assets/en/29.webp)
![image](assets/en/30.webp)

3. Optional: add a smart plug

If you want to turn on/off your Antminer from your smartphone and monitor its power consumption, you can add a smart plug. We tested the ANTELA plug in the 16A version, compatible with the smartlife app. This smart plug allows you to view daily and monthly power consumption and connects directly to your internet router via WiFi.

![image](assets/en/31.webp)

List of equipment and links

- 2X 3D adapter piece 140mm to 120mm

- [2X NF-A14 iPPC-2000 PWM](https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW)

- [2X 140 mm fan grilles](https://www.amazon.fr/dp/B06XD4FTSQ)
- [Noctua NF-A6x25 PWM](https://www.amazon.fr/Noctua-nf-a6-25-PWM-Ventilateur-Marron/dp/B00VXTANZ4)

- [Electrician's sugar 2.5 mm²](https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS)
- [Vonets vap11g-300](https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W)
- [Optional ANTELA smart plug](https://www.amazon.fr/dp/B09YYMVXJZ)

# Attakai - Modifying the Software of an Antminer S9

<partId>afc9c29a-84aa-5f1d-82e2-5fd9ff2e1805</partId>

## Setting up a Vonet WIFI/Ethernet Bridge

<chapterId>3cf487a4-21ef-5b24-83d5-789b811f740f</chapterId>

To connect your ASIC via WIFI, you will need a device called a bridge. This device allows you to retrieve the WIFI signal from your router and transmit it to another device via Ethernet.

Many devices can perform this function, but we recommend the VONETS WiFi Bridge/Repeater for its convenience.

Power the bridge by connecting it via USB.

From your computer, connect to the VONETS\_**\*\*** WIFI network with the password 12345678.

![image](assets/en/32.webp)

Login with the username "admin" and password "admin".

![image](assets/en/33.webp)

Choose Wizard.

![image](assets/en/34.webp)

Select the WIFI network you want to connect your miner to, then click Next.

NOTE: The Vonet bridge only works on the 2.4GHz frequency. Nowadays, routers usually offer two WIFI networks, one on 2.4GHz and one on 5GHz.

![image](assets/en/35.webp)

Enter the password for your WIFI network in the "Source WIFI hotspot password" field. If you do not want to use your Vonet bridge to extend your WIFI network, check the "Disable Hotspot" box. Otherwise, leave it unchecked.

You can then click Apply.

Finally, click on reboot to restart the bridge. It will take a few minutes to reboot.

The bridge should connect to your router and appear under the name "[VONETS.COM](http://vonets.com/)". If it still does not connect after a few minutes, you may need to unplug/replug the bridge.

Once the bridge is connected, connect the Ethernet cable from the bridge to your ASIC, and then plug the ASIC into the power outlet. You can then access the ASIC interface in the same way as if it were directly connected to your router via Ethernet.

## Resetting an Antminer S9

<chapterId>b518b6bd-9dae-5136-ae3c-1fafb1cb2592</chapterId>

Before installing BraiinOS+, it may be necessary to reset your S9 to its factory settings.
This method can be applied between 2 minutes and 10 minutes after starting the miner.
2 minutes after turning on the miner, please press the "Reset" button for 5 seconds, then release it. The miner will be restored to factory settings within 4 minutes and will restart automatically (there is no need to turn it off).

![image](assets/en/36.webp)

## Installing BraiinsOS+ on an Antminer S9

<chapterId>38e8b1a8-8b1d-51ed-8b92-59d4ddb15184</chapterId>

The original software installed by Antminer on their mining machines is limited in functionality. That's why in this guide, we will install another software called BraiinsOS+. It is a third-party software developed by the very first Bitcoin mining pool that has more features and allows, for example, modifying the machine's power.

There are several ways to install Braiins OS+ on an ASIC. You can refer to this guide as well as the [official Braiins documentation](https://academy.braiins.com/en/braiins-os/about/).

Here, we will see how to easily install Braiins OS+ directly on the memory of your Antminer using the BOS toolbox software, replacing the original operating system, through the detailed steps below.

1. Power on your Antminer and connect it to your internet box.
2. Download BOS toolbox for Windows / Linux.
3. Unzip the downloaded file and open the bos-toolbox.bat file. Choose the language, and after a few moments, you will see this window:

![image](assets/en/37.webp)

4. Bos toolbox will allow you to easily find the IP address of your Antminer and install BraiinsOS+. If you already know the IP address of your machine, you can skip to step 8. Otherwise, go to the scan tab.

![image](assets/en/38.webp)

5. Usually, on home networks, the IP address range is between 192.168.1.1 and 192.168.1.255, so enter "192.168.1.0/24" in the IP range field. If your network is different, please change these addresses accordingly. Then click on "Start".

6. Attention, if the Antminer has a password, the detection will not work. If that's the case, the simplest solution is to perform a reset.

7. You should see all the Antminers on your network appear here, and the IP address is 192.168.1.37.

![image](assets/en/39.webp)

8. Click on "Back" and then the "Install" tab, enter the previously found IP address, and click on "Start".

> If the installation does not work, it may be necessary to perform a reset and try again (see the previous section).  

![image](assets/en/40.webp)

9. After a few moments, your Antminer will restart and you will be able to access the Braiins OS+ interface at the specified IP address, here 192.168.1.37, directly in the address bar of your browser. The default username is "root" and there is no default password.

## Configure BraiinsOS+

<chapterId>36e432f2-85bc-52d0-a62a-009fc4c69338</chapterId>

You will need to connect to your ASIC using the local IP address of your device on your network through a browser.

You can find the IP address of your machine using the BOS toolbox tool or directly on your router's web page.

The default credentials are the same as the original operating system.

- username: root
- password: (none)

You will then be greeted by the Brains OS+ Dashboard.

### Dashboard

![image](assets/en/41.webp)

On this first page, you can observe the real-time performance of your machine.

- Three real-time graphs that show the temperature, hashrate, and overall status of your machine.
- On the right, the real hashrate, average chip temperature, estimated efficiency in W/THs, and power consumption.
- Below, the fan speed as a percentage of the maximum speed and the number of rotations per minute.

![image](assets/en/42.webp)

- Further down, you will find a detailed view of each hashboard. The average temperature of the board and the chips it contains, as well as the voltage and frequency.
- Details on the active mining pools in Pools.
- The status of autotuning in Tuner Status.
- On the right, details on the data transmitted to the pool.

### Configuration

![image](assets/en/43.webp)

### System

![image](assets/en/44.webp)

### Quick actions

![image](assets/en/45.webp)

# Attakai - Fan Modification

<partId>98266a8f-3745-58a0-9f6b-26a9734e1427</partId>

## Replace the Power Supply Fan

<chapterId>0c6befa7-f3ef-5bcf-ae8d-0ad5e5d41d70</chapterId>

> WARNING: It is essential to have previously installed Braiins OS+ on your miner, or any other software that can reduce the performance of your machine. This measure is crucial because in order to reduce noise, we will install less powerful fans that can dissipate less heat.  

![image](assets/en/46.webp)

### Required materials

- 1 Noctua NF-A6x25 PWM fan
- 2.5mm2 electrician's sugar

> WARNING: First of all, before starting, make sure you have unplugged your miner to avoid any risk of electrocution.  

![image](assets/en/47.webp)

First, remove the 6 screws on the side of the case that hold it closed. Once the screws are removed, carefully open the case to remove the plastic protection covering the components.

![image](assets/en/48.webp)
![image](assets/en/49.webp)

Next, it's time to remove the original fan, taking care not to damage the other components. To do this, remove the screws that hold it in place and gently peel off the white glue surrounding the connector. It is important to proceed with care to avoid damaging the wires or connectors.

![image](assets/en/50.webp)

Once the original fan is removed, you will notice that the connectors of the new Noctua fan do not match those of the original fan. Indeed, the new fan has 3 wires, including a yellow wire that allows for speed control. However, this wire will not be used in this specific case. To connect the new fan, it is therefore recommended to use a special adapter. However, it is important to note that this adapter can sometimes be difficult to find.

![image](assets/en/51.webp)

If you do not have this adapter, you can still proceed to connect the new fan using an electrician's sugar. To do this, you will need to cut the cables of the old and new fan.

![image](assets/en/52.webp)
![image](assets/en/53.webp)

On the new fan, use a cutter and carefully cut the contours of the main sheath at 1 cm without cutting the sheaths of the cables underneath.

![image](assets/en/54.webp)

Then, by pulling the main sheath downwards, cut the sheaths of the red and black cables in the same way as before. And cut the yellow cable flush.

![image](assets/en/55.webp)

On the old fan, it is more delicate to cut the main sheath without damaging the sheaths of the red and black wires. For this, we used a needle that we slid between the main sheath and the red and black wires.

![image](assets/en/56.webp)
![image](assets/en/57.webp)

Once the red and black wires are exposed, cut the sheaths carefully to avoid damaging the electrical wires.

![image](assets/en/58.webp)

Then, connect the cables with a sugar, the black wire with the black and the red wire with the red. You can also add electrical tape.

![image](assets/en/59.webp)
![image](assets/en/60.webp)

Once the connection is made, it's time to install the new Noctua fan with the grille and the old screws. The new screws in the box will be reused later. Make sure to place it in the correct orientation. You will notice an arrow on one side of the fan, indicating the direction of airflow. It is important to position the fan so that this arrow points towards the inside of the case. Then reconnect the fan.

![image](assets/en/61.webp)
![image](assets/en/62.webp)

> Optional: If you are knowledgeable in electricity, you can directly add a female 5.5mm jack connector to the 12V power output, which will directly power the Vonet Wi-Fi bridge. However, if you are unsure of your electrical skills, it is best to use the USB connector with a smartphone-type charger to avoid any risk of short circuit or electrical damage.  

![image](assets/en/63.webp)

Once the connections are made, place the plastic cover over the case plastic and not inside.

![image](assets/en/64.webp)

Finally, put the case cover back in place and screw the 6 screws on the sides to hold everything in place. And there you have it, your power supply case is now equipped with a new fan.

## Replacing the Main Fans

<chapterId>a29f60f1-3fa3-57fc-a630-9c97cec30e56</chapterId>

> WARNING: It is essential to have previously installed Braiins OS+ on your miner, or any other software capable of reducing the performance of your machine. This measure is crucial because in order to reduce noise, we will install less powerful fans, which will dissipate less heat.  

![image](assets/en/46.webp)

### Required Materials

- 2 pieces 3D adapter 140mm to 120mm
- 2 Noctua NF-A14 iPPC-2000 PWM fans
- 2 140mm fan grilles

> WARNING: First of all, before starting, make sure to disconnect your miner to avoid any risk of electrocution.  

1. First, disconnect the fans and unscrew them.

![image](assets/en/65.webp)

2. The connectors of the new Noctua fans do not match the original ones, but don't worry! Take out your cutter and carefully cut the small plastic tabs so that the connectors fit perfectly on your miner.

![image](assets/en/66.webp)
![image](assets/en/67.webp)

3. It's time to install the 3D parts!
Attach them on both sides of the miner using the screws you removed from the fans. Screw them in until the screw head is flush with the 3D part and it is securely in place. Be careful not to tighten too much, as you could deform the part and one of the screws might touch a capacitor!

![image](assets/en/68.webp)

4. Now let's move on to the fans.

Attach them to the 3D parts using the screws provided in the box. Pay attention to the direction of airflow, the arrows on the sides of the fans will indicate the direction to follow. Go from the Ethernet port side to the other side. See photo below.

![image](assets/en/69.webp)
![image](assets/en/70.webp)
![image](assets/en/71.webp)

5. Last step: connect the fans and attach the grilles on top with the screws that were not used in the power supply fan box. You only have 4 of them, but 2 per grille in opposite corners will be enough. You can also look for similar screws in a hardware store if needed.

![image](assets/en/72.webp)
![image](assets/en/73.webp)

While waiting to be able to offer a more stylish casing for your new heater, you can attach the case and the power supply with electrician's cable ties.

![image](assets/en/74.webp)

And for the finishing touch, connect the Vonet bridge to the Ethernet port and its power supply.

![image](assets/en/75.webp)

And there you have it, congratulations! You have just replaced the entire mechanical part of your miner. You should now hear much less noise.

# Attakai - Configuration

<partId>9c3918a8-d9a3-5a1f-bb9a-70314f7ac175</partId>

## Joining a Mining Pool

<chapterId>b57a6105-0a53-5fe9-bad1-d6d9daf97c0d</chapterId>

One can imagine a mining pool as a farming cooperative. Farmers pool their production together to reduce the variance of supply and demand and thus obtain more stable income for their operation. A mining pool operates in the same way, with the shared resource being hashes. Indeed, the discovery of a single valid hash allows for the creation of a block and the winning of the coinbase or reward, currently 6.25 BTC plus the transaction fees included in the block.

If you mine alone, you will only be rewarded when you find a block. Being in competition against all other miners on the planet, you would have very little chance of winning this lottery and you would still have to pay the fees associated with using your miner without any guarantee of success. Mining pools address this issue by pooling the computing power of several (thousands) of miners and sharing their rewards based on the percentage of participation in the pool's hashrate when a block is found. To visualize your chances of mining a block alone, you can use this tool. By entering the information for an Antminer S9, we can see that the chances of finding a hash that allows for the creation of a block are 1 in 24,777,849 for each block or 1 in 172,068 per day. On average (with a constant hashrate and difficulty), it would take at least 471 years to find a block (as difficulty increases).

However, since everything in Bitcoin is based on probability, it sometimes happens that solo miners are rewarded for taking this risk: Solo Bitcoin Miner Solves Block With Hash Rate of Just 10 TH/s, Beating Extremely Unlikely Odds – Decrypt

If you like to gamble, you can try it, but our guide will not focus in that direction. Instead, we will concentrate on the mining pool that best suits our needs for creating a heating system.

Considerations to have when choosing a mining pool are the operation of the pool's rewards, which can vary, as well as the minimum amount before being able to withdraw rewards to an address. For example, Braiins, which offers the software we are discussing here, also offers a pool. This pool has a reward system called "Score" that encourages miners to mine for long periods. Participation includes a uptime factor expressed as a "scoring hashrate". In our case, where we want a heating system that can be turned on for only a few minutes, this is not the ideal reward system. We prefer a reward system that gives us an equal reward for each participation. Additionally, the minimum withdrawal amount for Braiins Pool is 100,000 sats and On-Chain. So we lose some sats in transaction fees and a portion of our reward can be locked if we don't mine enough during the winter.

The reward model that interests us is PPS, which stands for "pay-per-share". This means that the miner will receive a reward for each valid share. There is also a variant of this system, FPPS (Full Pay Per Share), which not only divides the coinbase reward, but also the transaction fees included in the block. The mining pools we recommend for connecting your mining/heating are Linecoin Pool (FPPS) and Nicehash (PPS).

- Nicehash: The advantage of Nicehash is that withdrawal can be done using Lightning with minimal fees. Additionally, the minimum withdrawal amount is 2000 sats. The disadvantage is that Nicehash uses its hashrate for the most profitable blockchain, without really giving control to the user, so it may not necessarily contribute to the Bitcoin hashrate.

- Linecoin: The advantage of Linecoin is the number of features offered, such as a detailed dashboard, the ability to make withdrawals with a Paynym (BIP 47) for better privacy protection, and the integration of a Telegram bot as well as directly configurable automations in the mobile application. This pool only mines Bitcoin blocks, but the minimum amount to withdraw remains high at 100,000 sats. We will examine the interface of one of these pools in more detail in a future article.

To configure a pool in Braiins OS+, you will need to create an account in one of the pools of your choice. Here we will take the example of Linecoin:

![image](assets/en/76.webp)

Once your account is created, click on Connect To Pool

Then copy the Stratum address and your username:

![image](assets/en/77.webp)

You can now go back to the Braiins OS+ interface to enter these credentials. For the password, you can leave the field empty.

![image](assets/en/78.webp)

## Optimizing the Performance of Your Antminer S9

<chapterId>25380972-31c7-540d-80d8-17a06b171ca0</chapterId>

Both overclocking and autotuning involve adjusting the frequencies on the hashing boards to improve the performance of the ASIC. The difference between the two lies in the complexity of these frequency settings.

Overclocking is a simple adjustment that involves increasing the frequency on the hashing boards to increase the machine's hash rate. Underclocking, on the other hand, involves reducing the clock frequency of an integrated circuit below its nominal frequency. By reducing the clock frequency of an ASIC through underclocking, the heat generated by the hardware is also reduced. This allows for a decrease in the speed of the fans required to cool the ASIC, as they do not have to work as hard to maintain an appropriate temperature. By reducing the fan speed, the noise generated by the ASIC is also reduced. This can be particularly useful for users who use ASICs at home and are looking to minimize the noise disturbances caused by mining equipment.

Braiins OS+ supports overclocking, underclocking of ASICs, and autotuning. It allows users to adjust the clock frequency of their hardware flexibly to maximize performance or save energy according to their preferences.

### Optimizing the performance of your Antminer S9 with auto-tuning

Before 2018, miners had two ways to gain an advantage in their activity: finding electricity at a reasonable cost and buying more efficient hardware. However, in 2018, a new advancement was discovered in the field of mining software and firmware, called AsicBoost. This technique allows miners to reduce their costs by approximately 13% by modifying the firmware running on their devices.

Today, there is a new advancement in the software and firmware mining sector called autotuning, which offers an even greater advantage than AsicBoost. ASICs are composed of many small computer chips that perform hashing. These chips are made of silicon, the same element widely used in semiconductors and other microelectronic components. The key understanding here is that not all silicon chips are identical, each can vary slightly in its electrical properties. Hardware manufacturers are aware of this and publish the performance specifications of their mining machines based on the lower limit of their tolerances. In other words, manufacturers know the frequency that works best for average chips and they use this frequency uniformly for all chips in the machine.

This puts an upper limit on the hash rate a machine can have. Autotuning is a process in which algorithms evaluate the optimal frequencies for chip-by-chip hashing, instead of treating the entire machine as a single unit. This means that a higher-quality chip that can perform more hashes per second will get a higher frequency, and a lower-quality chip that can perform relatively fewer hashes will get a lower frequency. Chip-level autotuning is essentially a way to optimize the performance of an ASIC through the software and firmware running on it.

The end result is a higher hash rate per watt of electricity, which means larger profit margins for miners. The reason why machines are not distributed with this type of software is that machine variance is undesirable, as customers want to know exactly what they are getting, so it is a bad idea for manufacturers to sell a product that does not have consistent and predictable performance from one machine to another. Additionally, chip-level autotuning requires considerable development resources, as it is complex to implement. Manufacturers already spend a lot of resources developing their own firmwares. There are software solutions that allow for autotuning, such as Braiins OS+. In addition to improving ASIC performance by up to 20%.

# Conclusion

<partId>fa42ec0b-b1fd-47f6-8268-6eab684c1d2b</partId>

## Evaluate this course

<chapterId>6af13742-df68-5cf4-b7aa-93dc0c2eaae9</chapterId>
<isCourseReview>true</isCourseReview>

## Final exam

<chapterId>f51a7c88-3b7e-48df-b45f-22bb10fe619f</chapterId>
<isCourseExam>true</isCourseExam>

## Conclusion

<chapterId>2941f29a-d6ce-4a3c-b61b-6e399f5395b1</chapterId>
Congratulations on completing this course!

We are delighted that you have reached this important milestone in your learning journey.

Through your dedication and commitment, you have gained valuable knowledge and skills that will serve you in your professional development.

To continue exploring the Bitcoin universe in depth, we invite you to discover all other courses available on Plan ₿ Network:

#### Discover Bitcoin and its fundamentals with

https://planb.network/courses/btc101

#### Discover the Lightning Network with

https://planb.network/courses/lnp201

#### Master the principles of privacy on Bitcoin

https://planb.network/courses/btc204

#### Discover the history of Bitcoin's origins with

https://planb.network/courses/his201

#### Understand how the Bitcoin wallet works with

https://planb.network/courses/cyp201
