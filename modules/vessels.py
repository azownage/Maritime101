import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.markdown('<p class="main-header">🚢 Vessels & Containers</p>', unsafe_allow_html=True)
    
    # Hero metrics
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Largest Vessels Today", "24,000 TEU", help="MGX-24 class mega vessels")
    with col2:
        st.metric("First Container Ship", "1956", help="Ideal X - 58 containers")
    with col3:
        st.metric("Size Growth (60+ years)", "480x", help="From 58 to 24,000+ TEU")
    with col4:
        st.metric("Typical Crew", "13-26 people", help="Modern container ships")
    with col5:
        st.metric("Global Fleet", "~6,000", help="Container ships worldwide")
    
    st.markdown("---")
    
    # Container Revolution
    st.markdown('<p class="section-header">The Container Revolution (1956)</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        ### How a Simple Box Changed the World
        
        **Before Containers (Pre-1956):**
        - **Break-bulk shipping** - cargo loaded piece by piece
        - **Weeks in port** - manual loading/unloading with stevedores
        - **High labor costs** - hundreds of workers per ship
        - **Frequent damage** - manual handling led to losses
        - **Limited intermodal** - difficult to transfer between ship/truck/train
        - **Expensive shipping** - cost dominated by port time, not ocean transport
        
        **The Innovation: Malcolm McLean (1956)**
        
        American trucking entrepreneur Malcolm McLean had a revolutionary idea:
        - Keep cargo in standardized boxes from origin to destination
        - Don't unpack at ports - just transfer the box
        - Use same box on ships, trucks, and trains
        - First voyage: SS Ideal X (April 26, 1956) - 58 containers, Newark to Houston
        
        **Immediate Impact:**
        - **Loading time**: Weeks → Days
        - **Cost per ton**: $5.86 → $0.16 (97% reduction!)
        - **Labor**: 20 men in hours vs 100+ men over days
        - **Damage rates**: Plummeted
        - **Inventory costs**: Reduced dramatically
        
        **The Standardization (1960s-1970s):**
        
        Initially, every shipping line had different container sizes. This was chaos. 
        The **ISO standardized** containers in 1968:
        - **Length**: 20ft, 40ft, 45ft
        - **Width**: 8ft (2.4m)
        - **Height**: 8.5ft standard, 9.5ft high cube
        - **Corner fittings**: Identical on all containers (twist locks)
        
        This standardization unlocked global trade - any container fits any ship, crane, truck, or train.
        """)
    
    with col2:
        st.markdown('<div class="success-box">', unsafe_allow_html=True)
        st.markdown("""
        ### 📊 The Economic Revolution
        
        **Cost Transformation:**
        
        Pre-containerization (1950s):
        - Shipping cost: **25% of retail price**
        - Port time: **50-70%** of total voyage
        - Cargo theft/damage: **15-20%** losses
        
        Post-containerization (1970s+):
        - Shipping cost: **1-2%** of retail price
        - Port time: **10-20%** of total voyage
        - Cargo loss: **<1%**
        
        **Global Trade Explosion:**
        
        1960: **~100M tons** containerized goods
        2020: **~1.9B TEU** moved globally
        
        **Employment Shift:**
        
        1960s NYC port: **30,000** dock workers
        Today: **<3,000** workers (more productive)
        
        Jobs moved from ports to:
        - Manufacturing (cheaper goods)
        - Logistics & supply chain
        - Technology & automation
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.info("""
        **💡 Fun Fact:** The container enabled globalization. 
        
        Your smartphone contains parts from 20+ countries. Without containers, it would be too expensive to ship components globally.
        
        The average container makes **5-6 voyages per year** and lasts **10-15 years** before retirement.
        """)
    
    st.markdown("---")
    st.markdown('<p class="section-header">Container Ship Evolution (1956-Present)</p>', unsafe_allow_html=True)
    
    # Vessel evolution timeline
    evolution_data = pd.DataFrame({
        'Year': [1956, 1968, 1972, 1980, 1985, 1988, 1996, 2000, 2006, 2013, 2017, 2019, 2020],
        'Generation': ['Ideal X (First)', 'Converted Vessels', 'First Generation',
                      'Panamax', 'Panamax Max', 'Post-Panamax I', 'Post-Panamax II',
                      'Post-Panamax III', 'VLCS Era', 'ULCS Introduced', 'Mega Maersk',
                      'MGX-24 Class', 'LNG-Powered'],
        'TEU': [58, 750, 1500, 3000, 4000, 4500, 6000, 8000, 12500, 18000, 20000, 24000, 23112],
        'LOA_m': [135, 185, 200, 250, 275, 285, 300, 320, 366, 395, 399, 400, 400],
        'Beam_m': [17, 23, 25, 32.2, 32.3, 40, 42, 43, 48, 54, 59, 61, 61],
        'Draft_m': [9, 10, 10.5, 12.0, 12.5, 13.0, 13.5, 14.0, 15.5, 16.0, 16.0, 16.0, 16.0],
        'Notable_Vessels': ['SS Ideal X', 'Sea-Land Services', 'Fully Cellular',
                          'Panamax Standard', 'APL C-10', 'Regina Maersk', 'Susan Maersk',
                          'Sovereign Maersk', 'Emma Maersk', 'CSCL Globe', 'Madrid Maersk',
                          'HMM Algeciras', 'CMA CGM Jacques Saade']
    })
    
    # Interactive evolution chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=evolution_data['Year'],
        y=evolution_data['TEU'],
        mode='lines+markers',
        name='TEU Capacity',
        marker=dict(size=10, color='#3B82F6', line=dict(width=2, color='white')),
        line=dict(width=3, color='#3B82F6'),
        text=evolution_data['Notable_Vessels'],
        customdata=evolution_data['Generation'],
        hovertemplate='<b>%{text}</b><br>' +
                     'Generation: %{customdata}<br>' +
                     'Year: %{x}<br>' +
                     'TEU: %{y:,.0f}<extra></extra>'
    ))
    
    # Add era annotations
    eras = [
        (1956, 'Container\nRevolution', 200),
        (1980, 'Panamax\nEra', 3500),
        (2000, 'Post-Panamax\nGrowth', 8500),
        (2013, 'Mega-Ship\nRevolution', 20000)
    ]
    
    for year, label, teu in eras:
        fig.add_annotation(
            x=year, y=teu,
            text=label,
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='#64748B',
            font=dict(size=10, color='#1E293B', weight='bold'),
            bgcolor='#FEF3C7',
            bordercolor='#F59E0B',
            borderwidth=2,
            opacity=0.9
        )
    
    fig.update_layout(
        title='60+ Years of Container Ship Evolution (Exponential Growth)',
        xaxis=dict(title='Year', gridcolor='#E2E8F0', showgrid=True),
        yaxis=dict(title='TEU Capacity (Log Scale)', type='log', gridcolor='#E2E8F0'),
        height=500,
        hovermode='closest',
        plot_bgcolor='white'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed specifications table
    st.markdown("### Detailed Evolution Timeline with Specifications")
    
    display_df = evolution_data[['Year', 'Generation', 'TEU', 'LOA_m', 'Beam_m', 'Draft_m', 'Notable_Vessels']].copy()
    display_df.columns = ['Year', 'Class/Era', 'TEU', 'Length (m)', 'Width (m)', 'Depth (m)', 'Famous Ship']
    
    # Format numbers
    display_df['TEU'] = display_df['TEU'].apply(lambda x: f"{x:,}")
    
    st.dataframe(display_df, use_container_width=True, hide_index=True, height=500)
    
    st.markdown("---")
    st.markdown('<p class="section-header">Vessel Size Classifications</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Modern container ships are classified by size. Each class has different capabilities, routes, and port requirements.
    """)
    
    # Comprehensive vessel classes
    classes_data = pd.DataFrame({
        'Class': ['Feeder', 'Feedermax', 'Panamax', 'Panamax Max', 'Post-Panamax', 
                 'New Panamax', 'VLCS', 'ULCS', 'Mega Class'],
        'TEU Range': ['100-1,000', '1,000-2,000', '2,000-3,000', '3,000-5,000', '5,000-10,000',
                     '10,000-14,500', '14,500-20,000', '20,000-24,000', '24,000+'],
        'Length (m)': ['100-150', '150-200', '200-250', '250-300', '280-350', 
                      '350-366', '366-395', '395-400', '400+'],
        'Width (m)': ['20-23', '23-30', '30-32.2', '32.3', '40-45', 
                     '49', '48-54', '54-59', '59-61'],
        'Depth (m)': ['8-10', '10-11', '11-12', '12-12.5', '13-14.5', 
                     '15.2', '15.5-16', '16', '16+'],
        'Panama Canal': ['✓', '✓', '✓ Original', '✓ Original', '✗', 
                        '✓ Expanded 2016', '✗', '✗', '✗'],
        'Typical Routes': ['Regional/Coastal', 'Intra-regional', 'Global (smaller)', 
                          'Global', 'Major lanes', 'Major lanes', 'Mainline only', 
                          'Asia-Europe mainline', 'Asia-Europe only'],
        'Examples': ['Island trader', 'Regional feeder', 'NYK Altair', 'APL C-10',
                    'Sovereign Maersk', 'CMA CGM Brazil', 'Emma Maersk', 'CSCL Globe',
                    'HMM Algeciras']
    })
    
    st.dataframe(classes_data, use_container_width=True, hide_index=True, height=400)
    
    st.markdown("---")
    st.markdown('<p class="subsection-header">Understanding Key Vessel Dimensions</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 📏 LOA (Length Overall)
        
        **Definition:** Total length of the vessel from bow to stern
        
        **Why it matters:**
        - Determines berth requirements
        - Affects maneuverability
        - Impacts port access
        
        **Modern vessels:**
        - Feeder: 100-200m
        - Panamax: 250-300m
        - ULCS: 395-400m
        - Limit: ~400m (practical)
        
        **Constraint:** Berth length must accommodate LOA + safety buffer (usually 10-20m extra)
        
        **Fun comparison:**
        - 400m = Length of 4 football fields
        - 400m = Height of Empire State Building (laid flat!)
        """)
    
    with col2:
        st.markdown("""
        ### 📐 Beam (Width)
        
        **Definition:** Maximum width of the vessel
        
        **Why it matters:**
        - Determines container rows across deck
        - Limits which canals ship can transit
        - Affects stability
        
        **Key thresholds:**
        - **32.3m** = Max for old Panama Canal
        - **49m** = Max for new Panama Canal
        - **61m** = Modern mega-ships
        
        **Container capacity:**
        - 32m beam = ~13 containers across
        - 49m beam = ~19 containers across
        - 61m beam = ~24 containers across
        
        **Trade-off:** Wider = more cargo BUT fewer ports can handle it
        """)
    
    with col3:
        st.markdown("""
        ### ⚓ Draft (Depth)
        
        **Definition:** Vertical distance from waterline to bottom of keel
        
        **Critical importance:**
        - Determines minimum water depth needed
        - Most limiting factor for port access
        - Varies with cargo load
        
        **Typical drafts:**
        - Feeder: 8-10m
        - Panamax: 12-12.5m
        - ULCS: 16m (fully loaded)
        
        **Port requirements:**
        - Berth depth must be draft + 2-3m clearance
        - 16m draft ship needs 18-19m deep berth
        - Requires constant dredging
        
        **Constraints:**
        - Straits of Malacca: 25m (no problem)
        - Suez Canal: 24m (deep enough)
        - Many ports: <15m (can't handle ULCS)
        """)
    
    st.markdown("---")
    st.markdown('<p class="section-header">Container Types & Specifications</p>', unsafe_allow_html=True)
    
    st.markdown("""
    While the steel box looks simple, there are many specialized container types for different cargo needs.
    All follow ISO standards to ensure they work with all ships, cranes, trucks, and trains globally.
    """)
    
    # Comprehensive container specifications
    container_specs = pd.DataFrame({
        'Type': [
            '20ft Dry Van',
            '40ft Dry Van',
            '40ft High Cube',
            '45ft High Cube',
            '20ft Reefer (Refrigerated)',
            '40ft Reefer High Cube',
            '20ft Open Top',
            '40ft Open Top',
            '20ft Flat Rack',
            '40ft Flat Rack',
            '20ft Tank Container',
            '20ft Bulk Container',
            '40ft Ventilated Container'
        ],
        'External_Length': ['6.1m (20ft)', '12.2m (40ft)', '12.2m (40ft)', '13.7m (45ft)',
                           '6.1m', '12.2m', '6.1m', '12.2m', '6.1m', '12.2m', '6.1m', '6.1m', '12.2m'],
        'External_Width': ['2.4m (8ft)'] * 13,
        'External_Height': ['2.6m (8.5ft)', '2.6m (8.5ft)', '2.9m (9.5ft)', '2.9m (9.5ft)',
                           '2.6m', '2.9m', '2.6m (removable top)', '2.9m (removable top)',
                           '2.4m', '2.4m', '2.6m', '2.6m', '2.6m'],
        'Internal_Volume': ['33 m³', '67 m³', '76 m³', '86 m³', '28 m³', '67 m³',
                           '32 m³', '65 m³', 'N/A', 'N/A', '21-26 m³', '30 m³', '66 m³'],
        'TEU': ['1', '2', '2', '2.25', '1', '2', '1', '2', '1', '2', '1', '1', '2'],
        'Max_Gross_Weight': ['24 tons', '30.5 tons', '30.5 tons', '30.5 tons',
                            '27 tons', '32 tons', '30.5 tons', '30.5 tons',
                            '45 tons', '48 tons', '36 tons', '30 tons', '30 tons'],
        'Typical_Cargo': [
            'General: electronics, textiles, packaged goods',
            'General: machinery, large items, palletized goods',
            'Light/voluminous: furniture, bags, light manufactures',
            'Automotive parts, garments, oversized light goods',
            'Frozen food, meat, fish, ice cream (-30°C to -20°C)',
            'Fresh produce, pharmaceuticals, flowers (+2°C to +8°C)',
            'Heavy/tall: machinery, glass, marble slabs',
            'Steel coils, paper rolls, timber',
            'Heavy machinery, construction equipment, vehicles',
            'Large machinery, boats, oversized cargo',
            'Liquids: chemicals, wine, oils, food-grade',
            'Dry bulk: grains, coffee beans, minerals',
            'Agricultural: coffee, cocoa, onions, potatoes'
        ],
        'Approx_Cost_New': ['$2,000', '$3,000', '$3,500', '$4,000',
                           '$12,000', '$16,000', '$3,500', '$4,500',
                           '$5,000', '$6,500', '$15,000', '$3,500', '$3,500']
    })
    
    st.dataframe(container_specs, use_container_width=True, hide_index=True, height=500)
    
    st.markdown("---")
    st.markdown('<p class="subsection-header">Special Container Categories</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### ❄️ Reefer Containers (Refrigerated)
        
        **How they work:**
        - Built-in refrigeration unit
        - Requires electrical power connection
        - Temperature range: -30°C to +30°C
        - Controlled atmosphere options (CA) for produce
        
        **Power requirements:**
        - On vessel: Plugged into ship's power grid (reefer slots)
        - In yard: Connected to reefer racks with power
        - On truck: Powered by generator or truck
        
        **Typical cargo:**
        - **Frozen** (-25°C): Meat, fish, ice cream, frozen vegetables
        - **Chilled** (+2°C): Fresh produce, dairy, pharmaceuticals
        - **Climate controlled** (+12-15°C): Bananas, flowers, chocolate
        
        **Special considerations:**
        - Must be monitored constantly
        - Temperature alarms critical
        - Pre-trip inspection (PTI) required
        - Accounts for ~10% of global container fleet
        - Critical for global food supply chain
        
        **Cost:** 4-5x more expensive than dry containers
        """)
        
        st.markdown("""
        ### 🚨 Dangerous Goods (DG) Containers
        
        **IMDG Classification (9 Classes):**
        
        1. **Explosives** - Fireworks, ammunition (rare on ships)
        2. **Gases** - LPG, aerosols, compressed gas
        3. **Flammable liquids** - Paint, adhesives, perfumes
        4. **Flammable solids** - Matches, sulfur
        5. **Oxidizing substances** - Fertilizers, bleach
        6. **Toxic substances** - Pesticides, medical waste
        7. **Radioactive** - Medical isotopes (very rare)
        8. **Corrosive** - Batteries, acids, cleaning agents
        9. **Miscellaneous** - Lithium batteries, dry ice
        
        **Stowage rules:**
        - Must be segregated by class
        - Minimum separation distances
        - Special deck positioning
        - Cannot be near food/reefers
        - Clear labeling and placards required
        
        **Documentation:**
        - Dangerous Goods Declaration mandatory
        - Emergency response information
        - Vessel stow plans must show DG locations
        """)
    
    with col2:
        st.markdown("""
        ### 📦 Out-of-Gauge (OOG) Containers
        
        **Definition:** Cargo that exceeds standard container dimensions
        
        **Types:**
        
        **1. Over-Height (OH)**
        - Exceeds height limit
        - Example: Large machinery, factory equipment
        - Uses: Open-top or flat rack
        
        **2. Over-Width (OW)**
        - Exceeds width limit
        - Example: Construction vehicles
        - Uses: Flat rack, platform
        
        **3. Over-Length (OL)**
        - Exceeds 45ft
        - Example: Long beams, pipes
        - Rare, needs special handling
        
        **Challenges:**
        - Requires special stowage planning
        - Often placed on deck (not below)
        - Affects vessel stability calculations
        - Higher freight rates
        - Limited to specific ships/terminals
        
        **Examples:**
        - Yachts and boats
        - Industrial generators
        - Aircraft parts
        - Transformers
        - Mining equipment
        """)
        
        st.markdown("""
        ### 📋 Container Status Categories
        
        **Laden vs Empty:**
        
        **Laden (Full)**
        - Contains cargo
        - Heavy (up to 30 tons gross)
        - Revenue-generating
        - Carefully positioned for stability
        
        **Empty**
        - No cargo, just the box
        - Light (~2.2-4 tons)
        - Repositioning for next load
        - Stack higher (6-8 high vs 4-5 laden)
        - ~20% of global movements
        
        **SOC vs COC:**
        
        **SOC (Shipper-Owned Container)**
        - Owned by cargo owner/shipper
        - They manage the container
        - Usually specialized types
        
        **COC (Carrier-Owned Container)**
        - Owned by shipping line
        - Most common (~95%)
        - Line manages pool
        """)
    
    st.markdown("---")
    st.markdown('<p class="section-header">Why Vessels Keep Getting Bigger</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 📉 Economies of Scale
        
        **The fundamental economics:**
        
        Bigger ships = Lower cost per TEU moved
        
        **Real cost comparison:**
        
        | Vessel Size | Cost per TEU |
        |-------------|--------------|
        | 2,000 TEU | $120 |
        | 8,000 TEU | $65 |
        | 18,000 TEU | $45 |
        | 24,000 TEU | $35 |
        
        **Why bigger is cheaper:**
        
        **1. Crew costs spread:**
        - 24,000 TEU ship: 26 crew
        - 8,000 TEU ship: 24 crew
        - Same crew, 3x capacity!
        
        **2. Fuel efficiency:**
        - Larger hull = better hydrodynamics
        - Bigger engines more efficient
        - Less fuel per container
        
        **3. Capital costs:**
        - Building 1 big ship < 2 medium ships
        - One set of engines, navigation, etc.
        
        **4. Port call costs:**
        - One call handles 3x cargo
        - Fewer calls needed
        - Less port fees overall
        
        **The math:**
        - Move 20,000 TEU with:
          - One 20K vessel: 1 port call
          - Five 4K vessels: 5 port calls
        - 5x port fees, 5x crew, worse fuel economy
        """)
    
    with col2:
        st.markdown("""
        ### 🌍 Trade Volume Growth
        
        **Demand keeps growing:**
        
        - **1990**: 28M TEU global trade
        - **2000**: 60M TEU
        - **2010**: 140M TEU
        - **2020**: 190M TEU
        - **2025**: ~220M TEU (projected)
        
        **Drivers of growth:**
        
        **1. E-commerce explosion**
        - Amazon, Alibaba, etc.
        - Direct-to-consumer shipping
        - Smaller, more frequent shipments
        
        **2. Globalization**
        - Manufacturing in Asia
        - Consumption in West
        - Complex supply chains
        
        **3. Emerging markets**
        - Growing middle class in Asia
        - Increased consumption
        - Two-way trade growing
        
        **4. Just-in-time manufacturing**
        - Less warehouse inventory
        - More frequent shipments
        - Reliability critical
        
        **Route concentration:**
        
        Major routes get biggest ships:
        - **Asia-Europe**: 24K TEU vessels
        - **Trans-Pacific**: 18-20K TEU
        - **Intra-Asia**: 10-15K TEU
        - **Regional**: 2-5K TEU
        
        **Alliance strategy:**
        - Mega-ships on trunk routes
        - Feeder network for distribution
        - Hub-and-spoke model
        """)
    
    with col3:
        st.markdown("""
        ### 🏗️ Infrastructure Arms Race
        
        **Ports enabling bigger ships:**
        
        **Historical progression:**
        
        **1970s ports:**
        - 10m draft berths
        - 30m outreach cranes
        - 200m berth length
        
        **Modern mega-ports:**
        - 18m+ draft berths
        - 70m outreach cranes
        - 400m+ berth length
        - Automated operations
        
        **Investment required:**
        
        To handle 24K TEU vessels:
        - **Dredging**: $200-500M
        - **Berth construction**: $300-600M
        - **Cranes** (each): $12-15M
        - **Automation**: $500M-1B
        - **Total**: $1.5-2.5B per terminal!
        
        **Competitive pressure:**
        
        Ports compete for business:
        - Biggest ships = most cargo
        - Most cargo = lowest costs
        - Lowest costs = win business
        - Winner-takes-all dynamic
        
        **Examples:**
        - **Singapore**: Tuas Port (65M TEU capacity)
        - **Shanghai**: Yangshan Deep Water
        - **Rotterdam**: Maasvlakte 2
        - **Los Angeles**: TraPac terminal
        
        **Technology advances:**
        - Better ship design
        - Stronger materials (high-tensile steel)
        - Advanced navigation systems
        - Fuel-efficient engines
        - LNG/methanol propulsion
        """)
    
    st.markdown("---")
    st.markdown('<p class="section-header">The Cascading Effect</p>', unsafe_allow_html=True)
    
    st.markdown("""
    ### How New Mega-Vessels Reshape Global Shipping Routes
    
    When shipping lines introduce new mega-vessels, it triggers a "cascading" effect throughout the global fleet.
    Older, smaller vessels get pushed down to less profitable routes.
    """)
    
    # Create detailed cascading visualization
    fig_cascade = go.Figure()
    
    # Define the cascade levels
    routes = [
        'Asia-Europe Mainline<br>(Most Profitable)',
        'Trans-Pacific Main<br>(High Volume)',
        'Intra-Asia Main<br>(Regional Hub)',
        'Southeast Asia Feeder<br>(Hub Distribution)',
        'Coastal/Island Service<br>(Local Distribution)',
        'Laid Up or Scrapped<br>(End of Life)'
    ]
    
    vessel_types = [
        '24,000 TEU<br>Brand New ULCS',
        '18,000 TEU<br>Displaced ULCS',
        '10,000 TEU<br>Displaced VLCS',
        '5,000 TEU<br>Older Post-Panamax',
        '2,000 TEU<br>Aging Panamax',
        '500-1,000 TEU<br>Old Feeders'
    ]
    
    colors = ['#2563EB', '#3B82F6', '#60A5FA', '#93C5FD', '#BFDBFE', '#DBEAFE']
    
    for i, (route, vessel) in enumerate(zip(routes, vessel_types)):
        fig_cascade.add_trace(go.Bar(
            y=[route],
            x=[len(routes) - i],
            orientation='h',
            name=vessel,
            marker_color=colors[i],
            text=vessel,
            textposition='inside',
            textfont=dict(color='white', size=11),
            hovertemplate=f'<b>{route}</b><br>{vessel}<br>Priority Level: {len(routes)-i}<extra></extra>'
        ))
    
    fig_cascade.update_layout(
        title='Vessel Cascading: How Ships Move Down the Route Hierarchy',
        xaxis_title='Route Profitability & Priority',
        yaxis_title='',
        showlegend=False,
        height=500,
        xaxis=dict(showticklabels=False),
        barmode='stack'
    )
    
    st.plotly_chart(fig_cascade, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### The Cascade Process Explained
        
        **Step 1: New Vessel Delivered**
        - Shipping line takes delivery of new 24,000 TEU mega-ship
        - Deploys it on most profitable route: Asia-Europe
        - This is the only route with enough cargo volume to fill it
        
        **Step 2: Displacement Begins**
        - The 18,000 TEU vessel on that route is now "surplus"
        - Still good ship, just not the newest/biggest
        - Gets reassigned to Trans-Pacific route
        - Pushes existing Trans-Pac vessel down
        
        **Step 3: Domino Effect**
        - Each displacement pushes next vessel down
        - Like a game of musical chairs
        - Continues down through fleet
        
        **Step 4: Bottom Falls Out**
        - Oldest, smallest vessels have nowhere to go
        - Either:
          - Sold to smaller operators (developing markets)
          - Laid up (anchored, waiting for better market)
          - Scrapped (broken up for steel)
        
        **Timeline:** Full cascade takes 1-3 years to complete
        """)
    
    with col2:
        st.markdown("""
        ### Market Impacts of Cascading
        
        **For Shipping Lines:**
        - ✅ Lower operating costs on mainlines
        - ✅ Competitive advantage
        - ❌ Fleet oversupply on secondary routes
        - ❌ Rate pressure
        
        **For Ports:**
        - ✅ Bigger ships = more cargo per call
        - ❌ Must upgrade infrastructure or lose business
        - ❌ Massive capital investment required
        - Regional ports struggle to compete
        
        **For Freight Rates:**
        - Oversupply drives rates down
        - "Too many ships chasing too few cargoes"
        - Especially severe on intra-Asia routes
        - Rate volatility increases
        
        **For Shippers (Beneficial!):**
        - Lower freight costs
        - More capacity options
        - Better service frequency
        - Competitive carrier market
        
        **Real Example: 2016-2020**
        - 100+ ULCS delivered
        - Cascade pushed 50+ vessels to scrap
        - Freight rates dropped 40%
        - Smaller lines went bankrupt
        - Consolidation accelerated
        """)
    
    st.markdown("---")
    st.markdown('<p class="section-header">Environmental & Future Trends</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🌱 Environmental Considerations
        
        **The Size Paradox:**
        
        Bigger ships are:
        - ✅ More fuel-efficient per TEU
        - ✅ Lower emissions per container
        - ❌ BUT massive total emissions
        
        **A 24K TEU vessel:**
        - Burns: 200-300 tons of fuel per day
        - CO₂: ~600 tons per day
        - But per TEU: 3-5g CO₂ per TEU-km
        - vs Air freight: 500g CO₂ per TEU-km
        
        **New Fuel Technologies:**
        
        **LNG (Liquefied Natural Gas):**
        - 25% less CO₂ than heavy fuel oil
        - No sulfur emissions
        - Example: CMA CGM Jacques Saade
        - Growing fleet (~200 vessels)
        
        **Methanol:**
        - Can use green methanol (renewable)
        - Existing engine modifications
        - Maersk investing heavily
        
        **Ammonia (Future):**
        - Zero carbon when burned
        - Production can be green
        - Still in development
        
        **Hydrogen:**
        - Zero emissions
        - Storage challenges
        - Long-term solution
        
        **Slow Steaming:**
        - Reduce speed: 25 knots → 18 knots
        - 40% fuel savings!
        - Trade-off: longer transit time
        - Widely adopted since 2008
        """)
    
    with col2:
        st.markdown("""
        ### 🔮 Future of Container Ships
        
        **Have We Hit The Limit?**
        
        Physical constraints suggest ~25,000 TEU is practical maximum:
        
        **Port limitations:**
        - Draft: Can't go much deeper than 18m
        - Width: 61-65m absolute max for berths
        - Length: 400-420m infrastructure limit
        
        **Operational challenges:**
        - Longer port stays (2-3 days)
        - Requires 8-10 cranes simultaneously
        - Harder to fill (need huge cargo volume)
        - Schedule reliability suffers
        
        **Economics turning?**
        - Bigger not always better anymore
        - Flexibility becoming more valuable
        - "Cascade fatigue" in industry
        
        **Future Trends:**
        
        **1. Right-sizing not up-sizing**
        - 15-18K TEU "sweet spot"
        - Better schedule reliability
        - More flexible deployment
        
        **2. Dual-fuel / Alternative fuels**
        - Regulatory pressure (IMO 2030/2050)
        - Carbon taxes coming
        - Green fuel premium accepted
        
        **3. Automation**
        - Autonomous navigation (coastal)
        - Reduced crew (10-15 people)
        - Better fuel optimization
        
        **4. Data & optimization**
        - Real-time route optimization
        - Predictive maintenance
        - Better cargo matching
        
        **5. Specialized vessels**
        - Feeder ships optimized
        - Regional specialists
        - Not just "bigger is better"
        """)
    
    st.markdown("---")
    
    # Quick facts
    st.markdown('<p class="subsection-header">Quick Facts & Records</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.success("""
        **🏆 World Records**
        
        **Largest Container Ship:**
        - HMM Algeciras (24,000 TEU)
        - Built: 2020
        - 400m × 61m × 33m
        
        **Most Containers on One Ship:**
        - 21,433 containers (record load)
        - MSC Gülsün, 2019
        
        **Longest Container Ship:**
        - 400m (several vessels tied)
        - = 4 football fields!
        
        **Most Expensive:**
        - ~$200M for new 24K TEU vessel
        - ~$50M for reefer-equipped version
        """)
    
    with col2:
        st.info("""
        **⚙️ Technical Facts**
        
        **Engine Power:**
        - ULCS: 80,000-110,000 HP
        - Top speed: 22-25 knots
        - Fuel: 200+ tons/day
        
        **Stopping Distance:**
        - Full speed to stop: 3-5 km!
        - Takes 20+ minutes
        
        **Container Capacity:**
        - 24K TEU = ~48,000 containers (20ft)
        - Height: 10-12 high on deck
        - Below deck: 12-14 high
        
        **Crew:**
        - Modern ship: 13-26 people
        - Officers: 4-6
        - Engineers: 4-6
        - Ratings: 8-14
        """)
    
    with col3:
        st.warning("""
        **💰 Cost & Economics**
        
        **Operating Costs (24K TEU):**
        - Fuel: $30,000-50,000/day
        - Crew: $10,000/day
        - Maintenance: $5,000/day
        - Insurance: $3,000/day
        - Total: ~$50,000-70,000/day
        
        **Revenue:**
        - Average freight: $2,000/TEU
        - Full ship: $48M revenue
        - Trip time: 30-40 days
        - Net profit: $5-10M/trip
        
        **Port Call Costs:**
        - Berth fees: $50,000-100,000
        - Tugs: $20,000
        - Pilotage: $10,000
        - Services: $20,000
        - Total: $100-150K/port
        """)
    
    st.markdown("---")
    
    st.info("""
    **📚 Want to Learn More?**
    
    - **Next Section**: Port Operations - See how these massive vessels are handled in port
    - **Related**: Terminal Equipment - Learn about the cranes and equipment that move containers
    - **Advanced**: CITOS & Technology - Understand the systems that plan vessel operations
    """)
