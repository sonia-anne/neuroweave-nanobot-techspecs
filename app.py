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

# Diagrama de IA simplificado
st.subheader("🧠 Neural Network (Decision Core)")
nodes = ["pH", "Temp", "Location", "Layer 1", "Layer 2", "Release", "Move"]
edges = [("pH", "Layer 1"), ("Temp", "Layer 1"), ("Location", "Layer 1"),
         ("Layer 1", "Layer 2"), ("Layer 2", "Release"), ("Layer 2", "Move")]
edge_df = pd.DataFrame(edges, columns=["source", "target"])
node_df = pd.DataFrame({"node": nodes})
chart = alt.Chart(edge_df).mark_line().encode(
    x='source:N', x2='target:N',
    y=alt.value(150), strokeWidth=alt.value(3)
) + alt.Chart(node_df).mark_point(filled=True, size=200, color='cyan').encode(
    x='node:N', y=alt.value(150)
)
st.altair_chart(chart, use_container_width=True)

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
