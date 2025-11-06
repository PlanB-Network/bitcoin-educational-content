---
name: BIP-39 Mật khẩu SeedSigner
description: Làm thế nào để thêm passphrase vào danh mục SeedSigner của tôi?
---

![cover](assets/cover.webp)



passphrase BIP39 là mật khẩu tùy chọn, kết hợp với cụm từ gợi nhớ, cung cấp thêm một lớp bảo mật cho ví Bitcoin xác định và phân cấp. Trong hướng dẫn này, chúng ta sẽ cùng nhau khám phá cách thiết lập passphrase trên Bitcoin wallet của bạn khi sử dụng với SeedSigner.



![Image](assets/fr/01.webp)



## Điều kiện tiên quyết trước khi thêm Mật khẩu



Trước khi bắt đầu hướng dẫn này, nếu bạn không quen với khái niệm passphrase, cách thức hoạt động và ý nghĩa của nó đối với Bitcoin wallet của bạn, tôi thực sự khuyên bạn nên tham khảo bài viết lý thuyết khác này, trong đó tôi giải thích mọi thứ (điều này rất quan trọng, vì sử dụng passphrase mà không hiểu đầy đủ cách thức hoạt động của nó có thể khiến bitcoin của bạn gặp rủi ro):



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Trước khi bắt đầu hướng dẫn này, vui lòng đảm bảo bạn đã khởi tạo SeedSigner và tạo cụm từ ghi nhớ. Nếu chưa, và SeedSigner của bạn hoàn toàn mới, hãy làm theo hướng dẫn trên Plan ₿ Academy. Sau khi hoàn thành bước này, bạn có thể quay lại hướng dẫn này:



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## Làm thế nào để thêm passphrase vào SeedSigner?



Việc thêm passphrase vào danh mục đầu tư được quản lý thông qua SeedSigner sẽ tạo ra một danh mục đầu tư hoàn toàn mới, tạo ra một bộ khóa hoàn toàn riêng biệt. Do đó, nếu bạn đã có danh mục đầu tư chứa satss, bạn sẽ không thể truy cập danh mục đó bằng passphrase nữa, vì nó tạo ra một danh mục đầu tư hoàn toàn khác.



Để áp dụng passphrase cho SeedSigner, hãy bật thiết bị và quét SeedQR như bình thường. SeedSigner sau đó sẽ hiển thị dấu vân tay của wallet hiện tại, tương ứng với dấu vân tay **không có passphrase**. wallet có passphrase sẽ có dấu vân tay khác.



Nhấp vào nút `BIP-39 Passphrase`.



![Image](assets/fr/02.webp)



Sau đó, nhập mã passphrase bạn chọn vào ô được cung cấp, sử dụng bàn phím trên màn hình. Hãy đảm bảo tạo một hoặc nhiều bản sao lưu vật lý (giấy hoặc kim loại): việc mất mã passphrase này sẽ dẫn đến mất quyền truy cập vĩnh viễn vào bitcoin của bạn. **Để khôi phục mã wallet, cả mã ghi nhớ và mã passphrase đều cần thiết ** Nếu một trong hai mã bị mất, bitcoin của bạn sẽ bị chặn vĩnh viễn.



Sau khi hoàn tất mục nhập, hãy xác thực bằng cách nhấn nút `KEY3` ở góc dưới bên phải của SeedSigner.



![Image](assets/fr/03.webp)



*Trong ví dụ này, tôi đã sử dụng passphrase `pba`. Tuy nhiên, trong trường hợp của bạn, hãy đảm bảo chọn một passphrase mạnh mẽ. Để tìm hiểu cách xác định passphrase tối ưu, vui lòng tham khảo bài viết khác này:*



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Sau đó, SeedSigner sẽ hiển thị dấu vân tay mới của passphrase wallet. Hãy tạo nhiều bản sao dấu vân tay này: điều này rất quan trọng khi sử dụng wallet với passphrase, vì nó cho phép bạn kiểm tra xem bạn có mắc lỗi nhập liệu nào không và bạn đang truy cập đúng wallet mỗi lần nhập passphrase.



Ví dụ, nếu trong trường hợp của tôi, tôi vô tình viết passphrase `Pba` khi khởi động SeedSigner thay vì `pba`, thì việc thay đổi đơn giản này từ chữ thường sang chữ hoa sẽ tạo ra một danh mục đầu tư hoàn toàn khác với danh mục mà tôi muốn truy cập.



Dấu vân tay này không gây rủi ro cho tính bảo mật của khóa wallet. Nó không tiết lộ bất kỳ thông tin nào, dù công khai hay riêng tư, về khóa của bạn. Vì vậy, không giống như mã ghi nhớ và passphrase, bạn có thể lưu dấu vân tay trên một phương tiện kỹ thuật số. Tôi khuyên bạn nên giữ một bản sao ở nhiều nơi: trên một tờ giấy, trong trình quản lý mật khẩu, v.v.



Sau khi lưu dấu vân tay, hãy nhấp vào `Xong`.



![Image](assets/fr/04.webp)



Sau đó, bạn có thể truy cập vào tất cả các chức năng của danh mục đầu tư, giống như trên SeedSigner cổ điển.



![Image](assets/fr/05.webp)



Bây giờ bạn có thể nhập kho khóa vào Sparrow, Wallet và sử dụng wallet như bình thường. Mỗi lần khởi động lại, bạn sẽ cần quét SeedQR và nhập lại passphrase bằng bàn phím, như chúng tôi đã làm ở đây.



Trước khi thực sự sử dụng wallet với passphrase, tôi thực sự khuyên bạn nên thực hiện kiểm tra khôi phục hoàn toàn trống. Điều này sẽ cho phép bạn xác nhận rằng các bản sao lưu cụm từ ghi nhớ và passphrase của bạn là hợp lệ. Để tìm hiểu cách thực hiện kiểm tra này, hãy xem hướng dẫn sau:



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895