---
name: Kiểm Tra Khôi Phục
description: Làm thế nào để kiểm tra bản sao lưu của bạn để đảm bảo bạn không mất bitcoin?
---
![cover](assets/cover.webp)

Khi tạo một ví Bitcoin, bạn sẽ được yêu cầu ghi lại một cụm từ ghi nhớ, thường gồm 12 hoặc 24 từ. Cụm từ này cho phép bạn khôi phục quyền truy cập vào bitcoin của mình trong trường hợp mất, hỏng, hoặc bị đánh cắp thiết bị chứa ví của bạn. Trước khi bạn bắt đầu sử dụng ví Bitcoin mới của mình, việc xác minh tính hợp lệ của cụm từ ghi nhớ này là rất quan trọng. Cách tốt nhất để làm điều này là thực hiện một bài kiểm tra khôi phục dạng khô.

Bài kiểm tra này bao gồm việc mô phỏng việc khôi phục ví trước khi nạp bất kỳ bitcoin nào vào đó. Miễn là ví còn trống, chúng tôi mô phỏng tình huống mất thiết bị chứa khóa của chúng tôi, và tất cả những gì chúng tôi còn lại là cụm từ ghi nhớ của mình để cố gắng khôi phục bitcoin của mình.

![KIỂM TRA KHÔI PHỤC](assets/notext/01.webp)

## Mục đích là gì?

Quy trình kiểm tra này cho phép bạn xác minh rằng bản sao lưu vật lý của cụm từ ghi nhớ của bạn, dù là trên giấy hay kim loại, là có chức năng. Một sự cố trong quá trình kiểm tra khôi phục này báo hiệu một lỗi trong việc sao lưu cụm từ, do đó đặt bitcoin của bạn vào nguy cơ. Ngược lại, nếu bài kiểm tra thành công, nó xác nhận rằng cụm từ ghi nhớ của bạn hoàn toàn hoạt động, và bạn có thể sau đó an tâm sử dụng ví này để bảo quản bitcoin.

Thực hiện một bài kiểm tra khôi phục dạng khô có lợi ích kép. Không chỉ cho phép bạn kiểm tra độ chính xác của cụm từ ghi nhớ của mình, mà còn cho bạn cơ hội làm quen với quy trình khôi phục ví. Như vậy, bạn sẽ phát hiện ra những khó khăn tiềm ẩn trước khi một tình huống thực sự xảy ra với bạn. Vào ngày bạn thực sự cần khôi phục ví của mình, bạn sẽ ít căng thẳng hơn, vì bạn đã biết quy trình, giảm thiểu rủi ro sai lầm. Đó là lý do tại sao việc không bỏ qua bước kiểm tra này và dành thời gian cần thiết để thực hiện đúng cách là quan trọng.

## Kiểm tra khôi phục là gì?

Quy trình của bài kiểm tra khá đơn giản:
- Sau khi tạo ví Bitcoin mới của bạn, và trước khi nạp satoshis đầu tiên của bạn, ghi lại thông tin chứng nhận như một xpub, địa chỉ nhận đầu tiên, hoặc thậm chí là dấu vân tay khóa chính;
- Sau đó, cố ý xóa ví vẫn còn trống, ví dụ, bằng cách đặt lại ví cứng của bạn về cài đặt gốc;
- Tiếp theo, mô phỏng việc khôi phục ví của bạn chỉ sử dụng bản sao lưu giấy của cụm từ ghi nhớ và cụm từ bí mật của bạn nếu bạn sử dụng một;
- Cuối cùng, kiểm tra xem thông tin chứng nhận có khớp với thông tin của danh mục đầu tư được tái tạo hay không. Nếu thông tin khớp, bạn có thể yên tâm về độ tin cậy của bản sao lưu vật lý của mình, và bạn có thể sau đó gửi bitcoin đầu tiên của mình vào ví này.
Hãy cẩn thận, trong quá trình kiểm tra khôi phục, **bạn phải sử dụng cùng một thiết bị dành cho ví cuối cùng của mình**, để không tăng diện tích tấn công của ví. Ví dụ, nếu bạn tạo một ví trên Trezor Safe 5, hãy đảm bảo thực hiện bài kiểm tra khôi phục trên chính Trezor Safe 5 này. Quan trọng là không nhập cụm từ khôi phục của bạn vào bất kỳ phần mềm nào khác, vì điều này sẽ làm mất đi sự bảo mật mà ví cứng của bạn cung cấp, ngay cả khi ví vẫn còn trống.

## Làm thế nào để thực hiện một bài kiểm tra khôi phục?

Trong hướng dẫn này, tôi sẽ giải thích cách thực hiện một bài kiểm tra khôi phục trên một ví phần mềm Bitcoin, sử dụng Sparrow Wallet (cho một ví nóng). Tuy nhiên, quy trình vẫn giống nhau cho bất kỳ loại thiết bị nào khác. Một lần nữa, **nếu bạn đang sử dụng một ví cứng, không thực hiện bài kiểm tra khôi phục trên Sparrow Wallet** (xem phần trước).
Tôi vừa tạo một ví nóng mới trên Sparrow Wallet. Hiện tại, tôi chưa gửi bất kỳ bitcoin nào vào đó. Nó đang trống không.
![KIỂM TRA KHÔI PHỤC](assets/notext/02.webp)

Tôi đã cẩn thận ghi chú cụm từ ghi nhớ 12 từ của mình trên một tờ giấy. Và vì tôi muốn tăng cường bảo mật cho ví này, tôi cũng đã thiết lập một cụm từ bí mật BIP39 mà tôi đã lưu trên một tờ giấy khác:

