---
name: Linux Mint

description: Thiết lập máy tính cho giao dịch bitcoin
---

![image](assets/cover.webp)

## Điều gì sẽ xảy ra nếu bạn sử dụng một máy tính thông thường?

Khi thực hiện giao dịch Bitcoin, lý tưởng nhất là máy tính của bạn không chứa malware. Rõ ràng là như vậy.

Nếu bạn giữ cụm từ khôi phục Bitcoin của mình (thường là 12 hoặc 24 từ) ngoài máy tính với một thiết bị ký (ví dụ, một ví cứng - mục đích chính của nó), thì bạn có thể nghĩ rằng không quá quan trọng phải có một máy tính "sạch" - điều này không đúng.

Một máy tính nhiễm malware có thể đọc được địa chỉ Bitcoin của bạn, làm lộ số dư của bạn cho kẻ tấn công - họ không thể lấy bitcoin chỉ bằng cách biết địa chỉ, nhưng họ có thể thấy bạn có bao nhiêu và tính toán từ đó xem bạn có phải là mục tiêu đáng giá không. Họ cũng có thể tìm ra nơi bạn sống, ví dụ, và ép bạn trả tiền chuộc bằng cách đe dọa hoặc bắt cóc con cái của bạn.

## Giải pháp là gì?

Tôi khuyến khích hầu hết người dùng Bitcoin sử dụng một máy tính riêng biệt không chứa malware (có kết nối internet) để thực hiện giao dịch Bitcoin. Tôi đề xuất mọi người sử dụng một hệ điều hành mã nguồn mở như Linux Mint, nhưng nếu bạn muốn, có thể sử dụng Windows hoặc Mac - điều đó tốt hơn là sử dụng một máy tính thông thường, thường xuyên sử dụng, chắc chắn chứa malware ẩn bên trong.

Một trở ngại mà mọi người thường gặp là việc cài đặt một hệ điều hành mới trên những máy tính này. Hướng dẫn này sẽ giúp bạn vượt qua điều đó.

Có nhiều phiên bản của Linux và tôi đã thử nhiều phiên bản. Đề xuất của tôi dành cho người dùng Bitcoin là Linux Mint, bởi vì nó dễ cài đặt, rất nhanh (đặc biệt khi khởi động và tắt máy), không chứa phần mềm không cần thiết (mỗi phần mềm thêm vào là một rủi ro), và hiếm khi gặp sự cố hoặc hoạt động kỳ lạ (so với các phiên bản khác như Ubuntu và Debian).

Một số người có thể rất kháng cự với một hệ điều hành mới, thích Windows hoặc Mac OS. Tôi hiểu, nhưng hệ điều hành của Windows và Apple là mã nguồn đóng, vì vậy chúng ta phải tin tưởng vào những gì họ đang làm; tôi không nghĩ đó là một chính sách tốt, nhưng không phải là tất cả hoặc không gì cả. Tôi thích hơn nếu mọi người sử dụng một máy tính Windows hoặc Mac OS mới cài đặt riêng biệt thay vì một máy tính đã sử dụng nhiều (với biết bao nhiêu malware đã tích tụ trên đó). Một bước tiến hơn là sử dụng một máy tính Linux mới cài đặt, đó là những gì tôi sẽ trình bày.

Nếu bạn lo lắng về việc sử dụng Linux vì không biết, đó là tự nhiên, nhưng cũng tự nhiên khi dành thời gian để học. Rất nhiều thông tin có sẵn trực tuyến. Đây là một video ngắn xuất sắc giới thiệu về cơ bản của dòng lệnh mà tôi rất khuyến khích.
Chọn một máy tính

Tôi sẽ bắt đầu với lựa chọn tôi nghĩ là tốt nhất. Sau đó, tôi sẽ đưa ra ý kiến của mình về các lựa chọn khác.

Lựa chọn lý tưởng:

Đề xuất của tôi, nếu bạn có khả năng chi trả, và nếu kích thước của số bitcoin của bạn đáng giá, là mua một chiếc laptop cấp thấp mới. Mẫu cơ bản nhất được xây dựng ngày nay đủ tốt để xử lý những gì nó sẽ được sử dụng. Thông số kỹ thuật của bộ xử lý và RAM không quan trọng, bởi vì tất cả đều đủ tốt.

Tránh:

