import streamlit as st
import pandas as pd
import math 

st.title("Parámetros de reactividad")

st.write("Bienvenido. Este programa te calculara parámetros de reactividad")

st.subheader('Hartress')
ht = st.text_input("Hartress: ")
ht0 = st.text_input("Hartress 0: ")
ht1p = st.text_input("Hartress -1: ")
ht1m = st.text_input("Hartress +1: ")
st.subheader('Nucleofilicidad')
homo = st.text_input("HOMO:")
lumo = st.text_input("LUMO: ")
    
print("PARÁMETROS DE REACTIVIDAD")
print("Bienvenido. Este programa te calculara parámetros de reactividad\n")
print('HARTRESS')

ht = input("Hartress: ")
ht0 = input("Hartress 0: ")
ht1p = input("Hartress +1: ")
ht1m = input("Hartress -1: ")

next = st.button("Siguiente")

if next == true:
   eV0 = float(ht0) * 27.2116
   eVp = float(ht1p) * 27.2116
   eVm = float(ht1m) * 27.2116
   eV()

def eV():
    st.write("\neV 0: " + str(eV0))
    st.write("eV -1: " + str(eVp))
    st.write("eV +1: " + str(eVm) + "\n")


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

