import streamlit as st
import io
from PIL import Image



def title():
    st.title("Image Settings")

def upload_img():
    file= st.file_uploader(label="Upload a file", type=["jpg", "jpeg", "png"],label_visibility="hidden")
    if file is not None:
        #current= st.image(file, output_format="auto", caption=None )
        return file
    return



def change_ppp():

    cont= upload_img()
    if cont is not None:
        current= Image.open(cont)
        txt1= st.text_input(label="Save as", key=1)
        txt2= st.number_input(label="Set vertical DPI",step=1, key=2)
        txt3= st.number_input(label="Set horizotal DPI",step=1, key=3)
        btn= st.button("Apply")
        if btn:
            buffer= io.BytesIO()
            current.save(buffer,format="JPEG", dpi=(txt2, txt3))
            buffer.seek(0)
            st.image(current, output_format="auto")
            st.write(f'Size: {current.size}')
            st.text(f'Format: {current.format}')
            st.text(f'Mode: {current.mode}')
            st.download_button(label="Download IMG",data=buffer.getvalue() ,file_name=txt1 + ".jpeg", mime="image/jpeg", icon=":material/download:")





def options():
    menu_box= st.selectbox(label="Choose an option", options=["","dpi", "size", "rotation", "remove background"])
    
    if menu_box == "dpi":
        change_ppp()
    elif menu_box == "size":
        st.warning("Currently unavailable")
    elif menu_box == "rotation":
        st.warning("Currently unavailable")
    elif menu_box == "remove background":
        st.warning("Currently unavailable")

   








if __name__ == "__main__":

    title()
    options()
   

