import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# # Page title
# st.set_page_config(page_title='Interactive Data Explorer', page_icon='📊')
# st.title('📊 Interactive Data Explorer')

# st.sidebar.title('따라가기')
# st.title("oss 0327")
# st.color_picker('Choose your favorite color?')

rand=np.random.normal(1,2,size=20)
fig,ax=plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)