---
name: BIP-39 Passphrase Trezor
description: Làm thế nào để thêm passphrase vào danh mục đầu tư Trezor của tôi?
---
![cover](assets/cover.webp)



passphrase BIP39 là mật khẩu tùy chọn, kết hợp với cụm từ Mnemonic, cung cấp thêm Layer về bảo mật cho danh mục đầu tư Bitcoin xác định và phân cấp. Trong hướng dẫn này, chúng ta sẽ cùng nhau khám phá cách thiết lập passphrase trên Bitcoin Wallet an toàn của bạn trên Trezor (Safe 3, Safe 5 và Model One).



![Image](assets/fr/01.webp)



Trước khi bắt đầu hướng dẫn này, nếu bạn chưa quen với khái niệm passphrase, cách thức hoạt động và ý nghĩa của nó đối với Bitcoin Wallet của bạn, tôi thực sự khuyên bạn nên tham khảo bài viết lý thuyết khác này, trong đó tôi giải thích mọi thứ (điều này rất quan trọng, vì sử dụng passphrase mà không hiểu đầy đủ cách thức hoạt động của nó có thể khiến bitcoin của bạn gặp rủi ro):



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

passphrase trên Trezor được xử lý theo cách cổ điển nếu bạn đã chọn tiêu chuẩn BIP39 trong quá trình cấu hình (tôi khuyên bạn nên làm như vậy nếu bạn không cần *Sao lưu nhiều chia sẻ*). Điểm đặc biệt của Trezor là bạn có thể nhập passphrase trực tiếp trên Hardware Wallet hoặc thông qua bàn phím máy tính bằng phần mềm Trezor Suite. Tùy chọn thứ hai này kém an toàn hơn đáng kể vì máy tính có bề mặt tấn công lớn hơn nhiều so với Hardware Wallet. Tuy nhiên, việc nhập passphrase phức tạp có thể nhanh hơn trên bàn phím thông thường so với trên Hardware Wallet, điều này có thể khuyến khích sử dụng cụm mật khẩu mạnh. Vì vậy, tốt hơn hết là sử dụng passphrase, ngay cả khi phải nhập, hơn là không sử dụng. Tuy nhiên, điều quan trọng là phải luôn nhận thức được nguy cơ tấn công số tăng lên mà điều này ngụ ý.



Các tùy chọn này không khả dụng trên tất cả các phần mềm quản lý danh mục đầu tư tương thích với Trezor. Ví dụ, đối với Model One, passphrase có thể được nhập qua bàn phím trên Sparrow Wallet. Đối với các mẫu Model T, Safe 3 và Safe 5, bạn phải sử dụng Trezor Suite hoặc nhập passphrase trực tiếp trên Hardware Wallet, vì tùy chọn nhập qua Sparrow đã bị HWI vô hiệu hóa cách đây vài năm.



![Image](assets/fr/02.webp)



Trong Trezor Suite, bạn có hai cách khác nhau để quản lý nhu cầu passphrase. Bạn có thể kích hoạt tùy chọn "*passphrase*" trong tab "*Thiết bị*". Nếu được bật, Trezor Suite và tất cả các phần mềm quản lý danh mục đầu tư khác sẽ yêu cầu bạn nhập passphrase của mình một cách có hệ thống mỗi khi bạn khởi động. Nếu bạn thích cách tiếp cận kín đáo hơn khi sử dụng passphrase, bạn có thể giữ nguyên cài đặt ở "*Chuẩn*". Trong trường hợp này, bạn sẽ cần truy cập thủ công vào menu của Hardware Wallet ở góc trên bên trái và nhấp vào nút "*+ passphrase*" mỗi khi bạn khởi động.



Trước khi bắt đầu hướng dẫn này, vui lòng đảm bảo rằng bạn đã khởi tạo Trezor và tạo cụm từ Mnemonic. Nếu bạn chưa làm vậy và Trezor của bạn là mới, hãy làm theo hướng dẫn dành riêng cho từng mẫu có sẵn trên Plan ₿ Network. Sau khi hoàn tất bước này, bạn có thể quay lại hướng dẫn này.



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02


## Thêm passphrase vào Safe 3 hoặc Safe 5



Sau khi bạn tạo Wallet, lưu Mnemonic và đặt mã PIN, bạn sẽ được đưa đến menu trang chủ Trezor Suite. Ở góc trên bên trái, một cửa sổ sẽ xuất hiện mời bạn kích hoạt passphrase BIP39.



![Image](assets/fr/03.webp)



Nếu cửa sổ này không xuất hiện, bạn sẽ cần phải kích hoạt thủ công tùy chọn "*passphrase*" trong tab cài đặt "*Thiết bị*".



![Image](assets/fr/04.webp)



Cửa sổ này yêu cầu bạn nhập passphrase của mình. Chọn một passphrase mạnh và ngay lập tức tạo bản sao lưu vật lý, trên một phương tiện như giấy hoặc kim loại. Trong ví dụ này, tôi đã chọn passphrase: `fH3&kL@9mP#2sD5qR!82`. Đây là một ví dụ; tuy nhiên, tôi khuyên bạn nên chọn một passphrase dài hơn một chút. Từ 30 đến 40 ký tự sẽ là lý tưởng (như một mật khẩu tốt).



tất nhiên, bạn không bao giờ nên chia sẻ passphrase của mình trên Internet, như tôi đã làm trong hướng dẫn này. Ví dụ Wallet này sẽ chỉ được sử dụng trên Testnet và sẽ bị xóa vào cuối hướng dẫn.



