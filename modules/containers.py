import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">📦 Containers & Containerisation</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand ISO container standards, measurement systems (TEU), container types and specifications, 
    identification systems, and the three-dimensional addressing used in terminals and vessels. Grasp how 
    standardisation revolutionised global trade and enabled the modern intermodal transport system.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: The Container Revolution Context
    # ============================================================================
    
    st.markdown('<p class="section-header">The Container Revolution: From Concept to Global Standard</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Before diving into technical specifications, it's essential to understand why container standardisation 
    was revolutionary. In 1956, Malcolm McLean launched the **Ideal-X**, the first purpose-built container 
    ship, carrying just 58 containers from Newark to Houston. This simple innovation—a standardised, 
    reusable metal box—transformed global commerce by reducing shipping costs by over 90% and enabling 
    the intermodal transport system we rely on today.
    """)
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 The Power of Standardisation:</strong><br>
    <strong>Before containers</strong>: Cargo loaded piece by piece, taking 7-10 days per ship, with high theft 
    and damage rates<br>
    <strong>After containers</strong>: Sealed boxes loaded in under 24 hours, with dramatically reduced costs and 
    damage<br><br>
    The key insight was <strong>intermodal transport</strong>: the same container travels by truck from factory, 
    transfers to ship, then to rail, then truck again—all without unpacking the cargo. This required global 
    agreement on exact dimensions so that every crane, every ship, every truck, and every train could handle 
    the same standardised box.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 2: ISO Container Standards
    # ============================================================================
    
    st.markdown('<p class="section-header">ISO Container Standards: The Foundation of Interoperability</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The genius of containerisation lies in **standardisation**. ISO (International Organisation for 
    Standardization) containers have precise specifications that enable seamless global operations. Without 
    these standards, the global container shipping system simply could not function.
    """)
    
    st.markdown('<p class="subsection-header">Standard Container Dimensions</p>', unsafe_allow_html=True)
    
    # Container specifications - Enhanced with all sizes from lectures
    container_specs = pd.DataFrame({
        'Container Type': [
            '20ft Standard',
            '40ft Standard',
            '40ft High Cube',
            '45ft High Cube',
            '48ft High Cube',
            '53ft High Cube'
        ],
        'External Length': ['6.058m (19ft 10.5in)', '12.192m (40ft)', '12.192m (40ft)', '13.716m (45ft)', '14.630m (48ft)', '16.154m (53ft)'],
        'External Width': ['2.438m (8ft)', '2.438m (8ft)', '2.438m (8ft)', '2.438m (8ft)', '2.591m (8ft 6in)', '2.591m (8ft 6in)'],
        'External Height': ['2.591m (8ft 6in)', '2.591m (8ft 6in)', '2.896m (9ft 6in)', '2.896m (9ft 6in)', '2.896m (9ft 6in)', '2.896m (9ft 6in)'],
        'Internal Length': ['5.9m', '12.0m', '12.0m', '13.6m', '14.5m', '16.0m'],
        'Internal Width': ['2.35m', '2.35m', '2.35m', '2.35m', '2.49m', '2.49m'],
        'Internal Height': ['2.39m', '2.39m', '2.69m', '2.69m', '2.69m', '2.69m'],
        'Tare Weight': ['2,300 kg', '3,750 kg', '3,940 kg', '4,800 kg', '5,200 kg', '5,800 kg'],
        'Max Gross Weight': ['30,480 kg', '30,480 kg', '30,480 kg', '30,480 kg', '34,020 kg', '34,020 kg'],
        'Max Payload': ['28,180 kg', '26,730 kg', '26,540 kg', '25,680 kg', '28,820 kg', '28,220 kg'],
        'Cubic Capacity': ['33 m³', '67 m³', '76 m³', '86 m³', '97 m³', '109 m³'],
        'Primary Market': ['Global standard', 'Global standard', 'Global standard', 'Global/Europe', 'North America', 'North America']
    })
    
    st.dataframe(container_specs, width='stretch', hide_index=True)
    
    st.markdown("""
    **Key Observations:**
    
    **Universal 8-Foot Width (2.438m):**
    - All standard containers are **8 feet (2.438m) wide**
    - This is the fundamental standard that everything else is built around
    - Origin: Based on US truck width regulations from the 1950s
    - Ships, cranes, trucks, trains, and terminals worldwide designed for this width
    - 48ft and 53ft containers are slightly wider (8ft 6in) but only used domestically in North America
    
    **Length Standards:**
    - **20ft (6.058m)**: Original standard, still widely used for heavy cargo
    - **40ft (12.192m)**: Most common globally, exactly double the 20ft
    - **45ft (13.716m)**: European standard for higher volume
    - **48ft & 53ft**: Used exclusively in North American domestic markets
    - Multiples of standard lengths enable efficient stacking and transport planning
    
    **Height Variations:**
    - **Standard height**: 8ft 6in (2.591m) - Original traditional standard
    - **High Cube**: 9ft 6in (2.896m) - Extra 1 foot (30cm) of height
    - High Cube containers allow more volume without exceeding weight limits
    - Most new containers manufactured today are High Cube (more versatile for low-density cargo)
    - Height chosen to balance volume against clearance limits (bridges, tunnels, overhead wires)
    
    **Weight Limits:**
    - **Max gross weight**: 30,480 kg (30.48 tonnes) - International ISO standard
    - Some countries allow higher gross weights (up to 36 tonnes) for domestic transport
    - **Tare weight**: Empty container weight (2.3-5.8 tonnes depending on type and size)
    - **Max payload**: Gross weight minus tare weight (typically 25-28 tonnes)
    - Road transport often has lower limits (varies by country regulations)
    """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🎯 Why These Specific Dimensions?</strong><br><br>
    <strong>8ft width:</strong> Matched US truck width regulations in the 1950s when Malcolm McLean pioneered 
    containerisation. This became the global standard because early adoption drove infrastructure investment.<br><br>
    <strong>20ft/40ft lengths:</strong> Multiples for efficient stacking and transport. A 40ft position on a vessel 
    can hold one 40ft container or two 20ft containers. This flexibility is crucial for operations.<br><br>
    <strong>8ft 6in vs 9ft 6in heights:</strong> Balance between cargo volume and transport clearances. Bridges, 
    tunnels, overhead power lines, and vessel stability all constrain maximum height. High Cube adds valuable 
    volume for bulky, light cargo without exceeding weight limits.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 The Power of Standardisation:</strong><br>
    Because containers worldwide follow these exact specifications:<br>
    - <strong>Any container</strong> fits on any ship, truck, train, or terminal anywhere in the world<br>
    - <strong>Global infrastructure</strong> designed for these exact dimensions (berths, cranes, yards, roads)<br>
    - <strong>Equipment interoperability</strong>: Cranes and chassis work everywhere without modification<br>
    - <strong>Planning simplification</strong>: Port operators know exactly what they're handling<br>
    - <strong>Economies of scale</strong>: Mass production of containers and handling equipment<br>
    - <strong>Intermodal efficiency</strong>: Seamless transfer between transport modes<br><br>
    Without standardisation, global containerised shipping would be impossible. Each port would need different 
    equipment, vessels couldn't call at multiple ports efficiently, and costs would be prohibitive.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 3: TEU Measurement System
    # ============================================================================
    
    st.markdown('<p class="section-header">The TEU: Universal Container Measurement</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **TEU = Twenty-foot Equivalent Unit**
    
    The TEU is the standard unit for measuring container capacity, throughput, and vessel sizes. It provides 
    a universal language for the industry, normalising the mix of different container sizes into a single 
    comparable metric.
    """)
    
    st.markdown('<p class="subsection-header">Understanding TEU Calculation</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Basic Conversion:**
        - 1 × 20ft container = **1 TEU**
        - 1 × 40ft container = **2 TEU**
        - 1 × 45ft container = **2.25 TEU** (approximately)
        - 1 × 48ft container = **2.4 TEU** (North America only)
        - 1 × 53ft container = **2.65 TEU** (North America only)
        
        **Examples:**
        - Vessel carrying 10,000 × 20ft containers = 10,000 TEU
        - Vessel carrying 5,000 × 40ft containers = 10,000 TEU
        - Vessel carrying 3,000 × 20ft + 3,500 × 40ft = 10,000 TEU
        
        **Port Throughput:**
        - Singapore handles ~37 million TEU annually (2024)
        - This could be any mix of 20ft and 40ft containers
        - TEU provides standard measurement regardless of actual container size mix
        - Enables meaningful comparisons between ports globally
        """)
    
    with col2:
        st.markdown("""
        **Why TEU Rather Than Just "Container Count"?**
        
        **Problem:**
        - A 20ft and 40ft container are very different
        - 40ft has 2× length, ~2× volume, ~2× weight capacity
        - Saying "a port handled 1,000 containers" doesn't tell you much
        - Could be 1,000 × 20ft (1,000 TEU) or 1,000 × 40ft (2,000 TEU)
        
        **Solution:**
        - TEU normalises everything to 20ft equivalent
        - "10,000 TEU" gives clear sense of capacity and volume
        - Easy to compare vessels, ports, and throughput globally
        - Industry-wide standard for capacity planning
        
        **Industry Standard Usage:**
        - Vessel capacity: "A 20,000 TEU vessel"
        - Port throughput: "37M TEU per year"
        - Crane productivity: "30 moves per hour = 45 TEU/hour (if all 40ft)"
        - Terminal capacity: "Annual capacity of 15M TEU"
        """)
    
    # TEU comparison visualization - Enhanced
    st.markdown('<p class="subsection-header">TEU in Practice: Different Mixes, Same Capacity</p>', unsafe_allow_html=True)
    
    teu_examples = pd.DataFrame({
        'Container Mix': [
            'All 20ft containers',
            'All 40ft containers',
            'Mixed (50% each by count)',
            'Typical mix (20% 20ft, 80% 40ft by count)',
            'Volume-optimized (10% 20ft, 90% 40ft)'
        ],
        'Number of Containers': [10000, 5000, 6667, 5625, 5278],
        'Total TEU': [10000, 10000, 10000, 10000, 10000],
        'Average TEU per Container': [1.0, 2.0, 1.5, 1.78, 1.89],
        'Notes': [
            'Heavy cargo routes (metals, minerals)',
            'Light cargo routes (electronics, clothing)',
            'Balanced mix',
            'Common global average',
            'Modern mega-vessel typical mix'
        ]
    })
    
    st.dataframe(teu_examples, width='stretch', hide_index=True)
    
    st.markdown("""
    **Practical Implications:**
    
    **Moves vs Boxes vs TEU:**
    - **Moves**: Physical crane movements (lifting/lowering operations)
    - **Boxes**: Actual number of individual containers
    - **TEU**: Normalised capacity measure
    - Example: Moving 5,000 boxes that are all 40ft = 5,000 moves = 10,000 TEU
    - Productivity often measured in moves/hour, but capacity measured in TEU
    
    **Why the Mix Matters:**
    - Vessels designed for TEU capacity, not box count
    - A "20,000 TEU vessel" could carry 20,000 × 20ft or 10,000 × 40ft (or any mix totaling 20,000 TEU)
    - Port planning based on TEU throughput expectations
    - Heavy cargo (metals) tends toward 20ft; light cargo (electronics) toward 40ft
    """)
    
    # ============================================================================
    # SECTION 4: Container Types
    # ============================================================================
    
    st.markdown('<p class="section-header">Container Types: Specialised for Different Cargo</p>', unsafe_allow_html=True)
    
    st.markdown("""
    While standard dry containers dominate the global fleet, specialised containers exist for specific cargo 
    types. Understanding these types is essential for terminal operations, as each requires different handling 
    procedures and infrastructure.
    """)
    
    # Container types data - Enhanced with lecture information
    container_types = pd.DataFrame({
        'Type': [
            'Dry Van (General Purpose)',
            'Reefer (Refrigerated)',
            'Open Top',
            'Flat Rack',
            'Tank Container',
            'Out of Gauge (OOG)',
            'Platform/Bolster'
        ],
        'Percentage of Fleet': ['~90%', '~6%', '~1%', '~1%', '~1%', '<1%', '<1%'],
        'Primary Use': [
            'General cargo: boxes, pallets, bags, manufactured goods',
            'Perishables, pharmaceuticals, chemicals requiring temperature control',
            'Oversized cargo that exceeds standard height, loaded from top with crane',
            'Heavy machinery, construction equipment, oversized items needing open sides',
            'Liquids: chemicals, food-grade liquids, wine, oils, liquid bulk cargo',
            'Cargo exceeding container dimensions in any direction (very large equipment)',
            'Heavy cargo like steel coils, timber, vehicles, requiring open platform'
        ],
        'Key Features': [
            'Fully enclosed, weatherproof, lockable doors, corrugated steel construction',
            'Built-in refrigeration unit, temperature range -35°C to +30°C, requires continuous power',
            'Removable roof/tarpaulin, same footprint as standard, crane-accessible top',
            'Collapsible sides, can stack flat when empty, lashing points for securing',
            'Cylindrical tank in standard ISO frame, various sizes (14-26k litres), pressure-rated',
            'Oversized length/width/height, cannot stack containers on top, special stowage',
            'Flat base with corner posts, no walls or roof, designed for heavy/awkward loads'
        ],
        'Special Handling': [
            'Standard crane operations, forklift loading/unloading',
            'Must connect to power (vessel/terminal/truck), monitor temperature continuously, priority handling',
            'Top-loading requires crane access, cannot load with standard equipment from doors',
            'Special securing required, cannot stack other containers on top, careful weight distribution',
            'Requires certified cleaning between loads, hazmat regulations, specialized connections',
            'Special stowage positions, certified lifting equipment, cannot obstruct other containers',
            'Heavy-duty securing, special stowage considerations, load distribution critical'
        ]
    })
    
    st.dataframe(container_types, width='stretch', hide_index=True)
    
    st.markdown('<p class="subsection-header">Reefer Containers: Special Infrastructure Requirements</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Refrigerated containers (reefers) represent a critical specialised category requiring dedicated 
    infrastructure throughout the supply chain. Understanding reefer requirements is essential for terminal 
    design and operations planning.
    
    **Power Requirements:**
    - Reefers need **continuous electrical power** to maintain temperature
    - **Vessels**: Limited reefer plug positions in specific bays (typically 10-15% of total capacity)
      - Plugs integrated into vessel structure near holds and on deck
      - Restricts where reefers can be stowed (stowage constraint)
      - Power capacity limits number of reefers per voyage
    - **Terminals**: Dedicated power outlets in yard storage areas (reefer zones)
      - Electrical grid infrastructure required
      - Significant operational cost (continuous power consumption)
    - **Trucks**: Diesel-powered generators (clip-on gensets)
      - Added fuel cost and emissions
      - Maintenance requirements
    
    **Temperature Monitoring:**
    - **Remote monitoring systems** track all reefers in real-time
    - Alarms if temperature deviates from setpoint (immediate action required)
    - Temperature logs for customs and quality assurance
    - Cold chain integrity documentation required
    
    **Operational Challenges:**
    - **Limited plug positions on vessels** = stowage constraint (cannot stow reefers just anywhere)
    - **Power consumption at terminals** = significant cost consideration (electrical demand)
    - **Equipment breakdowns** require immediate attention (cargo spoilage risk within hours)
    - **Priority handling** = time-sensitive perishables cannot wait
    - **Cleaning requirements** between loads (food safety, cross-contamination prevention)
    
    **Common Reefer Cargo:**
    - **Frozen products**: Meat, fish, poultry (typically -18°C to -25°C)
    - **Fresh produce**: Fruits, vegetables (typically 0°C to +15°C, varies by product)
    - **Dairy products**: Cheese, butter, milk products (+2°C to +8°C)
    - **Pharmaceuticals**: Vaccines, medicines (very strict temperature requirements, often +2°C to +8°C)
    - **Chemicals**: Temperature-sensitive chemical products (varies widely)
    - **Wine and beverages**: Temperature-controlled transport (+12°C to +18°C typical)
    - **Flowers and plants**: Extending shelf life (+2°C to +10°C)
    """)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ Reefer Operational Criticality:</strong><br><br>
    Reefer containers represent high-value, time-sensitive cargo. A single power failure or temperature 
    deviation can result in complete cargo loss worth hundreds of thousands of dollars. This drives:<br>
    - <strong>Redundant power systems</strong> at terminals<br>
    - <strong>24/7 monitoring</strong> with immediate alert response<br>
    - <strong>Priority vessel stowage</strong> near power outlets<br>
    - <strong>Backup generator capacity</strong> for terminal power outages<br>
    - <strong>Preferential crane scheduling</strong> to minimise time without power
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 5: Container Anatomy and Specifications
    # ============================================================================
    
    st.markdown('<p class="section-header">Container Anatomy: Critical Components</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Understanding container structure is essential for grasping how containers are lifted, secured, and 
    stacked both on vessels and in terminals. Every component serves a specific purpose in the global 
    logistics system.
    """)
    
    st.markdown('<p class="subsection-header">Corner Castings: The Heart of the System</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Corner Castings:**
        - **Most critical component** of any container
        - **Location**: Steel fittings at all 8 corners (4 top, 4 bottom)
        - **Dimensions**: Standardised 178mm × 162mm × 119mm globally
        - **Shape**: Oval holes (not circular) designed for twist-locks
        - **Function**: Bear ALL lifting forces and securing loads
        
        **Why Corner Castings Enable Everything:**
        - **Crane lifting**: Spreaders engage top corner castings
        - **Vessel securing**: Twist-locks through corner castings connect to cell guides
        - **Chassis transport**: Bottom corners lock onto truck chassis
        - **Rail transport**: Corner castings secure to rail wagons
        - **Stacking**: Containers stack directly on corner castings (weight path)
        
        **The Twist-Lock Mechanism:**
        - Twist-locks insert into corner casting oval holes
        - Operator rotates lock 90 degrees to secure
        - Automated systems now handle twist-locks mechanically
        - Traditional method required stevedores working under suspended loads (hazardous)
        """)
    
    with col2:
        st.markdown("""
        **Other Structural Components:**
        
        **Floor:**
        - Hardwood (tropical hardwood) or steel floor construction
        - Must support distributed load up to maximum payload
        - Forklift access channels for loading/unloading operations
        - Drainage channels if liquid cargo spills
        - Load-bearing strength critical for heavy cargo
        
        **Walls and Roof:**
        - **Corrugated steel**: Provides strength while optimising weight
        - Weatherproof seals prevent water ingress
        - Structural rigidity for safe stacking
        - Double doors at one end with rubber seals
        - Locking bars secure doors (often with container seal)
        
        **Lashing Points:**
        - Additional securing points for internal cargo
        - Lashing rings or tracks for straps/chains
        - Prevent cargo shift during transport
        """)
    
    st.markdown('<p class="subsection-header">CSC Plate: Container Safety Convention</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Every container must have a **CSC Plate** (Container Safety Convention) affixed to it. This metal plate 
    contains critical safety and identification information required by international maritime law.
    
    **CSC Plate Information:**
    - **Container owner/operator**: Company name and details
    - **Container number**: Unique identification (discussed in next section)
    - **Manufacturing date**: When container was built
    - **Max gross weight**: Maximum total weight including container itself
    - **Tare weight**: Empty container weight
    - **Max payload**: Maximum cargo weight (gross minus tare)
    - **Max volume**: Cubic capacity that can be packed
    - **CSC approval number**: Safety certification
    - **Inspection dates**: Required periodic inspections
    - **Classification society marks**: Inspection and certification bodies
    
    **Legal Requirements:**
    - Required by International Convention for Safe Containers (CSC)
    - Must be clearly visible for inspection
    - Container cannot be loaded on vessel without valid CSC certification
    - Periodic inspections required (typically every 30 months)
    - Failure to maintain valid CSC can result in container being detained at port
    """)
    
    st.markdown('<p class="subsection-header">Weight Specifications and Considerations</p>', unsafe_allow_html=True)
    
    # Weight table - Enhanced with more detail
    weight_specs = pd.DataFrame({
        'Specification': [
            'Max Gross Weight (ISO)',
            'Max Gross Weight (Some Countries)',
            'Tare Weight (20ft)',
            'Tare Weight (40ft)',
            'Tare Weight (40ft HC)',
            'Max Payload (20ft)',
            'Max Payload (40ft)',
            'Typical Loaded Weight (20ft)',
            'Typical Loaded Weight (40ft)'
        ],
        'Value': [
            '30,480 kg (30.48 tonnes)',
            'Up to 36,000 kg (36 tonnes)',
            '2,200-2,400 kg',
            '3,600-3,900 kg',
            '3,900-4,200 kg',
            '28,080-28,280 kg',
            '26,580-26,880 kg',
            '20,000-25,000 kg',
            '22,000-26,000 kg'
        ],
        'Notes': [
            'International ISO 668 standard, accepted globally',
            'Some jurisdictions allow higher for domestic transport',
            'Dry van, varies by manufacturer and age',
            'Standard height, varies by construction',
            'High cube slightly heavier due to extra material',
            'Max gross minus tare weight (theoretical maximum)',
            'Max gross minus tare weight (theoretical maximum)',
            'Most containers volume-limited, not weight-limited',
            'Most 40ft containers reach volume limit before weight limit'
        ]
    })
    
    st.dataframe(weight_specs, width='stretch', hide_index=True)
    
    st.markdown("""
    **Critical Weight Considerations:**
    
    **Volume-Limited vs Weight-Limited Cargo:**
    - **Most cargo is volume-limited**: Fills container before reaching weight limit
    - Examples of volume-limited: Furniture, clothing, electronics, packaged goods (low density)
    - **Weight-limited cargo is less common**: Reaches weight limit before filling volume
    - Examples of weight-limited: Metals, minerals, machinery, stone products (high density)
    - This is why High Cube containers are popular—extra volume rarely exceeds weight limits
    
    **Road Transport Limitations:**
    - Many countries have lower weight limits for trucks than container maximum
    - **Example**: EU allows 44 tonnes total (truck + trailer + container + cargo)
    - This restricts payload to approximately 24-26 tonnes even though container can legally hold 28 tonnes
    - Trucking companies must carefully monitor weights to avoid fines
    - Different weight limits in different countries complicate planning
    
    **SOLAS VGM (Verified Gross Mass) Requirements:**
    - **Mandatory since July 1, 2016**: SOLAS (Safety of Life at Sea) amendment
    - **All export containers must be weighed** before loading on vessel
    - **Purpose**: Prevent overweight containers that risk vessel stability
    - **Responsibility**: Shipper must provide accurate verified weight
    - **Methods**: Weigh entire packed container, or weigh cargo pieces and add tare weight
    - **Enforcement**: Container without VGM cannot be loaded on vessel
    - **Safety rationale**: Incorrect cargo weights were causing vessel accidents
    """)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ Why SOLAS VGM Matters:</strong><br><br>
    <strong>Before VGM</strong>: Shippers often provided estimated or incorrect weights. Vessels loaded based on 
    these estimates, leading to improper weight distribution.<br><br>
    <strong>Problem</strong>: Actual weights sometimes differed by 3-5 tonnes per container. Multiply this across 
    20,000 containers and you have massive stability and structural stress issues.<br><br>
    <strong>Result</strong>: Container stack collapses, vessel listing, structural failures, and in extreme cases, 
    vessel losses.<br><br>
    <strong>VGM Solution</strong>: Mandatory verified weighing ensures vessels are loaded safely within structural 
    limits with proper stability.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 6: Container Identification System
    # ============================================================================
    
    st.markdown('<p class="section-header">Container Identification: The ISO 6346 System</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Every container in the world has a unique identification number following the **ISO 6346** international 
    standard. This system enables global tracking and ensures no two containers share the same identifier.
    """)
    
    st.markdown('<p class="subsection-header">Container Number Format and Structure</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Standard Format:** `ABCD 123456-7`
    
    **Example:** `MAEU 1234567`
    
    **Three Components:**
    
    **1. Owner Code (4 letters):**
    - **First 3 letters**: Identify container owner/operator (assigned by BIC - Bureau International des Containers)
    - **4th letter**: Always "**U**" (indicates "**U**nit" - i.e., freight container)
    - Examples of owner codes:
      - **MAEU** = Maersk Line (Denmark)
      - **MSCU** = Mediterranean Shipping Company - MSC (Switzerland)
      - **CMAU** = CMA CGM (France)
      - **CSQU** = COSCO Shipping (China)
      - **TEMU** = ONE - Ocean Network Express (Japan)
      - **HLBU** = Hapag-Lloyd (Germany)
      - **YMLU** = Yang Ming Line (Taiwan)
    - Owner codes are globally registered and unique
    - Operators recognize major lines instantly by these codes
    
    **2. Serial Number (6 digits):**
    - Unique number assigned sequentially by owner
    - Range: 000000 to 999999
    - Each owner manages their own serial number sequence
    - Usually allocated sequentially as new containers manufactured
    
    **3. Check Digit (1 digit):**
    - Mathematical validation digit calculated from owner code and serial number
    - **Purpose**: Detects data entry errors (transposition, typos)
    - **Algorithm**: Weighted sum modulo 11
    - Critically important when processing thousands of containers per day
    - OCR (Optical Character Recognition) systems validate check digit automatically
    
    **Size and Type Code (separate 4-character code):**
    - Not part of container number but appears on container
    - Indicates container specifications:
      - **1st character**: Length code (2=20ft, 4=40ft, L=45ft, M=48ft, N=53ft)
      - **2nd character**: Height code (0=8'6", 2=8'6" and higher, 5=9'6", etc.)
      - **3rd character**: Type code (G=general/dry, R=reefer, T=tank, U=open top, P=platform, etc.)
      - **4th character**: Detailed specifications (varies by type)
    - Example: **42G1** = 40ft length, High Cube height, General purpose, Standard configuration
    - Example: **22R1** = 20ft length, Standard height, Reefer, Standard configuration
    """)
    
    # Example container numbers - Enhanced
    example_numbers = pd.DataFrame({
        'Container Number': ['MAEU 1234567', 'MSCU 9876543', 'CMAU 5555555', 'TEMU 1111118', 'CSQU 7777772'],
        'Owner Code': ['MAEU', 'MSCU', 'CMAU', 'TEMU', 'CSQU'],
        'Owner': ['Maersk Line', 'MSC', 'CMA CGM', 'ONE', 'COSCO'],
        'Serial': ['123456', '987654', '555555', '111111', '777777'],
        'Check Digit': ['7', '3', '5', '8', '2'],
        'Size/Type (example)': ['42G1', '22G1', '45R1', '42G1', '22T1'],
        'Meaning': ['40ft HC dry van', '20ft std dry van', '45ft HC reefer', '40ft HC dry van', '20ft std tank']
    })
    
    st.dataframe(example_numbers, width='stretch', hide_index=True)
    
    st.markdown("""
    **Why This System is Essential:**
    - **Global uniqueness**: No two containers anywhere in the world have the same number
    - **Instant identification**: Operators recognize owner by code (MAEU = immediately know it's Maersk)
    - **Error detection**: Check digit catches data entry mistakes (prevents wrong container being tracked)
    - **Automated processing**: OCR cameras at gates read and validate container numbers automatically
    - **Supply chain tracking**: Container can be tracked globally across ocean, rail, truck
    - **Documentation matching**: Bill of lading, customs forms, and physical container all linked by this number
    - **Damage and repair tracking**: Container's service history maintained throughout its 12-15 year lifespan
    """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Automated Container Identification:</strong><br><br>
    Modern terminals use <strong>Optical Character Recognition (OCR)</strong> systems mounted on gate portals:<br>
    - <strong>Cameras</strong> automatically photograph trucks entering/exiting<br>
    - <strong>OCR software</strong> reads container number, chassis number, truck licence plate<br>
    - <strong>System validates</strong> check digit to confirm accurate read<br>
    - <strong>Recognition accuracy</strong>: 95-98% (manual verification for failed reads)<br>
    - <strong>Processing speed</strong>: Instant, as truck passes through gate<br>
    - <strong>Gate throughput</strong>: Automated lanes process trucks in 20-30 seconds vs 5-10 minutes manual<br><br>
    This automation is only possible because of the ISO 6346 standardised numbering system.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 7: Bay-Row-Tier Coordinate System
    # ============================================================================
    
    st.markdown('<p class="section-header">Bay-Row-Tier: 3D Positioning System</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Containers in terminals and vessels are positioned using a precise three-dimensional coordinate system 
    called **Bay-Row-Tier**. This addressing system enables unambiguous identification of every container 
    position, which is essential for stowage planning, crane operations, and cargo tracking.
    """)
    
    st.markdown('<p class="subsection-header">The Three Dimensions Explained</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Bay (Longitudinal Position)**
        
        **Definition:**
        - Position along vessel/block length
        - Numbered front to back
        
        **On Vessels:**
        - Bow (front) to Stern (back)
        - **Odd numbers**: 20ft bay positions (01, 03, 05, 07...)
        - **Even numbers**: 40ft bay positions (02, 04, 06, 08...)
        - A 40ft container **occupies 2 bays** (e.g., Bay 02 spans bays 01+03)
        - Large vessels: Bay numbers up to 200+
        - 20ft containers can go in odd bays; 40ft can only go in even bays
        
        **In Terminals:**
        - Similar longitudinal concept
        - Yard blocks divided into bays
        - Sequential numbering along block length
        - Bays typically 20ft intervals
        """)
    
    with col2:
        st.markdown("""
        **Row (Transverse Position)**
        
        **Definition:**
        - Position across width
        - Numbered left to right (or centre out)
        
        **On Vessels:**
        - Port (left) to Starboard (right)
        - **Centre line**: 00
        - **Odd numbers**: Port side (01, 03, 05, 07...)
        - **Even numbers**: Starboard side (02, 04, 06, 08...)
        - Range depends on vessel width (e.g., 00-24 for wide vessels)
        - Mega vessels: 24 containers across (Row 00-23)
        
        **In Terminals:**
        - Across yard block width (perpendicular to block length)
        - Usually numbered 01-08 or 01-10
        - Depends on RTG/RMG span width
        - Simpler numbering than vessels (just sequential)
        """)
    
    with col3:
        st.markdown("""
        **Tier (Vertical Position)**
        
        **Definition:**
        - Vertical stacking position
        - Numbered bottom to top
        
        **On Vessels:**
        - **Below deck**: 02, 04, 06, 08... (even numbers, descending from deck)
        - **Deck level**: 80
        - **Above deck**: 82, 84, 86, 88, 90... (even numbers, ascending)
        - Example: Tier 02 = 1 below deck, Tier 86 = 3 above deck
        
        **In Terminals:**
        - **Ground level**: 01
        - **Second tier**: 02
        - **Third tier**: 03, etc.
        - Typical stacking: 01-06 (six high with RTG)
        - Some terminals stack higher with RMG (up to 08 or 10)
        """)
    
    st.markdown("""
    **Example Container Position on Vessel:**
    
    **Bay 12, Row 04, Tier 86**
    
    Let's decode this position:
    - **Bay 12**: 12th longitudinal position from bow (this is a 40ft container position, as Bay 12 is even)
    - **Row 04**: 4th position from port side, which means this is on the **starboard (right) side** (even number)
    - **Tier 86**: This is **3 tiers above deck level** (Deck=80, 82=1st above, 84=2nd above, 86=3rd above)
    
    So this container is toward the front-middle of the vessel, on the starboard side, three containers above 
    the deck level. The crane operator can immediately locate this container using these coordinates.
    
    **Why This System is Critical:**
    
    **Unambiguous Positioning:**
    - Every position on vessel or in terminal has a unique three-dimensional coordinate
    - No confusion about which container to pick or where to place it
    - Crane operators work with thousands of containers—precise addressing essential
    
    **Stowage Planning:**
    - Stowage planners specify exact position for each container on vessel
    - Considers weight distribution, destination sequence, container type
    - Bay plans show complete vessel load with Bay-Row-Tier for every container
    - Digital systems automatically generate stowage plans using these coordinates
    
    **Operational Efficiency:**
    - Crane operators receive exact Bay-Row-Tier instructions
    - Terminal Operating System (TOS) tracks every container by position
    - No time wasted searching for containers
    - Automated equipment (ASC, AGV) navigate using these coordinates
    
    **Safety:**
    - Ensures proper weight distribution (stability)
    - Dangerous goods segregation verified by position
    - Stack weight limits monitored by tier
    - Prevents overloading structural elements
    
    **Vessel Stability:**
    - Longitudinal balance (bow to stern): controlled by bay distribution
    - Transverse balance (port to starboard): controlled by row distribution
    - Vertical centre of gravity: controlled by tier distribution (heavy low, light high)
    - Stowage planners use Bay-Row-Tier coordinates to calculate and maintain vessel stability
    """)
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 From Planning to Execution:</strong><br><br>
    <strong>48 hours before arrival</strong>: Stowage planner creates vessel loading plan with Bay-Row-Tier for 
    each container<br>
    <strong>24 hours before arrival</strong>: Plan uploaded to Terminal Operating System (TOS)<br>
    <strong>At vessel arrival</strong>: Crane operators receive work instructions with exact Bay-Row-Tier positions<br>
    <strong>During operations</strong>: TOS tracks container movements in real-time by Bay-Row-Tier<br>
    <strong>After completion</strong>: Final bay plan confirmed with actual positions loaded<br><br>
    This coordinate system enables handling 10,000+ containers per vessel call with precision and safety.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 8: Container Economics
    # ============================================================================
    
    st.markdown('<p class="section-header">Container Economics: The Business Side</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Understanding container costs helps explain operational decisions by shipping lines and terminal operators. 
    Containers represent significant capital investment and ongoing operational costs.
    """)
    
    st.markdown('<p class="subsection-header">Container Costs and Economics</p>', unsafe_allow_html=True)
    
    # Cost breakdown - Enhanced with more detail
    container_costs = pd.DataFrame({
        'Item': [
            'New 20ft Dry Container',
            'New 40ft Dry Container',
            'New 40ft High Cube Dry',
            'New 40ft Reefer',
            'Container Lifespan',
            'Annual Maintenance',
            'Daily Leasing Cost (Dry)',
            'Daily Leasing Cost (Reefer)',
            'Repositioning Cost (Empty)',
            'Minor Repair (Dents/Scratches)',
            'Major Repair (Structural)',
            'Total Fleet (Global)',
            'Empty Containers Moved'
        ],
        'Cost/Value': [
            '$2,000-2,500',
            '$2,500-3,000',
            '$3,000-3,500',
            '$12,000-15,000',
            '12-15 years',
            '$100-200 per container',
            '$1-3',
            '$8-15',
            '$500-2,000',
            '$200-500',
            '$1,000-3,000',
            '~55 million TEU',
            '20-25% of moves'
        ],
        'Notes': [
            'Basic dry container, prices fluctuate with steel costs',
            'Most common type globally, mass production benefits',
            'Extra height adds material cost but provides volume flexibility',
            'Refrigeration unit accounts for majority of cost premium',
            'After service life, retired or sold for storage/conversion',
            'Periodic inspection, cleaning, minor repairs',
            'Daily rate, varies with market conditions and lease term',
            'Much higher due to reefer unit maintenance and monitoring',
            'Moving empties to where demand exists, varies by distance',
            'Cosmetic and minor structural repairs, dents in walls',
            'Floor replacement, extensive corrosion, structural damage',
            'Approximate global container fleet size (2024)',
            'Industry estimate of empty container movements annually'
        ]
    })
    
    st.dataframe(container_costs, width='stretch', hide_index=True)
    
    st.markdown("""
    **The Empty Container Problem: Trade Imbalances**
    
    One of the most significant challenges in container shipping economics is the **empty container repositioning 
    problem**. This stems from fundamental global trade imbalances.
    
    **The Problem:**
    - Trade flows are **not balanced** in both directions
    - **Example**: Asia exports far more goods to Europe/North America than it imports
    - Containers **accumulate** at destination ports (deficit at origin, surplus at destination)
    - **Real example**: China exports 4 TEU to US for every 1 TEU imported from US
    - Result: Massive container surpluses in US ports, shortages in Chinese ports
    
    **Regional Trade Imbalances:**
    - **Asia → Europe/North America**: Heavy export flows (manufacturing goods, electronics, clothing)
    - **Europe/North America → Asia**: Lighter import flows (raw materials, some specialized goods)
    - **Europe → Africa**: Equipment, machinery flows south
    - **Africa → Europe**: Raw materials, agricultural products flow north
    - Pattern: Manufacturing regions accumulate empties at consumption regions
    
    **Repositioning Costs:**
    - Costs **$500-2,000 per container** depending on distance
    - This is **pure cost**—no revenue earned moving empty containers
    - Vessel space used for empties = **lost revenue opportunity** (could carry paying cargo)
    - Terminal handling costs still apply (empties need to be loaded/unloaded)
    - Industry estimates **20-25% of global container moves are empty**
    
    **Solutions and Strategies:**
    
    **1. Backhaul Incentives:**
    - Offer **dramatically reduced rates** on return direction to attract any cargo
    - Example: China → US might cost $1,500/TEU, but US → China only $400/TEU
    - Still better to carry cargo cheaply than move empty container
    
    **2. Regional Triangulation:**
    - Route empties through **third countries** where they're needed
    - Example: Empties from US → Panama → Chile (where mining equipment is shipped to China)
    - Creates longer routing but captures revenue on multiple legs
    
    **3. Container Leasing Companies:**
    - Specialized companies **own large fleets** and lease to shipping lines
    - Help **balance supply/demand** across regions
    - Can reposition containers between lessees
    - Major lessors: Triton, Textainer, CAI International
    
    **4. One-Way Leases:**
    - Lease container for **one-way trip** only
    - Lessor handles repositioning
    - Shifts repositioning cost and risk to leasing company
    
    **5. Strategic Container Positioning:**
    - **Predictive analytics** forecast where containers will be needed
    - Pre-position empties in advance of seasonal demand
    - Example: Position empties in agricultural regions before harvest season
    
    **6. Collapsible Containers (Future):**
    - Research into containers that **fold flat** when empty
    - Would dramatically reduce space needed for empty repositioning
    - Technical challenges remain (structural integrity, cost)
    - Not yet commercially viable at scale
    """)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ Economic Impact of Empty Repositioning:</strong><br><br>
    <strong>Global scale</strong>: With ~800M TEU moved annually, 20-25% empty = 160-200M empty TEU moves<br>
    <strong>Cost estimate</strong>: At $1,000 average repositioning cost = $160-200 billion annually<br>
    <strong>Environmental impact</strong>: Ships burning fuel to move empty containers across oceans<br>
    <strong>Capacity waste</strong>: Vessel space and port capacity consumed by empties rather than revenue cargo<br>
    <strong>Rate pressure</strong>: Shipping lines must build repositioning costs into freight rates<br><br>
    This is why backhaul rates (return direction) are often 50-70% lower than headhaul rates—shipping lines would 
    rather carry cargo cheaply than move empty containers.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 9: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways: Containers & Containerisation</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **ISO Standards Foundation:**
        - Universal **2.438m (8ft) width** - the fundamental global standard
        - Standard lengths: **20ft, 40ft, 45ft** (plus 48ft/53ft North America only)
        - Heights: **8ft 6in (standard)** or **9ft 6in (high cube)**
        - Max gross weight: **30,480 kg (30.48 tonnes)** - international standard
        - Standardisation enables global interoperability of equipment and infrastructure
        
        **TEU Measurement System:**
        - TEU = **Twenty-foot Equivalent Unit** (universal capacity metric)
        - 20ft container = **1 TEU**, 40ft container = **2 TEU**
        - Universal measure for comparing capacity, throughput, and vessel sizes
        - Normalises different container size mixes into single metric
        - Essential for port planning and capacity measurement
        
        **Container Type Distribution:**
        - **Dry van: ~90%** of fleet (general cargo)
        - **Reefer: ~6%** (temperature-controlled, requires power)
        - **Specialised: <4%** (open top, flat rack, tank, OOG)
        - Each type requires different handling and infrastructure
        
        **Container Anatomy:**
        - **Corner castings**: Most critical component for lifting and securing
        - **CSC plate**: Legal requirement for safety certification
        - **Weight**: Tare 2.3-4.2 tonnes, max payload 25-28 tonnes
        - **SOLAS VGM**: Mandatory verified weighing since 2016 (safety)
        """)
    
    with col2:
        st.markdown("""
        **ISO 6346 Identification:**
        - Format: **Owner code (4 letters) + Serial (6 digits) + Check digit**
        - Example: MAEU 1234567 (Maersk container)
        - Globally unique identification for every container
        - Enables automated tracking and processing
        - Check digit validates accurate data entry
        
        **Bay-Row-Tier System:**
        - 3D coordinate system for precise positioning
        - **Bay**: Longitudinal (front to back, odd=20ft, even=40ft)
        - **Row**: Transverse (left to right, port/starboard)
        - **Tier**: Vertical (bottom to top, below/above deck)
        - Enables unambiguous positioning in vessels and terminals
        - Critical for stowage planning and crane operations
        
        **Container Economics:**
        - Purchase cost: $2,000-3,500 (dry), $12,000-15,000 (reefer)
        - Lifespan: 12-15 years of service
        - Empty repositioning costs: $500-2,000 per container
        - **20-25% of global moves are empty** containers
        - Major cost driver due to trade imbalances
        
        **Historical Context:**
        - **1956**: Malcolm McLean's Ideal-X (birth of containerisation)
        - Reduced shipping costs by **90%+**
        - Enabled global supply chains and intermodal transport
        - Foundation of modern global trade
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Containers follow precise <strong>ISO standards</strong> (2.438m width, 20/40ft lengths, 
    30.48 tonne max weight) that enable global interoperability. The <strong>TEU (Twenty-foot Equivalent Unit)</strong> provides 
    universal measurement for the industry. Approximately <strong>90% are standard dry vans</strong>, with specialised types 
    (reefer, tank, OOG) for specific cargo requiring dedicated infrastructure. Each container has a unique <strong>ISO 
    6346 identifier</strong> (owner code + serial + check digit) enabling global tracking. The <strong>Bay-Row-Tier coordinate 
    system</strong> enables precise 3D positioning in terminals and vessels. <strong>Corner castings</strong> are the critical component 
    connecting containers to all handling equipment. Understanding these fundamentals is essential for 
    understanding how container terminal operations work and why standardisation was so revolutionary for 
    global trade.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** 🚢 Container Vessels & Evolution - Explore vessel anatomy, the dramatic growth from 
    500 TEU to 25,000+ TEU, vessel classifications (Panamax, Post-Panamax, ULCV), and the complex art of 
    stowage planning that balances stability, destination sequence, and operational efficiency.
    """)
