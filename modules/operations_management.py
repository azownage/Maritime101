import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">🎯 Operations Management Fundamentals</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand the fundamental principles of operations management that drive port competitiveness, 
    including the "Big Six" competencies, quality management, capacity planning, and strategic trade-offs.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Introduction to Operations Management
    # ============================================================================
    
    st.markdown('<p class="section-header">What is Operations Management?</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Operations Management** is the administration of business practices to create the highest level 
    of efficiency possible within an organization. It involves converting materials and labor into goods 
    and services as efficiently as possible to maximize profit.
    
    In the context of **port operations**, operations management focuses on:
    - Moving containers from vessels to trucks/trains (and vice versa) efficiently
    - Optimizing resource utilization (berths, cranes, yard space, labor)
    - Meeting customer requirements (shipping lines, cargo owners)
    - Balancing cost, quality, speed, and reliability
    - Planning capacity for current and future demand
    
    **Core Question:** How do we design and operate port systems to be competitive and profitable?
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Primary Goal", "Efficiency", help="Maximum output with minimum input")
    with col2:
        st.metric("Key Constraint", "Resources", help="Berths, cranes, space, labor, time")
    with col3:
        st.metric("Success Metric", "Customer Satisfaction", help="Meeting shipping line requirements")
    
    # ============================================================================
    # SECTION 2: The "Big Six" Competencies
    # ============================================================================
    
    st.markdown('<p class="section-header">The "Big Six" Competitive Competencies</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Six key operational competencies determine whether a port (or any operation) attracts and retains 
    customers. These are the dimensions on which operations compete.
    """)
    
    st.markdown('<p class="subsection-header">1. Quality</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Definition:** Conformance to specifications and meeting customer expectations
    
    **In Port Operations:**
    - **Zero damage**: Containers handled without damage to cargo or equipment
    - **Accuracy**: Correct containers loaded/discharged, no mix-ups
    - **Completeness**: All documentation accurate and complete
    - **Compliance**: Meeting safety, security, environmental standards
    
    **Quality Dimensions:**
    - **Performance**: Does the service work as promised?
    - **Features**: What additional services are offered?
    - **Reliability**: How consistent is the service quality?
    - **Conformance**: Does it meet regulatory/contractual specifications?
    - **Durability**: Long-term service consistency
    - **Serviceability**: How easy to fix problems when they occur?
    - **Aesthetics**: Professional appearance and presentation
    - **Perceived Quality**: Reputation and brand image
    
    **Port Example:**
    - Shipping line expects: Container loaded in correct position on vessel, undamaged, documentation 
      accurate, within agreed timeframe
    - Quality failure: Wrong container loaded, container damaged, paperwork errors, delays
    """)
    
    st.markdown('<p class="subsection-header">2. Reliability</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Definition:** Dependability in delivery promises and operational consistency
    
    **In Port Operations:**
    - **Berth on Arrival (BOA)**: Vessel berths immediately on arrival (target >90%)
    - **Schedule adherence**: Vessel departs on promised time
    - **Predictability**: Consistent turnaround times regardless of conditions
    - **Uptime**: Equipment available when needed (minimal breakdowns)
    
    **Why Reliability Matters:**
    - Shipping lines operate tight schedules with connections
    - Delays cascade through the entire network
    - Unreliable ports disrupt just-in-time supply chains
    - Predictability allows better planning
    
    **Singapore's Performance:**
    - BOA >90% consistently maintained
    - Vessel turnaround times highly predictable
    - Minimal weather-related disruptions
    - 24/7 operations year-round
    """)
    
    st.markdown('<p class="subsection-header">3. Responsiveness (Speed)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Definition:** Ability to respond quickly to customer requests and demands
    
    **In Port Operations:**
    - **Vessel turnaround time**: Hours from arrival to departure
    - **Gate processing time**: Minutes for trucks to enter/exit
    - **Flexibility**: Ability to accommodate last-minute changes
    - **Quick response**: Fast answers to queries and issues
    
    **Speed Metrics:**
    - **Gross crane moves per hour (GCMPH)**: Containers moved per crane per hour (target: 30+)
    - **Net crane moves per hour (NCMPH)**: Actual working time only (target: 35-40)
    - **Vessel port stay**: Total hours in port (target: <24 hours for mega vessels)
    - **Truck turnaround time**: Gate entry to gate exit (target: <45 minutes)
    
    **Economic Impact:**
    - Every hour saved = lower costs for shipping line
    - Faster turnaround = more voyages per vessel per year
    - Time is money in maritime operations
    """)
    
    st.markdown('<p class="subsection-header">4. Agility (Flexibility)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Definition:** Ability to adapt to changing customer needs and market conditions
    
    **In Port Operations:**
    - **Volume flexibility**: Handle demand fluctuations (seasonal peaks, alliance changes)
    - **Mix flexibility**: Accommodate different container types (standard, reefer, OOG, dangerous goods)
    - **Schedule flexibility**: Adjust berth windows, swap vessel priorities
    - **Service flexibility**: Customize services for different shipping lines
    
    **Examples:**
    - Sudden weather event → Reallocate berths and reschedule vessels
    - Alliance restructuring → Accommodate new vessel sizes and schedules
    - Unexpected vessel arrival → Find berth space without disrupting others
    - Special cargo request → Provide dedicated handling and storage
    
    **Enablers of Agility:**
    - Excess capacity (spare berths, cranes, yard space)
    - Cross-trained workforce
    - Flexible IT systems
    - Modular infrastructure design
    """)
    
    st.markdown('<p class="subsection-header">5. Service</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Definition:** Support activities that enhance the core product/service offering
    
    **In Port Operations:**
    - **Customer support**: Dedicated account management for major shipping lines
    - **Information services**: Real-time tracking, vessel schedules, container status
    - **Problem resolution**: Quick handling of issues and complaints
    - **Value-added services**: Customs clearance assistance, cargo inspection facilities
    - **Communication**: Proactive updates on vessel status, delays, issues
    
    **Service Excellence:**
    - 24/7 customer service hotline
    - Dedicated terminal representatives for major customers
    - Real-time visibility through web portals and APIs
    - Proactive problem identification and resolution
    - Consultative approach to customer needs
    
    **Beyond Basic Operations:**
    - Empty container depot management
    - Container maintenance and repair
    - Cargo consolidation/deconsolidation
    - Inland transportation coordination
    - Bunkering and ship services coordination
    """)
    
    st.markdown('<p class="subsection-header">6. Cost</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Definition:** Delivering service at competitive prices while maintaining profitability
    
    **In Port Operations:**
    - **Container handling charges**: Price per TEU moved
    - **Storage fees**: Price per TEU per day for yard storage
    - **Service charges**: Reefer monitoring, special handling, etc.
    - **Total cost of service**: All-in cost to shipping line
    
    **Cost Structure:**
    - **Fixed costs**: Berths, cranes, IT systems, overhead (60-70% of total)
    - **Variable costs**: Labor, fuel, maintenance, utilities (30-40%)
    - **High fixed costs** → Economies of scale crucial
    
    **Cost Management Strategies:**
    - Maximize throughput to spread fixed costs
    - Automation to reduce variable labor costs
    - Energy efficiency to reduce utility costs
    - Preventive maintenance to avoid expensive breakdowns
    - Process optimization to improve productivity
    
    **Trade-off:**
    - Lowest price doesn't always win
    - Customers willing to pay premium for quality, reliability, speed
    - Value = Quality + Speed + Service - Cost
    """)
    
    # Big Six visualization
    big_six_data = pd.DataFrame({
        'Competency': ['Quality', 'Reliability', 'Responsiveness', 'Agility', 'Service', 'Cost'],
        'Importance': [95, 98, 90, 85, 88, 80],
        'Singapore Score': [95, 98, 92, 88, 90, 75],
        'Description': [
            'Zero damage, accuracy, compliance',
            'BOA >90%, predictable schedules',
            'Fast turnaround, high crane productivity',
            'Handle demand fluctuations, service mix',
            'Customer support, information, problem solving',
            'Competitive pricing with value delivery'
        ]
    })
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=big_six_data['Singapore Score'],
        theta=big_six_data['Competency'],
        fill='toself',
        name='Singapore Performance',
        line=dict(color='#3B82F6', width=3),
        fillcolor='rgba(59, 130, 246, 0.3)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100])
        ),
        showlegend=False,
        title={
            'text': 'The "Big Six" Operational Competencies',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#1F2937'}
        },
        height=500
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    <div class="insight-box">
    <strong>🎯 Key Insight:</strong> The Big Six are not independent—they interact and sometimes conflict:<br>
    - <strong>Quality vs Speed</strong>: Taking time to ensure accuracy vs fast operations<br>
    - <strong>Cost vs Service</strong>: Lower prices vs premium service offerings<br>
    - <strong>Agility vs Efficiency</strong>: Spare capacity for flexibility vs maximizing utilization<br>
    - <strong>Reliability vs Responsiveness</strong>: Predictable schedules vs accommodating urgent requests<br><br>
    World-class operations balance all six competencies rather than maximizing just one.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 3: Quality Management
    # ============================================================================
    
    st.markdown('<p class="section-header">Quality Management in Port Operations</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Quality management ensures that operations consistently meet specifications and customer expectations. 
    In port operations, quality failures can be costly—damaged cargo, wrong containers loaded, documentation 
    errors, safety incidents.
    """)
    
    st.markdown('<p class="subsection-header">Failure Mode and Effects Analysis (FMEA)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **FMEA** is a systematic method for identifying potential failure modes and their impacts before they 
    occur. It's widely used in port operations planning.
    
    **FMEA Process:**
    
    **Step 1: Identify Potential Failures**
    - What could go wrong? (e.g., crane breakdown, wrong container loaded, documentation error)
    
    **Step 2: Assess Severity**
    - How bad is the impact? (Scale 1-10, where 10 = catastrophic)
    - Minor inconvenience = 2-3
    - Major delay = 6-7
    - Safety incident = 9-10
    
    **Step 3: Assess Occurrence**
    - How likely is it to happen? (Scale 1-10, where 10 = very frequent)
    - Rare = 1-2
    - Occasional = 4-5
    - Frequent = 8-10
    
    **Step 4: Assess Detection**
    - Can we detect it before it causes problems? (Scale 1-10, where 10 = very hard to detect)
    - Easy to detect = 1-2
    - Moderate difficulty = 4-5
    - Very difficult = 8-10
    
    **Step 5: Calculate Risk Priority Number (RPN)**
    - RPN = Severity × Occurrence × Detection
    - Higher RPN = higher priority to address
    - Focus mitigation efforts on high RPN items
    """)
    
    # FMEA example
    fmea_example = pd.DataFrame({
        'Failure Mode': [
            'Crane breakdown during operations',
            'Wrong container loaded on vessel',
            'Container damaged during handling',
            'Reefer power failure in yard',
            'Documentation error (wrong destination)',
            'Yard equipment collision'
        ],
        'Severity (1-10)': [7, 9, 8, 9, 7, 10],
        'Occurrence (1-10)': [3, 2, 3, 2, 4, 2],
        'Detection (1-10)': [2, 6, 3, 4, 5, 3],
        'RPN': [42, 108, 72, 72, 140, 60],
        'Mitigation Strategy': [
            'Preventive maintenance, backup cranes',
            'Double-check systems, RFID tracking',
            'Operator training, equipment sensors',
            'Redundant power, monitoring systems',
            'Automated systems, verification checks',
            'Collision avoidance systems, training'
        ]
    })
    
    # Sort by RPN
    fmea_example = fmea_example.sort_values('RPN', ascending=False)
    
    st.dataframe(fmea_example, width='stretch', hide_index=True)
    
    # RPN visualization
    fig = go.Figure(data=[
        go.Bar(
            x=fmea_example['RPN'],
            y=fmea_example['Failure Mode'],
            orientation='h',
            marker=dict(
                color=fmea_example['RPN'],
                colorscale='Reds',
                line=dict(color='#1F2937', width=1)
            ),
            text=fmea_example['RPN'],
            textposition='outside'
        )
    ])
    
    fig.update_layout(
        title={
            'text': 'Risk Priority Numbers (RPN) - Focus on Highest First',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        xaxis_title="Risk Priority Number (Higher = More Urgent)",
        height=400,
        plot_bgcolor='white',
        xaxis=dict(gridcolor='#E5E7EB')
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 FMEA Benefits:</strong><br>
    - <strong>Proactive</strong>: Identify risks before they occur<br>
    - <strong>Systematic</strong>: Structured approach to risk assessment<br>
    - <strong>Prioritized</strong>: Focus resources on highest-risk items<br>
    - <strong>Actionable</strong>: Clear mitigation strategies<br>
    - <strong>Continuous</strong>: Regular review and update as operations evolve<br><br>
    Modern terminals use FMEA in planning new equipment, procedures, and technologies.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">Other Quality Management Tools</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Six Sigma:**
        - Statistical approach to quality
        - Target: 3.4 defects per million opportunities
        - DMAIC process: Define, Measure, Analyze, Improve, Control
        - Used for process improvement projects
        
        **Total Quality Management (TQM):**
        - Organization-wide commitment to quality
        - Continuous improvement culture
        - Customer focus
        - Employee involvement at all levels
        
        **ISO Standards:**
        - ISO 9001: Quality management systems
        - ISO 14001: Environmental management
        - ISO 45001: Occupational health and safety
        - ISPS Code: Port security standards
        """)
    
    with col2:
        st.markdown("""
        **Statistical Process Control (SPC):**
        - Monitor processes for abnormal variation
        - Control charts to detect trends
        - Distinguish normal vs special cause variation
        - Take corrective action when needed
        
        **Root Cause Analysis (RCA):**
        - "5 Whys" technique
        - Fishbone (Ishikawa) diagrams
        - Identify underlying causes, not symptoms
        - Prevent recurrence
        
        **Key Performance Indicators (KPIs):**
        - Crane moves per hour
        - Vessel turnaround time
        - Gate transaction time
        - Error rates (misloads, damage)
        - Track trends, benchmark, improve
        """)
    
    # ============================================================================
    # SECTION 4: Capacity Management
    # ============================================================================
    
    st.markdown('<p class="section-header">Capacity Management</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Capacity** is the maximum output an operation can produce in a given time period. For ports, capacity 
    determines how much throughput can be handled.
    """)
    
    st.markdown('<p class="subsection-header">Three Types of Capacity</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Design Capacity**
        
        **Definition:**
        - Maximum theoretical output
        - Ideal conditions
        - 100% utilization
        - No downtime
        
        **Example:**
        - 10 berths × 3M TEU/berth
        - = 30M TEU design capacity
        
        **Reality:**
        - Never achieved in practice
        - Useful for planning only
        """)
    
    with col2:
        st.markdown("""
        **Effective Capacity**
        
        **Definition:**
        - Realistic maximum output
        - Accounts for scheduled downtime
        - Maintenance windows
        - Normal inefficiencies
        
        **Example:**
        - 30M TEU design capacity
        - × 85% efficiency factor
        - = 25.5M TEU effective capacity
        
        **Reality:**
        - Best achievable under normal conditions
        - Used for operational planning
        """)
    
    with col3:
        st.markdown("""
        **Actual Output**
        
        **Definition:**
        - Real production achieved
        - Includes all disruptions
        - Unplanned downtime
        - Demand fluctuations
        
        **Example:**
        - 25.5M TEU effective capacity
        - 23M TEU actual throughput
        - = 90% capacity utilization
        
        **Reality:**
        - What actually happens
        - Used for performance measurement
        """)
    
    # Capacity metrics
    st.markdown("""
    **Key Capacity Metrics:**
    
    **Utilization Rate = (Actual Output / Design Capacity) × 100%**
    - Example: 23M / 30M = 77% utilization
    
    **Efficiency Rate = (Actual Output / Effective Capacity) × 100%**
    - Example: 23M / 25.5M = 90% efficiency
    
    **Optimal Utilization:** Typically 80-90% of effective capacity
    - Too low (< 70%): Underutilized assets, higher unit costs
    - Too high (> 95%): No flexibility, quality issues, delays
    """)
    
    # Capacity visualization
    capacity_data = pd.DataFrame({
        'Capacity Type': ['Design Capacity', 'Effective Capacity', 'Actual Output'],
        'TEU (Millions)': [30, 25.5, 23],
        'Percentage': [100, 85, 77]
    })
    
    fig = go.Figure()
    
    fig.add_trace(go.Funnel(
        y=capacity_data['Capacity Type'],
        x=capacity_data['TEU (Millions)'],
        textposition="inside",
        textinfo="value+percent initial",
        marker=dict(color=['#3B82F6', '#10B981', '#F59E0B']),
        connector={"line": {"color": "#64748B", "width": 3}}
    ))
    
    fig.update_layout(
        title={
            'text': 'Port Capacity: Design → Effective → Actual',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        height=400
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown('<p class="subsection-header">Capacity Planning Horizons</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Capacity decisions operate on different time horizons with different decision-making approaches:
    """)
    
    capacity_horizons = pd.DataFrame({
        'Time Horizon': ['Long-term (5-10 years)', 'Medium-term (6-18 months)', 'Short-term (Daily-Weekly)'],
        'Decisions': [
            'New berths, terminals, major equipment investments',
            'Equipment purchases, workforce planning, maintenance schedules',
            'Berth allocation, crane assignment, shift scheduling'
        ],
        'Capacity Changes': [
            'Add/remove major capacity (berths, cranes, terminals)',
            'Add/remove minor capacity (equipment, staffing levels)',
            'Optimize existing capacity (better scheduling, utilization)'
        ],
        'Flexibility': ['Low - Hard to reverse', 'Medium - Moderately reversible', 'High - Easily adjusted'],
        'Investment': ['Very high ($billions)', 'Moderate ($millions)', 'Low (operating costs)'],
        'Examples': [
            'Tuas Mega Port development (S$20B+, 20+ years)',
            'Purchase 3 new quay cranes ($15M each)',
            'Add overtime shift for peak season'
        ]
    })
    
    st.dataframe(capacity_horizons, width='stretch', hide_index=True)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ The Capacity-Demand Challenge:</strong><br>
    - <strong>Lead time problem</strong>: New berths take 5-7 years to build, but demand forecasts are uncertain<br>
    - <strong>Lumpiness</strong>: Capacity comes in large chunks (can't build half a berth)<br>
    - <strong>Irreversibility</strong>: Once built, very expensive to remove<br>
    - <strong>Uncertainty</strong>: Trade patterns, alliances, technology all change<br><br>
    <strong>Singapore's Approach:</strong><br>
    - Plan long-term (Tuas announced 2012 for 2040)<br>
    - Build in phases (flexibility to adjust pace)<br>
    - Maintain excess capacity as buffer (agility)<br>
    - Invest in efficiency gains (more output from same capacity)
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 5: Demand Management Strategies
    # ============================================================================
    
    st.markdown('<p class="section-header">Demand Management Strategies</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Rather than just adding capacity to meet demand, operations can also manage demand patterns to better 
    match existing capacity.
    """)
    
    st.markdown('<p class="subsection-header">Four Demand Management Strategies</p>', unsafe_allow_html=True)
    
    demand_strategies = pd.DataFrame({
        'Strategy': ['Level Strategy', 'Chase Strategy', 'Mixed Strategy', 'Demand Management (Pricing)'],
        'Description': [
            'Maintain constant output regardless of demand fluctuations',
            'Adjust capacity to match demand changes (hire/fire, overtime)',
            'Combination of level and chase strategies',
            'Use pricing to shift demand from peak to off-peak periods'
        ],
        'Advantages': [
            'Stable workforce, predictable operations, lower training costs',
            'Minimum inventory, high capacity utilization, matches demand',
            'Balances costs and flexibility, pragmatic approach',
            'Smooths demand, improves utilization, maximizes revenue'
        ],
        'Disadvantages': [
            'Excess capacity in low periods, inventory costs, inflexibility',
            'Workforce instability, higher hiring/training costs, quality issues',
            'Complexity in execution, requires careful balance',
            'May lose price-sensitive customers, complex pricing models'
        ],
        'Port Application': [
            'Maintain fixed berth/crane/labor capacity year-round',
            'Hire temporary workers for peak season, overtime shifts',
            'Core permanent staff + temporary workers for peaks',
            'Peak pricing during busy periods, discounts for off-peak'
        ]
    })
    
    st.dataframe(demand_strategies, width='stretch', hide_index=True)
    
    st.markdown("""
    **Port Industry Reality:**
    
    Most ports use a **Mixed Strategy with Demand Management**:
    - Maintain core capacity (berths, cranes) as **level capacity**
    - Adjust labor through overtime and temporary workers (**chase**)
    - Use pricing incentives to smooth demand (**demand management**)
    
    **Example:**
    - Base capacity handles 80% of demand
    - Peak periods: Add overtime shifts, temporary workers, premium pricing
    - Off-peak: Run standard schedule, offer discounts to attract cargo
    """)
    
    # ============================================================================
    # SECTION 6: Maintenance Management
    # ============================================================================
    
    st.markdown('<p class="section-header">Maintenance Management</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Maintaining equipment availability is critical for port capacity and reliability. Different maintenance 
    approaches have different cost-benefit profiles.
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Reactive (Breakdown) Maintenance**
        
        **Approach:**
        - Fix it when it breaks
        - No scheduled maintenance
        - Run to failure
        
        **Advantages:**
        - No maintenance costs until breakdown
        - Maximum equipment utilization
        - Simple to manage
        
        **Disadvantages:**
        - Unpredictable downtime
        - Emergency repairs expensive
        - Cascading failures
        - Disrupts operations
        
        **Use Case:**
        - Non-critical equipment only
        - Low-cost items
        """)
    
    with col2:
        st.markdown("""
        **Preventive Maintenance**
        
        **Approach:**
        - Scheduled maintenance
        - Regular inspections
        - Replace parts on schedule
        
        **Advantages:**
        - Predictable maintenance windows
        - Reduced breakdown risk
        - Longer equipment life
        - Better planning
        
        **Disadvantages:**
        - Costs even when no problem
        - May replace functioning parts
        - Takes capacity offline
        
        **Use Case:**
        - Critical equipment (cranes)
        - Predictable wear patterns
        - High failure cost
        """)
    
    with col3:
        st.markdown("""
        **Predictive Maintenance**
        
        **Approach:**
        - Condition monitoring
        - Sensors and data analysis
        - Maintain when needed
        
        **Advantages:**
        - Optimal timing
        - Minimum unnecessary maintenance
        - Prevent failures before they happen
        - Data-driven decisions
        
        **Disadvantages:**
        - Requires sensors and IT systems
        - Upfront investment
        - Technical expertise needed
        
        **Use Case:**
        - Modern automated terminals
        - High-value equipment
        - IoT-enabled systems
        """)
    
    st.markdown("""
    **Modern Port Approach:**
    
    Combine all three maintenance strategies:
    - **Predictive** for critical, expensive equipment (quay cranes, AGVs)
    - **Preventive** for important equipment without sensors (yard cranes, trucks)
    - **Reactive** for low-cost, non-critical items (hand tools, minor components)
    
    **Tuas Mega Port:**
    - IoT sensors on all major equipment
    - Real-time condition monitoring
    - AI predicts maintenance needs
    - Scheduled during low-demand windows
    """)
    
    # ============================================================================
    # SECTION 7: Strategic Trade-offs
    # ============================================================================
    
    st.markdown('<p class="section-header">Strategic Trade-offs in Operations</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Operations management is fundamentally about making trade-offs. You cannot maximize all objectives 
    simultaneously—choices must be made.
    """)
    
    st.markdown('<p class="subsection-header">Common Trade-offs</p>', unsafe_allow_html=True)
    
    tradeoffs = pd.DataFrame({
        'Trade-off': [
            'Cost vs Quality',
            'Cost vs Flexibility',
            'Speed vs Quality',
            'Capacity vs Utilization',
            'Standardization vs Customization',
            'Automation vs Employment'
        ],
        'Description': [
            'Lower costs often mean lower quality materials/processes vs premium quality costs more',
            'Excess capacity for flexibility is expensive vs maximize utilization reduces flexibility',
            'Rushing operations increases error risk vs careful work takes longer',
            'Build excess capacity for peaks (expensive) vs run at high utilization (inflexible)',
            'Standard processes are efficient but inflexible vs custom services are expensive',
            'Automation reduces labor costs but eliminates jobs vs labor-intensive preserves jobs'
        ],
        'Port Example': [
            'Cheap cranes break down more vs expensive cranes more reliable',
            'Extra berths costly but handle peaks vs no spare capacity means delays in peaks',
            'Fast turnaround risks mistakes vs thorough checks slow operations',
            "Tuas 65M TEU capacity but currently 37M throughput vs build only what's needed now",
            'All vessels follow same process (efficient) vs customized handling for special cargo',
            'AGVs replace human drivers (cost-efficient) vs human workforce (employment)'
        ],
        'How Ports Decide': [
            'Premium pricing justifies quality investment',
            'Maintain ~10-15% excess capacity as buffer',
            'Balance with automation and checks',
            'Long-term planning, build in phases',
            'Standard core + premium options',
            'Gradual transition, retrain workers'
        ]
    })
    
    st.dataframe(tradeoffs, width='stretch', hide_index=True)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🎯 The Art of Operations Management:</strong><br><br>
    There is no "perfect" operation. Every decision involves trade-offs:<br>
    - More capacity → Higher costs but better service<br>
    - More automation → Lower costs but higher unemployment<br>
    - More quality checks → Fewer errors but slower operations<br>
    - More flexibility → Higher costs but better customer satisfaction<br><br>
    <strong>World-class operations:</strong><br>
    - Understand the trade-offs explicitly<br>
    - Make conscious strategic choices<br>
    - Align trade-offs with competitive strategy<br>
    - Continuously improve to expand the frontier (achieve more of multiple objectives)<br><br>
    <strong>Singapore's Approach:</strong><br>
    - Premium positioning allows higher costs for quality/reliability/service<br>
    - Strategic excess capacity for flexibility<br>
    - Automation with workforce retraining programs<br>
    - Continuous improvement to push performance boundaries
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 8: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **The "Big Six" Competencies:**
        - Quality: Conformance to specifications
        - Reliability: Dependability and consistency
        - Responsiveness: Speed of operations
        - Agility: Flexibility to adapt
        - Service: Support and problem-solving
        - Cost: Competitive pricing with value
        
        **Quality Management:**
        - FMEA for proactive risk management
        - Six Sigma, TQM, ISO standards
        - Statistical process control
        - Root cause analysis
        - Continuous improvement culture
        
        **Capacity Types:**
        - Design capacity (theoretical max)
        - Effective capacity (realistic max)
        - Actual output (real performance)
        - Optimal utilization: 80-90%
        """)
    
    with col2:
        st.markdown("""
        **Capacity Planning:**
        - Long-term: Major infrastructure (5-10 years)
        - Medium-term: Equipment and staffing (6-18 months)
        - Short-term: Scheduling and optimization (daily)
        - Build in phases for flexibility
        
        **Demand Management:**
        - Level: Constant capacity
        - Chase: Match demand variations
        - Mixed: Combination approach
        - Pricing: Shift demand patterns
        
        **Maintenance:**
        - Reactive: Fix when broken
        - Preventive: Scheduled maintenance
        - Predictive: Condition-based monitoring
        - Combine strategies by equipment type
        
        **Strategic Trade-offs:**
        - Cost vs Quality/Flexibility/Service
        - Conscious choices aligned with strategy
        - Continuous improvement expands frontier
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Operations management is about optimizing the Big Six competencies 
    (Quality, Reliability, Responsiveness, Agility, Service, Cost) while managing capacity and demand 
    effectively. Success requires understanding trade-offs, making strategic choices, implementing quality 
    management systems (like FMEA), and planning capacity across multiple time horizons. World-class ports 
    like Singapore balance all these factors through premium positioning, strategic infrastructure investment, 
    automation, and continuous improvement.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** 🏗️ Terminal Operations & Planning - Dive deep into the operational workflows of container 
    terminals, from berth planning to vessel stowage to equipment scheduling.
    """)
