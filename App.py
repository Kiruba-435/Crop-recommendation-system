import streamlit as st
import pickle 

pickle_model=open("soil_classification.pkl",'rb')
classifier=pickle.load(pickle_model)

def prediction(N,P,K,Temperature,Humidity,ph,Rainfall):
    prediction=classifier.predict([[N,P,K,Temperature,Humidity,ph,Rainfall]])
    print(prediction)
    return prediction

def main():
    st.title('Crop Recommendation')

    N=st.text_input("Nitrogen","")
    P=st.text_input("Phosphorus","")
    K=st.text_input("Potassium","")
    Temperature=st.text_input("Temperature","")
    Humidity=st.text_input("Humidity","")
    ph=st.text_input("ph","")
    Rainfall=st.text_input("Rainfall","")
    result=""

    if st.button("Predict crop"):
        result=prediction(N,P,K,Temperature,Humidity,ph,Rainfall)
        st.markdown(f"<h2 style='color:balck;'>The Recommended crop is {result}</h2>",unsafe_allow_html=True)
    
    st.toast(f'The Recommendation Crop is {result}')
    if st.button("About"):
        st.text("Data Driven Crop Recommendation ")
        st.text("It takes the Value of nitrogen,phosperus,pottasium of the soil with temperature, humidity,rainfall and return crop suitable for this inputs")


main()

