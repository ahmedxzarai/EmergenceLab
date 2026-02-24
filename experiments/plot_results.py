# =============================================================================
# 🛡️ EmergenceLab v5 — Paper Asset Generator
# File        : plot_results.py
# Author      : AHMED ZARAI
# Purpose     : Generate high-quality figures for publications from simulation logs
# =============================================================================

import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# -----------------------------------------------------------------------------
# 📂 Paths
# -----------------------------------------------------------------------------
FIGURE_DIR = "paper/figures"
LOG_PATH = "results/metrics_log.csv"
DASHBOARD_PATH = "results/live_dashboard.json"


# =============================================================================
# 🔎 Generate Figures for Paper
# =============================================================================
def generate_paper_assets():
    """
    Generates line plots for entropy, KL divergence, mutual information,
    and network connectivity graphs for use in publications.
    """

    # -------------------------------------------------------------------------
    # Check simulation log
    # -------------------------------------------------------------------------
    if not os.path.exists(LOG_PATH):
        print(f"❌ Error: {LOG_PATH} not found. Run simulation first!")
        return

    os.makedirs(FIGURE_DIR, exist_ok=True)
    df = pd.read_csv(LOG_PATH)

    # -------------------------------------------------------------------------
    # --- Line Plots ---
    # -------------------------------------------------------------------------
    plt.style.use('ggplot')
    plots = [
        ("entropy", "Entropy Decay", "entropy_plot.png", "royalblue"),
        ("kl_divergence", "Belief Convergence (KL)", "kl_plot.png", "crimson"),
        ("mutual_information", "Information Growth (MI)", "mi_plot.png", "seagreen")
    ]

    for column, title, filename, color in plots:
        plt.figure(figsize=(8, 4))
        plt.plot(df["timestep"], df[column], color=color, linewidth=2)
        plt.title(title)
        plt.xlabel("Timestep")
        plt.ylabel("Value")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(os.path.join(FIGURE_DIR, filename), dpi=300)
        plt.close()
        print(f"✅ Saved {filename}")

    # -------------------------------------------------------------------------
    # --- Network Connectivity Graph ---
    # -------------------------------------------------------------------------
    if os.path.exists(DASHBOARD_PATH):
        try:
            with open(DASHBOARD_PATH, "r") as f:
                data = json.load(f)
            beliefs = data.get("beliefs", [])

            if beliefs:
                G = nx.Graph()
                agents = [b["agent"] for b in beliefs]
                N = len(agents)

                # Add nodes
                G.add_nodes_from(agents)

                # Compute weighted edges from belief vectors
                for i in range(N):
                    for j in range(i + 1, N):
                        b1, b2 = beliefs[i]["belief"], beliefs[j]["belief"]
                        dist = sum((x - y) * 2 for x, y in zip(b1, b2)) * 0.5 / len(b1)
                        weight = 1 - dist
                        G.add_edge(agents[i], agents[j], weight=weight)

                # Draw network
                plt.figure(figsize=(6, 6))
                pos = nx.spring_layout(G, seed=42)
                edges = G.edges(data=True)
                weights = [e[2]["weight"] * 5 for e in edges]

                nx.draw_networkx_nodes(G, pos, node_color="#00f5d4", node_size=500)
                nx.draw_networkx_labels(G, pos, font_color="white")
                nx.draw_networkx_edges(G, pos, width=weights, alpha=0.6)

                plt.title("Network Connectivity Field")
                plt.axis('off')
                plt.tight_layout()
                plt.savefig(os.path.join(FIGURE_DIR, "network_connectivity.png"), dpi=300)
                plt.close()
                print("✅ Saved network_connectivity.png")

        except Exception as e:
            print(f"⚠️ Failed to generate network connectivity figure: {e}")


# =============================================================================
# 🏁 Entry Point
# =============================================================================
if __name__ == "__main__":
    generate_paper_assets()