- Bất kỳ sự kết hợp máy tính bảng nào, bao gồm Surface Pro
- Chromebooks – thường dung lượng lưu trữ quá thấp
- Bất kỳ máy tính nào có ổ đĩa eMMC; Nếu nó có ổ đĩa SSD, đó là hoàn hảo
- Macs – chúng đắt đỏ, và phần cứng không tương thích tốt với hệ điều hành Linux theo kinh nghiệm của tôi
- Bất cứ thứ gì đã được tân trang hoặc đã qua sử dụng (không phải là điều không thể chấp nhận được hoàn toàn)

Thay vào đó, hãy tìm một chiếc laptop Windows 11 (Hiện tại Windows 11 là phiên bản mới nhất. Đừng lo, chúng tôi sẽ loại bỏ phần mềm đó.). Tôi đã tìm trên amazon.com với từ khóa “Windows 11 Laptop” và tìm thấy ví dụ tốt này:
![hình ảnh](assets/1.webp)
Giá của chiếc máy này ở trên khá tốt. Cấu hình cũng đủ dùng. Nó có camera tích hợp mà chúng ta có thể sử dụng để giao dịch PSBT bằng mã QR (nếu không bạn sẽ phải mua một camera USB để làm điều đó). Đừng lo lắng về việc nó không phải là một thương hiệu nổi tiếng (nó rẻ). Nếu bạn muốn một thương hiệu tốt hơn, bạn sẽ phải trả thêm tiền, ví dụ:

![hình ảnh](assets/2.webp)

Một số máy tính giá rẻ chỉ có 64Gb dung lượng ổ đĩa; Tôi chưa thử nghiệm laptop với ổ đĩa nhỏ như vậy - có lẽ 64Gb là đủ, nhưng có thể sẽ hơi chật chội.

## Các lựa chọn khác – Tails

Tails là một hệ điều hành khởi động từ ổ USB, và tạm thời kiểm soát phần cứng của bất kỳ máy tính nào. Nó chỉ sử dụng kết nối Tor, vì vậy bạn cần phải thoải mái khi sử dụng Tor. Không có dữ liệu nào bạn ghi vào bộ nhớ trong phiên làm việc được lưu vào ổ đĩa (nó bắt đầu mới mỗi lần) trừ khi bạn chỉnh sửa cài đặt và tạo một tùy chọn lưu trữ vĩnh viễn (trên ổ USB) - mà bạn khóa bằng mật khẩu.

Đây không phải là một lựa chọn tồi và nó miễn phí, nhưng hơi cồng kềnh cho mục đích của chúng ta. Cài đặt phần mềm mới trên nó không phải là dễ dàng. Một tính năng tốt là nó đi kèm với Electrum, nhưng nhược điểm của điều này là bạn không tự cài đặt nó. Đảm bảo rằng ổ USB bạn sử dụng có ít nhất 8Gb.

Sự linh hoạt của bạn sẽ giảm nếu bạn sử dụng Tails. Bạn có thể không thể theo dõi các hướng dẫn để thiết lập những gì bạn cần và làm cho nó hoạt động đúng cách. Ví dụ, nếu bạn theo hướng dẫn của tôi để cài đặt Bitcoin Core, có những chỉnh sửa cần thiết để nó hoạt động. Tôi không nghĩ mình sẽ tạo một hướng dẫn cụ thể cho Tails, vì vậy bạn cần phải xây dựng kỹ năng và tự làm.

Tôi cũng không chắc là ví cứng sẽ tương tác như thế nào với hệ điều hành này.

Nói tất cả những điều này, một máy tính Tails cho giao dịch Bitcoin là một lựa chọn bổ sung tốt, và chắc chắn sẽ giúp kỹ năng bảo mật tổng thể của bạn khi học cách sử dụng Tails.

## Các lựa chọn khác – Khởi động Hệ Điều Hành Trực Tiếp

Điều này rất giống với Tails, ngoại trừ hệ điều hành không tập trung vào quyền riêng tư. Cách cơ bản để sử dụng điều này là ghi một ổ USB với hệ điều hành Linux theo lựa chọn của bạn và khiến máy tính khởi động từ đó thay vì ổ đĩa nội bộ. Cách làm này sẽ được giải thích sau.

Ưu điểm là bạn ít bị hạn chế hơn và mọi thứ sẽ hoạt động mà không cần chỉnh sửa nâng cao.

