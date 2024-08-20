Trong bối cảnh chung của lĩnh vực máy tính, payload chỉ dữ liệu thiết yếu được chứa trong một gói dữ liệu lớn hơn. Ví dụ, trong một địa chỉ SegWit V0 trên Bitcoin, payload tương ứng với hash của khóa công khai, không bao gồm các metadata khác nhau (phần dễ đọc bởi con người (HRP), dấu phân cách, phiên bản SegWit, và checksum). Ví dụ, trong địa chỉ `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj`, chúng ta có:
* `bc` : phần dễ đọc bởi con người (HRP);
* `1` : dấu phân cách;
* `q` : phiên bản SegWit. Ở đây, đó là phiên bản 0;
* `c2eukw7reasfcmrafevp5dhv8635yuqa` : payload, ở đây, là hash của khóa công khai;
* `ys50gj` : checksum.