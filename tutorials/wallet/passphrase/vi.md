---
name: Cụm từ BIP39
description: Hiểu cách hoạt động của một cụm từ bí mật
---
![cover](assets/cover.webp)

## Cụm từ bí mật BIP39 là gì?

Ví HD thường được tạo ra từ một cụm từ ghi nhớ bao gồm 12 hoặc 24 từ. Cụm từ này rất quan trọng vì nó cho phép khôi phục tất cả các khóa của ví trong trường hợp phương tiện vật lý (như ví cứng, chẳng hạn) bị mất. Tuy nhiên, nó tạo thành một điểm thất bại duy nhất vì nếu nó bị xâm phạm, kẻ tấn công có thể ăn cắp tất cả bitcoin.

![PASSPHRASE BIP39](assets/notext/01.webp)

Đây là nơi mà cụm từ bí mật xuất hiện. Đó là một mật khẩu tùy chọn mà bạn có thể tự do chọn, được thêm vào cụm từ ghi nhớ trong quá trình phát sinh khóa để tăng cường bảo mật cho ví.

![PASSPHRASE BIP39](assets/notext/02.webp)

Hãy cẩn thận không nhầm lẫn cụm từ bí mật với mã PIN của ví cứng hoặc mật khẩu được sử dụng để mở khóa truy cập vào ví trên máy tính của bạn. Không giống như tất cả các yếu tố này, cụm từ bí mật đóng vai trò trong quá trình phát sinh khóa của ví. **Điều này có nghĩa là nếu không có nó, bạn sẽ không bao giờ có thể khôi phục được bitcoin của mình.**

Cụm từ bí mật hoạt động cùng với cụm từ ghi nhớ, thay đổi hạt giống từ đó các khóa được tạo ra. Do đó, ngay cả khi ai đó có được cụm từ 12 hoặc 24 từ của bạn, mà không có cụm từ bí mật, họ không thể truy cập vào quỹ của bạn. **Sử dụng một cụm từ bí mật cơ bản tạo ra một ví mới với các khóa riêng biệt. Chỉnh sửa (ngay cả một chút) cụm từ bí mật sẽ tạo ra một ví khác.**

## Tại sao bạn nên sử dụng cụm từ bí mật?

Cụm từ bí mật là tùy ý và có thể là bất kỳ sự kết hợp ký tự nào do người dùng chọn. Sử dụng cụm từ bí mật do đó mang lại một số lợi ích. Đầu tiên, nó giảm mọi rủi ro liên quan đến việc cụm từ ghi nhớ bị xâm phạm bằng cách yêu cầu một yếu tố thứ hai để truy cập vào quỹ (trộm cắp, truy cập vào nhà bạn, v.v.).

Tiếp theo, nó có thể được sử dụng một cách chiến lược để tạo ra một ví dụ như, để đối phó với các ràng buộc vật lý nhằm ăn cắp quỹ của bạn như cuộc tấn công nổi tiếng "*cuộc tấn công bằng cờ lê 5 đô la*". Trong kịch bản này, ý tưởng là có một ví không có cụm từ bí mật chỉ chứa một lượng nhỏ bitcoin, đủ để thỏa mãn một kẻ tấn công tiềm năng, trong khi có một ví ẩn. Ví này sau đó sử dụng cùng một cụm từ ghi nhớ nhưng được bảo vệ bằng một cụm từ bí mật bổ sung.

Cuối cùng, sử dụng cụm từ bí mật là thú vị khi người ta muốn kiểm soát sự ngẫu nhiên của việc tạo hạt giống ví HD.

## Làm thế nào để chọn một cụm từ bí mật tốt?
Để cụm từ bí mật có hiệu quả, nó phải đủ dài và ngẫu nhiên. Giống như với một mật khẩu mạnh, tôi khuyên bạn nên chọn một cụm từ bí mật càng dài và ngẫu nhiên càng tốt, với sự đa dạng của các chữ cái, số và biểu tượng để làm cho bất kỳ cuộc tấn công bằng cách dùng lực brút không thể xảy ra.

Cũng quan trọng là phải lưu trữ cụm từ bí mật này một cách đúng đắn, cũng như cụm từ ghi nhớ. **Mất nó có nghĩa là mất quyền truy cập vào bitcoin của bạn**. Tôi khuyên bạn không nên chỉ nhớ nó trong đầu, vì điều này tăng rủi ro mất mát một cách không hợp lý. Lý tưởng nhất là viết nó ra trên một phương tiện vật lý (giấy hoặc kim loại) riêng biệt từ cụm từ ghi nhớ. Bản sao lưu này rõ ràng phải được lưu trữ ở một vị trí khác nơi bạn giữ cụm từ ghi nhớ để ngăn chặn cả hai bị xâm phạm cùng một lúc.

## Hướng dẫn

Để thiết lập một cụm từ bí mật trên thiết bị Ledger (Stax, Flex, hoặc Nano), bạn có thể tham khảo hướng dẫn này:

https://planb.network/tutorials/wallet/hardware/passphrase-ledger-9ae6d9a2-7293-438a-8fe0-e59147ef2f49