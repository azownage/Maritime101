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
    Standardization) containers have precise specifications that enable seamless global operations.
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
    
    st.dataframe(container_specs, width='stretch', hide_index=True)
    
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
    - Most new containers are High Cube (more versatile)
    
    **Weight Limits:**
    - **Max gross weight**: 30,480 kg (30.48 tonnes) - International standard
    - **Tare weight**: Empty container weight (2.3-4.8 tonnes depending on type)
    - **Max payload**: Gross minus tare (26-28 tonnes typically)
    - Road transport may have lower limits (varies by country)
    
    **Why These Specific Dimensions?**
    - 8ft width: Matches US truck width regulations (1950s standard)
    - 20ft/40ft length: Multiples for efficient stacking and transport
    - Heights: Balance between volume and clearance limits (bridges, tunnels)
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
    Without standardisation, global containerised shipping would be impossible.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 2: TEU Measurement System
    # ============================================================================
    
    st.markdown('<p class="section-header">The TEU: Universal Container Measurement</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **TEU = Twenty-foot Equivalent Unit**
    
    The TEU is the standard unit for measuring container capacity, throughput, and vessel sizes.
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
        - Singapore handles ~37 million TEU annually
        - This could be any mix of 20ft and 40ft containers
        - TEU provides standard measurement regardless of container size mix
        """)
    
    with col2:
        st.markdown("""
        **Why TEU and Not Just "Container Count"?**
        
        **Problem:**
        - A 20ft and 40ft container are very different
        - 40ft has 2x length, ~2x volume, ~2x weight
        - Saying "1,000 containers" doesn't tell you much
        
        **Solution:**
        - TEU normalises to 20ft equivalent
        - "10,000 TEU" gives clear sense of capacity/volume
        - Easy to compare vessels, ports, and throughput
        
        **Industry Standard:**
        - Vessel capacity: "A 20,000 TEU vessel"
        - Port throughput: "37M TEU per year"
        - Crane productivity: "30 moves per hour = 45 TEU/hour (if all 40ft)"
        """)
    
    # TEU comparison visualization
    teu_examples = pd.DataFrame({
        'Container Mix': ['All 20ft', 'All 40ft', 'Mixed (50/50)', 'Typical Mix (20% 20ft, 80% 40ft)'],
        'Number of Containers': [10000, 5000, 6667, 5625],
        'Total TEU': [10000, 10000, 10000, 10000],
        'Average TEU per Container': [1.0, 2.0, 1.5, 1.78]
    })
    
    st.dataframe(teu_examples, width='stretch', hide_index=True)
    
    # ============================================================================
    # SECTION 3: Container Types
    # ============================================================================
    
    st.markdown('<p class="section-header">Container Types: Specialised for Different Cargo</p>', unsafe_allow_html=True)
    
    st.markdown("""
    While standard dry containers are most common, specialised containers exist for specific cargo types.
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
        'Percentage of Fleet': ['~90%', '~6%', '~1%', '~1%', '~1%', '<1%', '<1%'],
        'Primary Use': [
            'General cargo, boxes, pallets, bags',
            'Perishables, pharmaceuticals, chemicals requiring temperature control',
            'Oversized cargo that exceeds height, loaded from top',
            'Heavy machinery, construction equipment, oversized items',
            'Liquids: chemicals, food-grade liquids, wine, oils',
            'Cargo exceeding container dimensions (very large equipment)',
            'Heavy cargo like steel coils, timber, vehicles'
        ],
        'Key Features': [
            'Fully enclosed, weatherproof, lockable',
            'Built-in refrigeration unit, temperature range -35°C to +30°C, requires power',
            'Removable roof/tarpaulin, same footprint as standard',
            'Collapsible sides, can stack flat when empty, lashing points',
            'Cylindrical tank in standard ISO frame, various sizes (14-26k litres)',
            'Oversized length/width/height, cannot stack containers on top',
            'Flat base with corner posts, no walls or roof, secure heavy loads'
        ],
        'Special Handling': [
            'Standard',
            'Must connect to power (vessel/terminal/truck), monitor temperature continuously',
            'Crane access required for loading/unloading from top',
            'Special securing, cannot stack other containers on top',
            'Requires certified cleaning between loads, hazmat regulations',
            'Special stowage positions, certified lifting equipment',
            'Heavy-duty securing, special stowage considerations'
        ]
    })
    
    st.dataframe(container_types, width='stretch', hide_index=True)
    
    st.markdown('<p class="subsection-header">Reefer Containers: Special Attention Required</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Refrigerated containers (reefers) require special infrastructure and monitoring:
    
    **Power Requirements:**
    - Reefers need continuous electrical power
    - Vessels: Reefer plugs in specific positions (limited number per bay)
    - Terminals: Power outlets in yard (reefer zones)
    - Trucks: Diesel-powered generators (clip-on units)
    
    **Temperature Monitoring:**
    - Continuous monitoring of temperature
    - Alarms if temperature deviates from setpoint
    - Remote monitoring systems
    - Temperature logs for customs/quality assurance
    
    **Operational Challenges:**
    - Limited reefer plug positions on vessels (stowage constraint)
    - Power consumption at terminals (cost consideration)
    - Breakdowns require immediate attention (cargo spoilage risk)
    - Priority handling (time-sensitive perishables)
    
    **Common Reefer Cargo:**
    - Frozen meat, fish, poultry
    - Fresh fruits and vegetables
    - Dairy products
    - Pharmaceuticals (vaccines, medicines)
    - Chemicals requiring temperature control
    - Wine and beverages
    - Flowers and plants
    """)
    
    # ============================================================================
    # SECTION 4: Container Anatomy and Specifications
    # ============================================================================
    
    st.markdown('<p class="section-header">Container Anatomy: Key Components</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Understanding container structure helps explain handling procedures and stowage planning.
    """)
    
    st.markdown('<p class="subsection-header">Critical Container Components</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Corner Castings:**
        - **Most critical component** of container
        - Steel fittings at all 8 corners
        - Standard dimensions: 178mm × 162mm × 119mm
        - Oval holes (not circular) for twist-locks
        - Bear all lifting forces and securing loads
        - Connect container to:
          - Crane spreaders (lifting)
          - Vessel cell guides (securing on ship)
          - Chassis (road transport)
          - Rail wagons (rail transport)
        
        **Floor:**
        - Hardwood or steel floor
        - Must support distributed load
        - Forklift access for loading/unloading
        - Drainage channels (if liquid spills)
        """)
    
    with col2:
        st.markdown("""
        **Walls and Roof:**
        - Corrugated steel (strength + weight optimisation)
        - Weatherproof seals
        - Structural rigidity
        - Doors: Double doors at one end, rubber seals, locking bars
        
        **CSC Plate (Container Safety Convention):**
        - Metal plate affixed to container
        - Contains critical information:
          - Container owner/operator
          - Container number
          - Maximum gross weight
          - Tare weight
          - Manufacturing date
          - CSC approval and inspection dates
        - Required by international law
        - Must be clearly visible
        """)
    
    st.markdown('<p class="subsection-header">Weight Specifications</p>', unsafe_allow_html=True)
    
    # Weight table
    weight_specs = pd.DataFrame({
        'Specification': [
            'Max Gross Weight',
            'Tare Weight (20ft)',
            'Tare Weight (40ft)',
            'Max Payload (20ft)',
            'Max Payload (40ft)',
            'Typical Cargo (20ft)',
            'Typical Cargo (40ft)'
        ],
        'Value': [
            '30,480 kg (30.48 tonnes)',
            '2,200-2,400 kg',
            '3,600-3,900 kg',
            '28,080-28,280 kg',
            '26,580-26,880 kg',
            '20,000-25,000 kg',
            '22,000-26,000 kg'
        ],
        'Notes': [
            'International ISO standard, some countries allow higher',
            'Depends on container type (dry van vs reefer vs tank)',
            'High cube slightly heavier than standard',
            'Max gross minus tare weight',
            'Max gross minus tare weight',
            'Most containers not loaded to maximum (volume limit reached first)',
            'Most 40ft containers hit volume limit before weight limit'
        ]
    })
    
    st.dataframe(weight_specs, width='stretch', hide_index=True)
    
    st.markdown("""
    **Important Weight Considerations:**
    
    **Volume vs Weight Limits:**
    - Most cargo is **volume-limited** (fills container before reaching weight limit)
    - Example: Furniture, clothing, electronics (low density)
    - **Weight-limited** cargo is less common
    - Example: Metals, minerals, machinery (high density)
    
    **Road Transport Limits:**
    - Many countries have lower weight limits for trucks
    - Example: EU allows 44 tonnes total (truck + trailer + container + cargo)
    - May restrict payload to 24-26 tonnes even though container can legally hold 28 tonnes
    
    **Weighing Requirements:**
    - **SOLAS VGM (Verified Gross Mass)**: Mandatory since 2016
    - All containers must be weighed before loading on vessel
    - Prevents overweight containers (safety risk for vessel stability)
    - Shipper responsible for providing accurate weight
    """)
    
    # ============================================================================
    # SECTION 5: Container Identification System
    # ============================================================================
    
    st.markdown('<p class="section-header">Container Identification: The ISO 6346 System</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Every container has a unique identification number following the ISO 6346 standard.
    """)
    
    st.markdown('<p class="subsection-header">Container Number Format</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Format:** `ABCD 123456-7`
    
    **Example:** `MAEU 1234567`
    
    **Components:**
    
    **1. Owner Code (4 letters):**
    - First 3 letters: Identify container owner/operator
    - Examples:
      - MAEU = Maersk Line
      - MSCU = Mediterranean Shipping Company (MSC)
      - CMAU = CMA CGM
      - CSQU = COSCO
      - TEMU = ONE (Ocean Network Express)
    - 4th letter: Always "U" (indicates Unit, i.e., container)
    
    **2. Serial Number (6 digits):**
    - Unique number assigned by owner
    - Range: 000000 to 999999
    - Sequential allocation (usually)
    
    **3. Check Digit (1 digit):**
    - Mathematical validation digit
    - Calculated from owner code + serial number
    - Prevents data entry errors
    - Algorithm: Weighted sum modulo 11
    
    **Size and Type Code (separate):**
    - 4-character code indicating:
      - Length (2 = 20ft, 4 = 40ft, L = 45ft)
      - Height (0 = 8'6", 5 = 9'6")
      - Type (G = general, R = reefer, T = tank, etc.)
    - Example: 42G1 = 40ft, High Cube, General Purpose
    """)
    
    # Example container numbers
    example_numbers = pd.DataFrame({
        'Container Number': ['MAEU 1234567', 'MSCU 9876543', 'CMAU 5555555', 'TEMU 1111118'],
        'Owner Code': ['MAEU', 'MSCU', 'CMAU', 'TEMU'],
        'Owner': ['Maersk Line', 'MSC', 'CMA CGM', 'ONE'],
        'Serial': ['123456', '987654', '555555', '111111'],
        'Check Digit': ['7', '3', '5', '8'],
        'Size/Type (example)': ['42G1', '22G1', '45R1', '42G1'],
        'Meaning': ['40ft HC dry', '20ft std dry', '40ft HC reefer', '40ft HC dry']
    })
    
    st.dataframe(example_numbers, width='stretch', hide_index=True)
    
    st.markdown("""
    **Why This System?**
    - **Global uniqueness**: No two containers have same number
    - **Easy identification**: Operators recognize owner codes instantly
    - **Error detection**: Check digit catches typos (important for thousands of containers)
    - **Automated processing**: Optical Character Recognition (OCR) at gates
    - **Tracking**: Follow container journey globally
    """)
    
    # ============================================================================
    # SECTION 6: Bay-Row-Tier Coordinate System
    # ============================================================================
    
    st.markdown('<p class="section-header">Bay-Row-Tier: 3D Positioning System</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Containers in terminals and vessels are positioned using a three-dimensional coordinate system.
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
        - Odd numbers: 20ft positions
        - Even numbers: 40ft positions
        - Example: Bay 01, 02, 03, 04...
        - A 40ft container occupies 2 bays (e.g., Bay 02 covers bays 01+03)
        
        **In Terminals:**
        - Similar concept
        - Yard blocks divided into bays
        - Sequential numbering
        """)
    
    with col2:
        st.markdown("""
        **Row (Transverse)**
        
        **Definition:**
        - Position across width
        - Numbered left to right
        
        **On Vessels:**
        - Port (left) to Starboard (right)
        - Centre line: 00
        - Odd: Port side (01, 03, 05...)
        - Even: Starboard side (02, 04, 06...)
        - Example: Row 00-24 (depends on vessel width)
        
        **In Terminals:**
        - Across yard block width
        - Usually numbered 01-08 (typical RTG span)
        """)
    
    with col3:
        st.markdown("""
        **Tier (Vertical)**
        
        **Definition:**
        - Vertical stacking position
        - Numbered bottom to top
        
        **On Vessels:**
        - Below deck: 02, 04, 06... (even, descending)
        - Deck level: 80
        - Above deck: 82, 84, 86, 88... (even, ascending)
        
        **In Terminals:**
        - Ground level: 01
        - Second tier: 02
        - And so on...
        - Typical: 01-06 (six high)
        """)
    
    st.markdown("""
    **Example Container Position:**
    
    **Bay 12, Row 04, Tier 86**
    - **Bay 12**: 12th longitudinal position (40ft container position)
    - **Row 04**: 4th position from port side (starboard side)
    - **Tier 86**: 3 tiers above deck (80 = deck, 82 = 1st above, 84 = 2nd above, 86 = 3rd above)
    
    **Why This System?**
    - **Unambiguous**: Every position has unique coordinate
    - **Planning**: Stowage planners specify exact positions
    - **Operations**: Crane operators know exactly where to go
    - **Tracking**: Terminal Operating System tracks every container location
    - **Safety**: Ensures proper weight distribution and stability
    """)
    
    # ============================================================================
    # SECTION 7: Container Economics
    # ============================================================================
    
    st.markdown('<p class="section-header">Container Economics: The Business Side</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Understanding container costs helps explain shipping line and terminal operational decisions.
    """)
    
    st.markdown('<p class="subsection-header">Container Costs</p>', unsafe_allow_html=True)
    
    # Cost breakdown
    container_costs = pd.DataFrame({
        'Item': [
            'New 20ft Dry Container',
            'New 40ft Dry Container',
            'New 40ft High Cube Dry',
            'New 40ft Reefer',
            'Lifespan',
            'Maintenance per Year',
            'Leasing Cost (per day)',
            'Repositioning Cost (empty)',
            'Repair (minor damage)',
            'Repair (major damage)'
        ],
        'Cost': [
            '$2,000-2,500',
            '$2,500-3,000',
            '$3,000-3,500',
            '$12,000-15,000',
            '12-15 years',
            '$100-200',
            '$1-3 (dry), $8-15 (reefer)',
            '$500-2,000 depending on distance',
            '$200-500',
            '$1,000-3,000'
        ],
        'Notes': [
            'Basic dry container, prices fluctuate with steel costs',
            'Most common type globally',
            'Extra height adds cost but provides flexibility',
            'Refrigeration unit is expensive component',
            'After 12-15 years, retired or sold for storage/modification',
            'Inspection, cleaning, minor repairs',
            'Daily leasing rate, shipping lines often lease rather than own',
            'Moving empty containers to where demand is (imbalance problem)',
            'Dents, scratches, door repairs',
            'Structural damage, floor replacement, extensive corrosion'
        ]
    })
    
    st.dataframe(container_costs, width='stretch', hide_index=True)
    
    st.markdown("""
    **The Empty Container Problem:**
    
    **Trade Imbalances:**
    - More cargo flows certain directions (e.g., Asia → Europe/US > Europe/US → Asia)
    - Results in container surplus at destination, deficit at origin
    - **Example**: China exports far more to US than imports from US
    - Containers accumulate in US, shortage in China
    
    **Repositioning:**
    - Shipping lines must move empty containers back to high-demand origins
    - Costs $500-2,000 per container to reposition
    - Vessel space used for empties = lost revenue opportunity
    - Industry estimates 20-25% of containers moved globally are empty
    
    **Solutions:**
    - Incentivise backhaul cargo (lower rates for return direction)
    - Regional triangulation (move empties through third country)
    - Container leasing companies help balance supply/demand
    - Collapsible containers (research stage, not yet viable commercially)
    """)
    
    # ============================================================================
    # SECTION 8: Key Takeaways
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
        
        **TEU Measurement:**
        - TEU = Twenty-foot Equivalent Unit
        - 20ft container = 1 TEU
        - 40ft container = 2 TEU
        - Universal measure for capacity and throughput
        
        **Container Types:**
        - Dry van: ~90% of fleet (general cargo)
        - Reefer: ~6% (temperature-controlled)
        - Specialised: Open top, flat rack, tank, OOG (<4%)
        """)
    
    with col2:
        st.markdown("""
        **Container Anatomy:**
        - Corner castings: Critical for lifting and securing
        - CSC plate: Safety certification and specifications
        - Weight: Tare 2.3-3.9 tonnes, max payload 26-28 tonnes
        - SOLAS VGM: Mandatory weighing before vessel loading
        
        **Identification System:**
        - Format: Owner code (4 letters) + Serial (6 digits) + Check digit
        - Example: MAEU 1234567
        - Globally unique identification
        - ISO 6346 standard
        
        **Bay-Row-Tier System:**
        - 3D coordinate system for positioning
        - Bay: Longitudinal (front to back)
        - Row: Transverse (left to right)
        - Tier: Vertical (bottom to top)
        - Enables precise stowage planning
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Containers follow precise ISO standards (2.4m width, 20/40ft lengths, 
    30.48 tonne max weight) that enable global interoperability. The TEU (Twenty-foot Equivalent Unit) 
    provides universal measurement. ~90% are dry vans, with specialised types (reefer, tank, OOG) for specific 
    cargo. Each container has a unique ISO 6346 identifier (owner code + serial + check digit). The 
    Bay-Row-Tier coordinate system enables precise 3D positioning in terminals and vessels. Understanding 
    these fundamentals is essential for understanding how container terminal operations work.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** 🚢 Container Vessels & Evolution - Explore vessel anatomy, the dramatic growth from 
    500 to 24,000 TEU, vessel classifications, and the complex art of stowage planning.
    """)
