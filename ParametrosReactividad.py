import streamlit as st
import pandas as pd
import math 

st.title("Parámetros de reactividad")

st.write("Bienvenido. Este programa te calculara parámetros de reactividad")


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

if st.button('Calcular'):
  eV0 = ht0 * 27.2116
  eV1p = ht1p * 27.2116
  eV1m = ht1m * 27.2116
  
  kcal = str(ht*627.5)

  A = eV0-eV1m
  I = eV1p - eV0

  n_aproxE = (I-A)/2
  u_aproxE = (I+A)/2
  w_aproxE = pow(u_aproxE,2)/(2*n)


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
  col1.metric(label="Dureza", value=str(n_aproxE))
  col2.metric(label="Electronegatividad", value=str(u_aproxE))
  col3.metric(label="Electrofilicidad", value=str(w_aproxE))

  st.subheader("Aproximación Orbital")

  A_orb = -27*e_lumo
  I_orb = -27*e_homo

  n_orb = (I - A) / 2
  u_orb = (I + A) / 2
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




  

    
#print("PARÁMETROS DE REACTIVIDAD")
#print("Bienvenido. Este programa te calculara parámetros de reactividad\n")
#print('HARTRESS')

#ht = input("Hartress: ")
#ht0 = input("Hartress 0: ")
#ht1p = input("Hartress +1: ")
#ht1m = input("Hartress -1: ")
#st.button('hola')


#if next == true:
   #eV0 = float(ht0) * 27.2116
   #eVp = float(ht1p) * 27.2116
   #eVm = float(ht1m) * 27.2116
   #eV()

#def eV():
    #st.write("\neV 0: " + str(eV0))
    #st.write("eV -1: " + str(eVp))
    #st.write("eV +1: " + str(eVm) + "\n")


#Hartress en eV
#eV0 = float(ht0) * 27.2116
#eVp = float(ht1p) * 27.2116
#eVm = float(ht1m) * 27.2116

#def eV():
#    print("\neV 0: " + str(eV0))
#    print("eV -1: " + str(eVp))
#    print("eV +1: " + str(eVm) + "\n")
#eV()

#def kcal():
#    print("kCal/mol 0: : " + str(float(ht0)*627.5))
#    print("kCal/mol +1: " + str(float(ht1p) * 627.5))
#    print("kCal/mol -1: " + str(float(ht1m) * 627.5) + "\n")
#kcal()

#def aprox_E():
#    A = eV0-eVm
#    I = eVp - eV0
#    print("APROXIMACIÓN DE ENERGÍAS")
#    print("Afinidad electrónica: " + str(A))
#    print("Potencial de ionización: " + str(I) + "\n")

#    n = (I-A)/2
#    u = (I+A)/2
#    w = pow(u,2)/(2*n)
#    print("Dureza: " + str(n))
#    print("Electronegatividad: " + str(u))
#    print("Electrofilicidad: " + str(w) + "\n")
#aprox_E()

#e_homo = float(input("E HOMO: "))
#e_lumo = float(input("E LUMO: "))

#def aprox_orb():
#    print("\nAPROXIMACIÓN ORBITAL")
#    A = -27*e_lumo #Afinidad electrónica
#    I = -27*e_homo #Potencial de ionización
#    print("Afinidad electrónica: " + str(A))
#    print("Potencial de ionización: " + str(I))

#    n = (I - A) / 2
#    u = (I + A) / 2
#    w = pow(u, 2) / (2 * n)
#    print("Dureza: " + str(n))
#    print("Electronegatividad: " + str(u))
#    print("Electrofilicidad: " + str(w) + "\n")

#    homo_o = float(input("HOMO(O): "))
#    lumo_o = float(input("LUMO(V): "))
#    gap = lumo_o - homo_o
#    gap_eV = gap*27.2116
#    print("GAP: " + str(gap))
#    print("GAP (eV): " + str(gap_eV))

#st.write('ht*27.2116')



#st.write("Hola mundo")
#st.button("Holi")
#st.button(":D")
#dt es data frame
#df = pd.read_csv('https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv')
#st.write(df)
#st.map(df)
#Buscar steamlit API
#st.latex("\r^2 + a r^3\sum_{k=0}^{n-1} ar^\")
#st.markdown(" **este es una viñeta** ")

