---
description: Danh sách việc HCNS cần làm trong tháng – hạn pháp lý, ngày nghỉ lễ, HĐLĐ sắp hết hạn, văn bản đến chưa xử lý, việc định kỳ.
argument-hint: "[tháng/năm, file danh sách nhân viên nếu có]"
---

Lập danh sách việc HCNS cho: $ARGUMENTS (mặc định tháng hiện tại)

Dùng skill `lich-tuan-thu-hcns`:
1. `lich_tuan_thu_hcns` cho năm tương ứng → lọc các mục trong tháng.
2. Nếu có danh sách nhân viên: tính mốc HĐ hết hạn (báo trước 15 ngày), kết thúc thử việc, xóa kỷ luật trong tháng.
3. `tra_cuu_so_van_ban` (loai=den, chi_chua_xong=true) → văn bản đến chưa xử lý, sắp/quá hạn.
4. Việc định kỳ: báo tăng/giảm BHXH, chấm công, phối hợp kế toán tính lương.
Trình bày bảng xếp theo hạn: Hạn | Việc | Người phụ trách | Căn cứ. Hỏi có xuất .ics không.
