import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">🚢 Maritime 101</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.8rem; color: #64748B; margin-bottom: 2rem;">Complete Maritime Knowledge for Digital Twin Development</p>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Global Trade by Sea", "80%+")
    with col2:
        st.metric("Singapore Ranking", "#2 World")
    with col3:
        st.metric("Annual Throughput", "37.3M TEU")
    with col4:
        st.metric("Vessel Calls/Year", "140,000+")
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🎯 Purpose")
        st.success("""
        **Deep Domain Knowledge for Digital Twins**
        
        - Physical maritime operations
        - Port workflows and processes
        - Equipment and infrastructure
        - Performance metrics (KPIs)
        - Industry dynamics
        - Real-world constraints
        """)
    
    with col2:
        st.markdown("### 👥 Target Audience")
        st.info("""
        **Who Should Use This**
        
        - Product Managers
        - Software Engineers
        - Data Scientists
        - Business Analysts
        - Digital Twin Architects
        """)
    
    with col3:
        st.markdown("### 🚀 What You'll Learn")
        st.warning("""
        **Comprehensive Coverage**
        
        ✅ Global trade & economics
        ✅ Vessel types & containerization
        ✅ Port operations workflows
        ✅ Equipment & automation
        ✅ Performance metrics
        ✅ Digital twin implementation
        """)
    
    st.markdown("---")
    st.markdown("## Why Maritime Matters")
    
    st.markdown("""
    ### 🌍 The Lifeblood of Global Economy
    
    **Critical Statistics:**
    - **80%+** of global trade volumes by sea
    - **64%** of seaborne trade at Asian ports
    - **~33%** passes through Singapore Straits
    - **>230** container services call Singapore
    - **140,000** vessel calls/year in Singapore
    
    **Economic Impact:**
    - Enables global manufacturing
    - Supports retail supply chains
    - Critical for energy security
    - Foundation of international trade
    """)
    
    st.info("""
    💡 **Digital Twin Connection**: Understanding maritime operations is essential for building
    accurate digital twins of port systems. This guide provides the domain knowledge needed to
    model vessels, containers, equipment, and processes correctly.
    """)
