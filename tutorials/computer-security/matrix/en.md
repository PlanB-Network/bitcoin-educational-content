---
name: Matrix
description: A guide to understanding, configuring and using Matrix, the secure, open and decentralized communications platform.
---

![cover](assets/cover.webp)


## What is Matrix?


Matrix is a **decentralized communication protocol** designed to enable the exchange of messages, files and audio/video calls between users and applications, without dependence on a central enterprise. Unlike traditional messaging platforms, Matrix is an **open infrastructure**, comparable to email: anyone can choose a server or operate one themselves, while retaining the ability to exchange with the rest of the network.


Matrix is distinguished by three fundamental principles:


### A protocol, not an application


Matrix is not an application like WhatsApp or Telegram.

It's a standardized language that many applications can use.

In other words, a wide variety of Element software, FluffyChat, Cinny, Nheko and others, provide access to the same Matrix network.


This guarantees total freedom: change of application without loss of contacts, diversity of interfaces, independence from a single supplier.


![capture](assets/fr/03.webp)


### A decentralized, federated network


Matrix's structure is based on **federation**, a model in which several independent servers cooperate with each other.

Each server (called _homeserver_) can host users, chat rooms and synchronize messages with other servers on the network.

Thus :



- no single entity controls the entire system;
- a server can disappear without affecting the rest of the network;
- each organization or individual can manage its own space.


This model ensures **high resilience** and reflects the values of technological sovereignty.


![capture](assets/fr/03.webp)


### A secure, encrypted system


Matrix supports **end-to-end encryption (E2EE)** for private exchanges and encrypted groups.

Messages can only be read by participants, not by intermediate servers.

This approach makes it possible to communicate without exposing the content of exchanges to a third party, while retaining the transparency of the protocol and the possibility of hosting one's own server.


![capture](assets/fr/05.webp)


### Unique interoperability


One of Matrix's major assets is its ability to act as a **bridge between different communication systems**. Thanks to _bridges_, it is possible to connect :



- Telegram
- WhatsApp
- Signal
- Messenger
- Slack
- Discord
- IRC, XMPP, etc.


This makes it possible to unify communities scattered across several platforms, while retaining control over the infrastructure.


![capture](assets/fr/06.webp)


## How does Matrix work?


This section presents the internal structure of the Matrix network to understand how users, servers and applications interact within this decentralized ecosystem. Matrix is based on three essential elements: _homeservers_, identities, and _clients_ used to communicate.


### Servers: homeservers


Matrix runs on independent servers called _homeservers_.

Each homeserver manages :



- the user accounts it hosts,
- private conversations and lounges in which these users participate,
- synchronization with other network servers.


All homeservers connected to the Matrix network automatically exchange messages and events from shared living rooms. For example:



- a user registered on server A can chat with a user on server B,
- a salon can be spread over dozens of servers,
- no one has control over a salon or a community as a whole.


This model is highly resilient and allows each organization or individual to manage their own infrastructure.


### Matrix identifiers


Each user has a unique identifier, called **MXID** (_Matrix ID_), which looks like an address:


```bash
@nomdutilisateur:serveur.xyz
```


It consists of :



- a user name, preceded by **@**
- the name of the server on which the account was created, preceded by **:**


Examples:



- `@alice:matrix.org`
- `@bened:monserveur.bj`


This identifier enables communication with any other Matrix user, regardless of the originating server.


### Matrix clients (applications)


To use Matrix, you need to connect with an application called **client Matrix**.


The best-known are :



- Element (web, mobile, desktop)
- FluffyChat (mobile)
- Cinny (minimalist web/desktop)
- Nheko (desktop)


These applications are merely interfaces for :



- to view messages,
- send text, images or files,
- join or create trade shows,
- make audio/video calls.


All applications communicate with servers via the same standardized protocol.


### Rooms and private messages (DM)


In Matrix, exchanges take place in **rooms** :



- a room can be public or private
- it can hold two people or thousands
- it can be shared between several servers
- it has a unique identifier starting with **!**


Private messages are simply chat rooms with two participants, often referred to as **DM (Direct Messages)**.


Salon synchronization takes place in real time between participating servers, ensuring a seamless experience while maintaining decentralization.


## Why use Matrix?


Matrix is not just an alternative to centralized messaging systems: it's a technology that meets real needs in terms of digital sovereignty, security and interoperability. There are many reasons why more and more people, companies and institutions are choosing this protocol to communicate.


