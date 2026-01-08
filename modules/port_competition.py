import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">⚓ Port Strategy & Competition</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand the critical success factors for transshipment hubs, analyse competitive dynamics in Southeast 
    Asia, explore strategic planning frameworks, and examine Singapore\'s response to regional competition 
    through infrastructure investment and operational excellence.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Critical Success Factors
    # ============================================================================
    
    st.markdown('<p class="section-header">Critical Success Factors for Transshipment Hubs</p>', unsafe_allow_html=True)
    
    st.markdown("""
    What makes a port successful as a transshipment hub? Eight critical factors determine competitive 
    position, and these factors are **not independent**—they interact and reinforce each other.
    """)
    
    st.markdown('<p class="subsection-header">The Eight Critical Factors</p>', unsafe_allow_html=True)
    
    # Critical factors detailed breakdown
    factors_data = pd.DataFrame({
        'Critical Factor': [
            '1. Strategic Location',
            '2. Efficiency & Flexibility',
            '3. Reliability',
            '4. Security & Safety',
            '5. Connectivity',
            '6. Infrastructure & Technology',
            '7. Cost vs Service Level',
            '8. Skilled Workforce & Governance'
        ],
        'Description': [
            'Proximity to major trade routes, centre of regional trade',
            'Fast vessel turnaround, high crane productivity, adaptable operations',
            'Berth on Arrival >90%, consistent service quality, minimal disruptions',
            'Low pilferage, ISPS compliance, safe working environment',
            'Number of shipping lines, ports connected, sailing frequencies',
            'Deep berths, modern equipment, adequate capacity, digital systems',
            'Competitive pricing with tight connections and quality service',
            'Experienced operators, capable management, stable supportive government'
        ],
        'Why It Matters': [
            'Minimises deviation from main shipping routes, natural stopping point',
            'Reduces vessel port time (20-30% of voyage time at port)',
            'Predictable schedules enable tight container connections',
            'Protects cargo value, ensures workforce safety, regulatory compliance',
            'More options for cargo routing, higher frequencies attract cargo',
            'Enables handling of mega vessels, supports operational efficiency',
            'Balance between competitive rates and service quality attracts customers',
            'Ensures consistent quality, long-term stability, continuous improvement'
        ],
        'Singapore Rating': [
            'Excellent',
            'Excellent',
            'Excellent',
            'Excellent',
            'Excellent',
            'Excellent',
            'Good',
            'Excellent'
        ]
    })
    
    st.dataframe(factors_data, width='stretch', hide_index=True)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ Critical Point:</strong> These factors are <strong>not independent</strong>—they interact and reinforce each other:<br>
    - <strong>Good infrastructure</strong> enables <strong>efficiency and flexibility</strong><br>
    - <strong>Efficiency</strong> attracts <strong>connectivity</strong> (more shipping lines call)<br>
    - <strong>Connectivity</strong> increases volumes, justifying <strong>infrastructure investment</strong><br>
    - <strong>Reliability</strong> builds reputation, attracting more <strong>shipping lines</strong><br>
    - <strong>Skilled workers</strong> improve <strong>efficiency, reliability, and safety</strong><br>
    - <strong>Strategic location</strong> makes all infrastructure investment worthwhile<br><br>
    
    This creates a <strong>virtuous cycle</strong> for successful ports:<br>
    Volume → Investment → Efficiency → More Volume → More Investment...<br><br>
    
    And a <strong>vicious cycle</strong> for struggling ports:<br>
    Low Volume → Underinvestment → Inefficiency → Less Volume → Further Decline...
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">Deep Dive: Key Success Factors</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Strategic Location:**
        
        **Why Location Matters:**
        - Vessels follow established trade routes
        - Deviation from route costs time and fuel
        - Ports on main routes have natural advantage
        - Centre of regional trade captures feeder traffic
        
        **Singapore's Locational Advantages:**
        - On main Asia-Europe route (33% global trade)
        - Centre of Southeast Asia
        - Malacca Strait chokepoint
        - Equidistant from major Asian economies
        - Natural hub for regional distribution
        
        **But Location Alone Isn't Enough:**
        - Hong Kong has excellent location but Singapore surpassed it
        - Other factors (efficiency, connectivity) can overcome locational disadvantage
        - Location is an advantage, not a guarantee
        
        **Efficiency & Flexibility:**
        
        **Operational Metrics:**
        - Vessel turnaround time: <24 hours for mega vessels
        - Crane productivity: 30+ moves per hour
        - Truck turnaround: <30 minutes
        - Adaptability to demand fluctuations
        
        **Why Efficiency Matters:**
        - Vessels spend 10-20% of voyage time in port
        - Every hour saved = cost savings for shipping lines
        - Faster turnaround = more voyages per year per vessel
        - Flexibility handles demand surges without delays
        
        **How Singapore Achieves Efficiency:**
        - 24/7/365 operations (no holidays)
        - Highly automated equipment
        - Experienced workforce
        - Digital systems (PORTNET, TOS)
        - Continuous process improvement
        """)
    
    with col2:
        st.markdown("""
        **Reliability:**
        
        **What Reliability Means:**
        - **Berth on Arrival (BOA)**: Vessel berths on scheduled arrival time
        - **Schedule integrity**: Vessels depart on time
        - **Consistent quality**: No surprises, predictable service
        - **Minimal disruptions**: Weather, labour, equipment
        
        **Singapore's Reliability:**
        - BOA >90% consistently
        - No labour strikes (stable industrial relations)
        - Robust equipment maintenance
        - Weather resilient (no typhoons, hurricanes)
        
        **Why Reliability Matters:**
        - Shipping lines plan tight connections
        - Container arrives on Vessel A, departs on Vessel B (same day)
        - Any delay cascades through network
        - Unreliability = lost transshipment business
        
        **Connectivity:**
        
        **Measuring Connectivity:**
        - Number of shipping lines calling
        - Number of ports connected
        - Sailing frequencies per week
        - Diversity of routes served
        
        **Singapore's Connectivity:**
        - 200+ shipping lines
        - 600+ ports in 123 countries
        - Multiple sailings daily to major hubs
        - All three mega-alliances present
        
        **Network Effects:**
        - More lines → More destinations → More cargo
        - More cargo → More lines attracted
        - Becomes self-reinforcing
        - Difficult for competitors to replicate
        """)
    
    # ============================================================================
    # SECTION 2: Port Types Classification
    # ============================================================================
    
    st.markdown('<p class="section-header">Port Types: Gateway, Transshipment, and Hybrid</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Ports serve different functions in global trade networks. Understanding these types helps explain 
    competitive dynamics and strategic positioning.
    """)
    
    # Port types detailed comparison
    port_types = pd.DataFrame({
        'Port Type': [
            'Gateway Port',
            'Transshipment Hub',
            'Hybrid Port'
        ],
        'Primary Function': [
            'Serve local hinterland (domestic economy)',
            'Connect feeder and mainline services (pure hub)',
            'Mix of gateway and transshipment'
        ],
        'Transshipment %': [
            '10-30%',
            '70-90%',
            '40-60%'
        ],
        'Key Characteristics': [
            'Large local economy, origin/destination cargo dominates, import/export focus',
            'Strategic location, pure hub function, minimal local cargo',
            'Regional economic centre with hub function, balanced mix'
        ],
        'Examples': [
            'Los Angeles, Rotterdam, Hamburg, Shanghai',
            'Singapore (85%), Colombo (95%), Salalah (100%)',
            'Hong Kong (45%), Dubai (65%), Busan (45%)'
        ],
        'Competitive Advantages': [
            'Captive local market, less dependent on transshipment',
            'Location on trade routes, efficiency focus, low costs',
            'Diversified revenue, resilient to trade pattern changes'
        ],
        'Vulnerabilities': [
            'Limited by hinterland economy size, infrastructure constraints',
            'Vulnerable to direct shipping bypassing hub, competition from other hubs',
            'May not excel at either gateway or transshipment function'
        ]
    })
    
    st.dataframe(port_types, width='stretch', hide_index=True)
    
    st.markdown("""
    **Singapore as Pure Transshipment Hub:**
    
    **The 85% Transshipment Model:**
    - Only 15% of cargo originates or terminates in Singapore
    - 85% arrives on one vessel, transfers to another, departs
    - Unlike gateway ports where most cargo is for local consumption
    
    **Advantages of Pure Hub Model:**
    - Not constrained by local economy size
    - Can grow volumes beyond domestic needs
    - Focus purely on operational excellence
    - Compete globally for transshipment traffic
    
    **Disadvantages of Pure Hub Model:**
    - No captive local market (vulnerable to competition)
    - Must maintain superiority in efficiency and connectivity
    - Shipping lines can shift to competing hubs more easily
    - Success depends entirely on competitive position
    
    **Strategic Implications:**
    - Singapore cannot afford to be complacent
    - Must continuously invest to stay ahead
    - Operational excellence is existential, not optional
    - Tuas investment critical to maintaining position
    """)
    
    # Transshipment % visualisation
    transship_data = pd.DataFrame({
        'Port': ['Salalah (Oman)', 'Colombo (Sri Lanka)', 'Singapore', 'Dubai (UAE)', 
                 'Busan (Korea)', 'Hong Kong', 'Shanghai', 'Los Angeles', 'Hamburg'],
        'Transshipment %': [100, 95, 85, 65, 45, 45, 30, 15, 20],
        'Type': ['Pure Hub', 'Pure Hub', 'Pure Hub', 'Hybrid', 'Hybrid', 'Hybrid', 'Gateway', 'Gateway', 'Gateway']
    })
    
    fig = go.Figure(data=[
        go.Bar(
            x=transship_data['Port'],
            y=transship_data['Transshipment %'],
            marker=dict(color=['#EF4444' if t == 'Pure Hub' else '#3B82F6' if t == 'Hybrid' else '#10B981' 
                               for t in transship_data['Type']]),
            text=transship_data['Transshipment %'],
            texttemplate='%{text}%',
            textposition='outside'
        )
    ])
    
    fig.update_layout(
        title={
            'text': 'Transshipment Percentage by Port Type',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        xaxis_title="Port",
        yaxis_title="Transshipment %",
        height=450,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='#E5E7EB', range=[0, 110]),
        xaxis=dict(tickangle=-45)
    ))
    
    st.plotly_chart(fig, width='stretch')
    
    # ============================================================================
    # SECTION 3: Regional Competition
    # ============================================================================
    
    st.markdown('<p class="section-header">Regional Competition in Southeast Asia</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore faces growing competition from regional ports in Malaysia, Indonesia, Thailand, and Vietnam. 
    Understanding these competitors is essential for strategic planning.
    """)
    
    st.markdown('<p class="subsection-header">Major Regional Competitors</p>', unsafe_allow_html=True)
    
    # Regional competitors detailed analysis
    competitors = pd.DataFrame({
        'Port': [
            'Singapore',
            'Port Klang (Malaysia)',
            'Tanjung Pelepas (Malaysia)',
            'Tanjung Priok (Indonesia)',
            'Laem Chabang (Thailand)',
            'Cai Mep (Vietnam)',
            'Hambantota (Sri Lanka)'
        ],
        '2023 Throughput (M TEU)': [37.3, 14.1, 12.5, 8.9, 8.1, 6.8, 1.4],
        'Transshipment %': ['85%', '65%', '85%', '25%', '30%', '40%', '90%'],
        'Key Strengths': [
            'Location, efficiency, connectivity, ecosystem, reliability',
            'Lower costs, proximity to Kuala Lumpur, growing volumes',
            'Modern facilities, Maersk dedicated terminal, competitive pricing',
            'Massive domestic market (275M people), gateway function',
            'Gateway to Thailand (70M people), lower labour costs',
            'Modern facilities, rapid growth, Vietnam economy boom',
            'Strategic location on Asia-Europe route, Chinese investment'
        ],
        'Key Weaknesses': [
            'Higher costs than neighbours, no local market',
            'Lower efficiency, less connectivity, congestion issues',
            'Limited connectivity compared to Singapore, newer port',
            'Domestic focus, lower efficiency, congestion',
            'Domestic focus, lower transshipment role',
            'Still developing connectivity, smaller scale',
            'Limited connectivity, political instability concerns'
        ],
        'Threat Level to Singapore': ['N/A', 'Moderate-High', 'Moderate-High', 'Low-Moderate', 'Low', 'Moderate', 'Low']
    })
    
    st.dataframe(competitors, width='stretch', hide_index=True)
    
    st.markdown('<p class="subsection-header">Detailed Competitor Analysis</p>', unsafe_allow_html=True)
    
    # Malaysia threats
    st.markdown("""
    **Malaysia: The Closest Threat**
    
    **Port Klang:**
    - Location: West Malaysia, near Kuala Lumpur
    - 2023 Throughput: 14.1M TEU (growing steadily)
    - Strategy: Gateway for Malaysian economy + transshipment (65%)
    - Advantages: Lower costs, proximity to domestic market
    - Challenges: Congestion, lower efficiency than Singapore
    - Assessment: Moderate-High threat (steady volume growth, cost advantage)
    
    **Tanjung Pelepas (PTP):**
    - Location: Johor, Malaysia (just across from Singapore)
    - 2023 Throughput: 12.5M TEU
    - Strategy: Pure transshipment hub (85%), Maersk dedicated terminal
    - Advantages: Modern facilities, competitive pricing, Maersk commitment
    - Challenges: Limited connectivity beyond Maersk, newer port
    - Assessment: Moderate-High threat (directly competes with Singapore on transshipment)
    
    **East Coast Rail Link (ECRL):**
    - Connects east and west coasts of Malaysia
    - Potential to divert cargo from Singapore to Malaysian east coast ports
    - Could bypass Malacca Strait entirely for some cargo
    - Still under development, impact uncertain
    
    **Melaka Gateway:**
    - Proposed mega port in Malacca
    - Chinese-backed investment
    - If built, could become major competitor
    - Currently delayed due to financing issues
    """)
    
    # Indonesia threats
    st.markdown("""
    **Indonesia: The Giant Gateway**
    
    **Tanjung Priok (Jakarta):**
    - Indonesia's largest port
    - 2023 Throughput: 8.9M TEU
    - Population: 275 million (domestic market)
    - Transshipment: Only 25% (primarily gateway)
    - Challenges: Congestion, lower efficiency, cabotage laws
    - Cabotage Laws: Require domestic cargo on Indonesian-flagged vessels (protectionism)
    
    **Why Indonesia Is Moderate Threat:**
    - Massive domestic market but primarily gateway function
    - Lower efficiency and connectivity limit transshipment appeal
    - Cabotage laws keep some cargo domestic (doesn't transship through Singapore)
    - Unlikely to become major transshipment hub (gateway focus)
    
    **But:**
    - If efficiency improves significantly, could attract more transshipment
    - Domestic market growth reduces Singapore's Indonesian feeder traffic
    - Direct shipping to Indonesia bypasses Singapore hub
    """)
    
    # Thailand and Vietnam
    st.markdown("""
    **Thailand: Laem Chabang**
    
    - Gateway to Thailand (70 million people)
    - 2023 Throughput: 8.1M TEU
    - Primarily gateway (70%), limited transshipment (30%)
    - Lower labour costs than Singapore
    
    **Isthmus of Kra Canal (Proposed):**
    - Canal across southern Thailand
    - Would bypass Malacca Strait entirely
    - Could cut 1,200 km off Asia-Europe route
    - **Existential threat to Singapore if built**
    - Likelihood: Low (massive cost, environmental concerns, decades away if ever)
    
    **Vietnam: Cai Mep**
    
    - 2023 Throughput: 6.8M TEU
    - Rapid growth (Vietnam economy booming)
    - Modern facilities, deep water
    - Transshipment: ~40% (hybrid port)
    - Growing connectivity
    - Moderate threat: Fast growth, competitive costs
    """)
    
    # Throughput comparison chart
    throughput_data = pd.DataFrame({
        'Year': [2018, 2019, 2020, 2021, 2022, 2023],
        'Singapore': [36.6, 37.2, 36.9, 37.5, 37.3, 37.3],
        'Port Klang': [12.3, 13.2, 13.2, 13.6, 14.0, 14.1],
        'Tanjung Pelepas': [9.1, 9.7, 9.6, 10.5, 11.8, 12.5],
        'Tanjung Priok': [7.6, 7.8, 7.2, 7.8, 8.4, 8.9]
    })
    
    fig = go.Figure()
    
    for port in ['Singapore', 'Port Klang', 'Tanjung Pelepas', 'Tanjung Priok']:
        fig.add_trace(go.Scatter(
            x=throughput_data['Year'],
            y=throughput_data[port],
            mode='lines+markers',
            name=port,
            line=dict(width=3),
            marker=dict(size=8)
        ))
    
    fig.update_layout(
        title={
            'text': 'Regional Port Throughput Trends (2018-2023)',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        xaxis_title="Year",
        yaxis_title="Throughput (Million TEU)",
        height=450,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='#E5E7EB'),
        xaxis=dict(gridcolor='#E5E7EB'),
        legend=dict(x=0.02, y=0.98)
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ The Overcapacity Risk:</strong> Southeast Asia faces potential <strong>port overcapacity</strong> if all 
    countries expand simultaneously:<br>
    - Malaysia: Port Klang expansion, PTP growth, Melaka Gateway (if built), ECRL<br>
    - Indonesia: Tanjung Priok expansion, new ports planned<br>
    - Thailand: Laem Chabang expansion, Kra Canal (if built)<br>
    - Vietnam: Cai Mep expansion, new deepwater ports<br><br>
    
    <strong>If overcapacity occurs:</strong><br>
    - Price wars and margin compression<br>
    - Underutilised facilities (wasted investment)<br>
    - Only the most efficient ports survive<br>
    - Consolidation of volumes to top performers<br><br>
    
    <strong>Singapore's response:</strong> Focus on <strong>efficiency, reliability, and connectivity</strong> rather than 
    competing purely on price. Build switching costs through ecosystem and lock-in strategies.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 4: Alternative Trade Routes
    # ============================================================================
    
    st.markdown('<p class="section-header">Alternative Trade Routes: Future Threats</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Beyond direct port competition, alternative trade routes could fundamentally change shipping patterns 
    and threaten Singapore's position.
    """)
    
    # Alternative routes analysis
    alternative_routes = pd.DataFrame({
        'Alternative Route': [
            'Kra Canal (Thailand)',
            'Arctic Northern Sea Route',
            'Belt and Road Initiative (BRI)',
            'Sunda/Makassar Straits',
            'Direct Shipping (bypassing hubs)',
            'Land Bridge Routes'
        ],
        'Description': [
            'Canal across southern Thailand cutting 1,200km off Asia-Europe route',
            'Ice-free Arctic route from Asia to Europe via Russia',
            'Land-based trade corridors reducing reliance on sea routes',
            'Alternative straits bypassing Malacca (longer but avoids Singapore)',
            'Vessels sailing directly to destination ports, skipping transshipment',
            'Rail/truck across land instead of sea shipping'
        ],
        'Impact if Realized': [
            'Catastrophic: Bypasses Malacca Strait and Singapore entirely',
            'Moderate-High: 30% shorter than Suez route, could divert 30% of traffic',
            'Low-Moderate: Complements sea trade, limited capacity vs maritime',
            'Low: Longer route, only attractive if Malacca unavailable',
            'Moderate: Reduces transshipment volumes, hurts hub ports',
            'Low: Limited capacity, only viable for high-value/time-sensitive'
        ],
        'Likelihood/Timeline': [
            'Low: Massive cost ($28B+), environmental concerns, political complexity, decades away if ever',
            'Moderate: Climate-dependent, viable 2-3 months/year now, could extend to 6+ months by 2040s',
            'High: Ongoing development, gradual impact over decades',
            'Low: Only used when Malacca congested or blocked',
            'Ongoing: Already happening for some routes, limited by economics',
            'Low: Cannot match maritime cost and capacity for bulk goods'
        ],
        'Singapore Impact': [
            'Existential threat if built (bypasses entirely)',
            'Moderate threat if Arctic becomes year-round viable',
            'Indirect: Changes trade flows gradually',
            'Minimal: Emergency alternative only',
            'Moderate: Reduces transshipment demand',
            'Minimal: Niche alternative'
        ]
    })
    
    st.dataframe(alternative_routes, width='stretch', hide_index=True)
    
    st.markdown("""
    **Kra Canal: The Existential Threat**
    
    **What It Is:**
    - Canal across Isthmus of Kra in southern Thailand
    - 50-100 km long, 400m wide, 25m deep (estimates vary)
    - Would connect Andaman Sea (west) to Gulf of Thailand (east)
    
    **Impact:**
    - Cuts 1,200 km off Asia-Europe route
    - Saves 2-3 days sailing time
    - Bypasses Malacca Strait entirely
    - **Singapore becomes irrelevant for Asia-Europe trade**
    
    **Why It Hasn't Been Built:**
    - **Massive cost**: $28-35 billion estimated
    - **Environmental damage**: Ecosystem destruction
    - **Political complexity**: Southern Thailand instability
    - **Engineering challenges**: Massive excavation
    - **Uncertain economics**: Would shipping lines actually use it?
    
    **Likelihood Assessment:**
    - Extremely low in next 20-30 years
    - Discussed for decades, never progressed beyond proposals
    - Thailand has other priorities (land bridge proposal instead)
    - If ever built, would be 2050+ at earliest
    
    **Singapore's Position:**
    - Monitor closely but don't panic
    - Continue building efficiency and ecosystem advantages
    - Even if built, Singapore retains intra-Asia and trans-Pacific roles
    - Diversify port value proposition (bunkering, ship repair, maritime services)
    """)
    
    # ============================================================================
    # SECTION 5: Strategic Planning Framework
    # ============================================================================
    
    st.markdown('<p class="section-header">Port Strategic Planning Framework</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Ports use strategic planning to position themselves for long-term success. Understanding this framework 
    helps appreciate Singapore's Tuas investment.
    """)
    
    st.markdown('<p class="subsection-header">Strategic Planning Process</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Strategic Plan Components:**
    
    1. **Mission and Vision Statements**
       - Mission: Why the port exists, core purpose
       - Vision: Desired future state (5-10 years)
    
    2. **Values and Behavioural Standards**
       - Safety first
       - Operational excellence
       - Environmental responsibility
       - Customer focus
    
    3. **Analysis of Business and Environmental Factors**
       - Market trends (vessel sizes, trade flows)
       - Competitive landscape
       - Technological changes
       - Regulatory environment
    
    4. **Strategic Objectives**
       - Measurable goals (throughput, efficiency, market share)
       - Financial targets (revenue, profitability)
       - Quality targets (BOA%, crane productivity)
    
    5. **Lines of Action and Forward Responsibilities**
       - Infrastructure projects (berths, cranes, automation)
       - Technology initiatives (digital systems)
       - Workforce development
       - Customer engagement
       - Sustainability initiatives
    
    **Time Frame:** Typically 5-10 years
    
    **Review Cycle:** Annual review and adjustment based on changing conditions
    """)
    
    st.markdown('<p class="subsection-header">Levels of Strategic Planning</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Multi-National Level**
        
        **Scope:**
        - Alliance of ports
        - Regional cooperation
        
        **Examples:**
        - Baltic Sea ports alliance
        - Dover/Calais coordination
        
        **Objectives:**
        - Share best practices
        - Coordinate capacity
        - Collective marketing
        - Avoid destructive competition
        """)
    
    with col2:
        st.markdown("""
        **Regional/National Level**
        
        **Scope:**
        - National government planning
        - Regional port system
        
        **Examples:**
        - Singapore national port strategy
        - China port system planning
        
        **Objectives:**
        - Optimise national capacity
        - Avoid domestic overcapacity
        - Strategic positioning
        - Economic development
        """)
    
    with col3:
        st.markdown("""
        **Individual Port/Terminal Level**
        
        **Scope:**
        - Single port or terminal
        - Operational focus
        
        **Examples:**
        - PSA terminal planning
        - Tuas Mega Port development
        
        **Objectives:**
        - Capacity expansion
        - Efficiency improvement
        - Technology adoption
        - Customer service
        """)
    
    # ============================================================================
    # SECTION 6: Singapore's Competitive Response
    # ============================================================================
    
    st.markdown('<p class="section-header">Singapore\'s Competitive Response Strategy</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Facing intensifying regional competition, Singapore has adopted a multi-pronged strategy centred on 
    massive infrastructure investment, technology leadership, and ecosystem lock-in.
    """)
    
    st.markdown('<p class="subsection-header">Tuas Mega Port: The Infrastructure Response</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Scale of Investment:**
        - **Total cost**: S$20+ billion (US$15B+)
        - **Timeline**: Phased development to 2040
        - **Ultimate capacity**: 65 million TEU
        - **Current capacity**: ~37 million TEU
        - **Expansion headroom**: +75% capacity
        
        **Why This Scale?**
        - Anticipate mega vessel growth (24,000+ TEU)
        - Accommodate all three alliances
        - Pre-empt regional competition
        - Lock in Singapore's position for next 50 years
        
        **Phased Development:**
        - Phase 1 (2021-2027): 21 berths, 23M TEU
        - Phase 2 (2027-2040): Additional berths to 65M TEU
        - Allows adaptation to market conditions
        - Spreads financial burden over time
        """)
    
    with col2:
        st.markdown("""
        **Design Features:**
        - **65 berths** when complete
        - **400m+ berth length** (handle 24,000 TEU vessels)
        - **20m depth** (accommodate deepest draft vessels)
        - **Fully automated** (AGVs, automated cranes)
        - **Climate resilient**: Built 5m above sea level
        - **Integrated operations**: Single mega terminal
        
        **Operational Targets:**
        - Berth productivity: 200+ moves/hour
        - BOA: >95%
        - Vessel turnaround: <24 hours (mega vessels)
        - Energy efficiency: 50% reduction vs conventional
        
        **Consolidation Benefits:**
        - Current: 5 terminals across Singapore
        - Future: 1 mega terminal at Tuas
        - Better equipment utilisation
        - Simplified operations
        - Freed up land for redevelopment (city centre)
        """)
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 Tuas Mega Port Green Features:</strong><br>
    Singapore isn\'t just building bigger—it\'s building smarter and greener:<br>
    - <strong>Climate resilience</strong>: Built 5 metres above mean sea level (sea level rise protection)<br>
    - <strong>Solar panel canopies</strong>: Throughout the terminal (renewable energy)<br>
    - <strong>Fully electrified quay cranes</strong>: Zero diesel emissions (vs conventional diesel cranes)<br>
    - <strong>Automated Guided Vehicles (AGVs)</strong>: Replace diesel prime movers<br>
    - <strong>Energy-efficient operations</strong>: Digital optimisation reduces waste<br>
    - <strong>Sustainable reclamation</strong>: Waste circularity in land reclamation<br>
    - <strong>Shore power ready</strong>: Vessels can plug into grid (zero emissions at berth)<br><br>
    
    Sustainability is becoming a <strong>competitive advantage</strong>—shipping lines face pressure to reduce carbon 
    footprint, and green ports will be preferred partners.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">Technology Leadership Strategy</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Digital Transformation Initiatives:**
    
    **digitalPORT@SG:**
    - AI-based port operations control
    - Predictive analytics for vessel traffic
    - Real-time optimisation
    - Digital twin for scenario testing
    
    **Automation at Tuas:**
    - Automated quay cranes (remote controlled)
    - AGVs for horizontal transport
    - Automated yard cranes
    - Minimal manual intervention
    
    **Data Analytics:**
    - Machine learning for demand forecasting
    - Predictive maintenance (equipment failures)
    - Dynamic yard planning
    - Container flow optimisation
    
    **Benefits:**
    - Higher productivity (24/7 operations, no fatigue)
    - Lower operating costs (less labour)
    - Consistent quality (no human error)
    - Scalability (add capacity without proportional workforce)
    - Competitive edge (technology barrier to entry)
    """)
    
    st.markdown('<p class="subsection-header">Lock-In Strategies</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Creating Switching Costs:**
    
    **Long-Term Terminal Leases:**
    - 20-30 year agreements with terminal operators
    - Operators make multi-billion dollar investments
    - High exit costs (cannot easily move)
    - Provides stability and predictability
    
    **Alliance-Dedicated Terminals:**
    - Dedicated berths for specific alliances
    - Customised to alliance needs
    - Deep integration with alliance operations
    - Alliance reluctant to switch (disruption cost)
    
    **Joint Ventures:**
    - PSA partners with shipping lines (e.g., MSC, CMA CGM)
    - Shared ownership = shared interests
    - Alignment of incentives
    - Reduces competition (partners, not just customers)
    
    **Ecosystem Advantage:**
    - Not just a port—complete maritime cluster
    - Bunkering, ship repair, finance, legal, technology
    - One-stop solution (convenience)
    - High switching cost (lose access to entire ecosystem)
    
    **Network Effects:**
    - 200+ shipping lines create network
    - Each line benefits from others' presence (cargo connections)
    - Self-reinforcing: More lines → Better network → Attracts more lines
    - Competitor needs to replicate entire network (nearly impossible)
    """)
    
    # ============================================================================
    # SECTION 7: Big Hub vs Vital Node
    # ============================================================================
    
    st.markdown('<p class="section-header">Strategic Positioning: "Big Hub" vs "Vital Node"</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore's strategic thinking has evolved from "being the biggest hub" to "being a vital node in an 
    interconnected port network." This shift is significant.
    """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🎯 The Strategic Shift: Big Hub → Vital Node</strong><br><br>
    
    <strong>Old Thinking: "Big Hub" Mentality</strong><br>
    - Winner-takes-all competition<br>
    - Size matters most (biggest = best)<br>
    - Centralised hub-and-spoke model<br>
    - Single point of failure vulnerability<br>
    - Pure volume focus<br><br>
    
    <strong>New Thinking: "Vital Node" Mentality</strong><br>
    - Network resilience matters<br>
    - Reliability + connectivity + efficiency = value<br>
    - Multiple complementary ports coexist<br>
    - Strategic position in network topology<br>
    - Quality over quantity focus<br><br>
    
    <strong>Why This Shift?</strong><br>
    - <strong>Mega vessels</strong>: Can\'t call at every port, need efficient hubs<br>
    - <strong>Alliance structures</strong>: Multiple hubs in network (not single mega hub)<br>
    - <strong>Risk management</strong>: Shipping lines want backup options (Suez blockage lesson)<br>
    - <strong>Regional development</strong>: Other hubs will exist (can\'t prevent), better to be best quality<br>
    - <strong>Sustainability</strong>: Efficiency and reliability becoming differentiators<br><br>
    
    <strong>What "Vital Node" Means:</strong><br>
    - <strong>Indispensable</strong>: Network functions poorly without this node<br>
    - <strong>Efficient</strong>: Fastest, most reliable, most cost-effective<br>
    - <strong>Connected</strong>: Links to more destinations than alternatives<br>
    - <strong>Resilient</strong>: Handles disruptions better than others<br>
    - <strong>Trusted</strong>: Consistent quality builds long-term relationships<br><br>
    
    <strong>Singapore\'s Implementation:</strong><br>
    - Focus on operational excellence (efficiency, reliability)<br>
    - Invest in technology (maintain edge)<br>
    - Build ecosystem (switching costs)<br>
    - Foster relationships (alliances, joint ventures)<br>
    - Accept coexistence with other hubs (Port Klang, PTP) but remain superior<br><br>
    
    Being the <strong>most reliable, most connected, most efficient</strong> hub is more valuable than being the 
    absolute largest.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 8: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Critical Success Factors (8):**
        - Strategic location (main trade routes)
        - Efficiency & flexibility (fast turnaround)
        - Reliability (BOA >90%, consistency)
        - Security & safety (low pilferage, safe operations)
        - Connectivity (200+ lines, 600+ ports)
        - Infrastructure & technology (deep berths, automation)
        - Cost vs service level (competitive with quality)
        - Skilled workforce & governance (stable, supportive)
        - Factors interact and reinforce (virtuous/vicious cycles)
        
        **Port Types:**
        - Gateway: 10-30% transshipment (serve local economy)
        - Transshipment Hub: 70-90% (pure hub function)
        - Hybrid: 40-60% (mix of both)
        - Singapore: 85% transshipment (pure hub, vulnerable)
        """)
    
    with col2:
        st.markdown("""
        **Regional Competition:**
        - Malaysia: Port Klang (14.1M), PTP (12.5M) - moderate-high threat
        - Indonesia: Tanjung Priok (8.9M) - low-moderate threat
        - Thailand: Laem Chabang (8.1M), Kra Canal (existential if built)
        - Vietnam: Cai Mep (6.8M) - moderate threat
        - Overcapacity risk if all expand simultaneously
        
        **Singapore\'s Response:**
        - Tuas Mega Port: S$20B+, 65M TEU by 2040
        - Technology leadership: Automation, AI, digital systems
        - Lock-in strategies: Long-term leases, JVs, ecosystem
        - "Vital node" positioning: Quality over quantity
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Success as a transshipment hub requires eight critical factors (location, 
    efficiency, reliability, security, connectivity, infrastructure, cost/service balance, skilled workforce) that 
    interact and reinforce each other in virtuous or vicious cycles. Singapore, as an 85% transshipment hub (pure hub), 
    faces moderate-to-high competition from regional ports (Malaysia\'s Port Klang and PTP, Vietnam\'s Cai Mep) and 
    potential existential threats (Kra Canal if ever built, Arctic route if viable year-round). Singapore responds 
    through massive infrastructure investment (Tuas S$20B+, 65M TEU capacity), technology leadership (full automation, 
    AI, digital systems), lock-in strategies (long-term leases, joint ventures, ecosystem advantages), and strategic 
    repositioning from "biggest hub" to "vital node" emphasising reliability, efficiency, and connectivity over pure 
    size. The risk of regional overcapacity makes operational excellence critical for survival.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** ⚙️ Operations Management - Explore the "Big Six" competitive competencies, quality management 
    frameworks (FMEA), capacity planning strategies, demand management techniques, and the critical trade-offs facing 
    port operators in day-to-day decision-making.
    """)
