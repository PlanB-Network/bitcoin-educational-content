---
name: Electrum

description: Hướng dẫn toàn diện về Electrum, từ cơ bản đến nâng cao
---

![cover](assets/cover.webp)

Mô tả cho Electrum

https://twitter.com/ElectrumWallet
https://electrum.org/
https://electrum.readthedocs.io/

> "Phải nói là, khi tôi tìm thấy hướng dẫn này tôi đã rất ngạc nhiên. Xin chúc mừng Arman the Parman về điều này. Thật đáng tiếc nếu không đăng tải nó ở đây và dịch ra càng nhiều ngôn ngữ càng tốt. Thực sự, hãy tip cho anh chàng đó." Rogzy

Bài viết gốc:

![Electrum Desktop Wallet (Mac / Linux) - tải xuống, xác minh, kết nối với node của bạn.](https://youtu.be/wHmQNcRWdHM)

![Thực hiện giao dịch Bitcoin với Electrum](https://youtu.be/-d_Zd7VcAfQ)

## Tại sao chọn Electrum?

Đây là một hướng dẫn chi tiết về cách sử dụng Ví Bitcoin Electrum, với giải pháp cho tất cả các bẫy và điểm lưu ý - điều mà tôi đã phát triển sau nhiều năm sử dụng và giảng dạy sinh viên về bảo mật/riêng tư Bitcoin. Electrum không phải là ví Bitcoin tốt nhất cho người muốn giữ mọi thứ càng đơn giản càng tốt và muốn ở lại ở cấp độ người mới bắt đầu. Thay vào đó, nó dành cho người mà là, hoặc muốn trở thành, một người dùng "nâng cao".

Đối với người mới sử dụng Bitcoin, nó chỉ tốt nếu dưới sự giám sát của một người dùng có kinh nghiệm để chỉ cho họ cách thức. Nếu tự học sử dụng nó, nó sẽ an toàn miễn là họ dành thời gian và sử dụng nó trong môi trường thử nghiệm với chỉ một số lượng nhỏ sats ban đầu. Hướng dẫn này hỗ trợ nỗ lực đó, nhưng nó cũng là một tài liệu tham khảo tốt cho bất kỳ ai khác.

> Cảnh báo: Hướng dẫn này rất lớn. Đừng cố gắng làm tất cả trong một ngày. Tốt nhất là lưu hướng dẫn và thực hiện từ từ theo thời gian.

## Tải xuống Electrum

Lý tưởng nhất, sử dụng một máy tính Bitcoin ch dedicated dành riêng cho các giao dịch Bitcoin của bạn (Hướng dẫn của tôi cho điều này https://armantheparman.com/mint/) _(CŨNG có sẵn trong phần riêng tư)_. Thực hành với số lượng nhỏ trên một máy tính "bẩn" khi bạn mới bắt đầu là ổn (ai biết máy tính thường xuyên của bạn đã tích lũy bao nhiêu malware ẩn kín qua bao nhiêu năm - bạn không muốn phơi bày ví Bitcoin của mình cho chúng).

Lấy Electrum từ https://electrum.org/.

Nhấp vào tab Download ở phía trên.

Nhấp vào liên kết tải xuống tương ứng với máy tính của bạn. Bất kỳ máy tính Linux hoặc Mac nào cũng có thể sử dụng liên kết Python (vòng tròn đỏ). Một máy tính Linux với chip Intel hoặc AMD có thể sử dụng Appimage (vòng tròn xanh lá; giống như một tệp thực thi Windows). Một thiết bị Raspberry Pi có bộ vi xử lý ARM và chỉ có thể sử dụng phiên bản Python (vòng tròn đỏ), không phải Appimage, mặc dù Pi chạy Linux. Vòng tròn xanh là cho Windows và vòng tròn đen là cho Mac.

![image](assets/1.webp)

## Xác minh Electrum

Mục đích của việc "xác minh" việc tải xuống là để đảm bảo không một bit dữ liệu nào bị thay đổi. Nó ngăn bạn sử dụng phiên bản phần mềm "bị hack" có hại. Bạn có thể bỏ qua bước này nếu bạn chỉ sử dụng bản sao đã tải xuống để thực hành, tức là không sử dụng ví chứa số tiền lớn. Sau đó, khi bạn sẵn sàng sử dụng Electrum cho quỹ thực sự của mình, bạn nên xóa bản sao của mình và bắt đầu lại, lần này là xác minh việc tải xuống của bạn.
Để thực hiện điều này, chúng tôi sử dụng công cụ mã hóa khóa công khai/khóa riêng - gpg, mà chúng tôi đã viết một hướng dẫn về nó tại đây (https://armantheparman.com/gpg/). Công cụ gpg có sẵn trên tất cả các hệ điều hành Linux. Đối với Mac và Windows, xem liên kết gpg để biết hướng dẫn tải xuống.

Ngoài việc tải xuống phần mềm Electrum, vì lý do bảo mật, bạn cũng cần có CHỮ KÝ số của phần mềm. Đây là một chuỗi văn bản (thực ra là một số được mã hóa dưới dạng văn bản) mà nhà phát triển tạo ra bằng khóa gpg RIÊNG của mình. Sử dụng chương trình gpg, chúng ta có thể sau đó "kiểm tra" CHỮ KÝ đối với khóa CÔNG KHAI của anh ấy (được tạo từ khóa riêng của nhà phát triển) mà mọi người đều có thể truy cập, so với tệp TẢI XUỐNG.

Nói cách khác, với ba đầu vào (chữ ký, khóa công khai và tệp dữ liệu), chúng ta nhận được một kết quả đúng hoặc sai để xác nhận rằng tệp không bị can thiệp.

Để lấy chữ ký, nhấp vào liên kết tương ứng với tệp bạn đã tải xuống (xem mũi tên màu):

![image](assets/2.webp)

Nhấp vào liên kết có thể tự động tải tệp xuống thư mục tải xuống của bạn, hoặc nó có thể mở trong trình duyệt. Nếu nó mở trong trình duyệt, bạn cần lưu tệp. Bạn có thể nhấp chuột phải và chọn “lưu thành”. Tùy thuộc vào hệ điều hành hoặc trình duyệt, bạn có thể cần nhấp chuột phải vào khu vực không gian trắng, không phải văn bản.

Dưới đây là cách trông của văn bản đã tải xuống. Bạn có thể thấy có nhiều chữ ký - đây là chữ ký của nhiều người khác nhau. Bạn có thể xác minh từng cái hoặc bất kỳ cái nào. Tôi sẽ chỉ cho bạn cách xác minh chữ ký của nhà phát triển.

![image](assets/3.webp)

Tiếp theo, bạn cần lấy khóa công khai của ThomasV - anh ấy là nhà phát triển chính. Bạn có thể lấy trực tiếp từ anh ấy, tài khoản Keybase của anh ấy, Github, hoặc từ người khác, từ một máy chủ khóa, hoặc từ trang web Electrum.

Lấy nó từ trang web Electrum thực sự là cách ít an toàn nhất, bởi vì nếu trang web này có ý đồ xấu (chính xác là điều chúng ta đang kiểm tra) tại sao chúng ta lại lấy một khóa công khai từ nó (khóa công khai có thể là giả)?

Để giữ cho mọi thứ đơn giản lúc này, tôi sẽ chỉ cho bạn cách lấy nó từ trang web dù sao, nhưng hãy nhớ điều này. Đây là bản sao (https://github.com/spesmilo/electrum/blob/master/pubkeys/ThomasV.asc) trên GitHub mà bạn có thể so sánh.

Cuộn xuống trang một chút để tìm liên kết đến khóa công khai của ThomasV (vòng tròn màu đỏ bên dưới). Nhấp vào nó và tải xuống, hoặc nếu nó mở một số văn bản trong trình duyệt, nhấp chuột phải để lưu.

![image](assets/4.webp)

Bây giờ bạn có 3 tệp mới, có lẽ tất cả đều ở trong thư mục tải xuống. Không quan trọng chúng ở đâu, nhưng quá trình sẽ dễ dàng hơn nếu bạn đặt tất cả chúng vào cùng một thư mục.

Ba tệp:

1. Tệp tải xuống Electrum
2. Tệp chữ ký (thường là cùng tên tệp với tệp tải xuống Electrum với thêm “.asc”
3. Khóa công khai của ThomasV.

Mở một cửa sổ terminal trên Mac hoặc Linux, hoặc dấu nhắc lệnh (CMD) trên Windows.

Di chuyển đến thư mục Downloads (hoặc bất cứ nơi nào bạn đặt ba tệp). Nếu bạn không biết điều này có nghĩa là gì, học từ video ngắn này cho Linux/Mac (https://www.youtube.com/watch?v=AO0jzD1hpXc) và cái này cho Windows (https://www.youtube.com/watch?v=9zMWXD-xoxc). Nhớ rằng trên máy tính Linux, tên thư mục phân biệt chữ hoa chữ thường.
Trong terminal, gõ lệnh này để nhập khóa công khai của ThomasV vào "bộ sưu tập khóa" trên máy tính của bạn (bộ sưu tập khóa là một khái niệm trừu tượng - thực chất nó chỉ là một tệp trên máy tính của bạn):
```bash
gpg --import ThomasV.asc
```

Hãy chắc chắn rằng tên tệp trùng khớp với tệp bạn đã tải xuống. Lưu ý rằng đây là dấu gạch nối kép chứ không phải gạch nối đơn. Ngoài ra, chú ý có một khoảng trắng trước và sau “--import”. Sau đó nhấn <enter>.

Tệp sẽ được nhập. Nếu bạn nhận được một lỗi, kiểm tra bạn đang ở trong thư mục nơi tệp thực sự tồn tại. Để kiểm tra thư mục bạn đang ở (trên Mac hoặc Linux), gõ pwd. Để xem những tệp nào đang trong thư mục bạn đang ở (trên Mac hoặc Linux), gõ ls. Bạn nên thấy tệp văn bản “ThomasV.asc” được liệt kê, có thể cùng với các tệp khác.

Sau đó, chúng ta chạy lệnh để xác minh chữ ký.

```bash
gpg --verify Electrum-4.1.5.tar.gz.asc Electrum-4.1.5.tar.gz
```

Lưu ý có 4 “phần tử” ở đây, mỗi phần được tách bởi một khoảng trắng. Tôi đã in đậm văn bản xen kẽ để giúp bạn nhìn thấy. Bốn phần tử là:

1. chương trình gpg
2. tùy chọn --verify
3. tên tệp của chữ ký
4. tên tệp của chương trình

Điều đáng chú ý, đôi khi bạn có thể bỏ qua phần tử thứ 4 và máy tính sẽ đoán ý bạn. Tôi không chắc, nhưng tôi tin rằng nó chỉ hoạt động nếu tên tệp chỉ khác nhau bởi “asc” ở cuối.

Đừng chỉ sao chép tên tệp mà tôi đã chỉ ra ở đây - hãy chắc chắn chúng trùng khớp với tên tệp của những gì bạn có trên hệ thống của mình.

Nhấn <enter> để chạy lệnh. Bạn nên thấy một “chữ ký tốt từ ThomasV” để chỉ ra thành công. Sẽ có một số lỗi vì chúng ta không có khóa công khai cho chữ ký của những người khác được chứa trong tệp chữ ký (hệ thống này của việc kết hợp chữ ký trong một tệp có thể thay đổi trong các phiên bản sau). Ngoài ra, có một cảnh báo ở phía dưới mà chúng ta có thể bỏ qua (điều này cảnh báo chúng ta rằng chúng ta chưa rõ ràng thông báo cho máy tính rằng chúng ta tin tưởng khóa công khai của ThomasV).

Bây giờ chúng ta có một bản sao của Electrum đã được xác minh là an toàn để sử dụng.

## Chạy Electrum

### Chạy Electrum nếu sử dụng Python

Nếu bạn đã tải xuống phiên bản Python, đây là cách để làm cho nó hoạt động. Bạn sẽ thấy trên trang tải xuống điều này:

![image](assets/5.webp)

Đối với Linux, Đầu tiên nên cập nhật hệ thống của bạn:

```bash
sudo apt-get update
sudo apt-get upgrade
```

Sao chép văn bản được làm nổi bật màu vàng, dán vào terminal, và nhấn <enter>. Bạn sẽ được yêu cầu mật khẩu, có thể là xác nhận để tiếp tục, và sau đó nó sẽ cài đặt những tệp đó (“dependencies”).

Bạn cũng cần giải nén tệp zip vào một thư mục theo lựa chọn của bạn. Bạn có thể làm điều này với giao diện người dùng đồ họa, hoặc từ dòng lệnh (lệnh được làm nổi bật màu hồng) - nhớ rằng tên tệp của bạn có thể khác. (Lưu ý rằng khi chúng tôi đã xác minh tải xuống trong phần trước, đó là tệp zip chúng tôi đã xác minh, không phải thư mục đã giải nén.)

Có một tùy chọn để “cài đặt” sử dụng chương trình PIP, nhưng điều này không cần thiết, và thêm các bước cũng như cài đặt thêm tệp. Chỉ cần chạy chương trình sử dụng terminal để bỏ qua tất cả những điều đó.

Các bước (Linux) là:

1. điều hướng đến thư mục nơi các tệp được giải nén
2. gõ: ./run_electrum

Trên Mac, các bước là tương tự nhưng bạn có thể cần cài đặt Python3 trước, và sử dụng lệnh này để chạy:
```bash
python3 ./run_electrum
```

Một khi Electrum đã được chạy, cửa sổ terminal sẽ vẫn mở. Nếu bạn đóng nó lại, chương trình Electrum sẽ bị kết thúc. Chỉ cần thu nhỏ nó lại khi bạn đang sử dụng Electrum.

### Chạy Electrum với Appimage

Cách này dễ dàng hơn một chút, nhưng không dễ như file thực thi Windows. Tùy thuộc vào phiên bản Linux bạn đang sử dụng, mặc định, các file Appimage có thể được thiết lập các thuộc tính sao cho hệ thống không cho phép thực thi. Chúng ta cần phải thay đổi điều này. Nếu Appimages của bạn hoạt động, bạn có thể bỏ qua bước này. Di chuyển đến nơi chứa file, sử dụng terminal, sau đó chạy lệnh này:

```bash
sudo chmod ug+x Electrum-4.1.5-x86_64.AppImage
```

“sudo” cấp quyền superuser; “chmod” là lệnh để thay đổi mode, thay đổi ai có thể đọc, viết, hoặc thực thi; “ug+x” có nghĩa là chúng ta đang chỉnh sửa quyền của người dùng và nhóm để cho phép thực thi.

Điều chỉnh tên file cho phù hợp với phiên bản của bạn.

Sau đó, Electrum sẽ chạy bằng cách nhấp đúp vào biểu tượng Appimage.

### Chạy Electrum trên Mac

Chỉ cần nhấp đúp vào file đã tải (nó là một “ổ đĩa”). Một cửa sổ sẽ mở ra. Kéo biểu tượng Electrum trong cửa sổ vào desktop của bạn, hoặc bất cứ nơi nào bạn muốn giữ chương trình. Bạn có thể sau đó “eject” ổ đĩa, và xóa ổ đĩa (file đã tải).

Để chạy chương trình, chỉ cần nhấp đúp vào nó. Bạn có thể gặp một số lỗi cụ thể của Mac cần phải vượt qua.

### Chạy Electrum trên Windows

Mặc dù tôi ghét Windows nhất, đây là phương pháp đơn giản nhất. Chỉ cần nhấp đúp vào file thực thi để chạy.

## Bắt đầu với một ví giả

Khi bạn lần đầu tiên tải Electrum, một cửa sổ sẽ mở ra như thế này:

![image](assets/6.webp)

Chúng ta sẽ sau này chọn máy chủ của bạn một cách thủ công, nhưng bây giờ, hãy để mặc định và tự động kết nối.

Tiếp theo, tạo một ví giả - đừng bao giờ đặt tiền vào ví này. Mục đích của ví giả này là để tiến qua phần mềm và đảm bảo mọi thứ hoạt động tốt trước khi bạn tải ví thực của mình. Chúng ta đang cố gắng tránh việc vô tình từ bỏ quyền riêng tư với một ví thực. Nếu bạn chỉ đang thực hành, ví bạn tạo có thể được coi là một ví giả dù sao.

Bạn có thể để tên là “default_wallet” hoặc thay đổi nó thành bất cứ cái gì bạn thích, và nhấp vào tiếp theo. Sau này, nếu bạn có nhiều ví, bạn có thể tìm và mở chúng ở giai đoạn này bằng cách đầu tiên nhấp vào “Choose…”

![image](assets/7.webp)

Chọn “Standard wallet” và <Next>:

![image](assets/8.webp)

Sau đó, chọn “I already have a seed”. Tôi không muốn bạn quen với việc tạo một seed của Electrum, vì nó sử dụng giao thức riêng của mình không tương thích với các ví khác - đó là lý do tại sao chúng ta không nhấp vào “new seed”.

![image](assets/9.webp)

Truy cập https://iancoleman.io/bip39/ và tạo một seed giả. Đầu tiên, thay đổi số từ thành 12 (đây là thực hành phổ biến), sau đó nhấp vào “generate” và sao chép các từ trong hộp vào clipboard của bạn.

![image](assets/10.webp)

Sau đó dán các từ vào Electrum. Dưới đây là một ví dụ:

![image](assets/11.webp)

Electrum sẽ tìm kiếm các từ phù hợp với giao thức của mình. Chúng ta phải vượt qua điều đó. Nhấp vào tùy chọn, và chọn BIP39 Seed:

![image](assets/12.webp)
Hạt giống sau đó trở nên hợp lệ. (Trước khi thực hiện điều này, Electrum đang chờ đợi một hạt giống Electrum nên hạt giống này được coi là không hợp lệ). Trước khi bạn nhấn tiếp theo, hãy chú ý đến dòng chữ nói rằng “Checksum OK”. Điều này rất quan trọng (đối với ví thực bạn có thể sử dụng sau này) là bạn cần thấy điều này trước khi tiếp tục, vì nó xác nhận tính hợp lệ của hạt giống bạn đã nhập. Cảnh báo gần cuối có thể bỏ qua, đó là lời than phiền của nhà phát triển Electrum về BIP39 và những tuyên bố “FUD’ey” của họ rằng phiên bản của họ (không tương thích với các ví khác) là tốt hơn.

> Một lời cảnh báo quan trọng nhanh chóng. Mục đích của checksum là để đảm bảo bạn đã nhập hạt giống của mình mà không có lỗi đánh máy. Checksum là phần cuối cùng của hạt giống (từ thứ 12 cuối cùng là từ checksum) mà về mặt toán học được xác định bởi phần đầu tiên của hạt giống (11 từ). Nếu bạn nhập sai một cái gì đó ở phần đầu, từ checksum sẽ không khớp về mặt toán học, và phần mềm ví sẽ cảnh báo bạn bằng một thông báo. Điều này không có nghĩa là hạt giống không thể được sử dụng để tạo một Ví Bitcoin hoạt động. Hãy tưởng tượng tạo một ví với lỗi đánh máy, nạp ví với bitcoin, sau đó một ngày nào đó bạn cần phục hồi ví, nhưng khi bạn làm vậy, bạn không tái tạo lỗi đánh máy - bạn sẽ phục hồi nhầm ví! Thật nguy hiểm khi Electrum cho phép bạn tiếp tục tạo ví nếu checksum của bạn không hợp lệ, vì vậy hãy được cảnh báo, đó là trách nhiệm của bạn để đảm bảo. Các ví khác sẽ không cho phép bạn tiếp tục, điều này an toàn hơn nhiều. Đây là một trong những điều tôi muốn nói khi tôi nói Electrum là tốt để sử dụng, một khi bạn học cách sử dụng nó đúng cách (các nhà phát triển Electrum nên sửa lỗi này).

Lưu ý rằng nếu bạn muốn thêm một cụm mật khẩu, cơ hội để chọn điều đó nằm ở cửa sổ tùy chọn này, ngay ở phía trên cùng.

Sau khi nhấn OK, bạn sẽ được đưa trở lại nơi bạn đã nhập cụm từ hạt giống. Nếu bạn đã chọn một tùy chọn cụm mật khẩu, bạn KHÔNG nhập nó với các từ hạt giống (lời nhắc cho điều đó xuất hiện tiếp theo).

Nếu bạn không yêu cầu một cụm mật khẩu, bạn sẽ thấy màn hình tiếp theo này - nhiều tùy chọn hơn cho loại kịch bản ví và đường dẫn phái sinh mà bạn có thể tìm hiểu tại đây (https://armantheparman.com/public-and-private-keys/), nhưng chỉ cần để mặc định và tiếp tục.

![image](assets/13.webp)

> Thông tin thêm: Tùy chọn đầu tiên cho phép bạn chọn giữa legacy (địa chỉ bắt đầu bằng “1”), pay-to-script-hash (địa chỉ bắt đầu bằng “3”), hoặc bech32/native segwit (địa chỉ bắt đầu bằng “bc1q”). Tại thời điểm viết bài, Electrum chưa hỗ trợ taproot (địa chỉ bắt đầu bằng “bc1p”). Tùy chọn thứ hai trong cửa sổ này cho phép bạn chỉnh sửa đường dẫn phái sinh. Tôi đề xuất bạn không bao giờ chỉnh sửa điều này, đặc biệt là trước khi hiểu nó có nghĩa là gì. Mọi người sẽ nhấn mạnh tầm quan trọng của việc ghi lại đường dẫn phái sinh để bạn có thể khôi phục ví của mình nếu cần, nhưng nếu bạn để nó như mặc định, bạn sẽ có lẽ ổn, vì vậy đừng hoảng sợ - nhưng vẫn là thực hành tốt để ghi lại đường dẫn phái sinh.

Tiếp theo, bạn sẽ được đưa ra lựa chọn để thêm một MẬT KHẨU. Điều này không được nhầm lẫn với “CỤM MẬT KHẨU”. Một mật khẩu khóa tệp trên máy tính của bạn. Một cụm mật khẩu là một phần của cấu trúc khóa riêng tư. Vì đây là một ví giả, bạn có thể để trống mật khẩu và tiếp tục.

![image](assets/14.webp)
Bạn sẽ nhận được một cửa sổ pop-up thông báo về phiên bản mới (Tôi gợi ý bạn chọn không). Ví tiền sẽ tự động được tạo và sẵn sàng sử dụng (nhưng nhớ rằng, ví này được dùng để xóa, chỉ là một ví giả mạo).
![hình ảnh](assets/15.webp)

Có một số việc tôi gợi ý bạn nên làm để thiết lập môi trường phần mềm (chỉ cần thực hiện một lần):

### Đổi đơn vị sang BTC

Vào menu trên cùng, công cụ –> tùy chọn electrum, và tại đây dưới tab chung, bạn sẽ tìm thấy tùy chọn để đổi “đơn vị cơ bản” sang BTC.
Kích hoạt tab Địa chỉ và Tiền xu

Vào menu trên cùng, xem, và chọn “hiển thị địa chỉ”. Sau đó quay lại xem và chọn “hiển thị tiền xu”.

### Kích hoạt Oneserver

Mặc định, Electrum kết nối với một nút ngẫu nhiên. Nó cũng kết nối với nhiều nút phụ khác. Tôi không chắc dữ liệu nào được trao đổi với những nút phụ này, nhưng chúng ta không muốn điều này xảy ra, vì lý do riêng tư. Ngay cả khi bạn chỉ định một nút, ví dụ nút của riêng bạn, những nút khác cũng sẽ được kết nối, và tôi không chắc thông tin nào được chia sẻ. Dù sao, việc ngăn chặn điều này cũng khá dễ dàng. Trước khi tôi chỉ cho bạn cách chỉ định nút của riêng bạn, chúng ta sẽ buộc Electrum chỉ kết nối với một máy chủ tại một thời điểm.

> Có một cách để làm điều này bằng cách chỉ định “oneserver” từ dòng lệnh, nhưng tôi không khuyến khích cách này. Tôi sẽ chỉ một phương án thay thế mà tôi nghĩ là dễ dàng hơn về lâu dài, và có khả năng không để bạn vô tình kết nối với các nút khác.

Lý do chúng ta sử dụng một ví giả mạo là nếu chúng ta đã tải ví thực của mình, với bitcoin thực của mình, chúng ta sẽ đã vô tình kết nối với một nút ngẫu nhiên bây giờ (ngay cả khi chúng ta đã chọn “thiết lập máy chủ theo cách thủ công” ngay từ đầu, nó vẫn kết nối với các nút phụ khác vì một số lý do (này các nhà phát triển Electrum, bạn nên sửa điều này). Nếu ví của chúng ta là riêng tư, điều này sẽ là một thảm họa.

Chúng ta cũng không thể thực hiện các bước tôi sẽ chỉ dưới đây mà không trước tiên tải lên một loại ví nào đó. (Chúng ta sẽ chỉnh sửa một tệp cấu hình chỉ được điền và sẵn sàng để chỉnh sửa sau khi một ví được tải).

**Tắt Electrum (QUAN TRỌNG, nếu bạn không làm điều này, những thay đổi sau đây bạn thực hiện sẽ bị xóa).**

### Tệp Cấu Hình LINUX/MAC

Mở terminal trong Linux hoặc Mac (hướng dẫn cho Windows sau):

Bạn sẽ tự động ở trong thư mục home. Từ đó, điều hướng đến thư mục cài đặt ẩn của electrum (khác với nơi ứng dụng được cài đặt).

```bash
cd .electrum
```

Chú ý dấu chấm trước “electrum” chỉ ra rằng đây là một thư mục ẩn.

Một cách khác để đến đó là gõ:

```bash
cd ~/.electrum
```

nơi “~” đại diện cho đường dẫn của thư mục home của bạn. Bạn có thể xem đường dẫn đầy đủ của thư mục hiện tại với lệnh “pwd“.

Một khi đã ở trong thư mục “.electrum”, gõ “nano config” và nhấn <enter>.

Một trình soạn thảo văn bản sẽ mở (gọi là nano) với tệp cấu hình mở. Chuột không hoạt động nhiều ở đây. Sử dụng các phím mũi tên để di chuyển đến dòng nói:

```json
"oneserver": false,
```

Thay đổi “false” thành “true”; và không làm xáo trộn cú pháp (không xóa dấu phẩy hoặc dấu chấm phẩy).

Nhấn <ctrl> x, để thoát, sau đó “y” để lưu, rồi <enter> để xác nhận thay đổi mà không chỉnh sửa tên tệp.
Bây giờ, hãy chạy lại Electrum. Sau đó, nhấp vào biểu tượng hình tròn ở góc dưới bên phải, điều này sẽ mở cài đặt mạng. Tiếp theo, gần đầu trong tab tổng quan, bạn sẽ thấy "đã kết nối với 1 node" - điều này chỉ ra thành công.
Ngay bên dưới đó, bạn sẽ thấy một trường văn bản và địa chỉ của máy chủ được hiển thị ở đó. Bạn hiện đang kết nối với node ngẫu nhiên đó. Phần kết nối với một node sẽ được giới thiệu trong phần tiếp theo.

### Tệp Cấu Hình Windows

Tệp cấu hình Windows hơi khó tìm hơn. Đường dẫn là: `C:/Users/Parman/AppData/Roaming/Electrum`

Rõ ràng, bạn phải thay đổi "Parman" thành tên người dùng của bạn trên máy tính.

Trong thư mục đó bạn sẽ tìm thấy tệp cấu hình. Mở nó với trình soạn thảo văn bản và chỉnh sửa dòng:

```json
"oneserver": false,
```

Thay đổi "false" thành "true"; không làm xáo trộn cú pháp (không xóa dấu phẩy hoặc dấu chấm phẩy).

Sau đó lưu tệp và thoát.

## Kết nối Electrum với một node

Tiếp theo, chúng ta muốn kết nối ví giả của mình với một node theo lựa chọn của chúng ta. Nếu bạn chưa sẵn sàng để chạy một node, bạn có thể thực hiện một trong những cách sau:

1. Kết nối với node cá nhân của một người bạn (yêu cầu Tor)
2. Kết nối với node của một công ty đáng tin cậy
3. Kết nối với một node ngẫu nhiên (không được khuyến nghị).

Nhân tiện, đây là hướng dẫn để chạy node của riêng bạn, và đây là những lý do tại sao bạn nên làm điều đó. (tất cả hướng dẫn trong phần Node hoặc trong các khóa học miễn phí của chúng tôi)

### Kết nối với node của bạn bè qua Tor (Hướng dẫn sẽ sớm có.)

### Kết nối với node của một công ty đáng tin cậy

Lý do duy nhất để làm điều này là nếu bạn cần truy cập blockchain và bạn không có node của riêng mình (hoặc của một người bạn).

Hãy kết nối với node của Bitaroo - Chúng tôi được biết rằng họ không thu thập dữ liệu. Họ là một sàn giao dịch chỉ dành cho Bitcoin, được điều hành bởi một người đam mê Bitcoin. Kết nối với họ đòi hỏi một chút tin tưởng, nhưng nó tốt hơn là kết nối với một node ngẫu nhiên, có thể là một công ty giám sát.

Truy cập Cài đặt Mạng bằng cách nhấp vào biểu tượng hình tròn ở góc dưới bên phải của cửa sổ Ví (màu đỏ chỉ ra chưa kết nối, màu xanh lá cây chỉ ra đã kết nối, và màu xanh dương chỉ ra đã kết nối qua Tor).

![image](assets/16.webp)

Khi bạn nhấp vào biểu tượng hình tròn, một cửa sổ pop-up sẽ xuất hiện: Ví của bạn sẽ hiển thị "đã kết nối với 1 node" vì chúng tôi đã buộc điều đó trước đó.

Bỏ chọn hộp "chọn máy chủ tự động", và sau đó trong Trường Máy chủ, nhập chi tiết của Bitaroo như được hiển thị:

![image](assets/17.webp)

Đóng cửa sổ, và bây giờ chúng ta nên đã kết nối với node của Bitaroo. Để xác nhận, biểu tượng hình tròn nên là màu xanh lá. Nhấp vào nó một lần nữa và kiểm tra xem chi tiết máy chủ có thay đổi trở lại thành một node ngẫu nhiên không.

### Kết nối với node của riêng bạn

Nếu bạn có node của riêng mình thì tuyệt vời. Nếu bạn chỉ có Bitcoin Core, và không phải là một Electrum SERVER, bạn chưa thể kết nối một Electrum WALLET với node của mình.

> Lưu ý: Electrum Server và Electrum Wallet là hai thứ khác nhau. Server là phần mềm cần thiết để Electrum Wallet có thể giao tiếp với blockchain Bitcoin - Tôi không biết tại sao nó được thiết kế như vậy - có thể vì tốc độ nhưng tôi có thể nhầm.
Nếu bạn chạy một gói phần mềm node như MyNode (cái mà tôi khuyên mọi người nên bắt đầu với), Raspiblitz (được khuyến nghị khi bạn trở nên nâng cao hơn), hoặc Umbrel (cá nhân tôi chưa khuyến nghị vì tôi đã gặp quá nhiều vấn đề), sau đó bạn sẽ có thể kết nối ví của mình chỉ bằng cách nhập địa chỉ IP của máy tính (Raspberry Pi) đang chạy node, cộng với dấu hai chấm, và 50002, như được hiển thị trong hình ảnh ở phần trước. (Phía dưới tôi sẽ chỉ bạn cách tìm địa chỉ IP của node của bạn).

Mở cài đặt Mạng (nhấp vào vòng tròn màu xanh lá cây hoặc đỏ ở góc dưới bên phải). Bỏ chọn hộp "chọn máy chủ tự động", sau đó nhập địa chỉ IP của bạn như tôi đã làm, địa chỉ của bạn sẽ khác, nhưng dấu hai chấm và "50002" nên giống nhau.

![image](assets/18.webp)

Đóng cửa sổ, và bây giờ chúng ta nên đã kết nối với node của bạn. Để xác nhận, nhấp vào vòng tròn một lần nữa và kiểm tra xem chi tiết máy chủ có thay đổi trở lại thành một node ngẫu nhiên không.

Đôi khi, mặc dù đã làm mọi thứ đúng, dường như nó từ chối kết nối. Dưới đây là một số cách thử...

- Nâng cấp lên phiên bản mới hơn của Electrum, và phần mềm node của bạn
- Thử xóa thư mục cache trong thư mục ".electrum"
- Thử thay đổi cổng từ 50002 sang 50001 trong cài đặt mạng
- Sử dụng hướng dẫn này để kết nối sử dụng Tor như một phương án thay thế (https://armantheparman.com/tor/)
- Cài đặt lại Electrum Server trên node

## TÌM ĐỊA CHỈ IP CỦA NODE CỦA BẠN

Địa chỉ IP không phải là thứ mà người dùng thông thường thường biết cách tra cứu và sử dụng. Tôi đã giúp nhiều người chạy một node, sau đó kết nối ví của họ với node - một trở ngại thường gặp dường như là tìm địa chỉ IP của nó.

Đối với MyNode, bạn có thể gõ trong cửa sổ trình duyệt: `mynode.local`

Đôi khi, "mynode.local" không hoạt động (đảm bảo bạn không gõ nó trong thanh tìm kiếm Google. Để buộc thanh điều hướng nhận ra văn bản của bạn là một địa chỉ chứ không phải là một tìm kiếm, hãy thêm `http://` như thế này: `http://mynode.local`. Nếu điều đó không hoạt động, thử nó với một "s", như thế này: `https://mynode.local`.

Điều này sẽ truy cập vào thiết bị, và bạn có thể nhấp vào liên kết cài đặt (xem "vòng tròn" màu xanh của tôi dưới đây) để hiển thị màn hình này nơi địa chỉ IP được đặt:

![image](assets/19.webp)

Trang này sẽ tải và bạn sẽ thấy địa chỉ IP của node (vòng tròn màu xanh)

![image](assets/20.webp)

Sau đó, trong tương lai, bạn có thể gõ 192.168.0.150, hoặc http://192.168.0.150 vào trình duyệt của mình.

Đối với Raspiblitz (khi không kết nối màn hình), bạn cần một phương pháp khác (cũng hoạt động cho MyNode):

Đăng nhập vào trang web của bộ định tuyến - tại đây chúng ta sẽ tìm thấy địa chỉ IP của tất cả các thiết bị đã kết nối của bạn. Trang web của bộ định tuyến sẽ là một địa chỉ IP mà bạn nhập vào trình duyệt web. Địa chỉ của tôi là:

    http://192.168.0.1

Để lấy thông tin đăng nhập vào bộ định tuyến, bạn có thể tìm nó trong sách hướng dẫn sử dụng hoặc đôi khi ngay cả trên một nhãn dán trên chính bộ định tuyến. Tìm kiếm tên người dùng và mật khẩu. Nếu bạn không tìm thấy, thử Tên người dùng: "admin" Mật khẩu: "password"

Nếu bạn có thể đăng nhập, bạn sẽ thấy các thiết bị đã kết nối của mình và từ tên của chúng, có thể rõ ràng là node của bạn là cái nào. Địa chỉ IP sẽ ở đó.
### Nếu hai phương pháp đầu tiên không thành công, phương pháp cuối cùng sẽ hoạt động nhưng nó khá mất thời gian:
Đầu tiên, tìm địa chỉ IP của bất kỳ thiết bị nào trên mạng của bạn (máy tính hiện tại sẽ làm được).

Trên Mac, bạn sẽ tìm thấy nó trong Network preferences:

![image](assets/21.webp)

Chúng ta quan tâm đến 4 phần tử đầu tiên (192.168.0), không phải phần tử thứ 4, “166” mà bạn thấy trong hình (của bạn sẽ khác).

Đối với Linux, sử dụng dòng lệnh:

```bash
ifconfig | grep inet
```

Dấu gạch dọc là biểu tượng “pipe” và bạn sẽ tìm thấy nó dưới phím <delete>. Bạn sẽ thấy một số kết quả và một địa chỉ IP. (Bỏ qua 127.0.0.1 vì nó không phải, và bỏ qua netmask)

Đối với Windows, mở cửa sổ lệnh (cmd) và gõ:

```bash
ipconfig/all
```

và nhấn Enter. Địa chỉ IP có thể được tìm thấy trong kết quả.

Đó là phần dễ. Phần khó giờ là tìm địa chỉ IP của node của bạn – chúng ta cần phải đoán mò. Giả sử ví dụ địa chỉ IP của máy tính của bạn bắt đầu với 192.168.0.xxx, sau đó cho node của bạn, trong trình duyệt, thử: `https://192.168.0.2`

Số nhỏ nhất có thể là 2 (0 có nghĩa là bất kỳ thiết bị nào, và 1 thuộc về router) và cao nhất, tôi tin là 255 (điều này tương đương với 11111111 trong nhị phân, số lớn nhất được giữ bởi 1 byte).

Lần lượt làm việc của bạn lên đến 255. Cuối cùng, bạn sẽ dừng lại ở số chính xác mà tải trang MyNode của bạn (hoặc trang RaspiBlitz). Sau đó bạn sẽ biết số nào để nhập vào cài đặt mạng Electrum để kết nối với node của bạn.

Nó sẽ trông giống như thế này (đảm bảo bạn bao gồm dấu hai chấm và số sau đó):

![image](assets/22.webp)

> Điều hữu ích cần biết là những địa chỉ IP này là NỘI BỘ trong mạng nhà bạn. Không ai bên ngoài có thể thấy chúng và chúng không nhạy cảm. Chúng giống như các đầu số điện thoại trong một tổ chức lớn hướng dẫn bạn đến các điện thoại khác nhau.

## Xóa ví giả

Bây giờ chúng ta đã thành công kết nối với một và chỉ một node. Đây là cách Electrum sẽ tải mặc định từ bây giờ. Bạn nên xóa ví giả (Menu: file –> delete), trường hợp bạn vô tình gửi tiền vào ví không an toàn này (Nó không an toàn vì chúng ta không tạo nó theo cách an toàn).

## Tạo một ví thực hành

Sau khi xóa ví giả, bắt đầu lại và tạo một cái mới, theo cùng một cách, chỉ lần này, ghi lại các từ khóa hạt giống và giữ chúng ở nơi tương đối an toàn.

Đây là một ý tưởng tốt để học cách Electrum hoạt động với ví thực hành này, mà không cần ví cứng phức tạp (cần cho an ninh cao). Chỉ đặt một lượng nhỏ bitcoin vào ví này – Giả sử bạn sẽ mất số tiền này. Một khi thành thạo, sau đó học cách sử dụng Electrum với ví cứng.

Trong ví mới bạn đã tạo, bạn sẽ thấy một danh sách các địa chỉ. Những cái màu xanh được gọi là “địa chỉ nhận”. Chúng là sản phẩm của 3 thứ:

- Cụm từ hạt giống
- Cụm từ mật khẩu
- Đường dẫn phái sinh

Ví mới của bạn có một tập hợp các địa chỉ nhận có thể được tạo một cách toán học và có thể tái tạo bởi bất kỳ ví phần mềm nào có hạt giống, cụm từ mật khẩu và đường dẫn phái sinh. Có 4.3 tỷ cái! Nhiều hơn bạn cần. Electrum chỉ hiển thị 20 cái đầu tiên, và sau đó thêm nữa khi bạn sử dụng hết những cái đầu tiên.
Dưới đây là thông tin chi tiết hơn về khóa riêng của bitcoin có thể được tìm thấy trong hướng dẫn này.
![image](assets/23.webp)

Điều này rất khác biệt so với một số ví khác chỉ hiển thị 1 địa chỉ mỗi lần.

Vì bạn đã nhập cụm từ hạt giống khi tạo ví này, Electrum có khóa riêng cho từng địa chỉ, và việc chi tiêu từ những địa chỉ này là có thể.

Cũng lưu ý rằng có những địa chỉ màu vàng, được gọi là “địa chỉ thay đổi” – Đây chỉ là một tập hợp khác của các địa chỉ từ một nhánh toán học khác (còn tồn tại thêm 4.3 tỷ địa chỉ như vậy). Chúng được ví sử dụng để tự động gửi số tiền thừa trở lại vào ví như tiền thối. Ví dụ, nếu bạn lấy 1.5 bitcoin và chi tiêu 0.5 cho một người bán hàng, số dư 1.0 cần phải đi đâu đó. Ví của bạn sẽ chi tiêu nó vào địa chỉ thay đổi màu vàng tiếp theo trống không – nếu không, số tiền đó sẽ đi vào tay thợ mỏ! Để biết thêm thông tin về điều này (UTXOs), xem hướng dẫn này. (https://armantheparman.com/utxo/)

Tiếp theo, quay lại trang web khóa riêng của Ian Colman và nhập cụm từ hạt giống (thay vì tạo một cái mới). Bạn sẽ thấy thông tin khóa riêng và khóa công khai thay đổi phía dưới; mọi thứ phía dưới phụ thuộc vào những gì ở trên trang.

> Nhớ rằng, bạn không bao giờ nên nhập cụm từ hạt giống trên máy tính cho ví Bitcoin thực của bạn – malware có thể ăn cắp nó. Chúng tôi chỉ sử dụng một ví thực hành, cho mục đích học hỏi, nên bây giờ nó vẫn ổn.

Cuộn xuống và thay đổi đường dẫn phái sinh thành BIP84 (segwit) để phù hợp với ví Electrum của bạn bằng cách nhấp vào tab BIP84.

![image](assets/24.webp)

Phía dưới, bạn sẽ thấy khóa riêng mở rộng của tài khoản và khóa công khai mở rộng của tài khoản:

![image](assets/25.webp)

Đi đến Electrum, và so sánh chúng có khớp không. Có một menu ở phía trên, ví –> thông tin:

![image](assets/26.webp)

Cửa sổ này hiện ra:

![image](assets/27.webp)

Lưu ý rằng hai khóa công khai khớp nhau.

Tiếp theo, so sánh các địa chỉ. Quay lại trang của Ian Coleman và cuộn xuống phía dưới:

![image](assets/28.webp)

Lưu ý rằng chúng khớp với các địa chỉ trong Electrum.

Bây giờ chúng ta sẽ kiểm tra các địa chỉ thay đổi. Cuộn lên một chút đến đường dẫn phái sinh và thay đổi số 0 cuối cùng thành 1:

![image](assets/29.webp)

Bây giờ cuộn xuống và so sánh các địa chỉ khớp với các địa chỉ màu vàng trong Electrum

Tại sao chúng ta làm tất cả điều này?

Chúng ta đã lấy cụm từ hạt giống và đưa chúng qua hai chương trình phần mềm độc lập khác nhau để đảm bảo rằng chúng đang cung cấp cho chúng ta cùng một thông tin. Điều này giảm đáng kể rủi ro rằng mã độc hại đang ẩn nấp bên trong và cung cấp cho chúng ta các khóa riêng hoặc công khai giả mạo, hoặc địa chỉ.

Bước tiếp theo là nhận một lượng nhỏ thử nghiệm và chi tiêu nó trong ví từ một địa chỉ này sang địa chỉ khác.

## Kiểm tra Ví (Học cách sử dụng nó)

Ở đây tôi sẽ chỉ bạn cách nhận một UTXO vào ví của bạn và sau đó di chuyển nó (chi tiêu nó) sang một địa chỉ khác trong ví. Đây là một lượng rất nhỏ mà chúng ta không ngại mất.

Điều này có một số mục đích.

- Nó sẽ chứng minh rằng bạn có quyền lực để chi tiêu tiền trong ví mới.
- Nó sẽ hướng dẫn cách sử dụng phần mềm Electrum để thực hiện một giao dịch (và một số tính năng), trước khi chúng ta thêm độ phức tạp bổ sung cho an toàn (sử dụng ví cứng hoặc máy tính không kết nối mạng)
- Nó sẽ củng cố ý tưởng rằng bạn có nhiều địa chỉ để chọn lựa nhận và chi tiêu, trong cùng một ví.
Mở ví Electrum thử nghiệm của bạn và nhấp vào tab Địa chỉ, sau đó nhấp chuột phải vào địa chỉ đầu tiên và chọn Sao chép –> Địa chỉ:
![image](assets/30.webp)

Địa chỉ bây giờ đã được lưu trong bộ nhớ máy tính của bạn.

Bây giờ hãy đến một sàn giao dịch nơi bạn có một số bitcoin, và hãy rút một lượng nhỏ vào địa chỉ này, ví dụ 50,000 sats. Tôi sẽ sử dụng Coinbase làm ví dụ vì đây là sàn giao dịch được sử dụng phổ biến nhất, mặc dù họ là kẻ thù của Bitcoin, và tôi cảm thấy ghê tởm khi phải đăng nhập vào một tài khoản bỏ hoang vì mục đích này.

Đăng nhập, và nhấp vào nút Gửi/Nhận, tính đến thời điểm hiện tại nằm ở góc trên bên phải của trang web.

![image](assets/31.webp)

Rõ ràng tôi không có quỹ với Coinbase, nhưng hãy tưởng tượng rằng bạn có quỹ ở đây và làm theo: Dán địa chỉ từ Electrum vào trường “Đến” như tôi đã làm. Bạn cũng cần chọn một số lượng (tôi đề xuất khoảng 50,000 sats hoặc tương tự). Đừng đặt “tin nhắn tự chọn” – Coinbase đang thu thập đủ dữ liệu của bạn (và bán chúng), không cần phải giúp họ. Cuối cùng, nhấp “Tiếp tục”. Sau đó tôi không biết bạn sẽ gặp pop-up nào nữa, bạn tự xử lý, nhưng phương pháp tương tự áp dụng cho tất cả các sàn giao dịch.

![image](assets/32.webp)

Tùy thuộc vào sàn giao dịch, bạn có thể thấy sats trong ví của mình ngay lập tức, hoặc có thể có sự chậm trễ vài giờ/ngày.

Lưu ý rằng Electrum sẽ cho bạn biết bạn đã nhận được tiền ngay cả khi chúng chưa được xác nhận trên blockchain. Số tiền bạn có được đọc từ danh sách chờ của một Node Bitcoin, hay còn gọi là “mempool”. Khi nó được đưa vào một khối, bạn sẽ thấy số tiền được xác nhận.

Bây giờ chúng ta có một UTXO trong ví, chúng ta nên gắn nhãn cho nó. Chỉ chúng ta mới thấy nhãn này, nó không liên quan gì đến sổ cái công cộng. Tất cả nhãn Electrum của chúng ta chỉ hiển thị trên máy tính mà chúng ta đang sử dụng. Chúng ta thực sự có thể lưu một tệp và sử dụng nó để khôi phục tất cả nhãn của mình vào một máy tính khác chạy ví tương tự.

### Tạo nhãn cho một UTXO

Tôi cần một khoản quyên góp cho ví thử nghiệm này, cảm ơn @Sathoarder đã cung cấp cho tôi một UTXO trực tiếp (10,000 sats), và một người khác (ẩn danh) đã quyên góp cho cùng một địa chỉ (5000 sats). Lưu ý rằng có 15,000 sats trong số dư địa chỉ đầu tiên, và tổng cộng 2 giao dịch (cột ngoài cùng bên phải). Phía dưới, số dư là 10,000 sats đã được xác nhận, và 5,000 sats khác chưa được xác nhận (vẫn trong mempool).

![image](assets/33.webp)

Bây giờ, nếu chúng ta chuyển qua tab Coins, chúng ta có thể thấy hai “tiền nhận được” hoặc UTXOs. Cả hai đều ở cùng một địa chỉ.

![image](assets/34.webp)

Quay lại tab địa chỉ, nếu bạn nhấp đúp vào khu vực “nhãn” bên cạnh địa chỉ, bạn sẽ có thể nhập một số văn bản, sau đó nhấn <enter> để lưu:

![image](assets/35.webp)

Đây là một thực hành tốt để bạn có thể theo dõi nguồn gốc của tiền của mình, nếu chúng không phải là KYC hay không, và mỗi UTXO tốn bao nhiêu (trong trường hợp bạn cần bán và tính toán thuế phải nộp cho chính phủ của mình).
Lý tưởng nhất, bạn nên tránh tích lũy nhiều đồng tiền trong cùng một địa chỉ. Nếu bạn quyết định làm điều đó (không nên), bạn có thể gán nhãn cho từng đồng tiền thay vì gán cùng một nhãn cho tất cả bằng phương pháp địa chỉ. Bạn không thể trực tiếp vào tab “coins” và chỉnh sửa nhãn ở đó (không, điều đó quá trực quan rồi!). Bạn phải vào tab Lịch sử, tìm giao dịch, gán nhãn cho nó, và sau đó bạn sẽ thấy nhãn trong phần đồng tiền. Bất kỳ nhãn nào bạn thấy trong phần đồng tiền đều từ nhãn Địa chỉ HOẶC nhãn Lịch sử, nhưng bất kỳ nhãn Lịch sử nào cũng sẽ ghi đè lên nhãn Địa chỉ. Để sao lưu nhãn của bạn vào một tệp, bạn có thể xuất chúng từ menu ở trên cùng, ví–>nhãn–>xuất.

Tiếp theo, hãy chi tiêu đồng tiền từ địa chỉ đầu tiên sang địa chỉ thứ hai. Nhấp chuột phải vào địa chỉ đầu tiên và chọn “chi tiêu từ” (Thực ra điều này không cần thiết trong tình huống này, nhưng hãy tưởng tượng chúng ta có nhiều đồng tiền trong nhiều địa chỉ; sử dụng tính năng này, chúng ta có thể buộc ví chỉ chi tiêu những đồng tiền mà chúng ta muốn. Nếu chúng ta muốn chọn nhiều đồng tiền trong nhiều địa chỉ, chúng ta có thể chọn các địa chỉ bằng cách nhấp chuột trái trong khi giữ phím lệnh, sau đó nhấp chuột phải và chọn “chi tiêu từ”:

![hình ảnh](assets/36.webp)

Một khi bạn làm điều đó, sẽ có một thanh màu xanh ở phía dưới cửa sổ ví chỉ ra số lượng đồng tiền bạn đã chọn và tổng số có thể chi tiêu.

Bạn cũng có thể chi tiêu từng đồng tiền riêng lẻ trong một địa chỉ và loại trừ những đồng khác trong cùng một địa chỉ, nhưng điều này không được khuyến khích vì bạn đang để lại đồng tiền trong một địa chỉ đã bị yếu đi về mặt mật mã do việc chi tiêu một trong những đồng tiền (một lý do khác không nên để nhiều đồng tiền trong một địa chỉ, ngoài lý do về quyền riêng tư, là vì nếu bạn chi tiêu một, bạn nên chi tiêu tất cả, điều này trở nên tốn kém không cần thiết). Đây là cách chọn một đồng tiền duy nhất từ một địa chỉ chung, nhưng đừng làm vậy:

![hình ảnh](assets/37.webp)

Bây giờ, chúng ta đã chọn hai đồng tiền để chi tiêu. Tiếp theo, chúng ta quyết định nơi để chi tiêu chúng. Hãy gửi chúng đến địa chỉ thứ hai. Chúng ta cần sao chép địa chỉ như sau:

![hình ảnh](assets/38.webp)

Sau đó vào tab “Gửi”, và dán địa chỉ thứ hai vào trường “thanh toán cho”. Không cần thêm mô tả; bạn có thể làm, nhưng bạn có thể làm điều đó sau bằng cách chỉnh sửa nhãn. Đối với số lượng, chọn “Max” để chi tiêu tất cả các đồng tiền đã chọn. Sau đó nhấp “Thanh toán”, và sau đó nhấp vào nút “nâng cao” trên cửa sổ pop-up xuất hiện.

![hình ảnh](assets/39.webp)

Luôn nhấp vào “nâng cao” ở giai đoạn này để chúng ta có thể kiểm soát kỹ lưỡng và kiểm tra chính xác những gì có trong giao dịch. Đây là giao dịch:

![hình ảnh](assets/40.webp)

Chúng ta thấy hai hộp cửa sổ màu trắng bên trong. Cửa sổ trên cùng là cửa sổ đầu vào (những đồng tiền đang được chi tiêu), và cửa sổ dưới cùng là cửa sổ đầu ra (nơi đồng tiền đi đến).

Lưu ý, trạng thái (góc trên bên trái) hiện tại là “chưa ký”. “Số tiền gửi” là 0 vì đồng tiền đang được chuyển trong ví. Phí là 481 sats. Lưu ý rằng nếu nó là 480 sats, số không cuối cùng sẽ bị bỏ đi, như thế này, 0.0000048 và đối với mắt mệt mỏi, điều này có thể trông giống như 48 sats – hãy cẩn thận (điều mà các nhà phát triển Electrum nên sửa).
Kích thước của giao dịch ám chỉ đến kích thước dữ liệu tính bằng byte, không phải là số lượng bitcoin. Tính năng "replace by fee" được bật mặc định, cho phép bạn gửi lại giao dịch với mức phí cao hơn nếu cần. LockTime cho phép bạn điều chỉnh thời gian giao dịch có hiệu lực - Tôi chưa thử nghiệm với tính năng này, nhưng khuyên bạn không sử dụng nó trừ khi bạn hoàn toàn hiểu bạn đang làm gì và đã có kinh nghiệm thực hành với số lượng nhỏ.

Ở phía dưới, chúng ta có một số công cụ điều chỉnh phí khai thác mỏ phức tạp. Tất cả những gì bạn cần làm cho các giao dịch nội bộ là thiết lập mức phí tối thiểu là 1 sat/byte. Chỉ cần nhập số vào trường Phí Mục tiêu. Để kiểm tra mức phí phù hợp cho một khoản thanh toán bên ngoài, bạn có thể tham khảo https://mempool.space để xem mempool đang bận rộn như thế nào, và một số mức phí đề xuất được hiển thị.

![image](assets/41.webp)

Tôi đã chọn 1 sat/byte.

Trong cửa sổ nhập, chúng ta thấy hai mục nhập. Mục đầu tiên là quyên góp 5000 sat. Chúng ta thấy ở bên trái là hash giao dịch của nó (mà chúng ta có thể tra cứu trên blockchain). Kế bên nó, có một "21" - điều này chỉ ra rằng đó là đầu ra được gắn nhãn 21 trong giao dịch đó (thực tế là đầu ra thứ 22 vì đầu ra đầu tiên được gắn nhãn là không).

Điều cần lưu ý ở đây: UTXOs chỉ tồn tại bên trong một giao dịch. Để chi tiêu một UTXO, chúng ta phải tham chiếu nó, và đặt tham chiếu đó vào đầu vào của một giao dịch mới. Các đầu ra sau đó trở thành UTXOs mới và UTXO cũ trở thành STXO (Spent transaction output).

Dòng thứ hai là quyên góp 10,000 sat. Nó có một "0" kế bên hash giao dịch mà nó đến từ đó vì đó là đầu ra đầu tiên (và có thể là duy nhất) cho giao dịch đó.

Ở cửa sổ dưới cùng, chúng ta thấy địa chỉ của mình. Lưu ý tổng số bitcoin của các đầu vào không hoàn toàn khớp với tổng số của các đầu ra. Sự chênh lệch được chuyển cho thợ mỏ. Thợ mỏ xem xét sự chênh lệch trong tất cả các giao dịch trong khối mà nó đang cố gắng khai thác, và thêm số đó vào phần thưởng của mình. (Phí khai thác theo cách này hoàn toàn tách biệt khỏi chuỗi giao dịch và bắt đầu một cuộc sống mới).

Nếu chúng ta điều chỉnh phí khai thác, giá trị đầu ra sẽ tự động thay đổi.

> Điều đáng chú ý ở đây: Chú ý đến màu sắc của các địa chỉ trong cửa sổ giao dịch. Nhớ rằng các địa chỉ màu xanh lá cây được liệt kê trong tab địa chỉ của bạn. Nếu một địa chỉ được làm nổi bật bằng màu xanh lá cây (hoặc vàng) trong cửa sổ giao dịch, thì Electrum đã nhận ra địa chỉ đó là một trong những địa chỉ của mình. Nếu địa chỉ không được làm nổi bật, thì đó là một địa chỉ bên ngoài (ngoài ví đang mở), và bạn nên kiểm tra nó với sự cẩn thận extra.

Một khi bạn kiểm tra mọi thứ trong giao dịch và chắc chắn bạn hài lòng với việc bạn đang chi tiêu những đồng xu nào, và những đồng xu đó đang đi đâu, bạn có thể nhấp vào “finalise.”

![image](assets/42.webp)

Sau khi bạn nhấp vào “finalise”, bạn không thể chỉnh sửa nữa – Nếu bạn cần, bạn phải đóng này và bắt đầu lại. Lưu ý rằng nút “finalise” đã thay đổi thành “export”, và các nút mới xuất hiện: “save”, “combine”, “sign” và “broadcast”. Nút “broadcast” bị mờ vì giao dịch chưa được ký và do đó không hợp lệ ở giai đoạn này.

Một khi bạn nhấp vào sign, nếu bạn có mật khẩu cho ví, bạn sẽ được nhắc nhập mật khẩu đó, và sau đó trạng thái (phía trên bên phải) sẽ thay đổi từ “Unsigned” thành “Signed”. Sau đó nút “Broadcast” sẽ có thể sử dụng.
Sau khi bạn phát sóng, bạn có thể đóng cửa sổ giao dịch. Nếu bạn chuyển đến tab địa chỉ, bạn sẽ thấy địa chỉ đầu tiên trống, và địa chỉ thứ hai có 1 UTXO.
Lưu ý: Bạn sẽ thấy tất cả những thay đổi này ngay cả trước khi giao dịch được khai thác vào một khối, hay "xác nhận". Điều này là bởi vì Electrum cập nhật số dư/giao dịch dựa trên không chỉ dữ liệu blockchain, mà còn dữ liệu mempool nữa. Không phải tất cả ví đều làm điều này.

Một điều cần chỉ ra là thay vì phát sóng, chúng ta có thể lưu giao dịch để sử dụng sau. Nó có thể được lưu ở trạng thái chưa ký hoặc đã ký.

Nhấn nút "export" (một cách nghịch lý, KHÔNG nhấn vào nút "save"), và bạn sẽ thấy một số lựa chọn. Giao dịch được mã hóa bằng văn bản, và do đó có thể được lưu theo một số cách.

![hình ảnh](assets/43.webp)

Lưu thành mã QR rất thú vị. Nếu bạn chọn điều này, một mã QR sẽ xuất hiện:

![hình ảnh](assets/44.webp)

Bạn có thể chụp ảnh mã QR đó. Có một số việc bạn có thể làm với nó, nhưng bây giờ, hãy chỉ nói rằng bạn đang tải nó trở lại vào ví sau. Bạn có thể đóng Electrum, tải lại ví, và đi đến menu Công cụ:

![hình ảnh](assets/45.webp)

Điều này sẽ kích hoạt camera của máy tính bạn. Sau đó bạn chỉ camera vào ảnh mã QR trong điện thoại của bạn, và điều này sẽ tải lại giao dịch, y hệt như bạn đã để lại.

Việc tải một giao dịch đã lưu không phải là điều trực quan, vì vậy hãy chú ý đặc biệt. Tải một giao dịch không phải là một "công cụ" nhưng lựa chọn này được ẩn trong menu công cụ (một điều mà các nhà phát triển Electrum nên sửa).

Một quy trình tương tự có thể thực hiện với một giao dịch được lưu dưới dạng một tệp. Hãy thử thực hành với bất kỳ phương pháp nào, trong cùng một ví. Tôi sẽ không đi qua nó ở đây nhưng bạn có thể sử dụng tính năng này để chuyển một giao dịch qua lại giữa cùng một ví trên các máy tính khác nhau, giữa các ví đa chữ ký, và từ và đến các ví phần cứng. Dưới đây là một số hướng dẫn.

Bây giờ, quay lại với nút "save" – đây không phải là cách để lưu văn bản giao dịch. Điều này thực sự làm là báo cho ví Electrum biết rằng giao dịch này trên máy tính cục bộ được gửi như một khoản thanh toán. Nếu bạn làm điều đó một cách vô tình, bạn sẽ thấy giao dịch với một biểu tượng máy tính nhỏ. Bạn có thể nhấp chuột phải và xóa giao dịch – đừng lo, bạn không thể xóa bitcoin theo cách này. Electrum sẽ sau đó quên rằng giao dịch này từng xảy ra, và sẽ "hoàn lại" các sats và hiển thị các sats ở vị trí chính xác nơi chúng thực sự tồn tại.

### Địa chỉ thay đổi

Địa chỉ thay đổi là thú vị. Bạn cần hiểu về UTXOs để hiểu giải thích này. Nếu bạn chi tiêu cho một địa chỉ một số tiền nhỏ hơn UTXO, thì số bitcoin còn lại sẽ đi vào tay thợ mỏ trừ khi một đầu ra thay đổi được chỉ định.

Bạn có thể có một UTXO 6.15 bitcoin và muốn chi tiêu 0.15 bitcoin để quyên góp cho một số người biểu tình đang bị áp bức bởi chính phủ “dân chủ” độc tài nào đó trên thế giới. Bạn sẽ lấy 6.15 bitcoin (sử dụng chức năng "chi tiêu từ" trong Electrum), và đặt nó vào một giao dịch.

Bạn sẽ dán địa chỉ của người biểu tình vào trường "pay to", có thể bạn sẽ đặt "EndTheFed & WEF" vào trường "description", và cho số lượng, bạn sẽ đặt 0.15 bitcoin và nhấn "pay", sau đó "advanced".
Trong màn hình giao dịch, tại cửa sổ nhập, bạn sẽ thấy UTXO 6.15 bitcoin. Đối với cửa sổ xuất, bạn sẽ thấy một địa chỉ không được làm nổi bật (đây là địa chỉ của người biểu tình) với 0.15 bitcoin bên cạnh. Bạn cũng sẽ thấy một địa chỉ màu vàng với số lượng bitcoin nhỏ hơn một chút so với 6.0. Đây là địa chỉ nhận tiền lẻ được ví tự động chọn từ một trong số các địa chỉ tiền lẻ màu vàng của chính nó. Mục đích của địa chỉ nhận tiền lẻ là để ví có thể đặt tiền lẻ vào đó mà không làm ảnh hưởng đến khả năng sử dụng của các địa chỉ nhận tiền mà bạn có thể có kế hoạch sử dụng, hoặc đã gửi hóa đơn cho. Nếu chúng sẽ được sử dụng sau này bởi khách hàng, ví dụ, bạn không muốn ví của mình tự động sử dụng chúng và làm đầy chúng. Điều này lộn xộn và không tốt cho quyền riêng tư.
Lưu ý rằng khi bạn điều chỉnh phí khai thác, số lượng tiền lẻ xuất sẽ tự động điều chỉnh, không phải số lượng thanh toán.

### Thay đổi thủ công hoặc thanh toán cho nhiều người

Đây là một tính năng thực sự thú vị của Electrum. Bạn truy cập nó như thế này.

![hình ảnh](assets/46.webp)

Sau đó, bạn có thể nhập nhiều điểm đến cho số dư UTXO mà bạn đang chi tiêu, như thế này:

![hình ảnh](assets/47.webp)

Dán địa chỉ, gõ vào một dấu phẩy, sau đó là một khoảng trắng, sau đó là số lượng, sau đó <enter>, sau đó làm lại. KHÔNG NHẬP SỐ LƯỢNG TRONG CỬA SỔ “SỐ LƯỢNG” – Electrum sẽ điền tổng số ở đây khi bạn gõ các số lượng cá nhân vào cửa sổ “Thanh toán cho”.

Điều này cho phép bạn tự xác định nơi tiền lẻ đi (ví dụ một địa chỉ cụ thể trong ví của bạn, hoặc một ví khác), hoặc bạn có thể thanh toán cho nhiều người cùng một lúc. Nếu tổng số của bạn không đủ cao để tương ứng với kích thước của UTXO, Electrum vẫn sẽ tạo một đầu ra tiền lẻ bổ sung cho bạn.

Tính năng Thanh toán cho Nhiều người cũng cho phép khả năng tạo ra “PayJoins” hoặc “CoinJoins” của riêng bạn – nằm ngoài phạm vi của bài viết này, nhưng tôi có một hướng dẫn ở đây. (https://armantheparman.com/cj/)

## Ví

Tôi muốn giới thiệu một Ví Chỉ Xem sử dụng Electrum. Để làm điều đó, tôi cần định nghĩa trước “ví”. Có hai cách “ví” được sử dụng trong Bitcoin:

- Loại A, “ví” – chỉ phần mềm hiển thị địa chỉ và số dư của bạn, ví dụ Electrum, Blue Wallet, Sparrow Wallet, v.v.

- Loại B, “ví” – chỉ bộ sưu tập địa chỉ độc đáo được liên kết với sự kết hợp của seed_phrase/passphrase/derivation_path của chúng ta. Có 8.6 tỷ địa chỉ trong bất kỳ ví nào (4.3 tỷ địa chỉ nhận và 4.3 tỷ địa chỉ tiền lẻ). Nếu bạn thay đổi bất cứ thứ gì trong seed phrase, passphrase, hoặc derivation path, bạn sẽ nhận được một ví chưa sử dụng với 8.6 tỷ địa chỉ trống mới, và tất cả đều độc đáo.

Loại ví nào được người ta đề cập khi sử dụng từ “ví” là rõ ràng trong ngữ cảnh.

## Ví Chỉ Xem – một bài tập

Không hoàn toàn rõ ràng ví chỉ xem dùng để làm gì, nhưng tôi sẽ bắt đầu bằng cách giải thích nó là gì, cách tạo một ví thực hành, và sau đó chúng ta sẽ quay lại mục đích của nó sau khi tôi giải thích thêm về ví cứng. (Đối với một bài đánh giá chi tiết về cách sử dụng ví cứng, và các thương hiệu cụ thể, xem ở đây.)
Chúng ta sẽ tạo một ví tiền ảo thông thường (lần này thêm một chút phức tạp với mật khẩu cụ thể), và sau đó là ví theo dõi tương ứng. Nếu bạn muốn, bạn có thể sao chép chính xác ví mà tôi đã tạo, hoặc tạo ví của riêng bạn - ví này sẽ được loại bỏ; đừng thực sự sử dụng nó. Bắt đầu bằng cách tạo một chuỗi 12 từ khóa sử dụng trang web của Ian Coleman.
Chú ý đến 12 từ ngẫu nhiên trong ảnh chụp màn hình dưới đây, và tôi đã nhập một mật khẩu cụ thể vào trường mật khẩu cụ thể:

MẬT KHẨU CỤ THỂ: “Craig Wright là kẻ nói dối và lừa đảo và nên bị giam cầm. Ngoài ra, Ross Ulbricht nên được thả tự do ngay lập tức.”

Mật khẩu cụ thể có thể dài tới 100 ký tự, và lý tưởng nên rõ ràng và không quá ngắn - Mật khẩu cụ thể tôi đã sử dụng chỉ là cho vui - Tôi thường khuyên tránh sử dụng chữ cái in hoa và ký hiệu chỉ để giảm bớt căng thẳng khi thử các kết hợp nếu bạn từng gặp vấn đề với việc nhớ mật khẩu cụ thể của mình.

![image](assets/48.webp)

Tiếp theo, trong Electrum, đi tới menu file–>new/restore. Đặt một tên duy nhất để tạo ví mới và nhấn “next”.

![image](assets/49.webp)

Các bước tiếp theo bạn nên đã quen thuộc bây giờ, vì vậy tôi sẽ liệt kê chúng mà không cần hình ảnh:

- Ví tiêu chuẩn
- Tôi đã có seed
- Sao chép và dán 12 từ vào ô, hoặc nhập chúng thủ công.
- Nhấn vào tùy chọn và chọn BIP39, và cũng nhấn vào dấu kiểm mật khẩu cụ thể (“mở rộng seed này với từ tùy chỉnh”)
- Nhập mật khẩu cụ thể của bạn chính xác như bạn đã làm trên trang của Ian Coleman
- Để nguyên ngữ nghĩa kịch bản và đường dẫn xuất phát mặc định
- Không cần thêm mật khẩu (khóa ví)

Bây giờ quay lại trang của Ian Coleman, xuống phần “đường dẫn xuất phát”, và nhấn vào tab “BIP 84” để chọn ngữ nghĩa kịch bản giống như mặc định trong Electrum (Native Segwit).

![image](assets/50.webp)

Khóa riêng và khóa công khai mở rộng ngay bên dưới, và chúng thay đổi khi bạn thực hiện thay đổi đến đường dẫn xuất phát (hoặc bất cứ thứ gì khác ở phần trên của trang).

![image](assets/51.webp)

Bạn cũng sẽ thấy “khóa riêng/khóa công khai mở rộng BIP32” - những khóa này sẽ được bỏ qua lúc này.

Khóa riêng mở rộng của tài khoản có thể được sử dụng để tái tạo hoàn toàn ví của bạn. Tuy nhiên, khóa công khai mở rộng của tài khoản chỉ có thể tạo ra một phiên bản giới hạn của cùng một ví (ví theo dõi) - Nếu bạn đặt khóa này vào Electrum, nó vẫn sẽ tạo ra tất cả 8.6 tỷ địa chỉ mà seed hoặc khóa riêng mở rộng có thể có, nhưng sẽ không có khóa riêng nào có sẵn cho Electrum, vì vậy không thể thực hiện giao dịch. Hãy làm điều này ngay bây giờ để minh họa điểm này:

Sao chép “khóa công khai mở rộng của tài khoản” vào clipboard.

Sau đó đi tới Electrum, để ví hiện tại chúng ta đã tạo mở, và đi tới file–>new/restore. Quy trình tạo ví hơi khác so với trước:

- Ví tiêu chuẩn
- Sử dụng một khóa chính
- Dán khóa công khai mở rộng vào ô và tiếp tục
- Không cần nhập mật khẩu cụ thể; nó đã là một phần của khóa công khai mở rộng
- Không cần nhập ngữ nghĩa kịch bản và đường dẫn xuất phát
- Không cần thêm mật khẩu (khóa ví)

Khi ví được tải, bạn sẽ nhận thấy rằng chính xác cùng một địa chỉ được tải như trước khi seed được nhập. Bạn cũng sẽ chú ý ở phía trên cùng trong thanh tiêu đề, nó nói “ví theo dõi”. Ví này có thể cho bạn xem địa chỉ và số dư của bạn (bằng cách kiểm tra số dư qua một nút), nhưng bạn không thể KÝ giao dịch (vì ví theo dõi không có khóa riêng).
Vậy thì mục đích của nó là gì?
Một lý do, không phải là lý do chính, là bạn có thể quan sát ví và số dư của mình trên máy tính mà không cần phơi bày khóa riêng tư của mình cho bất kỳ phần mềm độc hại nào trên máy tính.

Một lý do khác là nó là ĐIỀU KIỆN BẮT BUỘC để thực hiện thanh toán nếu bạn chọn giữ khóa riêng tư của mình ngoài máy tính; Tôi sẽ giải thích:

> Ví cứng (HWW) được tạo ra để một thiết bị có thể giữ khóa riêng tư của bạn một cách an toàn (được khóa bằng mã PIN), không bao giờ tiết lộ khóa cho máy tính (ngay cả khi được kết nối với máy tính qua cáp), và chính nó không thể kết nối với internet. Một thiết bị như vậy không thể thực hiện giao dịch một mình vì tất cả giao dịch bitcoin bắt đầu bằng cách tham chiếu đến một UTXO(s) trên blockchain (nằm trên một nút). Ví phải chỉ định ID giao dịch nào chứa UTXO, và đầu ra nào của giao dịch là cái sẽ được chi tiêu. Chỉ sau khi chỉ định đầu vào, một giao dịch mới có thể được tạo ra trước tiên, chứ đừng nói đến việc được ký. Ví cứng không thể tạo giao dịch vì chúng không có quyền truy cập vào bất kỳ UTXO nào - chúng không được kết nối với bất cứ thứ gì! Một khóa công khai mở rộng thường được trích xuất từ HWW, và địa chỉ sau đó được hiển thị trên máy tính - nhiều người sẽ quen thuộc với phần mềm Ledger hoặc Trezor Suite hiển thị địa chỉ và số dư trên máy tính của họ - đây là một ví quan sát. Những chương trình này có thể tạo giao dịch, nhưng không thể ký. Chúng chỉ có thể có giao dịch được ký bởi HWWs được kết nối với chúng. HWW nhận giao dịch mới được tạo từ ví quan sát, ký nó, và sau đó gửi lại cho máy tính để phát sóng đến một nút. HWW không thể phát sóng một mình, ví quan sát liên kết của nó làm điều đó. Theo cách này, hai ví (ví khóa công khai trên máy tính, và ví khóa riêng tư trong HWW) hợp tác để tạo ra, ký và phát sóng, tất cả trong khi đảm bảo khóa riêng tư được cô lập và tránh xa thiết bị kết nối internet.

## Giao Dịch Bitcoin Được Ký Một Phần (PSBTs)

Có thể tạo một giao dịch và lưu vào tệp, sau đó tải lại, ký, lưu, tải lại và cuối cùng phát sóng - Tôi không nói rằng ai cũng cần làm điều này; đó chỉ là một điều có thể thực hiện được.

Bây giờ xem xét một ví đa chữ ký 3 trên 5 - 5 khóa riêng tư tạo ra một ví, và 3 khóa cần thiết để ký đầy đủ một giao dịch (Xem tại đây để tìm hiểu thêm về khóa ví đa chữ ký). Có thể có 5 máy tính khác nhau mỗi máy với một trong năm khóa riêng tư.

Máy tính thứ nhất có thể tạo một giao dịch và ký nó. Sau đó, nó có thể lưu vào tệp và gửi qua email cho Máy tính 2. Máy tính 2 sau đó có thể ký, và có thể lưu tệp vào một mã QR, và truyền mã QR qua cuộc gọi Zoom cho Máy tính 3 ở phía bên kia của thế giới. Máy tính 3 có thể chụp mã QR, tải giao dịch vào electrum, và ký giao dịch. Sau 2 chữ ký đầu tiên, giao dịch là một PSBT (giao dịch bitcoin được ký một phần). Sau chữ ký thứ 3, giao dịch trở nên được ký đầy đủ và hợp lệ, sẵn sàng để phát sóng.

Để tìm hiểu thêm về PSBTS, xem hướng dẫn này. (https://armantheparman.com/psbt/)

## Sử Dụng Ví Cứng với Electrum

Tôi có một hướng dẫn về việc sử dụng ví cứng nói chung, mà tôi nghĩ sẽ quan trọng cho những người mới làm quen với HWWs, để đọc. (https://armantheparman.com/using-hwws/)
Cũng có các hướng dẫn về việc kết nối các loại ví cứng HWWs với Sparrow Bitcoin Wallet tại đây. (https://armantheparman.com/hwws/)
Đây sẽ là hướng dẫn đầu tiên của tôi về cách sử dụng ví cứng với Electrum - Tôi sẽ sử dụng ví cứng ColdCard để minh họa. Điều này không nhằm mục đích là một hướng dẫn chi tiết về ColdCard cụ thể, hướng dẫn đó ở đây. Tôi chỉ trình bày các điểm cụ thể về Electrum. (https://armantheparman.com/cc/)

### Kết nối qua thẻ micro SD (không kết nối mạng)

Trước khi kết nối ví thực của bạn qua ColdCard, tôi hy vọng bạn đã thực hiện các bước trước đó như tải ví Electrum giả mạo và thiết lập các tham số mạng.

Sau đó, trên ColdCard, hãy chèn thẻ SD. Tôi giả định bạn đã tạo seed của mình. Nếu bạn truy cập ví bằng mật khẩu, hãy áp dụng nó ngay bây giờ. Cuộn xuống và chọn menu Advanced/Tools –>Export Wallet –> Electrum Wallet.

Bạn có thể cuộn xuống và đọc thông điệp. Nó luôn đề nghị bạn chọn “1” để nhập một số tài khoản khác không (một phần của đường dẫn phái sinh), nhưng nếu bạn theo lời khuyên của tôi, bạn không đã thay đổi các đường dẫn phái sinh mặc định nên bạn sẽ không muốn một số tài khoản khác không; chỉ cần nhấn dấu kiểm để tiếp tục.

Sau đó chọn ngữ nghĩa kịch bản. Hầu hết mọi người sẽ chọn “Native Segwit”.

Nó sẽ thông báo “Electrum wallet file written”, và sẽ hiển thị tên file. Hãy ghi nhớ nó.

Sau đó lấy thẻ micro SD ra và đặt nó vào máy tính có Electrum.

Một số hệ điều hành sẽ tự động mở trình duyệt file khi bạn chèn thẻ microSD. Nhiều người sẽ thấy file ví mới và nhấp đúp vào nó, và tự hỏi tại sao nó không hoạt động. Đó không phải là thiết kế tốt. Bạn thực sự phải bỏ qua trình duyệt file (đóng nó), và mở file ví bằng Electrum:

Mở Electrum. Nếu nó đã mở với ví khác, chọn file –> new. Chúng ta đang tìm cửa sổ này:

![image](assets/52.webp)

Đây là mẹo, nó không trực quan. Nhấp “choose”. Sau đó điều hướng hệ thống file trên thẻ microSD và tìm file ví và mở nó.

Bây giờ bạn đã mở ví theo dõi tương ứng của ví cứng. Tốt.

### Kết nối qua cáp USB.

Cách này nên dễ dàng hơn, nhưng đối với máy tính Linux, nó khó khăn hơn nhiều. Một cái gọi là “Udev rules” cần được cập nhật. Dưới đây là cách thực hiện (hướng dẫn chi tiết https://armantheparman.com/gpg-articles/ ), và một cách ngắn gọn:

Nên đảm bảo hệ thống được cập nhật. Sau đó:

```bash
sudo apt-get install libusb-1.0-0-dev libudev-dev
```

sau đó...

```bash
python3 -m pip install ckcc-protocol
```

Nếu bạn gặp lỗi hãy đảm bảo pip đã được cài đặt. Bạn có thể kiểm tra với (pip –version), và bạn có thể cài đặt nó với (sudo apt install python3-pip)

Tạo hoặc chỉnh sửa, file, /etc/udev/rules.d/

Như thế này:

```bash
sudo nano /etc/udev/rules.d
```

Một trình soạn thảo văn bản sẽ mở ra. Sao chép văn bản từ đây và dán nó vào file rules.d, lưu và thoát.

![image](assets/53.webp)

Sau đó chạy các lệnh này lần lượt:

```bash
sudo groupadd plugdev
sudo usermod -aG plugdev $(whoami)
sudo udevadm control –reload-rules && sudo udevadm trigger
```
Nếu bạn nhận được thông báo “nhóm plugdev” đã tồn tại, không sao cả, tiếp tục thực hiện. Sau lệnh thứ hai, bạn sẽ không nhận được phản hồi/trả lời, chỉ cần tiếp tục sang lệnh thứ ba.
Bạn có thể cần phải ngắt kết nối và sau đó kết nối lại ColdCard với máy tính.

Nếu sau tất cả những điều này bạn vẫn không thể kết nối ColdCard, tôi sẽ thử cập nhật firmware (hướng dẫn sẽ sớm có, nhưng hiện tại, bạn có thể tìm hướng dẫn trên trang web của nhà sản xuất).

Tiếp theo, tạo một ví mới:

- Ví tiêu chuẩn
- Sử dụng một thiết bị phần cứng
- Nó sẽ quét và phát hiện ColdCard của bạn. Tiếp tục.
- Chọn ngữ pháp kịch bản và đường dẫn phái sinh
- Quyết định xem tệp ví có nên được mã hóa hay không (khuyến nghị)

### Giao dịch sử dụng ColdCard

Với cáp kết nối, việc giao dịch rất dễ dàng. Việc ký giao dịch sẽ diễn ra mượt mà.

Nếu sử dụng thiết bị theo cách không kết nối mạng, bạn phải thủ công chuyển giao dịch đã lưu giữa các thiết bị sử dụng thẻ microSD. Có một số mẹo.

Sau khi tạo một giao dịch và hoàn tất nó, bạn cần nhấp vào nút xuất ở góc dưới bên trái. Bạn sẽ thấy “lưu vào tệp” mà trái với bản năng, không phải là điều chúng ta muốn. Thực sự bạn phải trước tiên đi đến tùy chọn menu cuối cùng nói “cho ví phần cứng”, và sau đó, từ trong lựa chọn đó, tìm “lưu vào tệp” khác và chọn nó. Sau đó lưu tệp vào thẻ microSD, lấy thẻ ra và đặt vào ColdCard. Nhớ rằng bạn có thể cần áp dụng một cụm mật khẩu để chọn ví đúng. Màn hình sẽ hiển thị sẵn sàng để ký. Nhấp vào dấu kiểm, kiểm tra giao dịch, và tiếp tục xác nhận bằng dấu kiểm. Khi xong, lấy thẻ ra và đặt lại vào máy tính.

Sau đó chúng ta cần mở giao dịch sử dụng electrum. Chức năng này được ẩn trong menu công cụ –> tải giao dịch. Duyệt hệ thống tệp và tìm tệp. Sẽ có ba tệp mỗi lần bạn ký. Tệp đã lưu gốc mà Ví Quan Sát tạo ra, và hai tệp do ColdCard tạo ra (tôi không biết tại sao nó làm như vậy). Một sẽ nói “đã ký” và một sẽ nói “cuối cùng”. Điều này không trực quan nhưng tệp “đã ký” không hữu ích, chúng ta cần mở giao dịch “cuối cùng”.

Khi bạn tải nó, bạn có thể nhấp vào “phát sóng” và thanh toán sẽ được thực hiện.

## Cập nhật Electrum và thư mục ẩn “.electrum”

Electrum tồn tại trên máy tính của bạn ở hai nơi. Có ứng dụng thực sự, và có một thư mục cấu hình ẩn. Thư mục này nằm ở những nơi khác nhau tùy thuộc vào hệ điều hành của bạn:

Windows:

> C:/Users/ten_nguoi_dung_cua_ban/AppData/Roaming/Electrum

Mac:

> /Users/ten_nguoi_dung_cua_ban/.electrum

Linux:

> /home/ten_nguoi_dung_cua_ban/.electrum

Lưu ý rằng “.” trước “electrum” trong Linux và Mac – điều này chỉ ra rằng thư mục được ẩn. Cũng lưu ý rằng thư mục này chỉ được tạo (tự động) một khi bạn chạy Electrum lần đầu tiên. Thư mục chứa tệp cấu hình electrum và cũng chứa thư mục chứa bất kỳ ví nào bạn đã lưu.

Nếu bạn xóa chương trình Electrum khỏi máy tính của mình, thư mục ẩn sẽ vẫn còn lại, trừ khi bạn chủ động xóa nó nữa.
Để nâng cấp Electrum, bạn thực hiện cùng một quy trình như tôi đã mô tả ở đầu để tải xuống và xác minh. Sau đó, bạn sẽ có hai bản của chương trình trên máy tính của mình, và bạn có thể chạy bất kỳ bản nào – mỗi chương trình sẽ truy cập vào cùng một thư mục electrum ẩn cho cấu hình và truy cập ví của mình. Tất cả những gì chúng ta đã lưu, như đơn vị cơ bản, nút mặc định để kết nối, các tùy chọn khác, và truy cập vào ví, sẽ được giữ nguyên vì tất cả những điều đó được lưu trong thư mục đó.

### Chuyển Electrum và Ví của bạn sang máy tính khác

Để làm điều này, bạn có thể sao chép các tệp chương trình vào ổ USB, và cũng sao chép thư mục .electrum. Sau đó sao chép hoặc di chuyển chúng sang máy tính mới. Bạn không cần phải xác minh lại chương trình. Hãy chắc chắn sao chép thư mục .electrum vào vị trí mặc định (nhớ sao chép nó TRƯỚC khi chạy Electrum lần đầu tiên trên máy tính đó, nếu không một thư mục .electrum mặc định trống sẽ được tạo ra, và bạn có thể sẽ bị nhầm lẫn).

## Nhãn

Như tôi đã giải thích trước đó, trên tab địa chỉ, có một cột nhãn. Bạn có thể nhấp đúp vào đó và nhập ghi chú cho bản thân (chỉ có trên máy tính của bạn, không công khai, và không trên blockchain).

![hình ảnh](assets/54.webp)

Khi chuyển ví Electrum của bạn sang máy tính khác, bạn có thể không muốn mất tất cả những ghi chú này. Bạn có thể sao lưu chúng vào một tệp sử dụng menu, ví–> nhãn –>xuất, và sau đó trên máy tính mới, sử dụng ví–>nhãn–>nhập.

## Mẹo:

Nếu bạn thấy nguồn thông tin này hữu ích, và bạn muốn hỗ trợ những gì tôi làm cho Bitcoin, bạn có thể quyên góp một số sats tại đây:

Địa chỉ Lightning Tĩnh: dandysack84@walletofsatoshi.com
https://armantheparman.com/electrum/