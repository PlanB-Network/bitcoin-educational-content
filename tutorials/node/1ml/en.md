---
name: 1ML
description: Learn how to use the 1ML explorer to understand and analyze Bitcoin's Lightning network.
---
![cover](assets/cover.webp)


## Introduction


Lightning Network is a fast, low-cost payment solution built on top of Bitcoin, enabling instant, secure transactions. Observing this network is essential to understanding how it works, its topology and the state of the nodes that make it up. A Lightning explorer, like 1ML, is used to visualize the network's public data, including active nodes, open channels and available capacity, providing a valuable overview for users, developers and node operators.


## Access 1ML and understand the home page


To access 1ML, simply open your web browser and type in [https://1ml.com](https://1ml.com). This takes you to the home page, which serves as the Lightning Network's global dashboard.


![capture](assets/fr/03.webp)


This page displays several important statistics at the top of the screen, including :



- The **total number of active nodes** on the network, i.e. the computers involved in sending and receiving Lightning payments.
- The **number of open channels**, which correspond to the connections between these nodes enabling funds transfers.
- The **total network capacity**, expressed in bitcoin (BTC), which indicates the sum of the capacities of all public channels.


These figures are updated regularly to reflect the current state of the network. They give an idea of its size, growth and robustness.


![capture](assets/fr/04.webp)


Just below, the page offers lists with rankings:



- The **most connected nodes**, which have the most open channels to other nodes.
- The **highest capacities** on the nodes, indicating which nodes can transfer the largest amounts.
- The most important channels in terms of capacity.


Filters can also be used to refine these lists by geographic location or other criteria.


This page is an ideal starting point for exploring Lightning Network and understanding its general topology.


![capture](assets/fr/05.webp)


![capture](assets/fr/06.webp)


## Exploring Lightning nodes


To explore a node on 1ML, start by using the search bar at the top of the page. You can enter the **Node ID**, i.e. the node's unique identifier, or its **alias**, which is an easier-to-remember name.


Once the search has been completed, click on the corresponding node to access its detailed page.


![capture](assets/fr/07.webp)


On this page, several important pieces of information are displayed:



- Node ID**: this unique identifier is a long string of characters that allows the node to be precisely identified throughout the network.


![capture](assets/fr/08.webp)



- Alias**: this is the name chosen by the node owner to represent it publicly.


![capture](assets/fr/09.webp)



- The **number of channels** indicates how many connections the node has open with other nodes, while the **total capacity** represents the sum of bitcoins available in these channels. A node with a large number of channels and high capacity is generally well connected and capable of transferring large amounts of money quickly across the network.


![capture](assets/fr/10.webp)



- The **uptime**, or availability, measures how long a node has remained active and accessible online, reflecting its reliability. The **age** of the node, on the other hand, indicates how long it has been present on the network, reflecting its stability and experience within Lightning Network.


![capture](assets/fr/11.webp)


This data helps you understand the importance and reliability of a node in Lightning Network. For example, a node with a large number of channels, high capacity and high uptime is often a major player in the network.


## Exploring lightning channels


### What is a Lightning channel?


A Lightning channel is a direct connection between two network nodes. It enables these two nodes to exchange instant, low-cost payments without going through the Bitcoin main chain for each transaction. Channels are the foundation that makes Lightning Network fast and scalable.


### Read channel information on 1ML


On 1ML, each channel has its own page or description sheet containing a number of important data:


From a node's page, you can access a list of its channels. By clicking on a channel, 1ML displays a dedicated page with several key pieces of information.


![capture](assets/fr/12.webp)


![capture](assets/fr/13.webp)


The main visible data are as follows:



- Partner nodes**: each channel links two nodes. 1ML displays both identifiers and their respective aliases.


![capture](assets/fr/14.webp)



- Channel capacity**: this is the total amount of bitcoins locked in this channel. This capacity represents the maximum limit of payments that can transit through this channel.


![capture](assets/fr/15.webp)



- Channel age**: indicates how long the channel has been open. An old channel is often a sign of a stable relationship between two nodes.


![capture](assets/fr/16.webp)


### Channel visibility limits


It's important to understand that 1ML only shows **part** of Lightning Network. The explorer only shows **public channels**, i.e. those that have been announced on the network. Private channels, often used for reasons of confidentiality or strategy, are not visible. Furthermore, 1ML does not show the exact distribution of funds on each side of a channel, nor the payments made, nor the liquidity actually available at a given moment. The information displayed can therefore be used to analyze the **general structure of the network**, but not its actual financial activity or detailed liquidity status.


## Explore Lightning Network by location


### Nodes by country and region


1ML allows you to explore Lightning Network according to a **geographical breakdown**. From the home page or via dedicated sections, it is possible to display nodes by country or region. This feature is based on location information declared by node operators.

In the navigation bar, you'll see the **Location** link. On the page, nodes are grouped by continent, country and city.


![capture](assets/fr/17.webp)


By selecting a country, 1ML displays a list of associated nodes, along with aggregated statistics such as the number of nodes and total visible capacity for that geographical area.


#### What this says about local adoption



- Technology adoption**: A large number of nodes in a region indicates that Bitcoin users, companies or services are actively adopting Lightning Network. This shows technological maturity and a willingness to take advantage of Lightning's benefits (fast transactions, lower costs).
- Economic ecosystem** : The dense presence of nodes can also signal a local economic fabric around Bitcoin: merchants accepting Lightning, startups developing tools, community events, etc.
- Security and resilience**: Diverse geographical distribution enhances network resilience in the face of local outages or restrictions. The more dispersed the nodes, the more decentralized and difficult to censor the network.
- Policies and regulations**: Some countries may see faster adoption thanks to a favorable regulatory framework or a proactive community. Conversely, in areas where regulations are strict or hostile, the number of nodes will be lower.


#### Limits of geographic data


Bear in mind, however, that the geolocation of Lightning nodes has its limits and biases:



- Approximate IP location**: 1ML generally uses the public IP address of nodes to estimate their location. However, this method can be distorted by the use of VPNs, cloud servers (AWS, Google Cloud), or hosting in countries different from the node owner's actual domicile.
- Virtual nodes**: Some operators host their nodes on remote servers for reasons of reliability and availability, which can give a false sense of physical location.
- User mobility**: A node operator may change location, move his infrastructure, or open several nodes in different regions, making data reading more complex.
- Invisibility of private nodes**: Some nodes don't publish their IP address or use methods to hide their location, making geolocation impossible.


## 1ML concrete use cases


### Understanding network topology


1ML allows you to visualize the **general structure of Lightning Network**. By observing the connections between nodes, the number of channels and overall capacity, it's possible to understand how the network is organized, which nodes play a central role and how payment flows can theoretically circulate.


This understanding is essential if we are to understand how the Lightning Network works, and not just for wallet use.


### Identify important nodes


Thanks to the rankings offered by 1ML (most connected nodes, highest capacity, age), it is possible to identify the nodes that occupy an important place in the network. These nodes often serve as major gateways for Lightning payments.


![capture](assets/fr/18.webp)


### Check the public visibility of a node


For a node operator, 1ML allows you to check whether your node is **publicly advertised** on Lightning Network. If a node appears on 1ML, this means it is visible and accessible to other nodes for opening public channels.

This can be useful for diagnosing visibility or connectivity problems.


### Watching Lightning Network evolve over time


By comparing global statistics over different periods, 1ML enables us to observe the evolution of Lightning Network: increase or decrease in the number of nodes, variations in total capacity or changes in geographical distribution.

These observations offer an interesting perspective on the growth, maturity and trends of Lightning Network.


## 1ML best practices and limitations


### Public data ≠ complete reality


1ML is based solely on the **publicly announced** data on Lightning Network. This means that the tool only shows part of the reality. Many channels may be private, some nodes may not be advertised, and the actual liquidity available in channels is not visible. It is therefore essential to use 1ML as a global analysis tool, not as an exhaustive representation of the network.


### Privacy and Lightning


Lightning Network has been designed with a strong focus on **payment privacy**. Individual transactions are not visible on 1ML, and exact channel balances are not public. This limitation is not a fault of the explorer, but a fundamental feature of Lightning Network, designed to protect users' privacy.


### Don't jump to conclusions


A node with high capacity or many channels is not necessarily more "reliable" or "efficient" in all cases. Similarly, a temporary drop in overall network capacity does not necessarily mean a structural problem. Figures should always be interpreted with hindsight and put into context.


### Complementarity with other tools


1ML is an excellent starting point for exploring Lightning Network, but it's best used in conjunction with other tools such as Lightning wallets, node management interfaces and other explorers. This approach provides a more complete and nuanced view of the network.


## 1ML connection option (advanced functionality)


1ML offers a **log-in / create account** option, visible on the site, but this is **not necessary** to view Lightning Network data. All the features discussed so far in this tutorial are available **without an account**.


The connection is aimed primarily at **Lightning node operators**. In particular, it enables a node to be associated with a 1ML account in order to manage certain public information, such as the node's presentation, contact links and other metadata. This feature is designed to improve the visibility and identification of a node within the explorer.


It is important to note that 1ML is **not a custodial service**. The creation of an account does not give access to funds, channels or payments of a node. It only serves to interact with the explorer from a declarative and informative point of view.


In the context of learning or discovering the Lightning Network, this option can therefore be considered **optional** and reserved for more advanced use.


## Conclusion


1ML is a valuable tool for observing and understanding Lightning Network from its public data. It lets you explore the structure of the network, analyze nodes and channels, and track the overall evolution of Lightning Network adoption over time. Without the need for an account or the handling of funds, 1ML offers an accessible gateway for anyone wishing to deepen their understanding of how Lightning works.

If you want to go further with the Lightning Network, I recommend the complete Introduction to Lightning Network course:


https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb