import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.markdown('<p class="main-header">🚢 Vessels & Containers</p>', unsafe_allow_html=True)
    
    # Hero metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Largest Vessels", "24,000 TEU", help="MGX-24 class")
    with col2:
        st.metric("First Container Ship", "1956", help="500 TEU capacity")
    with col3:
        st.metric("Size Growth", "48x", help="500 → 24,000 TEU")
    with col4:
        st.metric("Crew Size (Modern)", "~26 people", help="For 24K TEU vessel")
    
    st.markdown("---")
    st.markdown('<p class="section-header">Container Ship Evolution (1956-2019)</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        # Vessel evolution data
        evolution_data = pd.DataFrame({
            'Year': [1956, 1970, 1980, 1985, 1988, 2000, 2006, 2013, 2014, 2019, 2020],
            'Generation': ['Early Container Ships', 'Fully Cellular', 'Panamax', 'Panamax Max',
                          'Post Panamax I', 'Post Panamax II', 'VLCS', 'ULCS', 'CSCL 18400', 
                          'MGX-24', 'CMA CGM Jacques Saade'],
            'TEU': [500, 1500, 3000, 4000, 5000, 7000, 12500, 18000, 18400, 24000, 23112],
            'LOA_m': [137, 200, 215, 250, 280, 300, 366, 395, 400, 400, 400],
            'Beam_m': [17, 20, 20, 32, 32, 40, 48, 54, 58.6, 61, 61],
            'Draft_m': [9, 9, 10, 12.5, 13, 14, 15.5, 16, 16, 16, 16],
            'Containers_Across': [6, 8, 10, 13, 17, 18, 22, 23, 23, 24, 23],
            'Crew_Size': [25, 25, 25, 25, 25, 25, 25, 25, 25, 26, 26]
        })
        
        # Interactive evolution chart
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=evolution_data['Year'],
            y=evolution_data['TEU'],
            mode='lines+markers',
            name='TEU Capacity',
            marker=dict(size=12, color='#3B82F6', line=dict(width=2, color='white')),
            line=dict(width=3, color='#3B82F6'),
            text=evolution_data['Generation'],
            hovertemplate='<b>%{text}</b><br>Year: %{x}<br>TEU: %{y:,.0f}<extra></extra>'
        ))
        
        # Add annotations for key milestones
        milestones = [
            (1956, 500, 'First Container Ship'),
            (1980, 3000, 'Panamax Era'),
            (2006, 12500, 'VLCS Introduced'),
            (2019, 24000, 'MGX-24 Mega Vessels')
        ]
        
        for year, teu, label in milestones:
            fig.add_annotation(
                x=year, y=teu,
                text=label,
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=2,
                arrowcolor='#64748B',
                font=dict(size=10, color='#1E293B'),
                bgcolor='#F1F5F9',
                bordercolor='#64748B',
                borderwidth=1
            )
        
        fig.update_layout(
            title='Container Ship Size Evolution (1956-2020)',
            xaxis=dict(title='Year', gridcolor='#E2E8F0'),
            yaxis=dict(title='TEU Capacity', gridcolor='#E2E8F0'),
            height=450,
            hovermode='x unified',
            plot_bgcolor='white'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Detailed evolution table
        st.markdown("### Detailed Vessel Specifications by Generation")
        
        display_df = evolution_data[['Year', 'Generation', 'TEU', 'LOA_m', 'Beam_m', 
                                     'Draft_m', 'Containers_Across']].copy()
        display_df.columns = ['Year', 'Class', 'TEU', 'Length (m)', 'Width (m)', 
                             'Depth (m)', 'Boxes Across']
        
        st.dataframe(display_df, use_container_width=True, hide_index=True)
    
    with col2:
        st.markdown("### Key Vessel Classes")
        
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("""
        **Early Container Ships (1956)**
        - 500-800 TEU
        - 137m × 17m × 9m
        - 6 containers across
        - Revolutionary concept
        
        **Panamax (1980)**
        - 3,000-3,400 TEU  
        - 215m × 20m × 10m
        - Limited by Panama Canal
        - 10 containers across
        
        **Post-Panamax (1988-2000)**
        - 4,000-8,500 TEU
        - Too wide for Panama
        - Enabled by Suez Route
        - 17-18 containers across
        
        **VLCS (2006)**
        - Very Large: 11,000-15,000 TEU
        - 366m × 48m × 15.5m
        - 22 containers across
        - Economies of scale
        
        **ULCS (2013-Present)**
        - Ultra Large: 18,000+ TEU
        - 395-400m × 54-61m × 16m
        - 23-24 containers across
        - Requires specialized ports
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="success-box">', unsafe_allow_html=True)
        st.markdown("""
        **CMA CGM Jacques Saade (2020)**
        
        *Largest LNG-Powered Container Ship*
        
        - **Capacity:** 23,112 TEU
        - **Length:** 400m (4 football fields!)
        - **Height:** 78m
        - **Width:** 61m  
        - **Draft:** 16m
        - **Crew:** 26 people
        - **Fuel:** LNG (cleaner emissions)
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown('<p class="section-header">Vessel Size Classifications</p>', unsafe_allow_html=True)
    
    # Vessel classes comparison
    classes_data = pd.DataFrame({
        'Class': ['Feeder', 'Feedermax', 'Panamax', 'Post-Panamax', 'New Panamax', 
                 'VLCS', 'ULCS', 'Mega Vessels'],
        'TEU Range': ['100-1,000', '1,000-3,000', '3,000-5,000', '5,000-10,000', 
                     '10,000-14,500', '14,500-20,000', '20,000-24,000', '24,000+'],
        'LOA (m)': ['100-150', '150-230', '250-300', '280-350', '350-370', 
                   '370-395', '395-400', '400+'],
        'Max Beam (m)': ['23', '32', '32.3', '45', '49', '56', '60', '61'],
        'Max Draft (m)': ['10', '12', '12.5', '14.5', '15.2', '16', '16', '16'],
        'Panama Canal': ['✓', '✓', '✓ Old', '✗', '✓ Expanded', '✗', '✗', '✗'],
        'Typical Routes': ['Regional/Coastal', 'Intra-Asia', 'All routes', 'Major routes',
                          'Major routes', 'Mainline only', 'Mainline only', 'Asia-Europe'],
        'Port Requirements': ['Basic', 'Standard', 'Standard', 'Deep water', 'Deep water',
                             'Mega port', 'Mega port', 'Specialized']
    })
    
    st.dataframe(classes_data, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown('<p class="subsection-header">Why Vessels Keep Getting Bigger</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 📉 Economies of Scale
        
        **Cost per TEU Decreases:**
        - Larger vessels = Lower cost/container
        - Fuel efficiency improves with size
        - Crew costs spread over more cargo
        
        **Example:**
        - 5,000 TEU vessel: $100/TEU
        - 20,000 TEU vessel: $40/TEU
        - **60% cost reduction!**
        
        **Operating Efficiency:**
        - One large vessel vs 4 small vessels
        - Fewer port calls
        - Reduced crew requirements
        - Lower insurance costs
        """)
    
    with col2:
        st.markdown("""
        ### 🌍 Trade Growth
        
        **Demand Drivers:**
        - Global trade volume increasing
        - E-commerce explosion
        - Manufacturing consolidation
        - Just-in-time delivery
        
        **Route Concentration:**
        - Asia-Europe mainline
        - Trans-Pacific routes
        - High-volume corridors
        
        **Alliance Strategy:**
        - Mega-ships for trunk routes
        - Feeder network distribution
        - Hub-and-spoke model
        - Shared vessel capacity
        """)
    
    with col3:
        st.markdown("""
        ### 🏗️ Port Modernization
        
        **Infrastructure Enables Size:**
        - Deeper berths (16m+ draft)
        - Longer quays (400m+)
        - Bigger cranes (70m+ reach)
        - Automated operations
        
        **Technology Advances:**
        - Better ship design
        - Advanced materials
        - Navigation systems
        - Fuel efficiency
        
        **Competitive Pressure:**
        - Port arms race
        - Attract largest vessels
        - Transshipment volumes
        """)
    
    st.markdown("---")
    st.markdown('<p class="section-header">Container Standardization</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Standard Container Dimensions")
        
        container_specs = pd.DataFrame({
            'Type': [
                '20ft Standard (Dry Van)',
                '40ft Standard (Dry Van)',
                '40ft High Cube',
                '45ft High Cube',
                '20ft Reefer',
                '40ft Reefer',
                '20ft Open Top',
                '40ft Flat Rack',
                '20ft Tank Container'
            ],
            'External Length': ['6.1m (20ft)', '12.2m (40ft)', '12.2m (40ft)', '13.7m (45ft)',
                               '6.1m', '12.2m', '6.1m', '12.2m', '6.1m'],
            'External Width': ['2.4m (8ft)'] * 9,
            'External Height': ['2.6m (8.5ft)', '2.6m (8.5ft)', '2.9m (9.5ft)', '2.9m (9.5ft)',
                               '2.6m', '2.9m', '2.6m', '2.4m', '2.6m'],
            'TEU': ['1', '2', '2', '2.25', '1', '2', '1', '2', '1'],
            'Max Gross Weight': ['24,000 kg', '30,480 kg', '30,480 kg', '30,480 kg',
                                '27,000 kg', '32,000 kg', '30,480 kg', '45,000 kg', '36,000 kg'],
            'Typical Use': [
                'General cargo, retail goods',
                'General cargo, machinery',
                'Light/voluminous goods',
                'Automotive, oversized',
                'Frozen/chilled food',
                'Pharmaceuticals, produce',
                'Heavy/tall cargo',
                'Machinery, vehicles',
                'Liquids, chemicals'
            ]
        })
        
        st.dataframe(container_specs, use_container_width=True, hide_index=True)
        
        st.markdown("### TEU (Twenty-foot Equivalent Unit)")
        st.info("""
        **TEU** is the standard unit for measuring container capacity:
        - **1 TEU** = One 20-foot container
        - **2 TEU** = One 40-foot container
        - **2.25 TEU** = One 45-foot container
        
        **Why TEU matters:**
        - Vessel capacity measured in TEU
        - Port throughput measured in TEU
        - Yard planning uses TEU
        - Standardized global metric
        """)
    
    with col2:
        st.markdown("### Container Types")
        
        st.markdown('<div class="success-box">', unsafe_allow_html=True)
        st.markdown("""
        **By Function:**
        
        🔲 **Dry Van** (most common)
        - Fully enclosed
        - Weather-proof
        - 95% of containers
        
        ❄️ **Reefer** (refrigerated)
        - Temperature controlled
        - -30°C to +30°C
        - Power supply needed
        
        ⬜ **Open Top**
        - Removable roof
        - Tall cargo
        - Crane loading
        
        📦 **Flat Rack**
        - No sides/roof
        - Heavy machinery
        - Oversized cargo
        
        🛢️ **Tank**
        - Liquids/gases
        - Chemical transport
        - Pressurized
        
        📏 **Special**
        - Out-of-gauge (OOG)
        - Dangerous goods
        - Custom builds
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown('<p class="subsection-header">Vessel Cascading Effect</p>', unsafe_allow_html=True)
    
    st.markdown("""
    ### How Older Vessels Move Down the Hierarchy
    
    As new mega-vessels enter service on mainline routes, existing vessels get "cascaded" to secondary routes:
    """)
    
    # Create cascading flow diagram
    fig_cascade = go.Figure()
    
    routes = ['Asia-Europe\nMainline', 'Intra-Asia\nRegional', 'Southeast Asia\nFeeder', 'Coastal\nLocal']
    vessel_sizes = ['24,000 TEU\n(New ULCS)', '12,000 TEU\n(Displaced VLCS)', 
                   '5,000 TEU\n(Older Post-Panamax)', '2,000 TEU\n(Feeder)']
    
    for i in range(len(routes)):
        fig_cascade.add_trace(go.Bar(
            x=[routes[i]],
            y=[len(routes) - i],
            name=vessel_sizes[i],
            marker_color=['#3B82F6', '#10B981', '#F59E0B', '#EF4444'][i],
            text=vessel_sizes[i],
            textposition='inside',
            textfont=dict(color='white', size=11),
            hovertemplate=f'<b>{routes[i]}</b><br>{vessel_sizes[i]}<extra></extra>'
        ))
    
    fig_cascade.update_layout(
        title='Vessel Cascading: Newest Ships → Most Profitable Routes',
        xaxis_title='Route Type',
        yaxis_title='Vessel Priority',
        showlegend=False,
        height=350,
        yaxis=dict(showticklabels=False)
    )
    
    st.plotly_chart(fig_cascade, use_container_width=True)
    
    st.markdown("""
    **Cascading Process:**
    1. **New ULCS delivered** → Deployed on Asia-Europe mainline (highest profit)
    2. **VLCS displaced** → Moved to intra-Asia routes  
    3. **Post-Panamax displaced** → Moved to Southeast Asia feeders
    4. **Older feeders** → Retired or sold to smaller operators
    
    **Impact:**
    - Vessel oversupply on secondary routes
    - Freight rate pressure
    - Smaller ports need bigger infrastructure
    - Older vessels to scrap markets
    """)
    
    st.markdown("---")
    st.markdown('<p class="subsection-header">Port Infrastructure Requirements</p>', unsafe_allow_html=True)
    
    st.markdown("""
    ### What Ports Need to Handle Modern Mega-Vessels
    """)
    
    requirements_data = pd.DataFrame({
        'Infrastructure Element': [
            'Berth Depth',
            'Berth Length',
            'Quay Cranes',
            'Crane Outreach',
            'Crane Height',
            'Apron Width',
            'Yard Space',
            'Yard Stacking',
            'Gate Lanes',
            'Channel Depth',
            'Channel Width'
        ],
        'Feeder Port (3,000 TEU)': [
            '10-12m', '200-250m', '2-3 cranes', '40m', '50m',
            '40m', '20 hectares', '4-5 high', '4-6 lanes',
            '12m', '150m'
        ],
        'Regional Port (8,000 TEU)': [
            '14m', '300m', '4-5 cranes', '50m', '60m',
            '50m', '40 hectares', '5 high', '8-10 lanes',
            '15m', '200m'
        ],
        'Mega Port (24,000 TEU)': [
            '16-18m', '400m+', '6-8 cranes', '65-70m', '70-80m',
            '60m', '80+ hectares', '6+ high (automated)', '12-16 lanes',
            '18m', '300m+'
        ],
        'Investment Cost': [
            '$200-300M', '$500-700M', '$1.5-2B+', '', '', '', '', '', '', '', ''
        ]
    })
    
    st.dataframe(requirements_data, use_container_width=True, hide_index=True)
    
    st.warning("""
    **Mega-Vessel Challenge for Ports:**
    
    - **Deepening berths:** Massive dredging projects
    - **Longer quays:** Land reclamation often required  
    - **Bigger cranes:** $10-15M per super-QC
    - **Yard expansion:** Need 3x space for same throughput
    - **Automation:** Manual operations can't keep pace
    - **Capital investment:** $1-2 billion for mega-terminal
    
    **Result:** Only major hub ports can handle largest vessels, reinforcing hub-and-spoke model
    """)
    
    st.markdown("---")
    
    # Digital Twin Connection
    st.markdown('<div class="digital-twin-callout">', unsafe_allow_html=True)
    st.markdown("""
    ### 💡 Digital Twin Connection - Vessel Modeling
    
    **Critical Vessel Attributes to Track:**
    
    ```python
    vessel_entity = {
        # Identification
        'imo_number': '9876543',  # Unique vessel ID
        'vessel_name': 'CMA CGM JACQUES SAADE',
        'call_sign': 'FNWO',
        'mmsi': '228380600',
        
        # Physical Characteristics
        'loa': 400.0,  # Length Overall (meters)
        'beam': 61.0,  # Width (meters)
        'draft': 16.0,  # Depth (meters) - determines berth compatibility
        'teu_capacity': 23112,
        'reefer_plugs': 2000,
        'containers_across': 23,
        'max_stack_on_deck': 10,
        'max_stack_below': 12,
        
        # Operational
        'shipping_line': 'CMA CGM',
        'alliance': 'Ocean Alliance',
        'service_route': 'FAL1',  # French Asia Line 1
        'vessel_class': 'ULCS',
        'build_year': 2020,
        'flag': 'France',
        'fuel_type': 'LNG',
        
        # Current Voyage
        'previous_port': 'Shanghai',
        'current_port': 'Singapore',
        'next_port': 'Rotterdam',
        'eta': '2024-01-15 14:00',
        'etd': '2024-01-17 06:00',
        
        # Berth Requirements
        'required_depth': 16.5,  # Draft + clearance
        'required_length': 420,  # LOA + buffer
        'required_cranes': 7,  # For 24h turnaround
        'preferred_berth': 'T01',
        
        # Cargo Manifest
        'total_containers': 22500,
        'import': 3500,
        'export': 4200,
        'transship': 14800,
        'empty': 500,
        'reefer': 1200,
        'dangerous_goods': 150,
        
        # Performance Targets
        'target_moves': 8000,  # Import + export + transship discharge/load
        'target_turnaround': 36,  # hours
        'target_crane_intensity': 3.5,
        'target_gcr': 35  # moves per crane hour
    }
    ```
    
    **Vessel State Machine:**
    
    ```python
    vessel_states = {
        'scheduled': {
            'duration': 'varies',
            'next_states': ['approaching'],
            'data_needed': ['ETA', 'manifest', 'stow_plan']
        },
        'approaching': {
            'duration': '4-8 hours',
            'next_states': ['anchorage', 'berthing'],
            'triggers': ['pilot_boarding', 'berth_ready']
        },
        'anchorage': {
            'duration': '0-24 hours',  # BOA = 0 hours
            'next_states': ['berthing'],
            'cost_per_hour': 5000  # Opportunity cost
        },
        'berthing': {
            'duration': '2-4 hours',
            'next_states': ['operations'],
            'resources': ['tugboats', 'pilot', 'linesmen']
        },
        'operations': {
            'duration': '24-48 hours',
            'next_states': ['unberthing'],
            'parallel_tasks': [
                'discharge_import',
                'discharge_transship', 
                'load_export',
                'load_transship',
                'refuel',
                'resupply'
            ]
        },
        'unberthing': {
            'duration': '1-2 hours',
            'next_states': ['departed'],
            'resources': ['tugboats', 'pilot']
        },
        'departed': {
            'duration': 0,
            'next_states': None
        }
    }
    ```
    
    **Size-Based Modeling Considerations:**
    
    | Vessel Size | Berth Allocation | QC Assignment | Turnaround Target | Complexity |
    |-------------|------------------|---------------|-------------------|------------|
    | Feeder (<3K TEU) | Any available berth | 2-3 cranes | 12-18 hours | Low |
    | Panamax (3-5K) | Standard berth | 3-4 cranes | 18-24 hours | Medium |
    | Post-Panamax (5-10K) | Deep berth | 4-6 cranes | 24-30 hours | Medium-High |
    | ULCS (20K+) | Mega berth only | 6-8 cranes | 36-48 hours | Very High |
    
    **Why Vessel Size Matters for Digital Twin:**
    
    1. **Berth Compatibility**: Draft vs available depth (constraints)
    2. **Crane Requirements**: Bigger vessels need more cranes simultaneously
    3. **Yard Impact**: 24K TEU = 24,000 containers to store/retrieve
    4. **Schedule Criticality**: Delays on mega-vessels very expensive
    5. **Complexity**: More containers = more moves = more optimization needed
    
    **Implementation Tips:**
    
    - Store vessel master data separate from voyage data
    - Index vessels by size class for quick filtering
    - Pre-calculate berth compatibility matrix
    - Model crane productivity as function of vessel size
    - Account for slot positioning complexity on larger vessels
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
