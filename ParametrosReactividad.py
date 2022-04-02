import streamlit as st
import pandas as pd
import math as math

st.title("Parámetros de reactividad")

st.write("Bienvenido. Este programa te calculara parámetros de reactividad")

ht = input("Hartress: ")
ht0 = input("Hartress 0: ")
ht-1 = input ("Hartress -1: ")
ht+1 = input("Hartress +1: ")
st.write: Nucleofilicidad
nc = input("Nucleofilicidad:")

#INPUTS
#Hartrees
    #Hartress
    #Cargas (0, +1, -1)
#Nucleofilicidad
    #HOMO, LUMO 


#OUTPUTS
    #eV(E) = Hartress*27.2116
    #kCal/mol = Hartress*627.5
#eV (E)
    #0=27.21226*(c0,c+1,c-1   
#Aproximación de energías
    #E(0)- E(-1) = Afinidad electrónica (A)
    # E(+) - E(0) = Potencial de ionización (I)

    #(I-A)/2 Dureza(n)
    #(I+A)/2 Electronegatividad (u)
    # w = u^2/2n Electrofilicidad (w)
#Aproximación orbital
    #E_HOMO, E_LUMO
    #A = -ELUMO*27 Afinidad electrónica
    #I = -E HOMO*27 Potencial de ionización

    #(I-A)/2 Dureza (n)
    #(I+A)/2 Electronegatividad (u)
    #w = u^2/2n Electrofilicidad (w)

#HOMO(O), LUMO(V)
    #GAP(Hartress) = LUMO(V)-HOMO(O)


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

