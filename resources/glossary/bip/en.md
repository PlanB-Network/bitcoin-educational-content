---
term: BIP
---

Acronym for "Bitcoin Improvement Proposal." A Bitcoin Improvement Proposal (BIP) is a formal process for proposing and documenting improvements and changes to the Bitcoin protocol and its standards. Since Bitcoin does not have a central entity to decide on updates, BIPs allow the community to suggest, discuss, and implement improvements in a structured and transparent manner. Each BIP details the objectives of the proposed improvement, the justifications, potential impacts on compatibility, as well as the advantages and disadvantages. BIPs can be written by any member of the community, but must be approved by other developers and the editors who maintain the Bitcoin Core GitHub database: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun, and Ruben Somsen. However, it is important to understand that the role of these individuals in editing BIPs does not mean they control Bitcoin. If someone proposes an improvement that is not accepted within the formal BIP framework, they can still present it directly to the Bitcoin community or even create a fork including their modification. The advantage of the BIP process lies in its formality and centralization, which facilitate debate to avoid division among Bitcoin users, seeking to implement updates in a consensual manner. In the end, it is the principle of economic majority that determines the power dynamics within the protocol.

BIPs are classified into three main categories:
* *Standards Track BIPs*: Concern modifications that directly affect Bitcoin implementations, such as transaction and block validation rules;
* *Informational BIPs*: Provide information or recommendations without proposing direct changes to the protocol;
* *Process BIPs*: Describe changes in the procedures surrounding Bitcoin, such as governance processes.

Standards Track and Informational BIPs are also classified by "Layer":
* *Consensus Layer*: BIPs in this layer concern the consensus rules of Bitcoin, such as modifications to the block or transaction validation rules. These proposals can be either soft forks (backward-compatible modifications) or hard forks (non-backward-compatible modifications). For example, the BIPs for SegWit and Taproot belong to this category;
* *Peer Services*: This layer concerns the operation of the Bitcoin node network, that is, how nodes find and communicate with each other on the Internet.
* *API/RPC*: The BIPs of this layer concern the Application Programming Interfaces (API) and Remote Procedure Calls (RPC) that allow Bitcoin software to interact with nodes;
* *Applications Layer*: This layer pertains to applications built on top of Bitcoin. The BIPs in this category typically deal with modifications at the level of Bitcoin wallet standards.

The process of submitting a BIP begins with the conceptualization and discussion of the idea on the *Bitcoin-dev* mailing list. If the idea is promising, the author drafts a BIP following a specific format and submits it via a Pull Request on the Core GitHub repository. The editors review this proposal to verify that it meets all the criteria. The BIP must be technically feasible, beneficial to the protocol, comply with the required formatting, and be in accordance with Bitcoin's philosophy. If the BIP meets these conditions, it is officially integrated into the GitHub repository of BIPs. It is then assigned a number. This number is generally decided by the editor, often Luke Dashjr, and is assigned logically: BIPs dealing with similar subjects often receive consecutive numbers.

BIPs then go through different statuses over their lifecycle. The current status is specified in the header of each BIP:
* Draft: The proposal is still in the drafting and debate phase;
* Proposed: The BIP is considered complete and ready for review by the community;
* Deferred: The BIP is put on hold for later by the champion or an editor;
* Rejected: A BIP is classified as rejected if it has shown no activity for 3 years. Its author may choose to resume it later, which would allow it to return to the draft status;
* Withdrawn: The BIP has been withdrawn by its author;
* Final: The BIP is accepted and widely implemented on Bitcoin;
* Active: For process BIPs only, this status is assigned once a certain consensus is reached;
* Replaced / Obsolete: The BIP is no longer applicable or has been replaced by a more recent proposal that renders it unnecessary.

![](../../dictionnaire/assets/25.webp)

> ► *BIP is the acronym for "Bitcoin Improvement Proposal". In French, it can be translated as "Proposition d'amélioration de Bitcoin". However, most French texts directly use the acronym "BIP" as a common noun, sometimes feminine, sometimes masculine.*