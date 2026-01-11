import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">🌍 Global Shipping & Alliances</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand industry consolidation, the dramatic 2025 alliance reshuffling, the power of shipping 
    alliances, hub-and-spoke network structures, and how geopolitics shapes global shipping patterns.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Industry Consolidation
    # ============================================================================
    
    st.markdown('<p class="section-header">Industry Consolidation: From Many to Few</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The container shipping industry has undergone dramatic consolidation over the past two decades. 
    What was once a fragmented industry with dozens of independent carriers is now dominated by 
    a handful of mega-carriers and strategic alliances.
    """)
    
    st.markdown('<p class="subsection-header">The Consolidation Journey</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Year 2000", "15+ Major Carriers", help="Independent carriers competing globally")
    with col2:
        st.metric("Year 2025", "9 Major Players", help="After mergers, acquisitions, and bankruptcies")
    with col3:
        st.metric("Alliance/Solo Control", "~80%", help="Four groups (3 alliances + MSC solo) control ~80% of global capacity")
    
    st.markdown("""
    **Key Consolidation Events:**
    
    **1990s-2000s: Fragmented Competition**
    - 15+ major global carriers competing independently
    - Regional carriers dominating local trades
    - Minimal cooperation beyond vessel sharing
    - Intense price competition, thin margins
    
    **2010s: Merger Wave Begins**
    - **2005**: P&O Nedlloyd acquired by Maersk
    - **2014**: Hamburg Süd acquired by Maersk (completed 2017)
    - **2016**: APL acquired by CMA CGM
    - **2016**: Hanjin Shipping bankruptcy (world's 7th largest carrier collapsed)
    - **2017**: OOCL acquired by COSCO ($6.3 billion)
    - **2018**: Japanese carriers (NYK, MOL, K Line) merge into ONE
    
    **2020s: Alliance Dominance and Reshuffling**
    - **2015-2024**: Three mega-alliances control 80-83% of global capacity
    - **2023**: Maersk & MSC announce 2M Alliance dissolution
    - **2024**: Major alliance reshuffling announced
    - **2025**: Complete restructuring takes effect (February 1)
    - **Current**: Four groups compete (3 alliances + MSC solo)
    """)
    
    # Industry consolidation data - updated through 2025
    consolidation_data = pd.DataFrame({
        'Year': [2000, 2005, 2010, 2015, 2017, 2020, 2024, 2025],
        'Number of Major Carriers': [17, 15, 15, 15, 12, 10, 9, 9],
        'Top 3 Market Share (%)': [28, 32, 35, 39, 42, 48, 52, 54],
        'Alliance/Group Control (%)': [0, 15, 35, 60, 75, 82, 83, 80]
    })
    
    # Create side-by-side charts
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(
            x=consolidation_data['Year'],
            y=consolidation_data['Alliance/Group Control (%)'],
            mode='lines+markers',
            fill='tozeroy',
            line=dict(color='#3B82F6', width=3),
            marker=dict(size=10),
            name='Alliance/Group Control'
        ))
        fig1.update_layout(
            title='Alliance/Group Control Growth',
            xaxis_title="Year",
            yaxis_title="Market Control (%)",
            height=350,
            plot_bgcolor='white',
            yaxis=dict(gridcolor='#E5E7EB', range=[0, 100]),
            xaxis=dict(gridcolor='#E5E7EB')
        )
        st.plotly_chart(fig1, use_container_width=True)
    
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
        st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("""
    **Why Consolidation Happened:**
    
    **Overcapacity Crisis (2015-2016):**
    - Carriers ordered too many mega vessels in 2000s-2010s
    - Supply growth exceeded demand growth → Freight rates collapsed
    - Many carriers losing money (2015-2016 particularly severe)
    - Hanjin bankruptcy shocked industry (August 2016)
    - Forced wave of mergers, acquisitions, and consolidation
    
    **Economies of Scale:**
    - Bigger carriers negotiate better prices with ports and suppliers
    - Spread fixed costs (IT systems, management, brand) over larger volumes
    - Larger networks attract more customers (network effects)
    - Better bargaining power with ports for terminal rates
    - Can deploy mega vessels economically (20,000+ TEU)
    
    **Survival Strategy:**
    - Small carriers couldn't compete on costs alone
    - Mergers and acquisitions provided scale economies
    - Alliances allowed cooperation without full mergers
    - **"Get big or get out"** became industry mantra
    - Only the largest survived profitably
    """)
    
    # ============================================================================
    # SECTION 2: The Great Reshuffling of 2025
    # ============================================================================
    
    st.markdown('<p class="section-header">The Great Reshuffling of 2025</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ MAJOR INDUSTRY RESTRUCTURING - February 1, 2025</strong><br>
    The alliance structure that dominated container shipping for a decade completely changed on February 1, 2025. 
    The 2M Alliance (MSC + Maersk) dissolved, THE Alliance lost its largest member, and two new competitive 
    groups emerged. This represents the biggest reshuffling of global shipping alliances since their formation.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">Timeline of the 2025 Reshuffling</p>', unsafe_allow_html=True)
    
    # Timeline
    timeline_data = pd.DataFrame({
        'Date': [
            'January 2023',
            'January 17, 2024',
            'September 9, 2024',
            'January 31, 2025',
            'February 1, 2025',
            'February-May 2025',
            'June 2025'
        ],
        'Event': [
            '2M Alliance Dissolution Announced',
            'Gemini Cooperation Announced',
            'Premier Alliance Announced',
            'Last Day of 2M and THE Alliances',
            'New Alliance Structure Takes Effect',
            'Transition Period (Network Phase-In)',
            'Gemini Fully Operational'
        ],
        'Impact': [
            'MSC & Maersk announce end of 10-year partnership (effective Jan 2025)',
            'Maersk + Hapag-Lloyd announce new long-term cooperation starting Feb 2025',
            'ONE + HMM + Yang Ming announce 5-year cooperation (THE rebranded)',
            '2M ends after decade; Hapag-Lloyd exits THE Alliance 2 years early',
            'Ocean (unchanged), Gemini (new), Premier (rebranded), MSC (solo) begin',
            'Gradual rollout of new networks, services, port rotations',
            'All Gemini vessels operating on new schedules, >90% reliability target'
        ]
    })
    
    st.dataframe(timeline_data, use_container_width=True, hide_index=True)
    
    st.markdown("""
    **Why the Reshuffling Happened:**
    
    **MSC-Maersk Divorce (2M Dissolution):**
    - **Strategic divergence**: MSC focused on aggressive growth and scale; Maersk pivoted to integrated logistics
    - **Cultural mismatch**: MSC owner-operated (Aponte family); Maersk publicly traded (shareholder pressure)
    - **Growth trajectories**: MSC adding capacity rapidly (400+ ships in 5 years); Maersk more selective
    - **Business models**: MSC remains pure shipping; Maersk expanding into air freight, warehousing, trucking
    - **Scale disparity**: By 2024, MSC (6.4M TEU) had grown 50% larger than Maersk (4.5M TEU)
    - **Competitive tension**: Partners becoming rivals rather than collaborators
    
    **Maersk-Hapag-Lloyd Partnership (Gemini Formation):**
    - **"Like-minded" carriers**: Both focus on reliability, service quality, decarbonisation
    - **Complementary assets**: Both own terminal networks (APM Terminals, Hapag-Lloyd terminals)
    - **Environmental alignment**: Maersk (net-zero 2040), Hapag-Lloyd (2045) - most ambitious timelines
    - **Operational philosophy**: Both prioritise schedule reliability over maximum port coverage
    - **Strategic fit**: Gemini enables Maersk's integrator strategy with controlled terminals
    
    **THE Alliance Breakdown (Hapag-Lloyd Exit):**
    - Hapag-Lloyd left 2 years ahead of schedule (original agreement until March 2027)
    - Remaining members (ONE, HMM, Yang Ming) rebranded as **Premier Alliance**
    - Loss of largest member (Hapag-Lloyd ~2M TEU) created capacity gap
    - Premier now smallest alliance (~3.6M TEU), must prove viability
    
    **MSC Goes Solo:**
    - World's largest carrier (7.1M TEU) has scale to operate independently
    - Flexibility to deploy capacity without alliance constraints
    - Can optimise network for its own strategic priorities
    - Retains slot exchange partnerships (e.g., with ZIM on trans-Pacific)
    """)
    
    # ============================================================================
    # SECTION 3: The New Alliance Structure (2025-Present)
    # ============================================================================
    
    st.markdown('<p class="section-header">The New Alliance Structure (2025-Present)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    As of February 1, 2025, global container shipping is organised into **four competitive groups**: 
    three alliances (Ocean Alliance, Gemini Cooperation, Premier Alliance) plus MSC operating independently.
    """)
    
    # New alliance data (2025)
    alliance_data_2025 = pd.DataFrame({
        'Group': ['Ocean Alliance', 'Gemini Cooperation', 'MSC (Independent)', 'Premier Alliance', 'Other Independents'],
        'Market Share (%)': [29, 21, 20, 11, 19],
        'Total Capacity (M TEU)': [8.91, 6.75, 7.10, 3.57, 6.5],
        'Operational Capacity (M TEU)': [3.8, 3.4, 6.4, 3.0, 'N/A'],
        'Number of Vessels (Operational)': [330, 290, 886, 250, 'Varies'],
        'Key Members': [
            'CMA CGM, COSCO, OOCL, Evergreen',
            'Maersk, Hapag-Lloyd',
            'MSC only',
            'ONE, HMM, Yang Ming',
            'ZIM, Wan Hai, PIL, others'
        ]
    })
    
    st.dataframe(alliance_data_2025, use_container_width=True, hide_index=True)
    
    # Market share visualization
    fig = go.Figure(data=[go.Pie(
        labels=alliance_data_2025['Group'],
        values=alliance_data_2025['Market Share (%)'],
        marker=dict(colors=['#10B981', '#3B82F6', '#EF4444', '#F59E0B', '#94A3B8']),
        textinfo='label+percent',
        textfont=dict(size=13, color='white'),
        hole=0.4
    )])
    
    fig.update_layout(
        title={
            'text': 'Global Container Shipping Market Share by Group (February 2025)',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        annotations=[dict(text='Total<br>Market', x=0.5, y=0.5, font_size=16, showarrow=False)],
        height=450
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('<p class="subsection-header">1. Ocean Alliance (29% Market Share - LARGEST)</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        **Members:**
        - CMA CGM (France) - 3rd largest carrier
        - COSCO Shipping (China) - 4th largest
        - OOCL (Hong Kong/China)
        - Evergreen (Taiwan) - 7th largest
        
        **Formation:** 2017
        
        **Status:** Extended to 2032
        
        **Capacity:**
        - Combined: 8.91M TEU
        - Operational: ~3.8M TEU
        - Vessels: ~390 ships, ~330 operational
        """)
    
    with col2:
        st.markdown("""
        **Characteristics:**
        - **LARGEST ALLIANCE** in 2025 restructuring
        - **ONLY UNCHANGED** alliance (stable through reshuffling)
        - Strongest Asian presence (COSCO, OOCL, Evergreen)
        - CMA CGM brings European strength and global reach
        - **Dominant on trans-Pacific**: 15 weekly USWC sailings, 8 USEC sailings
        - Widest North Europe coverage: 7 services (matches MSC)
        
        **Strategy:**
        - Balanced approach: good coverage + competitive service
        - Ultra-large vessel deployment (average 13,200 TEU)
        - Multiple port calls per service
        - Focus on Asia trade lanes
        
        **Key Routes (41 Services Across 8 Markets):**
        - Far East - North Europe (7 services)
        - Far East - Mediterranean
        - Far East - USWC / USEC / US Gulf
        - Trans-Atlantic (with ONE slot exchange)
        - Far East - Middle East
        - Far East - Red Sea
        """)
    
    st.markdown('<p class="subsection-header">2. Gemini Cooperation (21% Market Share - NEWEST)</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        **Members:**
        - Maersk (Denmark) - 2nd largest carrier
        - Hapag-Lloyd (Germany) - 5th largest
        
        **Formation:** February 1, 2025
        
        **Duration:** Long-term (4-5+ years)
        
        **Capacity:**
        - Combined: 6.75-6.82M TEU
        - Operational: 3.4-3.7M TEU
        - Vessels: 290-340 ships
        - Split: Maersk 60%, Hapag-Lloyd 40%
        """)
    
    with col2:
        st.markdown("""
        **Characteristics:**
        - **NEWEST ALLIANCE** (launched February 2025)
        - **SMALLEST WEEKLY SAILINGS** among major groups
        - **HIGHEST RELIABILITY TARGET**: >90% (vs industry 60%)
        - **Hub-and-spoke model**: 12 global hubs + dedicated shuttles
        - **Fewer direct port calls**: Focus on controlled terminals
        - **Like-minded** carriers: reliability, decarbonisation, service quality
        
        **Innovative Network Design (57 Services):**
        - **26 mainline services**: Connect major trade lanes
        - **32 shuttle services**: Hub-to-port feedering
          - 14 Europe shuttles
          - 13 Asia shuttles
          - 4 Middle East shuttles
          - 1 Gulf of Mexico shuttle
        - **12 global hubs**: Key transshipment points
        
        **Coverage (7 Trade Lanes):**
        - Asia - North Europe (4 services)
        - Asia - Mediterranean (3 services)
        - Asia - Middle East (1 service)
        - India/Middle East - Europe (4 services)
        - Trans-Atlantic (5 services)
        - Trans-Pacific (USWC, USEC)
        
        **Phase-In:**
        - Launched: February 1, 2025
        - Transition: Feb-May 2025 (gradual rollout)
        - Fully operational: June 2025
        - **Red Sea**: Continuing Cape of Good Hope routing
        
        **Environmental Leadership:**
        - Maersk: Net-zero target 2040 (methanol-powered vessels)
        - Hapag-Lloyd: Net-zero target 2045
        - Most ambitious decarbonisation timelines in industry
        """)
    
    st.markdown("""
    <div class="info-box">
    <strong>💡 Gemini's Reliability Gambit:</strong><br>
    Gemini's >90% schedule reliability target is <strong>unprecedented</strong>. The industry average has been 
    ~60% since COVID-19 disruptions. Achieving this requires:<br>
    - Fewer port calls (reduces disruption points)<br>
    - Controlled terminals (own APM Terminals, Hapag-Lloyd facilities)<br>
    - Buffer time in schedules<br>
    - Simplified vessel operator structure (one operator per mainline service)<br>
    - Advanced IT systems and predictive planning<br><br>
    <strong>Early results (March 2025):</strong> Gemini achieving 80%+ reliability during phase-in, 
    significantly above market average but below 90% target. Full assessment due June 2025.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">3. MSC (20% Market Share - LARGEST SOLO OPERATOR)</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        **Status:** Independent (solo)
        
        **Formation:** Operating independently from Feb 1, 2025 
        (left 2M Alliance)
        
        **Capacity:**
        - Total: 7.1M TEU (November 2025)
        - Operational: 6.4M TEU
        - Vessels: 886-887 ships
        
        **Ranking:** World's largest container carrier
        
        **Market Share:** ~20%
        """)
    
    with col2:
        st.markdown("""
        **Characteristics:**
        - **WORLD'S LARGEST CARRIER** operating solo
        - **Unmatched scale**: 7.1M TEU (50% larger than #2 Maersk)
        - **Massive orderbook**: 2.2M TEU (130+ vessels) - largest in industry
        - **Aggressive growth**: Added 831,000 TEU in 2025 (5th consecutive year)
        - **Flexibility**: Can optimise network without alliance constraints
        - **Family-owned**: Aponte family (Swiss/Italian), private company
        
        **Standalone Network (34 Loops Across 5 East-West Trades):**
        - Asia - North Europe (7 services, matching Ocean Alliance)
        - Asia - Mediterranean
        - Asia - USWC
        - Asia - USEC
        - Trans-Atlantic
        
        **Strategy:**
        - **Maximum port coverage**: Direct calls to more ports vs Gemini
        - **Ultra-large vessels**: Average 13,200 TEU
        - **Volume focus**: Economies of scale through sheer size
        - **Rapid expansion**: Acquiring vessels aggressively (400+ ships in 5 years)
        - **Slot exchanges**: Maintain partnerships where beneficial
        
        **Partnerships:**
        - **ZIM**: Transpacific operational cooperation (6 services, launched Feb 2025)
        - **Premier Alliance**: Slot exchange on 9 Asia-Europe services
        - Maintains flexibility while leveraging partner networks
        
        **Environmental Approach:**
        - LNG-focused (vs Maersk/Evergreen methanol focus)
        - Scrubber installations (allows high-sulphur fuel use)
        - Less ambitious net-zero timeline than Gemini
        """)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ MSC's Solo Bet:</strong><br>
    MSC is the ONLY top-5 carrier operating without a full alliance. This is unprecedented but enabled by:<br>
    - <strong>Unmatched scale</strong>: 7.1M TEU = larger than many alliances<br>
    - <strong>Massive orderbook</strong>: 2.2M TEU on order (33% of current fleet)<br>
    - <strong>Owner-operated</strong>: No shareholder pressure, long-term view<br>
    - <strong>Cost advantage</strong>: Secondhand ship acquisitions at favourable prices<br><br>
    <strong>Risk</strong>: If overcapacity worsens in 2025-2026, MSC bears full exposure alone. 
    Alliances can share risk; MSC cannot.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">4. Premier Alliance (11% Market Share - SMALLEST)</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        **Members:**
        - ONE (Ocean Network Express) - Japan
        - HMM (Hyundai Merchant Marine) - South Korea
        - Yang Ming - Taiwan
        
        **Formation:** February 2025 
        (Rebranded from THE Alliance)
        
        **Duration:** 5-year agreement (2025-2030)
        
        **Capacity:**
        - Combined: 3.57-3.59M TEU
        - Operational: ~3.0M TEU
        - Vessels: ~250 ships
        """)
    
    with col2:
        st.markdown("""
        **Characteristics:**
        - **SMALLEST ALLIANCE** (lost Hapag-Lloyd to Gemini)
        - **Northeast Asian focus**: Japanese, Korean, Taiwanese carriers
        - **Capacity challenge**: Lost ~2M TEU when Hapag-Lloyd exited
        - **Survival mode**: Must prove viability with smaller scale
        - **Strategic dilemma**: Too small to compete alone, but who to add?
        
        **Network Focus:**
        - **East-West trades**: Asia - USWC, USEC, Europe, Med, Middle East
        - Strong trans-Pacific services (traditional strength)
        - Asia-Europe services
        - Intra-Asia feedering
        
        **Coping Strategies:**
        - **MSC slot exchange**: 9 Asia-Europe services (critical support)
        - **Vessel-sharing agreements**: Fill capacity gaps
        - **Newbuild deliveries**: ONE and HMM adding vessels 2024-2025
        - **Service optimisation**: Focus on core routes
        
        **Key Challenge:**
        - **Scale disadvantage**: 3.6M TEU vs Ocean 8.9M, Gemini 6.8M, MSC 7.1M
        - **Cost pressure**: Harder to negotiate with ports at smaller scale
        - **Competitive squeeze**: Between larger, more capable groups
        - **Uncertain future**: Can they attract a new member? Will they survive 5 years?
        
        **Possible Scenarios:**
        - Status quo: Operate as 3-member alliance
        - Expansion: Recruit new member (Zim? Wan Hai?)
        - Absorption: Members join other alliances
        - Reorganisation: Merge with independents
        """)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ Premier's Survival Question:</strong><br>
    Industry analysts question Premier Alliance's long-term viability:<br>
    - <strong>Scale gap</strong>: 3.6M TEU vs 6.8-8.9M TEU for larger alliances<br>
    - <strong>Market share</strong>: Just 11% limits negotiating power<br>
    - <strong>Cost disadvantage</strong>: Smaller scale = higher cost per TEU<br>
    - <strong>Competitive pressure</strong>: Squeezed by larger, more capable groups<br><br>
    <strong>Critical period</strong>: 2025-2026 will determine if Premier can thrive or must reorganise. 
    MSC's slot exchange support provides temporary relief but isn't a long-term solution.
    </div>
    """, unsafe_allow_html=True)
    
    # Comparison table
    st.markdown('<p class="subsection-header">Alliance Comparison (2025)</p>', unsafe_allow_html=True)
    
    comparison_table = pd.DataFrame({
        'Metric': [
            'Market Share',
            'Combined Capacity',
            'Operational Capacity',
            'Vessel Count',
            'Average Vessel Size',
            'Primary Strategy',
            'Port Coverage',
            'Reliability Target',
            'Environmental Target',
            'Competitive Advantage'
        ],
        'Ocean Alliance': [
            '29% (Largest)',
            '8.91M TEU',
            '3.8M TEU (~330 ships)',
            '~390 total',
            '~13,200 TEU',
            'Balanced: Coverage + Service',
            'Widest (multiple calls)',
            'Industry standard (~60%)',
            'Varied by member',
            'Scale, Asia strength, stability'
        ],
        'Gemini': [
            '21%',
            '6.75M TEU',
            '3.4M TEU (~290 ships)',
            '290-340 total',
            '~12,400 TEU',
            'Reliability over coverage',
            'Hub-and-spoke (12 hubs)',
            '>90% (unprecedented)',
            'Ambitious (2040/2045)',
            'Reliability, controlled terminals, quality'
        ],
        'MSC (Solo)': [
            '20%',
            '7.1M TEU',
            '6.4M TEU (~886 ships)',
            '886 total',
            '~13,200 TEU',
            'Maximum coverage, volume',
            'Direct calls, many ports',
            'Not disclosed',
            'LNG focus',
            'Scale, flexibility, growth capacity'
        ],
        'Premier': [
            '11% (Smallest)',
            '3.57M TEU',
            '~3.0M TEU (~250 ships)',
            '~250 total',
            '~11,900 TEU',
            'Focus on core East-West',
            'Strategic routes',
            'Industry standard',
            'Varied by member',
            'Northeast Asia expertise, agility'
        ]
    })
    
    st.dataframe(comparison_table, use_container_width=True, hide_index=True)
    
    # ============================================================================
    # SECTION 4: How Alliances Work
    # ============================================================================
    
    st.markdown('<p class="section-header">How Shipping Alliances Work</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Alliances are operational partnerships, not mergers. Understanding what they share (and don't share) 
    is crucial to understanding modern maritime operations.
    """)
    
    st.markdown('<p class="subsection-header">What Alliances Share vs Keep Independent</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Shared Resources (Cooperation):**
        
        **Vessel Space:**
        - Members contribute vessels to joint services
        - Share capacity on each other's vessels (slot charter)
        - Coordinate vessel deployments and schedules
        - Optimise utilisation across combined fleet
        - Example: Maersk vessel carries Hapag-Lloyd containers
        
        **Port Calls and Terminals:**
        - Coordinate port rotations (which ports, in what order)
        - Share terminal facilities (reducing costs)
        - Joint negotiations with ports for berth rates
        - Optimise port call sequences for efficiency
        - Shared handling equipment and labour
        
        **Operations and Planning:**
        - Shared vessel schedules and sailing frequencies
        - Coordinated service planning (which routes to operate)
        - Joint network optimisation (minimize empty repositioning)
        - Shared operational best practices
        - Coordinated capacity management (add/remove vessels together)
        
        **Why Share?**
        - **Economies of scale**: Fill vessels more fully
        - **Network reach**: Serve more ports together than alone
        - **Frequency**: Offer daily/multiple weekly sailings
        - **Cost reduction**: Share fixed port and operational costs
        """)
    
    with col2:
        st.markdown("""
        **Retained Independence (Competition):**
        
        **Pricing (MOST CRITICAL):**
        - **Each carrier sets own freight rates** (no price-fixing)
        - **Independent contract negotiations** with customers
        - **Compete on price within alliance** (undercutting partners is legal)
        - Rate decisions made separately, confidentially
        - NO sharing of customer pricing information
        
        **Sales and Marketing:**
        - **Own sales forces** and sales strategies
        - **Independent customer relationships** (own client base)
        - **Separate brand identities** (Maersk ≠ Hapag-Lloyd)
        - **Compete for same customers** (alliance partners are rivals)
        - Own marketing campaigns and value propositions
        
        **Digital and Logistics:**
        - **Separate digital platforms** (booking systems, tracking)
        - **Independent logistics operations** (trucking, warehousing, air freight)
        - **Own feeder networks** (connecting to alliance mainline)
        - **Individual competitive strategies** (Maersk's integrator strategy unique)
        
        **Why Separate?**
        - **Legal requirement**: Price-fixing is illegal (anti-trust)
        - **Competition law**: Alliances must compete on pricing
        - **Customer choice**: Shippers choose carrier within alliance
        - **Regulatory scrutiny**: Competition authorities monitor closely
        """)
    
    st.markdown("""
    **The Alliance Paradox:**
    
    Alliance members **COOPERATE** on vessel operations and network planning while **COMPETING** vigorously 
    on pricing and customer acquisition. This paradox allows them to:
    - Achieve economies of scale (shared vessels, better port terms, fuller utilisation)
    - Maintain competitive market dynamics (independent pricing prevents monopoly)
    - Offer comprehensive global networks (coordinated services reach more ports)
    - Preserve individual brands and customer relationships (maintain differentiation)
    
    **Example: Maersk and Hapag-Lloyd in Gemini**
    - **Cooperate**: Both put vessels on Asia-Europe route, share capacity
    - **Compete**: Customer booking Asia-Europe gets quotes from BOTH, who undercut each other
    - **Result**: Customer benefits from competitive pricing AND comprehensive service
    
    **Regulatory Balance:**
    - **Competition authorities ALLOW** operational cooperation (vessel sharing, joint services)
    - But **CLOSELY MONITOR** for price-fixing or anti-competitive behaviour
    - Alliances must demonstrate customer benefits (better service, lower costs, not higher prices)
    - Regular reporting to regulators (EU, US FMC, etc.)
    - Violations can result in massive fines and forced dissolution
    """)
    
    # Benefits visualization
    st.markdown('<p class="subsection-header">Why Alliances Exist: The Benefits</p>', unsafe_allow_html=True)
    
    alliance_benefits = pd.DataFrame({
        'Benefit': [
            'Network Coverage',
            'Service Frequency',
            'Vessel Utilisation',
            'Port Negotiation',
            'Operational Flexibility',
            'Risk Sharing',
            'Capital Efficiency'
        ],
        'Without Alliance': [
            'Carrier serves 50-100 ports alone',
            'Weekly service requires 6-8 vessels alone',
            '70-80% full (must absorb empty slots)',
            'Small carrier, weak negotiating position',
            'Limited - constrained by own fleet',
            'Full exposure to market volatility alone',
            'Must own full fleet for all routes'
        ],
        'With Alliance': [
            'Alliance serves 200+ ports collectively',
            'Daily service with 3-4 vessels per carrier',
            '85-90% full (partners fill empty slots)',
            'Large alliance, strong negotiating leverage',
            'Can swap capacity across partner routes',
            'Shared exposure - smoother revenue',
            'Share vessels, reduce capital needs'
        ],
        'Impact': [
            'More destinations served at lower cost',
            'Attractive to shippers (more sailing options)',
            '15-20% efficiency gain per vessel',
            '20-30% lower terminal costs',
            'Better adapt to demand fluctuations',
            'Lower earnings volatility',
            '30-40% less capital required per carrier'
        ]
    })
    
    st.dataframe(alliance_benefits, use_container_width=True, hide_index=True)
    
    st.markdown("""
    **Bottom Line:**
    Alliances enable carriers to offer better service at lower cost than operating alone, while still 
    competing on price. This benefits both carriers (lower costs) and shippers (more choice, competitive pricing).
    """)
    
    # ============================================================================
    # SECTION 5: Hub-and-Spoke Network Model
    # ============================================================================
    
    st.markdown('<p class="section-header">Hub-and-Spoke Network Model</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Modern container shipping operates primarily on a **hub-and-spoke model**, where large vessels connect 
    major hub ports, and smaller feeder vessels distribute cargo to regional ports. This model dominates 
    global maritime logistics.
    """)
    
    st.markdown('<p class="subsection-header">How Hub-and-Spoke Works</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **The Hub Port:**
        - **Major transshipment centre** handling massive volumes
        - **Deep water berths** (16+ metres) for mega vessels
        - **Large cranes** (65-80m outreach) for 24-wide vessels
        - **Extensive terminal capacity** (multiple berths, high throughput)
        - **Strategic location** on major trade routes
        - **Connects multiple trade lanes** (Asia-Europe, Trans-Pacific, etc.)
        
        **Examples of Major Hubs:**
        - **Singapore**: World's #1 transshipment hub (85% transshipment)
        - **Rotterdam**: Europe's gateway
        - **Dubai (Jebel Ali)**: Middle East hub
        - **Colombo**: Indian Ocean hub
        - **Los Angeles/Long Beach**: US West Coast gateway
        - **Shanghai**: Asia's largest port
        
        **Hub Functions:**
        - Receive mega vessels from multiple trade lanes
        - Transship containers to connecting services
        - Sort cargo by destination
        - Consolidate shipments for feeder distribution
        - Provide warehousing, customs, inspection services
        """)
    
    with col2:
        st.markdown("""
        **The Spoke (Feeder Service):**
        - **Smaller vessels** (500-3,000 TEU) connecting hub to regional ports
        - **More frequent calls** to smaller ports (weekly or multiple times weekly)
        - **Shallow draft** (10-12m) to access ports mega vessels cannot
        - **Regional distribution** from hub to secondary ports
        - **Flexible scheduling** to match local demand
        
        **Why Feeder Vessels?**
        - Small ports lack depth for mega vessels
        - Small ports lack cranes for mega vessels
        - Small ports have insufficient cargo volume for direct mega vessel call
        - More economical to hub-and-spoke than direct call
        - Provides connectivity without mega-vessel infrastructure
        
        **Example: Singapore as Hub**
        - **Mainline**: Shanghai → Singapore (mega vessel, 15,000+ containers)
        - **Transshipment**: Singapore sorts, consolidates cargo
        - **Feeder 1**: Singapore → Bangkok (feeder vessel, 500 containers)
        - **Feeder 2**: Singapore → Jakarta (feeder vessel, 800 containers)
        - **Feeder 3**: Singapore → Ho Chi Minh City (feeder vessel, 600 containers)
        - **Result**: 85% of cargo in Singapore transships to other destinations
        """)
    
    st.markdown("""
    **Economics of Hub-and-Spoke:**
    
    **For Shipping Lines:**
    - **Cost savings**: Mega vessels only call major hubs (fewer port calls, faster voyages)
    - **Efficiency**: High utilisation on mainline (concentrated cargo flows)
    - **Flexibility**: Feeder network adjusts to demand without changing mainline
    - **Scale**: Deploy 20,000 TEU vessels economically on high-volume routes
    
    **For Hub Ports:**
    - **Volume**: Handle cargo from multiple trade lanes (multiplier effect)
    - **Revenue**: Terminal fees from both mainline and feeder vessels
    - **Value-add services**: Transshipment, warehousing, customs, inspection
    - **Strategic importance**: Become critical nodes in global supply chain
    
    **For Shippers:**
    - **Connectivity**: Access to 200+ ports via hub connections
    - **Frequency**: More sailing options through hub consolidation
    - **Trade-off**: Longer transit time (hub transshipment adds 3-7 days)
    - **Cost**: Lower freight rates (economies of scale on mainline offset feeder cost)
    
    **Alternative: Point-to-Point Service**
    - Direct service (no transshipment at hub)
    - Faster transit time BUT requires sufficient cargo volume
    - Only economical on high-volume trade lanes
    - Most cargo globally (85%+) goes via hub-and-spoke, not point-to-point
    """)
    
    st.markdown('<p class="subsection-header">Singapore: The World's Premier Hub</p>', unsafe_allow_html=True)
    
    # Singapore statistics
    singapore_stats = pd.DataFrame({
        'Metric': [
            'Container Throughput (2024)',
            'Transshipment Percentage',
            'Shipping Lines Calling',
            'Ports Connected',
            'Vessel Calls per Year',
            'Weekly Container Services',
            'Average Vessel Size',
            'Geographic Advantage'
        ],
        'Value': [
            '39.9 million TEU (world #2 after Shanghai)',
            '85% (highest among major ports)',
            '200+ shipping lines',
            '600+ ports in 120+ countries',
            '140,000+ vessel calls',
            '1,000+ weekly services',
            '8,000-12,000 TEU average',
            'On major trade routes: Asia-Europe, Intra-Asia, Trans-Pacific'
        ],
        'Significance': [
            'Massive volume enables scale economies',
            'Pure transshipment hub (not destination)',
            'Comprehensive carrier coverage',
            'Global connectivity unmatched',
            'Highest port efficiency (quick turnaround)',
            'Frequent sailings (shipper choice)',
            'Accommodates large and small vessels',
            'Natural chokepoint (Malacca Strait) and central location'
        ]
    })
    
    st.dataframe(singapore_stats, use_container_width=True, hide_index=True)
    
    st.markdown("""
    **Why Singapore Dominates as Hub:**
    
    **Geographic Location:**
    - **Malacca Strait**: Natural chokepoint for Asia-Europe trade (40% of world trade)
    - **Central position**: Equidistant from China, India, Southeast Asia, Australia
    - **On major trade routes**: All Asia-Europe and many Trans-Pacific services pass through
    - **Deep water**: Natural harbour with 20m+ depth (handles mega vessels)
    
    **Infrastructure Excellence:**
    - **World-class terminals**: PSA, Jurong Port (high efficiency, low costs)
    - **Advanced technology**: Automated cranes, AI-optimised operations
    - **Massive capacity**: Can handle 50+ million TEU (room to grow)
    - **Quick turnaround**: Vessels in/out in 10-16 hours (vs 24-48 hours elsewhere)
    
    **Business Environment:**
    - **Free trade port**: No tariffs on transshipment cargo
    - **Efficient customs**: Fast clearance, minimal bureaucracy
    - **Stable government**: Predictable regulations, strong rule of law
    - **Skilled workforce**: Maritime expertise, multilingual staff
    - **24/7 operations**: No labour strikes, consistent service
    
    **Network Effects:**
    - **200+ lines**: All major carriers call Singapore
    - **600+ ports connected**: Go anywhere from Singapore
    - **1,000+ services**: Frequent departures (shipper convenience)
    - **Self-reinforcing**: More carriers attract more cargo, which attracts more carriers
    
    **Result:**
    Singapore is **THE** global transshipment hub. 85% of its cargo transships (arrives on one vessel, 
    departs on another). This is by design - Singapore optimised for hub-and-spoke model.
    """)
    
    st.markdown("""
    <div class="info-box">
    <strong>💡 Gemini's Hub-and-Spoke Strategy:</strong><br>
    Gemini Cooperation (Maersk + Hapag-Lloyd) took hub-and-spoke to the extreme with their 2025 network design:<br>
    - <strong>12 global hubs</strong>: Carefully selected strategic locations<br>
    - <strong>26 mainline services</strong>: Mega vessels connect ONLY the 12 hubs<br>
    - <strong>32 dedicated shuttles</strong>: Feeder vessels distribute from hubs to 100+ ports<br>
    - <strong>Rationale</strong>: Fewer port calls = higher reliability (90% target vs 60% industry)<br>
    - <strong>Trade-off</strong>: Less direct port coverage but much better schedule integrity<br><br>
    <strong>Contrast with MSC</strong>: MSC's standalone network emphasizes direct port calls (maximum coverage), 
    while Gemini prioritizes reliability through hub concentration. Two opposite strategies competing in 2025.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 6: Major Trade Routes
    # ============================================================================
    
    st.markdown('<p class="section-header">Major Global Trade Routes</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Container shipping operates on well-established trade routes connecting major economic regions. 
    Understanding these routes is essential to understanding global trade flows and alliance strategies.
    """)
    
    # Trade routes data
    trade_routes = pd.DataFrame({
        'Trade Route': [
            'Intra-Asia',
            'Asia - North Europe',
            'Trans-Pacific (Asia-USWC)',
            'Trans-Pacific (Asia-USEC)',
            'Asia - Mediterranean',
            'Trans-Atlantic',
            'Asia - Middle East',
            'North-South (multiple)'
        ],
        'Annual Volume (TEU)': [
            '~35 million',
            '~24 million',
            '~16 million',
            '~10 million',
            '~10 million',
            '~7 million',
            '~8 million',
            '~15 million (combined)'
        ],
        'Transit Time': [
            '3-7 days',
            '30-35 days (Suez) / 40-45 days (Cape)',
            '12-16 days',
            '21-28 days (Panama) / 25-35 days (Suez)',
            '25-30 days',
            '10-14 days',
            '15-20 days',
            'Varies (10-25 days)'
        ],
        'Key Characteristics': [
            'Highest volume, shortest distance, frequent service',
            'Longest route, largest vessels (20,000+ TEU), Red Sea disruptions 2024-2025',
            'High-value cargo, fast transit, largest US trade',
            'Panama Canal or Suez via Asia-Europe, longer but more capacity',
            'Growing trade, similar to Asia-Europe but shorter',
            'Balanced trade (Europe-US exports/imports), moderate volumes',
            'Oil-related, strong growth, strategic importance',
            'Emerging markets, Europe/Asia to Africa/South America/Oceania'
        ],
        'Alliance Competition': [
            'All groups compete, regional carriers strong',
            'Ocean Alliance + MSC dominant (7 services each)',
            'Ocean Alliance leader (15 weekly sailings)',
            'Balanced across all groups',
            'Ocean + Gemini + MSC compete',
            'Gemini strong (5 services), Ocean slot exchange',
            'All groups present, growing focus',
            'Mix of mainline and regional services'
        ]
    })
    
    st.dataframe(trade_routes, use_container_width=True, hide_index=True)
    
    st.markdown('<p class="subsection-header">Trade Route Deep Dive: Asia-Europe</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The Asia-Europe trade route is the world's most important container shipping route by vessel size and 
    strategic significance.
    
    **Route:**
    - **Origin**: East Asia (China, South Korea, Japan, Taiwan, Hong Kong)
    - **Via**: Southeast Asia → Malacca Strait → (Suez Canal OR Cape of Good Hope) → Mediterranean/North Europe
    - **Destination**: Mediterranean (Italy, Spain, Egypt, Turkey), North Europe (Rotterdam, Hamburg, Antwerp, Felixstowe/London Gateway)
    
    **Statistics:**
    - **Volume**: ~24 million TEU annually (eastbound + westbound combined)
    - **Direction imbalance**: Westbound (Asia→Europe) ~60%, Eastbound (Europe→Asia) ~40%
    - **Transit time**: 30-35 days via Suez, 40-45 days via Cape of Good Hope
    - **Vessel size**: LARGEST vessels (20,000-24,000 TEU) deployed here
    
    **2024-2025 Red Sea Disruption:**
    - **Crisis**: Red Sea security issues (late 2023-present) forced rerouting
    - **Impact**: Mega vessels (18,000+ TEU) avoided Suez for 20+ consecutive months
    - **Alternative**: Cape of Good Hope (+3,500 nautical miles, +7-10 days, +$500K-800K fuel)
    - **Consequence**: Global emissions +5% in 2024, freight rate volatility, service delays
    - **2025 status**: Gemini explicitly continuing Cape routing; others case-by-case
    
    **Alliance Deployment (2025):**
    - **Ocean Alliance**: 7 services to North Europe (widest coverage)
    - **MSC (solo)**: 7 services (matching Ocean)
    - **Gemini**: 4 services North Europe + 3 Mediterranean (hub-focused)
    - **Premier**: Multiple services + MSC slot exchange on 9 services (critical support)
    
    **Port Changes (2025 Reshuffling):**
    - **Singapore**: +6 weekly calls Asia-Europe (beneficiary of reshuffling)
    - **Antwerp**: -4 weekly calls (lost Gemini services)
    - **Felixstowe**: Dropped by Gemini (switched to London Gateway)
    - **Rotterdam**: Maintained as key hub
    
    **Why Asia-Europe Matters:**
    - **Largest vessels**: Only route with economies of scale for 20,000+ TEU deployment
    - **Alliance battlefield**: All major groups compete intensely here
    - **Strategic importance**: Connects world's two largest economic blocs
    - **Bellwether route**: Freight rates here signal global market conditions
    """)
    
    # ============================================================================
    # SECTION 7: Geopolitics and Trade Shifts
    # ============================================================================
    
    st.markdown('<p class="section-header">Geopolitics Reshaping Global Trade</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Geopolitical tensions, particularly US-China relations, are fundamentally reshaping container shipping 
    patterns. The "China+1" strategy and supply chain diversification are creating new trade flows and 
    challenging established hub dominance.
    """)
    
    st.markdown('<p class="subsection-header">US-China Trade Tensions</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Tension:**
    - **Trade war** (2018-present): Tariffs, sanctions, export controls
    - **Tech restrictions**: US limits on semiconductor exports to China
    - **Port fees**: Proposed US fees on Chinese-built vessels (2025)
    - **Decoupling rhetoric**: Political pressure to reduce China dependence
    - **Supply chain security**: Concerns about over-reliance on Chinese manufacturing
    
    **Impact on Shipping:**
    - **Trade volume volatility**: US-China trade fluctuates with policy changes
    - **Tariff-driven shifts**: Companies relocate production to avoid tariffs
    - **Fleet deployment challenges**: Carriers uncertain about future volumes
    - **Rate uncertainty**: Freight rates spike with policy announcements
    
    **Carrier Exposure:**
    - **COSCO/OOCL**: Highest exposure (Chinese carriers, Chinese-built fleet)
    - **CMA CGM**: Significant exposure (many Chinese-built vessels)
    - **MSC/Maersk**: Lower exposure (diverse fleet sources, less Chinese-built)
    - **Strategy**: Carriers redeploying Chinese-built vessels away from US routes
    """)
    
    st.markdown('<p class="subsection-header">"China+1" and Manufacturing Diversification</p>', unsafe_allow_html=True)
    
    # China+1 growth data
    intermediary_growth = pd.DataFrame({
        'Country': ['Vietnam', 'Malaysia', 'Thailand', 'Indonesia', 'Bangladesh', 'Mexico', 'India'],
        'Export Growth 2019-2024 (%)': ['+80%', '+45%', '+35%', '+40%', '+60%', '+55%', '+50%'],
        'Key Industries': [
            'Electronics, textiles, furniture',
            'Electronics, semiconductors, E&E',
            'Auto parts, electronics, food processing',
            'Textiles, electronics, commodities',
            'Garments, textiles',
            'Auto, electronics (nearshoring to US)',
            'Pharmaceuticals, textiles, IT services'
        ],
        'Port Investment': [
            'Expanding Cai Mep, Hai Phong',
            'Port Klang expansion, Tanjung Pelepas',
            'Laem Chabang expansion',
            'Tanjung Priok expansion',
            'Chittagong expansion',
            'Pacific coast ports expansion',
            'JNPT, Mundra expansion'
        ],
        'Impact on Singapore': [
            'Increased feeder traffic',
            'Competition + cooperation (nearby hub)',
            'Increased feeder traffic',
            'Increased feeder traffic',
            'Alternative hub (Colombo)',
            'Reduces Asia-US via Singapore',
            'Alternative hub (own ports)'
        ]
    })
    
    st.dataframe(intermediary_growth, use_container_width=True, hide_index=True)
    
    st.markdown("""
    **"China+1" Strategy Explained:**
    - **Definition**: Companies maintain China production BUT add secondary manufacturing base
    - **Goal**: Diversify supply chain risk, avoid tariffs, reduce geopolitical exposure
    - **NOT "China exit"**: China remains critical, but no longer sole source
    - **Timeline**: Accelerated 2018-present (trade war), further accelerated by COVID-19
    
    **Winners: Intermediate Countries**
    - **Southeast Asia**: Vietnam (+80%), Malaysia (+45%), Thailand (+35%), Indonesia (+40%)
    - **South Asia**: Bangladesh (+60%), India (+50%)
    - **Latin America**: Mexico (+55%, nearshoring to US)
    - **Characteristics**: Lower labour costs, political stability, improving infrastructure
    
    **Impact on Shipping:**
    - **New trade lanes**: Growing volumes to/from intermediate countries
    - **Hub shifts**: Vietnam, Malaysia, India becoming import/export hubs (not just transshipment)
    - **Feeder growth**: More feeder services connecting intermediate countries to major hubs
    - **Alliance strategies**: Must adapt networks to new trade patterns
    
    **Impact on Singapore:**
    - **Positive**: More feeder traffic (intermediate countries → Singapore → global mainline)
    - **Negative**: Some direct services bypass Singapore (e.g., Vietnam → US direct)
    - **Adaptation needed**: Maintain relevance as trade patterns shift
    """)
    
    st.markdown('<p class="subsection-header">Emerging Alternative Routes and Long-Term Threats</p>', unsafe_allow_html=True)
    
    # Alternative routes
    alternative_routes = pd.DataFrame({
        'Alternative Route/Development': [
            'Arctic Route (Northern Sea Route)',
            'Thailand Kra Canal (proposed)',
            'China-Europe Rail (Belt & Road)',
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
            'Competes for China-Europe high-value cargo (limited capacity, ~5% of maritime volume)',
            'Creates alternative trade corridors (road/rail), reduces reliance on sea routes',
            'Handles larger vessels, speeds Asia-Europe transit (benefits Singapore)',
            'Allows New-Panamax vessels (14,500 TEU) on Trans-Pacific routes'
        ],
        'Likelihood/Timeline': [
            'Climate-dependent, 2030s-2040s possible as Arctic warms',
            'Low likelihood (<10%), decades away if ever (environmental, political obstacles)',
            'Niche role (high-value, time-sensitive only), limited growth potential',
            'Gradual development over decades, uneven success',
            'Already implemented (2015)',
            'Already implemented (2016)'
        ],
        'Singapore Impact': [
            'Moderate threat if Arctic becomes viable (diverts some Asia-Europe traffic)',
            'Existential threat if built (would bypass Malacca/Singapore entirely)',
            'Minimal (rail cannot match maritime volume or cost)',
            'Indirect (shifts some trade to land corridors)',
            'Positive (larger vessels use Singapore as hub)',
            'Neutral (different route, Singapore not affected)'
        ]
    })
    
    st.dataframe(alternative_routes, use_container_width=True, hide_index=True)
    
    st.markdown("""
    **Key Threats to Traditional Routes:**
    
    **Arctic Route (Northern Sea Route):**
    - **Potential**: Shorten Asia-Europe by ~40% (vs Suez), save 10-15 days transit
    - **Current limitation**: Ice-free only 3-4 months/year, requires icebreaker escorts
    - **Climate change**: Arctic warming could extend ice-free period
    - **Timeline**: Potentially viable 2030s-2040s if current warming trends continue
    - **Impact**: If viable year-round, could divert 20-30% of Asia-Europe traffic from Suez/Singapore
    - **Singapore risk**: Moderate (would bypass Malacca Strait)
    
    **Kra Canal (Thailand):**
    - **Proposal**: Cut canal across Thai peninsula, bypass Malacca Strait
    - **Distance saved**: ~1,200 km (~2-3 days sailing)
    - **Cost**: Estimated $20-30 billion (massive infrastructure project)
    - **Challenges**: Environmental concerns, political obstacles, financing uncertainty, Thai government skepticism
    - **Likelihood**: Very low (<10% chance of being built)
    - **Singapore impact**: EXISTENTIAL THREAT if built (but unlikely)
    
    **China-Europe Rail (Belt & Road):**
    - **Current**: Operational, ~5,000-8,000 containers/day capacity
    - **Transit time**: 14-18 days (vs 30-35 days maritime)
    - **Cost**: 2-3× maritime freight rates
    - **Use case**: High-value, time-sensitive cargo (electronics, auto parts)
    - **Limitation**: Cannot match maritime volume (rail ~1% of maritime TEU)
    - **Singapore impact**: Minimal (different market segment)
    
    **Bottom Line:**
    Traditional maritime routes (Suez, Malacca, Panama) remain dominant. Alternative routes are niche 
    or distant threats. Singapore's position is secure medium-term (10-20 years) but must monitor Arctic 
    and continue infrastructure investment (Tuas Port) to maintain long-term competitiveness.
    """)
    
    # ============================================================================
    # SECTION 8: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Industry Consolidation:**
        - 15+ carriers (2000) → 9 major players (2025)
        - ~80% controlled by 4 groups (3 alliances + MSC solo)
        - Overcapacity crisis (2015-2016) forced mergers and cooperation
        - Further consolidation possible (Premier Alliance vulnerable)
        
        **The 2025 Reshuffling (February 1):**
        - **2M Alliance DISSOLVED** (MSC + Maersk ended after 10 years)
        - **Gemini Cooperation FORMED** (Maersk + Hapag-Lloyd, NEW)
        - **Premier Alliance FORMED** (THE rebranded, lost Hapag-Lloyd)
        - **MSC INDEPENDENT** (world's largest carrier operating solo)
        - Biggest alliance reorganisation in a decade
        
        **Current Alliance Structure:**
        - **Ocean**: CMA CGM + COSCO + OOCL + Evergreen (29%, LARGEST)
        - **Gemini**: Maersk + Hapag-Lloyd (21%, NEWEST, 90% reliability target)
        - **MSC**: Solo (20%, LARGEST CARRIER, 7.1M TEU)
        - **Premier**: ONE + HMM + Yang Ming (11%, SMALLEST, survival challenge)
        """)
    
    with col2:
        st.markdown("""
        **Hub-and-Spoke Dominance:**
        - 85% of cargo transships at hubs (not point-to-point)
        - **Singapore**: World's premier hub (85% transshipment, 200+ lines, 600+ ports)
        - **Mega vessels** connect hubs, **feeder vessels** distribute to regional ports
        - **Gemini's extreme**: 12 hubs + 32 shuttles (reliability over coverage)
        
        **Major Trade Routes:**
        - **Intra-Asia**: Highest volume (~35M TEU)
        - **Asia-Europe**: Longest route, largest vessels (24M TEU, 30-45 days)
        - **Trans-Pacific**: High-value cargo (26M TEU combined USWC+USEC)
        - **Red Sea disruption** (2024-2025): Mega vessels via Cape (+7-10 days, +$500K-800K)
        
        **Geopolitics Reshaping Trade:**
        - **US-China tensions**: Tariffs, sanctions, decoupling rhetoric
        - **"China+1"**: Vietnam +80%, Malaysia +45%, Mexico +55% exports (2019-2024)
        - **Intermediate countries**: Benefiting from supply chain diversification
        - **Alternative routes**: Arctic (long-term), Kra Canal (unlikely), China-Europe rail (niche)
        
        **Singapore's Challenge:**
        - Maintain hub dominance amid changing trade patterns
        - Adapt to "China+1" (opportunity + threat)
        - **Tuas Port**: Massive investment to stay ahead
        - **Competition**: Malaysia, Vietnam, India growing
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> The container shipping industry underwent its biggest restructuring in 
    a decade on February 1, 2025. The 2M Alliance (MSC + Maersk, 34% market share) dissolved after 10 years. 
    Maersk formed the new <strong>Gemini Cooperation</strong> with Hapag-Lloyd (21%, targeting unprecedented 
    >90% reliability). MSC now operates <strong>independently</strong> as the world's largest carrier (7.1M TEU, 
    20%). THE Alliance lost Hapag-Lloyd and rebranded as <strong>Premier Alliance</strong> (ONE + HMM + Yang Ming, 
    11%, smallest). The <strong>Ocean Alliance</strong> (CMA CGM + COSCO + OOCL + Evergreen, 29%) remained 
    unchanged and became the largest alliance.
    <br><br>
    Modern shipping operates on a <strong>hub-and-spoke model</strong>, with Singapore as the world's premier 
    transshipment hub (85% transshipment, 200+ lines, 600+ ports connected, 39.9M TEU throughput). Gemini took 
    this model to the extreme with 12 global hubs and 32 dedicated shuttles, prioritizing reliability over 
    coverage. Meanwhile, <strong>geopolitical tensions</strong> (US-China trade war) and <strong>"China+1" 
    diversification</strong> are reshaping trade patterns, with intermediate countries (Vietnam +80%, Malaysia 
    +45%) experiencing rapid export growth 2019-2024.
    <br><br>
    <strong>2025-2026 Outlook:</strong> Watch (1) Can Gemini achieve 90% reliability? (2) Can Premier Alliance 
    survive at just 11% market share? (3) Does MSC's solo bet pay off amid potential overcapacity? (4) When 
    will mega vessels return to Suez Canal (Red Sea security)? The next 12-24 months will determine if 2025's 
    massive reshuffling was successful or requires further reorganisation.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** 🇸🇬 Maritime Singapore Ecosystem - Explore Singapore's comprehensive maritime cluster, 
    MPA's dual role as regulator and developer, the Tuas Port mega-project, and the innovation ecosystem 
    driving maritime technology forward in Singapore's quest to remain the world's premier maritime hub.
    """)
