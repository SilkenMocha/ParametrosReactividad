import streamlit as st
import pandas as pd
import math 

st.title("Parámetros de reactividad")

st.write("Bienvenido. Este programa te calculara parámetros de reactividad")


reactividad=st.button("Parametros de reactividad")

if reactividad:
  with st.form(key='calc_react'):
    st.subheader('Hartress')
    ht = st.number_input("Hartress: ")
    ht0 = st.number_input("Hartress 0: ")
    ht1p = st.number_input("Hartress +1: ")
    ht1m = st.number_input("Hartress -1: ")
    st.subheader('Nucleofilicidad')
    homo = st.number_input("HOMO:")
    lumo = st.number_input("LUMO: ")
    homo_o = st.number_input("HOMO (O):")
    lumo_o = st.number_input("LUMO (V): ")

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
    w = pow(u,2)/(2*n)


    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="H 0", value=ht0)
    col2.metric(label="H -1", value=ht1m)
    col3.metric(label="H +1", value=ht1p)
    col4.metric(label="kCal/mol", value=kcal)

    col1, col2, col3 = st.columns(3)
    col1.metric(label="eV 0", value=str(eV0))
    col2.metric(label="eV -1", value=str(eV1p))
    col3.metric(label="eV +1", value=str(eV1m))
  
    st.subheader("Aproximación de energias")

    col1, col2 = st.columns(2)
    col1.metric(label="Afinidad electrónica", value=str(A))
    col2.metric(label="Potencial de ionización", value=str(I))

    col1, col2, col3 = st.columns(3)
    col1.metric(label="Dureza", value=str(n))
    col2.metric(label="Electronegatividad", value=str(u))
    col3.metric(label="Electrofilicidad", value=str(w))

    st.subheader("Aproximación Orbital")

    A_orb = -27*lumo
    I_orb = -27*homo

    n_orb = (I_orb - A_orb) / 2
    u_orb = (I_orb + A_orb) / 2
    w_orb = pow(u, 2) / (2 * n)
  
    col1, col2 = st.columns(2)
    col1.metric(label="Afinidad electrónica", value=str(A_orb))
    col2.metric(label="Potencial de ionización", value=str(I_orb))

    col1, col2, col3 = st.columns(3)
    col1.metric(label="Dureza", value=str(n_orb))
    col2.metric(label="Electronegatividad", value=str(u_orb))
    col3.metric(label="Electrofilicidad", value=str(w_orb))

    gap = lumo_o - homo_o
    gap_eV = gap*27.2116
  
    col1, col2 = st.columns(2)
    col1.metric(label="GAP", value=str(gap))
    col2.metric(label="GAP (eV", value=str(gap_eV))


