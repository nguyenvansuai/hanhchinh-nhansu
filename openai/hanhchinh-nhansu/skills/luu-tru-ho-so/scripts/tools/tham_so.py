"""Tham số pháp lý theo thời điểm. Mỗi mục có nguồn; khi văn bản thay đổi chỉ sửa file này.

Mức độ tin cậy: "da_doi_chieu" = đã đối chiếu nhiều nguồn; "can_kiem_tra" = cần đối chiếu văn bản gốc.
Cập nhật lần cuối: 11/2026.
"""
from datetime import date

LUONG_TOI_THIEU_VUNG = [
    # (áp dụng từ, {vùng: (tháng, giờ)}, nguồn)
    (date(2024, 7, 1), {1: (4_960_000, 23_800), 2: (4_410_000, 21_200), 3: (3_860_000, 18_600), 4: (3_450_000, 16_600)},
     "Nghị định 74/2024/NĐ-CP"),
    (date(2026, 1, 1), {1: (5_310_000, 25_500), 2: (4_730_000, 22_700), 3: (4_140_000, 20_000), 4: (3_700_000, 17_800)},
     "Nghị định 293/2025/NĐ-CP (đã đối chiếu)"),
]

LUONG_CO_SO = [
    (date(2024, 7, 1), 2_340_000, "Nghị định 73/2024/NĐ-CP"),
    (date(2026, 7, 1), 2_530_000, "Nghị định 161/2026/NĐ-CP (cần kiểm tra văn bản gốc)"),
]

# Tỷ lệ đóng bảo hiểm bắt buộc (Luật BHXH 2024, Luật BHYT, Luật Việc làm 2025) – không đổi trong 2026
TY_LE_BH = {
    "nld": {"bhxh": 0.08, "bhyt": 0.015, "bhtn": 0.01},
    "dn": {"bhxh_huu_tri": 0.14, "bhxh_om_dau_thai_san": 0.03, "tnld_bnn": 0.005, "bhyt": 0.03, "bhtn": 0.01},
    "kpcd": 0.02,  # Kinh phí công đoàn (Luật Công đoàn 2024) – doanh nghiệp đóng
    "nguon": "Luật BHXH 2024 (hiệu lực 01/7/2025), Luật Việc làm 2025 (hiệu lực 01/01/2026), Luật Công đoàn 2024",
}

GIAM_TRU_GIA_CANH = [
    (date(2020, 7, 1), 11_000_000, 4_400_000, "Nghị quyết 954/2020/UBTVQH14"),
    (date(2026, 1, 1), 15_500_000, 6_200_000, "Nghị quyết 110/2025/UBTVQH15 (đã đối chiếu)"),
]

BIEU_THUE_TNCN = [
    # (áp dụng từ, [(ngưỡng trên/tháng, thuế suất)], nguồn)
    (date(2009, 1, 1), [(5e6, .05), (10e6, .10), (18e6, .15), (32e6, .20), (52e6, .25), (80e6, .30), (float("inf"), .35)],
     "Luật Thuế TNCN 2007 (biểu 7 bậc)"),
    (date(2026, 1, 1), [(10e6, .05), (30e6, .10), (60e6, .20), (100e6, .30), (float("inf"), .35)],
     "Luật Thuế TNCN số 109/2025/QH15 – biểu 5 bậc áp dụng kỳ tính thuế 2026 (bậc 30% cần đối chiếu văn bản gốc)"),
]

# Thời gian thử việc tối đa (Điều 25 BLLĐ 2019)
THU_VIEC_TOI_DA = {
    "quan_ly_doanh_nghiep": (180, "Người quản lý doanh nghiệp theo Luật Doanh nghiệp"),
    "cao_dang_tro_len": (60, "Chức danh nghề nghiệp cần trình độ cao đẳng trở lên"),
    "trung_cap": (30, "Trình độ trung cấp, công nhân kỹ thuật, nhân viên nghiệp vụ"),
    "khac": (6, "Công việc khác (tính theo ngày làm việc)"),
}


def theo_ngay(bang, ngay):
    kq = None
    for dong in bang:
        if dong[0] <= ngay:
            kq = dong
    return kq
