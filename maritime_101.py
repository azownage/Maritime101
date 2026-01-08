import streamlit as st

st.set_page_config(
    page_title="Maritime 101 - Knowledge Base",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS
st.markdown("""
<style>
.main-header {
    font-size: 3.5rem;
    font-weight: bold;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    padding: 1.5rem 0;
}
.section-header {
    font-size: 2.2rem;
    font-weight: bold;
    color: #2563EB;
    border-bottom: 4px solid #2563EB;
    padding-bottom: 0.5rem;
    margin-top: 2.5rem;
    margin-bottom: 1.5rem;
}
.subsection-header {
    font-size: 1.8rem;
    font-weight: bold;
    color: #3B82F6;
    margin-top: 2rem;
    margin-bottom: 1rem;
}
.info-box {
    background-color: #FEF3C7; 
    padding: 1.2rem; 
    border-radius: 0.5rem; 
    border-left: 4px solid #F59E0B; 
    margin: 1rem 0;
}
.warning-box {
    background-color: #FEE2E2; 
    padding: 1.2rem; 
    border-radius: 0.5rem; 
    border-left: 4px solid #EF4444; 
    margin: 1rem 0;
}
.success-box {
    background-color: #D1FAE5; 
    padding: 1.2rem; 
    border-radius: 0.5rem; 
    border-left: 4px solid #10B981; 
    margin: 1rem 0;
}
.insight-box {
    background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
    border-left: 6px solid #3B82F6;
    padding: 1.5rem;
    margin: 1.5rem 0;
    border-radius: 0.5rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("## 🧭 Navigation")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Select Section:",
    [
        "🏠 Maritime Industry Foundation",
        "📦 Containers & Containerisation",
        "🚢 Container Vessels & Evolution",
        "🌍 Global Shipping & Alliances",
        "🏛️ Maritime Singapore Ecosystem",
        "⚓ Port Strategy & Competition",
        "🎯 Operations Management Fundamentals",
        "🔄 Terminal Operations & Planning",
        "🤖 Equipment, Automation & CITOS",
        "🌱 Green Maritime & Future Trends",
        "🏗️ Tuas Mega Port Case Study"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("""
📘 **Maritime 101 Knowledge Base**  

Comprehensive maritime education covering:
- Industry fundamentals
- Physical infrastructure
- Global trade patterns
- Operations & technology
- Singapore case studies
- Future trends

""")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Quick Facts")
st.sidebar.metric("Global Trade by Sea", "80%+")
st.sidebar.metric("Singapore Throughput", "37.3M TEU")
st.sidebar.metric("Largest Vessels", "25,000 TEU")
st.sidebar.metric("Alliance Control", ">80%")
st.sidebar.metric("Tuas Target", "65M TEU")

# Route to pages
if page == "🏠 Maritime Industry Foundation":
    from modules import foundation
    foundation.show()
elif page == "📦 Containers & Containerisation":
    from modules import containers
    containers.show()
elif page == "🚢 Container Vessels & Evolution":
    from modules import vessels
    vessels.show()
elif page == "🌍 Global Shipping & Alliances":
    from modules import global_shipping
    global_shipping.show()
elif page == "🏛️ Maritime Singapore Ecosystem":
    from modules import singapore_ecosystem
    singapore_ecosystem.show()
elif page == "⚓ Port Strategy & Competition":
    from modules import port_competition
    port_competition.show()
elif page == "🎯 Operations Management Fundamentals":
    from modules import operations_management
    operations_management.show()
elif page == "🔄 Terminal Operations & Planning":
    from modules import terminal_operations
    terminal_operations.show()
elif page == "🤖 Equipment, Automation & CITOS":
    from modules import equipment_technology
    equipment_technology.show()
elif page == "🌱 Green Maritime & Future Trends":
    from modules import green_innovation
    green_innovation.show()
elif page == "🏗️ Tuas Mega Port Case Study":
    from modules import tuas_development
    tuas_development.show()

# Footer
st.markdown("---")
