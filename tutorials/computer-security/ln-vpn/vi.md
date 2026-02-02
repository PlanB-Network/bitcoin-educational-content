---
name: LN VPN

description: Cấu hình LN VPN với Lightning cho một VPN ẩn danh và theo nhu cầu
---

![image](assets/cover.webp)

LN VPN là một dịch vụ VPN có thể tùy chỉnh chỉ chấp nhận thanh toán qua lightning. Hôm nay, tôi sẽ hướng dẫn bạn cách sử dụng nó và để lại ít dấu vết hơn khi duyệt web.

Có nhiều nhà cung cấp dịch vụ VPN chất lượng, nhưng LN VPN nổi bật, và chúng tôi không thể bỏ lỡ cơ hội giới thiệu nó cho bạn.

Hầu hết các nhà cung cấp dịch vụ VPN như ProtonVPN và Mullvad đều cung cấp tùy chọn thanh toán bằng bitcoin nhưng yêu cầu tạo tài khoản và mua gói dịch vụ cho một thời hạn dài hoặc ngắn, có thể không phù hợp với ngân sách của mọi người.

LN VPN cho phép sử dụng VPN theo nhu cầu ngắn hạn như một giờ, nhờ vào việc triển khai thanh toán bitcoin qua mạng lightning. Thanh toán lightning tức thì và ẩn danh, mở ra một thế giới mới của các khoản thanh toán nhỏ.

> 💡 Hướng dẫn này mô tả cách sử dụng LN VPN từ hệ thống Linux Ubuntu 22.04 LTS.

## Yêu cầu: Wireguard

Nói một cách đơn giản, Wireguard được sử dụng để tạo một đường hầm an toàn giữa máy tính của bạn và máy chủ từ xa mà qua đó bạn sẽ duyệt Internet. Địa chỉ IP của máy chủ này sẽ xuất hiện như là của bạn trong suốt thời gian thuê bao mà bạn sẽ ký kết theo hướng dẫn này.

Hướng dẫn cài đặt chính thức của Wireguard: https://www.wireguard.com/install/

```
Cài đặt Wireguard
          $ sudo apt-get update
          $ sudo apt install wireguard
```

## Yêu cầu: Ví Bitcoin Lightning

Nếu bạn chưa có ví Bitcoin Lightning, đừng lo, chúng tôi đã tạo một hướng dẫn rất đơn giản cho bạn tại đây. (phần hướng dẫn LN có thể giúp bạn)

## Bước 1: Ký kết một Hợp đồng Thuê

Từ https://lnvpn.com, bạn sẽ cần chọn quốc gia của địa chỉ IP thoát của đường hầm VPN và thời hạn. Sau khi các tham số này được thiết lập, nhấp vào Thanh toán bằng lightning.

![image](assets/1.webp)

Một hóa đơn lightning sẽ được hiển thị, và bạn chỉ cần quét nó với ví lightning của mình.

Sau khi hóa đơn được thanh toán, bạn sẽ cần chờ đợi vài giây đến hai phút để cấu hình Wireguard của bạn được tạo. Nếu mất một chút thời gian hơn, đừng hoảng sợ, chúng tôi đã thực hiện quy trình này hàng chục lần, và đôi khi nó chỉ mất một chút thời gian hơn.
Màn hình tiếp theo sẽ xuất hiện và bạn chỉ cần nhấp vào "Tải xuống dưới dạng Tệp" để nhận tệp cấu hình của mình, sẽ có tên giống như lnvpn-xx-xx.conf nơi "xx" sẽ tương ứng với ngày hiện tại.
![image](assets/2.webp)

## Bước 2: Kích hoạt đường hầm

Đầu tiên, bạn sẽ cần đổi tên tệp cấu hình thu được ở bước trước để nó có thể được Wireguard tự động nhận diện.

Đi đến thư mục tải xuống của bạn, hoặc trong cửa sổ terminal hoặc với trình quản lý tệp, và đổi tên tệp lnvpn-xx-xx.conf thành wg0.conf như sau:

```
    $ sudo ln -s usrbin/resolvectl usrlocal/bin/resolvconf
    $ sudo wg-quick up ~/Downloads/wg0.conf
```

Đó là! Đường hầm đã được kích hoạt!

## Bước 3: Xác minh

Sử dụng một dịch vụ trực tuyến như whatismyip để xác minh rằng địa chỉ IP công cộng của bạn bây giờ là từ VPN mà bạn vừa kích hoạt.

## Bước 4: Vô hiệu hóa
Khi hợp đồng thuê của bạn hết hạn, bạn sẽ cần vô hiệu hóa kết nối để lấy lại quyền truy cập vào internet. Bạn có thể lặp lại các bước 1 đến 3 bất cứ khi nào bạn muốn thiết lập một hợp đồng thuê với LN VPN.
Vô hiệu hóa đường hầm:

```
    $ sudo ip link delete dev wg0
```

Đó là! Bây giờ bạn đã biết cách sử dụng LN VPN, một dịch vụ VPN độc đáo!