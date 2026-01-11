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
        st.metric("Global Trade by Sea", "80%", help="80% of global trade by volume is transported by sea")
    with col2:
        st.metric("Asian Port Dominance", "64%", help="64% of global container throughput handled by Asian ports")
    with col3:
        st.metric("Via Singapore/Malacca", "33%", help="33% of global trade passes through Malacca Strait/Singapore")
    
    st.markdown("""
    **The Hidden Foundation of Global Trade:**
    
    Maritime shipping moves the physical goods that power the global economy. Nearly everything we use 
    daily—from smartphones to clothing to food—has travelled by container ship at some point in its 
    supply chain.
    
    **Scale of Maritime Operations (2024):**
    - **109,000 merchant vessels** operate globally (UNCTAD, vessels ≥100 gross tons)
    - **~6,300 container ships** specifically handle containerised cargo
    - **30+ million TEU** global container fleet capacity (first time surpassed in 2024)
    - **12.3 billion tonnes** of goods transported by sea in 2023
    - **80% of world trade by volume** travels by sea
    - **2.4 billion deadweight tonnes** total fleet capacity globally
    
    **Why Sea Transport Dominates:**
    - **Cost-effective**: Significantly cheaper than air freight for bulk cargo
    - **High capacity**: Single large vessel carries 24,000+ containers (worth $500M+ cargo)
    - **Energy efficient**: Most fuel-efficient mode for bulk cargo per tonne-kilometre
    - **Global reach**: Connects all continents and major economies
    - **Scalable**: Can handle everything from raw materials to finished goods
    
    **Recent Developments (2024):**
    - Container fleet grew by **8-10%** in 2023-2024, fastest growth in years
    - **478 new container ships** delivered in 2024 alone (3.1M TEU capacity)
    - Fleet renewal accelerating with focus on alternative fuels (50% of orderbook)
    - Geopolitical disruptions (Red Sea, Suez Canal) causing longer routes
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
        
        **Challenges:**
        - **Extremely time-consuming**: Days to load/unload a single ship
        - **Labour-intensive**: Hundreds of workers needed per ship
        - **High theft and damage**: Loose cargo vulnerable
        - **Port congestion**: Ships spent majority of voyage time in port
        - **Expensive**: Labour costs dominated shipping economics
        
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
        
        **Breakthrough Advantages:**
        - **Rapid loading/unloading**: Hours instead of days
        - **Minimal labour**: Automated cranes replace hundreds of workers
        - **Theft and damage drastically reduced**: Sealed containers
        - **Intermodal efficiency**: Seamless ship-truck-train transfer
        - **Standardisation**: Works everywhere globally
        
        **Impact:**
        - Shipping costs collapsed dramatically
        - More voyages per ship per year
        - Global supply chains became viable
        - Manufacturing moved to optimal locations
        - "Flat world" globalisation enabled
        - Just-in-time manufacturing made possible
        """)
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 The Container Revolution Impact:</strong><br>
    Malcolm McLean's simple idea—a standardised metal box—fundamentally changed the world economy. In 1956, 
    the Ideal-X sailed into Houston with 58 containers, and 58 trucks waited to haul them onwards. This 
    marked the birth of modern containerisation. The standardised container eliminated the need to handle 
    individual items thousands of times, reduced theft, enabled automation, and created a globally 
    interoperable system. Today, over 30 million TEU of container capacity moves goods worth trillions of 
    dollars annually.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">Key Container Standards</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **ISO Container Standards (International Organisation for Standardisation):**
    
    **Standard Sizes:**
    - **20-foot container**: 20ft long × 8ft wide × 8ft 6in high (internal volume: ~33 cubic metres)
    - **40-foot container**: 40ft long × 8ft wide × 8ft 6in high (internal volume: ~67 cubic metres)
    - **40-foot High Cube**: 40ft long × 8ft wide × 9ft 6in high (internal volume: ~76 cubic metres)
    
    **Why Standardisation Matters:**
    - **Interoperability**: Any container fits any ship, crane, truck, train anywhere in the world
    - **Infrastructure**: Ports, terminals design for standard dimensions globally
    - **Equipment**: Cranes, chassis, stackers designed for standard sizes
    - **Global system**: Works seamlessly across all countries and continents
    - **Economies of scale**: Mass production of containers and handling equipment
    - **Predictability**: Shippers know exactly what fits and how to pack
    
    **The TEU Measure:**
    - **TEU = Twenty-foot Equivalent Unit**
    - Standard unit for measuring container capacity industry-wide
    - One 20ft container = 1 TEU
    - One 40ft container = 2 TEU
    - One 40ft High Cube = 2 TEU
    - Vessel capacity measured in TEU (e.g., "24,000 TEU vessel")
    - Port throughput measured in TEU (e.g., "Singapore: 37.3M TEU annually")
    """)
    
    # ============================================================================
    # SECTION 3: Three Waves of Change
    # ============================================================================
    
    st.markdown('<p class="section-header">Three Waves of Change Reshaping Maritime</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The maritime industry is currently experiencing three simultaneous transformations that are fundamentally 
    changing how shipping operates. These three waves were identified by industry leaders and represent the 
    most significant shifts since containerisation itself.
    """)
    
    st.markdown('<p class="subsection-header">Wave 1: Mega Vessels (Scale)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Trend:**
    Container ships have grown dramatically in size over the past 60 years, driven by relentless pursuit of 
    economies of scale.
    
    **Evolution Timeline:**
    - **1956**: First container ship (Ideal X) - 500 TEU capacity
    - **1970**: Early cellular ships - 1,500-2,500 TEU
    - **1980s**: Panamax vessels - 3,000-4,500 TEU (limited by Panama Canal width of 32.3m)
    - **1988**: Panamax Max - 4,500 TEU (physical Panama Canal limit)
    - **2000**: Post-Panamax I - 6,000 TEU (wider than canal)
    - **2006**: Post-Panamax II / Emma Maersk - 15,000 TEU
    - **2013**: Maersk Triple-E - 18,270 TEU
    - **2014**: CSCL 18400 Class - 18,400 TEU
    - **2016**: New Panama Canal opens (49m width) - enables 14,500 TEU vessels
    - **2019**: MGX-24 Class - 21,000-25,000 TEU
    - **2020**: CMA CGM Jacques Saade - 23,112 TEU (largest LNG-powered)
    - **Today**: Multiple vessels >23,000 TEU operating, 24 containers across beam
    
    **Why Bigger? The Economics of Scale:**
    - **Crew costs**: Same ~25-26 crew whether ship carries 5,000 or 24,000 TEU
    - **Fuel efficiency**: Larger vessels more efficient per TEU (up to 50% savings)
    - **Port costs**: Fixed port fees spread over more containers
    - **Capital costs**: Building costs don't scale linearly with capacity
    
    **Result**: A 20,000 TEU vessel can cost **40-50% less per TEU** to operate than a 5,000 TEU vessel
    
    **Physical Dimensions of Modern Mega Vessels:**
    - **Length**: 400 metres (longer than 4 football fields)
    - **Width (Beam)**: 61 metres (24 containers across)
    - **Height**: 78 metres above waterline
    - **Draft**: 16 metres (depth in water)
    - **Capacity**: 24,000+ TEU
    - **Cargo Value**: Typically $400-600 million per vessel
    - **Crew**: 25-26 people
    """)
    
    # Vessel size evolution chart
    vessel_evolution = pd.DataFrame({
        'Year': [1956, 1980, 2000, 2010, 2015, 2020, 2024],
        'Max Vessel Size (TEU)': [500, 4500, 8000, 15000, 18400, 24000, 25000],
        'Typical Vessel (TEU)': [500, 3000, 5000, 8000, 10000, 14000, 16000]
    })
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=vessel_evolution['Year'],
        y=vessel_evolution['Max Vessel Size (TEU)'],
        mode='lines+markers',
        name='Maximum Vessel Size',
        line=dict(color='#EF4444', width=3),
        marker=dict(size=10),
        fill='tonexty'
    ))
    
    fig.add_trace(go.Scatter(
        x=vessel_evolution['Year'],
        y=vessel_evolution['Typical Vessel (TEU)'],
        mode='lines+markers',
        name='Typical New Vessel Size',
        line=dict(color='#3B82F6', width=3),
        marker=dict(size=10),
        fill='tozeroy',
        fillcolor='rgba(59, 130, 246, 0.2)'
    ))
    
    fig.update_layout(
        title={
            'text': 'Container Vessel Size Evolution (1956-2024)',
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
    - Ports must invest in deeper berths (16-18 metres water depth)
    - Larger cranes needed (65-80m outreach for 24 containers across)
    - Longer berths required (400+ metres)
    - More complex stowage planning and port operations
    - Only **20-30 ports globally** can fully handle 24,000+ TEU mega vessels
    - Concentration of cargo at hub ports increases
    
    **The Limit Question:**
    - **Panama Canal (New)**: Max ~14,500 TEU (49m width limit)
    - **Suez Canal**: Can handle all current sizes (77.5m width, 20.1m draft)
    - **Port infrastructure**: Crane reach, berth depth limit practical size
    - **Operational risks**: One 24,000 TEU vessel = $500M+ cargo value
    - **Market consensus**: 24,000-25,000 TEU likely practical limit for now
    """)
    
    st.markdown('<p class="subsection-header">Wave 2: Mega Alliances (Concentration)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Trend:**
    Shipping lines have consolidated dramatically from many independent carriers into three dominant alliances 
    that now control the majority of global container capacity.
    
    **The Consolidation Journey:**
    - **Year 2000**: 15+ major independent carriers competing
    - **Year 2010**: Consolidation begins with mergers
    - **Year 2017**: Three mega alliances formed
    - **Year 2024**: 9 major carriers organised into 3 alliances
    - **Current state**: Three alliances control **83% of global container capacity**
    
    **Alliance Control Over Time:**
    - **1990s**: 0% (independent carriers)
    - **2000s**: 30% (early cooperation)
    - **2015**: 75% (major alliance formation)
    - **2017-2024**: >80% (mega alliance dominance)
    """)
    
    st.markdown("""
    **The Big Three Alliances (2024):**
    
    **1. 2M Alliance (34% market share)**
    - **MSC** (Mediterranean Shipping Company - Swiss/Italian)
    - **Maersk Line** (Danish)
    - Formed: 2015
    - Fleet: ~700 vessels, ~4.2M TEU capacity
    - Note: MSC recently overtook Maersk as world's #1 carrier by capacity
    
    **2. Ocean Alliance (30% market share)**
    - **CMA CGM** (France)
    - **COSCO Shipping** (China)
    - **OOCL** (Hong Kong/China)
    - **Evergreen** (Taiwan)
    - Formed: 2017
    - Fleet: ~650 vessels, ~3.7M TEU capacity
    
    **3. THE Alliance (19% market share)**
    - **ONE (Ocean Network Express)** - Merger of Japanese carriers: NYK, MOL, K Line
    - **HMM** (Hyundai Merchant Marine - Korea)
    - **Yang Ming** (Taiwan)
    - Formed: 2017
    - Fleet: ~350 vessels, ~2.3M TEU capacity
    
    **Independent Carriers (17%)**
    - ZIM, Wan Hai, PIL, regional carriers
    """)
    
    # Alliance market share
    alliance_data = pd.DataFrame({
        'Year': [2000, 2005, 2010, 2015, 2020, 2024],
        'Alliance Control (%)': [0, 15, 35, 75, 82, 83],
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
            'text': 'Alliance Control of Global Container Capacity (2000-2024)',
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
    **Why Alliances Exist:**
    - **Network coverage**: No single carrier can serve all ports economically
    - **Vessel sharing**: Share capacity on routes, improve utilisation rates
    - **Cost reduction**: Economies of scale on operations, shared terminals
    - **Frequency**: Offer daily or multiple weekly services by pooling vessels
    - **Survival**: 2015-2016 overcapacity crisis forced cooperation or bankruptcy
    - **Bargaining power**: Negotiate better terms with ports and suppliers
    
    **How Alliances Work:**
    - **Cooperation**: Share vessels, terminals, slots on specific trade routes
    - **Competition**: Still compete on pricing, service quality, customer relationships
    - **Slot sharing**: Members buy/sell space on each other's vessels
    - **Joint services**: Operate combined Asia-Europe, Trans-Pacific routes
    - **Terminal agreements**: Share or co-locate at major hub ports
    
    **Impact on Ports:**
    - Ports negotiate with alliances (not individual carriers)
    - Need to accommodate multiple alliance members simultaneously
    - Long-term terminal lease agreements (20-30 years) with alliances
    - Port strategy must attract/retain alliance business
    - **Losing an alliance = losing 19-34% of potential throughput**
    """)
    
    st.markdown('<p class="subsection-header">Wave 3: Cargo Changes (Complexity)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Trend:**
    The nature of cargo and trade patterns is changing dramatically due to geopolitics, supply chain 
    reconfiguration, and evolving consumer behaviour.
    """)
    
    st.markdown("""
    **Geopolitical Shifts: US-China Trade Reconfiguration**
    
    **The "China+1" Strategy:**
    - Companies diversifying manufacturing beyond China (not abandoning, but adding)
    - US-China bilateral trade growth slowing or declining
    - Intermediate countries benefiting dramatically
    
    **Export Growth in China+1 Countries (2018-2022):**
    - **Vietnam**: +80% (change in total goods import value from China by USA)
    - **Malaysia**: +45%
    - **Thailand**: +41%
    - **Mexico**: +42% (nearshoring to serve US market)
    - **India**: +35% (pharmaceuticals, IT services)
    - **Poland**: +28% (nearshoring to serve EU market)
    
    **Why China+1?**
    - Geopolitical risk mitigation
    - Tariff avoidance
    - Supply chain diversification
    - Resilience against disruptions
    
    **Impact on Maritime Trade:**
    - More complex routing (multi-hop supply chains)
    - Increased transshipment volumes
    - New port-to-port trade lanes emerging
    - Greater demand for flexible, frequent services
    """)
    
    # Trade pattern changes
    trade_changes = pd.DataFrame({
        'Country': ['Vietnam', 'Mexico', 'Malaysia', 'Thailand', 'India', 'Poland', 'China'],
        'Export Growth 2018-2022 (%)': [80, 42, 45, 41, 35, 28, -0.4],
        'Primary Driver': [
            'China+1, electronics',
            'Nearshoring to US',
            'Electronics, E&E',
            'Automotive, electronics',
            'Pharma, IT, textiles',
            'Nearshoring to EU',
            'US trade tensions'
        ]
    })
    
    fig = go.Figure(data=[
        go.Bar(
            x=trade_changes['Country'],
            y=trade_changes['Export Growth 2018-2022 (%)'],
            marker=dict(color=['#10B981' if x >=0 else '#EF4444' for x in trade_changes['Export Growth 2018-2022 (%)']]),
            text=trade_changes['Export Growth 2018-2022 (%)'],
            texttemplate='%{text}%',
            textposition='outside',
            hovertemplate='<b>%{x}</b><br>Growth: %{y}%<br>Driver: %{customdata}<extra></extra>',
            customdata=trade_changes['Primary Driver']
        )
    ])
    
    fig.update_layout(
        title={
            'text': 'Export Growth: China+1 Beneficiaries (2018-2022)',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        xaxis_title="Country",
        yaxis_title="Change in Imports from China by USA (%)",
        height=450,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='#E5E7EB'),
        xaxis=dict(tickangle=-45)
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    **Critical Maritime Chokepoints Under Pressure (2024):**
    
    **Red Sea / Suez Canal Crisis:**
    - Geopolitical tensions causing vessel diversions
    - Suez transits down **70%** by mid-2024
    - Cape of Good Hope route up **89%**
    - **+3,500 nautical miles** and **+7-10 days** per voyage
    - **+$400,000** in fuel costs per Asia-Europe voyage (20,000+ TEU vessel)
    - **+12%** increase in container ship demand (longer voyages = more vessels needed)
    
    **Panama Canal Disruption:**
    - Low water levels due to drought
    - Transit restrictions and delays
    - **+31%** sailing distance for affected routes
    - Vessels diverting to Suez or around South America
    
    **Impact:**
    - Global vessel ton-mile demand up **3%** overall in 2024
    - Container shipping demand up **12%** (much longer routes)
    - Higher freight rates
    - Increased CO₂ emissions
    - Supply chain uncertainty
    """)
    
    # ============================================================================
    # SECTION 4: Maritime Economics
    # ============================================================================
    
    st.markdown('<p class="section-header">Maritime Economics: The Business of Shipping</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Understanding the economics helps explain why ports and shipping lines make certain strategic decisions.
    """)
    
    st.markdown('<p class="subsection-header">Cost Structure & Business Model</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Shipping Line Economics:**
        
        **High Fixed Costs:**
        - Vessel purchase/lease (ships cost $50-200M each)
        - Crew salaries (25-26 crew per vessel)
        - Insurance (hull, cargo, liability)
        - Administration, IT systems
        - Typically 60-70% of total costs
        
        **Variable Costs:**
        - **Fuel** (largest variable, ~40-50% of voyage costs)
        - Port charges and handling
        - Canal fees (Suez: ~$500k, Panama: ~$450k per transit)
        - Maintenance and repairs
        - Typically 30-40% of total costs
        
        **Critical Implication:**
        - Empty sailing still costs ~70% of full sailing
        - Strong pressure to fill vessels even at low rates
        - **Must maintain high utilisation** (85%+ load factor ideal)
        - Rate wars during overcapacity periods
        """)
    
    with col2:
        st.markdown("""
        **Port Terminal Economics:**
        
        **High Fixed Costs:**
        - Infrastructure (berths, cranes, yard) - billions in capital
        - Land acquisition and reclamation
        - IT systems (TOS, PORTNET, automation)
        - Administration and management
        - Typically 70-80% of total costs
        
        **Variable Costs:**
        - Labour (operators, drivers, planners)
        - Equipment maintenance
        - Utilities (electricity for cranes, reefers)
        - Typically 20-30% of total costs
        
        **Critical Implication:**
        - **Marginal cost** of handling one more container is low
        - Can offer competitive pricing when utilisation is good
        - **Must attract and retain high volumes**
        - Investments are long-term (20-30 year payback)
        """)
    
    st.markdown("""
    **The Virtuous/Vicious Cycle:**
    
    **Virtuous Cycle (Successful Hub Ports like Singapore):**
    1. High throughput → Low cost per TEU
    2. Low cost → Competitive pricing
    3. Competitive pricing → Attracts more shipping lines
    4. More lines → Better connectivity (more destinations)
    5. Better connectivity → Attracts more cargo
    6. More cargo → Higher throughput *(cycle repeats, strengthening)*
    
    **Vicious Cycle (Struggling Ports):**
    1. Low throughput → High cost per TEU
    2. High cost → Uncompetitive pricing
    3. Uncompetitive pricing → Shipping lines avoid port
    4. Fewer lines → Poor connectivity
    5. Poor connectivity → Less cargo attracted
    6. Less cargo → Lower throughput *(cycle repeats, weakening)*
    
    **Strategic Implication:** Ports must maintain and grow volumes to stay competitive. This drives massive 
    infrastructure investments like Singapore's Tuas Mega Port (65M TEU capacity, $20B investment). 
    **First-mover advantage and scale advantages create powerful competitive moats.**
    """)
    
    # ============================================================================
    # SECTION 5: Current Industry Challenges & Future Outlook
    # ============================================================================
    
    st.markdown('<p class="section-header">Current Industry Challenges (2024-2025)</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Operational Challenges:**
        
        **Overcapacity Concerns:**
        - **478 new container ships** delivered in 2024
        - Fleet growth (8-10%) exceeding trade growth (2.4-3%)
        - Supply-demand imbalance widening
        - Pressure on freight rates
        
        **Geopolitical Disruptions:**
        - Red Sea/Suez tensions (70% reduction in transits)
        - Panama Canal drought restrictions
        - Longer voyage distances = more vessel requirements
        - Supply chain unpredictability
        
        **Port Congestion (2023-2024):**
        - Singapore waiting times nearly doubled
        - Vessels rerouted due to Suez disruptions
        - Container ship port calls hit record levels
        """)
    
    with col2:
        st.markdown("""
        **Decarbonisation Pressure:**
        
        **Regulatory Requirements:**
        - IMO 2030/2050 emissions targets
        - EU Emissions Trading System (ETS) applied to shipping
        - Carbon Intensity Indicator (CII) ratings
        - EEXI (Energy Efficiency Existing Ship Index)
        
        **Alternative Fuels:**
        - **50%** of orderbook designed for alternative fuels
        - **LNG**: 36.1% of alt-fuel capable orderbook
        - **Methanol**: 9.3% (up from 4% in 2023)
        - **Ammonia**: First orders placed in 2023
        - Wind-assisted propulsion gaining interest
        
        **Fleet Renewal:**
        - Average fleet age: 12.5 years (by deadweight)
        - Over 50% of fleet >15 years old
        - Low demolition rates delaying renewal
        - Need to accelerate scrapping of old tonnage
        """)
    
    st.markdown("""
    **Technology & Digitisation:**
    - **AI-powered port operations**: Reducing waiting times, optimising berth allocation
    - **Blockchain**: Improving cargo tracking and documentation
    - **Automation**: Asia leading in automated terminals (63% of global port calls)
    - **IoT sensors**: Real-time container tracking and reefer monitoring
    - **Predictive maintenance**: Reducing vessel downtime
    """)
    
    # ============================================================================
    # SECTION 6: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Why Maritime Matters:**
        - **80%** of global trade by volume travels by sea (12.3 billion tonnes in 2023)
        - Most cost-effective transport for bulk goods
        - Enables globalisation and international commerce
        - 109,000 merchant vessels, 30M+ TEU container capacity
        
        **Container Revolution (1956):**
        - Malcolm McLean's standardised container
        - Ideal-X: First container ship, 500 TEU
        - Eliminated handling of individual items
        - Enabled intermodal transport (ship-truck-train)
        - Created globally interoperable system
        - Transformed world trade economics
        """)
    
    with col2:
        st.markdown("""
        **Three Waves of Change:**
        - **Wave 1**: Mega vessels (500 TEU → 25,000 TEU, 50x growth)
        - **Wave 2**: Mega alliances (3 alliances control 83%)
        - **Wave 3**: Cargo changes (geopolitics, supply chain shifts)
        
        **Maritime Economics:**
        - High fixed costs → Need high utilisation (vessels and ports)
        - Virtuous vs vicious cycles determine port competitiveness
        - Scale advantages create powerful competitive moats
        - Strategic infrastructure investments essential (e.g., Tuas $20B)
        
        **Current Challenges:**
        - Overcapacity (fleet growth exceeds trade growth)
        - Geopolitical disruptions (Suez -70%, longer routes)
        - Decarbonisation pressure (50% of orderbook alternative fuel)
        - Technology transformation (automation, AI, blockchain)
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Maritime shipping is the invisible backbone of global commerce, moving 
    80% of trade by volume. The 1956 container revolution created a standardised, interoperable global system 
    that enabled modern globalisation. Today, the industry faces three simultaneous transformations: 
    **mega vessels** (driven by economies of scale, now reaching 24,000+ TEU), **mega alliances** 
    (consolidation to 3 alliances controlling 83% of capacity), and **cargo changes** (geopolitical tensions, 
    supply chain reconfiguration, China+1 diversification). The industry also grapples with overcapacity 
    (fleet growing faster than trade), geopolitical disruptions (Suez -70%, longer routes), and urgent 
    decarbonisation requirements (50% of new orders alternative-fuel capable). Understanding these fundamentals 
    is essential for grasping why ports like Singapore invest $20 billion in Tuas and how these complex 
    operations work in an increasingly challenging environment.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** 📦 Containers & Containerisation - Dive deep into container standards, types, 
    measurements, TEU calculations, and the physical specifications that make global shipping possible.
    """)
