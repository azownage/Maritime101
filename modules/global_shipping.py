import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">🌍 Global Shipping & Alliances</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand industry consolidation, the formation and power of mega shipping alliances, 
    hub-and-spoke network structures, and how geopolitics shapes global shipping patterns.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Industry Consolidation
    # ============================================================================
    
    st.markdown('<p class="section-header">Industry Consolidation: From Many to Few</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The container shipping industry has undergone dramatic consolidation over the past two decades. 
    What was once a fragmented industry with dozens of independent carriers is now dominated by 
    just three mega-alliances.
    """)
    
    st.markdown('<p class="subsection-header">The Consolidation Journey</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Year 2000", "15+ Major Carriers", help="Independent carriers competing globally")
    with col2:
        st.metric("Year 2024", "9 Major Players", help="After mergers and acquisitions")
    with col3:
        st.metric("Alliance Control", "83%", help="Three alliances control 83% of global capacity")
    
    st.markdown("""
    **Key Consolidation Events:**
    
    **1990s-2000s: Fragmented Competition**
    - 15+ major global carriers competing independently
    - Regional carriers dominating local trades
    - Minimal cooperation beyond vessel sharing
    - Price competition intense
    
    **2010s: Merger Wave Begins**
    - 2005: P&O Nedlloyd acquired by Maersk
    - 2014: Hamburg Süd acquired by Maersk (2017)
    - 2016: APL acquired by CMA CGM
    - 2016: Hanjin Shipping bankruptcy (world's 7th largest)
    - 2017: OOCL acquired by COSCO
    - 2018: Japanese carriers (NYK, MOL, K Line) merge into ONE
    
    **2020s: Alliance Dominance**
    - Three mega-alliances control 83% of global capacity
    - Only 9 major carriers remain
    - Further consolidation expected
    """)
    
    # Industry consolidation data
    consolidation_data = pd.DataFrame({
        'Year': [2000, 2005, 2010, 2015, 2017, 2020, 2024],
        'Number of Major Carriers': [17, 15, 15, 15, 12, 10, 9],
        'Top 3 Market Share (%)': [28, 32, 35, 39, 42, 48, 52],
        'Alliance Control (%)': [0, 15, 35, 60, 75, 82, 83]
    })
    
    # Create side-by-side charts
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(
            x=consolidation_data['Year'],
            y=consolidation_data['Alliance Control (%)'],
            mode='lines+markers',
            fill='tozeroy',
            line=dict(color='#3B82F6', width=3),
            marker=dict(size=10),
            name='Alliance Control'
        ))
        fig1.update_layout(
            title='Alliance Control Growth',
            xaxis_title="Year",
            yaxis_title="Alliance Control (%)",
            height=350,
            plot_bgcolor='white',
            yaxis=dict(gridcolor='#E5E7EB', range=[0, 100]),
            xaxis=dict(gridcolor='#E5E7EB')
        )
        st.plotly_chart(fig1, width='stretch')
    
    with col2:
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(
            x=consolidation_data['Year'],
            y=consolidation_data['Number of Major Carriers'],
            mode='lines+markers',
            fill='tozeroy',
            line=dict(color='#EF4444', width=3),
            marker=dict(size=10),
            name='Major Carriers'
        ))
        fig2.update_layout(
            title='Number of Major Players Declining',
            xaxis_title="Year",
            yaxis_title="Number of Major Carriers",
            height=350,
            plot_bgcolor='white',
            yaxis=dict(gridcolor='#E5E7EB', range=[0, 20]),
            xaxis=dict(gridcolor='#E5E7EB')
        )
        st.plotly_chart(fig2, width='stretch')
    
    st.markdown("""
    **Why Consolidation Happened:**
    
    **Overcapacity Crisis:**
    - Carriers ordered too many mega vessels in 2000s-2010s
    - Supply exceeded demand → Freight rates collapsed
    - Many carriers losing money (2015-2016 particularly severe)
    - Bankruptcy wave forced consolidation
    
    **Economies of Scale:**
    - Bigger carriers can negotiate better prices with ports and suppliers
    - Spread fixed costs (IT systems, management) over larger volumes
    - Larger networks attract more customers
    - Better bargaining power with ports
    
    **Survival Strategy:**
    - Small carriers couldn't compete on costs alone
    - Mergers and acquisitions provided economies of scale
    - Alliances allowed cooperation without full mergers
    - "Get big or get out" became industry mantra
    """)
    
    # ============================================================================
    # SECTION 2: The Big Three Alliances
    # ============================================================================
    
    st.markdown('<p class="section-header">The Big Three Alliances</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Today, three mega-alliances dominate global container shipping. Understanding these alliances 
    is essential to understanding modern maritime trade.
    """)
    
    # Alliance data
    alliance_data = pd.DataFrame({
        'Alliance': ['2M Alliance', 'Ocean Alliance', 'THE Alliance', 'Independent'],
        'Market Share (%)': [34, 30, 19, 17],
        'Number of Vessels': [700, 650, 350, 400],
        'Total TEU Capacity (M)': [4.2, 3.7, 2.3, 2.1],
        'Member Lines': [
            'MSC, Maersk',
            'CMA CGM, COSCO, OOCL, Evergreen',
            'ONE, HMM, Yang Ming',
            'ZIM, various regional carriers'
        ]
    })
    
    st.dataframe(alliance_data, width='stretch', hide_index=True)
    
    st.markdown('<p class="subsection-header">2M Alliance (34% Market Share)</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        **Members:**
        - MSC (Mediterranean Shipping Company)
        - Maersk Line
        
        **Formation:** 2015
        
        **Status:**
        - Largest alliance globally
        - MSC recently became #1 carrier (overtook Maersk)
        """)
    
    with col2:
        st.markdown("""
        **Characteristics:**
        - Originally defensive move by Maersk to counter Asian competition
        - MSC (Swiss/Italian) and Maersk (Danish) bring complementary strengths
        - Maersk: Brand, reliability, digital innovation
        - MSC: Aggressive growth, cost efficiency, owner-operated
        - Cover all major trade lanes globally
        - Focus on operational reliability and schedule integrity
        
        **Key Routes:**
        - Asia-Europe (via Suez Canal)
        - Trans-Pacific (Asia-North America)
        - Transatlantic (Europe-North America)
        - North-South routes (Europe/Asia to South America, Africa)
        """)
    
    st.markdown('<p class="subsection-header">Ocean Alliance (30% Market Share)</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        **Members:**
        - CMA CGM (France)
        - COSCO Shipping (China)
        - OOCL (Hong Kong/China)
        - Evergreen (Taiwan)
        
        **Formation:** 2017
        
        **Status:**
        - Second-largest alliance
        - Strong Asian presence
        """)
    
    with col2:
        st.markdown("""
        **Characteristics:**
        - Replaced the CKYHE Alliance and G6 Alliance
        - Combines French, Chinese, and Taiwanese carriers
        - COSCO brings Chinese government backing and domestic market access
        - CMA CGM brings global reach and European strength
        - Evergreen provides Taiwan Strait and intra-Asia expertise
        - OOCL adds Hong Kong hub connectivity
        
        **Key Routes:**
        - Asia-Europe (multiple services)
        - Trans-Pacific (comprehensive coverage)
        - Asia-Middle East-Europe via Suez
        - Strong intra-Asia services
        """)
    
    st.markdown('<p class="subsection-header">THE Alliance (19% Market Share)</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        **Members:**
        - ONE (Ocean Network Express - Japan)
        - HMM (Hyundai Merchant Marine - Korea)
        - Yang Ming (Taiwan)
        
        **Formation:** 2017
        
        **Status:**
        - Smallest of big three
        - Northeast Asian focus
        """)
    
    with col2:
        st.markdown("""
        **Characteristics:**
        - ONE formed from merger of three Japanese carriers (NYK, MOL, K Line)
        - Represents Northeast Asian carriers (Japan, Korea, Taiwan)
        - Strong trans-Pacific focus (Asia-US routes)
        - Smaller scale than 2M and Ocean Alliance
        - Focus on service reliability and quality over volume
        
        **Key Routes:**
        - Trans-Pacific (strong US West Coast coverage)
        - Asia-Europe via Suez Canal
        - Intra-Asia feeder services
        - Asia-Middle East services
        
        **Note:** "THE" stands for "The, Hyundai, Evergreen" but Evergreen left for Ocean Alliance
        """)
    
    # Alliance market share visualization
    fig = go.Figure(data=[go.Pie(
        labels=alliance_data['Alliance'],
        values=alliance_data['Market Share (%)'],
        marker=dict(colors=['#3B82F6', '#10B981', '#F59E0B', '#94A3B8']),
        textinfo='label+percent',
        textfont=dict(size=14, color='white'),
        hole=0.4
    )])
    
    fig.update_layout(
        title={
            'text': 'Global Container Shipping Market Share by Alliance (2024)',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        annotations=[dict(text='Total<br>Market', x=0.5, y=0.5, font_size=16, showarrow=False)],
        height=450
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ Alliance Power:</strong> The Big Three alliances control pricing and capacity:<br>
    - <strong>Market power</strong>: 83% control means significant pricing influence<br>
    - <strong>Barriers to entry</strong>: Extremely difficult for new carriers to compete<br>
    - <strong>Port leverage</strong>: Alliances negotiate favourable terms with ports<br>
    - <strong>Regulatory scrutiny</strong>: Competition authorities monitor for anti-competitive behaviour<br>
    - <strong>Customer concern</strong>: Shippers worry about reduced competition and higher prices
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 3: How Alliances Work
    # ============================================================================
    
    st.markdown('<p class="section-header">How Shipping Alliances Work</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Alliances are operational partnerships, not mergers. Understanding what they share (and don't share) 
    is crucial to understanding modern maritime operations.
    """)
    
    st.markdown('<p class="subsection-header">What Alliances Share</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Shared Resources:**
        
        **Vessel Space:**
        - Members contribute vessels to joint services
        - Share capacity on each other's vessels
        - Coordinate vessel deployments
        - Optimise utilisation across fleet
        
        **Port Calls:**
        - Coordinate port rotations
        - Share terminal facilities
        - Joint negotiations with ports
        - Optimise port call sequences
        
        **Operations:**
        - Shared vessel schedules
        - Coordinated sailing frequencies
        - Joint service planning
        - Network optimisation
        """)
    
    with col2:
        st.markdown("""
        **Retained Independence:**
        
        **Pricing:**
        - Each carrier sets own freight rates
        - No price fixing (illegal)
        - Independent contract negotiations with customers
        - Compete on price within alliance
        
        **Sales and Marketing:**
        - Own sales forces
        - Independent customer relationships
        - Separate brand identities
        - Compete for same customers
        
        **Other Services:**
        - Separate logistics operations
        - Independent digital platforms
        - Own feeder networks
        - Individual competitive strategies
        """)
    
    st.markdown("""
    **The Alliance Paradox:**
    
    Alliance members **cooperate** on vessel operations and network planning while **competing** on 
    pricing and customer acquisition. This allows them to:
    - Achieve economies of scale (shared vessels, better port terms)
    - Maintain competitive market dynamics (independent pricing)
    - Offer comprehensive global networks (coordinated services)
    - Preserve individual brands and customer relationships
    
    **Regulatory Balance:**
    - Competition authorities allow operational cooperation
    - But closely monitor for price-fixing or anti-competitive behaviour
    - Alliances must demonstrate customer benefits (better service, lower costs)
    """)
    
    st.markdown('<p class="subsection-header">Why Alliances Exist</p>', unsafe_allow_html=True)
    
    # Benefits data
    alliance_benefits = pd.DataFrame({
        'Benefit': [
            'Network Coverage',
            'Vessel Utilisation',
            'Frequency and Reliability',
            'Economies of Scale',
            'Risk Sharing',
            'Port Negotiations'
        ],
        'Without Alliance': [
            'Limited geographic reach, gaps in coverage',
            '70-75% average (excess capacity wasted)',
            'Weekly service requires many vessels alone',
            'Small scale, higher unit costs',
            'Bear all demand fluctuations alone',
            'Weak negotiating position with ports'
        ],
        'With Alliance': [
            'Global coverage through partner networks',
            '85-90% average (shared capacity optimised)',
            'Multiple sailings per week via partners',
            'Large combined scale, lower unit costs',
            'Share capacity in peaks/troughs',
            'Strong collective bargaining power'
        ]
    })
    
    st.dataframe(alliance_benefits, width='stretch', hide_index=True)
    
    # ============================================================================
    # SECTION 4: Hub-and-Spoke Networks
    # ============================================================================
    
    st.markdown('<p class="section-header">Hub-and-Spoke Network Structure</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Modern container shipping operates primarily on a **hub-and-spoke** model, with major transshipment 
    hubs connecting mainline and feeder services.
    """)
    
    st.markdown('<p class="subsection-header">Hub-and-Spoke vs Point-to-Point</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Point-to-Point Model:**
        
        **Concept:**
        - Direct service between origin and destination
        - No intermediate transshipment
        - Container loaded at origin, discharged at final destination
        
        **Example:**
        - Shanghai → Los Angeles (direct)
        - Rotterdam → New York (direct)
        
        **Advantages:**
        - Faster transit (no transshipment delay)
        - Lower risk of damage/loss
        - Simpler operations
        
        **Disadvantages:**
        - Requires sufficient cargo volume on specific route
        - Less frequent services (not enough demand for daily)
        - Limited network reach
        - Higher cost per TEU (smaller vessels or lower utilisation)
        
        **Used For:**
        - Very high-volume routes (Asia-US West Coast)
        - Major trade lanes with consistent demand
        """)
    
    with col2:
        st.markdown("""
        **Hub-and-Spoke Model:**
        
        **Concept:**
        - Mainline vessels connect major hubs
        - Feeder vessels connect hubs to smaller ports
        - Containers transship at hubs
        
        **Example:**
        - Singapore Hub: Receives cargo from Malaysia, Indonesia, Thailand via feeders
        - Mainline vessel carries to Europe
        - European hub (Rotterdam) distributes via feeders
        
        **Advantages:**
        - Covers more destinations with fewer vessels
        - Higher frequency on mainline routes (consolidate cargo)
        - Better vessel utilisation (larger ships on main routes)
        - Economic viability for smaller ports
        
        **Disadvantages:**
        - Longer total transit time (transshipment delay)
        - Higher risk of damage/loss (multiple handlings)
        - Complex operations and coordination
        
        **Used For:**
        - Global network coverage
        - Serving smaller ports economically
        - 85% of global container traffic
        """)
    
    st.markdown('<p class="subsection-header">Singapore as Global Transshipment Hub</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore is the world's premier example of a pure transshipment hub. Understanding Singapore's role 
    illustrates the hub-and-spoke model.
    
    **Singapore's Hub Characteristics:**
    
    **Transshipment Dominance:**
    - **85% transshipment cargo**: Only 15% originates/terminates in Singapore
    - Container arrives from feeder → Transfers to different vessel → Departs to another destination
    - Unlike gateway ports (Los Angeles, Hamburg) where most cargo is local
    
    **Strategic Location:**
    - On main Asia-Europe shipping lane (33% of global trade)
    - Centre of Southeast Asia (ideal for regional distribution)
    - Malacca Strait chokepoint
    - Equidistant from major Asian economies
    
    **Connectivity:**
    - 200+ shipping lines call at Singapore
    - 600+ ports connected globally
    - Multiple sailings per day to/from major hubs
    - Unmatched global reach
    
    **Operational Excellence:**
    - BOA (Berth on Arrival) >90%
    - 24-36 hour vessel turnaround for mega vessels
    - Highly efficient operations minimise transshipment delay
    - Reliable, predictable service
    
    **Business Model:**
    - Competes on efficiency, reliability, connectivity
    - Not origin/destination for cargo (no local market)
    - Success depends on maintaining hub status (vulnerable to competition)
    - Massive investment in infrastructure (Tuas) to lock in position
    """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🎯 The Hub Strategy:</strong><br>
    Singapore is a <strong>"big hub"</strong> but increasingly positions itself as a <strong>"vital node in 
    an interconnected network"</strong>:<br><br>
    
    - <strong>Big Hub Mentality</strong>: Compete on volume, be the largest, winner-takes-all<br>
    - <strong>Vital Node Mentality</strong>: Be the most reliable, most connected, most efficient link in 
    global network<br><br>
    
    This shift recognises that being <strong>indispensable</strong> (due to reliability and connectivity) 
    is more valuable than simply being biggest. Multiple hubs can coexist if they each provide unique value.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 5: Major Trade Routes
    # ============================================================================
    
    st.markdown('<p class="section-header">Major Global Container Trade Routes</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Global container trade flows along established routes connecting major economic regions.
    """)
    
    # Trade routes data
    trade_routes = pd.DataFrame({
        'Trade Lane': [
            'Intra-Asia',
            'Asia-North Europe',
            'Trans-Pacific Eastbound',
            'Trans-Pacific Westbound',
            'Europe-North America',
            'Asia-Mediterranean',
            'Asia-Middle East',
            'North-South (Various)'
        ],
        'Annual Volume (M TEU)': [35, 24, 15, 11, 8, 7, 6, 15],
        'Typical Transit Time': [
            '1-7 days',
            '30-35 days',
            '14-18 days',
            '18-22 days',
            '7-12 days',
            '25-30 days',
            '12-18 days',
            '15-35 days'
        ],
        'Key Hubs': [
            'Singapore, Hong Kong, Shanghai, Busan',
            'Singapore, Colombo, Rotterdam, Hamburg',
            'Shanghai, Busan, Los Angeles, Long Beach',
            'Los Angeles, Shanghai, Ningbo',
            'Rotterdam, New York, Norfolk',
            'Singapore, Suez, Piraeus, Algeciras',
            'Singapore, Jebel Ali, Salalah',
            'Various regional hubs'
        ],
        'Characteristics': [
            'Highest volume, short distances, frequent services',
            'Longest route, mega vessels, via Suez Canal',
            'High-value cargo, time-sensitive, US imports',
            'Empty containers + some exports, lower freight rates',
            'Mature trade, balanced flows',
            'Growing route, connects to Southern Europe',
            'Oil/gas economies, infrastructure growth',
            'Diverse: Europe-Africa, Asia-Oceania, etc.'
        ]
    })
    
    st.dataframe(trade_routes, width='stretch', hide_index=True)
    
    # Trade volume visualisation
    fig = go.Figure(data=[
        go.Bar(
            x=trade_routes['Trade Lane'],
            y=trade_routes['Annual Volume (M TEU)'],
            marker=dict(color='#3B82F6'),
            text=trade_routes['Annual Volume (M TEU)'],
            textposition='outside'
        )
    ])
    
    fig.update_layout(
        title={
            'text': 'Global Container Trade Volumes by Route (2023)',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        xaxis_title="Trade Lane",
        yaxis_title="Annual Volume (Million TEU)",
        height=450,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='#E5E7EB'),
        xaxis=dict(tickangle=-45)
    )
    
    st.plotly_chart(fig, width='stretch')
    
    # ============================================================================
    # SECTION 6: Geopolitics and Trade Patterns
    # ============================================================================
    
    st.markdown('<p class="section-header">Geopolitics Reshaping Shipping Patterns</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Global trade patterns are increasingly influenced by geopolitical tensions and strategic considerations, 
    particularly US-China relations.
    """)
    
    st.markdown('<p class="subsection-header">US-China Trade Tensions</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Key Developments:**
    
    **Trade War (2018-present):**
    - Tariffs on hundreds of billions of dollars of goods
    - Supply chain disruptions
    - Companies seeking alternatives to Chinese manufacturing
    
    **Strategic Decoupling:**
    - US policy to reduce dependence on China for critical goods
    - Reshoring and nearshoring initiatives
    - "Friendshoring" to allied countries
    
    **Technology Restrictions:**
    - Export controls on semiconductors and advanced technology
    - Investment restrictions
    - Supply chain security concerns
    
    **Impact on Shipping:**
    
    **"China+1" Strategy:**
    - Companies diversifying manufacturing beyond China
    - Not abandoning China, but adding alternative locations
    - Vietnam, Malaysia, Thailand, Mexico, India gaining volume
    
    **Trade Flow Changes:**
    - Direct China-US volumes plateauing or declining slightly
    - Intermediate country trade growing (e.g., Vietnam imports Chinese components, assembles, exports to US)
    - More complex, multi-hop supply chains
    - Transshipment volumes increasing
    """)
    
    # Intermediary country growth data
    intermediary_growth = pd.DataFrame({
        'Country': ['Vietnam', 'Malaysia', 'Thailand', 'India', 'Mexico', 'Poland', 'Turkey'],
        '2018 Export Growth Index': [100, 100, 100, 100, 100, 100, 100],
        '2023 Export Growth Index': [180, 145, 141, 135, 142, 128, 130],
        'Growth (%)': ['+80%', '+45%', '+41%', '+35%', '+42%', '+28%', '+30%'],
        'Primary Beneficiary Of': [
            'China+1, low-cost manufacturing',
            'Electronics, electrical goods',
            'Automotive, electronics',
            'Pharmaceuticals, IT services',
            'Nearshoring from China to US',
            'Nearshoring from China to EU',
            'Nearshoring from China to EU'
        ]
    })
    
    st.dataframe(intermediary_growth, width='stretch', hide_index=True)
    
    st.markdown('<p class="subsection-header">Emerging Alternative Routes and Threats</p>', unsafe_allow_html=True)
    
    # Alternative routes
    alternative_routes = pd.DataFrame({
        'Alternative Route/Development': [
            'Arctic Route (Northern Sea Route)',
            'Thailand Kra Canal (proposed)',
            'Trans-Pacific Rail (China-Europe)',
            'Belt and Road Initiative (BRI)',
            'Suez Canal Expansion',
            'Panama Canal (New Locks)'
        ],
        'Status': [
            'Operational but limited',
            'Proposed (not funded)',
            'Operational',
            'Ongoing development',
            'Completed 2015',
            'Completed 2016'
        ],
        'Potential Impact': [
            'Could divert 30% of Asia-Europe traffic from Suez (if ice-free year-round)',
            'Would bypass Singapore and Malacca Strait entirely (catastrophic for Singapore if built)',
            'Competes with maritime for some China-Europe cargo (limited capacity)',
            'Creates alternative trade corridors, reduces reliance on sea routes',
            'Handles larger vessels, speeds transit',
            'Allows larger vessels on trans-Pacific route'
        ],
        'Likelihood/Timeline': [
            'Climate-dependent, 2030s-2040s possible',
            'Low likelihood, decades away if ever',
            'Niche role, limited by capacity',
            'Gradual development over decades',
            'Already implemented',
            'Already implemented'
        ],
        'Singapore Impact': [
            'Moderate threat if Arctic becomes viable',
            'Existential threat if built (bypasses entirely)',
            'Minimal (rail cannot match maritime volume)',
            'Indirect impact on trade flows',
            'Positive (more efficient Suez route)',
            'Neutral (different route)'
        ]
    })
    
    st.dataframe(alternative_routes, width='stretch', hide_index=True)
    
    # ============================================================================
    # SECTION 7: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Industry Consolidation:**
        - 15+ carriers (2000) → 9 major players (2024)
        - Three alliances control 83% of capacity
        - Overcapacity crisis forced mergers and cooperation
        - Further consolidation likely
        
        **The Big Three Alliances:**
        - **2M**: MSC + Maersk (34%)
        - **Ocean Alliance**: CMA CGM + COSCO + OOCL + Evergreen (30%)
        - **THE Alliance**: ONE + HMM + Yang Ming (19%)
        - Cooperate on operations, compete on pricing
        
        **Hub-and-Spoke:**
        - 85% of cargo transships at hubs
        - Singapore: 85% transshipment, world's premier hub
        - Mainline vessels connect hubs (mega vessels)
        - Feeder vessels connect hubs to smaller ports
        """)
    
    with col2:
        st.markdown("""
        **Major Trade Routes:**
        - Intra-Asia: Largest volume (35M TEU)
        - Asia-Europe: Longest route (24M TEU, 30-35 days)
        - Trans-Pacific: High-value cargo (26M TEU combined)
        - Various North-South routes
        
        **Geopolitics:**
        - US-China tensions reshaping trade patterns
        - "China+1" diversification (Vietnam +80%, Malaysia +45%)
        - Intermediate countries benefiting
        - Alternative routes emerging (Arctic, BRI, Kra Canal proposal)
        
        **Singapore's Challenge:**
        - Maintain position as vital hub
        - Face competition from regional ports
        - Adapt to changing trade patterns
        - Invest in infrastructure (Tuas) to stay ahead
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> The container shipping industry has consolidated dramatically, with three 
    mega-alliances (2M, Ocean Alliance, THE Alliance) now controlling 83% of global capacity. These alliances 
    cooperate on vessel operations and network planning whilst competing on pricing. Modern shipping operates 
    primarily on a hub-and-spoke model, with Singapore as the world's premier transshipment hub (85% 
    transshipment cargo, 200+ lines, 600+ ports connected). Geopolitical tensions, particularly US-China 
    relations, are reshaping trade patterns through "China+1" diversification, with Vietnam, Malaysia, and 
    other intermediate countries experiencing rapid export growth. Alternative routes (Arctic, Kra Canal, BRI) 
    pose potential long-term threats to established hubs like Singapore.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** 🇸🇬 Maritime Singapore Ecosystem - Explore Singapore's comprehensive maritime cluster, 
    MPA's dual role as regulator and developer, and the innovation ecosystem driving maritime technology forward.
    """)
