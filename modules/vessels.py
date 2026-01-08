import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">🚢 Container Vessels & Evolution</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand container vessel anatomy, the dramatic evolution in vessel sizes, vessel classification 
    systems, and the principles of vessel stowage planning.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Container Vessel Anatomy
    # ============================================================================
    
    st.markdown('<p class="section-header">Container Vessel Anatomy</p>', unsafe_allow_html=True)
    
    st.markdown("""
    A container vessel is a highly specialized cargo ship designed specifically to carry standardized 
    containers. Understanding vessel anatomy is essential for comprehending port operations.
    """)
    
    st.markdown('<p class="subsection-header">Key Vessel Components</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Main Structure:**
        - **Bow**: Front of the vessel (pointed end)
        - **Stern**: Rear of the vessel (back end)
        - **Port Side**: Left side when facing forward
        - **Starboard Side**: Right side when facing forward
        - **Hull**: Main body of the ship
        - **Deck**: Top surface of the ship
        
        **Cargo Areas:**
        - **Holds**: Below-deck cargo spaces (inside the ship)
        - **Hatch Covers**: Large steel covers over holds
        - **Cell Guides**: Vertical guide rails in holds to stack containers
        - **On-Deck Stacks**: Containers stacked on top of deck
        """)
    
    with col2:
        st.markdown("""
        **Operational Areas:**
        - **Bridge (Castle)**: Navigation and control center
        - **Accommodation**: Living quarters for crew
        - **Engine Room**: Propulsion and power systems
        - **Ballast Tanks**: For vessel stability control
        
        **Container-Specific Features:**
        - **Reefer Plugs**: Power outlets for refrigerated containers
        - **Lashing Bridges**: Walkways for securing deck containers
        - **Twist Locks**: Devices securing containers to deck/each other
        - **Container Ducts**: Ventilation for refrigerated containers
        """)
    
    st.markdown('<p class="subsection-header">Vessel Dimensions</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Key measurements that determine where a vessel can operate:
    
    - **LOA (Length Overall)**: Total length from bow to stern (e.g., 400 meters for ULCV)
    - **Beam**: Width of the vessel at widest point (e.g., 59 meters for ULCV)
    - **Draft**: Depth of vessel below waterline when loaded (e.g., 16 meters)
    - **Air Draft**: Height from waterline to highest point (determines bridge clearance)
    - **TEU Capacity**: Number of TEU slots available (e.g., 24,000 TEU)
    - **Containers Across**: How many containers wide (e.g., 24 across for MGX-24)
    """)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ Port Infrastructure Requirements:</strong> A vessel's dimensions determine which ports 
    it can visit:
    - **Draft** requires deep-water berths (16m+ for mega vessels)
    - **Beam** determines berth width and crane reach requirements
    - **LOA** determines minimum berth length
    - **Containers across** determines required crane outreach
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 2: Rows, Bays, and Tiers on Vessels
    # ============================================================================
    
    st.markdown('<p class="section-header">Container Positioning: Bays, Rows & Tiers</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Containers on vessels are organized in a three-dimensional grid system for precise positioning.
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Bays (Longitudinal)**
        - Front (bow) to back (stern)
        - Odd numbers: 01, 03, 05...
        - For 20 ft container positions
        - Even numbers: 02, 04, 06...
        - For 40 ft container positions
        - Example: Bay 01 = front, Bay 20 = middle, Bay 40 = stern
        """)
    
    with col2:
        st.markdown("""
        **Rows (Transverse)**
        - Port (left) to starboard (right)
        - 00 or 01 at centerline
        - Odd numbers on port side
        - Even numbers on starboard side
        - Example: Rows 01, 03, 05 (port)
        - Rows 02, 04, 06 (starboard)
        - Modern vessels: up to 24 rows across
        """)
    
    with col3:
        st.markdown("""
        **Tiers (Vertical)**
        - Bottom to top stacking
        - Below deck: 02, 04, 06, 08...
        - On deck: 82, 84, 86, 88...
        - 80+ indicates above deck
        - Example: Tier 02 = bottom hold
        - Tier 06 = 3rd level in hold
        - Tier 86 = 3rd level on deck
        """)
    
    st.markdown("""
    **Example Container Position: 180684**
    - **Bay 18**: Middle section of ship
    - **Row 06**: Starboard side, 3rd position from center
    - **Tier 84**: Second tier on deck (above deck level)
    """)
    
    # ============================================================================
    # SECTION 3: Vessel Size Evolution
    # ============================================================================
    
    st.markdown('<p class="section-header">The Evolution of Container Vessel Sizes</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Over the past 70 years, container vessels have grown dramatically in size, driven by economies of scale. 
    This evolution has fundamentally changed port infrastructure requirements and global shipping economics.
    """)
    
    # Detailed vessel evolution table
    vessel_evolution = pd.DataFrame({
        'Era': ['1956', '1970', '1980', '1985', '1988', '2000', '2006', '2013', '2014', '2019'],
        'Class': ['Early Container', 'Fully Cellular', 'Panamax', 'Panamax Max', 'Post-Panamax I', 
                  'Post-Panamax II', 'VLCS', 'ULCS', 'New-Panamax', 'MGX-24'],
        'TEU Capacity': [500, 1500, 3200, 4000, 5000, 7500, 13000, 19500, 12500, 23000],
        'Containers Across': [6, 8, 10, 10, 13, 16, 19, 22, 20, 24],
        'Typical Draft (m)': [9, 9, 10, 10, 12, 14, 15, 16, 15, 16],
        'Key Milestone': [
            'First container ship (Ideal X)',
            'Purpose-built cellular design',
            'Panama Canal size limit',
            'Maximum Panamax dimensions',
            'Exceeded Panama Canal width',
            'Exceeded Panama limits significantly',
            'Very Large Container Ship',
            'Ultra Large Container Ship',
            'Panama Canal expansion',
            'Maximum practical size today'
        ]
    })
    
    st.dataframe(vessel_evolution, width='stretch', hide_index=True)
    
    # Vessel size growth chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=vessel_evolution['Era'],
        y=vessel_evolution['TEU Capacity'],
        mode='lines+markers',
        line=dict(color='#3B82F6', width=4),
        marker=dict(size=14, color='#2563EB', line=dict(color='white', width=2)),
        name='TEU Capacity',
        text=[f"{teu:,} TEU" for teu in vessel_evolution['TEU Capacity']],
        textposition='top center',
        textfont=dict(size=10)
    ))
    
    fig.update_layout(
        title={
            'text': '70 Years of Vessel Evolution: 500 TEU → 25,000 TEU',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#1F2937'}
        },
        xaxis_title="Year / Era",
        yaxis_title="Container Capacity (TEU)",
        height=500,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='#E5E7EB'),
        showlegend=False,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, width='stretch')
    
    # ============================================================================
    # SECTION 4: Vessel Classifications
    # ============================================================================
    
    st.markdown('<p class="section-header">Vessel Classification Categories</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">Feeder Vessels (100-3,000 TEU)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Purpose:** Short-sea shipping, connecting smaller ports to major hub ports
    
    **Characteristics:**
    - Small to medium size (typically 500-2,500 TEU)
    - Can access smaller, shallower ports
    - Flexible and agile operations
    - Lower draft requirements (8-10 meters)
    - Operate regional routes (e.g., within Southeast Asia)
    
    **Typical Routes:**
    - Singapore ↔ Jakarta
    - Singapore ↔ Manila
    - Hong Kong ↔ Taiwan
    
    **Role in Network:** Collect cargo from smaller ports and bring to major hubs (hub-and-spoke system)
    """)
    
    st.markdown('<p class="subsection-header">Panamax (3,000-5,000 TEU)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Purpose:** Named after Panama Canal—sized to fit through the original canal locks
    
    **Characteristics:**
    - Length: ~294 meters (max for old Panama Canal locks)
    - Beam: ~32 meters (max width for canal)
    - Draft: ~12 meters
    - 10-13 containers across deck
    - Capacity: 3,000-5,000 TEU
    
    **Historical Significance:**
    - Dominated global shipping from 1980s-2000s
    - Panama Canal dictated maximum practical vessel size
    - Optimized for trans-Pacific and trans-Atlantic routes
    
    **Current Status:** Still widely used, but being superseded by larger vessels on major routes
    """)
    
    st.markdown('<p class="subsection-header">Post-Panamax (5,000-10,000 TEU)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Purpose:** Exceeded Panama Canal limits to achieve greater economies of scale
    
    **Characteristics:**
    - Too wide for original Panama Canal
    - Beam: 32-45 meters
    - 13-18 containers across
    - Draft: 12-14 meters
    - Capacity: 5,000-10,000 TEU
    
    **Impact:**
    - Required ports to invest in longer-reach cranes
    - Could not use Panama Canal (until 2016 expansion)
    - Forced route planning around Cape Horn or Suez Canal
    - Became standard for Asia-Europe routes
    """)
    
    st.markdown('<p class="subsection-header">New-Panamax (10,000-14,500 TEU)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Purpose:** Sized for the expanded Panama Canal (opened 2016)
    
    **Characteristics:**
    - Length: ~366 meters (new canal lock maximum)
    - Beam: ~49 meters (new canal maximum)
    - Draft: ~15 meters
    - 20 containers across
    - Capacity: 12,000-14,500 TEU
    
    **Significance:**
    - Represents the "new standard" for trans-Pacific routes
    - Can use expanded Panama Canal
    - More economical than Post-Panamax but not as extreme as ULCV
    """)
    
    st.markdown('<p class="subsection-header">VLCS - Very Large Container Ships (10,000-18,000 TEU)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Purpose:** Mega-vessels for high-volume routes (primarily Asia-Europe)
    
    **Characteristics:**
    - Length: 350-400 meters
    - Beam: 48-56 meters
    - 19-21 containers across
    - Draft: 14-16 meters
    - Capacity: 11,000-18,000 TEU
    
    **Requirements:**
    - Deep-water berths (15+ meters)
    - Super-post-Panamax cranes (70+ meter outreach)
    - Extended berth length (400+ meters)
    - High crane productivity requirements
    """)
    
    st.markdown('<p class="subsection-header">ULCS - Ultra Large Container Ships (18,000-25,000 TEU)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Purpose:** Maximum economies of scale for ultra-high-volume routes
    
    **Characteristics:**
    - Length: 400+ meters (longer than 4 football fields)
    - Beam: 59+ meters
    - 22-24 containers across (record: 24 across on MGX-24 class)
    - Draft: 16+ meters
    - Capacity: 18,000-25,000 TEU
    - Can carry over 200,000 tons of cargo
    
    **Notable Examples:**
    - MSC Gülsün: 23,756 TEU
    - HMM Algeciras: 23,964 TEU
    - Ever Ace: 23,992 TEU
    - MSC Irina: 24,346 TEU (largest as of 2023)
    
    **Extreme Requirements:**
    - Only a handful of ports worldwide can accommodate
    - Requires 65+ meter crane outreach
    - Needs 16+ meter draft berths
    - 8-12 cranes working simultaneously for efficiency
    - Port call duration: 24-48 hours even with optimal operations
    """)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ Operational Challenges of Mega Vessels:</strong><br>
    - <strong>Limited port access</strong>: Only 20-30 ports globally can handle 20,000+ TEU vessels<br>
    - <strong>Concentration risk</strong>: One vessel carries cargo worth $500 million+<br>
    - <strong>Slower port rotations</strong>: Fewer port calls per voyage<br>
    - <strong>Canal restrictions</strong>: Cannot use Panama Canal (too wide)<br>
    - <strong>Weather sensitivity</strong>: More affected by wind due to high stacks<br>
    - <strong>Single point of failure</strong>: Breakdown affects thousands of containers
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 5: Maritime Economics of Scale
    # ============================================================================
    
    st.markdown('<p class="section-header">Maritime Economics of Scale</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The dramatic growth in vessel size is driven by **economies of scale**: larger vessels have 
    significantly lower cost per TEU transported.
    """)
    
    # Cost per TEU analysis
    cost_analysis = pd.DataFrame({
        'Vessel Size': ['Feeder\n1,000 TEU', 'Panamax\n5,000 TEU', 'Post-Panamax\n10,000 TEU', 
                       'VLCS\n15,000 TEU', 'ULCS\n20,000 TEU', 'ULCS\n24,000 TEU'],
        'Relative Cost per TEU': [100, 50, 32, 24, 20, 18],
        'Crew Size': [15, 20, 22, 23, 24, 25],
        'Fuel per TEU (Index)': [100, 55, 38, 30, 26, 24]
    })
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=cost_analysis['Vessel Size'],
        y=cost_analysis['Relative Cost per TEU'],
        marker=dict(
            color=['#EF4444', '#F59E0B', '#3B82F6', '#10B981', '#059669', '#047857'],
            line=dict(color='#1F2937', width=2)
        ),
        text=cost_analysis['Relative Cost per TEU'],
        textposition='outside',
        name='Cost per TEU (Indexed to 100)'
    ))
    
    fig.update_layout(
        title={
            'text': 'Economies of Scale: Cost per TEU Decreases with Vessel Size',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        yaxis_title="Relative Cost per TEU (Indexed)",
        xaxis_title="Vessel Type & Capacity",
        height=450,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='#E5E7EB', range=[0, 120]),
        showlegend=False
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    **Why Larger = Cheaper:**
    
    1. **Crew Costs:** A 24,000 TEU vessel needs only 25 crew vs 15 for 1,000 TEU vessel
       - Per TEU crew cost: 24x larger vessel, only 1.7x more crew
    
    2. **Fuel Efficiency:** Fuel consumption doesn't scale linearly with capacity
       - Doubling capacity increases fuel use by only ~50%
    
    3. **Port Costs:** Some port fees are per-vessel, not per-container
       - Larger vessel spreads fixed costs over more TEU
    
    4. **Capital Costs:** Building a 20,000 TEU vessel doesn't cost 20x a 1,000 TEU vessel
       - Capital cost per TEU slot decreases with size
    """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>💡 The Catch:</strong> While larger vessels have lower cost per TEU, they require:
    - Massive capital investment upfront (€150-200 million per vessel)
    - Specialized port infrastructure at every port of call
    - Consistent high-volume cargo to fill the capacity
    - Longer time in port (even with many cranes)
    
    This is why only major shipping alliances can effectively operate these mega vessels on high-volume 
    routes like Asia-Europe.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 6: Vessel Stowage Principles
    # ============================================================================
    
    st.markdown('<p class="section-header">Vessel Stowage Planning Principles</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Stowage planning** is the process of determining exactly where each container should be positioned 
    on a vessel. This is a complex optimization problem balancing multiple constraints.
    """)
    
    st.markdown('<p class="subsection-header">Key Stowage Constraints</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **1. Vessel Stability**
        - Must maintain proper center of gravity
        - Weight distribution fore/aft (longitudinal)
        - Weight distribution port/starboard (transverse)
        - Metacentric height (stability measure)
        - Prevents vessel from listing or being unstable
        
        **2. Structural Limits**
        - **Stack weight limits**: Maximum weight per bay
        - **Deck load limits**: Weight capacity of each deck section
        - **Hatch cover strength**: Limits on containers above holds
        - Heavy containers on bottom, lighter on top
        
        **3. Destination Sequence**
        - Containers for later ports on bottom/back
        - Containers for next port on top/accessible
        - Minimize "re-handles" (moving containers to access others)
        - "Last in, first out" principle where possible
        """)
    
    with col2:
        st.markdown("""
        **4. Container Compatibility**
        - **Dangerous Goods (DG)**: Segregation requirements
        - **Reefers**: Must be near power outlets
        - **OOG (Out of Gauge)**: Cannot stack containers on top
        - **Empty vs Full**: Empties typically on top
        - **Heavy vs Light**: Weight distribution
        
        **5. Operational Efficiency**
        - **Crane productivity**: Minimize crane moves
        - **Tight connections**: Priority containers for time-sensitive cargo
        - **Bay planning**: Complete bays for faster operations
        - **Minimize shifting**: Avoid moving same container multiple times
        
        **6. Special Requirements**
        - Away from boiler (AFB) for heat-sensitive cargo
        - Cargo requiring special ventilation
        - High-value cargo in secure locations
        - Customs/inspection requirements
        """)
    
    st.markdown('<p class="subsection-header">Stowage Planning Process</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Step 1: Information Collection (72 hours before arrival)**
    - Shipping line provides vessel details via PORTNET
    - Container list with: size, weight, type, destination, special requirements
    - Vessel stowage plan from previous port
    - Discharge and loading lists
    
    **Step 2: Discharge Planning**
    - Determine which containers to remove
    - Sequence to minimize re-handles
    - Assign to specific quay cranes
    
    **Step 3: Loading Planning**
    - Allocate each export container to specific bay-row-tier position
    - Optimize for stability, destination sequence, and constraints
    - Generate loading sequence for crane operators
    
    **Step 4: Verification & Review**
    - Check all stability calculations
    - Verify all constraints satisfied
    - Confirm dangerous goods segregation
    - Review for operational efficiency
    
    **Step 5: Execution**
    - Real-time adjustments as needed
    - Handle no-shows or last-minute changes
    - Confirm final stowage matches plan
    """)
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 Intelligent Stowage Systems:</strong> Modern terminals use AI-powered stowage planning systems 
    that can:
    - Plan 1,000+ container positions in minutes (vs hours manually)
    - Automatically satisfy all constraints
    - Optimize for multiple objectives simultaneously
    - Adapt in real-time to changes
    - Learn from past stowage plans to improve
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 7: Vessel Technology Evolution
    # ============================================================================
    
    st.markdown('<p class="section-header">Vessel Technology Evolution</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Modern container vessels have evolved in three major areas beyond just size:
    """)
    
    st.markdown('<p class="subsection-header">1. Growth in Size</p>', unsafe_allow_html=True)
    st.markdown("""
    - 500 TEU (1956) → 25,000 TEU (2024)
    - Driven by economies of scale
    - Created infrastructure arms race for ports
    """)
    
    st.markdown('<p class="subsection-header">2. Increasing Specialization</p>', unsafe_allow_html=True)
    st.markdown("""
    - **Pure car/truck carriers (PCTC)**: Dedicated to vehicles
    - **Heavy-lift vessels**: For industrial equipment
    - **Reefer-optimized vessels**: More reefer plugs for perishables
    - **LNG dual-fuel vessels**: Can run on liquefied natural gas
    - **Fast container vessels**: Trade fuel for speed on premium routes
    """)
    
    st.markdown('<p class="subsection-header">3. Environmental Impact Reduction</p>', unsafe_allow_html=True)
    st.markdown("""
    **Regulatory Drivers:**
    - IMO 2020: Low sulfur fuel requirements
    - IMO 2030: 40% carbon intensity reduction target
    - IMO 2050: Net-zero emissions target
    
    **Technology Solutions:**
    - **LNG propulsion**: 20-25% CO2 reduction vs conventional fuel
    - **Scrubbers**: Clean exhaust gases to meet sulfur limits
    - **Hull optimization**: Improved hydrodynamics for fuel efficiency
    - **Slow steaming**: Reduced speed saves fuel (but increases transit time)
    - **Wind assistance**: Modern sail technology (Flettner rotors, kites)
    - **Shore power**: Plug into grid electricity while in port
    - **Alternative fuels (future)**: Methanol, ammonia, hydrogen
    """)
    
    # ============================================================================
    # SECTION 8: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Vessel Anatomy:**
        - Bow (front), Stern (back), Port (left), Starboard (right)
        - Holds (below deck), On-deck stacks
        - Bay-Row-Tier 3D coordinate system
        - LOA, Beam, Draft determine port accessibility
        
        **Vessel Evolution:**
        - 500 TEU (1956) → 25,000 TEU (2024)
        - Driven by economies of scale
        - Cost per TEU: 80% reduction from Feeder to ULCV
        
        **Vessel Classifications:**
        - Feeder (100-3,000 TEU): Regional routes
        - Panamax (3,000-5,000 TEU): Original canal size
        - Post-Panamax (5,000-10,000 TEU): Exceeded canal
        - New-Panamax (10,000-14,500 TEU): Expanded canal
        - VLCS (10,000-18,000 TEU): Very large ships
        - ULCS (18,000-25,000 TEU): Ultra large ships
        """)
    
    with col2:
        st.markdown("""
        **Economics of Scale:**
        - Larger vessels = lower cost per TEU
        - But require massive infrastructure investment
        - Only viable on high-volume routes
        - Limited number of ports can handle ULCV
        
        **Stowage Planning:**
        - Must balance stability, destination, weight, special cargo
        - Complex optimization problem
        - 72-hour planning window
        - AI systems now standard for efficiency
        
        **Technology Trends:**
        - Environmental regulations driving innovation
        - LNG, scrubbers, alternative fuels
        - Increasing specialization
        - Digital systems integration
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Container vessels have grown from 500 TEU to 25,000 TEU in 70 years, 
    driven by dramatic economies of scale. However, these mega vessels require specialized ports with 
    deep-water berths, super-sized cranes, and sophisticated planning systems. Only ports that can meet 
    these requirements remain competitive in the global container shipping network.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** 🌍 Global Shipping & Alliances - Understand how shipping lines have consolidated into 
    mega alliances controlling 83% of global container volumes, and how this shapes the competitive landscape.
    """)
