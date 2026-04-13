import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def generate_validator_consensus_diagram():
    # Setup figure and axis
    fig, ax = plt.subplots(figsize=(18, 10), dpi=300)
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Color palette
    color_main = '#f0f4f8'
    color_border = '#627d98'
    color_text = '#102a43'
    color_honest = '#e3f9e5'
    color_honest_border = '#38a169'
    color_adversarial = '#fff5f5'
    color_adversarial_border = '#e53e3e'

    # 1. MESSAGE INPUT
    ax.add_patch(patches.FancyBboxPatch((0.5, 4.5), 2.5, 1.0, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_border, facecolor=color_main))
    ax.text(1.75, 5, "Verification\nMessage $M_t$", ha='center', va='center', fontweight='bold', fontsize=12)
    
    # 2. VALIDATOR CLUSTER (Circular)
    center_x, center_y = 7, 5
    radius = 3
    num_validators = 7
    honest_indices = [0, 1, 3, 4, 6]
    adversarial_indices = [2, 5]
    
    validator_positions = []
    for i in range(num_validators):
        angle = 2 * np.pi * i / num_validators
        vx = center_x + radius * np.cos(angle)
        vy = center_y + radius * np.sin(angle)
        validator_positions.append((vx, vy))
        
        is_honest = i in honest_indices
        color = color_honest if is_honest else color_adversarial
        border = color_honest_border if is_honest else color_adversarial_border
        label = "Honest" if is_honest else "Adversarial"
        
        # Draw Validator Node
        circ = patches.Circle((vx, vy), 0.6, facecolor=color, edgecolor=border, lw=2, zorder=3)
        ax.add_patch(circ)
        ax.text(vx, vy, f"V_{i+1}\n({label})", ha='center', va='center', fontweight='bold', fontsize=8, zorder=4)
        
        # Arrow from M_t to each validator
        ax.annotate('', xy=(vx - 0.6, vy), xytext=(3.1, 5), arrowprops=dict(arrowstyle='->', lw=1, color=color_border, alpha=0.3, connectionstyle="arc3,rad=0.1"))

    # 3. AGGREGATION
    agg_x, agg_y = 13, 5
    ax.add_patch(patches.FancyBboxPatch((agg_x-1, agg_y-0.7), 2.5, 1.4, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_border, facecolor=color_main))
    ax.text(agg_x+0.25, agg_y, "Aggregation\n$\Sigma_t$", ha='center', va='center', fontweight='bold', fontsize=12)

    # Arrows from validators to aggregation
    for i, (vx, vy) in enumerate(validator_positions):
        is_honest = i in honest_indices
        color = color_honest_border if is_honest else color_adversarial_border
        ls = '-' if is_honest else '--'
        ax.annotate('', xy=(agg_x - 1, agg_y), xytext=(vx + 0.6, vy), arrowprops=dict(arrowstyle='->', lw=1.5, color=color, ls=ls, alpha=0.6))
        
        if not is_honest:
            # Add X over adversarial signatures
            ax.text((vx + agg_x)/2, (vy + agg_y)/2, "X", color=color_adversarial_border, fontweight='heavy', fontsize=15, ha='center')

    # 4. THRESHOLD CHECK
    check_x = 15.5
    ax.add_patch(patches.FancyBboxPatch((check_x, agg_y - 0.5), 2.0, 1.0, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_border, facecolor=color_main))
    ax.text(check_x + 1.0, agg_y, "Threshold\nCheck\n$t = 5$ of $7$", ha='center', va='center', fontweight='bold', fontsize=10)
    ax.annotate('', xy=(check_x, agg_y), xytext=(agg_x + 1.6, agg_y), arrowprops=dict(arrowstyle='->', lw=1.5, color=color_border))

    # 5. FINAL DECISION
    # Accept
    ax.text(17.5, agg_y + 1.5, "ACCEPT", ha='center', va='center', fontweight='heavy', color=color_honest_border, fontsize=12, bbox=dict(facecolor=color_honest, edgecolor=color_honest_border, boxstyle='round,pad=0.5'))
    ax.annotate('', xy=(17.5, agg_y + 1.0), xytext=(check_x + 1.0, agg_y + 0.5), arrowprops=dict(arrowstyle='->', lw=1.5, color=color_honest_border))
    
    # Annotations
    ax.text(9, 9.2, "SYSTEM REMAINS SECURE IF $f < t$", ha='center', fontweight='bold', fontsize=16, color=color_text)
    ax.text(9, 0.8, "ADVERSARIAL VALIDATORS CANNOT INFLUENCE OUTCOME BELOW THRESHOLD", ha='center', fontweight='bold', fontsize=12, color=color_border)
    
    # Equation
    ax.text(9, 8.2, r"$t = \lfloor \frac{2n}{3} \rfloor + 1$", fontsize=18, ha='center', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

    plt.title("Distributed Validator Consensus and Threshold Security Model", fontsize=20, pad=50, fontweight='bold', color=color_text)
    
    plt.tight_layout()
    plt.savefig('/Users/jitterx/Downloads/RCO_Patent_Documentation/figures/validator_consensus.png', bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    generate_validator_consensus_diagram()
