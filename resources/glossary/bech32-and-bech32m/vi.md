`Bech32` và `Bech32m` là hai định dạng mã hóa địa chỉ được sử dụng để nhận bitcoin. Chúng dựa trên một phiên bản base 32 được chỉnh sửa nhẹ. Chúng bao gồm một checksum dựa trên một thuật toán sửa lỗi gọi là BCH (*Bose-Chaudhuri-Hocquenghem*). So với địa chỉ Legacy, được mã hóa trong `Base58check`, các địa chỉ `Bech32` và `Bech32m` có checksum hiệu quả hơn, cho phép phát hiện và có khả năng tự động sửa chữa lỗi đánh máy. Định dạng của chúng cũng cung cấp khả năng đọc tốt hơn, chỉ với các ký tự chữ thường. Dưới đây là ma trận cộng cho định dạng này từ base 10:

&nbsp;

| +   | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | q   | p   | z   | r   | y   | 9   | x   | 8   |
| 8   | g   | f   | 2   | t   | v   | d   | w   | 0   |
| 16  | s   | 3   | j   | n   | 5   | 4   | k   | h   |
| 24  | c   | e   | 6   | m   | u   | a   | 7   | l   |

&nbsp;
Bech32 và Bech32m là các định dạng mã hóa được sử dụng để biểu diễn địa chỉ SegWit. Bech32 là một định dạng mã hóa địa chỉ được giới thiệu bởi BIP173 vào năm 2017. Nó sử dụng một bộ ký tự cụ thể, bao gồm các số và chữ cái thường, để giảm thiểu lỗi đánh máy và tạo điều kiện thuận lợi cho việc đọc. Địa chỉ Bech32 thường bắt đầu với `bc1` để chỉ ra rằng chúng là bản địa của SegWit. Định dạng này chỉ được sử dụng trên địa chỉ SegWit V0, với các script P2WPKH (Pay to Witness Public Key Hash) và P2WSH (Pay to Witness Script Hash). Tuy nhiên, có một lỗi nhỏ không mong muốn cụ thể cho định dạng Bech32. Bất cứ khi nào ký tự cuối cùng của địa chỉ là một `p`, việc thêm hoặc loại bỏ bất kỳ số lượng ký tự `q` nào ngay trước nó không làm mất hiệu lực của checksum. Điều này không ảnh hưởng đến các sử dụng hiện tại của địa chỉ SegWit V0 (BIP173) do hạn chế của chúng với hai độ dài xác định. Tuy nhiên, điều này có thể ảnh hưởng đến các sử dụng tương lai của mã hóa Bech32. Định dạng Bech32m đơn giản là một định dạng Bech32 với lỗi này được sửa chữa. Nó được giới thiệu với BIP350 vào năm 2020. Địa chỉ Bech32m cũng bắt đầu với `bc1`, nhưng chúng được thiết kế cụ thể để tương thích với SegWit V1 (Taproot) và các phiên bản sau này, với script P2TR (Pay to TapRoot).