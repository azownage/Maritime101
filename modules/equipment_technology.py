import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">🤖 Equipment, Automation & CITOS</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand the equipment used in container terminals, automation technologies transforming operations, 
    and PSA's CITOS terminal operating system that coordinates all activities.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Quay-Side Equipment (Vessel Interface)
    # ============================================================================
    
    st.markdown('<p class="section-header">Quay-Side Equipment: Ship-to-Shore Interface</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Quay-side equipment handles the critical interface between vessel and terminal, transferring containers 
    from ship to shore and vice versa.
    """)
    
    st.markdown('<p class="subsection-header">Ship-to-Shore (STS) Quay Cranes</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Design and Specifications:**
    
    **Physical Dimensions:**
    - **Height**: 70-100+ metres above ground (taller than 20-storey building)
    - **Outreach**: 60-80 metres (to reach containers on mega vessels 24 containers wide)
    - **Back reach**: 15-25 metres (for landside operations)
    - **Lift height**: 35-50 metres above quay
    - **Rail gauge**: 30-35 metres (distance between crane rails)
    
    **Capacity:**
    - **Lifting capacity**: 50-65 tonnes (twin-lift: two 20ft containers or one 40ft)
    - **Hoisting speed**: 60-90 metres/minute (empty), 40-60 m/min (loaded)
    - **Trolley speed**: 180-240 metres/minute
    - **Gantry speed**: 30-45 metres/minute (crane travelling along quay)
    
    **Performance:**
    - **Gross moves per hour (GMPH)**: 25-35 containers/hour (industry average)
    - **World-class**: 35-45 GMPH
    - **Peak performance**: 50+ GMPH achievable in ideal conditions
    """)
    
    # Quay crane specifications
    qc_specs = pd.DataFrame({
        'Specification': [
            'Outreach',
            'Back Reach',
            'Lift Height',
            'Lifting Capacity',
            'Hoisting Speed (Loaded)',
            'Trolley Speed',
            'Gantry Speed',
            'Target Productivity',
            'Typical Cost',
            'Lifespan'
        ],
        'Panamax Crane': [
            '45-50m (13 containers across)',
            '15m',
            '35m',
            '40-50 tonnes',
            '45 m/min',
            '180 m/min',
            '30 m/min',
            '25-30 GMPH',
            '$5-8 million',
            '25-30 years'
        ],
        'Post-Panamax Crane': [
            '50-65m (18 containers across)',
            '20m',
            '40m',
            '50-60 tonnes',
            '50 m/min',
            '200 m/min',
            '35 m/min',
            '30-35 GMPH',
            '$10-13 million',
            '25-30 years'
        ],
        'Super Post-Panamax': [
            '65-80m (24 containers across)',
            '25m',
            '50m',
            '60-65 tonnes',
            '60 m/min',
            '240 m/min',
            '45 m/min',
            '35-40 GMPH',
            '$13-18 million',
            '25-30 years'
        ]
    })
    
    st.dataframe(qc_specs, width='stretch', hide_index=True)
    
    st.markdown("""
    **Key Components:**
    
    **Spreader:**
    - Device that attaches to containers via corner castings
    - **Telescoping**: Extends/retracts to handle 20ft or 40ft containers
    - **Twistlocks**: Mechanical locks that secure to container corners
    - **Sensors**: Detect container position and weight
    - **Types**: Single-lift (one container), Twin-lift (two 20ft), Tandem-lift (two 40ft stacked)
    
    **Control System:**
    - **Operator cabin**: Positioned high on crane for visibility
    - **Computer-assisted**: Anti-sway system, collision avoidance, position tracking
    - **Semi-automation**: Spreader auto-lands on container corners
    - **Full automation (ASC)**: Automated Stacking Cranes operate without human in cabin
    
    **Power Supply:**
    - **Traditional**: Diesel generators on crane
    - **Modern**: Electric power from shore (eco-friendly, quieter, cleaner)
    - **Hybrid**: Combination diesel-electric with regenerative braking
    """)
    
    st.markdown('<p class="subsection-header">Quay Crane Operations</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Operating Cycle (Discharge):**
    1. **Positioning**: Trolley moves over vessel hatch
    2. **Lowering**: Spreader lowers to container on vessel
    3. **Locking**: Twistlocks engage container corner castings
    4. **Hoisting**: Container lifted from vessel
    5. **Trolley move**: Container transported to landside
    6. **Lowering**: Container lowered to prime mover/AGV on apron
    7. **Unlocking**: Spreader releases container
    8. **Return**: Empty spreader returns to vessel for next container
    
    **Cycle time**: 60-90 seconds per container (world-class: <60 seconds)
    
    **Factors Affecting Productivity:**
    - **Container location**: Deck containers faster than hold containers (no hatch covers)
    - **Container weight**: Heavier containers = slower hoisting
    - **Vessel lashing**: Time to unlock securing equipment
    - **Equipment availability**: Prime movers/AGVs ready when crane ready
    - **Weather**: High winds (>15 m/s) can stop operations
    - **Operator skill**: Experienced operators 20-30% faster
    - **Crane maintenance**: Well-maintained cranes have less downtime
    """)
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 Triple Hoist Technology:</strong><br><br>
    Modern quay cranes feature <strong>three independent hoists</strong>:<br>
    - <strong>Main hoist</strong>: Lifts containers (primary)<br>
    - <strong>Auxiliary hoist</strong>: Backup and special cargo<br>
    - <strong>Boom hoist</strong>: Adjusts crane boom angle<br><br>
    <strong>Benefit</strong>: Whilst main hoist lowers container landside, auxiliary hoist can already be picking up 
    next container from vessel, reducing cycle time by 15-20%.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 2: Yard Equipment (Storage Operations)
    # ============================================================================
    
    st.markdown('<p class="section-header">Yard Equipment: Container Storage and Handling</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Yard equipment moves containers within the storage area, stacking them efficiently and retrieving them 
    when needed.
    """)
    
    st.markdown('<p class="subsection-header">Rubber-Tyred Gantry Cranes (RTG)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Design:**
    - Gantry crane on rubber tyres that straddles container stacks
    - Can move freely within yard block
    - Operator cabin on top or ground-level remote control
    
    **Specifications:**
    - **Span**: 6-8 containers wide (typical: 6+1 configuration)
    - **Stacking height**: 5-7 containers high (6 high typical)
    - **Lane**: One truck lane under crane (for loading/unloading)
    - **Lifting capacity**: 40-50 tonnes
    - **Stacking speed**: 10-15 moves per hour
    
    **Advantages:**
    - **Flexible**: Can relocate between yard blocks
    - **Lower capital cost**: $2-3 million per RTG
    - **Simple infrastructure**: No rails required
    
    **Disadvantages:**
    - **Diesel-powered**: Traditional RTGs produce emissions
    - **Higher operating cost**: Fuel consumption
    - **Operator intensive**: Requires skilled operators
    """)
    
    st.markdown('<p class="subsection-header">Rail-Mounted Gantry Cranes (RMG)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Design:**
    - Gantry crane on fixed rails, cannot relocate
    - Electric-powered (overhead cable or busbar)
    - Can be semi-automated or fully automated (ARMG)
    
    **Specifications:**
    - **Span**: 6-10 containers wide
    - **Stacking height**: 5-8 containers high (automated: up to 10 high)
    - **Lifting capacity**: 40-65 tonnes
    - **Stacking speed**: 15-20 moves per hour (automated: 20-25)
    
    **Advantages:**
    - **Electric power**: Zero emissions, lower operating costs
    - **Automation-ready**: Can be fully automated (ARMG)
    - **Higher productivity**: Faster and more consistent than RTG
    - **Precision**: Computer-controlled positioning
    
    **Disadvantages:**
    - **Fixed location**: Cannot move between blocks
    - **Higher capital cost**: $3-5 million per RMG + rail infrastructure
    - **Infrastructure required**: Rails, electrical systems
    """)
    
    st.markdown('<p class="subsection-header">Automated RMG (ARMG)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Full Automation:**
    - No operator required
    - Computer-controlled via TOS
    - Sensors and cameras for positioning
    - Remote monitoring from control room
    
    **Performance:**
    - **24/7 operations**: No breaks, shifts, fatigue
    - **Consistent productivity**: 20-25 moves per hour
    - **Higher stacking**: Up to 10 containers high (no operator safety limit)
    - **Precision**: ±2cm positioning accuracy
    
    **Benefits:**
    - **Labour savings**: 70-80% reduction in yard crane operators
    - **Safety**: No humans in yard block, fewer accidents
    - **Efficiency**: Optimal path planning, no idle time
    - **Space**: Higher stacking = more capacity per hectare
    
    **Challenges:**
    - **Very high capital cost**: $5-8 million per ARMG + automation systems
    - **Complexity**: Sophisticated IT and maintenance requirements
    - **Transition**: Requires workforce retraining and organisational change
    """)
    
    st.markdown('<p class="subsection-header">Other Yard Equipment</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Reach Stackers:**
        - Mobile crane on wheels
        - Telescoping boom reaches over stacks
        - **Capacity**: 40-45 tonnes
        - **Stacking**: 4-5 high
        - **Use**: Flexible, smaller terminals, special cargo
        - **Cost**: $400,000-800,000
        
        **Advantages:**
        - Very flexible, can work anywhere
        - Lower capital cost
        - Good for low-volume operations
        
        **Disadvantages:**
        - Lower productivity (5-8 moves/hour)
        - Higher maintenance costs
        - Operator intensive
        """)
    
    with col2:
        st.markdown("""
        **Straddle Carriers:**
        - Mobile crane that straddles container
        - Lifts container from beneath
        - **Capacity**: 35-40 tonnes
        - **Stacking**: 3-4 high
        - **Use**: Combines transport + stacking
        - **Cost**: $600,000-1,000,000
        
        **Advantages:**
        - No separate transport equipment needed
        - Flexible operations
        - Direct vessel-to-yard or yard-to-gate
        
        **Disadvantages:**
        - Lower stacking height
        - Higher operating costs
        - Complex to operate
        """)
    
    # Equipment comparison
    equipment_comparison = pd.DataFrame({
        'Equipment': ['RTG', 'RMG', 'ARMG', 'Reach Stacker', 'Straddle Carrier'],
        'Capital Cost ($M)': [2.5, 4.0, 6.0, 0.6, 0.8],
        'Stacking Height': [6, 7, 10, 4, 3],
        'Moves/Hour': [12, 18, 23, 6, 8],
        'Power': ['Diesel', 'Electric', 'Electric', 'Diesel', 'Diesel'],
        'Automation': ['Manual', 'Semi-auto', 'Full auto', 'Manual', 'Manual'],
        'Flexibility': ['High', 'Low', 'Low', 'Very High', 'Very High']
    })
    
    st.dataframe(equipment_comparison, width='stretch', hide_index=True)
    
    # ============================================================================
    # SECTION 3: Horizontal Transport Equipment
    # ============================================================================
    
    st.markdown('<p class="section-header">Horizontal Transport: Moving Containers Around Terminal</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Horizontal transport equipment moves containers between quay cranes and yard storage, bridging the 
    critical interface.
    """)
    
    st.markdown('<p class="subsection-header">Prime Movers (Terminal Tractors)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Traditional Approach:**
    
    **Design:**
    - Heavy-duty tractor with trailer for containers
    - Human driver
    - Diesel-powered
    - **Speed**: 15-25 km/h in terminal
    
    **Operations:**
    - **Chassis system**: Container placed on separate chassis (trailer)
    - Prime mover hooks to chassis, transports to yard
    - Unhooks, returns to quay for next container
    - **Fleet size**: Typically 1.5-2 prime movers per quay crane
    
    **Advantages:**
    - **Proven technology**: Decades of operational experience
    - **Flexible**: Can adapt to exceptions and unusual situations
    - **Lower upfront cost**: $100,000-150,000 per unit
    
    **Disadvantages:**
    - **Labour intensive**: Requires many drivers
    - **Safety risks**: Human drivers, accident potential
    - **Emissions**: Diesel exhaust
    - **Inefficiency**: Empty return trips, waiting time
    - **Variability**: Driver skill affects productivity
    """)
    
    st.markdown('<p class="subsection-header">Automated Guided Vehicles (AGVs)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Modern Automated Approach:**
    
    **Design:**
    - Driverless electric vehicles
    - Battery-powered (lithium-ion, fast-charging)
    - Guided by embedded magnets, wires, or laser navigation
    - Lifts container from below (no separate chassis needed)
    
    **Navigation Systems:**
    - **Magnetic guidance**: Follow embedded magnetic strips in pavement (most common)
    - **Laser navigation**: Use lasers to detect position relative to fixed reflectors
    - **GPS/GNSS**: Satellite positioning (newer systems)
    - **Vision-based**: Cameras and AI for navigation (cutting edge)
    
    **Specifications:**
    - **Capacity**: 60-80 tonnes (including AGV weight)
    - **Speed**: 15-20 km/h loaded, 25 km/h empty
    - **Battery**: 2-4 hours operation, 15-30 minute fast charge
    - **Lifting**: Hydraulic platform lifts container from beneath
    
    **Fleet Management:**
    - **Central control system**: Computer dispatches AGVs dynamically
    - **Optimisation**: Minimises empty travel, balances workload
    - **Pooling**: AGVs shared across all quay cranes (not assigned to specific crane)
    - **Collision avoidance**: Sensors prevent AGV-to-AGV collisions
    - **Traffic management**: Optimal routing, congestion avoidance
    
    **Advantages:**
    - **Labour savings**: No drivers required (70-80% labour reduction)
    - **24/7 operations**: No breaks, shifts, or fatigue
    - **Consistency**: Predictable performance
    - **Safety**: No human drivers in operations area
    - **Zero emissions**: Electric power
    - **Efficiency**: Optimal routing, minimal empty travel
    - **Scalability**: Easy to add more AGVs as needed
    
    **Disadvantages:**
    - **Very high capital cost**: $300,000-500,000 per AGV
    - **Infrastructure**: Magnetic strips, charging stations, control systems
    - **Complexity**: Sophisticated software and maintenance
    - **Inflexibility**: Cannot handle exceptions as well as humans
    - **Dependency**: System failure affects entire fleet
    """)
    
    st.markdown('<p class="subsection-header">Automated Lift Vehicles (ALVs)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Next-Generation Alternative:**
    
    **Design:**
    - Automated vehicle with integrated lifting capability
    - Can lift container higher than AGV (stacks 2-3 high)
    - No need for separate yard crane in some configurations
    - Battery-powered, automated navigation
    
    **Capability:**
    - **Direct stacking**: Can place container in yard without yard crane
    - **Higher productivity**: Eliminates yard crane bottleneck
    - **Flexible operations**: Adapts to different workflows
    
    **Status:**
    - Still relatively new technology
    - Used in some automated terminals
    - Higher complexity than standard AGVs
    - Cost: $500,000-700,000 per unit
    """)
    
    # PM vs AGV comparison
    pm_agv_comparison = pd.DataFrame({
        'Aspect': [
            'Capital Cost',
            'Operating Cost',
            'Labour Required',
            'Productivity',
            'Flexibility',
            'Safety',
            'Emissions',
            'Predictability'
        ],
        'Prime Movers': [
            '$100K-150K per unit',
            'High (fuel, maintenance, labour)',
            'One driver per PM',
            '3-4 cycles/hour',
            'High (human adaptability)',
            'Moderate (human error risk)',
            'Diesel emissions',
            'Variable (driver dependent)'
        ],
        'AGVs': [
            '$300K-500K per unit + infrastructure',
            'Lower (electricity, maintenance)',
            'Zero drivers (remote monitoring only)',
            '6-8 cycles/hour',
            'Moderate (programmed routes)',
            'High (no humans in operations)',
            'Zero (electric)',
            'High (consistent performance)'
        ]
    })
    
    st.dataframe(pm_agv_comparison, width='stretch', hide_index=True)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🎯 PM Deployment Strategy:</strong><br><br>
    <strong>Traditional Fixed Assignment:</strong><br>
    - 2 Prime Movers assigned to each Quay Crane<br>
    - PMs dedicated to "their" crane<br>
    - Simple coordination but inefficient (PMs idle when crane busy with another container)<br><br>
    <strong>Modern Pooling Strategy:</strong><br>
    - Fleet of PMs/AGVs shared across all cranes<br>
    - Dynamic dispatch by TOS based on:<br>
      - Which crane needs transport next<br>
      - Which PM/AGV is closest and available<br>
      - Minimise empty travel distance<br>
      - Balance workload across fleet<br><br>
    <strong>Result</strong>: 30-40% reduction in fleet size needed, higher utilisation, lower costs
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 4: Gate Complex Equipment
    # ============================================================================
    
    st.markdown('<p class="section-header">Gate Complex: Truck Entry and Exit</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The gate complex is where external trucks enter and exit the terminal to pick up or deliver containers.
    """)
    
    st.markdown('<p class="subsection-header">Gate Operations Systems</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Traditional Gate Process:**
    1. Truck arrives at gate
    2. **Documentation check**: Driver presents paperwork (delivery order, customs clearance)
    3. **Manual inspection**: Gate clerk verifies documents, container number, seal
    4. **System entry**: Clerk enters information into TOS
    5. **Gate pass issued**: Truck authorised to enter
    6. Time: 5-10 minutes per transaction
    
    **Modern Automated Gate:**
    
    **Optical Character Recognition (OCR):**
    - Cameras automatically read:
      - Licence plate number
      - Container number
      - Chassis number  
      - ISO code
      - Seal number
    - **Accuracy**: 95-98% recognition rate
    - **Speed**: Instant reading as truck passes
    
    **Automated Gate Operating System (GOS):**
    - Computer system validates truck appointment
    - Cross-checks container authorisation
    - Verifies customs clearance
    - Issues automated gate pass
    - Records transaction automatically
    
    **Automated Lane:**
    1. Truck arrives at gate lane (no stop)
    2. OCR cameras read all information
    3. Computer validates in real-time (<5 seconds)
    4. Traffic light signals: Green (authorised) or Red (problem)
    5. If green: Truck proceeds directly into terminal
    6. Time: 30-60 seconds per transaction
    
    **Benefits:**
    - **10x faster**: 30-60 seconds vs 5-10 minutes
    - **Higher accuracy**: No manual data entry errors
    - **Labour savings**: No gate clerks needed
    - **24/7 operations**: No staffing constraints
    - **Better tracking**: Automatic record of all movements
    """)
    
    st.markdown('<p class="subsection-header">Truck Appointment System</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Problem:** Without appointments, trucks arrive randomly → gate congestion, long queues
    
    **Solution:** **Truck Appointment System (TAS)**
    
    **How It Works:**
    - Trucking companies book time slots online (e.g., "Monday 2:00-2:30 PM")
    - System limits appointments per time slot (e.g., 20 trucks per 30 minutes)
    - Prevents overcrowding
    - Spreads demand throughout the day
    
    **Benefits:**
    - **Eliminate queues**: No more 2-hour waits at gates
    - **Predictability**: Trucks know their time slot
    - **Productivity**: Terminal can plan yard crane operations
    - **Environment**: Less truck idling = lower emissions
    
    **Incentives:**
    - **Off-peak pricing**: Discounts for appointments outside 9 AM - 5 PM
    - **Penalty fees**: Charge for no-shows or late arrivals
    - **Priority lanes**: Faster processing for appointment holders
    
    **Singapore Example:**
    - Mandatory TAS at major terminals
    - 30-minute time windows
    - Average gate time: <3 minutes
    - Virtually eliminated gate congestion
    """)
    
    # Gate performance metrics
    gate_performance = pd.DataFrame({
        'System Type': ['Traditional Manual', 'Semi-Automated', 'Fully Automated + TAS'],
        'Transaction Time': ['5-10 minutes', '2-3 minutes', '30-60 seconds'],
        'Throughput (trucks/hour/lane)': [6-12, 20-30, 60-80],
        'Labour Required': ['1-2 clerks per lane', '1 clerk per 2-3 lanes', 'Remote monitoring only'],
        'Accuracy': ['85-90% (human error)', '95-97%', '98-99%'],
        'Peak Hour Queues': ['30-60 minute waits', '10-15 minute waits', 'No queues']
    })
    
    st.dataframe(gate_performance, width='stretch', hide_index=True)
    
    # ============================================================================
    # SECTION 5: Automation Levels and Technologies
    # ============================================================================
    
    st.markdown('<p class="section-header">Automation Levels in Container Terminals</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Container terminals can be automated to different degrees, from conventional manual operations to 
    fully automated "lights-out" facilities.
    """)
    
    # Automation levels
    automation_levels = pd.DataFrame({
        'Level': [
            'Level 1: Conventional',
            'Level 2: Semi-Automated',
            'Level 3: Highly Automated',
            'Level 4: Fully Automated'
        ],
        'Quay Cranes': [
            'Manual operation',
            'Computer-assisted (anti-sway)',
            'Semi-automated positioning',
            'Fully automated (ASC)'
        ],
        'Horizontal Transport': [
            'Prime movers (human drivers)',
            'Prime movers + GPS tracking',
            'AGVs (automated)',
            'AGVs or ALVs'
        ],
        'Yard Operations': [
            'RTG (human operators)',
            'RTG with remote operation',
            'RMG semi-automated',
            'ARMG (fully automated)'
        ],
        'Gate': [
            'Manual documentation',
            'Some OCR, manual verification',
            'Automated OCR + validation',
            'Fully automated + TAS'
        ],
        'Labour Reduction': [
            'Baseline (100%)',
            '20-30% reduction',
            '50-60% reduction',
            '70-80% reduction'
        ],
        'Examples': [
            'Most ports worldwide',
            'Many modern terminals',
            'Singapore PSA (some terminals)',
            'Rotterdam (Maasvlakte II), Hamburg (CTA), Los Angeles (LBCT), Singapore (Tuas Phase 1)'
        ]
    })
    
    st.dataframe(automation_levels, width='stretch', hide_index=True)
    
    st.markdown("""
    **Automation Technologies:**
    
    **Sensors and Detection:**
    - **RFID tags**: Track equipment and containers
    - **GPS/GNSS**: Vehicle positioning
    - **LiDAR**: 3D environment scanning
    - **Cameras**: Visual inspection, OCR
    - **Load cells**: Weight measurement
    - **Proximity sensors**: Collision avoidance
    
    **Control Systems:**
    - **TOS integration**: Equipment controlled by Terminal Operating System
    - **Fleet management**: Optimise equipment deployment
    - **Collision avoidance**: Prevent equipment crashes
    - **Predictive maintenance**: IoT sensors monitor equipment health
    
    **Communication:**
    - **Wireless networks**: 4G/5G for real-time communication
    - **Edge computing**: Process data locally for faster response
    - **Cloud platforms**: Centralised data and analytics
    
    **Artificial Intelligence:**
    - **Machine learning**: Optimise equipment scheduling
    - **Computer vision**: Automated inspection, damage detection
    - **Predictive analytics**: Forecast demand, plan capacity
    - **Operational simulation**: Virtual simulation of terminal operations
    """)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ Automation Trade-offs:</strong><br><br>
    <strong>Advantages:</strong><br>
    - 70-80% labour reduction<br>
    - 24/7 consistent operations<br>
    - Higher safety (fewer human accidents)<br>
    - Better space utilisation (higher stacking)<br>
    - Lower long-term operating costs<br>
    - Environmental benefits (electric power)<br><br>
    <strong>Challenges:</strong><br>
    - <strong>Very high capital investment</strong>: $500M-1B+ for fully automated terminal<br>
    - <strong>Long payback period</strong>: 10-15 years to recover investment<br>
    - <strong>Complexity</strong>: Sophisticated IT and maintenance requirements<br>
    - <strong>Inflexibility</strong>: Harder to handle exceptions and unusual situations<br>
    - <strong>Workforce impact</strong>: Job displacement requires retraining and social management<br>
    - <strong>Technology risk</strong>: System failures affect entire terminal<br><br>
    <strong>Strategic Decision:</strong><br>
    - Greenfield (new) terminals → Often choose full automation<br>
    - Brownfield (existing) terminals → Gradual automation difficult and expensive<br>
    - Labour costs → High labour costs favour automation<br>
    - Throughput volume → High volumes justify investment
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 6: Non-Conventional Terminal Layouts
    # ============================================================================
    
    st.markdown('<p class="section-header">Non-Conventional Terminal Layouts</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Some automated terminals use innovative layouts that differ from conventional parallel-to-quay designs.
    """)
    
    st.markdown('<p class="subsection-header">Grid-Based Layout</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Concept:**
    - Yard organised in dense grid pattern
    - Automated cranes move in X-Y grid (like chess board)
    - Containers stored very densely with minimal space between
    
    **Advantages:**
    - **Maximum density**: 40-50% more capacity per hectare
    - **Efficient land use**: Critical in space-constrained ports
    - **Flexible storage**: Any container can go in any slot
    
    **Disadvantages:**
    - **Complex automation**: Requires sophisticated control systems
    - **Higher cost**: Specialised equipment and software
    
    **Example**: AutoStore-style systems (emerging in some ports)
    """)
    
    st.markdown('<p class="subsection-header">Perpendicular Layout</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Concept:**
    - Yard blocks positioned perpendicular to quay (90° rotated vs conventional)
    - AGVs travel longer distance but straighter paths
    - Automated RMGs serve multiple parallel yard blocks
    
    **Advantages:**
    - **Fewer RMGs needed**: Each RMG covers more area
    - **Simpler AGV routing**: Straight paths reduce complexity
    - **Better scalability**: Easy to extend inland
    
    **Disadvantages:**
    - **Longer transport distance**: AGVs travel further on average
    - **Layout constraints**: Requires specific terminal geometry
    
    **Example**: Some European automated terminals (Hamburg CTA)
    """)
    
    # ============================================================================
    # SECTION 7: PSA CITOS - Terminal Operating System
    # ============================================================================
    
    st.markdown('<p class="section-header">PSA CITOS®: Comprehensive Terminal Operating System</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **CITOS (Computer Integrated Terminal Operation System)** is PSA's proprietary Terminal Operating 
    System, developed in-house and deployed across PSA terminals globally.
    """)
    
    st.markdown('<p class="subsection-header">CITOS Development History</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Background:**
    - Developed by PSA starting in the 1980s
    - Originally for managing Singapore's container terminals
    - Continuously evolved over 40+ years
    - Now deployed in PSA terminals worldwide (Singapore, Belgium, Italy, Korea, China, etc.)
    - Considered one of the world's leading TOS platforms
    
    **Why Develop In-House?**
    - **Customisation**: Tailored exactly to PSA's operational philosophy
    - **Competitive advantage**: Proprietary system competitors cannot easily copy
    - **Control**: PSA controls development roadmap and features
    - **Integration**: Deep integration with PSA processes and equipment
    - **Continuous improvement**: Refined based on operational experience
    """)
    
    st.markdown('<p class="subsection-header">CITOS Core Modules</p>', unsafe_allow_html=True)
    
    # CITOS modules
    citos_modules = pd.DataFrame({
        'Module': [
            'Berth Planning Module',
            'Vessel Planning Module',
            'Yard Planning Module',
            'Resource Planning Module',
            'Equipment Control Module',
            'Gate Operating Module',
            'Reefer Monitoring Module',
            'Dangerous Goods Module',
            'PORTNET Integration',
            'Billing Module'
        ],
        'Primary Functions': [
            'Allocate vessels to berths, optimise BOA, schedule berth windows',
            'Generate discharge/loading plans, stowage coordination, crane work lists',
            'Allocate yard locations, minimise re-handles, track inventory',
            'Schedule QCs, YCs, PMs/AGVs, optimise utilisation',
            'Real-time dispatching, tracking, performance monitoring',
            'Truck appointments, OCR integration, automated authorisation',
            'Monitor temperature, power connections, alarms for refrigerated containers',
            'Track DG containers, ensure segregation compliance, safety alerts',
            'Exchange data with port authority, customs, shipping lines',
            'Track transactions, generate invoices, payment processing'
        ],
        'Key Technologies': [
            'Optimisation algorithms, conflict resolution',
            'Stability calculations, AI-powered stowage optimisation',
            'Machine learning for location prediction, re-handle minimisation',
            'Real-time optimisation, predictive maintenance alerts',
            'Fleet management, collision avoidance, route optimisation',
            'OCR, automated validation, TAS integration',
            'IoT sensors, automated alerts, remote monitoring',
            'Regulatory database, automated checking',
            'EDI, APIs, real-time data exchange',
            'Automated invoicing, payment tracking'
        ]
    })
    
    st.dataframe(citos_modules, width='stretch', hide_index=True)
    
    st.markdown('<p class="subsection-header">CITOS Information Flow</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Inputs to CITOS:**
    
    **From External Systems:**
    - **PORTNET**: Vessel schedules, port clearances, customs declarations
    - **Shipping Lines**: Container manifests, booking information, stowage requests
    - **Trucking Companies**: Delivery orders, pickup appointments
    - **Customs**: Clearance status, inspection requirements
    
    **From Terminal Equipment:**
    - **Cranes**: Position, status, productivity, faults
    - **AGVs/PMs**: Location, battery level, assignments
    - **Yard Cranes**: Position, inventory changes, equipment status
    - **Gates**: Truck arrivals, OCR readings, transactions
    - **Reefers**: Temperature readings, power status, alarms
    
    **CITOS Processing:**
    - **Planning algorithms**: Optimise berth, yard, equipment allocation
    - **Real-time coordination**: Dispatch equipment, adjust plans dynamically
    - **Exception handling**: Alert supervisors to problems, suggest solutions
    - **Performance tracking**: Calculate KPIs, identify bottlenecks
    
    **Outputs from CITOS:**
    
    **To Equipment Operators:**
    - **Quay crane operators**: Which container to pick next, where to place
    - **Yard crane operators**: Which container to retrieve, storage location
    - **AGV control system**: Dispatch instructions, routing
    - **Gate systems**: Authorisation decisions, truck routing
    
    **To Management:**
    - **Dashboards**: Real-time operations overview
    - **KPI reports**: Productivity, utilisation, delays
    - **Alert notifications**: Equipment failures, delays, exceptions
    - **Historical analytics**: Trends, patterns, improvement opportunities
    
    **To External Stakeholders:**
    - **PORTNET**: Vessel status, cargo manifests, berth occupancy
    - **Shipping Lines**: Container tracking, vessel progress
    - **Trucking Companies**: Container availability, pickup authorisation
    - **Customs**: Container movements, inspection coordination
    """)
    
    st.markdown('<p class="subsection-header">CITOS Advanced Features</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **AI and Machine Learning:**
        - **Predictive berth planning**: Forecast vessel arrival delays
        - **Yard location optimisation**: Learn from historical patterns
        - **Equipment scheduling**: ML-optimised crane and AGV deployment
        - **Maintenance prediction**: IoT data predicts equipment failures
        
        **Real-Time Optimisation:**
        - **Dynamic re-planning**: Adjust plans as situations change
        - **What-if scenarios**: Simulate impact of changes before implementing
        - **Constraint satisfaction**: Balance multiple competing objectives
        - **Emergency response**: Rapid replanning during disruptions
        """)
    
    with col2:
        st.markdown("""
        **Operational Simulation Integration:**
        - **Virtual terminal model**: Real-time operational replica
        - **Simulation capability**: Test changes before implementation
        - **Training environment**: Train operators without disrupting operations
        - **Optimisation testing**: Evaluate improvement scenarios
        
        **Mobile and Cloud:**
        - **Mobile apps**: Supervisors monitor operations on tablets
        - **Cloud deployment**: Scalable infrastructure
        - **APIs**: Integration with customer systems
        - **Analytics platform**: Big data processing for insights
        """)
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 CITOS Competitive Advantage:</strong><br><br>
    CITOS gives PSA several strategic advantages:<br><br>
    1. <strong>Operational Excellence</strong>: Optimised operations → higher productivity, lower costs<br>
    2. <strong>Rapid Innovation</strong>: PSA controls development → can implement new features quickly<br>
    3. <strong>Vendor Independence</strong>: Not dependent on external TOS vendors<br>
    4. <strong>Global Deployment</strong>: Standard platform across PSA terminals worldwide<br>
    5. <strong>Data Advantage</strong>: Decades of operational data improve AI algorithms<br>
    6. <strong>Customer Integration</strong>: Deep APIs allow shipping lines to integrate directly<br><br>
    World-class terminals like Singapore consistently achieve:<br>
    - <strong>BOA >90%</strong> (berth on arrival)<br>
    - <strong>35+ GMPH</strong> (gross moves per hour per crane)<br>
    - <strong><3 minute</strong> average gate transaction time<br>
    - <strong><24 hour</strong> mega vessel turnaround<br><br>
    CITOS is a critical enabler of this performance.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 8: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Quay-Side Equipment:**
        - Ship-to-Shore (STS) cranes: $10-18M each
        - 60-80m outreach for mega vessels
        - Target: 35-40 GMPH productivity
        - Triple hoist technology for efficiency
        
        **Yard Equipment:**
        - RTG: Flexible, diesel, $2-3M
        - RMG: Electric, fixed, $3-5M
        - ARMG: Fully automated, $5-8M
        - Higher automation = higher stacking, productivity
        
        **Horizontal Transport:**
        - Prime Movers: Traditional, $100-150K
        - AGVs: Automated, $300-500K + infrastructure
        - AGVs: 70-80% labour reduction, 24/7 operations
        - Pooling strategy reduces fleet size 30-40%
        """)
    
    with col2:
        st.markdown("""
        **Gate Automation:**
        - OCR + GOS: 10x faster than manual
        - Truck Appointment System eliminates queues
        - <1 minute transaction time achievable
        
        **Automation Levels:**
        - Level 1: Conventional (baseline)
        - Level 2: Semi-automated (20-30% reduction)
        - Level 3: Highly automated (50-60% reduction)
        - Level 4: Fully automated (70-80% reduction)
        
        **PSA CITOS:**
        - Proprietary TOS developed in-house
        - 40+ years of continuous evolution
        - Deployed globally across PSA terminals
        - AI/ML, operational simulation, real-time optimisation
        - Competitive advantage for PSA
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Modern container terminals use sophisticated equipment ranging from 
    $10M+ quay cranes to $500K AGVs. Automation levels vary from conventional manual operations to fully 
    automated "lights-out" terminals that achieve 70-80% labour reduction and 24/7 consistent productivity. 
    PSA's CITOS terminal operating system coordinates all equipment and operations, using AI/ML and 
    real-time optimisation to achieve world-class performance (>90% BOA, 35+ GMPH, <24h vessel turnaround). 
    The choice to automate involves major capital investment ($500M-1B+) but delivers long-term operational 
    advantages, especially in high-labour-cost environments.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** 🌱 Green Maritime & Future Trends - Explore decarbonisation initiatives, alternative 
    fuels, green port technologies, and the future of sustainable maritime operations.
    """)
