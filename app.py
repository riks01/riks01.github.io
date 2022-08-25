import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from matplotlib import pyplot 
from PIL import Image
import numpy as np
from PIL import Image

st.header('Fake Image Generator')
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(30, 200, 49);font-size:20px;height:3em;width:30em;
}
</style>""", unsafe_allow_html=True)

def save_plot(examples, n):
    examples = (examples + 1) / 2.0
    for i in range(n * n):
        pyplot.subplot(n, n, i+1)
        pyplot.axis("off")
        pyplot.imshow(examples[i])
    pyplot.savefig('static/fake.png')
    pyplot.close()

image = Image.open('static/fake.png')
st.image(image)
if st.button('Generate'):
    model = load_model("saved_model/g_model.h5")
    n_samples = 16    ## n should always be a square of an integer.
    latent_dim = 128
    latent_points = np.random.normal(size=(n_samples, latent_dim))
    examples = model.predict(latent_points)
    save_plot(examples, int(np.sqrt(n_samples)))

    # image = Image.open('static/fake.png')
