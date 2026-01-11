import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">⚓ Port Strategy & Competition</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand the critical success factors for transshipment hubs, competitive dynamics between ports, 
    and strategic responses to emerging threats and opportunities.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Critical Success Factors for Transshipment Hubs
    # ============================================================================
    
    st.markdown('<p class="section-header">Critical Success Factors for Transshipment Hubs</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Not all ports are created equal. To succeed as a major transshipment hub in today's competitive 
    maritime environment, ports must excel across multiple dimensions simultaneously.
    """)
    
    st.markdown('<p class="subsection-header">The Essential Eight Factors</p>', unsafe_allow_html=True)
    
    # Success factors with detailed breakdown
    success_factors = pd.DataFrame({
        'Factor': [
            'Efficiency & Flexibility',
            'Reliability',
            'Security & Safety',
            'Cost vs Service Level',
            'Connectivity',
            'Infrastructure & Technology',
            'Skilled Workers + Management',
            'Strategic Location'
        ],
        'Why It Matters': [
            'Fast turnaround times reduce vessel port stay, lowering costs for shipping lines',
            'Predictable schedules allow tight connections; JIT supply chains demand reliability',
            'Cargo safety, port security, maritime safety standards; ISPS compliance required',
            'Balance competitive pricing with quality service; "tight connections" for time-sensitive cargo',
            'Number of shipping lines, frequency of services, global port network reach',
            'Adequate capacity for current + future demand; modern equipment; automation; IT systems',
            'Technical expertise, operational excellence, stable labour relations, capable leadership',
            'Proximity to major shipping lanes; centrality to trade flows; natural deep-water harbor'
        ],
        "Singapore's Performance": [
            'Excellent: Fast vessel turnaround; flexible berth allocation',
            'Outstanding: BOA >90%; minimal weather disruptions; strong track record',
            'World-class: ISPS certified; advanced security systems; low piracy risk',
            'Competitive: Not cheapest but excellent value; premium service justifies pricing',
            'Best-in-class: 200+ lines, 600+ ports; unmatched global reach',
            'Leading: Major Tuas investment; automated systems; CITOS; latest cranes',
            'Strong: Skilled workforce; SMA training; stable government; capable MPA/PSA management',
            'Ideal: On Asia-Europe route; 33% of global trade through Straits of Malacca/Singapore'
        ]
    })
    
    st.dataframe(success_factors, width='stretch', hide_index=True)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ Critical Point:</strong> These factors are <strong>not independent</strong>. They interact and reinforce 
    each other. For example:<br>
    - <strong>Good infrastructure</strong> enables <strong>efficiency</strong><br>
    - <strong>Efficiency</strong> attracts <strong>connectivity</strong> (more shipping lines)<br>
    - <strong>Connectivity</strong> increases volumes, justifying <strong>infrastructure investment</strong><br>
    - <strong>Skilled workers</strong> improve <strong>reliability and efficiency</strong><br>
    - <strong>Strategic location</strong> makes infrastructure investment worthwhile<br><br>
    This creates a <strong>virtuous cycle</strong> for successful ports and a <strong>vicious cycle</strong> for struggling ones.
    </div>
    """, unsafe_allow_html=True)
    
    # Visual representation of factor importance
    factors_radar = pd.DataFrame({
        'Factor': ['Efficiency', 'Reliability', 'Security', 'Cost/Service', 
                   'Connectivity', 'Infrastructure', 'Workforce', 'Location'],
        'Singapore': [95, 95, 98, 85, 100, 95, 90, 100],
        'Competitor Average': [75, 70, 80, 70, 65, 70, 75, 60]
    })
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=factors_radar['Singapore'],
        theta=factors_radar['Factor'],
        fill='toself',
        name='Singapore',
        line=dict(color='#3B82F6', width=3),
        fillcolor='rgba(59, 130, 246, 0.3)'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=factors_radar['Competitor Average'],
        theta=factors_radar['Factor'],
        fill='toself',
        name='Regional Competitor Avg',
        line=dict(color='#EF4444', width=3),
        fillcolor='rgba(239, 68, 68, 0.2)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100])
        ),
        showlegend=True,
        title={
            'text': 'Port Competitiveness: Singapore vs Regional Competitors',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        height=500
    )
    
    st.plotly_chart(fig, width='stretch')
    
    # ============================================================================
    # SECTION 2: Port Types and Strategic Positioning
    # ============================================================================
    
    st.markdown('<p class="section-header">Port Types: Gateway vs Transshipment vs Hub</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Different ports serve different strategic roles in the global shipping network. Understanding these 
    roles is key to understanding competitive dynamics.
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Gateway Port**
        
        **Definition:**
        - Serves local/regional cargo
        - Origin or destination point
        - Imports for local consumption
        - Exports from local production
        
        **Examples:**
        - Los Angeles/Long Beach (US)
        - Hamburg (Germany)
        - Sydney (Australia)
        
        **Characteristics:**
        - Hinterland-dependent
        - Economic health tied to region
        - Limited by local demand
        - Less vulnerable to competition
        
        **Strategy:**
        - Efficient inland connections
        - Strong customs/logistics
        - Regional market focus
        """)
    
    with col2:
        st.markdown("""
        **Transshipment Hub**
        
        **Definition:**
        - Cargo changes vessels
        - Not origin/destination
        - Connects feeder to mainline
        - 70-90% transshipment cargo
        
        **Examples:**
        - Singapore (85% transship)
        - Dubai (70%+ transship)
        - Colombo (Sri Lanka)
        
        **Characteristics:**
        - Location-critical
        - Network position vital
        - Highly competitive
        - Vulnerable to route changes
        
        **Strategy:**
        - Maximize connectivity
        - Ultra-high efficiency
        - Lock in shipping lines
        - Scale advantages
        """)
    
    with col3:
        st.markdown("""
        **Hybrid Hub Port**
        
        **Definition:**
        - Mix of gateway + transship
        - Serves local + connects
        - Balanced cargo portfolio
        - 30-60% transshipment
        
        **Examples:**
        - Rotterdam (40% transship)
        - Hong Kong (mixed)
        - Busan (South Korea)
        
        **Characteristics:**
        - More resilient
        - Diversified revenue
        - Regional + global role
        - Strategic flexibility
        
        **Strategy:**
        - Balance both functions
        - Develop hinterland
        - Maintain hub connectivity
        - Risk diversification
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🎯 Singapore's Position:</strong> Singapore is a <strong>pure transshipment hub</strong> with ~85% 
    transshipment cargo. This creates both enormous opportunity (tap into global flows) and significant 
    risk (vulnerable to shipping line decisions). Singapore's strategy is to be so efficient, connected, 
    and reliable that shipping lines cannot afford to bypass it.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 3: Regional Competition Landscape
    # ============================================================================
    
    st.markdown('<p class="section-header">Facing Increasing Regional Competition</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore does not compete in isolation. Ambitious port developments across Southeast Asia are 
    intensifying competition for transshipment volumes.
    """)
    
    st.markdown('<p class="subsection-header">Major Regional Competitors</p>', unsafe_allow_html=True)
    
    # Regional ports data
    regional_ports = pd.DataFrame({
        'Port Development': [
            'Malaysia - Carey Island',
            'Malaysia - Melaka Gateway',
            'Malaysia - East Coast Rail Link',
            'Indonesia - Tanjung Priok',
            'Thailand - Isthmus of Kra (proposed)',
            'Vietnam - Cai Mep',
            'Myanmar - Kyaukpyu'
        ],
        'Location': [
            'Near Port Klang, Malaysia',
            'Malacca Strait, Malaysia',
            'Kuantan to Port Klang rail',
            'Jakarta, Indonesia',
            'Southern Thailand',
            'Near Ho Chi Minh City',
            'Myanmar (Chinese investment)'
        ],
        'Status': [
            'Planned/Developing',
            'Under development',
            'Under construction',
            'Expanding capacity',
            'Proposed (decades)',
            'Growing rapidly',
            'Chinese BRI project'
        ],
        'Threat Level to Singapore': [
            'Medium: Proximity to Malacca Strait',
            'Medium: Strategic location',
            'Low-Medium: Inland connectivity',
            'Low: Gateway port focus',
            'High (if built): Would bypass Singapore',
            'Low-Medium: Different hinterland',
            'Medium: Alternative route to China'
        ],
        'Key Advantages': [
            'Lower costs, land availability',
            'Good location, government support',
            'Connects east-west Malaysia',
            'Serves Indonesian market (large)',
            'Could save 2-3 days transit time',
            'Growing Vietnamese economy',
            'Chinese backing, strategic route'
        ]
    })
    
    st.dataframe(regional_ports, width='stretch', hide_index=True)
    
    st.markdown("""
    **Competitive Dynamics:**
    
    **Cost Competition:**
    - Regional ports often have **lower labour costs**
    - **Cheaper land** for expansion
    - **Lower operating costs** overall
    - Singapore competes on **value** not just **price**
    
    **Location Competition:**
    - Some ports (Carey Island, Melaka Gateway) vie for similar routing
    - Thailand's Kra Canal (if built) would bypass Malacca Strait entirely
    - Alternative routes threaten Singapore's locational advantage
    
    **Government Support:**
    - Aggressive government backing for rival ports
    - Subsidies and incentives to attract shipping lines
    - National pride and strategic importance drive investment
    
    **Scale Race:**
    - Multiple ports expanding simultaneously
    - Risk of regional overcapacity
    - "Build it and they will come" approach doesn't always work
    """)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ The Overcapacity Risk:</strong> If Malaysia, Indonesia, Thailand, and other neighbors all 
    expand capacity simultaneously, Southeast Asia could face <strong>port overcapacity</strong>. This would lead to:<br>
    - Price wars and margin compression<br>
    - Underutilised facilities<br>
    - Wasted infrastructure investment<br>
    - Only the most efficient ports survive<br><br>
    This is why Singapore focuses on <strong>efficiency, reliability, and connectivity</strong> rather than just 
    competing on price.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 4: Global Competition
    # ============================================================================
    
    st.markdown('<p class="section-header">Global Port Competition</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore also competes globally with other major transshipment hubs for specific trade lanes and 
    shipping line partnerships.
    """)
    
    # Global competitors
    global_competitors = pd.DataFrame({
        'Port': ['Shanghai', 'Ningbo-Zhoushan', 'Shenzhen', 'Busan', 'Hong Kong', 'Dubai', 'Rotterdam', 'Antwerp'],
        'Country': ['China', 'China', 'China', 'S. Korea', 'China', 'UAE', 'Netherlands', 'Belgium'],
        'Annual TEU (M)': [49.0, 35.0, 30.0, 22.0, 18.0, 14.0, 15.0, 14.0],
        'Primary Type': ['Gateway', 'Gateway', 'Gateway', 'Hub', 'Hub', 'Hub', 'Hub', 'Gateway'],
        'Competitive Focus': [
            'Chinese exports',
            'Chinese exports, bulk cargo',
            'Pearl River Delta gateway',
            'Northeast Asia hub',
            'South China gateway + hub',
            'Middle East/Africa hub',
            'European gateway + hub',
            'European gateway'
        ]
    })
    
    st.dataframe(global_competitors, width='stretch', hide_index=True)
    
    # Top 10 ports visualization
    top_ports = pd.DataFrame({
        'Port': ['Shanghai', 'Singapore', 'Ningbo-Zhoushan', 'Shenzhen', 'Guangzhou', 
                 'Busan', 'Qingdao', 'Hong Kong', 'Tianjin', 'Rotterdam'],
        'TEU (Millions)': [49.0, 37.3, 35.0, 30.0, 25.0, 22.0, 21.0, 18.0, 17.0, 15.0],
        'Type': ['Gateway', 'Transship Hub', 'Gateway', 'Gateway', 'Gateway',
                'Hub', 'Gateway', 'Hub', 'Gateway', 'Hub']
    })
    
    fig = go.Figure(data=[
        go.Bar(
            x=top_ports['TEU (Millions)'],
            y=top_ports['Port'],
            orientation='h',
            marker=dict(
                color=['#94A3B8' if t == 'Gateway' else '#3B82F6' for t in top_ports['Type']],
                line=dict(color='#1F2937', width=1)
            ),
            text=top_ports['TEU (Millions)'],
            textposition='outside',
            textfont=dict(size=12)
        )
    ])
    
    fig.update_layout(
        title={
            'text': "World's Top 10 Container Ports by Annual Throughput",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        xaxis_title="Annual TEU (Millions)",
        height=450,
        plot_bgcolor='white',
        xaxis=dict(gridcolor='#E5E7EB'),
        annotations=[
            dict(x=35, y='Singapore', text='#1 Transshipment Hub', 
                 showarrow=True, arrowhead=2, ax=-50, ay=-30, font=dict(color='#3B82F6', size=11))
        ]
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    **Key Observations:**
    
    1. **Chinese Ports Dominate by Volume**
       - Top 10 includes 7 Chinese ports
       - Driven by massive manufacturing exports
       - Mostly gateway ports serving local cargo
    
    2. **Singapore's Unique Position**
       - #2 globally by volume
       - #1 by transshipment volume
       - Only pure transshipment hub in top 10
    
    3. **Hub Ports vs Gateway Ports**
       - Hub ports (Singapore, Busan, Dubai, Rotterdam) play different strategic role
       - Gateway ports (Shanghai, Ningbo) less vulnerable to competition
       - Singapore competes primarily with other hubs, not gateway ports
    """)
    
    # ============================================================================
    # SECTION 5: Strategic Planning for Port Competitiveness
    # ============================================================================
    
    st.markdown('<p class="section-header">Strategic Planning for Port Competitiveness</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Maintaining competitiveness requires deliberate, long-term strategic planning. Successful ports 
    follow structured strategic planning processes.
    """)
    
    st.markdown('<p class="subsection-header">The Strategic Planning Framework</p>', unsafe_allow_html=True)
    
    st.markdown("""
    A comprehensive port strategic plan typically includes:
    
    **1. Mission and Vision Statements**
    - Define the port's purpose and long-term aspirations
    - Example: Singapore's vision to remain as "vital port in inter-connected network"
    
    **2. Values and Behavioral Standards**
    - Core principles guiding decision-making
    - Safety, efficiency, reliability, innovation
    
    **3. Analysis of Business and Environmental Factors**
    - **SWOT Analysis**: Strengths, Weaknesses, Opportunities, Threats
    - Market trends and forecasts
    - Competitive intelligence
    - Technology trends
    - Regulatory environment
    
    **4. Strategic Objectives**
    - Specific, measurable goals
    - Examples: Throughput targets, efficiency metrics, market share goals
    
    **5. Lines of Action and Forward Responsibilities**
    - Detailed implementation plans
    - Resource allocation
    - Accountability assignments
    - Timeline and milestones
    
    **Planning Horizon:** Typically 5-10 years for major infrastructure decisions, with annual reviews 
    and adjustments.
    """)
    
    st.markdown('<p class="subsection-header">Singapore\'s Strategic Response to Competition</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Infrastructure Investment:**
        - **Tuas Mega Port**: S$20+ billion investment
        - 65M TEU capacity by 2040
        - World's largest automated port
        - Consolidates terminals for efficiency gains
        
        **Technology Leadership:**
        - CITOS® terminal operating system
        - Automated guided vehicles (AGVs)
        - AI-powered berth planning
        - Next-generation port control systems
        
        **Operational Excellence:**
        - BOA target >90% (berth on arrival)
        - Sub-24-hour turnaround for mega vessels
        - Continuous process improvement
        - Lean operations methodology
        """)
    
    with col2:
        st.markdown("""
        **Lock-In Strategies:**
        - **Joint ventures** with shipping lines (long-term commitment)
        - Dedicated terminals for major alliances
        - Customized services for key customers
        - Multi-year service agreements
        
        **Ecosystem Development:**
        - Complete maritime cluster (finance, legal, tech)
        - One-stop maritime services
        - High switching costs for shipping lines
        - Network effects and agglomeration benefits
        
        **Policy Stability:**
        - Predictable government support
        - "No U-turns" policy commitment
        - Long-term infrastructure planning
        - Pro-business regulatory environment
        """)
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 Singapore's Core Strategy:</strong> Rather than competing solely on price (a race to the 
    bottom), Singapore competes on:<br>
    - <strong>Efficiency</strong>: Fastest turnaround times<br>
    - <strong>Reliability</strong>: Minimal disruptions, predictable operations<br>
    - <strong>Connectivity</strong>: Unmatched global network<br>
    - <strong>Ecosystem</strong>: Complete maritime services cluster<br>
    - <strong>Innovation</strong>: Technology leadership<br><br>
    This strategy creates <strong>sustainable competitive advantages</strong> that are difficult for competitors to replicate.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 6: Emerging Threats and Route Changes
    # ============================================================================
    
    st.markdown('<p class="section-header">Emerging Threats: New Trade Routes and Channels</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Beyond port-to-port competition, Singapore faces potential threats from entirely new routing options 
    that could bypass traditional shipping lanes.
    """)
    
    st.markdown('<p class="subsection-header">Alternative Routes Under Development</p>', unsafe_allow_html=True)
    
    # Threats analysis
    threats_data = pd.DataFrame({
        'Threat': [
            'Arctic Route (Northern Sea Route)',
            'Kra Canal (Thailand)',
            'Trans-Pacific Rail Link',
            'Economic Zones Shifts',
            'Shipping Alliance Changes'
        ],
        'Description': [
            'Arctic melting opens Norway-Korea route, 30% shorter than Suez',
            'Canal across Thai isthmus bypasses Malacca Strait entirely',
            'Seaway to rail connection across North America',
            'Manufacturing shifts affect origin/destination patterns',
            'Alliance restructuring changes port calling patterns'
        ],
        'Likelihood': ['Medium (2030s-2040s)', 'Low (decades away)', 'Low-Medium', 'High (ongoing)', 'Medium-High'],
        'Impact if Occurs': [
            'High: Could divert Asia-Europe traffic away from Singapore',
            "Very High: Direct threat to Singapore's strategic location",
            'Low: Limited to specific routes, capacity constrained',
            'Medium: Requires adaptation but manageable',
            'Medium: Can be mitigated through relationships and JVs'
        ],
        "Singapore's Response": [
            'Monitor; maintain cost competitiveness; diversify services',
            'Tuas investment locks in scale; ecosystem creates switching costs',
            'Not directly addressable; maintain overall competitiveness',
            'Adapt to new trade patterns; flexible infrastructure',
            'Joint ventures; dedicated terminals; long-term partnerships'
        ]
    })
    
    st.dataframe(threats_data, width='stretch', hide_index=True)
    
    st.markdown("""
    **Competitive Advantage Trade-offs:**
    
    Singapore's strategy explicitly recognizes trade-offs between different competitive factors:
    
    - **Location vs Efficiency**: Location is fixed (advantage), but efficiency must be continuously improved
    - **Costs vs Service**: Not the cheapest, but offers best value for money
    - **Scale vs Flexibility**: Massive Tuas investment vs ability to adapt to market changes
    - **Connectivity vs Concentration**: Extensive network creates resilience but also dependencies
    """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🎯 "Big Hub vs Vital Node" Strategy:</strong><br><br>
    Singapore increasingly emphasizes being a <strong>vital node in an inter-connected port network</strong> rather than 
    simply the "biggest hub":<br><br>
    <strong>Big Hub Mentality:</strong><br>
    - Winner-takes-all competition<br>
    - Size matters most<br>
    - Vulnerability to single-point failure<br><br>
    <strong>Vital Node Mentality:</strong><br>
    - Network resilience matters<br>
    - Reliability + connectivity + efficiency = value<br>
    - Multiple complementary ports coexist<br>
    - Strategic position in network topology<br><br>
    This shift recognizes that being the <strong>most reliable, most connected, most efficient</strong> hub can be more 
    valuable than being the absolute largest.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 7: Green Ports and Sustainability
    # ============================================================================
    
    st.markdown('<p class="section-header">Green Ports and Sustainability</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Environmental sustainability is increasingly a competitive factor in port strategy. Leading ports 
    integrate green thinking into masterplanning processes.
    """)
    
    st.markdown("""
    **Why Green Ports Matter:**
    
    **Regulatory Pressures:**
    - IMO 2030/2050 decarbonization targets
    - Regional air quality regulations
    - Carbon pricing mechanisms
    - ESG (Environmental, Social, Governance) requirements
    
    **Customer Demands:**
    - Shipping lines face pressure to reduce carbon footprint
    - Cargo owners demand sustainable supply chains
    - Green credentials becoming competitive differentiator
    
    **Economic Benefits:**
    - Energy efficiency reduces operating costs
    - Green technology can improve productivity
    - Attracts eco-conscious customers and investors
    - Prepares for future carbon pricing
    """)
    
    st.markdown('<p class="subsection-header">Green Port Initiatives</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Infrastructure Design:**
        - Solar panels on terminal roofs
        - LED lighting throughout facilities
        - Energy-efficient building design
        - Rainwater harvesting systems
        - Green spaces and biodiversity
        
        **Equipment Electrification:**
        - Electric/hybrid quay cranes
        - Electric yard cranes (E-RTG)
        - Automated guided vehicles (AGVs) battery-powered
        - Shore power for vessels at berth
        - Electric trucks and prime movers
        """)
    
    with col2:
        st.markdown("""
        **Operational Measures:**
        - Optimised routing to reduce fuel use
        - Predictive maintenance to improve efficiency
        - Waste management and recycling programs
        - Carbon footprint monitoring and reporting
        
        **Strategic Partnerships:**
        - Collaboration with shipping lines on green initiatives
        - Research partnerships on alternative fuels
        - Industry consortia on sustainability standards
        - Green technology development
        
        **MPA Green Port Program:**
        - Incentives for green vessels
        - Support for alternative fuel bunkering
        - Green technology trials and adoption
        """)
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 Tuas Mega Port Green Features:</strong><br>
    - Built <strong>5 meters above mean sea level</strong> (climate resilience)<br>
    - <strong>Solar panel canopies</strong> throughout the terminal<br>
    - <strong>Fully electrified quay cranes</strong> (no diesel)<br>
    - <strong>AGVs</strong> instead of diesel prime movers<br>
    - <strong>Energy-efficient grab dredger</strong> for reclamation<br>
    - <strong>Sustainable reclamation</strong> with waste circularity<br>
    - <strong>Digital systems</strong> to optimise operations and reduce waste<br><br>
    Sustainability is not just environmental responsibility—it's becoming a <strong>competitive advantage</strong>.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 8: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Critical Success Factors:**
        - Eight key factors determine competitiveness
        - Factors are interdependent and self-reinforcing
        - Excellence required across all dimensions
        - Virtuous vs vicious cycles
        
        **Port Types:**
        - Gateway: Serves local hinterland
        - Transshipment Hub: Connects shipping networks
        - Hybrid: Mix of both functions
        - Singapore is pure transshipment hub (85%)
        
        **Regional Competition:**
        - Malaysia, Indonesia, Thailand developing ports
        - Lower costs but less established
        - Risk of overcapacity in Southeast Asia
        - Singapore competes on value, not just price
        """)
    
    with col2:
        st.markdown("""
        **Strategic Planning:**
        - 5-10 year planning horizons
        - SWOT analysis and market intelligence
        - Infrastructure, technology, operations
        - Lock-in strategies and partnerships
        
        **Emerging Threats:**
        - Arctic routes (climate change)
        - Kra Canal (if built)
        - Alliance restructuring
        - Trade pattern shifts
        
        **Strategic Response:**
        - Tuas investment (scale advantage)
        - Technology leadership (efficiency)
        - Ecosystem development (switching costs)
        - "Vital node" vs "biggest hub" mentality
        - Green port leadership
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Port competition is multidimensional and intensifying. Success requires 
    excellence across efficiency, reliability, connectivity, infrastructure, workforce, and location. 
    Singapore's stable government, long-term planning, and comprehensive ecosystem approach provide strong 
    competitive advantages, but continuous improvement and massive infrastructure investment (Tuas) are 
    necessary to stay ahead. Being a vital, reliable node in the inter-connected network is more valuable 
    than simply being the biggest hub.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** 🎯 Operations Management Fundamentals - Understand the "Big Six" competencies that 
    attract customers, quality management principles, and capacity planning strategies that drive port 
    operational excellence.
    """)
