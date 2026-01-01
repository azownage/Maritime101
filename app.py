import streamlit as st

st.set_page_config(
    page_title="Maritime 101 - Complete Edition",
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
.digital-twin-callout {
    background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
    border-left: 6px solid #3B82F6;
    padding: 1.5rem;
    margin: 1.5rem 0;
    border-radius: 0.5rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.info-box {background-color: #FEF3C7; padding: 1.2rem; border-radius: 0.5rem; border-left: 4px solid #F59E0B; margin: 1rem 0;}
.warning-box {background-color: #FEE2E2; padding: 1.2rem; border-radius: 0.5rem; border-left: 4px solid #EF4444; margin: 1rem 0;}
.success-box {background-color: #D1FAE5; padding: 1.2rem; border-radius: 0.5rem; border-left: 4px solid #10B981; margin: 1rem 0;}
</style>
""", unsafe_allow_html=True)

# Import all page modules
from pages import (
    home,
    global_trade,
    vessels,
    port_operations,
    equipment,
    kpis,
    alliances,
    singapore,
    citos,
    digital_twin,
    glossary
)

# Sidebar Navigation
st.sidebar.markdown("## 🧭 Navigation")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Select Section:",
    [
        "🏠 Home & Overview",
        "🌊 Global Maritime Trade",
        "🚢 Vessels & Containers",
        "⚓ Port Operations",
        "🏗️ Terminal Equipment",
        "📊 KPIs & Performance",
        "🤝 Shipping Alliances",
        "🇸🇬 Singapore & Tuas",
        "🎯 CITOS & Technology",
        "💻 Digital Twin Guide",
        "📚 Comprehensive Glossary"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("""
📘 **Maritime 101**  
Complete Multi-Module Edition

**All sections fully expanded**

Content from 8 comprehensive lecture modules.
""")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Quick Stats")
st.sidebar.metric("Global Trade", "80%+ by Sea")
st.sidebar.metric("Singapore TEU", "37.3M")
st.sidebar.metric("Largest Vessels", "24,000 TEU")
st.sidebar.metric("BOA Rate", ">90%")

# Route to appropriate page
if page == "🏠 Home & Overview":
    home.show()
elif page == "🌊 Global Maritime Trade":
    global_trade.show()
elif page == "🚢 Vessels & Containers":
    vessels.show()
elif page == "⚓ Port Operations":
    port_operations.show()
elif page == "🏗️ Terminal Equipment":
    equipment.show()
elif page == "📊 KPIs & Performance":
    kpis.show()
elif page == "🤝 Shipping Alliances":
    alliances.show()
elif page == "🇸🇬 Singapore & Tuas":
    singapore.show()
elif page == "🎯 CITOS & Technology":
    citos.show()
elif page == "💻 Digital Twin Guide":
    digital_twin.show()
elif page == "📚 Comprehensive Glossary":
    glossary.show()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #64748B; padding: 2rem;'>
    <p style='font-size: 1.2rem;'><strong>Maritime 101 - Complete Multi-Module Edition</strong></p>
    <p>Comprehensive maritime knowledge for digital twin development</p>
    <p style='font-size: 0.9rem;'>Built with detailed content from PSA International, NUS MTM5001, and industry materials</p>
</div>
""", unsafe_allow_html=True)

