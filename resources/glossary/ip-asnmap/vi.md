---
term: IP_ASN.MAP

---
File used in Bitcoin Core to store the ASMAP, which enhances the bucketing (i.e., grouping) of IP addresses by relying on Autonomous System Numbers (ASN). Instead of grouping outgoing connections by IP network prefixes (/16), this file allows for diversifying connections by establishing an IP addressing map to ASNs, which are unique identifiers for each network on the Internet. The idea is to improve the security and topology of the Bitcoin network by diversifying connections to protect against certain attacks (notably the Erebus attack).