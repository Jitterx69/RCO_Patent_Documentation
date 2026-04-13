import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_pipeline_diagram():
    # Setup figure and axis
    fig, ax = plt.subplots(figsize=(18, 6), dpi=300)
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Color palette
    color_main = '#f0f4f8'
    color_border = '#627d98'
    color_text = '#102a43'
    color_accept = '#e3f9e5'
    color_accept_border = '#38a169'
    color_reject = '#fff5f5'
    color_reject_border = '#e53e3e'

    # Box dimensions
    box_w = 1.6
    box_h = 0.8
    y_center = 3

    # Pipeline stages
    stages = [
        {"label": "Telemetry\nInput ($D_t$)", "x": 0.5},
        {"label": "Canonicalization\n$B_t = S(D_t)$", "x": 2.6},
        {"label": "Hashing\n$H_t = H(B_t)$", "x": 4.7},
        {"label": "Lineage\n$L_t = H(H_t || L_{t-1})$", "x": 6.8},
        {"label": "State Binding\n$M_t = H(S_t) || L_t$", "x": 8.9},
    ]

    # Draw nodes and arrows
    for i, stage in enumerate(stages):
        # Draw box
        rect = patches.FancyBboxPatch(
            (stage["x"], y_center - box_h/2), box_w, box_h,
            boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_border, facecolor=color_main
        )
        ax.add_patch(rect)
        ax.text(stage["x"] + box_w/2, y_center, stage["label"], 
                ha='center', va='center', fontweight='bold', fontsize=10, color=color_text)

        # Draw arrow to next stage
        if i < len(stages) - 1:
            ax.annotate('', xy=(stages[i+1]["x"], y_center), xytext=(stage["x"] + box_w + 0.1, y_center),
                        arrowprops=dict(arrowstyle='->', lw=1.5, color=color_border))

    # Validator Nodes (Distributed cluster)
    validator_x = 11.2
    validator_y_start = 1.0
    validator_y_end = 5.0
    validator_count = 5
    v_ys = [1.5, 2.25, 3.0, 3.75, 4.5]
    
    # Label for Validator section
    ax.text(validator_x + 0.4, 5.2, "Validator Nodes", ha='center', fontweight='bold', fontsize=11)
    ax.text(validator_x + 0.4, 0.8, "Independent Verification\n+ Signing", ha='center', fontsize=8, color=color_border)

    # Main arrow to validator cluster
    ax.annotate('', xy=(validator_x, y_center), xytext=(stages[-1]["x"] + box_w + 0.1, y_center),
                arrowprops=dict(arrowstyle='->', lw=1.5, color=color_border))

    for vy in v_ys:
        # Fan out
        ax.plot([validator_x, validator_x + 0.3], [y_center, vy], color=color_border, lw=1)
        # Small node
        circ = patches.Circle((validator_x + 0.4, vy), 0.15, facecolor='white', edgecolor=color_border, lw=1.5)
        ax.add_patch(circ)
        ax.text(validator_x + 0.4, vy, "V", ha='center', va='center', fontsize=8, fontweight='bold')

    # Signature Aggregation node
    agg_x = 12.8
    rect_agg = patches.FancyBboxPatch(
        (agg_x, y_center - box_h/2), box_w, box_h,
        boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_border, facecolor=color_main
    )
    ax.add_patch(rect_agg)
    ax.text(agg_x + box_w/2, y_center, "Signature\nAggregation ($\Sigma_t$)\n(Convergence)", 
            ha='center', va='center', fontweight='bold', fontsize=9, color=color_text)

    # Fan in to aggregation
    for vy in v_ys:
        ax.plot([validator_x + 0.5, agg_x], [vy, y_center], color=color_border, lw=1)

    # Verification Engine
    engine_x = 15.0
    rect_engine = patches.FancyBboxPatch(
        (engine_x, y_center - box_h/2), 1.2, box_h,
        boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_border, facecolor=color_main
    )
    ax.add_patch(rect_engine)
    ax.text(engine_x + 0.6, y_center, "Verification\nEngine", 
            ha='center', va='center', fontweight='bold', fontsize=9, color=color_text)

    ax.annotate('', xy=(engine_x, y_center), xytext=(agg_x + box_w + 0.1, y_center),
                arrowprops=dict(arrowstyle='->', lw=1.5, color=color_border))

    # Accept / Reject branches
    out_x = 16.8
    # Accept
    rect_acc = patches.FancyBboxPatch((out_x, y_center + 0.5), 1.0, 0.4, boxstyle="round,pad=0.05", 
                                       linewidth=1.5, edgecolor=color_accept_border, facecolor=color_accept)
    ax.add_patch(rect_acc)
    ax.text(out_x + 0.5, y_center + 0.7, "ACCEPT", ha='center', va='center', fontweight='heavy', fontsize=10, color=color_accept_border)
    
    # Reject
    rect_rej = patches.FancyBboxPatch((out_x, y_center - 0.9), 1.0, 0.4, boxstyle="round,pad=0.05", 
                                       linewidth=1.5, edgecolor=color_reject_border, facecolor=color_reject)
    ax.add_patch(rect_rej)
    ax.text(out_x + 0.5, y_center - 0.7, "REJECT", ha='center', va='center', fontweight='heavy', fontsize=10, color=color_reject_border)

    # Output lines
    ax.plot([engine_x + 1.2, out_x], [y_center, y_center + 0.7], color=color_border, lw=1)
    ax.plot([engine_x + 1.2, out_x], [y_center, y_center - 0.7], color=color_border, lw=1)

    # Title
    plt.title("End-to-End RCO Validation Pipeline", fontsize=16, pad=30, fontweight='bold', color='#102a43')
    
    plt.tight_layout()
    plt.savefig('/Users/jitterx/Downloads/RCO_Patent_Documentation/figures/pipeline_diagram.png', bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    generate_pipeline_diagram()
