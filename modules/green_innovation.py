import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">🌱 Green Maritime & Future Trends</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand the maritime industry's decarbonisation journey, alternative fuel technologies, green port 
    initiatives, digital transformation, and future trends shaping sustainable maritime operations.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: The Decarbonization Imperative
    # ============================================================================
    
    st.markdown('<p class="section-header">The Decarbonisation Imperative</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The maritime industry faces mounting pressure to reduce its carbon footprint and achieve net-zero 
    emissions by 2050. This represents one of the most significant transformations in maritime history.
    """)
    
    st.markdown('<p class="subsection-header">Current State and Targets</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Global Shipping Emissions", "~3% of CO2", help="Maritime transport accounts for ~3% of global CO2 emissions")
    with col2:
        st.metric("IMO 2030 Target", "-40% intensity", help="40% reduction in carbon intensity by 2030 vs 2008")
    with col3:
        st.metric("IMO 2050 Target", "Net Zero", help="Net-zero greenhouse gas emissions by 2050")
    
    st.markdown("""
    **International Maritime Organisation (IMO) Targets:**
    
    **Short-term (2030):**
    - **40% reduction** in carbon intensity (CO2 per tonne-mile) compared to 2008 baseline
    - Applicable to all international shipping
    - Phased implementation through Energy Efficiency Design Index (EEDI) and Carbon Intensity Indicator (CII)
    
    **Mid-term (2040):**
    - Additional measures and technologies deployed
    - Alternative fuel infrastructure scaling up
    - Fleet transition accelerating
    
    **Long-term (2050):**
    - **Net-zero greenhouse gas emissions** from international shipping
    - Complete transformation of maritime fuel mix
    - Industry-wide adoption of zero-carbon technologies
    
    **Regulatory Framework:**
    - **EEDI (Energy Efficiency Design Index)**: Mandatory for new ships since 2013
    - **SEEMP (Ship Energy Efficiency Management Plan)**: Required for all ships
    - **CII (Carbon Intensity Indicator)**: Annual rating from 2023 (A-E grades)
    - **EU ETS (Emissions Trading System)**: Maritime included from 2024
    - **FuelEU Maritime**: EU regulation on fuel carbon intensity
    """)
    
    # Emissions reduction pathway
    reduction_pathway = pd.DataFrame({
        'Year': [2008, 2015, 2020, 2025, 2030, 2035, 2040, 2045, 2050],
        'Carbon Intensity (Index)': [100, 95, 90, 75, 60, 45, 30, 15, 0],
        'Technology Phase': [
            'Baseline',
            'Efficiency improvements',
            'Early alternative fuels',
            'Alternative fuels scaling',
            '40% reduction target',
            'Majority alternative fuels',
            'Zero-carbon majority',
            'Near-complete transition',
            'Net-zero achieved'
        ]
    })
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=reduction_pathway['Year'],
        y=reduction_pathway['Carbon Intensity (Index)'],
        mode='lines+markers',
        line=dict(color='#10B981', width=4),
        marker=dict(size=12, color='#059669', line=dict(color='white', width=2)),
        fill='tozeroy',
        fillcolor='rgba(16, 185, 129, 0.2)',
        name='Carbon Intensity',
        hovertemplate='%{x}<br>Carbon Intensity: %{y}<br>%{text}<extra></extra>',
        text=reduction_pathway['Technology Phase']
    ))
    
    # Add target markers
    fig.add_hline(y=60, line_dash="dash", line_color="#F59E0B", 
                  annotation_text="2030 Target: -40%", annotation_position="right")
    fig.add_hline(y=0, line_dash="dash", line_color="#EF4444", 
                  annotation_text="2050 Target: Net Zero", annotation_position="right")
    
    fig.update_layout(
        title={
            'text': 'IMO Decarbonisation Pathway: 2008 → 2050',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#1F2937'}
        },
        xaxis_title="Year",
        yaxis_title="Carbon Intensity (Indexed to 2008 = 100)",
        height=500,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='#E5E7EB', range=[0, 110]),
        xaxis=dict(gridcolor='#E5E7EB')
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ The Challenge:</strong> Achieving net-zero by 2050 requires:<br>
    - <strong>Complete fuel transition</strong>: From fossil fuels to zero-carbon alternatives<br>
    - <strong>New ship designs</strong>: Vessels optimised for alternative fuels<br>
    - <strong>Infrastructure transformation</strong>: Bunkering facilities for new fuels at ports worldwide<br>
    - <strong>Economic viability</strong>: Alternative fuels currently 2-4x more expensive than conventional fuel<br>
    - <strong>Technology maturity</strong>: Some solutions still in development or early deployment<br>
    - <strong>Fleet replacement</strong>: 25-30 year ship lifespan means ships ordered today will still operate in 2050<br><br>
    This is not just an engineering challenge—it's an economic, political, and social transformation.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 2: Alternative Fuels for Shipping
    # ============================================================================
    
    st.markdown('<p class="section-header">Alternative Fuels: The Transition Pathway</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Multiple alternative fuel options are being developed and deployed, each with different characteristics, 
    benefits, and challenges.
    """)
    
    st.markdown('<p class="subsection-header">1. Liquefied Natural Gas (LNG)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Current Status:** Most mature alternative fuel, widely available today
    
    **Characteristics:**
    - **Carbon reduction**: 20-25% less CO2 than conventional marine fuel oil
    - **Emissions**: Near-zero SOx and particulate matter, 90% less NOx
    - **Technology maturity**: Proven, commercial, many LNG-powered vessels operating
    - **Infrastructure**: 185+ ports worldwide offer LNG bunkering
    
    **Advantages:**
    - Available now (proven technology)
    - Significant emissions reduction vs conventional fuel
    - Abundant supply globally
    - Meets current IMO 2030 targets
    - Price competitive with low-sulphur fuel oil
    
    **Disadvantages:**
    - Still a fossil fuel (not zero-carbon)
    - Methane slip (unburned methane emissions) is potent greenhouse gas
    - Cannot achieve IMO 2050 net-zero target alone
    - Stranded asset risk (vessels may become obsolete before end of life)
    
    **Strategic Role:**
    - **Transition fuel**: Bridge from conventional oil to zero-carbon fuels
    - **Near-term solution**: Helps meet 2030 targets
    - **Infrastructure building**: LNG bunkering infrastructure can be adapted for bio-LNG or synthetic methane
    
    **Current Adoption:**
    - 300+ LNG-powered vessels in operation or on order
    - Primarily cruise ships, ferries, short-sea shipping
    - Some container ships and tankers
    - Growing but still <5% of global fleet
    """)
    
    st.markdown('<p class="subsection-header">2. Methanol</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Current Status:** Emerging as leading alternative fuel candidate
    
    **Characteristics:**
    - **Carbon potential**: Conventional methanol (grey): 10-15% reduction; Bio-methanol: 65-95% reduction; 
      E-methanol (green): 100% carbon-neutral
    - **Form**: Liquid at ambient temperature and pressure (easy handling)
    - **Energy density**: 50% of conventional fuel (requires ~2x tank volume)
    - **Technology**: Dual-fuel engines available, retrofitting possible
    
    **Advantages:**
    - **Liquid form**: Easy to handle, store, and bunker (like conventional fuel)
    - **Pathway to zero-carbon**: Can be produced from renewable sources (bio or e-methanol)
    - **Retrofitting**: Existing vessels can be converted to methanol
    - **Infrastructure**: Can use modified existing bunkering infrastructure
    - **Safety**: Lower fire risk than LNG (no cryogenic temperatures)
    - **Growing availability**: 122 ports globally offer methanol bunkering
    
    **Disadvantages:**
    - **Energy density**: Requires approximately double the fuel tank space
    - **Cost**: 2-3x more expensive than conventional fuel (especially green methanol)
    - **Production scale**: Bio and e-methanol production needs massive scaling
    - **Toxic**: Methanol is poisonous, requires careful handling
    
    **Production Pathways:**
    - **Grey methanol** (from natural gas): Small emissions reduction, available today
    - **Blue methanol** (from natural gas + carbon capture): Moderate reduction, emerging
    - **Bio-methanol** (from biomass): 65-95% reduction, limited feedstock availability
    - **E-methanol/Green methanol** (from renewable H2 + captured CO2): 100% carbon-neutral, expensive, scaling up
    
    **Industry Momentum:**
    - **Maersk**: Committed to methanol, ordered 25+ methanol-powered vessels
    - **CMA CGM**: Ordered methanol dual-fuel vessels
    - **Partnerships**: Shipping lines partnering with methanol producers
    - Expected to be major fuel by 2030s
    """)
    
    st.markdown('<p class="subsection-header">3. Ammonia (NH3)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Current Status:** Promising long-term solution, still in development
    
    **Characteristics:**
    - **Carbon-free**: No carbon in molecule (N-H bonds only)
    - **Energy density**: 45% of conventional fuel
    - **Form**: Liquid at -33°C or pressurised at ambient temperature
    - **Production**: Haber-Bosch process (established industrial chemistry)
    
    **Advantages:**
    - **Zero-carbon**: No CO2 emissions when burned (only N2 and H2O)
    - **Existing infrastructure**: Ammonia already produced and transported globally (fertiliser industry)
    - **Energy carrier**: Can be produced from renewable electricity (green ammonia)
    - **High energy density**: Better than hydrogen (though less than methanol)
    
    **Disadvantages:**
    - **Highly toxic**: Very dangerous to humans, strict safety protocols required
    - **Corrosive**: Requires special materials for tanks and engines
    - **NOx emissions**: Combustion produces nitrogen oxides (though manageable)
    - **Technology immature**: No commercial ammonia-powered ships yet (expected 2024-2026)
    - **Cost**: Green ammonia very expensive (3-4x conventional fuel)
    - **Handling complexity**: Requires specialised training and equipment
    
    **Timeline:**
    - **2024-2026**: First ammonia-powered vessels expected
    - **2030s**: Commercial deployment scaling up
    - **2040s**: Potentially major fuel for large vessels
    
    **Best Suited For:**
    - Large ocean-going vessels (long-haul routes)
    - Bulk carriers, tankers, container ships
    - Where volumetric energy density less critical
    """)
    
    st.markdown('<p class="subsection-header">4. Hydrogen (H2)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Current Status:** Challenging for shipping, better suited for other transport sectors
    
    **Characteristics:**
    - **Zero-carbon**: Only produces water when burned
    - **Energy density**: Very low (requires 4x volume vs conventional fuel)
    - **Form**: Gas at ambient conditions; liquid at -253°C; compressed gas at high pressure
    - **Production**: Electrolysis (green H2) or steam methane reforming (grey/blue H2)
    
    **Advantages:**
    - **Zero emissions**: Only water vapour produced
    - **Abundant**: Can be produced from water and renewable electricity
    - **Multiple uses**: Fuel cells or combustion engines
    
    **Disadvantages:**
    - **Very low energy density**: Requires enormous tank volume (4x conventional fuel)
    - **Cryogenic challenges**: Liquefied hydrogen extremely cold (-253°C)
    - **Boil-off**: Liquid hydrogen evaporates if not used quickly
    - **Safety concerns**: Highly flammable, explosion risk
    - **Cost**: Green hydrogen very expensive
    - **Infrastructure**: Minimal bunkering infrastructure exists
    
    **Realistic Application:**
    - Short-distance ferries
    - Small vessels
    - Port equipment (terminal tractors, tugs)
    - **Not practical for large ocean-going vessels** due to space constraints
    """)
    
    st.markdown('<p class="subsection-header">5. Biofuels</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Current Status:** Drop-in solution, limited by feedstock availability
    
    **Characteristics:**
    - **Types**: Biodiesel (FAME), Hydrotreated Vegetable Oil (HVO), Bio-LNG
    - **Carbon reduction**: 65-95% depending on feedstock and production method
    - **Form**: Liquid, similar to conventional fuel
    - **Compatibility**: Drop-in replacement (no engine modifications needed)
    
    **Advantages:**
    - **Drop-in fuel**: Can use in existing ships without modification
    - **Proven technology**: Used in road transport, aviation
    - **Carbon reduction**: Significant reduction vs fossil fuels
    - **Existing infrastructure**: Can use existing bunkering facilities
    
    **Disadvantages:**
    - **Feedstock limits**: Not enough sustainable biomass to fuel entire shipping fleet
    - **Food vs fuel**: Competition with food production for feedstock
    - **Cost**: 2-3x more expensive than conventional fuel
    - **Sustainability concerns**: Need to ensure truly sustainable sourcing
    
    **Strategic Role:**
    - **Blending**: Mix with conventional fuel (e.g., 30% biofuel, 70% conventional)
    - **Niche applications**: High-value cargo, cruise ships (PR benefit)
    - **Not a complete solution**: Cannot scale to replace all fossil fuels
    """)
    
    # Alternative fuels comparison
    fuels_comparison = pd.DataFrame({
        'Fuel': ['Conventional HFO', 'LNG', 'Methanol (Grey)', 'Methanol (Green)', 'Ammonia (Green)', 'Hydrogen (Green)', 'Biofuels'],
        'CO2 Reduction (%)': [0, 20, 10, 100, 100, 100, 80],
        'Technology Maturity': ['Mature', 'Mature', 'Developing', 'Emerging', 'Early stage', 'Early stage', 'Mature'],
        'Infrastructure Availability': ['Global', 'Good (185 ports)', 'Growing (122 ports)', 'Limited', 'Very limited', 'Very limited', 'Moderate'],
        'Relative Cost': ['1.0x', '1.2x', '2.0x', '3.0x', '4.0x', '4.5x', '2.5x'],
        'Energy Density (vs HFO)': ['100%', '60%', '50%', '50%', '45%', '25%', '90%'],
        'Best For': [
            'Baseline',
            'Transition fuel, near-term',
            'Transition, container ships',
            'Long-term zero-carbon',
            'Large vessels, long-haul',
            'Short-range, small vessels',
            'Drop-in supplement'
        ]
    })
    
    st.dataframe(fuels_comparison, width='stretch', hide_index=True)
    
    # Fuel adoption timeline
    fig = go.Figure()
    
    fuels_timeline = [
        {'fuel': 'LNG', 'start': 2015, 'peak': 2030, 'color': '#3B82F6'},
        {'fuel': 'Methanol', 'start': 2023, 'peak': 2035, 'color': '#10B981'},
        {'fuel': 'Ammonia', 'start': 2025, 'peak': 2040, 'color': '#F59E0B'},
        {'fuel': 'Biofuels', 'start': 2020, 'peak': 2035, 'color': '#8B5CF6'}
    ]
    
    for i, fuel in enumerate(fuels_timeline):
        years = list(range(2015, 2051))
        adoption = []
        for year in years:
            if year < fuel['start']:
                adoption.append(0)
            elif year < fuel['peak']:
                # Ramp up
                progress = (year - fuel['start']) / (fuel['peak'] - fuel['start'])
                adoption.append(progress * 100)
            else:
                # At peak
                adoption.append(100)
        
        fig.add_trace(go.Scatter(
            x=years,
            y=adoption,
            mode='lines',
            name=fuel['fuel'],
            line=dict(color=fuel['color'], width=3)
        ))
    
    fig.update_layout(
        title={
            'text': 'Alternative Fuel Adoption Timeline (Projected)',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        xaxis_title="Year",
        yaxis_title="Relative Adoption (%)",
        height=450,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='#E5E7EB'),
        xaxis=dict(gridcolor='#E5E7EB'),
        legend=dict(x=0.02, y=0.98, bgcolor='rgba(255,255,255,0.8)')
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown("""
    <div class="insight-box">
    <strong>🎯 The Transition Strategy:</strong><br><br>
    Most shipping lines and ports are pursuing a <strong>multi-fuel strategy</strong>:<br><br>
    <strong>Phase 1 (2020-2030): Transition Fuels</strong><br>
    - LNG as primary alternative fuel<br>
    - Methanol (grey/bio) emerging<br>
    - Biofuel blending<br>
    - Focus on meeting 2030 targets (-40% intensity)<br><br>
    <strong>Phase 2 (2030-2040): Zero-Carbon Scaling</strong><br>
    - Green methanol scaling up<br>
    - Ammonia commercial deployment<br>
    - LNG phasing out<br>
    - Multiple fuels coexisting<br><br>
    <strong>Phase 3 (2040-2050): Net-Zero Achievement</strong><br>
    - Green methanol and ammonia dominate<br>
    - Final fossil fuel phase-out<br>
    - Net-zero achieved<br><br>
    <strong>Key Uncertainty:</strong> Which fuel(s) will win long-term? Or will multiple fuels coexist?<br>
    - Methanol favoured for container ships (easier handling)<br>
    - Ammonia may dominate bulk carriers, tankers (long routes, less space constraint)<br>
    - Portfolio approach reduces risk of choosing "wrong" fuel
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 3: Green Port Technologies and Initiatives
    # ============================================================================
    
    st.markdown('<p class="section-header">Green Port Technologies and Initiatives</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Ports play a critical role in maritime decarbonisation through infrastructure, operations, and 
    ecosystem development.
    """)
    
    st.markdown('<p class="subsection-header">1. Alternative Fuel Bunkering Infrastructure</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Singapore's Strategy:**
    
    **LNG Bunkering (Established):**
    - First LNG bunker vessel in Asia (2017)
    - Multiple LNG bunkering service providers
    - Ship-to-ship and truck-to-ship operations
    - 40+ million tonnes marine fuel supplied annually (world's #1)
    
    **Methanol Bunkering (Scaling Up):**
    - Pilot programmes launched
    - Infrastructure investments
    - Partnerships with methanol producers and shipping lines
    - Target: Become major methanol bunkering hub by 2030
    
    **Ammonia Bunkering (Future):**
    - Feasibility studies and planning
    - Safety protocols development
    - Infrastructure requirements being defined
    - Expected commercial availability 2030+
    
    **Multi-Fuel Port Vision:**
    - Support all alternative fuels simultaneously
    - Flexibility as fuel preferences evolve
    - Comprehensive bunkering infrastructure
    - Lock in position as global bunkering hub regardless of which fuel wins
    """)
    
    # Bunkering infrastructure availability
    bunkering_data = pd.DataFrame({
        'Fuel Type': ['Conventional HFO/MGO', 'LNG', 'Methanol', 'Biofuels', 'Ammonia', 'Hydrogen'],
        'Ports Offering (Globally)': [500, 185, 122, 50, 0, 5],
        'Singapore Status': [
            'Established (#1 globally, 40M+ tonnes)',
            'Established (multiple providers)',
            'Developing (pilot programmes)',
            'Limited (blending)',
            'Planning (2030+ target)',
            'Research (limited scope)'
        ]
    })
    
    fig = go.Figure(data=[
        go.Bar(
            x=bunkering_data['Fuel Type'],
            y=bunkering_data['Ports Offering (Globally)'],
            marker=dict(color=['#94A3B8', '#3B82F6', '#10B981', '#8B5CF6', '#F59E0B', '#EF4444']),
            text=bunkering_data['Ports Offering (Globally)'],
            textposition='outside'
        )
    ])
    
    fig.update_layout(
        title={
            'text': 'Alternative Fuel Bunkering Infrastructure Availability',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        xaxis_title="Fuel Type",
        yaxis_title="Number of Ports Offering (Globally)",
        height=400,
        plot_bgcolor='white',
        yaxis=dict(gridcolor='#E5E7EB')
    )
    
    st.plotly_chart(fig, width='stretch')
    
    st.markdown('<p class="subsection-header">2. Port Equipment Electrification</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Electrifying Port Operations:**
    
    **Quay Cranes:**
    - **Traditional**: Diesel generators on crane
    - **Modern**: Shore power (electric from grid)
    - **Benefit**: Zero emissions, quieter operations, lower operating costs
    - **Tuas**: All quay cranes electrically powered
    
    **Yard Equipment:**
    - **Traditional**: Diesel RTGs, prime movers
    - **Modern**: Electric RMGs, battery-electric AGVs
    - **E-RTG**: Electric RTG with regenerative braking (50% energy savings)
    - **AGVs**: Fully battery-powered, zero emissions
    
    **Horizontal Transport:**
    - **Traditional**: Diesel prime movers
    - **Modern**: Battery-electric AGVs/ALVs
    - **Charging infrastructure**: Fast-charging stations throughout terminal
    
    **Impact:**
    - 60-70% reduction in terminal emissions
    - Improved air quality for workers and neighbours
    - Lower noise pollution
    - Reduced operating costs (electricity cheaper than diesel)
    """)
    
    st.markdown('<p class="subsection-header">3. Shore Power (Cold Ironing)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Concept:**
    - Vessels plug into shore-based electrical grid whilst at berth
    - Shut down onboard diesel generators (which normally provide power for crew, reefers, pumps)
    - Use clean grid electricity instead
    
    **Benefits:**
    - **Emissions**: Zero emissions at berth (vs running diesel generators)
    - **Air quality**: Major improvement in port neighbourhoods
    - **Noise**: Much quieter (no generator engines running)
    
    **Challenges:**
    - **Infrastructure cost**: $2-5 million per berth for shore power installation
    - **Vessel compatibility**: Ships need to be equipped with shore power connection
    - **Different standards**: US (60 Hz) vs Europe/Asia (50 Hz) electrical systems
    - **Pricing**: Need competitive pricing to incentivise use
    
    **Singapore Status:**
    - Shore power being deployed at Tuas Mega Port
    - Incentives for vessels to use shore power
    - Part of broader green port strategy
    """)
    
    st.markdown('<p class="subsection-header">4. Renewable Energy Generation</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Solar Power:**
    - **Rooftop solar**: Solar panels on terminal buildings, warehouses
    - **Canopy solar**: Solar panel canopies over container stacks
    - **Tuas**: Extensive solar deployment (one of world's largest solar-powered ports)
    
    **Energy Storage:**
    - **Battery systems**: Store excess solar for night operations
    - **Load balancing**: Smooth out demand peaks
    
    **Energy Efficiency:**
    - **LED lighting**: Throughout terminal
    - **Smart controls**: AI-optimised energy usage
    - **Building design**: Energy-efficient HVAC and insulation
    """)
    
    st.markdown('<p class="subsection-header">5. Climate Resilience</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Ports must adapt to climate change impacts whilst reducing emissions.
    
    **Sea Level Rise Protection:**
    - **Tuas Mega Port**: Built **5 metres above mean sea level**
    - Protects against projected sea level rise through 2100
    - Incorporates climate models and storm surge predictions
    
    **Extreme Weather Resilience:**
    - Reinforced structures for stronger storms
    - Improved drainage systems for heavier rainfall
    - Heat-resistant materials and cooling systems
    
    **Sustainable Design:**
    - Natural ventilation where possible
    - Green spaces and biodiversity preservation
    - Circular economy principles (waste reduction, recycling)
    """)
    
    # ============================================================================
    # SECTION 4: Digital Transformation and Innovation
    # ============================================================================
    
    st.markdown('<p class="section-header">Digital Transformation: The Future is Data-Driven</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Beyond green technologies, digital innovation is transforming how ports operate and compete.
    """)
    
    st.markdown('<p class="subsection-header">1. Digital Documentation and Paperless Trade</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Paper Problem:**
    - Traditional shipping generates massive paperwork (bills of lading, customs docs, certificates)
    - Paper-based processes slow, error-prone, expensive
    - Physical documents must be couriered globally
    
    **Digital Solutions:**
    
    **Electronic Bill of Lading (eBL):**
    - **Blockchain-based**: Secure, tamper-proof digital record
    - **Instant transfer**: No physical courier needed
    - **Cost savings**: Eliminates printing, courier, storage costs
    - **Time savings**: Hours vs days for document transfer
    - **Singapore adoption**: MPA promoting eBL adoption
    
    **Electronic Bunker Delivery Note (e-BDN):**
    - Digital record of fuel delivered to vessel
    - Automated data capture and verification
    - Reduces fraud and errors
    - Integrated with port systems
    
    **E-Certificates:**
    - Digital ship certificates (safety, security, classification)
    - Instantly verifiable by port authorities
    - Reduces administrative burden
    - IMO-approved frameworks emerging
    
    **Benefits:**
    - 30-40% faster document processing
    - 80%+ reduction in documentation errors
    - Significant cost savings (estimated $6.5B annually for global shipping)
    - Environmental: Less paper, less courier travel
    """)
    
    st.markdown('<p class="subsection-header">2. digitalPORT@SG Initiative</p>', unsafe_allow_html=True)
    
    st.markdown("""
    MPA's comprehensive digital transformation programme for Singapore's maritime sector.
    
    **Key Components:**
    
    **AI-Based Integrated Port Operations Control:**
    - Centralised AI system coordinates all port operations
    - Predictive analytics for berth planning, resource allocation
    - Real-time optimisation of vessel traffic, crane deployment
    - Machine learning improves over time based on operational data
    
    **Multi-Sensor Track Fusion:**
    - Integrate data from radar, AIS, cameras, sensors
    - Complete real-time picture of all vessel movements
    - Enhanced safety and security
    - Better traffic management
    
    **Predictive Analytics:**
    - Forecast vessel arrival delays
    - Predict equipment failures before they happen
    - Optimise maintenance scheduling
    - Anticipate demand patterns
    
    **Operational Simulation:**
    - Virtual replica of entire port operations
    - Test scenarios and optimisations before implementing
    - Training environment for operators
    - "What-if" analysis for planning
    """)
    
    st.markdown('<p class="subsection-header">3. digitalOCEANS Platform</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Vision:** Digital representation of Singapore's entire maritime domain
    
    **Capabilities:**
    - **Real-time situational awareness**: All vessel movements, port operations, marine traffic
    - **Data integration**: Connect all maritime stakeholders on single platform
    - **Analytics and insights**: Advanced analytics on maritime patterns, trends, efficiency
    - **Collaborative ecosystem**: Shipping lines, ports, authorities share data securely
    
    **Benefits:**
    - Better coordination across maritime ecosystem
    - Faster decision-making with real-time data
    - Identify optimisation opportunities
    - Enhanced safety and security
    - Platform for innovation (third-party apps can build on digitalOCEANS)
    """)
    
    st.markdown('<p class="subsection-header">4. BLOCK71 Maritime Innovation Hub</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Singapore's Maritime Technology Accelerator** (launched 2018)
    
    **Purpose:**
    - Connect startups with maritime industry challenges
    - Accelerate development and deployment of maritime technologies
    - Foster innovation ecosystem
    
    **Focus Areas:**
    - Autonomous vessels and robotics
    - AI and data analytics
    - Cybersecurity for maritime systems
    - Green technologies (alternative fuels, efficiency)
    - Blockchain and digital trade
    - IoT and sensors
    
    **How It Works:**
    - Startups apply with innovative maritime solutions
    - Receive funding, mentorship, industry connections
    - Pilot technologies with actual maritime companies
    - Scale successful solutions globally
    
    **Impact:**
    - 100+ startups supported
    - Multiple technologies deployed commercially
    - Singapore positioned as maritime tech innovation leader
    """)
    
    # ============================================================================
    # SECTION 5: Maritime Safety and Risk Management
    # ============================================================================
    
    st.markdown('<p class="section-header">Maritime Safety and Risk Management</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Safety remains paramount in maritime operations. Understanding and managing risk is fundamental.
    """)
    
    st.markdown('<p class="subsection-header">Risk Equations in Maritime</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Fundamental Risk Equation:**
    
    **Risk = Probability of Incident × Consequence of Incident**
    
    **Example:**
    - **Low probability, high consequence**: Ship collision (rare but catastrophic)
    - **High probability, low consequence**: Minor equipment damage (frequent but manageable)
    - **High probability, high consequence**: Unacceptable risk, must be eliminated
    
    **Risk Management Strategies:**
    
    **1. Reduce Probability:**
    - Better training for operators
    - Automation (eliminates human error)
    - Preventive maintenance
    - Enhanced safety systems (collision avoidance, fire detection)
    - Strict procedures and checklists
    
    **2. Reduce Consequence:**
    - Emergency response plans
    - Backup systems and redundancy
    - Containment measures (fire suppression, spill containment)
    - Insurance
    - Compartmentalisation (isolate problems)
    
    **3. Eliminate Risk:**
    - Don't perform dangerous activities
    - Substitute safer alternatives
    - Physical barriers and guards
    """)
    
    st.markdown('<p class="subsection-header">Safety Culture in World-Class Ports</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Zero Incident Mindset:**
    - **Goal**: Zero fatalities, zero serious injuries, zero environmental incidents
    - **Not just a slogan**: Backed by policies, training, investment
    - **Safety first**: Operations stop if unsafe conditions exist
    
    **Safety Layers:**
    - **Engineering controls**: Physical safeguards (guards, barriers, automation)
    - **Administrative controls**: Procedures, training, supervision
    - **PPE**: Personal protective equipment (last line of defence)
    
    **Continuous Improvement:**
    - Near-miss reporting and investigation
    - Regular safety audits
    - Lessons learned sharing
    - Benchmarking against best practices
    
    **Technology Enablers:**
    - Automation reduces human exposure to danger
    - Sensors detect hazards before incidents
    - Cameras and monitoring ensure compliance
    - AI identifies risky patterns
    """)
    
    # ============================================================================
    # SECTION 6: Future Trends and Challenges
    # ============================================================================
    
    st.markdown('<p class="section-header">Future Trends: What\'s Next for Maritime?</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Looking ahead, several major trends will shape the maritime industry over the next 20-30 years.
    """)
    
    st.markdown('<p class="subsection-header">1. Autonomous Vessels</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Vision:** Ships that navigate and operate without human crews (or minimal crews)
    
    **Technology Status:**
    - **Short-range autonomous**: Ferries, harbour operations (trials ongoing)
    - **Remote-controlled**: Vessels controlled from shore (commercially available)
    - **Fully autonomous ocean-going**: Still many years away (2030s-2040s)
    
    **Benefits:**
    - **Safety**: Eliminate human error (80% of maritime accidents involve human error)
    - **Efficiency**: Optimal routing and fuel consumption
    - **Cost**: Reduce crew costs (significant expense)
    - **Design**: Ships without crew quarters can carry more cargo
    
    **Challenges:**
    - **Regulations**: International maritime law assumes human crew on board
    - **Reliability**: Systems must be extremely reliable (no second chances at sea)
    - **Cybersecurity**: Autonomous vessels vulnerable to hacking
    - **Public acceptance**: Society may resist crewless ships
    - **Liability**: Who's responsible if autonomous ship has accident?
    
    **Realistic Timeline:**
    - **2025-2030**: Autonomous harbour operations, short-range ferries
    - **2030-2040**: Remote-controlled ocean vessels (crew on shore)
    - **2040+**: Fully autonomous ocean-going ships (if regulatory framework allows)
    """)
    
    st.markdown('<p class="subsection-header">2. Hyperconnected Supply Chains</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Vision:** Complete visibility and integration across entire supply chain
    
    **Elements:**
    - **IoT sensors**: Every container tracked in real-time
    - **Blockchain**: Immutable record of ownership, location, condition
    - **AI optimisation**: Dynamic routing and scheduling based on real-time conditions
    - **Predictive analytics**: Anticipate delays, adjust plans proactively
    - **Customer transparency**: Customers see exactly where cargo is, when it will arrive
    
    **Impact:**
    - Eliminate information gaps and surprises
    - Faster response to disruptions
    - More efficient use of assets
    - Better customer experience
    - Just-in-time delivery becomes reliable
    """)
    
    st.markdown('<p class="subsection-header">3. Circular Economy and Waste Reduction</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Beyond Zero Emissions:**
    
    **Waste Circularity:**
    - Reuse and recycle port waste
    - Convert waste to energy
    - Zero waste to landfill targets
    - Tuas: Waste heat recovery, material recycling
    
    **Ship Recycling:**
    - Sustainable ship dismantling and recycling
    - Recover and reuse materials
    - Eliminate hazardous waste practices
    
    **Sustainable Procurement:**
    - Favour suppliers with sustainable practices
    - Lifecycle assessment of equipment and materials
    - Design for disassembly and recycling
    """)
    
    st.markdown('<p class="subsection-header">4. Geopolitical and Trade Pattern Shifts</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Ongoing Transformations:**
    
    **Trade Diversification:**
    - "China+1" strategies continue
    - Supply chain resilience prioritised over pure efficiency
    - Regional trade blocs gaining importance
    - Impact: More complex routing, more transshipment
    
    **Nearshoring and Friendshoring:**
    - Shift production closer to consumers or to allied nations
    - Shorter supply chains, different trade lanes
    - Impact: Changes in port volumes and patterns
    
    **Digital Trade Barriers:**
    - Data localisation requirements
    - Cross-border data flow restrictions
    - Impact: Complicates integrated digital platforms
    
    **Climate-Driven Changes:**
    - Carbon border adjustments (EU CBAM, etc.)
    - Pressure to reduce supply chain emissions
    - Impact: Favour efficient, green ports and shipping lines
    """)
    
    # ============================================================================
    # SECTION 7: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Decarbonisation Imperative:**
        - IMO 2030: -40% carbon intensity
        - IMO 2050: Net-zero emissions
        - Requires complete fuel transition
        - Economic, technical, political challenge
        
        **Alternative Fuels:**
        - **LNG**: Transition fuel (20% reduction, available now)
        - **Methanol**: Leading candidate (liquid, scalable to 100% with green methanol)
        - **Ammonia**: Long-term (zero-carbon, toxic, technology developing)
        - **Hydrogen**: Niche applications (energy density challenge)
        - **Biofuels**: Supplement (feedstock limited)
        - Multi-fuel strategy reduces risk
        
        **Green Port Initiatives:**
        - Alternative fuel bunkering infrastructure
        - Equipment electrification (cranes, AGVs)
        - Shore power for vessels at berth
        - Renewable energy generation (solar)
        - Climate resilience (Tuas: +5m above sea level)
        """)
    
    with col2:
        st.markdown("""
        **Digital Transformation:**
        - Paperless trade (eBL, e-BDN, e-Certificates)
        - digitalPORT@SG (AI, predictive analytics)
        - digitalOCEANS (maritime operational simulation)
        - BLOCK71 (innovation accelerator)
        - Data-driven operations and optimisation
        
        **Safety and Risk:**
        - Risk = Probability × Consequence
        - Zero incident mindset
        - Engineering + administrative controls + PPE
        - Automation improves safety
        
        **Future Trends:**
        - Autonomous vessels (2030s-2040s for ocean-going)
        - Hyperconnected supply chains (IoT, blockchain, AI)
        - Circular economy (waste reduction, recycling)
        - Geopolitical shifts (trade diversification)
        - Climate adaptation (sea level rise, extreme weather)
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> The maritime industry is undergoing its most significant transformation 
    in a century. Achieving net-zero by 2050 requires transitioning from fossil fuels to alternative fuels 
    (likely methanol and ammonia), massive infrastructure investment, and technological innovation. 
    Singapore positions itself as a leader through multi-fuel bunkering infrastructure, green port 
    technologies (Tuas built +5m above sea level, solar-powered, electrified equipment), and digital 
    transformation (digitalPORT@SG, digitalOCEANS, BLOCK71 innovation hub). Beyond decarbonisation, 
    autonomous vessels, hyperconnected supply chains, and geopolitical shifts will reshape maritime 
    competition. Ports that lead in sustainability, digitalisation, and adaptability will thrive; those 
    that lag will struggle.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Final Topic:** 🏗️ Tuas Mega Port Case Study - Explore Singapore's $20B+ mega port development, 
    understanding why it's being built, how it will operate, and whether it will be enough to maintain 
    Singapore's competitive position.
    """)
