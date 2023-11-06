# ---------------------------- imports ---------------------------- #
import streamlit as st
import pandas as pd
import sys

sys.path.append("../models")
from ordinal_dummies import *
import joblib

# ----------------------------------------------- #
# ---------------------------- Streamlit configs ---------------------------- #
st.set_page_config(page_title="Earthquake damage",
                   page_icon="⚒",
                   layout="wide")

st.title('Earthquake damage')
st.info('Machine Learning Classification Project')

# ---------------------------- Load ---------------------------- #
model = joblib.load('../models/model.h5')
scaler = joblib.load('../models/scaler.h5')

# ---------------------------- Technical solution ---------------------------- #
technical_solution_proposed = st.selectbox("Technical solution proposed", ['Reconstruction', 'Major repair', 'Minor repair', 'No need'])

if technical_solution_proposed == 'Reconstruction':
    technical_solution_proposed_reconstruction = 1
    technical_solution_proposed_major_repair = 0
    technical_solution_proposed_minor_repair = 0
    technical_solution_proposed_no_need = 0
elif technical_solution_proposed == 'Major repair' :
    technical_solution_proposed_reconstruction = 0
    technical_solution_proposed_major_repair = 1
    technical_solution_proposed_minor_repair = 0
    technical_solution_proposed_no_need = 0
elif technical_solution_proposed == 'Minor repair' :
    technical_solution_proposed_reconstruction = 0
    technical_solution_proposed_major_repair = 0
    technical_solution_proposed_minor_repair = 1
    technical_solution_proposed_no_need = 0
else:
    technical_solution_proposed_reconstruction = 0
    technical_solution_proposed_major_repair = 0
    technical_solution_proposed_minor_repair = 0
    technical_solution_proposed_no_need = 1
# ------------------------------------------------------------------------------- #

# ---------------------------- Condition post eq ---------------------------- #
condition_post_eq = st.selectbox("Condition post eq", ['Damaged-Not used', 'Damaged-Rubble unclear', 'Damaged-Used in risk',
                                                        'Damaged-Repaired and used', 'Damaged-Rubble clear', 'Not damaged',
                                                        'Damaged-Rubble Clear-New building built', 'Covered by landslide'])

if condition_post_eq == 'Damaged-Not used':
    condition_post_eq_not_damaged = 0
    condition_post_eq_damaged_rubble_unclear = 0
    condition_post_eq_damaged_not_used = 1
    condition_post_eq_damaged_rubble_clear = 0
    condition_post_eq_damaged_used_in_risk = 0
    condition_post_eq_damaged_repaired_and_used = 0
elif condition_post_eq == 'Damaged-Rubble unclear' :
    condition_post_eq_not_damaged = 0
    condition_post_eq_damaged_rubble_unclear = 1
    condition_post_eq_damaged_not_used = 0
    condition_post_eq_damaged_rubble_clear = 0
    condition_post_eq_damaged_used_in_risk = 0
    condition_post_eq_damaged_repaired_and_used = 0
elif condition_post_eq == 'Damaged-Used in risk' :
    condition_post_eq_not_damaged = 0
    condition_post_eq_damaged_rubble_unclear = 0
    condition_post_eq_damaged_not_used = 0
    condition_post_eq_damaged_rubble_clear = 0
    condition_post_eq_damaged_used_in_risk = 1
    condition_post_eq_damaged_repaired_and_used = 0
elif condition_post_eq == 'Damaged-Repaired and used':
    condition_post_eq_not_damaged = 0
    condition_post_eq_damaged_rubble_unclear = 0
    condition_post_eq_damaged_not_used = 0
    condition_post_eq_damaged_rubble_clear = 0
    condition_post_eq_damaged_used_in_risk = 0
    condition_post_eq_damaged_repaired_and_used = 1
elif condition_post_eq == 'Damaged-Rubble clear':
    condition_post_eq_not_damaged = 0
    condition_post_eq_damaged_rubble_unclear = 0
    condition_post_eq_damaged_not_used = 0
    condition_post_eq_damaged_rubble_clear = 1
    condition_post_eq_damaged_used_in_risk = 0
    condition_post_eq_damaged_repaired_and_used = 0
elif condition_post_eq == 'Not damaged':
    condition_post_eq_not_damaged = 1
    condition_post_eq_damaged_rubble_unclear = 0
    condition_post_eq_damaged_not_used = 0
    condition_post_eq_damaged_rubble_clear = 0
    condition_post_eq_damaged_used_in_risk = 0
    condition_post_eq_damaged_repaired_and_used = 0
elif condition_post_eq == 'Damaged-Rubble Clear-New building built':
    condition_post_eq_not_damaged = 0
    condition_post_eq_damaged_rubble_unclear = 0
    condition_post_eq_damaged_not_used = 0
    condition_post_eq_damaged_rubble_clear = 0
    condition_post_eq_damaged_used_in_risk = 0
    condition_post_eq_damaged_repaired_and_used = 0
