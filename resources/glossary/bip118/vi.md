---
term: BIP118
---

Đề xuất nhằm cải thiện Bitcoin bằng cách giới thiệu hai bộ chỉnh sửa mới cho SigHash Flag: `SIGHASH_ANYPREVOUT` và `SIGHASH_ANYPREVOUTANYSCRIPT`. Những tính năng này mở rộng khả năng của các giao dịch Bitcoin, đặc biệt là về mặt hợp đồng thông minh và các giải pháp phủ như Lightning Network. BIP118 sẽ cho phép sử dụng Eltoo một cách đáng chú ý. Lợi ích chính của `SIGHASH_ANYPREVOUT` là cho phép tái sử dụng chữ ký qua nhiều giao dịch, mang lại nhiều linh hoạt hơn. Cụ thể, những SigHash này cho phép một chữ ký không bao gồm bất kỳ đầu vào nào của giao dịch.