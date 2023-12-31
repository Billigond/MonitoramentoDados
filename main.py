from flask import Flask, render_template
import plotly.express as px
import pandas as pd
import random  # Importe a biblioteca random

app = Flask(__name__)

@app.route('/')
def index():
    # Crie uma lista de sexo
    sexo = ["Homem","Mulher","Outros"]

    # Gere Gastos aleatório para cada sexo
    Gastos = [random.randint(1000, 3000) for _ in sexo]

    # Crie um sexoFrame com sexo e Gastos aleatório
    dados = {'sexo': sexo, 'Gastos': Gastos}
    df = pd.DataFrame(dados)

    # Visualização de barras
    bar = px.bar(df, x='sexo', y='Gastos', title='Gastos Mensais',text='Gastos',color=df["sexo"])
    plot_div = bar.to_html(full_html=False)


    return render_template('index.html', plot_div=plot_div)


if __name__ == '__main__':
    app.run(debug=True)


