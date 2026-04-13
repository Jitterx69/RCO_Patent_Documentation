import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_topology_diagram():
    # Setup figure and axis
    fig, ax = plt.subplots(figsize=(20, 12), dpi=300)
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 12)
    ax.axis('off')

    # Color palette
    color_main = '#f8f9fa'
    color_border = '#adb5bd'
    color_text = '#212529'
    color_edge = '#e9ecef'
    color_cloud = '#f1f3f5'
    color_highlight = '#007bff'
    color_success = '#28a745'
    
    # 1. LAYERS / REGIONS (Backgrounds)
    # Edge Region
    ax.add_patch(patches.Rectangle((0.2, 0.5), 5.5, 11, facecolor=color_edge, edgecolor=color_border, ls='--', alpha=0.3))
    ax.text(3, 11.2, "EDGE REGION / PRODUCER LAYER", ha='center', fontweight='bold', fontsize=14, color=color_text)
    
    # Cloud Region
    ax.add_patch(patches.Rectangle((6.2, 0.5), 13.5, 11, facecolor=color_cloud, edgecolor=color_border, ls='--', alpha=0.3))
    ax.text(13, 11.2, "CLOUD REGION / FABRIC LAYER", ha='center', fontweight='bold', fontsize=14, color=color_text)

    # 2. EDGE PRODUCERS
    producers = ["Sensor Node", "IoT Device", "Application", "Edge Collector"]
    y_pos = [9, 7, 5, 3]
    for i, p in enumerate(producers):
        ax.add_patch(patches.FancyBboxPatch((1, y_pos[i]-0.5), 2.5, 0.8, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_border, facecolor=color_main))
        ax.text(2.25, y_pos[i], p, ha='center', va='center', fontweight='bold', fontsize=10)
        # Arrows to gateway
        ax.annotate('', xy=(6.5, 6), xytext=(3.6, y_pos[i]), arrowprops=dict(arrowstyle='->', lw=1.2, color=color_border))

    # 3. API & INGESTION (In Cloud)
    ax.add_patch(patches.FancyBboxPatch((6.5, 5), 2.5, 2, boxstyle="round,pad=0.1", linewidth=2.0, edgecolor=color_highlight, facecolor=color_main))
    ax.text(7.75, 6.4, "Ingestion Service", ha='center', fontweight='bold', fontsize=11, color=color_highlight)
    ax.text(7.75, 5.6, "Canonicalization\nHashing\nLineage\nState Binding", ha='center', fontsize=8)

    # 4. VALIDATOR FABRIC
    val_center_x, val_center_y = 12, 6
    val_radius = 2.5
    num_vals = 6
    for i in range(num_vals):
        import numpy as np
        angle = 2 * np.pi * i / num_vals
        vx = val_center_x + val_radius * np.cos(angle)
        vy = val_center_y + val_radius * np.sin(angle)
        
        ax.add_patch(patches.Circle((vx, vy), 0.5, facecolor=color_main, edgecolor=color_highlight, lw=1.5))
        ax.text(vx, vy, f"Val_{i+1}", ha='center', va='center', fontsize=8, fontweight='bold')
        
        # Connect from Ingestion
        ax.annotate('', xy=(vx-0.5, vy), xytext=(9.1, 6), arrowprops=dict(arrowstyle='->', lw=0.8, color=color_highlight, alpha=0.4))

    ax.text(val_center_x, val_center_y + 3.2, "VALIDATOR FABRIC", ha='center', fontweight='bold', fontsize=12)
    ax.text(val_center_x, val_center_y, "Distributed Independent\nVerification", ha='center', va='center', fontsize=8, color=color_highlight)

    # 5. AGGREGATION & VERIFICATION
    agg_x = 12
    ax.add_patch(patches.FancyBboxPatch((agg_x-1.5, 2), 3, 1, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_highlight, facecolor=color_main))
    ax.text(agg_x, 2.5, "Aggregation &\nVerification Engine", ha='center', va='center', fontweight='bold', fontsize=10)
    
    # Arrows from fabric to agg
    ax.annotate('', xy=(agg_x, 3.1), xytext=(val_center_x, 4.5), arrowprops=dict(arrowstyle='->', lw=1.5, color=color_highlight))

    # 6. PERSISTENCE LAYER
    color_success_border = '#28a745'
    ax.add_patch(patches.FancyBboxPatch((16.5, 6), 3, 1, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_success_border, facecolor=color_main))
    ax.text(18, 6.5, "Append-Only\nAudit Log", ha='center', va='center', fontweight='bold', fontsize=10)
    
    ax.add_patch(patches.FancyBboxPatch((16.5, 3), 3, 1, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_success_border, facecolor=color_main))
    ax.text(18, 3.5, "Audit Query\nService", ha='center', va='center', fontweight='bold', fontsize=10)

    # Final Arrows
    ax.annotate('', xy=(16.5, 5), xytext=(13.6, 2.8), arrowprops=dict(arrowstyle='->', lw=2.0, color=color_success_border, connectionstyle="angle3,angleA=0,angleB=90"))
    ax.text(15.2, 4.5, "Only Validated\nPersisted", ha='center', fontsize=9, fontweight='bold', color=color_success_border)

    plt.title("Distributed Deployment Topology of the RCO Protocol", fontsize=22, pad=60, fontweight='bold', color=color_text)
    
    plt.tight_layout()
    plt.savefig('/Users/jitterx/Downloads/RCO_Patent_Documentation/figures/deployment_topology.png', bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    generate_topology_diagram()
