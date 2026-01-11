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
    - **Over 80% of global trade by volume** travels by sea
    - Sea transport is the most cost-effective mode for bulk cargo
    - Container ships connect all continents and major economies
    - Modern vessels can carry over 20,000 containers
    
    **Why Sea Transport Dominates:**
    - **Cost-effective**: Most economical mode for international bulk cargo transport
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
        
        **Characteristics:**
        - Loading and unloading was labour-intensive
        - Operations were highly inefficient
        - Manual handling increased costs significantly
        - Theft and damage common with loose cargo
        
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
        
        **Transformation:**
        - **94% cost reduction** in shipping per tonne
        - Dramatically faster loading and unloading
        - Minimal labour (automated cranes)
        - Theft and damage drastically reduced
        
        **Impact:**
        - Shipping costs collapsed
        - More voyages per ship per year
        - Global supply chains became viable
        - Manufacturing moved to low-cost countries
        - "Flat world" globalisation enabled
        """)
    
    # Before/After comparison - focusing on verified data
    comparison_data = pd.DataFrame({
        'Aspect': [
            'Labour Intensity',
            'Productivity',
            'Cost Impact',
            'Efficiency',
            'Security'
        ],
        'Break-Bulk (Before)': [
            'Highly labour-intensive',
            '1.7 tons per hour',
            'Baseline cost',
            'Highly inefficient',
            'Theft and damage common'
        ],
        'Containerised (After)': [
            'Minimal labour (automated)',
            '30 tons per hour',
            '94% cost reduction',
            'Highly efficient',
            'Secure sealed containers'
        ]
    })
    
    st.dataframe(comparison_data, width='stretch', hide_index=True)
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 The Container Revolution Impact:</strong><br>
    - <strong>94% cost reduction</strong> in shipping per tonne (verified research finding)<br>
    - <strong>Productivity increase</strong>: From 1.7 tons/hour to 30 tons/hour<br>
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
    - **1956**: First container ships (Ideal-X era) - 500-800 TEU capacity
    - **1970**: Fully Cellular ships - 1,000-2,500 TEU
    - **1980**: Panamax - 3,000-3,400 TEU
    - **1988**: Post-Panamax I - 4,000-6,000 TEU
    - **2000**: Post-Panamax II - 6,000-8,500 TEU
    - **2006**: VLCS (Very Large Container Ships) - 11,000-15,000 TEU
    - **2013**: ULCS (Ultra Large Container Ships) - 18,000-21,000 TEU
    - **2019**: MGX-24 - 21,000-25,000 TEU
    
    **Example: CMA CGM Jacques Saadé (LNG-powered)**
    - Capacity: 23,112 TEU
    - Length: 400m (longer than 4 football fields)
    - Width: 61m
    - Height: 78m
    - Draft: 16m
    - Crew: 26 personnel
    
    **Driver: Economics of Scale**
    - Larger vessels = lower cost per container transported
    - Fuel efficiency improves with size (per TEU)
    - Crew costs spread over more containers
    - Fundamental economic advantage drives continued growth
    """)
    
    # Vessel size evolution visualization
    vessel_evolution = pd.DataFrame({
        'Year': [1956, 1970, 1980, 1988, 2000, 2006, 2013, 2019],
        'TEU Capacity': [650, 1750, 3200, 5000, 7250, 13000, 19500, 23000],
        'Category': ['Early Container', 'Fully Cellular', 'Panamax', 'Post-Panamax I', 
                     'Post-Panamax II', 'VLCS', 'ULCS', 'MGX-24']
    })
    
    fig = go.Figure(data=[
        go.Scatter(
            x=vessel_evolution['Year'],
            y=vessel_evolution['TEU Capacity'],
            mode='lines+markers',
            line=dict(color='#2563EB', width=3),
            marker=dict(size=10, color='#3B82F6'),
            text=vessel_evolution['Category'],
            hovertemplate='<b>%{text}</b><br>Year: %{x}<br>Capacity: %{y:,} TEU<extra></extra>'
        )
    ])
    
    fig.update_layout(
        title={
            'text': 'Container Vessel Size Evolution (1956-2019)',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        xaxis_title="Year",
        yaxis_title="Capacity (TEU)",
        height=450,
        plot_bgcolor='white',
        xaxis=dict(gridcolor='#E5E7EB'),
        yaxis=dict(gridcolor='#E5E7EB')
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ The Mega-Vessel Challenge:</strong><br>
    While larger vessels reduce per-container costs, they create new challenges:<br>
    - <strong>Port infrastructure</strong>: Need deeper berths, larger cranes, bigger yards<br>
    - <strong>Concentration risk</strong>: Fewer ports can handle mega-vessels<br>
    - <strong>Schedule reliability</strong>: One delay affects thousands of containers<br>
    - <strong>Capital intensity</strong>: Only large carriers can afford these vessels<br>
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Wave 2: Mega Alliances
    # ============================================================================
    
    st.markdown('<p class="subsection-header">Wave 2: Mega Alliances (Consolidation)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Trend:**
    Shipping lines have formed strategic alliances to share vessels, routes, and resources, leading to 
    massive industry consolidation.
    
    **Alliance Evolution:**
    - **1990s**: 0% of volumes controlled by alliances
    - **2000s**: 30% alliance control
    - **2015**: 75% alliance control
    - **2017-2024**: >80% alliance control
    
    **Current Landscape: Three Major Alliances Control 83%**
    
    The industry has consolidated from 15+ major carriers to 3 dominant alliances representing 9 main players:
    """)
    
    # Alliance data
    alliance_data = pd.DataFrame({
        'Alliance': ['2M', 'Ocean Alliance', 'THE Alliance', 'Others'],
        'Market Share (%)': [34, 30, 19, 17],
        'Key Members': [
            'Maersk, MSC',
            'CMA CGM, COSCO, OOCL, Evergreen',
            'ONE (MOL, K-Line, NYK), Yang Ming, Hapag-Lloyd, HMM',
            'ZIM, Wan Hai Lines, KMTC, PIL, and others'
        ]
    })
    
    st.dataframe(alliance_data, width='stretch', hide_index=True)
    
    # Alliance market share visualization
    fig = go.Figure(data=[
        go.Pie(
            labels=alliance_data['Alliance'],
            values=alliance_data['Market Share (%)'],
            hole=0.4,
            marker=dict(colors=['#1E40AF', '#3B82F6', '#60A5FA', '#93C5FD']),
            textinfo='label+percent',
            textfont=dict(size=14)
        )
    ])
    
    fig.update_layout(
        title={
            'text': 'Global Container Shipping Market Share by Alliance',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        height=450,
        showlegend=True
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    **Why Alliances Form:**
    - **Vessel sharing**: Pool capacity to fill ships efficiently
    - **Network reach**: Access alliance partners' routes without owning vessels
    - **Cost reduction**: Share slot costs, terminal operations
    - **Schedule reliability**: Backup capacity when vessels delayed
    - **Market power**: Collective bargaining with ports and suppliers
    
    **Impact on Ports:**
    - **Winner-takes-most**: Alliances choose hub ports strategically
    - **Volume concentration**: Example - Ocean Alliance shifted operations to Singapore in April 2017
    - **Infrastructure demands**: Must accommodate alliance vessel sizes and volumes
    - **Competitive pressure**: Ports must attract and retain alliance business
    """)
    
    st.markdown("""
    <div class="info-box">
    <strong>📊 Alliance Timeline Evolution:</strong><br>
    The progression from 0% (1990s) → 30% (2000s) → 75% (2015) → >80% (2017-2024) shows rapid industry 
    consolidation. Today's three mega-alliances carrying 83% of global volumes represent a fundamental 
    shift in maritime power structures.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Wave 3: Cargo Changes
    # ============================================================================
    
    st.markdown('<p class="subsection-header">Wave 3: Cargo Changes (New Trade Patterns)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Trend:**
    Global trade patterns are shifting due to geopolitics, e-commerce growth, and supply chain resilience concerns.
    """)
    
    st.markdown("""
    **Geopolitical Shifts: "China+1" Strategy**
    
    US-China trade tensions have prompted companies to diversify manufacturing beyond China, creating new trade routes:
    """)
    
    # Trade pattern changes - ONLY VERIFIED DATA FROM LECTURE NOTES
    trade_changes = pd.DataFrame({
        'Region': ['Vietnam', 'Malaysia', 'Thailand', 'Mexico'],
        'Export Growth 2018-2022 (%)': [80, 45, 41, 42],
        'Primary Driver': [
            'China+1, low-cost manufacturing',
            'Electronics, electrical goods',
            'Automotive, electronics',
            'Nearshoring to US'
        ]
    })
    
    fig = go.Figure(data=[
        go.Bar(
            x=trade_changes['Region'],
            y=trade_changes['Export Growth 2018-2022 (%)'],
            marker=dict(color='#F59E0B'),
            text=trade_changes['Export Growth 2018-2022 (%)'],
            texttemplate='%{text}%',
            textposition='outside'
        )
    ])
    
    fig.update_layout(
        title={
            'text': 'Export Growth in "China+1" Countries (2018-2022)',
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
    
    st.markdown("""
    **Key Observations:**
    - Vietnam leads with 80% export growth (major beneficiary of China+1)
    - Malaysia and Thailand show strong growth in electronics/automotive
    - Mexico benefits from nearshoring to US market
    - Trade patterns increasingly bypass direct US-China routes
    - Supply chains becoming longer and more complex
    """)
    
    st.markdown("""
    **E-Commerce Growth:**
    
    **Characteristics:**
    - Smaller, more frequent shipments
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
    
    # ============================================================================
    # SECTION 4: Maritime Economics
    # ============================================================================
    
    st.markdown('<p class="section-header">Maritime Economics: The Business of Shipping</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Understanding the economics helps explain why ports and shipping lines make certain strategic decisions.
    """)
    
    st.markdown('<p class="subsection-header">Economic Fundamentals</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Shipping Line Economics:**
        
        **Cost Structure:**
        - High fixed costs (vessel, crew, insurance)
        - Significant variable costs (fuel, port charges)
        - Empty sailing still incurs most costs
        
        **Key Challenges:**
        - Need high vessel utilisation
        - Fuel is largest variable cost
        - Port efficiency critical to schedule reliability
        - Pressure to fill vessels even at lower rates
        """)
    
    with col2:
        st.markdown("""
        **Port Economics:**
        
        **Cost Structure:**
        - Very high fixed costs (infrastructure, cranes, IT systems)
        - Lower variable costs (labour, utilities)
        - Marginal cost of handling additional containers is low
        
        **Key Challenges:**
        - Need high throughput to spread fixed costs
        - Must attract and retain alliance business
        - Competitive pricing when utilisation is good
        - Infrastructure investments are massive and long-term
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
        - Over 80% of global trade by volume travels by sea
        - 64% handled by Asian ports
        - 33% passes through Singapore/Malacca Strait
        - Most cost-effective transport for bulk goods
        - Enables globalisation and international commerce
        
        **Container Revolution:**
        - 1956: Malcolm McLean's standardised container
        - 94% reduction in shipping costs per tonne
        - Productivity: 1.7 → 30 tons per hour
        - Enabled "flat world" globalisation
        - Made just-in-time manufacturing possible
        """)
    
    with col2:
        st.markdown("""
        **Three Waves of Change:**
        - **Wave 1**: Mega vessels (500-800 TEU → 21,000-25,000 TEU)
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
    over 80% of trade. The 1956 container revolution reduced costs by 94% and enabled globalisation. Today, the 
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
