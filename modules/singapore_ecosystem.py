import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">🇸🇬 Maritime Singapore Ecosystem</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand Singapore's position as the world's #1 international maritime centre for 12 consecutive years,
    comprehend the comprehensive maritime cluster beyond just port operations (170+ international shipping groups,
    30+ shipbroking firms, 20+ banks, 30+ law firms, 100+ MarineTech startups), master MPA's unique dual role as
    both regulator and strategic developer, and explore the innovation ecosystem (BLOCK71, MINT Fund, academic
    partnerships) driving Maritime 4.0 transformation.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Singapore - The World's Leading International Maritime Centre
    # ============================================================================
    
    st.markdown('<p class="section-header">Singapore: The World\'s Leading International Maritime Centre</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore has systematically cultivated its position as the world's preeminent maritime hub over seven decades
    of strategic planning and consistent execution. What distinguishes Singapore from other major ports is not just
    the physical infrastructure for moving containers, but rather a **comprehensive maritime ecosystem** that provides
    every conceivable maritime service under one roof. This "one-stop shop" approach creates powerful network effects
    and high switching costs that reinforce Singapore's competitive position.
    """)
    
    st.markdown("""
    <div class="success-box">
    <strong>🏆 Singapore's Global Maritime Leadership (2024 Record-Breaking Performance):</strong><br><br>
    <strong>World's #1 International Maritime Centre</strong>: Ranked first for the <strong>12th consecutive year</strong>
    in the Xinhua-Baltic International Shipping Centre Development Index (ISCDI), scoring highest in three out of five
    pillars: Shipping, Ports and Logistics, and Attractiveness and Competitiveness.<br><br>
    <strong>Container Throughput Record</strong>: <strong>41.12 million TEU</strong> in 2024 (crossed 40M milestone for
    first time), growing 5.4% from 39.0 million TEU in 2023. World's largest container transshipment hub with approximately
    <strong>90% transshipment cargo</strong>.<br><br>
    <strong>Vessel Arrival Tonnage Record</strong>: <strong>3.11 billion gross tonnage (GT)</strong> in 2024, up 0.6%
    from 3.09 billion GT in 2023. Over <strong>130,000 vessel calls annually</strong>.<br><br>
    <strong>Bunkering Leadership</strong>: World's largest bunkering hub with <strong>54.92 million tonnes</strong> of
    bunker sales in 2024 (new high, 6.0% year-on-year increase). Alternative fuel bunkers exceeded <strong>1 million
    tonnes</strong> for first time (1.34M tonnes total).<br><br>
    <strong>Ship Registry Excellence</strong>: <strong>5th largest ship registry globally</strong> with <strong>108 million
    GT</strong> in 2024, exceeding 100 million GT milestone for first time (8.5% growth from 99.6M GT in 2023).<br><br>
    <strong>Global Connectivity</strong>: Connected to <strong>600+ ports</strong> in 120+ countries, with <strong>200+
    shipping lines</strong> calling at Singapore.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Container Throughput", "41.12M TEU", delta="+5.4% vs 2023", help="2024 record, crossed 40M TEU milestone for first time")
    with col2:
        st.metric("World Ranking", "#1 IMC, #2 Port", delta="12th consecutive year", help="#1 International Maritime Centre, #2 container port globally")
    with col3:
        st.metric("Vessel Arrival Tonnage", "3.11B GT", delta="+0.6% vs 2023", help="Annual vessel arrival tonnage 2024, new record")
    with col4:
        st.metric("Global Connectivity", "600+ ports", delta="200+ shipping lines", help="Connected to 600+ ports via 200+ shipping lines")
    
    st.markdown('<p class="subsection-header">The Twin Engines of Maritime Singapore</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore's maritime success rests on two interconnected pillars, which the lecture materials describe as the
    **"twin engines of growth"**: the **Global Hub Port** (physical infrastructure and operations) and the
    **International Maritime Centre** (comprehensive cluster of maritime services). Understanding the distinction
    and synergy between these two engines is essential to grasping Singapore's maritime strategy.
    
    **Engine 1: Global Hub Port - The Physical Foundation**
    
    The Global Hub Port encompasses the tangible infrastructure and operations that enable cargo movement:
    
    **Strategic Location - Geography as Competitive Advantage:**
    - **Malacca Strait position**: Located on the busiest maritime chokepoint, with 80,000+ annual vessel transits
    - **Asia-Europe mainline**: Positioned directly on the route carrying 33% of global container trade
    - **Southeast Asian centrality**: Equidistant from major Asian economies (China, India, Japan, Korea, ASEAN)
    - **Natural deep-water harbour**: 16+ metre depth allows mega vessels without extensive dredging
    - **Equatorial location**: No typhoons or hurricanes, enabling year-round 24/7 operations
    
    **World-Class Infrastructure:**
    - **Multiple terminal systems**: PSA terminals (Tanjong Pagar, Keppel, Brani, Pasir Panjang) plus Jurong Port
    - **Tuas Mega Port development**: 11 berths operational (2024), 7 more by 2027, ultimate capacity 65M TEU by 2040s
    - **Super Post-Panamax cranes**: Deployed to handle world's largest vessels (24,000+ TEU capacity ships)
    - **Automation and technology**: Progressive automation deployment, digital systems integration
    - **Multimodal connections**: Air-sea, sea-rail integration for comprehensive logistics
    
    **Operational Excellence - The Singapore Standard:**
    - **Berth on Arrival (BOA) >90%**: Vessels berth immediately without anchorage wait time (globally rare)
    - **24-36 hour vessel turnaround**: Mega vessels with 10,000+ container moves completed within 1.5 days
    - **Crane productivity 35-40 GMPH**: Gross moves per hour among highest globally
    - **24/7/365 operations**: No downtime, continuous availability year-round
    - **Efficient customs**: Streamlined documentation, TradeNet system, fast cargo clearance
    - **Minimal transshipment delays**: Sophisticated yard management optimises container flow
    
    **The Numbers Tell the Story:**
    - **41.12 million TEU** handled in 2024 (both PSA terminals and Jurong Port combined)
    - **622.67 million tonnes** of cargo throughput (5.2% increase from 2023)
    - **3.11 billion GT** vessel arrival tonnage (reflects over 130,000 vessel calls)
    - **90% transshipment ratio**: Only 10% local origin/destination, 90% cargo transships
    
    **Engine 2: International Maritime Centre - The Comprehensive Ecosystem**
    
    The International Maritime Centre comprises the complete cluster of maritime services beyond physical port operations.
    This is where Singapore truly differentiates itself from port competitors. According to lecture materials, Singapore
    recognised early that: **"Maritime Singapore would have to go beyond its status as a major hub to become an
    international maritime centre providing a full suite of services."**
    
    The strategic insight was profound: **"To compete effectively, we have to become a complete maritime cluster by
    adding our core group of ship-owners and operators, maritime support services such as maritime finance, insurance
    and legal services."** This vision, articulated in Singapore Nautilus Q1 2008, has been systematically executed
    over 15+ years.
    
    **The International Maritime Centre Includes:**
    
    **Maritime Companies and Services (The Cluster):**
    - **170+ international shipping groups**: Including top liner companies, commodity traders with shipping arms,
      dry bulk and tanker shipping companies, and leading ship management companies
    - **30+ leading international shipbroking firms**: Facilitating ship chartering and sale/purchase transactions globally
    - **20+ banks with shipping portfolios**: Providing ship financing, project finance, working capital facilities
    - **30+ law firms with shipping practice**: Maritime disputes, contracts, admiralty law, arbitration services
    - **10 IG P&I Clubs**: Protection and Indemnity insurance covering 95% of world's ocean-going tonnage
    - **~100 MarineTech startups**: Innovation ecosystem raised ~S&#36;50 million investment in past 4 years
    
    **Economic Impact:**
    - **S&#36;4.3 billion** in total maritime business spending in 2022 (excluding port operations)
    - **5th largest ship registry** globally with 108 million GT under Singapore flag (2024)
    - **World's largest bunkering hub**: 54.92 million tonnes supplied in 2024
    - **Complete value chain**: Ship design, construction, operation, financing, insurance, maintenance, recycling
    
    **Why This Comprehensive Approach Matters:**
    
    **Network Effects and Switching Costs:**
    
    When a shipping company establishes Singapore operations, they gain access to the entire ecosystem:
    - **Ship financing** from 20+ banks familiar with maritime sector
    - **Insurance coverage** from all major P&I Clubs and marine insurers
    - **Legal support** from 30+ specialised maritime law firms
    - **Ship management services** from leading global managers
    - **Bunker fuel supply** from world's largest bunkering hub
    - **Ship repair** during port calls at world-class yards
    - **Crew changes** with efficient immigration and travel connections
    - **Maritime technology** from 100+ startups and innovation centres
    
    Once established, the **switching costs** are enormous. Moving headquarters means:
    - Losing established banking relationships
    - Re-negotiating insurance coverage
    - Finding new legal counsel familiar with maritime law
    - Rebuilding supply chain connections
    - Training staff on different systems and processes
    - Potentially losing access to Singapore's tax treaties and business environment
    
    **The Strategic Commitment:**
    
    The lecture materials emphasise that Singapore's government provides certainty and stability: **"Singapore will
    live up to its reputation for stable pro-business policies that provide certainty. We avoid back tracking and
    U-turns, and we set out to make companies feel welcome and a valued part of the Singapore maritime ecosystem."**
    
    This long-term commitment spanning decades creates confidence for companies making major capital investments
    (building terminals, establishing offices, deploying vessels). Companies know Singapore's policies will remain
    consistent and supportive.
    """)
    
    # ============================================================================
    # SECTION 2: Maritime and Port Authority of Singapore (MPA) - The Unique Dual Role
    # ============================================================================
    
    st.markdown('<p class="section-header">Maritime and Port Authority of Singapore (MPA): The Strategic Orchestrator</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The Maritime and Port Authority of Singapore (MPA) occupies a globally unique position by combining **regulatory
    authority** with **strategic development responsibility**. This dual mandate—rare among major maritime nations—enables
    Singapore to pursue coherent long-term strategies that align safety, security, efficiency, and competitiveness.
    Understanding how MPA balances these potentially conflicting roles illuminates Singapore's maritime governance model.
    """)
    
    st.markdown('<p class="subsection-header">MPA\'s Dual Mandate: Regulator + Developer</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Role 1: REGULATOR - Safety, Security, Standards**
        
        **Port Safety and Security Operations:**
        - **Vessel Traffic Management (VTS)**: 24/7 monitoring of Singapore Strait traffic, coordinating 130,000+
          annual vessel transits through one of world's busiest waterways
        - **Port security (ISPS Code)**: International Ship and Port Facility Security Code enforcement, protecting
          against terrorism and piracy threats
        - **Marine safety regulations**: Navigational safety rules, collision prevention, emergency response protocols
        - **Accident investigation**: Root cause analysis, safety improvements, lessons learned dissemination
        - **Pilotage services oversight**: Licensing pilots, ensuring competency standards, regulating operations
        
        **Environmental Protection and Sustainability:**
        - **Marine pollution prevention**: Oil spill response, ballast water management, garbage disposal regulations
        - **Air emissions monitoring**: SOx, NOx, particulate matter from vessels, shore-based facilities
        - **Green shipping incentives**: Green Port Programme rewarding eco-friendly vessels with port dues rebates
        - **Alternative fuel infrastructure**: Facilitating LNG, methanol, ammonia bunkering capabilities
        
        **Standards, Compliance, and Certification:**
        - **Ship registration**: Singapore Registry of Ships (SRS), now 5th largest globally (108M GT)
        - **Crew certification**: STCW (Standards of Training, Certification and Watchkeeping) compliance
        - **Maritime labour standards**: ILO Maritime Labour Convention implementation, protecting seafarer rights
        - **International conventions**: IMO, SOLAS, MARPOL, Ballast Water Management implementation
        
        **Infrastructure Regulation and Oversight:**
        - **Port facility licensing**: Terminal operators, warehouses, dangerous goods facilities
        - **Terminal operator oversight**: Performance monitoring, safety audits, contract compliance
        - **Navigational aids maintenance**: Lighthouses, beacons, buoys, electronic navigation systems
        - **Hydrographic surveys**: Maintaining accurate charts, monitoring channel depths, dredging oversight
        
        **Why Regulation Matters:**
        
        Singapore's reputation as a **high-quality, safe, and secure port** attracts premium shipping lines and cargo.
        Rigorous standards ensure:
        - Vessels can call safely without collision or grounding risks
        - Cargo is secure from theft, damage, or security threats
        - Environmental impacts are minimised and controlled
        - International best practices are consistently maintained
        
        This reputation enables Singapore to **charge premium port dues** compared to lower-standard competitors,
        whilst shipping lines willingly pay because the reliability and safety justify the cost.
        """)
    
    with col2:
        st.markdown("""
        **Role 2: DEVELOPER - Growth, Innovation, Strategy**
        
        **Industry Promotion and Development:**
        - **Maritime cluster building**: Attracting shipping companies, financiers, law firms, technology providers
        - **Shipping line engagement**: Negotiating long-term commitments, understanding service requirements
        - **Business facilitation**: Streamlining approvals, providing incentives, removing regulatory barriers
        - **Investment attraction**: Tax incentives, grants, co-funding schemes for maritime businesses
        - **Trade route development**: Working with shipping lines to establish new services, increase frequencies
        
        **Innovation and Digital Transformation:**
        - **digitalPORT@SG programme**: AI-powered port operations, predictive maintenance, digital twins
        - **digitalOCEANS initiative**: Maritime domain awareness platform integrating multiple data sources
        - **R&D funding**: Co-funding research projects through Maritime Innovation and Technology (MINT) Fund
        - **Test-bedding facilities**: Providing real-world testing environments for new technologies
        - **Innovation programmes**: BLOCK71 maritime tech accelerator, startup support ecosystem
        
        **Human Capital and Talent Development:**
        - **Maritime training programmes**: Singapore Maritime Academy, professional certifications
        - **Scholarships and bursaries**: Maritime Singapore Connect scholarship scheme, undergraduate support
        - **Industry-academic partnerships**: Collaboration with NUS, NTU, SUTD on maritime programmes
        - **Workforce transformation**: SkillsFuture programmes for upskilling workers displaced by automation
        - **Attracting global talent**: Employment passes, permanent residency pathways for maritime professionals
        
        **Strategic Infrastructure Planning:**
        - **Long-term port master planning**: 20-30 year horizon, anticipating future vessel sizes and volumes
        - **Tuas Mega Port development**: S&#36;20 billion investment, ultimate 65M TEU capacity, world's largest automated port
        - **International partnerships**: Sister port agreements, green shipping corridors, collaborative initiatives
        - **Modal integration**: Sea-air, sea-rail connections, hinterland logistics development
        
        **Why Development Matters:**
        
        Without active development, even the best-regulated port will stagnate as competitors innovate and improve.
        MPA's developer role ensures Singapore:
        - Continuously invests in next-generation infrastructure (Tuas)
        - Attracts cutting-edge maritime technology and companies
        - Develops skilled workforce for future automation era
        - Maintains relevance as industry evolves (alternative fuels, digitization)
        
        The development function provides **forward momentum**, ensuring Singapore stays ahead of regional competitors
        through continuous improvement and strategic foresight.
        """)
    
    st.markdown("""
    **The Power of Integration: Why the Dual Role Works**
    
    **Coordinated Strategy Without Internal Conflict:**
    
    In most countries, port regulation and development are split between different government agencies, creating
    potential conflicts:
    - **Regulators** prioritise safety and security → may slow development with excessive caution
    - **Developers** prioritise growth and investment → may pressure regulators to lower standards
    
    Singapore's **unified MPA structure** eliminates this conflict through **single leadership** that balances both
    imperatives. When MPA plans Tuas development, the same organisation ensures:
    - **Safety standards** integrated from design phase (not imposed afterwards)
    - **Environmental requirements** built into specifications (not retrofit compliance)
    - **Operational efficiency** maximised whilst maintaining safety (optimised balance)
    - **Innovation encouraged** within appropriate regulatory guardrails (managed risk-taking)
    
    **Responsive and Adaptive Governance:**
    
    The dual role enables **rapid policy adaptation** to industry needs. When COVID-19 disrupted crew changes globally:
    - **MPA as regulator**: Temporarily relaxed restrictions whilst maintaining safety
    - **MPA as developer**: Worked with shipping lines to facilitate safe crew change protocols
    - **Coordination**: Implemented within weeks, not months of inter-agency negotiation
    
    When Red Sea crisis (2024) diverted vessels through Cape of Good Hope, causing Singapore port congestion:
    - **MPA as regulator**: Permitted night-tow operations at Pasir Panjang Terminal (first time)
    - **MPA as developer**: Fast-tracked commissioning of new Tuas berths, reactivated Keppel Terminal berths
    - **Coordination**: Worked with PSA, unions, and shipping lines to optimise schedules
    - **Result**: Most container vessels completed cargo handling and bunkering within one day despite disruption
    
    **Long-Term Vision Execution:**
    
    The Tuas Mega Port exemplifies the dual role advantage:
    
    **MPA as Developer:**
    - Conceived 65M TEU mega port concept in 2000s
    - Allocated S&#36;20 billion budget for 40-year development
    - Designed world's largest fully automated terminal
    - Negotiated long-term commitments from shipping alliances
    
    **MPA as Regulator:**
    - Ensured comprehensive environmental impact assessment
    - Integrated pollution prevention from design phase
    - Required shore power capability for all berths
    - Mandated cybersecurity standards for automation systems
    
    **Integration Benefit:**
    - Tuas will be simultaneously the **most efficient** (developer goal) and **safest, cleanest** (regulator goal)
      port globally
    - No compromises required—both objectives embedded from inception
    - Industry confidence: Shipping lines know Tuas will meet highest standards whilst maximising their operational
      efficiency
    
    **The Strategic Advantage:**
    
    According to lecture materials, Singapore's approach delivers: **"Coordinated strategy enables long-term vision...
    Infrastructure planning aligned with regulatory framework... Innovation encouraged within safety boundaries...
    Sustainable development prioritised."**
    
    This unified strategic direction, spanning decades, provides **certainty** for businesses making long-term
    investments. Shipping lines signing 20-30 year terminal leases at Tuas know Singapore's government will maintain
    consistent, supportive policies through both regulatory and developmental functions.
    """)
    
    # ============================================================================
    # SECTION 3: The Complete Maritime Cluster - Seven Pillars
    # ============================================================================
    
    st.markdown('<p class="section-header">The Complete Maritime Cluster: Seven Interdependent Pillars</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore's maritime ecosystem extends far beyond container terminals and cargo cranes. The **comprehensive
    maritime cluster** encompasses seven interconnected pillars, each providing essential services that reinforce
    the others. This "one-stop shop" approach creates powerful synergies: a shipping company can handle financing,
    insurance, legal work, crew changes, ship repairs, bunkering, and cargo operations all within Singapore—often
    within the same day—without coordination across multiple countries.
    """)
    
    st.markdown('<p class="subsection-header">The Seven Pillars Explained</p>', unsafe_allow_html=True)
    
    # Comprehensive maritime cluster data
    cluster_components = pd.DataFrame({
        'Pillar': [
            '1. Port and Terminal Operations',
            '2. Shipping and Liner Services',
            '3. Ship Repair and Shipbuilding',
            '4. Maritime Ancillary Services',
            '5. Maritime Finance and Insurance',
            '6. Maritime Law and Arbitration',
            '7. Maritime Technology and Innovation'
        ],
        'Key Players': [
            'PSA International, Jurong Port, cargo handlers, stevedores',
            '170+ international shipping groups (liner, bulk, tanker, management)',
            'Sembcorp Marine, Keppel Offshore & Marine, 40+ shipyards',
            'Bunker suppliers (50+ companies), ship chandlers, crew managers',
            '20+ banks, marine insurers, 10 IG P&I Clubs, ship brokers',
            '30+ law firms with shipping practice, arbitration centres',
            '~100 MarineTech startups, research institutes, universities'
        ],
        'Services Provided': [
            'Container/cargo handling, storage, transshipment, customs clearance',
            'Liner services (200+ lines), vessel operations, freight forwarding, ship management',
            'Dry-docking, major repairs, retrofits, conversions, new ship construction',
            'Bunkering (54.9M tonnes/year), provisions, crew changes, spare parts, supplies',
            'Ship financing, project finance, mortgages, hull insurance, cargo insurance, P&I coverage',
            'Maritime disputes resolution, contracts, admiralty law, arbitration, mediation',
            'Automation, AI, IoT, blockchain, alternative fuels, digitalization, R&D'
        ],
        'Annual Volume/Value': [
            '41.12M TEU containers (2024), 622.67M tonnes cargo',
            '170+ groups managing thousands of vessels globally',
            'World-class repair capability, ~100 vessels in yards at any time',
            '54.92M tonnes bunkers (world\'s largest), thousands of crew changes monthly',
            'S&#36;4.3B+ business spending, billions in ship loans outstanding',
            'Hundreds of cases annually, growing arbitration caseload',
            '~S&#36;50M raised by startups in 4 years, extensive R&D spending'
        ],
        'Strategic Importance': [
            'Core revenue generator, employs thousands, defines Singapore port status',
            'Brings cargo volumes, determines ship calls, builds global connections',
            'Retains vessels in Singapore waters, high-value services, skilled employment',
            'Essential services attract ship calls, bunkering drives port visits',
            'Enables ship purchases/operations, spreads maritime risk globally',
            'Resolves disputes efficiently, protects contracts, supports transactions',
            'Future competitiveness, maintains technological edge, attracts talent'
        ]
    })
    
    st.dataframe(cluster_components, width='stretch', hide_index=True)
    
    st.markdown("""
    **Understanding the Synergies and Network Effects:**
    
    The seven pillars do not operate independently—they create a self-reinforcing ecosystem where strength in one
    pillar enhances all others:
    
    **Pillar 1 + Pillar 4 Synergy: Port Operations × Maritime Ancillary Services**
    
    Singapore's position as world's largest bunkering hub (Pillar 4) directly drives container port volumes (Pillar 1):
    - Vessels calling for bunkers also discharge/load containers
    - Combined port call amortises voyage costs over multiple services
    - Efficient operations enable same-day bunkering + cargo handling
    - Result: Singapore captures cargo that might otherwise skip the port
    
    **Pillar 2 + Pillar 5 Synergy: Shipping Lines × Maritime Finance**
    
    With 20+ banks having shipping portfolios (Pillar 5), shipping companies (Pillar 2) can:
    - Secure ship financing in Singapore with minimal friction
    - Tap multiple lenders for competitive terms
    - Bundle services: vessel operations, financing, cash management in one location
    - Result: 170+ international shipping groups establish regional headquarters in Singapore
    
    **Pillar 3 + Pillar 1 Synergy: Ship Repair × Port Operations**
    
    Ships requiring repairs (Pillar 3) often discharge/load cargo simultaneously (Pillar 1):
    - Dry-docking schedules coordinate with port calls
    - Repair work done whilst loading/unloading cargo
    - Minimises vessel downtime (time = money in shipping)
    - Result: Singapore's shipyards stay busy whilst port gains additional cargo
    
    **Pillar 7 + All Others: Maritime Technology Accelerating Everything**
    
    Maritime technology innovations (Pillar 7) enhance every other pillar:
    - **Port automation** (Pillar 1): Faster crane operations, optimised yard management
    - **Digital platforms** (Pillar 2): Simplified booking, tracking, documentation for shipping lines
    - **Predictive maintenance** (Pillar 3): Reduced repair downtime using AI analytics
    - **Bunker digitalisation** (Pillar 4): e-BDN (electronic bunker delivery notes), MFM monitoring
    - **Fintech solutions** (Pillar 5): Blockchain-based trade finance, digital letters of credit
    - **Legaltech** (Pillar 6): Online dispute resolution, smart contracts, digital arbitration
    
    **The "One-Stop Shop" Competitive Advantage:**
    
    This comprehensive ecosystem creates **enormous convenience** for maritime businesses. Consider a shipping company's
    typical needs in Singapore:
    
    **Day 1 - Operational Services:**
    - **0600 hours**: Vessel arrives, berths immediately (BOA >90%)
    - **0630 hours**: Commence cargo operations with 6 cranes (Pillar 1)
    - **0700 hours**: Bunker vessel simultaneously with cargo ops (Pillar 4)
    - **0800 hours**: Crew change: 15 seafarers off, 15 on (Pillar 4)
    - **1200 hours**: Ship chandler delivers provisions, spare parts (Pillar 4)
    - **1800 hours**: Cargo ops + bunkering complete (12 hours for 3,000 moves + 2,000 tonnes bunkers)
    - **1900 hours**: Vessel departs for next port
    
    **Day 2 - Business Services:**
    - **0900 hours**: Meeting with ship financier to discuss newbuild loan (Pillar 5)
    - **1100 hours**: Review P&I insurance coverage with underwriter (Pillar 5)
    - **1400 hours**: Consult maritime lawyer on charter party dispute (Pillar 6)
    - **1600 hours**: Visit shipyard to inspect vessel undergoing retrofit (Pillar 3)
    
    **Week - Technology and Innovation:**
    - Pilot AI-powered predictive maintenance system developed by local startup (Pillar 7)
    - Test new digital bunkering platform reducing paperwork by 80% (Pillar 7)
    - Evaluate shore power connections for fleet decarbonisation (Pillar 7)
    
    **Result**: All maritime needs met in **one location**, with **minimal coordination** across time zones or
    jurisdictions, in **English** (business language), under **predictable legal framework** (Singapore commercial law).
    
    Compare this to alternative scenarios:
    - **Port in Country A**: Excellent terminal, but limited bunkering, must fly to Country B for ship financing
      meetings, legal disputes heard in Country C courts with multi-year delays
    - **Singapore**: Everything available locally, in same time zone, often same building, under consistent regulations
    
    **The Switching Cost Reality:**
    
    Once a shipping company establishes Singapore operations, relocating means:
    - **Lost banking relationships** built over years (20+ banks to choose from in Singapore, maybe 2-3 elsewhere)
    - **Rebuilding legal network** (30+ maritime law firms in Singapore, comprehensive expertise)
    - **New bunker suppliers** (losing world's largest, most competitive bunkering market)
    - **Finding alternative ship repair** (world-class yards in Singapore vs uncertain alternatives)
    - **Retraining staff** on different country's regulations, procedures, systems
    - **Losing efficiencies** of co-located services, time zone advantages, English working language
    
    These **astronomical switching costs** (likely millions of dollars + years of relationship rebuilding) mean
    companies almost never leave Singapore once established. This creates **extraordinarily sticky** customer
    relationships—precisely what Singapore's maritime cluster strategy intended to achieve.
    """)
    
    # ============================================================================
    # SECTION 4: Digital Transformation - Maritime 4.0
    # ============================================================================
    
    st.markdown('<p class="section-header">Digital Transformation: Positioning Singapore for Maritime 4.0</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore recognises that maintaining maritime leadership in the 21st century requires not just physical
    infrastructure but **digital infrastructure** and **technological innovation**. MPA's digital transformation
    initiatives position Singapore at the forefront of "Maritime 4.0"—the digital revolution transforming shipping
    through AI, IoT, blockchain, and automation.
    """)
    
    st.markdown('<p class="subsection-header">digitalPORT@SG: The Smart Port Initiative</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **digitalPORT@SG** is Singapore's comprehensive programme to transform port operations through digital technologies,
    automation, and data analytics. Launched by MPA, this initiative aims to make Singapore the world's smartest and
    most efficient port.
    
    **Core Components and Technologies:**
    
    **1. Port Operations Digital Twin**
    
    A complete virtual replica of Singapore's port operations running in real-time:
    - **3D visualization**: Every berth, crane, container, vessel represented digitally
    - **Real-time synchronisation**: Digital twin updates instantly as physical port changes
    - **Predictive simulation**: Test different scenarios (berth assignments, crane deployments) virtually before
      implementation
    - **Optimization algorithms**: AI identifies most efficient resource allocation across entire port system
    - **Impact**: Reduces vessel waiting time, optimizes crane utilisation, maximises throughput
    
    **What-if Analysis Example:**
    - Question: "If three mega vessels arrive simultaneously during peak cargo period, what's optimal berth assignment?"
    - Digital twin: Simulates 1,000+ allocation scenarios in seconds, identifies configuration minimising total
      turnaround time
    - Implementation: Port operators follow digital twin recommendation, avoiding bottlenecks
    
    **2. Predictive Maintenance Using AI and IoT**
    
    Preventing equipment failures before they occur:
    - **IoT sensors**: Thousands deployed on cranes, AGVs, yard equipment measuring vibration, temperature, load, cycles
    - **Real-time monitoring**: Data streams to central analytics platform 24/7
    - **AI pattern recognition**: Machine learning identifies equipment degradation patterns predicting failures weeks
      in advance
    - **Preventive intervention**: Maintenance scheduled during planned downtime, avoiding emergency repairs during
      critical cargo operations
    - **Impact**: >50% reduction in unplanned downtime, extended equipment lifespan, reduced maintenance costs
    
    **Real-World Impact:**
    - **Before AI**: Crane breaks down unexpectedly during mega vessel operation → 4-hour emergency repair → vessel
      delayed → schedule disruption cascades to feeder connections
    - **After AI**: Sensor data predicts bearing failure 3 weeks ahead → maintenance scheduled during vessel's planned
      absence → no operational disruption
    
    **3. Next-Generation Port Management Systems**
    
    Replacing legacy systems with cloud-based, AI-powered platforms:
    - **Dynamic berth planning**: Real-time optimization considering vessel size, draft, cargo volume, crane availability,
      pilot schedules
    - **Automated gate operations**: Truck identification via license plate recognition, automated documentation, paperless
      processing
    - **Intelligent yard management**: AI determines optimal container stacking positions minimising future re-handles
    - **Real-time visibility**: All stakeholders (shipping lines, truckers, customs, forwarders) see same information
      simultaneously
    
    **4. Blockchain for Trade Documentation**
    
    Eliminating paper documents through distributed ledger technology:
    - **Electronic Bill of Lading (eBL)**: Digital equivalent of paper B/L, legally recognised, fraud-proof
    - **Smart contracts**: Automated payment release when conditions met (cargo delivered, documents verified)
    - **Shared visibility**: All parties in supply chain see document status, approvals, changes in real-time
    - **Reduced fraud risk**: Blockchain immutability prevents document tampering, duplicate financing
    
    **Benefits Realised:**
    - **Time savings**: Documentation processing cut from 5-7 days to 1 day
    - **Cost reduction**: Estimated &#36;50-100 per container in administrative costs eliminated
    - **Fraud prevention**: Blockchain prevents duplicate bills of lading (historical problem in trade finance)
    """)
    
    st.markdown('<p class="subsection-header">digitalOCEANS: Maritime Domain Awareness Platform</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **digitalOCEANS** is Singapore's integrated maritime domain awareness platform, providing comprehensive situational
    awareness across Singapore's waters and beyond.
    
    **Platform Capabilities:**
    
    **Integrated Data Sources:**
    - **Vessel tracking**: AIS (Automatic Identification System) data from all vessels in Singapore waters
    - **Port operations**: Real-time berth occupancy, cargo operations, pilot boat movements
    - **Weather and oceanographic**: Wave heights, currents, visibility, wind for navigation safety
    - **Environmental monitoring**: Water quality, oil spill detection, marine debris tracking
    - **Security surveillance**: Integrated with maritime security systems, unauthorized vessel detection
    
    **Advanced Analytics and AI:**
    - **Anomaly detection**: AI identifies unusual vessel behavior (potential security threats, navigation violations)
    - **Predictive ETA**: Machine learning predicts accurate vessel arrival times considering weather, traffic, speed
    - **Route optimization**: Suggests optimal routes considering traffic, weather, fuel efficiency
    - **Risk assessment**: Evaluates collision risks, grounding risks, security threats automatically
    
    **Applications and Use Cases:**
    
    **1. Vessel Traffic Management:**
    - **Real-time monitoring**: VTS operators see every vessel in Singapore Strait (80,000+ annual transits)
    - **Collision prevention**: AI warns when vessels on collision course, suggests course corrections
    - **Congestion management**: Optimizes anchorage allocation during peak periods (Red Sea crisis response 2024)
    
    **2. Port Efficiency:**
    - **Accurate ETAs**: Shipping lines, port operators, pilots all working from same arrival prediction
    - **Resource planning**: Pilots, tugs, berths, cranes allocated efficiently based on actual vessel movements
    - **Just-in-time operations**: Minimises waiting time, maximises asset utilisation
    
    **3. Environmental Protection:**
    - **Emissions monitoring**: Tracks vessel emissions, enforces compliance with IMO regulations
    - **Oil spill response**: Rapid detection and response coordination
    - **Marine life protection**: Routes vessels away from sensitive marine habitats
    
    **4. Security and Safety:**
    - **Threat detection**: Identifies suspicious vessels, unauthorized entries, potential security risks
    - **Search and rescue**: Coordinates SAR operations with real-time vessel positions, capabilities
    - **Accident investigation**: Complete data trail for post-incident analysis
    """)
    
    # ============================================================================
    # SECTION 5: Innovation Ecosystem - BLOCK71, MINT Fund, Academic Partnerships
    # ============================================================================
    
    st.markdown('<p class="section-header">The Maritime Innovation Ecosystem: Cultivating Maritime 4.0</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore has systematically built a comprehensive innovation ecosystem to ensure it remains the global leader
    in maritime technology. This ecosystem connects startups, corporates, government, research institutions, venture
    capital, and academic institutions—creating a **vibrant innovation flywheel** where technology development,
    testing, and commercialisation happen seamlessly.
    """)
    
    st.markdown('<p class="subsection-header">BLOCK71 Maritime Innovation Hub</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **BLOCK71** represents Singapore's flagship maritime technology accelerator, established in **2018** by MPA as
    the **first maritime ecosystem innovation builder in the region**. BLOCK71's mission, according to lecture
    materials, is to **"catalyse the acceleration of innovation and transformation in the maritime industry."**
    
    **The Three-Part Strategy:**
    
    **1. Encourage Maritime Industry Innovation**
    
    Goal: Push traditional maritime companies to **"accelerate innovation and venture into adjacent/new growth areas
    through working with tech start-ups."**
    
    - **Challenge**: Established maritime companies (shipping lines, port operators, ship managers) often risk-averse,
      slow to adopt new technologies
    - **BLOCK71 Solution**: Provides safe environment for corporates to experiment with startup technologies at low risk
    - **Mechanism**: Pilot projects where startups deploy solutions in controlled settings (e.g., test automated mooring
      system on one berth before fleet-wide rollout)
    
    **2. Attract Global Maritime Technology Talent**
    
    Goal: **"Attract, connect and groom innovative global tech start-ups/entrepreneurs and private capitals to build
    capability and solutions for our maritime industry."**
    
    - **Global recruitment**: Actively scout maritime technology startups worldwide, offer relocation support to
      Singapore
    - **Funding access**: Connect startups with venture capital, government grants (MINT Fund), corporate investors
    - **Market access**: Singapore maritime cluster provides immediate customers (170+ shipping groups, PSA terminals,
      shipyards)
    - **Talent pool**: Access to maritime engineering graduates from NUS, NTU, Singapore Maritime Academy
    
    **3. Strengthen Singapore's Maritime Innovation Hub Status**
    
    Goal: **"Strengthen Singapore as a global maritime hub for innovation and talents."**
    
    - **Ecosystem development**: BLOCK71 creates visible innovation centre attracting additional startups, investors, talent
    - **Success breeds success**: Each successful startup attracts more entrepreneurs, more capital, more attention
    - **Network effects**: Larger ecosystem provides better matching between problems (from maritime companies) and
      solutions (from startups)
    
    **Focus Areas and Technologies:**
    
    BLOCK71 prioritises technologies addressing major maritime challenges:
    
    - **Autonomous vessels and robotics**: Unmanned surface vehicles, autonomous tugs, robotic inspection drones
    - **AI and data analytics**: Predictive maintenance, route optimization, fuel efficiency algorithms
    - **Cybersecurity**: Protecting vessels and port systems from cyber attacks (growing threat with digitization)
    - **Green technologies**: Alternative fuel solutions, energy efficiency systems, emissions monitoring
    - **Blockchain and digital trade**: Electronic documentation, smart contracts, supply chain visibility
    - **IoT and sensors**: Real-time monitoring of containers, vessels, port equipment, environmental conditions
    
    **The BLOCK71 Innovation Process:**
    
    **Stage 1: Application and Selection**
    - Startups apply with maritime innovation proposals
    - Selection criteria: Technology potential, team capability, market fit, scalability
    - Competitive process: Only strongest ideas selected (maintains quality)
    
    **Stage 2: Acceleration Programme**
    - **Funding support**: Grants, pitch opportunities to VCs, corporate investors
    - **Mentorship**: Maritime industry veterans, successful entrepreneurs, technical experts
    - **Workspace**: Co-working space in Singapore, access to testing facilities
    - **Curriculum**: Business model development, go-to-market strategy, IP protection, fundraising
    - **Duration**: Typically 3-6 months intensive acceleration
    
    **Stage 3: Pilot Projects**
    - **Real-world testing**: Deploy technology with actual maritime customers (PSA, shipping lines, yards)
    - **Risk mitigation**: Controlled scope, support from BLOCK71, insurance coverage if needed
    - **Data collection**: Measure performance, ROI, operational impact
    - **Iteration**: Refine solution based on real operational feedback
    
    **Stage 4: Commercialisation and Scale**
    - **Successful pilots**: Full commercial deployment with pilot customer
    - **Reference customers**: Singapore maritime companies become showcase clients for global sales
    - **Geographic expansion**: Use Singapore success to enter other markets (China, Europe, Americas)
    - **Fundraising**: Successful pilots unlock Series A/B funding from VCs
    
    **Success Metrics and Impact:**
    
    According to lecture materials:
    - **~100 MarineTech startups** supported through ecosystem
    - **~S&#36;50 million in investment** raised by startups in past 4 years
    - **Multiple commercial deployments**: Technologies now operational in Singapore port, ships
    - **Global reach**: Singapore-incubated technologies expanding to international markets
    
    **Real-World Impact:**
    - Autonomous vessel technology tested in Singapore waters now deployed commercially
    - AI-powered predictive maintenance systems reducing port equipment downtime
    - Blockchain trade documentation platforms processing thousands of transactions
    - Green technology startups developing alternative fuel bunkering solutions
    """)
    
    st.markdown('<p class="subsection-header">Maritime Innovation and Technology (MINT) Fund</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The **MINT Fund** complements BLOCK71 by providing **co-funding for maritime R&D projects and technology test-bedding**.
    This government funding mechanism reduces financial risk for companies experimenting with unproven technologies.
    
    **How MINT Fund Works:**
    
    **Funding Structure:**
    - **Government co-funding**: MPA funds up to **50% of eligible project costs**
    - **Company contribution**: Remainder funded by company (ensures skin in the game, commitment)
    - **Maximum grants**: Varies by project scope, typically S&#36;500K - S&#36;2M for major initiatives
    - **No equity requirement**: Unlike VC funding, MINT is grant-based (government doesn't take company shares)
    
    **Eligible Projects:**
    - **Digitalisation and automation**: AI systems, robotics, IoT implementations
    - **Green and sustainable technologies**: Alternative fuels, emissions reduction, energy efficiency
    - **Safety and security enhancements**: Cybersecurity, navigation safety, port security
    - **Productivity improvements**: Process automation, workflow optimization, data analytics
    - **Novel business models**: Platform businesses, sharing economy applications, new service concepts
    
    **Application Process:**
    - **Proposal submission**: Company describes technology, expected benefits, timeline, budget
    - **Technical evaluation**: MPA experts assess feasibility, innovation level, potential impact
    - **Funding approval**: Fast decision process (typically 2-3 months) to maintain momentum
    - **Milestone-based disbursement**: Funding released as project achieves agreed milestones
    - **Reporting requirements**: Regular updates, final report documenting results
    
    **Strategic Rationale:**
    
    **Why Government Co-Funding?**
    - **Market failure**: Companies under-invest in R&D due to uncertain returns, competitor free-riding
    - **Positive externalities**: Benefits extend beyond funding recipient (e.g., port automation benefits all users)
    - **Risk reduction**: Sharing costs makes marginal projects viable, accelerates innovation adoption
    - **Local capability building**: Ensures Singapore companies develop expertise, don't just buy foreign solutions
    
    **Example MINT-Funded Projects:**
    
    **Project 1: AI-Powered Berth Planning System**
    - **Challenge**: Manual berth allocation suboptimal, vessels waiting for optimal berths
    - **Solution**: AI system optimizing berth assignments considering 20+ variables
    - **MINT contribution**: S&#36;800K (50% of S&#36;1.6M total cost)
    - **Company contribution**: S&#36;800K
    - **Result**: 15% reduction in average vessel waiting time, system now deployed operationally
    
    **Project 2: Autonomous Tug Vessel**
    - **Challenge**: Tug operations dangerous (collisions, line handling accidents), costly (crew wages)
    - **Solution**: Retrofit existing tug with autonomous navigation, remote operation capability
    - **MINT contribution**: S&#36;1.2M (50% of S&#36;2.4M project)
    - **Company contribution**: S&#36;1.2M
    - **Result**: Successful trials, regulatory approval process underway for commercial operations
    
    **Project 3: Blockchain-Based Bunker Delivery System**
    - **Challenge**: Paper-based bunker delivery notes prone to errors, delays, disputes
    - **Solution**: Digital platform using blockchain for tamper-proof delivery documentation
    - **MINT contribution**: S&#36;400K (50% of S&#36;800K development cost)
    - **Company contribution**: S&#36;400K
    - **Result**: Now mandatory for all bunker suppliers in Singapore (April 2025), industry-wide adoption
    
    **Impact on Singapore's Maritime Sector:**
    
    MINT Fund achieves multiple strategic objectives simultaneously:
    - **Accelerates innovation**: Projects happen sooner, at larger scale than if companies self-funded
    - **De-risks experimentation**: Companies willing to try riskier, more ambitious technologies
    - **Builds local capabilities**: Singapore companies develop expertise, potentially export solutions globally
    - **Attracts investment**: Successful MINT projects attract VC follow-on funding, scale companies
    - **Maintains competitiveness**: Ensures Singapore maritime sector stays technologically advanced
    """)
    
    st.markdown('<p class="subsection-header">Academic and Research Partnerships</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore's maritime innovation ecosystem is anchored by strong academic research capabilities, connecting
    universities, research institutes, and maritime companies in **collaborative R&D that solves real-world problems**.
    
    **Key Academic Institutions:**
    
    **Singapore Maritime Institute (SMI):**
    - **Role**: Coordinating body for maritime R&D in Singapore
    - **Function**: Funds research projects, connects academia with industry, disseminates research findings
    - **Focus areas**: Port automation, sustainable shipping, supply chain resilience, maritime technology
    - **Funding**: Government grants for multi-year research programmes
    - **Output**: Research papers, patents, technology prototypes for commercial development
    
    **Universities with Maritime Programmes:**
    
    **National University of Singapore (NUS):**
    - **Department of Civil and Environmental Engineering**: Maritime infrastructure, port operations research
    - **Centre for Maritime Studies**: Industry-focused research on shipping economics, logistics, policy
    - **Research strengths**: Computational fluid dynamics (ship design), offshore structures, port optimization
    - **Industry collaboration**: Joint projects with PSA, shipping companies, MPA on real operational challenges
    
    **Nanyang Technological University (NTU):**
    - **School of Mechanical and Aerospace Engineering**: Ship propulsion, energy efficiency, alternative fuels
    - **Maritime Energy and Sustainable Development (MESD) Centre of Excellence**: Green shipping research
    - **Research strengths**: Alternative fuel combustion, LNG bunkering, methanol/ammonia feasibility studies
    - **Industry collaboration**: Working with bunker suppliers, engine manufacturers, classification societies
    
    **Singapore University of Technology and Design (SUTD):**
    - **Engineering Systems and Design**: Complex systems engineering for ports and shipping
    - **iTrust Centre**: Maritime cybersecurity research (protecting vessels and port systems from cyber attacks)
    - **Research strengths**: Systems thinking, cybersecurity, automation, human-machine interaction
    - **Industry collaboration**: MariOT testbed for ship operational technology cybersecurity testing
    
    **Research Focus and Industry Relevance:**
    
    **1. Autonomous Vessels and Navigation**
    - **Academic research**: Collision avoidance algorithms, sensor fusion, machine learning for navigation
    - **Industry need**: Addressing seafarer shortage, improving safety, reducing costs
    - **Test facilities**: Real-world trials in Singapore waters with regulatory support
    - **Commercial pathway**: Startups licensing university technology, deploying on actual vessels
    
    **2. Alternative Fuels and Decarbonisation**
    - **Academic research**: Methanol/ammonia combustion, hydrogen fuel cells, biofuel sustainability
    - **Industry need**: IMO 2050 net-zero target, short-term emissions reduction requirements
    - **Test facilities**: Engine test benches, emissions measurement, fuel quality analysis
    - **Commercial pathway**: Bunker suppliers using research to develop commercial-scale alternative fuel offerings
    
    **3. Port Automation and Optimization**
    - **Academic research**: AI planning algorithms, robotic systems, digital twin simulations
    - **Industry need**: Handling growing cargo volumes without proportional workforce increase
    - **Test facilities**: Port simulators, robotics laboratories, PSA terminals for real-world testing
    - **Commercial pathway**: Technology companies commercialising university algorithms, deploying at ports globally
    
    **4. Supply Chain Resilience**
    - **Academic research**: Network analysis, risk modeling, disruption recovery strategies
    - **Industry need**: COVID-19, Suez blockage, Red Sea crisis exposed supply chain vulnerabilities
    - **Test facilities**: Supply chain simulation labs, data from actual shipping networks
    - **Commercial pathway**: Consulting firms using research insights, shipping lines adopting risk management frameworks
    
    **5. Maritime Cybersecurity**
    - **Academic research**: Threat detection, vulnerability assessment, secure system design
    - **Industry need**: Growing digitization creates attack surface, critical infrastructure protection
    - **Test facilities**: MariOT testbed (world's first maritime OT cybersecurity facility)
    - **Commercial pathway**: Cybersecurity companies developing solutions specifically for maritime systems
    
    **Student Involvement and Talent Pipeline:**
    
    **Undergraduate Programmes:**
    - **Maritime engineering degrees**: NUS, NTU offering specialized maritime programmes
    - **Internships**: Students work on real industry projects (PSA operations, shipping line analytics)
    - **Final year projects**: Industry-sponsored research addressing actual operational problems
    - **Guaranteed employment**: Maritime companies hire from programs, ensuring talent supply
    
    **Graduate Programmes:**
    - **Master's programmes**: Specialized maritime programmes (shipping, ports, logistics)
    - **Ph.D. research**: Deep technical research on cutting-edge maritime challenges
    - **Industry funding**: Companies sponsor research students tackling their technical problems
    - **Career pathway**: Many graduates join maritime companies, startups, or government agencies
    
    **Knowledge Transfer Mechanisms:**
    
    **Industry Seminars and Workshops:**
    - **Regular knowledge sharing**: Universities host industry events presenting research findings
    - **Attendance**: Maritime executives, engineers, policymakers learn latest developments
    - **Two-way dialogue**: Industry feedback shapes future research directions
    
    **Collaborative Projects:**
    - **Industry-academic teams**: Professors work alongside company engineers on joint projects
    - **IP arrangements**: Clear frameworks for commercialising research (licensing, spin-offs)
    - **Government facilitation**: Grants specifically for industry-academic collaboration
    
    **Technology Transfer:**
    - **University spin-offs**: Startups founded by professors, students commercialising research
    - **Licensing agreements**: Companies licensing university patents, algorithms, designs
    - **Consulting**: Academics advising companies on technical challenges, strategic directions
    
    **Strategic Impact:**
    
    The academic-industry ecosystem ensures Singapore maintains **technological leadership** through:
    - **Continuous innovation pipeline**: Universities constantly generating new ideas, technologies
    - **Talent development**: Graduates with both theoretical knowledge and practical industry experience
    - **Global recognition**: Top-tier research attracts international talent, investment, partnerships
    - **Competitive advantage**: Technologies developed in Singapore deployed first locally, then exported globally
    """)
    
    # ============================================================================
    # SECTION 6: Sustainability and Green Maritime Initiatives
    # ============================================================================
    
    st.markdown('<p class="section-header">Positioning Singapore as a Green Maritime Leader</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore is strategically positioning itself as a global leader in maritime sustainability and decarbonisation.
    This positioning is not just environmental responsibility—it's **competitive strategy**. As the IMO's 2050 net-zero
    target drives industry transformation, Singapore aims to be the **preferred hub for green shipping**, capturing
    the next generation of maritime business through sustainability leadership.
    """)
    
    st.markdown('<p class="subsection-header">Green Port Programme: Incentivising Eco-Friendly Shipping</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore's **Green Port Programme** uses economic incentives to encourage shipping lines to invest in cleaner,
    more efficient vessels. The programme demonstrates how **market-based mechanisms** can drive environmental
    improvements whilst maintaining competitiveness.
    
    **How the Programme Works:**
    
    **Incentive Structure:**
    - **Port due rebates**: Vessels with superior environmental performance pay reduced port dues
    - **Tiered system**: Better performance = larger rebates (up to 75% discount on port dues)
    - **Immediate benefit**: Shipping lines see cost savings every port call, creating strong economic incentive
    
    **Assessment Criteria:**
    
    **1. Engine Emissions (NOx, SOx, Particulate Matter):**
    - **Tier III engines**: Highest rebate (85-90% reduction vs Tier I engines)
    - **Scrubber systems**: Vessels with SOx scrubbers qualify even with high-sulfur fuel
    - **Particulate filters**: Bonus for PM reduction systems
    
    **2. Energy Efficiency (CO₂ per tonne-mile):**
    - **EEDI/EEXI rating**: IMO's energy efficiency indices determine qualification
    - **Operational measures**: Slow steaming, optimized voyage planning rewarded
    - **Design efficiency**: Hull design, propulsion systems, energy recovery systems considered
    
    **3. Shore Power Capability:**
    - **Cold ironing readiness**: Vessels equipped to connect to shore power eligible for rebates
    - **Actual usage**: Additional rebates for actually using shore power during Singapore port calls
    - **Future requirement**: Tuas Port designed with universal shore power availability
    
    **Economic Impact on Shipping Lines:**
    
    **Cost-Benefit Analysis:**
    - **Investment**: Tier III engine vs Tier II costs &#36;500K - &#36;2M more per vessel
    - **Port due savings**: &#36;2,000 - &#36;5,000 per Singapore call (75% rebate)
    - **Singapore call frequency**: Major liners call 50-100 times annually
    - **Annual savings**: &#36;100K - &#36;500K per vessel in Singapore alone
    - **Payback period**: 1-4 years from Singapore savings alone, faster when all ports considered
    - **Competitive advantage**: As more ports adopt similar schemes, green vessels gain cost advantage globally
    
    **Strategic Rationale for Singapore:**
    
    **Why Offer Rebates?**
    - **First-mover advantage**: Pioneering port creates standard that others follow
    - **Network externality**: All ships become cleaner = better air quality for all
    - **Future-proofing**: Positions Singapore for increasingly strict global regulations
    - **Competitive differentiation**: "Green port" status attracts environmentally-conscious cargo owners
    - **Diplomatic benefit**: Demonstrates climate leadership, enhances Singapore's international standing
    """)
    
    st.markdown('<p class="subsection-header">Alternative Fuels Infrastructure: Multi-Fuel Future Strategy</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore recognises that maritime decarbonisation requires **multiple fuel pathways**—there is no single "winner"
    fuel that will dominate all vessel types and routes. Therefore, Singapore is developing **comprehensive alternative
    fuel infrastructure** across multiple fuel types, positioning as the **global leader** regardless of which fuels
    ultimately prevail.
    
    **2024 Alternative Fuel Bunker Sales Performance:**
    
    According to MPA, Singapore's alternative fuel bunker sales exceeded **1 million tonnes for the first time**,
    reaching **1.34 million tonnes in 2024** (year-on-year doubling from 2023):
    
    - **Biofuel blends**: 0.88 million tonnes (up from 0.52M in 2023)
      - B50 blends available commercially (50% biofuel, 50% conventional fuel)
      - B100 trials ongoing (100% biofuel)
      - Drop-in solution: Works with existing engines, no modifications required
    
    - **LNG (Liquefied Natural Gas)**: 0.46 million tonnes (up from 0.11M in 2023, 4× growth!)
      - Multiple LNG bunker vessels operational
      - Ship-to-ship bunkering well-established
      - Growing LNG-powered fleet (dual-fuel engines)
    
    - **Methanol**: 1,626 tonnes
      - Available on commercial scale in Singapore
      - Methanol-powered vessels increasing (Maersk, CMA CGM ordering methanol fleets)
      - Infrastructure expanding to meet anticipated demand
    
    - **Ammonia**: 9.74 tonnes
      - **World-first bunkering trials** conducted in Singapore (2024)
      - Proving technical feasibility, safety protocols
      - Infrastructure planning for 2030s commercial availability
    
    **Multi-Fuel Strategy Explained:**
    
    **Current Focus: LNG + Biofuels (2020s)**
    
    **LNG Infrastructure:**
    - **Multiple LNG bunker vessels** operating in Singapore waters
    - **Ship-to-ship bunkering** procedures established and proven safe
    - **LNG terminal capacity**: Leveraging existing LNG import terminal for bunkering
    - **Safety protocols**: Comprehensive regulations, training, emergency procedures
    - **Customer base**: Cruise ships, LNG carriers, new dual-fuel container ships all using LNG
    
    **Why LNG Now:**
    - **Proven technology**: LNG engines commercially mature, widely deployed
    - **Emissions reduction**: 20-25% CO₂ reduction vs conventional fuel, 85-90% SOx/NOx reduction
    - **Bridge fuel**: Reduces emissions today whilst awaiting zero-carbon alternatives
    - **Infrastructure exists**: Natural gas infrastructure can supply maritime demand
    
    **Biofuel Infrastructure:**
    - **Multiple suppliers**: Several companies offering biofuel blends in Singapore
    - **Blending facilities**: Can create B10, B20, B30, B50 blends to customer specification
    - **Quality assurance**: Testing labs ensure biofuel meets marine fuel specifications
    - **Supply chain**: Sustainable feedstock sourcing (waste oils, agricultural residues, not food crops)
    
    **Why Biofuels Now:**
    - **Drop-in compatibility**: Works with existing ships, engines, infrastructure (no vessel modifications)
    - **Immediate emissions reduction**: 60-80% lifecycle CO₂ reduction vs fossil fuels
    - **Scalability**: Production capacity growing globally
    - **Regulatory acceptance**: Approved by IMO as low-carbon fuel
    
    **Near-Term Developing: Methanol (Mid-2020s)**
    
    **Methanol Infrastructure Being Built:**
    - **Storage facilities**: Dedicated methanol storage tanks at bunker terminals
    - **Bunker vessels**: Methanol-capable bunker vessels under construction/conversion
    - **Safety systems**: Methanol-specific safety procedures (different hazards vs LNG or conventional fuel)
    - **Supply agreements**: Contracts with methanol producers (including green methanol from renewable sources)
    
    **Why Methanol Important:**
    - **Major carriers committed**: Maersk ordered 25+ methanol-powered vessels, CMA CGM following
    - **Easier handling than LNG**: Liquid at ambient temperature/pressure (simpler than cryogenic LNG)
    - **Green methanol potential**: Can be produced from renewable electricity + captured CO₂ (carbon-neutral)
    - **Dual-fuel engines**: New vessels being built with methanol/conventional dual-fuel capability
    
    **Future Preparing: Ammonia + Hydrogen (2030s)**
    
    **Ammonia (NH₃) Development:**
    - **World-first trials**: Singapore conducted **world's first ammonia bunkering trials** in 2024 (9.74 tonnes)
    - **Technical proving**: Demonstrating safe handling, transfer, storage procedures
    - **Infrastructure planning**: MPA coordinating with stakeholders on commercial-scale infrastructure requirements
    - **Timeline**: Significant ammonia fleet expected 2030s, Singapore positioning to serve them
    
    **Why Ammonia Matters:**
    - **Zero-carbon fuel**: Burns to produce only nitrogen and water (no CO₂ emissions)
    - **Existing distribution**: Ammonia already produced/traded globally (fertilizer industry)
    - **Energy density**: Higher than hydrogen, easier to store/transport
    - **Engine compatibility**: Ammonia engines under development by major manufacturers (MAN, Wärtsilä)
    
    **Hydrogen (H₂) Consideration:**
    - **Niche applications**: Likely limited to specialized vessels (short-distance ferries, offshore support)
    - **Storage challenges**: Cryogenic (-253°C) or high-pressure storage, low energy density
    - **Infrastructure complexity**: Requires completely new infrastructure, extremely expensive
    - **Singapore approach**: Monitor developments, ready to provide if demand materializes
    
    **The Strategic Flexibility Advantage:**
    
    **Why Multi-Fuel Strategy?**
    
    **Uncertainty about winning fuel**: No consensus yet on which fuel will dominate 2040s-2050s shipping
    - **LNG**: Good near-term but still fossil fuel (only ~20% CO₂ reduction)
    - **Biofuels**: Scalability questions (limited sustainable feedstock)
    - **Methanol**: Promising but production capacity needs massive scaling
    - **Ammonia**: Zero-carbon but toxicity concerns, engine technology still developing
    - **Hydrogen**: Ideal emissions but enormous infrastructure challenges, costs
    
    **Different fuels for different vessels**: One size does not fit all
    - **Short-sea ferries**: Hydrogen or battery-electric feasible
    - **Container ships**: Methanol or ammonia likely (need high-density fuel for long voyages)
    - **Bulk carriers**: LNG or ammonia (cost-sensitive, simpler engines)
    - **Cruise ships**: LNG currently (passenger safety paramount, proven technology)
    
    **Singapore's hedge strategy**: **Support all plausible fuels**, dominate regardless of which wins
    - **If LNG dominates**: Singapore already world's largest LNG bunker hub
    - **If methanol wins**: Singapore developing comprehensive methanol infrastructure
    - **If ammonia prevails**: Singapore proved technical feasibility first, infrastructure ready
    - **If multiple coexist**: Singapore the only hub offering all options (one-stop-shop advantage)
    
    **Competitive Positioning:**
    
    **Lock-in bunkering business regardless of fuel transition**: Singapore's investment in multi-fuel infrastructure
    ensures that as the global fleet transitions from conventional bunkers to alternatives, Singapore remains the
    **default bunkering location** because it offers **all fuel options**.
    
    Shipping lines appreciate this because:
    - **Fleet transition flexibility**: Can bunker different fuel types as fleet converts gradually
    - **Operational simplicity**: Don't need to route to different ports for different fuels
    - **Future-proof**: As fuel preferences shift, Singapore always has supply
    
    This locks in Singapore's position as **world's largest bunkering hub** for the next 30+ years of energy transition.
    """)
    
    st.markdown('<p class="subsection-header">Shore Power Infrastructure: Zero Emissions at Berth</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Shore power** (also called "cold ironing") allows vessels to shut down diesel generators whilst at berth,
    plugging into the port's electrical grid instead. This eliminates local air pollution and reduces CO₂ emissions
    (depending on grid electricity carbon intensity).
    
    **Tuas Mega Port Shore Power Plans:**
    
    According to MPA, Tuas Mega Port is being **designed with shore power capability at all berths**, representing
    the most ambitious shore power deployment globally:
    
    **Infrastructure Requirements:**
    - **High-voltage connections**: Each berth equipped with 6.6kV or 11kV shore power connections
    - **Frequency conversion**: Singapore grid operates at 50Hz, some vessels require 60Hz (converters installed)
    - **Multiple berths**: All Tuas berths (eventually 65M TEU capacity) will have shore power
    - **Automated connection**: Plug-in systems designed for rapid connection/disconnection
    
    **Environmental Impact:**
    - **Zero local emissions**: No diesel exhaust whilst at berth (improves air quality for port workers, nearby residents)
    - **CO₂ reduction**: Singapore grid ~70% natural gas, cleaner than vessel diesel generators
    - **Future improvement**: As Singapore grid decarbonises (solar, offshore wind, imported renewable electricity),
      shore power becomes carbon-neutral
    
    **Economic Considerations:**
    
    **For Shipping Lines:**
    - **Fuel savings**: Shore power cheaper than running diesel generators (grid electricity vs marine diesel)
    - **Engine maintenance**: Reduced generator runtime = lower maintenance costs, longer engine life
    - **Regulatory compliance**: Some jurisdictions (California, EU) requiring shore power usage
    
    **For Singapore:**
    - **Infrastructure investment**: ~S&#36;2-5 million per berth for shore power equipment
    - **Attractiveness**: Eco-conscious cargo owners prefer ports offering shore power
    - **Future-proofing**: As regulations tighten globally, shore power becomes necessity not option
    
    **Current Status:**
    - **Tuas Phase 1**: Shore power being incorporated into operational berths
    - **Incentives**: Green Port Programme offers additional rebates for vessels actually using shore power
    - **Adoption challenge**: Relatively few vessels currently equipped with shore power connections (retrofitting expensive)
    """)
    
    # ============================================================================
    # SECTION 7: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways: Understanding Maritime Singapore</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Record-Breaking 2024 Performance:**
        - Container throughput: **41.12M TEU** (first time crossing 40M)
        - Vessel arrivals: **3.11B GT** (new record, 130,000+ vessel calls)
        - Bunker sales: **54.92M tonnes** (world's largest, 6% growth)
        - Alternative fuels: **1.34M tonnes** (doubled from 2023, exceeded 1M milestone)
        - Ship registry: **108M GT** (5th largest globally, exceeded 100M GT first time)
        - **#1 International Maritime Centre** for **12th consecutive year**
        
        **Comprehensive Maritime Cluster:**
        - **170+ international shipping groups** (liner, bulk, tanker, management companies)
        - **30+ shipbroking firms** (facilitating global ship chartering, sales)
        - **20+ banks with shipping portfolios** (billions in ship financing)
        - **30+ maritime law firms** (disputes, contracts, arbitration)
        - **10 IG P&I Clubs** (covering 95% of world's ocean-going tonnage)
        - **~100 MarineTech startups** (raised ~S&#36;50M in 4 years)
        - **S&#36;4.3B+ business spending** in maritime services (2022)
        
        **MPA's Unique Dual Role:**
        - **Regulator**: Safety, security, standards, environment
        - **Developer**: Industry growth, innovation, talent, infrastructure
        - **Coordination benefit**: Long-term vision, rapid adaptation, aligned strategy
        - **Tuas exemplifies**: S&#36;20B investment combining efficiency with sustainability
        """)
    
    with col2:
        st.markdown("""
        **Digital Transformation Leadership:**
        - **digitalPORT@SG**: AI, digital twin, predictive maintenance, IoT sensors
        - **digitalOCEANS**: Maritime domain awareness, integrated data platform
        - **Electronic documentation**: eBL, e-BDN mandatory (April 2025), blockchain-based
        - **PORTNET evolution**: Singapore's maritime single window since 1980s continuously upgraded
        
        **Innovation Ecosystem:**
        - **BLOCK71**: First maritime innovation hub in region (est. 2018), accelerator for startups
        - **MINT Fund**: Co-funds up to 50% of R&D/pilot projects, de-risks innovation
        - **Academic partnerships**: SMI, NUS, NTU, SUTD providing research capabilities
        - **MariOT testbed**: World's first maritime cybersecurity testing facility
        - **Success stories**: 100+ startups, multiple commercial deployments, global technology exports
        
        **Green Maritime Leadership:**
        - **Green Port Programme**: Port due rebates (up to 75%) for eco-friendly vessels
        - **LNG bunkering**: 0.46M tonnes (2024), world-class infrastructure, 4× growth
        - **Biofuels**: 0.88M tonnes (2024), B50 commercial, B100 trials
        - **Methanol**: Commercial-scale supply available, infrastructure expanding
        - **Ammonia**: World-first bunkering trials completed (2024)
        - **Shore power**: All Tuas berths designed with shore power capability
        - **Multi-fuel strategy**: Hedging across all alternative fuel types
        
        **Strategic Switching Costs:**
        - Complete ecosystem creates **enormous relocation costs** for maritime businesses
        - Network effects strengthen over time (more players → more value → attracts more players)
        - Long-term government commitment provides **certainty** for major investments
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Singapore has systematically built the world's most comprehensive maritime 
    ecosystem over 70+ years, earning the #1 International Maritime Centre ranking for 12 consecutive years. The 2024 
    record-breaking performance (41.12M TEU containers, 3.11B GT vessel arrivals, 54.92M tonnes bunker sales) 
    demonstrates continued growth momentum despite global supply chain challenges. Beyond physical infrastructure, 
    Singapore offers a complete maritime cluster (170+ shipping groups, 30+ shipbroking firms, 20+ banks, 30+ law 
    firms, 100+ tech startups) providing every conceivable maritime service under one roof. MPA's globally unique dual 
    role as both regulator and strategic developer enables coordinated long-term planning exemplified by the S&#36;20 billion 
    Tuas Mega Port investment. Digital transformation initiatives (digitalPORT@SG, digitalOCEANS, mandatory electronic 
    documentation) position Singapore as a Maritime 4.0 leader. The innovation ecosystem (BLOCK71 accelerator, MINT 
    Fund co-financing, academic partnerships) cultivates maritime technology startups that benefit Singapore first before 
    scaling globally. Sustainability leadership through multi-fuel strategy (LNG, biofuels, methanol, ammonia), Green 
    Port Programme incentives, and universal shore power at Tuas prepares Singapore for maritime decarbonisation 
    regardless of which alternative fuel ultimately dominates. This comprehensive, integrated approach creates 
    <strong>extraordinarily high switching costs</strong> and powerful <strong>network effects</strong>—once maritime companies establish Singapore 
    operations, the ecosystem makes it economically rational to consolidate all their maritime services here, reinforcing 
    Singapore's position as the world's indispensable maritime hub.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** 🏆 Port Strategy & Competition - Explore the eight critical success factors for transshipment 
    hubs (efficiency, reliability, connectivity, infrastructure, workforce, location, government support, 
    technology), analyse competitive dynamics across gateway ports vs transshipment hubs, examine strategic planning 
    frameworks (SWOT analysis, Porter's Five Forces, scenario planning), understand Singapore's strategic response 
    to regional competition (Malaysia, Indonesia, Thailand, Vietnam), and master the "vital port in interconnected 
    network" philosophy versus the "biggest hub" mentality.
    """)
