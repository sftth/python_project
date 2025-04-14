
from elastic_data.services.elastic_api import get_indices
from flask import Flask, render_template_string
from elastic_data.services.elastic_api import get_indices_web

app = Flask(__name__)

@app.route('/')
def home():
#    template, html_table = get_indices_web()

    return render_template_string(template, table=html_table)

if __name__ == '__main__':
    print("Start app")
    app.run(debug=True)