### Regain control of your communications


Most messaging platforms operate on a centralized model: a single player controls servers, access, data and usage rules. This model implies total dependence on the supplier.

Matrix takes a different approach.

Anyone can choose where to host their account, or even deploy their own server. No entity is in a position to block a user, demand intrusive identification or impose a policy change.

This architecture gives autonomy back to both individuals and organizations. Communications are no longer based on trust in a company, but on an open, documented and verifiable protocol.


### Secure, encrypted communication


Matrix supports end-to-end encryption for private conversations and groups. This mechanism ensures that only participants can read messages, even if they pass through third-party servers in the federation.


The protocol uses the Megolm/Olm algorithm, designed specifically to provide strong security in distributed, multi-device environments.


This makes it possible to :



- protect sensitive conversations,
- prevent unauthorized access (even from the host server),
- maintain confidentiality over the long term.


Encryption is not an option: it's a core component of the protocol.


### No longer dependent on a single application


Matrix is not an application, but a protocol.


This diversity of customers guarantees :



- a choice adapted to individual needs,
- the ability to use Matrix on any type of device,
- no dependence on a single software.


If a customer is unsuitable or ceases to be maintained, simply select another: the account continues to operate normally.


### Federating and interconnecting different communities


Federation allows different servers to work together while being managed independently.

Thus :



- an organization can manage its own homeserver,
- individuals can join public servers,
- all can communicate with each other as if they were on the same platform.


This flexibility makes it possible to create communication spaces adapted to every need: teams, associations, communities, institutions or open source projects.


Matrix is particularly popular in technical circles, activist collectives, researchers, governments, and increasingly in Bitcoin communities.


### Unique interoperability in the messaging landscape


One of Matrix's major assets is its ability to **extend** exchanges thanks to bridges capable of linking :



- WhatsApp
- Telegram
- Signal
- Slack
- Discord
- IRC
- XMPP
- and many other platforms


Matrix thus becomes a unifying layer for communications, bringing together several communities scattered over different applications.


This interoperability reduces fragmentation and simplifies collaboration.


### A free, open and sustainable protocol


The Matrix protocol is entirely open source and transparently developed.

This guarantees several advantages:



- a continuous evolution of the standard,
- the ability for anyone to check the code,
- independence from commercial or political change,
- long-term resilience.


Unlike proprietary messaging systems, the future of Matrix does not depend on a single company, but on a global community and an open standard.


## How do I create a Matrix account?


Creating a Matrix account is simple and requires no technical skills. Users can join an existing server, create a login and start chatting immediately. This section outlines the essential steps.


### Choose a server (public or private)


Matrix is a federated network: there are numerous servers (homeservers) managed by different organizations, communities or individuals. The choice of server only determines _where_ the account is hosted, but does not prevent communication with the whole network.

**Two options are available:**


### - Use a public server


This is the simplest solution.

Examples of popular servers:



- _matrix.org_ (the best-known)
- _envs.net_
- thematic community servers (tech, privacy, open-source...)


These servers are suitable for novice users who want to register quickly.


### - Use a private server


Ideal for :



- an organization,
- a family,
- an open source project,
- a work team,
- or for sovereign, self-hosted use.


In this case, someone has to administer the server (Synapse, Dendrite, Conduit...).

No matter which server you choose, users can talk to each other thanks to federation.


### Create an account step by step


As Matrix is an open protocol, it can be accessed by several applications.

As described above, they offer different interfaces and functionalities depending on requirements:



- Element**: the most complete client, available on all platforms.
- FluffyChat**: simple, modern and ideal for mobiles.
- Nheko**: lightweight, ergonomic client for PCs.
- SchildiChat**: Element variant with ergonomic improvements.
- NeoChat**: integrated into the KDE ecosystem.


The choice of client has no impact on the account: all work with any Matrix server.


### Classic steps :



- Open the chosen application. In our case, we'll do this with [Element](app.element.io).
- Select "Create an account".


![cover-kali](assets/fr/10.webp)


For simplicity's sake, you can create a Matrix account using **Google, Facebook, Apple, GitHub or GitLab**. These services will only know that their account has been used to access Matrix: this is known as a **social connection**.


For greater confidentiality, you can also register manually by choosing a **username**, a **password** and an **e-mail address**.


Depending on the server chosen, a **captcha** may be required, as well as acceptance of the **terms of use**.


