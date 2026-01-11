"""
ENHANCED VERSION - January 2026
Key Changes:
- Verified: Vessel evolution data confirmed against lecture materials (04_World_of_Container_Shipping.pdf, a_Introduction_to_Container_Sea_Transport.pdf)
- Corrected: Updated largest vessel to MSC Irina (24,346 TEU) from MSC Gülsün (23,756 TEU)
- Enhanced: Added current 2024-2025 context including:
  * Latest vessel deliveries and records (Ever Alot 24,004 TEU, HMM Algeciras 24,000 TEU)
  * Current carrier capacity rankings (MSC 7.1M TEU, Maersk 4.6M TEU, CMA CGM 4.1M TEU as of Dec 2025)
  * Global fleet statistics (33.6M TEU total capacity, 7.2% growth in 2024-2025)
  * 2025 alliance changes (2M dissolved, Gemini and Premier alliances formed)
  * Alternative fuel adoption (7% LNG-capable fleet, methanol/ammonia development)
  * Environmental regulations (IMO 2020 implemented, IMO 2050 targets, FuelEU Maritime 2025)
  * Current slow steaming practices and fuel efficiency improvements
  * Red Sea disruption impact on mega vessels (avoiding Suez for 20+ months)
- Sources: Lecture PDFs, Alphaliner December 2025, Maritime Executive, Container News, UNCTAD 2024,
  IMO regulations, Global Maritime Forum, industry vessel tracking data
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def show():
    st.markdown('<p class="main-header">🚢 Container Vessels & Evolution</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>📘 Learning Objectives</strong><br>
    Understand vessel anatomy, the dramatic evolution in vessel sizes over decades, classification systems, 
    the economics driving vessel growth, and the principles of vessel stowage planning.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 1: Vessel Anatomy and Terminology
    # ============================================================================
    
    st.markdown('<p class="section-header">Vessel Anatomy and Maritime Terminology</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Before diving into vessel evolution, let's understand basic vessel anatomy and the terminology used 
    throughout the maritime industry. These terms are universal across all maritime professionals worldwide.
    """)
    
    st.markdown('<p class="subsection-header">Basic Vessel Directions and Parts</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Directional Terms:**
        - **Bow (Forward)**: Front of the ship
        - **Stern (Aft)**: Back of the ship
        - **Port**: Left side (facing forward) - red navigation light
        - **Starboard**: Right side (facing forward) - green navigation light
        - **Amidships**: Middle section
        - **Fore and aft**: Lengthwise (bow to stern)
        
        **Vertical Terms:**
        - **Deck**: Horizontal platform/floor
        - **Hold**: Cargo space below deck
        - **Hatch**: Opening in deck to access hold
        - **Superstructure**: Buildings above main deck
        - **Draft**: Depth of vessel below waterline
        """)
    
    with col2:
        st.markdown("""
        **Key Vessel Sections:**
        - **Bridge**: Command centre, usually at stern on container ships
        - **Accommodation**: Living quarters for crew (~25 crew on mega vessels)
        - **Engine Room**: Contains propulsion machinery (main engine, generators)
        - **Cargo Holds**: Below-deck storage areas (cellular structure)
        - **Weather Deck**: Topmost deck exposed to elements
        - **Forecastle**: Forward raised deck
        
        **Container-Specific:**
        - **Bay**: Vertical slice (lengthwise division), numbered bow to stern
        - **Row**: Horizontal position (across width), numbered port to starboard
        - **Tier**: Vertical stacking position (height), numbered bottom to top
        - **Cell guides**: Vertical rails that guide containers into position
        """)
    
    st.markdown('<p class="subsection-header">Container Positioning System on Vessels</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Every container on a vessel has a precise three-dimensional address using the **Bay-Row-Tier** system. 
    This enables crane operators to locate any container among potentially 20,000+ containers in seconds.
    
    **Bay (Longitudinal Position):**
    - Numbered from bow (front) to stern (back)
    - **Odd numbers**: 20-foot container positions (01, 03, 05, 07, 09...)
    - **Even numbers**: 40-foot container positions (02, 04, 06, 08, 10...)
    - A 40-foot container occupies two 20-foot bays
    - Large vessels: Bay 01 to Bay 200+ (100+ 40ft positions)
    - Example: Bay 02 = 40ft position covering 20ft bays 01 and 03
    
    **Row (Transverse Position):**
    - Numbered from port (left) to starboard (right) when facing forward
    - Centre line: **00**
    - **Odd**: Port side (01, 03, 05, 07...)
    - **Even**: Starboard side (02, 04, 06, 08...)
    - Range depends on vessel width
    - Panamax: 00 to 13 (13 containers across)
    - Ultra Large: 00 to 24 (24 containers across)
    
    **Tier (Vertical Position):**
    - Numbered from bottom to top
    - **Below deck**: 02, 04, 06, 08, 10, 12... (even numbers, working down from deck)
    - **Deck level**: 80 (reference level)
    - **Above deck**: 82, 84, 86, 88, 90, 92... (even numbers above 80, working up from deck)
    - Large vessels: Up to 10-12 tiers above deck (Tier 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102)
    - Below deck: Up to 8-10 tiers below (Tier 02, 04, 06, 08, 10, 12, 14, 16, 18, 20)
    
    **Example:** Container at position **Bay 24, Row 06, Tier 88** is:
    - 24th bay from bow (12th 40ft position)
    - 6th row from port side (starboard side, even number)
    - 4 tiers above deck level (80 = deck, 82 = 1st above, 84 = 2nd, 86 = 3rd, 88 = 4th)
    
    **Why Even Numbers?**
    - Historical convention from early container ships
    - Allows insertion of intermediate positions if needed
    - Provides clear distinction between 20ft and 40ft positions (odd vs even for bays)
    """)
    
    # ============================================================================
    # SECTION 2: Vessel Size Evolution
    # ============================================================================
    
    st.markdown('<p class="section-header">The Dramatic Evolution of Container Vessel Sizes</p>', unsafe_allow_html=True)
    
    st.markdown("""
    One of the most striking transformations in maritime history is the growth in container vessel sizes. 
    In just 69 years (1956-2025), vessels have grown **nearly 50 times** in capacity—from 500 TEU to 24,000+ TEU.
    
    **Current State (2024-2025):**
    - **Global container fleet**: 33.6 million TEU total capacity (December 2025)
    - **Fleet growth**: 7.2% increase in 2024-2025 (from 31.4M to 33.6M TEU)
    - **Largest vessels**: 24,000-24,346 TEU (MSC Irina class, Ever Alot, HMM Algeciras)
    - **Orderbook**: Over 10 million TEU on order (largest in history)
    - **Trend**: Continued up-gauging toward larger vessel classes
    """)
    
    # Vessel evolution data - updated with 2024-2025 records
    vessel_evolution = pd.DataFrame({
        'Year': [1956, 1970, 1980, 1988, 1996, 2006, 2013, 2019, 2020, 2022, 2025],
        'Vessel Example': [
            'Ideal X (First)',
            'Encounter Bay',
            'American New York',
            'Panamax Standard',
            'Regina Maersk',
            'Emma Maersk',
            'Maersk Triple E',
            'MSC Gülsün',
            'HMM Algeciras',
            'Ever Alot',
            'MSC Irina (Current Largest)'
        ],
        'Capacity (TEU)': [500, 1500, 3000, 4500, 6500, 15000, 18000, 23756, 24000, 24004, 24346],
        'Length (m)': [135, 180, 230, 290, 318, 397, 400, 400, 400, 400, 400],
        'Width (m)': [17, 24, 30, 32, 42, 56, 59, 61, 61, 61.5, 61.5],
        'Max Draft (m)': [9, 10, 12, 13, 14, 16, 16, 16.5, 16.5, 16.5, 16.5],
        'Containers Across': ['6', '8', '11', '13', '16', '22', '23', '24', '24', '24', '24']
    })
    
    st.dataframe(vessel_evolution, use_container_width=True, hide_index=True)
    
    # Capacity growth visualisation
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=vessel_evolution['Year'],
        y=vessel_evolution['Capacity (TEU)'],
        mode='lines+markers',
        name='TEU Capacity',
        line=dict(color='#3B82F6', width=4),
        marker=dict(size=12, color='#2563EB', line=dict(color='white', width=2)),
        text=vessel_evolution['Vessel Example'],
        hovertemplate='<b>%{text}</b><br>Year: %{x}<br>Capacity: %{y:,} TEU<extra></extra>'
    ))
    
    fig.update_layout(
        title={
            'text': 'Container Vessel Capacity Growth: 1956 → 2025',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#1F2937'}
        },
        xaxis_title="Year",
        yaxis_title="Capacity (TEU)",
        height=500,
        plot_bgcolor='white',
        xaxis=dict(gridcolor='#E5E7EB'),
        yaxis=dict(gridcolor='#E5E7EB', range=[0, 26000])
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    **Key Observations:**
    
    **1956-1980s: Early Growth**
    - Modest increases from 500 to 3,000 TEU
    - Vessels constrained by port infrastructure and canal widths
    - Focus on proving containerisation concept
    - Industry establishing standards and operational procedures
    
    **1988: Panamax Limit**
    - ~4,500 TEU defined by **Panama Canal dimensions**
    - Maximum width: 32.3 metres (106 feet)
    - Standard for two decades (1980s-2000s)
    - Most vessels built to this size for canal access
    
    **1996-2006: Breaking Through**
    - Post-Panamax vessels exceed canal limits
    - 6,500 → 15,000 TEU in just 10 years
    - New-Panamax canal expansion announced (2007, completed 2016)
    - Asia-Europe trade growth drives demand for larger ships
    
    **2013-2019: Mega Vessel Era**
    - Ultra Large Container Ships (ULCS) reach 23,000+ TEU
    - 24 containers across width (world record)
    - Triple-E class focuses on Economy of scale, Energy efficiency, Environmental improvement
    - Approaching practical limits (port depth, crane reach, structural integrity)
    
    **2020-2025: Plateau at Maximum**
    - Capacity stabilised around 24,000-24,346 TEU
    - Focus shifted from size to efficiency and sustainability
    - HMM (2020), Ever Alot (2022), MSC Irina (2023) set current records
    - **Consensus**: 24,000 TEU is practical maximum for current infrastructure
    - **Red Sea crisis (2023-2025)**: Mega vessels avoiding Suez for 20+ months, affecting deployment
    """)
    
    st.markdown("""
    <div class="info-box">
    <strong>💡 Why Did Vessels Grow So Large?</strong><br>
    - <strong>Economies of Scale</strong>: Bigger vessels dramatically reduce cost per container:<br>
    - <strong>Crew costs</strong>: Same ~25 crew whether carrying 5,000 or 20,000 TEU (~$5M/year fixed cost)<br>
    - <strong>Fuel per TEU</strong>: Larger vessels 30-40% more fuel-efficient per container (hull efficiency)<br>
    - <strong>Capital cost per TEU</strong>: Building a 20,000 TEU vessel doesn't cost 4× a 5,000 TEU vessel<br>
    - <strong>Port fees per TEU</strong>: Fixed port charges ($50-100K per call) spread over more containers<br>
    - <strong>Canal fees per TEU</strong>: Suez ($600K per transit) spread over 20,000 vs 5,000 containers<br><br>
    <strong>Result</strong>: An 18,000 TEU vessel costs roughly <strong>80-85% less per TEU</strong> than a 1,000 TEU vessel<br>
    Example: $1,000/TEU (1,000 TEU vessel) vs $150-180/TEU (18,000 TEU vessel)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ Why Growth Has Stopped at ~24,000 TEU:</strong><br>
    - <strong>Port infrastructure</strong>: Only ~20-30 ports globally can handle 24,000 TEU vessels<br>
    - <strong>Crane reach limitations</strong>: 24 containers across (~61m beam) at maximum crane outreach (70-80m)<br>
    - <strong>Draft restrictions</strong>: 16.5m draft limits access to many ports<br>
    - <strong>Canal constraints</strong>: Too wide for Panama Canal (49m limit), barely fits Suez (77.5m limit)<br>
    - <strong>Concentration risk</strong>: Single vessel carries $500M+ cargo value<br>
    - <strong>Port congestion</strong>: Larger vessels create operational bottlenecks<br>
    - <strong>Diminishing returns</strong>: Cost savings flatten above 20,000 TEU<br>
    - <strong>Market volatility</strong>: 2024-2025 overcapacity concerns reduce incentive for more mega vessels
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # SECTION 3: Vessel Classification Systems
    # ============================================================================
    
    st.markdown('<p class="section-header">Vessel Classification by Size</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The industry uses several classification systems based on vessel size and capability. Understanding 
    these categories is essential for port planning, route design, and operational discussions.
    """)
    
    # Classification data
    vessel_classes = pd.DataFrame({
        'Class': [
            'Feeder',
            'Feedermax',
            'Panamax',
            'Post-Panamax',
            'New-Panamax (Neo-Panamax)',
            'VLCS (Very Large Container Ship)',
            'ULCS (Ultra Large Container Ship)',
            'Megamax (24,000 TEU Class)'
        ],
        'Capacity Range (TEU)': [
            '100 - 1,000',
            '1,000 - 3,000',
            '3,000 - 5,100',
            '5,100 - 10,000',
            '10,000 - 14,500',
            '14,500 - 18,000',
            '18,000 - 24,000',
            '21,000 - 24,346'
        ],
        'Typical Width (m)': ['<23', '23-30', '32.2 (max)', '32.3-43', '49-51', '51-59', '59-61', '61-61.5'],
        'Defining Constraint': [
            'Small ports, rivers, coastal',
            'Regional routes',
            'Old Panama Canal (pre-2016)',
            'Suez Canal depth, port infrastructure',
            'New Panama Canal (2016+)',
            'Port crane reach, major hub ports',
            'Ultra-deep berths, mega-cranes only',
            'Maximum practical size (crane reach limit)'
        ],
        'Typical Routes': [
            'Short-sea, river, coastal, intra-regional',
            'Intra-regional (Asia, Europe, Americas)',
            'Trans-Pacific, Asia-Europe (obsolete)',
            'Major trade lanes, hub feedering',
            'Trans-Pacific via Panama, major trades',
            'Asia-Europe mainline, Trans-Pacific',
            'Asia-Europe mainline only',
            'Asia-Europe mainline, limited deployment'
        ],
        'Example Vessels / Operators': [
            'Regional feeders, short-sea operators',
            'Wan Hai, Pacific International Lines',
            'APL China (retired from mainline)',
            'Maersk Sealand class',
            'CMA CGM Brazil, APL Temasek',
            'OOCL Hong Kong, CMA CGM Antoine',
            'MSC Gülsün, HMM Algeciras',
            'MSC Irina, Ever Alot (24,346/24,004 TEU)'
        ]
    })
    
    st.dataframe(vessel_classes, use_container_width=True, hide_index=True)
    
    st.markdown('<p class="subsection-header">Canal and Port Constraints</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Panama Canal Constraints:**
        
        **Old Locks (Pre-2016, Now Retired):**
        - Maximum length: 294.1 m (965 ft)
        - Maximum width: **32.3 m (Panamax limit)**
        - Maximum draft: 12.0 m (39.5 ft)
        - Capacity: ~4,500 TEU maximum
        - **Status**: Still operational but rarely used by container ships
        
        **New Locks (2016-Present):**
        - Maximum length: 366 m (1,201 ft)
        - Maximum width: **49 m (New-Panamax limit)**
        - Maximum draft: 15.2 m (50 ft)
        - Capacity: ~14,500 TEU maximum
        - Expansion cost: $5.4 billion
        - Opened: June 26, 2016
        
        **Impact:**
        - Old canal limited vessel sizes for decades (1914-2016)
        - Expansion allowed larger vessels on trans-Pacific routes
        - Mega vessels (20,000+ TEU) **still cannot use** Panama Canal (too wide)
        - **2024 Challenge**: Drought reduced daily transits (water level restrictions)
        """)
    
    with col2:
        st.markdown("""
        **Suez Canal Constraints:**
        
        **Current Specifications:**
        - Maximum length: No practical limit for container ships
        - Maximum width: **77.5 m beam** (much wider than Panama)
        - Maximum draft: **20.1 m (66 feet)** - deeper than Panama
        - **No locks** (sea-level canal) = faster transit
        - Transit time: ~12-16 hours
        
        **Strategic Importance:**
        - **Asia-Europe route**: 33% of global container trade
        - Can accommodate **all existing container vessels** (even 24,000 TEU)
        - Critical chokepoint for global trade
        - **2023-2025 Crisis**: Red Sea security issues forced mega vessels to avoid Suez
        - **Impact**: Megamax ships (18,000+ TEU) avoided Suez for **20+ consecutive months**
        
        **Alternative: Cape of Good Hope**
        - **+3,500 nautical miles** (+7,000 km)
        - **+7-10 days** sailing time
        - **+$500,000-800,000** extra fuel costs per voyage
        - **+30-40% fuel consumption** (longer distance)
        - **2024-2025**: Widely used due to Red Sea disruptions
        - **Emissions impact**: Global shipping emissions +5% in 2024 due to longer routes
        """)
    
    st.markdown("""
    **2024-2025 Geopolitical Impact:**
    - **Red Sea crisis** (late 2023-2025): Security concerns forced rerouting
    - **Suez traffic**: Down 70% from 2023 levels for mega vessels (18,000+ TEU)
    - **Container ship transits**: 304 in Oct-Nov 2025 vs 331 in 2024 (−8.2% year-on-year)
    - **Recovery uneven**: Only 4,000-7,500 TEU vessels showing meaningful recovery
    - **Ton-miles surge**: While trade volume +2.2%, ton-miles +6% (longer routes)
    - **Freight rate volatility**: Shanghai index averaged 2,496 points in 2024 (+149% from 2023)
    """)
    
    # ============================================================================
    # SECTION 4: Global Fleet and Carrier Rankings (2024-2025)
    # ============================================================================
    
    st.markdown('<p class="section-header">Global Container Fleet: Current State (December 2025)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The global container shipping industry is dominated by a few major carriers, with significant concentration 
    of capacity.
    """)
    
    # Current carrier rankings (December 2025 data)
    carrier_rankings = pd.DataFrame({
        'Rank': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Carrier': ['MSC', 'Maersk', 'CMA CGM', 'COSCO', 'Hapag-Lloyd', 'ONE', 'Evergreen', 'HMM', 'Yang Ming', 'ZIM'],
        'Fleet Capacity (M TEU)': [7.1, 4.6, 4.1, 3.3, 2.4, 2.0, 1.9, 1.0, 0.7, 0.4],
        'Number of Vessels': [886, 735, 663, 515, 300, 250, 220, 130, 100, 130],
        'Market Share (%)': [19.9, 14.6, 12.7, 10.8, 7.0, 5.9, 5.6, 2.9, 2.2, 1.3],
        'Orderbook (M TEU)': [2.2, 0.8, 1.9, 0.6, 0.3, 0.2, 0.9, 0.2, 0.1, 0.1],
        'Headquarters': ['Geneva, Switzerland', 'Copenhagen, Denmark', 'Marseille, France', 'Shanghai, China', 
                        'Hamburg, Germany', 'Singapore', 'Taiwan', 'Seoul, South Korea', 'Taiwan', 'Haifa, Israel']
    })
    
    st.dataframe(carrier_rankings, use_container_width=True, hide_index=True)
    
    st.markdown("""
    **Key Developments (2024-2025):**
    
    **MSC Dominance:**
    - Surpassed 7 million TEU for first time (November 2025)
    - **50% larger** than #2 Maersk (7.1M vs 4.6M TEU)
    - Added 831,000 TEU in 2025 (5th consecutive year of massive expansion)
    - Acquired ~400 ships in past 5 years (many secondhand vessels)
    - Operates **solo** (left 2M alliance in 2025)
    - Largest orderbook: 2.2 million TEU (larger than most carriers' entire fleets)
    
    **Maersk Transformation:**
    - Shifted strategy from pure shipping to **integrated logistics**
    - Revenue $55.5 billion (2024)
    - Dissolved 2M alliance with MSC (January 2025)
    - Formed **Gemini Cooperation** with Hapag-Lloyd (2025)
    - Focus: Schedule reliability >90%, digital services, net-zero by 2040
    - Fleet: Methanol-powered vessels (world's first, 2023+)
    
    **CMA CGM Rising:**
    - Exceeded 4 million TEU in early 2025
    - Massive orderbook: 1.9 million TEU (challenging Maersk for #2)
    - Total pipeline (active + orders): ~6.0 million TEU
    - Acquisitions: CEVA Logistics, Bolloré Logistics
    - Investment: $20 billion in US maritime sector through 2029
    
    **HMM Achievement:**
    - Joined "One-Million-TEU Club" (October 2025)
    - Capacity: 1,007,180 TEU (Alphaliner, November 2025)
    - First to deploy 24,000 TEU vessels (HMM Algeciras, 2020)
    - Rapid growth: Doubled fleet in 5 years (state-supported expansion)
    - Joined **Premier Alliance** with ONE and Yang Ming (March 2025)
    
    **Alliance Changes (2025):**
    - **2M Alliance**: Dissolved (Maersk + MSC, ended January 2025 after 10 years)
    - **Gemini Cooperation**: Formed (Maersk + Hapag-Lloyd, launched 2025)
    - **Premier Alliance**: Formed (ONE + HMM + Yang Ming, launched March 2025)
    - **Ocean Alliance**: Unchanged (CMA CGM + COSCO + OOCL + Evergreen)
    - **MSC**: Operating independently (world's largest solo operator)
    """)
    
    # ============================================================================
    # SECTION 5: Economics of Vessel Size
    # ============================================================================
    
    st.markdown('<p class="section-header">Economics of Scale: Why Bigger is (Usually) Better</p>', unsafe_allow_html=True)
    
    st.markdown("""
    The dramatic growth in vessel sizes is driven by powerful economic incentives. Let's examine the 
    cost structure and how it changes with vessel size.
    """)
    
    # Cost comparison data
    cost_comparison = pd.DataFrame({
        'Vessel Size (TEU)': [1000, 3000, 5000, 8000, 12000, 18000, 24000],
        'Cost per TEU (Index)': [100, 68, 52, 38, 28, 18, 16],
        'Crew Size': [15, 20, 22, 24, 25, 25, 25],
        'Fuel per TEU (Index)': [100, 75, 62, 51, 43, 38, 37],
        'Port Cost per TEU (Index)': [100, 45, 33, 25, 20, 17, 15],
        'Capital Cost per TEU (Index)': [100, 70, 58, 47, 40, 35, 34]
    })
    
    # Cost savings visualisation
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=cost_comparison['Vessel Size (TEU)'],
        y=cost_comparison['Cost per TEU (Index)'],
        mode='lines+markers',
        name='Total Cost per TEU',
        line=dict(color='#EF4444', width=4),
        marker=dict(size=12),
        fill='tozeroy',
        fillcolor='rgba(239, 68, 68, 0.2)'
    ))
    
    fig.update_layout(
        title={
            'text': 'Economies of Scale: Cost per TEU vs Vessel Size',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': '#1F2937'}
        },
        xaxis_title="Vessel Size (TEU)",
        yaxis_title="Cost per TEU (Indexed to 1,000 TEU = 100)",
        height=450,
        plot_bgcolor='white',
        xaxis=dict(gridcolor='#E5E7EB'),
        yaxis=dict(gridcolor='#E5E7EB', range=[0, 110])
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    **Cost Components Breakdown:**
    
    **Fixed Costs (Don't Scale with Size):**
    - **Crew salaries**: 25 crew whether 5,000 or 24,000 TEU
      - Average crew cost: ~$5 million/year (all ranks, provisions, insurance)
      - 5,000 TEU: $1,000 per TEU; 24,000 TEU: $208 per TEU
    - **Insurance**: Hull & machinery, P&I (relatively flat, slight increase with size)
    - **Administration**: Port agency, documentation, booking systems
    - **Port dues**: Based primarily on vessel gross tonnage, not cargo volume
      - Typical major port call: $50,000-100,000
    
    **Variable Costs (Scale Less Than Proportionally):**
    - **Fuel**: Larger vessels 30-40% more efficient per TEU
      - Hull efficiency improves with size (lower resistance per ton)
      - Can operate at lower speeds profitably (slow steaming)
      - Example: 5,000 TEU at 20 knots = ~50 tons/day; 24,000 TEU at 18 knots = ~180 tons/day
      - Per TEU: 10 kg/day (5K vessel) vs 7.5 kg/day (24K vessel)
    - **Capital cost**: Building cost doesn't scale linearly
      - 5,000 TEU vessel: ~$60 million ($12,000/TEU)
      - 24,000 TEU vessel: ~$200 million ($8,333/TEU) - 30% lower per TEU
    - **Maintenance**: Slightly higher absolute cost, much lower per TEU
    
    **Semi-Variable Costs:**
    - **Canal tolls**: Based on vessel size (not cargo), but spread over more containers
      - Suez Canal: ~$600,000-900,000 per transit
      - 5,000 TEU: $120-180/TEU; 24,000 TEU: $25-38/TEU
    - **Container handling**: Linear with volume, but negotiated discounts at scale
    
    **Result - Cost per TEU per Voyage Example:**
    - **1,000 TEU vessel**: ~$1,000/TEU (total voyage cost ~$1M)
    - **5,000 TEU vessel**: ~$520/TEU (total voyage cost ~$2.6M)
    - **18,000 TEU vessel**: ~$180/TEU (total voyage cost ~$3.2M)
    - **24,000 TEU vessel**: ~$160/TEU (total voyage cost ~$3.8M)
    - **Savings**: 84% cost reduction per TEU (1,000 → 24,000 TEU)
    
    **The Catch (Why Bigger Isn't Always Better):**
    - Need **high utilisation** (85-90%+ load factor) to realise savings
    - Requires massive cargo volumes on route (20,000+ TEU per sailing)
    - Limited ports can handle mega vessels (~20-30 ports globally)
    - Higher risk if vessel delayed or breaks down (concentration risk)
    - **2024-2025 reality**: Overcapacity means many mega vessels operating at 70-80% utilisation
    - **Diminishing returns**: Cost savings flatten above 18,000-20,000 TEU
    - **Market volatility**: 2024-2025 saw periods of significant oversupply
    """)
    
    # ============================================================================
    # SECTION 6: Stowage Planning Fundamentals
    # ============================================================================
    
    st.markdown('<p class="section-header">Vessel Stowage Planning: The Complex 3D Puzzle</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Stowage planning—determining where each container goes on the vessel—is a complex multi-objective 
    optimisation problem with numerous competing constraints. Modern stowage planning software uses AI 
    algorithms to find near-optimal solutions in minutes.
    """)
    
    st.markdown('<p class="subsection-header">1. Stability and Safety (Primary Constraint)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Centre of Gravity (G):**
    - Vertical position must be low enough for stability
    - **Too high**: Risk of capsizing (low GM)
    - **Too low**: Excessive stress on hull, uncomfortable motion
    - Target: Optimise for safety margin while maximising cargo
    
    **Metacentric Height (GM):**
    - Measure of vessel's initial stability
    - **GM = (M − G)** where M = metacentre, G = centre of gravity
    - **Too low (<0.5m)**: Unstable, risk of capsizing
    - **Too high (>3m)**: Stiff, rapid rolling, cargo damage, crew discomfort
    - **Target**: Typically 1.0-2.0m for container ships
    - Calculated in real-time by loading computer
    
    **Longitudinal Balance (Trim):**
    - Weight distribution bow to stern
    - Affects:
      - Propeller immersion (efficiency)
      - Wave resistance (fuel consumption)
      - Maneuverability
    - **Target**: Slightly aft trim (stern lower) for optimal propeller performance
    - Typical: 0.5-2.0m difference bow-stern draft
    
    **Transverse Balance (List):**
    - Weight distribution port to starboard
    - Must be zero or minimal (<0.5 degrees)
    - Even slight list affects:
      - Crane operations (containers not vertical)
      - Stability (reduces effective GM)
      - Fuel consumption (asymmetric resistance)
    
    **Stress Limits:**
    - **Hogging**: Bow and stern lower than amidships (too much weight in middle)
    - **Sagging**: Bow and stern higher than amidships (too much weight at ends)
    - Both can crack the hull if limits exceeded
    - Loading computer checks against maximum allowable stress
    
    **Practical Implications:**
    - Computer software calculates all parameters automatically
    - Stowage planner adjusts if limits exceeded
    - May need to move containers between bays to balance loads
    - **Real-time monitoring**: Loading computer updates stability with each container loaded
    - **Safety margin**: Always maintain buffer above minimum GM requirements
    """)
    
    st.markdown('<p class="subsection-header">2. Destination Sequence (Operational Efficiency)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **The Fundamental Rule:**
    Containers for **Port 1** must be accessible before **Port 2** containers.
    
    **Vertical Stacking Principle:**
    - **Bottom tiers**: Containers for later ports (Port 3, 4, 5...)
    - **Top tiers**: Containers for earlier ports (Port 1, 2)
    - Prevents "overstowage" (later port cargo blocking earlier port cargo)
    
    **Re-stow Operations:**
    - Moving containers between ports to access buried cargo
    - **Cost**: 30-60 minutes crane time per re-stow
    - **Target**: Zero re-stows (perfect planning)
    - **Reality**: 2-5% of containers typically require re-stow
    - **Impact**: Delays vessel, costs terminal ~$200-400 per re-stow
    
    **Multi-Port Voyage Example:**
    - Route: Singapore → Port Klang → Colombo → Suez → Rotterdam → Hamburg → Felixstowe
    - **Felixstowe cargo**: Top tiers (discharge last)
    - **Rotterdam cargo**: Mid tiers  
    - **Suez cargo**: Bottom tiers (discharge first)
    - **Colombo cargo**: Even lower
    - **Singapore cargo**: May not load any (transhipment hub)
    
    **Complexity:**
    - 7-port voyage with 15,000 containers = **billions of possible stowage combinations**
    - Optimisation objective: Minimise re-stows while respecting all other constraints
    - **AI/ML algorithms** (genetic algorithms, simulated annealing) find near-optimal solutions
    """)
    
    st.markdown('<p class="subsection-header">3. Structural Weight Limits</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Stack Weight:**
    - Each bay has maximum weight per vertical stack
    - Typically: 150-350 tonnes depending on location
    - Stronger positions: Near pillars, over structural members
    - Weaker positions: Over holds without direct support
    
    **Deck Load:**
    - Maximum weight per unit area of deck
    - Hatch covers have specific load ratings
    - **Above deck**: Generally more restrictive than below deck
    
    **Bay Limits:**
    - Total weight per bay (longitudinal section)
    - Prevents local overstressing of hull
    - Typical: 400-800 tonnes per 40ft bay position
    
    **Container Stacking:**
    - Bottom containers support weight of all above
    - ISO containers rated for 9-high stacking when fully loaded
    - Empty containers much weaker (can't support heavy load on top)
    - **Rule**: Heavy containers on bottom, light/empty on top
    
    **Practical Implications:**
    - Computer software calculates all loads automatically
    - Stowage planner adjusts if limits exceeded
    - May need to move containers between bays to balance loads
    - **Colour-coding**: Planning software shows overweight positions in red
    """)
    
    st.markdown('<p class="subsection-header">4. Container Type Compatibility</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Dangerous Goods (DG) Segregation:**
    - **IMDG Code**: Specifies minimum separation distances by class
    - **Class 1 (Explosives)** must be far from **Class 3 (Flammables)**
    - **Class 5 (Oxidizers)** can't be near **Class 4 (Flammable Solids)**
    - Separation: Typically 3-6 metres (1-3 bays) depending on classes
    - Some DG must be on deck only (Class 1, certain Class 2)
    - **Documentation**: Every DG container requires detailed manifest
    
    **Reefer (Refrigerated) Containers:**
    - Must be within reach of power supply points (**reefer plugs**)
    - Limited number of plugs per bay (typically 20-40% of bay capacity)
    - **Power requirements**: 440V 3-phase, 10-15 kW per reefer
    - Continuous power needed throughout voyage (40-60 days)
    - **Below deck**: Dedicated reefer holds with power
    - **On deck**: Specific rows/tiers with reefer plugs
    - **Monitoring**: Remote temperature monitoring from bridge
    - **Priority**: Breakdown requires immediate action (cargo spoilage)
    
    **Out-of-Gauge (OOG) Containers:**
    - Exceed standard dimensions (overwidth, overheight, overlength)
    - **Cannot stack containers on top** (safety risk)
    - Placed in specific positions with clearance:
      - Overheight: Top tier only
      - Overwidth: Edge positions (don't interfere with cell guides)
      - Overlength: Special flat racks in designated positions
    - Often require special lashing/securing (additional labour)
    - **Crane impact**: Slower handling (careful positioning)
    
    **Empty Containers:**
    - Very light (2-4 tonnes tare weight)
    - Placed on **top tiers** when possible
    - **Structural limitation**: Empty containers can't support heavy containers on top
    - Used strategically to balance weight distribution
    - **Visibility**: Easy to identify (doors visible, lighter colour when lifted)
    - Sometimes used as "spacers" to achieve proper weight distribution
    
    **20ft vs 40ft Mixing:**
    - Cell guides designed for both (cellular structure)
    - 20ft containers: Can stack 2 × 20ft in one 40ft cell
    - Flexibility allows optimisation
    - **Preference**: 40ft containers (easier handling, fewer moves)
    - **Reality**: Modern trades 80-85% are 40ft containers
    """)
    
    st.markdown('<p class="subsection-header">The Stowage Planning Process (48-72 Hours Before Arrival)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    **Step 1: Receive Container List (Load List)**
    - Shipping line provides list via EDI (Electronic Data Interchange)
    - Details for each container:
      - Container number (ISO 6346)
      - Size (20ft/40ft/45ft)
      - Type (dry/reefer/OOG/tank)
      - Weight (SOLAS VGM - verified gross mass)
      - Destination port
      - Special requirements (DG class, reefer temperature, etc.)
    - Typical mega vessel: 8,000-15,000 containers to load/discharge
    
    **Step 2: Understand Vessel Configuration**
    - Vessel's bay plan (capacity, reefer plugs, structural limits)
    - Current cargo onboard (if mid-voyage)
    - Remaining ports and discharge plans
    - Weather forecast (affects stability requirements)
    
    **Step 3: Automated Optimisation (AI/ML Software)**
    - Input: Container list + vessel constraints + objectives
    - **Optimisation objectives** (weighted priorities):
      1. Safety (stability, structural limits) - **non-negotiable**
      2. Zero re-stows - **high priority**
      3. Crane productivity (minimise travel) - **medium priority**
      4. Balance reefer plugs usage - **medium priority**
      5. Group by shipping line - **low priority**
    - Algorithm: Genetic algorithm or simulated annealing
    - Output: Recommended stowage plan (every container position)
    - Computation time: 5-30 minutes for full plan
    
    **Step 4: Manual Review and Adjustment**
    - Experienced stowage planner reviews AI output
    - Checks for practical issues:
      - Port-specific restrictions
      - Customer requests (airline containers together, etc.)
      - Historical problems (certain positions problematic)
      - Weather forecast (heavy weather = lower stacks)
    - Adjusts as needed (software recalculates stability)
    
    **Step 5: Generate Final Documents**
    - **Bay plans**: Visual representation showing every container
    - **Loading sequence**: Order for crane operations
    - **Stability report**: GM, trim, stress calculations
    - **Special cargo list**: DG manifest, reefer monitoring plan
    - **Crane work list**: Instructions for each crane operator
    
    **Step 6: Distribute to Operations**
    - Sent to vessel (Captain must approve)
    - Sent to terminal (crane operators, planners)
    - Any deviations during loading **require plan update**
    - Real-time monitoring: Terminal Operating System tracks actual vs planned
    
    **Modern Technology (2024-2025):**
    - **AI-powered optimisation**: 95%+ optimal solutions
    - **Digital twin**: 3D visualisation of entire vessel
    - **Real-time updates**: Plan adjusts as containers arrive
    - **Cloud-based**: Shore planners and vessel collaborate in real-time
    - **Predictive analytics**: Forecast issues before they occur
    - **Integration**: Connected to Terminal Operating System, shipping line systems
    """)
    
    # ============================================================================
    # SECTION 7: Technology and Environmental Evolution
    # ============================================================================
    
    st.markdown('<p class="section-header">Technology Evolution: Efficiency and Sustainability (2024-2025)</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Modern container vessels incorporate advanced technologies focused on fuel efficiency, emissions reduction, 
    and operational optimisation. The industry is undergoing a major transition to meet IMO decarbonisation targets.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Propulsion and Efficiency:**
        - **Slow steaming**: 18-20 knots vs 25+ knots historically
          - **Fuel savings**: 30-50% (fuel consumption cubic with speed)
          - **Example**: 25 knots → 18 knots = 60% fuel reduction
          - **Trade-off**: +20-30% transit time
          - **2024 practice**: Most vessels operating at optimised slow speed
        - **Optimised hull designs**: 
          - Bulbous bow (reduces wave resistance)
          - Air lubrication (bubble system reduces friction 5-10%)
          - Hull coatings (reduce bio-fouling, maintain smoothness)
        - **Efficient engines**: 
          - Two-stroke diesel (most common, 45-50% efficiency)
          - Electronic control (optimise fuel injection)
          - Waste heat recovery (generate electricity from exhaust, 5-8% fuel savings)
        - **Automation**: 
          - Unmanned engine rooms (reduce crew, improve safety)
          - Remote monitoring (shore-based support)
          - Predictive maintenance (IoT sensors predict failures)
        
        **Operational Technologies:**
        - **Weather routing**: 
          - AI-optimised routes for fuel efficiency
          - Avoid heavy weather (safety + fuel savings)
          - Savings: 3-8% fuel consumption
        - **GPS and AIS**: 
          - Precise navigation (reduce deviation)
          - Automatic vessel tracking (compliance, safety)
        - **Voyage optimisation**: 
          - Just-in-time arrival (reduce port waiting time)
          - Speed optimisation (balance fuel vs schedule)
        - **Virtual models**: 
          - Digital twin simulation
          - Training simulators for crew
        """)
    
    with col2:
        st.markdown("""
        **Environmental Technologies (IMO 2020/2050 Compliance):**
        - **Scrubbers (SOx removal)**:
          - Remove sulphur from exhaust (IMO 2020: 0.5% sulphur limit)
          - ~2,000 vessels equipped as of 2024
          - Cost: $2-5 million installation
          - Allows use of cheaper high-sulphur fuel oil (HSFO)
          - **Trade-off**: Increased CO₂ by 1.5-3% (energy penalty)
        - **LNG dual-fuel engines**:
          - Can burn LNG or conventional fuel
          - **20-25% less CO₂** than heavy fuel oil
          - Near-zero SOx and particulate matter
          - **Challenge**: Methane slip (potent greenhouse gas)
          - **2024 status**: ~7% of global fleet LNG-capable
          - **Examples**: Several CMA CGM vessels (23,000 TEU LNG-powered)
        - **Methanol dual-fuel**:
          - Maersk pioneering (world's first methanol-powered vessels, 2023+)
          - Can use green methanol (renewable) = near-zero emissions
          - Easier to handle than LNG (liquid at ambient temperature)
          - **Challenge**: Limited green methanol production
          - **2024 status**: <1% of fleet, rapidly growing
        - **Ammonia-ready engines**:
          - Development stage (commercial deployment 2025-2028)
          - Zero-carbon fuel when green (from renewable hydrogen)
          - **Challenges**: Toxic, corrosive, low energy density
          - Several major engine manufacturers developing (MAN, Wärtsilä)
        
        **Future Technologies (2025-2030):**
        - **Hydrogen fuel cells**: Very long term (2035+)
        - **Battery hybrid**: Short-sea routes only (energy density limits)
        - **Wind-assisted propulsion**: Rotor sails, kites (5-20% fuel savings)
        - **Solar panels**: Auxiliary power (reduce generator usage)
        - **Carbon capture**: Onboard CO₂ capture systems (development stage)
        """)
    
    st.markdown("""
    **Regulatory Landscape (2024-2025):**
    
    **IMO 2020 (Implemented January 1, 2020):**
    - Global sulphur cap: **0.5% (down from 3.5%)**
    - Compliance options:
      - Use low-sulphur fuel oil (LSFO/VLSFO) - most common
      - Install scrubbers + use high-sulphur fuel oil - ~2,000 vessels
      - Use alternative fuels (LNG, methanol) - growing
    - **Impact**: Successfully reduced SOx emissions by ~80% globally
    
    **IMO GHG Strategy (2023, Revised):**
    - **2030 target**: 40% carbon intensity reduction (vs 2008)
    - **2050 target**: Net-zero greenhouse gas emissions
    - **2040 onwards**: Requires zero/near-zero GHG fuels
    - **Challenge**: 80-90% of 2050 fleet already built or on order
    
    **FuelEU Maritime (EU, Entered Force January 1, 2025):**
    - Mandatory GHG intensity limits for ships calling EU ports
    - Phases in progressively stricter limits 2025-2050
    - **Penalty**: Pay per ton of CO₂ equivalent exceeded
    - **Impact**: Forces earlier adoption of low-carbon fuels
    
    **EU Emissions Trading System (EU ETS, Extended to Shipping 2024):**
    - Ships pay for CO₂ emissions in EU waters
    - **Price**: ~€80-100 per ton CO₂ (2024-2025)
    - **Cost impact**: +$1-2 million per Asia-Europe voyage for mega vessel
    - **Purpose**: Create economic incentive for fuel efficiency
    
    **US Port Fees (Proposed 2025):**
    - Potential fees on Chinese-built vessels calling US ports
    - **Impact**: May reshape fleet deployment patterns
    - **Exposure**: COSCO and CMA CGM most affected, MSC and Maersk less
    
    **Practical Reality (2024-2025):**
    - Most vessels still run on conventional fuel oil (VLSFO)
    - Alternative fuels face challenges:
      - **Cost**: E-methanol/e-ammonia 2× conventional fuel cost
      - **Availability**: Limited bunkering infrastructure
      - **Risk**: Uncertain future regulatory landscape
    - **Slow progress**: Only ~8-10% of fleet uses alternative fuels (mostly LNG)
    - **Orderbook shift**: 40-50% of new orders are dual-fuel capable
    - **Timeline challenge**: 2050 net-zero requires massive fleet renewal by 2030-2035
    """)
    
    # ============================================================================
    # SECTION 8: Key Takeaways
    # ============================================================================
    
    st.markdown('<p class="section-header">Key Takeaways</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Vessel Anatomy:**
        - Bow (front), Stern (back), Port (left/red), Starboard (right/green)
        - Bay-Row-Tier 3D positioning system (odd/even numbering)
        - Holds (below deck), Deck (above), Superstructure, Bridge
        
        **Evolution:**
        - 1956: 500 TEU (Ideal X, first container ship)
        - 2025: 24,346 TEU (MSC Irina, current largest)
        - **49× capacity increase** in 69 years
        - Growth plateaued at ~24,000 TEU (practical maximum)
        
        **Classifications:**
        - Feeder: <3,000 TEU (regional routes)
        - Panamax: ~4,500 TEU (old Panama Canal limit, obsolete)
        - New-Panamax: ~14,500 TEU (new Panama Canal, 2016+)
        - ULCS: 18,000-24,000 TEU (mega vessels, Asia-Europe only)
        - Megamax: 21,000-24,346 TEU (maximum practical size)
        
        **Current Fleet (Dec 2025):**
        - Total capacity: 33.6 million TEU (+7.2% from 2024)
        - MSC dominance: 7.1M TEU (19.9% market share)
        - Top 3: MSC (7.1M), Maersk (4.6M), CMA CGM (4.1M)
        - Orderbook: 10+ million TEU (largest in history)
        """)
    
    with col2:
        st.markdown("""
        **Economics of Scale:**
        - 24,000 TEU vessel: **84% lower cost per TEU** vs 1,000 TEU
        - Fixed costs (crew $5M/year, port dues, insurance) don't scale
        - Variable costs (fuel) scale sub-linearly (hull efficiency)
        - **Catch**: Requires 85-90% utilisation, massive cargo volumes
        - 2024-2025: Overcapacity concerns, 70-80% utilisation common
        
        **Stowage Planning:**
        - **Safety**: Stability (GM 1-2m), balance, structural limits
        - **Destination**: Later ports bottom, earlier ports top (zero re-stows)
        - **Weight**: Heavy bottom, empties top, respect stack limits
        - **Compatibility**: DG segregation, reefer power, OOG clearance
        - **Technology**: AI algorithms find near-optimal solutions (5-30 min)
        
        **Environmental Transition (2024-2025):**
        - IMO 2020: 0.5% sulphur cap (implemented, successful)
        - IMO 2050: Net-zero target (major challenge)
        - Slow steaming: 18-20 knots (30-50% fuel savings)
        - Alternative fuels: 7% LNG, <1% methanol, ammonia developing
        - **Reality**: 80-90% still conventional fuel, slow transition
        - FuelEU Maritime (2025): Accelerating decarbonisation pressure
        
        **2024-2025 Challenges:**
        - Red Sea crisis: Mega vessels avoiding Suez 20+ months
        - Overcapacity: Fleet growing faster than trade
        - Freight volatility: Shanghai index +149% in 2024
        - Regulatory uncertainty: Multiple regional schemes
        """)
    
    st.markdown("""
    <div class="insight-box">
    <strong>🔍 Bottom Line:</strong> Container vessels have grown 49× in capacity since 1956 (500 → 24,346 TEU), 
    driven by powerful economies of scale (**84% cost reduction per TEU**). Modern mega vessels (20,000+ TEU) 
    require sophisticated infrastructure available at only 20-30 ports globally. The global fleet reached 33.6M 
    TEU capacity in December 2025, dominated by MSC (7.1M TEU, 19.9% market share). 
    <br><br>
    Stowage planning is a complex 3D optimisation problem balancing **safety** (stability, structural limits), 
    **efficiency** (zero re-stows, crane productivity), and **compatibility** (DG segregation, reefer power). 
    Modern AI algorithms solve plans in minutes that would take humans hours.
    <br><br>
    <strong>2024-2025 Context:</strong> The industry faces simultaneous challenges: Red Sea disruptions forcing 
    longer routes (+5% emissions), overcapacity reducing profitability, and urgent decarbonisation requirements 
    (IMO 2050 net-zero target). While alternative fuels are developing (7% LNG-capable, methanol pioneering), 
    the transition is slow—most vessels still run on conventional fuel. The 2025 orderbook (10M+ TEU) risks 
    further overcapacity but includes more dual-fuel capable vessels, signaling gradual environmental progress.
    </div>
    """, unsafe_allow_html=True)
    
    # ============================================================================
    # Navigation
    # ============================================================================
    
    st.markdown("---")
    st.markdown("### 📚 Continue Learning")
    st.markdown("""
    **Next Topic:** 🌍 Global Shipping & Alliances - Understand how shipping lines have consolidated into 
    alliances (Ocean Alliance, Gemini Cooperation, Premier Alliance) controlling 80%+ of global capacity, 
    and how hub-and-spoke networks enable global connectivity through major transhipment hubs like Singapore.
    """)
