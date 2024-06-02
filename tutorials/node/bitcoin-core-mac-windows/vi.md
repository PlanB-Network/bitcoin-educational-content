---
name: Noeud Bitcoin Core (mac & windows)
description: Cài đặt Bitcoin Core trên Mac hoặc Windows
---

Việc cài đặt Bitcoin Core trên máy tính cá nhân của bạn có thể được thực hiện, nhưng không phải là lý tưởng. Nếu bạn không phiền để máy tính của mình hoạt động 24/7, thì điều này sẽ hoạt động tốt. Nếu bạn cần tắt máy tính, việc chờ đợi phần mềm đồng bộ lại mỗi khi bạn bật lại máy sẽ trở nên khó chịu.

Những hướng dẫn này dành cho người dùng Mac hoặc Windows. Người dùng Linux có lẽ sẽ không cần đến sự giúp đỡ của tôi, nhưng hướng dẫn cho Linux rất giống với Mac.

## Bắt Đầu Từ Sạch

Lý tưởng nhất, bạn nên sử dụng một máy tính sạch, một máy không có malware. Ngay cả khi bạn sử dụng ví cứng, malware có thể lừa bạn mất tiền xu.

Bạn có thể hoàn toàn xóa sạch một máy tính cũ và sử dụng nó như một máy tính Bitcoin chuyên dụng, hoặc mua một máy tính/laptop chuyên dụng.

## Ổ Cứng

Bitcoin Core sẽ chiếm khoảng 400 gigabyte dữ liệu trên ổ đĩa của bạn và sẽ tiếp tục tăng lên. Bạn có thể sử dụng ổ đĩa nội bộ, nhưng bạn cũng có thể gắn thêm một ổ đĩa cứng ngoài. Tôi sẽ giải thích cả hai lựa chọn. Lý tưởng nhất, bạn nên sử dụng ổ đĩa trạng thái rắn (SSD). Nếu bạn có một máy tính cũ, có lẽ nó không có SSD bên trong. Chỉ cần mua một ổ SSD ngoài 1 hoặc 2 terabyte và sử dụng nó. Ổ đĩa thông thường có lẽ sẽ hoạt động, nhưng bạn có thể gặp phải vấn đề và nó sẽ chậm hơn nhiều.

![image](assets/1.webp)

## Tải xuống Bitcoin Core

Truy cập bitcoin.org (đảm bảo bạn không truy cập vào bitcoin.com, đó là một trang web shitcoin do Roger Ver sở hữu, lừa mọi người mua Bitcoin Cash thay vì Bitcoin)

Một khi bạn đã ở đó, không rõ ràng lắm về việc tìm phần mềm. Đi đến menu tài nguyên và nhấp vào “Bitcoin Core”, như hình dưới đây:

![image](assets/2.webp)

Điều này sẽ đưa bạn đến trang tải xuống:

![image](assets/3.webp)

Nhấp vào nút màu cam Download Bitcoin Core:

![image](assets/4.webp)

Có một số lựa chọn để chọn lựa, tùy thuộc vào máy tính của bạn. Hai lựa chọn đầu tiên liên quan đến hướng dẫn này; chọn Windows hoặc Mac trên thanh bên trái. Việc tải xuống sẽ bắt đầu sau khi bạn nhấp vào, hầu hết là vào thư mục Downloads.

## Xác minh tải xuống (phần 1)

Bạn cần tệp chứa các hash của các bản phát hành khác nhau. Tệp này trước đây nằm trên trang tải xuống của bitcoin.org, nhưng giờ đã chuyển sang bitcoincore.org/en/download:

![image](assets/5.webp)

Bạn cần tệp hash nhị phân SHA256. Tệp này chứa các hash SHA256 của các gói tải xuống khác nhau của Bitcoin Core.

Tiếp theo, chúng ta cần hash tải xuống Bitcoin Core và so sánh nó với những gì tệp nói hash nên là. Sau đó, chúng ta biết tải xuống giống hệt như mong đợi, theo bitcoincore.org.

Di chuyển đến thư mục Downloads một lần nữa và thực hiện lệnh này (thay thế X’s bằng tên tệp tải xuống bitcoin node đầy đủ chính xác):

```bash
shasum -a 256 XXXXXXXXXXXX # <--- CHO MAC
certutil -hashfile XXXXXXXXXXX SHA256 # <--- CHO WINDOWS
```

Bạn sẽ nhận được một đầu ra hash. Ghi chú lại nó và so sánh nó với hash trong tệp SHA256SUMS.

Nếu các đầu ra giống nhau, thì bạn đã xác minh rằng không có bit dữ liệu nào bị thay đổi... gần như vậy. Chúng ta vẫn cần chắc chắn rằng tệp SHA256SUMS không phải là độc hại.

