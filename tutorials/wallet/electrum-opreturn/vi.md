---
name: Electrum OP_RETURN
description: Đăng ký tin nhắn trên Blockchain Bitcoin với Electrum
---

![cover](assets/cover.webp)




Hướng dẫn từng bước này sẽ chỉ cho bạn cách viết tin nhắn trên Blockchain Bitcoin bằng cách sử dụng Electrum Wallet. Thao tác này sử dụng lệnh OP_RETURN để chèn văn bản vào giao dịch, hiển thị công khai trên Blockchain. Hãy làm theo các bước đơn giản sau để đăng ký thành công.



---
## Điều kiện tiên quyết





- Một máy tính (Windows, macOS hoặc Linux).
- Kết nối Internet.
- Một vài satoshi (Sats) hoặc bitcoin (BTC) trong Wallet của bạn để trang trải số tiền giao dịch và phí.
- Bộ chuyển đổi văn bản sang hex (ví dụ: trang web trực tuyến) hoặc công cụ chuyên dụng như [trình tạo tập lệnh OP_RETURN này](https://resources.davidcoen.it/opreturnelectrum/).



---

## Bước 1: Tải xuống và cài đặt Electrum



![image](assets/fr/01.webp)



1. Truy cập trang web chính thức của Electrum: [electrum.org](https://electrum.org/).


2. Tải xuống phiên bản tương ứng với hệ điều hành của bạn (Windows, macOS, Linux).


3. Cài đặt Electrum theo hướng dẫn của trình cài đặt.


4. Kiểm tra tính toàn vẹn của tệp đã tải xuống (tùy chọn, nhưng được khuyến nghị vì lý do bảo mật) bằng cách so sánh chữ ký của tệp hoặc Hash.



→ Chi tiết hơn về hướng dẫn Electrum:



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Bước 2: Tạo hoặc nhập Wallet



1. Khởi chạy Electrum.


2. Chọn Tạo Wallet mới hoặc Khôi phục Wallet hiện có nếu bạn đã có cụm từ seed (cụm từ khôi phục).


3. Làm theo hướng dẫn để cấu hình Wallet của bạn:




 - Đối với bài thi Wallet mới, hãy ghi lại câu seed của bạn và cất giữ ở nơi an toàn (giấy, két sắt, v.v.).
 - Đối với Wallet hiện có, hãy nhập cụm từ seed của bạn để khôi phục.


4. Đặt mật khẩu để bảo vệ Wallet của bạn.



→ Chi tiết hơn về hướng dẫn Electrum:



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Bước 3: Kiểm tra số tiền có sẵn



Đảm bảo Wallet của bạn chứa đủ bitcoin (BTC) hoặc satoshi (Sats) để:




- Số tiền giao dịch (ví dụ: 0,00001 BTC hoặc 1000 Sats).
- Phí giao dịch thay đổi tùy theo quy mô của mạng (thường là vài nghìn Sats).



Tham khảo Số dư trong Electrum để kiểm tra tiền của bạn.



![image](assets/fr/02.webp)



Nếu cần, hãy chuyển BTC hoặc Sats để nạp vào Wallet của bạn. Để thực hiện việc này, hãy vào tab "Nhận" và nhấp vào "Tạo Yêu cầu":



![image](assets/fr/03.webp)



Điều này sẽ hiển thị một tiếp nhận Address:



![image](assets/fr/04.webp)



→ Chi tiết hơn về hướng dẫn Electrum:



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## Bước 4: Chuẩn bị tin nhắn cần ghi



Chọn tin nhắn bạn muốn nhập (ví dụ: `Cảm ơn Satoshi`). Lưu ý: Tin nhắn OP_RETURN bị giới hạn ở 80 byte, tức là khoảng 80 ký tự ASCII.



*Hãy dành chút thời gian để suy nghĩ: những gì bạn viết trên Blockchain Bitcoin là vĩnh cửu và tất cả mọi người đều có thể tiếp cận, vì vậy :*




- để lại một biểu hiện đẹp đẽ về nhân tính của chúng ta,
- tránh nhập nội dung mà bạn có thể hối tiếc



*Không gian Blockchain và bitcoin của bạn rất quý giá, hãy sử dụng chúng một cách khôn ngoan và có mục đích*



Chuyển đổi tin nhắn của bạn sang hệ thập lục phân:




- Bạn có thể sử dụng [công cụ trực tuyến](https://www.rapidtables.com/convert/number/ascii-to-hex.html), nhưng hãy cẩn thận không xử lý dữ liệu nhạy cảm ở đó (mặc dù về nguyên tắc, thông tin dự định công bố trên Blockchain Bitcoin thông qua OP_RETURN không gây ra bất kỳ vấn đề bảo mật nào);
- Để bảo mật hơn, hãy thực hiện chuyển đổi cục bộ bằng Python nhỏ:



```py
#!/usr/bin/env python3

def main():
ascii_text = input("Enter ASCII text: ")
try:
hex_output = ascii_text.encode('ascii').hex()
print(hex_output)
except UnicodeEncodeError:
print("Error: Input contains non-ASCII characters.", file=sys.stderr)

if __name__ == "__main__":
import sys
main()
```



Ví dụ: `Thanks Satoshi` trong mã ASCII trả về `5468616e6b73205361746f736869` trong hệ thập lục phân.



Chuẩn bị kịch bản giao dịch. Dưới đây là ví dụ về định dạng dự kiến:



```script
bc1q879cv4p5q6s9537orange3zss33d3turzad8, 0.00001
script(OP_RETURN 5468616e6b73205361746f736869), 0
```



được tạo thành từ:





- Điểm đến **Address**: Bitcoin Address hợp lệ. Ici, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`. Đây có thể là Address của riêng bạn, nếu bạn muốn tự trả lại số tiền đã chuyển;
- **Số tiền đã chuyển**: số tiền của giao dịch, ở đây là `0,00001` BTC. **Xin lưu ý**: vì đơn vị được sử dụng trong Electrum là BTC, nên số tiền được chỉ định trong tập lệnh giao dịch cũng phải được thể hiện bằng BTC, chứ không phải bằng Sats;
- **Script OP_RETURN**: Tin nhắn được chuyển đổi sang hệ thập lục phân, bắt đầu bằng script(`OP_RETURN <messsage>), 0`. Ở đây, `5468616e6b73205361746f736869` cho tin nhắn ở hệ thập lục phân.



⚠️ **Thận trọng**: Việc chỉ định `0` sau OP_RETURN là rất quan trọng, vì mã lệnh này đánh dấu tập lệnh là không hợp lệ, khiến đầu ra không thể sử dụng được nữa. Các nút mạng sẽ xóa đầu ra này khỏi bộ UTXO của chúng. Nếu bạn nhập giá trị khác `0`, nó sẽ bị mất vĩnh viễn: số bitcoin của bạn sẽ được coi là đã bị đốt. Do đó, bạn nên luôn nhập `0` với OP_RETURN để ghi lại dữ liệu mong muốn, nhưng không liên kết tiền với nó, vì số tiền này sẽ bị mất.



Mẹo: Sử dụng công cụ [OP_RETURN Generator](https://resources.davidcoen.it/opreturnelectrum/) để tự động generate tập lệnh. Ngay cả khi công cụ này đề xuất nhập số tiền bằng BTC, hãy giữ nguyên đơn vị được cấu hình trong Electrum.



![image](assets/fr/05.webp)



Để thay đổi đơn vị được Electrum sử dụng, trên thanh menu hãy tìm "Tùy chọn", sau đó trong tab "Đơn vị", hãy chọn BTC / mBTC / bit hoặc Sats:



![image](assets/fr/06.webp)




---

## Bước 5: Gửi giao dịch



Trong Electrum, hãy chuyển đến tab Gửi.



![image](assets/fr/07.webp)



Trong trường "Thanh toán cho", hãy dán tập lệnh đã chuẩn bị (ví dụ: tập lệnh ở trên).



![image](assets/fr/08.webp)



Trường "Thanh toán cho" sẽ được hiển thị trong Green và số tiền giao dịch sẽ xuất hiện ở dòng bên dưới.



Kiểm tra số tiền và đơn vị của số tiền đó trong trường Số tiền.



Nhấp vào "Thanh toán..." và điều chỉnh phí giao dịch theo số tiền bạn sẵn sàng trả và tốc độ bạn muốn giao dịch được xử lý bởi Miner và được tích hợp vào khối.



![image](assets/fr/09.webp)



Nhấp vào OK và xác nhận giao dịch bằng mật khẩu của bạn. Một cửa sổ xác nhận sẽ xuất hiện.




---

## Bước 6: Xác minh đăng ký



Sau khi giao dịch được xác nhận (có thể mất vài phút), hãy chuyển đến tab "Lịch sử".



![image](assets/fr/10.webp)



Nhấp chuột phải vào giao dịch và chọn "Xem trên Explorer" để xem chi tiết.



Ngoài ra, hãy sao chép đích Address (ví dụ: `bc1q879cv4p5q6s9537orange3zss33d3turzad8`) và xem trên trình khám phá Blockchain như [Mempool.space](https://Mempool.space/) hoặc [blockstream.info](https://blockstream.info/).



Tìm trường OP_RETURN trong chi tiết giao dịch để xem tin nhắn của bạn.



![image](assets/fr/11.webp)




![image](assets/fr/12.webp)




---

## Mẹo và thực hành tốt nhất





- Kiểm tra với số tiền nhỏ: Bắt đầu với một giao dịch nhỏ (ví dụ: Sats 1000) để tránh những sai sót tốn kém.
- Đảm bảo rằng đầu ra chứa OP_RETURN bằng 0, nếu không bitcoin của bạn sẽ bị mất vĩnh viễn.
- Kiểm tra đơn vị: Đảm bảo số tiền nhập vào tương ứng với đơn vị hiển thị trong Electrum (BTC, mBTC hoặc Sats).
- Phí giao dịch: Nếu mạng bị tắc nghẽn, hãy tăng phí để xác nhận nhanh hơn.
- Tin nhắn ngắn: Các mục OP_RETURN bị giới hạn ở 80 byte. Hãy lập kế hoạch cho tin nhắn của bạn cho phù hợp.



---

## Tài nguyên hữu ích





- Tải xuống Electrum: [electrum.org](https://electrum.org/)
- Trình tạo tập lệnh OP_RETURN: [resources.davidcoen.it/opreturnelectrum/](https://resources.davidcoen.it/opreturnelectrum/)
- Blockchain Explorers: [Mempool.space](https://Mempool.space/), [blockstream.info](https://blockstream.info/)