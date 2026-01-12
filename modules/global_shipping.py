import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">🌍 Global Shipping & Alliances</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand the dramatic industry consolidation from 15+ independent carriers to just 9 major players 
    organised into alliances, comprehend the February 2025 alliance restructuring (dissolution of 2M Alliance, 
    formation of Gemini Cooperation and Premier Alliance), master the hub-and-spoke network model with Singapore 
    as the world's premier transshipment hub (85% transshipment cargo), and grasp how geopolitics is reshaping 
    global trade patterns through "China+1" diversification strategies.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Industry Consolidation - From Fragmentation to Concentration
    # ============================================================================
    
    st.markdown('<p class="section-header">Industry Consolidation: From Many to Few</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The container shipping industry has undergone one of the most dramatic consolidation waves in modern commerce. 
    What was once a highly fragmented industry with dozens of independent carriers competing globally has transformed 
    into an oligopoly dominated by just **nine major players** organised into strategic alliances that now control 
    **83% of global container capacity**. Understanding this consolidation journey is essential to comprehending 
    today's maritime power structure and competitive dynamics.
    """)
    
    st.markdown('<p class="subsection-header">The Consolidation Journey: Two Decades of Transformation</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Year 2000", "15+ Major Carriers", delta="Fragmented competition", help="Independent carriers competing globally")
    with col2:
        st.metric("Year 2025", "9 Major Players", delta="-6 carriers through M&A", help="After mergers, acquisitions, and bankruptcies")
    with col3:
        st.metric("Alliance Control", "83%", delta="Oligopoly power", help="Three alliance structures control 83% of global capacity")
    
    st.markdown("""
    **The Consolidation Timeline:**
    
    **Phase 1: Fragmented Competition (1990s-2000s)**
    
    At the turn of the millennium, the container shipping industry was highly competitive and fragmented:
    
    - **15+ major global carriers** competing independently across international routes
    - Dozens of **regional carriers** dominating specific trade lanes (intra-Asia, Mediterranean, etc.)
    - **Minimal cooperation** beyond occasional vessel sharing agreements
    - **Intense price competition** driving down freight rates
    - **Low barriers to entry**: Relatively easy for new entrants to charter vessels and compete
    - **Capacity disciplined**: Carriers matched capacity to demand, avoiding chronic overcapacity
    
    This era was characterised by healthy competition, stable margins, and relatively predictable market dynamics. 
    However, the seeds of change were already planted—the race to build ever-larger vessels was beginning, setting 
    the stage for the overcapacity crisis that would force consolidation.
    
    **Phase 2: The Merger Wave Begins (2005-2016)**
    
    The 2000s saw the beginning of consolidation through mergers and acquisitions:
    
    - **2005**: P&O Nedlloyd acquired by **Maersk** ($3.3 billion deal)
      - Created the undisputed global leader
      - Combined fleet exceeded 2 million TEU
      - Demonstrated that scale advantages were compelling
    
    - **2014-2017**: **Hamburg Süd** acquired by Maersk (completed 2017, $4 billion)
      - Strengthened Maersk's Latin America presence
      - Added 600,000 TEU capacity
      - Consolidated North-South trades
    
    - **2016**: **APL** (American President Lines) acquired by **CMA CGM** ($2.4 billion)
      - Gave CMA CGM strong US flag presence
      - Enhanced trans-Pacific services
      - Combined became #3 global carrier
    
    - **2016**: **Hanjin Shipping bankruptcy** - A watershed moment
      - World's 7th largest carrier collapsed
      - Left 500,000 TEU of cargo stranded at sea
      - 97 vessels arrested worldwide
      - Demonstrated that scale was now survival necessity
      - "Get big or get out" became industry mantra
    
    - **2017**: **OOCL** acquired by **COSCO** ($6.3 billion)
      - Created Chinese mega-carrier
      - Combined capacity ~3 million TEU
      - Gave Chinese state-owned enterprise global reach
    
    - **2018**: Three **Japanese carriers merge** into ONE (Ocean Network Express)
      - **NYK, MOL, and K Line** combined container operations
      - Created 7th largest carrier globally
      - Response to inability to compete individually
      - Kept cruise and bulk operations separate
    
    **Phase 3: Alliance Dominance and Ongoing Consolidation (2017-Present)**
    
    By 2017, the industry had consolidated into a new structure dominated by three mega-alliances. Then in 
    **February 2025**, a dramatic restructuring occurred:
    
    - **Three alliance structures** now control **83% of global container capacity**
    - Only **9 major carriers** remain as significant global players
    - **Alliance cooperation** on operations whilst maintaining **pricing competition**
    - **Further consolidation expected**: Smaller independent carriers face existential pressure
    - **Regulatory scrutiny increasing**: Competition authorities monitoring for anti-competitive behaviour
    
    The lecture materials explicitly state: **"Consolidations & Alliances in the industry – from 15 to 9 main 
    players; carrying 83% of shipping volumes."** This concentration represents one of the most dramatic 
    industry consolidations in modern economic history.
    """)
    
    # Enhanced consolidation data
    consolidation_data = pd.DataFrame({
        'Year': [2000, 2005, 2010, 2015, 2017, 2020, 2025],
        'Number of Major Carriers': [17, 15, 15, 15, 12, 10, 9],
        'Top 3 Market Share (%)': [28, 32, 35, 39, 42, 48, 54],
        'Alliance Control (%)': [0, 15, 35, 60, 75, 82, 83]
    })
    
    # Create side-by-side evolution charts
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(
            x=consolidation_data['Year'],
            y=consolidation_data['Alliance Control (%)'],
            mode='lines+markers',
            fill='tozeroy',
            line=dict(color='#3B82F6', width=4),
            marker=dict(size=12, color='#2563EB', line=dict(color='white', width=2)),
            name='Alliance Control'
        ))
        fig1.update_layout(
            title={
                'text': 'Alliance Control Growth<br>(0% → 83% in 25 years)',
                'x': 0.5,
                'xanchor': 'center'
            },
            xaxis_title="Year",
            yaxis_title="Alliance Control (%)",
            height=380,
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
            line=dict(color='#EF4444', width=4),
            marker=dict(size=12, color='#DC2626', line=dict(color='white', width=2)),
            name='Major Carriers'
        ))
        fig2.update_layout(
            title={
                'text': 'Major Players Declining<br>(17 → 9 carriers)',
                'x': 0.5,
                'xanchor': 'center'
            },
            xaxis_title="Year",
            yaxis_title="Number of Major Carriers",
            height=380,
            plot_bgcolor='white',
            yaxis=dict(gridcolor='#E5E7EB', range=[0, 20]),
            xaxis=dict(gridcolor='#E5E7EB')
        )
        st.plotly_chart(fig2, width='stretch')
    
    st.markdown("""
    **Why Consolidation Happened: The Perfect Storm**
    
    **Root Cause: The Chronic Overcapacity Crisis**
    
    The fundamental driver of consolidation was a massive overcapacity crisis that plagued the industry for over 
    a decade:
    
    - **Vessel ordering spree (2005-2015)**: Carriers ordered hundreds of mega vessels during boom years
    - **Construction lag**: Vessels ordered in 2010-2012 delivered in 2014-2016, after demand had cooled
    - **Supply exceeded demand**: Global container capacity grew 8-10% annually whilst demand grew only 3-5%
    - **Freight rate collapse**: Average rates fell 60-70% from 2010 peaks to 2016 lows
    - **Industry-wide losses**: 2015-2016 saw carriers collectively lose billions of dollars
    - **Hanjin bankruptcy**: The collapse of world's 7th largest carrier shocked the industry into action
    
    **Economic Imperative: Economies of Scale**
    
    Larger scale provides compelling cost advantages:
    
    - **Purchasing power**: Mega carriers negotiate 20-30% better prices with ports, suppliers, fuel providers
    - **Fixed cost spreading**: IT systems, management, marketing costs spread over larger volumes
    - **Network effects**: Larger networks attract more customers (virtuous cycle)
    - **Bargaining power**: Can demand favourable terminal lease terms, priority berth access
    - **Survival threshold**: Below 2-3% global market share, carriers cannot compete profitably
    
    **The Survival Imperative: "Get Big or Get Out"**
    
    Small and mid-sized carriers faced an impossible situation:
    
    - **Cannot match mega-carrier costs**: Structural cost disadvantage of 15-25% per TEU
    - **Cannot afford mega vessels**: $150-200M per ULCS requires enormous capital
    - **Cannot maintain global networks**: Need minimum scale to serve all major trade lanes
    - **Caught in vicious cycle**: Low volumes → high unit costs → customer defections → lower volumes
    
    **Strategic responses**:
    - **Merge or acquire**: Combine to reach minimum efficient scale
    - **Join alliance**: Share vessels with partners to gain network coverage
    - **Exit the market**: Bankruptcy (Hanjin) or sell to larger carrier (OOCL sold to COSCO)
    
    The result: "Get big or get out" became the industry mantra. Mid-sized carriers had no viable independent future.
    """)
    
    # ============================================================================
    # SECTION 2: The Alliance Restructuring of February 2025
    # ============================================================================
    
    st.markdown('<p class="section-header">February 2025: The Great Alliance Restructuring</p>', unsafe_allow_html=True)
    
    st.markdown("""
    In **February 2025**, the global shipping alliance landscape underwent its most dramatic transformation since 
    alliances were first formed. The 2M Alliance—which had dominated global shipping for a decade—dissolved, 
    triggering a complete reorganisation of carrier partnerships. Understanding this restructuring is essential 
    for anyone involved in maritime logistics, as it fundamentally changes how global container shipping operates.
    """)
    
    st.markdown("""
    <div class="warning-box">
    <strong>🔄 CRITICAL UPDATE: February 2025 Alliance Restructuring</strong><br><br>
    The alliance structure described in most 2024 materials is now <strong>outdated</strong>. As of February 2025, 
    the industry has completely reorganised:<br><br>
    <strong>DISSOLVED:</strong> 2M Alliance (MSC + Maersk) - Ended after 10 years<br>
    <strong>DISSOLVED:</strong> THE Alliance name - Rebranded as Premier Alliance<br><br>
    <strong>NEW:</strong> Gemini Cooperation (Maersk + Hapag-Lloyd) - Launched February 2025<br>
    <strong>NEW:</strong> Premier Alliance (ONE + HMM + Yang Ming) - Rebranded from THE Alliance<br>
    <strong>CHANGED:</strong> MSC now operates independently with selective cooperation<br>
    <strong>UNCHANGED:</strong> Ocean Alliance continues (CMA CGM + COSCO + OOCL + Evergreen)
    </div>
    """, unsafe_allow_html=True)
    
    # Updated alliance data reflecting February 2025 changes
    alliance_data_2025 = pd.DataFrame({
        'Alliance/Carrier': ['Gemini Cooperation', 'Ocean Alliance', 'Premier Alliance', 'MSC (Independent)', 'Other Independents'],
        'Members': [
            'Maersk, Hapag-Lloyd',
            'CMA CGM, COSCO, OOCL, Evergreen',
            'ONE, HMM, Yang Ming',
            'MSC (cooperates with Premier on Asia-Europe)',
            'ZIM, regional carriers'
        ],
        'Est. Market Share (%)': [25, 30, 17, 20, 8],
        'Est. Fleet Capacity (M TEU)': [3.4, 3.7, 2.3, 2.5, 1.0],
        'Formation/Status': ['Feb 2025 (New)', 'Continues from 2017', 'Feb 2025 (Rebranded)', 'Feb 2025 (Independent)', 'Various']
    })
    
    st.dataframe(alliance_data_2025, width='stretch', hide_index=True)
    
    st.markdown('<p class="subsection-header">1. Gemini Cooperation (Est. ~25% Market Share)</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        **Members:**
        - **Maersk** (Denmark)
        - **Hapag-Lloyd** (Germany)
        
        **Formation:** February 2025
        
        **Fleet:**
        - ~290 vessels
        - ~3.4M TEU capacity
        
        **Strategic Focus:**
        - Hub-and-spoke model
        - Schedule reliability (target >90%)
        - Integrated logistics
        """)
    
    with col2:
        st.markdown("""
        **The New Partnership:**
        
        **Background**: Maersk exited the 2M Alliance with MSC and Hapag-Lloyd left THE Alliance to form this 
        new partnership. This represents a fundamental strategic shift for both companies.
        
        **Strategic Rationale:**
        - **Maersk's evolution**: Shifting from pure carrier to integrated logistics provider (end-to-end supply chain)
        - **Hapag-Lloyd's positioning**: Seeking reliable partner after THE Alliance dissolution
        - **Complementary strengths**: Maersk's global brand and digital capabilities + Hapag-Lloyd's operational efficiency
        - **Divergence from MSC**: Maersk pursuing different business model than MSC's pure-carrier, volume-growth strategy
        
        **Network Design: Hub-and-Spoke Focus**
        
        Unlike traditional alliance models, Gemini emphasises a hub-and-spoke approach:
        - Consolidate cargo at major hub ports (Singapore, Rotterdam, New York)
        - Use feeder vessels for final distribution to smaller ports
        - Reduces port congestion and improves schedule integrity
        - Requires efficient terminal coordination
        
        **Key Trade Routes:**
        - Asia-Europe (via Suez Canal when accessible, Cape of Good Hope alternative)
        - Trans-Pacific (Asia-North America West Coast and via Panama to East Coast)
        - Transatlantic (Europe-North America)
        - Asia-Middle East
        
        **Service Priorities:**
        - **Schedule reliability >90%**: Industry-leading target
        - **Streamlined port calls**: Fewer ports per string, deeper calls at selected hubs
        - **Digital integration**: Advanced cargo tracking, predictive ETAs, automated documentation
        """)
    
    st.markdown('<p class="subsection-header">2. Ocean Alliance (Est. ~30% Market Share) - UNCHANGED</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        **Members:**
        - **CMA CGM** (France)
        - **COSCO** (China)
        - **OOCL** (Hong Kong/China)
        - **Evergreen** (Taiwan)
        
        **Formation:** 2017
        **Extended:** Through 2032
        
        **Fleet:**
        - ~650 vessels
        - ~3.7M TEU capacity
        
        **Status:**
        - Largest alliance by capacity
        - Most stable partnership
        - No changes in Feb 2025
        """)
    
    with col2:
        st.markdown("""
        **The Stable Giant:**
        
        **Why Ocean Alliance Survived Unchanged:**
        
        Ocean Alliance is the only major alliance partnership that remained intact through the February 2025 
        restructuring. This stability reflects several factors:
        
        - **Long-term commitment**: Extended cooperation agreement through 2032
        - **Complementary markets**: Members serve different home markets (France, China, Taiwan)
        - **Balanced partnership**: No single dominant member (unlike 2M where MSC overtook Maersk)
        - **Successful collaboration**: Strong track record of operational cooperation since 2017
        
        **Member Profiles:**
        
        **CMA CGM (France)**: 
        - 3rd largest global carrier (~12% market share)
        - Strong in French-speaking Africa, Mediterranean, Latin America
        - Family-owned (Saadé family), long-term strategic thinking
        - Investing heavily in LNG-powered vessels (environmental leadership)
        
        **COSCO (China)**:
        - State-owned Chinese carrier (~11% market share)
        - Acquired OOCL in 2017 but maintains separate brand
        - Critical access to Chinese domestic market
        - Belt and Road Initiative alignment
        
        **OOCL (Hong Kong/China)**:
        - Subsidiary of COSCO but operationally independent
        - Premium brand positioning
        - Strong Hong Kong hub connectivity
        
        **Evergreen (Taiwan)**:
        - Family-owned Taiwanese carrier (~6% market share)
        - Intra-Asia expertise
        - Taiwan Strait trade access
        - Operates Ever Given (the vessel that blocked Suez Canal in 2021)
        
        **Key Trade Routes:**
        - Asia-Europe (multiple services, comprehensive coverage)
        - Trans-Pacific (all major port pairs)
        - Asia-Middle East-Red Sea (when accessible)
        - Strong intra-Asia feeder networks
        
        **Strategic Advantages:**
        - **Asian market access**: Three members provide unmatched Asia coverage
        - **Political diversity**: French, Chinese, and Taiwanese carriers reduce geopolitical risk
        - **Service frequency**: Large combined fleet enables multiple weekly sailings
        """)
    
    st.markdown('<p class="subsection-header">3. Premier Alliance (Est. ~17% Market Share) - REBRANDED</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        **Members:**
        - **ONE** (Japan)
        - **HMM** (South Korea)
        - **Yang Ming** (Taiwan)
        
        **Formation:** 
        - THE Alliance: 2017
        - Rebranded to Premier Alliance: Feb 2025
        
        **Fleet:**
        - ~350 vessels
        - ~2.3M TEU capacity
        
        **Status:**
        - Smallest of three alliances
        - Lost Hapag-Lloyd to Gemini
        - Cooperates with MSC on Asia-Europe
        """)
    
    with col2:
        st.markdown("""
        **From THE Alliance to Premier Alliance:**
        
        **What Changed:**
        
        The former THE Alliance lost **Hapag-Lloyd** (which joined Maersk in Gemini Cooperation) but the remaining 
        three Northeast Asian carriers decided to continue their partnership under the new name "Premier Alliance."
        
        **Historical Note**: THE Alliance originally stood for "THHE" - **T**HE, **H**apag-Lloyd, **H**MM, and 
        **E**vergreen. When Evergreen left for Ocean Alliance and now Hapag-Lloyd has left for Gemini Cooperation, 
        only the Northeast Asian carriers remain.
        
        **Member Profiles:**
        
        **ONE** (Ocean Network Express - Japan):
        - Formed 2018 from merger of three Japanese carriers (NYK, MOL, K Line)
        - 6th largest global carrier (~6% market share)
        - Strong trans-Pacific focus (Japan-North America trade)
        - Emphasises service reliability over volume growth
        
        **HMM** (Hyundai Merchant Marine - South Korea):
        - State-supported South Korean carrier (~3% market share)
        - Operates some of world's largest vessels (24,000 TEU HMM Algeciras)
        - Strong Korea-US trade lane
        - Aggressive growth strategy with mega vessel investments
        
        **Yang Ming** (Taiwan):
        - State-owned Taiwanese carrier (~2% market share)
        - Regional focus (intra-Asia, Asia-US West Coast)
        - Smaller but strategically important
        
        **Strategic Response to Smaller Size:**
        
        With Hapag-Lloyd's departure, Premier Alliance is now the smallest of the three major alliances. To 
        compensate:
        
        - **MSC cooperation**: Slot-sharing agreement with MSC on Asia-Europe trade
        - **Direct port-to-port services**: Focus on efficiency over comprehensive coverage
        - **US West Coast expansion**: Three weekly Shanghai/Ningbo-Los Angeles services
        - **Emphasise reliability**: Compete on service quality rather than scale alone
        
        **Key Trade Routes:**
        - Trans-Pacific (comprehensive Asia-US coverage, especially West Coast)
        - Asia-Europe (in cooperation with MSC)
        - Asia-Mediterranean
        - Intra-Asia feeder services
        """)
    
    st.markdown('<p class="subsection-header">4. MSC - Operating Independently with Strategic Cooperation</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        **MSC (Mediterranean Shipping Company)**
        
        **Status:** Independent carrier
        **Market Share:** ~20% (World's largest)
        
        **Fleet:**
        - ~800 vessels
        - ~2.5M TEU capacity
        - Largest container fleet globally
        
        **Strategic Partnerships:**
        - Premier Alliance (Asia-Europe slot-sharing)
        - ZIM (Asia-North America East Coast VSA)
        
        **Approach:**
        - Mostly independent operations
        - Selective cooperation on specific routes
        """)
    
    with col2:
        st.markdown("""
        **Why MSC Left the 2M Alliance:**
        
        **Diverging Strategies:**
        
        MSC and Maersk, once the two pillars of the dominant 2M Alliance, developed fundamentally different 
        strategic visions:
        
        **MSC's Strategy: Pure Carrier, Volume Growth**
        - Aggressive vessel acquisition (now owns 800+ vessels)
        - Focus on being the largest container carrier globally
        - Vertical integration into terminals (owns 35+ terminals worldwide)
        - Family-owned by Aponte family (Switzerland/Italy), long-term capacity building
        - Willing to operate at lower margins to gain market share
        
        **Maersk's Strategy: Integrated Logistics Provider**
        - Shift from pure carrier to end-to-end logistics (warehousing, customs, trucking, rail)
        - Digital transformation and technology leadership
        - Higher-margin services beyond ocean freight
        - Publicly traded company, shareholder return focus
        - Strategic repositioning from commodity carrier to solutions provider
        
        These divergent paths made continued alliance partnership untenable. MSC wanted maximum fleet flexibility 
        for volume growth; Maersk wanted integrated service offerings.
        
        **MSC's Independent Network:**
        
        As world's largest carrier, MSC has capacity to operate largely independently:
        
        - **34 service loops** covering five major trade routes
        - **East-West trades**: Asia-Europe, Trans-Pacific, Transatlantic
        - **1,900+ direct port pairings** (via Suez when accessible)
        - **1,800+ port pairings** via Cape of Good Hope alternative
        
        **Strategic Cooperation (Not Full Alliance):**
        
        MSC maintains flexibility through targeted partnerships:
        - **Premier Alliance**: Slot-sharing on Asia-Europe services only
        - **ZIM**: Three-year vessel-sharing agreement on Asia-US East Coast
        - Benefits: Some economies of scale without alliance restrictions
        - Maintains pricing independence and network flexibility
        """)
    
    # Alliance market share pie chart
    fig = go.Figure(data=[go.Pie(
        labels=alliance_data_2025['Alliance/Carrier'],
        values=alliance_data_2025['Est. Market Share (%)'],
        marker=dict(colors=['#3B82F6', '#10B981', '#F59E0B', '#8B5CF6', '#94A3B8']),
        textinfo='label+percent',
        textfont=dict(size=13, color='white'),
        hole=0.4
    )])
    
    fig.update_layout(
        title={
            'text': 'Global Container Shipping Market Share<br>Post-February 2025 Restructuring (Estimated)',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        annotations=[dict(text='Feb 2025<br>Structure', x=0.5, y=0.5, font_size=15, showarrow=False)],
        height=500
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    <div class="insight-box">
    <strong>📊 Market Share Note:</strong> Market share percentages shown are estimates for the new alliance structure 
    effective February 2025. Final market share data will stabilise over 2025-2026 as the new partnerships fully 
    operationalise. The fundamental dynamic remains: <strong>three major alliance structures plus MSC operating 
    semi-independently control approximately 83% of global container capacity</strong>, maintaining the oligopolistic 
    industry structure despite the alliance reorganisation.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 3: How Alliances Work - Operations vs Competition
    # ============================================================================
    
    st.markdown('<p class="section-header">How Shipping Alliances Work: Cooperation Without Collusion</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Shipping alliances are operational partnerships, not mergers or cartels. Understanding what alliance members 
    share (and crucially, what they do not share) is essential to grasping how modern container shipping operates 
    and why competition authorities permit these partnerships.
    """)
    
    st.markdown('<p class="subsection-header">What Alliance Members Share (Operational Cooperation)</p>', unsafe_allow_html=True)
    
    # Alliance cooperation framework
    cooperation_framework = pd.DataFrame({
        'Cooperation Area': [
            'Vessel Sharing',
            'Service Planning',
            'Port Calls',
            'Terminal Operations',
            'Schedule Coordination'
        ],
        'What They Share': [
            'Vessels and capacity on specific services',
            'Joint route planning and network design',
            'Coordinate which ports to call and rotation sequence',
            'Shared use of dedicated alliance terminals',
            'Synchronise sailing schedules for connections'
        ],
        'How It Works': [
            'Carrier A provides vessel, Carriers B & C buy slots. Rotate vessel provision across partners',
            'Collectively design service network to maximise coverage whilst minimising vessel requirements',
            'Agree optimal port rotation for shared services. Standardise port pairs across alliance',
            'Negotiate joint terminal leases. Share berth access and crane resources',
            'Align departure/arrival times for effective cargo transshipment between alliance services'
        ],
        'Benefit to Shippers': [
            'More frequent sailings (daily or multiple weekly services possible)',
            'Comprehensive global coverage (alliance provides network no single carrier could afford)',
            'Better connectivity through aligned port networks',
            'Efficient operations reduce costs passed to customers',
            'Reliable connections enable tighter supply chains'
        ]
    })
    
    st.dataframe(cooperation_framework, width='stretch', hide_index=True)
    
    st.markdown('<p class="subsection-header">What Alliance Members Do NOT Share (Competition Preserved)</p>', unsafe_allow_html=True)
    
    # Competition areas
    competition_areas = pd.DataFrame({
        'Competition Area': [
            'Pricing',
            'Customer Contracts',
            'Brand and Marketing',
            'Cargo Booking',
            'Service Quality'
        ],
        'Maintained Independence': [
            'Each carrier sets own freight rates independently',
            'Separate contract negotiations with shippers',
            'Independent brands, sales teams, marketing',
            'Cargo booked with specific carrier, not alliance',
            'Service quality differentiation maintained'
        ],
        'Why This Matters': [
            'Prevents price-fixing. Carriers compete vigorously on rates',
            'Shippers can negotiate with multiple alliance members for best deal',
            'Carriers differentiate on service, reputation, customer relationships',
            'Cargo belongs to booking carrier. Alliance provides vessels, not customers',
            'Carriers compete on reliability, documentation, customer service'
        ],
        'Regulatory Importance': [
            'Maintains price competition - alliances cannot set rates collectively',
            'Prevents anti-competitive behaviour - each carrier independently seeks cargo',
            'Consumer choice preserved - distinct brands offer different value propositions',
            'Market competition sustained - booking carrier bears revenue risk',
            'Quality competition drives continuous improvement'
        ]
    })
    
    st.dataframe(competition_areas, width='stretch', hide_index=True)
    
    st.markdown("""
    **The Critical Balance: Cooperate to Compete**
    
    Alliances allow carriers to:
    - **Achieve economies of scale** through shared vessels and coordinated networks
    - **Maintain competitive market dynamics** through independent pricing and customer acquisition
    - **Offer comprehensive global networks** that no single carrier could afford independently
    - **Preserve individual brands** and customer relationships (alliance largely invisible to shippers)
    
    **Regulatory Oversight:**
    
    Competition authorities (US FMC, EU Commission, etc.) closely monitor alliances:
    - **Operational cooperation**: Permitted and encouraged (improves efficiency, benefits customers)
    - **Price coordination**: Strictly forbidden (would be illegal cartel behaviour)
    - **Market access**: Alliances cannot block competitors from ports or routes
    - **Customer choice**: Must maintain multiple independent booking options
    
    Alliances must demonstrate that benefits (better service, lower costs through efficiency) outweigh risks 
    (reduced competition). So far, authorities have concluded alliances improve service whilst competition on 
    pricing remains vigorous.
    """)
    
    # ============================================================================
    # SECTION 4: Hub-and-Spoke Networks - The Dominant Model
    # ============================================================================
    
    st.markdown('<p class="section-header">Hub-and-Spoke Network Structure: How Global Shipping Actually Works</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Modern container shipping operates primarily on a **hub-and-spoke model**, not point-to-point services. 
    Understanding this network structure is absolutely fundamental to comprehending maritime logistics, port 
    competition, and Singapore's strategic position. The lecture materials emphasise that **approximately 85% 
    of global container cargo transships at intermediate hub ports** rather than moving directly from origin to 
    final destination.
    """)
    
    st.markdown('<p class="subsection-header">Point-to-Point vs Hub-and-Spoke: A Critical Distinction</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Point-to-Point Model (Minority of Traffic):**
        
        **Concept:**
        - Direct service between origin and destination ports
        - No intermediate transshipment required
        - Container loaded at origin, discharged only at final destination
        
        **Example Routes:**
        - Shanghai → Los Angeles (major high-volume direct service)
        - Ningbo → Long Beach
        - Shenzhen → Rotterdam
        
        **When Point-to-Point Works:**
        - **Very high cargo volumes**: Enough containers to fill mega vessel (12,000-20,000 TEU)
        - **Major trade lanes**: Asia-US West Coast, Asia-Europe mainlines
        - **Consistent year-round demand**: Can justify dedicated weekly or bi-weekly service
        - **Specific high-value routes**: Justify direct service despite lower utilisation
        
        **Advantages:**
        - **Faster transit**: No transshipment delay (typically 2-4 days saved)
        - **Lower damage risk**: Fewer container handlings reduce potential for damage or loss
        - **Simpler tracking**: Straightforward origin-destination monitoring
        - **Customer preference**: Shippers prefer direct services when available
        
        **Disadvantages:**
        - **Limited geographic coverage**: Can only serve port pairs with sufficient volume
        - **Lower sailing frequency**: May only offer weekly service (insufficient demand for daily)
        - **Higher cost per TEU**: Unless vessel is 85-90%+ full, unit economics suffer
        - **Inflexible network**: Cannot efficiently serve smaller ports
        
        **Reality**: Only 10-15% of global container movements are truly point-to-point direct services.
        """)
    
    with col2:
        st.markdown("""
        **Hub-and-Spoke Model (Majority of Traffic):**
        
        **Concept:**
        - **Mainline vessels** (mega ships 15,000-24,000 TEU) connect major hub ports
        - **Feeder vessels** (smaller 1,000-3,000 TEU) connect hubs to regional ports
        - Containers **transship** at hubs (transferred between vessels)
        
        **Example Network:**
        - Malaysia export cargo collected by feeder → Singapore hub
        - Transshipped to mainline ULCS → Europe
        - European hub (Rotterdam) receives cargo
        - Distributed by feeders to regional destinations (Amsterdam, Hamburg, Antwerp)
        
        **When Hub-and-Spoke Dominates:**
        - **Moderate cargo volumes**: Most routes have insufficient volume for direct mega vessel service
        - **Geographic coverage**: Enables service to hundreds of smaller ports economically
        - **Network efficiency**: Consolidates cargo to fill mega vessels on main lanes
        - **85% of global traffic**: The dominant model in modern shipping
        
        **Advantages:**
        - **Comprehensive coverage**: Can serve 600+ ports globally through hub-feeder networks
        - **Higher mainline frequency**: Consolidating cargo enables daily/multiple weekly mega vessel services
        - **Better vessel utilisation**: Larger ships on trunk routes achieve 90%+ load factors
        - **Economic viability**: Makes small-port service profitable through feeder consolidation
        - **Network flexibility**: Can easily add/remove feeder connections without disrupting mainline
        
        **Disadvantages:**
        - **Longer total transit**: Transshipment adds 2-4 days vs direct (feeder wait + transfer time)
        - **Higher damage risk**: Multiple handlings increase potential for damage, loss, or delays
        - **Complex coordination**: Requires precise scheduling to minimise connection times
        - **Hub dependency**: Entire network vulnerable if hub experiences disruption
        
        **Reality**: **85% of containers transship** at intermediate hubs according to lecture materials and 
        Singapore's own operational data.
        """)
    
    st.markdown('<p class="subsection-header">Singapore: The World\'s Premier Transshipment Hub</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore represents the ultimate example of the hub-and-spoke model in action. Understanding Singapore's 
    role illuminates how hub-and-spoke networks function globally and why location, efficiency, and connectivity 
    are the three pillars of hub competitiveness.
    """)
    
    st.markdown("""
    <div class="success-box">
    <strong>🇸🇬 Singapore's Transshipment Statistics (Lecture Materials):</strong><br><br>
    <strong>85% transshipment cargo</strong>: Only 15% of containers calling Singapore originate or terminate there. 
    The vast majority arrives from one vessel and departs on another.<br><br>
    <strong>Connected to 600+ ports</strong> in 120+ countries: Unmatched global connectivity through hub-feeder 
    and mainline-mainline networks.<br><br>
    <strong>200+ shipping lines</strong> call at Singapore: Nearly every major carrier operates services through 
    Singapore, creating dense network effects.<br><br>
    <strong>Unrivalled connectivity</strong>: Lecture emphasis on Singapore's "unrivalled connectivity" as the 
    foundation of its hub status.<br><br>
    <strong>Strategic location</strong>: Positioned on main Asia-Europe shipping lane (33% of global container trade) 
    and at the centre of Southeast Asian growth markets.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Singapore's Hub Business Model: Pure Transshipment**
    
    Unlike gateway ports (Los Angeles, Hamburg) where most cargo serves local markets, Singapore operates as 
    a **pure transshipment hub**:
    
    **The Transshipment Process:**
    
    1. **Feeder vessel arrives** from regional port (e.g., Port Klang, Tanjung Pelepas, Bangkok)
       - Carries 500-2,000 TEU collected from 3-5 regional ports
       - Discharges containers at Singapore
    
    2. **Container enters terminal yard**
       - Stored temporarily (typically 12-48 hours)
       - Awaiting connection to outbound mainline vessel
    
    3. **Mainline vessel arrives** (mega vessel 18,000-24,000 TEU)
       - Receives transshipment cargo alongside Singapore origin cargo (15%)
       - Departs for long-haul destination (Europe, US, Africa)
    
    4. **At European hub** (Rotterdam, Hamburg, Antwerp)
       - Container discharges and transfers to European feeder
       - Final delivery to destination port (Amsterdam, Le Havre, etc.)
    
    **Result**: Container handled 4 times (origin port → feeder → Singapore → mainline → European hub → European 
    feeder → destination port) but enables economically viable service to small ports through consolidation.
    
    **Singapore's Strategic Advantages:**
    
    **1. Location - Geography is Destiny:**
    - **Malacca Strait chokepoint**: 80,000+ vessel transits annually, including 33% of global container trade
    - **Asia-Europe mainline**: Positioned directly on the highest-volume container route globally
    - **Regional centrality**: Equidistant from major Asian economies (China, India, ASEAN, Australia)
    - **Deep natural harbour**: 16+ metre depth allows mega vessels without dredging
    
    **2. Operational Excellence - Efficiency as Competitive Advantage:**
    - **Berth on Arrival >90%**: Vessels berth immediately without anchorage wait (unmatched globally)
    - **24-36 hour vessel turnaround**: Mega vessels with 10,000+ container moves complete in 1.5 days
    - **Crane productivity 35-40 GMPH**: Among highest globally, critical for mega vessel economics
    - **Minimal transshipment delays**: Efficient yard operations minimise time between feeder-mainline
    
    **3. Connectivity - Network Effects:**
    - **200+ shipping lines**: Critical mass creates virtuous cycle (more lines → more connections → attracts more lines)
    - **600+ connected ports**: Comprehensive coverage makes Singapore the default choice for regional distribution
    - **Multiple daily sailings**: High frequency to/from major markets (daily China service, multiple Europe strings)
    - **Alliance coverage**: All three alliances plus MSC operate through Singapore, ensuring comprehensive network
    
    **Singapore's Vulnerability: The Double-Edged Sword of Pure Transshipment**
    
    Singapore's 85% transshipment concentration creates both strength and vulnerability:
    
    **Strengths:**
    - Taps into global trade flows, not limited by local market size (5.8 million population)
    - Can grow with global trade regardless of Singapore's own economic growth
    - Benefits from Southeast Asian economic development (all growth routes through Singapore)
    
    **Vulnerabilities:**
    - **Shipping line decisions**: Vulnerable to alliance routing changes or new hub developments
    - **No local cargo base**: Cannot fall back on hinterland demand if transshipment volumes shift
    - **Regional competition**: Malaysia, Indonesia, Thailand developing alternative hub ports
    - **Route disruptions**: Red Sea crisis demonstrated vulnerability to trade route changes
    - **Existential threats**: Kra Canal (if ever built) would bypass Singapore entirely
    
    **Singapore's Strategic Response: "Vital Port in Interconnected Network"**
    
    The lecture materials emphasise that Singapore must position itself as a **"vital port in an inter-connected 
    port network"** rather than simply the "biggest hub." This reflects a strategic shift:
    
    **Old Mentality**: "Big Hub" - Compete purely on volume, be largest at any cost, winner-takes-all
    
    **New Mentality**: "Vital Node" - Be so efficient, reliable, and connected that shipping lines cannot 
    afford to bypass Singapore. Emphasise indispensability over mere size.
    
    This philosophical shift acknowledges that multiple hubs can coexist if each provides unique value, and that 
    being irreplaceable (due to efficiency and connectivity) is more valuable than being largest.
    """)
    
    # ============================================================================
    # SECTION 5: Major Global Trade Routes
    # ============================================================================
    
    st.markdown('<p class="section-header">Major Global Container Trade Routes</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Container trade flows along established routes connecting major economic regions. Understanding these 
    routes—their volumes, characteristics, and strategic importance—is essential for comprehending global 
    supply chains and port positioning strategies.
    """)
    
    # Trade routes data
    trade_routes = pd.DataFrame({
        'Trade Lane': [
            'Intra-Asia',
            'Asia-Europe',
            'Trans-Pacific (Asia-US West Coast)',
            'Trans-Pacific (Asia-US East Coast)',
            'Transatlantic (Europe-North America)',
            'Asia-Middle East',
            'North-South (Europe/Asia-Latin America)',
            'North-South (Europe/Asia-Africa)'
        ],
        'Est. Annual Volume (M TEU)': [35, 24, 17, 9, 8, 7, 6, 4],
        'Transit Time': ['3-7 days', '30-35 days (Suez)', '12-16 days', '20-25 days (via Panama)', '7-10 days', '10-14 days', '15-25 days', '15-20 days'],
        'Key Characteristics': [
            'Highest volume, intra-regional trade, frequent services',
            'Longest distance, largest vessels (ULCS), via Suez or Cape',
            'High-value cargo, direct services, Panamax/Post-Panamax vessels',
            'Growing with new Panama Canal, New-Panamax vessels',
            'Mature trade, premium cargo, smaller vessels',
            'Energy products, consumer goods, moderate volume',
            'Emerging markets, consumer goods to LatAm, commodities back',
            'Growth market, infrastructure, consumer goods'
        ],
        'Strategic Notes': [
            '35M TEU reflects China-ASEAN integration, short distances enable frequent rotations',
            '33% of global trade passes through Suez, Red Sea crisis forced Cape routing (+7-10 days)',
            'Direct services common due to volume, minimal transshipment',
            'Panama Canal expansion (2016) enabled larger vessels, growth accelerating',
            'Relatively balanced trade, premium brands, established routes',
            'Vulnerable to regional instability, important for energy equipment',
            'One-way trade imbalance (exports to LatAm, return empty/commodities)',
            'Long-term growth potential, infrastructure investment heavy'
        ]
    })
    
    st.dataframe(trade_routes, width='stretch', hide_index=True)
    
    # Trade volumes visualisation
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=trade_routes['Trade Lane'],
        y=trade_routes['Est. Annual Volume (M TEU)'],
        marker=dict(color='#3B82F6', line=dict(color='#1E40AF', width=2)),
        text=trade_routes['Est. Annual Volume (M TEU)'],
        textposition='outside',
        texttemplate='%{text}M TEU'
    ))
    
    fig.update_layout(
        title={
            'text': 'Global Container Trade Volumes by Route (2024 Estimates)',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        xaxis_title="Trade Lane",
        yaxis_title="Annual Volume (Million TEU)",
        height=500,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='#E5E7EB', range=[0, 40]),
        xaxis=dict(tickangle=-30)
    )
    
    st.plotly_chart(fig, width='stretch')
    
    # ============================================================================
    # SECTION 6: Geopolitics Reshaping Shipping Patterns
    # ============================================================================
    
    st.markdown('<p class="section-header">Geopolitics Reshaping Global Shipping Patterns</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Global trade patterns are increasingly influenced by geopolitical tensions, strategic considerations, and 
    government policies. The era of purely economic decision-making in global supply chains is giving way to 
    "geoeconomics"—where national security, political alliances, and strategic autonomy shape trade flows as 
    much as cost efficiency.
    """)
    
    st.markdown('<p class="subsection-header">US-China Trade Tensions and "China+1" Diversification</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Trade War and Beyond (2018-Present):**
    
    **Key Developments:**
    
    - **2018-2019: Tariff escalation**
      - US imposed tariffs on $370 billion of Chinese imports
      - China retaliated with tariffs on $110 billion of US goods
      - Average tariff on Chinese imports rose from 3% to 20%+
    
    - **2020-2022: Supply chain disruptions**
      - COVID-19 exposed vulnerabilities of concentrated Chinese manufacturing
      - Semiconductor shortages highlighted dependence on Asian supply chains
      - "Resilience" became as important as "efficiency" in supply chain design
    
    - **2023-Present: Strategic decoupling**
      - US implementing export controls on advanced semiconductors and manufacturing equipment
      - Investment restrictions on sensitive technologies
      - "Friend-shoring" and "de-risking" becoming corporate strategies
      - Both countries pursuing strategic autonomy in critical sectors
    
    **Impact on Container Shipping:**
    
    **The "China+1" Strategy:**
    
    Rather than abandoning China entirely (impractical given scale and infrastructure), companies are adopting 
    **"China+1"** strategies—maintaining Chinese production whilst adding manufacturing capacity in alternative 
    locations:
    
    - **Not abandoning China**: Too costly to exit entirely, China remains critical manufacturing base
    - **Adding alternatives**: Diversifying to reduce concentration risk and navigate tariffs
    - **"Plus One" locations**: Vietnam, Malaysia, Thailand, India, Mexico gaining manufacturing investments
    - **Supply chain complexity**: More complex, multi-country supply chains replacing simple China-centric models
    """)
    
    # China+1 beneficiaries data
    intermediary_growth = pd.DataFrame({
        'Country': ['Vietnam', 'Malaysia', 'Thailand', 'India', 'Mexico', 'Poland', 'Turkey'],
        '2018 Export Baseline': [100, 100, 100, 100, 100, 100, 100],
        '2024 Export Growth Index': [180, 145, 141, 135, 142, 128, 130],
        'Growth (%)': ['+80%', '+45%', '+41%', '+35%', '+42%', '+28%', '+30%'],
        'Primary Beneficiary Of': [
            'China+1, low-cost manufacturing, proximity to China',
            'Electronics, electrical goods, palm oil',
            'Automotive, electronics, food processing',
            'Pharmaceuticals, IT services, textiles',
            'Nearshoring to US, automotive, electronics',
            'Nearshoring to EU, automotive, white goods',
            'Nearshoring to EU, textiles, automotive parts'
        ],
        'Shipping Impact': [
            'Rapid growth in Vietnam-US services, intra-Asia feeder expansion',
            'Strengthened Port Klang and Tanjung Pelepas competitiveness',
            'Increased Bangkok/Laem Chabang connectivity requirements',
            'Nhava Sheva and Mundra capacity expansions',
            'Nearshore advantage: Short Mexico-US rail/truck, less container shipping',
            'Central Europe hub positioning',
            'Mediterranean feeder network growth'
        ]
    })
    
    st.dataframe(intermediary_growth, width='stretch', hide_index=True)
    
    st.markdown("""
    **The "Intermediate Country" Phenomenon:**
    
    An interesting pattern has emerged: direct China-US trade may be plateauing, but **intermediate countries** 
    are experiencing explosive export growth. Investigation often reveals:
    
    - **Component imports from China**: Vietnam imports Chinese components and sub-assemblies
    - **Final assembly locally**: Light assembly, packaging, or finishing work
    - **Export to US/EU**: Now labelled "Made in Vietnam" avoiding tariffs
    - **Value-add varies**: Sometimes substantial (genuine manufacturing), sometimes minimal (tariff arbitrage)
    
    This creates **more complex, multi-hop supply chains**:
    - China → Vietnam (components) → US (final goods)
    - China → Mexico (sub-assemblies) → US (finished products)
    - China → Poland (materials) → EU (consumer goods)
    
    **Impact on Ports and Shipping:**
    - **Transshipment volumes increasing**: More multi-leg routing boosts hub port demand
    - **Intra-Asia trade growing**: Component movements between Asian countries
    - **New port competition**: Vietnam, Malaysia, Thailand ports gaining relevance
    - **Singapore benefits**: Central position captures increased intra-Asian and transshipment flows
    """)
    
    st.markdown('<p class="subsection-header">Alternative Routes and Emerging Threats to Established Hubs</p>', unsafe_allow_html=True)
    
    # Alternative routes
    alternative_routes = pd.DataFrame({
        'Alternative Route/Development': [
            'Arctic Route (Northern Sea Route)',
            'Thailand Kra Canal (Proposed)',
            'China-Europe Rail (Belt & Road)',
            'Suez Canal Expansion',
            'Panama Canal New Locks',
            'India-Middle East-Europe Corridor (IMEC)'
        ],
        'Status': [
            'Operational but limited (summer ice-free)',
            'Proposed only (not funded)',
            'Operational since 2011',
            'Completed 2015',
            'Completed 2016',
            'Announced 2023, early planning'
        ],
        'Potential Impact': [
            '30% shorter Asia-Europe distance, could divert traffic from Suez if year-round accessible',
            'Would bypass Malacca Strait and Singapore entirely (95% shorter than Malacca route)',
            'Competes for time-sensitive cargo, limited by rail capacity (~1% of maritime volume)',
            'Accommodates larger vessels, faster transit, benefits Suez-dependent hubs',
            'Allows 14,500 TEU vessels to use canal, opened trans-Pacific East Coast services',
            'Multi-modal India-Middle East-Europe route, reduces dependence on sea routes'
        ],
        'Likelihood/Timeline': [
            'Climate-dependent, potentially viable 2030s-2040s as Arctic warming continues',
            'Very low likelihood, decades away if ever (cost $28B+, environmental concerns massive)',
            'Already operational, niche role for high-value time-sensitive cargo',
            'Already implemented and operational',
            'Already implemented and operational',
            'Long-term project, 2030s at earliest for significant operations'
        ],
        'Singapore Impact': [
            'Moderate long-term threat if Arctic becomes reliably ice-free year-round',
            'Existential threat if built (bypasses Singapore/Malacca Strait entirely)',
            'Minimal (rail can never match maritime volume and cost efficiency)',
            'Neutral to positive (more efficient Suez reinforces established route)',
            'Neutral (different ocean, but creates competitive alternative to Suez for some cargo)',
            'Potential threat if becomes major India-Europe route (bypasses Southeast Asia)'
        ]
    })
    
    st.dataframe(alternative_routes, width='stretch', hide_index=True)
    
    st.markdown("""
    **The Kra Canal: Singapore's Existential Nightmare (Low Probability, High Impact)**
    
    The proposed **Kra Canal** across Thailand's Isthmus of Kra would be Singapore's worst-case scenario:
    
    - **Route**: Cut through southern Thailand, connecting Andaman Sea (west) to Gulf of Thailand (east)
    - **Distance saving**: 1,200 kilometres shorter than Malacca Strait route (95% distance reduction)
    - **Impact on Singapore**: Would bypass Malacca Strait and Singapore entirely
    - **Estimated cost**: $28-40 billion (varies by proposal)
    - **Construction timeline**: 10+ years if ever started
    
    **Why Singapore Monitors This Closely (Despite Low Probability):**
    
    If built, Kra Canal would:
    - **Eliminate Singapore's locational advantage**: No longer on the mandatory Asia-Europe route
    - **Bypass Malacca Strait**: Remove the geographical necessity that underpins Singapore's position
    - **Devastate transshipment volumes**: Mega vessels could route directly through Thailand
    - **Create new Thai hub ports**: Thailand would capture transshipment business
    
    **Why Kra Canal Remains Unlikely:**
    
    - **Massive cost**: $28-40B investment with uncertain returns
    - **Environmental impact**: Would devastate ecosystems, massive opposition
    - **Geopolitical complexity**: Malaysia and Singapore would strongly oppose
    - **Economic uncertainty**: Would Thailand benefit enough to justify cost?
    - **Technical challenges**: Seabed geology complex, construction difficult
    - **No credible funding**: No serious investor backing despite decades of proposals
    
    Despite low probability, Singapore's **$20 billion Tuas investment** partially reflects the imperative to 
    lock in shipping line commitments and create such operational superiority that even a Kra Canal couldn't 
    easily divert traffic.
    """)
    
    # ============================================================================
    # SECTION 7: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways: Global Shipping & Alliances</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Industry Consolidation:**
        - 15+ independent carriers (2000) → 9 major players (2025)
        - Three alliance structures control 83% of global capacity
        - Overcapacity crisis (2015-2016) forced consolidation wave
        - Hanjin bankruptcy (2016) demonstrated scale necessity
        - Further consolidation likely over next decade
        
        **February 2025 Alliance Restructuring:**
        - **2M Alliance dissolved** (MSC + Maersk, 10-year partnership ended)
        - **Gemini Cooperation formed** (Maersk + Hapag-Lloyd, hub-spoke focus)
        - **Premier Alliance created** (ONE + HMM + Yang Ming, formerly THE Alliance)
        - **Ocean Alliance unchanged** (CMA CGM + COSCO + OOCL + Evergreen)
        - **MSC independent** (operates alone with selective cooperation)
        
        **Alliance Operations:**
        - Cooperate on: Vessels, service planning, port calls, schedules
        - Compete on: Pricing, contracts, customer service, quality
        - Regulatory oversight: Competition authorities monitor closely
        - Balance: Achieve economies of scale whilst preserving competition
        """)
    
    with col2:
        st.markdown("""
        **Hub-and-Spoke Dominance:**
        - 85% of containers transship at intermediate hubs
        - Singapore: 85% transshipment, world's premier hub
        - Connected to 600+ ports globally through hub-feeder networks
        - Mainline mega vessels connect hubs (18,000-24,000 TEU)
        - Feeder vessels connect hubs to regional ports (1,000-3,000 TEU)
        - "Vital port in interconnected network" vs "biggest hub" strategy
        
        **Major Trade Routes:**
        - Intra-Asia: Largest volume (35M TEU annually)
        - Asia-Europe: Longest distance (24M TEU, 30-35 days via Suez)
        - Trans-Pacific: High-value cargo (26M TEU combined East+West Coast)
        - Various North-South routes to Latin America, Africa, Middle East
        
        **Geopolitical Reshaping:**
        - US-China tensions driving "China+1" diversification strategies
        - Vietnam (+80%), Malaysia (+45%), Mexico (+42%) export growth
        - Intermediate countries benefit from supply chain reconfiguration
        - Alternative routes emerging (Arctic, BRI, Kra Canal proposal)
        - Trade patterns increasingly influenced by strategic considerations
        
        **Singapore's Challenge:**
        - Maintain position as indispensable transshipment hub
        - Face intensifying regional competition (Malaysia, Indonesia, Thailand)
        - Adapt to changing trade patterns and alliance restructuring
        - Massive Tuas investment ($20B) to lock in long-term competitiveness
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> The container shipping industry has consolidated dramatically, with just 9 major 
    carriers organised into three alliance structures (post-February 2025: Gemini Cooperation, Ocean Alliance, 
    Premier Alliance) plus MSC operating semi-independently, collectively controlling 83% of global capacity. This 
    oligopolistic structure emerged from the 2015-2016 overcapacity crisis that forced "get big or get out" dynamics. 
    Modern shipping operates primarily on hub-and-spoke networks, with 85% of cargo transshipping at intermediate 
    hubs. Singapore, as the world's premier transshipment hub (connected to 600+ ports, 200+ shipping lines), 
    exemplifies this model but faces intensifying competition and must position itself as a "vital port in an 
    interconnected network" through operational excellence and comprehensive connectivity. Geopolitical tensions, 
    particularly US-China trade disputes, are reshaping global trade patterns through "China+1" diversification, 
    with Vietnam, Malaysia, India, and Mexico experiencing rapid export growth as intermediate manufacturing 
    locations. Alternative routes (Arctic, Kra Canal, Belt and Road Initiative) pose potential long-term threats 
    to established shipping lanes and hub ports, requiring continuous strategic adaptation and infrastructure 
    investment to maintain competitive positions.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** 🇸🇬 Maritime Singapore Ecosystem - Explore Singapore's comprehensive maritime cluster beyond 
    the port (170+ international shipping groups, 30+ shipbroking firms, 20+ banks with shipping portfolios, 
    100+ MarineTech startups), understand MPA's dual role as both regulator and strategic developer, and discover 
    the innovation ecosystem that positions Singapore as the world's top international maritime centre for 11 
    consecutive years.
    """)
