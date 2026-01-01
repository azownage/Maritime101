import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">🚢 Maritime 101</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.8rem; color: #64748B; margin-bottom: 2rem;">Complete Maritime Knowledge for Digital Twin Development</p>', unsafe_allow_html=True)
    
    # Hero metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Global Trade by Sea", "80%+", help="Percentage of world trade volumes")
    with col2:
        st.metric("Singapore Ranking", "#2 World", help="Container volume globally")
    with col3:
        st.metric("Annual Throughput", "37.3M TEU", help="Singapore 2023")
    with col4:
        st.metric("Vessel Calls/Year", "140,000+", help="At Singapore ports")
    
    st.markdown("---")
    
    # Three-column value proposition
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🎯 Purpose")
        st.markdown('<div class="success-box">', unsafe_allow_html=True)
        st.markdown("""
        **Deep Domain Knowledge for Digital Twins**
        
        Essential understanding of:
        - Physical maritime operations
        - Port workflows and processes
        - Equipment and infrastructure
        - Performance metrics (KPIs)
        - Industry dynamics
        - Real-world constraints
        
        **Why it matters:** You can't model what you don't understand.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 👥 Target Audience")
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("""
        **Who Should Use This Guide**
        
        - **Product Managers** - Requirements & user stories
        - **Software Engineers** - System architecture
        - **Data Scientists** - Analytics & ML models
        - **DevOps Engineers** - Infrastructure planning
        - **Business Analysts** - Process modeling
        - **Digital Twin Architects** - Entity design
        
        **Background:** No maritime experience needed!
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown("### 🚀 What You'll Learn")
        st.markdown('<div class="warning-box">', unsafe_allow_html=True)
        st.markdown("""
        **Comprehensive Coverage**
        
        ✅ Global trade & shipping economics  
        ✅ Vessel types & containerization  
        ✅ Port operations end-to-end  
        ✅ Terminal equipment & automation  
        ✅ Performance metrics & KPIs  
        ✅ Shipping alliances & industry structure  
        ✅ Singapore port ecosystem  
        ✅ CITOS & technology systems  
        ✅ Digital twin implementation strategies  
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown('<p class="section-header">Why Maritime Matters to Global Economy</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        ### 🌍 The Lifeblood of International Trade
        
        Maritime shipping is the backbone of globalization and modern commerce:
        
        **Fundamental Statistics:**
        - **Over 80%** of global trade volumes carried by sea
        - **64%** of seaborne trade unloaded at Asian ports
        - **~33%** of global seaborne trade passes through Straits of Malacca & Singapore
        - **>230** active container services calling at Singapore
        - **140,000** vessel calls annually at Singapore ports
        - **11+ billion tons** of goods shipped globally each year
        - **50,000+** merchant ships in operation worldwide
        
        **Economic Impact:**
        - Enables global manufacturing supply chains
        - Supports just-in-time retail operations
        - Critical for energy security (oil, LNG, coal)
        - Foundation of international trade agreements
        - Makes consumer goods affordable worldwide
        
        **Why Shipping Dominates:**
        1. **Cost Efficiency** - Cheapest transport per ton-mile
        2. **Massive Scale** - Can move enormous volumes
        3. **Global Reach** - Connects all continents
        4. **Reliability** - Established routes and schedules
        5. **Environmental** - Lower CO2 per ton-mile vs air/truck
        
        **Real-World Impact:**
        - 90% of items in your home likely traveled by sea
        - Your smartphone components crossed multiple oceans
        - Global food security depends on maritime trade
        - Economic development in emerging markets
        """)
    
    with col2:
        # Supply chain flow visualization
        fig = go.Figure()
        
        stages = ['Factory/\nManufacturer', 'Inland\nTransport', 'Export\nPort', 
                 'Ocean\nShipping', 'Import\nPort', 'Distribution\nCenter', 'Retail/\nConsumer']
        
        for i, stage in enumerate(stages):
            y_pos = len(stages) - i
            fig.add_trace(go.Scatter(
                x=[1], y=[y_pos],
                mode='markers+text',
                marker=dict(size=45, color='#3B82F6'),
                text=stage,
                textposition="middle center",
                textfont=dict(color='white', size=9),
                showlegend=False,
                hoverinfo='text',
                hovertext=f"Step {i+1}: {stage}"
            ))
            
            if i < len(stages) - 1:
                fig.add_annotation(
                    x=1, y=y_pos - 0.5,
                    text='▼',
                    showarrow=False,
                    font=dict(size=20, color='#94A3B8')
                )
        
        fig.update_layout(
            title='Global Supply Chain Flow',
            xaxis=dict(showgrid=False, showticklabels=False, zeroline=False, range=[0.5, 1.5]),
            yaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
            height=450,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("""
        **Container Revolution (1956)**
        
        Standardized containers transformed shipping:
        - **90%+ cost reduction** in handling
        - **Days → Hours** in port
        - **Intermodal transport** (ship/truck/train)
        - **Global trade explosion**
        - **Just-in-time manufacturing**
        
        Standard sizes:
        - 20ft (1 TEU)
        - 40ft (2 TEU)  
        - 40ft High Cube
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Digital Twin Connection
    st.markdown('<div class="digital-twin-callout">', unsafe_allow_html=True)
    st.markdown("""
    ### 💡 Why Deep Maritime Knowledge is Critical for Digital Twins
    
    **The Challenge You Face:**
    
    You're building a virtual representation of one of the world's most complex logistical systems. 
    Port operations involve:
    - **Thousands of containers** moving simultaneously
    - **Multiple equipment types** that must coordinate perfectly
    - **Time-critical schedules** (vessel delays cost $40K-100K per day)
    - **Global dependencies** across supply chains
    - **Real-time optimization** requirements
    - **Safety-critical operations**
    
    **Why "Good Enough" Understanding Fails:**
    
    | Knowledge Gap | Consequence | Impact |
    |--------------|-------------|---------|
    | Don't know vessel sizes | Wrong berth allocation | Vessel can't dock, schedule chaos |
    | Miss stacking rules | Invalid yard plans | Physical impossibility, system crash |
    | Wrong productivity rates | Bad resource planning | Under/over staffing, cost overruns |
    | Ignore dependencies | Race conditions | Deadlocks, equipment collisions |
    | Missing constraints | Infeasible solutions | Model provides useless results |
    
    **What Your Digital Twin Must Accurately Model:**
    
    **Physical Entities:**
    - **Vessels** - Dynamic arrival/departure, cargo manifests, berth requirements
    - **Containers** - Millions tracked with attributes, location, journey, status
    - **Quay Cranes** - Critical bottleneck resources, productivity varies
    - **Yard Equipment** - RTGs, RMGs, straddle carriers with different capabilities
    - **AGVs/Prime Movers** - Autonomous routing, battery management, traffic flow
    - **Yard Blocks** - Capacity constraints, stacking rules, accessibility
    - **Berths** - Limited resources, depth restrictions, crane assignments
    
    **This Guide Provides:**
    ✅ Physical domain understanding (what exists)  
    ✅ Operational workflows (how things work)  
    ✅ Entity attributes (what to track)  
    ✅ Relationships & dependencies (how entities connect)  
    ✅ Constraints & business rules (what's possible)  
    ✅ Performance metrics (what to measure)  
    ✅ Implementation patterns (how to model)  
    
    **Bottom Line:** Build your digital twin on solid maritime fundamentals, not assumptions.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown('<p class="section-header">Learning Path & Module Overview</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 📖 Recommended Reading Sequence
        
        **Phase 1: Foundation (Start Here)**
        1. 🌊 **Global Maritime Trade** - Industry economics, trade dynamics
        2. 🚢 **Vessels & Containers** - Ship evolution, containerization
        3. 🤝 **Shipping Alliances** - Industry structure, market dynamics
        
        **Phase 2: Core Operations (Essential)**
        4. ⚓ **Port Operations** - Terminal workflows, vessel handling
        5. 🏗️ **Terminal Equipment** - Cranes, AGVs, automation
        6. 📊 **KPIs & Performance** - Metrics, benchmarking
        
        **Phase 3: Advanced Topics**
        7. 🇸🇬 **Singapore & Tuas** - Real-world case study
        8. 🎯 **CITOS & Technology** - TOS, planning systems
        9. 💻 **Digital Twin Guide** - Implementation strategies
        
        **Reference:** 📚 Comprehensive Glossary (use anytime)
        """)
    
    with col2:
        st.markdown("""
        ### 🎓 Content Sources
        
        **8 Comprehensive Modules:**
        
        📄 PSA International  
        📄 NUS MTM5001  
        📄 Port Development  
        📄 Container Operations  
        📄 Maritime Singapore  
        📄 CMA CGM Shipping  
        📄 Tuas Port Materials  
        📄 ABS Maritime Trends  
        
        ---
        
        ### 💡 Usage Tips
        
        **Quick Reference:**  
        Jump to topics via sidebar
        
        **Deep Learning:**  
        Read sections in order
        
        **Implementation:**  
        Focus on Digital Twin section
        """)
    
    # Module overview table
    st.markdown("---")
    modules_data = pd.DataFrame({
        'Module': [
            'Global Maritime Trade',
            'Vessels & Containers',
            'Port Operations',
            'Terminal Equipment',
            'KPIs & Performance',
            'Shipping Alliances',
            'Singapore & Tuas',
            'CITOS & Technology',
            'Digital Twin Guide',
            'Glossary'
        ],
        'Topics': [
            'Trade volumes, routes, challenges, geopolitics',
            'Evolution, TEU capacity, container types, cascading',
            'Terminal zones, workflows, stakeholders, yard planning',
            'QC, RTG, RMG, AGV, specifications, automation',
            'Berth productivity, GCR, turnaround, benchmarks',
            '2M, Ocean, THE alliances, consolidation, impact',
            'Port ranking, Tuas development, automation, sustainability',
            'Berth planning, yard mgmt, PM deployment, optimization',
            'Entity modeling, processes, simulation, implementation',
            'Maritime terminology, quick reference'
        ],
        'Complexity': [
            'Medium',
            'Low-Medium',
            'High',
            'High',
            'Medium-High',
            'Medium',
            'Medium',
            'Very High',
            'Very High',
            'Low'
        ]
    })
    
    st.dataframe(modules_data, use_container_width=True, hide_index=True)

