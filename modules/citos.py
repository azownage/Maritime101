import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.markdown('<p class="main-header">🎯 CITOS & Port Technology</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <p style="text-align: center; font-size: 1.5rem; color: #64748B; margin-bottom: 2rem;">
    <strong>CITOS</strong> - Container IT Operating System<br>
    The Brain Behind Singapore's Port Operations Excellence
    </p>
    """, unsafe_allow_html=True)
    
    # Hero metrics
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("First Deployed", "1988", help="PSA pioneered TOS")
    with col2:
        st.metric("Vessels/Day", "60+", help="Managed by CITOS")
    with col3:
        st.metric("BOA Achievement", ">90%", help="Berth on Arrival rate")
    with col4:
        st.metric("PORTNET Users", "10,000+", help="Integrated stakeholders")
    with col5:
        st.metric("Annual Transactions", "220M+", help="Via PORTNET")
    
    st.markdown("---")
    st.markdown('<p class="section-header">What is CITOS?</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        ### The Terminal Operating System (TOS)
        
        **CITOS** stands for **Container IT Operating System** - PSA's proprietary Terminal Operating System (TOS).
        
        Think of it as the **operating system for an entire port** - like Windows or macOS, but for managing:
        - Vessels arriving and departing
        - Thousands of containers moving simultaneously
        - Hundreds of pieces of equipment (cranes, trucks, AGVs)
        - Thousands of workers and their tasks
        - Complex logistics across multiple terminals
        
        **Historical Context:**
        
        **1988: CITOS Launched**
        - PSA was a pioneer in port automation
        - One of the world's first comprehensive TOS
        - Revolutionary for the time
        - Gave Singapore competitive edge
        
        **Evolution Over 35+ Years:**
        - Started as basic planning system
        - Evolved into comprehensive ERP
        - Now incorporates AI and machine learning
        - Cloud-based, real-time processing
        - Integrates with global supply chains
        
        **Why It Matters:**
        
        Without CITOS, Singapore couldn't:
        - Handle 60+ vessels daily across terminals
        - Achieve >90% Berth on Arrival (BOA)
        - Manage 37+ million TEU annually
        - Maintain world-class productivity
        - Coordinate tight transshipment connections
        
        **The Challenge CITOS Solves:**
        
        Managing a modern port is incredibly complex:
        - **24,000 TEU vessel** = 8,000 container moves
        - Each move involves: QC → PM/AGV → YC
        - Must plan: Which container? Which crane? Which sequence?
        - Optimize: Minimize vessel time, minimize reshuffles
        - Coordinate: 8 cranes + 50 PMs + 20 YCs working simultaneously
        - **All in real-time, 24/7, with changing conditions**
        
        CITOS makes this possible.
        """)
    
    with col2:
        st.markdown('<div class="success-box">', unsafe_allow_html=True)
        st.markdown("""
        ### 🎯 CITOS Core Functions
        
        **Planning Systems:**
        - **Berth Planning**: Which vessel, which berth, when
        - **Vessel Planning**: Container discharge/load sequence
        - **Yard Planning**: Where to store containers
        - **Resource Planning**: Cranes, equipment, workforce
        
        **Execution Systems:**
        - **Gate Operations**: Truck in/out processing
        - **Quay Crane Control**: Move-by-move instructions
        - **Yard Operations**: Container stacking/retrieval
        - **Equipment Dispatch**: PM/AGV routing
        
        **Monitoring Systems:**
        - **Real-time Tracking**: Every container location
        - **Performance Metrics**: GCR, CI, productivity
        - **Exception Handling**: Alerts and responses
        - **Reporting & Analytics**: Historical data analysis
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("""
        ### 📊 The Numbers
        
        **What CITOS Manages Daily:**
        
        - **60+ vessels** calling at terminals
        - **100,000+ containers** in yard
        - **10,000+ truck** movements  
        - **200+ quay cranes** operating
        - **500+ yard cranes** stacking
        - **1,000+ workers** coordinated
        - **Millions of data points** processed
        
        **Real-Time Requirements:**
        - **<1 second** response time for queries
        - **24/7/365** uptime requirement
        - **Zero tolerance** for system failure
        - **99.99%** reliability target
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown('<p class="section-header">CITOS Architecture & Modules</p>', unsafe_allow_html=True)
    
    st.markdown("""
    CITOS is not a single system, but a comprehensive suite of interconnected modules.
    Each module handles a specific aspect of terminal operations.
    """)
    
    # Create system architecture diagram
    fig = go.Figure()
    
    # Define layers and modules
    layers = {
        'Planning Layer': {
            'y': 4,
            'modules': ['Berth Planning', 'Yard Planning', 'Vessel Planning', 'Resource Planning'],
            'color': '#3B82F6'
        },
        'Execution Layer': {
            'y': 3,
            'modules': ['Gate Ops', 'QC Control', 'YC Control', 'PM/AGV Dispatch'],
            'color': '#10B981'
        },
        'Tracking Layer': {
            'y': 2,
            'modules': ['Container Tracking', 'Equipment Status', 'Location Services', 'Event Logging'],
            'color': '#F59E0B'
        },
        'Data Layer': {
            'y': 1,
            'modules': ['Database', 'Analytics', 'Reporting', 'Integration APIs'],
            'color': '#8B5CF6'
        }
    }
    
    for layer_name, layer_info in layers.items():
        y = layer_info['y']
        modules = layer_info['modules']
        color = layer_info['color']
        
        for i, module in enumerate(modules):
            x = i * 2.5
            
            # Draw module box
            fig.add_shape(
                type="rect",
                x0=x, y0=y-0.3, x1=x+2, y1=y+0.3,
                fillcolor=color,
                line=dict(color='white', width=2),
                opacity=0.8
            )
            
            # Add module label
            fig.add_annotation(
                x=x+1, y=y,
                text=f"<b>{module}</b>",
                showarrow=False,
                font=dict(size=9, color='white')
            )
        
        # Add layer label
        fig.add_annotation(
            x=-1.5, y=y,
            text=f"<b>{layer_name}</b>",
            showarrow=False,
            font=dict(size=11, color=color),
            xanchor='right'
        )
    
    # Add connecting lines (simplified)
    for i in range(4):
        fig.add_shape(type="line", x0=1, y0=4-i-0.3, x1=1, y1=4-i-0.7,
                     line=dict(color='#94A3B8', width=2, dash='dot'))
        fig.add_shape(type="line", x0=3.5, y0=4-i-0.3, x1=3.5, y1=4-i-0.7,
                     line=dict(color='#94A3B8', width=2, dash='dot'))
        fig.add_shape(type="line", x0=6, y0=4-i-0.3, x1=6, y1=4-i-0.7,
                     line=dict(color='#94A3B8', width=2, dash='dot'))
    
    fig.update_layout(
        title='CITOS System Architecture (Layered Modules)',
        xaxis=dict(showgrid=False, showticklabels=False, range=[-2, 9]),
        yaxis=dict(showgrid=False, showticklabels=False, range=[0.5, 4.5]),
        height=350,
        plot_bgcolor='white',
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.markdown('<p class="subsection-header">Key CITOS Modules Explained</p>', unsafe_allow_html=True)
    
    # Berth Planning
    with st.expander("**1. Berth Planning System** - The Foundation"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            ### How It Works
            
            **Inputs:**
            - Vessel schedules (72 hours ahead)
            - Vessel characteristics (LOA, beam, draft, TEU)
            - Expected cargo volume (imports, exports, transship)
            - Berth specifications (length, depth, crane capacity)
            - Current berth occupancy
            - Weather forecast
            
            **Planning Process:**
            
            **1. Berth Request Received (via PORTNET)**
            - Shipping line submits: Vessel name, ETA, cargo details
            - System validates request
            
            **2. Constraint Analysis:**
            - **Physical**: Does vessel fit the berth? (LOA vs berth length)
            - **Depth**: Does draft match berth depth? (16m vessel needs 18m berth)
            - **Timing**: Is berth available at ETA?
            - **Equipment**: Enough cranes available?
            - **Productivity**: Can achieve target turnaround time?
            
            **3. Optimization Algorithm:**
            - Minimize vessel waiting time (maximize BOA)
            - Balance berth utilization
            - Group vessels by shipping line (operational efficiency)
            - Consider connecting vessels (transshipment timing)
            - Avoid crane conflicts
            
            **4. Berth Allocation:**
            - Assigns specific berth (e.g., T01/02)
            - Confirms ETA and berth readiness
            - Notifies all stakeholders
            """)
        
        with col2:
            st.markdown("""
            ### Outputs
            
            **Berth Plan:**
            - Berth schedule for next 7 days
            - Vessel by vessel timeline
            - Equipment allocation
            - Expected completion times
            
            **Performance Target: BOA >90%**
            
            **BOA = Berth on Arrival** means vessel berths immediately upon arrival, no waiting at anchorage.
            
            **Singapore's Achievement:**
            - **90%+** of vessels berth on arrival
            - Industry-leading performance
            - Requires excellent planning
            
            **Why BOA Matters:**
            - Waiting costs shipping line **$30-50K/day**
            - Delays disrupt schedules
            - Affects transshipment connections
            - Competitive advantage for Singapore
            
            **Challenges:**
            
            **Weather Delays:**
            - Vessel arrives late
            - Berth plan disrupted
            - System re-optimizes in real-time
            
            **Emergency Priority:**
            - Vessel with damage
            - Requires immediate berth
            - Plan adjusted dynamically
            
            **Equipment Breakdown:**
            - Crane down for maintenance
            - Affects berth productivity
            - May reassign to different berth
            """)
        
        st.info("""
        **Example:** A 24,000 TEU vessel scheduled for Tuesday 14:00.
        
        - **72 hours before**: Shipping line submits berth request via PORTNET
        - **48 hours**: CITOS analyzes all pending vessels, assigns Berth T01/02
        - **24 hours**: Confirms 8 quay cranes allocated, expected completion: Thursday 02:00
        - **12 hours**: Finalizes discharge/load sequence
        - **ETA**: Vessel arrives 14:00, berth ready, tugs waiting → **BOA achieved!**
        """)
    
    # Yard Planning
    with st.expander("**2. Yard Planning System** - Storage Optimization"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            ### The Yard Planning Challenge
            
            **Scenario:**
            - 100,000 containers in yard at any time
            - Arriving: 3,000 containers from vessel discharge
            - Departing: 5,000 containers for vessel loading
            - Trucks: 10,000 gate movements daily
            
            **Question:** Where to store each container?
            
            **The Problem:**
            - Stack too high → More reshuffles
            - Wrong location → Longer PM/AGV distance
            - Poor grouping → Can't find containers quickly
            - Bad planning → Missed vessel connections
            
            **CITOS Yard Planning Solves This:**
            
            **Step 1: Categorize Containers**
            - **Import**: Destination, consignee, dwell time prediction
            - **Export**: Vessel, sailing date, load sequence
            - **Transshipment**: Next vessel, connecting time, destination
            - **Empty**: Size, condition, repositioning needs
            
            **Step 2: Assign Yard Blocks**
            - Import blocks: Near gate (fast truck access)
            - Export blocks: Near berth (fast vessel loading)
            - Transship blocks: Central or near berthing vessel
            - Reefer blocks: Near power racks
            - DG blocks: Segregated safety area
            
            **Step 3: Optimize Stack Position**
            
            **FILO Principle (First In, Last Out):**
            - Container arriving today → Bottom of stack
            - Container leaving tomorrow → Top of stack
            - Minimizes reshuffles
            
            **Algorithm Considers:**
            - **Dwell time**: How long will it stay?
            - **Next move**: When will it leave?
            - **Weight**: Heavy on bottom
            - **Type**: Reefer, DG, OOG, regular
            - **Connecting vessel**: Tight connection? Priority location
            """)
        
        with col2:
            st.markdown("""
            ### Smart Stacking Strategies
            
            **Dwell Time Prediction:**
            
            CITOS uses historical data and machine learning to predict:
            - **Import container**: When will consignee pick it up?
              - Average: 3-5 days
              - Rush cargo: <24 hours
              - Slow cargo: 7+ days
            
            - **Export container**: When will vessel load it?
              - Known: Vessel sailing date
              - Stack in reverse load sequence
            
            - **Transship container**: When does connecting vessel arrive?
              - Known: Next vessel ETA
              - Tight connection: Priority area
            
            **Reshuffle Minimization:**
            
            **Target**: <15% reshuffle rate
            
            **How CITOS Achieves This:**
            
            **1. Pre-Marshaling:**
            - Before vessel loading
            - Reorganize stacks into load sequence
            - Time-consuming but reduces vessel delays
            
            **2. Dedicated Stacks:**
            - One stack = one vessel load sequence
            - Clean loading (no reshuffles)
            
            **3. Height Discipline:**
            - Stack 5 high (manual RTG)
            - Stack 6-7 high (automated RMG)
            - Don't over-stack
            
            **4. Weight Segregation:**
            - Heavy containers (30 tons): Ground level only
            - Light containers (<15 tons): Can go high
            
            **5. Smart Grouping:**
            - Group by destination port
            - Group by vessel
            - Group by discharge sequence
            
            **Performance Metrics:**
            - **Reshuffle %**: Reshuffles / Total moves
            - **Target**: <15%
            - **World-class**: <10%
            - **Singapore**: 10-15% typical
            """)
        
        st.success("""
        **Real Example:** Container arriving from vessel today, transshipping to another vessel in 3 days.
        
        - **Day 1**: Discharged from Vessel A, CITOS assigns to Transship Block C, Row 15, Tier 2 (middle height)
        - **Day 2-3**: Sits in stack (no movement)
        - **Day 4**: Connecting Vessel B arrives, CITOS schedules retrieval, YC picks from Tier 2 (only 1 reshuffle!)
        - If poorly planned, could be Tier 1 with 5 containers on top → 5 reshuffles!
        """)
    
    # Vessel Planning
    with st.expander("**3. Vessel Planning System** - Move-by-Move Optimization"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            ### Vessel Stow Planning
            
            **The Challenge:**
            
            A 24,000 TEU vessel needs to load 5,000 containers.
            - **Where does each container go on the ship?**
            - Must balance for stability
            - Must sequence by port of discharge
            - Must respect weight limits
            - Must avoid dangerous goods conflicts
            
            **CITOS Vessel Planning Module:**
            
            **Inputs:**
            - Vessel bay plan (ship's structure)
            - Container list (5,000 containers to load)
            - Container attributes:
              - Size: 20ft, 40ft, 45ft
              - Weight: 5-30 tons
              - Type: Dry, reefer, DG, OOG
              - Destination: Rotterdam, Hamburg, Antwerp
              - Special requirements
            
            **Constraints:**
            
            **1. Vessel Stability:**
            - Must balance weight fore/aft
            - Must balance weight port/starboard
            - Center of gravity must be correct
            - Prevent listing (tilting)
            - Critical for safety at sea
            
            **2. Discharge Sequence:**
            - **First port** (Rotterdam): Containers on TOP
            - **Second port** (Hamburg): Containers in MIDDLE
            - **Last port** (Antwerp): Containers on BOTTOM
            - Prevents excessive reshuffles at discharge ports
            
            **3. Reefer Plugs:**
            - Limited number of power plugs on ship
            - Reefers must go in plug positions
            - Can't oversubscribe plugs
            
            **4. Dangerous Goods:**
            - Must segregate by class
            - Minimum separation distances
            - Away from crew quarters
            - Specific deck positions
            """)
        
        with col2:
            st.markdown("""
            ### Loading Sequence Optimization
            
            **After stow plan is created, CITOS generates loading sequence:**
            
            **Goal:** Minimize crane moves and time
            
            **Challenges:**
            
            **1. Hatch Cover Constraints:**
            - Can't load hold until hatch covers removed
            - Can't close hatch until hold loading complete
            - Sequence must respect this
            
            **2. Bay Sequence:**
            - Load bays in efficient order
            - Minimize crane travel distance
            - Coordinate multiple cranes
            
            **3. Crane Interference:**
            - 8 cranes working simultaneously
            - Can't cross paths
            - Must coordinate reach zones
            
            **4. Deck vs Hold:**
            - Load holds first (below deck)
            - Then load deck (above deck)
            - Hatch covers replaced between
            
            **Optimization Algorithm:**
            
            **CITOS considers:**
            - Yard location of each container
            - PM/AGV travel time
            - Crane availability
            - Load sequence efficiency
            - Dual-cycle opportunities
            
            **Dual Cycling:**
            - Crane discharges import container
            - **Immediately** picks up export container
            - No idle time
            - Increases productivity 20-30%
            - Requires perfect coordination
            
            **Output:**
            - Move-by-move loading sequence
            - Each move: Container ID, from yard location, to vessel position
            - Crane assignment for each move
            - Expected completion time
            - Crane Intensity (CI) target
            """)
        
        st.warning("""
        **Complexity:** For an 8,000-move vessel with 8 cranes:
        
        - **8,000 moves** to sequence
        - **8 cranes** to coordinate
        - **Millions of possible** sequences
        - **Constraints**: Stability, sequence, segregation, timing
        - **Goal**: Find optimal sequence in <1 hour
        - **CITOS**: Uses heuristic algorithms + optimization
        - **Result**: Near-optimal sequence that achieves <30-36 hours turnaround
        """)
    
    # Equipment Dispatch
    with st.expander("**4. Equipment Dispatch System** - Real-Time Coordination"):
        st.markdown("""
        ### Managing the Fleet
        
        **The Equipment Fleet (Typical Terminal):**
        
        - **20 Quay Cranes** (QC)
        - **50 Prime Movers** (PM) or AGVs
        - **30 Yard Cranes** (RTG/RMG)
        - **Plus**: Reefer trucks, empty handlers, maintenance vehicles
        
        **The Challenge:** Coordinate all equipment in real-time to support vessel operations
        
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **PM/AGV Deployment System:**
            
            **Each Container Move Requires:**
            1. QC picks container from vessel
            2. Places on PM/AGV
            3. PM/AGV transports to yard
            4. YC picks from PM/AGV
            5. YC stacks in yard
            6. PM/AGV returns to QC for next container
            
            **System Must:**
            - **Match PM/AGV to QC** at right time
            - **Route PM/AGV** to correct yard block
            - **Minimize empty travel** (deadheading)
            - **Balance workload** across fleet
            - **Handle breakdowns** dynamically
            
            **Automated vs Manual:**
            
            **Manual PM (Human Driver):**
            - Driver receives instruction on tablet
            - Drives to QC, receives container
            - Drives to yard block shown on screen
            - YC picks container
            - Driver returns
            - **Flexibility**: Can handle exceptions
            - **Variability**: Human factors (skill, fatigue)
            
            **Automated AGV:**
            - AGV guided by GPS/magnetic markers
            - System assigns job automatically
            - Optimal route calculated
            - No human intervention
            - **Consistency**: Same speed every time
            - **Efficiency**: Optimal routes always
            - **Limitation**: Can't handle exceptions well
            """)
        
        with col2:
            st.markdown("""
            **Yard Crane Coordination:**
            
            **Each Yard Crane:**
            - Covers specific yard block
            - Handles both import and export
            - Must coordinate with PMs/AGVs
            - Balances stacking and retrieval
            
            **Optimization Goals:**
            - **Minimize PM/AGV waiting** (truck arrives, YC picks immediately)
            - **Maximize YC productivity** (always has containers to handle)
            - **Reduce congestion** (avoid bottlenecks)
            
            **Queue Management:**
            
            **Problem:** 5 PMs arrive at yard block simultaneously
            - Only 1 YC available
            - PMs must wait in queue
            - Delays vessel operations
            
            **Solution:** CITOS predictive dispatch
            - Knows which containers loading soon
            - Pre-retrieves containers from yard
            - Stages near handover zone
            - Reduces PM waiting time
            
            **Real-Time Adjustments:**
            
            **Equipment Breakdown:**
            - PM breaks down mid-operation
            - CITOS detects (no movement for 10 min)
            - Automatically assigns backup PM
            - Reroutes jobs
            - Minimal disruption
            
            **Weather Impact:**
            - Wind >30 knots → QC operations stop
            - CITOS pauses vessel operations
            - Redeploys equipment to yard
            - Prioritizes critical tasks
            - Resumes when safe
            """)
        
        st.info("""
        **Real-Time Performance:**
        - **PM/AGV tracking**: GPS updates every 5 seconds
        - **Job assignment**: <1 second system response
        - **Route optimization**: Real-time traffic consideration
        - **Breakdown detection**: Within 10 minutes
        - **Recovery action**: Automatic reassignment
        """)
    
    st.markdown("---")
    st.markdown('<p class="section-header">PORTNET - The Port Community Platform</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        ### Singapore's Digital Port Ecosystem
        
        **PORTNET** is Singapore's port community system - connecting the entire maritime ecosystem digitally.
        
        **Launched:** 1984 (World's first nationwide port IT system!)
        
        **What PORTNET Does:**
        
        PORTNET is the **digital integration layer** that connects:
        - **Port operators** (PSA, Jurong Port)
        - **Shipping lines** (Maersk, MSC, CMA CGM, etc.)
        - **Freight forwarders** (logistics companies)
        - **Hauliers** (trucking companies)
        - **Government agencies** (Customs, Immigration, MPA)
        - **Service providers** (bunker suppliers, chandlers)
        
        **Key Functions:**
        
        **1. Berth Application & Management**
        - Shipping line submits berth request
        - Receives berth confirmation
        - Updates on berth readiness
        - Departure clearance
        
        **2. Cargo Documentation**
        - **Manifest submission** (vessel cargo list)
        - **Shipping instructions** (export containers)
        - **Delivery orders** (import release)
        - **Dangerous goods** declarations
        - **VGM certificates** (weight verification)
        
        **3. Customs Integration**
        - Import declarations
        - Export permits
        - Duty calculations
        - Automated clearance (green lane)
        - Inspection scheduling (red lane)
        
        **4. Truck Operations**
        - Truck booking system
        - Gate appointment scheduling
        - Container availability check
        - Pickup authorization
        """)
        
        st.markdown("""
        **5. Marine Services**
        - Pilotage booking
        - Tugboat requests
        - Bunkering orders
        - Water supply
        - Waste disposal
        
        **6. Transshipment Coordination**
        - Connecting vessel information
        - Tight connection alerts
        - Load confirmation
        
        **The Power of Integration:**
        
        **Before PORTNET (1980s):**
        - **Paper-based** documentation
        - **Manual submissions** to multiple agencies
        - **Phone/fax** communication
        - **Days** for customs clearance
        - **High error rates**
        - **No real-time visibility**
        
        **With PORTNET:**
        - **100% digital**
        - **Single submission** to all agencies
        - **Real-time updates**
        - **Hours** for customs clearance
        - **Automated validation** (fewer errors)
        - **Complete visibility**
        
        **EDI Standards:**
        - PORTNET uses **UN/EDIFACT** standard
        - Common data formats
        - Automated processing
        - Machine-to-machine communication
        """)
    
    with col2:
        st.markdown('<div class="success-box">', unsafe_allow_html=True)
        st.markdown("""
        ### 📊 PORTNET By Numbers
        
        **Users & Scale:**
        - **10,000+** registered users
        - **220+ million** transactions/year
        - **24/7** availability
        - **99.9%** uptime
        
        **User Categories:**
        
        **Carrier Community:**
        - 100+ shipping lines
        - 50+ ship agents
        - 200+ feeder operators
        
        **Logistics Community:**
        - 1,000+ freight forwarders
        - 500+ hauliers
        - 300+ consolidators
        
        **Government:**
        - Singapore Customs
        - Immigration & Checkpoints Authority (ICA)
        - Maritime & Port Authority (MPA)
        - Other agencies
        
        **Service Providers:**
        - Bunker suppliers
        - Ship chandlers
        - Container depots
        - Repair facilities
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("""
        ### 🔄 Example Flow
        
        **Import Container Journey:**
        
        **Day -2:** Vessel at sea
        - Shipping line submits manifest via PORTNET
        - PSA receives cargo details
        - Customs pre-processes
        
        **Day 0:** Vessel arrives
        - Berth confirmed via PORTNET
        - Container discharged
        - Location updated in system
        
        **Day 1:** Customs clearance
        - Importer submits declaration via PORTNET
        - Customs auto-clears (green lane)
        - Delivery order issued
        
        **Day 2:** Truck pickup
        - Haulier books gate slot via PORTNET
        - Checks container availability
        - Receives authorization
        
        **Day 3:** Collection
        - Truck enters gate
        - System validates (PORTNET data)
        - Container released in 25 seconds
        - Real-time update to all parties
        
        **All Paperless. All Digital.**
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown('<p class="section-header">Advanced Technologies</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🤖 Automation Technologies
        
        **Flow-Through Gate System:**
        
        **Fully automated truck processing:**
        1. Truck approaches gate
        2. **ANPR**: Cameras read license plate
        3. **RFID**: Driver's PSA Pass scanned
        4. **Biometric**: Fingerprint verification
        5. **OCR**: Container number captured
        6. **Weighbridge**: Automatic weighing
        7. **System validation**: Manifest check
        8. **Auto-clearance**: <25 seconds total!
        9. **SMS**: Yard location sent to driver
        
        **Benefits:**
        - **10x faster** than manual processing
        - **Zero paperwork**
        - **Lower error rate**
        - **Better security**
        - **Real-time data**
        
        **Won UK Award (1999)** for innovation
        
        **Remote Crane Operations (RCOC):**
        
        **Traditional:**
        - Operator sits in crane cabin
        - 40-50 meters high
        - Physical strain
        - Weather exposed
        
        **Remote Control (2000+):**
        - Operator in air-conditioned control room
        - Multiple cameras provide view
        - Ergonomic workstation
        - Can control multiple cranes
        - **50% productivity increase**
        - **Better operator welfare**
        """)
    
    with col2:
        st.markdown("""
        ### 🧠 AI & Machine Learning
        
        **Predictive Analytics:**
        
        **Container Dwell Time Prediction:**
        - Analyzes historical data
        - Predicts when import will be collected
        - Accuracy: 80%+
        - Used for yard planning
        - Reduces reshuffles 15-20%
        
        **Equipment Failure Prediction:**
        - Monitors equipment sensors
        - Predicts failures before they happen
        - Schedules preventive maintenance
        - Reduces breakdowns 30%
        - Improves uptime
        
        **Demand Forecasting:**
        - Predicts vessel volumes
        - Seasonal patterns
        - Holiday effects
        - Helps resource planning
        
        **Optimization Algorithms:**
        
        **Berth Allocation:**
        - Heuristic algorithms
        - Considers 100+ constraints
        - Near-optimal solution in seconds
        - Achieves BOA >90%
        
        **Yard Stacking:**
        - Genetic algorithms
        - Minimizes expected reshuffles
        - Adapts to changing conditions
        - Real-time re-optimization
        
        **Route Optimization:**
        - AGV path planning
        - Avoid congestion
        - Minimize distance
        - Dynamic re-routing
        """)
    
    with col3:
        st.markdown("""
        ### 📡 IoT & Connectivity
        
        **Smart Containers:**
        - GPS tracking devices
        - Temperature sensors (reefers)
        - Location updates every 15 min
        - Geofencing alerts
        - Predictive arrival times
        
        **Equipment Sensors:**
        - **Crane health monitoring**
          - Load sensors
          - Motor temperature
          - Hydraulic pressure
          - Vibration analysis
        
        - **PM/AGV telemetry**
          - Real-time GPS
          - Battery status
          - Speed monitoring
          - Collision detection
        
        **5G Network (Tuas):**
        - Ultra-low latency (<10ms)
        - High bandwidth
        - Massive device connectivity
        - Enables real-time automation
        - Remote crane operation
        
        **Blockchain (Future):**
        - **Digital Bill of Lading**
        - Immutable records
        - Faster trade finance
        - Fraud prevention
        
        **Current Pilots:**
        - TradeTrust (Singapore)
        - Maersk + IBM TradeLens
        - Global Shipping Business Network
        """)
    
    st.markdown("---")
    st.markdown('<p class="section-header">Integration with Global Systems</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore's port doesn't operate in isolation - it's part of a global digital ecosystem.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Shipping Line Integration
        
        **Major Lines Connected:**
        - Maersk (Denmark)
        - MSC (Switzerland)
        - CMA CGM (France)
        - COSCO (China)
        - Hapag-Lloyd (Germany)
        - ONE (Japan)
        - Evergreen (Taiwan)
        - 100+ total
        
        **Data Exchanged:**
        - **Vessel schedules** (advance notification)
        - **Cargo manifests** (container details)
        - **Stow plans** (vessel loading plans)
        - **Booking confirmations**
        - **Equipment interchange receipts** (EIR)
        - **Performance reports** (crane productivity)
        
        **Communication Methods:**
        - **EDI** (Electronic Data Interchange)
        - **API** connections (real-time)
        - **Web portals** (user interfaces)
        - **Mobile apps**
        
        **Standards Used:**
        - UN/EDIFACT (traditional)
        - XML/JSON (modern APIs)
        - BAPLIE (bay plan message)
        - COPRAR (container report)
        - COARRI (arrival message)
        """)
        
        st.markdown("""
        ### Customs & Government Integration
        
        **Singapore Customs (Fully Integrated):**
        
        **TradeNet System:**
        - Import/export declarations
        - Permit applications
        - Duty calculations
        - Automated clearance
        
        **Integration Flow:**
        1. PORTNET receives manifest
        2. Auto-submits to TradeNet
        3. Customs risk assessment
        4. **Green lane**: Auto-clear (80%+)
        5. **Red lane**: Inspection required
        6. Result back to PORTNET
        7. Updates all parties
        
        **Benefits:**
        - **<2 hours** clearance (vs days previously)
        - **24/7** processing
        - **Paperless** trade
        - **Lower costs**
        """)
    
    with col2:
        st.markdown("""
        ### Global Port Network
        
        **PSA Operates 60+ Terminals Globally:**
        
        **Asia:**
        - Singapore (7 terminals)
        - China (Guangzhou, Tianjin)
        - India (multiple ports)
        - Thailand, Vietnam, Indonesia
        
        **Europe:**
        - Belgium (Antwerp)
        - Italy, Portugal
        
        **Americas:**
        - USA (multiple terminals)
        - Panama, Colombia
        
        **CITOS Deployed Globally:**
        - Same system across network
        - Data sharing between terminals
        - Transshipment coordination
        - Best practices transfer
        
        **Network Benefits:**
        
        **For Shipping Lines:**
        - Consistent interface
        - One system to learn
        - Seamless transshipment
        - Integrated tracking
        
        **For PSA:**
        - Economies of scale
        - Shared development costs
        - Global visibility
        - Learning across terminals
        
        **Global PORTNET Concept:**
        
        Future vision:
        - PORTNET Singapore
        - PORTNET Guangzhou
        - PORTNET Antwerp
        - All interconnected
        - Seamless global network
        """)
    
    st.markdown("---")
    st.markdown('<p class="section-header">The Future: Next-Generation Technologies</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🚀 Emerging Technologies
        
        **Tuas Next-Gen Port:**
        
        **AI Control Center:**
        - **Centralized operations**
        - Monitor entire port from one location
        - AI-powered decision support
        - Predictive alerts
        - Autonomous operations oversight
        
        **Full Autonomy:**
        - **Autonomous QCs** (already testing)
        - **Autonomous AGVs** (deployed)
        - **Autonomous YCs** (partially deployed)
        - **Autonomous trucks** (testing at gate)
        - Goal: Fully automated terminal by 2030
        
        **Digital Twin:**
        - **Virtual replica** of entire port
        - Real-time synchronization
        - Simulation and testing
        - "What-if" scenarios
        - Training environment
        - Optimization laboratory
        
        **5G/6G Networks:**
        - Ultra-reliable low-latency
        - Massive IoT connectivity
        - Edge computing
        - Real-time video analytics
        """)
        
        st.markdown("""
        **Quantum Computing (Future):**
        - Complex optimization problems
        - Vessel scheduling
        - Yard planning
        - Resource allocation
        - Could solve in seconds vs hours
        
        **Drone Technology:**
        - **Automated inspections**
        - Container damage surveys
        - Inventory verification
        - Security patrols
        - Reefer temperature checks
        """)
    
    with col2:
        st.markdown("""
        ### 🌐 Blockchain & Distributed Systems
        
        **Electronic Bill of Lading (eBL):**
        
        **Problem with Paper B/L:**
        - Physical document required
        - Courier shipping costs
        - 5-7 days transit time
        - Cargo arrives before document!
        - Fraud risk (duplicate documents)
        
        **Blockchain Solution:**
        - **Digital B/L** on blockchain
        - Instant transfer
        - Tamper-proof
        - Multi-party verification
        - Cost savings: $4-6B globally
        
        **Singapore Initiatives:**
        
        **TradeTrust:**
        - Digital trade documents
        - Blockchain-based
        - Interoperable
        - Government-backed
        
        **ICC TradeFlow:**
        - Letter of Credit on blockchain
        - Faster trade finance
        - Lower risk
        
        **Benefits:**
        - **Speed**: Hours vs days
        - **Cost**: 80% reduction
        - **Security**: Immutable records
        - **Transparency**: All parties see
        - **Finance**: Faster settlements
        """)
        
        st.markdown("""
        **Smart Contracts:**
        
        **Automated Execution:**
        - Contract terms in code
        - Triggers automatic actions
        - No manual intervention
        
        **Example:**
        - Container delivered on time
        - Smart contract verifies (GPS + system)
        - Payment automatically released
        - Demurrage calculated automatically
        - Faster settlements
        """)
    
    st.markdown("---")
    
    st.info("""
    **📚 Related Sections:**
    
    - **Port Operations**: See how CITOS orchestrates the actual physical operations
    - **Terminal Equipment**: Learn about the equipment CITOS controls
    - **KPIs**: Understand the metrics CITOS tracks and optimizes
    - **Singapore & Tuas**: See CITOS evolution and Tuas next-gen implementation
    """)
    
    st.markdown("---")
    
    st.markdown('<div class="success-box">', unsafe_allow_html=True)
    st.markdown("""
    ### 🎓 Key Takeaways - CITOS & Technology
    
    **CITOS = The Orchestrator:**
    - Terminal Operating System managing entire port
    - Deployed since 1988 (pioneer)
    - Plans, executes, monitors, optimizes all operations
    - Handles 60+ vessels, 100K+ containers, 10K+ trucks daily
    
    **Four Core Modules:**
    - **Berth Planning**: BOA >90% achievement
    - **Yard Planning**: Minimize reshuffles, optimize storage
    - **Vessel Planning**: Stow plans and loading sequences
    - **Equipment Dispatch**: Real-time fleet coordination
    
    **PORTNET = The Connector:**
    - Singapore's port community platform (since 1984)
    - Connects all maritime stakeholders digitally
    - 10,000+ users, 220M+ transactions/year
    - Paperless, real-time, 24/7
    
    **Technology Evolution:**
    - **1980s**: Basic automation, PORTNET launched
    - **1990s**: CITOS deployed, EDI integration
    - **2000s**: Remote cranes, flow-through gates
    - **2010s**: AI/ML, predictive analytics, IoT
    - **2020s**: Full autonomy, blockchain, digital twin
    - **2030s+**: Quantum computing, 6G, full AI control
    
    **Competitive Advantage:**
    - Technology enables Singapore's efficiency
    - Without CITOS/PORTNET: Can't achieve world-class performance
    - Continuous innovation maintains lead
    - Tuas represents next quantum leap
    """)
    st.markdown('</div>', unsafe_allow_html=True)
