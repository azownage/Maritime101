import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

def show():
    st.markdown('<p class="main-header">🌍 Global Shipping & Alliances</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand how shipping lines have consolidated into powerful alliances, the network structures that 
    connect global trade, and the strategic implications for ports and shippers.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Industry Consolidation Overview
    # ============================================================================
    
    st.markdown('<p class="section-header">The Great Consolidation: From 15 to 9</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The container shipping industry has undergone massive consolidation over the past three decades. 
    What was once a fragmented industry with 15+ major independent carriers has become an oligopoly 
    dominated by 9 major players organized into 3 powerful alliances.
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Major Players (1990s)", "15+", help="Highly fragmented market")
    with col2:
        st.metric("Major Players (2025)", "9", help="Consolidated into 3 alliances")
    with col3:
        st.metric("Alliance Market Control", "83%", help="3 alliances control 83% of global volumes")
    
    # Timeline of consolidation
    consolidation_timeline = pd.DataFrame({
        'Period': ['1990s', '2000s', '2015', '2017', '2020', '2025'],
        'Alliance Control %': [0, 30, 75, 80, 82, 83],
        'Major Players': [15, 12, 10, 9, 9, 9],
        'Key Events': [
            'Independent carriers dominate',
            'First alliance formations begin',
            'Major consolidation wave',
            'Modern "Big 3" alliances formed',
            'COVID-19 accelerates consolidation',
            'Current mature alliance structure'
        ]
    })
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=consolidation_timeline['Period'],
        y=consolidation_timeline['Alliance Control %'],
        mode='lines+markers',
        name='Alliance Market Control',
        line=dict(color='#3B82F6', width=4),
        marker=dict(size=14, color='#2563EB', line=dict(color='white', width=2)),
        yaxis='y1',
        text=[f"{val}%" for val in consolidation_timeline['Alliance Control %']],
        textposition='top center'
    ))
    
    fig.add_trace(go.Scatter(
        x=consolidation_timeline['Period'],
        y=consolidation_timeline['Major Players'],
        mode='lines+markers',
        name='Number of Major Players',
        line=dict(color='#EF4444', width=4, dash='dash'),
        marker=dict(size=14, color='#DC2626', line=dict(color='white', width=2)),
        yaxis='y2',
        text=consolidation_timeline['Major Players'],
        textposition='bottom center'
    ))
    
    fig.update_layout(
        title={
            'text': 'Shipping Industry Consolidation: 0% → 83% Alliance Control',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#1F2937'}
        },
        xaxis_title="Time Period",
        yaxis=dict(
            title="Alliance Market Control (%)",
            titlefont=dict(color='#3B82F6'),
            tickfont=dict(color='#3B82F6'),
            gridcolor='#E5E7EB',
            range=[0, 100]
        ),
        yaxis2=dict(
            title="Number of Major Players",
            titlefont=dict(color='#EF4444'),
            tickfont=dict(color='#EF4444'),
            overlaying='y',
            side='right',
            range=[0, 20]
        ),
        height=500,
        plot_bgcolor='white',
        hovermode='x unified',
        legend=dict(x=0.01, y=0.99, bgcolor='rgba(255,255,255,0.8)')
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ Strategic Implication:</strong> With 83% of global container volumes controlled by just 
    3 alliances, the bargaining power has shifted dramatically from ports to carriers. Losing one alliance 
    partnership can mean losing 25-30% of a port's throughput overnight. This is why ports like Singapore 
    invest billions to remain attractive to these mega alliances.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 2: The Big Three Alliances
    # ============================================================================
    
    st.markdown('<p class="section-header">The "Big Three" Alliances (2025)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    As of 2025, three major alliances dominate global container shipping. Each alliance is a partnership 
    where member lines share vessels, coordinate schedules, and optimize routes while maintaining separate 
    commercial operations.
    """)
    
    # Alliance market share
    alliance_data = pd.DataFrame({
        'Alliance': ['2M Alliance', 'Ocean Alliance', 'THE Alliance', 'Others'],
        'Market Share %': [34, 30, 19, 17],
        'Color': ['#3B82F6', '#10B981', '#F59E0B', '#94A3B8']
    })
    
    fig = go.Figure(data=[go.Pie(
        labels=alliance_data['Alliance'],
        values=alliance_data['Market Share %'],
        marker=dict(colors=alliance_data['Color'], line=dict(color='white', width=2)),
        textinfo='label+percent',
        textfont=dict(size=14, color='white'),
        hole=0.4
    )])
    
    fig.update_layout(
        title={
            'text': 'Global Container Shipping Market Share (2025)',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#1F2937'}
        },
        annotations=[dict(text='83%<br>Alliance<br>Control', x=0.5, y=0.5, font_size=16, showarrow=False)],
        height=450
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # ============================================================================
    st.markdown('<p class="subsection-header">1. 2M Alliance (34% Market Share)</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        **Members:**
        - 🇨🇭 **MSC** (Mediterranean Shipping Company)
        - 🇩🇰 **Maersk** (A.P. Moller-Maersk)
        
        **Formation:** 2015
        
        **Fleet Size:** ~700 vessels
        """)
    
    with col2:
        st.markdown("""
        **Key Characteristics:**
        - Largest alliance by market share (34%)
        - MSC is world's #1 carrier by capacity
        - Maersk is historically most prestigious liner
        - Strong presence on all major trade lanes
        - Known for operational reliability
        
        **Strategic Focus:**
        - Trans-Pacific routes (Asia ↔ North America)
        - Trans-Atlantic routes (Europe ↔ North America)
        - Asia-Europe routes
        - Premium service quality positioning
        """)
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 Industry Leadership:</strong> The 2M alliance combines MSC's massive capacity (world's 
    largest carrier) with Maersk's century-old reputation for reliability and innovation. Together they 
    set industry standards for service levels and operational excellence.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    st.markdown('<p class="subsection-header">2. Ocean Alliance (30% Market Share)</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        **Members:**
        - 🇫🇷 **CMA CGM** (France)
        - 🇨🇳 **COSCO Shipping** (China)
        - 🇭🇰 **OOCL** (Orient Overseas Container Line)
        - 🇹🇼 **Evergreen** (Taiwan)
        
        **Formation:** 2017
        
        **Fleet Size:** ~650 vessels
        """)
    
    with col2:
        st.markdown("""
        **Key Characteristics:**
        - Second-largest alliance (30%)
        - Most diverse membership (4 major carriers)
        - Strong Asian presence (COSCO, OOCL, Evergreen)
        - CMA CGM brings European expertise
        - Extensive network coverage
        
        **Strategic Focus:**
        - Asia-Europe routes (core strength)
        - Intra-Asia connectivity
        - Trans-Pacific routes
        - Mediterranean services
        - Innovation in digitalization and sustainability
        """)
    
    st.markdown("""
    <div class="info-box">
    <strong>📊 Geographic Strength:</strong> Ocean Alliance has particularly strong coverage of Asia-Europe 
    routes and intra-Asian trades, leveraging COSCO's dominance in China, OOCL's Hong Kong hub, and 
    Evergreen's Taiwan base, complemented by CMA CGM's European network.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    st.markdown('<p class="subsection-header">3. THE Alliance (19% Market Share)</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        **Members:**
        - 🇯🇵 **ONE** (Ocean Network Express)
          - Merger of NYK Line, MOL, "K" Line
        - 🇰🇷 **HMM** (Hyundai Merchant Marine)
        - 🇹🇼 **Yang Ming**
        
        **Formation:** 2017
        
        **Fleet Size:** ~350 vessels
        """)
    
    with col2:
        st.markdown("""
        **Key Characteristics:**
        - Smallest of the "Big Three" (19%)
        - Strong Japanese and Korean presence
        - ONE represents consolidation of 3 Japanese carriers
        - Focuses on operational efficiency
        - Significant ULCV deployment
        
        **Strategic Focus:**
        - Trans-Pacific routes (Asia ↔ North America)
        - Asia-Europe routes
        - Intra-Asia services
        - Known for mega-vessel deployment
        - Strong service reliability metrics
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🎯 Efficiency Focus:</strong> THE Alliance may be smaller, but it's known for high operational 
    efficiency and schedule reliability. The consolidation of three Japanese carriers into ONE created 
    significant synergies and economies of scale.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 3: Why Alliances Exist
    # ============================================================================
    
    st.markdown('<p class="section-header">Why Do Shipping Alliances Exist?</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Shipping alliances are **vessel-sharing agreements (VSAs)** that allow carriers to cooperate on 
    operations while competing commercially. Understanding why they formed is key to understanding modern 
    maritime economics.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Benefits of Alliance Membership:**
        
        **1. Network Coverage**
        - Access to more ports without owning more ships
        - Fill gaps in geographic coverage
        - Offer customers more routing options
        
        **2. Vessel Utilization**
        - Share vessel capacity on routes
        - Reduce number of vessels needed
        - Higher load factors (fuller ships)
        
        **3. Frequency & Reliability**
        - More frequent departures
        - Better schedule reliability
        - Backup options if one vessel has issues
        
        **4. Economies of Scale**
        - Share fixed costs (terminal leases, IT systems)
        - Joint procurement of fuel, equipment
        - Negotiate better rates with ports
        """)
    
    with col2:
        st.markdown("""
        **Example: How It Works**
        
        **Without Alliance:**
        - Carrier A operates Asia-Europe route
        - Deploys 10 vessels
        - Weekly service
        - 70% average load factor
        - High fixed costs per vessel
        
        **With Alliance (A + B + C):**
        - Three carriers share route
        - Deploy 12 vessels total (4 each)
        - Three weekly departures
        - 90% average load factor
        - Share terminal costs
        - Each carrier offers customers 3x frequency
        
        **Result:**
        - 30% fewer vessels needed per carrier
        - Higher utilization rates
        - Better service for customers
        - Lower cost per TEU
        """)
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 Key Point:</strong> Alliances allow carriers to offer global coverage and high frequency 
    without the massive capital investment of operating alone. A customer can book with Maersk but their 
    container might travel on an MSC vessel as part of the 2M alliance cooperation.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **What Alliances Share vs Don't Share:**
    
    **✅ What They SHARE:**
    - Vessel capacity (slot sharing)
    - Route networks and schedules
    - Terminal facilities at some ports
    - Operational planning and coordination
    - Some IT systems and infrastructure
    
    **❌ What They DON'T Share:**
    - Pricing and commercial terms (independent)
    - Customer relationships (compete for cargo)
    - Revenue (each keeps their own)
    - Marketing and branding (separate)
    - Equipment pools (containers, chassis)
    """)
    
    # ============================================================================
    # SECTION 4: Hub-and-Spoke vs Point-to-Point
    # ============================================================================
    
    st.markdown('<p class="section-header">Network Structures: Hub-and-Spoke vs Direct Calling</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Shipping lines organize their networks in different ways depending on trade volumes and economics.
    """)
    
    st.markdown('<p class="subsection-header">Hub-and-Spoke Model</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **How It Works:**
    - Large "mainline" vessels (ULCV, VLCS) call only at major hub ports
    - Smaller "feeder" vessels distribute cargo to/from smaller regional ports
    - Hub port acts as transshipment center
    
    **Example: Singapore as Hub**
    - ULCV from Shanghai → Singapore → Rotterdam (Europe)
    - Feeder vessels connect Singapore to Jakarta, Manila, Yangon, etc.
    - Cargo from Manila bound for Europe goes: Manila → Singapore (feeder) → Rotterdam (mainline)
    
    **Advantages:**
    - Mega vessels achieve economies of scale on main routes
    - Can serve many ports without mega vessel calls
    - More flexible network (add/drop feeder routes easily)
    - Hub port concentrates volumes
    
    **Disadvantages:**
    - Extra handling (transshipment costs)
    - Longer transit time (two vessels instead of one)
    - Dependence on hub port performance
    - Container must be handled 2-4 times (origin, hub, destination)
    """)
    
    st.markdown('<p class="subsection-header">Point-to-Point (Direct Calling)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **How It Works:**
    - Vessels call directly at origin and destination ports
    - No intermediate transshipment
    - Typical for high-volume trade lanes
    
    **Example: Shanghai → Los Angeles**
    - Direct vessel service from Chinese port to US West Coast
    - No transshipment required
    - Container handled only twice (load in China, discharge in US)
    
    **Advantages:**
    - Faster transit times
    - Lower handling costs (no transshipment)
    - Less risk of damage or delay
    - Simpler logistics
    
    **Disadvantages:**
    - Requires sufficient cargo volume to fill large vessels
    - Limited to major port pairs
    - Less network flexibility
    - May not be economical for smaller markets
    """)
    
    st.markdown("""
    **Reality: Hybrid Approach**
    
    Most alliances use a **combination** of both models:
    - **Point-to-point** on high-volume lanes (Asia-US West Coast, Asia-Europe main ports)
    - **Hub-and-spoke** for secondary markets and regional distribution
    - Flexibility to adjust based on seasonal demand
    
    **Singapore's Role:**
    Singapore is the world's premier **transshipment hub**—approximately 85% of containers handled 
    at Singapore are transshipments (not origin/destination cargo). This makes Singapore a critical 
    node in the global hub-and-spoke network.
    """)
    
    # ============================================================================
    # SECTION 5: Inter-Connected Port Networks
    # ============================================================================
    
    st.markdown('<p class="section-header">Inter-Connected Port Networks</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The modern shipping industry has evolved from competing individual "hub ports" to an 
    **inter-connected network** where multiple ports work together.
    """)
    
    st.markdown('<p class="subsection-header">Big Hub Port vs Vital Network Node</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Traditional View: "Biggest Hub Wins"**
        - Size matters most
        - Winner-takes-all competition
        - Attract maximum vessel calls
        - Highest TEU throughput = success
        
        **Limitations:**
        - Focuses only on scale
        - Ignores connectivity quality
        - Can't capture network effects
        - Vulnerable to concentrated risk
        """)
    
    with col2:
        st.markdown("""
        **Modern View: "Vital Network Node"**
        - Connectivity matters most
        - Multiple complementary ports
        - Strategic position in network
        - Value = centrality + reliability + efficiency
        
        **Advantages:**
        - More resilient network
        - Optimized for different cargo types
        - Redundancy and flexibility
        - Better serves diverse shipping patterns
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🎯 Singapore's Strategy:</strong> Singapore positions itself as a **vital node** in the 
    inter-connected port network, not just the "biggest hub." This means:
    - Unmatched connectivity (200+ shipping lines, 600+ ports)
    - Reliability (BOA >90%, minimal disruptions)
    - Efficiency (fast turnaround times)
    - Strategic location on main Asia-Europe route
    
    Being a vital, reliable node can be more valuable than being the absolute largest port.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 6: Major Trade Routes
    # ============================================================================
    
    st.markdown('<p class="section-header">Major Global Trade Routes</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Container shipping flows along several major "trade lanes" connecting economic centers.
    """)
    
    # Trade lane data
    trade_lanes = pd.DataFrame({
        'Trade Lane': [
            'Asia - North Europe',
            'Asia - Mediterranean',
            'Trans-Pacific (Asia - US West Coast)',
            'Trans-Pacific (Asia - US East Coast)',
            'Trans-Atlantic (Europe - North America)',
            'Intra-Asia',
            'Asia - Middle East',
            'Europe - South America'
        ],
        'Annual Volume (Million TEU)': [24, 8, 16, 10, 7, 35, 6, 3],
        'Typical Transit Time (Days)': [30, 25, 14, 30, 10, 7, 18, 20],
        'Key Characteristics': [
            'Largest East-West trade lane, dominated by ULCV',
            'Mediterranean feeder from main Asia-Europe route',
            'High-volume consumer goods, fast transit required',
            'Via Panama Canal or Suez, longer route',
            'Lower volume, seasonal variations',
            'Highest total volume, many regional routes',
            'Energy equipment, construction materials',
            'Agricultural and industrial goods'
        ]
    })
    
    st.dataframe(trade_lanes, use_container_width=True, hide_index=True)
    
    # Trade lane volumes chart
    fig = go.Figure(data=[
        go.Bar(
            x=trade_lanes['Annual Volume (Million TEU)'],
            y=trade_lanes['Trade Lane'],
            orientation='h',
            marker=dict(
                color=trade_lanes['Annual Volume (Million TEU)'],
                colorscale='Blues',
                line=dict(color='#1F2937', width=1)
            ),
            text=trade_lanes['Annual Volume (Million TEU)'],
            textposition='outside',
            textfont=dict(size=12)
        )
    ])
    
    fig.update_layout(
        title={
            'text': 'Container Trade Lane Volumes (Million TEU/Year)',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        xaxis_title="Annual Volume (Million TEU)",
        height=450,
        plot_bgcolor='white',
        xaxis=dict(gridcolor='#E5E7EB')
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    **Key Observations:**
    
    1. **Intra-Asia is Largest:** 35 million TEU annually—more than any East-West route
       - Driven by regional supply chains
       - China-Southeast Asia trade
       - Manufacturing distribution
    
    2. **Asia-North Europe is Premier East-West Lane:** 24 million TEU
       - Longest route (30+ days)
       - Deployed the largest vessels (20,000+ TEU ULCV)
       - Highest value cargo
    
    3. **Trans-Pacific Routes:** Split between West Coast (fast, 14 days) and East Coast (slow, 30 days)
       - US West Coast: Critical for consumer electronics, time-sensitive cargo
       - US East Coast: Via Panama or Suez, serves eastern US population centers
    """)
    
    # ============================================================================
    # SECTION 7: Geopolitics and Trade Shifts
    # ============================================================================
    
    st.markdown('<p class="section-header">Geopolitics: Reshaping Trade Flows</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Recent geopolitical tensions have caused significant shifts in global trade patterns, affecting 
    container flows and port strategies.
    """)
    
    st.markdown('<p class="subsection-header">US-China Trade Tensions</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Shift (2018-2024):**
    - Direct US imports from China decreased slightly (-0.4%)
    - **BUT** total US imports increased through intermediary countries:
    
    **Intermediary Country Growth:**
    - 🇻🇳 **Vietnam:** +80% increase in exports to US (+159% imports from China)
    - 🇲🇾 **Malaysia:** +45% increase in exports to US (+38% imports from China)
    - 🇹🇭 **Thailand:** +41% increase in exports to US (+84% imports from China)
    - 🇲🇽 **Mexico:** +42% increase in exports to US (+32% imports from China)
    
    **What's Happening:**
    - Chinese manufacturing relocating to Southeast Asia
    - "China+1" diversification strategies
    - Re-export and value-added processing in intermediary countries
    - Supply chains becoming **longer and more complex**
    """)
    
    # Trade flow visualization
    trade_flow_data = pd.DataFrame({
        'Country': ['Vietnam', 'Malaysia', 'Thailand', 'Mexico', 'China (Direct)'],
        'Change in US Imports (%)': [80, 45, 41, 42, -0.4],
        'Color': ['#10B981', '#10B981', '#10B981', '#10B981', '#EF4444']
    })
    
    fig = go.Figure(data=[
        go.Bar(
            x=trade_flow_data['Country'],
            y=trade_flow_data['Change in US Imports (%)'],
            marker=dict(color=trade_flow_data['Color'], line=dict(color='#1F2937', width=2)),
            text=[f"+{val}%" if val > 0 else f"{val}%" for val in trade_flow_data['Change in US Imports (%)']],
            textposition='outside',
            textfont=dict(size=13, color='#1F2937')
        )
    ])
    
    fig.update_layout(
        title={
            'text': 'US Import Growth by Country (2018-2022)',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        yaxis_title="Change in US Imports (%)",
        height=400,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='#E5E7EB')
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ Impact on Ports:</strong> Trade diversification means:
    - **New routing patterns**: Containers now flow China → Vietnam → US instead of China → US direct
    - **More transshipment**: Increased complexity creates more hub port activity
    - **Southeast Asian ports surge**: Vietnam, Thailand, Malaysia ports see rapid growth
    - **Longer supply chains**: More vessel movements, more handling, more complexity
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">Alternative Trade Routes & Threats</p>', unsafe_allow_html=True)
    
    st.markdown("""
    New infrastructure and climate change are creating alternative routing options that could disrupt 
    traditional shipping lanes:
    
    **1. Arctic Route (Northern Sea Route)**
    - **Potential:** South Korea to Norway via Arctic (~30% shorter distance)
    - **Current Status:** Limited use, ice conditions restrict access
    - **Timeline:** Climate change may make viable by 2030s-2040s
    - **Impact:** Could bypass Suez Canal and Singapore entirely
    
    **2. Trans-Pacific Rail Corridors**
    - **Concept:** Sea transport to US/Canada West Coast → Rail to East Coast
    - **Competition:** Faster than all-water route via Panama/Suez
    - **Challenge:** Higher cost, capacity constraints
    
    **3. New Canals & Corridors**
    - **Thailand's Kra Canal:** Proposed canal across Thai isthmus (would bypass Malacca Strait)
    - **Status:** Discussed for decades, economically and politically challenging
    - **Risk to Singapore:** If built, could reduce traffic through Singapore
    
    **4. China Belt & Road Initiative**
    - Land-based rail corridors (China → Europe via Central Asia)
    - Reduce dependence on sea routes
    - Currently limited capacity but growing
    """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🎯 Singapore's Response:</strong> Singapore recognizes these potential threats and responds by:
    - Investing in Tuas Mega Port (65M TEU capacity) to lock in scale advantages
    - Improving efficiency to remain cost-competitive
    - Diversifying into adjacent services (bunkering, ship repair, maritime finance)
    - Building joint ventures with shipping lines to secure long-term commitments
    - Positioning as vital node vs just biggest hub (reliability > size)
    </strong>
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 8: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Industry Consolidation:**
        - 15+ carriers → 9 major players → 3 alliances
        - Alliances control 83% of global capacity
        - 2M (34%), Ocean Alliance (30%), THE Alliance (19%)
        
        **Why Alliances Exist:**
        - Share vessel capacity and routes
        - Achieve economies of scale
        - Offer better network coverage
        - Higher utilization and frequency
        - Compete commercially but cooperate operationally
        
        **Network Structures:**
        - Hub-and-spoke: Mega vessels + feeder distribution
        - Point-to-point: Direct services for high-volume lanes
        - Hybrid approach most common
        - Inter-connected networks > individual hub ports
        """)
    
    with col2:
        st.markdown("""
        **Major Trade Lanes:**
        - Intra-Asia: 35M TEU (largest)
        - Asia-North Europe: 24M TEU (premier East-West)
        - Trans-Pacific: 26M TEU combined
        - Singapore critical node on main routes
        
        **Geopolitical Shifts:**
        - US-China tensions driving trade diversification
        - Vietnam, Malaysia, Thailand surge
        - Supply chains becoming longer and more complex
        - More transshipment activity
        
        **Future Threats:**
        - Arctic routes (climate change)
        - Trans-Pacific rail corridors
        - Alternative canals (Kra Canal)
        - Belt & Road land routes
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> The container shipping industry has consolidated into 3 powerful 
    alliances controlling 83% of global trade. This gives alliances enormous bargaining power over ports. 
    Success for ports now depends on being a vital, reliable node in the inter-connected network—not just 
    being the biggest. Geopolitical shifts and potential new routes add complexity and uncertainty to the 
    competitive landscape.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** 🏛️ Maritime Singapore Ecosystem - Understand Singapore's unique maritime structure 
    with MPA as regulator/promoter and how the complete maritime cluster supports the port's success.
    """)