else:
    condition_post_eq_not_damaged = 0
    condition_post_eq_damaged_rubble_unclear = 0
    condition_post_eq_damaged_not_used = 0
    condition_post_eq_damaged_rubble_clear = 0
    condition_post_eq_damaged_used_in_risk = 0
    condition_post_eq_damaged_repaired_and_used = 0
# ------------------------------------------------------------------------------- #

# ---------------------------- Numbers ---------------------------- #
count_floors_post_eq = st.number_input("Count floors post eq", min_value=0)
count_floors_pre_eq = st.number_input("Count floors pre eq", min_value=0)

lost_floors = count_floors_pre_eq - count_floors_post_eq
height_ft_pre_eq = st.number_input("Height ft pre eq", min_value=0)
height_ft_post_eq = st.number_input("Height ft post eq", min_value=0)

# Calculate lost_height based on provided conditions
if height_ft_post_eq <= height_ft_pre_eq:
    lost_height = height_ft_pre_eq - height_ft_post_eq
else:
    lost_height = 0

plinth_area_sq_ft = st.number_input('Plinth area sq ft', min_value=0)
age_building = st.number_input('Age building', min_value=0)
# ... (other inputs)

# ---------------------------- Has ---------------------------- #
has_superstructure_cement_mortar_brick = st.checkbox("Superstructure cement mortar brick")
has_superstructure_mud_mortar_stone = st.checkbox("Superstructure mud mortar stone")
has_superstructure_timber = st.checkbox("Superstructure timber")

# ---------------------------- ordinal ---------------------------- #
ground_floor_type_sele = st.selectbox("Ground floor type", ['Brick/Stone', 'Mud', 'RC', 'Timber'])
ground_floor_type = ground_floor_type_dummies[ground_floor_type_sele]

roof_type_sele = st.selectbox("Roof type", ['Bamboo/Timber-Heavy roof', 'Bamboo/Timber-Light roof', 'RCC/RB/RBC' ])
roof_type = roof_type_dummies[roof_type_sele]

land_surface_condition_sele = st.selectbox("Land surface condition", ['Flat', 'Moderate slope', 'Steep slope'])
land_surface_condition = land_surface_condition_dummies[land_surface_condition_sele]

position_sele = st.selectbox("Position", ['Attached-1 side', 'Attached-2 side', 'Attached-3 side', 'Not attached'])
position = position_dummies[position_sele]

# ------------------------------------------------------------------------------------- #

# ---------------------------- ID ---------------------------- #

district_id = st.number_input("District id", min_value=0)
vdcmun_id = st.number_input("Vdcmun id", min_value=0)
ward_id = st.number_input("Ward id", min_value=0)

# ------------------------------------------------------------------------------------- #

# ---------------------------- Foundation type ---------------------------- #
foundation_type = st.selectbox("Foundation type", ['Mud mortar-Stone/Brick', 'Bamboo/Timber', 'Cement-Stone/Brick', 'RC', 'Other'])
if foundation_type == 'Mud mortar-Stone/Brick':
    foundation_type_mud_mortar_stone_brick = 1
else:
    foundation_type_mud_mortar_stone_brick = 0

# ------------------------------------------------------------------------------------- #

# ---------------------------- Other floor type ---------------------------- #
other_floor_type = st.selectbox("Other floor type", ['TImber/Bamboo-Mud', 'Timber-Planck', 'Not applicable', 'RCC/RB/RBC'])

if other_floor_type == 'TImber/Bamboo-Mud':
    other_floor_type_timber_bamboo_mud = 1
else:
    other_floor_type_timber_bamboo_mud = 0

# ------------------------------------------------------------------------------------- #

data = [height_ft_post_eq, count_floors_post_eq, technical_solution_proposed_reconstruction, technical_solution_proposed_major_repair,
        technical_solution_proposed_minor_repair, lost_floors, lost_height, condition_post_eq_not_damaged, plinth_area_sq_ft,
        age_building, ward_id, technical_solution_proposed_no_need, condition_post_eq_damaged_not_used, vdcmun_id, height_ft_pre_eq,
        condition_post_eq_damaged_rubble_unclear, condition_post_eq_damaged_used_in_risk, condition_post_eq_damaged_repaired_and_used,
        has_superstructure_mud_mortar_stone, district_id, roof_type, condition_post_eq_damaged_rubble_clear, ground_floor_type,
        foundation_type_mud_mortar_stone_brick, position, land_surface_condition, has_superstructure_timber, count_floors_pre_eq,
        other_floor_type_timber_bamboo_mud, has_superstructure_cement_mortar_brick]

# Make predictions
data_scaled = scaler.transform([data])

# Make predictions
prediction = model.predict(data_scaled)
st.write(f'The predicted class is : {prediction[0]}')



# ------ Hide streamlit style ------ #
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)