import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">🏗️ Tuas Mega Port Case Study</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand Singapore's strategic rationale for building Tuas Mega Port, its design features, 
    implementation challenges, and whether this massive investment will be sufficient to maintain 
    Singapore's competitive position in the evolving maritime landscape.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Why Tuas? The Strategic Imperative
    # ============================================================================
    
    st.markdown('<p class="section-header">Why Tuas? The Strategic Imperative</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Tuas Mega Port represents Singapore's largest infrastructure project—a S$20+ billion investment 
    to consolidate and expand container terminal capacity. Understanding **why** Singapore is making 
    this massive bet is crucial.
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Investment", "S$20B+", help="Total investment over multiple phases")
    with col2:
        st.metric("Target Capacity", "65M TEU", help="Annual capacity when fully completed by 2040")
    with col3:
        st.metric("Current Capacity", "37.3M TEU", help="Singapore's current throughput (2023)")
    with col4:
        st.metric("Growth Headroom", "+74%", help="Capacity increase from current levels")
    
    st.markdown('<p class="subsection-header">The Five Strategic Drivers</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **1. Consolidation for Efficiency Gains**
    
    **Current Problem:**
    - Container operations spread across **multiple terminals**: Tanjong Pagar, Keppel, Brani, Pasir Panjang
    - **Fragmentation** reduces operational efficiency
    - Vessels may need to call at multiple terminals to discharge/load all cargo
    - **Inter-terminal transfers** add cost and time
    - Difficult to optimise resources across separate facilities
    
    **Tuas Solution:**
    - **Single mega port** consolidates all container operations
    - **Continuous quay wall**: Vessels can berth anywhere along 26+ km of berth
    - **Integrated operations**: Optimise cranes, yard space, labour across entire port
    - **Eliminate inter-terminal transfers**: All cargo in one location
    - **Economies of scale**: Shared infrastructure, centralised control
    
    **Expected Benefits:**
    - 20-30% improvement in operational efficiency
    - Lower cost per TEU handled
    - Faster vessel turnaround times
    - Better resource utilisation
    """)
    
    st.markdown("""
    **2. Attract and Accommodate Mega Alliances and ULCV**
    
    **The Challenge:**
    - Mega alliances (2M, Ocean Alliance, THE Alliance) control 83% of global volumes
    - Ultra Large Container Vessels (ULCV) now exceed 24,000 TEU capacity
    - These vessels require:
      - **Deep berths**: 16-18 metre draft
      - **Long berths**: 400+ metre LOA
      - **Super-sized cranes**: 65-80 metre outreach, 24 containers across
      - **High productivity**: 8-12 cranes working simultaneously
      - **Fast turnaround**: <24-36 hours port stay
    
    **Existing Limitations:**
    - Some older terminals cannot accommodate latest mega vessels
    - Berth depth limitations in some areas
    - Crane coverage gaps
    - Congestion during peak periods
    
    **Tuas Advantage:**
    - **Purpose-built for mega vessels**: 16+ metre depth, long berths
    - **Latest crane technology**: Super-post-Panamax cranes with 65+ metre outreach
    - **Dedicated alliance terminals**: Customised facilities for major alliances
    - **Ample capacity**: Room for 8-12 cranes per vessel without congestion
    
    **Strategic Importance:**
    - Lock in long-term commitments from mega alliances
    - Prevent alliances from shifting to competing ports
    - Maintain hub status as vessel sizes continue growing
    """)
    
    st.markdown("""
    **3. Pre-emptive Response to Regional Competition**
    
    **Competitive Threats:**
    - **Malaysia**: Carey Island, Melaka Gateway (strategic Malacca Strait locations)
    - **Indonesia**: Tanjung Priok expansion (serving massive domestic market)
    - **Thailand**: Proposed Kra Canal (would bypass Singapore entirely)
    - **Vietnam**: Cai Mep expansion (riding on Vietnamese economic growth)
    
    **The "Build It Before They Do" Logic:**
    - If Singapore waits, competitors build first and capture volumes
    - Large infrastructure takes 10-15 years from planning to operation
    - **First-mover advantage**: Lock in shipping line commitments early
    - **Scale advantages**: Largest, most efficient hub is hardest to displace
    
    **Tuas as Competitive Moat:**
    - **65M TEU capacity**: Nearly double any single competitor
    - **Technology leadership**: Most automated, efficient port in region
    - **Long-term contracts**: Shipping lines sign 20-30 year terminal leases
    - **Switching costs**: Once committed to Tuas, expensive to switch to competitor
    
    **The Calculation:**
    - Better to build and have excess capacity than lose market share to competitors
    - Excess capacity provides **flexibility** and **bargaining power**
    - Can offer competitive pricing when needed (marginal cost is low)
    """)
    
    st.markdown("""
    **4. Enable Next-Generation Technology and Automation**
    
    **Brownfield Constraints:**
    - **Existing terminals** difficult to retrofit with automation
    - Layout not optimised for AGVs, ARMG
    - Gradual automation creates complexity (mixed manual/automated operations)
    - Infrastructure not designed for current technology
    
    **Greenfield Opportunity (Tuas):**
    - **Design from scratch** for full automation
    - Purpose-built for AGVs, ARMG, automated systems
    - Optimal layout for efficiency
    - Latest technology integrated from day one
    - No legacy constraints
    
    **Technology Features:**
    - **Automated Guided Vehicles (AGVs)**: Battery-electric, zero emissions
    - **Automated RMG (ARMG)**: Fully automated yard cranes, 24/7 operations
    - **Advanced TOS**: AI-powered CITOS with operational simulation
    - **Predictive analytics**: Optimise operations in real-time
    - **Remote control centres**: Centralised monitoring and management
    
    **Competitive Advantage:**
    - 30-40% higher productivity than conventional terminals
    - 70-80% reduction in labour costs
    - 24/7 consistent operations
    - Lower long-term operating costs despite higher upfront investment
    """)
    
    st.markdown("""
    **5. Green and Climate-Resilient Design**
    
    **Climate Imperatives:**
    - **Sea level rise**: Projected 0.5-1.0 metre by 2100 (some models higher)
    - **Extreme weather**: More intense storms, heavier rainfall
    - **Decarbonisation**: Need to meet IMO 2050 net-zero targets
    
    **Tuas Green Features:**
    
    **Climate Resilience:**
    - **Built 5 metres above mean sea level**: Protects against century-long sea level rise projections
    - **Reinforced structures**: Designed for more extreme weather
    - **Enhanced drainage**: Handle increased rainfall intensity
    
    **Zero Emissions Operations:**
    - **Fully electrified quay cranes**: No diesel generators, powered by grid
    - **Battery-electric AGVs**: Zero direct emissions, renewable energy charging
    - **Shore power**: Vessels plug into grid electricity at berth
    - **Solar panels**: Extensive solar canopies throughout terminal (one of world's largest solar ports)
    
    **Sustainable Design:**
    - **Energy-efficient buildings**: LED lighting, smart HVAC
    - **Waste circularity**: Recycle and reuse construction and operational waste
    - **Green spaces**: Biodiversity preservation where possible
    - **Sustainable reclamation**: Use of incineration ash and dredged material
    
    **Strategic Value:**
    - **Future-proof**: Won't need expensive retrofitting for climate adaptation
    - **Regulatory compliance**: Meets future environmental regulations
    - **Customer demand**: Shipping lines increasingly demand green ports
    - **Brand value**: Positions Singapore as sustainability leader
    """)
    
    # Strategic drivers visualization
    drivers_importance = pd.DataFrame({
        'Driver': [
            'Consolidation\nEfficiency',
            'Accommodate\nMega Vessels',
            'Regional\nCompetition',
            'Technology\nLeadership',
            'Climate\nResilience'
        ],
        'Strategic Importance': [95, 100, 90, 85, 80],
        'Urgency': [85, 95, 100, 80, 90]
    })
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Strategic Importance',
        x=drivers_importance['Driver'],
        y=drivers_importance['Strategic Importance'],
        marker_color='#3B82F6'
    ))
    
    fig.add_trace(go.Bar(
        name='Urgency',
        x=drivers_importance['Driver'],
        y=drivers_importance['Urgency'],
        marker_color='#10B981'
    ))
    
    fig.update_layout(
        title={
            'text': 'Tuas Strategic Drivers: Importance vs Urgency',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        yaxis_title="Score (0-100)",
        barmode='group',
        height=450,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='#E5E7EB', range=[0, 110])
    )
    
    st.plotly_chart(fig, width='stretch')
    
    # ============================================================================
    # SECTION 2: Tuas Design and Features
    # ============================================================================
    
    st.markdown('<p class="section-header">Tuas Mega Port: Design and Features</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Tuas is not just bigger—it's fundamentally different in design philosophy and operational approach.
    """)
    
    st.markdown('<p class="subsection-header">Scale and Capacity</p>', unsafe_allow_html=True)
    
    # Tuas specifications
    tuas_specs = pd.DataFrame({
        'Specification': [
            'Total Land Area',
            'Reclaimed Land',
            'Quay Length',
            'Number of Berths',
            'Water Depth',
            'Annual Capacity (Phase 1)',
            'Ultimate Capacity (2040)',
            'Quay Cranes',
            'Yard Cranes',
            'AGVs',
            'Total Investment'
        ],
        'Value': [
            '1,337 hectares (13.4 km²)',
            '~800 hectares of new land',
            '26+ kilometres continuous',
            '60+ berths',
            '16-20 metres (accommodate mega vessels)',
            '20-30M TEU (Phases 1-2)',
            '65M TEU (fully completed)',
            '200+ super-post-Panamax cranes',
            'Hundreds of ARMG',
            '1,000+ battery-electric AGVs',
            'S$20+ billion'
        ],
        'Comparison': [
            'Equivalent to ~2,000 football fields',
            'Largest reclamation project in Singapore',
            'Longest continuous quay wall globally',
            'More than entire Singapore currently has',
            'Deepest in region',
            'More than many countries\' total throughput',
            'Nearly 2x current Singapore throughput',
            'Most advanced crane fleet worldwide',
            'Fully automated yard operations',
            'Largest AGV fleet globally',
            'Singapore\'s largest infrastructure project'
        ]
    })
    
    st.dataframe(tuas_specs, width='stretch', hide_index=True)
    
    st.markdown('<p class="subsection-header">Phased Development Approach</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Why Phased?**
    - Spread investment over time (manage cash flow)
    - Learn from each phase (continuous improvement)
    - Flexibility to adjust to demand (if growth slower/faster than expected)
    - Gradual transition from existing terminals (minimise disruption)
    
    **Development Phases:**
    """)
    
    # Phases timeline
    phases_timeline = pd.DataFrame({
        'Phase': ['Phase 1', 'Phase 2A', 'Phase 2B', 'Phase 3', 'Phase 4'],
        'Timeline': ['2021-2027', '2027-2032', '2032-2037', '2037-2040', '2040+'],
        'Capacity Added (M TEU)': [8, 12, 15, 15, 15],
        'Key Features': [
            'First automated terminal, foundation infrastructure, pilot operations',
            'Scale up automation, additional berths, expand yard',
            'Continue expansion, refine operations, full automation',
            'Near completion, maximise productivity',
            'Final capacity, potential future expansion'
        ],
        'Status': [
            'Under construction',
            'Planning/early works',
            'Planned',
            'Planned',
            'Planned'
        ]
    })
    
    st.dataframe(phases_timeline, width='stretch', hide_index=True)
    
    # Capacity growth visualization
    years = [2020, 2027, 2032, 2037, 2040, 2050]
    capacity = [37, 45, 57, 72, 65, 65]  # Note: 2037-2040 adjustment for ultimate 65M
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=years,
        y=capacity,
        mode='lines+markers',
        line=dict(color='#3B82F6', width=4),
        marker=dict(size=14, color='#2563EB', line=dict(color='white', width=2)),
        fill='tozeroy',
        fillcolor='rgba(59, 130, 246, 0.2)',
        name='Capacity',
        text=[f"{val}M TEU" for val in capacity],
        textposition='top center'
    ))
    
    fig.update_layout(
        title={
            'text': 'Singapore Port Capacity Growth: Current → Tuas Fully Operational',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        xaxis_title="Year",
        yaxis_title="Annual Capacity (Million TEU)",
        height=450,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='#E5E7EB', range=[0, 80]),
        xaxis=dict(gridcolor='#E5E7EB')
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown('<p class="subsection-header">Technology and Automation</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Quay-Side Operations:**
        - **Next-gen quay cranes**: 65-80m outreach, fully electric
        - **Automated landing**: Spreaders auto-position on containers
        - **Remote monitoring**: Centralised control room
        - **Predictive maintenance**: IoT sensors monitor health
        - **Triple hoist**: Maximum productivity
        
        **Horizontal Transport:**
        - **1,000+ AGVs**: Largest fleet globally
        - **Battery-electric**: Zero emissions, fast charging
        - **Dynamic routing**: AI optimises paths in real-time
        - **Collision avoidance**: Sensors prevent accidents
        - **24/7 operations**: No breaks, consistent performance
        """)
    
    with col2:
        st.markdown("""
        **Yard Operations:**
        - **Fully automated ARMG**: No operators in yard
        - **10+ tier stacking**: Higher density than manual
        - **Computer-optimised**: Minimise re-handles
        - **Remote monitoring**: Central control
        - **Predictive algorithms**: Optimal container placement
        
        **IT Systems:**
        - **Advanced CITOS**: Next-generation TOS
        - **Operational simulation**: Virtual simulation capability
        - **AI and ML**: Continuous optimisation
        - **Real-time visibility**: Track every container
        - **Integrated with digitalOCEANS**: Platform connectivity
        """)
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 The Automation Payoff:</strong><br><br>
    <strong>Productivity Gains:</strong><br>
    - 30-40% higher crane productivity than conventional terminals<br>
    - 24/7 consistent operations (no human fatigue)<br>
    - 50% reduction in vessel turnaround time potential<br>
    - 70-80% reduction in labour requirements<br><br>
    <strong>Cost Savings:</strong><br>
    - Lower long-term operating costs despite higher upfront capital<br>
    - Payback period: 10-15 years<br>
    - Competitive pricing capability (low marginal costs)<br><br>
    <strong>Quality and Safety:</strong><br>
    - Higher consistency (no human variability)<br>
    - Fewer accidents (no humans in operations areas)<br>
    - Better equipment utilisation (optimised by AI)
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 3: Implementation Challenges
    # ============================================================================
    
    st.markdown('<p class="section-header">Implementation Challenges: Not Easy</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Building and operating Tuas Mega Port presents significant challenges that Singapore must navigate.
    """)
    
    st.markdown('<p class="subsection-header">1. Labour Transition and Workforce Impact</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Challenge:**
    - Automation eliminates 70-80% of traditional port jobs
    - Thousands of workers affected: crane operators, prime mover drivers, yard crane operators
    - Social and political sensitivity in employment-focused society
    
    **Singapore\'s Approach:**
    
    **Retraining Programmes:**
    - **SkillsFuture**: Government-funded reskilling initiatives
    - **Technical training**: Teach workers to maintain and monitor automated systems
    - **Career transition support**: Help workers move to other industries
    - **Early retirement packages**: For workers near retirement age
    
    **New Job Creation:**
    - **Technology roles**: IT specialists, data analysts, automation engineers
    - **Maintenance technicians**: Service AGVs, cranes, automated systems
    - **Remote operators**: Monitor and control equipment from central facility
    - **Planning and optimisation**: Advanced roles requiring higher skills
    
    **Gradual Transition:**
    - **Phased automation**: Not overnight, spreads over 20 years
    - **Natural attrition**: Retirement and voluntary departures reduce need for redundancies
    - **Parallel operations**: Existing terminals continue whilst Tuas ramps up
    
    **Remaining Challenge:**
    - Not all workers can be retrained (age, aptitude, willingness)
    - Some job displacement inevitable
    - Requires continued government support and social safety net
    """)
    
    st.markdown('<p class="subsection-header">2. Foreign Worker Dependency</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Current Situation:**
    - Singapore\'s port operations rely significantly on foreign workers
    - Lower-skilled positions filled by workers from Malaysia, Bangladesh, India, China
    - Automation reduces need for foreign workers
    
    **Implications:**
    
    **Positive:**
    - Reduced dependency on foreign labour (strategic advantage)
    - Less vulnerable to labour supply disruptions
    - Lower social integration challenges
    
    **Concerns:**
    - May affect bilateral relationships (fewer job opportunities for neighbours)
    - Reduced wage remittances to source countries
    - Singapore\'s reputation as employment destination
    
    **Policy Balance:**
    - Singapore must manage transition diplomatically
    - Maintain good relationships with labour source countries
    - Position automation as inevitable global trend, not targeting specific groups
    """)
    
    st.markdown('<p class="subsection-header">3. Transportation and Hinterland Connectivity</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Challenge:**
    - Tuas is in **western Singapore**, far from city centre
    - Current port facilities more centrally located
    - Moving port west creates transportation challenges
    
    **Infrastructure Requirements:**
    
    **Road Connections:**
    - **Tuas Second Link**: Bridge to Malaysia (already exists)
    - **Upgraded highways**: Handle truck traffic to/from port
    - **Congestion management**: Prevent bottlenecks
    
    **Rail Connections:**
    - **Port rail connection**: Direct rail link for containers
    - **Integrated logistics**: Seamless truck-rail transfer
    - **Future MRT extension**: Public transport for workers
    
    **Last-Mile Logistics:**
    - **Inland distribution centres**: Staging areas closer to customers
    - **Truck appointment system**: Spread demand, avoid congestion
    - **Off-peak incentives**: Encourage night/weekend pickups
    
    **Investment Required:**
    - S$5-10 billion in supporting transportation infrastructure
    - Coordinated planning across agencies
    - Multi-year implementation timeline
    """)
    
    st.markdown('<p class="subsection-header">4. Security and Cybersecurity</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Physical Security:**
    - Large perimeter to secure (26+ km quay, 1,337 hectares)
    - Automated systems require robust physical protection
    - Critical infrastructure protection standards
    
    **Cybersecurity Risks:**
    - **High dependency on IT systems**: Entire port controlled by computers
    - **Single point of failure**: Cyber attack could cripple operations
    - **Nation-state threats**: Strategic target for adversaries
    - **Ransomware**: Criminal attacks seeking financial gain
    
    **Singapore\'s Response:**
    
    **Multi-Layer Security:**
    - **Perimeter security**: Fencing, cameras, sensors, patrols
    - **Access control**: Biometric authentication, restricted zones
    - **ISPS compliance**: International Ship and Port Facility Security Code
    
    **Cybersecurity Measures:**
    - **Air-gapped systems**: Critical systems isolated from internet
    - **Redundancy**: Backup systems and manual override capabilities
    - **24/7 monitoring**: Security Operations Centre (SOC)
    - **Penetration testing**: Regular security audits
    - **Incident response**: Prepared plans for cyber attacks
    - **International cooperation**: Share threat intelligence
    
    **Ongoing Challenge:**
    - Cyber threats constantly evolving
    - Requires continuous investment and vigilance
    - Balance security with operational efficiency
    """)
    
    # ============================================================================
    # SECTION 4: Will It Be Enough? Critical Analysis
    # ============================================================================
    
    st.markdown('<p class="section-header">Critical Question: Will 65M TEU Be Enough?</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The ultimate question: Is Singapore making the right bet with Tuas? Will 65M TEU capacity be 
    sufficient, or could it be too much—or too little?
    """)
    
    st.markdown('<p class="subsection-header">Arguments FOR: Tuas Will Be Sufficient</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **1. Demand Growth Supports Expansion**
    - **Global trade growth**: 3-4% annually (historical average)
    - **Asian trade growth**: 4-5% annually (faster than global)
    - **Singapore\'s transshipment role**: 85% transshipment, taps into regional flows
    - **Current utilisation**: 37M TEU, approaching capacity limits
    - **By 2040**: 65M TEU capacity matches projected demand
    
    **2. Competitive Position Locked In**
    - **Scale advantage**: 65M TEU capacity much larger than any regional competitor
    - **Technology lead**: Most automated, efficient port in Southeast Asia
    - **Alliance commitments**: Long-term contracts with 2M, Ocean Alliance, THE Alliance
    - **Network effects**: Connectivity and reliability attract more shipping lines
    - **First-mover advantage**: Built before competitors can catch up
    
    **3. Flexibility Built In**
    - **Phased development**: Can slow or accelerate based on actual demand
    - **Marginal cost low**: Operating cost per TEU decreases with volume
    - **Strategic buffer**: Excess capacity allows competitive pricing
    - **Adaptability**: Infrastructure can be repurposed if needed
    
    **4. Irreplaceable Strategic Location**
    - **On main Asia-Europe route**: 33% of global trade passes through
    - **Centre of Southeast Asia**: Ideal hub for regional distribution
    - **Deep natural harbour**: Expensive for competitors to replicate
    - **Political stability**: Singapore\'s governance is unique competitive advantage
    """)
    
    st.markdown('<p class="subsection-header">Arguments AGAINST: Tuas May Not Be Enough (or Too Much)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **1. Demand Uncertainty**
    - **Slower growth**: Global trade growth slowing (2-3% vs historical 4-5%)
    - **Structural changes**: Nearshoring, regionalisation reduce long-haul shipping
    - **E-commerce**: Smaller shipments, more direct routes (less transshipment)
    - **Manufacturing shifts**: China+1 diversification changes traditional patterns
    - **What if demand only reaches 50M TEU by 2040?** → Overcapacity, stranded assets
    
    **2. Competitive Threats Real and Growing**
    - **Malaysia**: Carey Island, Melaka Gateway (lower costs, strategic location)
    - **Indonesia**: Massive domestic market (400M people), Tanjung Priok expansion
    - **Vietnam**: Rapid economic growth, port infrastructure investments
    - **Thailand Kra Canal**: Low probability but catastrophic if built (bypasses Singapore)
    - **What if competitors capture 20-30% of Singapore\'s transshipment volumes?** → Tuas underutilised
    
    **3. Technology Disruption**
    - **Autonomous vessels**: May prefer direct routes over hub-and-spoke (reduces transshipment)
    - **Blockchain and smart contracts**: Enable more efficient direct shipping
    - **Arctic routes**: Climate change opens shorter routes bypassing traditional lanes
    - **What if hub-and-spoke model becomes obsolete?** → Tuas capacity not needed
    
    **4. Geopolitical Risks**
    - **US-China decoupling**: Trade fragmentation reduces volumes on major routes
    - **Regional conflicts**: Disruption to Malacca Strait traffic
    - **Economic nationalism**: Countries favour own ports over neutral hubs
    - **What if geopolitical tensions reduce Singapore\'s neutral hub status?** → Volume loss
    
    **5. Environmental Regulations**
    - **Carbon pricing**: Makes shipping more expensive, could reduce trade volumes
    - **Slow steaming**: Reduced speed to save fuel = more vessels needed but less throughput per vessel
    - **What if environmental costs make long-distance trade uneconomical?** → Less transshipment demand
    """)
    
    # Scenario analysis
    st.markdown('<p class="subsection-header">Scenario Analysis: 2040 Outcomes</p>', unsafe_allow_html=True)
    
    scenarios = pd.DataFrame({
        'Scenario': [
            'Optimistic',
            'Base Case',
            'Conservative',
            'Pessimistic'
        ],
        'Probability': ['20%', '50%', '25%', '5%'],
        'Singapore 2040 Throughput': ['70M TEU', '55-60M TEU', '45-50M TEU', '35-40M TEU'],
        'Tuas Utilisation': ['107% (need expansion)', '85-92%', '69-77%', '54-62%'],
        'Outcome Assessment': [
            'Tuas insufficient, need Phase 5',
            'Tuas appropriate, well-utilised',
            'Tuas has excess capacity, lower ROI',
            'Tuas significantly underutilised, stranded assets'
        ],
        'Key Assumptions': [
            'Strong global trade, Singapore maintains share, technology helps efficiency',
            'Moderate trade growth, modest competition, stable market share',
            'Slow trade growth, increased competition, some volume loss',
            'Trade stagnation/decline, major competitive losses, technology disruption'
        ]
    })
    
    st.dataframe(scenarios, width='stretch', hide_index=True)
    
    # Scenario probability visualization
    fig = go.Figure(data=[go.Pie(
        labels=scenarios['Scenario'],
        values=[20, 50, 25, 5],
        marker=dict(colors=['#10B981', '#3B82F6', '#F59E0B', '#EF4444']),
        textinfo='label+percent',
        textfont=dict(size=14, color='white'),
        hole=0.4
    )])
    
    fig.update_layout(
        title={
            'text': 'Scenario Probability Distribution (Expert Assessment)',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        annotations=[dict(text='2040<br>Outlook', x=0.5, y=0.5, font_size=16, showarrow=False)],
        height=450
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ The Real Risk:</strong><br><br>
    The greatest risk is not that Tuas will be <strong>too small</strong> or <strong>too large</strong>, but that Singapore might be 
    optimising for the <strong>wrong future</strong>:<br><br>
    <strong>If the hub-and-spoke transshipment model declines:</strong><br>
    - Shipping lines increasingly prefer direct routes (autonomous vessels, point-to-point efficiency)<br>
    - Regional ports capture origin/destination cargo (less need for transshipment hubs)<br>
    - Trade patterns fragment (regionalisation, nearshoring)<br><br>
    <strong>Then:</strong><br>
    - Transshipment volumes globally decline<br>
    - Singapore\'s 85% transshipment model becomes vulnerability<br>
    - Massive Tuas capacity underutilised<br>
    - S$20B+ investment yields poor returns<br><br>
    <strong>However:</strong><br>
    - Singapore\'s government has 70+ years of strategic planning success<br>
    - Phased approach provides flexibility to adapt<br>
    - Technology and efficiency provide hedge against competition<br>
    - Even if transshipment share drops, absolute volumes may still grow<br>
    - Diversification into maritime services (finance, tech, bunkering) reduces dependency on port volumes alone
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">The Verdict: Calculated Risk, Not Reckless Bet</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Balanced Assessment:**
    
    **Tuas is likely to be "about right" under most plausible scenarios:**
    
    **Why the bet makes sense:**
    1. **Base case (50% probability)**: 55-60M TEU by 2040 → Tuas 85-92% utilised ✅
    2. **Downside protected**: Even conservative scenario (45-50M TEU) → 69-77% utilised (acceptable)
    3. **Upside captured**: Optimistic scenario → Can build Phase 5 if needed
    4. **Competitive moat**: Scale and technology make it very hard for competitors to displace Singapore
    5. **Flexibility**: Phased approach allows adjustments based on actual demand
    6. **Strategic buffer**: Better to have capacity and not need it than need it and not have it
    
    **The risks are real but manageable:**
    - Technology disruption: Possible but uncertain timing and magnitude
    - Competition: Serious but Singapore has structural advantages
    - Geopolitics: Could shift patterns but Singapore\'s neutrality is valuable
    - Demand: May grow slower than hoped but unlikely to decline absolutely
    
    **What would make Tuas a mistake:**
    - Catastrophic scenario (<5% probability): Major geopolitical shift, technology disruption, competitive collapse
    - Even then, infrastructure has long life and can be adapted
    
    **Conclusion:**
    Tuas represents a **calculated strategic bet** by Singapore to maintain its position as the world\'s 
    premier transshipment hub. The investment is massive, the risks are real, but the analysis suggests 
    it\'s more likely to be **"about right"** than wildly over or under capacity. Singapore is essentially 
    buying insurance against being displaced by competitors whilst positioning for continued growth.
    
    **The real genius:** Phased development provides flexibility to adjust course if reality diverges from 
    projections. This is strategic planning at its finest—bold vision combined with pragmatic adaptability.
    """)
    
    # ============================================================================
    # SECTION 5: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Why Tuas:**
        - **Consolidation**: Combine terminals for 20-30% efficiency gain
        - **Mega vessels**: Purpose-built for 24,000+ TEU ULCV
        - **Competition**: Pre-emptive response to regional threats
        - **Technology**: Greenfield enables full automation
        - **Sustainability**: Built +5m for sea level rise, zero emissions
        
        **Design Features:**
        - **Scale**: 65M TEU, 26+ km quay, 1,337 hectares
        - **Investment**: S$20B+ over multiple phases
        - **Automation**: 1,000+ AGVs, ARMG, advanced CITOS
        - **Green**: Solar, electric equipment, shore power
        - **Phased**: 2021-2040+ rollout provides flexibility
        
        **Implementation Challenges:**
        - **Labour**: 70-80% reduction, retraining programmes
        - **Foreign workers**: Reduced dependency, diplomatic implications
        - **Transport**: Hinterland connectivity infrastructure
        - **Security**: Physical and cybersecurity protection
        """)
    
    with col2:
        st.markdown("""
        **Will It Be Enough? Scenario Analysis:**
        
        **Optimistic (20%)**: 70M TEU → Need Phase 5 expansion
        
        **Base Case (50%)**: 55-60M TEU → Tuas well-utilised ✅
        
        **Conservative (25%)**: 45-50M TEU → Excess capacity but acceptable
        
        **Pessimistic (5%)**: <45M TEU → Significant underutilisation
        
        **Key Uncertainties:**
        - Trade growth rates (2-5% annually?)
        - Competitive displacement (0-30% volume loss?)
        - Technology disruption (hub-spoke vs direct?)
        - Geopolitical shifts (trade fragmentation?)
        
        **Strategic Assessment:**
        - **Calculated risk**, not reckless bet
        - Phased approach provides flexibility
        - Most likely outcome: "about right"
        - Downside protected, upside captured
        - Better to build and adjust than fall behind
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Tuas Mega Port is Singapore\'s S$20B+ bet to maintain its position as 
    the world\'s premier transshipment hub. The five strategic drivers (consolidation, mega vessels, 
    competition, technology, climate resilience) justify the investment. At 65M TEU capacity by 2040, Tuas 
    is likely to be well-utilised under most plausible scenarios (base case: 55-60M TEU = 85-92% utilisation). 
    The phased approach (2021-2040+) provides flexibility to adjust if reality diverges from projections. 
    Key challenges include labour transition (70-80% reduction, retraining programmes), transportation 
    infrastructure, and cybersecurity. The real risk is not that Tuas will be too large or too small, but 
    that the hub-and-spoke transshipment model itself could be disrupted by technology or trade pattern 
    changes. However, Singapore\'s strategic planning track record, structural advantages (location, 
    stability, ecosystem), and adaptive approach make Tuas a **calculated strategic bet** more likely to 
    succeed than fail. The investment buys insurance against competitive displacement whilst positioning 
    for continued growth—strategic planning at its finest.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Conclusion
    # ============================================================================
    
    st.markdown("---")
    st.markdown('<p class="section-header">🎓 Course Conclusion</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Congratulations!** You\'ve completed the comprehensive Maritime 101 educational journey.
    
    **What You\'ve Learned:**
    
    1. **Maritime Industry Foundation**: Why shipping matters, containerisation revolution, three waves of change
    2. **Containers & Containerisation**: ISO standards, TEU measurement, specialised types
    3. **Vessels & Evolution**: 500 TEU → 25,000 TEU, classifications, stowage principles
    4. **Global Shipping & Alliances**: Consolidation to 3 alliances (83% control), hub-spoke networks
    5. **Maritime Singapore Ecosystem**: MPA\'s dual role, complete maritime cluster, innovation
    6. **Port Competition**: Critical success factors, gateway vs transshipment, green ports
    7. **Operations Management**: Big Six competencies, FMEA, capacity planning, trade-offs
    8. **Terminal Operations**: Berth planning, yard operations, stowage, equipment coordination
    9. **Equipment & Automation**: QC/YC/AGVs, automation levels, CITOS system
    10. **Green Maritime**: Decarbonisation (IMO 2050), alternative fuels, digital transformation
    11. **Tuas Mega Port**: S$20B investment, 65M TEU capacity, strategic rationale and risks
    
    **You Now Understand:**
    - The physical maritime world your systems must model
    - Why ports make the decisions they do (competition, economics, technology)
    - How container terminal operations actually work end-to-end
    - The forces shaping the industry\'s future (decarbonisation, automation, geopolitics)
    
    **Next Steps:**
    - Apply this knowledge to build accurate operational models
    - Understand the operational context behind the data and systems
    - Recognise the strategic challenges ports face and how technology can help
    
    Thank you for your attention and engagement! 🚢📦🌍
    """)
