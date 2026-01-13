import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">🏗️ Container Terminal Operations</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Master the complete container terminal operational workflow from vessel arrival to departure, understand the 
    four key planning processes (berth planning, yard planning, stowage planning, transportation planning), comprehend 
    equipment coordination across quay cranes, yard cranes, and horizontal transport (prime movers/AGVs), explore 
    Terminal Operating Systems (TOS) that orchestrate these complex operations, and understand automation levels from 
    conventional to fully automated terminals.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Container Terminal Layout and Operational Zones
    # ============================================================================
    
    st.markdown('<p class="section-header">Container Terminal Layout: Understanding the Physical Infrastructure</p>', unsafe_allow_html=True)
    
    st.markdown("""
    A modern container terminal is a complex physical system divided into distinct operational zones, each serving 
    specific functions in the cargo handling process. Understanding this layout is essential for comprehending how 
    containers flow through the terminal and where bottlenecks can occur.
    
    The lecture materials emphasize that container terminal operations involve coordinated movement across multiple 
    zones, with equipment and information systems working together to achieve efficient cargo handling.
    """)
    
    st.markdown('<p class="subsection-header">The Seven Key Terminal Zones</p>', unsafe_allow_html=True)
    
    # Terminal zones comprehensive breakdown
    terminal_zones = pd.DataFrame({
        'Zone': [
            '1. Berth / Quay',
            '2. Apron Area',
            '3. Quay Crane Zone',
            '4. Storage Yard',
            '5. Yard Crane Zone',
            '6. Gate Complex',
            '7. Control Tower / TOS Center'
        ],
        'Primary Function': [
            'Where vessels dock; interface between maritime and terrestrial operations',
            'Buffer zone directly behind berth for container staging during loading/discharge operations',
            'Quay cranes (ship-to-shore cranes) transfer containers between vessel and apron',
            'Store containers awaiting vessel loading (exports) or truck pickup (imports); organized in blocks/bays',
            'Yard cranes move containers between storage locations and horizontal transport equipment',
            'Entry/exit point for external trucks; documentation verification, security checks, container exchange',
            'Central command center coordinating all terminal operations via Terminal Operating System (TOS)'
        ],
        'Key Equipment & Systems': [
            'Bollards, fenders, mooring equipment, vessel-to-shore power connections',
            'Prime movers (PM), Automated Guided Vehicles (AGV), chassis, container staging areas',
            'Ship-to-Shore (STS) cranes with 60-80m outreach, dual trolley systems, spreaders',
            'Rubber-Tyred Gantry (RTG), Rail-Mounted Gantry (RMG), Automated RMG (ARMG) cranes',
            'RTG/RMG/ARMG cranes, reach stackers, empty handlers, straddle carriers (some terminals)',
            'Optical Character Recognition (OCR) cameras, automated gates, truck appointment systems, weighbridges',
            'TOS software, communications systems, CCTV, vessel traffic monitoring, real-time data analytics'
        ],
        'Typical Dimensions & Capacity': [
            '300-450m berth length × 50-70m width per berth; accommodates 300-400m LOA vessels',
            '50-100m depth behind quay; provides staging for 100-200 containers during operations',
            '60-80m outreach spans 22-24 container rows; 40-50m lift height handles 8-10 tiers on vessel',
            '10-30 hectares per terminal; 20,000-50,000 ground slots; 6-8 containers high stacking',
            '1 yard crane per 3-5 hectares; 15-25 moves per hour productivity',
            '20-40 gate lanes; 200-400 truck transactions per hour capacity',
            'Central location with visibility across entire terminal; redundant systems for 24/7 operations'
        ],
        'Critical for Digital Twin': [
            'Berth occupancy modeling, vessel schedule optimization, BOA (Berth on Arrival) prediction',
            'Staging area utilization, quay crane productivity impact, horizontal transport queuing',
            'Crane allocation optimization, discharge/load sequence planning, interference avoidance',
            'Space utilization, container location tracking, dwell time analysis, re-handle minimization',
            'Yard crane workload balancing, travel distance minimization, simultaneous operations coordination',
            'Truck arrival patterns, gate processing time, appointment system optimization, peak period management',
            'Real-time decision support, predictive analytics, scenario simulation, KPI monitoring'
        ]
    })
    
    st.dataframe(terminal_zones, width='stretch', hide_index=True)
    
    st.markdown("""
    **Understanding Terminal Flow Patterns:**
    
    The lecture materials identify three primary cargo flow patterns through container terminals:
    
    **1. Import Flow (Vessel → Land Hinterland):**
    
    This flow handles containers arriving by vessel destined for local consumption or inland distribution:
    
    1. **Vessel arrives** and berths at **Quay** (pilot assistance, tugboat support, mooring operations)
    2. **Quay Crane discharges** containers from vessel → lowers to **Apron** staging area
    3. **Prime Mover/AGV** picks up container from apron → transports to **Storage Yard**
    4. **Yard Crane** lifts container from PM/AGV → stacks in designated **storage location**
    5. Container **dwells in yard** until truck arrival (typically 3-7 days, varies by port/cargo type)
    6. **Truck arrives** at **Gate Complex**, completes documentation and security checks
    7. **Yard Crane retrieves** container from storage → loads onto waiting truck
    8. **Truck exits** via gate to hinterland destination
    
    **Key Metric**: Import dwell time (time from vessel discharge to truck pickup) - target <5 days average
    
    **2. Export Flow (Land Hinterland → Vessel):**
    
    This flow handles containers arriving by truck destined for maritime transport:
    
    1. **Truck arrives** at **Gate Complex** with export container, completes entry procedures
    2. **Yard Crane** receives container from truck → places in **Export Storage Yard** location
    3. Container **dwells in yard** until vessel arrival (typically arrive 3-5 days before vessel, closing time varies)
    4. When **vessel scheduled**, yard crane retrieves container from storage
    5. **Prime Mover/AGV** transports container from yard to **Apron** staging area near assigned berth
    6. Containers **staged on apron** in loading sequence (specific order for vessel stowage plan)
    7. **Quay Crane** lifts container from apron → loads onto **vessel** in planned position
    8. **Vessel departs** when loading complete (typically 10-24 hours for full operation)
    
    **Key Metric**: Export dwell time (time from truck delivery to vessel loading) - target <4 days average
    
    **3. Transshipment Flow (Vessel → Vessel):**
    
    This flow handles containers transferred between vessels at the hub port (no land hinterland movement):
    
    1. **Container discharged** from arriving Vessel A to **Apron**
    2. **Prime Mover/AGV** transports to **Transshipment Yard** (often separate area from import/export yard)
    3. Container **dwells in yard** until connecting vessel arrives (ideally <24-48 hours for tight connections)
    4. **Yard Crane retrieves** container when Vessel B ready for loading
    5. **Prime Mover/AGV** transports to **Apron** for Vessel B
    6. **Quay Crane loads** onto Vessel B
    7. **Vessel B departs** with transshipped cargo continuing journey
    
    **Key Metric**: Transshipment dwell time - target <48 hours (enables "tight connections" critical for hub ports)
    
    **Singapore Context**: With 85-90% transshipment cargo, the transshipment flow dominates PSA operations. 
    Minimizing transshipment dwell time is critical for maintaining Singapore's hub competitiveness—shipping lines 
    demand fast, reliable connections between feeder and mainline vessels.
    """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>💡 Operational Efficiency Goals:</strong><br><br>
    Terminal operations aim to minimize four critical metrics:<br><br>
    1. <strong>Container dwell time</strong>: Minimize time containers spend in yard storage (reduces congestion, 
    improves yard utilization, faster cargo delivery)<br>
    2. <strong>Vessel port stay</strong>: Minimize total time from vessel arrival to departure (shipping lines pay 
    port dues by time, faster turnaround enables more voyages)<br>
    3. <strong>Equipment idle time</strong>: Keep cranes, prime movers, yard equipment actively working (maximize 
    asset utilization, reduce unit costs)<br>
    4. <strong>Re-handles</strong>: Minimize moving containers multiple times to access others underneath (each 
    re-handle costs 2-3 minutes, creates inefficiency)<br><br>
    <strong>World-class terminals like PSA Singapore achieve</strong>: <24-36 hour vessel turnaround for mega 
    vessels, <5 day average dwell time, <10% re-handle rate, >90% equipment utilization during operations.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 2: The Complete Container Terminal Operations Process
    # ============================================================================
    
    st.markdown('<p class="section-header">Container Terminal Operations: Complete Process Flow</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Container terminal operations follow a structured workflow from initial vessel notification through final 
    departure. The lecture materials emphasize that this process involves **four key planning processes** that must 
    be coordinated seamlessly: Berth Planning, Yard Planning, Stowage Planning, and Transportation Planning.
    
    Understanding this complete process flow is essential for operational planning and for developing digital twins 
    that accurately model terminal dynamics.
    """)
    
    st.markdown('<p class="subsection-header">Phase 1: Pre-Arrival Planning (72+ hours before vessel arrival)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Vessel Notification and Initial Planning:**
    
    Container terminal operations begin long before the physical vessel arrives. Shipping lines provide advance 
    notification of vessel arrival, allowing terminal planners to prepare.
    
    **Information Received from Shipping Line:**
    - **Vessel details**: Name, call sign, IMO number, dimensions (LOA, beam, draft), flag
    - **Estimated Time of Arrival (ETA)**: Initially rough estimate, refined as vessel approaches
    - **Container cargo manifest**: List of containers to discharge and load
    - **Discharge list**: Container numbers, types, weights, hazardous classifications, destinations
    - **Load list**: Export containers expected, weights, special requirements (reefers, OOG, hazardous)
    - **Special requirements**: Reefer connections, dangerous goods segregation, oversized cargo
    
    **Initial Planning Activities:**
    
    **1. Berth Planning (Preliminary):**
    - Determine which berth the vessel will use based on:
      - Vessel size and draft requirements
      - Quay crane availability at different berths
      - Conflicts with other scheduled vessels
      - Berth length and depth constraints
    - Reserve berth time slot in berth planning system
    - Coordinate with port authority (MPA in Singapore) for pilot and berth slot
    
    **2. Resource Estimation:**
    - Calculate required **quay cranes** based on container volume (typically 4-8 cranes for mega vessels)
    - Estimate **vessel operation time** (rules of thumb: 1,000 moves ≈ 10-12 hours with 4 cranes)
    - Identify **special equipment needs** (reefer connections, heavy lift cranes for OOG cargo)
    - Check **yard capacity** for expected import/transshipment containers
    
    **3. Yard Space Reservation:**
    - Reserve yard blocks for import containers (group by destination, shipping line, container type)
    - Confirm export container locations in yard (should already be receiving exports from trucks)
    - Reserve transshipment storage areas (separate from import/export to enable fast retrieval)
    
    **4. Communication with Stakeholders:**
    - Notify **customs** of pending arrival (begin import documentation processing)
    - Alert **stevedoring teams** for upcoming operation
    - Inform **trucking companies** of expected import container availability
    - Coordinate with **shipping line** on any special requirements or changes
    """)
    
    st.markdown('<p class="subsection-header">Phase 2: Detailed Operational Planning (24-48 hours before arrival)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    As the vessel approaches, planning becomes more detailed and specific. The lecture materials identify **four 
    key planning processes** that occur during this phase:
    
    **Planning Process 1: Berth Planning (Final Assignment)**
    
    **Objective**: Assign specific berth and time slot to each vessel, optimizing berth utilization.
    
    **Inputs**:
    - Updated vessel ETA (more accurate as vessel approaches)
    - Vessel specifications (LOA, beam, draft, container capacity)
    - Current berth occupancy and upcoming schedule
    - Expected handling time based on cargo volume
    
    **Planning Decisions**:
    - **Which berth**: Consider vessel size, crane availability, adjacent berth conflicts
    - **Arrival time window**: Coordinate with pilot service, tide/draft restrictions
    - **Berth on Arrival (BOA) feasibility**: Can vessel berth immediately or must wait at anchorage?
    - **Crane allocation**: Which cranes will serve this vessel (impacts berth choice)
    
    **Constraints**:
    - Berth length must exceed vessel LOA (typically require 50-100m additional space)
    - Berth depth must accommodate vessel draft (mega vessels require 16-18m depth)
    - Adjacent berth operations (cranes cannot interfere with neighboring berth operations)
    - Pilot availability and tidal windows (some ports tide-dependent)
    
    **Singapore Context**: PSA targets >90% Berth on Arrival (BOA)—vessels berth immediately without anchorage 
    wait. This requires excellent berth planning to ensure slot availability when vessels arrive.
    
    **Planning Process 2: Stowage Planning (Vessel Load Plan)**
    
    **Objective**: Determine exact position of each container on the vessel (bay-row-tier coordinates).
    
    **This is one of the most complex planning problems in terminal operations.** The stowage planner must balance 
    multiple competing constraints and objectives:
    
    **Key Constraints**:
    
    **1. Structural/Safety Constraints:**
    - **Weight limits**: Heavier containers on bottom, lighter on top (vessel stability)
    - **Stack weight limits**: Maximum weight each container can support (crushing prevention)
    - **Hatch cover strength**: Containers on hatch covers have lower weight limits than in holds
    - **Dangerous goods segregation**: IMO regulations require minimum separation distances
    
    **2. Operational Constraints:**
    - **Port sequence**: Containers for later ports must be accessible (can't put Hong Kong container under 
      Singapore container if Singapore is first port)
    - **Discharge efficiency**: Containers for same port should be grouped together (minimize crane travel)
    - **Loading efficiency**: Export containers should be near crane position when needed
    
    **3. Equipment Constraints:**
    - **Reefer positions**: Refrigerated containers require power connections (limited reefer slots on vessel)
    - **OOG positions**: Oversized cargo cannot stack (needs flat rack positions on deck)
    - **Heavy containers**: Weight distribution for vessel balance (fore/aft and port/starboard)
    
    **Stowage Planning Process**:
    
    1. **Group containers** by destination port, weight class, type (standard, reefer, OOG, hazardous)
    2. **Allocate bays** to each destination port along vessel's route
    3. **Assign positions** within bays considering weight, accessibility, equipment constraints
    4. **Balance vessel**: Check stability (GM), draft (fore/aft trim), stress on hull
    5. **Generate bay plans**: Document showing each container's position (bay-row-tier coordinate system)
    6. **Validate plan**: Check for constraint violations, optimize crane work sequences
    
    **Output**: Complete stowage plan showing every container's position, used by crane operators during loading.
    
    **Planning Process 3: Yard Planning (Storage Location Assignment)**
    
    **Objective**: Allocate specific yard storage locations for import containers and identify export container 
    locations for efficient retrieval.
    
    **Import Container Yard Planning**:
    
    **Grouping Strategy**:
    - **By destination**: Containers going to same location together (reduces truck travel in yard)
    - **By shipping line**: Keep each shipping line's containers in dedicated blocks
    - **By container type**: Reefers near power sources, OOG in special areas, dangerous goods in segregated zones
    - **By discharge sequence**: Consider which containers discharged first/last (impacts stacking)
    
    **Storage Location Factors**:
    - **Accessibility**: High-turnover containers (picked up quickly) in easily accessible positions
    - **Stacking height**: Heavier containers on bottom, consider maximum stack height (6-8 containers typical)
    - **Re-handle minimization**: Predict pickup sequence, stack accordingly to avoid moving containers twice
    - **Yard capacity**: Balance utilization across yard blocks (avoid overloading specific areas)
    
    **Export Container Yard Management**:
    
    **Receiving Strategy**:
    - Export containers arrive by truck in days before vessel
    - Must track location of each export container in yard
    - Verify container availability against load list (flag no-shows early)
    
    **Retrieval Planning**:
    - Plan retrieval sequence matching vessel loading plan
    - Stage export containers on apron in loading order (enables efficient crane operations)
    - Coordinate yard crane scheduling to retrieve containers just-in-time for loading
    
    **Planning Process 4: Transportation Planning (Equipment Scheduling)**
    
    **Objective**: Coordinate all equipment movements to execute the operational plan efficiently.
    
    **Quay Crane Allocation and Sequencing**:
    
    **Crane Assignment**:
    - Determine **crane intensity**: How many cranes to assign to vessel (typically 4-8 for mega vessels)
    - More cranes = faster operation, but diminishing returns due to crane interference
    - Assign specific cranes to specific bays on vessel (prevents cranes crossing paths)
    
    **Crane Work Sequence**:
    - **Discharge sequence**: Which containers to discharge in what order
    - **Loading sequence**: Follow stowage plan for export container loading
    - **Hatch cover operations**: Coordinate opening/closing of vessel holds
    - **Productivity target**: 30-40 Gross Moves Per Hour (GMPH) per crane
    
    **Horizontal Transport (Prime Movers / AGVs)**:
    
    The lecture materials distinguish between two approaches for moving containers between quay and yard:
    
    **Prime Mover (PM) Deployment**:
    - **Traditional approach**: Human-driven trucks with chassis/trailers
    - **Fixed assignment strategy**: 2 PMs assigned to each quay crane (dedicated service)
    - **Challenge**: PMs often travel empty on return trip (quay→yard loaded, yard→quay empty)
    - **Pooling strategy**: Fleet of PMs shared across all cranes (computer dispatches to next job)
    - **Hybrid approach**: Core PMs fixed to cranes, additional PMs pooled for overflow
    
    **AGV (Automated Guided Vehicle) Deployment**:
    - **Modern approach**: Battery-powered, computer-controlled autonomous vehicles
    - **Pooling strategy**: Fleet shared across all cranes (no fixed assignments)
    - **Dynamic dispatch**: AGV system calculates optimal assignment in real-time
    - **Bi-directional loading**: Can carry container both directions (quay→yard, yard→quay)
    - **Benefits**: Higher utilization, less empty travel, 24/7 operations, predictable performance
    
    **Dispatching Optimization**:
    - **Objective**: Minimize quay crane waiting time (always have PM/AGV ready when crane ready)
    - **Constraint**: Minimize empty travel distance (reduces fuel/energy, increases fleet productivity)
    - **Balancing**: Keep fleet size small (cost) while maintaining high service level (crane productivity)
    
    **Yard Crane Scheduling**:
    - Assign yard cranes to specific blocks
    - Schedule retrieve operations (export containers for loading)
    - Schedule placement operations (import containers from discharge)
    - Balance workload across yard cranes
    - Coordinate with horizontal transport (PM/AGV) arrival times
    """)
    
    st.markdown('<p class="subsection-header">Phase 3: Vessel Operations (During Port Stay)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Operational Execution Phase:**
    
    When the vessel physically arrives, all planning must execute seamlessly while adapting to real-time changes.
    
    **Vessel Arrival Sequence**:
    
    **1. Pilot Boarding and Navigation (1-1.5 hours)**:
    - Vessel arrives at **pilot boarding ground** (typically 3-5 nautical miles offshore)
    - **Maritime pilot** boards vessel via pilot boat (licensed by port authority to navigate local waters)
    - Pilot takes command of vessel navigation (captain retains overall command but defers to pilot's local knowledge)
    - **Tugboats** rendezvous with vessel (typically 2-4 tugs for large vessels)
    - Pilot navigates vessel through harbor approaches to assigned berth
    
    **2. Berthing and Mooring (30-45 minutes)**:
    - Tugboats maneuver vessel into berth position (push/pull to align with berth)
    - **Line handlers** on quay receive mooring lines from vessel
    - Vessel secured with multiple **mooring lines** to bollards (typically 8-12 lines)
    - **Fenders** between vessel and quay absorb movement and prevent hull damage
    - **Gangway** deployed for crew/personnel access between vessel and shore
    
    **3. Pre-Operations Setup (30-60 minutes)**:
    - **Safety inspection**: Terminal safety officer inspects vessel, confirms safe for operations
    - **Cargo documentation exchange**: Final cargo lists, bay plans, special instructions transferred
    - **Lashing/unlashing crew**: Begin removing container securing equipment (twist locks, lashing rods)
    - **Hatch cover removal**: Open vessel holds to expose containers below deck
    - **Reefer connections**: Identify and prepare to connect power to refrigerated containers
    - **Quay crane positioning**: Move assigned cranes into position along vessel
    
    **4. Discharge Operations (typically 8-14 hours for mega vessel)**:
    
    **Crane Operations**:
    - **Crane operator** in crane cab controls all movements (trained specialists, highly skilled role)
    - **Spreader** (crane attachment device) positioned over target container
    - **Twist locks** engage container corner castings (automatic locking mechanism)
    - Container **lifted** from vessel (operators must clear vessel rails, avoid obstacles)
    - **Trolley travels** horizontally along crane boom toward apron
    - Container **lowered** to apron staging area
    - **Spreader releases** container (twist locks disengage automatically)
    
    **Horizontal Transport**:
    - **Prime mover/AGV** positions under spreader to receive container
    - Once crane releases, PM/AGV transports container to yard
    - **Travel time**: Typically 3-5 minutes depending on yard distance
    - Arrives at designated yard block
    
    **Yard Operations**:
    - **Yard crane** picks up container from PM/AGV
    - **Stacks** container in planned storage location
    - PM/AGV returns to quay for next container
    - Process repeats until all discharge containers removed
    
    **Productivity Measurement**:
    - **Gross Moves Per Hour (GMPH)**: Total moves (including delays) / total time
    - **Target**: 30-40 GMPH per crane (world-class performance)
    - **Factors affecting productivity**: Crew skill, equipment reliability, weather, vessel stow complexity
    
    **5. Loading Operations (typically 10-16 hours for mega vessel)**:
    
    **Retrieval Process**:
    - **Yard cranes** retrieve export containers from storage locations
    - Sequence follows vessel stowage plan (bottom containers loaded first, etc.)
    - **PM/AGV** transports containers to apron staging area
    - Containers **staged on apron** in loading sequence order
    
    **Crane Loading**:
    - **Quay crane** picks up container from apron staging
    - **Lifts and travels** to vessel position
    - **Lowers** container into designated bay-row-tier position
    - **Spreader releases** container
    - **Lashing crew** secures container (twist locks, lashing rods, stacking cones)
    
    **Concurrent Operations**:
    - Discharge and loading often occur **simultaneously**
    - Different cranes work on different bays (fore/mid/aft sections of vessel)
    - Complex coordination required to avoid crane interference
    - Horizontal transport must serve both discharge and loading operations
    
    **6. Post-Operations and Departure (1-1.5 hours)**:
    
    **Final Activities**:
    - **Hatch covers replaced** and secured (close vessel holds)
    - **Final lashing inspection**: Verify all containers properly secured for sea voyage
    - **Reefer connections verified**: Confirm all refrigerated containers have power
    - **Paperwork completion**: Final cargo manifest, dangerous goods declaration, customs clearance
    - **Gangway removed**, shore connections disconnected
    
    **Departure Sequence**:
    - **Mooring lines released** and retrieved to vessel
    - **Tugboats** maneuver vessel away from berth
    - **Pilot** navigates vessel out of harbor
    - Pilot disembarks at pilot boarding ground
    - Vessel proceeds to next port
    
    **Typical Timeline Example** (Mega Vessel with 2,000 moves):
    - Arrival and mooring: 1.5 hours
    - Pre-operations: 1.0 hours
    - Discharge operations: 8.0 hours (1,000 imports)
    - Loading operations: 10.0 hours (1,200 exports)
    - Post-operations: 1.0 hours
    - Departure: 0.5 hours
    - **Total port stay: 22 hours** (excellent performance, achieves <24 hour turnaround target)
    """)
    
    st.markdown("""
    <div class="success-box">
    <strong>✅ World-Class Terminal Performance Benchmarks:</strong><br><br>
    <strong>PSA Singapore and top-tier terminals achieve</strong>:<br>
    • <strong>Berth on Arrival (BOA) >90%</strong>: Vessels berth immediately without anchorage wait<br>
    • <strong>Vessel turnaround <24-36 hours</strong>: For mega vessels with 2,000-3,000 container moves<br>
    • <strong>Crane productivity 35-40 GMPH</strong>: Gross moves per hour per crane (including all delays)<br>
    • <strong>Container dwell time <5 days</strong>: Average time from discharge to pickup (imports)<br>
    • <strong>Re-handle rate <10%</strong>: Percentage of containers moved multiple times in yard<br>
    • <strong>Equipment availability >95%</strong>: Percentage of time equipment operational (not broken down)<br><br>
    These metrics represent <strong>operational excellence</strong> achieved through sophisticated planning systems, 
    skilled workforce, well-maintained equipment, and continuous process improvement.
    </div>
    """, unsafe_allow_html=True)
    
    # Vessel operation timeline visualization
    operation_phases = pd.DataFrame({
        'Phase': ['Arrival & Mooring', 'Pre-Operations', 'Discharge', 'Loading', 'Post-Operations', 'Departure'],
        'Duration (hours)': [1.5, 1.0, 8.0, 10.0, 1.0, 0.5],
        'Key Activities': [
            'Pilot boarding, tugboat assist, vessel moors, gangway deployed',
            'Safety check, lashing crew, hatch cover removal, documentation exchange',
            '1,000 import containers discharged (4 cranes, 8 hours, 31 GMPH)',
            '1,200 export containers loaded (4 cranes, 10 hours, 30 GMPH)',
            'Hatch covers closed, lashing inspection, final paperwork, disconnections',
            'Lines released, tugboat assist, pilot navigates out, vessel departs'
        ]
    })
    
    # Create timeline visualization
    fig = go.Figure()
    
    cumulative = 0
    colors = ['#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6', '#EC4899']
    
    for idx, row in operation_phases.iterrows():
        fig.add_trace(go.Bar(
            y=[row['Phase']],
            x=[row['Duration (hours)']],
            orientation='h',
            name=row['Phase'],
            text=f"{row['Duration (hours)']}h",
            textposition='inside',
            marker=dict(color=colors[idx]),
            hovertemplate=f"<b>{row['Phase']}</b><br>{row['Key Activities']}<br>Duration: {row['Duration (hours)']} hours<extra></extra>"
        ))
    
    fig.update_layout(
        title='Typical Vessel Operation Timeline (2,000 Container Moves)',
        xaxis_title='Hours',
        yaxis_title='Operation Phase',
        showlegend=False,
        height=400,
        barmode='stack'
    )
    
    st.plotly_chart(fig, width='stretch')
    
    # ============================================================================
    # SECTION 3: Equipment Types and Coordination
    # ============================================================================
    
    st.markdown('<p class="section-header">Terminal Equipment: The Physical Assets</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Container terminal operations depend on sophisticated equipment working in coordinated sequences. The lecture 
    materials categorize equipment by operational zone: quay-side equipment (ship-to-shore), yard equipment (storage 
    handling), and horizontal transport (moving containers between zones).
    """)
    
    st.markdown('<p class="subsection-header">Quay-Side Equipment: Ship-to-Shore (STS) Cranes</p>', unsafe_allow_html=True)
    
    # STS Crane specifications
    sts_specs = pd.DataFrame({
        'Specification': [
            'Outreach (Reach across vessel)',
            'Lift Height',
            'Lifting Capacity',
            'Hoist Speed',
            'Trolley Speed',
            'Crane Travel Speed',
            'Productivity Target',
            'Cost',
            'Lifespan'
        ],
        'Modern STS Crane (Mega Vessel Capable)': [
            '60-80 meters (spans 22-24 container rows)',
            '40-50 meters above rail (handles 8-10 tiers on vessel + clearance)',
            '65-85 tonnes under spreader (2× 40ft laden containers)',
            '60-90 meters/minute (faster = higher productivity)',
            '180-240 meters/minute (boom trolley horizontal movement)',
            '30-45 meters/minute (crane moves along quay rails)',
            '35-40 Gross Moves Per Hour (GMPH) including all delays',
            'US$10-18 million per crane (new)',
            '25-35 years with proper maintenance and upgrades'
        ],
        'Technology Features': [
            'Twin-lift/Tandem-lift capability (handle 2 containers simultaneously)',
            'Automated container positioning (semi-automated lowering/raising)',
            'Anti-sway systems (reduce pendulum motion, speeds up operations)',
            'Dual trolley design (separate hoist/trolley for landside operations)',
            'Automated spreader twist-lock (engage/disengage corner castings)',
            'Remote monitoring sensors (vibration, load, position, maintenance predictions)',
            'LED lighting + CCTV (operator visibility, safety, remote supervision)',
            'Variable speed drives (energy efficient, smooth acceleration/deceleration)',
            'Diesel + electric hybrid (reduce fuel consumption, emissions)'
        ]
    })
    
    st.dataframe(sts_specs, width='stretch', hide_index=True)
    
    st.markdown("""
    **Understanding GMPH (Gross Moves Per Hour):**
    
    GMPH is the primary productivity metric for quay cranes. It measures total container moves divided by total 
    operation time, including all delays.
    
    **What counts as a "move":**
    - One container lifted from vessel and placed on apron = 1 move (discharge)
    - One container lifted from apron and placed on vessel = 1 move (loading)
    - Twin-lift (2 containers simultaneously) = 2 moves
    
    **What's included in "gross" time:**
    - Actual lifting and lowering operations
    - Trolley travel time (horizontal movement along boom)
    - Crane travel time (moving to different bay along vessel)
    - Waiting time (for PM/AGV to arrive, for yard to provide container, operator breaks)
    - Hatch cover operations (opening/closing holds)
    - Lashing operations (securing/unsecuring containers)
    - All delays and interruptions
    
    **Productivity Levels:**
    - **Below 25 GMPH**: Poor performance, indicates problems (equipment, planning, or skill issues)
    - **25-30 GMPH**: Average performance (acceptable but room for improvement)
    - **30-35 GMPH**: Good performance (well-operated terminal)
    - **35-40 GMPH**: Excellent performance (world-class operations like PSA Singapore)
    - **Above 40 GMPH**: Exceptional (requires perfect conditions, highly automated, expert crews)
    
    **Factors Affecting GMPH:**
    - **Crane operator skill**: Expert operators 20-30% more productive than novices
    - **Vessel stow complexity**: Simple stow (all containers accessible) vs complex (many re-handles on vessel)
    - **Horizontal transport efficiency**: Crane waits if PM/AGV not available when needed
    - **Weather**: High winds (>25 knots) slow operations or halt for safety
    - **Equipment reliability**: Breakdowns stop productivity
    - **Container characteristics**: Heavy/oversize containers take longer to handle safely
    """)
    
    st.markdown('<p class="subsection-header">Yard Equipment: Storage and Retrieval</p>', unsafe_allow_html=True)
    
    # Yard equipment comparison
    yard_equipment = pd.DataFrame({
        'Equipment Type': [
            'RTG - Rubber-Tyred Gantry',
            'RMG - Rail-Mounted Gantry',
            'ARMG - Automated RMG',
            'Reach Stacker',
            'Straddle Carrier'
        ],
        'Description': [
            'Gantry crane on rubber tyres, spans 6-8 container widths, diesel-powered, operator-driven',
            'Gantry crane on fixed rails, electric-powered, spans 6-8 container widths, operator-driven',
            'Fully automated RMG, computer-controlled, no human operator, electric-powered',
            'Mobile crane with telescopic boom, picks up containers from top, diesel, operator-driven',
            'Mobile vehicle that straddles container, lifts and carries, diesel, operator-driven'
        ],
        'Stacking Height': ['6-7 containers (1-over-6)', '8-10 containers (1-over-9)', '10-12 containers (1-over-11)', '4-5 containers', '3-4 containers'],
        'Productivity': ['15-25 moves/hour', '20-30 moves/hour', '25-35 moves/hour', '8-12 moves/hour', '10-15 moves/hour'],
        'Flexibility': ['High (can move anywhere in yard)', 'Low (fixed to rail block)', 'Low (fixed to rail block)', 'Very high (goes anywhere)', 'Very high (goes anywhere)'],
        'Labor': ['1 operator per crane', '1 operator per crane', 'Zero operators (automated)', '1 operator per unit', '1 operator per unit'],
        'Cost': ['US$2-3M', 'US$3-5M', 'US$5-8M + automation systems', 'US$300-500K', 'US$600K-1M'],
        'Best Use Case': [
            'Flexible yard operations, multiple blocks, growing terminals',
            'High-volume terminals, dense stacking, long-term fixed layout',
            'Fully automated terminals (Tuas), 24/7 operations, labor reduction',
            'Empty container handling, low-volume areas, supplemental equipment',
            'Small terminals, transshipment operations, combined transport-stacking'
        ]
    })
    
    st.dataframe(yard_equipment, width='stretch', hide_index=True)
    
    st.markdown("""
    **Automation Evolution in Yard Equipment:**
    
    The maritime industry is progressively automating yard operations to reduce labor costs, increase productivity, 
    and enable 24/7 operations:
    
    **Level 1 - Manual (Traditional)**: RTG/RMG with human operators in crane cab
    - Operator skill critical for productivity
    - Requires training, workforce management, labor costs
    - Subject to human factors (fatigue, variability)
    
    **Level 2 - Semi-Automated**: RMG with remote operation
    - Operators sit in control room, control cranes remotely via cameras
    - Reduces operator fatigue (comfortable office environment)
    - Multiple operators can cover more cranes (improved efficiency)
    - Safer (operators not on moving equipment)
    
    **Level 3 - Highly Automated**: ARMG with automated container handling
    - Computer system controls crane movements automatically
    - Human supervisor monitors multiple cranes, intervenes only if needed
    - Consistent productivity (no human variability)
    - 24/7 operations without night-shift labor premium
    
    **Level 4 - Fully Automated**: ARMG + AGV + automated gates (complete automation)
    - Entire terminal operates with minimal human intervention
    - Computer systems coordinate all equipment
    - Humans monitor systems, handle exceptions, perform maintenance
    - Ultimate efficiency but requires massive upfront investment
    
    **Singapore's Approach**: PSA's Tuas Mega Port deploying Level 4 automation (ARMGs + AGVs) as new capacity 
    comes online. Existing terminals use mix of RTG/RMG with progressive automation upgrades.
    """)
    
    st.markdown('<p class="subsection-header">Horizontal Transport: Prime Movers vs AGVs</p>', unsafe_allow_html=True)
    
    # PM vs AGV comparison
    pm_agv_comparison = pd.DataFrame({
        'Characteristic': [
            'Operation',
            'Navigation',
            'Productivity',
            'Flexibility',
            'Safety',
            'Emissions',
            'Consistency',
            'Cost per Unit',
            'Infrastructure Required',
            'Labor',
            'Operating Hours',
            'Maintenance'
        ],
        'Prime Mover (PM) - Traditional': [
            'Human-driven truck with trailer/chassis',
            'Driver navigates using roads, signage',
            '4-6 cycles/hour (quay-yard round trip)',
            'Very high (can adapt to any situation)',
            'Human error risks (accidents, damage)',
            'Diesel emissions (NOx, particulates)',
            'Variable (depends on driver skill, fatigue)',
            'US$100-150K per unit',
            'Roads, signage, parking areas',
            '1 driver per PM (plus relief drivers)',
            'Daytime shifts (night shift premium costs)',
            'Regular diesel engine maintenance'
        ],
        'Automated Guided Vehicle (AGV) - Modern': [
            'Battery-electric autonomous vehicle',
            'Magnetic/optical guidance + sensors + GPS + computer control',
            '8-12 cycles/hour (higher due to bi-directional loading, optimal routing)',
            'Medium (requires programmed routes, infrastructure)',
            'Very high (no human operators in operational zones, obstacle detection)',
            'Zero local emissions (electric, charged from grid)',
            'Very high (consistent performance 24/7, no fatigue)',
            'US$300-500K per unit (plus infrastructure: US$5-10M for charging, guidance)',
            'Magnetic markers / optical lines, charging stations, central control system',
            'Zero drivers (remote monitoring technicians only)',
            '24/7 operations (no labor constraints, battery rotation)',
            'Battery replacement cycles, electronic systems (more predictable than diesel)'
        ]
    })
    
    st.dataframe(pm_agv_comparison, width='stretch', hide_index=True)
    
    st.markdown("""
    **Singapore Deployment Strategy:**
    - **Legacy terminals** (Pasir Panjang, Keppel, Brani): Use Prime Mover fleet with pooling strategy for flexibility
    - **Tuas Mega Port** (new development): Deploying full AGV fleet from design phase (65+ AGVs per berth pair, scalable)
    - **Transition approach**: Gradual automation as old terminals decommissioned, new Tuas capacity comes online
    """)
    
    st.markdown("""
    **Economics of AGV Investment:**
    
    **Why terminals invest in AGVs despite 3-5× higher unit cost:**
    
    **Labor Savings** (Primary Benefit):
    - **PM approach**: 2 PMs per quay crane × 8 quay cranes = 16 PMs × 2 drivers per PM (24/7 shifts) = 32 drivers
    - **AGV approach**: 65 AGVs serving same 8 cranes with zero drivers
    - **Annual labor cost savings**: 32 drivers × US$60K average salary = ~US$2M per year
    - **Payback period**: AGV fleet cost US$20M (65 AGVs) + infrastructure US$10M = US$30M / US$2M savings = 
      15 years payback
    - **Actual payback**: Shorter (8-12 years) considering productivity gains, 24/7 operations, reduced accidents
    
    **Productivity Gains** (Secondary Benefit):
    - AGVs achieve 30-40% higher cycle rates through optimal routing and bi-directional loading
    - Enables same throughput with smaller fleet size (capital efficiency)
    - Consistent performance eliminates human variability in productivity
    
    **Operational Advantages**:
    - 24/7 operations without night-shift labor premiums
    - No training requirements (new PMs need 3-6 months training)
    - Predictable performance (easier planning, scheduling)
    - Safety improvements (fewer accidents, operator injuries)
    
    **When AGVs Make Sense:**
    - New terminal development (Tuas) - design with AGVs from start
    - High labor costs (Singapore, Europe, Japan) - payback faster
    - Large scale operations (>2M TEU/year) - volumes justify investment
    - Government support for automation (Singapore government backing for Tuas automation)
    
    **When PMs Still Preferred:**
    - Existing terminals with PM infrastructure already in place (retrofit cost prohibitive)
    - Lower labor cost countries (Southeast Asia, Africa) - longer payback period
    - Smaller terminals (<500K TEU/year) - insufficient scale
    - High layout flexibility needs (frequent changes) - PMs more adaptable
    """)
    
    # ============================================================================
    # SECTION 4: Terminal Operating System (TOS)
    # ============================================================================
    
    st.markdown('<p class="section-header">Terminal Operating System (TOS): The Digital Brain</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The Terminal Operating System (TOS) is the integrated software platform that plans, executes, and monitors all 
    terminal operations. The lecture materials emphasize that the TOS is essentially the **"brain"** of the terminal, 
    coordinating thousands of decisions and actions across berth planning, yard management, equipment scheduling, 
    and gate operations.
    
    Without a sophisticated TOS, modern container terminals could not achieve the efficiency levels required by 
    today's shipping industry. Understanding TOS architecture and capabilities is essential for digital twin development.
    """)
    
    st.markdown('<p class="subsection-header">Core TOS Modules and Functions</p>', unsafe_allow_html=True)
    
    # TOS modules breakdown
    tos_modules = pd.DataFrame({
        'TOS Module': [
            'Berth Planning Module',
            'Vessel Planning Module',
            'Yard Planning Module',
            'Resource Planning Module',
            'Equipment Control Module',
            'Gate Operating System (GOS)',
            'EDI Integration Module',
            'Reporting & Analytics'
        ],
        'Primary Functions': [
            'Berth allocation, vessel scheduling, BOA optimization, pilot coordination, quay crane assignment',
            'Stowage planning, discharge/load lists, bay plan generation, vessel stability calculations',
            'Storage location assignment, yard utilization optimization, re-handle minimization, container tracking',
            'Labor scheduling, equipment allocation, maintenance planning, shift management',
            'Real-time equipment dispatch (QC, YC, PM/AGV), dynamic routing, workload balancing, exception handling',
            'Truck appointment scheduling, OCR integration, automated gate processing, documentation verification',
            'PORTNET integration, shipping line systems, customs (TradeNet), trucking companies, rail operators',
            'KPI dashboards, operational reports, productivity analysis, predictive analytics, decision support'
        ],
        'Key Algorithms & Optimization': [
            'Berth window optimization, vessel arrival sequencing, crane-to-berth matching, conflict resolution',
            'Weight distribution algorithms, stowage constraints checking, sequence optimization, bay plan validation',
            'Clustering algorithms (group similar containers), stack optimization, retrieval sequencing, space allocation',
            'Shift planning, skill matching, equipment maintenance scheduling, resource leveling',
            'Dynamic dispatching, shortest path routing, load balancing, traffic management, collision avoidance (AGVs)',
            'Queue management, appointment slot allocation, lane assignment, throughput optimization',
            'Real-time data exchange, message queuing, error handling, system integration',
            'Data aggregation, real-time KPI calculation, trend analysis, anomaly detection, forecasting'
        ],
        'Typical Response Time': [
            'Seconds to minutes (updated as vessels arrive/depart)',
            'Minutes to hours (detailed planning as ETA approaches)',
            'Real-time (milliseconds for queries, seconds for optimization)',
            'Hours to days (shift schedules, maintenance windows)',
            'Real-time (milliseconds for dispatch decisions, AGV routing)',
            'Seconds (gate transaction processing, instant validation)',
            'Real-time (asynchronous messaging, event-driven)',
            'Real-time dashboards, batch reports (hourly/daily/weekly)'
        ]
    })
    
    st.dataframe(tos_modules, width='stretch', hide_index=True)
    
    st.markdown("""
    **PSA's CITOS: A Case Study in TOS Excellence**
    
    The lecture materials specifically mention PSA's proprietary Terminal Operating System called **CITOS** (Container 
    Terminal Information and Operating System). Understanding CITOS provides insights into world-class TOS capabilities:
    
    **CITOS Development History:**
    - **Developed in-house by PSA** starting in the 1980s (not purchased from vendor)
    - **Continuous evolution** over 40+ years of operational refinement
    - **Battle-tested** handling world's largest transshipment volumes (Singapore handles 41.12M TEU in 2024)
    - **Deployed globally** across PSA terminals worldwide (Singapore, Europe, Americas, Asia)
    
    **Why PSA Developed CITOS In-House (Strategic Rationale):**
    
    1. **Competitive Advantage**: Proprietary TOS creates differentiation vs competitors using commercial TOS products
    2. **Customization**: Can tailor exactly to PSA's operational philosophy and requirements
    3. **Rapid Innovation**: No vendor dependency, can implement new features immediately
    4. **Cost**: Long-term cost savings vs paying licensing fees to vendors
    5. **IP Protection**: Core operational know-how embedded in software, protected from competitors
    
    **CITOS Core Capabilities:**
    
    **1. Advanced Optimization Algorithms:**
    - **Berth planning**: Optimizes vessel-to-berth allocation considering multiple constraints
    - **Yard planning**: Minimizes re-handles through predictive container grouping
    - **Equipment dispatching**: Dynamic PM/AGV assignment optimizing productivity and travel distance
    - **Load sequencing**: Generates efficient crane work sequences
    
    **2. Real-Time Operations Management:**
    - **Live terminal view**: Visualizes all equipment, containers, operations in real-time
    - **Exception handling**: Alerts operators to problems (equipment breakdowns, no-shows, delays)
    - **Dynamic re-planning**: Automatically adjusts plans when disruptions occur
    - **Performance monitoring**: Tracks KPIs (crane productivity, dwell time, gate throughput) continuously
    
    **3. Integration with Physical Systems:**
    - **Crane interfaces**: Sends work instructions directly to crane operators, receives completion confirmations
    - **AGV control system**: Dispatches AGVs, monitors battery levels, coordinates routing
    - **Gate automation**: Integrates with OCR cameras, automated gates, truck appointment systems
    - **PORTNET**: Singapore's maritime single window for documentation, customs clearance
    
    **4. Data Analytics and AI/ML:**
    - **Predictive analytics**: Forecasts berth occupancy, yard utilization, gate traffic
    - **Machine learning**: Continuously improves optimization algorithms based on operational data
    - **Anomaly detection**: Identifies unusual patterns indicating potential problems
    - **What-if simulation**: Allows planners to test different scenarios before execution
    
    **5. Mobile and Cloud Capabilities:**
    - **Mobile apps**: Enable supervisors, operators to access CITOS functions from field
    - **Cloud deployment**: Modern architecture supports distributed operations, disaster recovery
    - **API access**: Allows shipping lines, trucking companies to integrate with CITOS
    
    **CITOS Competitive Impact:**
    
    PSA's CITOS provides several competitive advantages that are difficult for competitors to replicate:
    
    1. **Operational Excellence**: Enables PSA to consistently achieve industry-leading productivity (35-40 GMPH, 
       >90% BOA, <24 hour turnaround)
    2. **Global Standardization**: Same TOS across all PSA terminals enables best practice sharing, consistent service
    3. **Innovation Platform**: In-house development enables rapid deployment of new capabilities (AI, ML, digital twins)
    4. **Customer Integration**: Deep API integration allows shipping lines to directly access PSA systems (competitive 
       differentiator)
    5. **Data Advantage**: Decades of operational data from world's busiest port improves algorithms continuously
    
    **Implications for Digital Twin Development:**
    
    The digital twin must interface with TOS (CITOS in PSA's case) to access real-time operational data and 
    provide decision support:
    - **Data feeds**: Terminal digital twin receives real-time data from CITOS (vessel positions, equipment status, 
      container locations)
    - **Simulation scenarios**: Digital twin can test "what-if" scenarios independently, then recommend actions to CITOS
    - **Predictive insights**: Digital twin provides predictions (future berth occupancy, potential bottlenecks) that 
      CITOS uses for planning
    - **Optimization suggestions**: Digital twin suggests equipment schedules, container stow plans that CITOS can adopt
    
    The relationship is symbiotic: CITOS provides ground truth operational data; digital twin provides predictive 
    insights and scenario analysis that enhance CITOS planning capabilities.
    """)
    
    # ============================================================================
    # SECTION 5: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways: Container Terminal Operations</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Terminal Layout and Flows:**
        - Seven operational zones: Berth/Quay, Apron, QC Zone, Storage Yard, YC Zone, Gate, Control Tower
        - Three flow patterns: Import (vessel→land), Export (land→vessel), Transshipment (vessel→vessel)
        - Singapore 85-90% transshipment: Minimize transshipment dwell time critical for hub competitiveness
        - Operational efficiency goals: Minimize dwell time, vessel stay, equipment idle time, re-handles
        
        **Complete Operations Process:**
        - **Phase 1 (72+ hours)**: Pre-arrival planning, vessel notification, initial resource estimation
        - **Phase 2 (24-48 hours)**: Four key planning processes (berth, stowage, yard, transportation)
        - **Phase 3 (during port stay)**: Execution (arrival, berthing, discharge, loading, departure)
        - Typical mega vessel turnaround: 22-24 hours (PSA Singapore target <24 hours)
        
        **Four Key Planning Processes:**
        - **Berth Planning**: Vessel-to-berth allocation, BOA optimization (PSA >90% BOA)
        - **Stowage Planning**: Container position on vessel (bay-row-tier), complex constraint optimization
        - **Yard Planning**: Storage location assignment, grouping strategy, re-handle minimization
        - **Transportation Planning**: Equipment scheduling (QC/YC/PM/AGV coordination)
        """)
    
    with col2:
        st.markdown("""
        **Equipment and Technology:**
        - **Quay Cranes**: US$10-18M, 60-80m outreach, target 35-40 GMPH productivity
        - **Yard Equipment**: RTG (flexible), RMG (efficient), ARMG (automated), progressive automation
        - **Horizontal Transport**: Prime Movers (traditional) vs AGVs (modern automated)
        - **AGV benefits**: 70-80% labor reduction, 24/7 operations, 30-40% higher cycle rates
        
        **Terminal Operating System (TOS):**
        - The "brain" coordinating all terminal operations
        - Core modules: Berth, Vessel, Yard, Resource, Equipment, Gate, EDI, Analytics
        - **PSA's CITOS**: In-house developed, 40+ years evolution, deployed globally
        - Competitive advantage through proprietary algorithms, real-time optimization, AI/ML
        
        **World-Class Performance:**
        - **BOA >90%**: Berth on arrival without anchorage wait
        - **Crane productivity 35-40 GMPH**: Including all delays, world-leading
        - **Vessel turnaround <24 hours**: For 2,000-move mega vessels
        - **Dwell time <5 days**: Average import container yard residence
        - **Re-handle rate <10%**: Minimize unproductive container moves
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Container terminal operations involve intricate coordination across seven 
    operational zones (berth, apron, quay cranes, yard, yard cranes, gate, control tower) handling three distinct 
    cargo flows (import, export, transshipment—with Singapore 85-90% transshipment). Success requires excellence 
    in <strong>four key planning processes</strong>: berth planning (optimal vessel scheduling achieving >90% BOA), 
    stowage planning (complex container position optimization on vessels), yard planning (storage strategy minimizing 
    re-handles), and transportation planning (equipment coordination maximizing productivity). Operations execute 
    through sophisticated equipment ($10-18M quay cranes, automated yard systems, AGV fleets) orchestrated by 
    <strong>Terminal Operating Systems</strong> like PSA's proprietary CITOS that provide real-time optimization, 
    predictive analytics, and seamless integration. <strong>World-class terminals like PSA Singapore</strong> achieve 
    35-40 GMPH crane productivity, <24-hour mega vessel turnaround, and >90% Berth on Arrival through operational 
    excellence, advanced technology, and continuous improvement. Understanding these operations is essential for 
    developing digital twins that accurately model terminal dynamics and provide actionable decision support for 
    operational planning and optimization.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** 🚢 Tuas Mega Port Development - Explore Singapore's S$20 billion Tuas Mega Port project, the 
    world's largest fully automated container terminal under construction, understanding the strategic rationale 
    (pre-emptive response to competition, mega vessel accommodation, operational efficiency through automation), 
    development timeline and phases, advanced automation technologies (ARMG yard cranes, AGV fleet, automated gates), 
    sustainability features (solar power, shore power, green design), and implications for Singapore's maritime 
    competitiveness through 2040s and beyond.
    """)