Once the registration has been validated, a confirmation e-mail is sent.

Simply click on the link to activate your account and access the web application (Element) to join your first Matrix conversations.


![cover-kali](assets/fr/11.webp)


You now have an account and use the Web version of Element.


## Add your first contact


To communicate with someone on Matrix, all you need to know is their full identifier, called **Matrix ID**.


Example:


`@alice:matrix.org @bened:monserveur.bj`


### Add a contact


To invite friends to your group chat, click on the `i` circle in the top right corner. This opens the right-hand panel. Click on "People" to display the list of members in this room: you should be the only ones present at the moment.


![cover-kali](assets/fr/12.webp)


Click on "Invite to this room" at the top of the people list and a prompt will open so you can invite your friends to join you in Matrix. If they're already logged in to Matrix, enter their Matrix ID. If they're not, enter their e-mail address and they'll be invited to join us.


There is no "friend" system: a contact is simply a person with whom a conversation has been opened.


![cover-kali](assets/fr/13.webp)


The person you've invited can either accept or decline the invitation. If they accept, you should see them join the room. The more the merrier!


![cover-kali](assets/fr/14.webp)


### Setting up your own server


Matrix really comes into its own when used in conjunction with a personal server.

Deploying your own homeserver allows you to :



- maintain complete control over data,
- define its own rules of use,
- host multiple accounts (friends, team, community),
- and ensure maximum resilience in the event of restrictions or censorship.


**Available solutions:**



- Synapse**: the historic and most complete implementation.
- Dendrite**: lighter, more powerful and designed for the future of the protocol.
- Conduit**: a minimalist variant that's easy to deploy.


**Prerequisites:**



- a domain name,
- a machine or a VPS,
- minimum system administration skills.


Even if it requires a bit of configuration, managing your own server turns Matrix into a sovereign and durable tool.


### Joining your first trade shows


Matrix relies heavily on _rooms_ (living rooms).

There are public, private, community, technical, local and international trade shows.


**Three ways to join a salon:**


1. **Via an invitation link** (often in the form of a `matrix.to` URL).

2. **Searching for the salon name** in the application.

3. **By entering the full show ID**, e.g. :

`#bitcoin:matrix.org`

`#communauté-bénin:monsrv.bj`


Once joined, the chatroom behaves like a classic newsgroup, with history, encryption, files, reactions and audio/video calls, depending on the client used.


![capture](assets/fr/09.webp)


## Going further


Once you've mastered the basics, Matrix offers a host of advanced possibilities. Whether you want to connect other messaging systems, host your own server or organize a community, the ecosystem is very rich.


### Bridges (WhatsApp, Telegram, Signal, etc.)


A bridge connects Matrix to other messaging systems.

With it, you can send and receive messages from :



- WhatsApp
- Telegram**
- Signal**
- Facebook Messenger
- Discord
- Slack**
- IRC** (IRC)
- and many others


### What bridges can do



- Centralize all your conversations in Matrix
- Provide an open interface for interaction with proprietary services
- Manage a multi-platform community from a single location


Some bridges are official, others community-based.

Depending on the department, they may require :



- a personal server,
- an additional configuration,
- or the use of an existing public bridge.


### Using Matrix for a Bitcoin organization, community or project


Matrix is not just a personal tool.

It can be used to structure workgroups, organize local communities or manage project communication.


**Examples of use:**



- Open-source communities
- Bitcoin and Lightning ecosystem projects
- Student or developer groups
- Citizen organizations
- Independent media
- Local groups and associations


**Why is this interesting?



- 100% open-source** tool
- Sovereign and decentralized** communication
- Spaces organized into **lounges**, **subgroups**, **private lounges**, etc.
- Integrate with Nextcloud, GitLab, Mattermost, or custom bots
- Fine-tuned management of permissions and moderation


Matrix then becomes a communication pillar for any structure wishing to remain independent of the large centralized platforms.


## Conclusion


Matrix represents a modern, open and secure solution for real-time communication, offering a decentralized alternative to traditional platforms. Thanks to its federated architecture and advanced encryption protocols, it enables users to retain control of their data while enjoying a fluid, interoperable experience. Whether for personal, professional or community use, Matrix offers a robust and scalable framework for building communication environments adapted to today's needs.


To find out more and discover all the features offered by Matrix, you can consult the official documentation available here :

[https://matrix.org/docs/](https://matrix.org/docs/)