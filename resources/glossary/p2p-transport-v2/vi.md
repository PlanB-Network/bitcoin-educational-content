---
term: P2P TRANSPORT V2

---
New version of the Bitcoin P2P transport protocol incorporating opportunistic encryption to enhance the privacy and security of communications between nodes. This improvement aims to address several issues with the basic version of the P2P protocol, notably by making the exchanged data indistinguishable to a passive observer (such as an internet service provider), thereby reducing the risks of censorship and attacks through the detection of specific patterns in data packets.

The implemented encryption does not include authentication in order to avoid adding unnecessary complexity and to not compromise the permissionless nature of the network connection. This new P2P transport protocol nevertheless offers better security against passive attacks and makes active attacks significantly more costly and detectable (notably MITM attacks). The introduction of a pseudo-random data stream complicates the task for attackers wishing to censor or manipulate communications.

The P2P Transport V2 was included as an option (disabled by default) in version 26.0 of Bitcoin Core, deployed in December 2023. It can be activated with the `v2transport=1` option in the configuration file.