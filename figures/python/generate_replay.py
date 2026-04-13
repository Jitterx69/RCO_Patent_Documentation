import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_replay_prevention_diagram():
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

    box_w = 2.4
    box_h = 0.8
    y_valid = 7
    y_replay = 3

    # 1. SHARED INPUT DATA (Conceptual Start)
    # Original
    ax.add_patch(patches.FancyBboxPatch((0.5, y_valid - 0.4), box_w, box_h, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_valid_border, facecolor=color_valid))
    ax.text(1.7, y_valid, "Original\nInput $D_t$", ha='center', va='center', fontweight='bold', fontsize=10)
    
    # Replay
    ax.add_patch(patches.FancyBboxPatch((0.5, y_replay - 0.4), box_w, box_h, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_invalid_border, facecolor=color_invalid))
    ax.text(1.7, y_replay, "Replayed\nInput $D_t$\n(SAME DATA)", ha='center', va='center', fontweight='bold', fontsize=10)

    # 2. HASHING (SAME result)
    h_x = 4.0
    ax.add_patch(patches.FancyBboxPatch((h_x, y_valid - 0.4), box_w, box_h, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_border, facecolor=color_main))
    ax.text(h_x + box_w/2, y_valid, "Hash $H_t$\n(Valid)", ha='center', va='center', fontweight='bold', fontsize=10)
    
    ax.add_patch(patches.FancyBboxPatch((h_x, y_replay - 0.4), box_w, box_h, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_border, facecolor=color_main))
    ax.text(h_x + box_w/2, y_replay, "Hash $H_t$\n(SAME HASH)", ha='center', va='center', fontweight='bold', fontsize=10)

    # 3. LINEAGE (THE DIVERGENCE POINT)
    l_x = 7.5
    # Valid Lineage
    ax.add_patch(patches.FancyBboxPatch((l_x, y_valid - 0.45), 3.2, 0.9, boxstyle="round,pad=0.1", linewidth=2.0, edgecolor=color_valid_border, facecolor=color_valid))
    ax.text(l_x + 1.6, y_valid, "$L_t = \mathcal{H}(H_t || L_{t-1})$\n(Correct Context)", ha='center', va='center', fontweight='bold', fontsize=10)
    
    # Invalid Lineage (Replay context)
    ax.add_patch(patches.FancyBboxPatch((l_x, y_replay - 0.45), 3.2, 0.9, boxstyle="round,pad=0.1", linewidth=2.0, edgecolor=color_invalid_border, facecolor=color_invalid))
    ax.text(l_x + 1.6, y_replay, "$L_t' = \mathcal{H}(H_t || L'_{t-1})$\n(WRONG CONTEXT)", ha='center', va='center', fontweight='bold', fontsize=10)
    
    # Divergence highlight
    ax.text(l_x + 1.6, 5, "LINEAGE DIVERGES", ha='center', va='center', fontweight='heavy', color=color_invalid_border, fontsize=14, bbox=dict(facecolor='white', edgecolor=color_invalid_border, boxstyle='round,pad=0.5'))

    # 4. STATE BINDING -> MESSAGE
    m_x = 11.5
    ax.add_patch(patches.FancyBboxPatch((m_x, y_valid - 0.4), 2.2, box_h, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_valid_border, facecolor=color_valid))
    ax.text(m_x + 1.1, y_valid, "Message $M_t$", ha='center', va='center', fontweight='bold', fontsize=10)
    
    ax.add_patch(patches.FancyBboxPatch((m_x, y_replay - 0.4), 2.2, box_h, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_invalid_border, facecolor=color_invalid))
    ax.text(m_x + 1.1, y_replay, "Message $M_t'$", ha='center', va='center', fontweight='bold', fontsize=10)

    # 5. VALIDATORS -> FINAL
    f_x = 14.8
    # Accept
    ax.text(17, y_valid, "ACCEPT", ha='center', va='center', fontweight='heavy', color=color_valid_border, fontsize=12, bbox=dict(facecolor=color_valid, edgecolor=color_valid_border, boxstyle='round,pad=0.5'))
    # Reject
    ax.text(17, y_replay, "REJECT", ha='center', va='center', fontweight='heavy', color=color_invalid_border, fontsize=12, bbox=dict(facecolor=color_invalid, edgecolor=color_invalid_border, boxstyle='round,pad=0.5'))

    # Connectors
    def connect(x1, y1, x2, y2, color, ls='-'):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle='->', lw=1.5, color=color, ls=ls))

    # Top Path
    connect(0.5 + box_w, y_valid, h_x, y_valid, color_valid_border)
    connect(h_x + box_w, y_valid, l_x, y_valid, color_valid_border)
    connect(l_x + 3.2, y_valid, m_x, y_valid, color_valid_border)
    connect(m_x + 2.2, y_valid, 16.2, y_valid, color_valid_border)

    # Bottom Path
    connect(0.5 + box_w, y_replay, h_x, y_replay, color_invalid_border)
    connect(h_x + box_w, y_replay, l_x, y_replay, color_invalid_border)
    connect(l_x + 3.2, y_replay, m_x, y_replay, color_invalid_border)
    connect(m_x + 2.2, y_replay, 16.2, y_replay, color_invalid_border)

    # Replay attempt arrow
    ax.annotate('ATTEMPTED REUSE', xy=(1.7, y_replay + 0.5), xytext=(1.7, y_valid - 0.5), 
                ha='center', va='center', arrowprops=dict(arrowstyle='->', lw=1.5, color=color_invalid_border, ls='--'), fontsize=8, color=color_invalid_border)

    # Annotations
    ax.text(9, 9.2, "LINEAGE BINDS DATA TO TEMPORAL CONTEXT", ha='center', fontweight='bold', fontsize=16, color=color_text)
    ax.text(9, 0.8, "REPLAY FAILS DUE TO LINEAGE DIVERGENCE ($L_t \\neq L_t'$)", ha='center', fontweight='bold', fontsize=15, color=color_invalid_border)

    plt.title("Replay Attack Prevention via Lineage Dependency", fontsize=20, pad=50, fontweight='bold', color=color_text)
    
    plt.tight_layout()
    plt.savefig('/Users/jitterx/Downloads/RCO_Patent_Documentation/figures/replay_prevention.png', bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    generate_replay_prevention_diagram()
