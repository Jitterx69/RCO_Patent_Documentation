import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_api_flow_diagram():
    # Setup figure and axis
    fig, ax = plt.subplots(figsize=(18, 10), dpi=300)
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Color palette
    color_main = '#f0f4f8'
    color_border = '#627d98'
    color_text = '#102a43'
    color_accept = '#e3f9e5'
    color_accept_border = '#38a169'
    color_reject = '#fff5f5'
    color_reject_border = '#e53e3e'
    color_api = '#d9e2ec'

    y_center = 5

    # 1. CLIENT
    ax.add_patch(patches.FancyBboxPatch((0.5, y_center - 1), 2.5, 2, boxstyle="round,pad=0.1", linewidth=2.0, edgecolor=color_border, facecolor=color_main))
    ax.text(1.75, y_center + 0.2, "Client /\nApplication", ha='center', va='center', fontweight='bold', fontsize=12)
    ax.text(1.75, y_center - 0.5, "SDK or Direct\nAPI Call", ha='center', va='center', fontsize=9, color=color_border)

    # 2. API ENDPOINT
    ax.annotate('', xy=(3.8, y_center), xytext=(3.0, y_center), arrowprops=dict(arrowstyle='->', lw=1.5, color=color_border))
    ax.add_patch(patches.FancyBboxPatch((3.8, y_center - 0.8), 2.2, 1.6, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_border, facecolor=color_api))
    ax.text(4.9, y_center + 0.3, "POST /ingest", ha='center', va='center', fontweight='bold', fontsize=10)
    ax.text(4.9, y_center - 0.3, "{data, state,\nmetadata}", ha='center', va='center', fontsize=8, family='monospace')

    # 3. RCO PIPELINE (Large Box)
    ax.annotate('', xy=(6.5, y_center), xytext=(6.0, y_center), arrowprops=dict(arrowstyle='->', lw=1.5, color=color_border))
    ax.add_patch(patches.FancyBboxPatch((6.5, y_center - 2), 3.5, 4, boxstyle="round,pad=0.1", linewidth=2.0, edgecolor=color_border, facecolor=color_main))
    ax.text(8.25, y_center + 1.5, "RCO Processing\nPipeline", ha='center', fontweight='bold', fontsize=11)
    
    # Internal Steps
    steps = ["Canonicalization", "Hashing", "Lineage Computation", "State Binding"]
    for i, step in enumerate(steps):
        s_y = y_center + 0.6 - (i * 0.6)
        ax.add_patch(patches.Rectangle((6.8, s_y - 0.2), 2.9, 0.4, facecolor='white', edgecolor=color_border, lw=0.5))
        ax.text(8.25, s_y, step, ha='center', va='center', fontsize=8)

    # 4. VALIDATORS
    ax.annotate('', xy=(10.5, y_center), xytext=(10.0, y_center), arrowprops=dict(arrowstyle='->', lw=1.5, color=color_border))
    ax.add_patch(patches.FancyBboxPatch((10.5, y_center - 1.2), 2.5, 2.4, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_border, facecolor=color_main))
    ax.text(11.75, y_center + 0.8, "Validator Fabric", ha='center', fontweight='bold', fontsize=10)
    ax.text(11.75, y_center - 0.2, "Distributed\nVerification\n+ Signing", ha='center', va='center', fontsize=8, color=color_border)

    # 5. AGGREGATION & ENGINE
    ax.annotate('', xy=(13.5, y_center), xytext=(13.0, y_center), arrowprops=dict(arrowstyle='->', lw=1.5, color=color_border))
    ax.add_patch(patches.FancyBboxPatch((13.5, y_center - 0.8), 1.8, 1.6, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_border, facecolor=color_main))
    ax.text(14.4, y_center + 0.3, "Verification\nEngine", ha='center', va='center', fontweight='bold', fontsize=9)
    ax.text(14.4, y_center - 0.3, "$\Sigma_t$ Aggregation", ha='center', va='center', fontsize=8)

    # 6. RESPONSE (Split)
    # ACCEPT
    ax.add_patch(patches.FancyBboxPatch((15.8, y_center + 0.8), 2.0, 1.2, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_accept_border, facecolor=color_accept))
    ax.text(16.8, y_center + 1.2, "ACCEPT", ha='center', va='center', fontweight='heavy', fontsize=10, color=color_accept_border)
    ax.text(16.8, y_center + 1.0, "{lineage, hash,\nproof}", ha='center', va='top', fontsize=7, family='monospace')
    
    # REJECT
    ax.add_patch(patches.FancyBboxPatch((15.8, y_center - 2.0), 2.0, 1.2, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_reject_border, facecolor=color_reject))
    ax.text(16.8, y_center - 1.2, "REJECT", ha='center', va='center', fontweight='heavy', fontsize=10, color=color_reject_border)
    ax.text(16.8, y_center - 1.4, "{diagnostics,\nerror_code}", ha='center', va='top', fontsize=7, family='monospace')

    ax.annotate('', xy=(15.8, y_center + 1.4), xytext=(15.3, y_center), arrowprops=dict(arrowstyle='->', lw=1.5, color=color_accept_border, connectionstyle="angle,angleA=0,angleB=90,rad=5"))
    ax.annotate('', xy=(15.8, y_center - 1.4), xytext=(15.3, y_center), arrowprops=dict(arrowstyle='->', lw=1.5, color=color_reject_border, connectionstyle="angle,angleA=0,angleB=-90,rad=5"))

    # Return Arrow
    ax.annotate('API JSON Response', xy=(1.75, y_center - 1.2), xytext=(16.8, y_center - 2.2), 
                ha='center', va='center', arrowprops=dict(arrowstyle='->', lw=1.0, color=color_border, ls='--', connectionstyle="arc3,rad=0.2"), fontsize=9)

    # Annotations
    ax.text(9, 9.2, "DETERMINISTIC, VERIFIABLE API EXECUTION", ha='center', fontweight='bold', fontsize=16, color=color_text)
    ax.text(9, 0.8, "PROOF ENABLES INDEPENDENT VERIFICATION", ha='center', fontweight='bold', fontsize=12, color=color_border)

    plt.title("API Interaction Flow for RCO Protocol", fontsize=20, pad=50, fontweight='bold', color=color_text)
    
    plt.tight_layout()
    plt.savefig('/Users/jitterx/Downloads/RCO_Patent_Documentation/figures/api_interaction_flow.png', bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    generate_api_flow_diagram()
