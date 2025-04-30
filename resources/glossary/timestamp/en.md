---
term: HORODATAGE
---

Timestamping, or "Timestamp" in English, is a mechanism for associating a precise time mark with an event, data or message. In the general context of computer systems, timestamping is used to determine the chronological order of operations and to verify the integrity of data over time.

In the specific case of Bitcoin, timestamps are used to establish the chronology of transactions and blocks. Each block in Blockchain contains a timestamp indicating the approximate time of its creation. Satoshi Nakamoto even talks about a "timestamp server", in his White Paper, to describe what we would call "Blockchain" today. The role of timestamping on Bitcoin is to determine the chronology of transactions, so that, without the intervention of a central authority, it can be determined which transaction arrived first. This mechanism enables each user to verify the non-existence of a transaction in the past, and thus prevent a malicious user from making a double expenditure. This mechanism is justified by Satoshi Nakamoto in his White Paper with the famous sentence: " *This standard is based on the Unix time, which represents the total number of seconds passed since January 1, 1970.

> ► *Block timestamps are relatively flexible on Bitcoin, since for a timestamp to be considered valid, it is simply necessary for it to be greater than the median time of the 11 blocks preceding it (MTP) and smaller than the median of the times returned by the nodes (network-adjusted time) plus 2 hours.*