---
term: BIP0090

definition: Đề xuất đơn giản hóa việc xác minh kích hoạt các bản nâng cấp mềm (soft fork) cũ bằng cách sử dụng chiều cao khối thay vì tín hiệu của thợ đào.
---
Proposal to simplify the process of activating previous soft forks by replacing the miner signaling mechanism through block version numbers with simple block height checks. This change would eliminate the need to verify the previous 1000 blocks for the activation of consensus rules, thereby reducing the technical debt associated with implementing these soft forks.