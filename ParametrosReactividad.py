import streamlit as st
import pandas as pd
import math 

st.title("Parámetros de reactividad")

st.write("Bienvenido. Este programa te calculara parámetros de reactividad")

seleccion = st.selectbox("Seleccione una opción: ", ["Reactividad", "Visualizacion"])

if seleccion == "Reactividad":
  with st.form(key='calc_react'):
    st.subheader('Hartress')
    ht = st.number_input("Hartress: ", format="%.4f", step=1e-4)
    ht0 = st.number_input("Hartress 0: ", format="%.4f", step=1e-4)
    ht1p = st.number_input("Hartress +1: ", format="%.4f", step=1e-4)
    ht1m = st.number_input("Hartress -1: ", format="%.4f", step=1e-4)
    st.subheader('Nucleofilicidad')
    st.subheader('Nucleofilicidad')
    homo = st.number_input("HOMO:", format="%.4f", step=1e-4)
    lumo = st.number_input("LUMO: ", format="%.4f", step=1e-4)
    homo_o = st.number_input("HOMO (O):", format="%.4f", step=1e-4)
    lumo_o = st.number_input("LUMO (V): ", format="%.4f", step=1e-4)

    calcular = st.form_submit_button('Calcular')
 
 
  if calcular:
    eV0 = ht0 * 27.2116
    eV1p = ht1p * 27.2116
    eV1m = ht1m * 27.2116
  
    kcal = str(ht*627.5)

    A = eV0-eV1m
    I = eV1p - eV0

    n = (I-A)/2
    u = (I+A)/2
    w = (pow(u,2))/(2*n)


    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="H 0", value=round(ht0,5))
    col2.metric(label="H -1", value=round(ht1m,5))
    col3.metric(label="H +1", value=round(ht1p,5))
    col4.metric(label="kCal/mol", value=kcal)

    col1, col2, col3 = st.columns(3)
    col1.metric(label="eV 0", value=str(round(eV0,5)))
    col2.metric(label="eV -1", value=str(round(eV1p,5)))
    col3.metric(label="eV +1", value=str(round(eV1m,5)))
  
    st.subheader("Aproximación de energias")

    col1, col2 = st.columns(2)
    col1.metric(label="Afinidad electrónica", value=str(round(A,5)))
    col2.metric(label="Potencial de ionización", value=str(round(I,5)))

    col1, col2, col3 = st.columns(3)
    col1.metric(label="Dureza", value=str(n))
    col2.metric(label="Electronegatividad", value=str(round(u,5)))
    col3.metric(label="Electrofilicidad", value=str(round(w,5)))

    st.subheader("Aproximación Orbital")

    A_orb = -27*lumo
    I_orb = -27*homo

    n_orb = (I_orb - A_orb) / 2
    u_orb = (I_orb + A_orb) / 2
    w_orb = pow(u_orb, 2) / (2 * n_orb)
  
    col1, col2 = st.columns(2)
    col1.metric(label="Afinidad electrónica", value=str(round(A_orb,5)))
    col2.metric(label="Potencial de ionización", value=str(round(I_orb,5)))

    col1, col2, col3 = st.columns(3)
    col1.metric(label="Dureza", value=str(round(n_orb,5)))
    col2.metric(label="Electronegatividad", value=str(round(u_orb,5)))
    col3.metric(label="Electrofilicidad", value=str(round(w_orb,5)))

    gap = lumo_o - homo_o
    gap_eV = gap*27.2116
  
    col1, col2 = st.columns(2)
    col1.metric(label="GAP", value=str(round(gap,5)))
    col2.metric(label="GAP (eV", value=str(round(gap_eV,5)))





