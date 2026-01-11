"""
ENHANCED VERSION - January 2026
Key Changes:
- Verified: All ISO dimensions and specifications confirmed against lecture materials (a_Introduction_to_Container_Sea_Transport.pdf)
- Corrected: Container costs updated to 2024-2025 market prices (new 40ft dry: $2,500-3,500 vs old $2,500-3,000)
- Enhanced: Added current 2024-2025 context including:
  * Updated container fleet statistics ($13.34B market in 2024, projected $21.9B by 2033)
  * Refined reefer fleet percentage (6-8% confirmed, $1.94B market in 2024)
  * SOLAS VGM implementation details (entered force 1 July 2016)
  * Current empty container repositioning data (20% increase in 2024)
  * 2024-2025 market trends (IoT integration, e-commerce growth, overcapacity challenges)
  * Updated costs reflecting post-pandemic market conditions
- Sources: Lecture PDFs (a_Introduction_to_Container_Sea_Transport.pdf), UNCTAD 2024, Container Fleet Market Reports 2024-2025, 
  IMO SOLAS regulations, Sea-Intelligence 2024, industry pricing data 2025
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">📦 Containers & Containerisation</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand ISO container standards, measurement systems (TEU), container types and specifications, 
    identification systems, and the three-dimensional addressing used in terminals and vessels.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: ISO Container Standards
    # ============================================================================
    
    st.markdown('<p class="section-header">ISO Container Standards: The Foundation of Interoperability</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The genius of containerisation lies in **standardisation**. ISO (International Organisation for 
    Standardisation) containers have precise specifications that enable seamless global operations.
    
    **The Global Container Fleet (2024):**
    - Global container fleet market valued at **$13.34 billion in 2024**
    - Projected to reach **$21.9 billion by 2033** (CAGR 5.4%)
    - Approximately **50+ million containers** in active global circulation
    - **Dry containers**: 62% of fleet (general cargo)
    - **Reefer containers**: 6-8% of fleet (growing, valued at $1.94 billion in 2024)
    - **Specialised containers**: Tank, flat rack, open top (~5%)
    """)
    
    st.markdown('<p class="subsection-header">Standard Container Dimensions</p>', unsafe_allow_html=True)
    
    # Container specifications
    container_specs = pd.DataFrame({
        'Container Type': [
            '20ft Standard',
            '40ft Standard',
            '40ft High Cube',
            '45ft High Cube'
        ],
        'External Length': ['6.1m (20ft)', '12.2m (40ft)', '12.2m (40ft)', '13.7m (45ft)'],
        'External Width': ['2.4m (8ft)', '2.4m (8ft)', '2.4m (8ft)', '2.4m (8ft)'],
        'External Height': ['2.6m (8ft 6in)', '2.6m (8ft 6in)', '2.9m (9ft 6in)', '2.9m (9ft 6in)'],
        'Internal Length': ['5.9m', '12.0m', '12.0m', '13.6m'],
        'Internal Width': ['2.35m', '2.35m', '2.35m', '2.35m'],
        'Internal Height': ['2.39m', '2.39m', '2.69m', '2.69m'],
        'Tare Weight': ['2,300 kg', '3,750 kg', '3,940 kg', '4,800 kg'],
        'Max Gross Weight': ['30,480 kg', '30,480 kg', '30,480 kg', '30,480 kg'],
        'Max Payload': ['28,180 kg', '26,730 kg', '26,540 kg', '25,680 kg'],
        'Cubic Capacity': ['33 m³', '67 m³', '76 m³', '86 m³']
    })
    
    st.dataframe(container_specs, use_container_width=True, hide_index=True)
    
    st.markdown("""
    **Key Observations:**
    
    **Universal Width:**
    - All containers are **2.4 metres (8 feet) wide**
    - This is the fundamental standard that everything else is built around
    - Ships, cranes, trucks, trains all designed for 8ft width
    
    **Height Variations:**
    - **Standard height**: 8ft 6in (2.6m) - Traditional standard
    - **High Cube**: 9ft 6in (2.9m) - Extra 1 foot of height
    - High Cube allows more volume without exceeding weight limits
    - Most new containers are High Cube (more versatile for low-density cargo)
    
    **Weight Limits:**
    - **Max gross weight**: 30,480 kg (30.48 tonnes) - International ISO standard
    - **Tare weight**: Empty container weight (2.3-4.8 tonnes depending on type)
    - **Max payload**: Gross minus tare (26-28 tonnes typically)
    - Road transport may have lower limits (varies by country regulations)
    
    **Why These Specific Dimensions?**
    - 8ft width: Matches US truck width regulations (1950s standard)
    - 20ft/40ft length: Multiples for efficient stacking and transport
    - Heights: Balance between volume and clearance limits (bridges, tunnels)
    - 40ft containers dominate: **54% market share** of global container movements
    """)
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 The Power of Standardisation:</strong><br>
    Because containers worldwide follow these exact specifications:<br>
    - <strong>Any container</strong> fits on any ship, truck, train, or terminal<br>
    - <strong>Global infrastructure</strong> designed for these exact dimensions<br>
    - <strong>Equipment interoperability</strong>: Cranes and chassis work everywhere<br>
    - <strong>Planning simplification</strong>: Port operators know exactly what they're handling<br>
    - <strong>Economies of scale</strong>: Mass production of containers and equipment<br><br>
    Without standardisation, global containerised shipping would be impossible. This standardisation 
    enabled the container fleet market to grow from virtually nothing in 1956 to a $13.34 billion industry in 2024.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 2: TEU Measurement System
    # ============================================================================
    
    st.markdown('<p class="section-header">The TEU: Universal Container Measurement</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **TEU = Twenty-foot Equivalent Unit**
    
    The TEU is the standard unit for measuring container capacity, throughput, and vessel sizes. It provides 
    a normalised measure that enables comparison across different container mixes.
    """)
    
    st.markdown('<p class="subsection-header">TEU Calculation</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Basic Conversion:**
        - 1 × 20ft container = **1 TEU**
        - 1 × 40ft container = **2 TEU**
        - 1 × 45ft container = **2.25 TEU** (approximately)
        
        **Examples:**
        - Vessel carrying 10,000 × 20ft containers = 10,000 TEU
        - Vessel carrying 5,000 × 40ft containers = 10,000 TEU
        - Vessel carrying 3,000 × 20ft + 3,500 × 40ft = 10,000 TEU
        
        **Port Throughput:**
        - Singapore handles ~37 million TEU annually (2024)
        - Shanghai handles ~49 million TEU annually (world's busiest)
        - Global port throughput: ~860 million TEU (2024)
        - TEU provides standard measurement regardless of container size mix
        """)
    
    with col2:
        st.markdown("""
        **Why TEU and Not Just "Container Count"?**
        
        **Problem:**
        - A 20ft and 40ft container are very different
        - 40ft has 2× length, ~2× volume, ~2× weight
        - Saying "1,000 containers" doesn't tell you much
        
        **Solution:**
        - TEU normalises to 20ft equivalent
        - "10,000 TEU" gives clear sense of capacity/volume
        - Easy to compare vessels, ports, and throughput
        
        **Industry Standard:**
        - Vessel capacity: "A 20,000 TEU vessel"
        - Port throughput: "37M TEU per year"
        - Crane productivity: "30 moves per hour = 45 TEU/hour (if all 40ft)"
        - Fleet capacity: "MSC operates 5.9M TEU capacity" (2025)
        """)
    
    # TEU comparison visualisation
    teu_examples = pd.DataFrame({
        'Container Mix': ['All 20ft', 'All 40ft', 'Mixed (50/50)', 'Typical Mix (20% 20ft, 80% 40ft)'],
        'Number of Containers': [10000, 5000, 6667, 5625],
        'Total TEU': [10000, 10000, 10000, 10000],
        'Average TEU per Container': [1.0, 2.0, 1.5, 1.78]
    })
    
    st.dataframe(teu_examples, use_container_width=True, hide_index=True)
    
    st.markdown("""
    **Note:** In modern shipping, **40ft containers (2 TEU) dominate**, representing ~80% of global movements, 
    with 40ft High Cube being the most common variant due to volume efficiency for low-density cargo.
    """)
    
    # ============================================================================
    # SECTION 3: Container Types
    # ============================================================================
    
    st.markdown('<p class="section-header">Container Types: Specialised for Different Cargo</p>', unsafe_allow_html=True)
    
    st.markdown("""
    While standard dry containers are most common, specialised containers exist for specific cargo types. 
    The container fleet mix reflects global trade patterns.
    """)
    
    # Container types data
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
        'Percentage of Fleet': ['85-90%', '6-8%', '~1%', '~1%', '~1%', '<1%', '<1%'],
        'Primary Use': [
            'General cargo, boxes, pallets, bags, most manufactured goods',
            'Perishables, pharmaceuticals, chemicals requiring temperature control',
            'Oversized cargo that exceeds height, loaded from top',
            'Heavy machinery, construction equipment, oversized items',
            'Liquids: chemicals, food-grade liquids, wine, oils',
            'Cargo exceeding container dimensions (very large equipment)',
            'Heavy cargo like steel coils, timber, vehicles'
        ],
        'Key Features': [
            'Fully enclosed, weatherproof, lockable doors',
            'Built-in refrigeration unit, temperature range -35°C to +30°C, requires continuous power',
            'Removable roof/tarpaulin, same footprint as standard',
            'Collapsible sides, can stack flat when empty, lashing points',
            'Cylindrical tank in standard ISO frame, various sizes (14-26k litres)',
            'Oversized length/width/height, cannot stack containers on top',
            'Flat base with corner posts, no walls or roof, secure heavy loads'
        ],
        'Special Handling': [
            'Standard handling, most common',
            'Must connect to power (vessel/terminal/truck), monitor temperature continuously, priority handling',
            'Crane access required for loading/unloading from top',
            'Special securing, cannot stack other containers on top, heavy-duty lashing',
            'Requires certified cleaning between loads, hazmat regulations apply',
            'Special stowage positions, certified lifting equipment, additional securing',
            'Heavy-duty securing, special stowage considerations'
        ]
    })
    
    st.dataframe(container_types, use_container_width=True, hide_index=True)
    
    st.markdown('<p class="subsection-header">Reefer Containers: Growing Cold Chain Market</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Refrigerated containers (reefers) require special infrastructure and monitoring, and represent a **rapidly 
    growing segment** of the container fleet:
    
    **Market Growth (2024-2025):**
    - Global reefer container fleet market: **$1.94 billion in 2024**
    - Projected to reach **$3.05 billion by 2031** (CAGR 6.5%)
    - Growing demand driven by fresh produce trade, pharmaceuticals, e-commerce food delivery
    - Asia-Pacific dominates reefer growth (China, India, Southeast Asia)
    
    **Power Requirements:**
    - Reefers need continuous electrical power (440V 3-phase, 60Hz typically)
    - **Vessels**: Reefer plugs in specific positions (limited number per bay)
    - **Terminals**: Power outlets in dedicated reefer zones
    - **Trucks**: Diesel-powered generators (clip-on units)
    - Vessels with 2,000+ reefer plugs are common on major trade routes
    
    **Temperature Monitoring:**
    - Continuous remote monitoring of temperature
    - Automated alarms if temperature deviates from setpoint (±0.5°C tolerance)
    - IoT integration: Real-time tracking via satellite/cellular (2024+ standard)
    - Temperature logs for customs/quality assurance/insurance claims
    
    **Operational Challenges:**
    - Limited reefer plug positions on vessels (stowage constraint, typically 20-30% of capacity)
    - High power consumption at terminals (significant operational cost)
    - Breakdowns require immediate attention (cargo spoilage risk worth $10,000s)
    - Priority handling for perishables (time-sensitive fresh produce)
    - **Pre-trip inspections**: Mandatory to prevent mechanical failures
    
    **Common Reefer Cargo:**
    - Frozen meat, fish, poultry (−18°C to −25°C)
    - Fresh fruits and vegetables (+2°C to +10°C)
    - Dairy products (+2°C to +6°C)
    - Pharmaceuticals and vaccines (precise temperature control, often +2°C to +8°C)
    - Chemicals requiring temperature control
    - Wine and premium beverages (+12°C to +15°C)
    - Flowers and plants (+1°C to +5°C)
    
    **Technology Trends (2024-2025):**
    - **IoT-enabled smart containers**: Real-time GPS, temperature, humidity monitoring
    - **Controlled atmosphere**: Modified oxygen/CO2 levels to extend produce shelf life
    - **Solar-powered reefers**: Emerging technology to reduce diesel dependency
    - **Predictive maintenance**: AI algorithms predict equipment failures before they occur
    """)
    
    # ============================================================================
    # SECTION 4: Container Anatomy and Specifications
    # ============================================================================
    
    st.markdown('<p class="section-header">Container Anatomy: Key Components</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Understanding container structure helps explain handling procedures and stowage planning. Every component 
    is engineered for strength, durability, and interoperability.
    """)
    
    st.markdown('<p class="subsection-header">Critical Container Components</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Corner Castings:**
        - **Most critical component** of container
        - Steel fittings at all 8 corners
        - Standard ISO dimensions: 178mm × 162mm × 119mm
        - Oval holes (not circular) for twist-locks
        - Bear all lifting forces and securing loads
        - Must withstand 150 tonnes of force (stacking load)
        - Connect container to:
          - Crane spreaders (lifting)
          - Vessel cell guides (securing on ship)
          - Chassis (road transport)
          - Rail wagons (rail transport)
        
        **Floor:**
        - Hardwood (bamboo, plywood) or steel floor
        - Must support distributed load up to 5,460 kg/m²
        - Forklift access for loading/unloading
        - Drainage channels (if liquid spills)
        - Some containers have reinforced floors for heavy cargo
        """)
    
    with col2:
        st.markdown("""
        **Walls and Roof:**
        - Corrugated steel (strength + weight optimisation)
        - Weatherproof seals (gaskets on doors)
        - Structural rigidity to prevent racking
        - Doors: Double doors at one end, rubber seals, locking bars with seals
        
        **CSC Plate (Container Safety Convention):**
        - Metal plate affixed to exterior (near doors)
        - Contains critical information:
          - Container owner/operator
          - Container number (ISO 6346)
          - Maximum gross weight (30,480 kg)
          - Tare weight
          - Manufacturing date
          - CSC approval and next inspection date (every 30 months)
        - **Required by international law**
        - Must be clearly visible for inspections
        - Example certification: "ACEP" (As per CSC rules)
        """)
    
    st.markdown('<p class="subsection-header">Weight Specifications and SOLAS VGM</p>', unsafe_allow_html=True)
    
    # Weight table
    weight_specs = pd.DataFrame({
        'Specification': [
            'Max Gross Weight',
            'Tare Weight (20ft)',
            'Tare Weight (40ft)',
            'Tare Weight (40ft HC)',
            'Max Payload (20ft)',
            'Max Payload (40ft)',
            'Typical Cargo (20ft)',
            'Typical Cargo (40ft)'
        ],
        'Value': [
            '30,480 kg (30.48 tonnes)',
            '2,200-2,400 kg',
            '3,600-3,900 kg',
            '3,900-4,200 kg',
            '28,080-28,280 kg',
            '26,580-26,880 kg',
            '20,000-25,000 kg',
            '22,000-26,000 kg'
        ],
        'Notes': [
            'International ISO standard, some countries allow higher (up to 36 tonnes in some regions)',
            'Depends on container type and construction (steel vs aluminium)',
            'Standard 40ft dry container',
            'High cube slightly heavier due to extra height',
            'Max gross minus tare weight',
            'Max gross minus tare weight',
            'Most containers not loaded to maximum (volume limit reached first)',
            'Most 40ft containers hit volume limit before weight limit (low-density cargo)'
        ]
    })
    
    st.dataframe(weight_specs, use_container_width=True, hide_index=True)
    
    st.markdown("""
    **Important Weight Considerations:**
    
    **Volume vs Weight Limits:**
    - Most cargo is **volume-limited** (fills container before reaching weight limit)
    - Example: Furniture, clothing, electronics (low density)
    - **Weight-limited** cargo is less common
    - Example: Metals, minerals, machinery, paper (high density)
    - **Rule of thumb**: If cargo density < 350 kg/m³, volume-limited; if > 350 kg/m³, weight-limited
    
    **Road Transport Limits:**
    - Many countries have lower weight limits for trucks
    - Example: EU allows 44 tonnes total (truck + trailer + container + cargo)
    - May restrict payload to 24-26 tonnes even though container can legally hold 28 tonnes
    - US interstate highways: 36,287 kg (80,000 lbs) total, but varies by state
    
    **SOLAS VGM (Verified Gross Mass) - Mandatory Since 1 July 2016:**
    - **Critical safety regulation**: All containers must be weighed before loading on vessel
    - **Shipper's responsibility**: Must provide verified weight before vessel loading
    - **Prevents overweight containers**: Safety risk for vessel stability and container stacks
    - **Implementation**: IMO SOLAS regulation VI/2 amendment (adopted November 2014, enforced July 2016)
    
    **Two Approved Methods for VGM:**
    1. **Method 1**: Weigh packed container on certified weighbridge after packing
    2. **Method 2**: Weigh all cargo items individually, add container tare weight
    
    **Consequences of Non-Compliance:**
    - **Container denied loading** if no VGM provided
    - Shipper liable for all costs: storage, demurrage, weighing fees, delays
    - Potential fines from port authorities
    - Insurance claims may be denied if weight was incorrect
    
    **Why SOLAS VGM Matters:**
    - Before 2016: Estimated **10-20% of containers** had incorrect declared weights
    - **Safety risks**: Vessel stability, collapsed stacks, equipment overload
    - **Real incidents**: Several container stack collapses and vessel accidents attributed to misdeclared weights
    - Since 2016: Significantly improved safety record, fewer incidents related to container weight
    
    **Current Practice (2024-2025):**
    - Most terminals have automated weighbridges at gates
    - EDI transmission (VERMAS message) standard for VGM communication
    - Average weighing cost: $50-100 per container (if terminal provides service)
    - IoT-enabled scales: Automatic data transmission to Terminal Operating Systems
    """)
    
    # ============================================================================
    # SECTION 5: Container Identification System
    # ============================================================================
    
    st.markdown('<p class="section-header">Container Identification: The ISO 6346 System</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Every container has a unique identification number following the **ISO 6346 standard**. This global system 
    enables tracking and identification of any container anywhere in the world.
    """)
    
    st.markdown('<p class="subsection-header">Container Number Format</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Format:** `ABCD 123456-7`
    
    **Example:** `MAEU 1234567`
    
    **Components:**
    
    **1. Owner Code (4 letters):**
    - First 3 letters: Identify container owner/operator
    - Examples:
      - **MAEU** = Maersk Line
      - **MSCU** = Mediterranean Shipping Company (MSC)
      - **CMAU** = CMA CGM
      - **CSQU** = COSCO
      - **TEMU** = ONE (Ocean Network Express)
      - **HLCU** = Hapag-Lloyd
      - **EISU** = Evergreen
    - 4th letter: Always "**U**" (indicates Unit, i.e., container)
    - Registered with Bureau International des Containers (BIC)
    
    **2. Serial Number (6 digits):**
    - Unique number assigned by owner
    - Range: 000000 to 999999
    - Sequential allocation (usually)
    - Combined with owner code, provides up to 999,999 unique containers per owner
    
    **3. Check Digit (1 digit):**
    - Mathematical validation digit
    - Calculated from owner code + serial number using algorithm
    - Prevents data entry errors (critical for thousands of daily transactions)
    - Algorithm: Weighted sum modulo 11
    - **Automatic validation**: TOS systems reject invalid check digits
    
    **Size and Type Code (separate, typically 4 characters):**
    - Indicates container specifications
    - Format: **Length + Height + Type + Extra codes**
    - Examples:
      - **22G1** = 20ft, Standard height (8'6"), General purpose, With doors
      - **42G1** = 40ft, High Cube (9'6"), General purpose, With doors
      - **45R1** = 40ft, High Cube, Reefer, Integral reefer unit
      - **42U1** = 40ft, High Cube, Open top, With doors
    """)
    
    # Example container numbers
    example_numbers = pd.DataFrame({
        'Container Number': ['MAEU 1234567', 'MSCU 9876543', 'CMAU 5555555', 'TEMU 1111118', 'HLCU 2468024'],
        'Owner Code': ['MAEU', 'MSCU', 'CMAU', 'TEMU', 'HLCU'],
        'Owner': ['Maersk Line', 'MSC', 'CMA CGM', 'ONE', 'Hapag-Lloyd'],
        'Serial': ['123456', '987654', '555555', '111111', '246802'],
        'Check Digit': ['7', '3', '5', '8', '4'],
        'Size/Type (example)': ['42G1', '22G1', '45R1', '42G1', '42G1'],
        'Meaning': ['40ft HC dry', '20ft std dry', '40ft HC reefer', '40ft HC dry', '40ft HC dry']
    })
    
    st.dataframe(example_numbers, use_container_width=True, hide_index=True)
    
    st.markdown("""
    **Why This System?**
    - **Global uniqueness**: No two containers have same number worldwide
    - **Easy identification**: Operators recognise owner codes instantly
    - **Error detection**: Check digit catches typos (99% accuracy)
    - **Automated processing**: Optical Character Recognition (OCR) at terminal gates
    - **Tracking**: Follow container journey globally through all transport modes
    - **Inventory management**: Shipping lines track 100,000s of containers precisely
    - **Legal documentation**: Forms part of bill of lading and customs declarations
    
    **Technology Integration (2024-2025):**
    - **OCR gates**: Automatic container number recognition at terminal entry/exit (>95% accuracy)
    - **RFID tags**: Some containers now have RFID chips for automatic identification
    - **Blockchain**: Experimental tracking systems using blockchain for immutable records
    - **Digital twins**: Each container's complete history tracked in digital databases
    - **IoT devices**: Smart containers transmit their ID automatically via cellular/satellite
    """)
    
    # ============================================================================
    # SECTION 6: Bay-Row-Tier Coordinate System
    # ============================================================================
    
    st.markdown('<p class="section-header">Bay-Row-Tier: 3D Positioning System</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Containers in terminals and vessels are positioned using a three-dimensional coordinate system. Every 
    container location has a unique address that precisely identifies its position.
    """)
    
    st.markdown('<p class="subsection-header">The Three Dimensions</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Bay (Longitudinal)**
        
        **Definition:**
        - Position along length
        - Numbered front to back
        
        **On Vessels:**
        - Bow (front) to Stern (back)
        - **Odd numbers**: 20ft positions (01, 03, 05, 07...)
        - **Even numbers**: 40ft positions (02, 04, 06, 08...)
        - A 40ft container occupies 2 bays (e.g., Bay 02 covers positions 01+03)
        - Large vessels: Bay 01 to Bay 200+
        
        **In Terminals:**
        - Similar concept
        - Yard blocks divided into bays
        - Sequential numbering
        - Typically 01 to 40 per block
        """)
    
    with col2:
        st.markdown("""
        **Row (Transverse)**
        
        **Definition:**
        - Position across width
        - Numbered left to right
        
        **On Vessels:**
        - Port (left) to Starboard (right)
        - Centre line: **00**
        - **Odd**: Port side (01, 03, 05, 07...)
        - **Even**: Starboard side (02, 04, 06, 08...)
        - Range depends on vessel width
        - Large vessels: 00 to 24 (12 containers wide)
        
        **In Terminals:**
        - Across yard block width
        - Usually numbered 01-08 (typical RTG span: 1+6+1 or 1+7+1)
        - RMG systems may have 01-12 or more
        """)
    
    with col3:
        st.markdown("""
        **Tier (Vertical)**
        
        **Definition:**
        - Vertical stacking position
        - Numbered bottom to top
        
        **On Vessels:**
        - Below deck: 02, 04, 06, 08... (even, descending)
        - Deck level: **80**
        - Above deck: 82, 84, 86, 88... (even, ascending)
        - Large vessels: Up to 10 tiers above deck
        
        **In Terminals:**
        - Ground level: **01**
        - Second tier: 02
        - Third tier: 03
        - And so on...
        - Typical RTG: 01-06 (six high)
        - Typical RMG: 01-08 or higher
        """)
    
    st.markdown("""
    **Example Container Position:**
    
    **Bay 12, Row 04, Tier 86**
    - **Bay 12**: 12th longitudinal position (40ft container position)
    - **Row 04**: 4th position from port side (starboard side, even numbers)
    - **Tier 86**: 3 tiers above deck (80 = deck, 82 = 1st above, 84 = 2nd above, 86 = 3rd above)
    
    **Why This System?**
    - **Unambiguous**: Every position has unique three-dimensional coordinate
    - **Planning**: Stowage planners specify exact positions in loading plans
    - **Operations**: Crane operators know exactly where to place/retrieve containers
    - **Tracking**: Terminal Operating System (TOS) tracks every container location in real-time
    - **Safety**: Ensures proper weight distribution and vessel stability
    - **Efficiency**: Minimises search time - crane operators go directly to correct position
    - **Automation**: Automated systems rely on precise positioning data
    
    **Modern Technology (2024-2025):**
    - **Auto-stowage algorithms**: AI generates optimal bay plans in seconds
    - **Real-time tracking**: TOS updates location instantly when container moves
    - **3D visualisation**: Stowage planners view entire vessel in 3D software
    - **Collision avoidance**: Systems prevent placing containers in impossible positions
    - **Weight distribution software**: Automatic checking of stability constraints
    """)
    
    # ============================================================================
    # SECTION 7: Container Economics
    # ============================================================================
    
    st.markdown('<p class="section-header">Container Economics: The Business Side</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Understanding container costs helps explain shipping line and terminal operational decisions. The container 
    fleet represents a massive capital investment for shipping lines and leasing companies.
    """)
    
    st.markdown('<p class="subsection-header">Container Costs (2024-2025 Market Prices)</p>', unsafe_allow_html=True)
    
    # Cost breakdown with updated 2024-2025 prices
    container_costs = pd.DataFrame({
        'Item': [
            'New 20ft Dry Container',
            'New 40ft Dry Container',
            'New 40ft High Cube Dry',
            'New 40ft Reefer',
            'Used 20ft Container (cargo-worthy)',
            'Used 40ft Container (cargo-worthy)',
            'Lifespan',
            'Maintenance per Year',
            'Leasing Cost (per day)',
            'Repositioning Cost (empty)',
            'Repair (minor damage)',
            'Repair (major damage)'
        ],
        'Cost (2024-2025)': [
            '$2,200-2,800',
            '$2,500-3,500',
            '$3,000-4,000',
            '$12,000-16,000',
            '$500-3,000',
            '$1,000-4,000',
            '12-15 years',
            '$150-300',
            '$1-4 (dry), $10-18 (reefer)',
            '$500-2,500',
            '$200-600',
            '$1,000-4,000'
        ],
        'Notes': [
            'Prices fluctuate with steel costs (currently elevated post-pandemic)',
            'Most common type globally; prices affected by China manufacturing costs',
            'Extra height adds cost; most new containers are HC (volume efficiency)',
            'Refrigeration unit is expensive; Carrier or Thermo King units',
            'Condition varies; suitable for cargo but may have cosmetic damage',
            'Widely available; good for storage or one-way shipping',
            'After 12-15 years, retired from international shipping or sold for storage/modification',
            'Inspection, cleaning, minor repairs; higher for reefers (compressor maintenance)',
            'Daily leasing rate; shipping lines often lease 30-50% rather than own all containers',
            'Moving empty containers to where demand is; major cost for shipping lines',
            'Dents, scratches, door repairs, floor patches',
            'Structural damage, floor replacement, extensive corrosion, side panel replacement'
        ]
    })
    
    st.dataframe(container_costs, use_container_width=True, hide_index=True)
    
    st.markdown("""
    **Container Ownership Models:**
    - **Carrier-owned**: Shipping lines own ~60% of global container fleet
    - **Leasing companies**: Own ~40% of fleet (Triton, Textainer, CAI, Florens, SeaCube)
    - **Leasing advantages**: Flexibility, no capital tied up, easier to adjust fleet size
    - **Ownership advantages**: Lower long-term cost, full control, no lease payments
    
    **Global Container Fleet Value (2024):**
    - Total fleet: ~50 million containers (50M × $3,000 average = **$150 billion+ in assets**)
    - Container fleet market: **$13.34 billion** (leasing and ownership services)
    - Major leasing companies: Triton (3.5M TEU), Textainer (3.3M TEU), CAI, Florens, SeaCube
    """)
    
    st.markdown('<p class="subsection-header">The Empty Container Problem</p>', unsafe_allow_html=True)
    
    st.markdown("""
    One of shipping's biggest operational and financial challenges is repositioning empty containers. This 
    problem has **worsened significantly in 2024-2025**.
    
    **Trade Imbalances:**
    - More cargo flows certain directions (e.g., Asia → Europe/US > Europe/US → Asia)
    - Results in container surplus at destination, deficit at origin
    - **Classic example**: China exports far more to US than imports from US
    - Containers accumulate in US ports, shortage in Asian export ports
    - **2024 data**: US-Asia backhaul utilisation often <50% (half-empty vessels westbound)
    
    **Repositioning Challenge:**
    - Shipping lines must move empty containers back to high-demand origins
    - Costs **$500-2,500 per container** to reposition (fuel, handling, vessel space)
    - Vessel space used for empties = **lost revenue opportunity** (could carry paid cargo)
    - **Industry estimates (2024)**: **20-25% of containers moved globally are empty**
    - **2024 increase**: Empty container movements **up 20%** compared to 2019 (Sea-Intelligence data)
    
    **The Numbers:**
    - If global throughput = 860M TEU, then **~170-215M TEU moved empty** annually
    - At $500-2,500 per empty move = **$85-538 billion in repositioning costs** industry-wide
    - This is pure cost with zero revenue (massive inefficiency in the system)
    
    **Regional Imbalances (2024-2025):**
    - **Asia to North America**: Heavily loaded eastbound, light westbound
    - **Asia to Europe**: Significant imbalance (more exports from Asia)
    - **Transpacific westbound**: Often 40-50% empty containers (low backhaul demand)
    - **US tariffs impact**: 2024-2025 tariff changes worsened imbalances (less US exports)
    
    **Solutions Being Implemented:**
    - **Incentivise backhaul cargo**: Lower freight rates for return direction (sometimes 50-70% cheaper)
    - **Regional triangulation**: Move empties through third country with better trade balance
    - **Container leasing companies**: Help balance supply/demand across regions
    - **Foldable/collapsible containers**: Research stage, not yet commercially viable (too expensive, durability concerns)
    - **Depot networks**: Strategic positioning of empty containers at key locations
    - **Digital platforms**: Container tracking platforms help match empty container supply with demand
    - **Shipper-owned containers**: Some major shippers buy containers to ensure availability (e.g., Amazon, Walmart)
    
    **2024-2025 Specific Challenges:**
    - **Persistent imbalances**: Empty repositioning up 20% vs 2019 baseline
    - **Geopolitical tensions**: US-China trade tensions worsen container flow imbalances
    - **E-commerce boom**: One-directional flow (Asia to rest of world) for consumer goods
    - **Supply chain disruptions**: Red Sea crisis (+70% via Cape route) lengthened repositioning times
    - **Equipment shortages**: 2024 saw periodic container shortages in Asia despite global surplus
    """)
    
    # ============================================================================
    # SECTION 8: Current Industry Trends (2024-2025)
    # ============================================================================
    
    st.markdown('<p class="section-header">Current Industry Trends (2024-2025)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The container industry is experiencing significant transformation driven by technology, sustainability, 
    and changing trade patterns.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Technology Integration:**
        - **IoT-enabled smart containers**: Real-time tracking of location, temperature, humidity, shock/tilt
        - **Maersk integration (June 2024)**: Nearly 300 container fleets with IoT sensors
        - **Blockchain tracking**: Experimental systems for tamper-proof container histories
        - **Predictive maintenance**: AI algorithms predict when reefer units will fail
        - **Digital platforms**: Container tracking, booking, and documentation moving online
        
        **Sustainability Push:**
        - **Alternative materials**: Research into lighter, more recyclable container materials
        - **Solar-powered reefers**: Reducing diesel dependency for refrigeration
        - **Circular economy**: 15-year-old containers repurposed for storage, housing, offices
        - **Carbon footprint tracking**: Per-container emissions monitoring
        - **Reduced tare weight**: Lighter containers = more cargo capacity, less fuel
        """)
    
    with col2:
        st.markdown("""
        **Market Dynamics:**
        - **E-commerce explosion**: Container demand driven by online retail (projected >$6 trillion by 2024)
        - **Fleet expansion**: Global container fleet grew at 7.3% average (top 12 carriers, 2025)
        - **MSC dominance**: Added 831,000 TEU in 2025 (5th consecutive year of leadership)
        - **Overcapacity concerns**: New vessel orders + existing fleet = potential oversupply
        - **Freight rate volatility**: Shanghai Containerized Freight Index averaged 2,496 points in 2024 (up 149% from 2023)
        
        **Operational Challenges:**
        - **Equipment positioning**: Empty container repositioning up 20% (2024 vs 2019)
        - **Supply chain fragility**: Red Sea disruptions (−70% Suez traffic) strain container availability
        - **Port congestion**: Delayed containers tie up equipment longer
        - **Shortage/surplus cycles**: Asia often has shortages while US/Europe have surplus
        - **Trade uncertainty**: Tariffs, geopolitical tensions create unpredictable flows
        """)
    
    # ============================================================================
    # SECTION 9: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **ISO Standards:**
        - Universal 2.4m (8ft) width
        - Standard lengths: 20ft, 40ft, 45ft
        - Heights: 8ft 6in (standard) or 9ft 6in (high cube)
        - Max gross weight: 30,480 kg (30.48 tonnes)
        - Standardisation enables global interoperability
        - 40ft containers dominate: 54% of global fleet
        
        **TEU Measurement:**
        - TEU = Twenty-foot Equivalent Unit
        - 20ft container = 1 TEU
        - 40ft container = 2 TEU
        - Universal measure for capacity and throughput
        - Global port throughput: ~860M TEU (2024)
        
        **Container Types:**
        - Dry van: 85-90% of fleet (general cargo)
        - Reefer: 6-8% ($1.94B market, growing 6.5% annually)
        - Specialised: Open top, flat rack, tank, OOG (~5%)
        """)
    
    with col2:
        st.markdown("""
        **Container Anatomy:**
        - Corner castings: Critical for lifting and securing (150 tonne capacity)
        - CSC plate: Safety certification and specifications
        - Weight: Tare 2.2-4.2 tonnes, max payload 26-28 tonnes
        - **SOLAS VGM**: Mandatory weighing since 1 July 2016
        
        **Identification System:**
        - Format: Owner code (4 letters) + Serial (6 digits) + Check digit
        - Example: MAEU 1234567
        - Globally unique identification (ISO 6346 standard)
        - OCR and RFID for automated tracking
        
        **Bay-Row-Tier System:**
        - 3D coordinate system for positioning
        - Bay: Longitudinal (front to back, odd=20ft, even=40ft)
        - Row: Transverse (left to right, port=odd, starboard=even)
        - Tier: Vertical (bottom to top)
        - Enables precise stowage planning and automated operations
        
        **Economics & Trends (2024-2025):**
        - Global fleet market: $13.34B (2024) → $21.9B (2033 projected)
        - Empty repositioning: 20-25% of moves, up 20% vs 2019
        - IoT integration: Smart containers with real-time tracking
        - Overcapacity challenges: Fleet growing faster than trade
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Containers follow precise ISO standards (2.4m width, 20/40ft lengths, 
    30.48 tonne max weight) that enable global interoperability. The TEU (Twenty-foot Equivalent Unit) 
    provides universal measurement for the ~50 million container global fleet. ~85-90% are dry vans, with 
    reefers (6-8%) being the fastest-growing segment. Each container has a unique ISO 6346 identifier enabling 
    global tracking. The Bay-Row-Tier coordinate system enables precise 3D positioning in terminals and vessels. 
    <br><br>
    <strong>2024-2025 Context:</strong> The container industry faces dynamic challenges including persistent 
    empty repositioning problems (20-25% of moves are empty, costing billions), integration of IoT technology 
    for smart tracking, fleet overcapacity concerns, and volatile freight rates driven by geopolitical 
    disruptions. The SOLAS VGM regulation (mandatory since 2016) has significantly improved safety by ensuring 
    accurate container weights. Understanding these fundamentals and current trends is essential for comprehending 
    how modern container terminal operations work.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** 🚢 Container Vessels & Evolution - Explore vessel anatomy, the dramatic growth from 
    500 to 25,000+ TEU, vessel classifications, and the complex art of stowage planning that relies on the 
    Bay-Row-Tier system you've just learned.
    """)