Tôi không chắc hệ thống như vậy cô lập malware trên máy tính hiện tại khỏi ổ USB khởi động mà bạn sử dụng chứa hệ điều hành mới như thế nào. Có lẽ nó làm tốt công việc và có lẽ không tốt bằng Tails. Vì tôi không biết, sự ưu tiên của tôi là máy tính chuyên dụng.
Các lựa chọn khác – Máy tính cũ của bạn

Sử dụng một máy tính cũ không phải là lý tưởng, chủ yếu vì tôi không biết rõ về cơ chế hoạt động của malware phức tạp, cũng như việc lau ổ đĩa có đủ để loại bỏ nó hay không. Có lẽ là đủ nhưng tôi không muốn đánh giá thấp sự khéo léo của các hacker có ý đồ xấu. Bạn có thể quyết định, tôi không muốn cam kết.

Nếu bạn chọn sử dụng một máy tính để bàn cũ thay vì laptop, điều này sẽ ổn, ngoại trừ việc nó sẽ chiếm dụng không gian vĩnh viễn cho các giao dịch bitcoin có lẽ hiếm hoi của bạn; bạn không nên sử dụng nó cho bất cứ điều gì khác. Trong khi với một laptop, bạn có thể chỉ cất nó đi, và thậm chí ẩn nó đi để tăng cường bảo mật.

## Cài đặt Linux Mint trên bất kỳ máy tính nào
Đây là hướng dẫn để xóa bất kỳ hệ điều hành nào khỏi laptop mới của bạn và cài đặt Linux Mint, nhưng bạn có thể điều chỉnh để cài đặt hầu như bất kỳ phiên bản Linux nào trên hầu như bất kỳ máy tính nào.

Chúng ta sẽ sử dụng một máy tính bất kỳ để ghi hệ điều hành vào một loại ổ nhớ di động nào đó. Không quan trọng loại ổ nhớ nào, miễn là nó tương thích với cổng USB, và tôi đề xuất tối thiểu 16Gb.

Hãy sắm một trong những thứ này:

![hình ảnh](assets/3.webp)

Hoặc bạn có thể sử dụng thứ gì đó như thế này:

![hình ảnh](assets/4.webp)

Tiếp theo, truy cập vào linuxmint.com

![hình ảnh](assets/5.webp)

Di chuyển chuột lên menu Download ở phía trên và sau đó nhấp vào liên kết, “Linux Mint 20.3” hoặc bất kỳ phiên bản nào là mới nhất và được khuyến nghị tại thời điểm bạn thực hiện việc này.

![hình ảnh](assets/6.webp)

Sẽ có một vài “hương vị” để bạn lựa chọn. Chọn “Cinnamon” để theo dõi hướng dẫn này. Nhấp vào nút Download.

![hình ảnh](assets/7.webp)

Trên trang tiếp theo, bạn có thể cuộn xuống để xem các mirror (Mirror là các máy chủ khác nhau chứa bản sao của tệp mà chúng ta muốn). Bạn có thể xác minh việc tải xuống sử dụng SHA256 và gpg (được khuyến nghị), nhưng tôi sẽ bỏ qua việc giải thích điều này ở đây vì tôi đã viết hướng dẫn về điều này rồi.

![hình ảnh](assets/8.webp)

Chọn một mirror gần bạn nhất và nhấp vào liên kết của nó (văn bản màu xanh trong cột mirror). Tệp sẽ bắt đầu được tải xuống - phiên bản tôi đang tải xuống là 2.1 gigabyte.

Một khi nó đã được tải xuống, bạn có thể ghi tệp vào một thiết bị nhớ di động và làm cho nó có thể khởi động được. Cách dễ nhất là sử dụng Balena Etcher. Tải xuống và cài đặt nếu bạn chưa có.

Sau đó chạy nó:

![hình ảnh](assets/9.webp)

Nhấp vào flash from file, và chọn tệp LinuxMint bạn đã tải xuống.

Sau đó nhấp vào Select target. Đảm bảo rằng thiết bị nhớ đã được cắm vào và chắc chắn rằng bạn đang chọn đúng ổ đĩa, nếu không bạn có thể phá hủy nội dung của ổ đĩa sai!

Sau đó, chọn Flash! Bạn có thể cần nhập mật khẩu của mình. Khi hoàn tất, ổ đĩa có thể sẽ không được máy tính Windows hoặc Mac của bạn đọc được vì nó đã được chuyển đổi thành một thiết bị Linux. Chỉ cần rút nó ra.
Chuẩn bị máy tính đích

