import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">🚢 Maritime Industry Foundation</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand why maritime matters, the transformative impact of containerization, and the major forces 
    shaping the modern shipping industry.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Shipping as Lifeblood of World Economy
    # ============================================================================
    
    st.markdown('<p class="section-header">Shipping: The Lifeblood of the World Economy</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Global Trade by Sea", "80%+", help="Over 80% of global trade by volume is carried by sea")
    with col2:
        st.metric("Asian Port Volumes", "64%", help="64% of seaborne trade is unloaded at Asian ports")
    with col3:
        st.metric("Via Malacca/Singapore", "33%", help="33% of seaborne trade passes through Straits of Malacca and Singapore")
    
    st.markdown("""
    Maritime shipping is the backbone of global commerce and the international supply chain. Without ships 
    moving containers across oceans, modern international trade as we know it would not exist. The scale 
    is staggering: over 80% of world trade by volume travels by sea, making maritime transport absolutely 
    critical to the global economy.
    
    Asia dominates global maritime trade, with 64% of seaborne trade unloaded at Asian ports. The strategic 
    Straits of Malacca and Singapore serve as a critical chokepoint, handling 33% of global seaborne trade. 
    This geographic concentration makes the region—and particularly Singapore—vital to global supply chains.
    """)
    
    st.markdown('<p class="subsection-header">Maritime as a Team Sport</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Modern maritime logistics is not a solo endeavor. It's a complex ecosystem requiring tight coordination 
    among multiple stakeholders:
    
    - **Shipping Lines**: Operate the vessels that carry containers
    - **Port Authorities**: Regulate and plan port infrastructure (e.g., MPA in Singapore)
    - **Terminal Operators**: Handle actual cargo operations (e.g., PSA)
    - **Freight Forwarders**: Coordinate logistics for shippers
    - **Customs & Government Agencies**: Handle regulatory compliance
    - **Trucking Companies**: Provide last-mile delivery
    - **Maritime Services**: Provide bunkering, pilotage, towage, repairs
    - **Financial & Legal Services**: Enable transactions and contracts
    
    Success in this industry requires seamless collaboration across this entire supply chain network.
    """)
    
    # ============================================================================
    # SECTION 2: The Container Revolution
    # ============================================================================
    
    st.markdown('<p class="section-header">The Container Revolution</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Before containerization, cargo was loaded and unloaded as "break-bulk"—individual pieces handled 
    separately by longshoremen. This was slow, expensive, labor-intensive, and prone to theft and damage.
    
    The introduction of standardized shipping containers in the 1950s-1960s revolutionized global trade.
    """)
    
    # Economic impact visualization
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=['Break-Bulk Shipping', 'Container Shipping'],
        y=[100, 6],
        marker=dict(
            color=['#EF4444', '#10B981'],
            line=dict(color='#1F2937', width=2)
        ),
        text=['100% (Baseline)', '6% (94% Cost Reduction)'],
        textposition='outside',
        textfont=dict(size=14, color='#1F2937'),
        name='Relative Cost'
    ))
    
    fig.update_layout(
        title={
            'text': 'Container Shipping: 94% Cost Reduction vs Break-Bulk',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#1F2937', 'family': 'Arial Black'}
        },
        yaxis_title="Relative Cost (Indexed to 100)",
        xaxis_title="Shipping Method",
        height=400,
        showlegend=False,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='#E5E7EB', range=[0, 120])
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 Key Insight:</strong> Container shipping is 94% cheaper than break-bulk shipping for the same 
    product. This dramatic cost reduction enabled the explosion of global trade we see today.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">What Containerization Changed</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Before Containers (Break-Bulk Era):**
        - Loading/unloading took days or weeks per ship
        - High labor costs (large gangs of longshoremen)
        - Ships spent more time in port than at sea
        - Limited economies of scale
        - Expensive and unpredictable
        """)
    
    with col2:
        st.markdown("""
        **After Containers:**
        - Loading/unloading in hours
        - Minimal labor (crane operators + truck drivers)
        - Sealed containers reduce theft and damage
        - Ships maximize time at sea
        - Massive vessels (25,000+ TEU) achievable
        - Predictable, reliable, affordable
        """)
    
    # ============================================================================
    # SECTION 3: Three Waves of Change
    # ============================================================================
    
    st.markdown('<p class="section-header">Three Waves of Change: Reshaping Maritime</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The maritime industry has been transformed by three major waves of change over recent decades. 
    Understanding these trends is crucial to understanding the current state of the industry.
    """)
    
    # Wave A: Mega Vessels
    st.markdown('<p class="subsection-header">Wave A: Arrival of Mega Vessels</p>', unsafe_allow_html=True)
    
    vessel_evolution = pd.DataFrame({
        'Era': ['1956\nEarly', '1970\nFully Cellular', '1980\nPanamax', '1988\nPost-Panamax I', 
                '2000\nPost-Panamax II', '2006\nVLCS', '2013\nULCS', '2019\nMGX-24'],
        'TEU Capacity': [500, 1500, 3200, 5000, 7000, 13000, 19500, 23000],
        'Containers Across': [6, 8, 10, 13, 16, 19, 22, 24]
    })
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=vessel_evolution['Era'],
        y=vessel_evolution['TEU Capacity'],
        mode='lines+markers+text',
        line=dict(color='#3B82F6', width=4),
        marker=dict(size=12, color='#2563EB', line=dict(color='white', width=2)),
        text=vessel_evolution['TEU Capacity'],
        textposition='top center',
        textfont=dict(size=11, color='#1F2937'),
        name='Vessel Capacity'
    ))
    
    fig.update_layout(
        title={
            'text': 'Container Vessel Size Evolution: 500 TEU → 25,000 TEU',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        xaxis_title="Era / Vessel Type",
        yaxis_title="TEU Capacity",
        height=450,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='#E5E7EB'),
        showlegend=False
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    Container vessels have grown dramatically in size over the past 70 years:
    
    - **1956**: Early container ships carried just 500 TEU
    - **1980s**: Panamax vessels (3,000-3,400 TEU) - sized to fit through Panama Canal
    - **2000s**: Post-Panamax vessels exceeded Panama Canal limits (6,000-8,500 TEU)
    - **2014**: New-Panamax (12,500 TEU) after canal expansion
    - **2019**: MGX-24 ultra-large container ships reach 21,000-25,000 TEU
    
    This growth was driven by **economies of scale**: larger ships have lower cost per container moved. 
    However, mega vessels require specialized port infrastructure, deep water berths, and super-sized 
    quay cranes.
    """)
    
    # Wave B: Mega Alliances
    st.markdown('<p class="subsection-header">Wave B: Birth of Mega Alliances</p>', unsafe_allow_html=True)
    
    # Alliance evolution chart
    alliance_data = pd.DataFrame({
        'Period': ['1990s', '2000s', '2015', '2017-2024', '2025'],
        'Alliance Control': [0, 30, 75, 80, 83],
        'Status': ['Independent Era', 'Early Alliances', 'Consolidation', 'Mature Alliances', 'Current']
    })
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=alliance_data['Period'],
        y=alliance_data['Alliance Control'],
        marker=dict(
            color=['#94A3B8', '#64748B', '#3B82F6', '#2563EB', '#1E40AF'],
            line=dict(color='#1F2937', width=2)
        ),
        text=[f"{val}%" for val in alliance_data['Alliance Control']],
        textposition='outside',
        textfont=dict(size=14, color='#1F2937'),
        name='Alliance-Controlled Volume'
    ))
    
    fig.update_layout(
        title={
            'text': 'Shipping Alliance Market Control: 0% → 83%',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        xaxis_title="Period",
        yaxis_title="% of Global Container Volumes",
        height=400,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='#E5E7EB', range=[0, 100]),
        showlegend=False
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    Shipping lines formed alliances to share vessels, routes, and costs. Alliance control of global 
    container volumes has grown dramatically:
    
    - **1990s**: 0% - Carriers operated independently
    - **2000s**: 30% - Early alliance formations
    - **2015**: 75% - Major consolidation wave
    - **2017-2024**: >80% - Mature alliance era
    - **2025**: 83% - Current state with three major alliances
    
    **Today's Three Major Alliances:**
    
    1. **2M Alliance** (34% market share): Maersk + MSC
    2. **Ocean Alliance** (30% market share): CMA CGM + COSCO + OOCL + Evergreen
    3. **THE Alliance** (19% market share): ONE (NYK, MOL, "K" Line) + HMM + Yang Ming
    
    This means just 9 major shipping line groups control 83% of global container shipping. Industry 
    consolidation from 15+ major players down to 9 has fundamentally changed port competition dynamics.
    """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🎯 Strategic Implication for Ports:</strong> To remain competitive, ports must attract and 
    retain these mega alliances. Losing one alliance can mean losing 30%+ of your throughput overnight. 
    This is why ports invest billions in infrastructure to meet alliance requirements.
    </div>
    """, unsafe_allow_html=True)
    
    # Wave C: Change of Cargo
    st.markdown('<p class="subsection-header">Wave C: Change of Cargo</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The nature of containerized cargo has shifted dramatically, driven by:
    
    **Geopolitical Shifts:**
    - US-China trade tensions leading to diversification
    - Trade bypassing direct US-China routes via intermediaries
    - Rise of intermediary countries (Vietnam +80%, Malaysia +45%, Thailand +41%, Mexico +42%)
    - Supply chains becoming longer and more complex
    
    **E-commerce Explosion:**
    - Shift from bulk wholesale to individual consumer shipments
    - Smaller, more frequent shipments
    - Higher variability and unpredictability
    - Need for faster port turnaround times
    
    **Product Mix Changes:**
    - From raw materials to finished goods
    - From heavy industrial cargo to lighter consumer electronics
    - More refrigerated containers (reefers) for perishables
    - More high-value cargo requiring security
    
    These changes mean ports must be more flexible, responsive, and technologically advanced than ever before.
    """)
    
    # ============================================================================
    # SECTION 4: Maritime Economics Fundamentals
    # ============================================================================
    
    st.markdown('<p class="section-header">Maritime Economics of Scale</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The maritime industry operates on extremely tight margins, making economies of scale critical. 
    Consider the relationship between vessel size and efficiency:
    """)
    
    # Vessel economics comparison
    vessel_comparison = pd.DataFrame({
        'Vessel Type': ['Feeder\n(1,000 TEU)', 'Panamax\n(5,000 TEU)', 'Post-Panamax\n(10,000 TEU)', 
                       'ULCS\n(20,000 TEU)'],
        'Cost per TEU': [100, 45, 28, 18],
        'Port Requirements': ['Basic', 'Standard', 'Advanced', 'Ultra-Modern']
    })
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=vessel_comparison['Vessel Type'],
        y=vessel_comparison['Cost per TEU'],
        marker=dict(
            color=['#EF4444', '#F59E0B', '#3B82F6', '#10B981'],
            line=dict(color='#1F2937', width=2)
        ),
        text=[f"${val}" for val in vessel_comparison['Cost per TEU']],
        textposition='outside',
        textfont=dict(size=13, color='#1F2937'),
        name='Cost per TEU (Indexed)'
    ))
    
    fig.update_layout(
        title={
            'text': 'Larger Vessels = Lower Cost Per Container',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        xaxis_title="Vessel Type",
        yaxis_title="Relative Cost per TEU (Indexed)",
        height=400,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='#E5E7EB'),
        showlegend=False
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    Larger vessels are dramatically more efficient:
    - A 20,000 TEU vessel costs only 18% as much per container as a 1,000 TEU feeder vessel
    - However, larger vessels require deeper berths, bigger cranes, and more sophisticated terminals
    - This creates a "barrier to entry" for ports—only well-equipped ports can handle mega vessels
    
    **The Trade-off:**
    - **Shipping lines** want the biggest ships possible to minimize cost per container
    - **Ports** must invest billions to accommodate these mega vessels
    - **Smaller ports** risk being left behind if they can't upgrade infrastructure
    """)
    
    # ============================================================================
    # SECTION 5: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Industry Scale:**
        - 80%+ of global trade moves by sea
        - Asia handles 64% of seaborne trade
        - Straits of Malacca/Singapore: 33% of global trade
        
        **Container Revolution:**
        - 94% cost reduction vs break-bulk
        - Enabled modern globalization
        - Standardization is key
        
        **Mega Vessels:**
        - Evolution from 500 TEU → 25,000 TEU
        - Driven by economies of scale
        - Requires specialized port infrastructure
        """)
    
    with col2:
        st.markdown("""
        **Mega Alliances:**
        - 3 alliances control 83% of market
        - Industry consolidated from 15 → 9 players
        - Alliances dictate port requirements
        
        **Changing Cargo:**
        - Geopolitical shifts (US-China tensions)
        - E-commerce growth
        - More complex supply chains
        
        **Maritime as Team Sport:**
        - Requires coordination across entire ecosystem
        - Success depends on all stakeholders
        - Technology enables collaboration
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> The maritime industry is the foundation of global trade, but it's 
    being transformed by massive vessels, powerful alliances, and changing trade patterns. Understanding 
    these forces is essential to understanding how ports must adapt to remain competitive.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** 📦 Containers & Containerization - Dive into the standardized boxes that make all this possible.
    """)
