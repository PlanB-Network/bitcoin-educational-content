---
name: NOSTR

description: Khám phá và bắt đầu sử dụng NOSTR
---

Cuối hướng dẫn này, bạn sẽ hiểu Nostr là gì, bạn đã tạo một tài khoản và bạn sẽ có thể sử dụng nó.

![Một thách thức mới đã xuất hiện](assets/1.webp)

## Nostr là gì?

Nostr là một giao thức có khả năng thay thế Twitter, Telegram và các nền tảng truyền thông xã hội khác. Đây là một giao thức mở đơn giản có khả năng tạo ra một mạng xã hội toàn cầu kháng cự một lần và mãi mãi.

## Nó hoạt động như thế nào?

Nostr dựa trên ba thành phần: cặp khóa, khách hàng và relay.

Mỗi người dùng có một hoặc nhiều danh tính, và mỗi danh tính được xác định bởi một cặp khóa mật mã.

Để truy cập vào mạng, bạn cần sử dụng phần mềm khách hàng và kết nối với relay để nhận và truyền tải nội dung.

![Hệ thống khóa](assets/2.webp)

## 1. Khóa Mật Mã

Khác với Facebook hoặc Twitter, nơi người dùng phải cung cấp địa chỉ email và nhiều thông tin cho một công ty tư nhân, Nostr hoạt động mà không cần một cơ quan trung ương. Người dùng tạo ra một cặp khóa mật mã, một khóa bí mật (còn được gọi là khóa riêng) và một khóa công khai.

Khóa bí mật, nsec, chỉ biết bởi người dùng, được sử dụng để xác thực và xuất bản nội dung.

Khóa công khai, npub, là một định danh duy nhất mà tất cả nội dung xuất bản bởi người dùng được gắn kết. Khóa công khai của bạn giống như một tên người dùng cho phép người dùng khác tìm thấy bạn và đăng ký vào nguồn cấp dữ liệu Nostr của bạn.

## 2. Khách Hàng

Khách hàng là phần mềm cho phép tương tác với Nostr. Các khách hàng chính là:

> iOS: damus
> Android: amethyst
> Web: iris.to; snort.social; astral.ninja

Khách hàng cho phép người dùng tạo một cặp khóa mới (tương đương với việc tạo một tài khoản) hoặc xác thực với một cặp khóa đã có.

## 3. Relay

Relay là các máy chủ đơn giản mà bạn có thể bỏ qua bất cứ lúc nào nếu bạn không thích nội dung mà chúng cung cấp cho bạn. Bạn cũng có thể tự chạy relay của mình nếu muốn.

> 💡 Mẹo chuyên nghiệp: Các relay trả phí thường hiệu quả hơn trong việc lọc spam và nội dung không mong muốn.

# Hướng dẫn

Bây giờ bạn đã biết đủ về Nostr để bắt đầu và tạo danh tính đầu tiên của mình trên giao thức này.

