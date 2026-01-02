import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.markdown('<p class="main-header">🌊 Global Maritime Trade</p>', unsafe_allow_html=True)
    
    # Hero metrics
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Global Trade by Sea", "80%+", help="Percentage of world trade by volume")
    with col2:
        st.metric("Annual Seaborne Trade", "12.37B tons", help="Total goods moved by ship (2023)")
    with col3:
        st.metric("Container Trade", "1.85B tons", help="Containerized cargo volume")
    with col4:
        st.metric("Asian Ports", "64%", help="Share of seaborne trade unloaded in Asia")
    with col5:
        st.metric("Global Fleet", "~50,000", help="Merchant ships worldwide")
    
    st.markdown("---")
    st.markdown('<p class="section-header">Why Maritime Trade Dominates Global Commerce</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        # Create seaborne trade breakdown
        trade_data = pd.DataFrame({
            'Category': ['Oil & Oil Products', 'Dry Bulk (Iron Ore, Coal, Grain)', 
                        'Containers (Manufactured Goods)', 'Other Cargo'],
            'Volume_Billion_Tons': [3.12, 5.53, 1.85, 1.87],
            'Share': [25.2, 44.7, 15.0, 15.1]
        })
        
        fig = go.Figure(data=[
            go.Pie(
                labels=trade_data['Category'],
                values=trade_data['Volume_Billion_Tons'],
                hole=0.4,
                marker_colors=['#EF4444', '#F59E0B', '#3B82F6', '#8B5CF6'],
                textinfo='label+percent',
                textfont_size=11,
                hovertemplate='<b>%{label}</b><br>Volume: %{value:.2f}B tons<br>Share: %{percent}<extra></extra>'
            )
        ])
        
        fig.update_layout(
            title='Global Seaborne Trade by Cargo Type (2023)<br>Total: 12.37 Billion Metric Tons',
            height=400,
            showlegend=True,
            annotations=[dict(text='12.37B<br>Tons', x=0.5, y=0.5, font_size=16, showarrow=False)]
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        ### The Numbers Behind Global Trade
        
        **Annual Volumes (2023):**
        - **Oil & Petroleum Products**: 3.12 billion metric tons
          - Crude oil, refined products, LNG
          - Energy security critical
        
        - **Dry Bulk**: 5.53 billion metric tons  
          - Iron ore (1.6B tons) - for steel production
          - Coal (1.2B tons) - energy and steel
          - Grain (500M tons) - global food security
          - Other minerals, fertilizers
        
        - **Containers**: 1.85 billion metric tons
          - Manufactured goods, consumer products
          - Fastest growing segment
          - High value-to-weight ratio
        
        **Why Shipping Wins:**
        - **Cost**: Cheapest per ton-mile (1/10th of air freight)
        - **Scale**: One ship = 10,000+ truckloads
        - **Reach**: Connects every continent
        - **Energy**: Most fuel-efficient transport mode
        - **Environment**: Lowest CO₂ per ton-mile
        """)
    
    with col2:
        st.markdown('<div class="success-box">', unsafe_allow_html=True)
        st.markdown("""
        ### 📊 Sea vs Other Transport
        
        **Modal Split (by volume):**
        
        | Mode | Share | Use Case |
        |------|-------|----------|
        | **Sea** | 80% | Bulk, international |
        | Road | 12% | Domestic, last-mile |
        | Rail | 5% | Inland bulk |
        | Air | 0.5% | High-value, urgent |
        | Pipeline | 2.5% | Oil, gas |
        
        **Cost Comparison (per ton-km):**
        
        - Sea: $0.01-0.05
        - Rail: $0.03-0.10
        - Road: $0.10-0.30
        - Air: $1.00-3.00
        
        **Speed vs Cost Trade-off:**
        
        - **Air**: Fast (1-3 days) but expensive
        - **Sea**: Slow (20-40 days) but cheap
        - Result: 99% of consumer goods by sea!
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.info("""
        **🌍 Geographic Reality:**
        
        - **71% of Earth** is ocean
        - **90% of world population** lives within 100km of coast
        - **Major manufacturing hubs** are coastal (China, SEA, India)
        - **Consumption centers** also coastal (US, Europe)
        
        **Result:** Ships connect production to consumption naturally
        """)
    
    st.markdown("---")
    st.markdown('<p class="section-header">Major Global Trade Routes</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The world's container trade flows along specific high-volume corridors, known as trade lanes or routes.
    These routes determine where the biggest ships go and where major ports develop.
    """)
    
    # Major trade routes table
    routes_data = pd.DataFrame({
        'Route': [
            'Asia - Europe (via Suez)',
            'Asia - North America (Trans-Pacific)',
            'Trans-Atlantic (Europe - North America)',
            'Intra-Asia',
            'Asia - Middle East',
            'Asia - Oceania',
            'North-South (Emerging Markets)',
            'Intra-Europe',
            'Latin America - North America'
        ],
        'Annual_Volume_TEU': [
            '25M',
            '22M',
            '7M',
            '40M',
            '8M',
            '3M',
            '15M',
            '6M',
            '5M'
        ],
        'Typical_Vessel_Size': [
            '18,000-24,000 TEU',
            '14,000-18,000 TEU',
            '8,000-14,000 TEU',
            '2,000-10,000 TEU',
            '8,000-12,000 TEU',
            '5,000-8,000 TEU',
            '4,000-8,000 TEU',
            '3,000-8,000 TEU',
            '4,000-10,000 TEU'
        ],
        'Transit_Time': [
            '25-30 days',
            '12-16 days (WC), 21-24 days (EC)',
            '8-10 days',
            '3-14 days',
            '14-18 days',
            '10-15 days',
            '18-25 days',
            '3-7 days',
            '8-14 days'
        ],
        'Major_Cargoes': [
            'Consumer electronics, furniture, apparel, automotive',
            'Electronics, toys, machinery, textiles',
            'Machinery, automotive, chemicals, foodstuffs',
            'Components, semi-finished goods, regional trade',
            'Manufactured goods, consumer products',
            'Consumer goods, vehicles, machinery',
            'Commodities, manufactured goods',
            'Finished goods, automotive, chemicals',
            'Fresh produce, manufactured goods'
        ],
        'Key_Ports': [
            'Singapore, Shanghai, Rotterdam, Hamburg',
            'Shanghai, LA/Long Beach, Oakland, Seattle',
            'Rotterdam, Hamburg, NY/NJ, Savannah',
            'Singapore, Hong Kong, Busan, Port Klang',
            'Dubai, Jebel Ali, Singapore, Shanghai',
            'Sydney, Melbourne, Brisbane, Singapore',
            'Santos, Cartagena, Durban, Lagos',
            'Rotterdam, Antwerp, Hamburg, Felixstowe',
            'Houston, Miami, Veracruz, Santos'
        ]
    })
    
    st.dataframe(routes_data, use_container_width=True, hide_index=True, height=400)
    
    st.markdown("---")
    st.markdown('<p class="subsection-header">The "Big Three" Trade Lanes</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🌏 Asia-Europe
        
        **The Largest Route**
        
        **Volume:** ~25 million TEU/year
        **Direction:** Mostly Asia → Europe
        
        **Typical Journey:**
        - **Origin**: Shanghai, Ningbo, Shenzhen
        - **Route**: East China Sea → South China Sea → **Strait of Malacca** → Indian Ocean → **Suez Canal** → Mediterranean → Europe
        - **Destination**: Rotterdam, Hamburg, Antwerp
        - **Distance**: ~11,000 nautical miles
        - **Transit**: 25-30 days
        
        **Vessel Characteristics:**
        - Largest ships (24,000 TEU)
        - Ultra Large Container Ships (ULCS)
        - Most profitable route
        - Premium services
        
        **Cargo Profile:**
        - **Eastbound (Asia→Europe)**: Electronics, furniture, apparel, toys, machinery
        - **Westbound (Europe→Asia)**: Machinery, automotive, chemicals, luxury goods
        
        **Trade Imbalance:**
        - 2-3x more cargo Asia→Europe
        - Many containers return empty
        - Westbound rates much lower
        
        **Strategic Importance:**
        - Connects world's factory (Asia) to major consumer market (Europe)
        - €600+ billion trade annually
        - Critical for European economy
        """)
    
    with col2:
        st.markdown("""
        ### 🌊 Trans-Pacific
        
        **The US-Asia Corridor**
        
        **Volume:** ~22 million TEU/year
        **Direction:** Mostly Asia → North America
        
        **Two Sub-routes:**
        
        **Trans-Pacific Eastbound (TPE):**
        - **From**: China, Taiwan, Korea
        - **To**: Los Angeles, Long Beach, Oakland, Seattle
        - **Distance**: ~5,500 nm
        - **Transit**: 12-16 days
        
        **Trans-Pacific Westbound (TPW):**
        - Much lower volumes
        - Agricultural products, waste paper, chemicals
        
        **Vessel Characteristics:**
        - 14,000-18,000 TEU typical
        - Slightly smaller than Asia-Europe
        - Why? West Coast port limitations
        
        **Cargo Profile:**
        - **Eastbound**: Electronics, furniture, toys, apparel
        - **Westbound**: Soybeans, cotton, scrap, lumber
        
        **Trade Imbalance:**
        - Massive eastbound flow
        - Westbound often <40% full
        - Empty container repositioning major issue
        
        **Recent Changes (2018-2024):**
        - US-China trade tensions
        - Nearshoring to Mexico
        - Vietnam/Malaysia growth
        - Supply chain diversification
        """)
    
    with col3:
        st.markdown("""
        ### 🌊 Trans-Atlantic
        
        **The Traditional Route**
        
        **Volume:** ~7 million TEU/year
        **Direction:** Relatively balanced
        
        **Route:**
        - **From**: Northern Europe OR US East Coast
        - **To**: US East Coast OR Northern Europe
        - **Distance**: ~3,500 nm
        - **Transit**: 8-10 days
        
        **Vessel Characteristics:**
        - 8,000-14,000 TEU typical
        - Smaller than Pacific routes
        - Faster, more frequent service
        
        **Cargo Profile:**
        - **Westbound (EU→US)**: Machinery, automotive, chemicals, wine, cheese
        - **Eastbound (US→EU)**: Machinery, chemicals, agricultural
        
        **Trade Balance:**
        - More balanced than other routes
        - Both directions well-utilized
        - Premium freight rates
        
        **Competition:**
        - Air freight competitive (only 8-10 days)
        - Time-sensitive cargo goes by air
        - Bulk/heavy stays on sea
        
        **Historical:**
        - Original shipping route
        - Developed infrastructure
        - Mature, stable market
        """)
    
    st.markdown("---")
    st.markdown('<p class="section-header">Critical Maritime Chokepoints</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Global shipping depends on narrow passages that concentrate trade flows. 
    These **chokepoints** are strategic vulnerabilities - if closed, global trade severely disrupted.
    """)
    
    # Chokepoints data
    chokepoints_data = pd.DataFrame({
        'Chokepoint': [
            'Strait of Malacca',
            'Suez Canal',
            'Panama Canal',
            'Strait of Hormuz',
            'Bab el-Mandeb',
            'Strait of Gibraltar',
            'Danish Straits',
            'Turkish Straits (Bosphorus)'
        ],
        'Location': [
            'Between Malaysia & Indonesia',
            'Egypt (connects Med & Red Sea)',
            'Panama (connects Atlantic & Pacific)',
            'Between Iran & Oman',
            'Between Yemen & Djibouti',
            'Between Spain & Morocco',
            'Between Denmark & Sweden',
            'Turkey (connects Black Sea & Med)'
        ],
        'Width_Minimum': [
            '2.8 km',
            '300m (canal)',
            '32m (locks)',
            '39 km',
            '29 km',
            '14 km',
            '4 km',
            '700m'
        ],
        'Daily_Transits': [
            '~227 ships',
            '~72 ships',
            '~39 ships',
            '~20 oil tankers',
            '~60 ships',
            '~90 ships',
            '~60 ships',
            '~140 ships'
        ],
        'Max_Capacity': [
            '~800 ships/day',
            '~100 ships/day',
            '45-57 ships/day',
            'No limit',
            'No limit',
            'No limit',
            'No limit',
            'No limit'
        ],
        'Share_World_Trade': [
            '~33%',
            '~15%',
            '~5%',
            '~21% oil',
            '~8%',
            '~10%',
            'Regional',
            'Regional'
        ],
        'Strategic_Risk': [
            'Piracy, collision, oil spill',
            'Political instability, blockage (2021)',
            'Water shortage, congestion',
            'Iran tensions, oil supply',
            'Yemen conflict, Houthi attacks',
            'Low risk',
            'Low risk',
            'Turkey control, Russia access'
        ],
        'Alternative_Route': [
            'Sunda/Lombok Straits (+3 days)',
            'Cape of Good Hope (+10 days, +$500K fuel)',
            'Cape Horn (+weeks)',
            'Cape of Good Hope',
            'Cape of Good Hope',
            'None practical',
            'None',
            'None for Black Sea'
        ]
    })
    
    st.dataframe(chokepoints_data, use_container_width=True, hide_index=True, height=400)
    
    # Highlight key chokepoints
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="warning-box">', unsafe_allow_html=True)
        st.markdown("""
        ### ⚠️ Strait of Malacca - The World's Most Critical
        
        **Why it matters:**
        - **33% of global seaborne trade** passes through
        - **Connects**: Indian Ocean ↔ Pacific Ocean
        - **Serves**: China, Japan, Korea, Taiwan (world's manufacturing hub)
        - **Alternative**: Sunda Strait (Indonesia) adds 3 days + fuel costs
        
        **Statistics:**
        - Length: 800 km
        - Narrowest point: 2.8 km (near Singapore)
        - Depth: 25m minimum (good for mega-ships)
        - Daily traffic: 200-300 vessels
        
        **Risks:**
        - **Piracy**: Historically high (now reduced)
        - **Collision**: Heavy traffic, narrow passage
        - **Oil spills**: Tankers pass through
        - **Political**: Borders Malaysia, Indonesia, Singapore
        
        **If it closed:**
        - Asian economies severely impacted
        - Global supply chains disrupted
        - Shipping costs spike
        - Energy security threatened (oil/LNG transit)
        
        **Singapore's Strategic Position:**
        - Located at southern exit
        - Becomes natural hub
        - All ships passing through can call
        - This geography built Singapore's port
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="warning-box">', unsafe_allow_html=True)
        st.markdown("""
        ### ⚠️ Suez Canal - The Asia-Europe Lifeline
        
        **Why it matters:**
        - **15% of global trade** uses Suez
        - **Shortcut**: Saves 10+ days vs sailing around Africa
        - **Critical for**: Asia-Europe container trade
        - **Alternative**: Cape of Good Hope adds $500K fuel + 10 days
        
        **Statistics:**
        - Length: 193 km
        - Width: 300m (canal)
        - Depth: 24m (allows ULCS)
        - Daily transits: 60-80 vessels
        - Capacity: ~100 ships/day
        - Revenue: $9 billion/year (Egypt)
        
        **2021 Ever Given Incident:**
        - 400m container ship stuck for 6 days
        - Blocked 400+ ships
        - $10 billion/day trade delayed
        - Global supply chain crisis
        - Insurance claims >$1 billion
        
        **Risks:**
        - **Single point of failure**: No alternative waterway
        - **Political**: Egypt controls, regional instability
        - **Technical**: Groundings, accidents
        - **Capacity**: Already near limits
        
        **Economic Impact:**
        - Europe imports 60% from Asia
        - Without Suez, shipping costs +30-40%
        - Transit time doubles
        - Just-in-time manufacturing fails
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown('<p class="section-header">The Hub-and-Spoke Model</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Modern container shipping uses a **hub-and-spoke** network, similar to airline industry.
    Large vessels call only at major hub ports, then smaller feeders distribute cargo regionally.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Create hub-and-spoke visualization
        fig = go.Figure()
        
        # Hub port (center)
        fig.add_trace(go.Scatter(
            x=[0], y=[0],
            mode='markers+text',
            marker=dict(size=60, color='#EF4444'),
            text=['HUB PORT<br>(Singapore,<br>Shanghai,<br>Rotterdam)'],
            textposition='middle center',
            textfont=dict(color='white', size=9),
            name='Hub Port',
            hovertext='Major transshipment hub<br>24,000 TEU vessels call here',
            hoverinfo='text'
        ))
        
        # Mainline routes (to other hubs)
        mainline_angles = [0, 120, 240]
        mainline_x = [2.5 * np.cos(np.radians(angle)) for angle in mainline_angles]
        mainline_y = [2.5 * np.sin(np.radians(angle)) for angle in mainline_angles]
        
        for i, (x, y) in enumerate(zip(mainline_x, mainline_y)):
            # Draw line
            fig.add_trace(go.Scatter(
                x=[0, x], y=[0, y],
                mode='lines',
                line=dict(color='#3B82F6', width=4),
                showlegend=False,
                hoverinfo='skip'
            ))
            # Add arrow
            fig.add_annotation(
                x=x, y=y,
                ax=0, ay=0,
                xref='x', yref='y',
                axref='x', ayref='y',
                showarrow=True,
                arrowhead=2,
                arrowsize=1.5,
                arrowwidth=3,
                arrowcolor='#3B82F6'
            )
            # Other hub
            fig.add_trace(go.Scatter(
                x=[x], y=[y],
                mode='markers+text',
                marker=dict(size=40, color='#3B82F6'),
                text=['OTHER<br>HUB'],
                textposition='top center',
                textfont=dict(size=8),
                showlegend=False,
                hovertext='Mother vessel 18-24K TEU',
                hoverinfo='text'
            ))
        
        # Feeder ports (spokes)
        feeder_angles = [30, 60, 90, 150, 180, 210, 270, 300, 330]
        feeder_x = [1.2 * np.cos(np.radians(angle)) for angle in feeder_angles]
        feeder_y = [1.2 * np.sin(np.radians(angle)) for angle in feeder_angles]
        
        for x, y in zip(feeder_x, feeder_y):
            # Draw line
            fig.add_trace(go.Scatter(
                x=[0, x], y=[0, y],
                mode='lines',
                line=dict(color='#10B981', width=2, dash='dot'),
                showlegend=False,
                hoverinfo='skip'
            ))
            # Feeder port
            fig.add_trace(go.Scatter(
                x=[x], y=[y],
                mode='markers',
                marker=dict(size=15, color='#10B981'),
                showlegend=False,
                hovertext='Feeder port<br>2-5K TEU vessels',
                hoverinfo='text'
            ))
        
        fig.update_layout(
            title='Hub-and-Spoke Network Model',
            xaxis=dict(showgrid=False, showticklabels=False, zeroline=False, range=[-3, 3]),
            yaxis=dict(showgrid=False, showticklabels=False, zeroline=False, range=[-3, 3]),
            height=500,
            showlegend=False,
            plot_bgcolor='white'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("""
        ### How Hub-and-Spoke Works
        
        **The System:**
        
        **1. Mainline Services (Mother Vessels)**
        - 18,000-24,000 TEU mega-ships
        - Connect major hubs only
        - Examples: Shanghai ↔ Singapore ↔ Rotterdam
        - Weekly/bi-weekly fixed schedules
        
        **2. Hub Ports (Transshipment Centers)**
        - Singapore, Shanghai, Rotterdam, Dubai
        - Containers transferred between vessels
        - 80-90% transshipment rate
        - Massive infrastructure
        
        **3. Feeder Services (Regional Distribution)**
        - 2,000-5,000 TEU smaller vessels
        - Connect hub to regional ports
        - Example: Singapore → Jakarta → Bangkok → Singapore
        - More frequent, flexible schedules
        
        **Why This Model?**
        
        ✅ **Economies of Scale:**
        - Huge ships on major routes = low cost per TEU
        - Smaller ships for low-volume routes
        
        ✅ **Network Effects:**
        - One hub connects many destinations
        - Don't need direct services everywhere
        
        ✅ **Flexibility:**
        - Easy to add/remove feeder routes
        - Mainline stays stable
        
        **Example Journey: Thailand → Germany**
        1. Truck: Bangkok factory → Laem Chabang port
        2. Feeder vessel: Laem Chabang → Singapore (2 days)
        3. **Transshipment** at Singapore hub (12-48 hours)
        4. Mother vessel: Singapore → Rotterdam (25 days)
        5. Feeder vessel: Rotterdam → Hamburg (1 day)
        6. Truck: Hamburg port → warehouse
        
        **Total:** ~33 days door-to-door
        """)
    
    st.markdown("---")
    st.markdown('<p class="section-header">Industry Consolidation & Mega Alliances</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The shipping industry has undergone massive consolidation in the past 25 years.
    From hundreds of independent lines to just **9 major players** controlling 83% of global capacity.
    """)
    
    # Timeline visualization
    timeline_data = pd.DataFrame({
        'Year': [1990, 2000, 2010, 2015, 2017, 2020, 2024],
        'Major_Lines': [20, 18, 15, 13, 11, 10, 9],
        'Alliance_Control': [0, 30, 45, 75, 80, 82, 83]
    })
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=timeline_data['Year'],
        y=timeline_data['Alliance_Control'],
        name='Alliance Market Share (%)',
        marker_color='#3B82F6',
        yaxis='y2',
        opacity=0.7
    ))
    
    fig.add_trace(go.Scatter(
        x=timeline_data['Year'],
        y=timeline_data['Major_Lines'],
        name='Number of Major Shipping Lines',
        mode='lines+markers',
        line=dict(color='#EF4444', width=3),
        marker=dict(size=10)
    ))
    
    fig.update_layout(
        title='Shipping Industry Consolidation (1990-2024)',
        xaxis_title='Year',
        yaxis=dict(title='Number of Major Lines', side='left', range=[0, 25]),
        yaxis2=dict(title='Alliance Control (%)', side='right', overlaying='y', range=[0, 100]),
        hovermode='x unified',
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Current alliance structure
    st.markdown("### The Big Three Mega Alliances (2024)")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("""
        ### 2M Alliance
        **Market Share: 34%**
        
        **Members:**
        - **Maersk** (Denmark) 🇩🇰
        - **MSC** (Switzerland) 🇨🇭
        
        **Fleet:**
        - ~750 vessels
        - 4.3M TEU capacity
        - Largest alliance
        
        **Characteristics:**
        - Only 2 members (simpler)
        - Very profitable
        - Premium services
        - Strong Asia-Europe focus
        
        **Note:** Maersk announced exit from 2M by 2025, alliance ending
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("""
        ### Ocean Alliance
        **Market Share: 30%**
        
        **Members:**
        - **CMA CGM** (France) 🇫🇷
        - **COSCO** (China) 🇨🇳
        - **OOCL** (Hong Kong) 🇭🇰
        - **Evergreen** (Taiwan) 🇹🇼
        
        **Fleet:**
        - ~350 vessels
        - 3.8M TEU capacity
        - Most vessels shared
        
        **Characteristics:**
        - 4 members (more complex)
        - Strong Asian presence
        - Comprehensive network
        - Established 2017
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("""
        ### THE Alliance
        **Market Share: 19%**
        
        **Members:**
        - **ONE** (Japan) 🇯🇵
          - Merger of MOL, K Line, NYK
        - **Yang Ming** (Taiwan) 🇹🇼
        - **Hapag-Lloyd** (Germany) 🇩🇪
        - **HMM** (South Korea) 🇰🇷
        
        **Fleet:**
        - ~240 vessels
        - 2.4M TEU capacity
        - Smallest of the three
        
        **Characteristics:**
        - 4 members
        - Strong trans-Pacific
        - Formed 2017
        - Competitive on Asia-US
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Why Alliances?
    
    **Benefits:**
    - **Vessel Sharing**: Share ship capacity, reduce costs
    - **Network Coverage**: Access to more ports via partners
    - **Economies of Scale**: Bigger ships, better utilization
    - **Risk Sharing**: Spread market volatility
    - **Schedule Reliability**: Combined resources = better service
    
    **How It Works:**
    - Alliance members share vessels on specific routes
    - Each line books slots on partner ships
    - Joint scheduling and planning
    - **But:** They compete on price and service!
    - **Not a merger**: Still independent companies
    
    **Impact on Industry:**
    - ✅ Lower operating costs
    - ✅ Better service coverage
    - ✅ More stable schedules
    - ❌ Less competition (only 3 alliances!)
    - ❌ Higher market power
    - ❌ Harder for smaller lines to compete
    """)
    
    st.markdown("---")
    st.markdown('<p class="section-header">Trade Disruptions & Geopolitics</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🌐 US-China Trade War Impact (2018-2024)
        
        **What Happened:**
        - 2018: US imposed tariffs on Chinese goods
        - China retaliated with counter-tariffs
        - Trade tensions escalated
        - Supply chains disrupted
        
        **The Numbers:**
        - **US imports from China**: -0.4% (2018-2022)
        - **But US total imports**: +32% (demand didn't stop!)
        
        **Supply Chain Rerouting:**
        
        Trade **through intermediaries** exploded:
        - **Vietnam**: +159% from China, +80% to US
        - **Malaysia**: +38% from China, +45% to US
        - **Thailand**: +84% from China, +41% to US
        - **Mexico**: +32% from China, +42% to US
        
        **What Actually Happened:**
        1. Chinese goods shipped to Vietnam/Malaysia
        2. Minor processing/assembly
        3. Re-exported to US (tariff-free)
        4. "Made in Vietnam" label
        
        **Result:**
        - Supply chains longer, more opaque
        - More transshipment
        - Higher shipping demand
        - Intermediate countries boomed
        
        **Lessons:**
        - Trade routes flexible
        - Tariffs don't stop trade, they reroute it
        - Geography matters less than economics
        - Shipping industry adapts quickly
        """)
        
        st.markdown("""
        ### 📉 COVID-19 Pandemic (2020-2022)
        
        **Unprecedented Disruption:**
        
        **2020 Q1-Q2: Demand Collapse**
        - Lockdowns worldwide
        - Manufacturing stopped
        - Shipping plummeted 20%
        - Lines cancelled 30% of sailings
        - Freight rates crashed
        
        **2020 Q3-2021: Explosive Recovery**
        - E-commerce boom
        - Stimulus spending
        - Everyone buying goods
        - Demand surged 25%
        
        **The Crisis:**
        - Ships in wrong locations
        - Containers in wrong places
        - Port congestion (LA: 100+ ships waiting)
        - Crew change crisis
        - Supply chain gridlock
        
        **Freight Rate Explosion:**
        - Pre-COVID: $1,500/FEU (Asia-US)
        - Peak 2021: $20,000/FEU
        - 13x increase!
        - Shipping lines made record profits
        
        **2022-2023: The Correction**
        - Demand normalized
        - New ships delivered
        - Rates crashed back down
        - $1,200/FEU by end 2023
        
        **Long-term Changes:**
        - Inventory strategies changed
        - Just-in-time → Just-in-case
        - Nearshoring accelerated
        - Supply chain transparency increased
        """)
    
    with col2:
        st.markdown("""
        ### 🏴‍☠️ Red Sea Crisis (2023-2024)
        
        **The Situation:**
        - Yemen Houthi rebels attacking ships
        - Bab el-Mandeb strait targeted
        - Red Sea unsafe for commercial shipping
        - Suez Canal route compromised
        
        **Shipping Response:**
        - Major lines rerouted via Cape of Good Hope
        - +10 days transit time (Asia-Europe)
        - +$500K-1M fuel per voyage
        - 15% of global trade affected
        
        **Impacts:**
        - Freight rates spiked 50-100%
        - Longer supply chains
        - More ships needed (same cargo, longer routes)
        - Emissions increased
        
        **Alternative Routes:**
        - **Cape of Good Hope**: 19,000 km vs 11,000 km
        - **Northern Sea Route**: Seasonal, risky
        - **Overland**: Rail through Russia/China
        
        ### 🇺🇦 Russia-Ukraine War (2022+)
        
        **Immediate Impact:**
        - Black Sea shipping halted
        - Grain exports blocked (Ukraine = breadbasket)
        - Energy crisis (Russian gas/oil)
        - Sanctions on Russian shipping
        
        **Global Effects:**
        - Grain prices spiked 50%
        - Food security crisis (Africa, Middle East)
        - LNG shipping boom (replace Russian pipeline gas)
        - Baltic Sea tensions
        
        **Energy Trade Shifts:**
        - Europe stopped Russian imports
        - Russian oil/gas to Asia increased
        - US LNG exports to Europe exploded
        - Tanker trade patterns completely changed
        
        ### 🌊 Panama Canal Drought (2023-2024)
        
        **The Problem:**
        - Climate change → less rainfall
        - Canal uses freshwater (locks)
        - Lake Gatun water level dropped
        - Forced to reduce transits
        
        **Impacts:**
        - Normal: 36-38 ships/day
        - Drought: 22-24 ships/day
        - Waiting times increased to weeks
        - Many ships rerouted via Suez or Cape Horn
        
        **Economic Cost:**
        - Panama Canal revenue down 40%
        - Shipping costs up
        - Supply chain delays
        - US East Coast imports affected
        
        **Long-term Concern:**
        - Climate change = more droughts
        - Canal may become unreliable
        - Alternative routes gain importance
        """)
    
    st.markdown("---")
    st.markdown('<p class="section-header">Future Trends & Challenges</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🌱 Decarbonization
        
        **IMO Regulations:**
        - 2030: 40% CO₂ reduction
        - 2050: Net-zero emissions
        - Mandatory targets
        
        **Solutions:**
        - LNG fuel (25% less CO₂)
        - Methanol (green methanol = zero)
        - Ammonia (zero emission)
        - Hydrogen (future)
        - Slow steaming (40% fuel savings)
        
        **Challenges:**
        - New fuel infrastructure
        - Engine retrofits
        - Higher costs
        - Technology still developing
        
        **Investment:**
        - $1-3 trillion needed globally
        - Lines ordering dual-fuel ships
        - Ports building bunkering
        """)
    
    with col2:
        st.markdown("""
        ### 🤖 Digitalization
        
        **Technologies:**
        - Blockchain for documentation
        - IoT sensors on containers
        - AI route optimization
        - Automated booking platforms
        - Real-time tracking
        
        **Benefits:**
        - Reduce paperwork (80% still paper!)
        - Better visibility
        - Faster customs clearance
        - Predictive maintenance
        - Optimized schedules
        
        **Examples:**
        - Maersk TradeLens (blockchain)
        - Smart containers (real-time monitoring)
        - Digital Bill of Lading
        - Automated port operations
        
        **Barriers:**
        - Industry fragmentation
        - Standardization needed
        - Legacy systems
        - Data sharing concerns
        """)
    
    with col3:
        st.markdown("""
        ### 🌏 Supply Chain Resilience
        
        **Lessons from COVID:**
        - Over-reliance on single sources risky
        - Just-in-time too fragile
        - Need redundancy
        
        **Strategies:**
        
        **1. Nearshoring:**
        - Move manufacturing closer to consumers
        - Mexico for US, Eastern Europe for EU
        - Shorter supply chains
        
        **2. Diversification:**
        - Multiple suppliers
        - Multiple routes
        - Geographic spread
        
        **3. Inventory Buffers:**
        - More safety stock
        - Regional distribution centers
        - Just-in-case vs just-in-time
        
        **4. Vertical Integration:**
        - Own your supply chain
        - Less dependence on third parties
        
        **Trade-off:**
        - More resilient
        - But higher costs
        - Lower efficiency
        - Balance needed
        """)
    
    st.markdown("---")
    
    st.info("""
    **📚 Want to Learn More?**
    
    - **Next Section**: Shipping Alliances - Deep dive into 2M, Ocean, and THE Alliance
    - **Related**: Singapore & Tuas - See how one port became a global hub
    - **Also See**: Port Operations - Understand how ports handle this massive trade flow
    """)