Để tiếp tục với bước tiếp theo, chúng ta phải có gpg được cài đặt trên máy tính của mình.
Để làm điều đó, xem hướng dẫn SHA256/gpg của tôi, và cuộn khoảng nửa trang đến phần "Tải xuống gpg", và tìm tiêu đề phụ của hệ điều hành của bạn. Sau đó quay lại đây.
## Lấy Khóa Công Khai

Quay lại trang tải xuống, lấy tệp chữ ký băm SHA256

![hình ảnh](assets/6.webp)

Nhấp vào và lưu tệp vào đĩa, ưu tiên là thư mục Tải xuống.

Tệp này chứa chữ ký của nhiều người, của tệp SHA256SUMS.

Chúng ta muốn khóa công khai của nhà phát triển chính, Wladimir J. van der Laan trên móc khóa máy tính của chúng ta. ID khóa công khai của ông là:
1 - 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964

Sao chép văn bản đó vào lệnh sau:

```bash
gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys 01EA5486DE18A882D4C2684590C8019E36C2E964
```

Nếu bạn quan tâm, bất cứ lúc nào, bạn có thể xem những khóa nào có trong móc khóa máy tính với lệnh này:

```bash
gpg --list-keys
```

## Xác minh tải xuống (phần 2)

Chúng ta có khóa công khai, vì vậy bây giờ chúng ta có thể xác minh tệp SHA256SUMS chứa các băm của tải xuống Bitcoin Core, và chữ ký cho những băm đó.

Mở Terminal hoặc CMD lại, và đảm bảo bạn đang ở trong thư mục Tải xuống. Từ đó, thực hiện lệnh này:

```bash
gpg –verify SHA256SUMS.asc SHA256SUMS
```

Tệp được liệt kê đầu tiên là chính tả chính xác của tệp chữ ký. Tệp được liệt kê thứ hai nên là chính tả chính xác của tệp văn bản chứa các băm. Cả hai tệp nên ở trong cùng một thư mục và bạn cần ở trong thư mục của các tệp, nếu không, bạn phải gõ đường dẫn đầy đủ cho mỗi tệp.

Đây là kết quả bạn nên nhận được

![hình ảnh](assets/7.webp)

Bạn có thể bỏ qua thông báo CẢNH BÁO – đó chỉ là nhắc nhở bạn rằng bạn chưa gặp Wladimir tại một phần quan trọng và hỏi ông ấy về khóa công khai của mình, sau đó nói với máy tính của bạn để tin tưởng hoàn toàn vào khóa này.

Nếu bạn nhận được thông báo này, bạn bây giờ biết rằng tệp SHA256SUMS.asc không bị can thiệp sau khi Wladimir ký vào nó.

## Cài đặt Bitcoin Core

Bạn không nên cần hướng dẫn chi tiết về cách cài đặt chương trình.

![hình ảnh](assets/8.webp)

## Chạy Bitcoin Core

Trên Mac, bạn có thể nhận được cảnh báo (Apple vẫn chống lại Bitcoin)

![hình ảnh](assets/9.webp)

Nhấp OK, sau đó mở Tùy chọn Hệ thống của bạn

![hình ảnh](assets/10.webp)

Nhấp vào biểu tượng Bảo mật và Quyền riêng tư:

![hình ảnh](assets/11.webp)

Sau đó nhấp vào "mở bất kể thế nào":

![hình ảnh](assets/12.webp)

Lỗi sẽ xuất hiện lại, nhưng lần này bạn sẽ có một nút MỞ. Nhấp vào nó.

![hình ảnh](assets/13.webp)

Bitcoin Core sẽ được tải và bạn sẽ được trình bày một số tùy chọn:

![hình ảnh](assets/14.webp)

Ở đây bạn có thể chọn sử dụng đường dẫn mặc định cho nơi blockchain sẽ được tải xuống, hoặc bạn có thể chọn ổ đĩa ngoài của mình. Tôi khuyên bạn không thay đổi đường dẫn mặc định nếu bạn sẽ sử dụng ổ đĩa nội bộ, nó làm cho việc thiết lập dễ dàng hơn khi bạn cài đặt phần mềm khác để giao tiếp với Bitcoin Core.
Bạn có thể chọn chạy một node đã được cắt tỉa, điều này giúp tiết kiệm không gian, nhưng hạn chế những gì bạn có thể làm với node của mình. Dù bạn chọn cách nào, bạn vẫn sẽ tải xuống toàn bộ blockchain và xác minh nó, vì vậy nếu bạn có đủ không gian, hãy giữ lại những gì bạn đã tải xuống và không cắt tỉa nếu bạn có thể tránh được.

Khi bạn xác nhận, blockchain sẽ bắt đầu được tải xuống. Quá trình này có thể mất nhiều ngày.

![hình ảnh](assets/15.webp)

Bạn có thể tắt máy tính và quay lại để tiếp tục tải xuống nếu bạn muốn, điều này không gây hại gì.