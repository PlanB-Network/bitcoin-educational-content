---
term: SEED (BITCOIN)
---

Trong bối cảnh của Bitcoin, seed là một giá trị 512-bit được sử dụng để sinh ra tất cả các khóa riêng và khóa công khai liên quan đến ví HD (Hierarchical Deterministic). Về mặt kỹ thuật, seed là một giá trị khác biệt so với cụm từ khôi phục (hoặc ghi nhớ). Cụm từ này, thường gồm 12 hoặc 24 từ, được tạo ra một cách giả ngẫu nhiên từ một nguồn entropy và được hoàn thiện bởi một mã kiểm tra. Cụm từ này giúp việc sao lưu bởi con người trở nên dễ dàng hơn bằng cách cung cấp một biểu diễn văn bản của giá trị tại cơ sở của ví.

Để thu được seed thực sự, cụm từ khôi phục, có thể kèm theo một cụm từ mật khẩu tùy chọn, được xử lý qua thuật toán PBKDF2 (*Password-Based Key Derivation Function 2*). Kết quả của phép tính này là một seed 512-bit. Chính seed này được sử dụng để sinh ra một cách định hình khóa chính, và sau đó là toàn bộ bộ khóa cho ví HD, phù hợp với BIP32.

![](../../dictionnaire/assets/31.png)

> ► *Tuy nhiên, trong ngôn ngữ thông thường, đa số người dùng bitcoin thường nhắc đến cụm từ ghi nhớ khi họ nói về "seed," và không phải là trạng thái trung gian của quá trình sinh ra nằm giữa cụm từ ghi nhớ và khóa chính.*