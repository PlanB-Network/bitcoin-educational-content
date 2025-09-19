---
name: Trezor Shamir Backup
description: Cụm từ Mnemonic chia sẻ đơn và chia sẻ nhiều trên Trezor
---
![cover](assets/cover.webp)



*Tín dụng hình ảnh: [Trezo.io](https://trezor.io/)*



## Tùy chọn sao lưu mới trên Trezor



Từ năm 2023, Trezor đã cung cấp một định dạng sao lưu mới có tên là ***Sao lưu chia sẻ đơn***, dần thay thế phương pháp dựa trên BIP39 cổ điển có trên hầu hết các danh mục đầu tư. Không giống như các cụm từ Mnemonic 12 hoặc 24 từ truyền thống, định dạng mới này dựa trên một cụm từ 20 từ duy nhất có nguồn gốc từ một tiêu chuẩn do SatoshiLabs phát triển: **SLIP39**. Mục đích là cải thiện tính mạnh mẽ và khả năng đọc của bản sao lưu, đồng thời cho phép di chuyển trơn tru sang mô hình sao lưu phân tán.



Mô hình phân tán này được gọi là ***Sao lưu nhiều chia sẻ***. Nó dựa trên cùng một nguyên tắc, nhưng thay vì tạo ra một cụm từ Mnemonic duy nhất, nó chia cụm từ đó thành nhiều phần được gọi là ***chia sẻ***, mỗi phần là một cụm từ Mnemonic theo đúng nghĩa của nó. Để khôi phục danh mục đầu tư, một số lượng nhất định các *chia sẻ* này (được xác định bởi *ngưỡng*) phải được hợp nhất lại. Ví dụ, trong một chương trình 3 trong số 5, bất kỳ 3 *chia sẻ* nào trong số 5 sẽ khôi phục danh mục đầu tư. Xin lưu ý rằng hệ thống sao lưu phân tán của Trezor khác với ví Multisig. Để chi tiêu bitcoin của bạn, chỉ cần Trezor Hardware Wallet của bạn. Chỉ cần một chữ ký. Phân phối chỉ áp dụng ở cấp độ của cụm từ Mnemonic, tức là bản sao lưu.



![Image](assets/fr/01.webp)



Hệ thống này giải quyết vấn đề về điểm lỗi đơn của cụm từ Mnemonic mà không có những bất lợi liên quan đến việc quản lý BIP39 của Multisig hoặc passphrase. Quá trình khôi phục không còn dựa trên một thông tin duy nhất nữa mà dựa trên nhiều thông tin, với lợi ích bổ sung là khả năng chịu mất mát nhờ ngưỡng.



Người dùng đã tạo danh mục đầu tư với *Single-share Backup* có thể chuyển sang *Multi-share Backup* bất kỳ lúc nào mà không cần phải di chuyển danh mục đầu tư của họ. Địa chỉ nhận và tài khoản sẽ vẫn giống hệt nhau. Hệ thống *Multi-share* chỉ ảnh hưởng đến bản sao lưu, trong khi phần còn lại của danh mục đầu tư vẫn không thay đổi.



Tính năng Sao lưu nhiều chia sẻ* khả dụng trên Trezor Model T, Safe 3 và Safe 5. Tính năng này không được Trezor Model One hỗ trợ.



**Lưu ý quan trọng:** Hệ thống *Multi-share* của Trezor an toàn về mặt mật mã vì nó sử dụng chương trình *Shamir's Secret Sharing* để phân phối. Chúng tôi khuyên bạn không nên áp dụng hệ thống tương tự theo cách thủ công, bằng cách tự chia một cụm từ Mnemonic cổ điển. Đây là một hành vi xấu làm tăng đáng kể nguy cơ bị trộm cắp và mất bitcoin của bạn, vì vậy đừng làm vậy. Một cụm từ Mnemonic cổ điển được lưu trữ toàn bộ.



## Chia sẻ bí mật của Shamir trong SLIP39



Cơ chế mật mã cơ bản cho sao lưu *Nhiều cổ phiếu* trên Trezor là *Shamir's Secret Sharing Scheme* (SSSS). Nguyên lý của nó như sau: thông tin bí mật (trong trường hợp này là seed của danh mục đầu tư) được chuyển đổi thành đa thức toán học. Sau đó, một số điểm của đa thức này được tính toán, mỗi điểm trở thành một cổ phiếu. Bí mật ban đầu được tái tạo bằng nội suy đa thức, bằng cách thu thập một số điểm tối thiểu (ngưỡng).



Không thể suy ra thông tin bí mật nào từ số lượng chia sẻ dưới ngưỡng, đảm bảo tính bảo mật lý thuyết hoàn hảo của thông tin bí mật. Nói cách khác, ngay cả kẻ tấn công có sức mạnh tính toán không giới hạn cũng không thể đoán được seed nếu ngưỡng không đạt tới.



SLIP39 sử dụng sơ đồ này để phân phối danh mục đầu tư seed. Mỗi cổ phiếu là một câu 20 từ, được xây dựng từ danh sách 1024 từ (khác với danh sách BIP39).



## Thiết lập sao lưu nhiều chia sẻ trên Trezor



Khi tạo danh mục đầu tư trên Trezor, bạn có ba tùy chọn khác nhau:




- Sử dụng cụm từ BIP39 Mnemonic cổ điển gồm 12 hoặc 24 từ;
- Sử dụng cụm từ Mnemonic chia sẻ đơn (SLIP39);
- Cấu hình nhiều cụm từ Mnemonic trong Multi-share (SLIP39).



Nếu bạn chọn cụm từ Single-share SLIP39 Mnemonic, bạn sẽ có thể nâng cấp lên Multi-share sau này mà không cần phải thiết lập lại danh mục đầu tư. Mặt khác, nếu bạn bắt đầu với danh mục đầu tư BIP39 cổ điển (cụm từ 12 hoặc 24 từ), bạn sẽ không thể chuyển đổi trực tiếp thành Multi-share. Bạn sẽ phải tạo một danh mục đầu tư Multi-share mới từ đầu và chuyển tiền của mình từ danh mục đầu tư cũ sang danh mục đầu tư mới thông qua một hoặc nhiều giao dịch Bitcoin. Đây là một hoạt động phức tạp và tốn kém hơn. Nếu bạn muốn thực hiện quá trình di chuyển này, tôi khuyên bạn nên mua một ví Trezor Hardware Wallet mới để tránh phải nhập seed của mình vào phần mềm danh mục đầu tư.



Trong hướng dẫn này, trước tiên chúng ta sẽ xem cách thiết lập Đa cổ phiếu khi tạo danh mục đầu tư, sau đó, trong phần tiếp theo, chúng ta sẽ xem cách chuyển đổi Một cổ phiếu thành Nhiều cổ phiếu trên danh mục đầu tư hiện có.



Nếu bạn cần trợ giúp về thiết lập ban đầu cho thiết bị của mình, chúng tôi cũng có hướng dẫn chi tiết cho từng mẫu Trezor:



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

### Trên danh mục đầu tư mới



Bây giờ bạn đã hoàn tất cấu hình ban đầu cho Trezor và đã sẵn sàng để tạo danh mục đầu tư. Trong Trezor Suite, hãy nhấp vào nút "*Tạo Wallet mới*".



![Image](assets/fr/02.webp)



Chọn tùy chọn "*Sao lưu nhiều bản chia sẻ*", sau đó nhấp vào "*Tạo Wallet*".



![Image](assets/fr/03.webp)



Chấp nhận các điều khoản sử dụng trên Trezor của bạn và xác nhận việc tạo danh mục đầu tư.



![Image](assets/fr/04.webp)



Trong Trezor Suite, nhấp vào "*Tiếp tục sao lưu*".



![Image](assets/fr/05.webp)



Đọc kỹ hướng dẫn, xác nhận rồi nhấp vào "*Tạo bản sao lưu Wallet*".



![Image](assets/fr/06.webp)



Để biết thêm thông tin về cách lưu và quản lý cụm từ Mnemonic đúng cách, tôi thực sự khuyên bạn nên làm theo hướng dẫn khác này, đặc biệt nếu bạn là người mới bắt đầu:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Trên Trezor, hãy chọn tổng số cổ phiếu bạn muốn cấu hình. Các cấu hình phổ biến nhất là 2-de-3 và 3-de-5. Đối với ví dụ này, tôi sẽ tạo 2-de-3, vì vậy tôi sẽ chọn 3 cổ phiếu. Mỗi cổ phiếu sẽ đại diện cho một cụm từ Mnemonic gồm 20 từ.



*Đối với người dùng Safe 5, mặc dù màn hình sẽ hiển thị "Nhấn để tiếp tục", nhưng thực tế bạn cần phải vuốt lên để xác nhận*



![Image](assets/fr/07.webp)



Sau đó xác nhận ngưỡng, tức là số lượng cổ phiếu cần thiết để lấy lại quyền truy cập vào Wallet và số bitcoin mà nó chứa.



![Image](assets/fr/08.webp)



Trezor sẽ tạo ra nhiều cổ phiếu khác nhau của bạn (cụm từ Mnemonic) bằng cách sử dụng trình tạo số ngẫu nhiên của nó. Đảm bảo rằng bạn không bị theo dõi trong quá trình này. Viết ra các từ được cung cấp trên màn hình trên phương tiện vật lý mà bạn chọn. Điều quan trọng là phải đánh số các từ và theo thứ tự tuần tự.



Tôi khuyên bạn nên ghi chú lại từng chia sẻ trên một phương tiện riêng biệt và quản lý cẩn thận nơi lưu trữ của chúng để tránh việc nhiều chia sẻ có thể truy cập được ở cùng một nơi. Ví dụ, đối với cấu hình 2 trong 3 như của tôi, một lựa chọn sẽ là giữ một chia sẻ ở nhà, một chia sẻ khác với một người bạn đáng tin cậy và chia sẻ cuối cùng trong két an toàn của ngân hàng. Lựa chọn vị trí lưu trữ sẽ phụ thuộc vào chiến lược bảo mật cá nhân của bạn.



Bạn có thể thấy ở đầu màn hình những chia sẻ bạn đang xem.



tất nhiên, bạn không bao giờ được chia sẻ những từ này trên Internet, như tôi đang làm trong hướng dẫn này. Ví dụ Wallet này sẽ chỉ được sử dụng trên Testnet và sẽ bị xóa vào cuối hướng dẫn.



![Image](assets/fr/09.webp)



Để chuyển sang các từ tiếp theo, hãy nhấp vào cuối màn hình. Bạn có thể quay lại bằng cách trượt xuống. Sau khi đã viết hết các từ, hãy giữ ngón tay trên màn hình để chuyển sang phần chia sẻ tiếp theo và lặp lại thao tác.



![Image](assets/fr/10.webp)



Vào cuối mỗi bản ghi âm chia sẻ, bạn sẽ được yêu cầu chọn các từ trong cụm từ Mnemonic của mình để xác nhận rằng bạn đã viết chúng chính xác.



![Image](assets/fr/11.webp)



Và thế là xong, bạn đã sao lưu thành công danh mục đầu tư của mình bằng tùy chọn Chia sẻ nhiều. Bây giờ bạn có thể tiếp tục với phần còn lại của hướng dẫn cấu hình.



### Trên danh mục đầu tư một cổ phiếu hiện có



Nếu bạn đã có Trezor Wallet với bản sao lưu chia sẻ đơn (cụm từ SLIP39 Mnemonic, không phải cụm từ BIP39 cổ điển) và muốn cải thiện tính khả dụng và bảo mật của bản sao lưu Wallet, bạn có thể thiết lập hệ thống chia sẻ nhiều mà không cần phải chuyển bitcoin của mình.



Để thực hiện việc này, hãy kết nối và mở khóa Hardware Wallet của bạn. Trong Trezor Suite, hãy vào Cài đặt.



![Image](assets/fr/12.webp)



Chuyển đến tab "*Thiết bị*".



![Image](assets/fr/13.webp)



Sau đó nhấp vào "*Tạo bản sao lưu chia sẻ nhiều lần*".



![Image](assets/fr/14.webp)



Đọc hướng dẫn, sau đó nhấp vào "*Tạo bản sao lưu chia sẻ nhiều*".



![Image](assets/fr/15.webp)



Sau đó, bạn sẽ cần nhập cụm từ Mnemonic hiện tại của mình (chia sẻ đơn lẻ) trên màn hình Trezor. Chọn số lượng từ (mặc định là 20).



![Image](assets/fr/16.webp)



Sau đó, sử dụng bàn phím trên màn hình Trezor để nhập từng từ trong cụm từ Mnemonic hiện tại của bạn.



![Image](assets/fr/17.webp)



Sau đó, bạn có thể chọn cấu hình Sao lưu nhiều chia sẻ bằng cách làm theo hướng dẫn được cung cấp ở phần trước.



![Image](assets/fr/18.webp)



Sau khi tạo Bản sao lưu nhiều chia sẻ, bạn sẽ cần quyết định phải làm gì với cụm từ Mnemonic chia sẻ đơn ban đầu của mình. Vì danh mục đầu tư Bitcoin vẫn giữ nguyên, nên cụm từ đơn này sẽ luôn cho phép truy cập vào nó. Điều này sẽ phụ thuộc vào chiến lược bảo mật của bạn, nhưng nói chung, bạn nên hủy cụm từ này để loại bỏ điểm lỗi đơn này, đó chính xác là mục đích của Bản sao lưu nhiều chia sẻ. Nếu bạn quyết định hủy nó, hãy đảm bảo rằng bạn thực hiện một cách an toàn, vì **nó vẫn cho phép truy cập vào bitcoin của bạn**.



Xin chúc mừng, giờ bạn đã nắm được cách sử dụng Single-share và Multi-share Backups trên ví phần cứng Trezor. Nếu bạn muốn nâng cao bảo mật Wallet của mình hơn nữa, hãy xem hướng dẫn này về cụm mật khẩu BIP39:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Nếu bạn thấy hướng dẫn này hữu ích, tôi sẽ rất biết ơn nếu bạn để lại một ngón tay cái Green bên dưới. Hãy thoải mái chia sẻ bài viết này trên mạng xã hội của bạn. Cảm ơn bạn rất nhiều!



## Tài nguyên bổ sung





- [SLIP-0039: Chia sẻ bí mật của Shamir cho mã Mnemonic](https://github.com/satoshilabs/slips/blob/master/slip-0039.md);
- [Sao lưu nhiều tài khoản trên Trezor](https://trezor.io/learn/a/multi-share-backup-on-trezor);
- [Wikipedia: Chia sẻ bí mật của Shamir](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing).