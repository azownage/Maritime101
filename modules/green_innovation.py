import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">🌱 Green Maritime & Future Trends</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Master the maritime industry's transformation toward net-zero emissions by 2050 through comprehensive understanding 
    of IMO's revised greenhouse gas (GHG) strategy with aggressive reduction targets (20-30% by 2030, 70-80% by 2040, 
    net-zero by ~2050), explore alternative fuel technologies (LNG with 185 global bunkering ports, methanol with 122 
    ports, emerging ammonia and hydrogen), analyse real-world fleet adoption (CMA CGM deploying 77 dual-fuel vessels 
    by 2026, 15% of fleet to be green by 2028), understand green port initiatives (shore power, equipment 
    electrification, renewable energy, Singapore's Future Fuels Port Network), comprehend digital transformation 
    (digitalPORT&#64;SG, paperless trade, AI optimization), and evaluate the economic, technical, and political 
    challenges of achieving the most significant maritime transformation in history.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: IMO Decarbonization Strategy - Revised 2023 Targets
    # ============================================================================
    
    st.markdown('<p class="section-header">IMO Revised GHG Strategy: The Accelerated Pathway to Net-Zero</p>', unsafe_allow_html=True)
    
    st.markdown("""
    In **July 2023**, the International Maritime Organization (IMO) adopted a **revised and significantly more 
    ambitious Greenhouse Gas (GHG) Strategy** at MEPC 80 (Marine Environment Protection Committee, 80th session). 
    This revision represents a dramatic acceleration of maritime decarbonization commitments compared to the initial 
    2018 strategy, reflecting mounting scientific evidence and political pressure to address climate change.
    
    The lecture materials emphasize this historic shift in ambition, with the revised strategy committing the global 
    maritime industry to **net-zero GHG emissions by or around 2050**—a target previously considered impossible by 
    many industry stakeholders.
    """)
    
    # Key metrics display
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Current Emissions", "~3% Global CO₂", help="Maritime transport accounts for ~3% of global CO2 emissions (~1 billion tonnes/year)")
    with col2:
        st.metric("2030 Target", "20-30% Reduction", help="Revised target: 20% reduction, striving for 30%, vs 2008 baseline")
    with col3:
        st.metric("2040 Target", "70-80% Reduction", help="Revised target: 70% reduction, striving for 80%, vs 2008 baseline")
    with col4:
        st.metric("2050 Target", "Net-Zero GHG", help="Net-zero greenhouse gas emissions by or around 2050")
    
    st.markdown('<p class="subsection-header">Comparing Initial vs Revised IMO Strategies</p>', unsafe_allow_html=True)
    
    # IMO strategy comparison table
    imo_comparison = pd.DataFrame({
        'Metric': [
            'Annual GHG Emissions Reduction (2030)',
            'Annual GHG Emissions Reduction (2040)',
            'Annual GHG Emissions Reduction (2050)',
            'Carbon Intensity Reduction (2030)',
            'Carbon Intensity Reduction (2050)',
            'Alternative Fuel Uptake Target',
            'Timeframe for Net-Zero'
        ],
        'Initial Strategy (2018)': [
            'Not specified',
            'Not specified',
            '50% reduction vs 2008',
            '40% reduction vs 2008',
            '70% reduction vs 2008 (aspirational)',
            'Not specified',
            'By end of this century (2100)'
        ],
        'Revised Strategy (2023)': [
            '20%, striving for 30% vs 2008',
            '70%, striving for 80% vs 2008',
            'Net-zero (100% reduction)',
            '40% reduction vs 2008 (maintained)',
            'Not specified (superseded by net-zero target)',
            'At least 5%, striving for 10% by 2030',
            'By or around 2050 (50 years earlier!)'
        ],
        'Implication': [
            'Immediate action required starting now (2024-2030)',
            'Aggressive fleet transition needed throughout 2030s',
            'Complete fuel transformation by 2050 (30 years earlier than initial strategy)',
            'Operational efficiency improvements + some alternative fuel adoption',
            'Net-zero supersedes intensity targets—requires zero-carbon fuels',
            'Forces rapid alternative fuel infrastructure development',
            'Industry must complete transformation in 26 years vs 76 years'
        ]
    })
    
    st.dataframe(imo_comparison, width='stretch', hide_index=True)
    
    st.markdown("""
    **Understanding the Magnitude of Change:**
    
    The revised strategy represents a **50-year acceleration** in the net-zero timeline (2050 vs 2100). This is 
    extraordinary given that:
    
    **Fleet Lifespan Reality:**
    - Container vessels have **25-30 year operational lives**
    - A vessel ordered in 2024 will still be operating in 2050-2054
    - **This means vessels ordered TODAY must be net-zero compatible or risk becoming stranded assets**
    
    **Investment Implications:**
    - **US&#36;1-3 trillion** estimated global maritime industry investment needed by 2050
    - Includes new vessel designs, fuel production infrastructure, bunkering facilities, port equipment
    - **Annual investment: US&#36;40-120 billion** required across industry
    
    **Technology Challenge:**
    - Some required technologies (green ammonia engines, large-scale hydrogen carriers) **not yet commercially proven**
    - Must go from R&D → commercial deployment → global scale in 20-25 years
    - Historical precedent: Previous fuel transitions (coal→oil, diesel→HFO) took 40-50 years
    
    The lecture materials' visualization shows the divergence between the "Initial GHG Strategy" (gradual decline to 
    50% by 2050) and "Revised Strategy" (steep decline to net-zero by 2050)—the gap between these curves represents 
    the accelerated ambition and intensified challenge the industry now faces.
    """)
    
    st.markdown('<p class="subsection-header">Regulatory Framework and Enforcement</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Key IMO Regulations Driving Decarbonization:**
    
    **1. EEDI (Energy Efficiency Design Index) - Mandatory Since 2013:**
    - Applies to **new ship designs**
    - Sets minimum energy efficiency standards based on vessel type and size
    - **Phases**: Progressive tightening every 5 years (Phase 0→1→2→3, now entering Phase 4)
    - **Phase 3 (2022-2025)**: 30% more efficient than baseline
    - **Phase 4 (2025+)**: 40%+ more efficient than baseline
    - **Enforcement**: Ships not meeting EEDI cannot receive certification (cannot operate internationally)
    
    **2. SEEMP (Ship Energy Efficiency Management Plan) - Required Since 2013:**
    - Mandatory for **all existing ships**
    - Requires vessels to develop and implement plans to improve operational efficiency
    - Includes: Fuel consumption monitoring, efficiency measures implementation, continuous improvement
    - **Enforcement**: Port state control inspections verify SEEMP compliance
    
    **3. CII (Carbon Intensity Indicator) - Mandatory Since 2023:**
    - **Annual rating system**: Ships graded A (best) through E (worst) based on actual carbon intensity performance
    - **Calculation**: Grams of CO₂ emitted per tonne-mile of cargo transport
    - **Consequences**:
      - Ships rated D for 3 consecutive years OR E for 1 year must submit corrective action plan
      - Poor CII ratings damage commercial reputation (charterers avoid low-rated vessels)
      - May face higher insurance premiums, port dues
    - **Strategic impact**: Forces shipowners to optimize operations—slow steaming, route optimization, hull cleaning
    
    **4. EU ETS (Emissions Trading System) - Maritime Included from 2024:**
    - **Coverage**: 50% of emissions from voyages to/from EU ports + 100% of emissions within EU
    - **Mechanism**: Shipping companies must purchase carbon allowances for emissions
    - **Cost**: ~€80-100 per tonne of CO₂ (2024 prices, expected to rise)
    - **Impact**: Adds significant operational costs—example: 10,000 TEU vessel Asia-Europe round trip generates 
      ~3,000 tonnes CO₂ in EU waters = €240-300K carbon cost per voyage
    - **Drives change**: Creates strong economic incentive to reduce emissions (lower fuel consumption, alternative fuels)
    
    **5. FuelEU Maritime - EU Regulation from 2025:**
    - Sets **maximum greenhouse gas intensity limits** for fuels used by vessels calling EU ports
    - **Progressive tightening**: Limits reduce 2% by 2025, 6% by 2030, 13% by 2035, etc.
    - **Enforcement**: Non-compliant vessels pay penalties OR must use lower-carbon fuels
    - **Goal**: Force transition away from conventional marine fuel oil toward alternatives
    
    **The Compliance Cascade:**
    
    These regulations create a **reinforcing cycle of pressure**:
    1. **EEDI** → New vessels must be efficient (design constraint)
    2. **CII** → Existing vessels must operate efficiently (operational constraint)  
    3. **EU ETS** → Carbon has a price (economic constraint)
    4. **FuelEU** → Fuel carbon intensity capped (fuel constraint)
    5. **IMO 2050 net-zero** → Ultimate constraint—zero-carbon fuels required
    
    Shipowners face choice: **Adapt proactively OR face escalating costs and competitive disadvantage.**
    """)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ The Existential Challenge:</strong> Achieving net-zero by 2050 requires:<br><br>
    <strong>Complete Fleet Transformation:</strong> Global merchant fleet of 100,000+ vessels must transition to 
    zero-carbon fuels within 26 years. At current new-building rates (~2,000 vessels/year), this means <strong>EVERY 
    new vessel from now through 2050 must be zero-carbon capable</strong>, AND ~40,000 existing vessels must either 
    be retrofitted or scrapped early.<br><br>
    <strong>Fuel Infrastructure Revolution:</strong> Need to build <strong>zero-carbon fuel production capacity 
    equivalent to 300+ million tonnes per year</strong> (current marine fuel consumption), plus bunkering facilities 
    at 2,000+ ports globally. Current zero-carbon marine fuel production: <1 million tonnes/year = <0.3% of target.<br><br>
    <strong>Economic Burden:</strong> Alternative fuels currently cost <strong>2-4× conventional marine fuel</strong>. 
    At current prices, industry fuel costs would increase from ~US&#36;200 billion/year to US&#36;400-800 billion/year. 
    This must be passed through supply chains or absorbed by industry.<br><br>
    <strong>Technology Gaps:</strong> Some required technologies (large-scale green ammonia engines, hydrogen carriers) 
    <strong>not yet commercially proven</strong>. Must complete R&D, testing, commercialization, and global deployment 
    in 15-20 years.<br><br>
    <strong>This is not just an engineering challenge—it's an economic, political, and social transformation 
    unprecedented in maritime history.</strong>
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 2: Alternative Fuels - The Technology Landscape
    # ============================================================================
    
    st.markdown('<p class="section-header">Alternative Marine Fuels: Comprehensive Technology Assessment</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Achieving net-zero emissions requires transitioning from fossil-based marine fuels to **zero-carbon alternatives**. 
    Multiple fuel options are being pursued simultaneously, each with distinct advantages, challenges, and readiness 
    levels. The industry has not yet converged on a single "winning" fuel—suggesting multiple fuels will coexist through 
    2050 and beyond, with different fuels optimal for different vessel types and routes.
    
    The lecture materials provide verified data on **global bunkering availability** and **fleet adoption statistics** 
    that reveal which fuels are scaling fastest.
    """)
    
    st.markdown('<p class="subsection-header">1. Liquefied Natural Gas (LNG) - The Transition Fuel</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Current Status:** Most mature alternative fuel, widely deployed today
    
    **Global Infrastructure (Lecture Materials Verified):**
    - **185 ports worldwide** offer LNG bunkering capability
    - **Geographic distribution**: 41% Asia, 28% Europe, 16% North America, 15% other regions
    - **Growth trajectory**: 50+ new LNG bunkering ports added 2020-2024
    - **Bunkering vessels**: 80+ dedicated LNG bunker vessels operating globally
    
    **Technical Characteristics:**
    
    **Emissions Performance:**
    - **CO₂ reduction**: 20-25% less than conventional Heavy Fuel Oil (HFO)
    - **SOx reduction**: Near-zero (99%+ reduction)—critical for SECA (Sulphur Emission Control Area) compliance
    - **NOx reduction**: 85-90% less than HFO
    - **Particulate matter**: 95%+ reduction
    - **Methane slip concern**: Unburned methane emissions (potent GHG, 25-28× CO₂ warming potential over 100 years)
    
    **Engine Technology:**
    - **Dual-fuel engines**: Can run on LNG OR conventional fuel (operational flexibility)
    - **Technology maturity**: Proven, commercially available from major engine manufacturers (MAN, Wärtsilä, WinGD)
    - **Retrofit possibility**: Existing vessels can be converted to LNG (expensive: US&#36;30-60M per vessel)
    
    **Fleet Adoption (Real-World Statistics):**
    
    The lecture materials cite **CMA CGM** (one of world's largest container shipping lines) as a leading adopter:
    
    **CMA CGM's LNG Fleet Strategy:**
    - **32 dual-fuel LNG vessels** operating as of 2022
    - **77 dual-fuel vessels planned** by 2026 (includes vessels under construction and on order)
    - **Strategic quote from lecture materials**: *"Most advanced solution to preserve air quality, prevent ocean 
      acidification and initiate our energy transition"*
    - **Business case**: LNG vessels enable compliance with tightening emissions regulations while using commercially 
      available fuel
    
    **Global Fleet Adoption:**
    - **~400 LNG-powered vessels** in operation globally (2024)
    - **~300 LNG-capable vessels** on order
    - **Vessel types**: Predominantly cruise ships (60+), ferries (150+), some container ships, tankers, bulk carriers
    - **Market share**: Still <2% of global merchant fleet but growing rapidly
    
    **Advantages:**
    - **Available NOW**: Infrastructure exists, fuel supply established, technology proven
    - **Regulatory compliance**: Meets all current IMO regulations, EU ETS-favorable vs HFO
    - **Cost competitive**: LNG prices often comparable or lower than low-sulfur fuel oil (LSFO)
    - **No infrastructure lock-in**: LNG bunkering infrastructure can potentially be adapted for bio-LNG or synthetic LNG
    - **Operational flexibility**: Dual-fuel engines provide fallback to conventional fuel if LNG unavailable
    
    **Disadvantages and Limitations:**
    - **Still a fossil fuel**: LNG is natural gas (methane)—not zero-carbon
    - **Cannot achieve 2050 net-zero alone**: 20-25% CO₂ reduction insufficient for IMO targets
    - **Methane slip**: Unburned methane emissions partially offset CO₂ benefits (highly dependent on engine technology)
    - **Stranded asset risk**: LNG vessels may become obsolete before end of 25-30 year lifespan if regulations tighten
    - **Carbon lock-in**: Building LNG infrastructure might delay transition to truly zero-carbon fuels
    
    **Strategic Role:**
    
    LNG is best understood as a **"transition fuel"**—a stepping stone from conventional fuels to zero-carbon alternatives:
    - **Near-term (2024-2030)**: Helps industry meet IMO 2030 target (-40% carbon intensity)
    - **Medium-term (2030-2040)**: Buys time for zero-carbon fuel technologies to mature and scale
    - **Long-term (2040-2050)**: Must be phased out in favor of green methanol, green ammonia, or bio-LNG/synthetic LNG
    
    The lecture materials position LNG as *"an important steppingstone"* toward full decarbonization—acknowledging it's 
    not the final destination but a necessary bridge.
    """)
    
    st.markdown('<p class="subsection-header">2. Methanol - The Leading Zero-Carbon Candidate</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Current Status:** Rapidly scaling, increasingly viewed as leading zero-carbon fuel for container shipping
    
    **Global Infrastructure (Lecture Materials Verified):**
    - **122 ports worldwide** currently offer methanol bunkering
    - **Geographic distribution**: ~50% Europe and North America, relatively few in Asia (infrastructure gap)
    - **Growth trajectory**: 40+ ports added methanol bunkering capability 2022-2024
    - **Singapore positioning**: Building methanol bunkering capabilities as part of Future Fuels Port Network
    
    **Methanol Variants (Critical Distinction):**
    
    **Grey Methanol (Fossil-Based):**
    - **Production**: Synthesized from natural gas via steam methane reforming
    - **CO₂ reduction**: ~10-15% vs conventional marine fuel (modest improvement)
    - **Availability**: Abundant—global methanol production ~110 million tonnes/year (primarily for chemicals)
    - **Cost**: US&#36;300-400 per tonne (vs US&#36;400-600 for marine fuel oil)
    - **Strategic role**: Transition fuel, enables engine/infrastructure development
    
    **Bio-Methanol (Biomass-Based):**
    - **Production**: Produced from sustainable biomass (agricultural waste, forestry residues, municipal solid waste)
    - **CO₂ reduction**: 65-95% vs conventional fuel (lifecycle analysis, depending on feedstock)
    - **Availability**: Limited—current production ~1-2 million tonnes/year
    - **Cost**: US&#36;500-700 per tonne (1.5-2× grey methanol)
    - **Sustainability concerns**: Feedstock availability limits scale potential
    
    **Green Methanol (E-Methanol, Renewable-Based):**
    - **Production**: Synthesized from captured CO₂ + green hydrogen (from renewable electricity electrolysis)
    - **CO₂ reduction**: 100% zero-carbon (carbon-neutral—CO₂ emitted during combustion equals CO₂ captured during production)
    - **Availability**: Tiny—pilot projects, <100,000 tonnes/year production capacity (2024)
    - **Cost**: US&#36;800-1,200+ per tonne (2-3× conventional fuel, expected to decline with scale)
    - **Strategic role**: Ultimate target—scalable to industry needs without feedstock constraints
    
    **Technical Characteristics:**
    
    **Handling and Safety:**
    - **Form**: Liquid at ambient temperature and pressure (major advantage vs cryogenic fuels)
    - **Energy density**: ~50% of conventional fuel by volume (vessels need 2× larger fuel tanks)
    - **Toxicity**: Toxic but less so than ammonia—established handling protocols exist (methanol widely used in chemical industry)
    - **Fire safety**: Lower flashpoint than diesel but manageable with proper procedures
    - **Existing supply chains**: Methanol already shipped globally as chemical feedstock—infrastructure partially exists
    
    **Engine Technology:**
    - **Dual-fuel engines**: Can operate on methanol OR conventional fuel (redundancy, flexibility)
    - **Technology readiness**: Commercial engines available (MAN, WinGD)—proven technology
    - **Retrofit potential**: Possible but expensive (US&#36;20-40M per vessel depending on size)
    - **Pure methanol engines**: Under development—higher efficiency, purpose-built for methanol
    
    **Fleet Adoption (Real-World Statistics):**
    
    The lecture materials provide verified order statistics showing **methanol's rapid growth**:
    
    **CMA CGM's Methanol Strategy:**
    - **18 e-methanol ready vessels ordered** (as of 2024)
    - Positioned as part of *"large energy mix"* strategy
    - Hedging bets: LNG + methanol + exploring other alternatives
    
    **Global Methanol Fleet Growth:**
    - **~25 methanol-powered vessels** operating (2024)—mostly smaller vessels and ferries
    - **~150+ methanol-capable vessels** on order—**explosive growth in orders 2022-2024**
    - **Major container lines committing**: Maersk (19 vessels), CMA CGM (18), MSC, Hapag-Lloyd
    - **Trend**: Container shipping industry converging on methanol as preferred fuel
    
    **Why Container Shipping Favors Methanol:**
    
    **Operational Advantages:**
    - **Liquid handling**: Container ships operate on tight schedules—liquid bunkering faster than cryogenic fuels
    - **Tank space**: Container vessels have flexibility to allocate space for larger fuel tanks (vs bulk carriers, tankers with less flexibility)
    - **High-value cargo**: Container shipping can absorb higher fuel costs (cargo value US&#36;10,000-50,000+ per TEU)
    - **Regulatory exposure**: Container ships call at many EU ports—high EU ETS exposure incentivizes lower-carbon fuels
    
    **Advantages:**
    - **Zero-carbon pathway**: Green methanol achieves 100% decarbonization (scalable without feedstock limits)
    - **Liquid fuel**: Easier handling than cryogenic (LNG, LH₂) or toxic (ammonia) alternatives
    - **Infrastructure partially exists**: Methanol supply chains, storage, safety protocols already established
    - **Drop-in potential**: With some modifications, can use existing port infrastructure
    - **Dual-fuel flexibility**: Engines can switch between methanol and conventional fuel (risk mitigation)
    
    **Disadvantages and Challenges:**
    - **Green methanol scarce**: Production capacity far below shipping industry needs (<0.1% of requirement)
    - **High cost**: Green methanol 2-3× conventional fuel cost—adds US&#36;500-1,000+ per TEU to Asia-Europe routes
    - **Energy density penalty**: 50% energy density → need 2× fuel tank volume (design constraint)
    - **Production scaling challenge**: Need to build ~200-300 million tonnes/year green methanol production by 2050 
      (current capacity <0.1 million)—requires massive renewable energy and CO₂ capture infrastructure
    - **Cost pass-through**: Shipping lines must convince customers to pay green premium (ongoing negotiation)
    
    **Strategic Assessment:**
    
    The lecture materials' data showing **150+ methanol vessels on order** (vs ~400 LNG vessels in operation) reveals 
    industry momentum shifting toward methanol for **new builds**, particularly in container shipping. Methanol is 
    emerging as the leading candidate for achieving IMO 2050 net-zero in container sector, with expectation that green 
    methanol production will scale through 2030s-2040s to meet demand.
    
    The lecture materials reference industry collaboration: CMA CGM working on *"bio-methane"* projects (Salamandre/Titan), 
    indicating multi-fuel approach: LNG today → bio-LNG/bio-methanol near-term → green methanol long-term.
    """)
    
    st.markdown('<p class="subsection-header">3. Ammonia (NH₃) - The Long-Term Zero-Carbon Fuel</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Current Status:** Emerging technology, expected to play major role 2030s-2050 for long-haul bulk shipping
    
    **Why Ammonia?**
    
    **Zero-Carbon Potential:**
    - **Combustion product**: NH₃ → N₂ (nitrogen) + H₂O (water)—**zero CO₂ emissions**
    - **Energy carrier**: Efficient way to store and transport hydrogen (hydrogen "carrier molecule")
    - **Green ammonia**: Produced from green hydrogen (renewable electricity electrolysis) + nitrogen from air (Haber-Bosch process)
    
    **Technical Characteristics:**
    
    **Physical Properties:**
    - **Form**: Liquid under moderate pressure (~8-10 bar at ambient temperature) OR ambient pressure at -33°C
    - **Energy density**: ~50% of conventional fuel by volume (similar to methanol)
    - **Toxicity**: **HIGHLY TOXIC**—NH₃ gas is corrosive, irritant, fatal at high concentrations
    - **Handling complexity**: Requires specialized equipment, training, safety protocols far beyond conventional fuels
    
    **Engine Technology:**
    - **Combustion engines**: Ammonia can be burned in modified marine engines (development stage)
    - **Challenges**: Low flame speed, high ignition temperature requires pilot fuel (typically diesel or hydrogen)
    - **NOx emissions**: Combustion produces NOx (nitrogen oxides)—requires selective catalytic reduction (SCR) systems
    - **Technology readiness**: **Pilot projects only**—first commercial ammonia-powered vessels expected 2025-2027
    - **Major manufacturers**: MAN, Wärtsilä, WinGD developing ammonia engines
    
    **Fuel Cells:**
    - **Alternative**: Solid oxide fuel cells (SOFC) can use ammonia directly—potentially higher efficiency
    - **Technology readiness**: Early research stage—commercial availability uncertain
    
    **Current Development Status:**
    
    **Vessel Orders:**
    - **~30 ammonia-ready vessels** on order (2024)—primarily bulk carriers and tankers
    - **Shipping companies**: NYK, Mitsui O.S.K. Lines (MOL), Maersk exploring ammonia
    - **Focus sectors**: Long-haul bulk carriers, tankers (less passenger exposure, longer routes justify complexity)
    
    **Infrastructure:**
    - **Bunkering facilities**: Virtually none exist today for marine fuel use
    - **Production capacity**: Green ammonia production <1 million tonnes/year (marine fuel needs: 200-300 million tonnes/year)
    - **Pilot projects**: Singapore, Rotterdam, Japan developing ammonia bunkering capabilities
    
    **Advantages:**
    - **Zero-carbon**: True zero-carbon fuel when produced from green hydrogen
    - **No CO₂ capture required**: Unlike e-methanol which needs CO₂ feedstock
    - **Existing production**: Ammonia produced at scale today (~180 million tonnes/year globally) for agriculture 
      (fertilizer)—production infrastructure partially exists
    - **Energy density**: Better than hydrogen (11× more hydrogen per unit volume when stored as ammonia)
    - **Long-range capability**: Suitable for long transoceanic routes (unlike batteries or hydrogen)
    
    **Disadvantages and Major Challenges:**
    - **Extreme toxicity**: NH₃ leaks could be catastrophic—crew safety, port safety, public acceptance concerns
    - **Handling complexity**: Requires extensive safety systems, crew training, emergency response protocols
    - **Unproven technology**: No commercial ammonia-powered ocean-going vessels operating (2024)
    - **NOx emissions**: Combustion produces NOx—requires additional abatement systems
    - **High cost**: Green ammonia expensive (US&#36;600-1,000+ per tonne)—economics unclear
    - **Regulatory uncertainty**: IMO still developing ammonia safety codes (expected 2025-2027)
    - **Public perception**: Toxic fuel on large ships calling at ports near populated areas—acceptance issues
    
    **Strategic Role:**
    
    The lecture materials categorize ammonia as part of long-term strategy: *"Methanol, ammonia and hydrogen will 
    represent most of the fuel mix by 2050."* This positions ammonia as a **2030s-2050 solution** rather than 
    near-term option.
    
    **Most likely adoption pattern:**
    - **2025-2030**: Pilot vessels, initial commercial deployments
    - **2030-2040**: Scaling up for bulk carriers, tankers, long-haul routes (less safety-sensitive applications)
    - **2040-2050**: Potential major role if safety concerns managed, costs decline, infrastructure scales
    
    Ammonia is **higher-risk, higher-complexity** than methanol but may be essential for certain vessel types and routes 
    where methanol's lower energy density is prohibitive.
    """)
    
    st.markdown('<p class="subsection-header">4. Hydrogen (H₂) - The Niche Application Fuel</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Current Status:** Limited deployment, primarily short-range and harbor craft applications
    
    **Why Hydrogen is Challenging for Shipping:**
    
    **The Energy Density Problem:**
    - **Volumetric energy density**: Hydrogen has extremely low energy density by volume
    - **Compressed hydrogen (700 bar)**: ~5% the energy density of diesel
    - **Liquid hydrogen (-253°C)**: ~25% the energy density of diesel
    - **Implication**: Vessel needs 4-20× larger fuel tanks vs diesel—impractical for long-haul cargo vessels
    
    **Storage Options and Tradeoffs:**
    
    **Compressed Gas (CGH₂):**
    - Storage: Ultra-high pressure tanks (350-700 bar)
    - Advantage: Simpler than cryogenic
    - Disadvantage: Extremely low energy density, heavy pressure vessels
    - Applications: Very short routes, harbor craft only
    
    **Liquid Hydrogen (LH₂):**
    - Storage: Cryogenic tanks at -253°C (20K above absolute zero)
    - Advantage: Higher energy density than compressed
    - Disadvantage: Energy-intensive liquefaction, boil-off losses (1-5% per day), complex insulation
    - Applications: Potentially medium-range ferries, naval vessels
    
    **Fuel Cells:**
    - **Proton Exchange Membrane (PEM) fuel cells**: High efficiency (~50-60% vs ~40% for combustion engines)
    - **Zero emissions**: H₂ + O₂ → H₂O + electricity (only byproduct is water)
    - **Challenge**: Expensive (US&#36;3,000-5,000 per kW vs US&#36;300-500 for diesel engine)
    
    **Current Applications:**
    
    **Ferries and Harbor Craft:**
    - **~10 hydrogen fuel cell ferries** operating globally (Norway, Japan, UK)
    - **Short routes**: Typically <50 km, frequent refueling possible
    - **Demonstration projects**: Proving technology feasibility
    
    **Advantages:**
    - **True zero-emission**: Only byproduct is water vapor
    - **High efficiency**: Fuel cells more efficient than combustion engines
    - **Fast refueling**: Faster than battery recharging (vs electric vessels)
    - **Suitable for short-range**: Harbor craft, tugs, short-route ferries
    
    **Disadvantages:**
    - **Energy density**: Prohibitively low for long-haul shipping
    - **Cost**: Extremely expensive—fuel cells, storage systems, fuel production
    - **Infrastructure**: Virtually no hydrogen bunkering infrastructure exists
    - **Safety concerns**: Hydrogen extremely flammable, leaks easily (smallest molecule)
    - **Fuel production**: Green hydrogen production requires massive renewable electricity capacity
    
    **Strategic Role:**
    
    Hydrogen will likely remain a **niche application** in maritime:
    - **Harbor craft**: Tugs, pilot boats, ferries within ports
    - **Short-range ferries**: Routes <100 km with frequent port calls
    - **Hydrogen carrier**: May be transported as ammonia or LOHC (Liquid Organic Hydrogen Carrier) rather than pure H₂
    
    For deep-sea shipping, hydrogen's role will primarily be as a **feedstock for other fuels** (green ammonia, 
    e-methanol, e-LNG) rather than direct use as marine fuel.
    """)
    
    st.markdown('<p class="subsection-header">5. Biofuels - The Drop-In Supplement</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Current Status:** Available today, limited by feedstock availability
    
    **Types of Marine Biofuels:**
    
    **FAME (Fatty Acid Methyl Ester) Biodiesel:**
    - Production: From vegetable oils, animal fats via transesterification
    - Blending: Typically B7-B20 (7-20% biodiesel, 80-93% conventional diesel)
    - Compatibility: Good with existing engines up to B20
    
    **HVO (Hydrotreated Vegetable Oil):**
    - Production: Advanced process, chemically identical to fossil diesel
    - Blending: Can be 100% pure HVO (drop-in replacement)
    - Performance: Superior to FAME (better cold-weather performance, longer storage stability)
    
    **Bio-LNG:**
    - Production: Upgrading biogas from organic waste (landfills, agricultural waste, wastewater treatment)
    - Compatibility: Chemically identical to fossil LNG—direct drop-in
    - Availability: Limited—<5 million tonnes/year global production capacity
    
    **The lecture materials reference**: CMA CGM working on *"bio-methane"* (bio-LNG), noting: *"Same molecule can 
    be created through biological waste and reduce carbon emissions by 67%."* This references bio-LNG's **67% lifecycle 
    CO₂ reduction** vs fossil LNG (accounting for methane emissions from organic waste that would otherwise decompose).
    
    **Advantages:**
    - **Drop-in fuel**: No engine modifications required (up to certain blend percentages)
    - **Existing infrastructure**: Can use current bunkering facilities
    - **Immediate availability**: Can deploy today
    - **Significant CO₂ reduction**: 65-95% depending on feedstock and production pathway
    
    **Disadvantages and Limitations:**
    
    **The Fundamental Constraint - Feedstock Availability:**
    - Global marine fuel consumption: ~300 million tonnes/year
    - Sustainable biomass availability for marine biofuels: **~30-50 million tonnes/year** (10-15% of need)
    - **Cannot scale** to meet entire industry demand without competing with food production, causing deforestation
    
    **Cost:**
    - Biofuels typically **2-3× conventional fuel cost**
    - HVO: US&#36;800-1,200 per tonne vs US&#36;500-600 for marine diesel
    - Bio-LNG: US&#36;600-900 per tonne vs US&#36;400-500 for fossil LNG
    
    **Sustainability Concerns:**
    - **Food vs fuel debate**: Using arable land for fuel crops competes with food production
    - **Indirect land use change (ILUC)**: Biofuel crop expansion can drive deforestation elsewhere
    - **Certification essential**: Need robust sustainability certification (ISCC, RSB) to ensure truly sustainable sourcing
    
    **Strategic Role:**
    
    Biofuels are best understood as a **"drop-in supplement"** rather than complete solution:
    - **Near-term emissions reduction**: Blend 10-30% biofuel with conventional fuel for immediate CO₂ reduction
    - **High-value routes**: Premium services willing to pay green premium (luxury cruise ships, container lines with 
      corporate sustainability commitments)
    - **Bridging role**: Helps meet interim targets while zero-carbon fuels scale up
    - **Not scalable**: Cannot replace 300 million tonnes/year marine fuel consumption sustainably
    
    The lecture materials position biofuels as part of bridging strategy: *"Biofuels, methanol and blue ammonia will 
    help bridge the gap"* (between LNG transition fuels and long-term zero-carbon fuels).
    """)
    
    # Comprehensive alternative fuels comparison table
    fuels_comprehensive = pd.DataFrame({
        'Fuel Type': [
            'Conventional Marine Fuel (HFO/LSFO)',
            'LNG (Fossil)',
            'Bio-LNG',
            'Grey Methanol',
            'Bio-Methanol',
            'Green Methanol (E-Methanol)',
            'Blue Ammonia',
            'Green Ammonia',
            'Green Hydrogen',
            'Biofuels (HVO/FAME)'
        ],
        'CO₂ Reduction vs Baseline': [
            '0% (baseline)',
            '20-25%',
            '65-75%',
            '10-15%',
            '65-95%',
            '95-100% (carbon neutral)',
            '80-90%',
            '95-100% (zero carbon)',
            '100% (zero carbon)',
            '65-95%'
        ],
        'Technology Readiness (2024)': [
            'Mature (baseline)',
            'Commercial (400+ vessels operating)',
            'Early commercial (pilot scale)',
            'Commercial (chemicals industry)',
            'Pilot scale',
            'Demonstration (pilot projects)',
            'Early development',
            'Early development (pilots expected 2025-27)',
            'Demonstration (ferries/harbor craft only)',
            'Commercial (road transport, aviation)'
        ],
        'Global Bunkering Infrastructure': [
            '2,000+ ports',
            '185 ports',
            '<10 ports',
            '122 ports',
            '10-20 ports',
            '5-10 ports',
            'None (planned)',
            'None (planned)',
            '<5 ports',
            '50+ ports'
        ],
        'Fuel Cost (Relative)': [
            '1.0× (US&#36;500-600/tonne)',
            '0.8-1.2× (competitive)',
            '1.5-2.0×',
            '0.6-0.8×',
            '1.5-2.5×',
            '2.0-3.0×',
            '1.5-2.0×',
            '2.0-3.0×',
            '3.0-5.0×',
            '2.0-3.0×'
        ],
        'Energy Density (vs Conventional)': [
            '100% (baseline)',
            '~60% (cryogenic)',
            '~60% (cryogenic)',
            '~50% (liquid)',
            '~50% (liquid)',
            '~50% (liquid)',
            '~45% (liquid)',
            '~45% (liquid)',
            '~5-25% (compressed/liquid)',
            '~90-95% (liquid)'
        ],
        'Primary Challenges': [
            'High emissions, regulatory pressure',
            'Still fossil fuel, methane slip, stranded asset risk',
            'Feedstock limited, high cost, sustainability concerns',
            'Modest CO₂ reduction, still fossil-based',
            'Feedstock limited, medium cost',
            'Very high cost, production capacity tiny, scaling challenge',
            'Medium CO₂ reduction, NOx emissions',
            'Toxicity, unproven technology, high cost, NOx emissions',
            'Extremely low energy density, very high cost, infrastructure absent',
            'Cannot scale (feedstock limits), food vs fuel, high cost'
        ],
        'Strategic Role (2024-2050)': [
            'Phase out by 2040-2050',
            'Transition fuel (2024-2040), phase out by 2050',
            'Niche supplement, limited scale',
            'Near-term bridge (2024-2035)',
            'Near-term supplement, limited scale',
            'Leading long-term candidate for container ships (2030-2050)',
            'Medium-term option if blue hydrogen scales',
            'Long-term candidate for bulk carriers/tankers (2030-2050)',
            'Niche applications (harbor craft, short ferries)',
            'Supplement/blending, cannot replace fossil fuels entirely'
        ],
        'Vessel Types Most Suitable': [
            'All (current)',
            'Cruise, container, some tankers/bulkers',
            'Same as LNG (limited supply)',
            'Container ships (liquid handling ease)',
            'Container ships, short-sea',
            'Container ships (liquid handling, schedule-sensitive)',
            'Bulk carriers, tankers (long routes)',
            'Bulk carriers, tankers (long routes, less safety-sensitive)',
            'Harbor craft, tugs, short ferries only',
            'All vessel types (blending), premium services'
        ]
    })
    
    st.dataframe(fuels_comprehensive, width='stretch', hide_index=True)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🎯 Industry Trends - What the Data Reveals:</strong><br><br>
    <strong>LNG Dominance Today (2024):</strong> 185 bunkering ports, 400+ vessels operating, mature technology → 
    <strong>clear leader for 2024-2030</strong> timeframe<br><br>
    <strong>Methanol's Explosive Growth (2022-2024):</strong> 122 bunkering ports, 150+ vessels on order (vs only ~25 
    operating) → <strong>industry converging on methanol for new container ship builds</strong><br><br>
    <strong>Ammonia's Future Potential:</strong> Only ~30 vessels on order, zero infrastructure, unproven technology → 
    <strong>high-risk 2030s-2050 bet, primarily bulk carriers/tankers</strong><br><br>
    <strong>Multi-Fuel Hedging Strategy:</strong> CMA CGM's approach (32 LNG + 77 planned LNG + 18 methanol + biomethane 
    R&D) exemplifies industry strategy → <strong>don't bet on single fuel, build flexible portfolio</strong><br><br>
    <strong>The Uncertainty:</strong> No single fuel has emerged as clear "winner" for all vessel types and routes. 
    Most likely outcome: <strong>Multiple fuels coexist through 2050</strong>, with methanol dominant in container shipping, 
    ammonia in bulk/tanker segments, biofuels as supplements, LNG phasing out 2040-2050.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 3: Green Port Technologies and Initiatives
    # ============================================================================
    
    st.markdown('<p class="section-header">Green Port Technologies: Infrastructure for Sustainable Operations</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Ports play a critical role in maritime decarbonization by providing the **infrastructure, services, and ecosystem** 
    necessary for zero-carbon shipping. Green port initiatives span alternative fuel bunkering, equipment electrification, 
    renewable energy generation, and climate resilience.
    """)
    
    st.markdown('<p class="subsection-header">1. Alternative Fuel Bunkering Infrastructure</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Singapore's Future Fuels Port Network:**
    
    The lecture materials highlight Singapore's strategic initiative: **"Future Fuels Port Network"**—a collaboration 
    among ports globally to build alternative fuel bunkering infrastructure.
    
    **Singapore's Multi-Fuel Strategy:**
    
    **LNG Bunkering (Established):**
    - Singapore is **world's largest LNG bunkering hub**
    - 6+ LNG bunker vessels operating
    - 200,000+ tonnes LNG bunkered annually (2023)
    - Supporting LNG-powered vessels calling at Singapore
    
    **Methanol Bunkering (Developing):**
    - Pilot methanol bunkering programs launched 2023-2024
    - Building methanol storage facilities at Jurong Island (chemical hub)
    - Target: Establish methanol bunkering capability at Tuas by 2027-2030
    - Positioning: Be ready when methanol vessels enter service in volume (2025-2030)
    
    **Ammonia Bunkering (Future):**
    - Research phase: Safety protocols, handling procedures, infrastructure requirements
    - Target timeframe: 2030-2035 for commercial ammonia bunkering
    - Waiting for: Technology maturity, regulatory clarity (IMO ammonia fuel code expected 2025-2027)
    
    **Biofuels Supply:**
    - Already possible through existing infrastructure (drop-in fuels)
    - Building sustainable sourcing partnerships
    - Certification systems to ensure truly sustainable biofuels
    
    **Strategic Rationale:**
    
    **Bunkering is Sticky Business:**
    - Vessels bunker 60-80% of fuel at hub ports (where they spend most time)
    - **Lock-in effect**: Once bunkering infrastructure established, shipping lines commit to that port
    - **Singapore's goal**: Regardless of which fuel(s) win long-term, Singapore has infrastructure to supply it
    
    **Network Effects:**
    - Future Fuels Port Network creates **coordinated alternative fuel availability** across major routes
    - Example: If Singapore, Rotterdam, and Dubai all offer methanol, shipping lines can confidently order methanol 
      vessels knowing fuel available at major ports
    - Reduces "chicken and egg" problem: Need vessels to justify infrastructure, need infrastructure to order vessels
    
    **Investment Scale:**
    - Alternative fuel infrastructure at major port: US&#36;200-500 million per fuel type
    - Includes: Storage tanks, bunkering vessels, pipelines, safety systems, fire protection, training facilities
    - Singapore committing: Multi-billion dollar investment across multiple fuels over next decade
    """)
    
    st.markdown('<p class="subsection-header">2. Equipment Electrification and Renewable Energy</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Tuas Mega Port - Zero Emissions Operations:**
    
    The lecture materials emphasize Tuas as **"Smarter, greener and automated"**—designed from the ground up for 
    sustainability:
    
    **Electrified Terminal Equipment:**
    
    **Quay Cranes:**
    - All quay cranes electric-powered (grid electricity, not diesel generators)
    - **Zero local emissions** during operations
    - Regenerative braking systems recover energy when lowering containers
    
    **AGV Fleet (1,000+ vehicles):**
    - **Battery-electric automated guided vehicles** (zero emissions)
    - Automated charging stations (vehicles charge during idle periods)
    - Eliminates: Diesel prime movers that would generate ~50,000 tonnes CO₂/year
    
    **ARMG Yard Cranes (200+ cranes):**
    - **Electric rail-mounted gantry cranes** (zero diesel)
    - Grid-powered operations
    - Regenerative systems capture energy from lowering containers
    
    **Result**: Tuas terminal equipment generates **~80-90% less local emissions** vs conventional diesel-powered terminals
    
    **Renewable Energy Generation:**
    
    **Solar Power Deployment:**
    - **Extensive rooftop solar** on terminal buildings, warehouses, office facilities
    - **Solar canopies** over parking areas, walkways
    - **Target capacity**: 40-60 MW solar generation (when Tuas fully developed)
    - **Annual output**: ~50-80 GWh electricity/year (offset ~10-15% of Tuas electricity consumption)
    
    **Grid Integration:**
    - Connection to Singapore's electrical grid (which is transitioning to renewables)
    - Singapore target: 30% solar + imported renewable electricity by 2030
    - Tuas benefits as grid decarbonizes over time
    
    **Climate Resilience Infrastructure:**
    
    **Elevated Construction (+5m Above Sea Level):**
    - Tuas built at +5 meters (vs +3m at existing terminals)
    - Protection against **2-3 meter sea level rise** by 2100 (even under pessimistic scenarios)
    - **40-50+ year operational life** guaranteed regardless of climate change impacts
    
    **Extreme Weather Preparedness:**
    - Reinforced structures for potential increased storm intensity
    - Flood management systems
    - Redundant power systems (terminal can operate during grid disruptions)
    """)
    
    st.markdown('<p class="subsection-header">3. Shore Power (Cold Ironing)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **What is Shore Power?**
    
    Shore power (also called "cold ironing") enables vessels to **plug into electrical grid while berthed**, allowing 
    them to **shut down auxiliary diesel generators** that normally run 24/7 to power onboard systems (lighting, 
    ventilation, refrigeration, accommodation).
    
    **Emissions Impact:**
    
    **Vessel at Berth:**
    - Large container vessel at berth: Auxiliary engines consume 50-100 tonnes heavy fuel oil per day
    - Emissions: 150-300 tonnes CO₂ per day + NOx, SOx, particulates
    - **Singapore average vessel stay**: 24 hours → 150-300 tonnes CO₂ per vessel call
    
    **Shore Power Benefits:**
    - Vessel shuts down diesel generators, connects to grid electricity
    - **Zero local emissions** (no exhaust in port area)
    - **Quieter operations** (no engine noise)
    - **CO₂ reduction**: Depends on grid electricity source (Singapore grid: ~30% reduction vs diesel generation)
    
    **Tuas Shore Power Design:**
    
    The lecture materials note Tuas designed with **shore power capability** from the start:
    - **All berths equipped** with shore power connection points
    - High-voltage electrical infrastructure (6.6-11 kV)
    - Automated connection systems (reduce crew workload)
    - **Frequency conversion**: Ships use different electrical frequencies (50Hz vs 60Hz depending on flag state)—
      Tuas has converters to accommodate all vessels
    
    **Adoption Challenges:**
    
    **Vessel-Side Requirements:**
    - Vessels must be **shore power-ready** (onboard electrical systems, connection equipment)
    - **Retrofit cost**: US&#36;500K - 2M per vessel depending on size
    - **Current fleet**: <5% of global fleet is shore power-ready (2024)
    
    **Economic Challenge:**
    - Shore power electricity cost must be **competitive with bunker fuel** for vessels to use it
    - Singapore approach: **Green Port Programme rebates** offset shore power costs
    - EU approach: Mandatory shore power use at major ports from 2030 (regulatory forcing)
    
    **Strategic Importance:**
    
    **Local Air Quality:**
    - Shore power eliminates port emissions (critical for ports near urban areas)
    - Health benefits: Reduced respiratory illnesses, hospital admissions in port-adjacent neighborhoods
    
    **Regulatory Compliance:**
    - **EU regulations**: Shore power mandatory at TEN-T core ports by 2030
    - **US California**: Shore power mandatory at California ports since 2014
    - Singapore positioning: Ready when regulations expand to Asia
    """)
    
    st.markdown('<p class="subsection-header">4. Green Port Programme and Incentives</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **MPA's Green Port Programme:**
    
    **Incentive Structure:**
    - Vessels receive **port due rebates** based on environmental performance
    - **Criteria**: NOx emissions, SOx emissions, CO₂ efficiency (based on EEDI, CII ratings)
    - **Rebate levels**: Up to 50% reduction in port dues for best-performing green vessels
    
    **Example Impact:**
    - Large container vessel call: Port dues ~US&#36;20-40K
    - Green vessel (LNG-powered, high EEDI rating, A/B CII rating): 25-50% rebate = US&#36;5-20K savings per call
    - **Annual savings** for vessels calling Singapore frequently: US&#36;100-500K
    
    **Strategic Effect:**
    - Creates **economic incentive** for shipping lines to invest in green technology
    - Vessels optimize operations to improve CII ratings (slow steaming, route optimization, hull cleaning)
    - Competitive advantage: Green vessels save costs vs competitors still using conventional fuel
    
    **Green Shipping Corridors:**
    
    **Concept:**
    - **Bilateral/multilateral agreements** between ports on specific routes
    - Preferential treatment for zero-carbon vessels
    - Coordinated alternative fuel availability
    
    **Singapore Participation:**
    - Green Corridor with Rotterdam (Asia-Europe route)
    - Collaboration with Los Angeles/Long Beach (trans-Pacific route)
    - **Goal**: Create "green lane" where zero-carbon vessels receive priority berthing, faster turnaround, lower fees
    """)
    
    # ============================================================================
    # SECTION 4: Digital Transformation and Innovation
    # ============================================================================
    
    st.markdown('<p class="section-header">Digital Transformation: The Fourth Industrial Revolution in Maritime</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Beyond physical decarbonization, the maritime industry is undergoing **digital transformation**—leveraging data, 
    AI, IoT, and automation to optimize operations, reduce waste, and improve efficiency.
    """)
    
    st.markdown('<p class="subsection-header">digitalPORT&#64;SG - Singapore\'s Maritime AI Platform</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Singapore's digitalPORT&#64;SG initiative** represents comprehensive digital transformation of port operations:
    
    **Core Capabilities:**
    
    **AI-Powered Berth Planning:**
    - Machine learning predicts vessel arrival times (±30 minutes accuracy 24 hours ahead)
    - Optimization algorithms allocate berths to maximize utilization while meeting service level targets (>90% BOA)
    - **Result**: 5-10% improvement in berth utilization = capacity increase without building new berths
    
    **Predictive Analytics:**
    - Equipment failure prediction using IoT sensor data
    - Maintenance scheduling optimization (perform maintenance during low-demand periods)
    - **Result**: 30-40% reduction in unplanned downtime
    
    **Real-Time Visibility:**
    - Track every container in Singapore port ecosystem in real-time
    - Vessel positions, container locations, truck movements, crane operations—all visible on single dashboard
    - **Result**: Faster exception handling, reduced dwell time, improved customer service
    
    **Optimization Engines:**
    - Yard stacking optimization (minimize re-handles)
    - Equipment routing (AGVs, cranes, trucks)
    - Gate scheduling (reduce truck congestion)
    
    **Integration:**
    - digitalPORT&#64;SG integrates with CITOS (PSA's Terminal Operating System)
    - Connection to PORTNET (Singapore maritime single window)
    - APIs for shipping lines, trucking companies, cargo owners
    """)
    
    st.markdown('<p class="subsection-header">Paperless Trade and Digital Documentation</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Paper Problem:**
    
    Traditional maritime trade generates **massive paper documentation**:
    - **Bills of Lading (B/L)**: Legal document of cargo ownership—typically 3-6 physical copies
    - **Certificates of Origin**: Customs documentation
    - **Cargo Manifests**: Detailed cargo listings
    - **Delivery Orders**: Authorization for cargo release
    
    **Costs of Paper:**
    - **Courier costs**: US&#36;50-100 per B/L set to send physical documents internationally
    - **Time delays**: 3-7 days for documents to reach destination (cargo often arrives before documents!)
    - **Errors**: Manual data entry errors in 5-10% of transactions
    - **Fraud risk**: Paper documents can be forged, lost, stolen
    
    **Digital Solutions:**
    
    **Electronic Bill of Lading (eBL):**
    - Digital document with cryptographic signatures
    - **Instant transfer**: Ownership transfer happens electronically in minutes (vs days for physical courier)
    - **Cost savings**: US&#36;50-100 saved per transaction
    - **Singapore implementation**: eBL platform connecting shipping lines, banks, cargo owners
    
    **Blockchain for Trade Finance:**
    - Distributed ledger ensures document authenticity
    - Reduces fraud, enables instant verification
    - Singapore piloting blockchain trade finance platforms
    
    **E-Bunker Delivery Notes (e-BDN):**
    - Digital documentation of fuel delivery to vessels
    - Eliminates paper-based bunker delivery notes
    - Faster processing, reduced errors
    
    **Benefits:**
    
    **Cost Reduction:**
    - Industry estimate: Digitalization saves **US&#36;50-100 per TEU** in documentation costs
    - Singapore throughput 41M TEU → **US&#36;2-4 billion annual savings potential** across supply chain
    
    **Time Savings:**
    - Document processing time: 3-7 days → minutes
    - Enables **just-in-time cargo release** (no waiting for documents to arrive)
    
    **Sustainability:**
    - Eliminate millions of sheets of paper annually
    - Reduce courier flights for document delivery
    - Lower carbon footprint of trade documentation
    """)
    
    st.markdown('<p class="subsection-header">BLOCK71 - Maritime Innovation Hub</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Singapore's BLOCK71** is a maritime technology innovation hub focused on accelerating maritime tech startups:
    
    **Focus Areas:**
    - **Decarbonization technologies**: Alternative fuels, energy efficiency, emissions monitoring
    - **Digitalization**: AI/ML for operations, IoT sensors, predictive analytics
    - **Automation**: Autonomous vessels, automated terminal equipment, drone inspections
    - **Sustainability**: Circular economy, waste reduction, green shipping
    
    **Support for Startups:**
    - Co-working space, mentorship from maritime industry veterans
    - Access to testbeds: digitalOCEANS simulation facility, MariOT cybersecurity lab
    - Funding: Government grants, connections to venture capital
    - Customer access: Introductions to PSA, MPA, shipping lines
    
    **Strategic Purpose:**
    
    **Innovation Ecosystem:**
    - Attract global maritime tech talent to Singapore
    - Accelerate commercialization of maritime innovations
    - Position Singapore as **maritime innovation hub** (not just logistics hub)
    
    **Examples of BLOCK71 Startups:**
    - Emissions monitoring platforms (real-time CO₂, NOx, SOx tracking)
    - AI-powered vessel routing optimization
    - Drone inspection services for vessel hulls, cranes
    - Blockchain supply chain traceability
    """)
    
    # ============================================================================
    # SECTION 5: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways: Green Maritime & Future Trends</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **IMO Decarbonization Strategy (Revised 2023):**
        - **2030 target**: 20-30% GHG reduction vs 2008
        - **2040 target**: 70-80% GHG reduction vs 2008
        - **2050 target**: Net-zero GHG emissions (50 years earlier than initial strategy!)
        - **Alternative fuel uptake**: 5-10% by 2030
        - **Regulatory enforcement**: EEDI, SEEMP, CII, EU ETS, FuelEU Maritime
        
        **Alternative Fuels Landscape:**
        - **LNG (185 ports)**: Transition fuel, 20-25% CO₂ reduction, 400+ vessels operating
        - **Methanol (122 ports)**: Leading zero-carbon candidate, 150+ vessels on order
        - **Green methanol**: 100% decarbonization, but very high cost (2-3× conventional)
        - **Ammonia**: Long-term zero-carbon, ~30 vessels on order, toxicity challenges
        - **Hydrogen**: Niche applications only (energy density too low for deep-sea)
        - **Biofuels**: Drop-in supplement, limited by feedstock (10-15% of industry needs)
        - **Multi-fuel strategy**: Industry hedging—no single winner clear
        
        **Real Fleet Adoption (Lecture Verified):**
        - **CMA CGM**: 32 LNG vessels operating, 77 dual-fuel planned by 2026, 18 methanol-ready ordered
        - **15% of fleet** projected to be green fuel by 2028
        - **Industry trend**: Container shipping converging on methanol for new builds
        """)
    
    with col2:
        st.markdown("""
        **Green Port Technologies:**
        - **Alternative fuel bunkering**: Singapore's Future Fuels Port Network
          - LNG established (world's largest hub)
          - Methanol developing (pilot programs 2023-2024)
          - Ammonia future (2030-2035 target)
        - **Equipment electrification**: Tuas 1,000+ AGVs, 200+ ARMGs (zero emissions)
        - **Shore power**: All Tuas berths equipped (eliminate vessel emissions at berth)
        - **Renewable energy**: 40-60 MW solar at Tuas (10-15% of consumption)
        - **Climate resilience**: Tuas built +5m (sea level rise protection through 2100)
        - **Green incentives**: Port due rebates up to 50% for green vessels
        
        **Digital Transformation:**
        - **digitalPORT&#64;SG**: AI-powered berth planning, predictive analytics, real-time visibility
        - **Paperless trade**: eBL (electronic bills of lading), e-BDN, blockchain
        - **Cost savings**: US&#36;50-100 per TEU in documentation costs
        - **BLOCK71**: Maritime innovation hub, startup acceleration
        
        **The Challenge:**
        - **US&#36;1-3 trillion** industry investment needed by 2050
        - **Technology gaps**: Green ammonia engines, large-scale e-fuel production
        - **Cost pass-through**: Alternative fuels 2-4× more expensive
        - **Infrastructure build-out**: Need alternative fuel availability at 2,000+ ports
        - **Fleet replacement**: Every new vessel 2024-2050 must be zero-carbon capable
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> The maritime industry faces its <strong>most significant transformation in history</strong>—
    achieving net-zero GHG emissions by 2050 requires <strong>complete fuel transition</strong> from fossil-based marine fuels to 
    zero-carbon alternatives within 26 years. The <strong>IMO's revised 2023 strategy</strong> accelerated the timeline by 50 years 
    (2050 vs 2100), creating urgent pressure for action. <strong>Alternative fuels landscape</strong> shows no single winner: 
    <strong>LNG dominates today</strong> (185 bunkering ports, 400+ vessels) as transition fuel achieving 20-25% CO₂ reduction but 
    cannot achieve net-zero alone; <strong>methanol emerging as container shipping favorite</strong> (122 bunkering ports, 150+ 
    vessels on order) with green methanol providing 100% decarbonization pathway albeit at 2-3× cost; <strong>ammonia positioned 
    for bulk carriers/tankers</strong> (~30 vessels on order) offering zero-carbon potential but facing toxicity and unproven 
    technology challenges; <strong>biofuels limited to supplemental role</strong> (10-15% of industry needs due to feedstock 
    constraints). Real-world adoption data shows <strong>industry hedging with multi-fuel portfolios</strong>—CMA CGM exemplifies 
    this with 32 LNG + 77 dual-fuel planned + 18 methanol-ready + biomethane R&D. <strong>Singapore positions as green maritime 
    leader</strong> through Future Fuels Port Network (LNG established, methanol developing, ammonia future), <strong>Tuas Mega 
    Port sustainability</strong> (1,000+ electric AGVs, 200+ ARMGs, shore power all berths, 40-60 MW solar, +5m climate resilience), 
    and <strong>digital transformation</strong> (digitalPORT&#64;SG AI platform, paperless trade saving US&#36;50-100/TEU, BLOCK71 
    innovation hub). The <strong>fundamental challenge</strong>: US&#36;1-3 trillion investment needed, alternative fuels 2-4× more 
    expensive requiring cost pass-through to supply chains, technology gaps in green ammonia engines and large-scale e-fuel 
    production, infrastructure build-out across 2,000+ global ports, and fleet replacement urgency where every vessel ordered 
    2024-2050 must be zero-carbon capable or risk becoming stranded asset. Success requires <strong>coordinated action across 
    shipowners, ports, fuel producers, regulators, and cargo owners</strong>—the most complex industrial transformation ever 
    attempted, with global trade and climate stability hanging in the balance.
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