Bật laptop mới, và trong khi nó đang khởi động, giữ phím BIOS. Thông thường là F2, nhưng cũng có thể là F1, F8, F10, F11, F12 hoặc Delete. Thử từng cái một cho đến khi bạn tìm ra, hoặc tìm trên internet về mẫu máy tính của bạn và đặt câu hỏi đúng.

Ví dụ: “BIOS key Dell laptops”.

Mỗi máy tính sẽ có một menu BIOS khác nhau. Khám phá và tìm menu nào cho phép bạn cấu hình thứ tự khởi động. Đối với mục đích của chúng ta, chúng ta muốn máy tính cố gắng khởi động từ thiết bị kết nối USB (nếu có kết nối), trước khi cố gắng khởi động từ ổ đĩa cứng nội bộ (nếu không Windows sẽ được tải). Một khi bạn đã thiết lập điều đó, bạn có thể cần lưu trước khi thoát hoặc nó có thể tự động lưu.

Khởi động lại máy tính và nó sẽ tải từ thiết bị nhớ USB. Chúng ta có thể cài đặt Linux trên ổ đĩa cứng nội bộ và Windows sẽ được gỡ bỏ hoàn toàn.

Khi bạn đến màn hình sau, chọn “OEM install (dành cho nhà sản xuất)”. Nếu bạn chọn “Start Linux Mint”, bạn sẽ có một phiên Linux Mint được tải từ thiết bị nhớ, nhưng một khi bạn tắt máy tính, không có thông tin nào của bạn được lưu lại – cơ bản đó là một phiên tạm thời để bạn có thể thử nghiệm.
Bạn sẽ được hướng dẫn qua một trình hướng dẫn đồ họa, nơi sẽ đặt bạn một số câu hỏi nên là dễ dàng. Một trong số đó sẽ là cài đặt ngôn ngữ, một khác sẽ là kết nối mạng internet nhà bạn và mật khẩu. Nếu được yêu cầu cài đặt thêm phần mềm, hãy từ chối. Khi bạn đến phần hỏi về loại cài đặt, một số người có thể sẽ do dự - bạn cần chọn “Xóa đĩa và cài đặt Linux Mint”. Ngoài ra, không mã hóa ổ đĩa và không chọn LVM.

Cuối cùng, bạn sẽ đến được màn hình desktop. Tại thời điểm này, bạn chưa hoàn toàn hoàn thành. Thực tế, bạn đang hành động như là nhà sản xuất (tức là ai đó đang lắp ráp máy tính và cài đặt Linux cho khách hàng). Bạn cần nhấp đúp vào biểu tượng trên màn hình desktop, “Cài đặt Linux Mint”, để hoàn tất quá trình.

Nhớ rút ổ nhớ USB, sau đó khởi động lại. Sau khi khởi động lại, bạn sẽ sử dụng hệ điều hành lần đầu tiên như một người dùng mới. Xin chúc mừng.

Một trong những việc đầu tiên cần làm (và thực hiện thường xuyên), là giữ hệ thống được cập nhật.

Mở ứng dụng Terminal, và gõ lệnh sau:

```bash
sudo apt-get update
```

ấn <enter>, xác nhận lựa chọn của bạn, và sau đó là lệnh này:

```bash
sudo apt-get upgrade
```

ấn <enter> và xác nhận lựa chọn của bạn.

Hãy để nó thực hiện, có thể mất vài phút.

Tiếp theo, tôi thích cài đặt Tor (phân biệt chữ hoa chữ thường):

```bash
sudo apt-get install tor
```

> _BỔ SUNG: Bạn cũng có thể chạy khởi động Linux Mint từ “Cài đặt OEM” (Đảm bảo bạn đã kết nối internet, nếu không bạn có thể gặp lỗi). Nếu bạn làm điều này, sau đó bạn cần nhấp vào biểu tượng “gửi đến người dùng cuối” nên có trên màn hình desktop. Sau đó bạn khởi động lại và bắt đầu hệ điều hành như thể bạn đang mở máy tính lần đầu tiên._

Hướng dẫn này giải thích tại sao bạn có thể cần một máy tính dành riêng cho các giao dịch Bitcoin, và cách cài đặt một hệ điều hành Linux Mint mới trên đó.