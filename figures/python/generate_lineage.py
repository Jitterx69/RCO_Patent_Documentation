import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_lineage_diagram():
    # Setup figure and axis
    fig, ax = plt.subplots(figsize=(16, 7), dpi=300)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 7)
    ax.axis('off')

    # Color palette
    color_main = '#f0f4f8'
    color_border = '#627d98'
    color_text = '#102a43'
    color_hash = '#d9e2ec'
    color_tamper = '#e53e3e' # Red for tamper propagation

    # Box dimensions
    box_w = 2.4
    box_h = 1.0
    y_center = 3.5

    # Nodes definition
    nodes = [
        {"id": "L0", "label": "Genesis\n$L_0$", "x": 0.5, "y": y_center},
        {"id": "L1", "label": "$L_1 = H(H_1 || L_0)$", "x": 4.5, "y": y_center},
        {"id": "L2", "label": "$L_2 = H(H_2 || L_1)$", "x": 8.5, "y": y_center},
        {"id": "L3", "label": "$L_3 = H(H_3 || L_2)$", "x": 12.5, "y": y_center},
    ]

    # Draw nodes
    for node in nodes:
        rect = patches.FancyBboxPatch(
            (node["x"], node["y"] - box_h/2), box_w, box_h,
            boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_border, facecolor=color_main
        )
        ax.add_patch(rect)
        ax.text(node["x"] + box_w/2, node["y"], node["label"], 
                ha='center', va='center', fontweight='bold', fontsize=11, color=color_text)

    # Draw inputs (H1, H2, H3)
    inputs = [
        {"label": "$H_1$", "target": "L1", "x": 4.5 + box_w/2, "y": 5.5},
        {"label": "$H_2$", "target": "L2", "x": 8.5 + box_w/2, "y": 5.5},
        {"label": "$H_3$", "target": "L3", "x": 12.5 + box_w/2, "y": 5.5},
    ]

    for inp in inputs:
        # Input node
        circ = patches.Circle((inp["x"], inp["y"]), 0.4, facecolor=color_hash, edgecolor=color_border, lw=1.2)
        ax.add_patch(circ)
        ax.text(inp["x"], inp["y"], inp["label"], ha='center', va='center', fontweight='bold', fontsize=11)
        
        # Arrow down to L_t
        ax.annotate('', xy=(inp["x"], y_center + 0.6), xytext=(inp["x"], inp["y"] - 0.4),
                    arrowprops=dict(arrowstyle='->', lw=1.5, color=color_border))

    # Main chain arrows (L_t-1 to L_t)
    for i in range(len(nodes) - 1):
        ax.annotate('', xy=(nodes[i+1]["x"], y_center), xytext=(nodes[i]["x"] + box_w + 0.1, y_center),
                    arrowprops=dict(arrowstyle='->', lw=2.0, color=color_border))

    # TAMPER PROPAGATION VISUALIZATION
    # Red dashed arrow showing if H1 changes
    ax.annotate('', xy=(nodes[3]["x"] + box_w/2, y_center - 0.6), 
                xytext=(inputs[0]["x"], 5.5),
                arrowprops=dict(arrowstyle='->', lw=2.0, color=color_tamper, ls='--', connectionstyle="arc3,rad=-0.3"))
    
    # Tamper text
    ax.text(8, 1.2, "IF $H_1$ CHANGES $\longrightarrow$ $L_3$ CHANGES", 
            ha='center', va='center', color=color_tamper, fontweight='bold', fontsize=12,
            bbox=dict(facecolor='white', edgecolor=color_tamper, boxstyle='round,pad=0.5', alpha=0.9))

    # Annotations
    ax.text(8, 6.5, "EACH LINEAGE STATE DEPENDS ON ENTIRE HISTORY", 
            ha='center', va='center', fontweight='bold', fontsize=14, color=color_text)
    
    ax.text(1.5, 1.0, "ANY MODIFICATION IN $H_i$ PROPAGATES FORWARD", 
            ha='left', va='center', fontweight='bold', fontsize=10, color=color_border)

    plt.title("Lineage Chain Construction and Temporal Integrity", fontsize=18, pad=40, fontweight='bold', color=color_text)
    
    plt.tight_layout()
    plt.savefig('/Users/jitterx/Downloads/RCO_Patent_Documentation/figures/lineage_structure.png', bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    generate_lineage_diagram()
