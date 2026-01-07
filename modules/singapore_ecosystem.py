import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">🏛️ Maritime Singapore Ecosystem</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand Singapore's unique maritime governance structure, MPA's dual role as regulator and promoter, 
    and how the complete maritime cluster creates a world-leading ecosystem.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Singapore's Maritime Position
    # ============================================================================
    
    st.markdown('<p class="section-header">Singapore: The World\'s Premier Maritime Hub</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore is not just a port—it's a comprehensive **International Maritime Centre (IMC)** offering 
    a complete suite of maritime services. This ecosystem approach is what differentiates Singapore from 
    competitors who focus solely on cargo handling.
    """)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Container Throughput", "37.3M TEU", help="Annual container volume (2023)")
    with col2:
        st.metric("Vessel Calls", "130,000+", help="Annual vessel arrivals")
    with col3:
        st.metric("Connected Ports", "600+", help="Ports in 120+ countries")
    with col4:
        st.metric("Shipping Lines", "200+", help="Active container services")
    
    st.markdown("""
    **Singapore's Unique Strengths:**
    
    - **#1 Container Transshipment Hub:** ~85% of throughput is transshipment (not origin/destination)
    - **#1 Bunkering Port:** 40+ million tonnes of marine fuel supplied annually
    - **Strategic Location:** On main Asia-Europe trade route, center of Southeast Asia
    - **Straits of Malacca/Singapore:** 33% of global seaborne trade passes through
    - **Deep Natural Harbor:** Can accommodate largest vessels (16+ meter draft)
    - **Political Stability:** Predictable, pro-business government policies
    - **World-Class Infrastructure:** State-of-the-art terminals and equipment
    - **Skilled Workforce:** Strong technical and management capabilities
    """)
    
    # Singapore's role visualization
    services_data = pd.DataFrame({
        'Service Category': [
            'Container Handling',
            'Bunkering',
            'Ship Repair',
            'Maritime Finance',
            'Ship Management',
            'Maritime Legal',
            'Maritime Tech',
            'Logistics Services'
        ],
        'Global Ranking': [1, 1, 3, 3, 1, 1, 2, 1],
        'Description': [
            '37.3M TEU, world\'s busiest transshipment hub',
            '40M+ tonnes fuel, largest bunkering port',
            'Most advanced facilities in Southeast Asia',
            'Major center for ship financing and insurance',
            'Home to 130+ ship management companies',
            'Leading maritime arbitration and legal center',
            'Innovation hub for maritime technology',
            'Complete logistics and supply chain services'
        ]
    })
    
    st.dataframe(services_data, width='stretch', hide_index=True)
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 The Singapore Advantage:</strong> Unlike ports that only handle cargo, Singapore offers a 
    **complete maritime cluster**. A shipping line can:
    - Transship containers at PSA terminals
    - Refuel their vessels (bunkering)
    - Conduct repairs at Sembcorp or Keppel shipyards
    - Arrange ship financing from Singapore banks
    - Purchase marine insurance from Singapore underwriters
    - Resolve disputes through Singapore maritime arbitration
    - Access maritime technology and innovation partners
    
    This one-stop ecosystem creates enormous switching costs and loyalty.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 2: MPA - Maritime and Port Authority of Singapore
    # ============================================================================
    
    st.markdown('<p class="section-header">MPA: The Regulator and Promoter</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The Maritime and Port Authority of Singapore (MPA) is unique in the maritime world because it plays 
    **dual roles** as both regulator and industry promoter.
    """)
    
    st.markdown('<p class="subsection-header">MPA Formation and Vision</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Formation Timeline:**
    
    **1996: MPA Created through Merger**
    - **Singapore Marine Department** (regulatory functions)
    - **PSA's Regulatory Departments** (port regulation)
    - **National Maritime Board** (maritime promotion)
    
    **2004: Industry Promotion Enhanced**
    - Took over industry promotion functions from IE Singapore (now Enterprise Singapore)
    - Became comprehensive regulator + promoter
    
    **MPA Vision:**
    > "A leading maritime agency driving Singapore's global maritime aspirations"
    
    **Dual Identity:**
    - **Regulator** for safety, security, environment
    - **Promoter** for industry growth and development
    """)
    
    # MPA organizational structure
    st.markdown('<p class="subsection-header">MPA Roles and Responsibilities</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **As PORT AUTHORITY:**
        - Manage port operations and traffic
        - Allocate berths and anchorages
        - Coordinate vessel movements
        - Ensure safe navigation in port waters
        - Maintain marine infrastructure
        
        **As PORT REGULATOR:**
        - Set port safety standards
        - License port operators and service providers
        - Monitor compliance with regulations
        - Enforce maritime laws
        - Investigate marine incidents
        
        **As PORT PLANNER:**
        - Long-term port development planning
        - Infrastructure investment decisions
        - Tuas Mega Port masterplanning
        - Land use optimization
        - Future capacity expansion
        """)
    
    with col2:
        st.markdown("""
        **As IMC PROMOTER:**
        - Attract maritime companies to Singapore
        - Develop maritime services cluster
        - Promote ship registration
        - Support maritime startups and innovation
        - Market Singapore as maritime hub
        
        **As IMC DEVELOPER:**
        - Develop talent and workforce
        - Support R&D and innovation
        - Build maritime technology capabilities
        - Foster maritime finance and legal services
        - Develop maritime knowledge hub
        
        **As NATIONAL MARITIME REPRESENTATIVE:**
        - Represent Singapore at IMO (International Maritime Organization)
        - Participate in regional maritime forums
        - Negotiate bilateral maritime agreements
        - Shape international maritime standards
        - Advocate for Singapore's maritime interests
        """)
    
    # MPA roles visualization
    fig = go.Figure()
    
    roles_data = [
        {'Role': 'Port Authority', 'Score': 100, 'Color': '#3B82F6'},
        {'Role': 'Port Regulator', 'Score': 100, 'Color': '#2563EB'},
        {'Role': 'Port Planner', 'Score': 100, 'Color': '#1E40AF'},
        {'Role': 'IMC Promoter', 'Score': 100, 'Color': '#10B981'},
        {'Role': 'IMC Developer', 'Score': 100, 'Color': '#059669'},
        {'Role': 'National Rep', 'Score': 100, 'Color': '#047857'}
    ]
    
    fig.add_trace(go.Barpolar(
        r=[d['Score'] for d in roles_data],
        theta=[d['Role'] for d in roles_data],
        marker=dict(color=[d['Color'] for d in roles_data]),
        name='MPA Roles'
    ))
    
    fig.update_layout(
        title={
            'text': 'MPA\'s Six Key Roles',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#1F2937'}
        },
        polar=dict(
            radialaxis=dict(visible=False, range=[0, 100])
        ),
        showlegend=False,
        height=500
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    <div class="insight-box">
    <strong>🎯 Why This Dual Role Matters:</strong> Most countries separate regulation (government) from 
    promotion (industry associations). MPA's unique structure allows:
    - **Coordinated policy-making**: Regulations designed with industry growth in mind
    - **Fast decision-making**: Single agency coordinates all maritime matters
    - **Industry responsiveness**: Direct channel between government and industry
    - **Strategic planning**: Long-term vision with regulatory backing
    
    This explains why Singapore can implement major changes like Tuas Mega Port so effectively.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 3: Singapore Maritime Ecosystem
    # ============================================================================
    
    st.markdown('<p class="section-header">The Complete Maritime Cluster</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore has deliberately built a **complete maritime ecosystem** where all components support and 
    reinforce each other.
    """)
    
    st.markdown('<p class="subsection-header">Core Components of the Cluster</p>', unsafe_allow_html=True)
    
    # Ecosystem components
    ecosystem_components = pd.DataFrame({
        'Cluster Component': [
            'Port Operations',
            'Ship Owners & Operators',
            'Shipbuilding & Repair',
            'Maritime Finance',
            'Maritime Insurance',
            'Maritime Legal Services',
            'Maritime Tech & Innovation',
            'Logistics & Supply Chain',
            'Bunkering Services',
            'Maritime Education',
            'Classification Societies',
            'Maritime Agencies'
        ],
        'Key Players / Details': [
            'PSA (terminals), Jurong Port (multipurpose)',
            '130+ ship management companies, 5,000+ vessels registered',
            'Sembcorp Marine, Keppel Offshore & Marine - leading repair facilities',
            'DBS, OCBC, Standard Chartered - ship financing; Insurance placement',
            'Major P&I clubs, hull & machinery underwriters',
            'Top-tier law firms specializing in maritime; SCMA arbitration center',
            'BLOCK71 maritime startups, R&D centers, digitalPORT@SG initiatives',
            'Global freight forwarders, 3PLs, warehouse operators',
            '40M+ tonnes annually, major bunkering companies (Chemoil, Sentek)',
            'Singapore Maritime Academy, NUS Maritime programs',
            'Lloyd\'s Register, DNV, ABS, ClassNK offices',
            'IMO regional presence, ASEAN maritime cooperation'
        ],
        'Global Standing': [
            '#1 Container Port',
            'Top 5 Ship Registry',
            'Top 3 in Asia',
            'Top 3 Globally',
            'Major Center',
            '#1 in Asia',
            'Leading Hub',
            'Top Tier',
            '#1 Globally',
            'Regional Leader',
            'Complete Coverage',
            'Strategic Center'
        ]
    })
    
    st.dataframe(ecosystem_components, width='stretch', hide_index=True)
    
    st.markdown('<p class="subsection-header">The Cluster Network Effect</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Each component strengthens the others, creating a **self-reinforcing ecosystem**:
    
    **Example 1: Ship Owner → Multiple Services**
    - Ship owner establishes office in Singapore
    - Uses Singapore banks for ship financing
    - Registers vessels under Singapore flag
    - Sends vessels to Singapore for repairs
    - Bunkers in Singapore
    - Uses Singapore lawyers for contracts
    - Calls at Singapore port for cargo
    
    **Example 2: Port Success → Industry Growth**
    - High port throughput attracts shipping lines
    - Shipping lines establish regional HQs
    - Need for finance, legal, insurance grows
    - Service providers set up Singapore offices
    - Concentration of expertise attracts more companies
    - Creates jobs for maritime professionals
    - Attracts talent and education programs
    
    **Result:** Once established, very difficult for competitors to replicate this complete cluster.
    """)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ Government Policy Foundation:</strong> This cluster didn't happen by accident. Singapore 
    government deliberately:
    - Provides **stable, predictable policies** ("no U-turns")
    - Maintains **pro-business environment** with competitive taxes
    - Invests in **infrastructure** before demand (Tuas planning started in 2012)
    - Develops **talent pipelines** through education
    - Creates **regulatory sandboxes** for innovation
    - Actively **markets Singapore** internationally
    
    As former Minister said: "Maritime Singapore would have to go beyond its status as a major hub to 
    become an international maritime centre providing a full suite of services."
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 4: Innovation and Digitalization
    # ============================================================================
    
    st.markdown('<p class="section-header">Innovation: Maritime Regulatory Sandbox</p>', unsafe_allow_html=True)
    
    st.markdown("""
    MPA operates a **Maritime Regulatory Sandbox** to accelerate innovation while managing risk. 
    This allows companies to test new technologies and business models with regulatory flexibility.
    """)
    
    st.markdown('<p class="subsection-header">Two Key Focus Areas</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **1. Accelerating Digitalisation & Innovation**
        
        **digitalPORT@SG Initiative:**
        - AI-based integrated port operations control
        - Multi-sensor track fusion for vessel monitoring
        - Predictive analytics for berth planning
        - Real-time port traffic optimization
        
        **digitalOCEANS Platform:**
        - Digital twin of Singapore's maritime domain
        - Real-time situational awareness
        - Data sharing across stakeholders
        - Integration with PORTNET
        
        **Digital Solutions:**
        - **eBL (electronic Bill of Lading)**: Blockchain-based, paperless documentation
        - **e-BDN (electronic Bunker Delivery Note)**: Digital fuel receipts
        - **e-Certificates**: Digital certification for vessels
        
        **BLOCK71 Maritime:**
        - First maritime ecosystem innovation builder in region (2018)
        - Connects startups with industry challenges
        - Funding and mentorship programs
        - Test bed for maritime technologies
        """)
    
    with col2:
        st.markdown("""
        **2. Drive Maritime Decarbonisation**
        
        **Future Fuels Port Network:**
        - Singapore as bunkering hub for alternative fuels
        - LNG bunkering capabilities
        - Methanol bunkering infrastructure
        - Ammonia bunkering (future)
        
        **Low-to-Zero Carbon Fuel Adoption:**
        - Guidelines for ammonia and methanol use
        - Safety standards development
        - Infrastructure planning
        - Industry collaboration (SABRE consortium)
        
        **Green Port Initiatives:**
        - Shore power for vessels at berth
        - Electrification of port equipment
        - Carbon footprint tracking
        - Incentives for green vessels
        
        **Technology Development:**
        - Funding for green maritime R&D
        - Collaboration with research institutions
        - International partnerships
        - Net-zero 2050 pathway development
        """)
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 The Sandbox Approach:</strong> Rather than waiting for perfect regulations, MPA allows 
    controlled testing:
    - Companies apply to test new technology/service
    - MPA grants temporary regulatory relief
    - Real-world trials with risk controls
    - Learn from results, then create permanent regulations
    - Fast-tracks innovation while maintaining safety
    
    This approach has attracted global maritime tech companies to test innovations in Singapore first.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 5: Talent Development
    # ============================================================================
    
    st.markdown('<p class="section-header">Talent Development: Building Maritime Workforce</p>', unsafe_allow_html=True)
    
    st.markdown("""
    A sophisticated maritime industry requires sophisticated talent. Singapore invests heavily in 
    developing maritime human capital.
    """)
    
    st.markdown('<p class="subsection-header">Education and Training Programs</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Academic Programs:**
        - **Singapore Maritime Academy (SMA)**: Diploma programs for seafarers
        - **National University of Singapore (NUS)**: Maritime studies, shipping management
        - **Nanyang Technological University (NTU)**: Maritime engineering, logistics
        - **Singapore Management University (SMU)**: Shipping and transport management
        
        **Professional Development:**
        - **Singapore Maritime Foundation (SMF)**: Scholarships and career development
        - **Maritime Cluster Fund**: Co-funding for capability building
        - Executive education programs
        - Industry attachment programs
        """)
    
    with col2:
        st.markdown("""
        **Career Pathways:**
        - **Technical**: Naval architects, marine engineers, port engineers
        - **Operations**: Ship captains, port operators, terminal managers
        - **Commercial**: Shipping managers, chartering, freight forwarding
        - **Legal**: Maritime lawyers, arbitrators
        - **Finance**: Ship finance, insurance, risk management
        - **Technology**: Maritime IT, digitalization, innovation
        
        **"Sea The Difference" Campaign:**
        - MPA career promotion initiative
        - Showcases diverse maritime careers
        - Attracts young talent to industry
        - Highlights innovation and technology aspects
        """)
    
    st.markdown("""
    **The Talent Ecosystem:**
    
    Singapore's approach creates a **virtuous cycle**:
    1. World-class industry attracts talented professionals
    2. Presence of talent attracts more companies
    3. Companies invest in training and development
    4. Strong education institutions produce more graduates
    5. Government supports with scholarships and programs
    6. Ecosystem becomes globally competitive for talent
    """)
    
    # ============================================================================
    # SECTION 6: Government Support and Policies
    # ============================================================================
    
    st.markdown('<p class="section-header">Government Support: The Foundation</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore's maritime success is underpinned by **consistent, long-term government support** and 
    **pro-business policies**.
    """)
    
    st.markdown('<p class="subsection-header">Key Government Attributes</p>', unsafe_allow_html=True)
    
    # Government support factors
    support_factors = pd.DataFrame({
        'Factor': [
            'Political Stability',
            'Long-Term Thinking',
            'Policy Consistency',
            'Infrastructure Investment',
            'Regulatory Efficiency',
            'Pro-Business Environment',
            'Rule of Law',
            'Transparency'
        ],
        'Description': [
            'Stable government for decades, predictable succession',
            '10-20 year planning horizons (Tuas announced 2012 for 2040)',
            '"No U-turns" - policies maintained across administrations',
            'S$20B+ investment in Tuas before first container handled',
            'Fast approvals, streamlined processes, single-window clearance',
            'Competitive tax rates, incentives for maritime companies',
            'Strong legal framework, enforceable contracts, low corruption',
            'Clear regulations, published criteria, fair processes'
        ],
        'Impact on Maritime': [
            'Companies confident to make long-term investments',
            'Industry can plan knowing government support continues',
            'Reduces risk and uncertainty for investors',
            'World-class facilities attract mega vessels and alliances',
            'Low bureaucracy costs, fast business setup',
            'Competitive operating costs despite high land/labor costs',
            'Singapore as trusted location for contracts and arbitration',
            'Clear rules attract international companies'
        ]
    })
    
    st.dataframe(support_factors, width='stretch', hide_index=True)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🎯 The Singapore Model:</strong> A Minister explained Singapore's approach:
    
    > "Singapore will live up to its reputation for stable pro-business policies that provide certainty. 
    > We avoid back tracking and U-turns, and we set out to make companies feel welcome and a valued part 
    > of the Singapore maritime ecosystem."
    
    This consistency and reliability is perhaps Singapore's greatest competitive advantage—companies know 
    what to expect 10, 20, 30 years into the future.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 7: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Singapore's Position:**
        - 37.3M TEU container throughput
        - 130,000+ annual vessel calls
        - Connected to 600+ ports globally
        - 85% transshipment (critical hub role)
        - #1 bunkering port (40M+ tonnes)
        
        **MPA's Unique Structure:**
        - Dual role: Regulator + Promoter
        - Six key functions: Authority, Regulator, Planner, IMC Promoter, IMC Developer, National Rep
        - Formed 1996 through strategic merger
        - Single coordinating agency for all maritime
        
        **Complete Maritime Cluster:**
        - Port operations + ship owners/operators
        - Finance, insurance, legal services
        - Shipbuilding, repair, bunkering
        - Technology, innovation, education
        - Self-reinforcing network effects
        """)
    
    with col2:
        st.markdown("""
        **Innovation Leadership:**
        - Maritime Regulatory Sandbox
        - Digital initiatives (eBL, digitalPORT, digitalOCEANS)
        - BLOCK71 startup ecosystem
        - Decarbonization and green fuels
        - Test bed for new technologies
        
        **Talent Development:**
        - Multiple educational pathways
        - Scholarships and career programs
        - "Sea The Difference" campaign
        - Professional development support
        
        **Government Support:**
        - Political stability and consistency
        - Long-term planning (Tuas 2012→2040)
        - Pro-business policies
        - Major infrastructure investment
        - "No U-turns" policy commitment
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Singapore's maritime leadership isn't just about having a good port—
    it's about creating a complete ecosystem where government, industry, education, finance, and innovation 
    all work together. MPA's dual role as regulator and promoter allows coordinated policy-making. The 
    complete maritime cluster creates massive switching costs and network effects. Stable, long-term 
    government support provides the foundation for sustained competitiveness. This integrated approach 
    is extremely difficult for competitors to replicate.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** ⚓ Port Strategy & Competition - Understand what makes ports competitive, the factors 
    that determine success or failure, and how Singapore positions itself against regional and global rivals.
    """)
