import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">⚓ Maritime Industry Foundation</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand why maritime trade matters globally, how containerisation revolutionised shipping, 
    and the three major waves of change reshaping the industry today.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Why Maritime Matters
    # ============================================================================
    
    st.markdown('<p class="section-header">Why Maritime Trade Matters</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Maritime shipping is the backbone of global commerce, yet it operates largely out of sight. 
    Understanding its scale and importance is the first step in appreciating the complexity of 
    port operations.
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Global Trade by Sea", "80%+", help="Over 80% of global trade by volume is transported by sea")
    with col2:
        st.metric("Asian Port Dominance", "64%", help="64% of global container throughput handled by Asian ports")
    with col3:
        st.metric("Via Singapore/Malacca", "33%", help="33% of global trade passes through Malacca Strait/Singapore")
    
    st.markdown("""
    **The Hidden Foundation of Global Trade:**
    
    Maritime shipping moves the physical goods that power the global economy. Nearly everything we use 
    daily—from smartphones to clothing to food—has travelled by container ship at some point in its 
    supply chain.
    
    **Scale of Maritime Operations:**
    - **50,000+ merchant ships** operate globally
    - **5,400+ container ships** specifically handle containerised cargo
    - **800 million+ TEU** moved annually (Twenty-foot Equivalent Units)
    - **$14 trillion** worth of goods transported by sea each year
    - **90% of world trade by volume** travels by sea
    
    **Why Sea Transport Dominates:**
    - **Cost-effective**: 10-40x cheaper than air freight per tonne-kilometre
    - **High capacity**: Single large vessel carries 20,000+ containers
    - **Energy efficient**: Most fuel-efficient mode for bulk cargo
    - **Global reach**: Connects all continents and major economies
    - **Scalable**: Can handle everything from raw materials to finished goods
    """)
    
    # ============================================================================
    # SECTION 2: The Container Revolution
    # ============================================================================
    
    st.markdown('<p class="section-header">The Container Revolution: How a Simple Box Changed Everything</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Before containerisation, shipping was slow, expensive, and labour-intensive. The introduction of 
    standardised containers in 1956 transformed global trade.
    """)
    
    st.markdown('<p class="subsection-header">Before Containers: Break-Bulk Shipping</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **The Old Way (Pre-1956):**
        
        **Break-Bulk Method:**
        - Cargo loaded piece by piece (crates, barrels, sacks)
        - Manual handling by longshoremen (dockworkers)
        - Each item lifted by crane or carried by hand
        - Stowed carefully in ship's hold
        
        **Time and Cost:**
        - **7-10 days** to load/unload a single ship
        - **50-70% of total voyage time** spent in port
        - Labour costs extremely high
        - Theft and damage common (loose cargo)
        
        **Impact:**
        - Shipping expensive → International trade limited
        - Long port stays → Fewer voyages per ship per year
        - Labour-intensive → High costs, strikes common
        - Inefficient → Goods remained expensive
        """)
    
    with col2:
        st.markdown("""
        **The Container Solution (1956+):**
        
        **Standardised Container:**
        - Sealed metal box (20ft or 40ft standard)
        - Loaded once at factory, sealed, opened at destination
        - Handled by specialised cranes and equipment
        - Can transfer between ship, truck, train without unpacking
        
        **Time and Cost:**
        - **<24 hours** to load/unload same ship
        - **<10% of total voyage time** in port
        - Minimal labour (automated cranes)
        - Theft and damage drastically reduced
        
        **Impact:**
        - Shipping costs collapsed (94% reduction per tonne)
        - More voyages per ship per year
        - Global supply chains became viable
        - Manufacturing moved to low-cost countries
        - "Flat world" globalisation enabled
        """)
    
    # Before/After comparison
    comparison_data = pd.DataFrame({
        'Metric': [
            'Loading/Unloading Time',
            'Port Time % of Voyage',
            'Cost per Tonne',
            'Labour Required',
            'Theft/Damage Rate',
            'Voyages per Ship/Year'
        ],
        'Break-Bulk (Before)': [
            '7-10 days',
            '50-70%',
            '$420 (indexed)',
            '100 workers',
            '20-30%',
            '4-5 voyages'
        ],
        'Containerised (After)': [
            '<24 hours',
            '<10%',
            '$25 (94% reduction)',
            '10-15 workers',
            '<1%',
            '12-15 voyages'
        ]
    })
    
    st.dataframe(comparison_data, width='stretch', hide_index=True)
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 The Container Revolution Impact:</strong><br>
    - <strong>94% cost reduction</strong> in shipping per tonne<br>
    - <strong>10x faster</strong> port operations<br>
    - <strong>3x more voyages</strong> per ship per year<br>
    - <strong>Enabled globalisation</strong>: Made international trade economically viable for most goods<br>
    - <strong>Supply chain transformation</strong>: "Just-in-time" manufacturing became possible<br>
    - <strong>Economic development</strong>: Developing nations could access global markets<br><br>
    Malcolm McLean's simple idea—a standardised metal box—fundamentally changed the world economy.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">Key Container Standards</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **ISO Container Standards (International Organisation for Standardization):**
    
    **Standard Sizes:**
    - **20-foot container**: 20ft long × 8ft wide × 8ft 6in high
    - **40-foot container**: 40ft long × 8ft wide × 8ft 6in high
    - **40-foot High Cube**: 40ft long × 8ft wide × 9ft 6in high
    
    **Why Standardisation Matters:**
    - **Interoperability**: Any container fits any ship, crane, truck, train
    - **Infrastructure**: Ports design for standard dimensions
    - **Equipment**: Cranes, chassis designed for standard sizes
    - **Global system**: Works everywhere in the world
    - **Economies of scale**: Mass production of containers and equipment
    
    **The TEU Measure:**
    - **TEU = Twenty-foot Equivalent Unit**
    - Standard unit for measuring container capacity
    - One 20ft container = 1 TEU
    - One 40ft container = 2 TEU
    - Vessel capacity measured in TEU (e.g., "20,000 TEU vessel")
    """)
    
    # ============================================================================
    # SECTION 3: Three Waves of Change
    # ============================================================================
    
    st.markdown('<p class="section-header">Three Waves of Change Reshaping Maritime</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The maritime industry is currently experiencing three simultaneous transformations that are fundamentally 
    changing how shipping operates.
    """)
    
    st.markdown('<p class="subsection-header">Wave 1: Mega Vessels (Scale)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Trend:**
    Container ships have grown dramatically in size over the past 60 years, driven by economies of scale.
    
    **Evolution:**
    - **1956**: First container ship (Ideal X) - 500 TEU capacity
    - **1980s**: Panamax vessels - 4,500 TEU (limited by Panama Canal width)
    - **2006**: Post-Panamax - 15,000 TEU
    - **2013**: Maersk Triple-E - 18,000 TEU
    - **2019**: MSC Gülsün - 23,756 TEU (current largest)
    - **Today**: Multiple vessels >20,000 TEU operating
    
    **Why Bigger?**
    - **Economies of scale**: Larger vessels cost less per container moved
    - **Crew costs**: Same ~25 crew whether ship carries 5,000 or 20,000 TEU
    - **Fuel efficiency**: Larger vessels more efficient per TEU
    - **Port costs**: Fixed port fees spread over more containers
    
    **Result**: A 20,000 TEU vessel costs roughly **40-50% less per TEU** than a 5,000 TEU vessel
    """)
    
    # Vessel size evolution chart
    vessel_evolution = pd.DataFrame({
        'Year': [1956, 1980, 2000, 2010, 2020],
        'Max Vessel Size (TEU)': [500, 4500, 8000, 15000, 24000],
        'Typical Vessel (TEU)': [500, 3000, 5000, 8000, 12000]
    })
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=vessel_evolution['Year'],
        y=vessel_evolution['Max Vessel Size (TEU)'],
        mode='lines+markers',
        name='Maximum Vessel Size',
        line=dict(color='#EF4444', width=3),
        marker=dict(size=10)
    ))
    
    fig.add_trace(go.Scatter(
        x=vessel_evolution['Year'],
        y=vessel_evolution['Typical Vessel (TEU)'],
        mode='lines+markers',
        name='Typical Vessel Size',
        line=dict(color='#3B82F6', width=3),
        marker=dict(size=10)
    ))
    
    fig.update_layout(
        title={
            'text': 'Container Vessel Size Evolution (1956-2020)',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        xaxis_title="Year",
        yaxis_title="Vessel Capacity (TEU)",
        height=400,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='#E5E7EB'),
        xaxis=dict(gridcolor='#E5E7EB'),
        legend=dict(x=0.02, y=0.98)
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    **Impact on Ports:**
    - Ports must invest in deeper berths (16+ metres)
    - Larger cranes needed (65-80m outreach for 24 containers across)
    - Longer berths required (400+ metres)
    - More complex stowage planning
    - Only 20-30 ports globally can handle mega vessels
    """)
    
    st.markdown('<p class="subsection-header">Wave 2: Mega Alliances (Concentration)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Trend:**
    Shipping lines have consolidated from many independent carriers into three dominant alliances.
    
    **The Consolidation:**
    - **Year 2000**: 15+ major independent carriers competing
    - **Year 2024**: 9 major carriers organised into 3 alliances
    - **Current state**: Three alliances control **83% of global container capacity**
    
    **The Big Three Alliances:**
    
    **1. 2M Alliance (34% market share)**
    - MSC (Mediterranean Shipping Company)
    - Maersk Line
    - Formed: 2015
    
    **2. Ocean Alliance (30% market share)**
    - CMA CGM
    - COSCO
    - OOCL
    - Evergreen
    - Formed: 2017
    
    **3. THE Alliance (19% market share)**
    - ONE (Ocean Network Express)
    - HMM (Hyundai Merchant Marine)
    - Yang Ming
    - Formed: 2017
    
    **Why Alliances?**
    - **Network coverage**: No single carrier can serve all ports economically
    - **Vessel sharing**: Share capacity, improve utilisation
    - **Cost reduction**: Economies of scale on operations
    - **Frequency**: Offer daily or multiple weekly services by pooling vessels
    - **Survival**: Overcapacity crisis forced cooperation
    """)
    
    # Alliance market share
    alliance_data = pd.DataFrame({
        'Year': [2000, 2005, 2010, 2015, 2020, 2024],
        'Alliance Control (%)': [0, 15, 35, 60, 82, 83],
        'Major Carriers': [17, 15, 15, 15, 10, 9]
    })
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=alliance_data['Year'],
        y=alliance_data['Alliance Control (%)'],
        mode='lines+markers',
        name='Alliance Control %',
        line=dict(color='#10B981', width=4),
        marker=dict(size=12),
        fill='tozeroy',
        fillcolor='rgba(16, 185, 129, 0.2)'
    ))
    
    fig.update_layout(
        title={
            'text': 'Alliance Control of Global Container Capacity',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        xaxis_title="Year",
        yaxis_title="Alliance Control (%)",
        height=400,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='#E5E7EB', range=[0, 100]),
        xaxis=dict(gridcolor='#E5E7EB')
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    **Impact on Ports:**
    - Ports negotiate with alliances (not individual carriers)
    - Need to accommodate multiple alliance members simultaneously
    - Long-term terminal lease agreements with alliances
    - Port strategy must attract/retain alliance business
    - Losing an alliance = losing significant throughput
    """)
    
    st.markdown('<p class="subsection-header">Wave 3: Cargo Changes (Complexity)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Trend:**
    The nature of cargo and trade patterns is changing due to geopolitics, e-commerce, and supply chain shifts.
    
    **Geopolitical Shifts:**
    
    **US-China Trade Tensions:**
    - Tariffs and trade restrictions
    - "China+1" strategy: Companies diversifying manufacturing beyond China
    - Intermediate countries growing (Vietnam +80%, Malaysia +45%, Thailand +41%)
    - More complex, multi-hop supply chains
    - Impact: Shifting trade lanes, more transshipment
    
    **Nearshoring/Friendshoring:**
    - Moving production closer to consumers (reduce risk, faster delivery)
    - Emphasis on allied/trusted countries
    - Mexico growing for US market (+42%)
    - Eastern Europe growing for EU market
    - Impact: Shorter trade routes, different port demands
    
    **E-commerce Explosion:**
    
    **Changing Cargo Characteristics:**
    - Smaller, more frequent shipments (vs bulk orders)
    - Higher value goods (consumer electronics, fashion)
    - Time-sensitive delivery expectations
    - More SKUs (Stock Keeping Units) = more complexity
    - Direct-to-consumer models
    
    **Impact on Logistics:**
    - Need for faster port turnaround
    - More complex inventory management
    - Higher frequency of smaller container movements
    - Last-mile delivery challenges
    - Integration of maritime with e-commerce platforms
    
    **Supply Chain Resilience:**
    
    **Post-COVID Lesson:**
    - Single-source dependencies are risky
    - "Just-in-time" vulnerable to disruptions
    - "Just-in-case" inventory becoming more common
    - Redundancy and flexibility valued over pure cost optimisation
    
    **New Priorities:**
    - Visibility: Real-time tracking and transparency
    - Agility: Ability to adapt quickly to disruptions
    - Resilience: Multiple suppliers, routes, and options
    - Sustainability: Environmental pressures growing
    """)
    
    # Trade pattern changes
    trade_changes = pd.DataFrame({
        'Region': ['Vietnam', 'Malaysia', 'Thailand', 'Mexico', 'India', 'Poland'],
        'Export Growth 2018-2023 (%)': [80, 45, 41, 42, 35, 28],
        'Primary Driver': [
            'China+1, low-cost manufacturing',
            'Electronics, electrical goods',
            'Automotive, electronics',
            'Nearshoring to US',
            'Pharmaceuticals, IT',
            'Nearshoring to EU'
        ]
    })
    
    fig = go.Figure(data=[
        go.Bar(
            x=trade_changes['Region'],
            y=trade_changes['Export Growth 2018-2023 (%)'],
            marker=dict(color='#F59E0B'),
            text=trade_changes['Export Growth 2018-2023 (%)'],
            texttemplate='%{text}%',
            textposition='outside'
        )
    ])
    
    fig.update_layout(
        title={
            'text': 'Export Growth in "China+1" Countries (2018-2023)',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        xaxis_title="Country",
        yaxis_title="Export Growth (%)",
        height=400,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='#E5E7EB')
    )
    
    st.plotly_chart(fig, width='stretch')
    
    # ============================================================================
    # SECTION 4: Maritime Economics
    # ============================================================================
    
    st.markdown('<p class="section-header">Maritime Economics: The Business of Shipping</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Understanding the economics helps explain why ports and shipping lines make certain strategic decisions.
    """)
    
    st.markdown('<p class="subsection-header">Cost Structure</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Shipping Line Costs:**
        
        **Fixed Costs (60-70%):**
        - Vessel purchase/lease
        - Crew salaries
        - Insurance
        - Administration
        - IT systems
        
        **Variable Costs (30-40%):**
        - Fuel (largest variable cost)
        - Port charges
        - Container handling
        - Maintenance
        - Canal fees
        
        **Implication:**
        - High fixed costs → Need high utilisation
        - Empty sailing still costs ~70% of full sailing
        - Pressure to fill vessels even at low rates
        """)
    
    with col2:
        st.markdown("""
        **Port Costs:**
        
        **Fixed Costs (70-80%):**
        - Infrastructure (berths, cranes, land)
        - IT systems (TOS, PORTNET)
        - Administration
        - Maintenance
        
        **Variable Costs (20-30%):**
        - Labour (operators, drivers)
        - Equipment maintenance
        - Utilities
        
        **Implication:**
        - High fixed costs → Need high throughput
        - Marginal cost of handling one more container is low
        - Can offer competitive pricing when utilisation is good
        """)
    
    st.markdown("""
    **The Virtuous/Vicious Cycle:**
    
    **Virtuous Cycle (Successful Ports):**
    1. High throughput → Low cost per TEU
    2. Low cost → Competitive pricing
    3. Competitive pricing → Attracts more shipping lines
    4. More lines → Better connectivity
    5. Better connectivity → Attracts more cargo
    6. More cargo → Higher throughput (back to step 1)
    
    **Vicious Cycle (Struggling Ports):**
    1. Low throughput → High cost per TEU
    2. High cost → Uncompetitive pricing
    3. Uncompetitive pricing → Shipping lines avoid port
    4. Fewer lines → Poor connectivity
    5. Poor connectivity → Less cargo
    6. Less cargo → Lower throughput (back to step 1)
    
    **Strategic Implication:** Ports must maintain and grow volumes to stay competitive. This drives massive 
    infrastructure investments like Singapore's Tuas Mega Port.
    """)
    
    # ============================================================================
    # SECTION 5: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Why Maritime Matters:**
        - 80%+ of global trade by volume travels by sea
        - Most cost-effective transport for bulk goods
        - Enables globalisation and international commerce
        - 50,000+ ships, 800M+ TEU annually
        
        **Container Revolution:**
        - 1956: Malcolm McLean's standardised container
        - 94% reduction in shipping costs per tonne
        - 10x faster port operations
        - Enabled "flat world" globalisation
        - Made just-in-time manufacturing possible
        """)
    
    with col2:
        st.markdown("""
        **Three Waves of Change:**
        - **Wave 1**: Mega vessels (500 TEU → 24,000 TEU)
        - **Wave 2**: Mega alliances (3 alliances control 83%)
        - **Wave 3**: Cargo changes (geopolitics, e-commerce, resilience)
        
        **Maritime Economics:**
        - High fixed costs → Need high utilisation
        - Virtuous vs vicious cycles
        - Scale advantages crucial
        - Strategic infrastructure investments essential
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Maritime shipping is the invisible backbone of global commerce, moving 
    80%+ of trade. The 1956 container revolution reduced costs by 94% and enabled globalisation. Today, the 
    industry faces three simultaneous transformations: mega vessels (economies of scale), mega alliances 
    (consolidation to 3 alliances controlling 83%), and cargo changes (geopolitics, e-commerce, supply chain 
    resilience). Understanding these fundamentals is essential for grasping why ports like Singapore invest 
    billions in infrastructure and how these complex operations work.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** 📦 Containers & Containerisation - Dive deep into container standards, types, 
    measurements, and the TEU system that makes global shipping possible.
    """)
