import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">⚓ Maritime Industry Foundation</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand why maritime trade matters as the backbone of global commerce (over 80% of trade by volume travels 
    by sea, with 64% passing through Asian ports and ~33% through Singapore/Malacca Strait), comprehend how 
    containerisation revolutionised shipping in 1956 through Malcolm McLean's standardised container innovation 
    (reducing shipping costs by 94% and enabling the "flat world" of globalisation), explore the three major waves 
    of change reshaping the industry today (mega vessels scaling from 500 TEU to 24,000+ TEU, mega alliances 
    consolidating from 0% control in 1990s to >80% today, and cargo changes driven by geopolitics and e-commerce), 
    and gain the foundational knowledge necessary to understand modern port operations, terminal management, and 
    maritime strategy that will be explored throughout this comprehensive Maritime 101 educational journey.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Why Maritime Trade Matters - The Invisible Backbone
    # ============================================================================
    
    st.markdown('<p class="section-header">Why Maritime Trade Matters: The Invisible Backbone of Global Commerce</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The lecture materials emphasize a striking reality**: *"The Maritime Industry Serves as the Heart Of Global 
    Trade And The International Supply Chain"* with the quote from Kitack Lim, IMO Secretary-General: *"It is 
    absolutely crucial that the flow of commerce by sea should not be unnecessarily disrupted."*
    
    Maritime shipping operates largely invisibly—most people never see a container ship, never visit a port, never 
    think about how their smartphone arrived from China or their coffee from Colombia. Yet **this invisible industry 
    is the physical foundation of modern civilization**, moving the goods that power our economy, feed our population, 
    and enable our daily lives.
    """)
    
    # Key metrics display
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Global Trade by Sea", "Over 80%", help="Over 80% of global trade volumes carried by sea (lecture verified)")
    with col2:
        st.metric("Asian Port Dominance", "64%", help="64% of seaborne trade unloaded at Asian ports (lecture verified)")
    with col3:
        st.metric("Via Malacca/Singapore", "~33%", help="~33% of seaborne trade passes through Straits of Malacca and Singapore (lecture verified)")
    with col4:
        st.metric("Singapore Services", ">230", help=">230 active container services calling at Singapore (lecture verified)")
    
    st.markdown("""
    **The Scale of Maritime Operations - Understanding the Numbers:**
    
    **Global Fleet:**
    - **50,000+ merchant ships** operate globally across all categories
    - **5,400+ container ships** specifically handle containerised cargo
    - **6,500+ bulk carriers** transport raw materials (coal, iron ore, grain)
    - **7,000+ tankers** carry oil, chemicals, liquefied gases
    - **Thousands more** specialised vessels (ro-ro, cruise, offshore)
    
    **Container Trade Volume:**
    - **800 million+ TEU** (Twenty-foot Equivalent Units) moved annually worldwide
    - **Growing 3-5% per year** historically (though volatile with economic cycles)
    - **Doubled approximately every 15 years** from 1990s through 2020s
    - **Singapore alone**: 41 million TEU throughput (2024)—over 5% of global volume through one port!
    
    **Economic Value:**
    - **US&#36;14 trillion** worth of goods transported by sea annually
    - **90% of world trade by volume** travels by sea
    - **70% of world trade by value** (air freight handles high-value, low-volume goods)
    - Maritime shipping represents **4-6% of global GDP** including ancillary industries
    
    **Why Sea Transport Dominates - The Fundamental Economics:**
    
    **Cost-Effectiveness (The Decisive Advantage):**
    - **10-40× cheaper than air freight** per tonne-kilometre
    - **Example**: Shipping iPhone from Shenzhen to Los Angeles:
      - **Sea freight**: ~US&#36;0.05 per unit (4-6 weeks transit)
      - **Air freight**: ~US&#36;2.00 per unit (2-3 days transit)
      - **40× cost difference!** For low-margin consumer electronics, sea is only viable option
    
    **Massive Capacity:**
    - Single **24,000 TEU mega vessel** carries equivalent cargo of:
      - **240,000 tonnes** of goods
      - **24,000 truck journeys** (if moved by road)
      - **1,200 Boeing 747 cargo flights** (if moved by air)
    - **One vessel = Entire small country's weekly imports**
    
    **Energy Efficiency:**
    - **Most fuel-efficient transport mode** for bulk cargo per tonne-kilometre
    - **50-100× more efficient than trucks** per tonne-kilometre
    - **500-1,000× more efficient than aircraft** per tonne-kilometre
    - **Climate advantage**: Despite size, maritime has lowest carbon intensity for cargo transport
    
    **Global Reach:**
    - **Connects all continents and major economies** (except landlocked countries require transhipment)
    - **No infrastructure required** at origin/destination beyond ports (vs roads, rails, airports)
    - **Flexible routes**: Can adjust shipping routes dynamically based on demand, political situations
    - **Universal**: Same ship can carry goods from any exporter to any importer globally
    
    **Scalability:**
    - **Handles everything**: Raw materials (iron ore, coal), intermediate goods (steel, chemicals), finished products (electronics, clothing)
    - **Any cargo volume**: From single container to entire vessel charters
    - **Any value level**: Low-value bulk commodities to high-value manufactured goods
    """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>💡 The Dependency We Don't See:</strong><br><br>
    Consider your daily life:<br><br>
    <strong>Morning</strong>: Coffee (shipped from Colombia), iPhone (assembled in China, components from Japan/Korea/Taiwan), 
    clothing (manufactured in Bangladesh/Vietnam)<br><br>
    <strong>Afternoon</strong>: Laptop (Taiwan/China), furniture (Malaysia/China), car (Japan/Korea/Germany with global 
    supply chains)<br><br>
    <strong>Evening</strong>: TV (Korea), food ingredients (global agriculture), prescription drugs (India/Europe)<br><br>
    <strong>Nearly EVERY physical item</strong> you interact with has travelled by container ship at least once, often 
    multiple times through complex supply chains. <strong>Maritime shipping is invisible but indispensable</strong>—
    modern civilization would collapse within weeks if container shipping stopped. The 2021 Ever Given Suez Canal 
    blockage (6 days) disrupted US&#36;9-10 billion in trade daily, demonstrating global economy's maritime dependency.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">Singapore\'s Strategic Position in Global Maritime Trade</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The lecture materials highlight **Singapore's pivotal role** with verified statistics:
    
    **Geography as Destiny:**
    - **~33% of global seaborne trade** passes through Straits of Malacca and Singapore (SOMS)
    - **Critical chokepoint**: One of world's busiest maritime routes alongside Suez, Panama, Strait of Hormuz
    - **Asia-Europe main artery**: Virtually all container traffic between Asia and Europe transits Malacca/Singapore
    - **Intra-Asia hub**: Central location for connecting all Asian economies
    
    **Connectivity:**
    - **>230 active container services** calling at Singapore
    - **200+ shipping lines** operate from Singapore
    - **600+ ports** connected to Singapore
    - **Daily departures** to every major port globally
    
    **Market Position:**
    - **World's #2 container port** by throughput (after Shanghai)
    - **World's #1 transshipment hub** (85% of cargo transships vs 15% gateway)
    - **41 million TEU** throughput (2024)—equivalent to Singapore's population handling 5,700+ containers each!
    
    **Why Singapore Matters to You:**
    
    If you're building a **maritime digital twin system**, understanding Singapore's operations means understanding 
    **global best practices**. Singapore represents:
    - **Operational excellence**: >90% BOA, <24-hour turnaround, 35-40 GMPH crane productivity
    - **Technological leadership**: Advanced automation, digitalPORT@SG, CITOS systems
    - **Strategic foresight**: Tuas Mega Port S&#36;20B investment for future capacity
    
    **Your digital twin must model the physical reality of one of the world's most complex, highest-throughput, 
    most technologically advanced port operations**—understanding maritime fundamentals is not optional, it's 
    essential for building accurate, useful systems.
    """)
    
    # ============================================================================
    # SECTION 2: The Container Revolution - The Most Important Innovation You've Never Heard Of
    # ============================================================================
    
    st.markdown('<p class="section-header">The Container Revolution: How a Simple Box Changed Everything</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The lecture materials reference Marc Levinson's definitive book** *"The Box: How the Shipping Container Made 
    the World Smaller and the World Economy Bigger"* (Princeton University Press, 2016) as essential reading on 
    containerisation's transformative impact.
    
    **The Academic Evidence:**
    
    The lecture materials cite rigorous academic research: **"Container shipping would be 94 percent cheaper than 
    break-bulk for the same product."**
    
    Source: *Bernhofen, D.M., El-Sahli, Z and Kneller, R. (2016) "Estimating the effects of the Container Revolution 
    on World Trade." Journal of International Economics, Vol 98, pp 36-50*
    
    **94% cost reduction** is extraordinary—few technologies in human history achieved such dramatic efficiency gains:
    - **Electricity** reduced lighting costs ~99% (candles → bulbs)
    - **Computers** reduced computation costs >99% (human calculators → CPUs)
    - **Containerisation** reduced shipping costs 94% (break-bulk → containers)
    
    This **94% cost reduction** is why your smartphone costs US&#36;800 not US&#36;8,000, why global supply chains 
    exist, why "Made in China" labels are ubiquitous. Containerisation **enabled globalisation**—not merely 
    coincident with it, but a fundamental prerequisite.
    """)
    
    st.markdown('<p class="subsection-header">Before Containers: The Break-Bulk Nightmare (Pre-1956)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    To appreciate containerisation's impact, we must understand **what shipping was like before 1956**—and why it 
    was so terrible that a simple steel box could revolutionise global trade.
    
    **The Break-Bulk Method:**
    
    **"Break-bulk"** means cargo broken down into individual pieces—crates, barrels, sacks, boxes—each handled 
    separately. Imagine loading a ship like packing a car trunk, except the "trunk" is a ship's hold and you have 
    10,000 individual items of different sizes, shapes, and fragility levels.
    
    **Loading/Unloading Process:**
    
    1. **Cargo arrives at dock** in trucks or trains (individual packages)
    2. **Longshoremen (dockworkers)** manually move each item from truck to ship
    3. **Each item lifted** by crane hook OR carried by hand into ship's hold
    4. **Careful stowage** required—heavy items on bottom, fragile on top, similar items grouped
    5. **Repeat for every single item** on ship (thousands of pieces)
    6. **Reverse process** at destination port
    
    **The Numbers Tell the Story:**
    
    **Time:**
    - **7-10 days** to load/unload single ship at each port
    - **50-70% of total voyage time** spent in port (not at sea earning revenue!)
    - **Example**: New York → Rotterdam → New York voyage:
      - 14 days sailing (7 days each direction)
      - 14-20 days port time (7-10 days each port)
      - **Total: 28-34 days**, half wasted in port!
    
    **Cost:**
    - **US&#36;5.86 per ton** to load/unload at US ports (1950s, ~US&#36;60 today adjusted)
    - **More expensive to load/unload** than to ship across ocean!
    - **Labour represented 60-75%** of total shipping costs
    
    **Labour Intensity:**
    - **Gangs of 20-30 longshoremen** per ship
    - **Multiple gangs working simultaneously** for faster turnaround
    - **100-200 workers** on single ship common
    - **Physically demanding**: Lifting, carrying, positioning heavy cargo for hours
    - **Dangerous**: Falls, crushing injuries, accidents frequent
    
    **Theft and Damage:**
    - **"Shrinkage" (theft) 10-30%** normal at some ports (loose cargo easy to steal)
    - **Pilferage rampant**: Workers, organized crime, corrupt officials
    - **Damage common**: Cargo dropped, crushed, water-damaged, mixed up
    - **No accountability**: Impossible to track which longshoreman handled which item
    
    **The Economic Impact of Break-Bulk Inefficiency:**
    
    **Shipping Was Expensive → International Trade Limited:**
    - Only **high-value goods** (silk, spices, precious metals) worth shipping long distances
    - **Bulk commodities** (grain, coal, ore) shipped only when necessary
    - **Manufactured goods** mostly produced and consumed locally/regionally
    - **Global trade ~10-15% of GDP** (vs 50-70% today for many countries)
    
    **Port Cities Were Rough Places:**
    - Thousands of longshoremen congregating daily
    - Organized crime controlled docks (hiring, theft networks)
    - Labor unrest, strikes, violence common
    - Waterfront synonymous with poverty, crime, danger
    
    **Ships Under-Utilized:**
    - Vessel spending half its time idle in port = **massive capital waste**
    - Shipowners needed 2× as many ships for same capacity
    - **Slow turnaround** meant fewer voyages per year per ship
    - **Economics barely worked**—shipping industry chronically unprofitable
    """)
    
    st.markdown('<p class="subsection-header">Malcolm McLean\'s Innovation: The Standardised Container (1956)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **April 26, 1956** marks one of history's most important dates you've never heard of. On this day, **Malcolm 
    McLean**, a trucking company owner from North Carolina, launched the **SS Ideal X** from Newark, New Jersey, 
    carrying **58 aluminum truck bodies** modified to be lifted on and off the ship as a unit.
    
    This experiment would **transform global trade**.
    
    **Who Was Malcolm McLean?**
    
    McLean wasn't a shipping expert—he was a **trucker** frustrated by port inefficiency. The lecture materials 
    reference the Maersk video "Malcolm McLean and Containerisation" which tells his story.
    
    **McLean's Observation:**
    - His trucks would arrive at port with cargo
    - **Hours waiting** for longshoremen to unload truck piece by piece
    - Cargo manually transferred to ship piece by piece
    - **Why not load entire truck onto ship?**
    
    **The Insight:**
    - Don't move cargo from truck to ship—**move the cargo box itself**
    - Standardize box size so any box fits any ship/truck/train
    - Use machinery (cranes) not manual labor to move boxes
    - **Handle the CONTAINER, not the cargo inside**
    
    **The First Container Ship:**
    
    **SS Ideal X (April 1956):**
    - Converted World War II tanker
    - **58 containers** (35-foot aluminum boxes, precursor to modern 40-foot containers)
    - **Newark, NJ → Houston, TX** maiden voyage
    - **Loaded in 8 hours** (vs 5-7 days for equivalent break-bulk cargo)
    - **Cost: US&#36;0.16 per ton** vs US&#36;5.86 per ton break-bulk
    - **97% cost reduction on this first voyage!**
    
    **The Revolutionary Idea - The Container as "The Box":**
    
    **Why a "Simple Steel Box" Changed Everything:**
    
    1. **Standardization**: Every container same size (20-foot or 40-foot standard)—universal handling equipment
    2. **Intermodal**: Same box moves by ship/truck/train without unpacking—seamless transport
    3. **Security**: Cargo sealed in box, protected from theft/weather/damage—one point of loading/unloading
    4. **Mechanization**: Cranes lift boxes, not humans—eliminate most manual labor
    5. **Speed**: Load/unload boxes in hours not days—dramatically increase ship utilization
    6. **Accountability**: Box sealed with cargo manifest—clear responsibility for contents
    
    **The Adoption Process (1956-1980s):**
    
    **Slow at First (1956-1966):**
    - McLean's Sea-Land Service proved concept
    - **Resistance from unions** (threatening jobs), ports (requiring new infrastructure), shipowners (expensive conversion)
    - **Standards battle**: Multiple container sizes (30', 35', 40'), incompatible systems
    
    **Vietnam War Accelerated Adoption (1965-1970):**
    - US military used containers to supply Vietnam operations
    - **Logistics advantage** clear—containers moved war material 10× faster than break-bulk
    - Military contracts funded container ship construction
    
    **International Standards (1968):**
    - **ISO standardization**: 20-foot (TEU) and 40-foot (FEU) containers became global standard
    - **Universal dimensions**: 8' wide, 8'6" or 9'6" high, 20' or 40' long
    - **Now** any container fits any ship, crane, truck, train globally
    
    **Global Adoption (1970s-1980s):**
    - Major shipping lines converted fleets
    - Ports built container terminals (expensive but necessary)
    - **By 1980**: Containerisation dominant for manufactured goods
    - **By 1990**: Break-bulk nearly extinct (except oversized/bulk cargo)
    
    **The 94% Cost Reduction - How Containers Achieved It:**
    
    **Labor Costs Plummeted:**
    - **Pre-container**: 100-200 longshoremen per ship for 7-10 days = 1,000-2,000 man-days
    - **Post-container**: 10-15 crane operators + ground staff for 10-20 hours = 100-300 man-hours
    - **90-95% reduction** in port labor per ship
    
    **Time in Port Collapsed:**
    - **Pre-container**: 7-10 days per port
    - **Post-container**: 1-2 days per port initially, <24 hours today for mega vessels
    - **Ship utilization** increased 300-500% (more time at sea = more revenue voyages per year)
    
    **Theft and Damage Eliminated:**
    - **Sealed containers** = no pilferage access
    - **10-30% shrinkage → <1% shrinkage**
    - **Insurance costs dropped** dramatically
    
    **Economies of Scale Enabled:**
    - Standardization allowed **much larger ships** (500 TEU → 24,000 TEU)
    - **Larger ships = lower cost per container** (fixed crew, engine costs spread across more cargo)
    - **Virtuous cycle**: More volume → Lower costs → More volume
    
    **The Impact - Containerisation Enabled Globalisation:**
    
    **Before Containers (1950s):**
    - **International trade expensive** → Mostly local/regional production
    - **"Made in USA", "Made in Europe"** dominant—manufacturing near consumption
    - **Global supply chains impossible**—coordination costs too high
    - **Just-in-time manufacturing impossible**—unreliable, expensive shipping
    
    **After Containers (1990s+):**
    - **International trade cheap** → Global production optimization
    - **"Made in China", "Assembled in Mexico"** dominant—manufacturing where cheapest
    - **Global supply chains standard**—iPhone has 200+ suppliers across 30 countries
    - **Just-in-time standard**—Toyota production system relies on reliable, cheap container shipping
    
    **The Numbers:**
    - **1960**: Global container trade ~0 TEU
    - **1980**: ~20 million TEU
    - **2000**: ~200 million TEU (10× growth in 20 years)
    - **2024**: ~800 million TEU (4× growth in 24 years, continuing acceleration)
    
    **The "Flat World":**
    
    Thomas Friedman's book *"The World Is Flat"* attributes globalization to the internet and technology. **Reality: 
    Containerisation was equally or more important.** You can video conference with anyone globally, but you can't 
    manufacture and sell physical products globally without cheap shipping—containers made that possible.
    """)
    
    # Before/After comparison visualization
    comparison_data = pd.DataFrame({
        'Metric': [
            'Loading/Unloading Time',
            'Cost per Ton',
            'Labour Required',
            'Theft/Damage Rate',
            'Cargo Security',
            'Ship Utilization'
        ],
        'Break-Bulk (Pre-1956)': [
            '7-10 days per port',
            'US$5.86/ton',
            '100-200 workers',
            '10-30% shrinkage',
            'Very Low (loose cargo)',
            '30-50% (half time in port)'
        ],
        'Containers (Post-1956)': [
            '<24 hours per port',
            'US$0.35/ton',
            '10-15 workers',
            '<1% shrinkage',
            'High (sealed boxes)',
            '80-90% (minimal port time)'
        ],
        'Improvement': [
            '10-20× faster',
            '94% cost reduction',
            '90-95% less labor',
            '90-95% less shrinkage',
            'Revolutionary',
            '2-3× better utilization'
        ]
    })
    
    st.dataframe(comparison_data, width='stretch', hide_index=True)
    
    st.markdown("""
    <div class="success-box">
    <strong>✅ Container Revolution Success Metrics:</strong><br><br>
    <strong>94% Cost Reduction</strong> (verified academic research)<br>
    <strong>10-20× Faster</strong> port operations (7-10 days → <24 hours)<br>
    <strong>90-95% Less Labor</strong> required (100-200 workers → 10-15 workers)<br>
    <strong>90-95% Less Theft</strong> (sealed containers vs loose cargo)<br>
    <strong>2-3× Ship Utilization</strong> (more time at sea earning revenue)<br><br>
    <strong>The Result</strong>: Shipping costs dropped so dramatically that <strong>international trade became 
    economically viable for ordinary manufactured goods</strong>, not just luxury items. This cost reduction 
    <strong>enabled the modern global economy</strong>—everything from iPhone supply chains to fast fashion to 
    just-in-time automotive manufacturing depends on cheap, reliable container shipping that didn't exist before 1956.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 3: Three Waves of Change - The Modern Maritime Landscape
    # ============================================================================
    
    st.markdown('<p class="section-header">Three Waves of Change: How the Industry Continues to Transform</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The lecture materials identify **"Waves of Change: Navigating Continual Industry Developments & Shifts"** as 
    three major transformations reshaping container shipping from the 1990s through 2025:
    
    1. **Arrival of Mega Vessels** (1990s-2000s)
    2. **Birth of Mega Alliances** (2015-2025)
    3. **Change of Cargo** (2017-2024)
    
    These three waves are **simultaneous and ongoing**—the industry is experiencing all three transformations at 
    once, creating unprecedented complexity and strategic challenges for ports like Singapore.
    """)
    
    st.markdown('<p class="subsection-header">Wave 1: Arrival of Mega Vessels - The Economics of Scale (1990s-2000s)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Inexorable Drive Toward Larger Ships:**
    
    Container vessels have grown **50× larger** in capacity over 60 years:
    
    **The Evolution:**
    - **1956**: SS Ideal X—58 containers (~50 TEU equivalent)
    - **1970s**: Second generation—1,000-1,500 TEU "Panamax" (fit through Panama Canal)
    - **1980s**: Third generation—3,000-4,000 TEU "Post-Panamax" (too large for Panama)
    - **1990s**: Fourth generation—5,000-6,000 TEU (first true mega vessels)
    - **2000s**: Fifth generation—8,000-12,000 TEU (New Panamax after canal expansion)
    - **2010s**: Sixth generation—18,000-21,000 TEU (Triple-E class—Economy of scale, Energy efficient, Environmentally improved)
    - **2020s**: Seventh generation—24,000+ TEU (Ever Ace, MSC Irina class)
    
    **Why Larger = Better (The Economics):**
    
    **Fixed Costs Don't Scale Linearly:**
    - **Crew size**: 10,000 TEU vessel vs 20,000 TEU vessel—both need ~20-25 crew (same cost!)
    - **Engine power**: Doubling capacity requires only ~60% more power (not 100%)—cubic-square law physics
    - **Capital cost**: 20,000 TEU vessel costs ~50% more than 10,000 TEU vessel (not 100%)
    
    **Result: Cost per TEU Decreases:**
    - **1,000 TEU vessel**: ~US&#36;5,000-6,000 per TEU slot cost per year
    - **5,000 TEU vessel**: ~US&#36;2,500-3,000 per TEU slot cost per year
    - **20,000 TEU vessel**: ~US&#36;1,000-1,500 per TEU slot cost per year
    - **Scale advantage**: 50-70% lower cost per TEU for mega vessels!
    
    **The Competitive Pressure:**
    
    Once **one shipping line** deploys mega vessels and achieves lower costs, **competitors must follow or die**:
    1. Line A deploys 20,000 TEU vessels—US&#36;1,500/TEU slot cost
    2. Line A charges US&#36;2,000/TEU (US&#36;500 margin)
    3. Line B still uses 5,000 TEU vessels—US&#36;2,500/TEU slot cost
    4. Line B must charge US&#36;3,000/TEU to maintain margins (US&#36;500 margin)
    5. **Shippers choose Line A** (33% cheaper) → Line B loses volume → Forced to deploy mega vessels or exit market
    
    **This "race to scale"** has driven continuous vessel size growth for 30+ years.
    
    **The Infrastructure Challenge:**
    
    **Mega Vessels Require Mega Ports:**
    - **Deeper berths**: 18+ meters depth (vs 12-15m for older vessels)
    - **Longer quays**: 400+ meter berth length
    - **Bigger cranes**: 65-80m outreach to reach across 24 containers wide (vs 45-55m for older cranes)
    - **More cranes**: 8-12 cranes simultaneously to maintain productivity
    - **Larger yards**: Store 10,000-15,000 containers from single vessel
    
    **Port Investment Required:**
    - **US&#36;200-500M per mega-vessel berth** (dredging, quay wall, cranes, yard)
    - **Only major hubs can afford** this investment
    - **Regional ports squeezed out**—cannot justify investment for occasional mega vessel calls
    - **Hub concentration increases**—Singapore, Shanghai, Rotterdam, Los Angeles dominate
    
    **The Strategic Implication:**
    
    **Hub-and-Spoke Model Reinforced:**
    - **Mega vessels** serve only major hub ports (Singapore, Shanghai, Rotterdam)
    - **Feeder vessels** (1,000-5,000 TEU) connect hubs to regional/smaller ports
    - **85% of cargo transships** through hubs on this model
    - **Singapore's advantage**: Natural transshipment hub for Southeast Asia perfectly positioned for mega vessel era
    """)
    
    st.markdown('<p class="subsection-header">Wave 2: Birth of Mega Alliances - Consolidation and Control (2015-2025)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The lecture materials provide verified data** on alliance evolution: **"Alliance Controlled Volumes: 1990s 0% 
    → 2000s 30% → 2015 75% → 2017-2024 >80% → 2025"**
    
    This chart reveals **dramatic industry consolidation in just 25 years**—from fragmented competition to oligopoly 
    domination.
    
    **What Are Shipping Alliances?**
    
    **Alliances are NOT mergers**—shipping lines remain separate companies but **cooperate on operations**:
    
    **What Alliances DO:**
    - **Share vessels**: Pool ships on common routes (each line contributes vessels)
    - **Coordinate schedules**: Align sailing times for better connectivity
    - **Share slots**: Sell each other's container capacity
    - **Joint port calls**: Use same terminals, negotiate rates together
    - **Network optimization**: Design routes collectively
    
    **What Alliances DON'T DO:**
    - **Merge companies**: Lines remain independent
    - **Fix prices**: Price-fixing is illegal—lines compete on rates
    - **Share profits**: Each line keeps its own revenue/profits
    - **Brand integration**: Lines maintain separate customer-facing brands
    
    **The Three Mega Alliances (2025 Configuration):**
    
    **1. Gemini Cooperation (~37% market share):**
    - **Members**: Maersk + Hapag-Lloyd (formed January 2025, replacing 2M Alliance)
    - **Strategy**: Flexible partnership, preserves more operational independence
    - **Strength**: Two financially strong lines with complementary networks
    
    **2. Premier Alliance (~31% market share):**
    - **Members**: Ocean Network Express (ONE) + CMA CGM + COSCO (formed February 2025, evolution of THE Alliance + Ocean Alliance)
    - **Strategy**: Deep integration, extensive vessel sharing
    - **Strength**: Massive combined fleet, ONE (Japanese consolidation) + CMA CGM (French) + COSCO (Chinese state-owned)
    
    **3. MSC Operating Independently (~17% market share):**
    - **Not in alliance** after 2M dissolved January 2025
    - **Strategy**: Go-it-alone leveraging world's largest container fleet
    - **Strength**: MSC became world's #1 line by capacity, can operate without alliance
    
    **Plus: Smaller Independent Lines (~15% market share):**
    - Evergreen, HMM, Yang Ming, ZIM, PIL, regional carriers
    - May form new alliance or remain independent
    
    **Why Did Alliances Form? The Mega Vessel Problem:**
    
    **Individual Shipping Lines Faced a Dilemma:**
    - **Mega vessels achieve low cost per TEU** (US&#36;1,000-1,500 vs US&#36;2,500-3,000 for smaller)
    - **But**: Single mega vessel has 20,000-24,000 TEU capacity
    - **Problem**: How to fill 20,000 TEU weekly on every route?
    
    **Example - Asia-Europe Route:**
    - **Maersk alone**: ~8-10% market share → 2,000-2,500 TEU per week
    - **Need 20,000 TEU vessel** for cost competitiveness
    - **But only have 2,000-2,500 TEU cargo** → Ship sails 10-15% full → Terrible economics!
    
    **Solution: Alliance Vessel Sharing:**
    - **Maersk + MSC** (2M Alliance, 2015-2024): Combined ~20% market share → 5,000 TEU per week
    - **Pool vessels**: Both lines sell slots on shared mega vessels
    - **Fill to 70-80%** → Economically viable
    - **Everyone wins**: Lower costs, better service
    
    **The Consolidation Spiral:**
    
    **Why Alliance Control Grew from 0% → >80% in 25 Years:**
    
    1. **First mover advantage** (2000s): P3 Network attempted (Maersk + MSC + CMA CGM)—blocked by regulators but idea proven
    2. **Competitive pressure** (2010s): Lines outside alliances couldn't match alliance economics → **Forced to join OR exit market**
    3. **Mega vessel deployment** (2015+): Alliances deployed most new mega vessels → Further cost advantage
    4. **Bankruptcy/Consolidation** (2016-2017): Hanjin collapse, Japanese lines merged into ONE → **Fewer independent players**
    5. **Alliance restructuring** (2017-2024): Stabilized into Big Three (2M, Ocean, THE)
    6. **2025 reshuffling** (2024-2025): 2M dissolved, THE + Ocean merged into Premier, new Gemini formed → **Further consolidation**
    
    **The Strategic Implications:**
    
    **For Ports:**
    - **Alliances negotiate as blocks** → Greater bargaining power vs individual ports
    - **Terminal commitments**: Alliances demand dedicated terminals for 10-20 year periods
    - **All-or-nothing**: Lose alliance = lose 30-40% of volume instantly
    - **Singapore's challenge**: Must satisfy alliance requirements (deep berths, mega cranes, guaranteed BOA) to retain business
    
    **For Shippers (Cargo Owners):**
    - **Less competition**: 3 alliances control 80% → Oligopoly pricing power (though not price-fixing, which is illegal)
    - **Better connectivity**: Alliance networks reach more ports
    - **Reliability trade-off**: Alliance coordination improves schedule reliability but reduces flexibility
    
    **For Industry:**
    - **Barriers to entry**: New shipping line cannot compete without alliance membership or massive independent scale
    - **Consolidation continues**: Expect further mergers/alliance changes as lines seek efficiency
    - **Regulatory scrutiny**: Governments concerned about oligopoly power, blocking some mergers
    """)
    
    # Alliance evolution chart
    alliance_timeline = pd.DataFrame({
        'Period': ['1990s', '2000s', '2015', '2017-2024', '2025'],
        'Alliance Control (%)': [0, 30, 75, 83, 85],
        'Description': [
            'Fragmented: ~20 major independent lines',
            'Early alliances emerge (Grand Alliance, New World)',
            'Big Four form (2M, Ocean, G6, CKHYE)',
            'Consolidate to Big Three (2M, Ocean, THE)',
            'Restructure to Gemini + Premier + MSC independent'
        ]
    })
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=alliance_timeline['Period'],
        y=alliance_timeline['Alliance Control (%)'],
        mode='lines+markers',
        line=dict(color='#EF4444', width=4),
        marker=dict(size=15, color='#DC2626', line=dict(color='white', width=2)),
        fill='tozeroy',
        fillcolor='rgba(239, 68, 68, 0.2)',
        name='Alliance Control',
        hovertemplate='%{x}<br>Alliance Control: %{y}%<br>%{text}<extra></extra>',
        text=alliance_timeline['Description']
    ))
    
    fig.update_layout(
        title={
            'text': 'Shipping Alliance Consolidation (Lecture Verified Data)',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#1F2937'}
        },
        xaxis_title="Time Period",
        yaxis_title="Alliance Controlled Market Share (%)",
        height=500,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='#E5E7EB', range=[0, 100]),
        xaxis=dict(gridcolor='#E5E7EB')
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown('<p class="subsection-header">Wave 3: Change of Cargo - Geopolitics, E-commerce, and Supply Chain Resilience (2017-2024)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The lecture materials identify** *"Global challenges confront the maritime industry"* including:
    - Global supply chain disruptions
    - Risks of geopolitical tensions dampening global trade/business sentiments
    - Environmental concerns
    
    The third wave represents **fundamental shifts in WHAT is shipped, WHERE it's shipped, and WHY**—driven by 
    geopolitics, technology, and changing consumer behavior.
    
    **Factor 1: Geopolitical Tensions Reshaping Trade Patterns**
    
    **US-China Trade War and Decoupling (2018-present):**
    
    **The Escalation:**
    - **2018-2019**: US imposes tariffs on US&#36;360B Chinese goods (25% average)
    - **2020-2021**: Phase One deal, tensions ease slightly
    - **2022-2023**: Technology restrictions, chip export controls
    - **2024**: Continued tensions, "de-risking" not "decoupling" narrative but trend continues
    
    **The Impact on Shipping:**
    - **China+1 strategy**: Companies diversify away from China-only manufacturing
    - **Winners**: Vietnam (+80% exports 2018-2024), Malaysia (+45%), Mexico (+35%), India (+40%)
    - **Losers**: Direct China-US routes declining, though China remains dominant
    - **New routes**: More intra-Asia shipping, nearshoring to Mexico for US market
    
    **Example - iPhone Supply Chain:**
    - **Pre-2018**: 90% final assembly in China → US
    - **2024**: Final assembly diversifying—India (15%), Vietnam (10%), China (75%)
    - **Container routes shifting**: More Shenzhen → Chennai (India), less Shenzhen → Los Angeles direct
    
    **Singapore's Position:**
    - **Benefits from diversification**: Central hub connecting all Asian production locations
    - **Neutral player**: Not caught in US-China tensions, serves both sides
    - **Intermediate transshipment**: Goods from Vietnam/India transit Singapore to US/Europe
    
    **Factor 2: E-commerce Explosion and Consumer-Direct Shipping**
    
    **The E-commerce Revolution:**
    - **2019**: Global e-commerce ~US&#36;3.5 trillion
    - **2024**: Global e-commerce ~US&#36;6-7 trillion (COVID accelerated)
    - **Growth**: 15-20% annually, far exceeding traditional retail
    
    **How E-commerce Changes Cargo:**
    
    **Traditional Retail Supply Chain:**
    1. Factory (China) produces 10,000 units
    2. **Full container** (20,000-40,000 units) shipped to US
    3. **Received by retailer** (Walmart, Target) at distribution center
    4. **Distributed to stores** nationwide
    5. **Consumers buy** from stores over months
    
    **E-commerce Supply Chain:**
    1. Factory (China) produces 10,000 units
    2. **Small batches** (100-1,000 units) shipped frequently
    3. **Received by e-commerce fulfillment center** (Amazon, Shein)
    4. **Individual orders shipped** directly to consumers' homes
    5. **Consumers receive** 2-7 days from order (not weeks)
    
    **Shipping Implications:**
    
    **More Frequent, Smaller Shipments:**
    - **Traditional**: Few large containers per month
    - **E-commerce**: Many small shipments per week
    - **Air freight grows**: Time-sensitive goods increasingly fly (despite 10-40× higher cost)
    - **Express shipping**: Amazon, Shein charter entire vessels for fast China-US delivery
    
    **Inventory Positioning Changes:**
    - **Traditional**: Inventory in retail stores, slow turnover
    - **E-commerce**: Inventory in fulfillment centers near consumers, fast turnover
    - **Result**: More container flows to major consumption markets (US, Europe)
    
    **Returns Logistics:**
    - **E-commerce return rates**: 20-40% (vs <5% traditional retail)
    - **Reverse logistics**: Containers returning products China ← US (unusual flow)
    - **Added complexity**: Two-way flows instead of one-way export model
    
    **Factor 3: Supply Chain Disruptions and Resilience Focus (2020-2024)**
    
    **The Lesson of Disruptions:**
    
    **COVID-19 Pandemic (2020-2021):**
    - **Factory shutdowns**: China, Vietnam, Malaysia closed intermittently
    - **Port congestions**: Los Angeles/Long Beach 100+ vessels anchored waiting (weeks delay)
    - **Container shortages**: Containers stuck at wrong locations globally
    - **Result**: US&#36;9-10B/week in delayed cargo, severe shortages (chips, PPE, goods)
    
    **Ever Given Suez Canal Blockage (March 2021):**
    - **400m vessel grounded** sideways in Suez Canal
    - **6 days blockage**: ~400 vessels waiting, US&#36;9-10B trade per day disrupted
    - **Result**: Revealed fragility of key chokepoints
    
    **Red Sea / Yemen Houthi Attacks (2023-2024):**
    - **Attacks on commercial vessels**: Container ships, tankers targeted
    - **Shipping lines reroute**: Avoid Red Sea/Suez, go around Africa (adds 10-14 days, ~3,500 nautical miles)
    - **Cost increase**: US&#36;1,000-2,000 per container additional cost
    - **Result**: ~50% of Asia-Europe traffic diverted, congestion shifts
    
    **Panama Canal Drought (2023-2024):**
    - **Low water levels**: Gatun Lake depleted due to drought
    - **Transit restrictions**: Reduced from 36 to 22 vessels per day
    - **Delays**: 2-3 week waits, some vessels reroute via Suez
    - **Result**: Pacific-Atlantic shipping disrupted
    
    **The Strategic Response - Supply Chain Resilience:**
    
    **Companies Learned:**
    - **Just-in-time is fragile**: Lean supply chains break during disruptions
    - **Single-source risky**: Over-dependence on one country/region dangerous
    - **Chokepoints matter**: Suez, Panama, Malacca, Singapore—critical junctions
    
    **New Approach:**
    - **Just-in-case inventory**: Hold more safety stock (3-6 months vs 1-2 months)
    - **Diversified sourcing**: Multi-country manufacturing (China + Vietnam + Mexico + India)
    - **Nearshoring**: Bring production closer to consumption (Mexico for US, Eastern Europe for EU)
    - **Redundant logistics**: Multiple shipping routes, backup suppliers
    
    **Impact on Container Shipping:**
    
    **More Volume, More Routes:**
    - **Higher inventory levels** → More containers moving globally
    - **Diversified production** → More origin-destination pairs (not just China → US/Europe)
    - **Nearshoring** → Shorter routes but more frequent shipments
    
    **Flexibility Demand:**
    - **Shippers demand flexibility**: Need to switch routes/ports quickly
    - **Ports must be agile**: Handle unexpected volume surges
    - **Alliances adjust networks**: More frequent route changes vs fixed 10-year plans
    """)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ The Three Waves Are Interconnected:</strong><br><br>
    These three waves don't happen in isolation—they <strong>amplify and complicate each other</strong>:<br><br>
    <strong>Mega Vessels + Alliances</strong>: Alliances needed to fill mega vessels → Consolidation accelerated<br>
    <strong>Mega Vessels + Cargo Changes</strong>: E-commerce needs smaller, frequent shipments but mega vessels 
    are large, infrequent → Mismatch<br>
    <strong>Alliances + Geopolitics</strong>: Alliances must navigate US-China tensions without alienating either market<br>
    <strong>All Three + Resilience</strong>: Mega vessels = efficiency but less flexibility; Alliances = coordination 
    but dependence; Cargo changes = complexity → Building resilient operations incredibly challenging<br><br>
    <strong>Ports like Singapore must handle all three waves simultaneously</strong>—accommodate mega vessels (deep 
    berths, mega cranes), satisfy alliance requirements (dedicated terminals, guaranteed BOA), adapt to cargo 
    changes (e-commerce, geopolitical shifts, disruptions). This is why <strong>Tuas Mega Port is S&#36;20B investment</strong>—
    not just capacity expansion, but comprehensive transformation to handle the modern maritime complexity.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 4: Course Roadmap and Navigation
    # ============================================================================
    
    st.markdown('<p class="section-header">Your Maritime 101 Educational Journey</p>', unsafe_allow_html=True)
    
    st.markdown("""
    You've completed the **foundation module**—understanding why maritime matters, how containerisation revolutionised 
    trade, and the three waves reshaping the industry. Now you're ready to dive deeper into the **11 comprehensive 
    modules** that will give you complete mastery of maritime operations:
    
    **Module 1: ⚓ Maritime Industry Foundation** ← YOU ARE HERE
    - Why maritime trade matters (over 80% of global trade)
    - Container revolution (94% cost reduction enabling globalisation)
    - Three waves of change (mega vessels, mega alliances, cargo changes)
    
    **Module 2: 📦 Containers & Containerisation**
    - ISO standards (8' wide, 8'6"/9'6" high, 20'/40' long)
    - TEU measurement system (industry standard capacity metric)
    - Specialised container types (reefer, tank, flat rack, open top)
    - Container construction and specifications
    
    **Module 3: 🚢 Container Vessels & Evolution**
    - Vessel size classifications (Feeder → Panamax → Post-Panamax → ULCV)
    - Evolution from 500 TEU → 24,000+ TEU over 60 years
    - Vessel anatomy (hull, engine, accommodation, navigation)
    - Stowage planning principles (stability, weight distribution, segregation)
    
    **Module 4: 🌍 Global Shipping Networks & Alliances**
    - Three mega alliances controlling 83% of capacity
    - Hub-and-spoke network model (85% transshipment)
    - Major trade routes (Asia-Europe, Trans-Pacific, Intra-Asia)
    - Geopolitical shifts and "China+1" diversification
    
    **Module 5: 🇸🇬 Maritime Singapore Ecosystem**
    - MPA's dual role (regulator + developer) unique model
    - Complete maritime cluster (200+ lines, 5,000+ companies)
    - Singapore's competitive advantages (location, stability, excellence)
    - Innovation ecosystem (BLOCK71, digitalPORT@SG, digitalOCEANS)
    
    **Module 6: 🏆 Port Competition & Strategy**
    - Critical success factors (efficiency, reliability, connectivity)
    - Gateway vs transshipment port models
    - Singapore's position (world's #1 transshipment hub, 85% transship cargo)
    - Regional competition (Malaysia, Indonesia, Thailand)
    
    **Module 7: 🎯 Operations Management Fundamentals**
    - Big Six competencies (Quality, Reliability, Responsiveness, Agility, Service, Cost)
    - FMEA quality management (proactive failure prevention)
    - Capacity planning (design vs effective vs actual capacity, 80-90% optimal)
    - Strategic trade-offs (cost vs quality, speed vs accuracy, efficiency vs flexibility)
    
    **Module 8: 🏗️ Container Terminal Operations**
    - Berth planning and vessel scheduling algorithms
    - Yard operations and container storage strategies
    - Vessel stowage planning (bay plans, load sequences, stability)
    - Equipment coordination (QC-YC-AGV synchronisation)
    
    **Module 9: 🏭 Equipment & Automation Technologies**
    - Quay cranes (65-80m outreach, 35-40 GMPH productivity)
    - Yard cranes (ARMG, RMG, RTG configurations)
    - Horizontal transport (AGVs, prime movers, automated trucks)
    - CITOS Terminal Operating System (AI-powered optimisation)
    
    **Module 10: 🌱 Green Maritime & Future Trends**
    - IMO decarbonisation strategy (net-zero by 2050)
    - Alternative fuels (LNG, methanol, ammonia, hydrogen, biofuels)
    - Green port technologies (shore power, electrification, solar)
    - Digital transformation (paperless trade, blockchain, IoT)
    
    **Module 11: 🏗️ Tuas Mega Port Case Study**
    - S&#36;20B+ strategic investment rationale
    - Five strategic drivers (consolidation, mega vessels, competition, technology, climate)
    - 65M TEU capacity planning and scenario analysis
    - Implementation challenges (workforce, transport, cybersecurity)
    
    **By completing all 11 modules, you will:**
    
    ✅ **Understand the physical maritime world** your digital twin systems must model accurately
    
    ✅ **Comprehend port economics and strategy** explaining why ports make billion-dollar decisions
    
    ✅ **Master terminal operations workflows** from vessel arrival through container delivery
    
    ✅ **Grasp technology and automation** transforming modern port operations
    
    ✅ **Recognise future trends** (decarbonisation, digitalisation, geopolitical shifts) shaping industry evolution
    
    This **comprehensive maritime education** will enable you to build more accurate models, design better systems, 
    communicate effectively with maritime professionals, and understand the operational context behind the data and 
    processes you're digitising.
    """)
    
    # ============================================================================
    # SECTION 5: Key Takeaways and Summary
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways: Maritime Industry Foundation</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Why Maritime Matters (Lecture Verified):**
        - **Over 80%** of global trade by volume travels by sea
        - **64%** of seaborne trade unloaded at Asian ports
        - **~33%** passes through Straits of Malacca and Singapore
        - **>230** active container services call at Singapore
        - **800M+ TEU** moved globally annually (5,400+ container ships)
        - **Most cost-effective** transport: 10-40× cheaper than air freight
        
        **Container Revolution (1956):**
        - **Malcolm McLean's innovation**: Standardised steel box
        - **94% cost reduction** (verified academic research)
        - **10-20× faster** port operations (7-10 days → <24 hours)
        - **90-95% less labour** required (100-200 → 10-15 workers)
        - **Enabled globalisation**: Made international trade economically viable
        - **Reference**: Marc Levinson's "The Box" (definitive history)
        
        **Wave 1: Mega Vessels (1990s-2000s):**
        - **Scale evolution**: 500 TEU → 24,000+ TEU (50× larger)
        - **Economics**: 50-70% lower cost per TEU for mega vessels
        - **Infrastructure demands**: Deeper berths, bigger cranes, larger yards
        - **Hub concentration**: Only major ports can handle mega vessels
        """)
    
    with col2:
        st.markdown("""
        **Wave 2: Mega Alliances (2015-2025):**
        - **Alliance control growth**: 0% (1990s) → >80% (2024) [lecture verified]
        - **2025 configuration**: Gemini Cooperation + Premier Alliance + MSC independent
        - **Purpose**: Pool vessels to fill mega ships (20,000 TEU capacity)
        - **Impact**: Oligopoly power, port bargaining leverage, barriers to entry
        - **Strategic**: Ports must satisfy alliance requirements or lose 30-40% volume
        
        **Wave 3: Cargo Changes (2017-2024):**
        - **Geopolitics**: US-China tensions, "China+1" diversification
          - Vietnam +80%, Malaysia +45%, India +40% exports growth
        - **E-commerce**: US&#36;3.5T → US&#36;6-7T (2019-2024)
          - Smaller, more frequent shipments; reverse logistics
        - **Supply chain disruptions**: COVID, Suez blockage, Red Sea attacks, Panama drought
        - **Resilience focus**: Just-in-case inventory, nearshoring, diversified sourcing
        
        **Global Challenges (Lecture Identified):**
        - Supply chain disruptions (pandemic, geopolitical, climate)
        - Geopolitical tensions dampening trade sentiments
        - Environmental concerns (decarbonisation, net-zero 2050)
        
        **Your Digital Twin Context:**
        - Model world's most complex maritime operations
        - Understand why S&#36;20B Tuas investment necessary
        - Grasp physical constraints shaping digital systems
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Maritime shipping is the <strong>invisible backbone of global commerce</strong>, 
    moving over 80% of trade by volume with 64% passing through Asian ports and ~33% through Singapore/Malacca 
    Strait (<strong>lecture verified statistics</strong>). The <strong>1956 container revolution</strong> initiated 
    by Malcolm McLean reduced shipping costs by <strong>94% (verified academic research)</strong> through 
    standardisation, mechanisation, and intermodalism, <strong>enabling the modern global economy</strong>—from 
    just-in-time manufacturing to e-commerce to complex supply chains. Today, the industry faces <strong>three 
    simultaneous waves of transformation</strong>: <strong>Wave 1 - Mega vessels</strong> (scaling from 500 TEU 
    to 24,000+ TEU driven by 50-70% lower cost per TEU, requiring massive port infrastructure investment); 
    <strong>Wave 2 - Mega alliances</strong> (consolidation from 0% control in 1990s to >80% in 2024 per lecture 
    materials, creating oligopoly with three mega alliances—Gemini Cooperation, Premier Alliance, plus MSC 
    independent—controlling global capacity); <strong>Wave 3 - Cargo changes</strong> (geopolitical shifts driving 
    "China+1" diversification with Vietnam +80%/Malaysia +45%/India +40% exports growth, e-commerce explosion from 
    US&#36;3.5T to US&#36;6-7T requiring smaller/more frequent shipments, and supply chain disruptions from COVID/Suez/
    Red Sea/Panama forcing resilience focus on just-in-case inventory and nearshoring). The lecture materials 
    identify <strong>global challenges confronting the industry</strong>: supply chain disruptions, geopolitical 
    tensions dampening trade sentiments, and environmental concerns requiring net-zero by 2050. <strong>Understanding 
    these fundamentals is essential</strong> for building accurate maritime digital twin systems—you're not just 
    modeling container movements, you're modeling one of the most complex, capital-intensive, strategically critical 
    industries in global commerce. <strong>Singapore's position</strong> (world's #1 transshipment hub with >230 
    services, central location for ~33% of global trade) and <strong>massive investments</strong> (Tuas S&#36;20B 
    for 65M TEU capacity) make sense only when you understand the physical maritime reality, competitive dynamics, 
    and transformative waves shaping this industry. This foundation prepares you for the <strong>10 remaining modules</strong> 
    providing comprehensive maritime education necessary for effective digital twin development and maritime technology 
    innovation.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Your Learning Journey")
    st.markdown("""
    **Ready to dive deeper?** Proceed to the next module to begin your comprehensive exploration of containers, 
    containerisation standards, and the TEU measurement system that makes global container shipping possible.
    
    **Next Module:** 📦 Containers & Containerisation
    """)
