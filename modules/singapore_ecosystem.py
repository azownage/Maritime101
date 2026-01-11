import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">🇸🇬 Maritime Singapore Ecosystem</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand Singapore's comprehensive maritime cluster, MPA's dual role as regulator and developer, 
    the complete ecosystem of maritime services, and cutting-edge innovation initiatives driving the 
    industry forward as Singapore maintains its position as the world's #1 maritime centre.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Singapore's Maritime Position
    # ============================================================================
    
    st.markdown('<p class="section-header">Singapore: The World\'s Maritime Capital</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore has deliberately cultivated its position as the global maritime hub over 70+ years through 
    strategic planning, continuous investment, and ecosystem development. In 2025, Singapore was ranked 
    **#1 in the Xinhua-Baltic International Shipping Centre Development Index** for the **12th consecutive year** 
    (score: 99.5/100), ahead of London, Shanghai, and Hong Kong.
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Container Throughput 2024", "41.12M TEU", delta="+5.4% YoY", help="First time exceeding 40M TEU (2023: 39.0M)")
    with col2:
        st.metric("World Ranking", "#2 Volume, #1 Hub", help="#2 by volume (after Shanghai), #1 transshipment hub globally")
    with col3:
        st.metric("Shipping Lines", "200+", help="Over 200 international shipping lines call Singapore")
    with col4:
        st.metric("Global Connectivity", "600+ ports", help="Connected to 600+ ports in 120+ countries")
    
    st.markdown("""
    **2024 Performance Highlights (Record Year):**
    
    **Container Throughput:**
    - **Total: 41.12 million TEU** (+5.4% from 39.0M in 2023)
    - **PSA Singapore: 40.9 million TEU** (+5.5%, historic record)
    - **PSA Global: 100.2 million TEU** (first time exceeding 100M TEU globally)
    - **Transshipment: ~90%** (approximately 37M TEU transshipment cargo)
    - **Milestone**: Crossed 40 million TEU barrier on December 24, 2024
    
    **Vessel Traffic:**
    - **Vessel arrival tonnage: 3.11 billion GT** (+0.6%, new record)
    - **Annual vessel calls: 140,000+** (consistent high traffic)
    - **Key categories**: Bulk carriers, container ships, tankers (each ~1/3, >90% combined)
    - **Bulk carrier arrivals**: Record high in 2024
    
    **Cargo and Bunkering:**
    - **Total cargo: 622.67 million tonnes** (+5.2% from 592.01M in 2023)
    - **Bunker sales: 54.92 million tonnes** (+6.0%, new record)
      - Partly driven by extended Asia-Europe routes via Cape (Red Sea disruptions)
    - **Alternative fuel sales: 1.34 million tonnes** (doubled from 2023, first time >1M)
      - Biofuel blends: 0.88M tonnes (up from 0.52M in 2023)
      - LNG: 0.46M tonnes (up from 0.11M in 2023)
      - Methanol: 1,626 tonnes (commercially available)
      - Ammonia: 9.74 tonnes (first global trials)
    
    **Singapore Registry of Ships:**
    - **Total tonnage: 108 million GT** (+8.5%, exceeded 100M GT for first time)
    - Growing attractiveness as ship registry of choice
    """)
    
    st.markdown("""
    <div class="success-box">
    <strong>✅ 2024 Resilience Demonstrated:</strong><br>
    Despite Red Sea disruptions causing mid-2024 port congestion, Singapore handled record volumes through:<br>
    - <strong>Rapid response</strong>: 11 Tuas berths commissioned, Keppel Terminal berths reactivated<br>
    - <strong>Capacity expansion</strong>: Yard spaces increased, manpower scaled up<br>
    - <strong>Operational flexibility</strong>: Night-tow operations for barges permitted (first time)<br>
    - <strong>Industry coordination</strong>: Close cooperation between MPA, PSA, unions, shipping lines<br><br>
    Singapore's operational excellence and flexibility enabled it to handle the bunching of vessel 
    arrivals when ships rerouted from Red Sea to Cape of Good Hope, reinforcing its position as 
    the world's most reliable transshipment hub.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">Singapore\'s Core Maritime Strengths</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Strategic Location:**
        - **Centre of Southeast Asia** and on major trade routes
        - **On Asia-Europe route** (33% of global container trade)
        - **Malacca Strait chokepoint** (natural gateway)
        - **Equidistant from major Asian economies**:
          - China, India, Japan, South Korea all within 5,000 km
        - **Deep natural harbour**: 20m+ depth without dredging
        
        **World-Class Infrastructure:**
        - **Current terminals**: Tanjong Pagar, Keppel, Brani, Pasir Panjang
        - **Tuas Mega Port** (under development):
          - 11 berths operational (as of 2024)
          - 7 more berths by 2027
          - Phase 2 reclamation 75% complete (2024)
          - Ultimate capacity: 65M TEU by 2040
          - World's largest fully automated terminal
        - **Super post-Panamax cranes**: Handle 24,000+ TEU mega vessels
        - **Deep-water berths**: 60+ container berths total
        
        **Operational Excellence:**
        - **Berth on Arrival (BOA)**: >90% achievement
        - **Vessel turnaround**: 10-16 hours (vs 24-48 hours elsewhere)
        - **24/7/365 operations**: No downtime, no strikes
        - **Customs efficiency**: Fast clearance, minimal bureaucracy
        - **Free trade port**: No tariffs on transshipment cargo
        """)
    
    with col2:
        st.markdown("""
        **Complete Maritime Ecosystem:**
        Not just a port—a comprehensive maritime cluster providing every maritime service:
        - **Port operations**: PSA, Jurong Port (world-class efficiency)
        - **Shipping lines**: 200+ lines, home to major Asia-Pacific headquarters
        - **Bunkering**: World's largest (54.92M tonnes in 2024)
        - **Ship repair**: 40+ shipyards, dry-docking for all vessel sizes
        - **Maritime finance**: Ship financing, insurance, reinsurance
        - **Maritime law**: Arbitration centres, maritime courts, legal expertise
        - **Maritime technology**: 140+ startups, R&D centres, innovation ecosystem
        - **One-stop solution**: All maritime needs met in single location
        
        **Global Recognition (2024-2025):**
        - **Xinhua-Baltic ISCDI**: #1 maritime centre (12th consecutive year, 99.5/100 score)
        - **DNV & Menon Economics**: #2 for Maritime Technology (2024)
        - **Consistent rankings**: Top 3 globally across all major maritime indices
        
        **Competitive Advantages:**
        - **Network effects**: More carriers → more cargo → more carriers (self-reinforcing)
        - **High switching costs**: Ecosystem lock-in (once established, costly to leave)
        - **Political stability**: Predictable pro-business policies, no backtracking
        - **Skilled workforce**: Multilingual, maritime-trained, highly productive
        - **Government support**: MPA dual role (regulator + developer), long-term vision
        - **Innovation culture**: Regulatory sandboxes, test-bedding facilities, PIER71 ecosystem
        """)
    
    # Performance comparison chart
    st.markdown('<p class="subsection-header">Singapore vs Competitor Ports (2024)</p>', unsafe_allow_html=True)
    
    port_comparison = pd.DataFrame({
        'Port': ['Singapore', 'Shanghai', 'Ningbo-Zhoushan', 'Shenzhen', 'Hong Kong', 'Busan', 'Rotterdam', 'Antwerp'],
        'Throughput (M TEU)': [41.1, 49.2, 35.3, 30.0, 17.8, 22.9, 14.5, 12.0],
        'Country': ['Singapore', 'China', 'China', 'China', 'China/HK', 'South Korea', 'Netherlands', 'Belgium'],
        'Transshipment %': [90, 45, 30, 40, 65, 50, 35, 55],
        'Role': [
            'Pure transshipment hub',
            'Import/export gateway',
            'Import/export gateway',
            'Import/export gateway',
            'Transshipment hub',
            'Regional transshipment',
            'European gateway',
            'European gateway'
        ]
    })
    
    st.dataframe(port_comparison, use_container_width=True, hide_index=True)
    
    st.markdown("""
    **Singapore's Unique Position:**
    - **Highest transshipment percentage (90%)**: Pure hub, not destination
    - **Strategic location**: On major trade routes, not destination market
    - **Efficiency**: 10-16 hour turnaround vs 24-48+ hours at destination ports
    - **Reliability**: No labour strikes, consistent 24/7 operations
    - **Competition**: Shanghai/Ningbo/Shenzhen are destination ports (serving Chinese market)
    - **Regional**: Hong Kong/Busan compete but less comprehensive ecosystem
    """)
    
    # ============================================================================
    # SECTION 2: Maritime and Port Authority of Singapore (MPA)
    # ============================================================================
    
    st.markdown('<p class="section-header">Maritime and Port Authority (MPA): The Dual Role</p>', unsafe_allow_html=True)
    
    st.markdown("""
    MPA is **unique globally** in combining regulatory and developmental functions. This dual mandate 
    enables coordinated long-term strategic planning that has positioned Singapore as the world's premier 
    maritime hub. Understanding MPA's role is essential to understanding Singapore's maritime success.
    """)
    
    st.markdown('<p class="subsection-header">MPA\'s Two Core Functions</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Function 1: Regulator (Safety, Security, Standards)**
        
        **Port Safety and Security:**
        - **Vessel Traffic Management (VTS)**: Real-time monitoring, traffic control
        - **Port security**: ISPS Code compliance, security assessments
        - **Marine safety regulations**: Vessel standards, crew requirements
        - **Accident investigation**: Marine incident analysis and prevention
        - **Pilotage services**: Licensed pilots for vessel movements
        - **Navigation aids**: Lighthouses, buoys, channel marking
        
        **Environmental Protection:**
        - **Marine pollution prevention**: Oil spill response, waste management
        - **Ballast water management**: International compliance (IMO standards)
        - **Emissions monitoring**: Air quality, GHG tracking
        - **Green shipping initiatives**: Incentives for low-emission vessels
        - **Alternative fuels**: LNG, methanol, ammonia standards development
        
        **Standards and Compliance:**
        - **Ship registration**: Singapore Registry of Ships (SRS) - 108M GT in 2024
        - **Crew certification**: STCW compliance, training standards
        - **Maritime labour standards**: MLC 2006 implementation
        - **Classification societies**: Oversight of IACS members
        - **Port facility approvals**: Safety and environmental compliance
        
        **Regulatory Innovation (2024-2025):**
        - **Mass Flow Meter (MFM) verification**: Reduced from 2× to 1× annually (April 2025)
          - Saves industry ~S$300,000 annually
        - **Digital bunkering mandatory**: All suppliers must provide e-BDN from April 1, 2025
          - Saves ~40,000 man-days annually
        - **Risk-based audits**: Focus resources on high-risk operations
        - **Regulatory sandboxes**: Allow innovation within controlled environments
        """)
    
    with col2:
        st.markdown("""
        **Function 2: Developer (Infrastructure, Innovation, Growth)**
        
        **Infrastructure Development:**
        - **Tuas Mega Port**: Largest port development project globally
          - S$20+ billion investment over 30+ years
          - 11 berths operational (2024), 7 more by 2027
          - Ultimate capacity: 65M TEU by 2040
          - World's largest fully automated terminal
        - **Existing terminals**: Maintaining/upgrading Pasir Panjang, etc.
        - **Maritime 5G**: 12 base stations by end 2025 (full port coverage)
        - **Alternative fuel infrastructure**: LNG, methanol bunkering facilities
        
        **Industry Development:**
        - **Attract shipping lines**: Incentives, business-friendly environment
        - **Cluster development**: Encourage maritime service providers
        - **International marketing**: Promote Singapore as maritime hub
        - **Bilateral cooperation**: Partnerships with major maritime nations
        - **Green and Digital Shipping Corridors (GDSCs)**: 6 corridors established
          - Singapore - Los Angeles/Long Beach
          - Singapore - Tianjin
          - Singapore - Rotterdam/Antwerp
          - Others with Korea, Japan, Australia
        
        **Innovation and Technology:**
        - **PIER71 ecosystem**: 140+ maritime tech startups (target 150 by end 2025)
        - **MINT Fund**: S$10M+ for maritime innovation projects
          - Since 2013: Supported 1,800+ scientists/engineers, 80+ technologies deployed
        - **Smart Port Challenge**: Annual competition (200+ proposals in 2024)
        - **Maritime Digital Twin**: Launched March 24, 2025 (MPA + GovTech partnership)
        - **AI applications**: DocuMind, DocuMatch (certificate processing in minutes vs days)
        - **Maritime Cyber Centre (MCAOC)**: Real-time threat monitoring, saves S$200K/company annually
        - **JIT Platform**: 150+ port users onboarded (2024), expanding to tankers/anchorages by end 2025
        
        **Sustainability Leadership:**
        - **Maritime Singapore Green Initiative (MSGI)**: Refreshed 2024, expanded incentives
        - **Alternative fuel trials**: Methanol (1,626 tonnes), ammonia (9.74 tonnes first globally)
        - **Standards development**: Methanol (2024), ammonia (2025) bunkering standards
        - **Green corridors**: 6 GDSCs for alternative fuel/digital solutions piloting
        """)
    
    st.markdown("""
    **Why the Dual Role Works:**
    
    **Coordinated Strategy:**
    - **No conflicting agendas**: Regulator and developer aligned under single authority
    - **Long-term planning**: Can plan 30+ years ahead (Tuas example)
    - **Rapid adaptation**: No bureaucratic silos between regulation and development
    - **Holistic approach**: Safety, growth, innovation, sustainability coordinated
    
    **Policy Alignment:**
    - **Regulation enables innovation**: Sandboxes allow testing new technologies safely
    - **Infrastructure supports standards**: Build facilities for new regulations (e.g., alternative fuels)
    - **Industry input embedded**: Consultation built into policy-making process
    - **Balance**: Maintain safety/environmental standards while supporting competitiveness
    
    **Example: Alternative Fuels Development**
    - **MPA as developer**: Builds LNG/methanol bunkering infrastructure
    - **MPA as regulator**: Develops safety standards (methanol 2024, ammonia 2025)
    - **Result**: Safe, commercially viable alternative fuel ecosystem
    - **Timeline**: Infrastructure and regulation co-developed, no delays
    
    **Contrast with Other Ports:**
    - **Typical model**: Regulator (government) separate from developer (port authority)
    - **Challenge**: Coordination difficulties, conflicting priorities, slower adaptation
    - **Singapore advantage**: Unified strategy, faster decision-making, aligned incentives
    """)
    
    # ============================================================================
    # SECTION 3: The Complete Maritime Cluster
    # ============================================================================
    
    st.markdown('<p class="section-header">Singapore\'s Complete Maritime Cluster</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore offers a comprehensive ecosystem of maritime services—this "one-stop shop" creates 
    powerful network effects and high switching costs, reinforcing Singapore's competitive position.
    """)
    
    st.markdown('<p class="subsection-header">The Seven Pillars of Maritime Singapore</p>', unsafe_allow_html=True)
    
    # Maritime cluster components - enhanced
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
            'PSA (40.9M TEU 2024), Jurong Port, cargo handlers',
            '200+ shipping lines, ship management companies, Asia-Pacific HQs',
            'Sembcorp Marine, Keppel, 40+ shipyards, dry-docking facilities',
            'Bunkering (54.92M tonnes 2024), ship chandlers, crew managers, supplies',
            'Major banks, ship financing, P&I clubs, marine insurers, reinsurers',
            'Maritime law firms, Singapore Chamber of Maritime Arbitration, courts',
            '140+ PIER71 startups, R&D centres (NUS, NTU, SUTD, A*STAR), SMI'
        ],
        'Services Provided': [
            'Container handling, cargo storage, transshipment (90% of throughput)',
            'Liner services, vessel operations, freight forwarding, ship management',
            'Dry-docking, repairs, retrofits, conversions, new builds (offshore/naval)',
            'Fuel supply (conventional + alternative), provisions, crew changes, maintenance',
            'Ship loans, project finance, hull/cargo/P&I insurance, reinsurance',
            'Maritime disputes, contracts, arbitration, litigation, advisory',
            'Digital solutions, automation, AI, IoT, blockchain, green tech, cybersecurity'
        ],
        'Why Critically Important': [
            'Core infrastructure - without efficient port, entire hub collapses',
            'Global connectivity - 200+ lines connect Singapore to 600+ ports worldwide',
            'Vessel maintenance - ships need periodic servicing (dry-dock every 2-5 years)',
            'Operational support - vessels need fuel, supplies, crew changes at every port call',
            'Capital and risk - shipping is capital-intensive, requires sophisticated finance',
            'Dispute resolution - international contracts need trusted legal framework',
            'Competitive edge - innovation drives efficiency, sustainability, future growth'
        ],
        'Singapore\'s Advantage': [
            'World-class efficiency (10-16h turnaround), reliability (no strikes), scale',
            'Most comprehensive liner connectivity globally, 200+ lines, frequent services',
            '40+ yards, all vessel types, offshore/naval expertise, strategic location',
            'World\'s largest bunkering port (54.92M tonnes), alternative fuels leadership',
            'Major financial centre (ranked top 5 globally), ship finance expertise',
            'Trusted neutral jurisdiction, English common law, maritime expertise',
            '140+ startups, S$100M+ raised, government support (MINT, PIER71), sandboxes'
        ]
    })
    
    st.dataframe(cluster_components, use_container_width=True, hide_index=True)
    
    st.markdown('<p class="subsection-header">Deep Dive: Key Pillars</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **1. Bunkering (Marine Fuel Supply) - World's Largest**
    
    **Singapore's Dominant Position:**
    - **54.92 million tonnes in 2024** (+6.0% YoY, new record)
    - **World's largest bunkering port** for 35+ consecutive years
    - **20+ licensed bunker suppliers** (competitive market)
    - **All fuel types available**:
      - Conventional: HSFO, LSFO, VLSFO, MGO, MDO
      - Alternative: LNG (0.46M tonnes), biofuel blends (0.88M tonnes, up to B50), methanol (1,626 tonnes)
      - Future-ready: Ammonia trials (9.74 tonnes, world's first), e-fuels infrastructure planned
    
    **2024 Milestones:**
    - **Alternative fuels: 1.34M tonnes** (doubled from 2023, first time >1M tonnes)
    - **Digital bunkering mandatory from April 1, 2025**: All suppliers must issue e-BDN
      - Saves ~40,000 man-days annually
      - Reduces errors, fraud detection, regulatory compliance
    - **Methanol bunkering standards**: Technical Reference released 2024
    - **Ammonia bunkering standards**: Under development, expected 2025
    - **LNG reloading EOI**: Launched December 2024 for sea-based LNG bunkering expansion
    
    **Why Bunkering Matters:**
    - **Lock-in effect**: Vessels must call Singapore to refuel → Generates port calls
    - **Revenue diversification**: Bunkering revenue supplements container handling
    - **Strategic control**: Fuel supply = influence over shipping routes
    - **Red Sea impact**: 2024 increase partly due to longer Asia-Europe routes via Cape
    
    **Bunkering Operations:**
    - **Ship-to-ship**: Tanker transfers fuel to vessel (most common, any location in port)
    - **Truck-to-ship**: For smaller quantities, specific locations
    - **24/7 operations**: Any time, any location, rapid response
    - **Mass Flow Meters (MFM)**: Accurate measurement, transparency (verification 1×/year from April 2025)
    - **Digital documentation**: e-BDN mandatory April 1, 2025 (default method)
    
    **Alternative Fuels Leadership:**
    - **First-mover advantage**: Biofuel blends commercially available (up to B50), B100 trials ongoing
    - **LNG infrastructure**: Operational LNG bunkering (0.46M tonnes in 2024), expanding capacity
    - **Methanol readiness**: Commercial-scale methanol bunkering (1,626 tonnes), Technical Reference published
    - **Ammonia pioneering**: World's first ammonia bunkering trials (9.74 tonnes), safety standards in development
    - **e-fuels future**: Expression of interest for scalable e-/bio-methane solutions
    
    **Competitive Positioning:**
    Singapore's early investment in alternative fuel infrastructure positions it to maintain bunkering 
    leadership as the industry decarbonises. Rotterdam, Antwerp, and Dubai are key competitors, but 
    Singapore's comprehensive ecosystem and first-mover advantage in Asia provide strategic advantage.
    
    ---
    
    **2. Ship Repair and Shipbuilding - Southeast Asia's Largest**
    
    **Capabilities:**
    - **40+ shipyards and repair facilities** across Singapore
    - **Dry-docking**: All vessel sizes, from feeder vessels to ULCVs
    - **Specialisations**:
      - Offshore platforms and FPSOs (Sembcorp Marine, Keppel)
      - Naval vessels and submarines (strategic capability)
      - Mega yachts and luxury vessels
      - Container ships and bulk carriers
    - **Retrofits and conversions**:
      - Scrubber installations (IMO 2020 compliance)
      - Ballast water treatment systems (BWTSs)
      - Energy efficiency upgrades (hull cleaning, propeller optimization)
      - Alternative fuel conversions (LNG/methanol dual-fuel)
    
    **Strategic Value:**
    - **Periodic maintenance**: Vessels require dry-docking every 2-5 years (regulatory requirement)
    - **Location advantage**: On major trade routes, convenient for scheduled maintenance
    - **Technical expertise**: Highly skilled workforce, advanced facilities
    - **High-value industry**: S$10+ billion annual revenue, skilled jobs, technology transfer
    
    **2024-2025 Trends:**
    - **Retrofit demand**: Ships installing scrubbers, BWTSs, efficiency upgrades
    - **Alternative fuel conversions**: Growing demand for LNG/methanol dual-fuel retrofits
    - **Offshore sector**: O&G vessel maintenance, offshore wind (new growth area)
    - **Naval contracts**: Singapore and regional navies (strategic importance)
    
    ---
    
    **3. Maritime Finance and Insurance - Asia's Hub**
    
    **Financial Services:**
    - **Ship financing**: Major banks offer ship loans (DBS, OCBC, UOB, international banks)
    - **Singapore dollar financing**: Growing share of ship finance denominated in SGD
    - **Shipping funds**: Private equity, asset-backed securities
    - **Leasing**: Operating leases, finance leases, bareboat charters
    - **Insurance markets**:
      - Hull and machinery (H&M) insurance
      - Protection and indemnity (P&I) clubs
      - Cargo insurance
      - Reinsurance market
    
    **Why Singapore?**
    - **Financial centre**: Ranked top 5 globally (GFCI), robust banking sector
    - **Regulatory framework**: MAS (Monetary Authority of Singapore) trusted regulator
    - **Tax incentives**: Maritime sector incentives (MSI scheme, approved shipping companies)
    - **Skilled workforce**: Finance and maritime expertise combined
    - **Time zone**: Bridges Europe and Americas, Asia trading hours
    
    **2024 Trends:**
    - **Green finance**: Sustainability-linked loans (SLLs) for eco-vessels
    - **Alternative fuel financing**: Higher risk premiums, specialized expertise needed
    - **Cyber risk insurance**: Growing demand (maritime cyber threats increasing)
    - **Asset-based finance**: Sale-and-leaseback transactions popular
    
    ---
    
    **4. Maritime Law and Arbitration - Asia's Centre**
    
    **Legal Services:**
    - **Maritime law firms**: 50+ firms with maritime expertise (Rajah & Tann, Allen & Gledhill, Watson Farley & Williams, etc.)
    - **Singapore Chamber of Maritime Arbitration (SCMA)**: Neutral arbitration venue
    - **Maritime courts**: Specialized judges, admiralty jurisdiction
    - **Legal framework**: English common law (familiar to international shipping)
    
    **Services:**
    - **Contracts**: Charterparties, bills of lading, shipbuilding contracts
    - **Disputes**: Arbitration, litigation, mediation
    - **Advisory**: Regulatory compliance, transactions, restructuring
    - **Admiralty**: Ship arrests, maritime liens, salvage
    
    **Why Singapore?**
    - **Neutral jurisdiction**: Not aligned with any major shipping nation
    - **Trusted legal system**: Rule of law, predictable outcomes
    - **Maritime expertise**: Judges and lawyers understand shipping
    - **Efficiency**: Fast resolution compared to many jurisdictions
    - **Regional hub**: Convenient for Asia-Pacific disputes
    
    **Growing Role:**
    Singapore increasingly chosen for maritime arbitration (competing with London), especially for 
    Asia-Pacific disputes. SCMA caseload growing, recognition increasing globally.
    """)
    
    # ============================================================================
    # SECTION 4: Innovation and Digital Transformation
    # ============================================================================
    
    st.markdown('<p class="section-header">Innovation and Digital Transformation</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore is positioning itself as the world's leading maritime technology hub through coordinated 
    initiatives spanning startups, R&D, digital platforms, and enabling infrastructure.
    """)
    
    st.markdown('<p class="subsection-header">PIER71: Maritime Technology Ecosystem</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Port Innovation Ecosystem Reimagined @ BLOCK71 (PIER71)**
    
    **Overview:**
    - **Joint initiative**: MPA + NUS Enterprise (National University of Singapore)
    - **Launched**: 2018
    - **Mission**: Grow Singapore into leading maritime technology startup hub
    - **Partnership renewed**: March 2025 (3-year extension)
    
    **Achievements (2018-2025):**
    - **140+ startups nurtured** (target: 150 by end 2025)
    - **>S$100 million raised** in investments since 2018
    - **2024 alone: S$28.9 million** raised by 14 startups
    - **61 projects funded** through MINT grants
    - **27 technologies deployed** in maritime industry from PIER71 startups
    
    **Programme Components:**
    
    **1. Smart Port Challenge (SPC):**
    - **Annual competition** for maritime tech solutions
    - **SPC 2024**: Record 200+ proposals received
    - **14 challenge statements** across 4 key areas:
      - Maritime green technologies
      - Smart shipping
      - Next generation ports
      - Digitalisation (AI, cybersecurity, cloud)
    - **Global expansion**: 2024 first year with international roadshows (6 cities across Asia, Europe, North America)
    - **Prizes**: Up to S$250,000 for winners, plus MINT grant eligibility
    
    **2. PIER71 Accelerate:**
    - **12-week programme** for shortlisted startups
    - **Mentorship**: Industry experts, technical advisors
    - **Industry connections**: Introductions to potential customers (shipping lines, ports)
    - **Resources**: Facilities, test-bedding opportunities, regulatory support
    - **Funding pathway**: MINT grant applications
    
    **3. PIER71 Ascend:**
    - **Growth-stage programme** for scaling startups
    - **Market access**: Help expand to international markets
    - **Investment facilitation**: Connect with VCs, corporate investors
    - **Network**: Global BLOCK71 ecosystem (Silicon Valley, China, etc.)
    
    **4. MINT Fund Grants:**
    - **S$10 million fund** for maritime innovation
    - **Since 2013**: Supported 1,800+ research scientists and engineers
    - **80+ technologies deployed** in maritime sector from MINT projects
    - **Grant levels**:
      - Proof-of-concept: Up to S$100,000
      - New product development: Up to S$250,000
    - **2024 grants**: 5 startups awarded S$250,000 total (biofuel optimization, vessel monitoring, cybersecurity, inspection tools, depot digital twin)
    
    **Global Network:**
    - **BLOCK71 integration**: Access to NUS' global startup network
    - **International presence**: Leveraging MPA's regional offices worldwide
    - **Partnerships**: Plug and Play (April 2025), major maritime clusters
    - **Overseas expansion support**: Help startups enter new markets
    
    **2025 Enhancements:**
    - **Expanded global outreach**: More international partnerships, roadshows
    - **Stronger corporate engagement**: More shipping lines, ports involved as problem-owners
    - **Investment catalysis**: Better access to maritime-focused VCs, corporate VCs
    - **Singapore Leaders' Network (SGLN)**: MLP alumni integration for global insights
    """)
    
    st.markdown('<p class="subsection-header">Digital Platforms and AI Applications</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Maritime Digital Twin (Launched March 24, 2025):**
    - **Partnership**: MPA + GovTech (Government Technology Agency)
    - **First in Singapore**: Dynamic virtual model of entire Port of Singapore
    - **Capabilities demonstrated**:
      - Real-time vessel monitoring and tracking
      - Underwater visualisation (hull inspection, cleaning)
      - Port operations simulation and optimization
      - Risk assessment and scenario planning
    - **Future use cases**:
      - Predictive maintenance of port infrastructure
      - Optimal berth allocation and traffic management
      - Environmental impact monitoring
      - Emergency response simulation
    - **Alignment**: Singapore Geospatial Master Plan (2024-2033)
    
    **DocuMind and DocuMatch (AI Applications, Launched January 2025):**
    - **DocuMind**: Multi-modal Large Language Model (LLM) application
      - Reads information from various document formats
      - Extracts relevant data automatically
    - **DocuMatch**: Data verification application
      - Verifies data against internal databases
      - Recommends application approvals
    - **Use case**: Singapore-registered ship certificate renewals
    - **Impact**: Processing time reduced from **3 days to minutes** for most transactions
    - **Rollout**: Pilot trials 2024, full industry adoption by end 2025
    - **Future**: MPA plans more AI-driven tools for other maritime processes
    
    **Just-In-Time (JIT) Platform:**
    - **Launched**: 2024 for container, general cargo, bulk sectors
    - **Users onboarded**: 150+ port users (2024)
    - **Purpose**: Coordinate vessel arrivals, optimize port resources
    - **Benefits**: Reduce waiting time, lower emissions (vessels arrive exactly when berth ready)
    - **Automation**: Working with shipping lines, marine service providers for data exchange
    - **Expansion**: Tankers calling at terminals, all vessels in anchorages by end 2025
    
    **Digital Bunkering (Mandatory from April 1, 2025):**
    - **Requirement**: All bunker suppliers must provide digital bunkering services
    - **Default method**: Electronic Bunker Delivery Notes (e-BDN)
    - **Pilot phase**: November 2023 - March 2025 (top 10 bunker players involved)
    - **Benefits**:
      - Efficient data sharing between buyers and suppliers
      - Expedite administrative processes
      - Improve accountability and compliance
      - Reduce potential for errors
      - Early detection of fraudulent activities
      - Streamlined, secured, environmentally friendly process
    - **Industry savings**: Close to 40,000 man-days annually
    
    **Maritime 5G Network:**
    - **Status**: 5 base stations operational (2024), 7 more by end 2025
    - **Full coverage**: All major fairways, anchorages, terminals, boarding grounds by end 2025
    - **Total**: 12 base stations
    - **Benefits**: Stronger, more stable connectivity throughout port
    - **Enabled use cases**:
      - Live data transfers for digital bunkering (ship-to-ship)
      - Drone operations (ship-to-shore applications)
      - Real-time communications and data exchange on ship movements
      - Enhanced safety of navigation
      - Remote operations and monitoring
    
    **Maritime Cyber Assurance and Operations Centre (MCAOC):**
    - **Launched**: 2024
    - **Services**: Real-time security monitoring, threat intelligence dissemination
    - **Benefits**: Early action on cyber threats, pooled monitoring capabilities
    - **Cost savings**: Estimated S$200,000 annually per participating company
    - **Onboarded**: 16 companies as of 2024 (growing)
    - **Importance**: Maritime sector increasingly targeted by cyber attacks
    """)
    
    st.markdown('<p class="subsection-header">Research and Development</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Singapore Maritime Institute (SMI):**
    - **Role**: Coordinate maritime R&D in Singapore
    - **Partners**: Universities (NUS, NTU, SUTD), A*STAR research centres
    - **Focus**: Academia-industry collaboration, technology translation
    - **Outcomes**: R&D talent development, technology deployment to industry
    
    **Centres of Excellence:**
    - **NUS**: Maritime Energy and Sustainable Development Centre, Centre for Maritime Studies
    - **NTU**: Maritime Research Centre, Energy Research Institute
    - **SUTD**: iTrust (Maritime Testbed for Ship Operational Technology - MariOT)
    - **A*STAR**: Institute of High Performance Computing (IHPC), others
    
    **MariOT (Maritime Testbed for Ship Operational Technology):**
    - **Launched**: April 2024 at iTrust SUTD Centre
    - **Purpose**: Industrial-grade simulator for ship systems
    - **Replicates**: Propulsion, machinery, energy, navigation systems
    - **Use**: Cybersecurity training, testing solutions in controlled environment
    - **Inaugural exercise**: March 2025
    - **Goal**: Strengthen resilience against cyber threats
    
    **Research Focus Areas (2024-2025):**
    - **Decarbonisation**: Alternative fuels, energy efficiency, emissions reduction
    - **Digitalisation**: AI/ML, digital twin, autonomous systems, blockchain
    - **Cybersecurity**: OT security, threat detection, resilience
    - **Green technology**: Low-carbon fuels, renewable energy, electrification
    - **Automation**: Autonomous vessels (MASS), unmanned systems, robotics
    - **Port operations**: Optimization, predictive analytics, smart terminals
    """)
    
    st.markdown('<p class="subsection-header">Regulatory Sandboxes and Test-Bedding</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Enabling Innovation Through Controlled Testing:**
    
    **1. Maritime Drone Estate:**
    - Designated sea-space for maritime drone testing
    - Safety regulations relaxed for approved trials
    - Use cases: Inspections, surveillance, cargo delivery
    
    **2. Maritime Autonomous Surface Ships (MASS) Testbed:**
    - Sea areas for autonomous vessel trials
    - Progressive testing (remote-controlled → autonomous)
    - International partnerships (Norway, Japan)
    
    **3. Living Labs:**
    - Real port environment for technology trials
    - Startups test solutions at Tuas Port, Pasir Panjang
    - PSA and MPA support, monitored deployments
    
    **4. Alternative Fuel Trials:**
    - **LNG bunkering**: Operational, expanding capacity
    - **Methanol bunkering**: Commercial-scale trials, standards published
    - **Ammonia bunkering**: World's first trials (9.74 tonnes 2024)
    - **Biofuel blends**: Up to B50 commercially available, B100 trials ongoing
    
    **5. Green and Digital Shipping Corridors (GDSCs):**
    - **6 corridors established** with international partners
    - **Singapore - LA/Long Beach**: Just-in-time trials, alternative fuels
    - **Singapore - Tianjin**: Green methanol quality standards, GHG intensity research
    - **Singapore - Rotterdam/Antwerp**: Digital data exchange
    - **Others**: Korea, Japan, Australia
    - **Purpose**: Pilot alternative fuels, digital solutions on commercial routes
    
    **Philosophy:**
    Singapore's approach is to enable innovation through structured testing rather than prohibit 
    new technologies. Regulatory sandboxes allow companies to trial solutions safely, with MPA 
    monitoring and adjusting regulations based on results. This accelerates deployment while 
    maintaining safety and environmental standards.
    """)
    
    # ============================================================================
    # SECTION 5: Sustainability and Green Shipping
    # ============================================================================
    
    st.markdown('<p class="section-header">Sustainability and Green Shipping</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore is positioning itself as a green maritime hub through infrastructure investment, 
    incentives, and international cooperation on decarbonisation.
    """)
    
    st.markdown('<p class="subsection-header">Maritime Singapore Green Initiative (MSGI) - Refreshed 2024</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Refreshed Programme (2024):**
    - **Purpose**: Encourage early adoption of zero and near-zero emission technologies and fuels
    - **Alignment**: IMO GHG Strategy 2023 (net-zero by 2050)
    - **Incentives**: Port dues discounts, grants, co-funding
    - **Target vessels**: Green ships using alternative fuels, energy-efficient vessels
    
    **Green Ship Programme:**
    - **Port dues reduction**: Up to 50% discount for qualifying eco-vessels
    - **Criteria**: IMO Tier III engines, alternative fuels (LNG/methanol/ammonia), energy efficiency measures
    - **Duration**: Multi-year incentives (5-year programmes)
    
    **Alternative Fuel Grants:**
    - **LNG bunkering**: Price parity support during transition
    - **Methanol**: Pilot programme support, price difference co-funded
    - **Ammonia**: Future-ready, incentives under development
    
    **Shore Power Infrastructure:**
    - **Objective**: Allow vessels to plug into grid electricity while at berth
    - **Benefits**: Eliminate vessel emissions in port
    - **Deployment**: Pilot installations at Tuas Port, expansion planned
    - **Challenge**: High infrastructure cost, vessel compatibility
    """)
    
    st.markdown('<p class="subsection-header">Alternative Fuel Infrastructure</p>', unsafe_allow_html=True)
    
    # Alternative fuels comparison
    alt_fuels = pd.DataFrame({
        'Fuel Type': ['Conventional (LSFO/MGO)', 'LNG', 'Methanol', 'Ammonia', 'Biofuels', 'Hydrogen'],
        'Singapore Status (2024-2025)': [
            'Fully operational (54.0M tonnes conventional in 2024)',
            'Operational (0.46M tonnes in 2024, expanding)',
            'Commercial-scale (1,626 tonnes in 2024, standards published)',
            'Trials phase (9.74 tonnes world first, standards in dev 2025)',
            'Commercial (0.88M tonnes blends up to B50, B100 trials)',
            'R&D phase (no commercial bunkering yet)'
        ],
        'GHG Reduction vs Conventional': [
            'Baseline (0%)',
            '20-25% (lifecycle), near-zero SOx',
            '10-15% (conventional), near-zero if green',
            'Zero (if green ammonia)',
            '30-80% (depending on blend, feedstock)',
            'Zero (if green hydrogen)'
        ],
        'Availability': [
            'Abundant globally',
            'Growing (7% of global fleet capable)',
            'Limited, production scaling',
            'Very limited, in development',
            'Limited, scaling production',
            'Very limited, in development'
        ],
        'Challenges': [
            'High GHG emissions, sulphur content',
            'Methane slip, cryogenic storage, cost',
            'Toxic, corrosive, lower energy density, cost 2× conventional',
            'Toxic, NOx emissions, low energy density, cost',
            'Feedstock availability, cost, compatibility',
            'Low energy density, storage, cost, safety'
        ],
        'Singapore Investment': [
            'Mature infrastructure',
            'LNG terminals, bunkering vessels, reloading (EOI Dec 2024)',
            'Bunkering facilities, Technical Reference 2024',
            'Safety standards 2025, pilot infrastructure',
            'Widely available (B50), trialing B100',
            'R&D support, future infrastructure planned'
        ]
    })
    
    st.dataframe(alt_fuels, use_container_width=True, hide_index=True)
    
    st.markdown("""
    **Alternative Fuels Trajectory (2024-2030):**
    
    **Current (2024-2025):**
    - **Conventional fuels**: Still 97.6% of bunker market (53.58M of 54.92M tonnes)
    - **Alternative fuels**: 2.4% (1.34M tonnes), but growing rapidly (doubled 2023-2024)
    - **LNG**: Operational, commercial scale (0.46M tonnes)
    - **Biofuels**: Commercially available (0.88M tonnes, up to B50 blends)
    - **Methanol**: Commercial-scale trials (1,626 tonnes), standards published
    - **Ammonia**: World's first bunkering trials (9.74 tonnes)
    
    **Near-term (2025-2027):**
    - **LNG expansion**: Additional capacity via sea-based reloading (EOI Dec 2024)
    - **Methanol scaling**: More bunkering infrastructure, commercial volumes growing
    - **Ammonia standards**: Safety standards published 2025, pilot infrastructure
    - **Biofuels B100**: Commercial availability after trials complete
    - **Green corridors**: Operational routes with alternative fuel support
    
    **Medium-term (2027-2030):**
    - **Alternative fuels target**: 10-15% of total bunker market
    - **Methanol/Ammonia**: Mainstream options alongside LNG
    - **Hydrogen**: Pilot projects beginning
    - **e-fuels**: Early commercial availability (e-methanol, e-ammonia)
    - **Shore power**: Widespread deployment at major terminals
    
    **Long-term (2030-2050):**
    - **Net-zero pathway**: Align with IMO 2050 net-zero target
    - **Alternative fuels dominant**: 50%+ of market by 2040
    - **Zero-carbon fuels**: Green hydrogen, green ammonia, e-fuels mainstream by 2050
    - **Singapore positioning**: Remain Asia's leading green fuels bunkering hub
    """)
    
    st.markdown('<p class="subsection-header">Standards Development Leadership</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Singapore Standards (SS) for Alternative Fuels:**
    
    **Methanol Bunkering (Technical Reference Published 2024):**
    - **Scope**: Safety procedures, crew competencies, custody transfer requirements
    - **Mass Flow Meter (MFM)**: Framework for methanol MFM and digital documentation
    - **Collaboration**: MPA + EnterpriseSG + industry stakeholders
    - **Impact**: Enable safe, transparent methanol bunkering operations
    - **Trials**: SIMOPS (Simultaneous Operations) trials completed 2024
    
    **Ammonia Bunkering (Standards Expected 2025):**
    - **Development**: EnterpriseSG + MPA + industry + class societies
    - **Scope**: Custody transfer, safety procedures, crew competencies, handling protocols
    - **Challenge**: Ammonia is toxic, corrosive - requires stringent safety measures
    - **Timeline**: Standards publication 2025, enable commercial bunkering 2026+
    - **Global first**: Singapore among first globally to develop comprehensive ammonia bunkering standards
    
    **Why Standards Matter:**
    - **Safety**: Ensure safe handling of new fuels
    - **Commercial viability**: Industry needs standards to invest confidently
    - **International acceptance**: Singapore standards may become regional/global benchmarks
    - **First-mover advantage**: Early standards development attracts alternative fuel bunkering business
    
    **Global Leadership:**
    Singapore actively contributes to IMO standards development, ensuring global regulations are 
    workable and Singapore remains at forefront of alternative fuel adoption.
    """)
    
    # ============================================================================
    # SECTION 6: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Maritime Singapore's Global Position:**
        - **#1 maritime centre**: 12th consecutive year (Xinhua-Baltic ISCDI 99.5/100, 2025)
        - **#2 container port**: 41.12M TEU (2024, first time >40M), after Shanghai's 49.2M
        - **#1 transshipment hub**: 90% transshipment ratio (37M+ TEU), world's largest
        - **#1 bunkering port**: 54.92M tonnes (2024, 35+ consecutive years as largest)
        - **Complete ecosystem**: 7 pillars fully developed (port, shipping, repair, ancillary, finance, legal, tech)
        
        **2024 Record Performance:**
        - **Container throughput**: 41.12M TEU (+5.4%)
        - **Cargo**: 622.67M tonnes (+5.2%)
        - **Vessel arrivals**: 3.11B GT (+0.6%, new record)
        - **Bunker sales**: 54.92M tonnes (+6.0%, new record)
        - **Alternative fuels**: 1.34M tonnes (doubled, >1M first time)
        - **Singapore Registry**: 108M GT (+8.5%, >100M first time)
        - **PSA Singapore**: 40.9M TEU (+5.5%, record)
        - **PSA Global**: 100.2M TEU (>100M first time)
        
        **Infrastructure Excellence:**
        - **Tuas Mega Port**: 11 berths operational (2024), 7 more by 2027, 65M TEU capacity by 2040
        - **Operational efficiency**: 10-16h turnaround, >90% BOA, 24/7/365 operations
        - **Resilience**: Handled mid-2024 Red Sea congestion (Keppel reactivated, night-tows, coordination)
        - **60+ container berths**: Across all terminals
        - **200+ shipping lines**: Connected to 600+ ports in 120+ countries
        """)
    
    with col2:
        st.markdown("""
        **MPA's Dual Role Success:**
        - **Regulator**: Safety, security, standards, environmental protection
        - **Developer**: Tuas Port, innovation ecosystem, industry growth, sustainability
        - **Coordination**: Aligned strategy, no silos, long-term planning (30+ years)
        - **Rapid adaptation**: Regulatory sandboxes, test-bedding, innovation-friendly
        
        **Innovation Ecosystem:**
        - **PIER71**: 140+ startups (target 150 by end 2025), >S$100M raised since 2018
        - **MINT Fund**: Since 2013, supported 1,800+ scientists/engineers, 80+ technologies deployed
        - **Smart Port Challenge**: 200+ proposals (2024 record), S$250K prizes + grants
        - **Maritime Digital Twin**: Launched March 24, 2025 (MPA + GovTech)
        - **AI applications**: DocuMind/DocuMatch (certificate processing minutes vs 3 days)
        - **Digital platforms**: JIT Platform (150+ users), digital bunkering (mandatory April 1, 2025)
        - **Maritime 5G**: Full coverage by end 2025 (12 base stations)
        - **Cyber centre (MCAOC)**: S$200K annual savings per company
        
        **Sustainability Leadership:**
        - **Alternative fuels**: 1.34M tonnes (2024, doubled from 2023)
          - LNG: 0.46M tonnes (operational, expanding)
          - Biofuels: 0.88M tonnes (B50 commercial, B100 trials)
          - Methanol: 1,626 tonnes (commercial, standards published 2024)
          - Ammonia: 9.74 tonnes (world's first trials, standards 2025)
        - **Green corridors**: 6 GDSCs with international partners
        - **MSGI refreshed**: 2024 expanded incentives for zero/near-zero emission vessels
        - **Standards leadership**: Methanol (2024), ammonia (2025) bunkering standards
        
        **Competitive Moat:**
        - **Network effects**: More carriers → more cargo → more services → more carriers
        - **High switching costs**: Complete ecosystem, established relationships, operational integration
        - **First-mover advantages**: Alternative fuels, digital platforms, innovation ecosystem
        - **Government support**: Long-term vision, coordinated strategy, sustained investment
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Singapore has built the world's most comprehensive maritime 
    ecosystem over 70+ years, combining world-class port infrastructure (41.12M TEU in 2024, first 
    time >40M) with a complete cluster of services (bunkering 54.92M tonnes world's largest, ship 
    repair 40+ yards, finance, legal, technology). MPA's dual role as regulator and developer enables 
    coordinated long-term strategy, exemplified by the S$20B+ Tuas Mega Port project (11 berths 
    operational, ultimate 65M TEU capacity by 2040).
    <br><br>
    <strong>Innovation leadership</strong> is accelerating through PIER71 (140+ startups, >S$100M raised), 
    Maritime Digital Twin (launched March 2025), AI applications (DocuMind/DocuMatch reduce certificate 
    processing to minutes), JIT Platform (150+ users), digital bunkering (mandatory April 1, 2025), 
    and Maritime 5G (full coverage end 2025). The MINT Fund has supported 1,800+ scientists/engineers 
    and deployed 80+ technologies since 2013.
    <br><br>
    <strong>Sustainability positioning</strong> is strategic: Alternative fuel sales doubled to 1.34M 
    tonnes in 2024 (LNG 0.46M, biofuels 0.88M, methanol 1,626 tonnes commercial, ammonia 9.74 tonnes 
    world's first trials). Singapore published methanol bunkering standards (2024) and is developing 
    ammonia standards (2025), positioning itself as Asia's green fuels bunkering hub. Six Green and 
    Digital Shipping Corridors with international partners pilot alternative fuels and digital solutions.
    <br><br>
    <strong>2025-2030 outlook:</strong> Singapore aims to maintain #1 maritime centre ranking by: 
    (1) Completing Tuas Port (18 berths by 2027), (2) Growing alternative fuel market share to 10-15%, 
    (3) Expanding PIER71 to 150+ startups, (4) Scaling digital platforms industry-wide, (5) Strengthening 
    global green corridors network. The comprehensive ecosystem creates high switching costs and network 
    effects—once companies establish operations in Singapore, the ecosystem makes it efficient to keep 
    all maritime services here. This competitive moat, combined with continuous innovation and government 
    support, positions Singapore to remain the world's premier maritime hub for decades to come.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** ⚓ Port Strategy & Competition - Explore the critical success factors for transshipment 
    hubs, competitive dynamics between Singapore and regional ports (Port Klang, Tanjung Pelepas, Colombo, 
    Jebel Ali), strategic planning frameworks, and Singapore's response to competition through Tuas Port 
    investment and ecosystem development.
    """)
