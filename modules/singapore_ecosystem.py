import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">🇸🇬 Maritime Singapore Ecosystem</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand Singapore's comprehensive maritime cluster, MPA's dual role as regulator and developer, 
    the complete ecosystem of maritime services, and innovation initiatives driving the industry forward.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Singapore's Maritime Position
    # ============================================================================
    
    st.markdown('<p class="section-header">Singapore: The World\'s Maritime Capital</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore has deliberately cultivated its position as a global maritime hub over 70+ years. Understanding 
    this ecosystem helps explain the context for port operations and digital innovation.
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Container Throughput", "37.3M TEU", help="Annual container throughput (2023)")
    with col2:
        st.metric("World Ranking", "#2", help="World's 2nd largest container port by volume")
    with col3:
        st.metric("Shipping Lines", "200+", help="Over 200 shipping lines call at Singapore")
    with col4:
        st.metric("Global Connectivity", "600+ ports", help="Connected to 600+ ports in 123 countries")
    
    st.markdown("""
    **Singapore's Maritime Strengths:**
    
    **Strategic Location:**
    - Centre of Southeast Asia
    - On main Asia-Europe shipping route (33% of global trade)
    - Malacca Strait chokepoint
    - Equidistant from major Asian economies (China, India, Japan, Korea)
    
    **World-Class Infrastructure:**
    - Multiple terminals: Tanjong Pagar, Keppel, Brani, Pasir Panjang
    - Tuas Mega Port under development (65M TEU capacity by 2040)
    - State-of-the-art equipment and automation
    - Deep-water berths accommodating mega vessels
    
    **Operational Excellence:**
    - Berth on Arrival (BOA) >90%
    - 24-hour vessel turnaround for mega vessels
    - 24/7/365 operations
    - Highly efficient customs and logistics
    
    **Complete Ecosystem:**
    - Not just a port—a comprehensive maritime cluster
    - Ship repair, bunkering, maritime finance, insurance, legal, technology
    - One-stop solution for maritime industry needs
    """)
    
    # ============================================================================
    # SECTION 2: Maritime and Port Authority of Singapore (MPA)
    # ============================================================================
    
    st.markdown('<p class="section-header">Maritime and Port Authority (MPA): The Dual Role</p>', unsafe_allow_html=True)
    
    st.markdown("""
    MPA is unique globally in combining regulatory and developmental functions. Understanding this dual role 
    explains Singapore's coordinated maritime strategy.
    """)
    
    st.markdown('<p class="subsection-header">MPA\'s Two Core Functions</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Function 1: Regulator**
        
        **Port Safety and Security:**
        - Vessel traffic management (VTS)
        - Port security (ISPS Code compliance)
        - Marine safety regulations
        - Accident investigation
        - Pilotage services regulation
        
        **Environmental Protection:**
        - Marine pollution prevention
        - Ballast water management
        - Emissions monitoring
        - Green shipping initiatives
        
        **Standards and Compliance:**
        - Ship registration
        - Crew certification
        - Maritime labour standards
        - International convention compliance
        
        **Infrastructure Regulation:**
        - Port facility licencing
        - Terminal operator oversight
        - Navigational aids maintenance
        """)
    
    with col2:
        st.markdown("""
        **Function 2: Developer**
        
        **Industry Development:**
        - Maritime cluster promotion
        - Attracting shipping lines and services
        - Business facilitation
        - Investment incentives
        
        **Innovation and Technology:**
        - Digital transformation (digitalPORT@SG)
        - R&D funding and support
        - Test-bedding facilities
        - Innovation programmes
        
        **Talent Development:**
        - Maritime training programmes
        - Scholarships and bursaries
        - Industry-academic partnerships
        - Workforce upskilling
        
        **Strategic Planning:**
        - Long-term port masterplanning
        - Tuas Mega Port development
        - International partnerships
        - Trade route development
        """)
    
    st.markdown("""
    **Why This Dual Role Matters:**
    
    **Coordinated Strategy:**
    - Single entity aligns regulation with development goals
    - Avoids conflict between safety/security and business growth
    - Holistic view of maritime ecosystem
    
    **Responsive Governance:**
    - Quick policy adaptation to industry needs
    - Balance between regulation and competitiveness
    - Industry consultation embedded in decision-making
    
    **Long-Term Vision:**
    - Infrastructure planning aligned with regulatory framework
    - Innovation encouraged within safety boundaries
    - Sustainable development prioritised
    
    **Example: Tuas Development**
    - MPA as developer: Plans and builds Tuas Mega Port
    - MPA as regulator: Ensures environmental compliance, safety standards
    - Coordination ensures world-class facility that's also sustainable and safe
    """)
    
    # ============================================================================
    # SECTION 3: The Complete Maritime Cluster
    # ============================================================================
    
    st.markdown('<p class="section-header">Singapore\'s Complete Maritime Cluster</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore offers a comprehensive ecosystem of maritime services—this "one-stop shop" is a key 
    competitive advantage.
    """)
    
    st.markdown('<p class="subsection-header">The Seven Pillars of Maritime Singapore</p>', unsafe_allow_html=True)
    
    # Maritime cluster components
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
            'PSA, Jurong Port, cargo handlers',
            '200+ shipping lines, ship management companies',
            'Sembcorp Marine, Keppel, 40+ shipyards',
            'Bunkering companies, ship chandlers, crew managers',
            'Banks, ship financing, P&I clubs, marine insurance',
            'Law firms, arbitration centres, maritime courts',
            'Tech startups, R&D institutes, innovation centres'
        ],
        'Services Provided': [
            'Container handling, cargo storage, transshipment',
            'Liner services, vessel operations, freight forwarding',
            'Dry-docking, repairs, retrofits, conversions, new builds',
            'Fuel supply, provisions, crew changes, maintenance',
            'Ship loans, project finance, hull/cargo insurance',
            'Maritime disputes, contracts, arbitration services',
            'Digital solutions, automation, AI, blockchain, IoT'
        ],
        'Why Important': [
            'Core infrastructure for cargo movement',
            'Connectivity to global trade network',
            'Vessel maintenance and lifecycle support',
            'Operational support for vessels in port',
            'Capital and risk management for shipping',
            'Legal framework and dispute resolution',
            'Innovation and efficiency improvements'
        ]
    })
    
    st.dataframe(cluster_components, width='stretch', hide_index=True)
    
    st.markdown('<p class="subsection-header">Deep Dive: Key Pillars</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Bunkering (Marine Fuel Supply):**
    
    **Singapore's Position:**
    - **World's largest bunkering port** (40+ million tonnes annually)
    - 20+ licensed bunker suppliers
    - Supplies all types: Conventional, Low-Sulphur, LNG, Biofuels
    - Future: Methanol, ammonia bunkering infrastructure planned
    
    **Why Bunkering Matters:**
    - Vessels need fuel → Must call at bunkering ports
    - Singapore's bunkering capabilities lock in port calls
    - Revenue source for port (alongside container handling)
    - Strategic: Control over fuel supply = influence over shipping routes
    
    **Operations:**
    - Ship-to-ship bunkering (tanker transfers fuel to vessel)
    - Truck-to-ship bunkering (for smaller quantities)
    - 24/7 operations, any location in port
    - Mass Flow Meter (MFM) systems ensure accurate measurement
    
    **Ship Repair and Shipbuilding:**
    
    **Capabilities:**
    - 40+ shipyards and repair facilities
    - Dry-docking facilities for all vessel sizes
    - Specialisations: Offshore platforms, naval vessels, mega yachts
    - Retrofits: Scrubber installations, ballast water systems, efficiency upgrades
    
    **Strategic Value:**
    - Vessels need periodic maintenance (dry-docking every 2-5 years)
    - Singapore's location + expertise = natural repair hub
    - High-value industry (skilled jobs, technology transfer)
    
    **Maritime Finance:**
    
    **Financial Hub:**
    - Major banks offer ship financing
    - Singapore dollar financing growing
    - Shipping funds and private equity
    - Insurance and reinsurance markets
    
    **Why Singapore?**
    - Political stability and strong rule of law
    - Favourable tax regime for maritime
    - Proximity to Asian shipowners
    - Expertise in complex shipping finance structures
    """)
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 The Ecosystem Advantage:</strong><br>
    A shipowner can come to Singapore and:<br>
    - <strong>Dock their vessel</strong> (port operations)<br>
    - <strong>Repair and maintain</strong> (shipyard services)<br>
    - <strong>Refuel</strong> (bunkering)<br>
    - <strong>Change crew</strong> (crew management services)<br>
    - <strong>Arrange financing</strong> (maritime banks)<br>
    - <strong>Insure the vessel</strong> (marine insurance)<br>
    - <strong>Resolve disputes</strong> (maritime lawyers/arbitration)<br>
    - <strong>Upgrade technology</strong> (maritime tech companies)<br><br>
    This comprehensive one-stop offering creates <strong>high switching costs</strong> and <strong>network 
    effects</strong>—once established in Singapore, companies find it efficient to keep all services here.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 4: Digital Transformation Initiatives
    # ============================================================================
    
    st.markdown('<p class="section-header">Digital Transformation: Building Maritime 4.0</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore is investing heavily in digitising and automating maritime operations.
    """)
    
    st.markdown('<p class="subsection-header">digitalPORT@SG Programme</p>', unsafe_allow_html=True)
    
    st.markdown("""
    MPA's comprehensive digital transformation initiative for Singapore's port ecosystem.
    
    **Key Components:**
    
    **1. AI-Based Integrated Port Operations Control**
    - Centralised AI system for port-wide optimisation
    - Predictive analytics for vessel traffic and berth planning
    - Real-time decision support for port operators
    - Machine learning improves over time
    
    **2. Multi-Sensor Track Fusion**
    - Integrate data from radar, AIS, cameras, sensors
    - Complete picture of all vessel movements
    - Enhanced situational awareness
    - Improved safety and security
    
    **3. Predictive Maintenance**
    - IoT sensors on all major equipment
    - Monitor equipment health in real-time
    - Predict failures before they happen
    - Optimise maintenance schedules
    
    **4. Digital Twin**
    - Virtual replica of entire port operations
    - Test scenarios before implementing changes
    - Training environment for operators
    - Optimisation through simulation
    
    **5. Next-Gen Port Control System**
    - Modern IT infrastructure
    - Cloud-based platforms
    - APIs for integration with shipping lines
    - Enhanced cybersecurity
    """)
    
    st.markdown('<p class="subsection-header">digitalOCEANS Platform</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Vision:** Digital twin of Singapore's entire maritime domain
    
    **Capabilities:**
    - **Real-time situational awareness**: Track all vessels in Singapore waters
    - **Data integration**: Connect all maritime stakeholders on single platform
    - **Analytics**: Advanced analytics on patterns, efficiency, safety
    - **Collaboration**: Shared platform for government, port operators, shipping lines
    
    **Use Cases:**
    - Optimise vessel routing and berth allocation
    - Coordinate pilot and tug services
    - Monitor marine traffic for safety
    - Environmental monitoring and compliance
    - Emergency response coordination
    
    **Benefits:**
    - Improved operational efficiency
    - Enhanced safety and security
    - Better environmental outcomes
    - Data-driven decision-making
    - Platform for innovation (third-party apps)
    """)
    
    st.markdown('<p class="subsection-header">Electronic Documentation</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Paperless Trade Initiatives:**
    
    **Electronic Bill of Lading (eBL):**
    - Digital replacement for paper Bill of Lading
    - Blockchain-based for security and authenticity
    - Instant transfer (vs days for physical document)
    - Reduces fraud risk
    - Cost savings: Estimated $6.5 billion annually globally if fully adopted
    
    **Electronic Bunker Delivery Note (e-BDN):**
    - Digital record of fuel delivered to vessels
    - Automated data capture
    - Reduces errors and fraud
    - Integrated with port systems
    
    **Digital Certificates:**
    - Ship certificates (safety, security, classification)
    - Crew certificates
    - Cargo certificates
    - Instantly verifiable, reducing delays
    
    **PORTNET:**
    - Singapore's maritime single window
    - All port-related transactions through one system
    - Integration with customs, immigration
    - 24/7 online clearance
    - Paperless vessel clearance since 1980s (pioneer)
    """)
    
    # ============================================================================
    # SECTION 5: Innovation Ecosystem
    # ============================================================================
    
    st.markdown('<p class="section-header">Maritime Innovation Ecosystem</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore actively cultivates maritime innovation through funding, infrastructure, and partnerships.
    """)
    
    st.markdown('<p class="subsection-header">BLOCK71 Maritime Innovation Hub</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Overview:**
    - Launched 2018 by MPA
    - Accelerator for maritime technology startups
    - Connect startups with industry challenges
    - Funding, mentorship, pilot opportunities
    
    **Focus Areas:**
    - Autonomous vessels and robotics
    - AI and data analytics
    - Cybersecurity
    - Green technologies (alternative fuels, efficiency)
    - Blockchain and digital trade
    - IoT and sensors
    
    **How It Works:**
    1. **Startups apply** with innovative maritime solutions
    2. **Selection** based on technology potential and market fit
    3. **Acceleration** programme: Funding, mentorship, workspace
    4. **Pilot projects** with maritime companies (real-world testing)
    5. **Scale** successful solutions globally
    
    **Success Stories:**
    - 100+ startups supported
    - Multiple technologies deployed commercially
    - Singapore positioned as maritime tech hub
    
    **Strategic Value:**
    - Innovation attracts talent and investment
    - Solutions benefit Singapore's ports first
    - Export technology globally (new revenue stream)
    - Maintain competitive edge through innovation
    """)
    
    st.markdown('<p class="subsection-header">Maritime Innovation and Technology (MINT) Fund</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Purpose:**
    - Co-fund R&D projects
    - Support test-bedding of new technologies
    - Accelerate adoption of innovation
    
    **How It Works:**
    - MPA co-funds up to 50% of project costs
    - Companies contribute remainder
    - Focus on technologies benefiting Singapore maritime
    - Fast approval process (encourage experimentation)
    
    **Eligible Technologies:**
    - Digitalisation and automation
    - Green and sustainable shipping
    - Safety and security enhancements
    - Productivity improvements
    - Novel business models
    
    **Impact:**
    - Reduces risk for companies to innovate
    - Accelerates technology adoption
    - Builds local innovation capabilities
    """)
    
    st.markdown('<p class="subsection-header">Academic and Research Partnerships</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Singapore Maritime Institute (SMI):**
        - Coordinates maritime R&D
        - Funds research projects
        - Connects academia with industry
        - Focus areas: Automation, sustainability, digitalisation
        
        **Universities:**
        - National University of Singapore (NUS)
        - Nanyang Technological University (NTU)
        - Singapore University of Technology and Design (SUTD)
        - Maritime programmes and research centres
        """)
    
    with col2:
        st.markdown("""
        **Research Focus:**
        - Autonomous vessels
        - Port automation and optimisation
        - Alternative fuels and propulsion
        - Digitalisation and cybersecurity
        - Supply chain resilience
        
        **Approach:**
        - Industry-led research (solve real problems)
        - Test-bedding facilities available
        - Student internships and projects
        - Knowledge transfer to industry
        """)
    
    # ============================================================================
    # SECTION 6: Workforce Development
    # ============================================================================
    
    st.markdown('<p class="section-header">Maritime Workforce Development</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Developing skilled maritime talent is critical for maintaining competitiveness, especially with 
    increasing automation.
    """)
    
    st.markdown('<p class="subsection-header">Singapore Maritime Academy (SMA)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Mission:**
    - Train maritime professionals
    - Sea-going and shore-based careers
    - Technical and management skills
    
    **Programmes:**
    - Diplomas in maritime studies, nautical studies, marine engineering
    - Degree programmes (with universities)
    - Professional certifications
    - Continuing education and upskilling
    
    **Facilities:**
    - Ship simulators (bridge, engine room)
    - Container terminal simulator
    - Safety training facilities
    - Industry-standard equipment
    
    **Industry Partnership:**
    - Curriculum designed with industry input
    - Internships and apprenticeships
    - Guest lecturers from industry
    - Guaranteed employment for graduates
    """)
    
    st.markdown('<p class="subsection-header">SkillsFuture and Workforce Transition</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Challenge:**
    - Automation reduces traditional port jobs (crane operators, drivers)
    - Need to reskill displaced workers
    - Create new jobs in technology and management
    
    **SkillsFuture Maritime:**
    - Government-funded training programmes
    - Reskilling for new roles (IT, data analytics, automation management)
    - Career coaching and transition support
    - Portable skills development
    
    **New Job Categories:**
    - Automation system operators (remote crane control)
    - Maintenance technicians (service AGVs, automated equipment)
    - Data analysts (optimise operations using data)
    - Cybersecurity specialists
    - Technology project managers
    
    **Approach:**
    - Gradual transition (automation phased over 20 years)
    - Natural attrition (retirements)
    - Retraining programmes for willing workers
    - Support for career transitions
    """)
    
    # ============================================================================
    # SECTION 7: Sustainability Initiatives
    # ============================================================================
    
    st.markdown('<p class="section-header">Green Maritime Initiatives</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore is positioning itself as a leader in maritime sustainability.
    """)
    
    st.markdown('<p class="subsection-header">Green Port Programme</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Incentives for Green Vessels:**
    - **Green Port Programme**: Rebates on port dues for eco-friendly vessels
    - Criteria: NOx emissions, SOx emissions, CO2 efficiency
    - Vessels with better environmental performance pay less
    - Encourages shipping lines to invest in green technology
    
    **Green Shipping Corridor:**
    - Collaboration with other ports
    - Preferential treatment for green vessels
    - Create demand for sustainable shipping
    
    **Shore Power:**
    - Vessels plug into grid electricity at berth
    - Shut down diesel generators (zero emissions at berth)
    - Tuas Mega Port designed with shore power capability
    - Incentives for vessels to use shore power
    """)
    
    st.markdown('<p class="subsection-header">Alternative Fuels Infrastructure</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Multi-Fuel Strategy:**
    
    **Current:**
    - LNG bunkering well-established
    - Multiple LNG bunker vessels operating
    - Supporting LNG-powered vessel growth
    
    **Developing:**
    - Methanol bunkering infrastructure
    - Pilot programmes with shipping lines
    - Building capabilities for green methanol
    
    **Future:**
    - Ammonia bunkering (2030s)
    - Hydrogen infrastructure (niche applications)
    - Biofuels blending and supply
    
    **Strategic Importance:**
    - Position as leading alternative fuel bunkering hub
    - Flexibility as industry transitions
    - Lock in bunkering business regardless of fuel type
    - Support shipping industry decarbonisation
    """)
    
    # ============================================================================
    # SECTION 8: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Singapore's Position:**
        - World's #2 container port (37.3M TEU)
        - 200+ shipping lines, 600+ ports connected
        - Strategic location (Malacca Strait, Asia-Europe route)
        - Operational excellence (>90% BOA, <24h turnaround)
        
        **MPA's Dual Role:**
        - Regulator: Safety, security, standards, environment
        - Developer: Industry promotion, innovation, talent, infrastructure
        - Coordinated strategy enables long-term vision
        
        **Complete Maritime Cluster:**
        - Port operations, shipping lines, ship repair
        - Bunkering (world's largest), ancillary services
        - Maritime finance, insurance, law
        - Technology and innovation
        - One-stop ecosystem advantage
        """)
    
    with col2:
        st.markdown("""
        **Digital Transformation:**
        - digitalPORT@SG: AI, predictive maintenance, digital twin
        - digitalOCEANS: Maritime domain digital platform
        - Electronic documentation: eBL, e-BDN, certificates
        - PORTNET: Maritime single window since 1980s
        
        **Innovation Ecosystem:**
        - BLOCK71: Maritime tech accelerator (100+ startups)
        - MINT Fund: Co-fund R&D and pilots
        - Academic partnerships: NUS, NTU, SUTD
        - Test-bedding facilities and support
        
        **Sustainability:**
        - Green Port Programme (incentives for eco-vessels)
        - Alternative fuels: LNG, methanol, ammonia (future)
        - Shore power infrastructure
        - Positioning as green maritime leader
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Singapore has built a comprehensive maritime ecosystem over 70+ years, 
    combining world-class port infrastructure with a complete cluster of services (bunkering, ship repair, 
    finance, legal, technology). MPA's dual role as regulator and developer enables coordinated long-term 
    strategy. Digital transformation initiatives (digitalPORT@SG, digitalOCEANS) position Singapore as a 
    Maritime 4.0 leader. The innovation ecosystem (BLOCK71, MINT Fund, academic partnerships) cultivates 
    maritime technology startups. Sustainability initiatives (green port programme, alternative fuels 
    infrastructure) prepare for decarbonisation. This comprehensive approach creates high switching costs 
    and network effects—once companies establish operations in Singapore, the ecosystem makes it efficient 
    to keep all maritime services here.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** ⚓ Port Strategy & Competition - Explore the critical success factors for transshipment 
    hubs, competitive dynamics, strategic planning frameworks, and Singapore's response to regional competition.
    """)
