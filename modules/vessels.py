import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">🚢 Container Vessels & Evolution</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand vessel anatomy and maritime terminology, trace the dramatic 50-fold growth in vessel capacity 
    since 1956, comprehend classification systems (Feeder through ULCS), grasp the economics driving vessel 
    growth, and master the principles of vessel stowage planning that balance stability, destination sequence, 
    structural limits, and container compatibility.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Vessel Anatomy and Maritime Terminology
    # ============================================================================
    
    st.markdown('<p class="section-header">Vessel Anatomy and Maritime Terminology</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Before exploring vessel evolution and operations, we must first establish a solid foundation in vessel 
    anatomy and the precise maritime terminology used throughout the industry. This vocabulary is universal—
    understood identically by crew members, port operators, and maritime professionals worldwide, enabling 
    clear communication in an inherently international industry.
    """)
    
    st.markdown('<p class="subsection-header">Directional and Positional Terms</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Directional Terms (Longitudinal):**
        - **Bow (Forward)**: Front of the vessel, where the ship points when moving ahead
        - **Stern (Aft)**: Back of the vessel, where the propeller and rudder are located
        - **Amidships**: Middle section of the vessel along its length
        - **Fore and Aft**: Towards the bow and towards the stern respectively
        
        **Directional Terms (Lateral):**
        - **Port**: Left side of the vessel when facing forward towards the bow
        - **Starboard**: Right side of the vessel when facing forward towards the bow
        - **Port and Starboard are absolute**: Always the same sides regardless of which way you're facing
        - **Historical origin**: "Starboard" from "steering board" (medieval ships steered from right side)
        - **Port origin**: Ships docked on the left side, opposite the steering board, at the port
        
        **Vertical Terms:**
        - **Deck**: Horizontal platform or floor, vessels have multiple decks
        - **Hold**: Cargo space below the main deck, enclosed storage area
        - **Hatch**: Opening in the deck that provides access to the cargo holds below
        - **Hatch cover**: Heavy steel cover that seals the hatch opening (can support containers on top)
        - **Superstructure**: Buildings and structures above the main deck
        - **Draft**: Depth of the vessel below the waterline (how deep it sits in the water)
        """)
    
    with col2:
        st.markdown("""
        **Key Vessel Sections:**
        - **Bridge (Command Centre)**: Where captain and officers control the vessel
          - Usually located at stern on modern container ships
          - Provides visibility over cargo area
          - Contains navigation equipment, communications, controls
        - **Accommodation**: Living quarters for crew (typically 20-25 people on modern vessels)
          - Cabins, mess hall, recreation areas
          - Usually integrated with bridge superstructure at stern
        - **Engine Room**: Contains main propulsion machinery
          - Massive two-stroke diesel engines (up to 100,000 horsepower)
          - Auxiliary generators for electrical power
          - Usually located at stern below accommodation
        - **Cargo Holds**: Below-deck storage spaces for containers
          - Typically 4-8 holds on a large vessel
          - Hold containers protected from weather and salt spray
          - Accessed via hatches in the main deck
        - **Weather Deck**: Topmost continuous deck exposed to elements
          - Containers stacked on deck above the holds
          - Modern mega vessels: 30-50% of capacity on deck
        
        **Container-Specific Terminology:**
        - **Bay**: Longitudinal slice (lengthwise section of the vessel)
        - **Row**: Transverse position (across the width of the vessel)
        - **Tier**: Vertical stacking position (height)
        - **Cell guides**: Vertical steel rails in holds that guide containers into position
        """)
    
    st.markdown('<p class="subsection-header">Cell Guides: The Critical Innovation</p>', unsafe_allow_html=True)
    
    st.markdown("""
    One of Malcolm McLean's key innovations in the 1950s was the **cell guide system**, perfected by engineer 
    **Keith Tantlinger**. Cell guides are vertical steel rails installed in cargo holds that guide containers 
    into precise positions and hold them securely during the voyage.
    
    **Design Specifications:**
    - **Vertical strips of steel** with a 90-degree angle profile
    - Positioned to align with container corner castings
    - Each cell must be **1¼ inches (3.2cm) longer** than the container length
    - Each cell must be **¾ inch (1.9cm) wider** than the container width
    
    **Why These Tolerances Matter:**
    - **Too tight**: Crane operator cannot easily guide container into the cell (slow operations, risk of damage)
    - **Too loose**: Container shifts excessively during voyage (potential structural damage from impacts)
    - **Precise dimensions**: Allow smooth entry whilst minimising movement at sea
    
    **Operational Benefits:**
    - **Fast loading**: Crane operator lowers container, cell guides automatically align it
    - **Secure stowage**: Containers locked in position by cell guides, minimal additional lashing needed
    - **Weight transfer**: Stack weight transfers through corner castings to cell guides to hull structure
    - **Stability**: Prevents containers shifting during vessel roll, pitch, and yaw in rough seas
    
    **Historical Impact:**
    The second fully cellular container ship (following Ideal-X) used cell guides and increased capacity from 
    58 containers to 226 containers—almost **four times** the load. This demonstrated the transformative power 
    of systematic design for containerisation. Today, all container vessels use cell guide systems in their holds, 
    though on-deck containers require lashing rods and twist-locks for securing.
    """)
    
    st.markdown('<p class="subsection-header">Bay-Row-Tier Positioning System</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Every container on a vessel has a precise three-dimensional address using the **Bay-Row-Tier** system. 
    This coordinate system enables unambiguous identification of any container position, which is absolutely 
    critical for stowage planning, crane operations, and cargo tracking.
    
    **Bay (Longitudinal Position - Front to Back):**
    - Numbered sequentially from **bow (front) to stern (back)**
    - **Odd numbers** (01, 03, 05, 07...): 20-foot container positions
    - **Even numbers** (02, 04, 06, 08...): 40-foot container positions
    - **Important**: A 40-foot container occupies two 20-foot bay positions
      - Example: A container in Bay 02 physically spans bays 01 and 03
    - Large vessels: Bay numbers run from 01 up to 200+ (depending on vessel length)
    - Each bay is approximately 20 feet (6.1m) wide longitudinally
    
    **Row (Transverse Position - Left to Right):**
    - Numbered from **port (left) to starboard (right)** when facing forward
    - **Centre line**: Row 00 (some vessels use this for the centreline position)
    - **Port side** (left): Odd numbers (01, 03, 05, 07...)
    - **Starboard side** (right): Even numbers (02, 04, 06, 08...)
    - Range depends on vessel width:
      - Panamax (13 containers across): Rows 00-12
      - Post-Panamax (18 containers across): Rows 00-17  
      - Mega vessels (24 containers across): Rows 00-23
    
    **Tier (Vertical Position - Bottom to Top):**
    - Numbered from **bottom to top** of the stacks
    - **Below deck** (in holds): 02, 04, 06, 08, 10, 12... (even numbers descending from deck)
      - Deepest hold tier might be 02, 04, 06 depending on hold depth
    - **Deck level**: 80 (standardised reference point)
    - **Above deck** (on deck): 82, 84, 86, 88, 90, 92... (even numbers ascending from deck)
      - Modern mega vessels: Stack up to 10+ tiers above deck (tier 100+)
    - Even numbers used to maintain consistency and allow intermediate positions if needed
    
    **Example Position: Bay 24, Row 08, Tier 86**
    
    Let's decode this completely:
    - **Bay 24**: The 24th longitudinal position from the bow (this is a 40-foot container position, as 24 is even)
    - **Row 08**: The 8th position across the width (this is on the **starboard side** because 08 is even)
    - **Tier 86**: This is **3 tiers above deck level** (Deck = 80, then 82 = 1st above, 84 = 2nd above, 86 = 3rd above)
    
    So this container is located about mid-ship, on the starboard side, three containers above the deck. 
    The crane operator can immediately locate this container with these coordinates, and the Terminal Operating 
    System tracks this exact position throughout all operations.
    """)
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 Why This System is Essential:</strong><br><br>
    <strong>Unambiguous positioning</strong>: Every single position on the vessel has a unique three-dimensional 
    coordinate. No confusion possible.<br><br>
    <strong>Stowage planning precision</strong>: Planners specify the exact Bay-Row-Tier for every one of the 
    10,000+ containers on a mega vessel.<br><br>
    <strong>Operational efficiency</strong>: Crane operators receive instructions like "Bay 24, Row 08, Tier 86" 
    and know exactly where to go. No searching, no delays.<br><br>
    <strong>Safety assurance</strong>: System ensures proper weight distribution (heavy low, light high) and 
    stability (balanced port-starboard, bow-stern).<br><br>
    <strong>Cargo tracking</strong>: Terminal Operating System (TOS) tracks every container movement by Bay-Row-Tier 
    throughout the entire port call.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 2: Vessel Size Evolution - The Dramatic Journey
    # ============================================================================
    
    st.markdown('<p class="section-header">The Dramatic Evolution of Container Vessel Sizes</p>', unsafe_allow_html=True)
    
    st.markdown("""
    One of the most striking transformations in maritime history is the relentless growth in container vessel 
    capacity. In just 64 years (1956-2020), vessels have grown approximately **50 times** in capacity—from 
    Malcolm McLean's pioneering 500 TEU Ideal-X to today's 24,000 TEU mega vessels. This represents one of 
    the most dramatic scaling achievements in engineering history, driven by powerful economic incentives.
    """)
    
    # Comprehensive vessel evolution data from lectures
    vessel_evolution = pd.DataFrame({
        'Year': [1956, 1968, 1972, 1980, 1984, 1996, 1997, 2002, 2003, 2005, 2006, 2012, 2013, 2014, 2017, 2019, 2020],
        'Vessel Name': [
            'Ideal-X',
            'Encounter Bay',
            'Hamburg Express',
            'Neptune Garnet',
            'American New York',
            'Regina Maersk',
            'Susan Maersk',
            'Charlotte Maersk',
            'Anna Maersk',
            'Gjertrud Maersk',
            'Emma Maersk',
            'Marco Polo (CMA CGM)',
            'Maersk Mc-Kinney Møller',
            'CSCL Globe/MSC Oscar',
            'OOCL Hong Kong',
            'MSC Gülsün',
            'HMM Algeciras'
        ],
        'Capacity (TEU)': [500, 1530, 2950, 4100, 4600, 6400, 8000, 8890, 9000, 10000, 11000, 16000, 18270, 19000, 21413, 23756, 23964],
        'LOA (m)': [137, 200, 215, 250, 250, 318, 347, 368, 368, 380, 397, 396, 399, 400, 400, 400, 400],
        'Beam (m)': [17, 20, 20, 32, 32, 42, 43, 43, 43, 54, 56, 54, 59, 59, 59, 61, 61],
        'Draft (m)': [9, 9, 10, 12.5, 12.5, 14, 14.5, 15, 15, 15.5, 16, 16, 16, 16, 16.5, 16, 16.5],
        'Containers Across': ['6', '8', '10', '11', '11', '16', '17', '17', '17', '20', '22', '19', '23', '23', '23', '24', '24'],
        'Era': ['Pioneer', 'Early Cellular', 'Early Cellular', 'Panamax', 'Panamax', 'Post-Panamax', 'Post-Panamax', 'Post-Panamax', 'Post-Panamax', 'VLCS', 'VLCS', 'New-Panamax', 'ULCS', 'ULCS', 'ULCS', 'ULCS', 'ULCS']
    })
    
    st.dataframe(vessel_evolution, width='stretch', hide_index=True)
    
    # Enhanced capacity growth visualisation
    fig = go.Figure()
    
    # Main capacity trend line
    fig.add_trace(go.Scatter(
        x=vessel_evolution['Year'],
        y=vessel_evolution['Capacity (TEU)'],
        mode='lines+markers',
        name='Vessel Capacity',
        line=dict(color='#2563EB', width=4),
        marker=dict(size=10, color='#2563EB', line=dict(color='white', width=2)),
        text=vessel_evolution['Vessel Name'],
        customdata=vessel_evolution[['Era', 'Containers Across']],
        hovertemplate='<b>%{text}</b><br>Year: %{x}<br>Capacity: %{y:,} TEU<br>Era: %{customdata[0]}<br>Width: %{customdata[1]} containers across<extra></extra>'
    ))
    
    # Add era annotations
    fig.add_annotation(x=1970, y=2000, text="Panamax Era<br>(Canal Limited)", showarrow=False, font=dict(size=11, color='#6B7280'))
    fig.add_annotation(x=2000, y=8000, text="Post-Panamax<br>(Breaking Limits)", showarrow=False, font=dict(size=11, color='#6B7280'))
    fig.add_annotation(x=2017, y=20000, text="ULCS Era<br>(Mega Vessels)", showarrow=False, font=dict(size=11, color='#EF4444'))
    
    fig.update_layout(
        title={
            'text': 'Container Vessel Capacity Growth: 1956 → 2020 (50× Increase)',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#1F2937'}
        },
        xaxis_title="Year",
        yaxis_title="Capacity (TEU)",
        height=550,
        plot_bgcolor='white',
        xaxis=dict(gridcolor='#E5E7EB', range=[1955, 2021]),
        yaxis=dict(gridcolor='#E5E7EB', range=[0, 26000])
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    **Key Phases in Vessel Evolution:**
    
    **Phase 1: The Pioneer Era (1956-1970) - Proving the Concept**
    - **1956: Ideal-X (500 TEU)** - Malcolm McLean's first container ship
      - Converted oil tanker with containers on deck
      - Carried just 58 containers from Newark to Houston
      - Proved containerisation concept economically viable
    - **1968: Encounter Bay (1,530 TEU)** - First purpose-built fully cellular vessel
      - Cell guides in holds for secure stacking
      - Container capacity tripled compared to Ideal-X
    - **1972: Hamburg Express (2,950 TEU)** - Early growth continues
    - **Focus**: Proving that containerisation reduces costs and increases efficiency
    - **Constraint**: Conservative growth as ports develop infrastructure
    
    **Phase 2: The Panamax Era (1980-1995) - Canal-Limited Growth**
    - **1980: Neptune Garnet (4,100 TEU)** - Approaching canal limits
    - **1984: American New York (4,600 TEU)** - Close to maximum Panamax size
    - **Defining constraint**: Panama Canal's old locks
      - Maximum beam (width): **32.3 metres**
      - Maximum capacity: **~4,500 TEU**
    - **Standard**: Panamax vessels dominated for two decades (1980s-2000s)
    - **Result**: Vessel sizes plateaued as canal created a natural ceiling
    
    **Phase 3: Breaking Free - Post-Panamax (1996-2012) - Rapid Expansion**
    - **1996: Regina Maersk (6,400 TEU)** - First Post-Panamax generation
      - Too wide for Panama Canal old locks (no longer constrained by canal)
      - Focused on high-volume Asia-Europe routes (via Suez Canal)
    - **2000s: Dramatic growth** - 6,400 → 11,000+ TEU in just 10 years
    - **2006: Emma Maersk (11,000 TEU)** - First vessel over 10,000 TEU
    - **2012: Marco Polo (16,000 TEU)** - Breaking through 15,000 TEU barrier
    - **Drivers**: 
      - Economics of scale becoming more compelling
      - Asia-Europe trade boom requiring larger vessels
      - Suez Canal has no width restrictions (no locks)
    
    **Phase 4: The Mega Vessel Era (2013-Present) - ULCS Dominance**
    - **2013: Maersk Mc-Kinney Møller (18,270 TEU)** - Maersk Triple-E class
      - Revolutionary design: Lower speed, extreme efficiency
      - Named after Maersk's visionary leader
    - **2014: CSCL Globe/MSC Oscar (19,000+ TEU)** - Breaking 19,000 TEU
    - **2017: OOCL Hong Kong (21,413 TEU)** - First vessel over 21,000 TEU
    - **2019: MSC Gülsün (23,756 TEU)** - Largest vessel globally (as of 2024)
    - **2020: HMM Algeciras (23,964 TEU)** - Current record holder
      - **400 metres long** - longer than 4 football fields placed end-to-end
      - **61 metres wide** - 24 containers across the width
      - **16.5 metres draft** - requires deep water ports
      - **Operated by 26 crew members** - same as much smaller vessels
    - **Approaching practical limits**:
      - Port infrastructure (crane reach, berth depth)
      - Suez Canal draft limit (~20m maximum)
      - Structural integrity of vessel (stress on hull)
      - Commercial risk (too many eggs in one basket)
    """)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ Have We Reached Peak Vessel Size?</strong><br><br>
    Most industry experts believe vessels have reached or are approaching practical maximum sizes:<br><br>
    <strong>Infrastructure constraints</strong>: Only 20-30 ports globally can handle 24,000 TEU vessels 
    (depth, crane reach, berth length)<br><br>
    <strong>Canal limits</strong>: Suez Canal draft limits vessels to approximately 25,000 TEU maximum. Panama Canal 
    limited to 14,500 TEU even with new locks<br><br>
    <strong>Structural limits</strong>: Hull stresses increase exponentially with size. Bending moments in rough 
    seas approach material limits<br><br>
    <strong>Commercial risk</strong>: One 24,000 TEU vessel carries cargo worth $500M+. Engine failure or grounding 
    causes massive supply chain disruption<br><br>
    <strong>Port productivity limits</strong>: Larger vessels require longer port stays (loading/unloading 
    10,000+ containers). Diminishing returns on size<br><br>
    Future growth likely to focus on <strong>efficiency improvements</strong> (fuel, emissions, automation) rather 
    than size increases.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 3: Vessel Classification Systems
    # ============================================================================
    
    st.markdown('<p class="section-header">Vessel Classification by Size and Capability</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The container shipping industry uses several classification systems based on vessel size, capability, and 
    the routes they can serve. Understanding these classifications is essential for port planning, berth 
    allocation, and comprehending operational discussions. These classifications are not arbitrary—they 
    correspond to real physical constraints (canals, ports) and operational patterns (trade routes, cargo volumes).
    """)
    
    # Enhanced classification data
    vessel_classes = pd.DataFrame({
        'Class': [
            'Feeder',
            'Feedermax',
            'Panamax',
            'Post-Panamax',
            'New-Panamax',
            'VLCS',
            'ULCS'
        ],
        'Full Name': [
            'Feeder',
            'Feedermax',
            'Panamax',
            'Post-Panamax',
            'New-Panamax (Neo-Panamax)',
            'Very Large Container Ship',
            'Ultra Large Container Ship'
        ],
        'Capacity (TEU)': [
            '100 - 1,000',
            '1,000 - 3,000',
            '3,000 - 5,000',
            '5,000 - 10,000',
            '10,000 - 14,500',
            '10,000 - 18,000',
            '18,000 - 25,000+'
        ],
        'Beam/Width (m)': ['<23', '23-30', '32.2 (max)', '32.3-49', '49 (max)', '49-59', '59-61+'],
        'Defining Constraint': [
            'Small ports, rivers, shallow water',
            'Regional ports, short-sea routes',
            'Old Panama Canal width limit (closed 2016)',
            'Suez Canal width (no strict limit)',
            'New Panama Canal width limit (2016+)',
            'Port infrastructure (crane reach, depth)',
            'Approaching theoretical maximum'
        ],
        'Typical Routes': [
            'Short-sea, coastal, river ports',
            'Intra-regional (within Asia, Europe)',
            'Trans-Pacific, Asia-Europe (historical)',
            'Major trade lanes, cannot use Panama',
            'Trans-Pacific via new Panama Canal',
            'Asia-Europe mainline via Suez',
            'Asia-Europe mainline via Suez only'
        ],
        'Ports Accessible': [
            'Nearly all ports globally',
            'Most regional and hub ports',
            'All major ports (historical standard)',
            'Major hub ports only (~100-150 globally)',
            'Major hub ports with depth (~80 globally)',
            'Elite hub ports with infrastructure (~40 globally)',
            'Only ~20-30 ports globally equipped'
        ]
    })
    
    st.dataframe(vessel_classes, width='stretch', hide_index=True)
    
    st.markdown('<p class="subsection-header">Canal Constraints: How Geography Shapes Vessel Sizes</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Panama Canal Constraints:**
        
        **Old Locks (1914-2016) - "Panamax" Standard:**
        - **Maximum length**: 294.1 metres (965 feet)
        - **Maximum beam (width)**: **32.3 metres** (106 feet) - **The Panamax Limit**
        - **Maximum draft**: 12.0 metres (39.5 feet)
        - **Capacity**: Approximately 4,500 TEU maximum
        - **Lock dimensions**: 320m × 33.5m × 26m deep
        - **Historical impact**: Defined vessel sizes for decades (1980s-2010s)
        
        **New Locks (2016-Present) - "New-Panamax" Standard:**
        - **Maximum length**: 366 metres (1,200 feet)
        - **Maximum beam (width)**: **49 metres** (161 feet) - **The New-Panamax Limit**
        - **Maximum draft**: 15.2 metres (50 feet)
        - **Capacity**: Approximately 14,500 TEU maximum
        - **Investment**: $5.25 billion expansion project
        - **Opened**: June 26, 2016 (third set of locks)
        
        **Economic Impact:**
        - Allows larger vessels on trans-Pacific routes
        - Reduced Asia-US East Coast shipping costs by 20-30%
        - But mega vessels (20,000+ TEU) still cannot use Panama Canal
        - These ultra-large vessels restricted to Asia-Europe via Suez or around Africa
        """)
    
    with col2:
        st.markdown("""
        **Suez Canal Constraints:**
        
        **Current Specifications (After Multiple Deepening Projects):**
        - **Maximum length**: No practical limit (canal is 193 km long)
        - **Maximum beam (width)**: **77.5 metres** - Much wider than Panama (no locks)
        - **Maximum draft**: **20.1 metres** (66 feet) - Deepest navigable draft
        - **No locks**: Sea-level canal (no width restriction from locks)
        - **Can accommodate**: All existing container vessels, including largest ULCS
        
        **Strategic Importance:**
        - **Asia-Europe route**: 33% of global container trade passes through Suez
        - **Alternative route**: Around Cape of Good Hope adds:
          - **+3,500 nautical miles** (+6,500 kilometres)
          - **+7-10 days sailing time**
          - **+$500,000 fuel costs** per voyage
        - **Critical chokepoint**: Blockage (e.g., Ever Given incident March 2021) disrupts global trade
        - **One-way operation**: Vessels travel in convoys, alternating directions
        - **Canal fees**: $500,000-$800,000 per transit for large vessels
        
        **Why Mega Vessels Dominate Asia-Europe:**
        - No width restriction (unlike Panama Canal)
        - Deep draft accommodates largest vessels
        - High-volume route justifies mega vessels (economies of scale)
        - Mega vessels physically cannot use Panama Canal
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🗺️ Geography Shapes Fleet Composition:</strong><br><br>
    <strong>Asia-Europe routes (via Suez)</strong>: Dominated by ULCS vessels (18,000-24,000 TEU) because Suez 
    can accommodate them and volumes justify the scale.<br><br>
    <strong>Trans-Pacific routes (Asia-US West Coast)</strong>: Mix of Post-Panamax (8,000-14,000 TEU) and 
    New-Panamax (up to 14,500 TEU) since new Panama Canal opened 2016.<br><br>
    <strong>Asia-US East Coast routes</strong>: New-Panamax vessels (10,000-14,500 TEU) dominate since 2016 
    expansion. Before 2016, cargo went to West Coast then rail across US.<br><br>
    <strong>Intra-regional routes</strong>: Feeder and Feedermax vessels (1,000-3,000 TEU) connect smaller ports 
    to major hub ports where mega vessels call.<br><br>
    The result: Vessel size is not just about economics—geography and infrastructure fundamentally determine 
    which vessels can serve which routes.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 4: Economics of Scale - Why Bigger is (Usually) Better
    # ============================================================================
    
    st.markdown('<p class="section-header">Economics of Scale: The Driving Force Behind Vessel Growth</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The relentless growth in vessel sizes is driven by powerful economic incentives. Understanding these 
    economics helps explain why shipping lines continue building larger vessels despite operational challenges 
    and infrastructure constraints. The fundamental principle is simple: many costs do not scale proportionally 
    with vessel size, creating dramatic per-container cost savings as vessels grow.
    """)
    
    # Cost comparison data
    cost_comparison = pd.DataFrame({
        'Vessel Size (TEU)': [1000, 3000, 5000, 8000, 12000, 18000],
        'Cost per TEU (Index)': [100, 68, 52, 38, 28, 18],
        'Crew Size': [15, 20, 22, 24, 25, 26],
        'Crew Cost per TEU (Index)': [100, 44, 29, 20, 14, 10],
        'Fuel per TEU (Index)': [100, 75, 62, 51, 43, 38],
        'Port Cost per TEU (Index)': [100, 45, 33, 25, 20, 17],
        'Capital Cost per TEU (Index)': [100, 70, 55, 43, 35, 28]
    })
    
    # Enhanced cost visualisation
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=cost_comparison['Vessel Size (TEU)'],
        y=cost_comparison['Cost per TEU (Index)'],
        mode='lines+markers',
        name='Total Cost per TEU',
        line=dict(color='#EF4444', width=4),
        marker=dict(size=14, color='#EF4444', line=dict(color='white', width=2)),
        fill='tozeroy',
        fillcolor='rgba(239, 68, 68, 0.1)'
    ))
    
    fig.add_trace(go.Scatter(
        x=cost_comparison['Vessel Size (TEU)'],
        y=cost_comparison['Crew Cost per TEU (Index)'],
        mode='lines+markers',
        name='Crew Cost per TEU',
        line=dict(color='#3B82F6', width=3, dash='dash'),
        marker=dict(size=10)
    ))
    
    fig.add_trace(go.Scatter(
        x=cost_comparison['Vessel Size (TEU)'],
        y=cost_comparison['Fuel per TEU (Index)'],
        mode='lines+markers',
        name='Fuel Cost per TEU',
        line=dict(color='#10B981', width=3, dash='dash'),
        marker=dict(size=10)
    ))
    
    fig.update_layout(
        title={
            'text': 'Economies of Scale: Cost per TEU vs Vessel Size<br>(Indexed to 1,000 TEU = 100)',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        xaxis_title="Vessel Capacity (TEU)",
        yaxis_title="Cost Index (1,000 TEU = 100)",
        height=500,
        plot_bgcolor='white',
        xaxis=dict(gridcolor='#E5E7EB'),
        yaxis=dict(gridcolor='#E5E7EB', range=[0, 110]),
        legend=dict(x=0.7, y=0.95)
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    **Understanding the Cost Structure:**
    
    **Fixed Costs (Do Not Scale with Size):**
    
    **Crew Salaries and Benefits:**
    - **Small vessel (1,000 TEU)**: Approximately 15 crew members
    - **Mega vessel (18,000 TEU)**: Approximately 26 crew members (only 1.7× more crew for 18× capacity)
    - **Annual crew cost**: $4-6 million per vessel (salaries, benefits, training, relief crews)
    - **Result**: Crew cost per TEU drops by **90%** from small to mega vessels
    
    **Insurance:**
    - Hull and machinery insurance relatively flat (based on replacement value, not cargo capacity)
    - Protection and indemnity (P&I) insurance scales somewhat but not proportionally
    
    **Administration and Overhead:**
    - Port agency fees, documentation, communications
    - Relatively fixed regardless of vessel size
    
    **Port Charges:**
    - Many port fees based on vessel dimensions (length, tonnage), not cargo volume
    - Larger vessels pay more in absolute terms but much less per TEU
    
    **Variable Costs (Scale Less Than Proportionally):**
    
    **Fuel Consumption:**
    - **Physics**: Doubling vessel capacity does NOT double fuel consumption
    - **Hull efficiency**: Larger vessels have better length-to-beam ratios (less resistance per TEU)
    - **Engine efficiency**: Modern two-stroke engines more efficient at larger scale
    - **Slow steaming**: Larger vessels can operate at lower speeds (18-20 knots vs 22-25 knots)
      - Speed reduction from 25 to 19 knots = 40-50% fuel saving
      - Larger vessels have schedule flexibility to accommodate slower speeds
    - **Result**: 18,000 TEU vessel uses 38% of fuel per TEU compared to 1,000 TEU vessel
    
    **Capital Cost (Building the Vessel):**
    - Building costs do NOT double when capacity doubles
    - Steel requirements scale by surface area (increases with square of dimensions)
    - Capacity scales by volume (increases with cube of dimensions)
    - **Example**: 18,000 TEU vessel costs ~$150M; 1,000 TEU vessel costs ~$25M
      - 18,000 TEU vessel is 6× more expensive but carries 18× more cargo
      - Cost per TEU slot: $8,333 vs $25,000 (70% reduction)
    
    **Maintenance and Repairs:**
    - Slightly higher in absolute terms for larger vessels
    - But not proportional to capacity increase
    - Scheduled drydock, engine overhauls, equipment replacement
    
    **The Bottom Line - Dramatic Cost Savings:**
    - **1,000 TEU vessel**: $1,000 cost per TEU per voyage (index 100)
    - **8,000 TEU vessel**: $380 cost per TEU per voyage (index 38) - **62% reduction**
    - **18,000 TEU vessel**: $180 cost per TEU per voyage (index 18) - **82% reduction**
    
    This is why shipping lines keep building larger vessels despite operational challenges. The cost savings 
    are simply too compelling to ignore.
    """)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ The Catch: Economies of Scale Have Prerequisites</strong><br><br>
    <strong>High utilisation required</strong>: Need to fill 85-90%+ of vessel capacity to realise cost savings. 
    Empty slots destroy the economics.<br><br>
    <strong>High-volume routes essential</strong>: Only major trade lanes (Asia-Europe, Trans-Pacific) generate 
    enough cargo to justify mega vessels. Regional routes cannot sustain them.<br><br>
    <strong>Limited port access</strong>: Only 20-30 ports globally have the infrastructure (depth, cranes, 
    yard space) to handle 20,000+ TEU vessels efficiently.<br><br>
    <strong>Concentration risk</strong>: One 24,000 TEU vessel carries cargo worth $500 million. Engine failure, 
    grounding, or port closure causes massive supply chain disruption.<br><br>
    <strong>Slower port rotations</strong>: Larger vessels call at fewer ports per voyage (only major hubs), 
    requiring more feeder vessels to distribute cargo.<br><br>
    <strong>Weather sensitivity</strong>: Mega vessels with high deck stacks are more affected by wind forces, 
    limiting operations in high winds (>15-20 m/s).<br><br>
    <strong>Single point of failure</strong>: If a mega vessel breaks down, thousands of containers are delayed. 
    Unlike smaller vessels where risk is distributed across more ships.<br><br>
    Despite these challenges, the 82% cost reduction drives continued deployment of mega vessels on high-volume 
    mainline routes.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 5: Vessel Stowage Planning - The 3D Tetris Challenge
    # ============================================================================
    
    st.markdown('<p class="section-header">Vessel Stowage Planning: Optimising the 3D Puzzle</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Vessel stowage planning—determining the exact position for every container on the vessel—is one of the 
    most complex optimisation problems in maritime logistics. A stowage planner must position 10,000-20,000 
    containers on a mega vessel whilst simultaneously satisfying multiple competing constraints: vessel stability, 
    destination sequence, structural limits, container compatibility, and operational efficiency. It's like 
    playing three-dimensional Tetris with thousands of pieces, strict physics rules, and millions of dollars 
    at stake if you get it wrong.
    """)
    
    st.markdown('<p class="subsection-header">The Stowage Planning Principles</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Modern stowage planning software considers five primary constraint categories, each with multiple sub-rules. 
    Violating any constraint can result in vessel instability, damaged cargo, operational delays, or safety hazards.
    """)
    
    st.markdown('<p class="subsection-header">Principle V1: Weight Distribution and Vessel Stability</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Vessel stability** is the paramount safety concern. An improperly loaded vessel can list dangerously, 
    capsize in rough seas, or suffer structural failure from excessive bending moments. The lecture materials 
    emphasise that "**stability is an important parameter to measure vessel safety**" and defines stability as 
    "**the ability of the vessel to tilt due to external forces (such as wind and surge) and automatically 
    return to the original equilibrium position when the external forces disappear**."
    
    **Critical Stability Concepts:**
    
    **Centre of Gravity (G) - The Balance Point:**
    - The single point where all the vessel's weight effectively acts
    - Lower G = more stable vessel (weight concentrated low)
    - Higher G = less stable vessel (top-heavy, risk of capsizing)
    - **Practical rule**: Heavy containers (>25 tonnes) go in lower holds, light containers (<15 tonnes) on upper deck tiers
    - Modern mega vessels have 30-50% of capacity on deck (lecture: "30% of total loading capacity... for modern container vessels, especially large ones, is even higher, almost half")
    - **Challenge**: Large number of on-deck containers raises centre of gravity, reducing stability
    
    **Metacentric Height (GM) - Stability Measure:**
    - Technical measure of initial stability
    - GM = distance between centre of gravity (G) and metacentre (M)
    - **Too low GM** (G too high): Vessel unstable, risk of capsizing in rough seas
    - **Too high GM** (G too low): Vessel rolls uncomfortably, harsh motion (bad for cargo and crew)
    - **Target range**: Typically GM between 0.5-2.0 metres (vessel-specific, verified by loading computer)
    - **Calculation**: Stowage planning software calculates GM automatically based on container positions and weights
    
    **Longitudinal Balance (Bow-to-Stern):**
    - Weight must be distributed evenly along vessel length
    - **Lecture guidance**: "In the longitudinal direction, the heavier should be in the middle, and the lighter at both ends"
    - **Specific rules**:
      - "The bays from the bow to one-fourth of the hull and behind the living quarters over the vessel should be loaded with lighter containers"
      - "The middle of the vessel with heavier containers"
    - **Prevents**:
      - **Hogging**: Excessive weight at bow and stern causes hull to bend upward amidships (structural failure risk)
      - **Sagging**: Excessive weight amidships causes hull to bend downward (structural failure risk)
    - **Target**: Near-zero trim (vessel level) or slight stern trim for propeller efficiency
    
    **Transverse Balance (Port-to-Starboard):**
    - Weight must be distributed evenly across vessel width
    - **Lecture guidance**: "In the lateral direction, the heavier should be in the middle, and the lighter at both sides"
    - **Within each bay**: "The heaviest containers are loaded to the centre rows, and the lighter to both sides"
    - **Prevents**:
      - **List**: Vessel leaning to one side (port or starboard)
      - Excessive list causes cargo shift, makes vessel uncomfortable, reduces stability
    - **Target**: Zero list (vessel perfectly upright)
    - **Monitoring**: Real-time measurement during loading, adjustments made if list develops
    
    **Vertical Weight Distribution Rules:**
    - **Heavy containers (≥25 tonnes)**: First or second tier on deck minimum (lecture: "heavy containers... should be stowed at the first or even the second tier on deck")
    - **Medium containers (15-25 tonnes)**: Mid-tiers
    - **Light containers (<15 tonnes)**: Third tier and above (lecture: "Containers below 15 t should be stowed above the third tier on deck")
    - **Principle**: "The higher the number of tiers, the lighter the containers will be, and the lighter the containers will be as they are away from the centre toward both sides"
    - **Rationale**: Minimises centre of gravity height whilst maintaining transverse stability
    """)
    
    st.markdown('<p class="subsection-header">Principle V2: Stack Weight and Structural Limits</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Beyond overall stability, stowage planners must respect the vessel's structural limits. The hull, deck, 
    and cell guides can only bear certain loads before risking structural damage.
    
    **Stack Weight Limits:**
    - Each vertical stack of containers has a maximum total weight
    - **Lecture explanation**: "In order to avoid the damage of rigid structure of the vessel, each bay of the 
    container vessel is indicated with the maximum permissible weight of each row"
    - Typically 200-300 tonnes per stack (vessel-specific, varies by position)
    - Depends on:
      - Cell guide strength (for below-deck positions)
      - Deck structure strength (for on-deck positions)
      - Hatch cover load capacity (for positions above holds)
    - **Example from lecture**: "The containers carried on the Middle East to India–Pakistan route, and other 
    shipping routes are very heavy, so it is necessary to pay attention to the stack weight of each row in 
    the actual stowage to avoid overweight"
    - **Consequence of violation**: Deformation of cell guides, deck damage, potential collapse of stack
    
    **Hatch Cover Load Capacity:**
    - Hatch covers are the steel plates that seal cargo hold openings
    - Must support weight of containers stacked on deck above the hold
    - **Weaker than solid deck structure** (removable, not part of primary hull)
    - Heavy containers should avoid hatch cover positions when possible
    - Stowage software tracks cumulative weight on each hatch cover section
    
    **Bay Weight Limits:**
    - Maximum total weight per bay (longitudinal section)
    - Prevents excessive bending moments on hull structure
    - Typically 1,000-2,000 tonnes per bay (vessel-specific)
    - Heavy cargo routes require careful distribution across multiple bays
    
    **Deck Load Distribution:**
    - Each deck section has maximum weight capacity per square metre
    - Typically 5-10 tonnes/m² depending on deck strength
    - Heavy containers must be spread across multiple positions
    - Cannot concentrate all heavy containers in one area
    """)
    
    st.markdown('<p class="subsection-header">Principle V3: Lashing and Securing Forces</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Containers on deck must be secured against vessel motion in rough seas. The lecture materials explain: 
    "**Lashing force is for the purpose of reducing or preventing the accidental loss of cargo due to the 
    rocking of the vessel's hull by waves, winds, and other external forces during navigation**."
    
    **Lashing Requirements:**
    - Every on-deck container must be secured with lashing rods and twist-locks
    - **Lashing rods**: Steel rods connecting containers vertically and diagonally
    - **Twist-locks**: Mechanical locks engaging corner castings
    - **Stacking cones**: Position on corner castings to align containers precisely
    
    **Weight-Based Lashing Strategy:**
    - From lecture: "The deck of each vessel must be re-lashed"
    - Heavy containers require more securing (lower centre of gravity but higher inertial forces)
    - Light containers easier to secure but more susceptible to wind forces
    - **Specific guidance**: Already covered in V1 (heavy containers at first/second tier on deck)
    
    **Lateral Forces from Vessel Motion:**
    - Vessel rolls and pitches in waves
    - Containers experience lateral accelerations
    - Higher tiers experience greater forces (longer moment arm from rolling centre)
    - Heavy containers at lower tiers reduce these forces
    - Principle reinforces V1 weight distribution rules
    """)
    
    st.markdown('<p class="subsection-header">Principle V4: Destination Sequence (Port Rotation)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Vessels typically call at 6-10 ports during a single voyage loop. Containers for Port 1 must be accessible 
    before containers for Port 2, otherwise crews must perform **restows**—temporarily removing containers to 
    access those underneath, then replacing them. Restows waste time and money.
    
    **The Destination Sequencing Rule:**
    - **Later ports on bottom/back**: Containers for the last port call go at the bottom of stacks
    - **Earlier ports on top/front**: Containers for the first port call go on top, easily accessible
    - **Segregate by destination**: Group containers by discharge port within each bay
    
    **Example Voyage:**
    Singapore → Hong Kong → Shanghai → Busan → Los Angeles → Oakland → Seattle
    
    **Stowage Strategy:**
    - **Seattle cargo** (last port): Bottom tiers, will remain untouched until final destination
    - **Oakland cargo**: Mid-tiers, accessible after Los Angeles discharge
    - **Los Angeles cargo**: Upper tiers, first US port, easily accessible
    - **Busan cargo** (first discharge): Top tiers, removed first after loading in Singapore
    
    **Re-stow Problem:**
    - If a Los Angeles container is mistakenly placed under Seattle containers, must:
      1. Lift Seattle containers off (1-2 crane moves per container)
      2. Set them aside temporarily on apron
      3. Remove Los Angeles container (1 crane move)
      4. Replace Seattle containers (1-2 crane moves per container)
    - **Cost**: Each re-stow = 3-6 crane moves wasted (time, labour, delay to vessel)
    - **Target**: <2% re-stow rate (ideally zero)
    - **Planning complexity**: For 10,000 containers visiting 8 ports, ensuring zero re-stows is computationally intensive
    """)
    
    st.markdown('<p class="subsection-header">Principle V5: Container Type Compatibility</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Different container types have specific stowage requirements that cannot be violated.
    
    **Dangerous Goods (DG) Segregation:**
    - **Regulatory framework**: IMDG Code (International Maritime Dangerous Goods Code)
    - **Classes must be separated** by minimum horizontal and vertical distances:
      - Class 1 (Explosives) far from Class 3 (Flammable Liquids)
      - Class 8 (Corrosives) far from Class 4 (Flammable Solids)
    - **Some DG cannot go in holds**: Must be on deck with ventilation
    - **Deck restrictions**: Some classes cannot be in accommodation vicinity
    - **Stowage software**: Automatically checks IMDG segregation rules and alerts planner to violations
    
    **Reefer (Refrigerated) Container Stowage:**
    - **Power requirement**: Must be positioned within reach of reefer power outlets
    - **Limited plug positions**: Each bay has finite number of reefer plugs (typically 10-20% of bay capacity)
    - **On-deck reefers**: Easier power access, less interference with cargo operations
    - **Hold reefers**: Require power runs into hold, more complex
    - **Stowage constraint**: Cannot place reefer where no power outlet available
    - **Priority cargo**: Time-sensitive perishables get priority reefer positions
    - **Monitoring**: Temperature monitored continuously throughout voyage
    
    **Out-of-Gauge (OOG) Containers:**
    - **Definition**: Exceed standard container dimensions (overwidth, overheight, overlength)
    - **Cannot stack on top**: Other containers cannot be placed above OOG
    - **Clearance required**: Must not interfere with crane operations or adjacent stacks
    - **Special positions**: Designated OOG positions on deck or holds
    - **Securing**: Often require special lashing equipment and procedures
    
    **Empty Containers:**
    - **Very light**: 2-4 tonnes vs 25-30 tonnes when full
    - **Stowage principle**: Place on top tiers when possible
    - **Rationale**: Lowers centre of gravity (heavy full containers below, light empties above)
    - **Limitation**: Cannot support heavy containers on top
    - **Weight distribution**: Used strategically to balance vessel (fill gaps whilst maintaining stability)
    """)
    
    st.markdown('<p class="subsection-header">The Stowage Planning Process: From Container List to Bay Plan</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Timeline: 48-72 Hours Before Vessel Arrival**
    
    **Step 1: Receive Container Data**
    - Shipping line/terminal provides complete export container list
    - Data includes:
      - Container number, size (20ft/40ft/45ft), type (dry/reefer/OOG/DG)
      - Weight (verified gross mass per SOLAS VGM)
      - Destination port
      - Special requirements (DG class, temperature settings, OOG dimensions)
      - Customer, booking reference
    
    **Step 2: Understand Vessel Configuration**
    - Vessel's bay plan template (which bays exist, how many tiers per bay)
    - Reefer plug locations and quantities per bay
    - Weight limits: Stack weight, bay weight, hatch cover limits
    - Current cargo onboard (if mid-voyage, what remains from previous ports)
    - Stability parameters: Required GM range, trim limits
    
    **Step 3: Group and Sort Containers**
    - **By destination port**: Essential for sequencing
    - **By size**: 20ft vs 40ft containers go in different bay positions
    - **By type**: Separate dry, reefer, OOG, dangerous goods
    - **By weight class**: Heavy (>25t), medium (15-25t), light (<15t)
    - **Priority categories**: Time-sensitive cargo, high-value cargo
    
    **Step 4: Initial Allocation (First Pass)**
    - **Destination-based**: Assign containers to bays based on port rotation
      - Last port discharge → bottom tiers/aft bays
      - First port discharge → top tiers/forward bays
    - **Weight-based**: Heavy containers to lower tiers, light to upper tiers
    - **Reefers**: Allocate to bays with available power outlets
    - **Dangerous goods**: Position per IMDG Code segregation rules
    - **OOG**: Assign to designated OOG positions
    
    **Step 5: Check Stability and Structural Limits**
    - **Load computer calculates**:
      - Centre of gravity height (G)
      - Metacentric height (GM)
      - Trim (longitudinal balance)
      - List (transverse balance)
      - Stack weights for each position
      - Bay weights
      - Hatch cover loads
    - **Identify violations**: Any parameter outside safe limits?
    - **Common issues**:
      - GM too low (too many heavy containers on deck)
      - Excessive list (unbalanced port/starboard)
      - Stack weight exceeded (too many heavy containers in one stack)
    
    **Step 6: Optimise and Adjust**
    - **If violations found**: Move containers to different positions
      - Move heavy containers from upper to lower tiers (increase GM)
      - Shift containers port/starboard to balance list
      - Redistribute weight between bays to balance trim
    - **Optimise crane operations**:
      - Minimise crane travel distance between picks
      - Complete bays sequentially when possible
      - Balance workload across multiple cranes (if 4-6 cranes working simultaneously)
    - **Iterative process**: May require multiple adjustments to satisfy all constraints
    
    **Step 7: Generate Final Bay Plans and Loading Sequence**
    - **Bay plans**: Detailed diagrams showing every container's Bay-Row-Tier position
    - **Loading sequence**: Order in which containers should be loaded
      - Consider: What's in yard, where it's located, crane efficiency
    - **Crane work assignment**: Which crane loads which containers (balancing workload)
    - **Special instructions**:
      - Dangerous goods handling procedures
      - Reefer connection requirements
      - OOG securing instructions
    - **Stability report**: Confirming all stability parameters within safe limits
    
    **Step 8: Execute and Monitor**
    - Bay plans sent to vessel and terminal 24 hours before arrival
    - Crane operators follow loading sequence precisely
    - **Real-time monitoring**: Check stability as loading progresses
    - **Deviations**: If plan changes (late cargo, damaged cargo), must recalculate stability
    - **Final verification**: Confirm actual loading matches plan, vessel stable for departure
    """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🎯 The Complexity of Modern Stowage Planning:</strong><br><br>
    <strong>Scale</strong>: Mega vessel with 20,000 TEU capacity calling at 8 ports = positioning 20,000 containers 
    across 150+ bays with 10+ tiers each whilst satisfying stability, structural, destination, and compatibility 
    constraints.<br><br>
    <strong>Constraints</strong>: Approximately 50-100 different rules and limits must be checked for each 
    container position (weight limits, stability, segregation, power availability, etc.).<br><br>
    <strong>Combinations</strong>: Theoretical number of possible arrangements is astronomical (billions of billions). 
    Finding optimal solution is NP-hard computational problem.<br><br>
    <strong>Time pressure</strong>: Plan must be completed 24-48 hours before arrival. No time for extensive manual 
    trial-and-error.<br><br>
    <strong>Software essential</strong>: Modern stowage planning software uses heuristic algorithms and constraint 
    satisfaction techniques. Even expert planners cannot solve this manually for vessels >5,000 TEU.<br><br>
    <strong>Safety critical</strong>: Errors in stowage planning can cause vessel instability, cargo damage, 
    structural failure, or safety incidents. The stakes are extremely high.<br><br>
    This is why stowage planning is considered one of the most complex operational challenges in container 
    shipping—it combines physics, optimisation, and logistics with significant safety and economic consequences.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 6: Modern Vessel Technology and Trends
    # ============================================================================
    
    st.markdown('<p class="section-header">Modern Vessel Technology and Future Trends</p>', unsafe_allow_html=True)
    
    st.markdown("""
    While vessel sizes have reached practical limits, technology continues evolving to improve efficiency, 
    reduce environmental impact, and enhance operations. Modern container vessels bear little resemblance 
    to the rudimentary Ideal-X of 1956.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Propulsion and Efficiency Technologies:**
        
        **Slow Steaming:**
        - Operate at 18-20 knots instead of 25+ knots
        - **Fuel savings**: 40-50% reduction at 19 knots vs 25 knots
        - **Physics**: Fuel consumption increases with cube of speed
        - **Trade-off**: Longer voyage times, but dramatic cost savings
        - **Enabler**: Larger vessels can maintain schedules at lower speeds
        
        **Hull Design Optimisation:**
        - **Bulbous bow**: Reduces wave-making resistance
        - **Optimised hull form**: Computer-modelled for minimum drag
        - **Hull coatings**: Low-friction coatings reduce resistance
        - **Regular cleaning**: Remove marine growth to maintain efficiency
        
        **Engine Efficiency:**
        - **Two-stroke diesels**: Most efficient marine engines (up to 50% thermal efficiency)
        - **Waste heat recovery**: Generate electricity from exhaust heat
        - **Engine derating**: Operate engines at lower power for better efficiency
        - **Automated control**: Optimise engine operation continuously
        
        **Operational Automation:**
        - **Unmanned engine rooms**: Remote monitoring, no continuous attendance required
        - **Predictive maintenance**: Sensors monitor equipment health, predict failures
        - **Voyage optimisation**: Weather routing software finds most efficient routes
        - **Trim optimisation**: Adjust ballast for optimal hydrodynamic performance
        """)
    
    with col2:
        st.markdown("""
        **Environmental Technologies:**
        
        **Exhaust Gas Cleaning (Scrubbers):**
        - Remove sulphur from exhaust to meet IMO 2020 regulations (<0.5% sulphur)
        - **Wet scrubbers**: Spray water through exhaust, remove sulphur oxides
        - **Dry scrubbers**: Chemical reaction with alkaline materials
        - **Cost**: $3-10 million per vessel, but allows using cheaper heavy fuel oil
        
        **LNG Dual-Fuel Engines:**
        - Can burn LNG (Liquefied Natural Gas) or conventional fuel
        - **Benefits**: 20% less CO₂, 85% less NOx, 99% less SOx and particulates
        - **Challenge**: LNG bunkering infrastructure still limited globally
        - **Examples**: CMA CGM's 23,000 TEU LNG-powered vessels (9 ships ordered)
        
        **Alternative Fuels (Future):**
        - **Methanol**: Several vessels ordered with methanol capability
        - **Ammonia**: Zero-carbon fuel, under development for marine use
        - **Hydrogen**: Potential long-term solution, significant technical challenges
        - **Biofuels**: Drop-in replacement for conventional fuel, limited availability
        
        **Shore Power (Cold Ironing):**
        - Plug into port electrical grid whilst at berth
        - **Zero emissions** whilst in port (no diesel generator running)
        - Requires port infrastructure investment
        - Increasingly mandated in environmental regulations
        """)
    
    st.markdown("""
    **Digital and Operational Technologies:**
    
    **Automated Stowage Planning:**
    - AI-powered software generates optimised stowage plans
    - Considers thousands of constraints simultaneously
    - Learns from historical data to improve recommendations
    - Reduces planning time from days to hours for complex vessels
    
    **Container Tracking and Monitoring:**
    - IoT sensors in containers track:
      - GPS location
      - Temperature (for reefers)
      - Shock/impact (for fragile cargo)
      - Door opening (security)
    - Real-time visibility throughout supply chain
    - Predictive arrival times based on actual vessel position
    
    **Reefer Container Remote Monitoring:**
    - Every reefer monitored continuously from vessel and shore
    - Automatic alerts if temperature deviates from setpoint
    - Remote adjustments possible
    - Reduces cargo loss from temperature failures
    
    **Load Computers and Stability Monitoring:**
    - Real-time stability calculations during loading
    - Immediate alerts if parameters approach limits
    - Integration with stowage plan for verification
    - Prevents loading errors that could compromise stability
    """)
    
    # ============================================================================
    # SECTION 7: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways: Container Vessels & Evolution</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Vessel Anatomy Fundamentals:**
        - **Directional**: Bow (front), Stern (back), Port (left), Starboard (right)
        - **Vertical**: Deck (above), Hold (below), Hatch (opening), Superstructure (accommodation)
        - **Container-specific**: Bay-Row-Tier coordinate system for precise 3D positioning
        - **Cell guides**: Keith Tantlinger's innovation holding containers secure in holds
        
        **Dramatic Evolution:**
        - **1956**: Ideal-X (500 TEU, 6 across) - First container vessel
        - **2020**: HMM Algeciras (23,964 TEU, 24 across) - Current largest
        - **Growth**: 50× capacity increase in 64 years
        - **Phases**: Pioneer → Panamax → Post-Panamax → ULCS
        - **Driver**: Powerful economics of scale (82% cost reduction per TEU)
        
        **Vessel Classifications:**
        - **Feeder**: <1,000 TEU (short-sea, coastal)
        - **Feedermax**: 1,000-3,000 TEU (regional distribution)
        - **Panamax**: 3,000-5,000 TEU (old Panama Canal, retired 2016)
        - **Post-Panamax**: 5,000-10,000 TEU (major trade lanes)
        - **New-Panamax**: 10,000-14,500 TEU (new Panama Canal 2016+)
        - **VLCS**: 10,000-18,000 TEU (Very Large Container Ships)
        - **ULCS**: 18,000-25,000 TEU (Ultra Large, mega vessels)
        """)
    
    with col2:
        st.markdown("""
        **Economics of Scale:**
        - **Fixed costs**: Crew, insurance, administration don't scale with size
        - **Variable costs**: Fuel, capital scale less than proportionally
        - **Result**: 18,000 TEU vessel = 82% lower cost per TEU vs 1,000 TEU
        - **Requirement**: High utilisation (85-90%+), high-volume routes
        - **Trade-off**: Fewer ports accessible, concentration risk
        
        **Stowage Planning Complexity:**
        - **V1: Stability**: Low centre of gravity, balanced port/starboard and bow/stern
        - **V2: Structural limits**: Stack weight, bay weight, hatch cover capacity
        - **V3: Lashing**: Secure on-deck containers against vessel motion
        - **V4: Destination sequence**: Later ports bottom, earlier ports top
        - **V5: Container compatibility**: DG segregation, reefer power, OOG clearance
        - **Challenge**: 20,000 containers × 8 ports × 100+ constraints = NP-hard problem
        - **Solution**: Advanced software using heuristic optimisation algorithms
        
        **Modern Technology Trends:**
        - **Efficiency**: Slow steaming, optimised hulls, waste heat recovery
        - **Environmental**: Scrubbers, LNG dual-fuel, shore power, alternative fuels
        - **Digital**: Automated stowage planning, IoT tracking, predictive maintenance
        - **Future**: Approaching size limits, focus shifting to efficiency and sustainability
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Container vessels have grown 50× in capacity since 1956 (500 → 24,000 TEU), 
    driven by powerful economies of scale that reduce cost per container by 82%. Vessels are classified by size 
    (Feeder through ULCS) with classifications defined by canal constraints (Panama, Suez) and port infrastructure 
    limits. Modern mega vessels (20,000+ TEU) can only call at 20-30 elite hub ports globally. Stowage planning 
    is an extraordinarily complex optimisation problem balancing vessel stability (weight distribution, GM, trim, 
    list), structural limits (stack weight, bay limits), destination sequencing (avoiding restows), and container 
    compatibility (dangerous goods, reefers, OOG). Advanced software is essential for vessels >5,000 TEU. Future 
    trends focus on efficiency improvements (slow steaming, hull optimisation) and environmental sustainability 
    (LNG, methanol, shore power) rather than further size increases, as vessels have reached practical maximum 
    capacity given infrastructure constraints. Understanding vessel evolution, classification, economics, and 
    stowage principles is fundamental to comprehending modern container terminal operations.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** 🌍 Global Shipping & Alliances - Explore how shipping lines have consolidated into three 
    mega-alliances (2M, Ocean Alliance, THE Alliance) controlling 80%+ of global capacity, vessel sharing 
    agreements, hub-and-spoke network structures, and how global connectivity is achieved through strategic 
    partnerships and port-to-port service strings.
    """)
