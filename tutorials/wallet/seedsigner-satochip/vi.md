---
name: Satochip x SeedSigner
description: Làm thế nào để sử dụng Satochip với SeedSigner của bạn?
---

![cover](assets/cover.webp)



*Cảm ơn [Crypto Guide](https://www.youtube.com/@CryptoGuide/) vì fork của phần mềm SeedSigner hỗ trợ thẻ thông minh mà chúng tôi sẽ sử dụng trong hướng dẫn này



---

Satochip là phần cứng định dạng thẻ thông minh wallet với thành phần bảo mật được chứng nhận EAL6+, một trong những tiêu chuẩn bảo mật cao nhất. Sản phẩm được thiết kế và sản xuất bởi công ty Bỉ cùng tên: Satochip.



Với mức giá khoảng 25 euro, Satochip nổi bật so với các đối thủ cạnh tranh nhờ giá trị vượt trội. Nhờ chip bảo mật, sản phẩm có khả năng chống lại các cuộc tấn công vật lý. Hơn nữa, mã nguồn applet của nó hoàn toàn là mã nguồn mở, được cấp phép theo *AGPLv3*.



Mặt khác, định dạng của nó đặt ra một số hạn chế về chức năng. Nhược điểm chính của Satochip là không có màn hình tích hợp: do đó, người dùng phải ký giao dịch một cách mù quáng, hoàn toàn dựa vào màn hình máy tính.



Để khắc phục điểm yếu này, một cấu hình đặc biệt thú vị là sử dụng nó kết hợp với SeedSigner. Trong thiết lập này, giao tiếp không còn diễn ra trực tiếp giữa máy tính và Satochip nữa, mà thông qua trao đổi mã QR giữa máy tính và SeedSigner. SeedSigner sau đó hoạt động như một màn hình tin cậy: nó hiển thị thông tin cần ký, trong khi chữ ký được thực hiện bởi Satochip. Không giống như việc sử dụng SeedSigner thông thường (hoặc thậm chí kết hợp với Seedkeeper), seed không bao giờ được tải vào SeedSigner. Do đó, SeedSigner trở thành màn hình của Satochip, loại bỏ các rủi ro liên quan đến việc ký ẩn.



Nếu chúng ta nhìn vấn đề theo hướng ngược lại, việc sử dụng SeedSigner với Satochip sẽ lấp đầy một khoảng trống lớn trong SeedSigner: khả năng lưu trữ và sử dụng seed trong secure element.



Theo tôi, cấu hình này mang lại một số lợi thế so với ví phần cứng thông thường:




- Satochip có giá khoảng 25 euro, và vì applet này là mã nguồn mở, bạn có thể tự cài đặt nó trên một thẻ thông minh trống. Sau đó, bạn cần cộng thêm chi phí cho các thành phần SeedSigner và phần mở rộng để đọc thẻ thông minh: tùy thuộc vào nơi bạn mua phần cứng này, tổng chi phí sẽ dao động từ 70 đến 100 euro.
- Tất cả phần mềm liên quan đến quá trình thiết lập đều là mã nguồn mở: chương trình cơ sở SeedSigner và ứng dụng Satochip.
- Bạn được hưởng lợi từ yếu tố bảo mật được chứng nhận.
- Việc cấu hình có thể được thực hiện hoàn toàn tự động, không cần sử dụng phần cứng được thiết kế riêng cho Bitcoin, điều này có thể cung cấp một hình thức phủ nhận hợp lý và khả năng chống lại một số mối đe dọa bên ngoài (bao gồm cả áp lực từ nhà nước, tùy thuộc vào quốc gia). Đây cũng là một giải pháp thú vị nếu việc truy cập vào ví phần cứng thương mại bị hạn chế hoặc không thể thực hiện được ở khu vực của bạn.




## 1. Vật liệu cần thiết



Để thực hiện thiết lập này, bạn sẽ cần những mục sau:




- Thiết bị thông thường cần có của một SeedSigner cổ điển:
 - một Raspberry Pi Zero với các chân GPIO,
 - Màn hình Waveshare 1,3",
 - một máy ảnh tương thích,
 - một thẻ nhớ microSD.



![Image](assets/fr/01.webp)





- Bộ mở rộng SeedSigner, có sẵn [tại cửa hàng Satochip chính thức](https://satochip.io/product/seedsigner-extension-kit/), cho phép bạn đọc và ghi vào thẻ thông minh trực tiếp từ SeedSigner. Một lựa chọn khác là sử dụng [đầu đọc thẻ thông minh ngoài](https://satochip.io/product/chip-card-reader/), có thể kết nối bằng cáp với cổng Micro-USB trên Raspberry Pi. Tuy nhiên, tôi chưa tự mình thử nghiệm giải pháp này;
- [Một Satochip](https://satochip.io/product/satochip/), hoặc một [thẻ thông minh trống](https://satochip.io/product/card-for-diy-project/) để cài đặt ứng dụng Satochip (bộ mở rộng do Satochip bán đã bao gồm một thẻ thông minh trống). Bộ mở rộng của Satochip cũng hỗ trợ định dạng [SIM JavaCard](https://satochip.io/product/blank-sim-javacard-for-diy-project/). Vì vậy, bạn có thể chọn định dạng này nếu muốn.



![Image](assets/fr/02.webp)



Để biết thêm chi tiết về thiết bị cần thiết để lắp ráp SeedSigner, vui lòng tham khảo Phần 1 của hướng dẫn khác này:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 2. Cài đặt chương trình cơ sở



Để sử dụng SeedSigner với Satochip, bạn cần cài đặt một firmware thay thế, khác với firmware của SeedSigner gốc, để hỗ trợ đọc thẻ thông minh. Để làm được điều này, [tôi khuyên bạn nên sử dụng fork từ "**3rdIteration**"](https://github.com/3rdIteration/seedsigner). Tải xuống [phiên bản mới nhất của hình ảnh](https://github.com/3rdIteration/seedsigner/releases) (`.zip`) tương ứng với model Raspberry Pi bạn đang sử dụng.



![Image](assets/fr/03.webp)



Nếu bạn chưa có, hãy tải xuống phần mềm [Balena Etcher] (https://etcher.balena.io/), sau đó thực hiện như sau:




- Cắm thẻ nhớ microSD vào máy tính;
- Khởi chạy Etcher;
- Chọn tệp `.zip` mà bạn vừa tải xuống;
- Chọn thẻ nhớ microSD làm mục tiêu;
- Nhấp vào `Flash!`.



![Image](assets/fr/04.webp)



Chờ cho đến khi quá trình hoàn tất: thẻ nhớ microSD của bạn đã sẵn sàng để sử dụng. Bây giờ bạn có thể chuyển sang lắp ráp thiết bị.



Để biết thêm chi tiết về cài đặt chương trình cơ sở và xác minh phần mềm (một bước tôi thực sự khuyên bạn nên thực hiện), hãy xem hướng dẫn sau:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 3. Lắp ráp đầu đọc thẻ thông minh



Bắt đầu bằng cách lắp camera vào Raspberry Pi Zero, cẩn thận lắp camera vào chân camera và khóa bằng chốt màu đen. Sau đó, đặt Pi xuống đáy hộp, đảm bảo các cổng được căn chỉnh với các lỗ tương ứng.



![Image](assets/fr/05.webp)



Sau đó, gắn đầu đọc thẻ thông minh vào chân GPIO của Raspberry Pi Zero.



![Image](assets/fr/06.webp)



Trượt nắp nhựa vào đầu đọc thẻ thông minh cho đến khi nắp được đặt đúng vị trí.



![Image](assets/fr/07.webp)



Sau đó thêm màn hình vào các chân GPIO của phần mở rộng.



![Image](assets/fr/08.webp)



Cuối cùng, lắp thẻ nhớ microSD chứa chương trình cơ sở vào cổng bên hông của Raspberry Pi Zero.



![Image](assets/fr/09.webp)



Bây giờ bạn có thể kết nối SeedSigner qua cổng Micro-USB của Raspberry Pi Zero hoặc qua cổng USB-C của bộ mở rộng. Cả hai tùy chọn đều hoạt động. Chờ vài giây để khởi động, sau đó bạn sẽ thấy màn hình chào mừng xuất hiện.



![Image](assets/fr/10.webp)



Để biết thêm chi tiết về cách thiết lập ban đầu cho SeedSigner, tôi khuyên bạn nên tham khảo phần 4 của hướng dẫn sau:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb


## 4. Nạp thẻ thông minh bằng ứng dụng Satochip (tùy chọn)



Nếu bạn đã sở hữu Satochip, bạn có thể bỏ qua bước này và chuyển thẳng đến bước 4. Trong phần này, chúng ta sẽ xem xét cách cài đặt applet Satochip trên thẻ thông minh trống (phương pháp tự làm). Applet này chỉ đơn giản là một chương trình nhỏ chạy trên thẻ thông minh, cho phép chúng ta quản lý các chức năng cụ thể.



Để bắt đầu, hãy mở menu `Công cụ > Công cụ thẻ thông minh` trên SeedSigner của bạn.



![Image](assets/fr/11.webp)



Sau đó chọn `DIY Tools > Install Applet`.



![Image](assets/fr/12.webp)



Cắm thẻ thông minh vào đầu đọc SeedSigner, mặt chip hướng xuống dưới và chọn ứng dụng `Satochip`.



![Image](assets/fr/13.webp)



Hãy kiên nhẫn trong quá trình cài đặt: quá trình này có thể mất vài chục giây.



![Image](assets/fr/14.webp)



Sau khi cài đặt thành công applet, bạn có thể tiến hành bước 4.



![Image](assets/fr/15.webp)




## 5. Tạo và lưu seed



### 5.1. Tạo seed



Bây giờ, khi tất cả phần cứng và phần mềm đã hoạt động bình thường, bạn có thể tiến hành tạo danh mục đầu tư Bitcoin. Để thực hiện, hãy cắm SeedSigner vào, sau đó generate vào seed như với SeedSigner thông thường, bằng cách tung xúc xắc hoặc chụp ảnh:




- Vào menu `Công cụ > Máy ảnh / Cuộn xúc xắc`;
- Sau đó thực hiện quá trình tạo entropy theo phương pháp đã chọn;
- Cuối cùng, hãy sao lưu seed vào phương tiện vật lý và kiểm tra bản sao lưu cẩn thận.



![Image](assets/fr/16.webp)



Nếu bạn muốn xem chi tiết về quy trình này, vui lòng làm theo phần 5 của hướng dẫn này:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

### 5.2. Lưu seed trên Seedkeeper



Sau khi seed được tạo ra, đây là lần duy nhất nó nằm trong RAM của SeedSigner. Trong trường hợp của tôi, tôi muốn lưu nó trên [Seedkeeper](https://satochip.io/product/seedkeeper/), một sản phẩm khác của Satochip được thiết kế để lưu trữ bí mật. Tôi sẽ sử dụng thiết bị này như một phương án cuối cùng, trong trường hợp Satochip của tôi bị mất.



Chiến lược sao lưu được chọn ở đây tùy thuộc vào sở thích của bạn, nhưng điều bắt buộc là phải có ít nhất một bản sao của cụm từ ghi nhớ, trên phương tiện vật lý (giấy hoặc kim loại) hoặc, như ở đây, trong Seedkeeper. Bạn cũng có thể nhân số lượng bản sao lưu tùy theo nhu cầu. Để biết thêm thông tin về các chiến lược sao lưu danh mục đầu tư, tôi khuyên bạn nên đọc hướng dẫn này:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Để sao lưu seed của bạn trên Seedkeeper, hãy vào trực tiếp menu `Sao lưu hạt giống`.



![Image](assets/fr/17.webp)



Sau đó, lắp Seedkeeper vào đầu đọc thẻ thông minh và chọn `Đến SeedKeeper`.



![Image](assets/fr/18.webp)



Nhập mã PIN để mở khóa.



![Image](assets/fr/19.webp)



Chọn một `Nhãn` để dễ dàng nhận dạng các bí mật khác nhau của bạn được lưu trữ trên Seedkeeper. Ví dụ: bạn có thể chỉ giữ nguyên dấu ấn wallet hoặc chỉ rõ `Seed`. Lựa chọn tùy thuộc vào sở thích và mức độ rủi ro của bạn.



![Image](assets/fr/20.webp)



Nếu chiến lược sao lưu của bạn chỉ dựa vào Seedkeeper này, tôi thực sự khuyên bạn nên chạy thử nghiệm khôi phục trống ngay bây giờ, sau đó so sánh dấu vân tay để kiểm tra xem bản sao lưu có hoạt động không.



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

Mã PIN của Seedkeeper nên càng dài và ngẫu nhiên càng tốt để ngăn chặn các nỗ lực tấn công bằng vũ lực trong trường hợp thẻ bị xâm phạm vật lý. Bạn cũng nên lưu trữ một bản sao lưu của mã PIN này ở một vị trí riêng biệt với Seedkeeper. Nếu không có mã PIN này, bạn sẽ không thể truy cập mã ghi nhớ được lưu trữ trong Seedkeeper và số bitcoin của bạn sẽ bị mất vĩnh viễn.



### 5.3. Lưu seed trên Satochip



Bây giờ danh mục đầu tư của bạn đã được tạo, lưu và xác minh, chúng tôi sẽ chuyển nó sang Satochip. Để thực hiện việc này, hãy đảm bảo seed đã được tải vào RAM của SeedSigner. Sau đó, vào `Công cụ > Công cụ Thẻ thông minh > Chức năng Satochip`.



![Image](assets/fr/21.webp)



Cắm Satochip vào đầu đọc thẻ thông minh, sau đó chọn `Khởi tạo bằng Seed`.



![Image](assets/fr/22.webp)



Thiết bị sẽ nhắc bạn nhập mã PIN Satochip; vì thẻ mới và chưa được khởi tạo nên chưa có mã PIN. Hãy nhập bất kỳ mã PIN nào để bỏ qua bước này (không phải mã chặn).



![Image](assets/fr/23.webp)



SeedSigner phát hiện Satochip của bạn chưa được khởi tạo. Nhấp vào `Tôi hiểu` để xác nhận.



![Image](assets/fr/24.webp)



Sau đó, bạn có thể đặt mã PIN Satochip, từ 4 đến 16 ký tự. Để tăng cường bảo mật cho wallet, hãy chọn một mã dài và ngẫu nhiên: đây là biện pháp bảo vệ duy nhất chống lại việc truy cập vật lý vào cụm từ ghi nhớ của bạn.



Hãy nhớ lưu mã PIN này ngay sau khi tạo, có thể là trong trình quản lý mật khẩu an toàn hoặc trên phương tiện vật lý, tùy thuộc vào chiến lược cá nhân của bạn. Trong trường hợp thứ hai, hãy đảm bảo không bao giờ lưu trữ phương tiện chứa mã PIN ở cùng nơi với Satochip của bạn, nếu không việc bảo vệ sẽ trở nên vô dụng. Điều quan trọng là phải có bản sao lưu: **Nếu không có mã PIN này, bạn sẽ không thể truy cập seed của mình và số bitcoin của bạn sẽ bị mất vĩnh viễn**.



![Image](assets/fr/25.webp)



Sau đó, SeedSigner sẽ hỏi bạn muốn nhập seed nào vào Satochip. Hãy chọn seed có dấu vân tay trùng khớp với danh mục đầu tư bạn vừa tạo.



![Image](assets/fr/26.webp)



seed của bạn hiện đã được nhập vào Satochip.



![Image](assets/fr/27.webp)



Bây giờ bạn có thể tắt SeedSigner.



Nếu bạn muốn sử dụng passphrase BIP39 để tăng cường bảo mật cho wallet, vui lòng xem phần 6 của hướng dẫn này:



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 6. Nhập wallet vào Sparrow



Bây giờ danh mục đầu tư của bạn đã được thiết lập và vận hành, chúng tôi sẽ nhập thông tin công khai của nó ("*keystore*") vào Sparrow Wallet hoặc một phần mềm quản lý danh mục đầu tư khác. Phần mềm này sẽ được sử dụng để tạo, phân phối và theo dõi các giao dịch của bạn. Tuy nhiên, nó sẽ không thể ký chúng, vì chỉ Satochip (và bất kỳ bản sao lưu nào) mới nắm giữ khóa riêng cần thiết cho thao tác này.



### 6.1 Chuẩn bị SeedSigner và Satochip



Lắp thẻ nhớ microSD chứa hệ điều hành vào, sau đó bật SeedSigner. Hiện tại, nó chưa thể làm gì được vì chưa nhận diện được seed của bạn. Bạn sẽ phải bắt đầu bằng cách lắp Satochip vào đầu đọc thẻ thông minh, vì đó là đầu đọc đang chứa seed của bạn.



Từ màn hình chính, truy cập menu `Công cụ > Công cụ thẻ thông minh > Chức năng Satochip`.



![Image](assets/fr/28.webp)



Sau đó nhấp vào `Xuất Xpub`.



![Image](assets/fr/29.webp)



Chọn loại danh mục đầu tư. Trong trường hợp này, đó là danh mục đầu tư đơn lẻ: chọn `Single Sig`.



![Image](assets/fr/30.webp)



Tiếp theo là lựa chọn chuẩn kịch bản. Chọn phiên bản mới nhất: `Native SegWit`.



![Image](assets/fr/31.webp)



Cuối cùng, chọn `Coordinator`, tức là phần mềm quản lý danh mục đầu tư bạn muốn sử dụng. Ở đây, chúng tôi sẽ sử dụng Sparrow Wallet.



![Image](assets/fr/32.webp)



Một thông báo cảnh báo xuất hiện: điều này hoàn toàn bình thường. Khóa công khai mở rộng (`xpub`) cho phép bạn xem tất cả các địa chỉ được lấy từ seed của bạn (trên tài khoản đầu tiên). Tuy nhiên, nó không cho phép bạn truy cập vào tiền của mình: việc tiết lộ khóa này sẽ làm ảnh hưởng đến quyền riêng tư của bạn, nhưng không ảnh hưởng đến tính bảo mật của bitcoin. Nói cách khác, nó cho phép bạn theo dõi số dư, nhưng không cho phép bạn chi tiêu chúng.



Nhấp vào `Tôi hiểu`.



![Image](assets/fr/33.webp)



Sau đó nhập mã PIN của Satochip để mở khóa. Đây là mã bạn đã xác định và lưu ở bước 5.



![Image](assets/fr/34.webp)



Cuối cùng, nhấp vào `Xuất Xpub` nếu bạn hài lòng với thông tin hiển thị.



![Image](assets/fr/35.webp)



Sau đó, SeedSigner sẽ tạo xpub của bạn dưới dạng mã QR động, chứa tất cả dữ liệu bạn cần để quản lý danh mục đầu tư của mình trong Sparrow Wallet. Bạn có thể điều chỉnh độ sáng màn hình bằng cần điều khiển để quét mã QR dễ dàng hơn.



### 6.2 Nhập danh mục đầu tư mới vào Sparrow Wallet



Hãy đảm bảo phần mềm Sparrow Wallet đã được cài đặt trên máy tính của bạn. Nếu bạn không biết cách tải xuống, hãy kiểm tra tính xác thực và cài đặt đúng cách, hãy xem hướng dẫn đầy đủ của chúng tôi về chủ đề này:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Trên máy tính của bạn, hãy mở Sparrow Wallet, sau đó trên thanh menu, nhấp vào `File → Import Wallet`.



![Image](assets/fr/36.webp)



Cuộn xuống `SeedSigner`, sau đó chọn `Quét...`. Webcam của bạn sẽ được kích hoạt: quét mã QR động hiển thị trên màn hình SeedSigner.



![Image](assets/fr/37.webp)



Đặt tên cho danh mục đầu tư của bạn, sau đó nhấp vào `Tạo Wallet`. Sau đó, Sparrow sẽ yêu cầu bạn đặt mật khẩu để khóa quyền truy cập cục bộ vào wallet này. Hãy chọn một mật khẩu mạnh: mật khẩu này sẽ bảo vệ dữ liệu của bạn trong Sparrow (khóa công khai, địa chỉ, nhãn và lịch sử giao dịch). Tuy nhiên, mật khẩu này không bắt buộc để khôi phục wallet trong tương lai: chỉ cần cụm từ ghi nhớ của bạn (và có thể cả passphrase) là được.



Tôi khuyên bạn nên lưu mật khẩu này trong trình quản lý mật khẩu để tránh bị mất.



![Image](assets/fr/38.webp)



Kho khóa của bạn đã được nhập thành công.



![Image](assets/fr/39.webp)



Bây giờ hãy kiểm tra xem `Dấu vân tay chính` hiển thị trong Sparrow Wallet có khớp với dấu vân tay trước đó được tìm thấy trên SeedSigner của bạn không.



Sau đó, SeedSigner sẽ yêu cầu bạn quét một địa chỉ nhận ngẫu nhiên từ Sparrow wallet của bạn để xác nhận tính hợp lệ của lệnh nhập.



![Image](assets/fr/40.webp)



Satochip (thông qua SeedSigner) và Sparrow Wallet của bạn hiện đã được kết nối an toàn. Sparrow hoạt động như một giao diện quản lý hoàn chỉnh, trong khi Satochip vẫn là thiết bị duy nhất có khả năng ký các giao dịch của bạn. Giờ đây, bạn đã sẵn sàng nhận và gửi bitcoin trong cấu hình hoàn toàn không kết nối mạng.



![Image](assets/fr/41.webp)



## 7. Nhận và gửi bitcoin



Satochip và Sparrow Wallet của bạn hiện đã được cấu hình để hoạt động cùng nhau. Trong phần này, chúng tôi sẽ hướng dẫn từng bước cách nhận và gửi bitcoin ở chế độ này.



### 7.1 Nhận bitcoin



#### 7.1.1 Tạo địa chỉ tiếp nhận



Trên máy tính, hãy mở Sparrow Wallet và mở khóa `Satochip-SeedSigner` wallet bằng mật khẩu của bạn. Kiểm tra xem phần mềm đã được kết nối với máy chủ chưa (chỉ báo ở góc dưới bên phải). Sau đó, trong thanh bên, nhấp vào `Nhận`.



![Image](assets/fr/42.webp)



Một địa chỉ Bitcoin mới sẽ xuất hiện. Bạn sẽ thấy:




- Địa chỉ ở định dạng văn bản (bắt đầu bằng `bc1q...` nếu bạn đang sử dụng P2WPKH, như trong ví dụ này);
- Mã QR liên quan;
- Trường `Nhãn` hữu ích để theo dõi các giao dịch của bạn.



Tôi thực sự khuyên bạn nên thêm nhãn vào mỗi biên lai Bitcoin trong wallet của mình. Điều này sẽ giúp bạn dễ dàng xác định nguồn gốc của mỗi UTXO và quản lý quyền riêng tư tốt hơn. Để tìm hiểu thêm về chủ đề quan trọng này, hãy xem khóa đào tạo chuyên sâu tại Plan₿ Academy:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Để thêm nhãn, chỉ cần nhập tên vào trường `Nhãn`, sau đó xác nhận.



Ví dụ:



```txt
Label : Sale of the Raspberry Pi Zero
```



Địa chỉ của bạn hiện được liên kết với nhãn này trong tất cả các phần Sparrow.



![Image](assets/fr/43.webp)



#### 7.1.2 Xác minh Address trên SeedSigner



Trước khi cung cấp địa chỉ nhận cho người thanh toán, điều quan trọng là phải kiểm tra xem địa chỉ đó có thuộc về seed của bạn hay không. Bước này đảm bảo Satochip của bạn có thể ký các giao dịch liên quan đến địa chỉ này. Nó cũng ngăn chặn các cuộc tấn công tiềm ẩn mà Sparrow có thể hiển thị địa chỉ giả mạo. Lưu ý rằng Sparrow chạy trên một môi trường không an toàn (máy tính của bạn), nơi có bề mặt tấn công lớn hơn nhiều so với Satochip của bạn, vốn hoàn toàn bị cô lập. Đây là lý do tại sao bạn không bao giờ nên tin tưởng mù quáng vào các địa chỉ được hiển thị trong Sparrow trước khi kiểm tra chúng trên phần cứng wallet của bạn.



Trong Sparrow, hãy nhấp vào mã QR của địa chỉ để phóng to: sau đó mã sẽ được hiển thị toàn màn hình.



![Image](assets/fr/44.webp)



Trên SeedSigner, hãy cắm thẻ Satochip vào đầu đọc, sau đó từ menu chính, chọn `Quét`. Quét mã QR hiển thị trên máy tính, sau đó chọn `Sử dụng thẻ Satochip`.



![Image](assets/fr/45.webp)



Sau đó xác nhận loại tập lệnh được sử dụng (trong trường hợp này là `Native SegWit`), nhập mã PIN Satochip để mở khóa và xác thực thông tin `xpub`.



![Image](assets/fr/46.webp)



Nếu địa chỉ được quét trùng khớp với địa chỉ lấy từ seed của bạn, SeedSigner sẽ hiển thị thông báo: `Address Verified`.



![Image](assets/fr/47.webp)



Sau đó, bạn có thể chắc chắn rằng địa chỉ đó thuộc về danh mục đầu tư của bạn.



#### 7.1.3 Nhận tiền



Bây giờ bạn có thể gửi địa chỉ này dưới dạng văn bản hoặc qua mã QR đến người hoặc bộ phận cần gửi satss cho bạn. Sau khi giao dịch được phát trên mạng, nó sẽ xuất hiện trong tab `Giao dịch` của Sparrow Wallet.



![Image](assets/fr/48.webp)



### 7.2 Gửi bitcoin



Gửi bitcoin bằng cấu hình Satochip-SeedSigner bao gồm 3 bước:




- Tạo giao dịch trong Sparrow;
- Ký giao dịch này trên Satochip, thông qua SeedSigner;
- Cuối cùng, giao dịch được phát qua mạng từ Sparrow.



Mọi trao đổi giữa hai thiết bị đều được thực hiện thông qua mã QR.



#### 7.2.1 Tạo giao dịch trong Sparrow



Trong Sparrow Wallet, bạn có thể tạo giao dịch bằng cách nhấp vào tab `Gửi` ở thanh bên trái. Tuy nhiên, tôi thích sử dụng tab `UTXOs` hơn, cho phép bạn thực hành *Kiểm soát Coin*. Phương pháp này cung cấp khả năng kiểm soát chính xác các UTXO đã chi tiêu, nhằm hạn chế thông tin bị tiết lộ trong quá trình giao dịch.



Trong tab `UTXOs`, hãy chọn loại tiền bạn muốn chi tiêu, sau đó nhấp vào `Gửi loại tiền đã chọn`.



![Image](assets/fr/49.webp)



Sau đó điền vào các trường giao dịch:




- Trong `Thanh toán đến`, hãy dán địa chỉ người nhận hoặc quét mã QR của họ bằng biểu tượng máy ảnh;
- Trong `Nhãn`, thêm nhãn để theo dõi chi phí này;
- Trong `Số tiền`, nhập số tiền cần gửi;
- Cuối cùng, hãy chọn mức phí theo điều kiện mạng hiện tại (có thể tham khảo ước tính tại [mempool.space](https://mempool.space/)).



Sau khi đã hoàn tất mọi trường, hãy xem lại thông tin thật kỹ, sau đó nhấp vào `Tạo giao dịch >>`.



![Image](assets/fr/50.webp)



Kiểm tra lại thông tin chi tiết giao dịch một lần nữa để đảm bảo tính chính xác, sau đó nhấp vào `Hoàn tất giao dịch để ký`.



![Image](assets/fr/51.webp)



Giao dịch hiện đã sẵn sàng, nhưng chưa được ký. Để hiển thị [PSBT (*Partially Signed Bitcoin Transaction*)](https://planb.academy/en/resources/glossary/psbt) dưới dạng mã QR, hãy nhấp vào `Hiển thị QR`.



![Image](assets/fr/52.webp)



#### 7.2.2 Ký giao dịch với Satochip



Bật SeedSigner và lắp Satochip như bình thường. Từ màn hình chính, chọn `Quét`, sau đó quét mã QR hiển thị trên Sparrow.



![Image](assets/fr/53.webp)



Chọn tùy chọn `Sử dụng thẻ Satochip`.



![Image](assets/fr/54.webp)



Nhập mã PIN để mở khóa thẻ thông minh.



![Image](assets/fr/55.webp)



SeedSigner phát hiện đây là PSBT và hiển thị tóm tắt giao dịch:




   - Số tiền đã gửi,
   - Địa chỉ đích,
   - Chi phí giao dịch liên quan.



Nhấp vào `Xem lại Chi tiết` và kiểm tra kỹ lưỡng tất cả thông tin trực tiếp trên màn hình SeedSigner. Những điểm quan trọng nhất cần kiểm tra là số tiền đã gửi, địa chỉ đích và phí giao dịch.



![Image](assets/fr/56.webp)



Nếu mọi thứ đều ổn, hãy chọn `Phê duyệt PSBT` để ký giao dịch bằng Satochip.



![Image](assets/fr/57.webp)



Sau khi chữ ký hoàn tất, SeedSigner sẽ tạo mã QR mới chứa giao dịch đã ký, sẵn sàng để Sparrow quét.



#### 7.2.3 Phát sóng giao dịch từ Sparrow



Bây giờ giao dịch đã được ký và xác thực, việc còn lại là phát nó lên mạng Bitcoin để thợ đào có thể đưa nó vào một khối. Trong Sparrow, nhấp vào `Quét QR`.



![Image](assets/fr/58.webp)



Trình bày mã QR hiển thị trên SeedSigner (mã chứa giao dịch đã ký) cho webcam. Sparrow sẽ hiển thị tất cả thông tin chi tiết về giao dịch. Kiểm tra xem tất cả thông tin đã chính xác chưa, sau đó nhấp vào "Phát sóng giao dịch" để phát sóng trên mạng Bitcoin.



![Image](assets/fr/59.webp)



Giao dịch của bạn hiện đã được truyền đến mạng. Bạn có thể theo dõi xác nhận giao dịch trong tab `Giao dịch` của Sparrow Wallet.



![Image](assets/fr/60.webp)



## 8. Lấy lại wallet của bạn



Như chúng ta đã thấy trong các phần trước, tùy thuộc vào chiến lược bảo mật của bạn, có một số cách để sao lưu cụm từ khôi phục ngoài Satochip của bạn:




- Sử dụng *SeedQR* cổ điển với SeedSigner;
- Bằng cách ghi lại cụm từ ghi nhớ trên một phương tiện vật lý;
- Hoặc bằng cách lưu trữ trên Seedkeeper, như đã giải thích trong phần 5.2.



Trong mọi trường hợp, có 2 tình huống chính mà bạn cần can thiệp: mất Satochip hoặc mất SeedSigner. Hãy cùng xem xét cách phản ứng trong từng tình huống này.



### 8.1. Lấy lại wallet của bạn bằng Satochip



Nếu bạn vẫn còn Satochip nhưng SeedSigner bị hỏng hoặc bị mất, tình huống này khá đơn giản để xử lý vì wallet của bạn vẫn còn trong Satochip.



Lựa chọn tốt nhất là đề xuất các thành phần cần thiết và xây dựng lại SeedSigner mới từ đầu. Vì đây là thiết bị "không trạng thái", nên việc bạn đang sử dụng cùng SeedSigner hay một SeedSigner khác không quan trọng: miễn là bạn có thể lắp Satochip, mọi thứ sẽ hoạt động bình thường.



Nếu bạn không muốn xây dựng lại, bạn cũng có thể sử dụng Satochip theo cách cổ điển, tức là trực tiếp từ máy tính, mà không cần thông qua SeedSigner. Phương pháp này hoạt động hoàn hảo, nhưng nó làm giảm đáng kể tính bảo mật của Bitcoin wallet: bạn mất đi khả năng cách ly "*air-gapped*" và giờ phải ký ẩn, vì SeedSigner hoạt động như một màn hình đáng tin cậy. Tuy nhiên, đây có thể là giải pháp tạm thời trong trường hợp khẩn cấp, hoặc nếu bạn không thể xây dựng lại SeedSigner.



Để thực hiện việc này, bạn cần có thẻ thông minh USB hoặc đầu đọc NFC. Mở wallet mà bạn muốn khôi phục trong Sparrow, sau đó vào tab `Cài đặt` và nhấp vào `Thay thế`.



![Image](assets/fr/61.webp)



Cắm Satochip vào đầu đọc thẻ thông minh được kết nối với máy tính, sau đó nhấp vào `Nhập` bên cạnh `Satochip`.



![Image](assets/fr/62.webp)



Cuối cùng, nhập mã PIN thẻ thông minh để mở khóa. Sau đó, bạn có thể truy cập wallet, tạo giao dịch và ký trực tiếp bằng Satochip được kết nối.



### 8.2. Lấy lại danh mục đầu tư của bạn với SeedSigner



Một tình huống khác, tế nhị hơn, là khi bạn mất quyền truy cập vào Satochip chứa seed: có thể do nó bị hỏng, bị mất, bị đánh cắp hoặc bạn quên mã PIN. Nếu Satochip của bạn bị đánh cắp hoặc thất lạc, chúng tôi đặc biệt khuyến nghị rằng, sau khi khôi phục quyền truy cập vào tiền của bạn, bạn nên ngay lập tức chuyển bitcoin sang một wallet hoàn toàn mới, được tạo bằng một seed khác. Điều này đảm bảo rằng kẻ tấn công tiềm ẩn sẽ không bao giờ có thể truy cập vào satss của bạn.



Để lấy lại quyền truy cập vào danh mục đầu tư và chuyển tiền, chỉ cần tải seed vào SeedSigner. Tùy thuộc vào phương tiện sao lưu bạn đã sử dụng, bạn có một số tùy chọn:





- Nhập thủ công cụm từ ghi nhớ của bạn vào menu `Seeds > Enter 12-word seed`.



![Image](assets/fr/63.webp)





- Quét *SeedQR* của bạn bằng cách nhấp vào nút `Quét` trên trang chủ.



![Image](assets/fr/64.webp)





- Hoặc tải seed từ Seedkeeper, thông qua menu `Seeds > From SeedKeeper` (đây là phương pháp tôi sử dụng trong hướng dẫn này). Bạn chỉ cần nhập mã PIN Seedkeeper và chọn bí mật để sử dụng làm seed trên SeedSigner.



![Image](assets/fr/65.webp)



Sau khi seed được tải vào SeedSigner, bất kể bạn sử dụng phương pháp nào, bạn sẽ có thể ký một hoặc nhiều giao dịch quét để chuyển bitcoin của mình sang wallet mới, chưa bị xâm phạm. Để tìm hiểu cách thực hiện việc này, hãy xem phần 7.2 của hướng dẫn sau:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

Bây giờ bạn đã biết cách sử dụng Satochip để quản lý danh mục đầu tư Bitcoin của mình một cách an toàn khi kết hợp với SeedSigner.



Nếu thiết lập này đã thuyết phục bạn, đừng ngần ngại hỗ trợ các dự án giúp bạn thực hiện được điều đó:




- Bằng cách mua thiết bị trực tiếp [trên trang web Satochip](https://satochip.io/shop/);
- Bằng cách [quyên góp cho dự án SeedSigner](https://seedsigner.com/donate/);
- Bằng cách đăng ký [kênh YouTube của Crypto Guide](https://www.youtube.com/@CryptoGuide/), do người quản lý kho lưu trữ GitHub lưu trữ chương trình cơ sở đã sửa đổi mà chúng tôi sử dụng trong hướng dẫn này điều hành.