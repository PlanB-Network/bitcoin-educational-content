---
term: TIMESTAMP

---
Timestamping, or "timestamp" in English, is a mechanism that involves associating a precise temporal marker with an event, data, or message. In the general context of computer systems, timestamping is used to determine the chronological order of operations and to verify the integrity of data over time.

In the specific case of Bitcoin, timestamps are used to establish the chronology of transactions and blocks. Each block in the blockchain contains a timestamp indicating the approximate moment of its creation. Satoshi Nakamoto even speaks of a "timestamp server" in his White Paper, to describe what we would call today the "blockchain." The role of timestamping in Bitcoin is to determine the chronology of transactions, in order to determine, without the intervention of a central authority, which transaction came first. This mechanism allows each user to verify the non-existence of a transaction in the past, and thus to prevent a malicious user from performing a double spend. This mechanism is justified by Satoshi Nakamoto in his White Paper with the famous phrase: "*The only way to confirm the absence of a transaction is to be aware of all transactions.*" This standard is established on Unix time, which represents the total seconds passed since January 1, 1970.

> ► *The block timestamping on Bitcoin is relatively flexible, as for a timestamp to be considered valid, it simply needs to be greater than the median time of the 11 preceding blocks (MTP) and less than the median of the times returned by the nodes (network-adjusted time) plus 2 hours.*