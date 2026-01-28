---
term: Tor (the onion router)

definition: Mạng lưới các máy chủ chuyển tiếp ẩn danh các kết nối TCP thông qua nhiều lớp mã hóa, có thể sử dụng với Bitcoin.
---
A network of relay servers (nodes) that anonymizes the origin of TCP connections on the internet. It operates by encapsulating data in multiple layers of encryption. Each relay node removes a layer to reveal the address of the next node, until the final destination is reached. The Tor network ensures anonymity by preventing intermediate nodes from knowing both the origin and destination of the data, making it very difficult for an observer to trace the user's activity. The TOR network can be used in the context of Bitcoin to avoid associating one's IP address with a Bitcoin node, thereby avoiding the leakage of certain personal information.

> ► *“TOR” stands for “The Onion Router”. It is important to differentiate between TOR the network, and TOR Browser, a web browser based on Firefox that is specifically designed to utilize the TOR network.*