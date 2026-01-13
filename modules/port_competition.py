import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">⚓ Port Strategy & Competition</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Master the critical success factors for transshipment hubs, understand competitive dynamics across gateway 
    vs transshipment ports, analyse regional competition from Malaysia, Indonesia, Thailand, evaluate emerging 
    threats (Kra Canal, Arctic routes, trade pattern shifts), comprehend strategic planning frameworks (SWOT, 
    Porter's Five Forces, scenario planning), and understand Singapore's "vital node in interconnected network" 
    philosophy versus the "big hub" mentality.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Critical Success Factors for Transshipment Hubs
    # ============================================================================
    
    st.markdown('<p class="section-header">Critical Success Factors for Transshipment Hubs</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The lecture materials emphasise a fundamental truth: not all ports can succeed as major transshipment hubs. 
    Success requires simultaneous excellence across multiple interdependent dimensions. Understanding these 
    **critical success factors** is essential for both port strategy and competitive analysis.
    
    The lecture framework identifies eight critical factors that determine whether a port can compete successfully 
    as a transshipment hub. Crucially, these factors are **not independent**—they interact and reinforce each 
    other in ways that create either virtuous cycles (for successful ports) or vicious cycles (for struggling ones).
    """)
    
    st.markdown('<p class="subsection-header">The Eight Critical Success Factors</p>', unsafe_allow_html=True)
    
    # Success factors with detailed breakdown
    success_factors = pd.DataFrame({
        'Factor': [
            '1. Efficiency & Flexibility',
            '2. Reliability',
            '3. Security & Safety',
            '4. Cost vs Service Level',
            '5. Connectivity',
            '6. Infrastructure & Technology',
            '7. Skilled Workers + Capable Management',
            '8. Strategic Location'
        ],
        'What It Means': [
            'Fast vessel turnaround times, flexible berth allocation, rapid cargo handling, adaptable operations',
            'Predictable schedules, consistent performance, minimal disruptions, dependable service delivery',
            'Cargo safety, port security (ISPS compliance), maritime safety standards, low theft/damage rates',
            'Competitive pricing balanced with quality service, enabling "tight connections" for time-sensitive cargo',
            'Number of shipping lines calling, service frequency, global port network reach, hub-feeder coverage',
            'Sufficient handling capacity for current + future demand, modern equipment, automation, IT systems',
            'Technical expertise, operational excellence, stable labour relations, capable port management, supportive government',
            'Proximity to major shipping lanes, centrality to trade flows, natural deep-water harbour, favourable geography'
        ],
        'Why Critical for Transshipment Hubs': [
            'Shipping lines minimize port time to maximize vessel utilization; slow ports lose competitiveness',
            'Tight transshipment connections require precise timing; unreliable ports break supply chains',
            'Transshipment cargo handled multiple times increases damage risk; security builds customer confidence',
            'Pure transshipment hubs compete primarily on value proposition; must balance cost with service quality',
            'Hub business model depends on extensive network; more connections = more cargo opportunities',
            'Mega vessels require specialized equipment; insufficient capacity creates congestion and delays',
            'Complex operations need skilled workforce; capable management makes strategic decisions; stable government provides certainty',
            'Cannot move geography; strategic location is foundational advantage but insufficient alone'
        ],
        "Singapore's Performance": [
            'Excellent: 24-36 hour turnaround for mega vessels (10,000+ moves), >90% Berth on Arrival',
            'Outstanding: Minimal weather disruptions (equatorial location), consistent track record, predictable service',
            'World-class: ISPS certified, advanced security systems, low piracy risk, strong rule of law',
            'Competitive: Not cheapest but premium value; efficient operations justify higher dues',
            'Best-in-class: 200+ shipping lines, 600+ ports connected globally, comprehensive hub-feeder network',
            'Leading: S$20B Tuas investment, automated systems, latest super post-Panamax cranes, digital infrastructure',
            'Strong: Skilled workforce via SMA training, capable MPA/PSA management, stable supportive government for 50+ years',
            'Ideal: On Asia-Europe mainline (33% global trade), Malacca Strait chokepoint (80,000+ transits annually)'
        ]
    })
    
    st.dataframe(success_factors, width='stretch', hide_index=True)
    
    st.markdown("""
    **Understanding Factor Interdependence:**
    
    The lecture materials explicitly state that these factors are **"not independent"**. This interdependence creates 
    powerful feedback loops that determine port competitiveness:
    
    **Positive Feedback Loop (Virtuous Cycle for Successful Ports):**
    
    1. **Good infrastructure** (Factor 6) → enables **high efficiency** (Factor 1)
    2. **High efficiency** → attracts **more shipping lines** (Factor 5 - connectivity)
    3. **More shipping lines** → increases cargo volumes → justifies **further infrastructure investment** (Factor 6)
    4. **Higher volumes** → improves **cost competitiveness** (Factor 4) through economies of scale
    5. **Skilled workers** (Factor 7) → improve **reliability and efficiency** (Factors 2 & 1)
    6. **Reliability** → attracts **premium cargo** requiring **tight connections** (Factor 4)
    7. **Strategic location** (Factor 8) → makes all **infrastructure investment** worthwhile (Factor 6)
    8. **Enhanced connectivity** → further increases volumes → cycle continues strengthening
    
    **Negative Feedback Loop (Vicious Cycle for Struggling Ports):**
    
    1. **Insufficient infrastructure** → **poor efficiency** → vessels experience delays
    2. **Delays** → **unreliable service** → shipping lines reduce calls
    3. **Fewer shipping lines** → **lower connectivity** → less cargo opportunities
    4. **Lower volumes** → **higher unit costs** (fixed costs spread over fewer containers)
    5. **Higher costs** + **poor service** → **lose competitiveness** → further volume decline
    6. **Declining volumes** → **cannot justify infrastructure investment** → efficiency worsens
    7. **Brain drain**: **Skilled workers** leave for better opportunities → **capability deteriorates**
    8. **Negative spiral**: Port becomes increasingly uncompetitive → eventual irrelevance
    
    **Strategic Implications:**
    
    These feedback loops explain why:
    - **Market leaders are hard to displace**: Singapore's established position reinforces itself through virtuous cycles
    - **New entrants face chicken-and-egg problems**: Need volumes to justify investment, but need investment to attract volumes
    - **Partial solutions don't work**: Excelling in only 3-4 factors is insufficient; gaps in any critical area become fatal weaknesses
    - **Small advantages compound**: Even marginal superiority in efficiency/reliability attracts more business, enabling further 
      improvements
    - **Decline accelerates**: Once a port loses momentum, the vicious cycle makes recovery extremely difficult
    
    This is why Singapore's **comprehensive approach** across all eight factors simultaneously creates such a formidable 
    competitive position. Competitors cannot simply match Singapore on one or two dimensions—they must match across 
    all eight to compete effectively.
    """)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ The "Factors Are Not Independent" Principle:</strong><br><br>
    The lecture materials emphasize this explicitly. Port competitiveness is not additive (8 separate factors scored 
    independently). Rather, it's <strong>multiplicative</strong>—weakness in any single factor undermines all others:<br><br>
    • Excellent efficiency (Factor 1) + poor reliability (Factor 2) = <strong>shipping lines avoid the port</strong><br>
    • Great location (Factor 8) + inadequate infrastructure (Factor 6) = <strong>cannot handle mega vessels</strong><br>
    • Strong connectivity (Factor 5) + security concerns (Factor 3) = <strong>premium cargo diverts elsewhere</strong><br><br>
    This multiplicative interaction explains why <strong>excellence requires simultaneous strength across all dimensions</strong>, 
    and why Singapore invests heavily to maintain leadership in every factor.
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
    
    st.plotly_chart(fig, use_container_width=True)
    
    # ============================================================================
    # SECTION 2: Port Types and Strategic Positioning
    # ============================================================================
    
    st.markdown('<p class="section-header">Port Types and Strategic Positioning</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Understanding different port types is essential for competitive analysis. Ports serve fundamentally different 
    strategic roles in global shipping networks, and these roles determine their competitive dynamics, vulnerabilities, 
    and strategic priorities.
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Gateway Port**
        
        **Definition:**
        - Serves local/regional cargo
        - Origin or destination point for trade
        - Imports consumed locally, exports from local production
        - Typically <30% transshipment cargo
        
        **Examples:**
        - Los Angeles/Long Beach (US West Coast gateway)
        - Hamburg (Germany/Northern Europe)
        - Sydney (Australian gateway)
        - Shanghai (serves Yangtze River Delta manufacturing)
        
        **Characteristics:**
        - **Hinterland-dependent**: Tied to local economic health
        - **Demand-driven**: Cargo volumes follow economic growth
        - **Captive cargo**: Local production/consumption must use this port
        - **Less competitive**: Geographic monopoly over hinterland
        
        **Strategic Priorities:**
        - Efficient inland connections (rail, truck, barge)
        - Strong customs facilitation
        - Warehousing and distribution capabilities
        - Serve regional market needs
        
        **Competitive Vulnerability:**
        - Low: Local cargo has limited alternatives
        - Main threat: Economic recession in hinterland
        """)
    
    with col2:
        st.markdown("""
        **Pure Transshipment Hub**
        
        **Definition:**
        - Cargo changes vessels, not origin/destination
        - Connects mainline to feeder vessels
        - Connects different mainline services
        - Typically 70-90% transshipment cargo
        
        **Examples:**
        - **Singapore** (85-90% transshipment)
        - Dubai/Jebel Ali (70%+ transshipment)
        - Colombo, Sri Lanka
        - Malta (Mediterranean transshipment)
        
        **Characteristics:**
        - **Location-critical**: Strategic position on trade routes
        - **Network-dependent**: Success requires extensive connectivity
        - **Highly competitive**: Must compete for discretionary cargo
        - **Route-vulnerable**: Shipping line routing decisions critical
        
        **Strategic Priorities:**
        - Maximize efficiency (minimize transshipment time)
        - Ultra-high reliability (enable tight connections)
        - Extensive connectivity (more lines = more opportunities)
        - Lock in shipping lines through relationships/JVs
        - Scale advantages (large hubs attract more calls)
        
        **Competitive Vulnerability:**
        - High: Vulnerable to new routes, competing hubs
        - Existential: Alternative routes bypass hub entirely
        """)
    
    with col3:
        st.markdown("""
        **Hybrid Hub Port**
        
        **Definition:**
        - Mix of gateway + transshipment functions
        - Serves local cargo AND connects networks
        - Balanced cargo portfolio
        - Typically 30-60% transshipment
        
        **Examples:**
        - Rotterdam (European gateway + transshipment)
        - Busan (South Korean gateway + Northeast Asia hub)
        - Hong Kong (historically, declining now)
        - Antwerp-Bruges (Belgian gateway + hub)
        
        **Characteristics:**
        - **Dual competitive position**: Gateway for local, hub for region
        - **More resilient**: Local cargo provides stable base
        - **Strategic flexibility**: Can shift focus as markets change
        - **Balanced risk**: Not fully dependent on either function
        
        **Strategic Priorities:**
        - Balance gateway and hub operations
        - Leverage local cargo to support hub function
        - Develop both hinterland and maritime connectivity
        - Invest in infrastructure supporting both roles
        
        **Competitive Vulnerability:**
        - Medium: Local cargo provides cushion
        - But: May lose competitiveness by trying to serve two masters
        - Risk: Pure hubs may be more efficient at transshipment
        """)
    
    st.markdown("""
    **Singapore's Position: Pure Transshipment Hub**
    
    Singapore operates as a **pure transshipment hub** with approximately **85-90% transshipment cargo**. Only 
    10-15% of containers calling Singapore originate or terminate there (local Singapore cargo). This creates both 
    enormous opportunity and significant strategic vulnerability.
    
    **The Opportunity:**
    - **Tap global trade flows**: Not limited by Singapore's local market size (5.8M population, small land area)
    - **Unlimited growth potential**: Can grow with global trade regardless of Singapore's GDP growth
    - **Southeast Asian beneficiary**: All regional growth routes through Singapore's hub
    - **Network effects**: More shipping lines → more connections → attracts even more lines
    
    **The Vulnerability:**
    
    As the lecture materials explicitly state: Singapore must remain as **"a vital port in an inter-connected port 
    network"**. The pure transshipment model creates several critical vulnerabilities:
    
    1. **Shipping line routing decisions**: Unlike gateway ports with captive cargo, every container through Singapore 
       is a discretionary choice by shipping lines. If alliances re-route services, Singapore loses volumes immediately.
    
    2. **No local cargo base to fall back on**: Gateway ports can survive losing transshipment business because they 
       still have hinterland cargo. Singapore has minimal local cargo—losing transshipment means losing the port business.
    
    3. **Regional competition**: Malaysia, Indonesia, Thailand, Vietnam all developing alternative hub ports with lower 
       costs and government support. Unlike local cargo (which cannot easily shift), transshipment cargo is fungible 
       across competing hubs.
    
    4. **Alternative route threats**: The proposed Kra Canal (if built) would bypass Singapore entirely. Gateway ports 
       are immune to route changes because local cargo still needs the port; transshipment hubs face existential threats 
       from route alternatives.
    
    5. **Trade pattern shifts**: Changes in global manufacturing (e.g., China+1 diversification) alter cargo flows. 
       Gateway ports benefit from local manufacturing; transshipment hubs must adapt to wherever cargo flows shift.
    
    **Singapore's Strategic Response:**
    
    Understanding this vulnerability explains Singapore's comprehensive strategy:
    - **Extreme efficiency**: Be so fast and reliable that routing through Singapore minimises total supply chain costs
    - **Unmatched connectivity**: 200+ lines, 600+ ports—provides one-stop access to global network
    - **Massive infrastructure investment**: S$20B Tuas locks in capacity advantage and long-term shipping line commitments
    - **Ecosystem development**: Complete maritime cluster creates enormous switching costs (can't just move port calls, 
      must relocate entire maritime operations)
    - **"Vital node" positioning**: Be indispensable through reliability and connectivity, not just largest
    
    This explains why Singapore cannot afford to be merely "good" across the eight critical factors—it must be 
    **exceptional** because every container is a competitive battle won or lost based on value proposition.
    """)
    
    # ============================================================================
    # SECTION 3: Regional Competition - The Intensifying Battle
    # ============================================================================
    
    st.markdown('<p class="section-header">Regional Competition: Facing Increasing Pressure</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The lecture materials explicitly highlight that Singapore faces **"rising port developments in SE Asia"** that 
    threaten its transshipment dominance. Understanding these competitive threats is essential for appreciating 
    Singapore's strategic investments and positioning.
    """)
    
    st.markdown('<p class="subsection-header">Major Regional Port Developments</p>', unsafe_allow_html=True)
    
    # Regional ports comprehensive data
    regional_ports = pd.DataFrame({
        'Development': [
            'Malaysia - Carey Island',
            'Malaysia - Melaka Gateway',
            'Malaysia - East Coast Rail Link',
            'Malaysia - Port Klang Expansion',
            'Malaysia - Tanjung Pelepas (PTP)',
            'Indonesia - Tanjung Priok',
            'Thailand - Isthmus of Kra (proposed)',
            'Thailand - Laem Chabang',
            'Vietnam - Cai Mep',
            'Myanmar - Kyaukpyu'
        ],
        'Location & Status': [
            'Near Malacca Strait, Malaysia (planned)',
            'Malacca Strait, Malaysia (developing)',
            'Kuantan to Port Klang rail link (under construction)',
            'Selangor, Malaysia (expanding)',
            'Southern Malaysia (operational, growing)',
            'Jakarta, Indonesia (major expansion)',
            'Southern Thailand (proposed, decades away)',
            'Near Bangkok, Thailand (expanding)',
            'Near Ho Chi Minh City, Vietnam (growing)',
            'Myanmar (Chinese BRI project)'
        ],
        'Competitive Threat Level': [
            'Medium: Strategic Malacca Strait location, lower costs',
            'Medium: Good location, aggressive government support',
            'Low-Medium: Improves Malaysia hinterland connectivity',
            'Medium: Already competes with Singapore, expanding capacity',
            'Medium-High: Operated by PSA competitor, efficient operations',
            'Low: Primarily gateway port for Indonesian market',
            'High (if built): Would bypass Singapore and Malacca Strait entirely',
            'Low-Medium: Primarily gateway for Thailand',
            'Low-Medium: Growing Vietnamese economy, different hinterland',
            'Medium: Chinese backing, alternative India-China route'
        ],
        'Key Advantages vs Singapore': [
            'Lower labour costs, cheaper land, proximity to Malacca Strait',
            'Strategic location, Malaysian government determination',
            'Connects east-west Malaysia, reduces transit time',
            'Lower costs, established operations, Malaysian gateway cargo',
            'Modern terminal, efficient, lower costs than Singapore',
            'Massive Indonesian market (280M people), gateway advantage',
            'Would save 2-3 days Asia-Europe transit, bypass Malacca Strait',
            'Growing Thai economy, gateway cargo provides base',
            'Rapidly growing Vietnamese exports, lower costs',
            'Geopolitical: China\'s Belt and Road Initiative support'
        ],
        "Singapore's Competitive Response": [
            'Superior efficiency, reliability, connectivity advantages',
            'Ecosystem switching costs, established relationships',
            'Not directly competing for same traffic',
            'Compete on value, not just price; maintain service quality',
            'Maintain efficiency edge, expand Tuas capacity',
            'Gateway port—different market segment',
            'Pre-emptive Tuas investment, ecosystem lock-in',
            'Gateway port—limited transshipment threat',
            'Monitor developments, maintain connectivity advantage',
            'Emphasize neutrality, reliability, comprehensive ecosystem'
        ]
    })
    
    st.dataframe(regional_ports, width='stretch', hide_index=True)
    
    st.markdown("""
    **Understanding the Competitive Dynamics:**
    
    **1. Cost Competition—The Double-Edged Sword:**
    
    Regional ports typically offer **significantly lower operating costs** than Singapore:
    - **Labour costs**: Malaysia/Indonesia/Thailand/Vietnam have labour costs 30-50% lower than Singapore
    - **Land costs**: Singapore faces extreme land scarcity; competitors have abundant cheap land for expansion
    - **Government subsidies**: Competitors often provide tax breaks, infrastructure subsidies to attract shipping lines
    - **Regulatory costs**: Singapore's high standards (safety, environment, labour) increase compliance costs
    
    **However, lower costs alone don't guarantee success:**
    
    Singapore's experience demonstrates that **total supply chain cost** matters more than port costs alone. A cheaper 
    port that causes delays, disruptions, or requires additional feeder connections may cost more in total than 
    Singapore's premium-priced but highly efficient operations.
    
    **The Value Equation:**
    - **Cheaper port** + unreliable service + poor connectivity = **Higher total supply chain cost**
    - **Premium port** + ultra-reliable + excellent connectivity + fast turnaround = **Lower total supply chain cost**
    
    Singapore competes on **total value**, not just **price**. The challenge is maintaining this value proposition as 
    competitors improve their efficiency and reliability.
    
    **2. Location Competition—The Kra Canal Existential Threat:**
    
    Among all competitive threats, the lecture materials specifically highlight the **Kra Canal** (Isthmus of Kra, Thailand) 
    as potentially catastrophic for Singapore.
    
    **What is the Kra Canal?**
    - Proposed canal across southern Thailand's narrow isthmus
    - Would connect Andaman Sea (Indian Ocean) to South China Sea (Pacific Ocean)
    - **Bypass Malacca Strait entirely**, cutting 1,200+ kilometres from Asia-Europe route
    - Save 2-3 days transit time for Asia-Europe services
    
    **Why Existential Threat to Singapore?**
    
    Unlike other competitive threats (which nibble at market share), the Kra Canal would **eliminate Singapore's 
    foundational locational advantage**:
    
    - **Singapore's entire position** rests on being at the **chokepoint** of Asia-Europe trade (Malacca Strait)
    - **Every vessel** currently using Malacca Strait calls at or near Singapore (captive traffic by geography)
    - **Kra Canal** would make Malacca Strait **optional**—vessels could skip it entirely using the new route
    - Singapore would transition from **"must call"** (on the route) to **"optional"** (off the route)
    
    **Current Status: Low Probability (But Not Zero):**
    
    - **Estimated cost**: US$28-40 billion (varies by design)
    - **Environmental concerns**: Massive ecological disruption
    - **Geopolitical opposition**: Singapore diplomatically opposes, Malaysia opposes (loses Port Klang traffic)
    - **No credible funding**: Thailand lacks resources, international funders wary of geopolitical backlash
    - **Technical challenges**: Excavation through mountainous terrain, extensive engineering required
    
    However, **China's Belt and Road Initiative** has renewed speculation—if China decided the strategic value justified 
    the cost, funding could materialize. The **30% time savings** on Asia-Europe routes provides strong economic 
    incentive for shipping lines if the canal were built.
    
    **Singapore's Response:**
    
    While Kra Canal remains low probability, Singapore's **S$20 billion Tuas investment** serves as insurance:
    - **If Kra Canal never built**: Tuas ensures Singapore maintains capacity and efficiency advantages over regional competitors
    - **If Kra Canal built**: Tuas's **65M TEU capacity** and **world-leading efficiency** make Singapore the best 
      transshipment option even without locational monopoly
    
    The lesson: Singapore cannot rely on geography alone—must continuously invest in **efficiency, connectivity, and 
    ecosystem** to maintain competitiveness regardless of routing changes.
    
    **3. Scale Competition—The Regional Overcapacity Risk:**
    
    A critical dynamic the lecture materials emphasise: if **all regional competitors expand simultaneously**, Southeast 
    Asia faces **port overcapacity**:
    
    - Malaysia expanding: Carey Island, Melaka Gateway, Port Klang, Tanjung Pelepas
    - Indonesia expanding: Tanjung Priok
    - Thailand developing: Laem Chabang expansion
    - Vietnam growing: Cai Mep
    - Singapore building: Tuas (65M TEU ultimate capacity)
    
    **Total planned capacity** across the region potentially exceeds **demand growth** for next 20-30 years.
    
    **What Happens with Overcapacity:**
    
    - **Price wars**: Ports compete by cutting dues, eroding profitability
    - **Underutilised facilities**: Expensive infrastructure sits idle
    - **Margin compression**: Fixed costs spread over fewer containers
    - **Survival of the fittest**: Only most efficient ports survive
    - **Stranded assets**: Billions invested in unused capacity
    
    **Singapore's Strategy in Overcapacity Scenario:**
    
    - **Efficiency advantage**: Tuas designed for lowest unit cost through automation
    - **Service quality**: Maintain reliability when competitors cut corners to reduce costs
    - **Ecosystem lock-in**: Comprehensive maritime cluster creates switching costs beyond just port operations
    - **Financial strength**: Singapore government backing ensures ability to weather price wars
    - **Long-term contracts**: Joint ventures and terminal agreements lock in volumes for 20-30 years
    
    The bet: In an overcapacity scenario, **efficiency and quality win**. Marginal, less-efficient ports close; Singapore 
    captures consolidated volumes. This explains the massive Tuas investment despite overcapacity risks—Singapore positions 
    to be the survivor.
    
    **4. Government Support Competition:**
    
    A critical dimension often overlooked: **national strategic importance** drives government support that distorts 
    normal market competition.
    
    **Why Governments Support Port Development:**
    
    - **National pride**: Port ranking seen as indicator of national status
    - **Economic development**: Ports create jobs, attract industry, generate export revenue
    - **Strategic autonomy**: Dependence on foreign ports seen as vulnerability
    - **Regional power**: Control over transportation infrastructure enhances geopolitical influence
    
    **Forms of Government Support:**
    
    - **Direct subsidies**: Covering losses, funding expansion
    - **Tax incentives**: Attracting shipping lines and maritime businesses
    - **Infrastructure investment**: Government-funded port facilities, rail links, highways
    - **Diplomatic pressure**: Using bilateral relationships to influence shipping line routing decisions
    - **Regulatory advantages**: Streamlined approvals, relaxed labour rules
    
    **Singapore's Approach:**
    
    Singapore also provides substantial government support, but differently:
    - **Stable, predictable policies**: 50+ year track record provides certainty for long-term investments
    - **World-class infrastructure**: Government commits billions (Tuas S$20B) ensuring cutting-edge facilities
    - **Ecosystem development**: MPA actively builds comprehensive maritime cluster (not just port operations)
    - **No arbitrary policy changes**: Lecture materials quote: "We avoid back tracking and U-turns"
    
    The competitive dynamic: Governments subsidise their ports for strategic reasons, making purely economic competition 
    difficult. Singapore's advantage is not just financial support but **quality of institutions, policy consistency, 
    and comprehensive ecosystem approach** that competitors struggle to replicate even with government backing.
    """)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ The Regional Overcapacity Risk:</strong><br><br>
    If Malaysia, Indonesia, Thailand, Vietnam, and Singapore all expand capacity simultaneously, Southeast Asia faces 
    <strong>significant port overcapacity</strong> within 10-15 years. This scenario would lead to:<br><br>
    • <strong>Destructive price competition</strong> eroding all ports' profitability<br>
    • <strong>Underutilised infrastructure</strong> representing billions in wasted investment<br>
    • <strong>Consolidation pressure</strong> forcing marginal ports to close<br>
    • <strong>Only the most efficient survive</strong>—operational excellence becomes decisive<br><br>
    This is why Singapore invests so heavily in <strong>efficiency (automation), reliability (track record), and 
    ecosystem (switching costs)</strong> rather than competing primarily on price. In an overcapacity scenario, 
    Singapore aims to be the <strong>last port standing</strong> when weaker competitors fail.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 4: Alternative Routes and Existential Threats
    # ============================================================================
    
    st.markdown('<p class="section-header">Emerging Threats: Alternative Routes and Trade Pattern Shifts</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Beyond port-to-port competition, Singapore faces potential threats from **entirely new routing options** and 
    **structural changes in global trade patterns** that could fundamentally alter demand for transshipment services.
    """)
    
    st.markdown('<p class="subsection-header">Alternative Maritime Routes</p>', unsafe_allow_html=True)
    
    # Alternative routes comprehensive analysis
    alternative_routes = pd.DataFrame({
        'Alternative Route': [
            'Arctic Route (Northern Sea Route)',
            'Kra Canal (Thailand Isthmus)',
            'Sunda/Makassar Straits (Indonesia)',
            'Belt and Road Initiative (Land Routes)',
            'Direct Shipping (Point-to-Point)'
        ],
        'Description': [
            'Arctic Ocean route from Norway/Europe to Northeast Asia, becoming viable as ice melts due to climate change',
            'Proposed canal through southern Thailand connecting Andaman Sea to South China Sea, bypassing Malacca Strait',
            'Alternative Indonesian straits routing to avoid Malacca Strait (longer distance but avoids potential chokepoint)',
            'Overland rail routes (China-Europe) providing alternative to maritime shipping for specific cargo',
            'Mega vessels sailing directly between origins/destinations without hub transshipment'
        ],
        'Time/Cost Impact': [
            '~30% time saving on Asia-Europe route (5,000 km shorter), significant fuel savings',
            '2-3 days time saving Asia-Europe route, ~1,200 km shorter than Malacca Strait routing',
            'Minimal time saving (actually longer) but strategic diversification away from Malacca Strait',
            'Faster than maritime (18-21 days vs 30-35 days Europe-China) but much higher cost per TEU',
            'Eliminates transshipment costs/time but requires very high vessel utilization (85-90%+)'
        ],
        'Current Status & Timeline': [
            'Operational but limited (summer only, icebreaker required); potentially viable 2030s-2040s year-round',
            'Proposed only, no credible funding, decades away if ever built (low probability)',
            'Always available, used occasionally for strategic reasons, not economically optimal',
            'Operational since 2011, niche role (~1% of maritime volume), limited by rail capacity',
            'Growing trend: larger vessels enable direct services on high-volume lanes, reduces transshipment %'
        ],
        'Threat Level to Singapore': [
            'Medium-High (2030s+): Could divert significant Asia-Europe traffic if becomes viable year-round',
            'Very High (if built): Existential threat—eliminates Singapore\'s locational advantage entirely',
            'Low: Not economically competitive, used only for specific strategic/security reasons',
            'Low: Niche solution for time-sensitive, high-value cargo; cannot replace maritime for volume',
            'Medium (growing): Gradual erosion of transshipment model as mega vessels enable more direct services'
        ],
        "Singapore's Response Strategy": [
            'Monitor developments; maintain cost/efficiency competitiveness; cannot directly address',
            'Pre-emptive Tuas investment locks in capacity; ecosystem creates switching costs even if route changes',
            'Not economically relevant; maintain service quality regardless',
            'Not directly competing (different cargo segments); focus on maritime efficiency',
            'Embrace hub-and-spoke efficiency gains; prove hub model remains economically superior for most cargo'
        ]
    })
    
    st.dataframe(alternative_routes, width='stretch', hide_index=True)
    
    st.markdown("""
    **Deep Dive: The Arctic Route—Climate Change as Competitive Threat**
    
    The lecture materials specifically mention the **"opening of Arctic lane from Norway to S Korea ~30% saving in trip time"** 
    as an emerging alternative route. This deserves detailed analysis because it represents a **structural change** driven 
    by climate change rather than economic competition.
    
    **Why the Arctic Route Matters:**
    
    Traditional Asia-Europe maritime route:
    - **Distance**: ~21,000 km (Shanghai to Rotterdam via Suez Canal and Malacca Strait)
    - **Transit time**: 30-35 days
    - **Passage through**: Malacca Strait → Indian Ocean → Suez Canal → Mediterranean → North Atlantic
    - **Singapore's position**: Right on this main route (Malacca Strait chokepoint)
    
    Northern Sea Route (Arctic):
    - **Distance**: ~14,000 km (Shanghai to Rotterdam via Arctic Ocean)
    - **Transit time**: 20-25 days (30% faster!)
    - **Passage through**: Bering Strait → Arctic Ocean → Barents Sea → North Atlantic
    - **Singapore's position**: Completely bypassed—not on route at all
    
    **Current Limitations (Why Not Used Today):**
    
    - **Ice coverage**: Only navigable 3-4 months per year (July-October) currently
    - **Icebreaker requirement**: Vessels need ice-class hull or icebreaker escort (expensive)
    - **Insurance costs**: Higher premiums due to risks (ice damage, limited rescue options, harsh conditions)
    - **Infrastructure gaps**: Limited ports, refuelling options along route
    - **Geopolitical concerns**: Russian control over much of route creates dependencies
    
    **Climate Change Impact (The Game Changer):**
    
    - Arctic sea ice declining **~13% per decade** since 1979
    - Ice-free summers potentially by **2030s-2040s** according to climate models
    - Longer navigation season: Potentially 6-8 months annually within 15-20 years
    - Eventually: **Year-round navigation** without icebreakers possible by 2050s
    
    **Implications for Singapore if Arctic Route Becomes Viable:**
    
    **Scenario 1: Partial Adoption (Most Likely 2030s-2040s)**
    - Summer months: Asia-Europe shipping shifts to Arctic route (30% time saving compelling)
    - Winter months: Traditional Malacca/Suez route continues
    - **Impact on Singapore**: ~30-40% reduction in Asia-Europe transshipment cargo during summer months
    - **Mitigation**: Singapore still essential for intra-Asia, trans-Pacific, other routes; seasonal adjustment possible
    
    **Scenario 2: Major Adoption (Possible 2050s+)**
    - Year-round Arctic route viability
    - 60-70% of Asia-Europe traffic diverts to Arctic route
    - **Impact on Singapore**: Fundamental threat to transshipment business model
    - **Mitigation**: Must pivot to other trade lanes, diversify beyond Asia-Europe dependency
    
    **Singapore's Strategic Calculus:**
    
    Singapore cannot prevent climate change or the opening of Arctic routes. Instead, the strategy focuses on:
    
    1. **Diversification**: Reduce dependency on Asia-Europe trade lane, strengthen intra-Asia, trans-Pacific routes
    2. **Efficiency**: Even if some routes shift, remain most efficient hub for routes that continue using Malacca Strait
    3. **Ecosystem strength**: Complete maritime cluster creates value beyond pure transshipment (bunkering, ship repair, 
       maritime services still needed regardless of routing)
    4. **Long-term uncertainty**: Arctic route viability timeline uncertain; don't over-react to potential 30+ year threat
    
    The Arctic route illustrates a fundamental reality: **geography is not permanently fixed**. Climate change, new canal 
    construction, or other technological changes can alter "strategic location" over time. Singapore's response is to 
    **maximise value across all other dimensions** (efficiency, reliability, connectivity, ecosystem) so competitiveness 
    doesn't rest solely on geography.
    """)
    
    # ============================================================================
    # SECTION 5: The "Vital Node" vs "Big Hub" Strategic Philosophy
    # ============================================================================
    
    st.markdown('<p class="section-header">Strategic Philosophy: "Vital Node" vs "Big Hub" Mentality</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The lecture materials introduce a profound strategic distinction that underlies Singapore's port strategy. The concept 
    of positioning as a **"vital port in an inter-connected port network"** rather than simply the **"biggest hub"** 
    represents a fundamental philosophical shift in how Singapore thinks about competition and resilience.
    """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🎯 Direct Quote from Lecture Materials:</strong><br><br>
    "Singapore must remain as a <strong>vital port in an inter-connected port network</strong> by staying on top in 
    handling transhipment containers."<br><br>
    This phrasing is deliberate and reveals Singapore's strategic thinking about port competition in an era of 
    increasing alternatives and potential route changes.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Understanding the Philosophical Shift:**
    
    **The "Big Hub" Mentality (Traditional Approach):**
    
    **Core Belief**: Size and volume determine success. The biggest port wins.
    
    **Strategy**:
    - Maximise throughput at any cost
    - Win market share through aggressive pricing
    - Build massive capacity to accommodate all possible volumes
    - Winner-takes-all competition—dominate or die
    
    **Assumptions**:
    - Shipping lines choose largest hub (network effects)
    - Scale advantages are decisive
    - Market leadership is self-reinforcing
    - Competitors cannot challenge the dominant hub
    
    **Vulnerabilities**:
    - **Single point of failure**: If "big hub" experiences disruption, entire network suffers
    - **Arrogance**: Complacency from dominance leads to service quality decline
    - **Price competition**: If only competing on size, vulnerable to cheaper alternatives
    - **Route dependence**: If shipping lanes shift, size advantage becomes liability (stranded assets)
    
    **The "Vital Node" Mentality (Singapore's Evolved Approach):**
    
    **Core Belief**: Indispensability and reliability determine success. Be so valuable that the network cannot function 
    optimally without you.
    
    **Strategy**:
    - Maximise efficiency, reliability, connectivity (not just volume)
    - Create comprehensive ecosystem (ports + maritime services)
    - Develop high switching costs (ecosystem lock-in)
    - Network resilience—be the hub others depend on for consistent performance
    - Collaborative mindset—multiple complementary hubs can coexist
    
    **Assumptions**:
    - Shipping lines choose most reliable, best-connected hub (value over size alone)
    - Service quality and predictability are decisive
    - Ecosystem completeness creates competitive moats
    - Network topology matters—being well-connected matters more than being largest
    
    **Advantages**:
    - **Resilient to competition**: Even if competitors grow larger, remain valuable through superior service
    - **Strategic flexibility**: Can adapt to market changes without depending solely on volume leadership
    - **Quality focus**: Continuous improvement in efficiency, reliability maintains differentiation
    - **Route independence**: Ecosystem value persists even if specific routes change
    
    **Practical Implications of "Vital Node" Philosophy:**
    
    **1. Investment Priorities Shift:**
    
    **"Big Hub" Approach**: Build maximum capacity, win on scale
    - Focus: Berths, cranes, yard space (physical assets to handle maximum volume)
    - Measure: Throughput (TEU handled per year)
    - Goal: Be #1 in volume rankings
    
    **"Vital Node" Approach**: Build comprehensive ecosystem, win on value
    - Focus: Efficiency (fast turnaround), reliability (minimal disruptions), connectivity (network reach), ecosystem 
      (maritime cluster)
    - Measure: Service quality, reliability metrics, customer satisfaction, ecosystem completeness
    - Goal: Be indispensable due to superior performance and switching costs
    
    **2. Competitive Response Changes:**
    
    **"Big Hub" Approach**: Respond to competitors by expanding capacity faster
    - If competitor adds capacity → Match or exceed their capacity
    - Price wars to maintain volume leadership
    - Risk: Overcapacity, margin compression, race to the bottom
    
    **"Vital Node" Approach**: Respond by enhancing value proposition
    - If competitor adds capacity → Improve efficiency, reliability, ecosystem services
    - Emphasize total value (not just price)
    - Result: Maintain profitability even if market share slightly eroded
    
    **3. Risk Management Philosophy:**
    
    **"Big Hub" Approach**: Concentration risk
    - Put all resources into being biggest hub for specific trade lanes
    - Vulnerable to route changes (e.g., Kra Canal would devastate pure "big hub" strategy)
    - Existential crisis if demand shifts
    
    **"Vital Node" Approach**: Diversification and resilience
    - Build value across multiple dimensions (not just volume)
    - Ecosystem provides value even if routing changes (bunkering, ship repair, maritime services continue)
    - Gradual adaptation possible as market evolves
    
    **Why Singapore Embraces "Vital Node" Philosophy:**
    
    **Historical Context**: Singapore became world's busiest port in 1990s pursuing "big hub" strategy. But by 2000s, 
    faced emerging challenges:
    
    - **Shanghai surpassed Singapore** in absolute volume (2010) due to China's massive gateway cargo
    - **Regional competition intensified**: Malaysia, Indonesia, Thailand all developing hub ports
    - **Alternative routes emerged**: Kra Canal proposals, Arctic route possibilities
    - **Trade patterns shifting**: Intra-Asia trade growing, reducing need for Singapore transshipment
    
    **Strategic Realisation**: Pure volume leadership is **unsustainable** when:
    - You're a pure transshipment hub (no local cargo base)
    - Competitors have government backing and lower costs
    - Your locational advantage could be undermined by new routes
    - Global trade patterns are shifting away from traditional flows
    
    **Solution**: Transition to **"vital node"** strategy:
    - Accept that Shanghai may have higher absolute volume (they have massive local cargo—different market segment)
    - Focus on being **world's largest transshipment hub** (different metric than total volume)
    - Invest in **ecosystem completeness** (170+ shipping groups, 30+ shipbrokers, 20+ banks, etc.)
    - Emphasise **reliability and efficiency** rather than just capacity
    - Build **switching costs** through comprehensive maritime cluster
    
    **The Result**: Singapore now positioned to remain relevant even in adverse scenarios:
    - **If Kra Canal built**: Ecosystem value persists (maritime services still needed)
    - **If Arctic route opens**: Intra-Asia, trans-Pacific routes still require transshipment
    - **If competitors grow**: Service quality and ecosystem differentiation maintain competitiveness
    - **If trade patterns shift**: Adaptable network position rather than rigid volume focus
    
    **Key Lesson for Digital Twin Context:**
    
    This philosophical shift from "big hub" to "vital node" thinking directly informs digital twin development priorities:
    
    - **Don't just model capacity**: Model efficiency, reliability, connectivity, ecosystem interactions
    - **Optimise for resilience**: Not just maximum throughput but adaptability to disruptions
    - **Value multiple dimensions**: Efficiency, service quality, network effects, not just volume
    - **Plan for uncertainty**: Scenario planning for route changes, competition, technology shifts
    
    The "vital node" philosophy recognises that in an **uncertain, competitive, evolving** maritime environment, 
    **sustainable competitive advantage** comes from **comprehensive value creation** rather than narrow excellence in 
    a single dimension (volume).
    """)
    
    # ============================================================================
    # SECTION 6: Strategic Planning Frameworks
    # ============================================================================
    
    st.markdown('<p class="section-header">Strategic Planning for Port Competitiveness</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Maintaining competitiveness in the intensely competitive port industry requires **systematic, long-term strategic 
    planning**. Successful ports like Singapore employ rigorous strategic planning frameworks that integrate analysis, 
    scenario planning, and execution.
    """)
    
    st.markdown('<p class="subsection-header">The Strategic Planning Process</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **1. Situation Analysis: Understanding Current Position**
    
    **SWOT Analysis Framework:**
    
    Strategic planning typically begins with comprehensive SWOT (Strengths, Weaknesses, Opportunities, Threats) analysis 
    to understand current competitive position.
    
    **Singapore's SWOT Example:**
    
    **Strengths:**
    - Strategic location on Asia-Europe mainline (Malacca Strait chokepoint)
    - World-class efficiency (24-36 hour vessel turnaround, >90% BOA)
    - Excellent reliability (minimal weather disruptions, stable operations)
    - Comprehensive maritime ecosystem (170+ shipping groups, complete service cluster)
    - Strong government support (stable policies, long-term commitment, S$20B Tuas)
    - Skilled workforce and capable management (MPA, PSA, SMA training)
    - Advanced technology infrastructure (automation, digital systems, innovation ecosystem)
    
    **Weaknesses:**
    - High cost structure (expensive land, labour, compliance costs)
    - Limited land for expansion (island geography constrains growth)
    - Pure transshipment dependence (85-90% transshipment, minimal local cargo base)
    - Vulnerable to shipping line decisions (no captive hinterland cargo)
    - Small domestic market (5.8M population limits local economic growth)
    
    **Opportunities:**
    - Growing intra-Asia trade (ASEAN+China integration)
    - ULCV deployment requires sophisticated hub facilities (competitive advantage)
    - Alternative fuel bunkering (LNG, methanol, ammonia—first-mover advantages)
    - Maritime technology leadership (digitalisation, automation, Maritime 4.0)
    - Regional economic growth (Southeast Asia growing 4-5% annually)
    
    **Threats:**
    - Regional port competition (Malaysia, Indonesia, Thailand expanding)
    - Kra Canal proposal (existential threat if built—bypasses Malacca Strait)
    - Arctic route emergence (climate change opens alternative Asia-Europe route)
    - Alliance restructuring (shipping line consolidation changes calling patterns)
    - Trade pattern shifts (US-China tensions, nearshoring, China+1 diversification)
    - Geopolitical risks (South China Sea tensions, regional conflicts)
    
    **2. Competitive Analysis: Porter's Five Forces**
    
    **Applying Porter's Framework to Port Competition:**
    
    **Force 1: Threat of New Entrants (MEDIUM-HIGH)**
    - **Barriers**: Massive capital requirements (US$1-5B for major terminals), long development timelines (10-15 years)
    - **Enablers**: Government backing reduces financial barriers, excess global investment seeking infrastructure returns
    - **Verdict**: High barriers but government support enables new entrants (Malaysia, Indonesia examples)
    
    **Force 2: Bargaining Power of Buyers (HIGH)**
    - **Buyers**: Shipping lines (alliances control 83% of capacity)
    - **Power**: Can shift routes/calls easily, negotiate long-term contracts, demand concessions
    - **Impact**: Ports must compete aggressively for shipping line commitments, limited pricing power
    
    **Force 3: Bargaining Power of Suppliers (LOW-MEDIUM)**
    - **Suppliers**: Equipment manufacturers, technology providers, labour
    - **Power**: Multiple equipment suppliers available, competitive labour markets
    - **Impact**: Ports can negotiate reasonably, though mega-crane manufacturers somewhat concentrated
    
    **Force 4: Threat of Substitutes (MEDIUM)**
    - **Substitutes**: Alternative routes (Arctic, Kra Canal), direct shipping (point-to-point), alternative modes (rail)
    - **Viability**: Some substitutes viable for specific cargo/routes, but maritime dominates for volume
    - **Impact**: Moderate threat—ports must maintain cost/efficiency competitiveness
    
    **Force 5: Rivalry Among Existing Competitors (VERY HIGH)**
    - **Competitors**: Multiple regional ports competing for same transshipment volumes
    - **Intensity**: Price competition, service competition, infrastructure arms race
    - **Impact**: Erodes margins, drives continuous improvement, forces massive investments
    
    **Conclusion**: Port industry competitiveness is **intense**, with high buyer power and rivalry creating constant 
    pressure. Sustainable advantage requires **differentiation** (efficiency, ecosystem, relationships) not just capacity.
    
    **3. Scenario Planning: Preparing for Alternative Futures**
    
    **Why Scenario Planning Matters:**
    
    Traditional forecasting assumes linear trends continue. But port planning faces **radical uncertainties**:
    - Will Kra Canal be built? (Unknown)
    - Will Arctic route become viable? (Climate-dependent)
    - How will trade patterns evolve? (Geopolitics-dependent)
    - What will vessel sizes be in 2040? (Technology-dependent)
    
    **Scenario Planning Approach:**
    
    Instead of single forecast, develop **multiple plausible scenarios** and strategies for each:
    
    **Scenario A: Continuation of Current Trends**
    - Malacca Strait remains primary route
    - Vessel sizes continue growing (up to 30,000 TEU)
    - Singapore maintains hub status
    - **Strategy**: Tuas expansion, efficiency improvements, ecosystem strengthening
    
    **Scenario B: Major Route Disruption (Kra Canal Built)**
    - Kra Canal opens 2040s, diverts 50%+ of Asia-Europe traffic
    - Singapore's locational advantage eliminated
    - Must compete without geography
    - **Strategy**: Ecosystem indispensability, intra-Asia focus, maritime services diversification
    
    **Scenario C: Technology Transformation**
    - Autonomous vessels enable direct point-to-point shipping
    - Transshipment volumes decline
    - Alternative fuels reshape bunkering
    - **Strategy**: Digital leadership, alternative fuel hub, adapt to smaller transshipment market
    
    **Scenario D: Geopolitical Fragmentation**
    - US-China decoupling accelerates
    - Trade blocs form (US+allies vs China+BRI)
    - Singapore's neutrality becomes liability
    - **Strategy**: Maintain neutrality, serve all markets, emphasize reliability and consistency
    
    **Multi-Scenario Strategy**: Invest in **capabilities valuable across scenarios**:
    - Efficiency improvements useful in all scenarios
    - Ecosystem strength provides resilience
    - Technology leadership enables adaptation
    - Financial reserves allow flexibility
    
    **4. Strategic Objectives and Execution**
    
    **Setting Measurable Goals (5-10 Year Horizon):**
    
    - **Capacity**: Complete Tuas Phase 1 & 2 (40M TEU operational by 2027)
    - **Efficiency**: Maintain <24 hour vessel turnaround for mega vessels
    - **Reliability**: Sustain >90% Berth on Arrival performance
    - **Connectivity**: Maintain 600+ port connections, 200+ shipping lines
    - **Technology**: Deploy comprehensive port automation, digital twin operations
    - **Sustainability**: Achieve 50% reduction in port emissions by 2030
    - **Market share**: Maintain world's largest transshipment hub status
    
    **Execution Mechanisms:**
    
    - **Joint ventures**: Lock in shipping lines through dedicated terminals (Evergreen-PSA JV example)
    - **Long-term contracts**: 20-30 year terminal leases create commitment
    - **Continuous improvement**: Kaizen-style operational excellence programmes
    - **Technology adoption**: Systematic automation deployment, digital transformation
    - **Workforce development**: SMA training, upskilling programmes, talent attraction
    - **Policy consistency**: Stable government commitment provides certainty
    
    **Review and Adaptation:**
    
    - **Annual strategic reviews**: Assess progress, adapt to market changes
    - **Quarterly operational reviews**: Track key performance indicators (KPIs)
    - **Continuous market intelligence**: Monitor competitors, technology trends, trade patterns
    - **Flexibility**: Adjust plans based on emerging developments whilst maintaining long-term direction
    """)
    
    # ============================================================================
    # SECTION 7: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways: Port Strategy and Competition</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Critical Success Factors:**
        - **Eight interdependent factors** determine transshipment hub competitiveness
        - Factors are **"not independent"**—weakness in one undermines all others
        - Excellence required **simultaneously across all dimensions**
        - **Virtuous cycles** for successful ports vs **vicious cycles** for struggling ports
        - Singapore excels across all eight factors creating formidable competitive position
        
        **Port Types and Positioning:**
        - **Gateway ports**: Serve local cargo (captive market, less competitive pressure)
        - **Transshipment hubs**: Connect shipping networks (highly competitive, vulnerable to routing)
        - **Hybrid ports**: Mix of both (more resilient but potentially less focused)
        - Singapore: **Pure transshipment hub** (85-90% transshipment)—high opportunity, high vulnerability
        
        **Regional Competition Intensifying:**
        - **Malaysia**: Carey Island, Melaka Gateway, Port Klang expansion—strategic locations, lower costs
        - **Indonesia**: Tanjung Priok expansion serving 280M population gateway market
        - **Thailand**: Laem Chabang growth; Kra Canal proposal (existential threat if built)
        - **Vietnam**: Cai Mep expansion riding Vietnamese economic growth
        - **Overcapacity risk**: Simultaneous expansion could create regional overcapacity
        """)
    
    with col2:
        st.markdown("""
        **Alternative Routes and Threats:**
        - **Arctic Route**: ~30% time saving Asia-Europe, potentially viable 2030s-2040s (medium-high threat)
        - **Kra Canal**: Would bypass Malacca Strait entirely (existential threat if built, but low probability)
        - **Trade pattern shifts**: US-China tensions, China+1 diversification altering flows
        - **Direct shipping**: Mega vessels enabling more point-to-point services (gradual transshipment erosion)
        
        **"Vital Node" vs "Big Hub" Philosophy:**
        - Traditional "big hub" mentality: Size matters most, winner-takes-all competition
        - Evolved "vital node" mentality: **Indispensability through reliability, efficiency, connectivity**
        - Be so valuable that network **cannot function optimally without you**
        - Ecosystem completeness creates **switching costs** beyond pure port operations
        - **Resilience** through comprehensive value creation, not just volume leadership
        
        **Singapore's Strategic Response:**
        - **Tuas S$20B investment**: Pre-emptive capacity, scale advantage, long-term lock-in
        - **Technology leadership**: Automation, digital twins, Maritime 4.0 positioning
        - **Ecosystem development**: 170+ shipping groups, comprehensive maritime cluster
        - **Service excellence**: Maintain efficiency, reliability advantages as competitors improve
        - **Vital node positioning**: Be indispensable through quality, not just size
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Port competition is <strong>multidimensional and intensifying</strong>. Success 
    as a transshipment hub requires simultaneous excellence across eight interdependent critical factors: efficiency, 
    reliability, security, cost/service balance, connectivity, infrastructure, skilled workforce, and strategic location. 
    Singapore's pure transshipment model (85-90% transshipment cargo) creates both enormous opportunity (tap global trade 
    flows) and significant vulnerability (no local cargo base, dependent on shipping line routing decisions). Regional 
    competition is intensifying as Malaysia, Indonesia, Thailand, and Vietnam develop alternative hub ports with lower 
    costs and government backing. Alternative routes (Arctic, Kra Canal) and trade pattern shifts (US-China tensions, 
    China+1 diversification) pose potential existential threats. Singapore's strategic response centres on the 
    <strong>"vital node in inter-connected network"</strong> philosophy: be so efficient, reliable, connected, and 
    ecosystem-complete that the global shipping network cannot function optimally without Singapore. This requires 
    massive infrastructure investment (Tuas S$20B), technology leadership (automation, digitalisation), ecosystem 
    development (comprehensive maritime cluster creating switching costs), and unwavering commitment to service excellence. 
    The lesson: <strong>sustainable competitive advantage</strong> in an uncertain, competitive environment comes from 
    <strong>comprehensive value creation</strong> across multiple dimensions rather than narrow excellence in size alone.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** 🔧 Container Terminal Operations - Dive deep into the physical operations of container terminals, 
    understanding vessel operations (berthing, cargo handling), yard operations (storage, stacking, retrieval), gate 
    operations (truck processing, documentation), equipment types (quay cranes, yard cranes, prime movers, AGVs), 
    operational planning and optimization, and the automation journey from manual to fully automated terminals.
    """)
