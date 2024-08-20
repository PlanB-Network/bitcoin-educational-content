---
term: COVENANT
---

Một cơ chế cho phép áp đặt các điều kiện cụ thể về cách một đơn vị tiền tệ nhất định có thể được chi tiêu, bao gồm cả trong các giao dịch tương lai. Ngoài các điều kiện thường được cho phép bởi ngôn ngữ script trên một UTXO, covenant thực thi thêm các ràng buộc về cách Bitcoin này có thể được chi tiêu trong các giao dịch tiếp theo. Về mặt kỹ thuật, việc thiết lập một covenant xảy ra khi `scriptPubKey` của một UTXO định rõ các hạn chế đối với `scriptPubKey` của các đầu ra của một giao dịch chi tiêu UTXO đó. Bằng cách mở rộng phạm vi của script, covenant sẽ cho phép nhiều phát triển trên Bitcoin như việc neo hai chiều của drivechains, việc triển khai vaults, hoặc việc cải thiện các hệ thống phủ như Lightning. Các đề xuất về covenant được phân biệt dựa trên ba tiêu chí:
* Phạm vi của chúng;
* Cách thức triển khai;
* Tính đệ quy của chúng.

Có nhiều đề xuất cho phép sử dụng covenant trên Bitcoin. Những cái tiên tiến nhất trong quá trình triển khai bao gồm: `OP_CHECKTEMPLATEVERIFY` (CTV), `SIGHASH_ANYPREVOUT` (APO), và `OP_VAULT`. Ngoài ra, còn có các đề xuất khác như: `OP_TX`, `OP_TAPLEAFUPDATEVERIFY` (TLUV), `OP_EVICT`, `OP_CHECKSIGFROMSTACKVERIFY` (CSFSV), `OP_CAT`, v.v.

Để hiểu rõ hơn về khái niệm covenant, hãy xem xét phép so sánh này: hãy tưởng tượng một két sắt chứa 500€ bằng tiền mặt nhỏ. Nếu bạn quản lý mở két này bằng chìa khóa đúng, thì bạn tự do sử dụng số tiền này theo ý muốn. Đây là tình huống bình thường với Bitcoin. Bây giờ, hãy tưởng tượng rằng cùng một két sắt không chứa 500€ bằng tiền mặt, mà là phiếu ăn có giá trị tương đương. Nếu bạn thành công trong việc mở két này, bạn có thể sử dụng số tiền này. Tuy nhiên, tự do chi tiêu của bạn bị hạn chế, vì bạn chỉ có thể sử dụng những phiếu này để thanh toán tại một số nhà hàng nhất định. Như vậy, có một điều kiện đầu tiên để chi tiêu số tiền này, đó là quản lý để mở két bằng chìa khóa phù hợp. Nhưng cũng có một điều kiện bổ sung về việc sử dụng số tiền này trong tương lai: nó phải được chi tiêu độc quyền tại các nhà hàng đối tác, và không được tự do. Hệ thống các ràng buộc này đối với các giao dịch tương lai được gọi là covenant.

> ► *Trong tiếng Pháp, không có thuật ngữ nào chính xác diễn đạt ý nghĩa của từ "covenant". Người ta có thể nói về "clause", "pact", hoặc "commitment", nhưng những từ này không hoàn toàn tương đương với thuật ngữ "covenant". Thuật ngữ này được mượn từ ngôn ngữ pháp lý cho phép mô tả một điều khoản hợp đồng áp đặt các nghĩa vụ lâu dài đối với một tài sản.*