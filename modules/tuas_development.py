import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">🏗️ Tuas Mega Port: Singapore\'s S&#36;20 Billion Bet</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Master Singapore's strategic rationale for the S&#36;20+ billion Tuas Mega Port investment—the world's largest 
    automated container terminal project—understand the five strategic drivers (consolidation efficiency, mega vessel 
    accommodation, pre-emptive competition response, greenfield automation opportunity, climate resilience), explore 
    the comprehensive design features (65M TEU capacity, 1,337 hectares, 26.3 km continuous quay, 1,000+ AGVs, 200+ 
    ARMGs), analyse the four-phase development timeline (2013-2040), comprehend implementation challenges (70-80% labor 
    reduction, workforce transformation, transport infrastructure, cybersecurity), and evaluate whether this massive 
    investment will be sufficient to maintain Singapore's hub dominance through scenario analysis.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: The Tuas Announcement and Strategic Context
    # ============================================================================
    
    st.markdown('<p class="section-header">The Tuas Mega Port Announcement: October 2012</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Tuas Mega Port was first announced by Singapore's Transport Minister Lui Tuck Yew in October 2012**, marking 
    the beginning of Singapore's most ambitious infrastructure project. The lecture materials capture the strategic 
    rationale articulated at that historic announcement.
    
    **Minister Lui's Key Statements (October 2012):**
    
    The lecture materials quote Transport Minister Lui Tuck Yew explaining the strategic imperatives:
    
    **On Land Efficiency:**
    
    *"Consolidation at Tuas will also free up prime land, which our City Terminals and Pasir Panjang Terminals are 
    currently occupying, for re-development."*
    
    This reveals a dual benefit: Tuas isn't just about port capacity—it's also about optimal land use. Singapore's 
    existing terminals (Tanjong Pagar, Keppel, Brani, Pasir Panjang) occupy prime waterfront land near the Central 
    Business District. Consolidating all operations at Tuas frees up approximately 1,000 hectares of valuable urban 
    land for residential, commercial, and recreational redevelopment.
    
    **On Efficiency and Productivity:**
    
    *"Given our land and manpower constraints, we have to strive for even greater efficiency and productivity."*
    
    This statement captures Singapore's fundamental challenge: As a small city-state (only 734 km² total area) with 
    limited workforce (5.8 million population), Singapore cannot compete through scale or low costs. The only path 
    forward is **operational excellence through technology and efficiency**—which requires greenfield investment like 
    Tuas to implement cutting-edge automation from the ground up.
    
    **On Technology and Innovation:**
    
    The lecture materials note that **"MPA and PSA had jointly launched the Port Technology R&D Program in April 2011"**—
    18 months *before* the Tuas announcement. This program was "studying automated container port systems, optimization 
    techniques and technologies, and green port technologies, among others."
    
    Minister Lui stated: *"We will be able to deploy some of the outcomes of these projects at Tuas Port."*
    
    This reveals Singapore's methodical approach: Research and develop automation technologies first (2011-2012), 
    *then* announce the mega port where these innovations will be deployed. Tuas wasn't a spontaneous decision—it 
    was the culmination of years of strategic planning and technology development.
    """)
    
    # Key metrics display
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Investment", "S&#36;20B+", help="Total capital investment across all phases")
    with col2:
        st.metric("Ultimate Capacity", "65M TEU", help="Annual capacity when fully completed (~2040)")
    with col3:
        st.metric("Land Area", "1,337 ha", help="Equivalent to ~2,000 football fields")
    with col4:
        st.metric("Quay Length", "26.3 km", help="Longest continuous berth in the world")
    
    st.markdown("""
    <div class="insight-box">
    <strong>💡 Understanding the Scale:</strong><br><br>
    <strong>S&#36;20+ billion</strong> = Singapore's largest infrastructure project ever, exceeding even Changi Airport 
    Terminal 5 (S&#36;13B) and the entire Circle Line MRT (S&#36;6B). To put in perspective: S&#36;20B could build 
    ~40 hospitals or ~200 schools.<br><br>
    <strong>65M TEU capacity</strong> = Nearly 2× Singapore's 2024 throughput (41.12M TEU), enough to handle ~10% 
    of global container trade if concentrated at one location.<br><br>
    <strong>1,337 hectares</strong> = Larger than Manhattan's Central Park (341 ha) or Singapore's Sentosa island 
    (500 ha). This represents ~1.8% of Singapore's entire land area dedicated to a single port.<br><br>
    <strong>26.3 km quay</strong> = Could berth 60+ mega vessels simultaneously end-to-end. Equivalent to driving 
    from Singapore's east coast to west coast.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 2: The Five Strategic Drivers for Tuas Investment
    # ============================================================================
    
    st.markdown('<p class="section-header">Why Build Tuas? The Five Strategic Drivers</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Singapore's decision to invest S&#36;20+ billion in Tuas is driven by five interconnected strategic imperatives. 
    Understanding these drivers reveals why Singapore views Tuas not as optional but as **existentially necessary** 
    for maintaining hub competitiveness.
    """)
    
    st.markdown('<p class="subsection-header">Driver #1: Consolidation for Operational Efficiency</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Current Fragmentation Problem:**
    
    Singapore's container operations are currently spread across **four separate terminal locations**:
    
    **City Terminals (Tanjong Pagar, Keppel, Brani):**
    - Located in prime urban areas near CBD
    - Older infrastructure (developed 1970s-1990s)
    - Space constraints limit expansion
    - Total capacity: ~15M TEU combined
    
    **Pasir Panjang Terminal:**
    - Southwestern Singapore
    - More modern (developed 1990s-2000s)
    - Better infrastructure than City Terminals
    - Total capacity: ~25M TEU
    
    **The Inefficiency Costs:**
    
    **Inter-Terminal Vessel Calls:**
    - Some mega vessels must call at multiple terminals to discharge/load complete cargo
    - Extra sailing time between terminals wastes 2-4 hours per vessel
    - Additional pilotage, tugboat usage increases operational costs
    - Coordination complexity—different terminals, different systems, different schedules
    
    **Inter-Terminal Container Transfers:**
    - Transshipment containers sometimes need transfer between terminals
    - Requires trucks or barges to move containers across Singapore
    - Adds 4-8 hours to transshipment dwell time (undermines "tight connection" advantage)
    - Extra handling increases damage risk, operational costs
    
    **Resource Optimization Challenges:**
    - Cannot share cranes, yard equipment, AGVs across terminals
    - Workforce scheduling more complex (can't dynamically shift labor to where needed)
    - Equipment utilization suffers (one terminal overloaded, another underutilized)
    - Redundant administrative functions (each terminal needs full support staff)
    
    **The Tuas Consolidation Solution:**
    
    **Single Mega Port Benefits:**
    
    **Operational Integration:**
    - **26.3 km continuous quay wall**: Vessels berth anywhere based on optimal positioning
    - **No inter-terminal calls**: All cargo discharged/loaded at single location
    - **No inter-terminal transfers**: Transshipment containers never leave terminal
    - **Unified operations**: Single CITOS system optimizes across entire port
    
    **Resource Sharing and Optimization:**
    - **Equipment mobility**: Cranes, AGVs, ARMGs can be deployed wherever needed dynamically
    - **Workforce flexibility**: Operators move between berths based on demand (no terminal boundaries)
    - **Integrated yard**: Optimal storage location selection across entire 1,337 hectare yard
    - **Centralized functions**: Single administration, maintenance, control eliminates redundancy
    
    **Expected Efficiency Gains:**
    
    **Quantified Benefits:**
    - **20-30% improvement in operational efficiency** vs fragmented operations
    - **Vessel turnaround time**: Target <24 hours for mega vessels (vs 30-36 hours at fragmented terminals)
    - **Cost per TEU**: 15-20% reduction through economies of scale
    - **Equipment utilization**: 80-85% vs 65-75% at fragmented terminals (higher asset productivity)
    
    **The lecture materials emphasized**: "Consolidation at Tuas will free up prime land" for redevelopment. This 
    creates a **win-win**: More efficient port operations *plus* valuable urban land released for housing, offices, 
    parks. The economic value of freed land (estimated S&#36;30-50 billion over decades) partially offsets Tuas 
    investment costs.
    """)
    
    st.markdown('<p class="subsection-header">Driver #2: Accommodate Mega Vessels and Ultra Large Container Vessels (ULCV)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Mega Vessel Challenge:**
    
    Container vessels have grown from 8,000 TEU (2000s) to 24,000 TEU (today), with potential for 30,000+ TEU vessels. 
    These Ultra Large Container Vessels (ULCVs) impose demanding infrastructure requirements that many existing ports 
    cannot meet.
    
    **ULCV Infrastructure Requirements:**
    
    **Physical Specifications:**
    - **Length (LOA)**: 400 meters (longer than four football fields)
    - **Width (Beam)**: 60-62 meters (spans 24 containers wide)
    - **Draft**: 16-18 meters when fully laden (requires deep berths and channel)
    - **Height**: 70+ meters above water (clearance under bridges, overhead power lines)
    
    **Operational Requirements:**
    - **Deep berth**: Minimum 16-18 meters water depth (many existing ports only 12-14m)
    - **Super post-Panamax cranes**: 65-80 meter outreach to reach 24 containers across
    - **Crane intensity**: 8-12 quay cranes working simultaneously for fast turnaround
    - **Fast productivity**: 35-40 GMPH per crane to complete 3,000-4,000 moves in 24-36 hours
    - **Massive yard capacity**: Space to temporarily store 2,000-3,000 containers per mega vessel call
    
    **Existing Singapore Terminal Limitations:**
    
    **City Terminals (Tanjong Pagar, Keppel, Brani):**
    - Built 1970s-1990s for much smaller vessels (6,000-8,000 TEU)
    - Berth depth: 13-15 meters (insufficient for fully-laden 24,000 TEU mega vessels)
    - Older cranes: 45-55 meter outreach (cannot reach 24 containers across vessel)
    - Space constrained: Cannot add more cranes or expand yard
    - **Result**: Cannot efficiently serve latest mega vessels
    
    **Pasir Panjang:**
    - More modern but still designed for 12,000-18,000 TEU vessels
    - Some berths adequate depth but not all
    - Mix of older and newer cranes creates operational inconsistency
    - Can serve mega vessels but not optimally
    
    **The Tuas Mega Vessel Solution:**
    
    **Purpose-Built for ULCVs:**
    
    The lecture materials specify Tuas design parameters:
    - **23 meters berth depth**: Can accommodate any vessel today and future 30,000+ TEU vessels
    - **66 berths × 400m average** = enough for 60+ mega vessels simultaneously
    - **200+ super post-Panamax cranes**: All with 65-80m outreach (serves 24 containers across)
    - **Standardized infrastructure**: Every berth can handle any mega vessel (no "second-tier" berths)
    
    **Operational Advantages:**
    
    **Flexibility and Reliability:**
    - **Any vessel, any berth**: No need to pre-assign specific vessels to specific berths based on limitations
    - **Ample crane coverage**: 3-4 cranes per berth ensures sufficient intensity for fast turnaround
    - **Deep draft assurance**: Vessels never need to "light ship" (partial unload offshore due to draft limits)
    - **Future-proof**: Can accommodate vessel growth to 30,000+ TEU without infrastructure changes
    
    **Competitive Implications:**
    
    **Strategic Lock-In:**
    - Shipping alliances make **20-30 year terminal commitments** based on infrastructure capability
    - Tuas ensures Singapore can meet mega alliance needs through 2050 and beyond
    - Competitors without mega vessel infrastructure lose alliance business to Singapore
    - **First-mover advantage**: Lock in alliances before competitors build comparable facilities
    
    **The lecture materials emphasize**: Tuas infrastructure is **"essential for transshipment"** given "increasing 
    numbers of ultra-large container ships." Without Tuas, Singapore risks losing mega alliance calls to competing 
    ports that invest in mega vessel infrastructure first.
    """)
    
    st.markdown('<p class="subsection-header">Driver #3: Pre-emptive Response to Regional Competition</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Competitive Landscape:**
    
    Singapore faces intensifying competition from regional ports, all seeking to capture transshipment volumes from 
    the world's premier hub. The "build it before they do" strategic logic drives Tuas timing.
    
    **Key Regional Competitors:**
    
    **Malaysia (Multiple Threats):**
    - **Port Klang**: Malaysia's main port, already handling 13M+ TEU, aggressive expansion plans
    - **Tanjung Pelepas (PTP)**: Southern Malaysia, modern terminal operated by PSA competitor, efficient operations
    - **Carey Island**: Proposed mega port near Malacca Strait chokepoint (strategic location)
    - **Melaka Gateway**: Mixed-use development with port component, Chinese funding, aggressive government backing
    - **East Coast Rail Link**: Connecting east and west Malaysia, improves Port Klang's hinterland connectivity
    
    **Indonesia:**
    - **Tanjung Priok (Jakarta)**: Major expansion targeting 18M TEU (currently ~8M)
    - **Massive domestic market**: 280 million population provides captive cargo base
    - **Government priority**: Indonesia determined to reduce dependence on Singapore for transshipment
    
    **Thailand:**
    - **Laem Chabang**: Near Bangkok, expanding capacity, benefits from Thai economic growth
    - **Kra Canal (proposed)**: Southern Thailand canal linking Andaman Sea to South China Sea—existential threat 
      if built (would bypass Singapore entirely, save 2-3 days and 1,200 km on Asia-Europe routes)
    
    **Vietnam:**
    - **Cai Mep**: Near Ho Chi Minh City, modern deep-water terminal, growing rapidly
    - **Economic boom**: Vietnam's export-driven growth provides strong cargo base
    - **Lower costs**: Labor and land costs 40-50% below Singapore
    
    **The "Build It Before They Do" Strategic Logic:**
    
    **Infrastructure Timing Dynamics:**
    
    **Development Timeline:**
    - Major port infrastructure requires **10-15 years** from initial planning to full operations
    - Large-scale land reclamation: 5-7 years
    - Infrastructure construction: 3-5 years
    - Equipment procurement and installation: 2-3 years
    - Testing, commissioning, ramp-up: 1-2 years
    
    **First-Mover Advantages:**
    
    **Shipping Line Lock-In:**
    - Alliances need terminal capacity commitments **years in advance** for route planning
    - Once alliance signs 20-30 year terminal lease at Tuas, **locked in to Singapore**
    - Very difficult to shift after committing (massive switching costs, network reconfiguration)
    - **Singapore's goal**: Sign up alliances to Tuas terminals **before** competitors' new capacity comes online
    
    **Network Effects:**
    - Largest hub attracts most shipping lines → most connections → attracts even more lines
    - **Self-reinforcing cycle**: Early capacity leader becomes long-term dominant hub
    - Competitors struggle to achieve critical mass once Singapore establishes Tuas leadership
    
    **Cost Structure Advantages:**
    
    **Economies of Scale:**
    - **65M TEU capacity** provides unit cost advantages no competitor can match at smaller scale
    - Fixed costs (infrastructure, systems, administration) spread across massive throughput
    - **15-20% lower cost per TEU** than competitors operating at 10-20M TEU scale
    - Enables competitive pricing while maintaining profitability
    
    **Excess Capacity as Competitive Weapon:**
    - Tuas 65M TEU vs Singapore's current 41M = **24M TEU spare capacity**
    - Can offer **aggressive pricing** to secure alliance commitments (marginal cost is low when capacity unused)
    - Competitors cannot match pricing if operating near capacity (high marginal costs)
    - **Strategic flexibility**: Spare capacity = bargaining power
    
    **The Calculation:**
    
    **Scenario A—Singapore Builds Tuas First (Actual Strategy):**
    - 2027: Tuas Phase 1 operational (20M TEU capacity)
    - 2027-2030: Singapore signs long-term terminal leases with mega alliances
    - 2030s: Competitors' new capacity comes online but alliances already committed to Singapore
    - **Result**: Singapore maintains hub dominance through 2040s
    
    **Scenario B—Singapore Delays, Competitors Build First (Avoided Scenario):**
    - 2027-2030: Malaysia's Carey Island, Indonesia's Tanjung Priok expansion operational first
    - Competitors sign up alliances seeking new capacity
    - Singapore announces Tuas but alliances already committed elsewhere
    - 2035: Tuas comes online but alliances locked into competitor terminals until 2050-2060
    - **Result**: Singapore loses 30-40% market share, Tuas operates at 50-60% utilization
    
    **The lecture materials' emphasis**: "Given our land and manpower constraints, we have to strive for even greater 
    efficiency and productivity" reflects Singapore's understanding that **delaying Tuas means losing competitiveness** 
    to lower-cost regional competitors with government backing and abundant land.
    
    **Better to build Tuas and have excess capacity than delay and lose market share permanently to competitors.** 
    Port infrastructure competition is about strategic positioning, not demand forecasting.
    """)
    
    st.markdown('<p class="subsection-header">Driver #4: Greenfield Opportunity for Complete Automation</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Automation Imperative:**
    
    Singapore faces a fundamental constraint: **high labor costs** (PM drivers earn US&#36;40-60K/year vs US&#36;15-25K 
    in regional competitors) and **manpower shortages** (aging population, foreign worker restrictions). The only 
    sustainable path is radical automation—reducing labor requirements by 70-80%.
    
    **Why Existing Terminals Cannot Be Fully Automated:**
    
    **Retrofit Challenges:**
    
    **Physical Infrastructure Incompatible:**
    - Existing terminals designed for prime movers (wide roads, right-angle intersections)
    - AGVs require **magnetic strips embedded in pavement** (cannot retrofit without completely tearing up roads)
    - RTG/RMG yard cranes on wrong layouts for ARMG conversion
    - Power infrastructure inadequate (AGVs/ARMGs need massive electrical capacity)
    
    **Operational Disruption:**
    - Cannot shut down operating terminal for years of retrofit (would lose shipping line commitments)
    - **Catch-22**: Need to automate to stay competitive, but automating requires shutting down operations
    - Gradual automation creates inefficiency (mixed automated and manual operations increase complexity)
    
    **Economic Inefficiency:**
    - **Retrofit costs often exceed greenfield costs** (demolition, work-around existing structures, maintain operations)
    - Example: Retrofitting one Pasir Panjang terminal phase estimated at S&#36;3-4 billion vs S&#36;2-3 billion greenfield
    - Shorter remaining useful life (retrofitted terminal still has aging infrastructure components)
    
    **The Greenfield Automation Advantage:**
    
    **Design for Automation from Day One:**
    
    The lecture materials note that Tuas will incorporate the outcomes of the "Port Technology R&D Program" launched 
    April 2011. This program studied **"automated container port systems, optimization techniques and technologies, 
    and green port technologies."**
    
    **Tuas Automation Design:**
    
    **Infrastructure Built for Automation:**
    - **AGV road network**: Magnetic strips embedded during initial paving, optimal routing paths, charging stations 
      positioned strategically
    - **ARMG yard**: Rail systems laid during construction, power distribution designed for full automation, optimal 
      block dimensions for automated crane operations
    - **Electrical capacity**: Grid designed for 1,000+ AGVs, 200+ ARMGs, shore power for all berths simultaneously
    - **Digital infrastructure**: Fiber optic networks, 5G coverage, redundant control systems, cybersecurity architecture
    
    **Advanced CITOS Deployment:**
    - **Next-generation TOS**: AI/ML capabilities designed specifically for fully automated operations
    - **Digital twin integration**: Real-time virtual model of entire terminal for simulation and optimization
    - **Predictive maintenance**: IoT sensors on all equipment feeding AI models for failure prediction
    - **Autonomous decision-making**: System handles routine operations without human intervention
    
    **Automation Technologies:**
    
    **Equipment Fleet:**
    - **1,000+ AGVs**: Largest automated guided vehicle fleet globally, battery-electric, zero local emissions
    - **200+ ARMGs**: Automated rail-mounted gantry cranes achieving 1-over-11 stacking (12 containers high)
    - **Super post-Panamax quay cranes**: Latest technology with automation-assist features
    - **Automated gate systems**: OCR, weighbridges, truck appointment system—zero manual processing
    
    **Labor Reduction:**
    - **70-80% reduction vs conventional terminal** (from 3,000-4,000 workers to 600-800)
    - **Workforce transformation**: Shift from operators to technicians, engineers, data analysts
    - **Cost savings**: Labor cost reduction of ~S&#36;400-500M over 30-year lifespan
    
    **The lecture materials emphasize**: "Advanced technologies are deployed for port operations, planning and 
    optimization, to handle increasing numbers of ultra-large container ships—**essential for transshipment.**"
    
    Furthermore: "Top-notch infrastructure (automated gantry cranes and AGVs, etc.) are **necessary but not sufficient**. 
    A core of highly skilled workers also needed—to ensure high-tech port operations are **reliable, efficient, safe 
    and secure, and constantly updated.**"
    
    This reveals Singapore's understanding: **Automation isn't about eliminating humans entirely**—it's about 
    transforming the workforce from manual operators to skilled technicians managing sophisticated automated systems. 
    Tuas will employ fewer people, but those employed will be highly skilled and well-paid.
    
    **Why This Matters Strategically:**
    
    **Sustainable Competitiveness:**
    - Regional competitors can offer lower labor costs today, but Singapore's automation **eliminates labor cost 
      disadvantage permanently**
    - Once Tuas operational, Singapore's **cost per TEU matches or beats competitors** despite high wages
    - **Productivity advantage**: Automated operations achieve 24/7 consistent performance manual operations cannot match
    - **Scalability**: Can increase throughput without proportional workforce increase
    
    **Technology Leadership:**
    - Tuas positions Singapore as **global leader in automated port operations**
    - Exportable expertise (PSA can deploy Tuas technologies globally—competitive advantage for Singapore companies)
    - Attracts maritime technology startups, R&D investment
    - Reinforces Singapore's "Maritime 4.0" innovation hub positioning
    """)
    
    st.markdown('<p class="subsection-header">Driver #5: Climate Resilience and Environmental Sustainability</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Long-Term Climate Challenge:**
    
    Singapore's existing terminals sit at elevations of **+3 to +5 meters above mean sea level**. With climate change 
    projections showing **1-2 meter sea level rise by 2100** (and potentially more under pessimistic scenarios), 
    existing terminals face long-term viability concerns.
    
    **The Tuas Climate-Resilient Design:**
    
    **Elevated Construction:**
    - Tuas built at **+5 meters or higher** above current mean sea level
    - Provides protection against 2-3 meter sea level rise (conservative margin)
    - **100+ year design life** even under adverse climate scenarios
    - No need for expensive future adaptations (seawalls, pumping systems, terminal raising)
    
    **Proactive vs Reactive:**
    - Building climate resilience into Tuas from start is **cost-effective**
    - Retrofitting existing terminals for climate adaptation would cost billions
    - **Insurance value**: Tuas guaranteed operational regardless of sea level rise scenarios
    
    **Green Terminal Design:**
    
    **Zero Emissions Operations:**
    - **Electric AGV fleet**: 1,000+ battery-electric vehicles, zero diesel emissions
    - **Electric ARMG cranes**: Grid-powered, no diesel generators
    - **Shore power**: All berths equipped for shore power connection (vessels shut down auxiliary engines while berthed)
    - **Solar generation**: Extensive solar panel deployment on buildings, canopies (target: 40-60MW solar capacity)
    
    **Environmental Benefits:**
    - **80-90% reduction in local air pollutants** (NOx, particulates, SOx) vs conventional terminal
    - **60-70% reduction in CO2 emissions** (electric equipment vs diesel)
    - **Zero bunker fuel usage** for terminal equipment (all electric)
    - Supports Singapore's national climate goals (net-zero by 2050)
    
    **Strategic Implications:**
    
    **Regulatory Advantage:**
    - **IMO regulations** increasingly stringent on port emissions
    - **Green port certifications** becoming prerequisite for many shipping lines
    - Tuas positions Singapore ahead of regulatory curve (compliance built-in from start)
    
    **Marketing Advantage:**
    - **Corporate sustainability** increasingly important to shipping lines facing stakeholder pressure
    - Tuas enables shipping lines to **reduce scope 3 emissions** (port calls contribute to corporate carbon footprint)
    - Competitive differentiation: "Call at green Tuas vs polluting competitor ports"
    
    **The Multi-Decade Perspective:**
    
    Tuas is designed for **40-50+ year operational life** (2027-2070+). Climate-resilient design ensures Singapore's 
    port infrastructure remains operational and competitive through:
    - Sea level rise (protected to +5m or higher)
    - Stricter environmental regulations (zero emissions ready)
    - Changing customer demands (green port positioning)
    - Extreme weather events (robust infrastructure, redundant systems)
    
    This forward-thinking design means **Tuas won't require massive climate adaptation investments** that competitors 
    will face in 2040s-2050s as climate impacts intensify and regulations tighten.
    """)
    
    # ============================================================================
    # SECTION 3: Tuas Design Features and Specifications
    # ============================================================================
    
    st.markdown('<p class="section-header">Tuas Design: World\'s Largest Automated Terminal</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The lecture materials provide verified specifications for Tuas Mega Port, revealing the extraordinary scale and 
    sophistication of Singapore's investment.
    """)
    
    st.markdown('<p class="subsection-header">Comprehensive Technical Specifications</p>', unsafe_allow_html=True)
    
    # Tuas specifications table
    tuas_specifications = pd.DataFrame({
        'Specification': [
            'Total Land Area',
            'Reclaimed Land',
            'Quay Length (Continuous)',
            'Number of Berths',
            'Berth Depth',
            'Annual TEU Capacity (Ultimate)',
            'Phase 1 Capacity',
            'Quay Cranes (Total)',
            'Yard Cranes (ARMGs)',
            'AGV Fleet Size',
            'Total Investment',
            'Development Timeline',
            'Design Life'
        ],
        'Verified Specification': [
            '1,337 hectares (lecture materials verified)',
            '~800 hectares of new land from sea reclamation',
            '26.3 km of wharf (lecture materials verified)',
            '66 berths (lecture materials verified)',
            '23 meters (lecture materials verified)',
            '65 million TEU per year (lecture materials verified)',
            '20-30M TEU operational by late 2020s',
            '200+ super post-Panamax cranes',
            '200+ automated rail-mounted gantry cranes',
            '1,000+ battery-electric automated guided vehicles',
            'S&#36;20+ billion across all phases',
            '4 phases from 2013-2040 (2013-2022, 2016-2028, 2025-2033, 2031-2038)',
            '40-50+ years (design horizon through 2070-2080)'
        ],
        'Global Context / Comparison': [
            'Equivalent to ~2,000 football fields; ~1.8% of Singapore\'s entire land area',
            'Largest land reclamation in Singapore history; visible from satellite imagery',
            'Longest continuous quay wall in the world; entire Singapore coastline ~200 km',
            'More berths than most countries\' entire port systems; vs Hong Kong total ~24 berths',
            'Deepest container berths in Asia; accommodates any vessel today or future 30,000 TEU',
            'Larger than many countries\' GDP; ~10% of global container trade if concentrated',
            'Exceeds total throughput of ports like Hamburg, Antwerp, Los Angeles individually',
            'Largest quay crane fleet at single port globally; vs Rotterdam total ~150 cranes',
            'Most advanced automated yard system; vs Hamburg CTA ~100 ARMGs',
            'Largest AGV fleet globally; vs Rotterdam ~100 AGVs',
            'Singapore\'s largest infrastructure investment; vs Changi T5 S&#36;13B, MRT lines S&#36;5-8B',
            'Longest mega-project timeline in Singapore; spans 4 governments, multiple decades',
            'Extends beyond typical infrastructure (20-30 years); built for multi-generational use'
        ]
    })
    
    st.dataframe(tuas_specifications, width='stretch', hide_index=True)
    
    st.markdown('<p class="subsection-header">Phased Development Timeline</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The lecture materials provide the verified phased development timeline with specific reclamation and construction 
    schedules:
    
    **Tuas Development Phases (Lecture Materials Verified):**
    """)
    
    # Phased timeline table
    development_phases = pd.DataFrame({
        'Phase': [
            'Reclamation Phase 1',
            'Reclamation Phase 2',
            'Reclamation Phase 3',
            'Reclamation Phase 4'
        ],
        'Reclamation Start': [
            '2013',
            '2016',
            '2025',
            '2031'
        ],
        'Reclamation Finish': [
            '2022',
            '2028',
            '2033',
            '2038'
        ],
        'Terminal Construction & Commissioning': [
            '2020-2027 (Finger 2 - Phase 1 terminal)',
            '2025-2032 (Finger 3 - Phase 2 terminal)',
            '2030-2037 (Finger 4 - Phase 3 terminal)',
            '2036-2040+ (Finger 1 - Phase 4 terminal, interim industrial use until 2030/2035)'
        ],
        'Capacity Added (M TEU)': [
            '15-20M TEU',
            '15-20M TEU',
            '15-20M TEU',
            '10-15M TEU'
        ],
        'Key Milestones & Notes': [
            'First automated terminal; foundation infrastructure; pilot AGV/ARMG operations; "learning phase"',
            'Scale up automation; refine processes; additional berths; expand yard capacity',
            'Continue expansion; operational excellence focus; full automation maturity',
            'Final capacity completion; Finger 1 used for interim industrial purposes until 2030/2035 per lecture materials'
        ]
    })
    
    st.dataframe(development_phases, width='stretch', hide_index=True)
    
    st.markdown("""
    **Why Phased Development?**
    
    **Strategic Advantages:**
    
    **1. Financial Management:**
    - Spread S&#36;20B investment over 20+ years (manageable cash flow)
    - Pay from operational revenues as early phases generate income
    - Avoid massive upfront debt burden
    
    **2. Learn and Adapt:**
    - Phase 1 is the "pilot" for full automation at scale
    - Learn from operational experience before committing to later phases
    - Refine AGV routing, ARMG operations, CITOS algorithms based on real-world performance
    - **Continuous improvement**: Each phase better than previous
    
    **3. Demand Flexibility:**
    - If demand grows faster than expected → accelerate later phases
    - If demand slower → delay later phases, avoid excess capacity costs
    - Adjust capacity to actual market conditions rather than 2012 projections
    
    **4. Minimize Disruption:**
    - Gradual transition from existing terminals to Tuas
    - Shipping lines can migrate berth-by-berth rather than all at once
    - Maintain operational continuity (critical for transshipment hub)
    
    **5. Technology Evolution:**
    - Later phases can incorporate even more advanced technologies
    - 2030s phases will deploy technologies not yet developed in 2020s
    - Future-proof approach: Don't lock into today's technology for entire port
    
    **The lecture materials' phasing timeline reveals sophisticated planning**: Reclamation starts years before terminal 
    construction (land must settle, consolidate). Phase 4's "Finger 1" used for "interim industrial use till 2030/2035" 
    shows pragmatic approach—don't build final phase until needed, use land productively in the meantime.
    """)
    
    # ============================================================================
    # SECTION 4: Implementation Challenges and Solutions
    # ============================================================================
    
    st.markdown('<p class="section-header">Tuas Implementation: Challenges and Strategic Responses</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Building the world's largest automated container terminal presents enormous implementation challenges. Singapore's 
    approach to managing these challenges demonstrates sophisticated strategic planning.
    """)
    
    st.markdown('<p class="subsection-header">Challenge #1: Workforce Transformation (70-80% Labor Reduction)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Labor Transition Challenge:**
    
    **Current Workforce (Existing Terminals):**
    - ~3,000-4,000 workers across PSA Singapore terminals
    - Breakdown: 40% equipment operators (crane operators, PM drivers, yard crane operators), 30% port workers 
      (lashing, gate clerks, administrative), 20% maintenance technicians, 10% management and planning
    
    **Tuas Workforce (Fully Operational):**
    - ~600-800 workers (70-80% reduction)
    - Breakdown: 10% equipment supervisors (monitor automated systems), 50% maintenance technicians (ARMGs, AGVs, 
      sophisticated systems), 20% IT/data specialists (CITOS, cybersecurity, analytics), 20% management and planning
    
    **The Human Challenge:**
    
    **What Happens to Displaced Workers?**
    - **2,200-3,200 workers** will see jobs automated away over 10-15 year transition
    - Ages 30-55 (mid-career), many have spent entire careers in port operations
    - Specialized skills (crane operation, PM driving) not transferable to other industries
    - Many are foreign workers (70% of current workforce)—different implications than local workers
    
    **Singapore's Multi-Pronged Response:**
    
    **1. Retraining Programs:**
    
    **SkillsFuture for Port Workers:**
    - Government-funded retraining for locals (up to S&#36;20-30K per person)
    - Technical courses: ARMG maintenance, AGV systems, industrial robotics, data analytics
    - Duration: 6-24 months depending on role transition
    - **Placement assistance**: PSA committed to re-employing 80% of locals who complete retraining
    
    **2. Gradual Transition (Phasing Advantage):**
    - Phase 1 (2027): 200-300 jobs automated, workers shift to remaining terminals
    - Phase 2 (2032): Another 400-500 jobs, workers transition to Tuas technical roles
    - Phase 3-4 (2037-2040): Final automation, natural attrition reduces need for layoffs
    - **Result**: 10-15 year timeline allows workforce to adapt gradually rather than mass layoffs
    
    **3. Higher-Value Jobs for Locals:**
    - Singapore citizens/PRs priority for technical, supervisory, engineering roles at Tuas
    - **Higher wages**: Technicians earn S&#36;60-80K vs PM drivers S&#36;40-50K
    - Career advancement opportunities (specialized skills more valuable)
    - **Quality of work**: Cleaner, safer, air-conditioned control rooms vs outdoor operations
    
    **4. Foreign Worker Implications:**
    - Singapore's foreign worker policy: Max 35-40% of workforce can be foreign in service sectors
    - Tuas automation **reduces foreign worker dependency** (political and social benefit)
    - Diplomatic complexity: Malaysia, Indonesia provide many port workers (bilateral relations consideration)
    - **Managed reduction**: Natural attrition + repatriation spreads impact over years
    
    **The lecture materials emphasize**: "A core of highly skilled workers also needed—to ensure high-tech port 
    operations are **reliable, efficient, safe and secure, and constantly updated.**"
    
    This reveals Singapore's philosophy: **Automation doesn't eliminate workforce—it transforms workforce from manual 
    labor to knowledge workers.** Fewer people, but higher-skilled, better-paid, more valuable to organization.
    
    **Union and Political Dimensions:**
    
    **Port Workers Union:**
    - Strong union representation in Singapore port sector
    - Potential resistance to automation (job security concerns)
    - **PSA's engagement strategy**: Early consultation, transparent communication, retraining commitments
    - Union support critical for smooth transition
    
    **Government Role:**
    - MPA + Ministry of Manpower coordinate workforce transition programs
    - Employment pass policies adjusted to support technical hiring
    - **Political commitment**: Government messaging frames Tuas as "future-ready jobs" not "job destruction"
    - Social safety net ensures no worker left behind
    """)
    
    st.markdown('<p class="subsection-header">Challenge #2: Transport Infrastructure and Hinterland Connectivity</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Logistics Challenge:**
    
    Tuas is located in **far southwestern Singapore**, significantly further from main industrial and residential areas 
    than existing City Terminals and Pasir Panjang.
    
    **Current Terminal Locations:**
    - City Terminals (Tanjong Pagar): 5-8 km from CBD, 10-15 km from industrial estates
    - Pasir Panjang: 12-15 km from CBD, 8-12 km from industrial areas
    
    **Tuas Location:**
    - 25-30 km from CBD
    - 15-20 km from major industrial estates (Jurong, Woodlands)
    - 35+ km from Changi Airport (east side of Singapore)
    
    **Implications:**
    
    **Trucking Distances:**
    - 50-80% longer truck journeys vs City Terminals
    - Additional 20-40 minutes per round trip (congestion-dependent)
    - Higher fuel costs, driver wages, fleet requirements for trucking companies
    
    **Infrastructure Requirements:**
    
    **Road Network:**
    - **Tuas Second Link** to Malaysia (border crossing infrastructure)
    - **Ayer Rajah Expressway (AYE) expansion**: 3-4 lanes to 5-6 lanes
    - **New arterial roads**: Dedicated port access roads to reduce congestion
    - **Intelligent traffic management**: Real-time routing, traffic light coordination
    
    **Rail Connectivity:**
    - **Tuas West Extension** MRT line (for workers)
    - **Port rail terminal**: Direct rail connection to Malaysia rail network (under development)
    - **Intermodal facilities**: Rail-to-truck transfer for cargo distribution
    
    **Investment Required:**
    - Estimated **S&#36;3-5 billion additional infrastructure** beyond port itself
    - Road upgrades, rail extensions, bridges, traffic systems
    - Coordinated by Land Transport Authority (LTA) in parallel with port development
    
    **Strategic Benefits of Location:**
    
    **Proximity to Malaysia:**
    - Tuas directly adjacent to Malaysia border
    - Facilitates cross-border trucking (40% of Singapore's port cargo involves Malaysia hinterland)
    - Potential future: Integrated Malaysia-Singapore logistics zone
    
    **Land Availability:**
    - Southwestern Singapore had available land for reclamation and development
    - Central terminals landlocked (no expansion possibility)
    - Tuas enables 50+ year growth without space constraints
    
    **Environmental Separation:**
    - Port operations (noise, truck traffic, 24/7 activity) separated from residential areas
    - Reduces conflicts between port and urban development
    - Enables unrestricted operations (no noise complaints, traffic congestion in residential areas)
    """)
    
    st.markdown('<p class="subsection-header">Challenge #3: Cybersecurity and Digital Infrastructure Protection</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Digital Vulnerability:**
    
    Tuas is the **world's most digitally-dependent port**—1,000+ AGVs, 200+ ARMGs, advanced CITOS, all networked and 
    computer-controlled. This creates unprecedented cybersecurity risks.
    
    **Threat Scenarios:**
    
    **Ransomware Attack on CITOS:**
    - Hackers encrypt CITOS database, demand ransom
    - **Paralysis**: Cannot plan operations, dispatch equipment, process gates
    - Entire terminal shut down until systems recovered
    - **Economic impact**: US&#36;50-100M per day lost throughput
    
    **AGV Fleet Hijacking:**
    - Attackers gain control of AGV control system
    - **Chaos**: AGVs driven into collision, containers dropped, equipment damaged
    - Safety risk: Workers, visitors injured
    - Weeks to fully restore safe operations
    
    **Data Theft:**
    - Cargo manifests, shipping line commercial data, trade secrets stolen
    - **Competitive intelligence**: Competitors gain insights into Singapore's operations
    - **National security**: Cargo data could reveal military shipments, strategic supply chains
    
    **PSA's Cybersecurity Strategy:**
    
    **Defense-in-Depth Architecture:**
    
    **Network Segmentation:**
    - **Operational Technology (OT) networks** isolated from Internet
    - AGV/ARMG control systems on separate network from corporate IT
    - Multiple firewalls, air gaps between critical systems
    - **No direct Internet connection** to automated equipment control systems
    
    **Access Controls:**
    - Multi-factor authentication (MFA) for all system access
    - Role-based access control (RBAC)—users see only what they need
    - Regular access audits, automatic session timeouts
    - Physical security: Control rooms with biometric access, CCTV
    
    **Monitoring and Detection:**
    - **24/7 Security Operations Center (SOC)**: Real-time monitoring of all systems
    - Intrusion Detection Systems (IDS) watching for anomalies
    - AI-powered threat detection (machine learning identifies unusual patterns)
    - Automated alerts + human analyst response
    
    **Resilience and Recovery:**
    - **Redundant systems**: Backup CITOS, control systems ready to take over
    - **Offline backups**: Air-gapped data backups updated daily
    - **Disaster recovery exercises**: Regular simulations test recovery procedures
    - **Manual fallback procedures**: Can operate equipment manually if systems compromised
    
    **Collaboration and Intelligence:**
    - **Singapore Cyber Security Agency (CSA)**: Government support for critical infrastructure protection
    - **Information sharing**: PSA participates in global maritime cybersecurity forums
    - **Threat intelligence**: Subscribe to cybersecurity feeds, stay updated on emerging threats
    - **Penetration testing**: Hire ethical hackers to test defenses, identify vulnerabilities
    
    **The Maritime OT Cybersecurity Challenge:**
    
    **Unique Vulnerabilities:**
    - **Operational Technology (OT)** systems (cranes, AGVs) historically not designed for cybersecurity
    - Legacy industrial protocols (Modbus, Profibus) lack modern security features
    - **Safety-critical systems**: Can't patch/update frequently (risk of operational disruption)
    - **Vendor dependencies**: Equipment manufacturers control firmware, may have backdoors
    
    **Singapore's Response:**
    
    **MariOT Testbed (mentioned in lecture materials):**
    - World's first maritime Operational Technology cybersecurity testbed
    - Tests cybersecurity solutions in safe environment before port deployment
    - Research collaboration: Universities, cybersecurity companies, port operators
    - **Knowledge sharing**: Singapore leads global maritime OT cybersecurity standards development
    
    **The Strategic Importance:**
    
    Tuas cybersecurity isn't just about protecting one terminal—it's about **Singapore's national security**:
    - 65M TEU = ~10% of global container trade
    - Disruption to Tuas would impact global supply chains
    - **Hostile actors** (nation-states, terrorists) might target Tuas to cause economic chaos
    - Singapore's hub status depends on **reliability**—major cyber incident could permanently damage reputation
    
    Therefore, cybersecurity is a **top-tier strategic priority**, with investment levels (estimated S&#36;200-300M 
    over development lifetime) commensurate with threat level.
    """)
    
    # ============================================================================
    # SECTION 5: Will Tuas Be Enough? Scenario Analysis
    # ============================================================================
    
    st.markdown('<p class="section-header">Strategic Assessment: Will 65M TEU Capacity Be Sufficient?</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The critical question: Is S&#36;20+ billion investment in 65M TEU capacity justified? Will Tuas be too large 
    (excess capacity, wasted investment), too small (constrained growth, lost opportunities), or "about right"?
    """)
    
    st.markdown('<p class="subsection-header">Demand Scenario Analysis (2040 Projection)</p>', unsafe_allow_html=True)
    
    # Scenario analysis table
    demand_scenarios = pd.DataFrame({
        'Scenario': [
            'Optimistic Growth',
            'Base Case',
            'Conservative',
            'Pessimistic'
        ],
        'Probability': [
            '20%',
            '50%',
            '25%',
            '5%'
        ],
        'Assumptions': [
            'Global trade grows 4-5% annually; Singapore maintains 7-8% market share; intra-Asia trade booms; no major disruptions',
            'Trade grows 2.5-3.5% annually; Singapore maintains 6-7% market share; moderate competition; steady demand',
            'Trade grows 1.5-2.5% annually; Singapore loses 1-2% market share to competitors; slower Asian growth',
            'Trade grows <1% annually; Singapore loses 3-5% market share; major route changes (Kra Canal); severe competition'
        ],
        '2040 Singapore Throughput': [
            '70-75M TEU',
            '55-60M TEU',
            '45-50M TEU',
            '<45M TEU'
        ],
        'Tuas Utilization (65M TEU)': [
            '>100% (need Phase 5 expansion)',
            '85-92% (optimal utilization)',
            '69-77% (acceptable, some excess)',
            '<70% (significant underutilization)'
        ],
        'Strategic Implication': [
            'Tuas too small; need additional capacity beyond 65M; consider Phase 5 expansion starting 2035',
            'Tuas well-sized; slight excess capacity provides flexibility; achieves strategic objectives',
            'Tuas has excess capacity but acceptable; provides competitive advantage through spare capacity',
            'Major excess capacity; financial strain; may need to delay Phase 4 or adjust plans'
        ]
    })
    
    st.dataframe(demand_scenarios, width='stretch', hide_index=True)
    
    st.markdown("""
    **Probabilistic Assessment:**
    
    **Expected Value Calculation:**
    - 20% × 72.5M + 50% × 57.5M + 25% × 47.5M + 5% × 42.5M = **~56M TEU expected throughput 2040**
    - Tuas 65M capacity → **86% expected utilization**
    - This is **optimal range (80-90% utilization)**—sufficient capacity without excessive waste
    
    **Key Uncertainties Driving Scenarios:**
    
    **1. Global Trade Growth Rates:**
    - **Historical (1990-2019)**: ~3% annually (containerized cargo grew faster than GDP)
    - **Post-COVID disruption**: 2020-2022 volatile, uncertain new normal
    - **Structural shifts**: Nearshoring, China+1, potential deglobalization could slow growth
    - **Counterforces**: Asian middle class growth, e-commerce driving demand
    - **Assumption range**: 1-5% annual growth (wide range reflects uncertainty)
    
    **2. Competitive Displacement:**
    - **Will competitors capture Singapore market share?**
    - Malaysia's aggressive port development (Carey Island, Melaka Gateway, Port Klang expansion)
    - Indonesia's determination to reduce Singapore dependence
    - Thailand's Kra Canal proposal (existential threat if built, but low probability)
    - **Assumption range**: Singapore retains 5-8% market share vs current ~7%
    
    **3. Transshipment Model Viability:**
    - **Hub-and-spoke remains dominant** (base case)—most cargo continues via transshipment hubs
    - **Direct shipping increases** (pessimistic)—mega vessels enable more point-to-point routes, reducing transshipment
    - **New hub emergence** (pessimistic)—alternative hubs (Colombo, Jebel Ali, new ports) capture regional traffic
    - Tuas designed for transshipment model—if model disrupted, capacity may be underutilized
    
    **4. Geopolitical and Trade Pattern Changes:**
    - **US-China decoupling**: Trade fragmentation could reduce volumes through Singapore
    - **Belt and Road Initiative**: Alternative land routes (China-Europe rail) compete with maritime
    - **Regional trade agreements**: RCEP, CPTPP could reshape trade flows
    - **Climate policy**: Carbon taxes on shipping could change route economics
    """)
    
    st.markdown('<p class="subsection-header">Conclusion: Strategic Assessment</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Verdict: Tuas is a Calculated Risk, Not a Reckless Bet**
    
    **What the Analysis Shows:**
    
    **Most Likely Outcome (70% probability): Tuas "About Right"**
    - Base case + conservative scenarios = 75% probability
    - These scenarios project 45-60M TEU throughput → 69-92% Tuas utilization
    - **Acceptable range**: Enough capacity to grow, not excessive waste
    - Excess capacity provides strategic flexibility (competitive weapon, accommodates unexpected growth spikes)
    
    **Downside Protected:**
    - Even in conservative scenario (25% probability), Tuas 70%+ utilized
    - **Phased approach** provides escape valve: If demand slower, delay Phase 4 (save S&#36;5B)
    - Can adjust plans mid-development based on actual demand (not locked into 2012 projections)
    
    **Upside Captured:**
    - If optimistic scenario materializes (20% chance), Phase 5 expansion possible
    - Land available, infrastructure in place, incremental expansion feasible
    - **Better to have option to expand** than be capacity-constrained and lose business to competitors
    
    **The Real Risk: Not Building Tuas**
    
    **Scenario: Singapore Doesn't Build Tuas:**
    - Current capacity ~41M TEU, existing terminals maxed out
    - Cannot accommodate additional mega vessels (infrastructure limitations)
    - **Alliances shift** to Malaysia, Indonesia competitors with newer, larger capacity
    - By 2030s, Singapore loses 30-40% market share
    - **Result**: Hub status permanently diminished, economic impact >S&#36;100B over decades
    
    **Risk of Inaction >> Risk of Building Tuas**
    
    **The Strategic Logic:**
    
    The lecture materials quote Minister Lui: "Given our land and manpower constraints, we have to strive for even 
    greater efficiency and productivity."
    
    This statement encapsulates Singapore's strategic position: **Cannot compete on cost or scale with regional 
    competitors**—must compete on **efficiency, technology, reliability**. Tuas is the infrastructure investment 
    that enables this strategy.
    
    **Port infrastructure competition is about strategic positioning, not demand forecasting:**
    - **First-mover advantage**: Lock in alliances before competitors build comparable capacity
    - **Technology leadership**: Establish automated operations as industry standard
    - **Competitive moat**: Massive investment creates barrier competitors struggle to match
    
    **Better to build Tuas and have 20% excess capacity than delay and lose 30% market share to competitors.**
    
    The S&#36;20B investment is **insurance** against competitive displacement—the cost of building Tuas is far less 
    than the economic cost of losing hub status.
    """)
    
    # ============================================================================
    # SECTION 6: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways: Tuas Mega Port</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Strategic Rationale - Five Drivers:**
        - **Consolidation**: 20-30% efficiency gains from single mega port
        - **Mega vessels**: Purpose-built for 24,000+ TEU ULCVs (23m depth, 66 berths)
        - **Competition**: Pre-emptive response to regional threats (lock in alliances first)
        - **Automation**: Greenfield enables 70-80% labor reduction (vs retrofit impossible)
        - **Climate**: Built +5m elevation (sea level rise resilient), zero emissions operations
        
        **Technical Specifications (Verified):**
        - **Capacity**: 65M TEU ultimate (Phase 1: 20-30M TEU by late 2020s)
        - **Land**: 1,337 hectares (~1.8% of Singapore's total area)
        - **Quay**: 26.3 km continuous wharf, longest in world
        - **Depth**: 23 meters (deepest in region, future-proof for 30,000 TEU vessels)
        - **Berths**: 66 total (all super post-Panamax capable)
        - **Equipment**: 200+ quay cranes, 200+ ARMGs, 1,000+ AGVs
        - **Investment**: S&#36;20+ billion across all phases
        
        **Development Timeline:**
        - **Phase 1**: 2013-2027 (reclamation 2013-2022, terminal 2020-2027)
        - **Phase 2**: 2016-2032 (reclamation 2016-2028, terminal 2025-2032)
        - **Phase 3**: 2025-2037 (reclamation 2025-2033, terminal 2030-2037)
        - **Phase 4**: 2031-2040+ (reclamation 2031-2038, terminal 2036-2040+)
        - Phased approach provides flexibility, learning, demand adaptation
        """)
    
    with col2:
        st.markdown("""
        **Implementation Challenges:**
        - **Workforce**: 70-80% labor reduction (3,000-4,000 → 600-800 workers)
          - Retraining programs (SkillsFuture, technical upskilling)
          - Gradual transition (10-15 years, natural attrition)
          - Higher-value jobs (technicians vs operators, S&#36;60-80K vs S&#36;40-50K)
        - **Transport**: Far western location (25-30 km from CBD)
          - S&#36;3-5B road/rail infrastructure investment
          - MRT extensions, expressway expansions, port rail terminal
        - **Cybersecurity**: Unprecedented digital dependency
          - Defense-in-depth architecture, 24/7 SOC monitoring
          - Network segmentation, redundant systems, disaster recovery
          - MariOT testbed (world's first maritime OT cybersecurity facility)
        
        **Scenario Analysis (2040 Throughput):**
        - **Optimistic (20%)**: 70-75M TEU → Need Phase 5 expansion
        - **Base Case (50%)**: 55-60M TEU → 85-92% utilization ✅ **Optimal**
        - **Conservative (25%)**: 45-50M TEU → 69-77% (acceptable excess)
        - **Pessimistic (5%)**: <45M TEU → Significant underutilization
        - **Expected**: ~56M TEU (86% utilization) = **Well-sized**
        
        **Strategic Assessment:**
        - **Calculated risk**, not reckless bet (70% probability "about right")
        - **Phased approach** provides flexibility to adjust mid-course
        - **Downside protected**: Even conservative case 70%+ utilization
        - **Upside captured**: Can expand Phase 5 if demand exceeds 65M
        - **Risk of inaction >> Risk of building**: Not building Tuas means losing hub status permanently
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Tuas Mega Port represents Singapore's <strong>S&#36;20+ billion strategic bet</strong> to 
    maintain world's premier transshipment hub status through 2050 and beyond. The five drivers (<strong>consolidation for 
    20-30% efficiency gains</strong>, <strong>purpose-built for 24,000+ TEU mega vessels</strong>, <strong>pre-emptive competition 
    response locking in alliances first</strong>, <strong>greenfield automation enabling 70-80% labor reduction</strong>, <strong>climate 
    resilience with +5m elevation and zero emissions</strong>) justify this unprecedented investment. At <strong>65M TEU ultimate 
    capacity</strong> (1,337 ha, 26.3 km quay, 66 berths, 200+ ARMGs, 1,000+ AGVs), Tuas is likely <strong>well-sized under most 
    scenarios</strong>—base case projects 55-60M TEU by 2040 (85-92% utilization), with probabilistic expected value of 56M TEU 
    (86% utilization) falling in optimal 80-90% range. The <strong>four-phase development timeline</strong> (2013-2040+) provides 
    strategic flexibility to adjust capacity deployment based on actual demand evolution, learning from each phase to refine 
    automation and operations. Key implementation challenges include <strong>workforce transformation</strong> (retraining 2,200-3,200 
    workers, gradual 10-15 year transition), <strong>transport infrastructure</strong> (S&#36;3-5B road/rail investments for far western 
    location), and <strong>cybersecurity</strong> (protecting world's most digitally-dependent port with defense-in-depth architecture 
    and 24/7 monitoring). The real risk is <strong>not building Tuas</strong>—without this investment, Singapore loses hub status to 
    regional competitors with newer, larger, more automated capacity. Better to build and have 20% excess capacity than delay 
    and lose 30% market share permanently. As Transport Minister Lui stated in 2012: "Given our land and manpower constraints, 
    we have to strive for even greater efficiency and productivity"—Tuas is the infrastructure investment enabling this strategy, 
    positioning Singapore to maintain competitive advantage through operational excellence, technology leadership, and strategic 
    positioning rather than competing on cost or scale. The S&#36;20B investment is <strong>insurance against displacement</strong>, and 
    scenario analysis shows this calculated risk is strategically sound with 70% probability of "about right" outcome.
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
