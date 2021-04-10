from flask import Flask, render_template

from bokeh.resources import INLINE

import jinja2

import pickle

import umap

app = Flask(__name__)

with open('graph_ind.pkl', "rb") as fIn:
    stored_data = pickle.load(fIn)
with open('graph_desc.pkl', "rb") as fIn:
    stored_data1 = pickle.load(fIn)
                                  


@app.route("/")
def index():
    script1 = stored_data['script']
    div1 = stored_data['div']

        
        
    
    script2 = stored_data1['script']
    div2 = stored_data1['div']


    # Render HTML with count variable
    #return template.render( plot_script1=script1, plot_div1=div1, plot_script2=script2, plot_div2=div2)
    return render_template("index.html",  plot_script1=script1, plot_div1=div1, plot_script2=script2, plot_div2=div2)

if __name__ == "__main__":
    app.run()
    
    

