---
term: Anchor
---

Trong giao thức RGB, Anchor biểu diễn một tập hợp dữ liệu phía máy khách được sử dụng để chứng minh việc đưa một Commitment duy nhất vào một giao dịch. Trong giao thức RGB, Anchor bao gồm Elements sau:




- transaction ID Bitcoin (txid) từ Witness Transaction ;
- Multi Protocol Commitment (MPC);
- Deterministic Bitcoin Commitment (DBC);
- Bằng chứng giao dịch bổ sung (ETP) nếu sử dụng cơ chế Tapret Commitment.


Do đó, Anchor phục vụ cho việc thiết lập liên kết có thể xác minh giữa giao dịch Bitcoin cụ thể và dữ liệu riêng tư được xác thực bởi giao thức RGB. Nó đảm bảo rằng dữ liệu này thực sự được đưa vào Blockchain mà không cần công khai nội dung chính xác của chúng.