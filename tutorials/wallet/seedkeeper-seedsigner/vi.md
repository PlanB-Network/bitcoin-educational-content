---
name: Seedkeeper x SeedSigner
description: Làm thế nào để sử dụng Seedkeeper với SeedSigner của tôi?
---

![cover](assets/cover.webp)



*Cảm ơn nhóm [Satochip](https://satochip.io/) đã đồng ý sử dụng lại [video của họ](https://www.youtube.com/@satochip/videos) trong hướng dẫn này. Cũng xin cảm ơn [Crypto Guide](https://www.youtube.com/@CryptoGuide/) vì đã cung cấp fork cho firmware SeedSigner, cho phép hỗ trợ thẻ thông minh.



---

SeedSigner là phần cứng wallet mà bạn tự lắp ráp từ phần cứng tiêu chuẩn, thường là xung quanh Raspberry Pi Zero. wallet này được gọi là "*stateless*": không giống như hầu hết các mẫu khác trên thị trường (Coldcard, Trezor, Ledger, v.v.), nó không lưu trữ bất kỳ dữ liệu nào trong bộ nhớ cố định và chỉ hoạt động trực tiếp từ RAM. Do đó, seed của danh mục đầu tư của bạn sẽ không bao giờ được lưu trữ trên SeedSigner. Mỗi lần khởi động lại, bạn sẽ cần điền thông tin để thiết bị có thể ký các giao dịch của mình. Phương pháp phổ biến nhất là lưu seed dưới dạng mã QR, sau đó bạn quét mã này mỗi khi sử dụng (*SeedQR*).



Tuy nhiên, cách tiếp cận này cũng tiềm ẩn một rủi ro đáng kể: seed phải được duy trì ở dạng văn bản rõ để có thể quét được. Trong trường hợp bị đánh cắp hoặc xâm nhập, kẻ tấn công có thể dễ dàng lấy được nó và đánh cắp bitcoin của bạn.



Để khắc phục điểm yếu này, SeedSigner có thể được kết hợp với [**Seedkeeper**](https://satochip.io/product/seedkeeper/), một thẻ thông minh do Satochip phát triển. Điều này cho phép lưu trữ các cụm từ ghi nhớ (hoặc các bí mật khác) trong thẻ secure element được bảo vệ bằng mã PIN. Applet Seedkeeper là mã nguồn mở và secure element của nó đã được chứng nhận EAL6+. Khi được sử dụng kết hợp với SeedSigner, nó cung cấp một tính năng bảo mật rất thú vị: khóa của bạn được quản lý hoàn toàn ngoại tuyến, bạn ký giao dịch trên một màn hình đáng tin cậy, và seed được bảo vệ vật lý bằng thẻ thông minh chống lại các cuộc tấn công vật lý.



Tất cả những gì bạn cần để hoàn tất quá trình cài đặt là:




- Thiết bị thông thường cần có cho SeedSigner cổ điển: Raspberry Pi Zero, màn hình Waveshare 1,3", máy ảnh tương thích và thẻ nhớ microSD (bạn sẽ tìm thấy thêm thông tin chi tiết trong hướng dẫn SeedSigner bên dưới);
- Bộ mở rộng SeedSigner, có sẵn [trên cửa hàng Satochip chính thức](https://satochip.io/product/seedsigner-extension-kit/), cho phép bạn đọc và ghi vào thẻ thông minh trực tiếp từ SeedSigner. Một lựa chọn khác là sử dụng đầu đọc thẻ thông minh ngoài, có thể kết nối bằng cáp với cổng Micro-USB trên Raspberry Pi. Tuy nhiên, tôi chưa tự mình thử nghiệm giải pháp này;
- Seedkeeper hoặc một thẻ thông minh trống để cài đặt ứng dụng Seedkeeper (bộ mở rộng do Satochip bán đã bao gồm một thẻ thông minh trống).



![Image](assets/fr/01.webp)



Hướng dẫn này bao gồm hai tình huống:




- Nếu bạn đã có danh mục đầu tư Bitcoin được quản lý thông qua SeedSigner, chỉ cần cài đặt chương trình cơ sở mới. Sau đó, bạn có thể tiếp tục sử dụng wallet hiện có, nhưng lần này sử dụng Seedkeeper để tăng cường bảo mật.
- Nếu bạn chưa có Bitcoin wallet được liên kết với SeedSigner, bạn cần làm theo các bước **5** và **6** của hướng dẫn bên dưới. Các phần này giải thích cách generate một cụm từ ghi nhớ với SeedSigner, lưu nó qua *SeedQR*, rồi kết nối wallet này với Sparrow Wallet để quản lý. Tôi sẽ không đi sâu vào các quy trình này ở đây và **Tôi giả định rằng bạn đã có Bitcoin wallet đang hoạt động, được cấu hình với Sparrow và SeedSigner**.



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 1. Cài đặt chương trình cơ sở



Để sử dụng SeedSigner với Seedkeeper, bạn cần cài đặt một firmware thay thế, khác với firmware của SeedSigner gốc, để hỗ trợ đọc thẻ thông minh. Để làm được điều này, [tôi khuyên bạn nên sử dụng fork từ "*3rdIteration*"](https://github.com/3rdIteration/seedsigner). Tải xuống [phiên bản mới nhất của hình ảnh](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) tương ứng với model Raspberry Pi bạn đang sử dụng.



![Image](assets/fr/02.webp)



Nếu bạn chưa có, hãy tải xuống phần mềm [Balena Etcher](https://etcher.balena.io/), sau đó thực hiện như sau:




- Cắm thẻ nhớ microSD vào máy tính;
- Khởi chạy Etcher;
- Chọn tệp `.zip` mà bạn vừa tải xuống;
- Chọn thẻ nhớ microSD làm mục tiêu;
- Nhấp vào `Flash!`.



![Image](assets/fr/03.webp)



Chờ cho đến khi quá trình hoàn tất: thẻ nhớ microSD của bạn đã sẵn sàng để sử dụng. Bây giờ bạn có thể chuyển sang lắp ráp thiết bị.



Để biết thêm chi tiết về cài đặt chương trình cơ sở và xác minh phần mềm (một bước tôi thực sự khuyên bạn nên thực hiện), hãy xem hướng dẫn sau:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Lắp ráp đầu đọc thẻ thông minh



![video](https://youtu.be/jqE8HDMCImA)



Bắt đầu bằng cách lắp camera vào Raspberry Pi Zero, cẩn thận lắp camera vào chân camera và khóa bằng chốt màu đen. Sau đó, đặt Pi xuống đáy hộp, đảm bảo các cổng được căn chỉnh với các lỗ tương ứng.



![Image](assets/fr/04.webp)



Sau đó, gắn đầu đọc thẻ thông minh vào chân GPIO của Raspberry Pi Zero.



![Image](assets/fr/05.webp)



Trượt nắp nhựa vào đầu đọc thẻ thông minh cho đến khi nắp được đặt đúng vị trí.



![Image](assets/fr/06.webp)



Sau đó thêm màn hình vào các chân GPIO của phần mở rộng.



![Image](assets/fr/07.webp)



Cuối cùng, lắp thẻ nhớ microSD chứa chương trình cơ sở vào cổng bên hông của Raspberry Pi Zero.



![Image](assets/fr/08.webp)



Bây giờ bạn có thể kết nối SeedSigner qua cổng Micro-USB của Raspberry Pi Zero hoặc qua cổng USB-C của bộ mở rộng. Cả hai tùy chọn đều hoạt động. Chờ vài giây để khởi động, sau đó bạn sẽ thấy màn hình chào mừng xuất hiện.



![Image](assets/fr/09.webp)



Để biết thêm chi tiết về cách thiết lập ban đầu cho SeedSigner, tôi khuyên bạn nên xem hướng dẫn sau:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Nạp thẻ thông minh bằng ứng dụng Seedkeeper (tùy chọn)



![video](https://youtu.be/NF4HemyEcOY)



Nếu bạn đã sở hữu Seedkeeper, bạn có thể bỏ qua bước này và chuyển thẳng đến bước 4. Trong phần này, chúng ta sẽ xem cách cài đặt ứng dụng Seedkeeper trên thẻ thông minh trống (phương pháp tự làm).



Để bắt đầu, hãy mở menu `Công cụ > Công cụ thẻ thông minh` trên SeedSigner của bạn.



![Image](assets/fr/10.webp)



Sau đó chọn `DIY Tools > Install Applet`.



![Image](assets/fr/11.webp)



Cắm thẻ thông minh vào đầu đọc SeedSigner, mặt chip hướng xuống dưới, sau đó chọn ứng dụng `SeedKeeper`.



![Image](assets/fr/12.webp)



Hãy kiên nhẫn trong quá trình cài đặt: quá trình này có thể mất vài chục giây.



![Image](assets/fr/13.webp)



Sau khi cài đặt thành công applet, bạn có thể tiến hành bước 4.



![Image](assets/fr/14.webp)



## 4. Lưu SeedQR hiện có trên Seedkeeper



![video](https://youtu.be/X-vmFHU9Ec8)



Bây giờ Seedkeeper của bạn đã hoạt động, bạn có thể lưu mã ghi nhớ Bitcoin wallet vào thẻ thông minh. Để bắt đầu, hãy bật SeedSigner như bình thường, sau đó quét *SeedQR* của wallet để tải mã vào thiết bị. Sau khi nhập seed, chỉ cần chọn `Done`.



![Image](assets/fr/15.webp)



Khi seed được tải, hãy truy cập vào menu `Backup Seed`.



![Image](assets/fr/16.webp)



Sau đó, chèn Seedkeeper vào ổ SeedSigner và chọn tùy chọn `To SeedKeeper`.



![Image](assets/fr/17.webp)



SeedSigner sau đó sẽ yêu cầu bạn nhập mã PIN cho Seedkeeper. Vì đây là thẻ trống nên chưa có mã nào được xác định. Hãy nhập bất kỳ mã nào để bỏ qua bước này, sau đó xác thực.



![Image](assets/fr/18.webp)



SeedSigner phát hiện Seedkeeper chưa được khởi tạo (tức là chưa đặt mật khẩu). Nhấp vào `Tôi hiểu` để tiếp tục.



![Image](assets/fr/19.webp)



Bây giờ, hãy chọn mã PIN mới của Seedkeeper, từ 4 đến 16 ký tự. Để tăng cường bảo mật, hãy chọn một mã dài và ngẫu nhiên: đây là rào cản duy nhất bảo vệ quyền truy cập vật lý vào cụm từ ghi nhớ của bạn.



Hãy nhớ lưu mã PIN này ngay sau khi tạo, có thể là trong một trình quản lý mật khẩu đáng tin cậy hoặc trên một phương tiện vật lý riêng biệt tùy thuộc vào chiến lược của bạn. Trong trường hợp sau, hãy đảm bảo không bao giờ để phương tiện chứa mã PIN ở cùng nơi với Seedkeeper, nếu không việc bảo vệ sẽ không hiệu quả. Điều quan trọng là phải có một bản sao lưu: **Nếu không có mã PIN này, bạn sẽ không thể truy cập seed và số bitcoin của bạn sẽ bị mất**.



![Image](assets/fr/20.webp)



Sau đó, bạn có thể định nghĩa một `Nhãn` liên kết với cụm từ ghi nhớ của mình. Nhãn này hữu ích nếu bạn lưu trữ nhiều bí mật trên Seedkeeper, giúp bạn có thể dễ dàng nhận dạng chúng.



![Image](assets/fr/21.webp)



Cụm từ ghi nhớ của bạn hiện đã được lưu trên thẻ thông minh.



![Image](assets/fr/22.webp)



Về chiến lược bảo mật, có nhiều phương pháp có thể áp dụng, tùy thuộc vào nhu cầu và mức độ rủi ro của bạn. Cá nhân tôi khuyên bạn nên giữ ít nhất 2 bản sao seed:




- Đây là lần đầu tiên thẻ thông minh được áp dụng, cho phép bạn dễ dàng truy cập cho các hoạt động hàng ngày, chẳng hạn như xác minh địa chỉ hoặc ký giao dịch. Phương pháp này rất thiết thực (như chúng ta sẽ thấy trong phần 5) và vẫn an toàn nhờ tính năng bảo vệ của mã PIN, vì vậy bạn có thể truy cập mà không gặp rủi ro lớn;
- Bản sao thứ hai của cụm từ ghi nhớ chưa được mã hóa, đóng vai trò là bản sao lưu cuối cùng cho danh mục đầu tư của bạn, chỉ được sử dụng trong trường hợp Seedkeeper bị mất hoặc bị đánh cắp. Vì phiên bản này chưa được mã hóa, bạn phải lưu trữ nó ở một nơi riêng biệt, an toàn hơn để tránh việc cả 2 bản sao lưu bị xâm phạm đồng thời.



Tùy thuộc vào chiến lược bảo vệ và hồ sơ rủi ro của bạn, bạn cũng có thể sao chép seed trên nhiều Seedkeeper khác nhau hoặc tạo nhiều bản sao vật lý của mã ghi nhớ. Để tìm hiểu thêm về các phương pháp này, hãy xem hướng dẫn sau:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


## 5. Nạp seed từ Seedkeeper



![video](https://youtu.be/ms0Iq_IyaoE)



Bây giờ bạn có thể sử dụng Seedkeeper để tải cụm từ ghi nhớ vào SeedSigner khi khởi động, và từ đó ký các giao dịch Bitcoin của bạn. Để bắt đầu, hãy bật SeedSigner bằng cách cắm điện, sau đó mở menu `Seeds`.



![Image](assets/fr/23.webp)



Sau đó chọn tùy chọn `Từ SeedKeeper`.



![Image](assets/fr/24.webp)



Cắm Seedkeeper vào đầu đọc thẻ thông minh, sau đó nhập mã PIN để mở khóa. Xác nhận mục nhập bằng cách nhấn nút xác nhận `KEY3` ở góc dưới bên phải.



![Image](assets/fr/25.webp)



Seedkeeper có thể chứa nhiều bí mật, vì vậy SeedSigner sẽ nhắc bạn chọn bí mật bạn muốn tải. Nhãn hiển thị tương ứng với tên bạn đã xác định ở bước 4. Nếu, như trong trường hợp của tôi, bạn chỉ đăng ký một seed, thì sẽ chỉ có một tùy chọn khả dụng.



![Image](assets/fr/26.webp)



seed của bạn hiện đã được tải. Hãy kiểm tra xem đây có phải là wallet chính xác hay không bằng cách so sánh dấu vân tay hiển thị trên màn hình với dấu vân tay được chỉ định trong cài đặt Sparrow Wallet của bạn. Dấu vân tay này cũng đã được cung cấp khi wallet được tạo lần đầu.



Nếu bạn đang sử dụng passphrase, bạn có thể áp dụng ở bước này (xem phần 6 của hướng dẫn này). Nếu không, chỉ cần nhấp vào `Xong`.



![Image](assets/fr/27.webp)



Sau đó, bạn có thể sử dụng wallet như bình thường: kiểm tra địa chỉ giao hàng và ký giao dịch, giống như SeedSigner cổ điển. Để tìm hiểu thêm về cách sử dụng, hãy xem hướng dẫn chuyên sâu:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 6. Sử dụng Seedkeeper với passphrase BIP39



Bạn có đang sử dụng passphrase để bảo vệ danh mục đầu tư Bitcoin của mình không? Bạn cũng có thể đăng ký passphrase trong Seedkeeper cùng với seed. Giải pháp này sẽ cho phép bạn nhanh chóng tải wallet lên SeedSigner mà không cần phải nhập thủ công passphrase trên bàn phím nhỏ mỗi lần sử dụng.



Tôi thấy phương pháp này đặc biệt thú vị, vì nó cho phép bạn tận dụng lợi thế bảo mật của passphrase, đồng thời loại bỏ những hạn chế liên quan đến việc sử dụng hàng ngày. Dưới đây là ví dụ về cấu hình tôi khuyên dùng:




- Lưu trữ seed và passphrase của bạn trong hộp Seedkeeper, được bảo vệ bằng mã PIN mạnh (điều này rất quan trọng). Bản sao lưu này sẽ giúp bạn dễ dàng sử dụng wallet hàng ngày. Nếu muốn, bạn có thể sao chép thông tin này trên một hộp Seedkeeper thứ hai;
- Ngoài ra, hãy giữ một bản sao rõ ràng của mã ghi nhớ và mã passphrase, trên giấy hoặc kim loại. Đây là phương án dự phòng cuối cùng nếu bạn làm mất Seedkeeper hoặc mã PIN. Hãy đảm bảo lưu trữ các bản sao này ở những nơi riêng biệt để chúng không bị xâm phạm cùng lúc.



Trong cấu hình này, nếu ai đó chỉ lấy được mã ghi nhớ dạng văn bản thuần túy của bạn, họ sẽ không thể đánh cắp bất cứ thứ gì nếu không biết mã passphrase (tất nhiên, với điều kiện mã này đủ mạnh để chống lại tấn công brute-force). Ngược lại, nếu ai đó phát hiện ra mã passphrase của bạn ở dạng văn bản thuần túy, mã này sẽ không thể sử dụng được nếu không có mã ghi nhớ tương ứng.



Cuối cùng, nếu ai đó cố gắng truy cập vật lý vào Seedkeeper của bạn bằng seed và passphrase, họ sẽ không thể trích xuất bất cứ thứ gì nếu không biết mã PIN. Không giống như passphrase, mã này không thể bị bẻ khóa bằng phương pháp brute-force, vì thẻ thông minh sẽ tự động khóa sau 5 lần thử không hợp lệ.



Do đó, tính an toàn của cấu hình này dựa trên 2 điểm thiết yếu:




- **Mã passphrase mạnh**: phải dài, ngẫu nhiên và chứa nhiều ký tự. Độ phức tạp của mã không phải là vấn đề với bạn, vì bạn chỉ cần nhập mã một lần trên bàn phím trong quá trình khởi tạo; sau đó, mã sẽ được Seedkeeper truyền đi;
- **Mã PIN mạnh** cho Seedkeeper: cũng ngẫu nhiên và bao gồm 16 ký tự.



Để thiết lập, hãy bắt đầu bằng cách tải passphrase vào SeedSigner theo cách thông thường. Bạn có thể làm theo quy trình được hướng dẫn chi tiết trong hướng dẫn này:



https://planb.academy/tutorials/wallet/backup/seedsigner-passphrase-7a61f64d-aa03-4bcf-8308-00c89a74cffe

Sau khi danh mục đầu tư của bạn với passphrase đã được tải chính xác lên SeedSigner, hãy mở menu `Seeds` và chọn footprint tương ứng với danh mục đầu tư này. Lưu ý rằng footprint này khác với footprint của danh mục đầu tư không có passphrase.



![Image](assets/fr/28.webp)



Sau đó nhấp vào `Sao lưu Seed`, chèn Seedkeeper vào ổ đĩa và chọn `Đến SeedKeeper`.



![Image](assets/fr/29.webp)



Nhập mã PIN để mở khóa Seedkeeper, sau đó gán nhãn cho bí mật này. Bạn có thể để dấu vân tay làm nhãn để duy trì một số hình thức phủ nhận hợp lý, hoặc ghi rõ ràng `Mật khẩu Wallet` chẳng hạn.



![Image](assets/fr/30.webp)



Danh mục đầu tư passphrase của bạn hiện đã được đăng ký trên Seedkeeper.



![Image](assets/fr/31.webp)



Lần tới khi khởi động, chỉ cần lắp Seedkeeper vào ổ đĩa, sau đó điều hướng đến `Seeds > From SeedKeeper`.



![Image](assets/fr/32.webp)



Nhập mã PIN để mở khóa thẻ thông minh, sau đó chọn wallet tương ứng với passphrase của bạn.



![Image](assets/fr/33.webp)



Kiểm tra dấu passphrase và dấu wallet của bạn, sau đó xác nhận.



![Image](assets/fr/34.webp)



Bây giờ bạn có thể truy cập danh mục đầu tư của mình bằng passphrase và ký các giao dịch như bình thường trên SeedSigner.



## 7. Các tùy chọn bổ sung



Trong menu `Công cụ > Công cụ thẻ thông minh`, bạn sẽ tìm thấy một số tùy chọn để quản lý Seedkeeper của mình:





- Trong menu `Công cụ chung`, bạn có thể:
 - Kiểm tra tính xác thực của thẻ;
 - Thay đổi mã PIN;
 - Thay đổi nhãn liên quan đến bí mật của bạn;
 - Tắt chức năng NFC (khuyến nghị nếu chỉ sử dụng đầu đọc chip);
 - Thực hiện khôi phục cài đặt gốc.





- Trong menu `Chức năng SeedKeeper`, bạn có thể:
 - Tham khảo danh sách bí mật đã đăng ký;
 - Lưu một bí mật mới;
 - Xóa bí mật hiện có;
 - Lưu hoặc tải mô tả của bạn (chức năng hữu ích cho danh mục đầu tư multi-sig).





- Trong menu `DIY Tools`, bạn có thể:
 - Biên dịch ứng dụng Seedkeeper;
 - Cài đặt ứng dụng nhỏ trên một thẻ trống;
 - Xóa một applet Seedkeeper để thiết lập lại và làm cho nó trống trở lại.



Bây giờ bạn đã biết cách sử dụng Seedkeeper để sao lưu danh mục đầu tư của mình một cách an toàn khi kết hợp với SeedSigner.



Nếu thiết lập này đã thuyết phục bạn, đừng ngần ngại hỗ trợ các dự án giúp bạn thực hiện được điều đó:




- Bằng cách mua thiết bị trực tiếp [trên trang web Satochip](https://satochip.io/shop/);
- Bằng cách [quyên góp cho dự án SeedSigner](https://seedsigner.com/donate/);
- Bằng cách đăng ký [kênh YouTube của Crypto Guide](https://www.youtube.com/@CryptoGuide/), do người duy trì kho lưu trữ GitHub lưu trữ chương trình cơ sở đã sửa đổi điều hành.