---
term: BIP
---

Acronym for "Bitcoin Improvement Proposal." A Bitcoin Improvement Proposal (BIP) is a formalized process for proposing and documenting improvements and changes to the Bitcoin protocol and its standards. Since Bitcoin has no central authority to decide on updates, BIPs allow the community to suggest, discuss, and implement improvements in a structured and transparent way. 

Each BIP details the objectives of the proposed improvement, the justifications, potential impacts on compatibility, as well as the advantages and disadvantages. BIPs can be written by any member of the community, but must be approved by other developers and the editors who maintain the Bitcoin Core GitHub database: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun, and Ruben Somsen. Their editorial role does not imply control over Bitcoin itself. Even if a proposal is not accepted through the formal BIP process, it can still be presented directly to the Bitcoin community or implemented in a separate fork.
The BIP process provides formality and a centralized reference point to facilitate debate and reduce fragmentation among Bitcoin users, aiming to implement updates by consensus. Ultimately, economic majority determines influence and decision‑making within the protocol.

BIPs are classified into three main categories:
* *Standards Track BIPs*: Concern modifications that directly affect Bitcoin implementations, such as transaction and block validation rules;
* *Informational BIPs*: Provide information or recommendations without proposing direct changes to the protocol;
* *Process BIPs*: Describe changes in the procedures surrounding Bitcoin, such as governance processes.

Standards Track and Informational BIPs are also classified by "Layer":
* *Consensus Layer*: Proposals that modify Bitcoin's consensus rules (e.g., block or transaction validation rules). These can be implemented as either soft forks (backward-compatible changes) or hard forks (non-backward-compatible changes). SegWit and Taproot BIPs fall into this category.
* *Peer Services*: Proposals relating to how nodes discover and communicate with each other over the network.
* *API/RPC*: Changes to Application Programming Interfaces (APIs) and Remote Procedure Calls (RPCs) used for software-to-node interaction.
* *Applications Layer*: Standards for applications built on top of Bitcoin, such as wallet formats.

Submitting a BIP begins with conceptualizing and discussing the idea on the Bitcoin-dev mailing list. If promising, the author drafts the BIP following a standardized format and submits it as a Pull Request to the GitHub repository. The editors review this proposal to verify that it meets all the criteria. The BIP must be technically feasible, beneficial to the protocol, comply with the required formatting, and be in accordance with Bitcoin's philosophy. If the BIP meets these conditions, it is officially integrated into the GitHub repository of BIPs. It is then assigned a number. This number is generally decided by the editor, often Luke Dashjr, and is assigned logically: BIPs dealing with similar subjects often receive consecutive numbers.

BIPs then go through different statuses over their lifecycle. The current status is specified in the header of each BIP:
* Draft: The proposal is still in the drafting and debate phase;
* Proposed: The BIP is considered complete and ready for review by the community;
* Deferred: The BIP is put on hold for later by the author or an editor;
* Rejected: A BIP is classified as rejected if it has shown no activity for 3 years. Its author may choose to resume it later, which would allow it to return to the draft status;
* Withdrawn: The BIP has been withdrawn by its author;
* Final: The BIP is accepted and widely implemented on Bitcoin;
* Active: For process BIPs only, this status is assigned once a certain consensus is reached;
* Replaced / Obsolete: The BIP is no longer applicable or has been replaced by a more recent proposal that renders it unnecessary.

![](../../dictionnaire/assets/25.webp)

> ► *BIP is the acronym for "Bitcoin Improvement Proposal". In French, it can be translated as "Proposition d'amélioration de Bitcoin". However, most French texts directly use the acronym "BIP" as a common noun, sometimes feminine, sometimes masculine.*