import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">🎯 Operations Management Fundamentals</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Master the fundamental principles of operations management that drive port competitiveness and operational 
    excellence, understand the "Big Six" competencies (Quality, Reliability, Responsiveness, Agility, Service, 
    Cost/Price) that determine whether ports attract and retain customers, learn systematic quality management 
    methodologies like FMEA (Failure Mode and Effects Analysis) used to proactively identify and mitigate risks, 
    comprehend capacity planning concepts (design vs effective vs actual capacity with optimal 80-90% utilization), 
    analyse strategic trade-offs between competing objectives (cost vs quality, speed vs accuracy, efficiency vs 
    flexibility), and understand maintenance strategies (reactive, preventive, predictive) essential for operational 
    reliability in capital-intensive port operations.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Introduction to Operations Management
    # ============================================================================
    
    st.markdown('<p class="section-header">What is Operations Management?</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Operations Management** is the administration of business practices designed to create the highest level of 
    efficiency possible within an organization. It involves **converting inputs (materials, labor, capital) into 
    outputs (goods and services)** as efficiently as possible to maximize organizational objectives—typically profit 
    in commercial operations, or service quality in public sector operations.
    
    **In the Context of Container Port Operations:**
    
    Operations management focuses on the **transformation process** of moving containers through the terminal:
    
    **Inputs:**
    - **Physical infrastructure**: Berths, quay cranes, yard cranes, AGVs, storage yard, gates
    - **Labor**: Crane operators, planners, supervisors, maintenance technicians, administrative staff
    - **Technology**: CITOS (Terminal Operating System), communication systems, equipment automation
    - **Information**: Vessel schedules, cargo manifests, stowage plans, customs documentation
    
    **Transformation Process:**
    - Discharge containers from vessel (quay crane operations)
    - Transport containers to storage yard (horizontal transport)
    - Stack containers in yard (yard crane operations)
    - Retrieve containers for loading or truck pickup
    - Load containers onto connecting vessels or external trucks/trains
    - Process documentation, customs clearances, gate transactions
    
    **Outputs:**
    - Containers moved from vessel → storage → truck/train (import flow)
    - Containers moved from truck/train → storage → vessel (export flow)
    - Containers moved from vessel → storage → connecting vessel (transshipment flow)
    - **Delivered service**: Fast turnaround, accurate handling, zero damage, complete documentation
    
    **The Core Operations Management Questions:**
    
    **Efficiency:**
    - How do we move the maximum number of containers with minimum resources?
    - What's the optimal combination of berths, cranes, yard equipment, labor?
    - How do we minimize costs while maintaining quality?
    
    **Effectiveness:**
    - Are we meeting customer requirements (shipping lines, cargo owners)?
    - Do vessels depart on schedule? Are containers undamaged? Is documentation accurate?
    - How do we balance multiple, sometimes conflicting, objectives?
    
    **Competitiveness:**
    - What operational competencies attract customers to our terminal vs competitors?
    - How do we deliver superior value (quality + speed + service) at competitive cost?
    - What strategic investments (automation, infrastructure, technology) enhance competitiveness?
    """)
    
    # Key metrics display
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Primary Goal", "Efficiency", help="Maximum output with minimum input resources")
    with col2:
        st.metric("Key Constraint", "Resources", help="Berths, cranes, space, labor, time are all limited")
    with col3:
        st.metric("Success Metric", "Customer Value", help="Quality + Speed + Service - Cost")
    with col4:
        st.metric("Challenge", "Trade-offs", help="Cannot maximize all objectives simultaneously")
    
    st.markdown("""
    <div class="insight-box">
    <strong>💡 Operations Management is Strategic, Not Just Tactical:</strong><br><br>
    Many people think operations management is about day-to-day execution—scheduling cranes, dispatching trucks, 
    managing queues. While these tactical activities are important, <strong>operations management is fundamentally 
    strategic</strong>:<br><br>
    • <strong>Capacity decisions</strong>: How many berths, cranes, AGVs to deploy? (US&#36;200-500M investments)<br>
    • <strong>Technology choices</strong>: Manual vs automated operations? (70-80% labor impact)<br>
    • <strong>Service positioning</strong>: Premium reliability vs low-cost efficiency? (competitive strategy)<br>
    • <strong>Capability development</strong>: What competencies to excel at? (resource allocation)<br><br>
    These strategic operations decisions determine <strong>long-term competitiveness and profitability</strong>—not 
    just operational efficiency.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 2: The "Big Six" Competitive Competencies
    # ============================================================================
    
    st.markdown('<p class="section-header">The "Big Six" Competitive Competencies</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The lecture materials identify **"The BIG SIX competencies that attract customers"** as the fundamental dimensions 
    on which operations compete. These six competencies determine whether customers (shipping lines, cargo owners) 
    choose your terminal over competitors.
    
    **The lecture materials emphasize**: These competencies **"are the main objectives of managing operations"**—
    meaning operations managers must consciously decide how to balance performance across all six dimensions.
    """)
    
    st.markdown('<p class="subsection-header">1. Quality - "High quality attracts customers; improving quality retains them!"</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Definition (from lecture materials):**
    
    *"If the service features satisfy or exceed the needs & desires of customers"*
    
    *"Attributes: performance, reliability, convenience, special services, consistency, security & safety—i.e., 
    value for money"*
    
    The lecture materials emphasize in red text: **"High quality attracts customers; improving quality retains them!"**
    
    This encapsulates quality's dual role: Initial quality attracts new customers (reputation, word-of-mouth, trial), 
    while consistent quality retains existing customers (satisfaction, loyalty, repeat business).
    
    **Quality in Port Operations - What Does It Mean?**
    
    **Performance:**
    - Does the terminal deliver the basic service promised?
    - Containers loaded/discharged correctly, on time, undamaged
    - Vessel departs on schedule
    
    **Reliability (Quality Dimension):**
    - Consistency—does quality remain high over time?
    - No variation in service level regardless of conditions (weather, volume fluctuations, shift changes)
    - Shipping lines can depend on consistent performance
    
    **Convenience:**
    - Easy booking process, simple documentation, straightforward procedures
    - Flexible appointment systems, 24/7 operations, accessible customer service
    - Minimal bureaucracy and red tape
    
    **Special Services:**
    - Reefer monitoring (temperature-controlled containers)
    - Dangerous goods handling expertise
    - Oversized cargo capabilities
    - Customs pre-clearance, bonded warehousing
    
    **Consistency:**
    - Same high-quality service across all shifts, all seasons, all vessel types
    - No "good days" vs "bad days"—predictably excellent
    
    **Security & Safety:**
    - Zero security breaches (theft, smuggling, unauthorized access)
    - Zero safety incidents (injuries, equipment damage, environmental spills)
    - Compliance with ISPS Code (International Ship and Port Facility Security)
    
    **Quality Dimensions Framework (Garvin's Eight Dimensions):**
    
    1. **Performance**: Core service delivered as promised
    2. **Features**: Additional services beyond basic offering
    3. **Reliability**: Consistency over time
    4. **Conformance**: Meeting specifications and standards
    5. **Durability**: Long-term service consistency
    6. **Serviceability**: Problem resolution when issues occur
    7. **Aesthetics**: Professional appearance, clean facilities
    8. **Perceived Quality**: Reputation and brand image
    
    **Port Quality Examples:**
    
    **High Quality:**
    - Container loaded in correct position on vessel (per stowage plan)
    - Zero damage to container or cargo
    - All documentation accurate (bill of lading, customs forms, delivery orders)
    - Vessel departs exactly on scheduled time
    - Cargo owner receives real-time tracking information
    
    **Quality Failures:**
    - Wrong container loaded (must be removed at sea or next port—expensive!)
    - Container damaged during handling (insurance claim, cargo compensation)
    - Documentation errors (customs delays, demurrage charges)
    - Vessel departure delayed (missed connection, schedule disruption)
    - Lost containers (cannot locate in yard—embarrassing and costly)
    
    **The Cost of Poor Quality:**
    
    **Direct Costs:**
    - Damage compensation (US&#36;10-50K per container depending on cargo)
    - Re-work costs (must discharge and reload wrong containers)
    - Demurrage penalties (shipping line charges for delays)
    
    **Indirect Costs:**
    - Reputation damage (shipping lines avoid terminals with quality issues)
    - Lost business (customers switch to competitors)
    - Higher insurance premiums (poor safety/security record)
    - Employee morale (working at low-quality operation is demoralizing)
    
    **Singapore's Quality Commitment:**
    - **Zero-incident mindset**: Safety and security incidents treated as unacceptable
    - **Continuous improvement culture**: Kaizen, Six Sigma, TQM methodologies
    - **Quality certifications**: ISO 9001, ISO 14001, OHSAS 18001 across operations
    - **Investment in quality**: Automation reduces human error, advanced training programs
    """)
    
    st.markdown('<p class="subsection-header">2. Reliability - "Unreliable means losing customers"</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Definition (from lecture materials):**
    
    *"Keeping promises: no service failure, always on time, no damage to containers, no loss, and with the correct 
    documentation"*
    
    *"JIT & responsive supply chains require reliability"*
    
    The lecture materials emphasize in red text: **"Unreliable means losing customers"**
    
    This stark statement reflects reality: In modern supply chains where just-in-time delivery and tight schedules 
    are critical, **unreliable ports are simply unusable**. Shipping lines cannot risk schedule disruptions, so 
    unreliable terminals quickly lose business to more dependable competitors.
    
    **Reliability in Port Operations - The Dependability Imperative:**
    
    **Berth on Arrival (BOA) - The Critical Reliability Metric:**
    
    **Definition:**
    - **BOA**: Percentage of vessels that berth immediately upon arrival (no anchorage wait)
    - **Industry target**: >90% BOA
    - **World-class performance**: 95%+ BOA (Singapore consistently achieves this)
    
    **Why BOA Matters:**
    - Vessels operate on tight schedules with multiple port calls
    - **Anchorage delays cascade**: If vessel late to Singapore, it's late to every subsequent port
    - **Costly delays**: Vessel charter costs US&#36;20-50K per day—waiting at anchorage is pure waste
    - **Schedule reliability**: Shipping lines cannot maintain published schedules if ports unreliable
    
    **What Determines BOA:**
    - **Berth availability**: Sufficient berths to handle peak demand
    - **Accurate ETA prediction**: Know when vessels actually arriving (not just scheduled time)
    - **Efficient operations**: Fast vessel turnaround frees berths for next arrival
    - **Flexible planning**: Can adjust berth allocation when vessels early/late
    
    **Schedule Adherence:**
    
    **Promise Made → Promise Kept:**
    - If terminal promises 24-hour turnaround, vessel must depart within 24 hours
    - **Consistency matters more than speed**: Reliable 30-hour turnaround better than unpredictable 20-30 hours
    - Shipping lines build schedules based on terminal commitments—deviations disrupt entire network
    
    **Predictability:**
    
    **Eliminating Variability:**
    - **Goal**: Same turnaround time for same vessel type regardless of when it arrives
    - **Example**: 18,000 TEU vessel should take 28-32 hours whether it arrives Monday morning or Friday night
    - **Challenges**: Weather, equipment failures, labor issues, peak periods—must manage these without impacting service
    
    **Equipment Uptime:**
    
    **Reliability Requires Working Equipment:**
    - **Target**: >98% equipment availability (cranes, AGVs, ARMGs)
    - **Preventive maintenance**: Scheduled maintenance during low-demand periods
    - **Redundancy**: Spare equipment, backup systems to handle failures
    - **Predictive maintenance**: IoT sensors, AI to predict failures before they occur
    
    **Why Reliability is Strategic:**
    
    **JIT Supply Chains Demand Reliability:**
    - Modern supply chains operate with minimal inventory (just-in-time manufacturing)
    - **Container delay = production line stoppage**: Automotive factory stops if parts container delayed
    - **Penalties**: Cargo owners penalize shipping lines for delays → shipping lines penalize unreliable ports
    
    **Alliance Commitments:**
    - Shipping alliances publish schedules 6-12 months ahead
    - **Inflexible**: Cannot easily change port calls once published
    - **Alliances choose reliable ports**: Won't risk schedule integrity on unreliable terminals
    
    **Network Effects:**
    - One unreliable port disrupts entire route
    - **Example**: Singapore-Rotterdam route with 8 port calls—if one port unreliable, entire service unreliable
    - **Reputation spreads**: Word travels fast in shipping industry about unreliable terminals
    
    **Singapore's Reliability Advantage:**
    
    **Consistent Excellence:**
    - **BOA >90%** maintained for decades (even during peak periods, bad weather)
    - **Minimal weather disruptions**: Tropical location with no typhoons, ice, fog
    - **24/7 operations**: No night shifts, weekends, holidays—always operational
    - **Political stability**: No strikes, labor disputes, government disruptions
    - **Infrastructure reliability**: Advanced maintenance, backup systems, redundancy
    """)
    
    st.markdown('<p class="subsection-header">3. Responsiveness - "The speed of response to customers\' demands"</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Definition (from lecture materials):**
    
    *"The speed of response to customers' demands"*
    
    *"Reducing time to gain a competitive advantage"*
    
    Responsiveness is about **speed**—how quickly the terminal can respond to customer needs, process vessels, 
    move containers, resolve issues, and adapt to changes.
    
    **Responsiveness in Port Operations:**
    
    **Vessel Turnaround Time:**
    
    **The Primary Speed Metric:**
    - **Time from arrival to departure**: How long does vessel spend in port?
    - **World-class benchmark**: <24 hours for 2,000-3,000 move mega vessels
    - **Container shipping is time-sensitive**: Every hour in port is hour not earning revenue at sea
    - **Cost impact**: Vessel charter US&#36;20-50K per day—faster turnaround = lower per-TEU cost
    
    **What Determines Turnaround Speed:**
    - **Crane productivity**: 35-40 GMPH (gross moves per hour) vs industry average 25-30 GMPH
    - **Crane intensity**: 8-10 cranes working simultaneously vs 4-6 cranes (resource allocation decision)
    - **Operational efficiency**: Minimal crane waiting time, optimized work sequences
    - **Documentation speed**: Paperless systems, automated customs clearance
    
    **Gate Transaction Time:**
    
    **Truck Processing Speed:**
    - **Traditional gates**: 5-10 minutes per truck (manual checks, paperwork)
    - **Automated gates**: <2 minutes per truck (OCR, automated validation)
    - **World-class target**: <1 minute average transaction time
    - **Impact**: Faster gate processing = less truck queuing = happier trucking companies = more business
    
    **Information Response Time:**
    
    **Customer Queries and Requests:**
    - **Container location**: Real-time tracking (answer instantly vs "I'll check and call you back")
    - **Booking confirmations**: Immediate vs 24-48 hour delay
    - **Special handling requests**: Can accommodate vs "not possible"
    - **Problem resolution**: Minutes to hours vs days
    
    **The Time-Based Competition Concept:**
    
    **Speed as Competitive Advantage:**
    - **Faster = More Capacity**: If vessel turnaround 20% faster, terminal can handle 20% more vessels with same berths
    - **Faster = Lower Costs**: Shipping lines save charter costs with faster turnaround
    - **Faster = Better Service**: Cargo reaches destination sooner—valuable for time-sensitive goods
    
    **Diminishing Returns:**
    - Going from 48-hour to 36-hour turnaround = valuable improvement
    - Going from 24-hour to 22-hour = marginal improvement (extra cost not justified by benefit)
    - **Optimization question**: What turnaround speed maximizes value?
    
    **Speed vs Quality Trade-off:**
    - **Rushing = Errors**: Very fast operations increase mistake risk
    - **Balance required**: Fast enough to be competitive but not so fast quality suffers
    - **Automation helps**: Automated systems fast AND accurate (no speed-quality tradeoff)
    
    **Singapore's Responsiveness:**
    
    **Fast Operations:**
    - **35-40 GMPH crane productivity** (world-leading)
    - **<24-hour turnaround** for mega vessels consistently
    - **<2-minute gate transactions** with automated systems
    
    **Quick Adaptation:**
    - Vessel arrives early? Can usually accommodate (berth flexibility)
    - Special cargo needs? Expertise and equipment to handle
    - Documentation issues? Experienced staff resolve quickly
    """)
    
    st.markdown('<p class="subsection-header">4. Agility - "Adapting quickly to changing demand, customer preferences & market conditions"</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Definition (from lecture materials):**
    
    *"Adapting quickly to changing demand, customer preferences & market conditions. Includes:"*
    
    - *"Volume: responding to changes in the amount demanded"*
    - *"Variety: providing the evolving range demanded"*
    - *"Innovation: developing new services and getting them to market ahead of the competition"*
    
    Agility is about **flexibility and adaptability**—the ability to respond to changes without major disruption. 
    In volatile maritime markets with seasonal demand, economic cycles, and evolving customer needs, **agile operations 
    survive and thrive while inflexible operations struggle**.
    
    **Agility in Port Operations:**
    
    **Volume Flexibility - Handling Demand Fluctuations:**
    
    **The Demand Volatility Challenge:**
    - Container volumes fluctuate **±20-30% seasonally** (pre-Christmas peak, post-Chinese New Year slack)
    - **Economic cycles**: Recessions reduce volumes 10-20%, recoveries increase volumes rapidly
    - **Route changes**: Alliances restructure networks, shifting volumes between ports overnight
    
    **How Agile Terminals Handle Volume Changes:**
    
    **Excess Capacity:**
    - Maintain **10-15% spare capacity** above average demand
    - **Costly**: Unused berths, cranes represent sunk capital
    - **Strategic value**: Can handle peak periods without delays (maintains reliability during peaks)
    
    **Flexible Labor:**
    - **Part-time/temporary workers**: Hire during peak seasons
    - **Overtime**: Extend shifts during high-volume periods
    - **Multi-skilling**: Train workers to perform multiple roles (deploy where needed)
    
    **Dynamic Resource Allocation:**
    - **CITOS optimization**: Reallocate cranes, AGVs, yard space dynamically based on actual demand
    - **Berth flexibility**: Continuous quay allows vessels to berth anywhere (not fixed berth assignments)
    
    **Variety Flexibility - Service Mix Adaptability:**
    
    **Diverse Customer Needs:**
    - **Standard dry containers**: 85-90% of volume (straightforward handling)
    - **Reefer containers**: 5-10% of volume (require power, temperature monitoring, expertise)
    - **Dangerous goods**: 2-5% of volume (require special handling, segregation, certifications)
    - **Oversized cargo (OOG)**: <1% of volume (require special equipment, planning)
    
    **Agile Terminals:**
    - **Equipment diversity**: Have specialized equipment for different container types
    - **Expertise**: Trained staff can handle all cargo types (not just standard containers)
    - **Flexible procedures**: Can accommodate special requests without disrupting standard operations
    
    **Example - Refrigerated Container Surge:**
    - Agricultural exports seasonal: Summer fruit exports from South America create reefer surge
    - **Inflexible terminal**: "Sorry, no reefer plugs available"—loses business
    - **Agile terminal**: Modular reefer racks, can quickly add capacity—captures business
    
    **Innovation - New Service Development:**
    
    **Staying Ahead of Competition:**
    - **Cold chain services**: Advanced reefer monitoring, quality assurance for pharmaceuticals, perishables
    - **E-commerce fulfillment**: Container unpacking, sorting, last-mile distribution integration
    - **Blockchain documentation**: Digital bills of lading, smart contracts, instant verification
    - **Predictive analytics**: AI-powered ETAs, berth planning, yard optimization
    
    **First-Mover Advantage:**
    - Terminal that develops new service first **captures initial business**
    - **Network effects**: As more customers use service, it becomes standard—late movers lose
    - **Example**: Singapore early adopter of LNG bunkering → now world's largest LNG bunker hub
    
    **Strategic Agility:**
    
    **Long-Term Adaptability:**
    - **Technology transitions**: LNG → Methanol → Ammonia bunkering (multi-fuel strategy maintains agility)
    - **Automation evolution**: Gradual automation deployment allows learning and adjustment
    - **Phased capacity expansion**: Tuas phases allow adjustment to actual demand vs 2012 projections
    
    **Why Agility Matters Strategically:**
    
    **Uncertainty is Constant:**
    - **Nobody can predict future accurately**: Trade wars, pandemics, technological disruptions
    - **Agile organizations adapt**: Inflexible organizations fail when reality differs from plans
    - **Resilience**: Agility = ability to absorb shocks and recover quickly
    
    **Agility Requires Investment:**
    - **Excess capacity**: Intentional under-utilization for flexibility (costly)
    - **Diverse capabilities**: Multiple equipment types, trained workforce, flexible systems
    - **Not free**: Agility costs more than hyper-efficient, specialized operations
    - **Strategic choice**: Premium-positioned terminals can afford agility investment
    """)
    
    st.markdown('<p class="subsection-header">5. Service - "Adds whatever else needed to keep customers satisfied"</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Definition (from lecture materials):**
    
    *"Service to customers: Adds whatever else needed to keep customers satisfied: attention, quick response to 
    queries, support & courtesy"*
    
    *"Potential for competitive advantage, especially for a transshipment hub"*
    
    Service is the "extras" beyond basic cargo handling—the **customer support, problem-solving, information sharing, 
    and professional interactions** that make customers prefer one terminal over another when basic operations 
    capabilities are similar.
    
    **Service in Port Operations:**
    
    **Information and Communication:**
    
    **Real-Time Visibility:**
    - **Container tracking**: Customers can see exact location of every container in real-time
    - **Vessel progress updates**: Automatic notifications when vessel arrives, berths, completes operations, departs
    - **Exception alerts**: Immediate notification of delays, issues, changes
    - **Accessible information**: Customer portals, mobile apps, API integrations
    
    **Proactive Communication:**
    - **Don't wait for customers to ask**: Anticipate information needs, provide updates automatically
    - **Example**: "Your container ready for pickup 2 hours ahead of schedule" (helps customer optimize trucking)
    - **Transparency**: Explain reasons for delays honestly rather than hiding problems
    
    **Customer Support:**
    
    **Responsive Account Management:**
    - **Dedicated account managers** for major shipping lines
    - **24/7 customer service**: Someone always available to answer questions, resolve issues
    - **Multi-channel support**: Phone, email, chat, portal—whatever customer prefers
    
    **Problem Resolution:**
    - **Empowered staff**: Customer-facing employees can make decisions, resolve issues without escalation
    - **Root cause analysis**: Don't just fix immediate problem—understand why it happened, prevent recurrence
    - **Service recovery**: When errors occur, over-deliver on resolution (turn problem into loyalty opportunity)
    
    **Professional Courtesy:**
    
    **The Human Element:**
    - **Respect**: Treat customers and their representatives professionally regardless of size/status
    - **Responsiveness**: Return calls/emails promptly (within hours, not days)
    - **Competence**: Staff knowledgeable, can answer questions accurately
    - **Reliability**: Follow through on commitments—if you say you'll do something, do it
    
    **Cultural Sensitivity:**
    - International business requires cultural awareness
    - Multilingual staff (English, Chinese, Malay, Japanese, Korean)
    - Understanding business etiquette across cultures
    
    **Value-Added Services:**
    
    **Beyond Basic Container Handling:**
    - **Customs facilitation**: Pre-clearance, bonded warehouses, customs consultancy
    - **Cargo inspection services**: Coordinate inspections, surveys, quality checks
    - **Container repair**: On-site repair facilities for damaged containers
    - **Transloading**: Transfer cargo between containers (e.g., consolidation/deconsolidation)
    - **Storage options**: Short-term, long-term, bonded, climate-controlled
    
    **Supply Chain Integration:**
    - **Coordination with trucking companies**: Truck appointment systems, real-time availability
    - **Rail connections**: Seamless rail intermodal services
    - **Air freight connections**: Fast transfer for time-sensitive cargo
    
    **The Service Differential:**
    
    **When Basic Operations are Commoditized:**
    - Most major terminals have similar **cranes, berths, technology**
    - Basic **productivity metrics** often similar (35-40 GMPH, 24-hour turnaround)
    - **Service becomes differentiator**: Excellence in customer support, information, problem-solving
    
    **Example Scenario:**
    
    **Terminal A (Basic Service):**
    - Container ready for pickup
    - Customer calls: "Is my container ready?" → "Let me check... yes, ready since yesterday"
    - Customer wastes day because didn't know container ready
    
    **Terminal B (Excellent Service):**
    - Container ready for pickup
    - System automatically emails customer: "Container X available, ready for pickup"
    - Customer optimizes logistics, picks up immediately, very satisfied
    
    **Same basic operation, vastly different service experience.**
    
    **Service and Premium Positioning:**
    
    **Singapore's Service Excellence:**
    - **World-class customer support**: Responsive, professional, knowledgeable
    - **Digital integration**: APIs allow shipping lines to integrate systems directly with PSA
    - **Continuous improvement**: Regular customer feedback, service quality monitoring
    - **Training investment**: Staff training programs ensure consistent service quality
    
    **Justifies Premium Pricing:**
    - Service excellence allows Singapore to charge **5-15% higher rates** than regional competitors
    - Customers willing to pay because **total value delivered** exceeds incremental cost
    - **Value = Quality + Speed + Service - Cost** (service is key component of value equation)
    """)
    
    st.markdown('<p class="subsection-header">6. Cost (and Price) - "Becoming more productive & efficient reduces costs"</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Definition (from lecture materials):**
    
    *"Cost (and price): Becoming more productive & efficient reduces costs & price"*
    
    *"Most costs are under the control of Operations Management"*
    
    The lecture materials emphasize that operations decisions directly determine costs, and **operations managers 
    control most cost drivers** (labor productivity, equipment utilization, process efficiency, maintenance costs).
    
    **Cost in Port Operations:**
    
    **Understanding Terminal Cost Structure:**
    
    **Fixed Costs (60-70% of total):**
    
    **Infrastructure:**
    - **Berths**: US&#36;200-300M per berth construction
    - **Quay cranes**: US&#36;10-18M each × 8-12 cranes per terminal
    - **Yard equipment**: US&#36;2-8M per crane × 50-100 cranes
    - **AGV fleet**: US&#36;300-500K per vehicle × 100-200 vehicles
    - **Land**: Reclamation costs, opportunity cost
    
    **Technology & Systems:**
    - **CITOS (TOS)**: Development, maintenance, upgrades
    - **IT infrastructure**: Servers, networks, cybersecurity
    - **Communication systems**: Radios, WiFi, 5G networks
    
    **Overhead:**
    - **Management**: Executive team, administrative staff
    - **Facilities**: Office buildings, workshops, utilities
    - **Insurance**: Property, liability, equipment coverage
    
    **Variable Costs (30-40% of total):**
    
    **Labor:**
    - **Operator wages**: Crane operators, PM drivers (if manual), supervisors
    - **Benefits**: Health insurance, pension, training
    - **Overtime**: Premium pay for peak periods, night shifts
    
    **Energy:**
    - **Electricity**: Cranes, lighting, HVAC, IT systems
    - **Diesel fuel**: Prime movers, yard equipment (if not electric)
    - **Variable with throughput**: More containers = more energy
    
    **Maintenance:**
    - **Preventive maintenance**: Regular servicing, parts replacement
    - **Corrective maintenance**: Repairs, breakdowns
    - **Proportional to usage**: More moves = more wear = more maintenance
    
    **The Economies of Scale Imperative:**
    
    **High Fixed Costs → Volume Critical:**
    - If terminal costs US&#36;400M/year fixed + US&#36;150M variable to handle 3M TEU:
    - **Cost per TEU** = (US&#36;400M + US&#36;150M) / 3M = **US&#36;183/TEU**
    - If increase to 4M TEU: (US&#36;400M + US&#36;160M) / 4M = **US&#36;140/TEU** (24% cost reduction per TEU!)
    - **Throughput growth is powerful**: Spreads fixed costs, dramatically lowers unit costs
    
    **Why Singapore Invests in Tuas:**
    - **65M TEU capacity** allows massive economies of scale
    - Unit costs at 65M TEU far lower than competitors at 10-20M TEU
    - Justifies S&#36;20B investment—**scale economies are strategic weapon**
    
    **Cost Management Strategies:**
    
    **Productivity Improvement:**
    - **Higher crane productivity**: 40 GMPH vs 30 GMPH = 33% more containers per crane-hour
    - **Result**: Same throughput with fewer cranes OR more throughput with same cranes
    - **Automation**: AGVs + ARMGs eliminate driver wages (70-80% labor cost reduction)
    
    **Energy Efficiency:**
    - **Electric equipment**: Lower cost per kWh than diesel fuel per gallon
    - **Renewable energy**: Solar generation (Tuas 40-60 MW) reduces grid electricity purchases
    - **Regenerative systems**: Cranes capture energy when lowering containers (10-15% energy savings)
    
    **Maintenance Optimization:**
    - **Preventive > Reactive**: Scheduled maintenance cheaper than emergency repairs
    - **Predictive maintenance**: IoT sensors + AI predict failures before they occur
    - **Result**: 30-40% reduction in maintenance costs, higher equipment uptime
    
    **Process Optimization:**
    - **Lean principles**: Eliminate waste in workflows
    - **CITOS optimization**: AI-powered berth planning, yard management, equipment scheduling
    - **Continuous improvement**: Kaizen culture—incrementally improve processes
    
    **The Cost-Quality Paradox:**
    
    **Higher Quality Often REDUCES Costs:**
    - **Conventional wisdom**: Quality costs money (inspection, redundancy, premium materials)
    - **Reality**: Poor quality is expensive (rework, damage claims, lost customers)
    
    **Example:**
    - **Low-quality crane** (cheap): US&#36;8M purchase, breaks down frequently, productivity 25 GMPH, 5-year life
    - **High-quality crane**: US&#36;15M purchase, reliable, productivity 40 GMPH, 30-year life
    - **Total cost of ownership**: High-quality crane cheaper over lifetime despite higher upfront cost
    
    **Cost vs Price:**
    
    **Different Concepts:**
    - **Cost**: What terminal spends to provide service
    - **Price**: What terminal charges customers
    - **Profit margin**: Price - Cost
    
    **Pricing Strategies:**
    
    **Cost-Plus Pricing:**
    - Calculate costs, add desired margin
    - **Problem**: Ignores what customers willing to pay, competitive dynamics
    
    **Value-Based Pricing:**
    - Price based on **value delivered to customer** (not just cost)
    - **Singapore approach**: Premium pricing justified by superior quality, reliability, service
    - Customers pay more because **total value** (quality + speed + service) exceeds incremental cost
    
    **Competitive Pricing:**
    - Price relative to competitors
    - Singapore: 5-15% premium over Malaysian, Indonesian competitors
    - Premium justified by operational excellence—customers accept higher price for better service
    
    **The Trade-off:**
    
    **Lowest Price Doesn't Always Win:**
    - Shipping lines evaluate **total value**, not just price
    - **Example**: Save US&#36;20/TEU at cheaper port but experience delays, damage → **penny-wise, pound-foolish**
    - **Smart customers** pay premium for reliability, quality, service
    
    **Cost Discipline Still Essential:**
    - Even premium-positioned terminals must control costs
    - **Efficiency gains** allow lower prices OR higher profits
    - Continuous cost reduction expands strategic options
    """)
    
    # Big Six spider chart visualization
    big_six_data = pd.DataFrame({
        'Competency': ['Quality', 'Reliability', 'Responsiveness', 'Agility', 'Service', 'Cost/Price'],
        'Singapore Performance': [95, 98, 92, 88, 90, 75],
        'Industry Average': [80, 75, 78, 70, 75, 80],
        'Description': [
            'Zero damage, accuracy, compliance',
            'BOA >90%, schedule adherence',
            'Fast turnaround (<24h), high productivity',
            'Volume/variety flexibility, innovation',
            'Customer support, information, problem-solving',
            'Competitive pricing with value delivery'
        ]
    })
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=big_six_data['Singapore Performance'],
        theta=big_six_data['Competency'],
        fill='toself',
        name='Singapore',
        line=dict(color='#3B82F6', width=3),
        fillcolor='rgba(59, 130, 246, 0.3)'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=big_six_data['Industry Average'],
        theta=big_six_data['Competency'],
        fill='toself',
        name='Industry Average',
        line=dict(color='#9CA3AF', width=2, dash='dash'),
        fillcolor='rgba(156, 163, 175, 0.1)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100])
        ),
        title={
            'text': 'The "Big Six" Operational Competencies - Singapore vs Industry',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#1F2937'}
        },
        height=550,
        showlegend=True,
        legend=dict(x=0.85, y=0.95)
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    <div class="insight-box">
    <strong>🎯 Critical Insight - The Big Six Interact and Trade-off:</strong><br><br>
    The lecture materials emphasize: <strong>"Competencies often require trade-offs, and need to be balanced"</strong><br><br>
    These six competencies are <strong>not independent</strong>—improving one often degrades another:<br><br>
    • <strong>Quality vs Speed (Responsiveness)</strong>: Taking time to ensure accuracy vs fast operations<br>
    • <strong>Cost vs Quality/Service</strong>: Lower prices vs premium quality/service offerings<br>
    • <strong>Agility vs Cost</strong>: Spare capacity for flexibility vs maximizing utilization for efficiency<br>
    • <strong>Reliability vs Responsiveness</strong>: Predictable schedules vs accommodating urgent requests<br><br>
    <strong>World-class operations don't maximize one competency—they optimize the BALANCE across all six</strong>, 
    aligned with competitive strategy and customer needs.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 3: Quality Management - FMEA
    # ============================================================================
    
    st.markdown('<p class="section-header">Quality Management: Failure Mode and Effects Analysis (FMEA)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The lecture materials emphasize: *"Important to plan maintenance: Failure mode and effects analysis (FMEA) 
    used to build reliability into design & development, and also for developing maintenance plans"*
    
    **FMEA is a systematic, proactive methodology** for identifying potential failures before they occur, assessing 
    their impacts, and implementing preventive measures. It's widely used in port operations planning, equipment 
    design, and maintenance strategy development.
    """)
    
    st.markdown('<p class="subsection-header">The FMEA Process</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Step 1: Identify Potential Failure Modes**
    
    **What could go wrong?**
    - Systematically examine each component, process, or operation
    - Brainstorm all possible ways things could fail
    - Consider: Equipment failures, human errors, process deviations, external factors
    
    **Port Operations Examples:**
    - **Quay crane failure**: Mechanical breakdown, electrical fault, structural damage
    - **Human errors**: Wrong container loaded, documentation mistakes, communication failures
    - **Process failures**: Yard congestion, berth conflicts, equipment scheduling errors
    - **External factors**: Weather delays, vessel late arrivals, power outages
    
    **Step 2: Assess Severity (S)**
    
    **How bad is the impact if this failure occurs?**
    
    **Severity Scale (1-10):**
    - **1-2 (Negligible)**: Minor inconvenience, no real impact on operations
    - **3-4 (Minor)**: Small delay, easily resolved, minimal cost
    - **5-6 (Moderate)**: Significant delay, requires attention, moderate cost
    - **7-8 (Major)**: Major operational disruption, high cost, customer dissatisfaction
    - **9-10 (Catastrophic)**: Safety incident, major damage, complete operational halt, reputation damage
    
    **Examples:**
    - **Printer jam in office**: Severity = 2 (minor inconvenience)
    - **One crane breaks down (7 others operational)**: Severity = 5 (moderate—productivity reduced but operations continue)
    - **All cranes break down**: Severity = 9 (catastrophic—terminal cannot operate)
    - **Container falls from crane, kills worker**: Severity = 10 (catastrophic—life lost, operations halted, regulatory investigation)
    
    **Step 3: Assess Occurrence (O)**
    
    **How likely is this failure to occur?**
    
    **Occurrence Scale (1-10):**
    - **1-2 (Remote)**: Extremely unlikely, almost impossible
    - **3-4 (Low)**: Rare, unlikely but possible
    - **5-6 (Moderate)**: Occasional, happens sometimes
    - **7-8 (High)**: Frequent, happens regularly
    - **9-10 (Very High)**: Almost certain, happens constantly
    
    **Examples:**
    - **Meteor strike damages crane**: Occurrence = 1 (remote, virtually impossible)
    - **Modern well-maintained crane breaks down**: Occurrence = 3 (low, but does happen occasionally)
    - **Human operator makes data entry error**: Occurrence = 6 (moderate, humans make mistakes)
    - **Truck arrives without booking**: Occurrence = 8 (high, happens daily at busy terminals)
    
    **Step 4: Assess Detection (D)**
    
    **Can we detect the failure before it causes problems?**
    
    **Detection Scale (1-10):** (Note: Higher = harder to detect)
    - **1-2 (Very High)**: Failure almost certain to be detected immediately
    - **3-4 (High)**: Failure likely to be detected quickly
    - **5-6 (Moderate)**: Failure might be detected, might not
    - **7-8 (Low)**: Failure unlikely to be detected until causes problems
    - **9-10 (Very Low)**: Failure almost impossible to detect in advance
    
    **Examples:**
    - **Crane stops moving**: Detection = 1 (immediately obvious, crane just stops)
    - **Crane bearing wearing out**: Detection = 3 (vibration sensors, temperature monitors alert maintenance)
    - **Wrong container loaded on vessel**: Detection = 7 (hard to detect until vessel arrives at next port)
    - **Data corruption in TOS database**: Detection = 9 (very hard to detect until causes operational problems)
    
    **Step 5: Calculate Risk Priority Number (RPN)**
    
    **RPN = Severity × Occurrence × Detection**
    
    **Range: 1 to 1,000**
    - **RPN < 100**: Low risk (monitor but no immediate action needed)
    - **RPN 100-300**: Moderate risk (develop preventive measures)
    - **RPN > 300**: High risk (immediate action required, priority mitigation)
    
    **Step 6: Prioritize and Mitigate**
    
    **Focus on Highest RPN Failures:**
    - **High RPN = High Priority**: These failures are likely, severe, and hard to detect—very dangerous!
    - **Develop mitigation strategies**: Reduce Severity, Occurrence, or improve Detection
    - **Implement controls**: Preventive maintenance, redundancy, inspection procedures, training
    - **Re-calculate RPN**: After implementing controls, assess new RPN (should be lower)
    """)
    
    # FMEA example table
    fmea_example = pd.DataFrame({
        'Failure Mode': [
            'Quay crane mechanical breakdown',
            'Wrong container loaded on vessel',
            'Yard storage location system crash',
            'AGV battery depleted mid-operation',
            'Severe weather (typhoon)',
            'Truck arrives without appointment'
        ],
        'Severity (S)': [7, 9, 8, 4, 10, 3],
        'Occurrence (O)': [3, 5, 2, 4, 1, 8],
        'Detection (D)': [2, 8, 3, 2, 1, 2],
        'RPN (S×O×D)': [42, 360, 48, 32, 10, 48],
        'Priority': ['Low', 'HIGH', 'Low', 'Low', 'Low', 'Low'],
        'Mitigation Strategy': [
            'Preventive maintenance program, spare parts inventory',
            'Automated verification system, RFID scanning, operator double-check',
            'Redundant database servers, regular backups, failover systems',
            'Battery monitoring system, auto-return-to-charge, fleet size buffer',
            'Early warning systems, emergency procedures (Singapore: low typhoon risk)',
            'Truck Appointment System (TAS), automated gate rejection without booking'
        ]
    })
    
    st.dataframe(fmea_example, width='stretch', hide_index=True)
    
    st.markdown("""
    **Analysis of FMEA Example:**
    
    **Highest Risk: "Wrong Container Loaded" (RPN = 360)**
    - **Why high risk?**: Severity 9 (major customer impact, expensive correction) × Occurrence 5 (human error happens) 
      × Detection 8 (hard to detect until vessel already departed) = **360 RPN**
    - **Mitigation**: Implement multiple verification layers—RFID scanning, barcode checks, operator confirmation, 
      automated CITOS validation
    - **Result**: Reduces Occurrence to 2 (automated system rarely fails) and Detection to 3 (system alerts to 
      mismatches) → New RPN = 9 × 2 × 3 = **54** (dramatic improvement!)
    
    **Strategic Insight:**
    - **FMEA guides investment priorities**: Highest RPN failures get most attention and resources
    - **Proactive vs Reactive**: Identify and prevent problems before they occur (cheaper than fixing after)
    - **Continuous improvement**: Re-run FMEA periodically as operations evolve, new failure modes emerge
    """)
    
    st.markdown("""
    <div class="success-box">
    <strong>✅ FMEA Success Story - Singapore PSA:</strong><br><br>
    PSA extensively uses FMEA in Tuas Mega Port design:<br><br>
    <strong>Example - AGV Fleet Reliability:</strong><br>
    • <strong>Failure mode identified</strong>: Multiple AGVs break down simultaneously (e.g., software bug)<br>
    • <strong>Severity</strong>: 8 (major operational disruption, all horizontal transport stops)<br>
    • <strong>Occurrence</strong>: 3 (software bugs rare but happen)<br>
    • <strong>Detection</strong>: 5 (might not detect until multiple AGVs affected)<br>
    • <strong>RPN</strong>: 8 × 3 × 5 = <strong>120 (moderate risk)</strong><br><br>
    <strong>Mitigation implemented</strong>:<br>
    • Maintain backup fleet of prime movers (manual fallback if AGV system fails)<br>
    • Diverse AGV manufacturers (multiple vendors reduces single-point-of-failure risk)<br>
    • Rigorous testing protocols before software updates deployed<br>
    • Real-time monitoring with automatic alerts<br><br>
    <strong>Result</strong>: Tuas design includes operational redundancy, can handle AGV system failures without 
    complete shutdown. This FMEA-driven design makes Tuas more resilient and reliable.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 4: Capacity Planning and Management
    # ============================================================================
    
    st.markdown('<p class="section-header">Capacity Planning and Management</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Capacity** is the maximum output an operation can produce under normal conditions. Capacity planning determines 
    how much capacity to build and when, while capacity management ensures existing capacity is used effectively.
    """)
    
    st.markdown('<p class="subsection-header">Three Types of Capacity</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **1. Design Capacity (Theoretical Maximum)**
    
    **Definition**: Maximum possible output under ideal conditions
    - Perfect equipment availability (zero breakdowns)
    - Perfect demand (continuous flow, no idle time)
    - Perfect operations (no errors, optimal efficiency)
    
    **Port Example:**
    - **Berth design capacity**: 365 days × 24 hours = 8,760 berth-hours per year
    - **Crane design capacity**: If crane can do 40 moves/hour, theoretical capacity = 40 × 8,760 = 350,400 moves/year per crane
    
    **Reality**: Never achieved in practice (equipment maintenance, demand variability, operational inefficiencies)
    
    **2. Effective Capacity (Realistic Maximum)**
    
    **Definition**: Maximum output under realistic operating conditions
    - Accounts for scheduled downtime (maintenance, inspections)
    - Accounts for demand patterns (not continuous, has peaks and valleys)
    - Accounts for normal inefficiencies (setup time, changeovers, breaks)
    
    **Port Example:**
    - **Berth effective capacity**:
      - Subtract maintenance windows: ~2% = 8,590 hours available
      - Subtract vessel turnaround gaps (cannot instantly switch vessels): ~5% = 8,160 operational hours
      - **Effective capacity: ~93% of design capacity**
    
    **3. Actual Output (Real Performance)**
    
    **Definition**: What the operation actually produces
    - Real equipment breakdowns, delays, inefficiencies
    - Real demand variability (seasonality, economic cycles)
    - Real operational issues (weather, labor issues, coordination problems)
    
    **Port Example:**
    - **Actual throughput**: Might be 75-85% of effective capacity
    - Gap = waste, inefficiency, under-utilization
    
    **Utilization Metrics:**
    
    **Utilization = (Actual Output / Effective Capacity) × 100%**
    
    **Optimal Utilization: 80-90%**
    - **<80%**: Under-utilized, excess capacity waste, higher unit costs
    - **80-90%**: Sweet spot—high efficiency with buffer for variability
    - **>90%**: Over-utilized, no flexibility, delays when demand spikes, quality suffers
    """)
    
    # Capacity types visualization
    capacity_data = pd.DataFrame({
        'Type': ['Design Capacity', 'Effective Capacity', 'Actual Output'],
        'Value': [100, 93, 82],
        'Description': [
            'Theoretical maximum (perfect conditions)',
            'Realistic maximum (normal conditions)',
            'Real performance (current operations)'
        ]
    })
    
    fig2 = go.Figure()
    
    colors = ['#60A5FA', '#34D399', '#FBBF24']
    
    for i, row in capacity_data.iterrows():
        fig2.add_trace(go.Bar(
            name=row['Type'],
            x=[row['Type']],
            y=[row['Value']],
            marker_color=colors[i],
            text=[f"{row['Value']}%"],
            textposition='outside',
            hovertemplate=f"<b>{row['Type']}</b><br>{row['Description']}<br><b>{row['Value']}%</b><extra></extra>"
        ))
    
    fig2.update_layout(
        title={
            'text': 'Three Types of Capacity',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        yaxis_title="Capacity (%)",
        yaxis=dict(range=[0, 110]),
        height=450,
        plot_bgcolor='white',
        showlegend=False
    )
    
    st.plotly_chart(fig2, width='stretch')
    
    st.markdown("""
    **Capacity Planning Horizons:**
    
    **Long-term Capacity Planning (5-10+ years):**
    
    **Major Infrastructure Decisions:**
    - How many berths to build?
    - Where to locate new terminals?
    - What automation level to deploy?
    - **Example**: Tuas Mega Port (65M TEU capacity decision made in 2012 for 2040 horizon)
    
    **Characteristics:**
    - **Large capital investment**: Billions of dollars
    - **Long lead time**: 5-10 years from decision to operational
    - **Irreversible**: Cannot easily undo once built
    - **Strategic**: Shapes competitive position for decades
    
    **Medium-term Capacity Planning (1-3 years):**
    
    **Equipment and Systems:**
    - Purchase additional cranes, AGVs, yard equipment
    - Expand IT systems, upgrade CITOS
    - Hire and train additional workforce
    - **Example**: Order 10 additional quay cranes for delivery in 18 months
    
    **Characteristics:**
    - **Moderate investment**: Millions to tens of millions
    - **Moderate lead time**: 6-24 months typical
    - **Some flexibility**: Equipment can be redeployed or sold
    - **Tactical**: Adjusts capacity to near-term demand forecasts
    
    **Short-term Capacity Management (Days to Months):**
    
    **Operational Adjustments:**
    - Overtime, additional shifts
    - Temporary workers for peak seasons
    - Reschedule maintenance to off-peak periods
    - Dynamic resource allocation (CITOS optimization)
    - **Example**: Add night shift during Christmas peak season
    
    **Characteristics:**
    - **Low investment**: Overtime wages, temporary staff costs
    - **Immediate**: Can implement in days or weeks
    - **Fully flexible**: Easily reversed when demand drops
    - **Reactive**: Responds to actual demand fluctuations
    """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>💡 The Capacity-Demand Matching Challenge:</strong><br><br>
    <strong>The Problem</strong>: Demand fluctuates (seasonality, economic cycles) but capacity is expensive and 
    fixed in short-term. How much capacity to build?<br><br>
    <strong>Build Too Little</strong>:<br>
    • Turn away business during peaks (lost revenue)<br>
    • High utilization (>95%) → delays, quality problems, unhappy customers<br>
    • Cannot accommodate growth → lose market share to competitors<br><br>
    <strong>Build Too Much</strong>:<br>
    • Low utilization (<70%) → high fixed costs spread across low volume = high unit costs<br>
    • Wasted capital investment (could have used money elsewhere)<br>
    • May never reach projected demand (Tuas risk scenario)<br><br>
    <strong>The Solution - Strategic Capacity Planning</strong>:<br>
    • Build for <strong>85-90% utilization at expected average demand</strong><br>
    • Provides 10-15% buffer for peak periods<br>
    • Use short-term management (overtime, temporary staff) for extreme peaks<br>
    • <strong>Phased expansion</strong>: Build incrementally as demand materializes (Tuas strategy)
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 5: Maintenance Strategy
    # ============================================================================
    
    st.markdown('<p class="section-header">Maintenance: "The Science of Caring for Things"</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The lecture materials define maintenance as: *"The science of caring for things. Aims to ensure that equipment 
    & facilities function according to specs and fully meet output, quality & safety requirements at the lowest 
    possible cost"*
    
    And emphasize: *"Excellent maintenance of facilities & equipment is key to operations management and operations 
    excellence"*
    
    In capital-intensive port operations where **equipment represents 40-50% of total investment** (US&#36;10-18M 
    per quay crane, US&#36;2-8M per yard crane, US&#36;300-500K per AGV), maintenance strategy directly impacts:
    - **Reliability**: Equipment uptime determines operational capacity
    - **Safety**: Poor maintenance causes accidents, injuries, fatalities
    - **Costs**: Maintenance represents 15-20% of operating budget
    - **Asset life**: Good maintenance extends equipment lifespan 50-100%
    """)
    
    st.markdown('<p class="subsection-header">Three Maintenance Strategies</p>', unsafe_allow_html=True)
    
    # Maintenance strategies comparison
    maintenance_strategies = pd.DataFrame({
        'Strategy': [
            'Reactive (Run-to-Failure)',
            'Preventive (Time-Based)',
            'Predictive (Condition-Based)'
        ],
        'Approach': [
            'Fix equipment when it breaks',
            'Scheduled maintenance at regular intervals (hours, months)',
            'Monitor equipment condition, maintain when needed (sensors, AI)'
        ],
        'When Applied': [
            'Low-cost equipment, non-critical, easy/cheap to replace',
            'Critical equipment, established maintenance schedules, moderate cost',
            'Very expensive/critical equipment, technology available, data-driven'
        ],
        'Advantages': [
            'Zero planned downtime, no inspection costs, maximum equipment usage, simple',
            'Prevents unexpected failures, scheduled during low-demand periods, proven effective',
            'Minimum downtime, optimal maintenance timing, extends asset life, lower costs'
        ],
        'Disadvantages': [
            'Unexpected failures disrupt operations, emergency repairs expensive, safety risks',
            'Some maintenance unnecessary (equipment fine), consumes resources, opportunity cost',
            'Requires sensors/IoT, data analytics capability, initial investment high'
        ],
        'Port Examples': [
            'Light bulbs, hand tools, safety cones—cheap, non-critical items',
            'Quay cranes (service every 500 hours), AGVs (battery replacement every 3-5 years)',
            'ARMG bearings (vibration sensors detect wear), crane motors (temperature monitoring)'
        ],
        'Typical Cost': [
            'US&#36;50-100/unit but high frequency (many failures)',
            'US&#36;100-200/maintenance cycle, scheduled frequency',
            'US&#36;200-300/maintenance (when needed), lower frequency = lower total cost'
        ]
    })
    
    st.dataframe(maintenance_strategies, width='stretch', hide_index=True)
    
    st.markdown("""
    **The Evolution of Maintenance - Reactive → Preventive → Predictive:**
    
    **Historical (1960s-1980s): Reactive Maintenance Dominant**
    - **Philosophy**: "If it ain't broke, don't fix it"
    - **Reality**: Unexpected equipment failures caused major operational disruptions
    - **Problem**: Emergency repairs expensive (2-3× cost vs planned maintenance), safety incidents
    
    **Modern (1990s-2010s): Preventive Maintenance Standard**
    - **Philosophy**: "Regular service prevents failures"
    - **Reality**: Scheduled maintenance (every X hours or Y months) became industry norm
    - **Improvement**: Fewer unexpected failures, safer operations, more reliable
    - **Limitation**: Sometimes maintaining equipment that doesn't need it (wasteful)
    
    **Future (2020s+): Predictive Maintenance Emerging**
    - **Philosophy**: "Monitor condition, maintain only when actually needed"
    - **Technology**: IoT sensors + AI analyze equipment health in real-time
    - **Prediction**: Alert when failure likely in next 2-4 weeks (schedule maintenance proactively)
    - **Optimization**: Minimum necessary maintenance = lowest cost, maximum uptime
    
    **Singapore Tuas Example:**
    
    **ARMGs with Predictive Maintenance:**
    - **Vibration sensors** on crane bearings, motors, gantry wheels
    - **Temperature sensors** on electrical components
    - **Usage tracking**: Hours operated, load carried, cycles completed
    - **AI model**: Learns normal operating patterns, detects deviations
    
    **When Sensor Data Shows Anomaly:**
    - Example: Bearing vibration increasing gradually over weeks
    - **AI prediction**: "Bearing likely to fail in 3-4 weeks"
    - **Proactive action**: Schedule bearing replacement during next low-demand period (e.g., weekend)
    - **Result**: Bearing replaced before failure, zero unplanned downtime, optimal timing
    
    **Benefits:**
    - **30-40% reduction** in maintenance costs vs time-based preventive maintenance
    - **Equipment uptime >99%** (vs 95-97% with preventive only)
    - **50-100% longer asset life** (optimal maintenance extends lifespan)
    """)
    
    # ============================================================================
    # SECTION 6: Strategic Trade-offs in Operations
    # ============================================================================
    
    st.markdown('<p class="section-header">Strategic Trade-offs: The Art of Operations Management</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The lecture materials emphasize: **"Competencies often require trade-offs, and need to be balanced"**
    
    This is the **fundamental reality of operations management**: You cannot maximize all objectives simultaneously. 
    Every decision involves trade-offs—improving one dimension often degrades another. **The art of operations 
    management is choosing which trade-offs to make** based on competitive strategy, customer needs, and resource 
    constraints.
    """)
    
    # Major trade-offs table
    major_tradeoffs = pd.DataFrame({
        'Trade-off': [
            'Cost vs Quality',
            'Cost vs Flexibility (Agility)',
            'Speed (Responsiveness) vs Quality',
            'Capacity vs Utilization',
            'Standardization vs Customization',
            'Automation vs Employment',
            'Efficiency vs Resilience'
        ],
        'The Tension': [
            'Lower costs mean cutting corners; higher quality requires premium investment',
            'Excess capacity enables flexibility but is expensive; high utilization is efficient but inflexible',
            'Rushing increases error rates; thoroughness takes time',
            'Build excess capacity (expensive) vs operate near capacity limits (inflexible)',
            'Standardized processes are efficient but cannot accommodate special needs; customization is expensive',
            'Automation reduces labor costs and improves consistency; displaces workers, creates social costs',
            'Specialized, optimized systems are efficient but fragile; redundant systems are resilient but costly'
        ],
        'Port Example': [
            'Cheap cranes break down frequently (low quality, low cost); premium cranes reliable (high quality, high cost)',
            'Tuas 65M TEU capacity with 41M throughput = flexibility for growth but 37% excess capacity cost',
            'Fast 22-hour turnaround risks mistakes; careful 26-hour turnaround ensures accuracy',
            'Build 10 berths for peak demand (expensive, often idle) vs build 8 berths (congestion during peaks)',
            'All vessels follow standard process (efficient) vs customized handling for special cargo (expensive)',
            'Tuas AGVs eliminate 2,000 driver jobs (efficient, controversial) vs keep human drivers (employment, costly)',
            'Single berth planning algorithm (efficient) vs multiple backup systems (resilient, redundant, costly)'
        ],
        'How Singapore Decides': [
            'Premium positioning → invest in quality equipment despite higher cost (justified by superior service)',
            'Deliberately maintain 10-15% excess capacity → strategic flexibility worth the cost',
            'Balance speed with quality checks → automation helps (fast AND accurate)',
            'Long-term phased approach → build in stages, adjust to actual demand (Tuas 4 phases)',
            'Standard core processes + premium custom services for willing-to-pay customers',
            'Gradual automation transition + extensive retraining programs + social safety net',
            'Build redundancy in critical systems (backup CITOS servers, diverse AGV fleet, spare equipment)'
        ],
        'Strategic Implication': [
            'Premium-positioned operations can afford quality investment; low-cost leaders cannot',
            'Capacity decisions are strategic bets on future demand with long-term consequences',
            'Speed-quality tradeoff managed through process design, automation, continuous improvement',
            'Phased capacity expansion provides flexibility to adjust as demand evolves',
            'Segment customers: standard service for price-sensitive, premium for quality-focused',
            'Automation inevitable in high-wage countries but social transition critical to manage',
            'Resilience investment is insurance—costs money but protects against catastrophic failures'
        ]
    })
    
    st.dataframe(major_tradeoffs, width='stretch', hide_index=True)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ There is No "Perfect" Operation:</strong><br><br>
    Every operation involves <strong>conscious strategic choices</strong> about which trade-offs to make:<br><br>
    <strong>Low-Cost Strategy</strong>:<br>
    • Sacrifice: Quality, Service, Flexibility (to minimize costs)<br>
    • Example: Basic container handling, standard service only, high utilization (90-95%)<br>
    • Target customers: Price-sensitive cargo owners, low-value commodities<br><br>
    <strong>Premium Strategy (Singapore)</strong>:<br>
    • Sacrifice: Cost (willing to pay more for quality, reliability, service, flexibility)<br>
    • Example: World-class equipment, superior service, excess capacity buffer (85% utilization)<br>
    • Target customers: Time-sensitive cargo, high-value goods, alliance commitments<br><br>
    <strong>Neither strategy is "wrong"</strong>—they're <strong>different choices</strong> aligned with different 
    competitive positioning and customer needs. The mistake is <strong>not choosing</strong>—trying to be all 
    things to all customers leads to mediocrity on all dimensions.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 7: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways: Operations Management Fundamentals</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **The "Big Six" Competencies (Lecture Verified):**
        - **Quality**: "High quality attracts customers; improving quality retains them!"
        - **Reliability**: "Unreliable means losing customers" (BOA >90%, schedule adherence)
        - **Responsiveness**: Speed of operations (<24h turnaround, 35-40 GMPH)
        - **Agility**: Volume/variety flexibility, innovation capabilities
        - **Service**: Customer support, information, problem-solving, courtesy
        - **Cost/Price**: Productive & efficient operations reduce costs
        - **Critical insight**: Competencies interact and require trade-offs
        
        **Quality Management - FMEA:**
        - Systematic method to identify potential failures proactively
        - **Process**: Identify failures → Assess Severity, Occurrence, Detection → Calculate RPN → Mitigate
        - **RPN = S × O × D** (range 1-1,000, >300 = high priority)
        - Used extensively in port equipment design, maintenance planning
        - Example: Wrong container loaded (RPN=360) → automated verification systems
        
        **Capacity Concepts:**
        - **Design capacity**: Theoretical maximum (100%)
        - **Effective capacity**: Realistic maximum (~93%)
        - **Actual output**: Real performance (~82%)
        - **Optimal utilization**: 80-90% (efficiency with flexibility buffer)
        - **<80%** = waste; **>90%** = no buffer, quality suffers
        """)
    
    with col2:
        st.markdown("""
        **Capacity Planning Horizons:**
        - **Long-term (5-10+ years)**: Major infrastructure (Tuas 65M TEU decision)
        - **Medium-term (1-3 years)**: Equipment purchases (cranes, AGVs, IT systems)
        - **Short-term (days-months)**: Operational adjustments (overtime, temporary staff)
        - **Phased approach**: Build incrementally, adjust to actual demand
        
        **Maintenance Strategies (Lecture Verified):**
        - **Reactive**: Fix when breaks (low-cost items only)
        - **Preventive**: Scheduled time-based maintenance (critical equipment standard)
        - **Predictive**: Condition-based with IoT sensors + AI (cutting-edge)
        - Quote: "Excellent maintenance key to operations management and excellence"
        - **Predictive benefits**: 30-40% cost reduction, >99% uptime, 50-100% longer asset life
        
        **Strategic Trade-offs:**
        - **Cost vs Quality/Flexibility/Service**: Cannot minimize cost AND maximize quality
        - **Speed vs Quality**: Fast operations risk errors
        - **Capacity vs Utilization**: Excess capacity expensive but provides flexibility
        - **Automation vs Employment**: Efficiency vs social impact
        - **No perfect operation**: Choose trade-offs aligned with strategy
        - **Singapore's choice**: Premium positioning → sacrifice cost for quality/reliability/service/flexibility
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Operations management is the strategic discipline of <strong>optimizing the "Big Six" 
    competencies</strong> (Quality, Reliability, Responsiveness, Agility, Service, Cost/Price) that determine customer attraction 
    and retention. The lecture materials emphasize that <strong>"High quality attracts customers; improving quality retains them!"</strong> 
    and <strong>"Unreliable means losing customers"</strong>—underscoring quality and reliability as foundational. Success requires 
    <strong>proactive quality management</strong> using methodologies like FMEA (Failure Mode and Effects Analysis, calculating 
    RPN = Severity × Occurrence × Detection to prioritize risk mitigation), <strong>strategic capacity planning</strong> across 
    multiple horizons (long-term infrastructure decisions like Tuas, medium-term equipment, short-term operational adjustments) 
    while maintaining optimal 80-90% utilization (efficiency with flexibility buffer), <strong>excellent maintenance</strong> 
    evolving from reactive through preventive to predictive (IoT sensors + AI enabling 30-40% cost reduction and >99% uptime), 
    and <strong>conscious trade-off management</strong> recognizing that competencies interact and conflict—the lecture materials 
    note that <strong>"Competencies often require trade-offs, and need to be balanced."</strong> There is no "perfect" operation 
    that maximizes all dimensions simultaneously; rather, <strong>world-class operations make strategic choices</strong> about 
    which trade-offs to accept based on competitive positioning, customer needs, and resource constraints. <strong>Singapore's 
    approach exemplifies premium positioning</strong>: sacrifice cost (deliberately maintain 10-15% excess capacity, invest in 
    world-class equipment, provide superior service) to excel at quality (zero-damage handling), reliability (>90% BOA consistently), 
    responsiveness (35-40 GMPH, <24h turnaround), agility (handle volume fluctuations, special cargo), and service (proactive 
    customer support)—justified by ability to charge 5-15% premium and capture high-value alliance commitments. The art of 
    operations management lies in <strong>understanding these trade-offs explicitly, making conscious strategic choices aligned 
    with competitive strategy, and continuously improving to expand the frontier</strong>—achieving more on multiple dimensions 
    through innovation, technology, process optimization, and operational excellence.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    Continue exploring maritime operations and industry dynamics to complete your comprehensive understanding of 
    the container shipping ecosystem and terminal operations that enable global trade.
    """)
