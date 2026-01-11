import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">🚢 Vessels & Evolution</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand vessel anatomy, the dramatic evolution in vessel sizes over decades, classification systems, 
    and the principles of vessel stowage planning.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Vessel Anatomy and Terminology
    # ============================================================================
    
    st.markdown('<p class="section-header">Vessel Anatomy and Maritime Terminology</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Before diving into vessel evolution, let's understand basic vessel anatomy and the terminology used 
    throughout the maritime industry.
    """)
    
    st.markdown('<p class="subsection-header">Basic Vessel Directions and Parts</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Directional Terms:**
        - **Bow (Forward)**: Front of the ship
        - **Stern (Aft)**: Back of the ship
        - **Port**: Left side (facing forward)
        - **Starboard**: Right side (facing forward)
        - **Amidships**: Middle section
        
        **Vertical Terms:**
        - **Deck**: Horizontal platform/floor
        - **Hold**: Cargo space below deck
        - **Hatch**: Opening in deck to access hold
        - **Superstructure**: Buildings above main deck
        """)
    
    with col2:
        st.markdown("""
        **Key Vessel Sections:**
        - **Bridge**: Command centre, usually at stern
        - **Accommodation**: Living quarters for crew
        - **Engine Room**: Contains propulsion machinery
        - **Cargo Holds**: Below-deck storage areas
        - **Weather Deck**: Topmost deck exposed to elements
        
        **Container-Specific:**
        - **Bay**: Vertical slice (lengthwise division)
        - **Row**: Horizontal position (across width)
        - **Tier**: Vertical stacking position (height)
        """)
    
    st.markdown('<p class="subsection-header">Container Positioning System on Vessels</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Every container on a vessel has a precise three-dimensional address using the **Bay-Row-Tier** system:
    
    **Bay (Longitudinal Position):**
    - Numbered from bow (front) to stern (back)
    - Odd numbers: 20-foot container positions (01, 03, 05, 07...)
    - Even numbers: 40-foot container positions (02, 04, 06, 08...)
    - A 40-foot container occupies two 20-foot bays
    
    **Row (Transverse Position):**
    - Numbered from port (left) to starboard (right)
    - Usually 00-24 (depends on vessel width)
    - 00 is centre-line, odd numbers port side, even numbers starboard side
    
    **Tier (Vertical Position):**
    - Numbered from bottom to top
    - Below deck: 02, 04, 06, 08... (even numbers, working down from deck)
    - On deck: 82, 84, 86, 88... (even numbers above 80, working up from deck)
    - Deck level itself is typically 80
    
    **Example:** Container at position **Bay 12, Row 04, Tier 86** is:
    - 12th bay from bow (40-foot position)
    - 4th row from port side (starboard side)
    - 3 tiers above deck level
    """)
    
    # ============================================================================
    # SECTION 2: Vessel Size Evolution
    # ============================================================================
    
    st.markdown('<p class="section-header">The Dramatic Evolution of Container Vessel Sizes</p>', unsafe_allow_html=True)
    
    st.markdown("""
    One of the most striking transformations in maritime history is the growth in container vessel sizes. 
    In just 60 years, vessels have grown **50 times** in capacity.
    """)
    
    # Vessel evolution data - based on lecture timeline
    vessel_evolution = pd.DataFrame({
        'Year': [1956, 1970, 1980, 1988, 2000, 2006, 2013, 2019],
        'Category': [
            'Early Container Ships',
            'Fully Cellular',
            'Panamax',
            'Post-Panamax I',
            'Post-Panamax II',
            'VLCS',
            'ULCS',
            'MGX-24'
        ],
        'Capacity Range (TEU)': ['500-800', '1,000-2,500', '3,000-3,400', '4,000-6,000', '6,000-8,500', '11,000-15,000', '18,000-21,000', '21,000-25,000'],
        'Typical Dimensions': [
            '137×17×9m',
            '200×20×9m',
            '250×32×12.5m',
            'Post-Panama width',
            'Wider beam',
            'Up to 400m length',
            '400m+ length',
            '400m+ length'
        ],
        'Containers Across': ['6', '8-10', '13', '13+', 'Wider', 'Up to 22', '23', '24']
    })
    
    st.dataframe(vessel_evolution, width='stretch', hide_index=True)
    
    # Capacity growth visualisation
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=vessel_evolution['Year'],
        y=[650, 1750, 3200, 5000, 7250, 13000, 19500, 23000],  # Midpoints of ranges
        mode='lines+markers',
        name='TEU Capacity',
        line=dict(color='#3B82F6', width=4),
        marker=dict(size=12, color='#2563EB', line=dict(color='white', width=2)),
        text=vessel_evolution['Category'],
        hovertemplate='<b>%{text}</b><br>Year: %{x}<br>Capacity: ~%{y:,} TEU<extra></extra>'
    ))
    
    fig.update_layout(
        title={
            'text': 'Container Vessel Capacity Growth: 1956 → 2019',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#1F2937'}
        },
        xaxis_title="Year",
        yaxis_title="Capacity (TEU)",
        height=500,
        plot_bgcolor='white',
        xaxis=dict(gridcolor='#E5E7EB'),
        yaxis=dict(gridcolor='#E5E7EB', range=[0, 25000])
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    **Key Observations:**
    
    **1956-1980s: Early Growth**
    - Modest increases from 500 to 3,000 TEU
    - Vessels constrained by port infrastructure and canal widths
    - Focus on proving containerisation concept
    
    **1988: Panamax Limit**
    - ~4,500 TEU defined by Panama Canal dimensions
    - Maximum width: 32.3 metres (106 feet)
    - Standard for two decades
    
    **1996-2006: Breaking Through**
    - Post-Panamax vessels exceed canal limits
    - 6,500 → 15,000 TEU in just 10 years
    - New-Panamax canal expansion announced
    
    **2013-2019: Mega Vessel Era**
    - Ultra Large Container Ships (ULCS) reach 23,000+ TEU
    - 24 containers across width
    - Approaching practical limits (port depth, crane reach, structural integrity)
    """)
    
    st.markdown("""
    <div class="info-box">
    <strong>💡 Why Did Vessels Grow So Large?</strong><br>
    - <strong>Economies of Scale</strong>: Bigger vessels reduce cost per container:<br>
    - <strong>Crew costs</strong>: Similar crew size regardless of vessel capacity<br>
    - <strong>Fuel efficiency</strong>: Larger vessels more fuel-efficient per container<br>
    - <strong>Capital costs</strong>: Building costs don't scale linearly with size<br>
    - <strong>Port fees</strong>: Fixed port charges spread over more containers<br><br>
    <strong>Result</strong>: Larger vessels achieve significantly lower costs per TEU transported
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 3: Vessel Classification Systems
    # ============================================================================
    
    st.markdown('<p class="section-header">Vessel Classification by Size</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The industry uses several classification systems based on vessel size and capability. Understanding 
    these categories is essential for port planning and operational discussions.
    """)
    
    # Classification data
    vessel_classes = pd.DataFrame({
        'Class': [
            'Feeder',
            'Feedermax',
            'Panamax',
            'Post-Panamax',
            'New-Panamax (Neo-Panamax)',
            'VLCS (Very Large Container Ship)',
            'ULCS (Ultra Large Container Ship)'
        ],
        'Capacity Range (TEU)': [
            '100 - 1,000',
            '1,000 - 3,000',
            '3,000 - 5,000',
            '5,000 - 10,000',
            '10,000 - 14,500',
            '10,000 - 18,000',
            '18,000 - 25,000+'
        ],
        'Typical Width (m)': ['<23', '23-30', '32.2 (max)', '32.3-49', '49-51', '51-59', '59-61'],
        'Defining Constraint': [
            'Small ports, rivers',
            'Regional routes',
            'Old Panama Canal (retired 2016)',
            'Suez Canal width',
            'New Panama Canal (2016+)',
            'Port crane reach',
            'Port infrastructure limits'
        ],
        'Typical Routes': [
            'Short-sea, river, coastal',
            'Intra-regional (Asia, Europe)',
            'Trans-Pacific, Asia-Europe',
            'Major trade lanes',
            'Trans-Pacific, Asia-Europe',
            'Asia-Europe mainline',
            'Asia-Europe mainline'
        ],
        'Example Vessels': [
            'Regional feeders',
            'CMA CGM Coral',
            'APL China (retired)',
            'Maersk Sealand',
            'CMA CGM Brazil',
            'Maersk Triple E',
            'MSC Gülsün, HMM Algeciras'
        ]
    })
    
    st.dataframe(vessel_classes, width='stretch', hide_index=True)
    
    st.markdown('<p class="subsection-header">Canal and Port Constraints</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Panama Canal Constraints:**
        
        **Old Locks (Pre-2016):**
        - Maximum length: 294.1 m
        - Maximum width: 32.3 m (**Panamax limit**)
        - Maximum draft: 12.0 m
        - Capacity: ~4,500 TEU maximum
        
        **New Locks (Post-2016):**
        - Maximum length: 427 m
        - Maximum width: 49 m (**New-Panamax limit**)
        - Maximum draft: 18.3 m
        - Capacity: ~12,600 TEU maximum
        
        **Impact:**
        - Old canal limited vessel sizes until 2016
        - Expansion allowed larger vessels on trans-Pacific routes
        - Mega vessels (20,000+ TEU) still cannot use Panama Canal
        """)
    
    with col2:
        st.markdown("""
        **Suez Canal Constraints:**
        
        **Current Specifications:**
        - Maximum length: No practical limit
        - Maximum width: 77.5 m beam (much wider than Panama)
        - Maximum draft: 20.1 m
        - **No locks** (sea-level canal)
        
        **Strategic Importance:**
        - Critical Asia-Europe route
        - Can accommodate all existing container vessels
        - Mega vessels fit comfortably
        - Critical chokepoint for global trade
        
        **Alternative: Cape of Good Hope**
        - Significantly longer route
        - Much higher fuel costs
        - Avoided unless Suez blocked
        """)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ Operational Challenges of Mega Vessels:</strong><br>
    - <strong>Limited port access</strong>: Only select ports globally can handle ultra-large vessels<br>
    - <strong>Concentration risk</strong>: One vessel carries enormous cargo value<br>
    - <strong>Slower port rotations</strong>: Fewer port calls per voyage<br>
    - <strong>Canal restrictions</strong>: Cannot use Panama Canal (too wide)<br>
    - <strong>Weather sensitivity</strong>: More affected by wind due to high stacks<br>
    - <strong>Single point of failure</strong>: Breakdown affects thousands of containers
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 4: Stowage Planning Fundamentals
    # ============================================================================
    
    st.markdown('<p class="section-header">Vessel Stowage Planning: The Tetris Challenge</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Stowage planning—determining where each container goes on the vessel—is a complex optimisation problem 
    with multiple competing constraints. It's like 3D Tetris with thousands of pieces and strict rules.
    """)
    
    st.markdown('<p class="subsection-header">Stowage Planning Principles</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>🎯 Stowage Planning Principles:</strong><br>
    - <strong>Stability</strong>: Keep centre of gravity low and balanced<br>
    - <strong>Structural limits</strong>: Don't exceed stack weight or deck load limits<br>
    - <strong>Destination sequence</strong>: First port off containers on top/accessible<br>
    - <strong>Container compatibility</strong>: Dangerous goods segregation, reefer power access<br>
    - <strong>Operational efficiency</strong>: Minimise crane movements, balance workload<br>
    - <strong>Special requirements</strong>: Out-of-gauge, hazmat, temperature-controlled
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">1. Vessel Stability</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Why Stability Matters:**
    - Vessel must remain upright and stable in all sea conditions
    - Too much weight high up → Risk of capsizing (top-heavy)
    - Uneven weight distribution → Vessel lists (leans) to one side
    - Weight too far forward/aft → Vessel "hogs" (bends upward) or "sags" (bends downward)
    
    **Key Stability Concepts:**
    
    **Centre of Gravity (G):**
    - Point where all weight effectively concentrated
    - Lower G = more stable
    - Heavy containers go low in holds, lighter on deck
    
    **Metacentric Height (GM):**
    - Measure of initial stability
    - Too low GM → Vessel unstable, may capsize
    - Too high GM → Vessel rolls uncomfortably (harsh motion)
    - Target: Optimal range varies by vessel design
    
    **Longitudinal Balance:**
    - Weight distributed evenly bow-to-stern
    - Prevent excessive "trim" (bow or stern too low)
    - Target: Near-zero trim or slight stern trim
    
    **Transverse Balance:**
    - Weight distributed evenly port-to-starboard
    - Prevent "list" (leaning to one side)
    - Target: Zero list (perfectly upright)
    
    **Practical Rules:**
    - Heavy containers in lower holds
    - Empty containers on top tiers
    - Balance weight port/starboard within each bay
    - Spread heavy containers throughout vessel length
    """)
    
    st.markdown('<p class="subsection-header">2. Destination Sequence (Port Rotation)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Challenge:**
    - Vessel calls at multiple ports on a voyage
    - Containers for Port 1 must be accessible before containers for Port 2
    - Otherwise, must move containers to access others ("re-stows")
    - Re-stows waste time and money
    
    **The Solution:**
    - **Later ports on bottom/back**: Containers for Port 5 at bottom of stacks
    - **Earlier ports on top/front**: Containers for Port 1 on top, easy to access
    - **Segregate by destination**: Group containers by discharge port
    
    **Example Vessel Route:**
    Singapore → Hong Kong → Shanghai → Busan → Los Angeles → Oakland → Seattle
    
    **Stowage Strategy:**
    - Seattle cargo: Bottom tier, inaccessible until final port
    - Oakland cargo: Mid-tiers, accessible after LA discharge
    - Los Angeles cargo: Upper tiers, accessible early
    - Busan cargo: Top tiers, accessible first after loading
    
    **Re-Stow Problem:**
    - If a Los Angeles container is buried under Seattle containers, must remove Seattle containers temporarily (re-stow)
    - Each re-stow costs 2-3 crane moves (lift off, set aside, replace after)
    - Target: <2% re-stow rate (ideally zero)
    """)
    
    st.markdown('<p class="subsection-header">3. Weight Distribution and Structural Limits</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Structural Constraints:**
    
    **Stack Weight Limits:**
    - Maximum weight can be stacked vertically
    - Typically 200-300 tonnes per stack
    - Depends on cell guide strength and deck structure
    - Heavy containers can't all be in same stack
    
    **Deck Load Limits:**
    - Each deck section has maximum weight capacity
    - Typically 5-10 tonnes per square metre
    - Heavy containers spread across multiple positions
    
    **Hatch Cover Strength:**
    - Hatch covers support containers on deck above hold
    - Limited load capacity (weaker than solid deck)
    - Heavy containers avoid hatch cover positions when possible
    
    **Bay Limits:**
    - Maximum weight per bay (longitudinal section)
    - Prevent excessive bending moments on hull
    - Typically 1,000-2,000 tonnes per bay (vessel-specific)
    
    **Practical Implications:**
    - Computer software calculates all loads automatically
    - Stowage planner adjusts if limits exceeded
    - May need to move containers between bays to balance loads
    """)
    
    st.markdown('<p class="subsection-header">4. Container Type Compatibility</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Dangerous Goods (DG) Segregation:**
    - Classes must be separated by minimum distances
    - Class 1 (explosives) kept far from Class 3 (flammables)
    - International Maritime Dangerous Goods (IMDG) Code specifies exact rules
    - Some DG can't be in holds (must be on deck with ventilation)
    
    **Reefer (Refrigerated) Containers:**
    - Must be within reach of power supply points
    - Limited number of reefer plugs per bay
    - Reefer stacks on deck or in specially-equipped holds
    - Monitor temperature continuously during voyage
    
    **Out-of-Gauge (OOG) Containers:**
    - Exceed standard dimensions (overwidth, overheight, overlength)
    - Cannot have containers stacked on top
    - Placed in specific positions with clearance
    - Often require special securing equipment
    
    **Empty Containers:**
    - Very light (2-4 tonnes vs 30+ tonnes full)
    - Placed on top tiers when possible
    - Can't support heavy containers on top
    - Used to balance weight distribution
    """)
    
    st.markdown('<p class="subsection-header">The Stowage Planning Process</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Timeline: 48-72 Hours Before Vessel Arrival**
    
    **Step 1: Receive Container List**
    - Shipping line / terminal provides list of containers to load
    - Details: Container number, size (20'/40'), weight, type, destination, special requirements
    
    **Step 2: Understand Vessel Configuration**
    - Vessel's bay plan (which bays exist, capacity of each)
    - Reefer plug locations
    - Weight limits for each position
    - Current cargo onboard (if mid-voyage)
    
    **Step 3: Group Containers**
    - By destination port
    - By size (20' vs 40')
    - By type (dry, reefer, OOG, dangerous goods)
    - By weight class (<15t, 15-25t, >25t)
    
    **Step 4: Initial Allocation**
    - Assign containers to bays based on destination sequence
    - Heavy containers to bottom tiers
    - Reefers to powered positions
    - Dangerous goods with proper segregation
    
    **Step 5: Check Stability**
    - Calculate centre of gravity (G)
    - Calculate metacentric height (GM)
    - Check longitudinal and transverse balance
    - Verify all structural limits
    
    **Step 6: Optimise for Efficiency**
    - Minimise crane travel between bays
    - Balance workload across multiple cranes
    - Sequence loading for operational efficiency
    - Identify any re-stow requirements
    
    **Step 7: Generate Final Plan**
    - Bay plans showing exact position of every container (bay-row-tier)
    - Loading sequence for cranes
    - Special instructions for DG, OOG, reefers
    - Stability report confirming safety
    
    **Output:**
    - Detailed stowage plan sent to vessel and terminal
    - Crane operators follow plan precisely
    - Any deviations require re-calculation of stability
    """)
    
    # ============================================================================
    # SECTION 6: Technology Evolution
    # ============================================================================
    
    st.markdown('<p class="section-header">Technology Evolution in Vessel Design</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Modern container vessels incorporate advanced technologies that weren't imaginable in the 1950s.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Propulsion and Efficiency:**
        - **Slow steaming**: Operate at 18-20 knots vs 25+ knots (30-50% fuel savings)
        - **Optimised hull designs**: Bulbous bow, improved hydrodynamics
        - **Efficient engines**: Two-stroke diesel, waste heat recovery
        - **Automation**: Unmanned engine rooms, remote monitoring
        
        **Environmental Technologies:**
        - **Scrubbers**: Remove sulphur from exhaust (meet IMO 2020 regulations)
        - **LNG dual-fuel**: Can burn LNG (20% less CO₂ than conventional fuel)
        - **Alternative fuels ready**: Methanol, ammonia capability in new builds
        - **Shore power**: Plug into port electricity (zero emissions at berth)
        """)
    
    with col2:
        st.markdown("""
        **Operational Technologies:**
        - **GPS and AIS**: Precise navigation and vessel tracking
        - **Weather routing**: Optimise route for fuel efficiency and safety
        - **Predictive maintenance**: Sensors monitor equipment health
        - **Virtual models**: Simulation and optimisation tools
        
        **Cargo Management:**
        - **Automated stowage planning**: AI-powered optimisation software
        - **Container tracking**: IoT sensors monitor location and condition
        - **Reefer monitoring**: Remote temperature and power monitoring
        - **Load computers**: Real-time stability calculations
        """)
    
    # ============================================================================
    # SECTION 7: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Vessel Anatomy:**
        - Bow (front), Stern (back), Port (left), Starboard (right)
        - Bay-Row-Tier positioning system
        - Holds (below deck), Deck (above), Superstructure
        
        **Evolution:**
        - 1956: 500 TEU (Ideal X, first container ship)
        - 2019: 23,000+ TEU (MSC Gülsün)
        - 46x capacity increase in 63 years
        
        **Classifications:**
        - Feeder: <3,000 TEU
        - Panamax: ~4,500 TEU (old Panama Canal limit)
        - New-Panamax: ~14,500 TEU (new Panama Canal)
        - ULCS: 18,000-25,000 TEU (mega vessels)
        """)
    
    with col2:
        st.markdown("""
        **Economics of Scale:**
        - 18,000 TEU vessel: 82% lower cost per TEU vs 1,000 TEU
        - Fixed costs (crew, insurance) don't scale with size
        - Variable costs (fuel) scale less than proportionally
        - Requires high utilisation and cargo volumes
        
        **Stowage Planning:**
        - Stability: Low centre of gravity, balanced
        - Destination: Later ports bottom, earlier ports top
        - Weight: Structural limits, heavy containers low
        - Compatibility: DG segregation, reefer power, OOG
        
        **Technology:**
        - Slow steaming (fuel efficiency)
        - Environmental (scrubbers, LNG, shore power)
        - Automation (AI stowage, predictive maintenance)
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Container vessels have grown 46x in capacity since 1956, driven by 
    powerful economies of scale. Modern mega vessels (20,000+ TEU) cost 80%+ less per container but require 
    sophisticated infrastructure and operational planning. Stowage planning is a complex 3D optimisation 
    problem balancing stability, destination sequence, structural limits, and container compatibility. 
    Advanced technology (slow steaming, scrubbers, AI-powered planning, IoT) enables efficient, safe, and 
    increasingly sustainable operations.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** 🌍 Global Shipping & Alliances - Understand how shipping lines have consolidated into 
    three mega-alliances controlling 83% of global capacity, and how hub-and-spoke networks enable global 
    connectivity.
    """)
