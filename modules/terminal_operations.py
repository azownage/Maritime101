import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

def show():
    st.markdown('<p class="main-header">🏗️ Terminal Operations & Planning</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand the complete container terminal operational workflow, from vessel arrival to departure, 
    including berth planning, yard operations, stowage planning, and equipment scheduling.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Container Terminal Layout
    # ============================================================================
    
    st.markdown('<p class="section-header">Container Terminal Layout and Zones</p>', unsafe_allow_html=True)
    
    st.markdown("""
    A modern container terminal is divided into distinct operational zones, each serving specific functions 
    in the cargo handling process.
    """)
    
    st.markdown('<p class="subsection-header">Terminal Zones Overview</p>', unsafe_allow_html=True)
    
    # Terminal zones
    terminal_zones = pd.DataFrame({
        'Zone': [
            'Berth / Quay',
            'Apron',
            'Quay Cranes (QC)',
            'Storage Yard',
            'Yard Cranes',
            'Gate Complex',
            'Control Tower',
            'Inland Transportation'
        ],
        'Function': [
            'Where vessels dock; interface between sea and land',
            'Area directly behind berth for container staging and crane operations',
            'Load/discharge containers between vessel and apron',
            'Store containers awaiting pickup or loading; organised in blocks/bays',
            'Move containers between yard storage and trucks/trains',
            'Entry/exit point for trucks; documentation and security checks',
            'Central command centre for terminal operations coordination',
            'Roads/rail connecting terminal to hinterland'
        ],
        'Key Equipment': [
            'Bollards, fenders, vessel-to-shore connections',
            'Prime movers, automated guided vehicles (AGVs)',
            'Ship-to-shore cranes, dual trolley systems',
            'Rubber-tyred gantry cranes (RTG), rail-mounted gantry (RMG)',
            'RTG, RMG, reach stackers, straddle carriers',
            'Optical character recognition (OCR), automated gates',
            'IT systems, communications, CCTV, vessel traffic management',
            'Trucks, trains, road/rail infrastructure'
        ],
        'Typical Dimensions': [
            '300-450m length × 50-70m width per berth',
            '50-100m depth behind quay',
            '60-80m outreach for mega vessels',
            '10-30 hectares per terminal',
            '6-8 containers high stacking',
            'Multiple lanes, 20-40 gates',
            'Central location with 360° visibility',
            'Road/rail corridors'
        ]
    })
    
    st.dataframe(terminal_zones, width='stretch', hide_index=True)
    
    st.markdown("""
    **Terminal Flow Logic:**
    
    **Import Flow (Vessel → Land):**
    1. Vessel arrives and berths at **Quay**
    2. **Quay Crane** discharges containers to **Apron**
    3. **Prime Mover/AGV** transports containers to **Storage Yard**
    4. **Yard Crane** places containers in storage location
    5. Truck arrives at **Gate**, processes paperwork
    6. **Yard Crane** retrieves container and loads onto truck
    7. Truck exits via **Gate** to hinterland
    
    **Export Flow (Land → Vessel):**
    1. Truck arrives at **Gate** with export container
    2. **Yard Crane** receives container and places in **Storage Yard**
    3. When vessel arrives, **Yard Crane** retrieves container
    4. **Prime Mover/AGV** transports to **Apron**
    5. **Quay Crane** loads container onto vessel
    6. Vessel departs when loading complete
    
    **Transshipment Flow (Vessel → Vessel):**
    1. Container discharged from Vessel A to **Apron**
    2. Moved to **Storage Yard** for temporary holding
    3. Retrieved and moved to **Apron** when Vessel B arrives
    4. Loaded onto Vessel B
    5. (Ideally minimises storage time in yard)
    """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>💡 Operational Efficiency:</strong> The goal is to minimise:<br>
    - <strong>Container dwell time</strong>: Time between discharge and pickup (imports) or drop-off and loading (exports)<br>
    - <strong>Vessel port stay</strong>: Total hours from arrival to departure<br>
    - <strong>Equipment idle time</strong>: Cranes, prime movers, yard equipment waiting<br>
    - <strong>Re-handles</strong>: Moving containers multiple times to access others<br><br>
    Every movement costs time and money. Efficient operations minimise unnecessary moves.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 2: Container Terminal Operations Process Flow
    # ============================================================================
    
    st.markdown('<p class="section-header">Container Terminal Operations: Complete Process</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Container terminal operations follow a structured workflow from vessel notification to departure. 
    Understanding this end-to-end process is crucial for operational planning.
    """)
    
    st.markdown('<p class="subsection-header">Phase 1: Pre-Arrival Planning (72+ hours before arrival)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Vessel Notification:**
    - Shipping line sends **vessel arrival notice** via PORTNET (Singapore's port clearance system)
    - Information includes: Vessel name, size, estimated time of arrival (ETA), cargo manifest
    - **Cargo manifest**: Complete list of containers to discharge and load
    
    **Information Exchange:**
    - Terminal receives detailed container data:
      - Container number, size (20ft/40ft), type (dry/reefer/OOG)
      - Weight, destination port, dangerous goods classification
      - Customer, booking reference, special handling requirements
    
    **Initial Planning:**
    - **Berth Planning**: Which berth to assign based on vessel size, draft, schedule
    - **Resource Planning**: How many cranes, prime movers, yard space needed
    - **Preliminary Stowage Plan**: Review shipping line's proposed stowage plan
    """)
    
    st.markdown('<p class="subsection-header">Phase 2: Detailed Planning (24-48 hours before arrival)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Berth Planning Confirmation:**
    - Finalise **berth window** (expected arrival and departure times)
    - Coordinate with other vessels to avoid conflicts
    - Target: **Berth on Arrival (BOA)** >90% (vessel berths immediately without waiting)
    
    **Discharge Planning:**
    - Plan sequence to discharge containers from vessel
    - Objective: Minimise crane movements and re-handles
    - Consider vessel stability during discharge process
    - Identify priority containers (time-sensitive, dangerous goods)
    
    **Loading Planning / Stowage Planning:**
    - Determine exact position for each export container on vessel
    - Constraints:
      - **Vessel stability**: Weight distribution fore/aft and port/starboard
      - **Destination sequence**: Containers for later ports on bottom
      - **Container type**: Reefers near power, OOG can't stack, dangerous goods segregation
      - **Weight limits**: Stack weight, hatch cover strength
    - Generate **bay plans** showing each container's position (bay-row-tier)
    
    **Yard Planning:**
    - Allocate **yard storage locations** for import containers
    - Group by destination, shipping line, container type
    - Plan for efficient retrieval when trucks arrive
    - Reserve space for export containers arriving by truck
    
    **Equipment Scheduling:**
    - Assign specific **quay cranes** to vessel (typically 4-8 cranes for mega vessels)
    - Schedule **yard crane** operations
    - Allocate **prime movers/AGVs** for horizontal transport
    - Plan equipment **maintenance windows** to avoid conflicts
    """)
    
    st.markdown('<p class="subsection-header">Phase 3: Vessel Operations (During port stay)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Vessel Arrival:**
    - Vessel arrives at anchorage or directly to berth
    - **Pilot** boards vessel to navigate into berth
    - **Tugboats** assist with docking
    - Vessel **moors** to berth (secured with lines)
    - **Gangway** deployed for crew access
    
    **Pre-Operations:**
    - **Safety inspection**: Confirm vessel safe for operations
    - **Lashing/unlashing**: Secure or release container securing equipment
    - **Hatch cover removal**: Open vessel holds for crane access
    - **Reefer connections**: Connect power to refrigerated containers
    
    **Discharge Operations:**
    - **Quay cranes** begin discharging containers
    - Each crane has **operator** controlling movements
    - **Spreader** (crane attachment) locks onto container corner castings
    - Container lifted from vessel → lowered to **apron**
    - **Prime mover/AGV** picks up container → transports to **yard**
    - **Yard crane** places container in designated storage location
    - Process continues until all discharge containers removed
    
    **Loading Operations:**
    - **Yard cranes** retrieve export containers from storage
    - **Prime movers/AGVs** transport to **apron staging area**
    - Containers staged in **loading sequence** for efficient crane operations
    - **Quay cranes** lift containers from apron → place on vessel
    - **Lashers** secure containers according to **lashing plan**
    - Process continues until all export containers loaded
    
    **Concurrent Operations:**
    - Import discharge and export loading often happen **simultaneously**
    - Different cranes work on different bays of vessel
    - Coordination critical to avoid conflicts and maintain efficiency
    
    **Real-Time Adjustments:**
    - **No-shows**: Expected export containers don't arrive → adjust plan
    - **Roll-overs**: Containers missed this vessel → reschedule for next
    - **Equipment breakdowns**: Reassign cranes, adjust operations
    - **Weather issues**: Suspend operations if unsafe (high winds, lightning)
    """)
    
    # Vessel operation timeline
    operation_timeline = pd.DataFrame({
        'Phase': ['Arrival & Mooring', 'Pre-Operations', 'Discharge', 'Loading', 'Post-Operations', 'Departure'],
        'Duration (hours)': [1.5, 1.0, 8.0, 10.0, 1.0, 0.5],
        'Activities': [
            'Pilot boards, tugboat assist, vessel moors, gangway',
            'Safety check, lashing/unlashing prep, hatch covers',
            '1,000 import containers discharged',
            '1,200 export containers loaded',
            'Hatch covers closed, final checks, paperwork',
            'Lines released, tugboat assist, vessel departs'
        ]
    })
    
    # Timeline visualization
    fig = go.Figure()
    
    cumulative_time = [0]
    for duration in operation_timeline['Duration (hours)']:
        cumulative_time.append(cumulative_time[-1] + duration)
    
    for i in range(len(operation_timeline)):
        fig.add_trace(go.Scatter(
            x=[cumulative_time[i], cumulative_time[i+1]],
            y=[operation_timeline['Phase'][i], operation_timeline['Phase'][i]],
            mode='lines+markers',
            line=dict(width=20, color=['#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6', '#06B6D4'][i]),
            marker=dict(size=10),
            name=operation_timeline['Phase'][i],
            hovertemplate=f"<b>{operation_timeline['Phase'][i]}</b><br>" +
                         f"Duration: {operation_timeline['Duration (hours)'][i]} hours<br>" +
                         f"{operation_timeline['Activities'][i]}<extra></extra>"
        ))
    
    fig.update_layout(
        title={
            'text': 'Typical Vessel Operations Timeline (22 hours total)',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        xaxis_title="Elapsed Time (hours)",
        yaxis_title="",
        height=400,
        showlegend=False,
        xaxis=dict(range=[0, 22], gridcolor='#E5E7EB'),
        plot_bgcolor='white'
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 Target Performance:</strong><br>
    - <strong>Mega vessel (20,000+ TEU)</strong>: 24-36 hour total port stay<br>
    - <strong>Quay crane productivity</strong>: 30-40 gross moves per hour (GMPH)<br>
    - <strong>Berth on Arrival (BOA)</strong>: >90% (vessel berths immediately)<br>
    - <strong>Zero damage</strong>: No containers or cargo damaged during handling<br><br>
    World-class terminals like Singapore PSA consistently meet or exceed these targets.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 3: Detailed Planning Processes
    # ============================================================================
    
    st.markdown('<p class="section-header">The Four Key Planning Processes</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Container terminal planning involves four interconnected optimisation problems that must be solved 
    in coordination.
    """)
    
    st.markdown('<p class="subsection-header">1. Berth Planning</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Objective:** Assign vessels to berths and time windows to maximise berth utilisation and minimise 
    vessel waiting time.
    
    **Planning Horizon:** 72+ hours ahead (rolling window)
    
    **Inputs:**
    - Vessel arrival schedule (ETA from shipping lines)
    - Vessel characteristics (length, draft, cargo volume)
    - Berth characteristics (length, depth, crane coverage)
    - Expected operation duration
    
    **Constraints:**
    - **Physical**: Vessel length ≤ berth length, vessel draft ≤ water depth
    - **Operational**: Vessel operations cannot overlap at same berth
    - **Safety**: Minimum separation between vessels
    - **Priority**: Some vessels have priority (alliances, schedule commitments)
    
    **Optimisation Objectives:**
    - **Primary**: Maximise BOA (Berth on Arrival) percentage - vessel berths immediately without waiting
    - **Secondary**: Minimise total vessel waiting time
    - **Tertiary**: Balance berth utilisation across all berths
    
    **Output:**
    - **Berth allocation plan**: Which vessel at which berth
    - **Time windows**: Expected berthing time and departure time for each vessel
    - **Crane allocation**: How many cranes assigned to each vessel
    
    **Key Performance Indicator:**
    - **BOA (Berth on Arrival)**: Percentage of vessels berthing immediately
    - Target: >90% BOA
    - Singapore consistently achieves >90% BOA
    """)
    
    # Berth planning visualization
    berth_plan = pd.DataFrame({
        'Berth': ['Berth 1', 'Berth 1', 'Berth 2', 'Berth 2', 'Berth 3', 'Berth 3', 'Berth 4'],
        'Vessel': ['Vessel A', 'Vessel D', 'Vessel B', 'Vessel E', 'Vessel C', 'Vessel F', 'Vessel G'],
        'Start': [0, 20, 2, 24, 5, 28, 10],
        'Duration': [20, 22, 22, 20, 23, 19, 26],
        'TEU': [8000, 9000, 7500, 8500, 8200, 7800, 9500]
    })
    
    fig = go.Figure()
    
    colors = ['#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6', '#06B6D4', '#EC4899']
    
    for i, row in berth_plan.iterrows():
        fig.add_trace(go.Bar(
            name=row['Vessel'],
            x=[row['Duration']],
            y=[row['Berth']],
            orientation='h',
            marker=dict(color=colors[i % len(colors)]),
            text=f"{row['Vessel']}<br>{row['TEU']} TEU<br>{row['Duration']}h",
            textposition='inside',
            base=row['Start'],
            hovertemplate=f"<b>{row['Vessel']}</b><br>" +
                         f"Berth: {row['Berth']}<br>" +
                         f"Start: {row['Start']}h<br>" +
                         f"Duration: {row['Duration']}h<br>" +
                         f"TEU: {row['TEU']}<extra></extra>"
        ))
    
    fig.update_layout(
        title={
            'text': 'Berth Allocation Plan (48-hour window)',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        xaxis_title="Time (hours)",
        barmode='overlay',
        height=400,
        showlegend=False,
        xaxis=dict(range=[0, 48], gridcolor='#E5E7EB'),
        plot_bgcolor='white'
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown('<p class="subsection-header">2. Storage Yard Planning</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Objective:** Allocate storage locations for containers in the yard to minimise handling time and 
    re-handles (moving containers to access others).
    
    **Planning Horizon:** 24-72 hours ahead
    
    **Storage Principles:**
    
    **For Import Containers (from vessel):**
    - Group by **destination** (same customer, same city)
    - Group by **shipping line** (for billing and tracking)
    - Group by **size and type** (20ft vs 40ft, dry vs reefer)
    - Place **popular destinations** in easy-access locations
    - **Reefers** near power connection points
    - **Dangerous goods** in designated isolated areas
    
    **For Export Containers (from trucks):**
    - Group by **destination port** (will load on same vessel)
    - Group by **vessel** (departing soonest near loading area)
    - Group by **size/type/weight** for stowage planning
    - **Heavy containers** on bottom of stacks
    - **Time-sensitive cargo** in priority locations
    
    **For Transshipment Containers:**
    - **Minimise dwell time**: Direct transfer from discharge to loading if possible
    - Group by **outbound vessel**
    - Segregate from import/export containers
    
    **Yard Block Organisation:**
    - Yard divided into **blocks** (rectangular sections)
    - Each block has multiple **bays** (columns)
    - Each bay has multiple **rows** (across width)
    - Each position has multiple **tiers** (stacking height, typically 5-7 high)
    - Address: Block-Bay-Row-Tier (e.g., Block 3, Bay 12, Row 04, Tier 03)
    
    **Optimisation Objectives:**
    - Minimise **re-handles**: Avoid moving containers to access others underneath
    - Minimise **yard crane travel distance**
    - Balance **yard utilisation** across blocks
    - Ensure **safe stacking**: Heavy on bottom, compatible types together
    
    **Key Challenges:**
    - **Uncertainty**: Don't know exactly when trucks will pick up import containers
    - **Dynamic**: Containers constantly arriving and departing
    - **Re-handles**: Sometimes unavoidable when container arrival sequence doesn't match departure sequence
    """)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ The Re-Handle Problem:</strong><br><br>
    <strong>Scenario:</strong> Import containers A, B, C, D arrive from vessel and stacked vertically (D on top of A).<br>
    - Truck for Container A arrives first<br>
    - Must move containers D, C, B to access A (<strong>3 re-handles</strong>)<br>
    - Each re-handle costs time, equipment, energy<br><br>
    <strong>Solution Strategies:</strong><br>
    - Predict truck arrival patterns using historical data<br>
    - Stack containers likely to be picked up soon on top<br>
    - Use AI/ML to optimise stacking decisions<br>
    - Accept some re-handles as unavoidable (target: <10% re-handle rate)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">3. Vessel Stowage Planning</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Objective:** Determine the exact position of each container on the vessel to ensure safety, stability, 
    and operational efficiency.
    
    **Planning Horizon:** 24-48 hours before vessel arrival
    
    **Critical Constraints:**
    
    **1. Vessel Stability:**
    - **Centre of gravity**: Must be within safe limits (too high = unstable, too low = excessive stress)
    - **Longitudinal balance**: Weight distribution bow to stern (prevent hogging/sagging)
    - **Transverse balance**: Weight distribution port to starboard (prevent listing)
    - **Metacentric height (GM)**: Measure of stability (too low = risk of capsizing)
    
    **2. Structural Limits:**
    - **Stack weight**: Maximum weight per vertical stack of containers
    - **Deck load**: Weight capacity of each deck section
    - **Hatch cover strength**: Maximum weight that can be placed on hatch covers
    - **Bay limits**: Maximum weight per bay (longitudinal section)
    
    **3. Destination Sequence:**
    - Containers for **Port 1** must be accessible before **Port 2** containers
    - Generally: **Later ports on bottom/back**, **earlier ports on top/front**
    - Minimise **re-stows**: Moving containers between ports to access others
    
    **4. Container Compatibility:**
    - **Dangerous Goods (DG)**: Segregation requirements (class-specific separation distances)
    - **Reefers**: Must be within reach of power outlets
    - **Out of Gauge (OOG)**: Cannot stack containers on top
    - **Heavy containers**: On bottom of stacks, over strong structural points
    - **Empty containers**: On top (lighter weight)
    
    **5. Operational Efficiency:**
    - Minimise **crane movements**: Complete bays sequentially
    - **Balance crane productivity**: Distribute work evenly across cranes
    - Consider **hatch cover operations**: Time to remove/replace covers
    - Enable **simultaneous operations**: Multiple cranes working without conflicts
    
    **Stowage Planning Process:**
    
    **Step 1:** Receive container list from shipping line / terminal
    - All export containers with specifications
    
    **Step 2:** Group containers by:
    - Destination port
    - Size (20ft / 40ft)
    - Type (dry / reefer / OOG / dangerous goods)
    - Weight category
    
    **Step 3:** Preliminary allocation
    - Assign containers to **bays** based on destination sequence
    - Heavy containers to bottom tiers
    - Reefers to locations with power
    - Dangerous goods with proper segregation
    
    **Step 4:** Stability calculation
    - Calculate centre of gravity
    - Check all stability parameters
    - Adjust if necessary
    
    **Step 5:** Optimise for efficiency
    - Minimise crane travel
    - Balance crane workload
    - Sequence for minimal re-handles
    
    **Step 6:** Generate final bay plans
    - Detailed position for every container (bay-row-tier)
    - Loading sequence for each crane
    - Special instructions for DG, OOG, reefers
    
    **Output:**
    - **Stowage plan**: Complete vessel loading plan with every container position
    - **Loading sequence**: Order in which containers should be loaded
    - **Crane work distribution**: Which crane loads which containers
    - **Stability report**: Confirming vessel will be safe
    """)
    
    # Bay plan example visualization
    st.markdown("""
    **Example: Bay Plan (Cross-Section View)**
    
    Looking at vessel from stern (back) toward bow (front), showing one bay:
    """)
    
    bay_plan_data = []
    # Create a sample bay plan
    for tier in range(1, 7):  # 6 tiers high
        for row in range(1, 9):  # 8 rows across
            # Colour code by destination
            if tier <= 2:
                dest = 'Port 3 (Last)'
                color = '#EF4444'
            elif tier <= 4:
                dest = 'Port 2'
                color = '#F59E0B'
            else:
                dest = 'Port 1 (First)'
                color = '#10B981'
            
            if row <= 4:
                side = 'Port'
            else:
                side = 'Starboard'
            
            bay_plan_data.append({
                'Row': row,
                'Tier': tier,
                'Destination': dest,
                'Color': color,
                'Side': side
            })
    
    bay_df = pd.DataFrame(bay_plan_data)
    
    fig = go.Figure(data=go.Scatter(
        x=bay_df['Row'],
        y=bay_df['Tier'],
        mode='markers',
        marker=dict(
            size=30,
            color=bay_df['Color'],
            line=dict(color='#1F2937', width=2),
            symbol='square'
        ),
        text=bay_df['Destination'],
        hovertemplate='Row: %{x}<br>Tier: %{y}<br>%{text}<extra></extra>'
    ))
    
    fig.update_layout(
        title={
            'text': 'Bay Plan Example: Stacking by Destination Port',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        xaxis_title="Row (Port ← → Starboard)",
        yaxis_title="Tier (Bottom → Top)",
        height=400,
        xaxis=dict(tickmode='linear', tick0=1, dtick=1, gridcolor='#E5E7EB'),
        yaxis=dict(tickmode='linear', tick0=1, dtick=1, gridcolor='#E5E7EB'),
        plot_bgcolor='white',
        annotations=[
            dict(x=2, y=6.5, text='Port 1 (First discharge)', showarrow=False, font=dict(color='#10B981', size=12)),
            dict(x=6, y=4, text='Port 2', showarrow=False, font=dict(color='#F59E0B', size=12)),
            dict(x=6, y=1.5, text='Port 3 (Last discharge)', showarrow=False, font=dict(color='#EF4444', size=12))
        ]
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown('<p class="subsection-header">4. Transportation Planning (Equipment Scheduling)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Objective:** Coordinate all equipment movements to execute the operational plan efficiently.
    
    **Planning Horizon:** Real-time to 24 hours ahead
    
    **Equipment Types to Coordinate:**
    
    **Quay Cranes (QC):**
    - Assign cranes to vessels
    - Determine **crane intensity**: How many cranes per vessel (typically 4-8 for mega vessels)
    - Create **crane work sequences**: Which crane discharges/loads which containers in what order
    - Optimise for **crane productivity** (target: 30-40 gross moves per hour per crane)
    - Avoid **crane interference**: Cranes can't cross paths
    
    **Yard Cranes (YC):**
    - Assign yard cranes to blocks
    - Schedule **retrieve operations**: Pick up export containers for loading
    - Schedule **placement operations**: Store import containers from discharge
    - Minimise **yard crane travel** within block
    - Balance **workload** across yard cranes
    
    **Horizontal Transport (Prime Movers / AGVs):**
    - Coordinate container movement between quay and yard
    - **Prime Movers (PM)**: Human-driven trucks with trailers
    - **AGVs**: Automated guided vehicles (battery-powered, computer-controlled)
    
    **Prime Mover Deployment:**
    - Traditional approach: Assign PMs to work with specific cranes
    - Each PM makes round trips: Quay → Yard → Quay
    - Challenge: **Empty travel** reduces efficiency (PM returns empty to quay)
    
    **AGV Deployment:**
    - Modern approach: Fleet of AGVs dynamically dispatched
    - **Pooling strategy**: AGVs shared across all cranes (no fixed assignment)
    - Computer system optimises routing in real-time
    - Can carry container in both directions (quay to yard, yard to quay)
    - **Benefits**: Higher utilisation, less empty travel, more flexible
    
    **Dispatching Strategy:**
    - **Fixed assignment**: PM always works with same crane (simple but inflexible)
    - **Dynamic pooling**: PM/AGV assigned to next available job (efficient but complex)
    - **Hybrid**: Core PMs fixed, additional PMs pooled
    
    **Optimisation Objectives:**
    - Minimise **quay crane waiting time** (always have PM/AGV ready when crane ready)
    - Minimise **empty travel distance**
    - Balance **fleet utilisation**
    - Avoid **congestion** at quay and yard interfaces
    """)
    
    # Equipment productivity comparison
    equipment_productivity = pd.DataFrame({
        'Equipment Type': ['Quay Crane', 'Yard Crane (RTG)', 'Prime Mover', 'AGV', 'Gate Transaction'],
        'Unit': ['Moves/hour', 'Moves/hour', 'Cycles/hour', 'Cycles/hour', 'Transactions/hour'],
        'Traditional System': [25, 15, 4, 0, 20],
        'Modern Automated': [35, 25, 0, 10, 40],
        'World-Class Target': [40, 30, 5, 12, 50]
    })
    
    st.dataframe(equipment_productivity, width='stretch', hide_index=True)
    
    # ============================================================================
    # SECTION 4: Terminal Capacity Planning
    # ============================================================================
    
    st.markdown('<p class="section-header">Terminal Capacity Planning</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Terminal capacity is determined by multiple bottleneck resources. Understanding these bottlenecks is 
    critical for expansion planning.
    """)
    
    st.markdown('<p class="subsection-header">Key Capacity Components</p>', unsafe_allow_html=True)
    
    # Capacity components
    capacity_components = pd.DataFrame({
        'Component': [
            'Berth Capacity',
            'Quay Crane Capacity',
            'Yard Storage Capacity',
            'Yard Crane Capacity',
            'Horizontal Transport',
            'Gate Capacity',
            'Marine Channel'
        ],
        'Formula / Calculation': [
            'Berth length × Utilisation × Vessel calls per year × TEU per call',
            'Number of cranes × Moves per hour × Operating hours per year',
            'Yard area × Ground slots × Stacking height × Turnover rate',
            'Number of YCs × Moves per hour × Operating hours per year',
            'Fleet size × Cycles per hour × Operating hours × Containers per cycle',
            'Number of lanes × Transactions per hour × Operating hours',
            'Channel depth × Width × Tidal windows × Vessel traffic capacity'
        ],
        'Typical Bottleneck?': [
            'Often - Determines vessel capacity',
            'Yes - Drives vessel turnaround time',
            'Sometimes - When high dwell time',
            'Sometimes - Can limit throughput',
            'Rarely - Usually adequate if planned',
            'Sometimes - Peak hour congestion',
            'Rarely - Usually adequate'
        ],
        'Expansion Strategy': [
            'Build additional berths (very expensive, long lead time)',
            'Add more cranes; improve crane productivity',
            'Increase stacking height; reduce dwell time; better yard planning',
            'Add more yard cranes; improve scheduling',
            'Add more PMs/AGVs; improve dispatching',
            'Add more lanes; automate; off-peak incentives',
            'Dredging for deeper channel; widening; traffic management'
        ]
    })
    
    st.dataframe(capacity_components, width='stretch', hide_index=True)
    
    st.markdown("""
    **Capacity Calculation Example:**
    
    **Given:**
    - 10 berths, each 400m long
    - Average vessel: 350m long, 2,000 TEU discharged + 2,000 TEU loaded = 4,000 TEU total moves
    - Berth utilisation target: 70% (to allow flexibility and maintenance)
    - Average vessel turnaround: 24 hours
    - 365 days per year
    
    **Calculation:**
    - Available berth-hours per year: 10 berths × 365 days × 24 hours = 87,600 berth-hours
    - Actual operational berth-hours: 87,600 × 70% = 61,320 berth-hours
    - Vessel calls possible: 61,320 / 24 hours per vessel = 2,555 vessel calls per year
    - Annual capacity: 2,555 vessels × 4,000 TEU per vessel = **10.2 million TEU per year**
    
    **Sensitivity:**
    - If vessel turnaround improves to 20 hours: +20% capacity (12.2M TEU)
    - If berth utilisation increases to 80%: +14% capacity (11.6M TEU)
    - If average vessel grows to 5,000 TEU moves: +25% capacity (12.8M TEU)
    """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🎯 Capacity Optimisation Strategies:</strong><br><br>
    Rather than building more berths (expensive, long lead time), optimise existing capacity:<br><br>
    1. <strong>Improve quay crane productivity</strong>: 25 → 35 GMPH (saves 4 hours per vessel)<br>
    2. <strong>Better berth planning</strong>: Improve BOA from 85% → 95% (reduce waiting)<br>
    3. <strong>Faster turnaround</strong>: Reduce vessel port stay from 30h → 24h (20% more capacity)<br>
    4. <strong>Yard efficiency</strong>: Reduce dwell time from 5 days → 3 days (40% more yard space)<br>
    5. <strong>Equipment availability</strong>: Better maintenance reduces downtime<br>
    6. <strong>Process improvement</strong>: Eliminate bottlenecks and inefficiencies<br><br>
    Modern terminals use operational simulations to identify bottlenecks and test improvement scenarios 
    before implementing expensive infrastructure changes.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 5: TOS - Terminal Operating System
    # ============================================================================
    
    st.markdown('<p class="section-header">Terminal Operating System (TOS)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Modern container terminals rely on sophisticated **Terminal Operating Systems (TOS)** to plan and 
    execute all operations. The TOS is the "brain" of the terminal.
    """)
    
    st.markdown('<p class="subsection-header">TOS Core Modules</p>', unsafe_allow_html=True)
    
    # TOS modules
    tos_modules = pd.DataFrame({
        'TOS Module': [
            'Berth Planning',
            'Vessel Planning',
            'Yard Planning',
            'Resource Planning',
            'Equipment Control',
            'Gate Operations',
            'Documentation',
            'Billing & Invoicing',
            'Reporting & Analytics'
        ],
        'Functions': [
            'Allocate vessels to berths and time windows; optimise BOA',
            'Generate discharge and loading plans; stowage coordination',
            'Allocate yard locations; minimise re-handles; manage inventory',
            'Schedule cranes, PMs, AGVs, yard cranes; optimise utilisation',
            'Real-time dispatching of equipment; track positions; performance monitoring',
            'Truck check-in/out; documentation verification; container matching',
            'Generate shipping instructions, delivery orders, customs documentation',
            'Track container movements for billing; generate invoices',
            'Performance dashboards; KPI tracking; historical analysis'
        ],
        'Key Outputs': [
            'Berth allocation plan, vessel schedule',
            'Bay plans, crane work lists, loading sequences',
            'Yard block plans, container locations, retrieval lists',
            'Equipment assignments, work schedules',
            'Real-time work orders, route optimisation',
            'Gate permits, truck appointments, container releases',
            'eBL, customs declarations, manifests',
            'Invoices, payment tracking',
            'Performance reports, bottleneck analysis'
        ]
    })
    
    st.dataframe(tos_modules, width='stretch', hide_index=True)
    
    st.markdown("""
    **TOS Information Flow:**
    
    **Inputs to TOS:**
    - Vessel schedules from shipping lines (via PORTNET or EDI)
    - Container manifests (discharge and loading lists)
    - Truck appointments and gate arrivals
    - Equipment status (location, availability, maintenance)
    - Yard inventory (current container locations)
    
    **TOS Processing:**
    - Optimisation algorithms for planning
    - Real-time dispatching and coordination
    - Exception handling and alerts
    - Performance monitoring
    
    **Outputs from TOS:**
    - Work instructions to equipment operators
    - Container tracking information
    - Performance reports and KPIs
    - Billing and invoicing data
    - Integration with PORTNET, customs, shipping lines
    """)
    
    st.markdown("""
    **Major TOS Vendors:**
    - **CITOS® (PSA)**: Developed in-house by PSA Singapore, used in PSA terminals globally
    - **Navis N4**: Leading commercial TOS, used by many terminals worldwide
    - **TOS.log (HHLA)**: Hamburg port TOS
    - **Cosmos (DP World)**: DP World's proprietary TOS
    
    **Modern TOS Trends:**
    - **Cloud-based**: Deployed on cloud infrastructure for scalability
    - **AI-powered**: Machine learning for optimisation and predictive analytics
    - **Real-time**: Instant visibility and dynamic re-planning
    - **Integrated**: Connected to PORTNET, shipping lines, customs, trucking companies
    - **Mobile**: Operators access via tablets and smartphones
    - **IoT-enabled**: Equipment sensors feed real-time data to TOS
    """)
    
    # ============================================================================
    # SECTION 6: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Terminal Layout:**
        - Berth/Quay, Apron, Storage Yard, Gate, Control Tower
        - Import, Export, Transshipment flows
        - Goal: Minimise dwell time, vessel stay, re-handles
        
        **Operations Process:**
        - Phase 1: Pre-arrival planning (72+ hours)
        - Phase 2: Detailed planning (24-48 hours)
        - Phase 3: Vessel operations (during port stay)
        - Target: <24-36 hour turnaround for mega vessels
        
        **Four Key Planning Processes:**
        - **Berth Planning**: Vessel-to-berth allocation (BOA >90%)
        - **Yard Planning**: Storage location optimisation
        - **Stowage Planning**: Container position on vessel
        - **Transportation Planning**: Equipment scheduling
        """)
    
    with col2:
        st.markdown("""
        **Terminal Capacity:**
        - Multiple bottlenecks: Berths, cranes, yard, gates
        - Optimisation > expansion (faster, cheaper)
        - Sensitivity to turnaround time and productivity
        
        **Equipment Coordination:**
        - Quay cranes: 30-40 GMPH target
        - Yard cranes: Storage and retrieval
        - Prime Movers: Traditional horizontal transport
        - AGVs: Modern automated transport
        
        **Terminal Operating System (TOS):**
        - "Brain" of the terminal
        - Berth, vessel, yard, resource, equipment modules
        - Real-time optimisation and control
        - Integration with PORTNET and stakeholders
        - Modern: Cloud, AI, IoT, mobile
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Container terminal operations involve complex, interconnected planning 
    processes across berth allocation, yard management, vessel stowage, and equipment coordination. Success 
    requires sophisticated Terminal Operating Systems (TOS) that optimise plans in real-time whilst managing 
    uncertainty and exceptions. World-class terminals like Singapore PSA achieve >90% BOA, <24-hour mega 
    vessel turnaround, and 35+ crane GMPH through operational excellence and continuous optimisation. 
    Understanding these workflows is essential for effective operational planning.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** 🤖 Equipment, Automation & CITOS - Deep dive into terminal equipment types, automation 
    technologies, and PSA's CITOS terminal operating system.
    """)
