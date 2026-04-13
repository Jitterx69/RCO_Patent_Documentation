import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def generate_feedback_loop_diagram():
    # Setup figure and axis
    fig, ax = plt.subplots(figsize=(15, 12), dpi=300)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 11)
    ax.axis('off')

    # Color palette
    color_main = '#f8f9fa'
    color_border = '#6c757d'
    color_text = '#212529'
    color_valid = '#28a745'
    color_invalid = '#dc3545'
    color_highlight = '#007bff'

    # 1. CORE NODES (Circular arrangement)
    # Positions
    n_state_pos = (0, 7)
    n_telemetry_pos = (7, 3)
    n_rco_pos = (4, -4)
    n_transition_pos = (-5, -2)
    n_accepted_pos = (-2, 2)

    # State S_t
    ax.add_patch(patches.FancyBboxPatch((n_state_pos[0]-2, n_state_pos[1]-1), 4, 2, boxstyle="round,pad=0.2", linewidth=2.0, edgecolor=color_highlight, facecolor=color_main))
    ax.text(n_state_pos[0], n_state_pos[1], "System State $S_t$", ha='center', va='center', fontweight='bold', fontsize=14)

    # Telemetry Generation
    ax.add_patch(patches.FancyBboxPatch((n_telemetry_pos[0]-2, n_telemetry_pos[1]-1.5), 4, 3, boxstyle="round,pad=0.2", linewidth=1.5, edgecolor=color_border, facecolor=color_main))
    ax.text(n_telemetry_pos[0], n_telemetry_pos[1], "Telemetry\nGeneration\n$D_t = \mathcal{O}(S_t)$", ha='center', va='center', fontweight='bold', fontsize=12)

    # RCO Validation Box
    ax.add_patch(patches.FancyBboxPatch((n_rco_pos[0]-3, n_rco_pos[1]-2), 6, 4, boxstyle="round,pad=0.2", linewidth=2.0, edgecolor=color_highlight, facecolor=color_main))
    ax.text(n_rco_pos[0], n_rco_pos[1]+1, "RCO Validation Layer", ha='center', va='center', fontweight='heavy', fontsize=12, color=color_highlight)
    ax.text(n_rco_pos[0], n_rco_pos[1]-0.5, "Canonicalization\nHashing\nLineage\nState Binding\nValidators", ha='center', va='center', fontsize=9)

    # Accepted Input
    ax.add_patch(patches.FancyBboxPatch((n_accepted_pos[0]-2, n_accepted_pos[1]-1), 4, 2, boxstyle="round,pad=0.2", linewidth=1.5, edgecolor=color_valid, facecolor=color_main))
    ax.text(n_accepted_pos[0], n_accepted_pos[1]+0.3, "Valid $D_t^{validated}$", ha='center', va='center', fontweight='bold', fontsize=11, color=color_valid)

    # State Transition function F
    ax.add_patch(patches.FancyBboxPatch((n_transition_pos[0]-2, n_transition_pos[1]-1), 4, 2, boxstyle="round,pad=0.2", linewidth=1.5, edgecolor=color_highlight, facecolor=color_main))
    ax.text(n_transition_pos[0], n_transition_pos[1], "Transition\nFunction $\mathcal{F}$", ha='center', va='center', fontweight='bold', fontsize=12)

    # 2. CONNECTORS (Arrows)
    # S_t to Telemetry
    ax.annotate('', xy=(n_telemetry_pos[0], n_telemetry_pos[1]+1.5), xytext=(2, 7), arrowprops=dict(arrowstyle='->', lw=2, color=color_border, connectionstyle="arc3,rad=-0.2"))
    
    # Telemetry to RCO
    ax.annotate('', xy=(n_rco_pos[0]+2, n_rco_pos[1]+2), xytext=(n_telemetry_pos[0], n_telemetry_pos[1]-1.5), arrowprops=dict(arrowstyle='->', lw=2, color=color_border, connectionstyle="arc3,rad=-0.1"))

    # RCO to Accepted (Within Loop)
    ax.annotate('', xy=(n_accepted_pos[0]+1, n_accepted_pos[1]-1), xytext=(n_rco_pos[0]-1, n_rco_pos[1]+2), arrowprops=dict(arrowstyle='->', lw=2, color=color_valid, connectionstyle="arc3,rad=-0.2"))
    
    # Accepted to F
    ax.annotate('', xy=(n_transition_pos[0]+2, n_transition_pos[1]), xytext=(n_accepted_pos[0]-2, n_accepted_pos[1]), arrowprops=dict(arrowstyle='->', lw=2, color=color_valid))

    # F to S_t+1 (Closing Loop)
    ax.annotate('', xy=(n_state_pos[0]-1, n_state_pos[1]-1), xytext=(n_transition_pos[0], n_transition_pos[1]+1), arrowprops=dict(arrowstyle='->', lw=2.5, color=color_valid, connectionstyle="arc3,rad=-0.2"))
    ax.text(-5, 5, "$S_{t+1} = \mathcal{F}(S_t, D_t^{validated})$", ha='center', fontweight='bold', color=color_valid, fontsize=12, rotation=45)

    # 3. REJECTION PATH (Exiting Loop)
    ax.annotate('', xy=(8, -8), xytext=(n_rco_pos[0]+1, n_rco_pos[1]-2), arrowprops=dict(arrowstyle='->', lw=2, color=color_invalid, ls='--'))
    ax.text(8.5, -8, "REJECTED\nINPUT\n(Discarded)", ha='center', va='top', fontweight='bold', color=color_invalid, fontsize=11, bbox=dict(facecolor='white', edgecolor=color_invalid, boxstyle='round,pad=0.5'))

    # Annotations
    ax.text(0, 10.5, "SYSTEM EVOLVES ONLY THROUGH VALIDATED INPUTS", ha='center', fontweight='bold', fontsize=18, color=color_text)
    ax.text(0, -9.5, "CLOSED-LOOP ENFORCEMENT OF INTEGRITY DYNAMICS", ha='center', fontweight='bold', fontsize=14, color=color_border)

    plt.tight_layout()
    plt.savefig('/Users/jitterx/Downloads/RCO_Patent_Documentation/figures/feedback_system_loop.png', bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    generate_feedback_loop_diagram()
