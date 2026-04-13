import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_state_binding_diagram():
    # Setup figure and axis
    fig, ax = plt.subplots(figsize=(18, 10), dpi=300)
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Color palette
    color_main = '#f0f4f8'
    color_border = '#627d98'
    color_text = '#102a43'
    color_valid = '#e3f9e5'
    color_valid_border = '#38a169'
    color_invalid = '#fff5f5'
    color_invalid_border = '#e53e3e'

    # Box dimensions
    box_w = 2.2
    box_h = 0.8
    y_center = 5

    # INPUT LAYER (Left)
    d_t_x = 0.5
    h_t_x = 3.5
    l_t_x = 6.5

    # D_t
    ax.add_patch(patches.FancyBboxPatch((d_t_x, y_center - 0.4), box_w, box_h, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_border, facecolor=color_main))
    ax.text(d_t_x + box_w/2, y_center, "Telemetry\nInput ($D_t$)", ha='center', va='center', fontweight='bold', fontsize=10)

    # H_t
    ax.add_patch(patches.FancyBboxPatch((h_t_x, y_center - 0.4), box_w, box_h, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_border, facecolor=color_main))
    ax.text(h_t_x + box_w/2, y_center, "Canonicalization\n+ Hashing ($H_t$)", ha='center', va='center', fontweight='bold', fontsize=9)

    # L_t
    ax.add_patch(patches.FancyBboxPatch((l_t_x, y_center - 0.4), box_w, box_h, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_border, facecolor=color_main))
    ax.text(l_t_x + box_w/2, y_center, "Lineage\n$L_t$", ha='center', va='center', fontweight='bold', fontsize=11)

    # Arrows for input layer
    ax.annotate('', xy=(h_t_x, y_center), xytext=(d_t_x + box_w + 0.1, y_center), arrowprops=dict(arrowstyle='->', lw=1.5, color=color_border))
    ax.annotate('', xy=(l_t_x, y_center), xytext=(h_t_x + box_w + 0.1, y_center), arrowprops=dict(arrowstyle='->', lw=1.5, color=color_border))

    # PARALLEL PATHS
    path_y_offset = 2.5
    path_valid_y = y_center + path_y_offset
    path_invalid_y = y_center - path_y_offset

    # Common source arrows from L_t
    ax.annotate('', xy=(9.5, path_valid_y), xytext=(l_t_x + box_w + 0.1, y_center), arrowprops=dict(arrowstyle='->', lw=1.5, color=color_valid_border, connectionstyle="angle,angleA=0,angleB=90,rad=10"))
    ax.annotate('', xy=(9.5, path_invalid_y), xytext=(l_t_x + box_w + 0.1, y_center), arrowprops=dict(arrowstyle='->', lw=1.5, color=color_invalid_border, connectionstyle="angle,angleA=0,angleB=-90,rad=10"))

    # PATH A: VALID CONTEXT (Green)
    ax.text(11, path_valid_y + 1.2, "PATH A: VALID CONTEXT", ha='center', va='center', fontweight='bold', color=color_valid_border, fontsize=12)
    # S_t
    ax.add_patch(patches.FancyBboxPatch((9.5, path_valid_y - 0.4), box_w, box_h, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_valid_border, facecolor=color_valid))
    ax.text(10.6, path_valid_y, "System State\n$S_t$", ha='center', va='center', fontweight='bold', fontsize=10)
    # H(S_t)
    ax.annotate('', xy=(12.5, path_valid_y), xytext=(11.8, path_valid_y), arrowprops=dict(arrowstyle='->', lw=1.5, color=color_valid_border))
    # M_t
    ax.add_patch(patches.FancyBboxPatch((12.5, path_valid_y - 0.4), 2.8, box_h, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_valid_border, facecolor=color_valid))
    ax.text(13.9, path_valid_y, "$M_t = \mathcal{H}(S_t) || L_t$", ha='center', va='center', fontweight='bold', fontsize=11)
    # Accept
    ax.annotate('', xy=(16.0, path_valid_y), xytext=(15.4, path_valid_y), arrowprops=dict(arrowstyle='->', lw=1.5, color=color_valid_border))
    ax.text(17, path_valid_y, "ACCEPT", ha='center', va='center', fontweight='heavy', color=color_valid_border, fontsize=12, bbox=dict(facecolor=color_valid, edgecolor=color_valid_border, boxstyle='round,pad=0.5'))

    # PATH B: INVALID CONTEXT (Red)
    ax.text(11, path_invalid_y - 1.2, "PATH B: INVALID CONTEXT / REPLAY", ha='center', va='center', fontweight='bold', color=color_invalid_border, fontsize=12)
    # S_t'
    ax.add_patch(patches.FancyBboxPatch((9.5, path_invalid_y - 0.4), box_w, box_h, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_invalid_border, facecolor=color_invalid))
    ax.text(10.6, path_invalid_y, "Different State\n$S_t'$", ha='center', va='center', fontweight='bold', fontsize=10)
    # H(S_t')
    ax.annotate('', xy=(12.5, path_invalid_y), xytext=(11.8, path_invalid_y), arrowprops=dict(arrowstyle='->', lw=1.5, color=color_invalid_border))
    # M_t'
    ax.add_patch(patches.FancyBboxPatch((12.5, path_invalid_y - 0.4), 2.8, box_h, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_invalid_border, facecolor=color_invalid))
    ax.text(13.9, path_invalid_y, "$M_t' = \mathcal{H}(S_t') || L_t$", ha='center', va='center', fontweight='bold', fontsize=11)
    # Reject
    ax.annotate('', xy=(16.0, path_invalid_y), xytext=(15.4, path_invalid_y), arrowprops=dict(arrowstyle='->', lw=1.5, color=color_invalid_border))
    ax.text(17, path_invalid_y, "REJECT", ha='center', va='center', fontweight='heavy', color=color_invalid_border, fontsize=12, bbox=dict(facecolor=color_invalid, edgecolor=color_invalid_border, boxstyle='round,pad=0.5'))

    # ANNOTATIONS
    ax.text(9, 9.2, "TELEMETRY VALIDITY DEPENDS ON SYSTEM STATE CONTEXT", ha='center', fontweight='bold', fontsize=14, color=color_text)
    ax.text(9, 0.8, "SAME DATA CANNOT BE REUSED ACROSS STATES", ha='center', fontweight='bold', fontsize=14, color=color_border)

    plt.title("State Binding Mechanism and Contextual Integrity", fontsize=18, pad=50, fontweight='bold', color=color_text)
    
    plt.tight_layout()
    plt.savefig('/Users/jitterx/Downloads/RCO_Patent_Documentation/figures/state_binding.png', bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    generate_state_binding_diagram()