Để mục đích của hướng dẫn này, chúng tôi sẽ sử dụng iris.to (https://iris.to/) vì trình khách web này hoạt động trên bất kỳ nền tảng nào.

## Bước 1: Tạo khóa

iris sẽ tạo một bộ khóa cho bạn mà bạn không cần phải làm gì nhiều hơn là nhập một tên (thực hoặc giả) cho hồ sơ của bạn. Sau đó nhấn vào GO và bạn đã xong!

![Menu chính](assets/3.webp)

> ⚠️ Chú ý! Bạn sẽ cần theo dõi khóa của mình nếu bạn muốn có thể truy cập lại hồ sơ của mình một khi phiên làm việc của bạn đã đóng. Tôi sẽ chỉ cho bạn cách làm điều này ở cuối hướng dẫn.

## Bước 2: Xuất bản nội dung

Để xuất bản nội dung, việc này đơn giản và trực quan như viết vài từ trong trường xuất bản.

![Xuất bản](assets/4.webp)

Đó là! Bạn đã xuất bản ghi chú đầu tiên của mình trên Nostr.

![Bài đăng](assets/5.webp)

## Bước 3: Tìm một người bạn

Tìm tôi trên Nostr và không bao giờ cảm thấy cô đơn nữa. Tôi sẽ đăng ký lại với bất kỳ ai đăng ký vào nguồn cấp dữ liệu của tôi. Để làm điều này, chỉ cần nhập khóa công khai của tôi

npub1hartx53w6t3q5wv9xdqdwrk7h6r5866t8u775q0304zedpn5zgssasp7d3 vào thanh tìm kiếm.
![Hồ sơ của tôi](assets/6.webp)
Nhấp vào "theo dõi" và trong vài ngày tối đa, tôi cũng sẽ đăng ký theo dõi bạn. Chúng ta sẽ trở thành bạn bè. Tôi cũng sẽ rất vui khi đọc tin nhắn của bạn nếu bạn muốn viết cho tôi.

Cuối cùng, hãy chắc chắn đăng ký theo dõi Agora256 để nhận thông báo mỗi khi chúng tôi xuất bản điều gì đó mới: npub1ag0rawstycy7nanuc6sz4v287rneen2yapcq3fd06972f8ncrhzqx

## Bước 4: Tùy chỉnh hồ sơ của bạn

Bạn vẫn còn một số công việc phải làm để tùy chỉnh hồ sơ của mình. Để làm điều này, nhấp vào avatar mà iris tự động tạo cho bạn ở góc trên bên phải của màn hình và sau đó nhấp vào "chỉnh sửa hồ sơ".

![Hồ sơ](assets/7.webp)

Bây giờ, tất cả những gì bạn cần làm là cho iris biết nơi tìm thấy hình ảnh và banner hồ sơ của bạn trên internet. Tôi khuyên bạn nên tự lưu trữ nội dung của mình: bảo vệ những gì là của bạn.

![Lựa chọn khác](assets/8.webp)

Nếu bạn muốn, bạn cũng có thể tải lên hình ảnh, chúng sẽ được iris lưu trữ cho bạn trên nostr.build, một dịch vụ lưu trữ nội dung hình ảnh miễn phí cho Nostr.

Như bạn có thể thấy, bạn cũng có thể cấu hình client của mình để có thể nhận và gửi sats. Như vậy, bạn có thể thưởng cho các tác giả của nội dung bạn thích hoặc, tốt hơn nữa, tích lũy sats cho nội dung tuyệt vời mà bạn sẽ xuất bản.

## Bước 5: Sao lưu cặp khóa

Bước này rất quan trọng nếu bạn muốn giữ quyền truy cập vào hồ sơ của mình sau khi bạn đã đăng xuất khỏi client hoặc phiên của bạn đã hết hạn.
Đầu tiên, nhấp vào biểu tượng "cài đặt" được biểu diễn bằng một bánh răng
![Cài đặt](assets/9.webp)

Sau đó, sao chép và dán từng cái một npub, npub hex, nsec, và nsec hex vào một tệp văn bản mà bạn sẽ giữ an toàn. Tôi khuyên bạn nên mã hóa tệp này nếu bạn biết cách làm điều đó.

![Khóa](assets/10.webp)

> ⚠️ Lưu ý cảnh báo mà iris đưa ra. Trong khi bạn có thể chia sẻ khóa công khai mà không sợ hãi, thì câu chuyện về khóa riêng tư lại khác. Bất kỳ ai có khóa sau sẽ có thể truy cập vào tài khoản của bạn.

## Kết luận

Đó là, em đà điểu nhỏ, bạn đã thực hiện những bước đầu tiên trên Nostr. Bây giờ, bạn sẽ cần phải học cách chạy với tốc độ ánh sáng. Chúng tôi sẽ sớm xuất bản các hướng dẫn sẽ chỉ cho bạn cách quản lý khóa của mình và cách tích hợp lightning vào trải nghiệm Nostr của bạn sử dụng getalby.