Để có những khuyến nghị cụ thể hơn về việc lựa chọn passphrase, tôi xin mời bạn một lần nữa tham khảo bài viết khác này:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Nếu bạn muốn nhập passphrase qua bàn phím máy tính, hãy nhập vào trường được cung cấp, sau đó nhấp vào "*Truy cập passphrase Wallet*".



![Image](assets/fr/05.webp)



Hardware Wallet của bạn sau đó sẽ hiển thị passphrase. Hãy đảm bảo nó khớp với bản sao lưu vật lý của bạn (giấy hoặc kim loại) trước khi nhấp vào màn hình để tiếp tục.



![Image](assets/fr/06.webp)



Thao tác này sẽ giúp bạn truy cập vào danh mục đầu tư được bảo vệ theo passphrase của mình.



![Image](assets/fr/07.webp)



Nếu bạn muốn tăng cường bảo mật bằng cách chỉ nhập passphrase vào Trezor, khi được nhắc, hãy nhấp vào "*Nhập passphrase vào Trezor*".



![Image](assets/fr/08.webp)



Bàn phím T9 sẽ xuất hiện trên Trezor của bạn, cho phép bạn nhập passphrase. Sau khi nhập xong, hãy nhấp vào dấu tích Green để áp dụng passphrase vào Wallet của bạn.



![Image](assets/fr/09.webp)



Sau đó, bạn sẽ có quyền truy cập vào passphrase an toàn Wallet của mình.



![Image](assets/fr/10.webp)



Để sử dụng Sparrow Wallet, quy trình cũng tương tự, nhưng đối với các mẫu T, Safe 3 và Safe 5, passphrase phải được nhập vào Hardware Wallet chứ không phải thông qua bàn phím máy tính.



Bất cứ khi nào Sparrow Wallet yêu cầu truy cập vào Trezor của bạn và passphrase vẫn chưa được áp dụng kể từ lần khởi động cuối cùng, bạn sẽ cần phải nhập Wallet bằng bàn phím T9.



![Image](assets/fr/11.webp)



## Thêm passphrase vào Model One



Trên Model One, việc sử dụng passphrase BIP39 gần như là không thể thiếu. Vì thiết bị này không tích hợp Secure Element nên việc trích xuất thông tin nhạy cảm tương đối dễ dàng. Do đó, nó không chống lại được các cuộc tấn công vật lý. Tuy nhiên, vì passphrase không được giữ lại trên thiết bị sau khi đã tắt, nên việc sử dụng passphrase mạnh (không thể tấn công bằng bruteable) có thể bảo vệ bạn khỏi hầu hết các cuộc tấn công vật lý đã biết trên model này.



Trên Model One, không thể nhập passphrase trực tiếp trên Hardware Wallet. Bạn sẽ phải nhập thông qua bàn phím máy tính.



Sau khi bạn tạo Wallet, lưu Mnemonic và đặt mã PIN, bạn sẽ được đưa đến menu trang chủ Trezor Suite. Ở góc trên bên trái, một cửa sổ mời bạn kích hoạt passphrase BIP39 sẽ xuất hiện.



![Image](assets/fr/12.webp)



Nếu cửa sổ này không xuất hiện, bạn cần kích hoạt tùy chọn "*passphrase*" trong tab "*Thiết bị*" của phần cài đặt.



![Image](assets/fr/13.webp)



Cửa sổ này yêu cầu bạn nhập passphrase của mình. Chọn một passphrase mạnh và ngay lập tức tạo bản sao lưu vật lý, trên một phương tiện như giấy hoặc kim loại. Trong ví dụ này, tôi đã chọn passphrase: `fH3&kL@9mP#2sD5qR!82`. Đây chỉ là một ví dụ; tuy nhiên, tôi khuyên bạn nên chọn một passphrase dài hơn một chút. Từ 30 đến 40 ký tự sẽ là lý tưởng (như một mật khẩu tốt).



Để có những khuyến nghị cụ thể hơn về việc lựa chọn passphrase, tôi xin mời bạn một lần nữa tham khảo bài viết khác này:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Nhập passphrase của bạn vào trường được cung cấp, sau đó nhấp vào nút "*Truy cập passphrase Wallet*".



![Image](assets/fr/14.webp)



Hardware Wallet của bạn sẽ hiển thị passphrase của bạn. Hãy đảm bảo nó khớp với bản sao lưu vật lý của bạn (giấy hoặc kim loại), sau đó nhấp vào nút bên phải để tiếp tục.



![Image](assets/fr/15.webp)



Thao tác này sẽ đưa bạn đến danh mục đầu tư được bảo vệ theo passphrase của bạn.



![Image](assets/fr/16.webp)



Để sử dụng Sparrow Wallet sau đó, quy trình vẫn giữ nguyên. Mỗi lần Sparrow yêu cầu truy cập vào Hardware Wallet của bạn và passphrase chưa được nhập kể từ lần thiết bị được khởi động gần nhất, bạn sẽ cần phải nhập vào.



![Image](assets/fr/17.webp)



Xin chúc mừng, giờ bạn đã nắm được cách sử dụng passphrase BIP39 trên ví phần cứng Trezor. Nếu bạn muốn nâng cao bảo mật Wallet của mình hơn nữa, hãy xem hướng dẫn này về hệ thống sao lưu *Multi-share* của Trezor (*Shamir's Secret Sharing Scheme*):



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

Nếu bạn thấy hướng dẫn này hữu ích, tôi sẽ rất biết ơn nếu bạn để lại một ngón tay cái Green bên dưới. Hãy thoải mái chia sẻ bài viết này trên mạng xã hội của bạn. Cảm ơn bạn rất nhiều!