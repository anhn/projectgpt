import streamlit as st
import plotly.graph_objects as go

# Step configuration
TOTAL_STEPS = 7
STEP_LABELS = [
    "📋 Khởi động",
    "🔧 Công nghệ",
    "⚖️ Pháp lý & Chính sách",
    "🏢 Tổ chức",
    "💰 Tài chính",
    "🤝 Người dùng & Chiến lược",
    "📊 Kết quả"
]

# Category and factors
categories = {
    "Công nghệ": {
        "TCH": "Sự sẵn sàng về công nghệ",
        "COM": "Khả năng tương thích hệ thống",
        "RAD": "Nhận thức lợi ích và ưu thế",
        "CPL": "Độ phức tạp kỹ thuật (↓ tốt hơn)"
    },
    "Pháp lý & Chính sách": {
        "LSG": "Khung pháp lý hỗ trợ",
        "DPR": "Chính sách dữ liệu và quyền riêng tư",
        "REC": "Công nhận pháp lý của dữ liệu blockchain"
    },
    "Tổ chức": {
        "ORG": "Năng lực tổ chức",
        "CHM": "Sẵn sàng chuyển đổi",
        "COL": "Hợp tác liên ngành"
    },
    "Tài chính": {
        "CAPEX": "Chi phí triển khai (↓ tốt hơn)",
        "OPEX": "Chi phí vận hành (↓ tốt hơn)",
        "ROI": "Tỷ suất lợi ích / chi phí"
    },
    "Người dùng & Chiến lược": {
        "TRU": "Niềm tin và mức chấp nhận",
        "SUP": "Sự ủng hộ của ngành",
        "USE": "Khả năng sử dụng thực tế",
        "POL": "Hỗ trợ chính trị",
        "GLB": "Khả năng tương thích quốc tế"
    }
}

# Initialize state
if 'step' not in st.session_state:
    st.session_state.step = 0
    for section in categories.values():
        for key in section:
            st.session_state[key] = 3

# Navigation
def next_step():
    st.session_state.step += 1

def reset():
    st.session_state.step = 0

# UI layout
st.set_page_config(page_title="Đánh giá khả thi Blockchain", layout="wide")
st.title("🧠 Hệ thống đánh giá khả thi ứng dụng Blockchain")

# Step bar
st.markdown("### 📌 Tiến trình thực hiện:")
cols = st.columns(TOTAL_STEPS)
for i in range(TOTAL_STEPS):
    step_label = STEP_LABELS[i]
    if i == st.session_state.step:
        cols[i].markdown(f"✅ **{step_label}**")
    else:
        cols[i].markdown(f"{step_label}")

st.divider()

# Step 0: Landing
if st.session_state.step == 0:
    st.subheader("📋 Giới thiệu tình huống đánh giá")
    st.selectbox("Chọn lĩnh vực", ["Quản lý đăng kiểm", "Vận tải hàng hóa", "Logistics", "Quản lý phương tiện", "Khác"])
    st.text_area("Mô tả tình huống", placeholder="VD: Tích hợp blockchain để theo dõi đăng kiểm và bảo hiểm xe...")
    if st.button("Bắt đầu đánh giá"):
        next_step()

# Steps 1–5: Category inputs
elif 1 <= st.session_state.step <= 5:
    cat_name = list(categories.keys())[st.session_state.step - 1]
    st.subheader(f"🔍 Đánh giá: {cat_name}")
    for key, label in categories[cat_name].items():
        with st.expander(label):
            st.slider(f"Chấm điểm (1 - rất yếu, 5 - rất tốt):", 1, 5, key=key)
    if st.button("Tiếp tục"):
        next_step()

# Step 6: Results
elif st.session_state.step == 6:
    st.subheader("📊 Tổng hợp kết quả đánh giá")
    avg_scores = {}
    for cat, factors in categories.items():
        score = 0
        for key, label in factors.items():
            val = st.session_state[key]
            if "↓" in label:
                val = 6 - val
            score += val
        avg_scores[cat] = round(score / len(factors), 2)

    # Radar Chart
    radar = go.Figure()
    radar.add_trace(go.Scatterpolar(
        r=list(avg_scores.values()),
        theta=list(avg_scores.keys()),
        fill='toself',
        name='Điểm trung bình'
    ))
    radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
        showlegend=False
    )
    st.plotly_chart(radar, use_container_width=True)

    # Bar Charts for each category
    st.markdown("### 📌 Chi tiết từng danh mục:")
    for cat, factors in categories.items():
        fig = go.Figure()
        for key, label in factors.items():
            actual = 6 - st.session_state[key] if "↓" in label else st.session_state[key]
            benchmark = 4
            fig.add_trace(go.Bar(name="Điểm đánh giá", x=[label], y=[actual]))
            fig.add_trace(go.Bar(name="Chuẩn tham chiếu", x=[label], y=[benchmark]))
        fig.update_layout(title=cat, barmode='group', yaxis=dict(range=[0, 5]))
        st.plotly_chart(fig, use_container_width=True)

    st.success("🎯 Đánh giá hoàn tất! Xem xét các điểm yếu để đề xuất hành động cụ thể.")
    st.button("🔁 Thực hiện lại", on_click=reset)
