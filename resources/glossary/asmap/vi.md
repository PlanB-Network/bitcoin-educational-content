---
term: ASMAP

definition: Một công cụ Bitcoin Core phân tán các kết nối giữa các nút theo các hệ thống tự trị (ASN) để ngăn chặn các cuộc tấn công Eclipse.
---
A tool invented by Gleb Naumenko and used by Bitcoin Core to enhance the security and topology of the Bitcoin network by diversifying connections among nodes. It is an IP address mapping to Autonomous System Numbers (ASN), allowing for a better distribution of outgoing connections based on ASN rather than IP prefixes. This helps to prevent Eclipse attacks (including the Erebus attack) by making it more difficult for an attacker to simulate multiple nodes.