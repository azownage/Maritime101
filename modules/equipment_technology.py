import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">🤖 Equipment, Automation & CITOS</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Master the sophisticated equipment powering modern container terminals, from US&#36;10-18 million quay cranes to 
    automated guided vehicle fleets, understand automation levels from conventional manual operations through fully 
    automated "lights-out" terminals achieving 70-80% labor reduction, explore PSA's proprietary CITOS Terminal 
    Operating System that coordinates all terminal activities using AI/ML and real-time optimization, and comprehend 
    the economics and strategic considerations driving terminal automation investments of US&#36;500M-1B+.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Quay-Side Equipment - Ship-to-Shore Cranes
    # ============================================================================
    
    st.markdown('<p class="section-header">Quay-Side Equipment: Ship-to-Shore (STS) Cranes</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Quay cranes—also called Ship-to-Shore (STS) cranes or container gantry cranes—are the massive structures 
    dominating container terminal skylines. These are among the largest and most expensive pieces of equipment in 
    terminal operations, with modern super post-Panamax cranes costing US&#36;13-18 million each.
    
    The lecture materials emphasize that quay crane specifications directly determine a terminal's ability to serve 
    modern mega vessels, making crane capability a critical infrastructure constraint for hub port competitiveness.
    """)
    
    st.markdown('<p class="subsection-header">Quay Crane Classifications and Design</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Structural Classifications:**
    
    The lecture materials identify two primary structural designs for quay cranes:
    
    **A-Shaped Quay Cranes:**
    - **Structure**: Single A-frame portal design on seaside
    - **Footprint**: Narrower base, less stable in high winds
    - **Historical**: Earlier generation design
    - **Usage**: Older terminals, smaller vessels
    - **Advantages**: Lower cost, simpler construction
    - **Disadvantages**: Limited outreach capability, less stable
    
    **H-Shaped Quay Cranes (Modern Standard):**
    - **Structure**: Dual portal frame creating "H" shape when viewed from vessel
    - **Footprint**: Wider, more stable base
    - **Modern**: Current industry standard for mega vessel terminals
    - **Usage**: All new terminal developments, mega vessel handling
    - **Advantages**: Greater stability in wind, longer outreach capability (65-80m), higher lifting capacity
    - **Disadvantages**: Higher cost (US&#36;13-18M vs US&#36;8-13M for A-shaped)
    
    **The lecture materials note**: "Due to the huge throughput in the terminals, the H-shaped are mostly adopted." 
    This reflects industry reality—H-shaped cranes dominate modern terminals because their superior stability and 
    outreach enable handling of 20,000-24,000 TEU mega vessels that are 24 containers wide.
    
    **Trolley System Classifications:**
    
    **Single Trolley System:**
    - **Operation**: One trolley moves horizontally along boom
    - **Function**: Carries spreader and container
    - **Travel**: Must travel full distance quay→vessel→quay for each move
    - **Productivity**: Lower (more travel time per move)
    - **Cost**: US&#36;8-13M (simpler system)
    - **Usage**: Older cranes, smaller terminals
    
    **Double Trolley System (Modern Standard):**
    - **Operation**: Two trolleys—main trolley + auxiliary trolley
    - **Function**: Main trolley serves vessel, auxiliary trolley serves apron (landside)
    - **Handoff**: Container transferred between trolleys mid-span
    - **Productivity**: Higher—while main trolley serves vessel, auxiliary trolley simultaneously transports 
      previous container to/from apron
    - **Time saving**: 15-25% improvement in cycle time
    - **Cost**: US&#36;10-15M (added complexity)
    - **Usage**: Most modern terminals
    
    **Triple Spreader System (Latest Technology):**
    - **Capability**: Can lift three 20ft containers simultaneously OR one 40ft + one 20ft
    - **Productivity boost**: Up to 50% increase in moves per hour on appropriate cargo
    - **Constraint**: Only works when consecutive containers in bay plan are all 20ft containers
    - **Reality**: In practice, 20-30% of moves can use triple-lift (mixed cargo limits usage)
    - **Cost premium**: Additional US&#36;1-2M over double trolley
    - **ROI**: Worthwhile for high-volume terminals with significant 20ft cargo
    - **Example**: Singapore PSA deploying triple-lift cranes at Tuas for productivity gains
    """)
    
    # Quay crane comparison table
    qc_comparison = pd.DataFrame({
        'Specification': [
            'Outreach (Reach across vessel)',
            'Back Reach (Landside)',
            'Lift Height Above Quay',
            'Lifting Capacity Under Spreader',
            'Hoisting Speed (Loaded)',
            'Trolley Travel Speed',
            'Crane Travel Speed (Along quay)',
            'Target Productivity (GMPH)',
            'Typical Cost (New)',
            'Design Lifespan',
            'Power Consumption',
            'Crew Required'
        ],
        'Panamax Crane': [
            '45-50m (serves vessels 13 containers wide)',
            '15m',
            '35m above quay level',
            '40-50 tonnes (twin 20ft or one 40ft)',
            '45 m/min',
            '180 m/min',
            '30 m/min',
            '25-30 GMPH (gross moves per hour)',
            'US&#36;5-8 million',
            '25-30 years with maintenance',
            '~1-1.5 MW per crane during operations',
            '1 operator per crane (+ maintenance team)'
        ],
        'Post-Panamax Crane': [
            '50-65m (serves vessels 18 containers wide)',
            '20m',
            '40m above quay level',
            '50-60 tonnes',
            '50 m/min',
            '200 m/min',
            '35 m/min',
            '30-35 GMPH',
            'US&#36;10-13 million',
            '25-30 years',
            '~1.5-2 MW per crane',
            '1 operator + maintenance'
        ],
        'Super Post-Panamax (Modern)': [
            '65-80m (serves mega vessels 22-24 containers wide)',
            '25m',
            '50m above quay level',
            '60-85 tonnes (triple-lift capable)',
            '60 m/min',
            '240 m/min',
            '45 m/min',
            '35-40 GMPH (world-class: 40-45 GMPH)',
            'US&#36;13-18 million',
            '30-35 years',
            '~2-2.5 MW per crane',
            '1 operator + maintenance'
        ]
    })
    
    st.dataframe(qc_comparison, width='stretch', hide_index=True)
    
    st.markdown("""
    **Understanding GMPH (Gross Moves Per Hour):**
    
    GMPH is the critical productivity metric for quay cranes, measuring total container moves divided by total 
    operation time including all delays. The lecture materials emphasize that world-class terminals target 35-40 GMPH 
    consistently.
    
    **What factors determine GMPH?**
    
    **Equipment factors:**
    - Crane speed (hoisting, trolley, gantry)—faster = more moves
    - Trolley system (double trolley 15-25% faster than single)
    - Spreader technology (triple-lift can boost by 50% on suitable cargo)
    - Equipment reliability (breakdowns stop productivity)
    
    **Operational factors:**
    - Operator skill (expert operators 20-30% more productive)
    - Horizontal transport availability (crane waits if no PM/AGV ready)
    - Vessel stow complexity (easy stows allow faster crane operations)
    - Weather (high winds >25 knots slow or halt operations)
    
    **Planning factors:**
    - Crane work sequence optimization (minimize crane travel between bays)
    - Container staging on apron (pre-positioned containers enable continuous loading)
    - Coordination across multiple cranes (avoid interference, optimize workload distribution)
    
    **Singapore PSA Performance**: Consistently achieves 35-40 GMPH average across operations, with peak performance 
    exceeding 45 GMPH under ideal conditions. This world-leading productivity results from combined excellence in 
    equipment (latest super post-Panamax cranes with triple-lift), operations (CITOS optimization), and workforce 
    (highly trained crane operators).
    """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>💡 Quay Crane Investment Economics:</strong><br><br>
    <strong>Capital Investment</strong>: A mega vessel terminal needs 8-12 super post-Panamax cranes @ US&#36;15M 
    each = US&#36;120-180M equipment investment just for quay cranes. Add infrastructure (berth, power, rails, 
    foundations) = total US&#36;200-300M per berth.<br><br>
    <strong>Operating Costs</strong>: Each crane consumes ~2 MW power (~US&#36;300K/year electricity) + operator 
    wages (~US&#36;80-120K/year in Singapore) + maintenance (US&#36;200-500K/year) = US&#36;600K-1M per crane 
    annually.<br><br>
    <strong>Productivity Impact</strong>: Upgrading from 30 GMPH to 40 GMPH = 33% faster vessel turnaround. For 
    terminal handling 2M TEU/year, this saves ~100,000 crane-hours annually, enabling 15-20% capacity increase 
    without additional berths.<br><br>
    <strong>The Bottom Line</strong>: Quay cranes are extraordinarily expensive but productivity gains justify 
    investment—faster vessel turnaround attracts more shipping line calls, enabling hub ports to grow volumes and 
    maintain competitiveness.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 2: Yard Equipment - Storage and Retrieval Systems
    # ============================================================================
    
    st.markdown('<p class="section-header">Yard Equipment: Container Storage and Retrieval</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Yard equipment moves containers within the terminal storage yard, stacking containers vertically to maximize 
    land utilization and retrieving containers when needed for vessel loading or truck pickup. The lecture materials 
    emphasize that yard equipment selection fundamentally shapes terminal layout, capacity, and operational efficiency.
    """)
    
    st.markdown('<p class="subsection-header">Yard Equipment Types: Comprehensive Comparison</p>', unsafe_allow_html=True)
    
    # Comprehensive yard equipment comparison
    yard_equipment_comparison = pd.DataFrame({
        'Equipment Type': [
            'RTG (Rubber-Tyred Gantry)',
            'RMG (Rail-Mounted Gantry)',
            'ARMG (Automated RMG)',
            'Reach Stacker',
            'Straddle Carrier'
        ],
        'Power Source & Mobility': [
            'Diesel engine, rubber tyres, can move anywhere in yard',
            'Electric (grid-powered), fixed on rail tracks within block',
            'Electric (grid-powered), fully automated on fixed rails',
            'Diesel engine, wheels, drives anywhere',
            'Diesel engine, wheels, drives anywhere'
        ],
        'Stacking Height Capability': [
            '1-over-6 (6 containers high, 1 suspended = 7 total)',
            '1-over-7 or 1-over-8 (8-9 containers total)',
            '1-over-9 to 1-over-11 (10-12 containers total)',
            '4-5 containers high maximum',
            '3-4 containers high (straddles bottom container)'
        ],
        'Productivity (Moves/Hour)': [
            '15-25 moves/hour (skilled operator)',
            '20-30 moves/hour (faster due to electric drive)',
            '25-35 moves/hour (consistent, optimized routing)',
            '8-12 moves/hour',
            '10-15 moves/hour'
        ],
        'Operational Flexibility': [
            'High—can relocate to different blocks as needed',
            'Low—fixed to assigned rail block, cannot move between blocks',
            'Low—fixed to rail block, requires manual intervention to relocate',
            'Very high—goes anywhere, multi-purpose (yard + empty depot)',
            'Very high—combined transport + stacking function'
        ],
        'Labor Requirements': [
            '1 operator per RTG (plus maintenance staff)',
            '1 operator per RMG',
            'Zero operators (remote monitoring only, 1 supervisor per 4-6 cranes)',
            '1 operator per reach stacker',
            '1 operator per straddle carrier'
        ],
        'Capital Cost': [
            'US&#36;2-3 million per RTG',
            'US&#36;3-5 million per RMG (includes rail infrastructure)',
            'US&#36;5-8 million per ARMG + automation systems',
            'US&#36;300-500K per reach stacker',
            'US&#36;600K-1M per straddle carrier'
        ],
        'Operating Costs (Annual)': [
            'US&#36;150-250K (diesel fuel, maintenance, operator)',
            'US&#36;120-200K (electricity cheaper than diesel, maintenance, operator)',
            'US&#36;80-150K (electricity, maintenance, no operator wage)',
            'US&#36;80-120K per unit',
            'US&#36;100-150K per unit'
        ],
        'Best Use Case': [
            'Flexible terminals, growing operations, need to adjust yard configuration',
            'High-volume terminals, fixed layout, dense stacking needed',
            'Fully automated terminals (Tuas, Rotterdam Maasvlakte), 24/7 operations',
            'Empty container depots, low-volume operations, supplemental equipment',
            'Small-medium terminals, transshipment focus, combined transport/stacking'
        ],
        'Advantages': [
            'Relocatable, no rail infrastructure needed, simpler operations',
            'Dense stacking (8-9 high), lower operating cost (electric), faster',
            'No operators (huge labor savings), 24/7 consistent performance, 10-12 high stacking',
            'Most flexible, multi-purpose, low capital cost',
            'Combined transport + stacking, no separate horizontal transport needed'
        ],
        'Disadvantages': [
            'Diesel emissions, higher fuel costs, limited stacking (6 high)',
            'Fixed position (expensive to relocate), requires rail investment',
            'Very high capital cost, complex automation, inflexible (hard to modify)',
            'Low productivity, limited stacking height, high operating cost per move',
            'Limited stacking height, higher capital cost than reach stackers'
        ]
    })
    
    st.dataframe(yard_equipment_comparison, width='stretch', hide_index=True)
    
    st.markdown("""
    **RTG vs RMG vs ARMG: The Strategic Choice**
    
    Terminals face a fundamental strategic decision when selecting yard equipment. Each option represents different 
    trade-offs between flexibility, cost, productivity, and automation level.
    
    **When to Choose RTG (Rubber-Tyred Gantry):**
    
    **Ideal for:**
    - Growing terminals where yard layout may change as volumes increase
    - Terminals needing operational flexibility (seasonal demand variation, different cargo types)
    - Brownfield sites retrofitting existing layouts
    - Terminals without capital for rail infrastructure
    - Medium-volume terminals (500K-2M TEU/year)
    
    **Real-world example**: Many Southeast Asian terminals (Thailand, Vietnam, Indonesia) use RTG fleets because 
    they're growing rapidly and need flexibility to reconfigure yard blocks as demand evolves.
    
    **When to Choose RMG (Rail-Mounted Gantry):**
    
    **Ideal for:**
    - High-volume terminals with stable, predictable operations (2M+ TEU/year)
    - Greenfield developments where rail infrastructure can be built from start
    - Terminals prioritizing dense stacking (land-constrained environments)
    - Operations where environmental concerns favor electric over diesel
    
    **Real-world example**: Singapore's existing PSA terminals (Pasir Panjang, Keppel, Brani) deployed RMG systems 
    in 1990s-2000s for dense stacking on limited land, achieving 1-over-7 and 1-over-8 configurations.
    
    **When to Choose ARMG (Automated RMG):**
    
    **Ideal for:**
    - Fully automated terminal developments (greenfield projects)
    - High-labor-cost environments (Singapore, Europe, North America, Japan)
    - Terminals targeting 24/7 operations without night-shift premiums
    - Long-term strategic investments (20-30 year planning horizon)
    - Terminals with sufficient capital (US&#36;500M-1B+ total automation investment)
    
    **Real-world example**: **Singapore's Tuas Mega Port** deploying ARMG as core technology from Phase 1. Lecture 
    materials note: "It is the main type of yard crane to be deployed at Automated Container Terminal." Tuas will 
    have 200+ ARMGs when fully operational, achieving 1-over-11 stacking (12 containers high total).
    
    **The lecture materials emphasize**: "Multiple ARMGs can be remotely controlled simultaneously"—this is the key 
    advantage. One supervisor can monitor 4-6 automated cranes from a control room, versus needing individual operators 
    in RTG/RMG cab. Over 20-30 year lifespan, labor savings dwarf higher upfront capital costs.
    """)
    
    st.markdown("""
    <div class="success-box">
    <strong>✅ Automation Economics - ARMG vs RMG Example:</strong><br><br>
    <strong>Scenario</strong>: Terminal needs 40 yard cranes to handle 3M TEU/year<br><br>
    <strong>Option A - RMG (Manual):</strong><br>
    • Capital: 40 RMGs @ US&#36;4M = US&#36;160M<br>
    • Labor: 40 operators × 3 shifts × US&#36;60K salary = US&#36;7.2M/year<br>
    • 30-year labor cost: US&#36;216M<br>
    • <strong>Total 30-year cost: US&#36;376M</strong><br><br>
    <strong>Option B - ARMG (Automated):</strong><br>
    • Capital: 40 ARMGs @ US&#36;7M = US&#36;280M + automation systems US&#36;50M = US&#36;330M<br>
    • Labor: 10 supervisors × 3 shifts × US&#36;80K = US&#36;2.4M/year (70% reduction!)<br>
    • 30-year labor cost: US&#36;72M<br>
    • <strong>Total 30-year cost: US&#36;402M</strong><br><br>
    <strong>Analysis</strong>: ARMG costs US&#36;26M more over 30 years BUT delivers: 24/7 consistent performance 
    (no human fatigue), higher productivity (25-35 vs 20-30 moves/hour), 10-12 high stacking vs 8-9 (20-30% more 
    yard capacity), fewer accidents/damage. <strong>The productivity and capacity gains easily justify the 7% cost 
    premium</strong>, especially in land-constrained, high-labor-cost Singapore.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 3: Horizontal Transport - Moving Containers Between Zones
    # ============================================================================
    
    st.markdown('<p class="section-header">Horizontal Transport: Prime Movers vs Automated Guided Vehicles</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Horizontal transport equipment moves containers between quay and yard—the critical link connecting ship-to-shore 
    cranes and yard cranes. The lecture materials emphasize this as a major automation frontier, with AGVs representing 
    the most transformative technology shift in terminal operations.
    """)
    
    st.markdown('<p class="subsection-header">Prime Movers: Traditional Approach</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **What are Prime Movers?**
    
    Prime Movers (PMs) are specialized terminal tractors that pull chassis or trailers carrying containers. The 
    lecture materials describe them as the conventional horizontal transport solution used at most container terminals 
    globally.
    
    **Specifications:**
    - **Power**: Diesel engine, 250-400 horsepower
    - **Speed**: 15-30 km/h maximum (terminal speed limits)
    - **Capacity**: Pull one 40ft or two 20ft containers on chassis/trailer
    - **Range**: Diesel tank enables full-day operations
    - **Cost**: US&#36;100-150K per unit (significantly cheaper than AGVs)
    
    **Operations:**
    - **Driver controlled**: Human operator navigates using roads, signage
    - **Fixed assignment (traditional)**: 2 PMs dedicated to each quay crane
    - **Pooling strategy (modern)**: Fleet shared dynamically across all cranes (TOS dispatches)
    - **Productivity**: 4-6 cycles/hour (quay→yard round trip)
    
    **Deployment Models:**
    
    **Traditional Fixed Assignment:**
    - Each quay crane assigned 2 dedicated PMs
    - PMs only serve "their" crane (simple coordination)
    - **Problem**: PMs idle when crane busy with different operation or during crane repositioning
    - **Utilization**: 50-60% (significant idle time)
    
    **Modern Pooling Strategy:**
    - Fleet of PMs shared across all quay cranes
    - **TOS dynamically dispatches** PM to whichever crane needs transport next
    - Algorithm optimizes: (1) Which crane gets next PM, (2) Which PM is closest/available
    - **Benefits**: 30-40% reduction in fleet size needed, 70-80% utilization
    - **Challenge**: More complex coordination (requires sophisticated TOS)
    
    **Prime Mover Advantages:**
    - **Low capital cost**: US&#36;100-150K vs US&#36;300-500K for AGVs
    - **Human flexibility**: Drivers adapt to unexpected situations (obstacles, emergencies, route changes)
    - **No infrastructure**: Works on regular roads, no magnetic strips or guidance systems needed
    - **Existing workforce**: Many terminals already have trained PM drivers
    
    **Prime Mover Disadvantages:**
    - **Labor intensive**: Each PM requires driver (plus relief drivers for 24/7 shifts)
    - **Inconsistent productivity**: Human variability—fatigue, skill differences, break requirements
    - **Higher operating costs**: Driver wages (US&#36;40-60K/year) + diesel fuel
    - **Emissions**: Diesel exhaust (local air quality concerns)
    - **Safety**: Human error risks—accidents, container damage, pedestrian hazards
    """)
    
    st.markdown('<p class="subsection-header">Automated Guided Vehicles (AGVs): Modern Automated Approach</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **What are AGVs?**
    
    Automated Guided Vehicles are battery-electric, computer-controlled autonomous vehicles that transport containers 
    without human operators. The lecture materials emphasize: "For automated terminals, automated guided vehicles (AGVs) 
    are individually guided by the AGV Development System"—highlighting that AGVs are the cornerstone of terminal 
    automation.
    
    **Technical Specifications:**
    - **Power**: Battery-electric (lithium-ion or lead-acid batteries)
    - **Guidance**: Magnetic strips buried in pavement + optical sensors + GPS + onboard computers
    - **Speed**: 10-20 km/h (slower than PMs but more consistent)
    - **Capacity**: Carry one 40ft or two 20ft containers on integrated platform
    - **Range**: 4-6 hours on battery, then auto-returns to charging station
    - **Cost**: US&#36;300-500K per AGV + infrastructure (magnetic strips, charging stations, control systems)
    
    **How AGVs Work:**
    
    **Navigation System:**
    1. **Magnetic guidance**: AGVs follow magnetic strips embedded in terminal pavement (primary navigation)
    2. **Optical sensors**: Cameras read painted lines, QR codes for position confirmation
    3. **GPS**: Provides coarse positioning (accuracy ±2-5 meters)
    4. **Onboard computer**: Processes sensor data, calculates optimal route, controls movement
    5. **Central control system**: AGV Development System dispatches vehicles, coordinates traffic, prevents collisions
    
    **Operational Workflow:**
    1. **CITOS dispatches** AGV to specific quay crane when container ready
    2. AGV navigates autonomously from current position to crane
    3. **Positions under crane spreader**, confirms ready via sensors
    4. Crane lowers container onto AGV platform, AGV confirms load secured
    5. AGV navigates to designated yard block (optimal route calculated by system)
    6. **Arrives at yard crane**, positions for container transfer
    7. Yard crane lifts container off AGV
    8. AGV immediately dispatched to next job (bi-directional loading—can carry container both directions)
    9. When battery low (<20%), AGV autonomously returns to charging station
    
    **Key Advantage - Bi-Directional Loading:**
    
    Unlike PMs (often travel empty on return trip), AGVs can efficiently carry containers both directions:
    - **Quay→Yard**: Deliver import container from discharge
    - **Yard→Quay**: On return trip, pick up export container from yard, deliver to crane for loading
    - **Result**: 30-40% fewer vehicles needed vs PM fixed assignment (higher utilization through optimal routing)
    
    **AGV Fleet Sizing:**
    
    **Rule of thumb**: 65-80 AGVs per berth pair (2 berths, 8-10 quay cranes total)
    
    **Example—Tuas Terminal:**
    - Phase 1: 4 berths (2 berth pairs) = 130-160 AGVs
    - Ultimate capacity (16 berths): 520-640 AGVs
    - Each AGV serves multiple cranes dynamically (pooling strategy)
    - System maintains 10-15% spare capacity (for charging rotation, maintenance, peak demand)
    """)
    
    # Prime Mover vs AGV detailed comparison
    pm_agv_detailed = pd.DataFrame({
        'Factor': [
            'Capital Cost per Unit',
            'Infrastructure Required',
            'Annual Operating Cost',
            'Labor Requirements',
            'Productivity (Cycles/Hour)',
            'Utilization Rate',
            'Operating Hours',
            'Consistency',
            'Emissions',
            'Maintenance',
            'Flexibility',
            'Safety',
            'Lifespan',
            'Technology Complexity'
        ],
        'Prime Movers (PM)': [
            'US&#36;100-150K (lower capital investment)',
            'Standard roads, signage, parking areas (minimal)',
            'US&#36;60-100K (fuel US&#36;20-30K + driver US&#36;40-60K + maintenance US&#36;10K)',
            '1 driver per PM × 3 shifts = 3 FTE per PM (labor intensive)',
            '4-6 cycles/hour (driver-dependent)',
            '50-70% (idle time during crane operations, breaks)',
            'Daytime preference (night shift 20-30% wage premium)',
            'Variable (human factors: fatigue, skill differences, experience)',
            'Diesel emissions (NOx, particulates, CO2—local air quality impact)',
            'Diesel engine maintenance (regular oil changes, repairs)',
            'Very high (adapts to any situation, changes, obstacles)',
            'Human error risks (accidents, damage from fatigue/inattention)',
            '10-15 years typical before replacement',
            'Low (conventional vehicle technology)'
        ],
        'Automated Guided Vehicles (AGV)': [
            'US&#36;300-500K + infrastructure US&#36;5-10M total system (higher capital)',
            'Magnetic strips in pavement, charging stations, central control room',
            'US&#36;25-45K (electricity US&#36;15-25K + maintenance US&#36;10-20K, NO driver)',
            'Zero drivers (1 supervisor monitors 20-30 AGVs remotely)',
            '8-12 cycles/hour (optimized routing, bi-directional loading)',
            '75-85% (continuous operations except charging/maintenance)',
            '24/7 (no labor constraints, battery rotation enables continuous operation)',
            'Very high (consistent performance, no fatigue, optimized routing)',
            'Zero local emissions (electric, battery charged from grid)',
            'Battery replacement (3-5 years), electronic systems (more predictable)',
            'Medium (requires programmed routes, magnetic strips, cannot improvise)',
            'Very high (no human operators in danger zones, collision avoidance sensors)',
            '15-20 years (longer than PMs due to electric drivetrain)',
            'High (complex navigation, control systems, fleet coordination)'
        ]
    })
    
    st.dataframe(pm_agv_detailed, width='stretch', hide_index=True)
    
    st.markdown("""
    **AGV Investment Economics: The Compelling Business Case**
    
    Despite 3-5× higher unit costs, AGVs deliver compelling ROI through labor savings and productivity gains:
    
    **Scenario—Medium Terminal (2M TEU/year, 4 berths, 8 quay cranes):**
    
    **Prime Mover Option:**
    - **Fleet size**: 40 PMs @ US&#36;125K = US&#36;5M capital
    - **Drivers**: 40 PMs × 3 shifts × 2 reliefs = 240 drivers × US&#36;50K = **US&#36;12M/year**
    - **Fuel**: US&#36;25K/PM/year × 40 = US&#36;1M/year
    - **Total annual operating cost**: US&#36;13M
    - **20-year total cost**: US&#36;5M capital + US&#36;260M operations = **US&#36;265M**
    
    **AGV Option:**
    - **Fleet size**: 130 AGVs @ US&#36;400K = US&#36;52M + infrastructure US&#36;25M = **US&#36;77M capital**
    - **Supervisors**: 10 supervisors × 3 shifts × US&#36;70K = US&#36;2.1M/year (91% labor reduction!)
    - **Electricity**: US&#36;20K/AGV/year × 130 = US&#36;2.6M/year
    - **Total annual operating cost**: US&#36;4.7M (64% lower than PMs!)
    - **20-year total cost**: US&#36;77M capital + US&#36;94M operations = **US&#36;171M**
    
    **AGV Advantage: US&#36;94M savings over 20 years (35% lower total cost)**
    
    **Plus additional benefits not quantified above:**
    - 30-40% higher productivity (faster vessel turnaround attracts more business)
    - 24/7 operations without night-shift premiums
    - Fewer accidents (reduced insurance, damage, injury costs)
    - Environmental benefits (zero local emissions supports green terminal certifications)
    - Scalability (add AGVs incrementally as volumes grow)
    
    **The lecture materials conclude**: AGVs deliver "70-80% labour reduction, 24/7 operations, and pooling strategy 
    reduces fleet size 30-40%"—making AGVs the clear choice for new automated terminals despite higher upfront costs.
    """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>💡 Why Singapore Tuas Chose Full AGV Automation:</strong><br><br>
    <strong>Labor cost context</strong>: Singapore PM drivers earn US&#36;40-60K/year (higher than regional 
    competitors). Over 30-year Tuas lifespan, PM labor costs would exceed US&#36;500M.<br><br>
    <strong>AGV investment</strong>: ~600 AGVs @ US&#36;400K = US&#36;240M + infrastructure US&#36;50M = US&#36;290M 
    capital. Operating costs US&#36;4M/year vs US&#36;18M/year for PM fleet = US&#36;420M savings over 30 years.<br><br>
    <strong>Strategic advantage</strong>: Tuas automation enables Singapore to maintain cost competitiveness despite 
    high labor costs, while achieving 24/7 consistent productivity that PM-based competitors cannot match. The 
    US&#36;130M net savings funds other terminal innovations (ARMGs, AI-powered CITOS, shore power infrastructure).
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 4: Automation Levels Framework
    # ============================================================================
    
    st.markdown('<p class="section-header">Terminal Automation Levels: From Manual to "Lights-Out"</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Container terminals exist along a spectrum from fully manual operations to completely automated "lights-out" 
    facilities operating 24/7 with minimal human intervention. The industry uses a four-level framework to classify 
    automation sophistication.
    """)
    
    st.markdown('<p class="subsection-header">The Four Automation Levels</p>', unsafe_allow_html=True)
    
    # Automation levels framework
    automation_framework = pd.DataFrame({
        'Automation Level': [
            'Level 1: Conventional Terminal',
            'Level 2: Semi-Automated Terminal',
            'Level 3: Highly Automated Terminal',
            'Level 4: Fully Automated Terminal'
        ],
        'Quay Operations': [
            'Manual quay cranes with human operators in cab',
            'Quay cranes with computer-assisted controls (anti-sway systems)',
            'Semi-automated crane positioning, operator supervises',
            'Fully automated ship-to-shore cranes (ASC—Auto Stacking Crane)'
        ],
        'Horizontal Transport': [
            'Prime Movers with human drivers',
            'Prime Movers with GPS tracking, dispatch optimization',
            'Automated Guided Vehicles (AGV fleet)',
            'AGVs or ALVs (Automated Lift Vehicles)'
        ],
        'Yard Operations': [
            'RTG with human operators in crane cab',
            'RTG with remote operation from control room',
            'RMG semi-automated (remote supervised)',
            'ARMG (Automated RMG) with zero operators'
        ],
        'Gate Operations': [
            'Manual documentation check, clerk verification',
            'Partial OCR (Optical Character Recognition), manual verification',
            'Automated OCR + system validation, minimal manual intervention',
            'Fully automated gate + TAS (Truck Appointment System)'
        ],
        'Labor Reduction': [
            'Baseline (100%)',
            '20-30% reduction vs Level 1',
            '50-60% reduction vs Level 1',
            '70-80% reduction vs Level 1'
        ],
        'Typical Capital Cost': [
            'US&#36;150-250M per berth (baseline)',
            'US&#36;200-300M per berth (+20-30%)',
            'US&#36;350-500M per berth (+100-150%)',
            'US&#36;500M-1B per berth (+200-300%)'
        ],
        'Global Examples': [
            'Most ports worldwide (majority of capacity)',
            'Many modern terminals in Asia, Europe, US West Coast',
            'Singapore PSA (some terminals), Hamburg CTB, Los Angeles LBCT',
            'Rotterdam Maasvlakte II, Hamburg CTA, Singapore Tuas, Qingdao, Long Beach LBCT'
        ]
    })
    
    st.dataframe(automation_framework, width='stretch', hide_index=True)
    
    st.markdown("""
    **Level 1: Conventional Terminal (Baseline)**
    
    **Characteristics:**
    - All equipment operated by humans (quay crane operators, PM drivers, yard crane operators, gate clerks)
    - Basic TOS for planning but manual execution
    - Labor-intensive operations requiring large workforce
    - Equipment utilization depends heavily on operator skill
    
    **When this makes sense:**
    - Low labor cost countries (Southeast Asia, Africa, Latin America)
    - Smaller terminals (<500K TEU/year)
    - Existing brownfield sites with established operations
    - Limited capital for automation investment
    
    **Operational reality**: Most global container terminal capacity operates at Level 1. While not cutting-edge, 
    well-run Level 1 terminals can achieve respectable productivity (25-30 GMPH) through skilled workforce and 
    efficient processes.
    
    **Level 2: Semi-Automated Terminal (Productivity Enhancement)**
    
    **Characteristics:**
    - Technology assists human operators rather than replacing them
    - Remote operation rooms (yard crane operators leave cab, control from office)
    - GPS tracking enables better fleet management
    - Partial gate automation (OCR speeds processing)
    
    **Key technologies:**
    - Anti-sway systems on quay cranes (faster, safer operations)
    - Remote-controlled RTGs (operators more comfortable, can supervise multiple cranes)
    - Automated gate OCR (10× faster than manual, eliminates data entry errors)
    - Real-time equipment tracking (TOS knows exact position of all equipment)
    
    **Benefits**: 20-30% labor reduction plus significant productivity gains without massive capital investment. 
    This is the "sweet spot" for many terminals—meaningful improvements at manageable cost.
    
    **When this makes sense:**
    - Terminals modernizing existing operations
    - Growing terminals investing incrementally
    - Balance of cost and performance
    
    **Level 3: Highly Automated Terminal (Selective Automation)**
    
    **Characteristics:**
    - AGV fleet eliminates PM drivers (major labor savings)
    - Some yard areas use ARMG (automated), others still RMG/RTG (manual)
    - Automated gates handle routine transactions
    - Significant reduction in terminal workforce
    
    **Implementation approach**: Automate highest-volume, most-repetitive operations first. For example, automate 
    main transshipment yard with ARMGs while keeping import/export yard manual (more variable workflows).
    
    **Benefits**: 50-60% labor reduction, 24/7 yard operations in automated areas, improved consistency.
    
    **Challenges**: Operating two systems simultaneously (automated + manual) creates complexity. Need staff skilled 
    in both traditional operations and automation systems management.
    
    **When this makes sense:**
    - Phased automation journey (step toward Level 4)
    - High-volume terminals in high-labor-cost regions
    - Terminals with sufficient capital (US&#36;350-500M per berth)
    
    **Level 4: Fully Automated Terminal ("Lights-Out" Operations)**
    
    **Characteristics:**
    - No human operators in operational zones (hence "lights-out"—don't need lighting for operators)
    - Automated quay cranes, AGV fleet, ARMG yard cranes, automated gates
    - Humans monitor from central control room, intervene only for exceptions
    - Truly 24/7 operations without workforce constraints
    
    **What "fully automated" means:**
    - Quay cranes automatically position spreader, pick containers from vessel without operator input
    - AGVs navigate autonomously, coordinate with cranes automatically
    - ARMGs stack/retrieve containers without operators
    - Gates process trucks without human clerks (OCR + system validates, traffic lights direct)
    - **Only human intervention**: Exception handling (equipment failures, damaged containers, non-standard situations)
    
    **The reality of "fully automated":** Even Level 4 terminals aren't completely unmanned. Still need:
    - Central control room staff (monitor systems, handle exceptions)
    - Maintenance teams (equipment repairs, preventive maintenance)
    - Management and planning staff
    - Security personnel
    - Gate guards for non-routine situations
    
    **Labor reduction**: 70-80% vs Level 1, but not 100%. Example: Conventional terminal with 1,000 employees → 
    Automated terminal with 200-300 employees (supervisors, maintenance, management, security).
    
    **Benefits:**
    - Massive long-term labor cost savings (justify high upfront investment)
    - Consistent 24/7 productivity (no fatigue, no strikes, no shift changes)
    - Higher yard density (ARMG can stack 10-12 high vs 6-7 for manual)
    - Enhanced safety (humans not in operational danger zones)
    - Environmental (electric AGVs, ARMGs—zero local emissions)
    - Predictable performance (easier capacity planning)
    
    **Challenges:**
    - Enormous capital investment (US&#36;500M-1B per berth, US&#36;2-4B for 4-berth terminal)
    - 5-7 year payback period minimum (labor savings accrue slowly)
    - Technology risk (complex systems, software bugs, integration issues)
    - Workforce transition (train existing workers or hire new tech-skilled staff?)
    - Inflexibility (automated systems harder to modify than manual operations)
    
    **Global Examples:**
    
    **Rotterdam Maasvlakte II (APM Terminals):** Europe's first fully automated terminal, operational 2015
    **Hamburg CTA (Container Terminal Altenwerder):** Pioneering automated terminal since 2002
    **Singapore Tuas Mega Port (PSA):** World's largest automated terminal project, Phase 1 operational 2026-2027
    **Qingdao Port (China):** Fully automated terminal showcasing Chinese automation technology
    **Long Beach LBCT (US):** Largest automated terminal in North America
    
    **When Level 4 makes sense:**
    - Greenfield developments (design automation from start, avoid retrofit costs)
    - High labor cost regions (Singapore, Europe, North America, Japan)
    - Long-term strategic investments (20-30+ year planning horizon)
    - Sufficient scale (2M+ TEU/year to justify investment)
    - Government support (strategic importance recognized)
    """)
    
    st.markdown("""
    <div class="success-box">
    <strong>✅ Automation Decision Framework - Key Questions:</strong><br><br>
    <strong>1. Labor Cost vs Capital Cost</strong>: In high-wage countries (US&#36;50K+ annual labor), automation 
    pays back faster. In low-wage countries (US&#36;15K labor), conventional makes more sense.<br><br>
    <strong>2. Time Horizon</strong>: Automation ROI requires 5-10 year payback. Short-term investments favor 
    conventional; long-term strategic investments favor automation.<br><br>
    <strong>3. Scale</strong>: Automation economics improve with scale. <1M TEU/year: difficult to justify. 
    2M+ TEU/year: compelling case. 5M+ TEU/year: clear winner.<br><br>
    <strong>4. Greenfield vs Brownfield</strong>: New terminals can design for automation (lower cost). Existing 
    terminals face expensive retrofits (often not viable).<br><br>
    <strong>5. Strategic Importance</strong>: National champions (Singapore, Rotterdam, Hamburg) get government 
    backing for automation—strategic asset to maintain hub status regardless of pure economics.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 5: PSA CITOS - Terminal Operating System
    # ============================================================================
    
    st.markdown('<p class="section-header">PSA CITOS®: The Digital Brain of Terminal Operations</p>', unsafe_allow_html=True)
    
    st.markdown("""
    CITOS (Computer Integrated Terminal Operation System) is PSA's proprietary Terminal Operating System—the 
    sophisticated software platform that plans, coordinates, and monitors all terminal activities. The lecture 
    materials emphasize: "CITOS®: An Enterprise Resource Planning system that plans and integrates every asset from 
    PMs/AGVs, [yard cranes] and quay cranes to containers and drivers."
    
    This section explores why CITOS represents a critical competitive advantage for PSA, and how advanced TOS 
    capabilities enable world-class terminal performance.
    """)
    
    st.markdown('<p class="subsection-header">CITOS Development History and Strategic Rationale</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Development Timeline:**
    
    **1980s - Origins:**
    - PSA began developing CITOS in-house to manage Singapore's growing container volumes
    - Initial system: basic berth planning, vessel scheduling, container tracking
    - Goal: Replace manual paper-based planning with computer-assisted operations
    
    **1990s - Expansion:**
    - Added sophisticated yard planning, equipment scheduling modules
    - Integration with PORTNET (Singapore's port community system)
    - Deployed across Singapore terminals (Tanjong Pagar, Keppel, Brani)
    
    **2000s - Global Deployment:**
    - CITOS exported to PSA international terminals (Belgium, Italy, Korea, China)
    - Evolution toward real-time optimization algorithms
    - Integration with automated equipment (AGVs, ARMGs)
    
    **2010s - AI/ML Integration:**
    - Machine learning for predictive analytics (vessel delay forecasting, berth planning optimization)
    - Cloud-based architecture for scalability
    - Mobile applications for supervisors, operators
    
    **2020s - Next Generation:**
    - Advanced AI for autonomous decision-making
    - Digital twin integration (virtual terminal model)
    - Tuas deployment with full automation capabilities
    - Currently: 40+ years of continuous evolution
    
    **Why PSA Developed CITOS In-House (Rather Than Buying Commercial TOS):**
    
    This strategic decision created lasting competitive advantages:
    
    **1. Customization to PSA's Operational Philosophy:**
    - PSA could embed its specific operational approaches, best practices into software
    - No compromises required to fit generic vendor product
    - Continuous refinement based on actual Singapore operations
    
    **2. Competitive Differentiation:**
    - Proprietary system competitors cannot replicate
    - Unique algorithms optimizing PSA-specific workflows
    - IP protection of operational know-how
    
    **3. Rapid Innovation:**
    - No vendor dependency—PSA controls development roadmap
    - Can implement new features immediately when operational needs identified
    - Fast response to industry changes (e.g., mega vessel handling, alliance restructuring)
    
    **4. Cost Savings:**
    - No ongoing vendor licensing fees (many commercial TOS charge annual fees based on throughput)
    - Over 40 years, savings enormous compared to commercial products
    - One-time development cost amortized across decades and multiple terminals globally
    
    **5. Global Deployment:**
    - Standard platform across all PSA terminals (Singapore, Europe, Asia, Americas)
    - Enables best practice sharing, consistent operations globally
    - Staff can transfer between PSA terminals using familiar system
    
    **6. Data Ownership and Analytics:**
    - Complete control of operational data (not shared with vendor or competitors)
    - Decades of data improve AI/ML algorithms
    - Insights from Singapore operations deployed globally
    """)
    
    st.markdown('<p class="subsection-header">CITOS Core Modules and Architecture</p>', unsafe_allow_html=True)
    
    # CITOS modules breakdown
    citos_modules = pd.DataFrame({
        'CITOS Module': [
            'Berth Planning Module',
            'Vessel Planning Module',
            'Yard Planning & Management',
            'Resource Planning Module',
            'Equipment Control & Dispatch',
            'PM/AGV Deployment System',
            'Gate Operating System (GOS)',
            'EDI & Integration Hub',
            'Reporting & Analytics Platform',
            'Mobile Operations Suite'
        ],
        'Primary Functions': [
            'Vessel-to-berth allocation, berth window optimization, BOA maximization, pilot coordination',
            'Stowage planning, discharge/load lists, bay plan generation, vessel stability calculations',
            'Container location tracking, storage assignment, yard utilization optimization, re-handle minimization',
            'Labor shift scheduling, equipment allocation, maintenance windows, skill matching',
            'Real-time crane assignment, work sequence optimization, productivity monitoring, exception alerts',
            'Dynamic PM/AGV dispatching, route optimization, battery management, traffic coordination, collision avoidance',
            'Truck appointment scheduling, OCR integration, automated authorization, lane assignment, throughput optimization',
            'PORTNET integration (Singapore maritime single window), shipping line EDI, customs TradeNet, rail operators',
            'Real-time KPI dashboards, productivity reports, trend analysis, predictive analytics, bottleneck identification',
            'Supervisor tablets, crane operator interfaces, maintenance mobile apps, field reporting'
        ],
        'Key Algorithms': [
            'Constraint satisfaction (berth length, draft, crane availability), genetic algorithms for optimal sequence',
            'Weight distribution algorithms, stowage constraints checking, destination sequencing, equipment compatibility',
            'Clustering (group similar containers), 3D bin packing, retrieval sequence prediction, hot/cold storage assignment',
            'Workforce optimization, equipment utilization balancing, preventive maintenance scheduling',
            'Dynamic task assignment, multi-crane coordination, interference avoidance, workload leveling',
            'Shortest path routing, task prioritization, fleet size optimization, energy management, deadlock prevention',
            'Queue management, slot allocation algorithms, peak-period load balancing, priority handling',
            'Message queuing, data transformation, error handling, real-time synchronization, audit trails',
            'OLAP cubes, time-series forecasting, anomaly detection, comparative benchmarking, simulation',
            'Responsive UI, offline capability, role-based access, location-aware features, push notifications'
        ],
        'Data Inputs': [
            'Vessel arrival notifications, ETA updates, vessel specifications, expected cargo volumes',
            'Cargo manifests, container types/weights, dangerous goods, special requirements (reefers, OOG)',
            'Container discharge/load lists, truck arrival notifications, customs clearances, container inventory',
            'Staff availability, equipment status, maintenance schedules, historical productivity patterns',
            'Equipment position sensors, crane work progress, container move completions, equipment health monitors',
            'AGV position (GPS + magnetic guidance), battery levels, job queue, container ready notifications',
            'Truck license plates (OCR), container numbers, booking references, customs documentation',
            'External system messages (PORTNET, shipping lines, customs, trucking companies, rail operators)',
            'Transaction logs, equipment telemetry, operational events, performance metrics, historical data warehouse',
            'User location, equipment assignments, task status, alerts, forms, checklists'
        ],
        'Typical Response Time': [
            'Seconds to minutes (real-time updates as vessel status changes)',
            'Minutes to hours (detailed planning as vessel ETA approaches within 24-48 hours)',
            'Real-time (milliseconds for location queries, seconds for optimization)',
            'Hours to days (shift planning, maintenance windows scheduled in advance)',
            'Real-time (milliseconds for dispatch decisions, crane operator instruction updates)',
            'Real-time (milliseconds for AGV routing, continuous position updates)',
            'Seconds (instant OCR processing, 2-3 second authorization validation)',
            'Real-time (asynchronous messaging, event-driven, typically <1 second message processing)',
            'Real-time dashboards (1-5 second refresh), batch reports (hourly/daily/weekly)',
            'Real-time (instant UI updates, <1 second for queries and transactions)'
        ]
    })
    
    st.dataframe(citos_modules, width='stretch', hide_index=True)
    
    st.markdown("""
    **CITOS Advanced Features: AI/ML and Real-Time Optimization**
    
    Modern CITOS incorporates cutting-edge technologies that elevate it beyond traditional TOS platforms:
    
    **Artificial Intelligence and Machine Learning:**
    
    **Predictive Berth Planning:**
    - ML models forecast vessel arrival delays based on weather, port congestion, vessel history
    - Accuracy: ±30 minutes for vessels within 24 hours of ETA (enables optimal berth preparation)
    - Algorithm continuously improves using decades of PSA arrival data
    
    **Yard Location Optimization:**
    - Learns from historical patterns which container types tend to dwell long vs short
    - Automatically assigns fast-moving cargo to easily accessible locations
    - Predicts truck pickup patterns, pre-positions containers accordingly
    
    **Equipment Maintenance Prediction:**
    - IoT sensors on cranes, AGVs, ARMGs feed data to ML models
    - Predicts equipment failures before they occur (predictive maintenance)
    - Schedules maintenance during low-demand periods to minimize disruption
    - Reduces unplanned downtime 30-40%
    
    **Real-Time Optimization:**
    
    **Dynamic Re-Planning:**
    - When disruptions occur (equipment failure, vessel delay, unexpected cargo), CITOS instantly recalculates plans
    - Reassigns equipment, adjusts schedules, notifies affected stakeholders
    - Resilient operations—system adapts without human intervention
    
    **What-If Scenario Simulation:**
    - Planners can test "what if?" scenarios before execution
    - Example: "What if vessel arrives 2 hours early? Will we have berth available? Enough cranes ready?"
    - Enables better decision-making under uncertainty
    
    **Constraint Satisfaction:**
    - Balances multiple competing objectives simultaneously
    - Example: Maximize berth utilization WHILE maintaining >90% BOA WHILE balancing crane workload WHILE 
      minimizing vessel waiting time
    - NP-hard optimization problem—CITOS uses heuristics to find near-optimal solutions in seconds
    
    **Operational Simulation Integration:**
    
    **Digital Twin Capability:**
    - CITOS maintains real-time virtual model of entire terminal
    - Simulates operations before execution, identifies bottlenecks
    - Training environment for operators without disrupting actual operations
    
    **Mobile and Cloud Capabilities:**
    
    **Field Operations:**
    - Supervisors use tablets to monitor operations, override automated decisions when needed
    - Crane operators see next container assignment on in-cab displays
    - Maintenance teams use mobile apps to log repairs, access equipment history
    
    **Cloud Architecture:**
    - Scalable infrastructure supports growing operations
    - Disaster recovery (backup systems, redundancy)
    - Remote monitoring enables PSA HQ to oversee global terminal network
    
    **API Integration:**
    - Shipping lines integrate directly with CITOS via APIs
    - Real-time container tracking, booking confirmations, vessel schedules
    - Reduces manual coordination, improves service quality
    """)
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 CITOS Competitive Advantage - Why It Matters:</strong><br><br>
    CITOS enables PSA to consistently achieve <strong>world-class performance benchmarks</strong>:<br><br>
    <strong>1. Berth On Arrival >90%</strong>: Vessels berth immediately without anchorage wait (industry average: 
    70-80%). Optimized berth planning ensures slot availability when vessels arrive.<br><br>
    <strong>2. Crane Productivity 35-40 GMPH</strong>: Gross Moves Per Hour per crane (industry average: 25-30 GMPH). 
    Optimized crane work sequences, perfect PM/AGV coordination, minimal waiting time.<br><br>
    <strong>3. Gate Transaction <3 minutes</strong>: Average truck processing time (industry average: 5-8 minutes). 
    Automated OCR + CITOS validation eliminates manual documentation.<br><br>
    <strong>4. Vessel Turnaround <24 hours</strong>: For 2,000-move mega vessels (industry average: 30-36 hours). 
    Optimized operations across all modules enable fast, reliable service.<br><br>
    <strong>These benchmarks are not accidental</strong>—they result from 40+ years of CITOS development, continuous 
    refinement using operational data from world's busiest port, and PSA's unwavering commitment to operational 
    excellence. Competitors using commercial TOS products struggle to match this performance.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 6: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways: Equipment, Automation & CITOS</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Quay Cranes (Ship-to-Shore):**
        - H-shaped design now standard (vs A-shaped legacy cranes)
        - Super post-Panamax: 65-80m outreach, US&#36;13-18M each
        - Double trolley + triple spreader = 35-40 GMPH productivity
        - Critical investment: 8-12 cranes @ US&#36;15M = US&#36;120-180M per terminal
        
        **Yard Equipment Evolution:**
        - RTG: Flexible, US&#36;2-3M, 1-over-6 stacking
        - RMG: Electric, US&#36;3-5M, 1-over-8 stacking
        - ARMG: Automated, US&#36;5-8M, 1-over-11 stacking, zero operators
        - Automation enables 70-80% labor reduction, 24/7 operations
        
        **Horizontal Transport:**
        - Prime Movers: US&#36;100-150K, human drivers, flexible
        - AGVs: US&#36;300-500K, automated, 75-85% utilization
        - AGV economics: Higher capital but 64% lower operating costs
        - Tuas: 600 AGVs enabling US&#36;420M labor savings over 30 years
        """)
    
    with col2:
        st.markdown("""
        **Automation Levels Framework:**
        - Level 1 (Conventional): Manual operations, 100% labor baseline
        - Level 2 (Semi-Auto): Remote operation, 20-30% labor reduction
        - Level 3 (Highly Auto): AGVs + some ARMG, 50-60% reduction
        - Level 4 (Fully Auto): Complete automation, 70-80% reduction
        - Capital: US&#36;150M (L1) → US&#36;500M-1B (L4) per berth
        
        **PSA CITOS System:**
        - Proprietary TOS, 40+ years continuous development
        - 10 core modules: Berth, Vessel, Yard, Resource, Equipment, PM/AGV, Gate, EDI, Analytics, Mobile
        - AI/ML: Predictive berth planning, yard optimization, maintenance forecasting
        - Competitive advantage: In-house control, rapid innovation, global deployment
        - Enables >90% BOA, 35-40 GMPH, <24h turnaround
        
        **Strategic Investment Decision:**
        - Automation ROI: 5-10 year payback in high-wage countries
        - Greenfield preferred (retrofit expensive)
        - Scale matters: 2M+ TEU/year justifies automation
        - Government support critical for strategic hubs
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Modern container terminals deploy sophisticated equipment ranging from <strong>US&#36;10-18M 
    quay cranes</strong> (H-shaped, double trolley, 65-80m outreach enabling 35-40 GMPH) through <strong>ARMG yard systems</strong> 
    (automated rail-mounted gantries achieving 1-over-11 stacking with zero operators) to <strong>AGV fleets</strong> (300-500 
    autonomous vehicles per major terminal delivering 70-80% labor reduction). Terminal <strong>automation levels</strong> range from 
    conventional manual (Level 1 baseline) through semi-automated (Level 2: 20-30% labor savings) and highly automated (Level 3: 
    50-60% savings) to fully automated "lights-out" facilities (Level 4: 70-80% savings, 24/7 operations)—with capital costs 
    escalating from US&#36;150M to US&#36;500M-1B per berth but delivering compelling ROI through labor savings and productivity gains 
    in high-wage environments. <strong>PSA's CITOS</strong> Terminal Operating System—developed in-house over 40+ years and deployed 
    globally—coordinates all equipment and operations through 10 integrated modules using AI/ML for predictive analytics and 
    real-time optimization, enabling world-class performance benchmarks (>90% BOA, 35-40 GMPH, <24h turnaround) that create 
    sustainable competitive advantage. <strong>Singapore's Tuas Mega Port</strong> exemplifies this integration: 200+ ARMGs, 600 AGVs, 
    latest super post-Panamax cranes, and advanced CITOS—a US&#36;20 billion investment in operational excellence that positions 
    Singapore to maintain hub leadership through 2050 despite intensifying regional competition.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** Continue exploring maritime operations and industry dynamics to complete your comprehensive 
    understanding of the container shipping ecosystem and terminal operations that enable global trade.
    """)
