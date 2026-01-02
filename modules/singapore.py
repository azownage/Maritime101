import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.markdown('<p class="main-header">🇸🇬 Singapore & Tuas Port</p>', unsafe_allow_html=True)
    
    # Hero metrics
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("World Ranking", "#2", help="2nd busiest container port globally")
    with col2:
        st.metric("Annual Throughput", "37.3M TEU", help="2023 volume")
    with col3:
        st.metric("Transshipment Rate", "85%", help="Containers transshipped")
    with col4:
        st.metric("Vessel Calls/Year", "140,000+", help="Busiest by shipping tonnage")
    with col5:
        st.metric("Container Services", "230+", help="Active shipping services")
    
    st.markdown("---")
    st.markdown('<p class="section-header">Why Singapore Became a Global Hub</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        ### The Perfect Storm of Advantages
        
        Singapore didn't become the world's #2 container port by accident. 
        It's a carefully orchestrated combination of geography, government policy, and operational excellence.
        
        **1. Strategic Geographic Location**
        
        **The Strait of Malacca Advantage:**
        - Located at the **southern exit** of the Strait of Malacca
        - **33% of global seaborne trade** passes through this strait
        - Ships sailing between Asia and Europe/Middle East/Africa **must pass by Singapore**
        - "At the crossroads of East-West trade"
        
        **Regional Position:**
        - **Center of Southeast Asia**
        - Within 7-day sailing of major Asian economies:
          - China (3-4 days)
          - Indonesia (1-2 days)
          - Thailand (2 days)
          - Vietnam (2-3 days)
          - India (4-5 days)
        - Perfect **hub-and-spoke** location for regional distribution
        
        **2. Natural Deep-Water Harbor**
        
        - **Sheltered waters** protected from storms
        - **Natural depth** of 15-20+ meters (no major dredging needed initially)
        - Can handle **largest container ships** (24,000 TEU)
        - **Ice-free year-round** (tropical location)
        - **No seasonal closures** (unlike some northern ports)
        
        **3. Government Vision & Support**
        
        Singapore's government identified maritime as a strategic pillar since independence (1965).
        
        **Key Policy Decisions:**
        - **1972**: Committed to containerization early (ahead of many Asian ports)
        - **1980s**: Invested heavily in port automation and technology
        - **1990s**: Established Maritime and Port Authority (MPA) for coordination
        - **2000s**: Expanded Pasir Panjang Terminal aggressively
        - **2010s**: Announced Tuas Mega Port development
        
        **Long-term Thinking:**
        - Planning horizon: **20-30 years ahead**
        - Willing to invest billions before demand materializes
        - Stable, predictable policies
        - Pro-business environment
        
        **4. Operational Excellence (PSA)**
        
        **PSA (Port of Singapore Authority, later PSA International):**
        - One of the world's most efficient port operators
        - Pioneered **CITOS** (Container IT Operating System) in 1988
        - Continuous innovation in automation
        - Best-in-class productivity metrics
        
        **Performance Numbers:**
        - **BOA (Berth on Arrival)**: >90% (ships berth immediately, no waiting)
        - **GCR (Gross Crane Rate)**: 35+ moves/hour
        - **Vessel Turnaround**: 24-48 hours for mega-ships
        - **Tight connections**: Can transship container in <24 hours
        """)
    
    with col2:
        st.markdown('<div class="success-box">', unsafe_allow_html=True)
        st.markdown("""
        ### 🏆 Current Rankings & Awards
        
        **Global Rankings (2023):**
        - **#1** Logistics Hub (World Bank)
        - **#1** Busiest port (shipping tonnage)
        - **#2** Container volume (after Shanghai)
        - **#1** Transshipment hub globally
        
        **Awards:**
        - **Best Global Seaport**: 3rd time (2023)
        - **Best Seaport in Asia**: 35th time
        - **World's Best Airport**: 12th time (Changi)
        
        **Market Share:**
        - **4%** of global container throughput
        - **14%** of world's transshipment volume
        - **230+** shipping services call Singapore
        - Connected to **600+ ports** worldwide
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("""
        ### 📍 Singapore's Strategic Position
        
        **What Ships Pass Through:**
        
        - **All Asia-Europe trade** (via Malacca)
        - **All Middle East-Asia trade**
        - **Most Oceania-Europe trade**
        - **Intra-Asia regional trade**
        
        **The Math:**
        - 300+ ships/day through Strait of Malacca
        - If just 30% call Singapore → 90+ vessels/day
        - Actual: 140,000 calls/year = **380+ vessels/day**
        
        **Comparative Advantage:**
        
        Why ships choose Singapore over alternatives:
        - **Reliability**: 99.9% uptime, no strikes
        - **Speed**: Fastest turnaround in region
        - **Connectivity**: More services than anywhere
        - **Efficiency**: Lower costs per container
        - **Services**: Bunkering, repairs, supplies
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown('<p class="section-header">Singapore Port Historical Development</p>', unsafe_allow_html=True)
    
    # Create historical timeline
    milestones_data = pd.DataFrame({
        'Year': [1819, 1965, 1968, 1972, 1982, 1984, 1988, 1990, 1991, 1994, 1997, 
                2000, 2003, 2004, 2006, 2011, 2020, 2021, 2027, 2040],
        'Event': [
            'Founding of modern Singapore',
            'Independence from Malaysia',
            'First container berths planned',
            'First container ship (MV Nihon)',
            '1M TEU milestone',
            'PORTNET launched',
            'CITOS system implemented',
            '5M TEU - World busiest port',
            'Keppel Terminal opens',
            '10M TEU milestone',
            'PSA corporatized',
            'Pasir Panjang Terminal opens',
            'Cosco-PSA JV terminal',
            '20M TEU milestone',
            'Emma Maersk (15,550 TEU) calls',
            '29M TEU - 400M total',
            '36.6M TEU',
            'Tuas Port Phase 1 begins',
            'Tuas Phase 2 (projected)',
            'Tuas fully operational (65M TEU)'
        ],
        'Throughput_M_TEU': [0, 0, 0, 0.2, 1, 1.2, 3, 5, 6, 10, 14, 17, 18.4, 20, 24.8, 29, 36.6, 37, 50, 65],
        'Significance': [
            'British trading post established',
            'Nation building begins',
            'Tanjong Pagar Terminal construction',
            'Container era begins',
            'Rapid growth starts',
            'First digital port platform',
            'Automation revolution',
            'Global leadership achieved',
            'Expansion continues',
            'Double-digit growth',
            'Commercial operations',
            'Major expansion',
            'Strategic partnerships',
            'Doubling capacity',
            'Mega-ship era',
            'Sustained growth',
            'COVID resilience',
            'Next generation begins',
            'Transition period',
            'Ultimate capacity'
        ]
    })
    
    # Interactive timeline chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=milestones_data['Year'],
        y=milestones_data['Throughput_M_TEU'],
        mode='lines+markers',
        name='TEU Throughput',
        line=dict(color='#3B82F6', width=3),
        marker=dict(size=8, color='#3B82F6', line=dict(width=2, color='white')),
        text=milestones_data['Event'],
        customdata=milestones_data['Significance'],
        hovertemplate='<b>%{x}</b><br>%{text}<br>Throughput: %{y}M TEU<br>%{customdata}<extra></extra>'
    ))
    
    # Add milestone annotations for key events
    key_milestones = [
        (1972, 0.2, 'First Container Ship'),
        (1990, 5, 'World #1'),
        (2006, 24.8, 'Mega-Ship Era'),
        (2040, 65, 'Tuas Complete')
    ]
    
    for year, teu, label in key_milestones:
        fig.add_annotation(
            x=year, y=teu,
            text=label,
            showarrow=True,
            arrowhead=2,
            arrowcolor='#EF4444',
            font=dict(size=10, color='#1E293B'),
            bgcolor='#FEE2E2',
            bordercolor='#EF4444',
            borderwidth=2
        )
    
    fig.update_layout(
        title='Singapore Port Development Timeline (1819-2040)',
        xaxis_title='Year',
        yaxis_title='Annual Throughput (Million TEU)',
        height=400,
        hovermode='closest',
        plot_bgcolor='white',
        xaxis=dict(gridcolor='#E2E8F0'),
        yaxis=dict(gridcolor='#E2E8F0')
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed milestones table
    st.markdown("### Key Milestones in Singapore Port History")
    
    display_df = milestones_data[['Year', 'Event', 'Throughput_M_TEU', 'Significance']].copy()
    display_df.columns = ['Year', 'Milestone', 'TEU (Millions)', 'Significance']
    display_df['TEU (Millions)'] = display_df['TEU (Millions)'].apply(lambda x: f"{x:.1f}" if x > 0 else "-")
    
    st.dataframe(display_df, use_container_width=True, hide_index=True, height=350)
    
    st.markdown("---")
    st.markdown('<p class="section-header">Current Port Terminals</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore's current container operations are spread across **four main terminals**, all operated by PSA.
    These will eventually consolidate into Tuas Mega Port.
    """)
    
    terminals_data = pd.DataFrame({
        'Terminal': [
            'Tanjong Pagar Terminal (City Terminals)',
            'Keppel Terminal',
            'Brani Terminal',
            'Pasir Panjang Terminal (PPT)'
        ],
        'Year_Opened': ['1972', '1991', '1974', '2000'],
        'Berths': ['9', '9', '10', '26'],
        'Total_Berth_Length': ['2,700m', '2,500m', '3,000m', '8,200m'],
        'Max_Depth': ['15m', '16m', '15m', '18m'],
        'Annual_Capacity': ['~5M TEU', '~5M TEU', '~6M TEU', '~35M TEU'],
        'Status': [
            'Operating (closing 2027)',
            'Operating (closing 2025)',
            'Operating (closing 2027)',
            'Operating (closing 2040)'
        ],
        'Key_Features': [
            'Original container terminal, city location',
            'Added capacity in 1990s',
            'Multi-purpose, general cargo',
            'Largest terminal, multiple phases, automated cranes'
        ]
    })
    
    st.dataframe(terminals_data, use_container_width=True, hide_index=True, height=250)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Why Consolidate to Tuas?
        
        **Current Problems:**
        
        **1. Land Constraints:**
        - City terminals occupy **prime waterfront land**
        - Tanjong Pagar, Keppel in downtown area
        - Land worth billions for redevelopment
        - Housing, commercial, recreation potential
        
        **2. Operational Inefficiency:**
        - **4 separate terminals** with different operators
        - **Inter-terminal haulage** needed to transfer containers
        - Trucks moving containers between terminals
        - Adds cost, time, congestion
        - Extra handling = higher breakage risk
        
        **3. Expansion Limitations:**
        - City terminals **cannot expand**
        - Surrounded by urban development
        - No room for bigger cranes, deeper berths
        - Cannot accommodate future mega-ships
        
        **4. Manpower Challenges:**
        - Singapore has **limited workforce**
        - Aging population
        - High labor costs
        - Need automation to stay competitive
        
        **Tuas Solution:**
        - **One consolidated location**
        - Built from scratch with latest technology
        - Room for expansion
        - Fully automated design
        - Free up valuable city land
        """)
    
    with col2:
        st.markdown("""
        ### Pasir Panjang Terminal (PPT)
        
        **Singapore's Current Workhorse**
        
        Pasir Panjang Terminal is the largest and most modern of the existing terminals.
        
        **Development Phases:**
        
        **Phase 1-2 (2000-2005):**
        - 7 berths
        - Conventional operations
        
        **Phase 3-4 (2008-2017):**
        - 15 berths  
        - 6km quay length
        - **Automated RMG cranes**
        - First automated terminal in Singapore
        - $3.5 billion investment
        
        **Phase 5 (Currently Operating):**
        - Additional capacity
        - Latest automation
        
        **Key Features:**
        - **Depth**: 18m (handles mega-ships)
        - **Berths**: 26 total
        - **Equipment**: Mix of manual and automated
        - **Partnerships**:
          - MSC-PSA Terminal (joint venture)
          - Cosco-PSA Terminal
          - PIL-PSA Terminal
        
        **Will Be Last to Close:**
        - Most modern terminal
        - Latest technology
        - Will operate until Tuas Phase 4 (2040)
        - Gradual migration to Tuas
        """)
    
    st.markdown("---")
    st.markdown('<p class="section-header">Tuas Mega Port - The Next Generation</p>', unsafe_allow_html=True)
    
    st.markdown("""
    ## The World's Largest Automated Container Terminal Project
    
    Announced in **October 2012**, Tuas Mega Port represents Singapore's vision for the future of container handling.
    It's not just a port - it's a complete reimagining of how ports should work.
    """)
    
    col1, col2 = st.columns([2, 3])
    
    with col1:
        st.markdown('<div class="success-box">', unsafe_allow_html=True)
        st.markdown("""
        ### 📊 Tuas By The Numbers
        
        **Ultimate Capacity (2040):**
        - **65 million TEU/year**
        - **66 berths**
        - **26.3 km of wharf** (continuous)
        - **23 meters depth** (deepest in region)
        - **1,337 hectares of land**
        
        **Scale Comparison:**
        - 1.75x current Singapore capacity
        - Larger than Los Angeles + Long Beach combined
        - Could handle all US West Coast trade
        - Equivalent to 10 average-sized ports
        
        **Development:**
        - **4 phases** (2021-2040)
        - **20-year construction**
        - Estimated **$20 billion** investment
        - World's largest port project
        
        **Technology:**
        - **Fully automated** operations
        - **Automated Guided Vehicles (AGVs)**
        - **Electrified quay cranes**
        - **Automated RMG yard cranes**
        - **AI-based planning systems**
        - **Digital twin** of entire port
        - **5G connectivity**
        - **Zero-emission goal**
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Create phase timeline
        phases_data = pd.DataFrame({
            'Phase': ['Phase 1', 'Phase 2', 'Phase 3', 'Phase 4'],
            'Timeline': ['2021-2027', '2027-2032', '2032-2037', '2037-2040'],
            'Berths': [21, 15, 15, 15],
            'Capacity_M_TEU': [20, 15, 15, 15],
            'Cumulative_TEU': [20, 35, 50, 65],
            'Status': ['Under Construction', 'Planned', 'Planned', 'Planned'],
            'Key_Features': [
                'First automated terminals, deep water berths',
                'Expansion of automation, more AGVs',
                'Advanced AI systems, full integration',
                'Final capacity, complete consolidation'
            ]
        })
        
        fig_phases = go.Figure()
        
        fig_phases.add_trace(go.Bar(
            x=phases_data['Phase'],
            y=phases_data['Capacity_M_TEU'],
            name='Additional Capacity',
            marker_color='#3B82F6',
            text=phases_data['Capacity_M_TEU'].apply(lambda x: f'{x}M TEU'),
            textposition='inside',
            textfont=dict(color='white', size=12)
        ))
        
        fig_phases.add_trace(go.Scatter(
            x=phases_data['Phase'],
            y=phases_data['Cumulative_TEU'],
            name='Cumulative Capacity',
            mode='lines+markers+text',
            line=dict(color='#EF4444', width=3),
            marker=dict(size=12, color='#EF4444'),
            text=phases_data['Cumulative_TEU'].apply(lambda x: f'{x}M'),
            textposition='top center',
            yaxis='y2'
        ))
        
        fig_phases.update_layout(
            title='Tuas Port Development Phases (2021-2040)',
            xaxis_title='Development Phase',
            yaxis=dict(title='Added Capacity (M TEU)', side='left'),
            yaxis2=dict(title='Total Capacity (M TEU)', side='right', overlaying='y'),
            height=400,
            legend=dict(x=0.01, y=0.99),
            hovermode='x unified'
        )
        
        st.plotly_chart(fig_phases, use_container_width=True)
        
        st.markdown("### Development Phases Detail")
        st.dataframe(phases_data[['Phase', 'Timeline', 'Berths', 'Capacity_M_TEU', 'Status']], 
                    use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown('<p class="subsection-header">Why Tuas? Location Advantages</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🌊 Natural Advantages
        
        **Deep Sheltered Waters:**
        - Natural depth: 20-23 meters
        - Protected from waves/storms
        - Can handle **22,000+ TEU** vessels
        - **26 containers across** vessel width
        - No major dredging needed
        
        **Strategic Position:**
        - West of Singapore
        - **Directly on** shipping lanes
        - Ships enter from west (from Malacca)
        - Natural first stop
        - Closer to Malaysia/Indonesia
        
        **Room to Grow:**
        - 1,337 hectares available
        - Can expand if needed
        - Not constrained by city
        - Flexible layout design
        """)
    
    with col2:
        st.markdown("""
        ### 🏗️ Infrastructure Benefits
        
        **Proximity to Jurong:**
        - Singapore's **industrial heartland**
        - Petrochemical complexes
        - Manufacturing zones
        - Jurong Port (multi-purpose)
        - Logistics providers nearby
        
        **Integrated Ecosystem:**
        - **Warehouse zones** adjacent
        - **Bonded facilities**
        - **Container depots**
        - **Freight forwarders**
        - **Value-added services**
        - Complete **supply chain hub**
        
        **Land Connection:**
        - Direct highway access
        - Rail connectivity planned
        - Minimize truck congestion
        - Efficient cargo distribution
        """)
    
    with col3:
        st.markdown("""
        ### 💡 Operational Benefits
        
        **Single Mega Terminal:**
        - **No inter-terminal haulage**
        - All berths connected
        - Unified operations
        - Economies of scale
        - Simpler planning
        
        **Greenfield Development:**
        - **Design from scratch**
        - Incorporate latest technology
        - Optimal layout
        - No legacy constraints
        - Future-proof design
        
        **Automation Possibilities:**
        - Built for full automation
        - Level ground (easier for AGVs)
        - Integrated power grid
        - Fiber optic network
        - Smart infrastructure
        """)
    
    st.markdown("---")
    st.markdown('<p class="subsection-header">Tuas Technology & Innovation</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Tuas isn't just bigger - it's **smarter, greener, and more automated**.
    Singapore is using this opportunity to leapfrog into the next generation of port technology.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🤖 Full Automation
        
        **Automated Equipment:**
        
        **1. Automated Quay Cranes (Ship-to-Shore)**
        - **Electrified** (not diesel)
        - **Remote controlled** from control room
        - Can operate **24/7** without fatigue
        - Precise container handling
        - Faster than manual (38+ moves/hour target)
        
        **2. Automated Guided Vehicles (AGVs)**
        - **Battery-electric** vehicles
        - Follow magnetic markers or GPS
        - Transport containers from quay to yard
        - No human drivers needed
        - Optimal route planning by AI
        - Wireless charging stations
        
        **3. Automated Rail-Mounted Gantry (RMG) Cranes**
        - Stack containers in yard
        - Fully automated picking/placing
        - Controlled by central system
        - Can stack 6+ containers high
        - Precise to 1cm accuracy
        
        **Benefits of Automation:**
        - ✅ **24/7 operations** (no shifts, breaks, holidays)
        - ✅ **Consistency** (no human error)
        - ✅ **Safety** (fewer accidents)
        - ✅ **Speed** (faster operations)
        - ✅ **Manpower efficiency** (limited workforce)
        - ✅ **Cost reduction** (lower long-term costs)
        
        **Workforce Transformation:**
        - Fewer manual workers
        - More **engineers and technicians**
        - **Equipment maintenance** specialists
        - **Data analysts and planners**
        - **Control room operators**
        - Higher-skilled, better-paid jobs
        """)
        
        st.markdown("""
        ### 📊 AI & Data Analytics
        
        **CITOS Next Generation:**
        - PSA's proprietary Terminal Operating System
        - **AI-powered** planning and optimization
        - Real-time decision making
        - Predictive analytics
        
        **Capabilities:**
        - **Vessel stow planning**: Optimal container placement
        - **Yard planning**: Minimize reshuffles
        - **Equipment allocation**: Assign cranes/AGVs efficiently
        - **Berthing optimization**: Which ship, which berth, when
        - **Tight connections**: Transship in <24 hours
        - **Predictive maintenance**: Fix before it breaks
        
        **Digital Twin:**
        - **Virtual replica** of entire port
        - Simulate operations before execution
        - Test different scenarios
        - Optimize before deploying
        - Continuous improvement
        """)
    
    with col2:
        st.markdown("""
        ### 🌱 Sustainability & Green Technology
        
        **Carbon Reduction Goals:**
        - **Net-zero emissions** by 2050
        - Intermediate targets: 40% by 2030
        - All-electric equipment
        - Renewable energy sources
        
        **Green Initiatives:**
        
        **1. Electrification**
        - All quay cranes: **electric powered**
        - All AGVs: **battery-electric**
        - All yard equipment: electric where possible
        - No diesel equipment in terminal
        
        **2. Renewable Energy**
        - **Solar panels** on buildings, canopies
        - Largest solar installation in Singapore
        - Generates **~40 MW** of power
        - Covers ~20% of energy needs
        
        **3. Energy Efficiency**
        - LED lighting throughout
        - Smart grid management
        - Energy recovery systems
        - Optimized equipment usage
        
        **4. Sustainable Construction**
        - **Waste circularity**: Recycle construction waste
        - Sustainable materials
        - Minimize environmental impact
        - Built **5m above sea level** (climate resilience)
        
        **5. Shore Power (Cold Ironing)**
        - Ships plug into port power grid
        - Turn off ship engines while berthed
        - Reduces emissions in port
        - Cleaner air quality
        
        **6. Smart Water Management**
        - Rainwater harvesting
        - Water recycling systems
        - Minimize freshwater use
        
        **Environmental Impact:**
        - **50% less emissions** than conventional port
        - Cleaner air for nearby communities
        - Quieter operations (electric equipment)
        - Wildlife-friendly design (green corridors)
        """)
        
        st.markdown("""
        ### 🔒 Safety & Security
        
        **Cybersecurity:**
        - Critical infrastructure protection
        - Multi-layered security
        - Real-time threat monitoring
        - Backup systems
        
        **Physical Security:**
        - Perimeter fencing and sensors
        - CCTV surveillance (AI-powered)
        - Access control systems
        - Drone detection
        
        **Worker Safety:**
        - Automated equipment = fewer accidents
        - Segregated zones (human/automated)
        - Emergency stop systems
        - Safety training programs
        """)
    
    st.markdown("---")
    st.markdown('<p class="subsection-header">Challenges & Competition</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### ⚠️ Challenges Facing Tuas
        
        **1. Regional Competition**
        
        Other countries are also building mega-ports:
        
        **Malaysia:**
        - **Port Klang**: Expanding capacity
        - **Carey Island**: New deep-water terminal
        - **Melaka Gateway**: $10B mega-port project
        - Geographic advantage: closer to Malacca
        - Lower costs than Singapore
        
        **Indonesia:**
        - **Tanjung Priok** (Jakarta): Massive expansion
        - **New Priok Terminal**: Automated systems
        - Domestic market huge (280M people)
        - Growing manufacturing base
        
        **Thailand:**
        - **Laem Chabang**: Major expansion
        - **Kra Canal** proposal (long-term threat)
        - Would bypass Malacca entirely!
        
        **2. Changing Trade Routes**
        
        **Belt & Road Initiative (China):**
        - Rail corridors: China → Europe overland
        - Bypass maritime routes
        - Singapore ↔ Chongqing rail link
        - Faster than sea, cheaper than air
        
        **Northern Sea Route (Arctic):**
        - Climate change opening new passage
        - Asia → Europe via Arctic Ocean
        - 30% shorter than Suez route
        - Bypasses Singapore entirely
        - Currently seasonal (July-October)
        - Could become year-round by 2050
        
        **3. Geopolitical Risks**
        
        **US-China Tensions:**
        - Trade war impacts volumes
        - Supply chain rerouting
        - Nearshoring reduces long-haul shipping
        
        **Regional Conflicts:**
        - South China Sea disputes
        - Taiwan tensions
        - Could disrupt shipping lanes
        
        **4. Technology Disruption**
        
        **Automation Race:**
        - Other ports also automating
        - First-mover advantage fading
        - Need continuous innovation
        
        **Digital Competition:**
        - Blockchain for documentation
        - Need to stay ahead in tech
        """)
    
    with col2:
        st.markdown("""
        ### 💪 Singapore's Competitive Advantages
        
        **How Singapore Stays Ahead:**
        
        **1. Location Still Matters**
        - Geography doesn't change
        - Malacca Strait won't move
        - 33% of trade still passes by
        - Natural hub position
        
        **2. Network Effects**
        - **230+ shipping services** already call Singapore
        - Connectivity breeds more connectivity
        - Shippers want maximum options
        - Hard for new port to replicate network
        
        **3. Ecosystem & Services**
        - **Complete maritime cluster**:
          - Bunkering (#1 globally, 40M+ tonnes/year)
          - Ship repair & conversion
          - Marine insurance
          - Shipping finance
          - Maritime arbitration
          - Technical services
        - **Not just a port** - complete maritime hub
        
        **4. Reliability & Trust**
        - **50+ years** of excellence
        - **Zero strikes** (stable labor)
        - **Predictable operations**
        - **Pro-business government**
        - **Rule of law**
        - Shippers value reliability
        
        **5. Efficiency**
        - **BOA >90%** (ships don't wait)
        - **24-48 hour turnaround**
        - **Tight connections** (<24 hours)
        - Time = money for shipping lines
        
        **6. Technology Leadership**
        - First with CITOS (1988)
        - First fully automated terminal in Asia
        - Continuous innovation
        - R&D investment
        
        **7. Skilled Workforce**
        - **Highly educated** population
        - English-speaking (international business)
        - Technical training programs
        - Attract global talent
        
        **8. Long-term Thinking**
        - Government planning 20-30 years ahead
        - Willing to invest before demand
        - Tuas started in 2012 for 2040 demand
        - **Foresight**, not reaction
        
        **9. Quality Over Quantity**
        - Not trying to be #1 in volume
        - Focus on being **vital node in network**
        - High-value transshipment
        - Premium services
        """)
    
    st.markdown("---")
    st.markdown('<p class="subsection-header">Singapore Maritime Beyond the Port</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### ⛽ Bunkering Hub
        
        **World's #1 Bunkering Port**
        
        **Statistics:**
        - **40+ million tonnes** of fuel sold annually
        - **World's largest** bunker port
        - **250+ bunker craft** operating
        - **12,000-15,000** bunkering operations/year
        
        **Services:**
        - Traditional marine fuel oil (HSFO, LSFO)
        - Low-sulfur fuel (IMO 2020 compliant)
        - **LNG bunkering** (growing)
        - **Biofuels** (emerging)
        - Future: **Methanol, ammonia**
        
        **Why Singapore Leads:**
        - Every ship passing by needs fuel
        - Competitive prices
        - Quality assurance
        - Reliable supply
        - Fast delivery (3-4 hours)
        - 24/7 availability
        
        **Economic Impact:**
        - **$10+ billion** industry
        - Thousands of jobs
        - Strategic advantage
        """)
    
    with col2:
        st.markdown("""
        ### 🔧 Ship Repair & Marine Services
        
        **Asia's Largest Repair Hub**
        
        **Facilities:**
        - **20+ shipyards** and repair facilities
        - **Sembcorp Marine**
        - **Keppel Shipyard**
        - Dry docks up to 400m
        
        **Services:**
        - Ship repair and maintenance
        - Conversion (oil to container, etc.)
        - Offshore rig construction
        - Specialized vessels
        - Regular maintenance
        
        **Capabilities:**
        - Handle ships up to **500,000 DWT**
        - Complex conversions
        - Fast turnaround
        - Quality workmanship
        - Skilled workforce
        
        **Why Ships Choose Singapore:**
        - Strategic location (en route)
        - Can repair while refueling
        - Minimize off-hire time
        - Expert workforce
        - Spare parts availability
        - Quality assurance
        """)
    
    with col3:
        st.markdown("""
        ### 📋 Maritime Services
        
        **Complete Business Ecosystem**
        
        **Shipping Lines:**
        - **100+ shipping lines** headquartered
        - Regional offices for global carriers
        - Maersk, MSC, CMA CGM, etc.
        
        **Maritime Finance:**
        - Ship financing
        - Trade finance
        - Marine insurance
        - Risk management
        
        **Legal & Arbitration:**
        - **Singapore Chamber of Maritime Arbitration**
        - International maritime law
        - Dispute resolution
        - Contracts and charters
        
        **Technical Services:**
        - Ship classification societies
        - Marine surveying
        - Technical consultancy
        - Training and education
        
        **Logistics:**
        - Freight forwarding (1,000+ companies)
        - Warehousing and distribution
        - Cold storage facilities
        - Customs brokerage
        
        **Education:**
        - **Singapore Maritime Academy**
        - **Nanyang Technological University**
        - Maritime training centers
        - Industry certifications
        """)
    
    st.markdown("---")
    st.markdown('<p class="section-header">The Future: 2030-2050</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore is not resting on its laurels. The maritime industry continues to evolve,
    and Singapore is positioning itself for the next 20-30 years.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🎯 Strategic Goals (2030-2050)
        
        **Tuas Completion Timeline:**
        - **2027**: Phase 1 fully operational (20M TEU)
        - **2032**: Phase 2 complete (35M TEU total)
        - **2037**: Phase 3 complete (50M TEU total)
        - **2040**: Phase 4 complete (65M TEU ultimate)
        - **City terminals close progressively**
        
        **Technology Roadmap:**
        
        **2025-2030:**
        - Full deployment of AGVs
        - 5G network across port
        - AI-optimized operations
        - Digital twin maturity
        - Remote crane operations
        
        **2030-2040:**
        - Autonomous vessels in port
        - Blockchain for documentation
        - Quantum computing for optimization
        - Advanced predictive analytics
        - Zero-emission operations
        
        **2040-2050:**
        - Fully autonomous port
        - Hydrogen/ammonia bunkering
        - AI managing entire ecosystem
        - Integration with smart city
        - Climate-resilient infrastructure
        
        **Sustainability Targets:**
        - **2030**: 40% emissions reduction
        - **2040**: 80% emissions reduction
        - **2050**: Net-zero emissions
        - All-electric equipment
        - 100% renewable energy
        """)
    
    with col2:
        st.markdown("""
        ### 💡 Innovation Focus Areas
        
        **1. Alternative Fuels**
        - LNG bunkering expansion
        - Methanol infrastructure
        - Ammonia bunkering (future)
        - Hydrogen capabilities
        - Biofuels supply chain
        
        **2. Digitalization**
        - **Blockchain** for bills of lading
        - **IoT** sensors on containers
        - **AI** for predictive maintenance
        - **Cloud-based** platforms
        - **Cybersecurity** enhancement
        
        **3. Autonomous Systems**
        - Self-driving AGVs (already deployed)
        - Autonomous tugboats
        - Drone inspections
        - Robotic maintenance
        - Automated documentation
        
        **4. Smart Port Integration**
        - Connected to smart city
        - Integrated logistics platform
        - Real-time cargo tracking
        - Seamless customs clearance
        - Supply chain visibility
        
        **5. Skills Development**
        - **Reskilling** existing workforce
        - **STEM education** emphasis
        - **Maritime scholarships**
        - **Industry partnerships**
        - Attract global talent
        
        **6. Regional Connectivity**
        - **ASEAN** port network
        - **Belt & Road** integration
        - Rail connections to hinterland
        - Air-sea cargo integration
        - Multimodal logistics
        """)
    
    st.markdown("---")
    
    st.info("""
    **📚 Related Sections:**
    
    - **Port Operations**: See how vessels are actually handled at Singapore's terminals
    - **CITOS & Technology**: Deep dive into PSA's terminal operating system
    - **Terminal Equipment**: Learn about the quay cranes, AGVs, and automation
    - **KPIs**: Understand the performance metrics that make Singapore efficient
    """)
    
    st.markdown("---")
    
    st.markdown('<div class="success-box">', unsafe_allow_html=True)
    st.markdown("""
    ### 🎓 Key Takeaways
    
    **Why Singapore Succeeded:**
    1. **Geography**: Right place (Malacca Strait exit)
    2. **Vision**: Government commitment since 1960s
    3. **Execution**: World-class operations (PSA)
    4. **Ecosystem**: Complete maritime cluster
    5. **Innovation**: First-mover in automation
    6. **Reliability**: Stable, predictable, efficient
    
    **Why Tuas is Critical:**
    1. **Capacity**: 65M TEU vs current 37M
    2. **Efficiency**: Full automation = lower costs
    3. **Sustainability**: Electric, green, clean
    4. **Future-proof**: Built for 2040-2060 demand
    5. **Land release**: City terminals for redevelopment
    6. **Competition**: Stay ahead of regional rivals
    
    **Singapore's Formula:**
    - Location × Technology × Reliability × Ecosystem = Global Hub
    - Not just a port, but a complete maritime center
    - Continuous reinvestment and innovation
    - Long-term thinking (20-30 year horizons)
    """)
    st.markdown('</div>', unsafe_allow_html=True)
