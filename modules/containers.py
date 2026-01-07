import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">📦 Containers & Containerization</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand the standardized containers that revolutionized global trade, their types, specifications, 
    and the measurement systems used throughout the maritime industry.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: What is Containerization?
    # ============================================================================
    
    st.markdown('<p class="section-header">What is Containerization?</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Containerization** is a system of intermodal freight transport using standardized shipping containers 
    (also called ISO containers). These containers can be seamlessly transferred between ships, trains, and 
    trucks without unpacking the cargo inside.
    
    The key word is **standardized**. Before containers, every shipment was different—different sizes, 
    different shapes, different handling requirements. Containerization brought uniformity to chaos.
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Standard Widths", "8 ft", help="All ISO containers are 8 feet wide")
    with col2:
        st.metric("Standard Heights", "8.5 or 9.5 ft", help="Standard or High-Cube")
    with col3:
        st.metric("Common Lengths", "20 or 40 ft", help="Most common container lengths")
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 Why Standardization Matters:</strong> A crane operator in Singapore can lift a container 
    from China and load it onto a truck—without knowing what's inside, who owns it, or where it's going. 
    The standardized dimensions and corner fittings make this possible.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 2: Standard Container Types & Dimensions
    # ============================================================================
    
    st.markdown('<p class="section-header">Standard Container Types & Dimensions</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">ISO Standard Containers</p>', unsafe_allow_html=True)
    
    # Container specifications table
    container_specs = pd.DataFrame({
        'Container Type': ['20 ft Standard', '40 ft Standard', '40 ft High-Cube', '45 ft High-Cube', '48 ft', '53 ft'],
        'Length': ['19 ft 10.5 in (6.058 m)', '40 ft 0 in (12.192 m)', '40 ft 0 in (12.192 m)', 
                   '45 ft 0 in (13.716 m)', '48 ft 0 in (14.630 m)', '53 ft 0 in (16.154 m)'],
        'Width': ['8 ft 0 in (2.438 m)', '8 ft 0 in (2.438 m)', '8 ft 0 in (2.438 m)', 
                  '8 ft 0 in (2.438 m)', '8 ft 6 in (2.591 m)', '8 ft 6 in (2.591 m)'],
        'Height': ['8 ft 6 in (2.591 m)', '8 ft 6 in (2.591 m)', '9 ft 6 in (2.896 m)', 
                   '9 ft 6 in (2.896 m)', '9 ft 6 in (2.896 m)', '9 ft 6 in (2.896 m)'],
        'TEU': [1.0, 2.0, 2.0, 2.25, 2.4, 2.65],
        'Typical Use': ['General cargo, heavy goods', 'General cargo (most common)', 
                        'Light, voluminous cargo', 'North American domestic', 
                        'North American domestic', 'North American domestic']
    })
    
    st.dataframe(container_specs, use_container_width=True, hide_index=True)
    
    st.markdown("""
    **Key Points:**
    - **20 ft and 40 ft** are the international standards and dominate global shipping
    - **High-Cube (HC)** containers are 1 foot taller (9.5 ft vs 8.5 ft) for voluminous but light cargo
    - **45 ft, 48 ft, and 53 ft** are primarily used in North American domestic transport
    - **Width is standardized** at 8 ft for international (8 ft 6 in for some domestic)
    """)
    
    # Visual comparison
    st.markdown('<p class="subsection-header">Container Size Comparison</p>', unsafe_allow_html=True)
    
    fig = go.Figure()
    
    # Simplified visual representation
    containers = [
        {'name': '20 ft', 'length': 20, 'height': 8.5, 'color': '#EF4444'},
        {'name': '40 ft', 'length': 40, 'height': 8.5, 'color': '#3B82F6'},
        {'name': '40 ft HC', 'length': 40, 'height': 9.5, 'color': '#10B981'},
        {'name': '45 ft HC', 'length': 45, 'height': 9.5, 'color': '#F59E0B'}
    ]
    
    for i, cont in enumerate(containers):
        fig.add_trace(go.Bar(
            x=[cont['length']],
            y=[cont['name']],
            orientation='h',
            marker=dict(color=cont['color']),
            name=cont['name'],
            text=f"{cont['length']} ft × {cont['height']} ft",
            textposition='inside',
            textfont=dict(size=12, color='white')
        ))
    
    fig.update_layout(
        title={
            'text': 'Container Length Comparison',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        xaxis_title="Length (feet)",
        height=350,
        showlegend=False,
        plot_bgcolor='white',
        xaxis=dict(gridcolor='#E5E7EB', range=[0, 55])
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # ============================================================================
    # SECTION 3: TEU - The Universal Measurement
    # ============================================================================
    
    st.markdown('<p class="section-header">TEU: The Universal Measurement</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **TEU** stands for **Twenty-foot Equivalent Unit**. It's the standard unit of measurement for container 
    capacity throughout the maritime industry.
    
    - **1 TEU** = One 20-foot container
    - **2 TEU** = One 40-foot container (also called **FEU** - Forty-foot Equivalent Unit)
    - **2.25 TEU** = One 45-foot container
    
    TEU is used to measure:
    - **Vessel capacity**: "This ship can carry 20,000 TEU"
    - **Port throughput**: "Singapore handled 37.3 million TEU last year"
    - **Terminal capacity**: "Tuas will handle 65 million TEU annually"
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Important Distinction:**
        - **TEU** = Capacity measurement (slots)
        - **Moves** = Actual crane lifts
        - **Boxes** = Physical containers
        
        Example: One 40 ft container = 2 TEU = 1 Box = 1 Move
        """)
    
    with col2:
        # TEU calculation example
        fig = go.Figure()
        
        data = [
            {'Type': '20 ft', 'Boxes': 100, 'TEU': 100},
            {'Type': '40 ft', 'Boxes': 100, 'TEU': 200},
            {'Type': 'Mixed', 'Boxes': 200, 'TEU': 300}
        ]
        
        fig.add_trace(go.Bar(name='Physical Boxes', x=[d['Type'] for d in data], 
                             y=[d['Boxes'] for d in data], marker_color='#3B82F6'))
        fig.add_trace(go.Bar(name='TEU Count', x=[d['Type'] for d in data], 
                             y=[d['TEU'] for d in data], marker_color='#10B981'))
        
        fig.update_layout(
            title='TEU vs Physical Boxes',
            barmode='group',
            height=300,
            showlegend=True,
            plot_bgcolor='white'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📊 Real-World Example:</strong> When you hear "Singapore handled 37.3 million TEU," this means 
    the equivalent of 37.3 million 20-foot containers passed through the port. The actual number of physical 
    containers (boxes) would be lower, since many are 40-footers (2 TEU each).
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 4: Specialized Container Types
    # ============================================================================
    
    st.markdown('<p class="section-header">Specialized Container Types</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Beyond standard dry containers, specialized containers exist for specific cargo needs:
    """)
    
    # Specialized containers table
    specialized = pd.DataFrame({
        'Container Type': [
            'Dry Van (Standard)',
            'Refrigerated (Reefer)',
            'Open Top',
            'Flat Rack',
            'Tank Container',
            'Out of Gauge (OOG)',
            'Platform'
        ],
        'Description': [
            'Enclosed box for general cargo',
            'Temperature-controlled for perishables (frozen food, pharmaceuticals)',
            'Removable top for tall cargo loaded by crane',
            'Collapsible sides for machinery, vehicles, oversized cargo',
            'For liquid cargo (chemicals, food-grade liquids, fuels)',
            'Cargo exceeds standard dimensions (width, height, or length)',
            'Flat base with no sides for very heavy or odd-shaped cargo'
        ],
        'Special Requirements': [
            'None',
            'Power supply for refrigeration unit',
            'Weather protection during transit',
            'Securing and lashing expertise',
            'Hazmat handling certification',
            'Special stowage planning',
            'Heavy-duty securing equipment'
        ],
        'Typical Cargo': [
            'Electronics, clothing, furniture',
            'Meat, fish, fruit, vegetables, medicine',
            'Glass, timber, machinery',
            'Construction equipment, yachts',
            'Wine, chemicals, vegetable oils',
            'Industrial equipment, wind turbine blades',
            'Marble slabs, steel coils, generators'
        ]
    })
    
    st.dataframe(specialized, use_container_width=True, hide_index=True)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ Operational Impact:</strong> Specialized containers require extra planning and handling:
    - **Reefers** need power hookups on the vessel and in the yard
    - **OOG cargo** affects vessel stowage plans (can't stack containers on top)
    - **Tank containers** may be classified as dangerous goods (DG) requiring special permits
    - **Flat racks** need experienced lashing crews to secure cargo properly
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 5: Container Anatomy & Specifications
    # ============================================================================
    
    st.markdown('<p class="section-header">Container Anatomy & Specifications</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">Key Components of a Container</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Structural Elements:**
        - **Corner Castings**: Standardized fittings at all 8 corners for lifting and securing
        - **Corrugated Walls**: Provide strength while minimizing weight
        - **Wooden Floor**: Typically marine plywood or bamboo
        - **Doors**: Double doors at one end (typically reinforced and lockable)
        - **Roof**: Steel sheet, often with slight curve for rain drainage
        
        **Corner castings are critical** - they're the same on every container worldwide, allowing any 
        crane spreader to lift any container.
        """)
    
    with col2:
        st.markdown("""
        **Container Markings & Plates:**
        - **Container Number**: Unique identifier (4 letters + 7 digits)
        - **Check Digit**: Verification number
        - **ISO Code**: Size and type code
        - **CSC Plate** (Convention for Safe Containers):
            - Maximum gross weight
            - Tare weight (empty container weight)
            - Maximum payload
            - Manufacturing date
            - Classification society approval
        """)
    
    st.markdown('<p class="subsection-header">CSC Safety Approval Plate</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The **CSC Plate** is mandatory on all containers used in international trade. It certifies that the 
    container meets safety standards set by the International Convention for Safe Containers.
    
    **Key information on CSC Plate:**
    - **Max Gross Weight**: Total weight including container + cargo (typically 30,480 kg for 20ft)
    - **Tare Weight**: Weight of empty container (typically 2,300 kg for 20ft)
    - **Max Payload**: Maximum cargo weight = Gross Weight - Tare Weight (typically 28,180 kg)
    - **Stacking Weight**: How much weight can be stacked on top
    - **Racking Test**: Transverse and longitudinal strength tests passed
    - **Next Inspection Due**: Containers must be inspected periodically
    """)
    
    # Weight comparison
    weight_data = pd.DataFrame({
        'Container Size': ['20 ft Standard', '40 ft Standard', '40 ft High-Cube'],
        'Tare Weight (kg)': [2300, 3800, 3900],
        'Max Gross (kg)': [30480, 30480, 30480],
        'Max Payload (kg)': [28180, 26680, 26580]
    })
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Tare Weight (Empty)',
        x=weight_data['Container Size'],
        y=weight_data['Tare Weight (kg)'],
        marker_color='#94A3B8'
    ))
    
    fig.add_trace(go.Bar(
        name='Max Payload',
        x=weight_data['Container Size'],
        y=weight_data['Max Payload (kg)'],
        marker_color='#3B82F6'
    ))
    
    fig.update_layout(
        title='Container Weight Specifications',
        yaxis_title='Weight (kg)',
        barmode='stack',
        height=400,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='#E5E7EB')
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📏 Why Weight Matters:</strong> Containers have strict weight limits for safety reasons. 
    Overweight containers can:
    - Damage vessels (exceed deck or hatch cover load limits)
    - Cause crane failures
    - Violate road weight limits for trucking
    - Create stability issues during vessel stowage
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 6: Container Numbering System
    # ============================================================================
    
    st.markdown('<p class="section-header">Container Numbering & ISO Codes</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="subsection-header">Container Number Format</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Every container has a unique identification number following ISO 6346 standard:
    
    **Format: ABCU 123456 7**
    
    - **First 3 letters (ABC)**: Owner code (registered with Bureau International des Containers)
    - **4th letter (U)**: Equipment category
        - **U** = Freight container
        - **J** = Detachable freight container equipment
        - **Z** = Trailer and chassis
    - **6 digits (123456)**: Serial number
    - **Last digit (7)**: Check digit (calculated from previous characters to verify accuracy)
    
    **Example: MSCU 1234567**
    - **MSC** = Mediterranean Shipping Company
    - **U** = Freight container
    - **123456** = Serial number
    - **7** = Check digit
    """)
    
    st.markdown('<p class="subsection-header">ISO Size and Type Codes</p>', unsafe_allow_html=True)
    
    iso_codes = pd.DataFrame({
        'ISO Code': ['22G1', '42G1', '45G1', '22R1', '42R1', '22U1', '42U1'],
        'Length': ['20 ft', '40 ft', '40 ft HC', '20 ft', '40 ft', '20 ft', '40 ft'],
        'Type': ['General (Dry Van)', 'General (Dry Van)', 'General High-Cube', 
                 'Reefer', 'Reefer', 'Open Top', 'Open Top'],
        'Description': [
            'Standard 20ft dry container',
            'Standard 40ft dry container',
            'High-cube 40ft dry container',
            'Refrigerated 20ft container',
            'Refrigerated 40ft container',
            'Open top 20ft container',
            'Open top 40ft container'
        ]
    })
    
    st.dataframe(iso_codes, use_container_width=True, hide_index=True)
    
    # ============================================================================
    # SECTION 7: Bay-Row-Tier Coordinate System
    # ============================================================================
    
    st.markdown('<p class="section-header">Bay-Row-Tier Coordinate System</p>', unsafe_allow_html=True)
    
    st.markdown("""
    To precisely locate containers on a vessel or in a yard, the maritime industry uses a three-dimensional 
    coordinate system: **Bay-Row-Tier**.
    
    **Bay (Longitudinal - Front to Back):**
    - Numbered from bow (front) to stern (rear) of the vessel
    - Odd numbers (01, 03, 05...) for 20 ft positions
    - Even numbers (02, 04, 06...) for 40 ft positions
    - Bay 01 is at the bow, highest bay number at the stern
    
    **Row (Transverse - Left to Right):**
    - Numbered from port (left) side to starboard (right) side
    - 00 or 01 at the centerline
    - Odd numbers on port side, even numbers on starboard side
    - Example: 01, 03, 05 on port; 02, 04, 06 on starboard
    
    **Tier (Vertical - Bottom to Top):**
    - Numbered from the bottom of the ship upward
    - Below deck: 02, 04, 06, 08... (even numbers)
    - On deck: 82, 84, 86, 88... (80+ indicates on deck)
    - Higher numbers = higher up
    
    **Example Position: 010482**
    - **Bay 01**: Very front of ship (bow)
    - **Row 04**: 4th position from center (starboard side, even number)
    - **Tier 82**: First tier on deck (82 means on deck)
    """)
    
    st.markdown("""
    <div class="success-box">
    <strong>💡 Why This Matters:</strong> This coordinate system allows precise communication between 
    ship planners, crane operators, and terminal systems. When a crane operator receives instruction 
    "Pick up container from 120684," they know exactly where to find it—no ambiguity.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 8: Economic Impact
    # ============================================================================
    
    st.markdown('<p class="section-header">Economic Impact of Containerization</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Containerization didn't just make shipping cheaper—it transformed the global economy:
    
    **Cost Revolution:**
    - 94% cost reduction compared to break-bulk shipping
    - Reduced ship port time from weeks to hours
    - Eliminated need for large stevedore gangs
    - Dramatically reduced cargo theft and damage
    
    **Speed Revolution:**
    - **Pre-container era**: 5-7 days to load/unload a ship
    - **Container era**: 8-24 hours to load/unload even mega vessels
    - Ships spend more time at sea (earning money) vs. in port (costing money)
    
    **Globalization Enabler:**
    - Made it economically viable to manufacture in one country and sell in another
    - Enabled just-in-time manufacturing
    - Created global supply chains
    - Allowed specialization by region
    
    **Job Transformation:**
    - Eliminated traditional longshoreman jobs (heavy manual labor)
    - Created new skilled jobs (crane operators, terminal planners, logistics coordinators)
    - Shifted from brawn to brain
    """)
    
    # Before/After comparison
    comparison_data = pd.DataFrame({
        'Metric': ['Loading Time', 'Labor Required', 'Cargo Damage Rate', 'Cost per Ton', 'Theft Rate'],
        'Before Containers': [7, 100, 15, 100, 25],
        'After Containers': [1, 5, 1, 6, 2]
    })
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Before Containers (Indexed to 100)',
        x=comparison_data['Metric'],
        y=comparison_data['Before Containers'],
        marker_color='#EF4444',
        text=comparison_data['Before Containers'],
        textposition='outside'
    ))
    
    fig.add_trace(go.Bar(
        name='After Containers',
        x=comparison_data['Metric'],
        y=comparison_data['After Containers'],
        marker_color='#10B981',
        text=comparison_data['After Containers'],
        textposition='outside'
    ))
    
    fig.update_layout(
        title='Containerization Impact: Before vs After',
        yaxis_title='Relative Value (Indexed)',
        barmode='group',
        height=450,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='#E5E7EB', range=[0, 120])
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # ============================================================================
    # SECTION 9: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Standardization is Everything:**
        - ISO standard dimensions enable global intermodal transport
        - 20 ft and 40 ft containers dominate international shipping
        - TEU (Twenty-foot Equivalent Unit) is universal measurement
        
        **Container Specifications:**
        - Standard: 8 ft wide, 8.5 ft or 9.5 ft tall
        - High-Cube: Extra 1 foot height for voluminous cargo
        - Max weight typically 30,480 kg gross
        
        **Specialized Types:**
        - Dry van (standard), Reefer (refrigerated), Open top
        - Flat rack, Tank, OOG (out of gauge), Platform
        - Each type has specific handling requirements
        """)
    
    with col2:
        st.markdown("""
        **Critical Components:**
        - Corner castings: Universal lifting/securing points
        - CSC Plate: Safety certification and specifications
        - Container number: Unique ISO 6346 identifier
        - ISO codes: Specify size and type
        
        **Location System:**
        - Bay-Row-Tier coordinates pinpoint exact position
        - Allows precise communication across entire supply chain
        
        **Economic Impact:**
        - 94% cost reduction vs break-bulk
        - Enabled modern globalization
        - Transformed shipping from labor-intensive to technology-driven
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> The humble shipping container—a simple standardized steel box—is 
    arguably one of the most important inventions of the 20th century. By creating a universal standard 
    for cargo transport, containerization made global trade cheap, fast, and reliable enough to enable 
    the interconnected world economy we have today.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** 🚢 Container Vessels & Evolution - Learn about the ships that carry these containers 
    and how they've grown from 500 TEU to 25,000 TEU mega vessels.
    """)
