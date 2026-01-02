import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.markdown('<p class="main-header">⚓ Port Operations</p>', unsafe_allow_html=True)
    
    # Hero metrics
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Typical Vessel Stay", "24-48 hours", help="For mega container ships")
    with col2:
        st.metric("Containers Moved", "3,000-8,000", help="Per vessel call")
    with col3:
        st.metric("Quay Cranes Used", "4-8 cranes", help="Simultaneously on large vessels")
    with col4:
        st.metric("Moves Per Hour", "30-40", help="Per crane (GCR)")
    with col5:
        st.metric("Daily Operations", "60+ vessels", help="At Singapore terminals")
    
    st.markdown("---")
    st.markdown('<p class="section-header">Container Terminal Layout & Zones</p>', unsafe_allow_html=True)
    
    st.markdown("""
    A modern container terminal is carefully organized into distinct functional zones.
    Understanding these zones is critical to understanding how port operations flow.
    """)
    
    # Create terminal layout visualization
    fig = go.Figure()
    
    # Define zones (x1, y1, x2, y2, color, name)
    zones = [
        # Water side
        (0, 8, 10, 10, '#3B82F6', 'Water / Berth'),
        # Quay
        (0, 7, 10, 8, '#1E40AF', 'Quay / Berth'),
        # Apron (behind quay cranes)
        (0, 6, 10, 7, '#60A5FA', 'Apron'),
        # Transfer zone
        (0, 5, 10, 6, '#93C5FD', 'Transfer Zone'),
        # Yard (multiple blocks)
        (0, 1, 3, 5, '#34D399', 'Yard Block A'),
        (3.5, 1, 6.5, 5, '#10B981', 'Yard Block B'),
        (7, 1, 10, 5, '#059669', 'Yard Block C'),
        # Gate area
        (0, 0, 10, 1, '#F59E0B', 'Gate Complex'),
        # Road access
        (0, -0.5, 10, 0, '#78716C', 'Access Road')
    ]
    
    for x1, y1, x2, y2, color, name in zones:
        fig.add_shape(
            type="rect",
            x0=x1, y0=y1, x1=x2, y1=y2,
            fillcolor=color,
            line=dict(color='white', width=2),
            opacity=0.8
        )
        # Add label
        fig.add_annotation(
            x=(x1+x2)/2, y=(y1+y2)/2,
            text=f"<b>{name}</b>",
            showarrow=False,
            font=dict(size=10, color='white'),
            bgcolor=color,
            opacity=0.9
        )
    
    # Add quay cranes
    for i in range(5):
        crane_x = 1 + i * 2
        fig.add_shape(type="rect", x0=crane_x-0.15, y0=7, x1=crane_x+0.15, y1=7.8,
                     fillcolor='#FCD34D', line=dict(color='#F59E0B', width=2))
        fig.add_annotation(x=crane_x, y=7.4, text="QC", showarrow=False, font=dict(size=8))
    
    # Add vessel
    fig.add_shape(type="rect", x0=2, y0=8.2, x1=8, y1=9.8,
                 fillcolor='#DC2626', line=dict(color='#991B1B', width=2))
    fig.add_annotation(x=5, y=9, text="<b>CONTAINER VESSEL</b>", 
                      showarrow=False, font=dict(size=12, color='white'))
    
    fig.update_layout(
        title='Typical Container Terminal Layout (Cross-Section View)',
        xaxis=dict(showgrid=False, showticklabels=False, range=[-0.5, 10.5]),
        yaxis=dict(showgrid=False, showticklabels=False, range=[-1, 10.5]),
        height=400,
        plot_bgcolor='white',
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Zone descriptions
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Terminal Zones Explained
        
        **1. Water / Berth Area**
        - Where vessels dock alongside quay
        - Depth: 15-23 meters (depends on terminal)
        - Must accommodate vessel draft + clearance
        - Protected from waves and weather
        
        **2. Quay (Pronounced "key")**
        - The wharf structure itself
        - Heavy-duty concrete or steel
        - Supports quay crane rails
        - Designed for 100+ year lifespan
        
        **3. Apron**
        - Paved area immediately behind quay
        - Where quay cranes operate
        - Width: 40-60 meters
        - Must support heavy equipment loads
        
        **4. Transfer Zone**
        - Intermediate staging area
        - Prime movers / AGVs pick up containers here
        - Containers briefly staged before yard transport
        - Minimizes truck waiting time
        
        **5. Container Yard**
        - Main storage area for containers
        - Organized into blocks and rows
        - Stacked 4-6 high (can be 7-8 with automation)
        - Separated by type: import, export, transshipment, empty
        """)
    
    with col2:
        st.markdown("""
        **6. Gate Complex**
        - Where trucks enter/exit terminal
        - Multiple lanes (8-16 lanes)
        - Security checkpoints
        - Documentation verification
        - Weight scales
        - Radiation scanners (for security)
        
        **7. Supporting Facilities**
        - **Maintenance workshop**: Repair containers and equipment
        - **Reefer racks**: Power supply for refrigerated containers
        - **Empty depot**: Store/stack empty containers
        - **DG area**: Segregated storage for dangerous goods
        - **CFS (Container Freight Station)**: LCL consolidation
        - **Admin building**: Operations control center
        
        ### Layout Design Considerations
        
        **Parallel vs Perpendicular:**
        
        **Parallel Layout (Most Common):**
        - Containers stacked parallel to quay
        - Yard cranes run perpendicular to quay
        - Shorter horizontal transport distance
        - Better for high-throughput terminals
        
        **Perpendicular Layout:**
        - Containers stacked perpendicular to quay
        - Yard cranes run parallel to quay
        - Longer but uses space efficiently
        - Good for narrow terminal sites
        """)
    
    st.markdown("---")
    st.markdown('<p class="section-header">The Complete Vessel Operation Workflow</p>', unsafe_allow_html=True)
    
    st.markdown("""
    From the moment a vessel is announced until it departs, port operations follow a carefully orchestrated sequence.
    Let's walk through the complete process step by step.
    """)
    
    # Create workflow timeline
    workflow_steps = pd.DataFrame({
        'Step': range(1, 11),
        'Phase': [
            '1. Pre-Arrival',
            '2. Approach & Pilotage',
            '3. Berthing',
            '4. Lashing/Unlashing',
            '5. Discharge Operations',
            '6. Load Operations',
            '7. Documentation',
            '8. Final Checks',
            '9. Unberthing',
            '10. Departure'
        ],
        'Duration': [
            '72-12 hours before',
            '2-4 hours',
            '1-2 hours',
            '1-2 hours',
            '10-20 hours',
            '10-20 hours',
            'Concurrent',
            '1-2 hours',
            '1 hour',
            'N/A'
        ],
        'Key_Activities': [
            'Berth booking, stow planning, customs clearance, resource allocation',
            'Pilot boards, tugs assigned, navigational channel transit',
            'Tugboats assist, mooring lines secured, gangway deployed',
            'Remove twist locks, disconnect reefers, safety checks',
            'QC discharge import + transshipment containers to yard',
            'QC load export + transshipment containers from yard',
            'Manifest updates, customs, billing, cargo release',
            'Cargo reconciliation, fuel/water supply, crew changes',
            'Mooring released, tugboats assist, pilot guides out',
            'Vessel proceeds to next port'
        ],
        'Who_Involved': [
            'Shipping line, port planner, customs, berth manager',
            'Pilot, tug captain, vessel master, VTS',
            'Pilot, linesmen, tug crew, vessel crew',
            'Lashing team, crane operators, safety officer',
            'QC operators, YC operators, PM/AGV drivers, planners',
            'QC operators, YC operators, PM/AGV drivers, planners',
            'Documentation team, customs, shipping line',
            'Port captain, bunker barge, chandler, immigration',
            'Pilot, linesmen, tug crew',
            'Pilot, vessel master'
        ]
    })
    
    # Create Gantt-style timeline
    fig_timeline = go.Figure()
    
    colors = ['#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6', 
             '#EC4899', '#14B8A6', '#F97316', '#06B6D4', '#84CC16']
    
    for i, row in workflow_steps.iterrows():
        fig_timeline.add_trace(go.Bar(
            y=[row['Phase']],
            x=[1],
            orientation='h',
            name=row['Phase'],
            marker_color=colors[i],
            text=f"Step {row['Step']}: {row['Duration']}",
            textposition='inside',
            hovertemplate=f"<b>{row['Phase']}</b><br>" +
                         f"Duration: {row['Duration']}<br>" +
                         f"Activities: {row['Key_Activities']}<br>" +
                         f"<extra></extra>",
            showlegend=False
        ))
    
    fig_timeline.update_layout(
        title='Vessel Operation Workflow (Sequential Flow)',
        xaxis=dict(showticklabels=False, title=''),
        yaxis=dict(title=''),
        height=400,
        barmode='stack'
    )
    
    st.plotly_chart(fig_timeline, use_container_width=True)
    
    # Detailed step breakdown
    st.markdown("### Detailed Step-by-Step Breakdown")
    
    for _, row in workflow_steps.iterrows():
        with st.expander(f"**{row['Phase']}** - Duration: {row['Duration']}"):
            st.markdown(f"""
            **Key Activities:**
            {row['Key_Activities']}
            
            **Who's Involved:**
            {row['Who_Involved']}
            """)
    
    st.markdown("---")
    st.markdown('<p class="subsection-header">Pre-Arrival Planning (72-12 Hours Before)</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### What Happens Before the Ship Arrives
        
        Modern port operations begin **days before** a vessel arrives. Extensive planning ensures smooth operations.
        
        **72 Hours Before Arrival:**
        
        **1. Berth Application (via PORTNET)**
        - Shipping line submits berth request
        - Vessel details: name, IMO, ETA, cargo manifest
        - Special requirements (reefers, DG, heavy cargo)
        
        **2. Berth Planning System**
        - CITOS analyzes all pending vessel arrivals
        - Considers: vessel size, draft, cargo volume, priorities
        - Allocates optimal berth for each vessel
        - **Goal: BOA (Berth on Arrival) >90%**
        - Minimize waiting at anchorage
        
        **48 Hours Before:**
        
        **3. Cargo Manifest Processing**
        - Complete list of all containers on vessel
        - Import, export, transshipment breakdown
        - Reefer containers (power needed)
        - Dangerous goods (special handling)
        - Out-of-gauge cargo (oversized)
        
        **4. Customs Pre-Clearance**
        - Import declarations processed
        - Duties and taxes calculated
        - Risk assessment for inspections
        - Cargo holds (if needed)
        """)
    
    with col2:
        st.markdown("""
        **24 Hours Before:**
        
        **5. Stow Plan Generation**
        
        CITOS automatically creates:
        - **Vessel Stow Plan**: Where to place containers on ship
        - Optimizes for:
          - Vessel stability (weight distribution)
          - Port of discharge sequence (Rotterdam before Hamburg)
          - Container type (reefers need power plugs)
          - Weight limits (heavy on bottom)
          - Dangerous goods segregation
        
        **6. Yard Planning**
        - Determine which yard blocks to use
        - Pre-allocate spaces for inbound containers
        - Minimize reshuffles
        - Group by destination for transshipment
        
        **12 Hours Before:**
        
        **7. Resource Allocation**
        - **Quay cranes**: How many? Which ones?
        - **Crane intensity (CI)**: Target moves per crane
        - **Yard cranes**: Allocate to support vessel
        - **Prime movers / AGVs**: Ensure enough available
        - **Workforce**: Assign crane operators, planners, lashing crew
        
        **8. Operational Sequence Planning**
        - Discharge sequence (which containers first)
        - Load sequence (optimize crane moves)
        - Minimize crane interference
        - Coordinate with connecting vessels
        - **Tight connections**: Containers arriving & departing same day
        """)
    
    st.markdown("---")
    st.markdown('<p class="subsection-header">Vessel Berthing Process</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### Approach & Pilotage
        
        **Pilotage is Mandatory:**
        - Large vessels cannot navigate port waters alone
        - **Pilot** boards vessel at pilot boarding ground
        - Pilot has local knowledge of:
          - Channels and depths
          - Currents and tides
          - Traffic patterns
          - Berth approaches
        
        **Pilot Boarding:**
        - Vessel slows to 5-8 knots
        - Pilot boat comes alongside
        - Pilot climbs rope ladder to deck
        - Takes control from bridge (captain still commands)
        
        **Tugboat Assistance:**
        - **2-4 tugboats** assigned (depends on vessel size)
        - 24,000 TEU vessel: 4-5 tugs
        - Tugs push/pull vessel for precise maneuvering
        - Critical for large vessels with poor maneuverability
        
        **Vessel Traffic Service (VTS):**
        - Monitors all vessel movements
        - Like air traffic control for ships
        - Provides traffic updates
        - Ensures safe spacing
        """)
    
    with col2:
        st.markdown("""
        ### Berthing Operations
        
        **Final Approach:**
        - Vessel approaches berth at 1-2 knots
        - Tugboats in position (fore, aft, sides)
        - Fenders deployed to protect quay
        - Mooring team ready on deck
        
        **Mooring Process:**
        
        **1. First Line Ashore (15-20 minutes)**
        - Heaving line thrown to linesmen on quay
        - Connected to heavy mooring rope
        - Linesmen pull rope ashore
        - Secure to bollard (strong mooring post)
        
        **2. Multiple Lines (30-45 minutes total)**
        - **Breast lines**: Hold vessel against quay
        - **Spring lines**: Prevent fore/aft movement
        - **Headline**: Front of vessel
        - **Stern line**: Back of vessel
        - Typically **10-16 lines** for large vessel
        
        **3. Final Positioning:**
        - Adjust lines to align vessel perfectly
        - Quay crane rails must align with vessel holds
        - Critical for crane operation
        - Precision: within 0.5 meters
        
        **4. Gangway Deployment:**
        - Crew access to shore
        - For immigration, customs, port officials
        - Emergency egress route
        """)
    
    with col3:
        st.markdown("""
        ### Safety & Preparation
        
        **Safety Checks:**
        - **Ship-shore safety checklist**
        - Fire safety equipment ready
        - Emergency procedures briefed
        - Communication systems tested
        - Weather monitoring
        
        **Unlashing Containers:**
        - **Lashing team** boards vessel
        - Remove twist locks (secure containers together)
        - Disconnect reefer power cables
        - Remove lashing rods
        - Safety: work at height, heavy equipment
        - **Time**: 1-2 hours for large vessel
        
        **Hatch Cover Removal:**
        - Open container holds
        - Remove hatch covers with cranes
        - Store covers on deck
        - Expose containers for discharge
        
        **Crane Positioning:**
        - Quay cranes move into position
        - Align with vessel holds (bays)
        - Spreader bars (lifting device) deployed
        - Operators receive discharge list
        - Ready to begin operations
        
        **Time Budget:**
        - Pilot boarding to berth: 2-4 hours
        - Mooring: 0.5-1 hour
        - Unlashing: 1-2 hours
        - **Total**: 3.5-7 hours before operations start
        """)
    
    st.markdown("---")
    st.markdown('<p class="subsection-header">Container Discharge & Loading Operations</p>', unsafe_allow_html=True)
    
    st.markdown("""
    This is the core activity - moving thousands of containers between vessel and yard as efficiently as possible.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Discharge Operations (Import + Transshipment)
        
        **The Process:**
        
        **1. Quay Crane Picks Container:**
        - Operator receives target container from system
        - Bay 12, Row 05, Tier 03 (position on ship)
        - Crane lowers spreader bar into hold
        - Spreader locks onto container corner castings
        - Lifts container (25-30 tons typical)
        
        **2. Crane Moves Container:**
        - Swings from vessel to apron
        - **Horizontal**: 40-60 meter reach
        - **Vertical**: Up to 50 meters high
        - Places on prime mover / AGV chassis
        
        **3. Transport to Yard:**
        
        **Manual Terminal (Prime Mover):**
        - Human driver
        - Receives yard location from system
        - Drives to assigned yard block
        - **Time**: 3-8 minutes round trip
        
        **Automated Terminal (AGV):**
        - Driverless vehicle
        - Follows magnetic markers / GPS
        - System assigns optimal route
        - **Time**: 3-5 minutes (more consistent)
        
        **4. Yard Crane Stacks Container:**
        - RTG / RMG crane picks from PM/AGV
        - Stacks in assigned position
        - **Import**: Grouped by consignee
        - **Transshipment**: Grouped by next vessel/destination
        - **Empties**: Separate empty yard
        
        **5. System Updates:**
        - Container location updated in CITOS
        - Customs notified (imports)
        - Consignee notified (available for pickup)
        - Connecting vessel planner notified (transship)
        """)
        
        st.markdown("""
        ### Operational Challenges
        
        **Reshuffles (The Enemy of Efficiency):**
        
        Problem: Target container is **under** other containers
        
        **Example:**
        - Need container in position (Bay 12, Row 05, Tier 03)
        - But 2 containers stacked on top
        - Must move top 2 containers first
        - Each move = time + crane cycle
        
        **Minimize Reshuffles:**
        - Smart stowage planning
        - Load heavy/late-discharge on bottom
        - Load light/early-discharge on top
        - Maintain "stowage height" discipline
        
        **Tight Connections:**
        - Container arrives on Vessel A (morning)
        - Must depart on Vessel B (evening)
        - Only 6-12 hours in terminal!
        - High priority in yard planning
        - Stored near berth for quick retrieval
        """)
    
    with col2:
        st.markdown("""
        ### Loading Operations (Export + Transshipment)
        
        **The Process (Reverse of Discharge):**
        
        **1. Load List Generated:**
        - CITOS creates optimal loading sequence
        - Based on vessel stow plan
        - Considers:
          - Weight distribution (stability)
          - Port of discharge (first out = top)
          - Reefer plug availability
          - Dangerous goods rules
        
        **2. Yard Crane Retrieves:**
        - Picks container from yard stack
        - Places on PM/AGV
        - May require reshuffles if buried
        
        **3. Transport to Vessel:**
        - PM/AGV brings to quay
        - Queues in transfer zone
        - System optimizes flow
        
        **4. Quay Crane Loads:**
        - Lifts from PM/AGV
        - Places in vessel hold
        - Exact position per stow plan
        - Precision critical for stability
        
        **5. Lashing:**
        - Lashing crew secures containers
        - Twist locks between tiers
        - Lashing rods for deck containers
        - Must withstand ocean voyage
        
        **Sequence Optimization:**
        
        **Dual Cycling (Advanced Technique):**
        - Crane picks import container from vessel
        - Swings to apron, places on PM/AGV
        - **Immediately** picks export container waiting
        - Swings back to vessel, loads
        - **Zero idle time** for crane
        - Requires perfect coordination
        - Increases productivity 20-30%
        
        **Crane Interference:**
        - Multiple cranes on same vessel
        - Must not cross paths
        - CITOS schedules to avoid conflicts
        - Sometimes crane must wait
        """)
        
        st.markdown("""
        ### Performance Metrics
        
        **Moves Per Hour (Gross Crane Rate):**
        - **Manual terminal**: 25-30 moves/hour/crane
        - **Automated terminal**: 35-40 moves/hour/crane
        - **World-class**: 40+ moves/hour/crane
        
        **A 24,000 TEU Vessel:**
        - Discharge: 3,000 containers
        - Load: 5,000 containers  
        - **Total**: 8,000 moves
        - With 8 cranes @ 35 moves/hour each:
          - 8 cranes × 35 moves/hour = 280 moves/hour
          - 8,000 moves ÷ 280 = **28.6 hours**
          - Add prep time: **30-36 hours total**
        
        **Crane Intensity (CI):**
        - CI = Number of cranes / (Moves ÷ 1000)
        - Target CI: 3.0-4.0
        - Example: 8,000 moves with 8 cranes
        - CI = 8 / (8000/1000) = 8/8 = 1.0 (too low!)
        - Should use 24-32 cranes (not practical!)
        - Compromise: Use max available, accept longer time
        """)
    
    st.markdown("---")
    st.markdown('<p class="subsection-header">Import, Export, and Transshipment Flows</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Containers move through terminals in three distinct flows, each with different processes and timelines.
    """)
    
    # Create flow comparison
    flow_data = pd.DataFrame({
        'Flow_Type': ['Import', 'Export', 'Transshipment'],
        'Percentage': [10, 5, 85],  # Singapore example
        'Origin': ['Vessel', 'Inland (truck/rail)', 'Vessel A'],
        'Destination': ['Consignee (truck/rail)', 'Vessel', 'Vessel B'],
        'Dwell_Time': ['3-7 days', '1-3 days (before vessel)', '1-2 days'],
        'Value_Add': ['Customs clearance, delivery', 'Consolidation, VGM', 'Quick transshipment']
    })
    
    # Horizontal bar chart
    fig_flows = go.Figure()
    
    colors_flow = {'Import': '#3B82F6', 'Export': '#10B981', 'Transshipment': '#F59E0B'}
    
    for _, row in flow_data.iterrows():
        fig_flows.add_trace(go.Bar(
            y=['Container Flows'],
            x=[row['Percentage']],
            name=row['Flow_Type'],
            orientation='h',
            marker_color=colors_flow[row['Flow_Type']],
            text=f"{row['Flow_Type']}<br>{row['Percentage']}%",
            textposition='inside',
            hovertemplate=f"<b>{row['Flow_Type']}</b><br>" +
                         f"Share: {row['Percentage']}%<br>" +
                         f"From: {row['Origin']}<br>" +
                         f"To: {row['Destination']}<br>" +
                         f"Dwell: {row['Dwell_Time']}<extra></extra>"
        ))
    
    fig_flows.update_layout(
        title='Container Flow Types (Singapore Example: 85% Transshipment Hub)',
        xaxis_title='Percentage',
        barmode='stack',
        height=200,
        showlegend=True
    )
    
    st.plotly_chart(fig_flows, use_container_width=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 📥 Import Flow
        
        **Journey:**
        1. Arrives on vessel (from overseas)
        2. Discharged to import yard
        3. Customs clearance
        4. Consignee arranges pickup
        5. Truck collects from gate
        6. Delivered to final destination
        
        **Timeline:**
        - Discharge: Day 1
        - Customs: Day 1-2
        - Available for pickup: Day 2
        - Pickup: Day 3-7
        - **Free time**: 5-7 days typically
        - After that: **demurrage charges** (storage fee)
        
        **Documentation:**
        - Bill of Lading (B/L)
        - Commercial invoice
        - Packing list
        - Import license (if required)
        - Customs declaration
        - Delivery order (D/O)
        
        **Customs Process:**
        - **Green lane**: Auto-clearance (80%+)
        - **Red lane**: Physical inspection (risky cargo)
        - **Yellow lane**: Document check
        - X-ray scanning for contraband
        - Duties and taxes paid
        
        **Challenges:**
        - Documentation errors delay clearance
        - Consignee must pay storage if delayed
        - Reefer containers: Must maintain power
        - Dangerous goods: Special storage
        """)
    
    with col2:
        st.markdown("""
        ### 📤 Export Flow
        
        **Journey:**
        1. Truck delivers container to gate
        2. Received and inspected
        3. Stored in export yard
        4. VGM (weight) verification
        5. Loaded onto vessel
        6. Departs to overseas destination
        
        **Timeline:**
        - Booking: 7-14 days before vessel
        - Delivery to terminal: 2-4 days before
        - Stored in export yard: 1-3 days
        - Loaded on vessel: Per schedule
        - **Cut-off time**: 24-48 hours before sailing
        
        **Documentation:**
        - Shipping instruction (SI)
        - Commercial invoice
        - Packing list
        - VGM certificate (mandatory!)
        - Export license (if required)
        - Bill of Lading issued after load
        
        **VGM (Verified Gross Mass):**
        - **Mandatory** since 2016 (SOLAS)
        - Container + cargo weight
        - Must be declared before loading
        - Either:
          - Weigh full container at terminal, OR
          - Weigh cargo + container separately
        - Safety: Prevent vessel instability
        
        **Challenges:**
        - Late documentation
        - VGM discrepancies
        - Overweight containers rejected
        - Missing cut-off = rolled to next vessel
        - Demurrage if container held too long
        """)
    
    with col3:
        st.markdown("""
        ### 🔄 Transshipment Flow
        
        **Journey:**
        1. Arrives on Vessel A (mother vessel)
        2. Discharged to transshipment yard
        3. Stored briefly
        4. Loaded onto Vessel B (feeder or another mother vessel)
        5. Departs to final destination
        
        **Timeline:**
        - Arrival on Vessel A: Day 1 morning
        - Discharge: Day 1 morning-afternoon
        - Storage: 1-48 hours
        - Loading on Vessel B: Day 1 evening or Day 2
        - **Tight connection**: Same day transship
        
        **Singapore Specialization:**
        - **85% of Singapore containers** are transshipment
        - World's largest transshipment hub
        - **Why**: Perfect location at Malacca crossroads
        
        **Types of Transshipment:**
        
        **1. Hub-and-Spoke:**
        - Mother vessel → Hub (Singapore)
        - Hub → Feeder vessel → Regional port
        - Example: Shanghai → Singapore → Jakarta
        
        **2. Cross-String:**
        - Mother vessel A → Hub
        - Hub → Mother vessel B (different route)
        - Example: Asia-Europe string to Trans-Pacific string
        
        **Operational Excellence:**
        - **<24 hour transshipment** common
        - Sometimes same-day!
        - Requires excellent planning
        - High-value service for shipping lines
        
        **Challenges:**
        - Tight timing (miss connection = delay 1 week)
        - Yard planning critical
        - Weather delays impact connections
        - Documentation must transfer correctly
        """)
    
    st.markdown("---")
    st.markdown('<p class="section-header">Gate Operations</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Truck Gate Process
        
        Gates are where containers enter/exit the terminal via trucks. 
        Efficiency here is critical to avoid congestion.
        
        **Inbound (Delivering Containers):**
        
        **1. Pre-Gate:**
        - Driver books time slot (some terminals)
        - Has documentation ready
        - Container booking number
        
        **2. Entry Lane:**
        - Security checkpoint
        - Driver presents documents
        - System verifies booking
        
        **3. Inspection:**
        - **Container condition check**: Damage?
        - **Seal verification**: Intact?
        - **Weight check**: Drive over scale
        - **Radiation scan**: Security
        - **X-ray** (random or red lane)
        
        **4. Documentation:**
        - Scan delivery order
        - Capture container number (OCR)
        - Print gate receipt
        
        **5. Direction to Yard:**
        - System assigns yard location
        - Driver proceeds to yard block
        - Yard crane lifts container off truck
        - Truck returns empty
        
        **Time: 15-30 minutes** (efficient terminal)
        """)
        
        st.markdown("""
        ### Peak Hour Management
        
        **The Problem:**
        - 8am-10am: Morning rush (deliveries)
        - 3pm-5pm: Afternoon rush (pickups)
        - Can have **100+ trucks** waiting
        
        **Solutions:**
        
        **1. Appointment Systems:**
        - Book time slot in advance
        - Spread arrivals throughout day
        - Penalties for no-shows
        
        **2. Extended Hours:**
        - 24/7 gate operations
        - Night gates (lower traffic)
        - Off-peak discounts
        
        **3. Fast Lanes:**
        - Pre-registered truckers
        - RFID automatic identification
        - Skip inspection (trusted)
        
        **4. Separate Gates:**
        - Import gate
        - Export gate
        - Empty gate
        - Reduces conflicts
        """)
    
    with col2:
        st.markdown("""
        **Outbound (Picking Up Containers):**
        
        **1. Pre-Requirements:**
        - Import duty paid (imports)
        - Delivery order obtained
        - Truck booking made
        
        **2. Entry & Verification:**
        - Driver presents delivery order
        - System checks container is released
        - Customs clearance confirmed
        
        **3. Direction to Yard:**
        - System shows container location
        - Driver proceeds to yard block
        - Waits for yard crane
        
        **4. Container Loaded:**
        - Yard crane lifts container
        - Places on truck chassis
        - Driver inspects (damage?)
        
        **5. Exit Gate:**
        - Final inspection
        - Seal check
        - Print exit receipt
        - Release truck
        
        **Time: 20-40 minutes** (depends on queue)
        
        **Special Cases:**
        
        **Reefer Containers:**
        - Must maintain temperature
        - Time-sensitive pickup
        - Power until last moment
        - Truck may have generator
        
        **Dangerous Goods:**
        - Special documentation
        - Trained drivers only
        - Placards displayed
        - Segregation rules
        
        **Overweight:**
        - Special permits needed
        - Route restrictions
        - May need special chassis
        """)
        
        st.markdown("""
        ### Technology at Gates
        
        **Modern Automation:**
        
        **1. OCR (Optical Character Recognition):**
        - Cameras read container numbers
        - Automatic data capture
        - No manual entry errors
        
        **2. RFID Tags:**
        - Trucks have RFID cards
        - Auto-identification on entry
        - Faster processing
        
        **3. Automated Gates:**
        - No human staff needed
        - Self-service kiosks
        - Driver scans documents
        - System validates
        - Gate opens automatically
        
        **4. Mobile Apps:**
        - Drivers book slots via app
        - Real-time queue status
        - Push notifications
        - Digital documentation
        
        **5. GPS Tracking:**
        - Track truck location
        - Predict arrival time
        - Optimize yard planning
        - Improve efficiency
        """)
    
    st.markdown("---")
    st.markdown('<p class="section-header">Yard Planning & Management</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The container yard is where containers are stored between vessel and gate. 
    Good yard planning is critical for terminal efficiency.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Yard Organization
        
        **Hierarchical Structure:**
        
        **1. Yard Blocks:**
        - Terminal divided into blocks (A, B, C, etc.)
        - Each block: 20-40 container stacks
        - Organized by function
        
        **2. Rows (Bays):**
        - Perpendicular to yard crane rails
        - Numbered: 01, 02, 03...
        - One row = one stack width
        
        **3. Tiers (Height):**
        - Vertical layers
        - Ground = Tier 1
        - Stack height: 4-6 containers (manual)
        - Stack height: 6-8 containers (automated)
        
        **4. Slots:**
        - Individual container positions
        - Address: Block-Row-Tier
        - Example: A-15-04 (Block A, Row 15, Tier 4)
        
        **Segregation Principles:**
        
        **By Flow Type:**
        - **Import blocks**: Near gate
        - **Export blocks**: Near berth
        - **Transship blocks**: Central or near berth
        - **Empty blocks**: Separate area
        
        **By Destination:**
        - Group by next vessel
        - Group by port of discharge
        - Minimize shuffles during loading
        
        **By Type:**
        - **Reefer area**: With power plugs
        - **Dangerous goods**: Segregated, low stack
        - **Heavy containers**: Bottom tiers
        - **Empties**: High stacks (lightweight)
        """)
        
        st.markdown("""
        ### Stacking Strategies
        
        **Height Optimization:**
        
        **Trade-offs:**
        - **Higher stacks** = More capacity, but more reshuffles
        - **Lower stacks** = Less capacity, but easier access
        
        **Optimal Height:**
        - **Manual (RTG)**: 5 high (6 possible)
        - **Automated (RMG)**: 6-7 high
        - **Straddle carrier**: 3 high only
        
        **Weight Distribution:**
        - Heavy containers (30+ tons) on ground
        - Light containers (<15 tons) can go high
        - System checks weight limits
        
        **FILO vs FIFO:**
        
        **FILO (First In, Last Out) - Traditional:**
        - Like a stack of plates
        - Last container in is on top (easy access)
        - First container in is on bottom (buried)
        - Problem: Reshuffles if need bottom container
        
        **FIFO (First In, First Out) - Ideal:**
        - First container in should go out first
        - Requires smart planning
        - Minimize reshuffles
        - Achieved through careful positioning
        """)
    
    with col2:
        st.markdown("""
        ### Reshuffle Management
        
        **The Reshuffle Problem:**
        
        Reshuffles = **Unproductive moves**
        - Need container in Tier 1 (ground)
        - But 4 containers stacked on top
        - Must move 4 containers aside
        - Retrieve target container
        - Re-stack 4 containers back
        - **5 crane cycles instead of 1!**
        
        **Cost of Reshuffles:**
        - Wasted crane time
        - Wasted labor
        - Increased equipment wear
        - Lower terminal throughput
        - Higher operating costs
        
        **Target Reshuffle Rate:**
        - **World-class**: <15% of moves
        - **Good**: 15-25%
        - **Poor**: >30%
        - Singapore targets: 10-15%
        
        **Minimization Strategies:**
        
        **1. Pre-Marshaling:**
        - Reorganize stacks before vessel loads
        - Move containers to correct sequence
        - Time-consuming but worth it
        
        **2. Dwell Time Consideration:**
        - Long dwell containers on bottom
        - Short dwell containers on top
        - Import prediction models
        
        **3. Vessel Load Sequence:**
        - Stack in reverse load order
        - Top of stack loads first
        - Bottom loads last
        
        **4. Dedicated Stacks:**
        - One stack per vessel
        - Organized by bay/sequence
        - Clean loading
        
        **5. AI Optimization:**
        - Machine learning predicts pickup time
        - Optimizes stacking locations
        - Reduces reshuffles 20-30%
        """)
        
        st.markdown("""
        ### Reefer Container Management
        
        **Special Requirements:**
        
        **Power Supply:**
        - Reefers need continuous electricity
        - **Reefer racks** in yard (vertical structures)
        - Each plug: 480V, 60Hz
        - Can stack 4-5 high on rack
        
        **Temperature Monitoring:**
        - 24/7 monitoring system
        - Alarms if temperature deviation
        - **Pre-trip inspection (PTI)**: Before load
        - Check compressor, seals, temperature
        
        **Types of Cargo:**
        - **Frozen**: -25°C to -18°C (meat, fish)
        - **Chilled**: +2°C to +8°C (produce, dairy)
        - **Climate controlled**: +12°C to +15°C (bananas, chocolate)
        
        **Operational Challenges:**
        - Limited reefer plug capacity
        - Must rotate to vessel quickly
        - Temperature excursions = cargo damage
        - Claims can be $100K+ for spoiled cargo
        
        **Planning:**
        - Priority discharge (minimize yard time)
        - Priority loading (get power on ship)
        - Pre-allocated reefer slots
        """)
    
    st.markdown("---")
    st.markdown('<p class="section-header">Supporting Operations</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### Vessel Services
        
        **Bunkering:**
        - Refueling ship while in port
        - Bunker barge comes alongside
        - Fuel types: HSFO, LSFO, MGO, LNG
        - Singapore: 40M+ tonnes/year
        - Can bunker while loading cargo
        
        **Fresh Water:**
        - Ships need fresh water supply
        - Drinking water and boiler water
        - Supplied via hose from quay
        - **10-100 tons** per call
        
        **Provisions:**
        - Food and supplies
        - Chandlers deliver to ship
        - Everything from food to spare parts
        
        **Crew Changes:**
        - Immigration/customs formalities
        - Crew sign on/off
        - Airport transportation
        
        **Waste Disposal:**
        - Garbage collection
        - Bilge water (oily water)
        - Sewage
        - Environmental regulations
        """)
    
    with col2:
        st.markdown("""
        ### Maintenance & Repair
        
        **Container Maintenance:**
        - **Damage inspection**: All inbound containers
        - **Minor repairs**: Patch holes, fix doors
        - **Cleaning**: Remove cargo residue
        - **Painting**: Repair rust spots
        - **Floor replacement**: Plywood floors wear out
        
        **Container Depot (M&R):**
        - Dedicated repair facility
        - Welders, carpenters, painters
        - **Repair or scrap decision**
        - Cost-benefit analysis
        
        **Equipment Maintenance:**
        - **Quay cranes**: Major services every 2,000 hours
        - **Yard cranes**: Daily checks
        - **Prime movers**: Fleet maintenance
        - **Preventive maintenance**: Scheduled
        - **Breakdown repairs**: Emergency
        
        **Downtime Impact:**
        - One QC down: -35 moves/hour
        - During vessel operations: Critical
        - Maintenance windows: Between vessels
        - Spare equipment buffer
        """)
    
    with col3:
        st.markdown("""
        ### Safety & Security
        
        **Safety Protocols:**
        
        **1. Equipment Safety:**
        - Regular inspections
        - Operator certifications
        - Load limits enforced
        - Emergency stop systems
        
        **2. Personnel Safety:**
        - Hard hats, safety shoes
        - High-visibility vests
        - Restricted zones
        - Safety briefings
        
        **3. Operational Safety:**
        - No workers under suspended loads
        - Crane collision prevention
        - Weather restrictions (wind >30 knots)
        
        **Security Measures:**
        
        **1. Access Control:**
        - ID cards and biometrics
        - Visitor registration
        - Vehicle passes
        - Restricted areas
        
        **2. Cargo Security:**
        - **ISPS Code** compliance (maritime security)
        - Container seals
        - Seal verification
        - Tampering detection
        
        **3. Monitoring:**
        - CCTV coverage
        - Security patrols
        - Perimeter fencing
        - Intrusion detection
        """)
    
    st.markdown("---")
    
    st.info("""
    **📚 Related Sections:**
    
    - **Terminal Equipment**: Learn about quay cranes, yard cranes, AGVs in detail
    - **CITOS & Technology**: Deep dive into the planning systems
    - **KPIs**: Understand the performance metrics (GCR, CI, BOA, etc.)
    - **Singapore & Tuas**: See how world's best port optimizes these operations
    """)
    
    st.markdown("---")
    
    st.markdown('<div class="success-box">', unsafe_allow_html=True)
    st.markdown("""
    ### 🎓 Key Takeaways - Port Operations
    
    **Planning is Everything:**
    - Operations begin 72 hours before vessel arrives
    - Berth allocation, stow planning, resource scheduling
    - Goal: BOA >90% (no waiting at anchorage)
    
    **Three Critical Flows:**
    - **Import** (10-15%): Vessel → Customs → Truck → Consignee
    - **Export** (5-10%): Shipper → Truck → Terminal → Vessel
    - **Transshipment** (80-85% in Singapore): Vessel A → Terminal → Vessel B
    
    **Efficiency Drivers:**
    - **Crane productivity**: 30-40 moves/hour
    - **Minimize reshuffles**: <15% target
    - **Yard planning**: Right container, right place, right time
    - **Gate efficiency**: 15-30 minutes per truck
    - **Tight connections**: <24 hour transshipment
    
    **Technology Enables Scale:**
    - CITOS plans every move
    - Automated equipment (QC, YC, AGV)
    - Real-time visibility (PORTNET)
    - Optimization algorithms
    - 60+ vessels/day possible at Singapore
    
    **The Symphony:**
    - Port operations are a carefully orchestrated symphony
    - Hundreds of moving parts must coordinate perfectly
    - One delay cascades through the system
    - Excellence = consistency, reliability, efficiency
    """)
    st.markdown('</div>', unsafe_allow_html=True)
