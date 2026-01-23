---
term: Tái sử dụng địa chỉ

definition: Một thực hành không được khuyến khích là sử dụng cùng một địa chỉ Bitcoin nhiều lần để nhận thanh toán, điều này làm tổn hại đến quyền riêng tư bằng cách cho phép theo dõi các quỹ.
---
Address reuse refers to the practice of using the same receiving address to block multiple UTXOs, sometimes within several different transactions. Bitcoins are typically locked using a cryptographic key pair that corresponds to a unique address. Since the blockchain is public, it is easy to see which addresses are associated with how many bitcoins. In the case of reusing the same address for multiple payments, it is reasonable to imagine that all the associated UTXOs belong to the same entity. Therefore, address reuse poses a problem for the user's privacy. It allows for deterministic links between multiple transactions and UTXOs, as well as perpetuating on-chain fund tracking. Satoshi Nakamoto already mentioned this problem in his White Paper:

> *Như một tường lửa bổ sung, nên sử dụng một cặp khóa mới cho mỗi giao dịch để tránh việc chúng bị liên kết với cùng một chủ sở hữu.*

Nakamoto, S. (2008). "*Bitcoin: A Peer-to-Peer Electronic Cash System*". https://bitcoin.org/bitcoin.pdf.

To preserve privacy at a minimum, it is strongly advised to use each receiving address only once. For each new payment, it is appropriate to generate a new address. For change outputs, a fresh address should also be used. Fortunately, thanks to deterministic and hierarchical wallets, it has become very easy to use a multitude of addresses. All key pairs associated with a wallet can be easily regenerated from the seed. This is also why wallet software always generates a new, different address when you click on the “Receive” button.