```txt
1. shield
2. brass
3. sentence
4. cube
5. marble
6. glad
7. satoshi
8. door
9. project
10. panic
11. prepare
12. general
```

```text
Cụm từ bí mật: YfaicGzXH9t5C#g&47Kzbc$JL
```

***Rõ ràng, bạn không bao giờ nên chia sẻ cụm từ ghi nhớ và cụm từ bí mật của mình trên internet, không giống như những gì tôi đang làm trong hướng dẫn này. Ví dụ ví này sẽ không được sử dụng và sẽ bị xóa ở cuối hướng dẫn.***

Bây giờ tôi sẽ ghi chú trên một bản nháp một mẩu thông tin chứng từ từ ví của mình. Bạn có thể chọn các mẩu thông tin khác nhau, như địa chỉ nhận đầu tiên, xpub, hoặc dấu vân tay khóa chính. Cá nhân tôi, tôi khuyên bạn nên chọn địa chỉ nhận đầu tiên. Điều này cho phép bạn xác minh rằng bạn có thể tìm thấy đường dẫn phái sinh đầu tiên hoàn chỉnh dẫn đến địa chỉ này.

Trên Sparrow, nhấp vào tab "*Địa chỉ*".

![KIỂM TRA KHÔI PHỤC](assets/notext/03.webp)

Sau đó, ghi chú trên một tờ giấy địa chỉ nhận đầu tiên của ví bạn. Trong ví dụ của tôi, địa chỉ là:

```txt
tb1qxv56mma5x5r7uhdkn0ldvcx6m0gj6f3kre0gwd
```

Sau khi ghi chú thông tin, đi đến menu "*File*", sau đó chọn "*Xóa Ví*". Tôi nhắc bạn một lần nữa rằng ví Bitcoin của bạn phải trống trước khi tiến hành thao tác này.

![KIỂM TRA KHÔI PHỤC](assets/notext/04.webp)

Nếu ví của bạn thực sự trống, xác nhận việc xóa ví của bạn.

![KIỂM TRA KHÔI PHỤC](assets/notext/05.webp)

Bây giờ bạn cần lặp lại quá trình tạo ví, nhưng sử dụng bản sao giấy của chúng tôi. Nhấp vào menu "*File*" và sau đó vào "*Ví Mới*".

![KIỂM TRA KHÔI PHỤC](assets/notext/06.webp)

Nhập lại tên của ví bạn.

![KIỂM TRA KHÔI PHỤC](assets/notext/07.webp)

Trong menu "*Loại Script*", bạn cần chọn cùng một loại script như ví bạn đã xóa trước đó.

![KIỂM TRA KHÔI PHỤC](assets/notext/08.webp)

Sau đó nhấp vào nút "*Ví Phần Mềm Mới hoặc Đã Nhập*".

![KIỂM TRA KHÔI PHỤC](assets/notext/09.webp)

Chọn số lượng từ chính xác cho hạt giống của bạn.

![KIỂM TRA KHÔI PHỤC](assets/notext/10.webp)

Nhập cụm từ ghi nhớ của bạn vào phần mềm. Nếu xuất hiện thông báo "*Checksum Không Hợp Lệ*", điều này chỉ ra rằng bản sao của cụm từ ghi nhớ của bạn không chính xác. Bạn sẽ phải bắt đầu lại quá trình tạo ví của mình từ đầu, vì bài kiểm tra khôi phục của bạn đã thất bại.

![KIỂM TRA KHÔI PHỤC](assets/notext/11.webp)

Nếu bạn có cụm từ bí mật, như trường hợp của tôi, cũng nhập nó.

![KIỂM TRA KHÔI PHỤC](assets/notext/12.webp)

Nhấp vào "*Tạo Keystore*", sau đó vào "*Nhập Keystore*".

![KIỂM TRA KHÔI PHỤC](assets/notext/13.webp)

Và cuối cùng, nhấp vào nút "*Áp dụng*".

![KIỂM TRA KHÔI PHỤC](assets/notext/14.webp)

Bây giờ bạn có thể quay trở lại tab "*Địa chỉ*".

![KIỂM TRA KHÔI PHỤC](assets/notext/15.webp)
Cuối cùng, hãy xác minh rằng địa chỉ nhận đầu tiên trùng khớp với địa chỉ bạn đã ghi chú như một nhân chứng trên bản nháp của mình.
![RECOVERY TEST](assets/notext/16.webp)

Nếu các địa chỉ nhận trùng khớp, bài kiểm tra khôi phục của bạn thành công, và bạn có thể sử dụng ví Bitcoin mới của mình. Nếu chúng không trùng khớp, điều này có thể chỉ ra lỗi trong việc chọn loại script, khiến cho đường dẫn phái sinh trở nên không chính xác, hoặc một vấn đề với việc sao lưu cụm từ ghi nhớ hoặc cụm từ mật khẩu của bạn. Trong cả hai trường hợp, tôi khuyến nghị mạnh mẽ việc bắt đầu lại từ đầu và tạo một ví Bitcoin mới từ đầu để tránh bất kỳ rủi ro nào. Lần này, hãy chú ý ghi chú cụm từ ghi nhớ mà không có lỗi.
Xin chúc mừng, bạn giờ đã nắm vững cách thực hiện bài kiểm tra khôi phục! Tôi khuyên bạn nên áp dụng quy trình này cho việc tạo tất cả các ví Bitcoin của mình. Nếu bạn thấy hướng dẫn này hữu ích, tôi sẽ rất biết ơn nếu bạn có thể để lại một lượt thích phía dưới. Đừng ngần ngại chia sẻ bài viết này trên các mạng xã hội của bạn. Cảm ơn bạn rất nhiều!