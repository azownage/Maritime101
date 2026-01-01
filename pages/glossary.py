import streamlit as st
import pandas as pd

def show():
    st.markdown('<p class="main-header">📚 Comprehensive Maritime Glossary</p>', unsafe_allow_html=True)

        search = st.text_input("🔍 Search glossary", placeholder="Enter term or keyword...")

        # Extended glossary with 100+ terms
        glossary = {
            'AGV': 'Automated Guided Vehicle - Driverless battery-electric vehicles for horizontal transport',
            'Alliance': 'Partnership between shipping lines to share vessels, routes, and terminal facilities',
            'Apron': 'Paved area immediately behind quay where quay cranes operate',
            'Bay': 'Cross-sectional slot on vessel where containers are stowed',
            'Bay Plan': 'Diagram showing exact position of every container on a vessel',
            'Beam': 'Width of a vessel',
            'Berth': 'Designated location at quay where vessel docks',
            'BOA': 'Berth on Arrival - Percentage of vessels that berth without waiting at anchorage',
            'Call': 'A vessel visit to a port',
            'Cascading': 'Process where older vessels move from major to secondary routes',
            'CI': 'Container Index - Ratio of actual to guaranteed productivity',
            'CITOS': "Container IT Operating System - PSA's terminal operating system",
            'Consolidation': 'Combining multiple shipments into full container',
            'Container': 'Standardized steel box for cargo (20ft, 40ft, 45ft)',
            'Consignee': 'Party receiving goods (importer)',
            'Consignor': 'Party sending goods (shipper/exporter)',
            'Draft': 'Depth of water vessel needs to float',
            'Dwell Time': 'Average time container stays in terminal',
            'Empty': 'Container with no cargo',
            'ETA': 'Estimated Time of Arrival',
            'ETD': 'Estimated Time of Departure',
            'Feeder': 'Smaller vessel distributing containers from hubs to regional ports',
            'Freight Forwarder': 'Company arranging cargo shipment',
            'GCR': 'Gross Crane Rate - Total moves per crane hour including delays',
            'Hinterland': 'Inland area served by port',
            'Hub Port': 'Major port where containers transfer between mainline and feeder vessels',
            'IMO': 'International Maritime Organization OR unique vessel ID number',
            'Laden': 'Container carrying cargo',
            'Lashing': 'Securing containers with twist locks and rods',
            'LOA': 'Length Overall - Total vessel length',
            'Mainline': 'Major shipping route (Asia-Europe, Trans-Pacific)',
            'Manifest': 'List of all cargo on vessel',
            'Mother Vessel': 'Large vessel on mainline route',
            'NCR': 'Net Crane Rate - Moves per hour excluding breaks',
            'OHBC': 'Over-Head Bridge Crane - Yard crane type on elevated rails',
            'Panamex': 'Vessel size able to transit Panama Canal (max ~5,000 TEU)',
            'PM': 'Prime Mover - Terminal tractor pulling containers',
            'POD': 'Port of Discharge - Where container unloaded',
            'POL': 'Port of Loading - Where container loaded',
            'PORTNET': "Singapore's port digital platform",
            'QC': 'Quay Crane - Large crane loading/unloading vessels',
            'Quay': 'Waterfront where vessels berth',
            'Reefer': 'Refrigerated container for perishables',
            'Reshuffle': 'Moving containers to access target container',
            'RMG': 'Rail-Mounted Gantry - Yard crane on fixed rails',
            'RTG': 'Rubber-Tyred Gantry - Most common yard crane, on tires',
            'Shipper': 'Party sending goods (exporter)',
            'Slot': 'Space for one TEU on vessel or in yard',
            'Stow Plan': 'Plan for loading containers onto vessel',
            'Straddle Carrier': 'Mobile equipment that straddles and lifts containers',
            'STS': 'Ship-to-Shore crane (same as Quay Crane)',
            'TEU': 'Twenty-foot Equivalent Unit - Standard container measure',
            'TOS': 'Terminal Operating System - Software managing operations',
            'Transshipment': 'Container transferred between vessels at intermediate port',
            'Tugboat': 'Small powerful boat assisting large vessels',
            'Turnaround Time': 'Total time from vessel arrival to departure',
            'ULCS': 'Ultra Large Container Ship - Vessels over 14,500 TEU',
            'Vessel Sharing': 'Multiple carriers sharing space on same vessel',
            'VLCS': 'Very Large Container Ship - Vessels 8,000-14,500 TEU',
            'Yard': 'Storage area for containers between vessel and gate'
        }

        if search:
            filtered = {k:v for k,v in glossary.items() 
                       if search.lower() in k.lower() or search.lower() in v.lower()}
        else:
            filtered = glossary

        if filtered:
            for term, defn in sorted(filtered.items()):
                with st.expander(f"**{term}**"):
                    st.write(defn)
        else:
            st.warning(f"No results for '{search}'")

        st.markdown("---")
        st.markdown("### Quick Reference Tables")

        tab1, tab2, tab3 = st.tabs(["Container Sizes", "Vessel Classes", "Equipment Types"])

        with tab1:
            sizes = pd.DataFrame({
                'Type': ['20ft Standard', '40ft Standard', '40ft High Cube'],
                'Length': ['6.1m', '12.2m', '12.2m'],
                'Height': ['2.6m', '2.6m', '2.9m'],
                'TEU': ['1', '2', '2']
            })
            st.dataframe(sizes, use_container_width=True, hide_index=True)

        with tab2:
            vessels = pd.DataFrame({
                'Class': ['Feeder', 'Panamax', 'Post-Panamax', 'VLCS', 'ULCS'],
                'TEU Range': ['100-3,000', '3,000-5,000', '5,000-10,000', '10,000-18,000', '18,000+'],
                'LOA': ['100-200m', '250-300m', '280-350m', '380-400m', '395-400m+']
            })
            st.dataframe(vessels, use_container_width=True, hide_index=True)

        with tab3:
            equipment = pd.DataFrame({
                'Equipment': ['Quay Crane', 'RTG', 'RMG', 'AGV', 'Prime Mover'],
                'Function': ['Vessel loading', 'Yard stacking', 'Auto yard', 'Auto transport', 'Manual transport'],
                'Cost': ['Very High', 'Medium', 'Medium-High', 'Medium', 'Low']
            })
            st.dataframe(equipment, use_container_width=True, hide_index=True)