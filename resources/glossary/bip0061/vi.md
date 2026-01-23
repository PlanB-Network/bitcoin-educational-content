---
term: BIP0061

definition: Tin nhắn từ chối giữa các nút cho biết lý do tại sao một giao dịch hoặc khối không hợp lệ. Đã bị loại bỏ trong Bitcoin Core 0.20.0.
---
Introduced a rejection message in the communication protocol between nodes. The goal of BIP61 is to add a feedback mechanism when a node receives a transaction or a block from another node that it considers invalid. This rejection message would allow a node to signal to the sender the reason why it was rejected. This type of communication was intended to improve interoperability among different clients and communications between full nodes and SPV clients. The functionalities brought by BIP61 were eventually abandoned starting from version 0.20.0 of Bitcoin Core, as they were considered unnecessary while they involved increased bandwidth needs.