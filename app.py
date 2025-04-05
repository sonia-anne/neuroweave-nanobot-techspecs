import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import altair as alt

st.set_page_config(page_title="NEUROWEAVE Nanobot - Technical Profile", layout="wide", page_icon="🧠")

st.title("🧠 NEUROWEAVE Nanobot: Technical Table & Smart Visualizations")
st.markdown("Explore the internal structure, autonomous intelligence, safety, and drug delivery efficiency of the world's most advanced regenerative nanobot.")

# Tabla técnica del nanobot
data = {
    "Component": [
        "Size", "Shape", "Material", "Coating", "Propulsion", "Sensors",
        "Cargo", "Navigation", "AI Brain", "Release System", "Biocompatibility", "Self-Destruction"
    ],
    "Details": [
        "5 x 5 x 2 microns (1/20 of a human hair)",
        "Rectangular body with 4 magnetic propulsors",
        "Graphene-reinforced biodegradable PLA",
        "PEG 2nm (immune invisibility)",
        "Magnetic nanoparticles (Fe₃O₄)",
        "Quantum sensors: pH, temp, pressure, signal",
        "BDNF + VEGF liposomes (controlled)",
        "AI-guided via magnetic + chemical gradients",
        "Deep reinforcement learning core",
        "pH-triggered nanochannels",
        "100% safe, immune-evasive, PEG-wrapped",
        "Dissolves in 72h after target task completed"
    ]
}
df = pd.DataFrame(data)

fig_table = go.Figure(data=[go.Table(
    header=dict(values=["<b>Component</b>", "<b>Specification</b>"],
                fill_color='#1f2937', font=dict(color='white', size=13), align="left"),
    cells=dict(values=[df[col] for col in df.columns],
               fill_color='#374151', font=dict(color='white', size=12), align="left"))
])
fig_table.update_layout(margin=dict(t=20, b=20))
st.plotly_chart(fig_table, use_container_width=True)

# Heatmap de riesgo biomecánico
st.subheader("⚠️ Biomechanical Risk Matrix")
risk_labels = ["Damage", "Rejection", "Toxicity", "Navigation", "Release Fail", "Data Loss"]
risk_data = np.random.rand(6, 6)
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(risk_data, xticklabels=risk_labels, yticklabels=risk_labels, cmap="coolwarm", annot=True)
st.pyplot(fig)

# Diagrama de IA corregido con altair
st.subheader("🧠 Neural Network (Decision Core)")

nodes = [
    {"name": "pH", "layer": 0},
    {"name": "Temp", "layer": 0},
    {"name": "Location", "layer": 0},
    {"name": "Layer 1", "layer": 1},
    {"name": "Layer 2", "layer": 2},
    {"name": "Release", "layer": 3},
    {"name": "Move", "layer": 3}
]

edges = [
    {"source": "pH", "target": "Layer 1"},
    {"source": "Temp", "target": "Layer 1"},
    {"source": "Location", "target": "Layer 1"},
    {"source": "Layer 1", "target": "Layer 2"},
    {"source": "Layer 2", "target": "Release"},
    {"source": "Layer 2", "target": "Move"}
]

nodes_df = pd.DataFrame(nodes)
edges_df = pd.DataFrame(edges).merge(
    nodes_df[['name', 'layer']], left_on='source', right_on='name'
).rename(columns={'layer': 'source_layer'}).drop('name', axis=1).merge(
    nodes_df[['name', 'layer']], left_on='target', right_on='name'
).rename(columns={'layer': 'target_layer'}).drop('name', axis=1)

# Asignar coordenadas
nodes_df['x'] = nodes_df['layer'] * 200
nodes_df['y'] = [i * 100 for i in range(len(nodes_df))]

# Dibujo
points = alt.Chart(nodes_df).mark_circle(size=300).encode(
    x='x:Q',
    y='y:Q',
    tooltip='name:N',
    color=alt.value('cyan')
)

text = alt.Chart(nodes_df).mark_text(dy=-20, fontSize=12, color='white').encode(
    x='x:Q',
    y='y:Q',
    text='name:N'
)

lines = alt.Chart(edges_df).mark_rule(strokeWidth=2).encode(
    x='source_layer:Q',
    x2='target_layer:Q',
    y='source:N',
    y2='target:N'
)

st.altair_chart(points + text, use_container_width=True)

# Gráfico de liberación BDNF
st.subheader("💊 BDNF Drug Release Over Time")
t = np.linspace(0, 72, 100)
release = 100 * (1 - np.exp(-0.1 * t))
fig_release = go.Figure()
fig_release.add_trace(go.Scatter(x=t, y=release, fill='tozeroy', line=dict(color='green')))
fig_release.update_layout(title="BDNF Release Curve (72 hours)", xaxis_title="Time (h)", yaxis_title="Release (%)")
st.plotly_chart(fig_release, use_container_width=True)

# Comparación Control Manual vs AI
st.subheader("🎮 AI vs Manual Control")
metrics = ["Precision", "Speed", "Efficiency", "Accuracy"]
manual = [0.7, 0.6, 0.65, 0.68]
auto = [0.95, 0.9, 0.92, 0.96]
fig_cmp = go.Figure()
fig_cmp.add_trace(go.Bar(x=metrics, y=manual, name="Manual", marker_color='red'))
fig_cmp.add_trace(go.Bar(x=metrics, y=auto, name="AI", marker_color='blue'))
fig_cmp.update_layout(barmode='group', title="Autonomous vs Manual Nanobot Control")
st.plotly_chart(fig_cmp, use_container_width=True)

# Mensaje Final
st.success("NEUROWEAVE is engineered for real-time decision making, safe self-destruction, and regenerative healing — all in a 5-micron machine.")
