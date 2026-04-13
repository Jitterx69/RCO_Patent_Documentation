import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_sdk_model_diagram():
    # Setup figure and axis
    fig, ax = plt.subplots(figsize=(20, 12), dpi=300)
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 12)
    ax.axis('off')

    # Color palette
    color_main = '#f8f9fa'
    color_border = '#adb5bd'
    color_text = '#212529'
    color_sdk = '#007bff'
    color_api = '#6c757d'
    color_valid = '#28a745'

    # --- PANEL TITLES ---
    ax.text(3.5, 11, "MICROSERVICES", ha='center', fontweight='bold', fontsize=14, color=color_text)
    ax.text(10, 11, "STREAMING / EVENT-DRIVEN", ha='center', fontweight='bold', fontsize=14, color=color_text)
    ax.text(16.5, 11, "GATEWAY / MIDDLEWARE", ha='center', fontweight='bold', fontsize=14, color=color_text)

    # --- DIVIDERS ---
    ax.axvline(6.8, 0.2, 0.9, color=color_border, ls='--', alpha=0.5)
    ax.axvline(13.2, 0.2, 0.9, color=color_border, ls='--', alpha=0.5)

    # --- LEFT PANEL: MICROSERVICES ---
    services = ["Service A", "Service B", "Service C"]
    y_pos = [9, 7.5, 6]
    for i, s in enumerate(services):
        # Service Box
        ax.add_patch(patches.FancyBboxPatch((1, y_pos[i]-0.4), 4.5, 0.8, boxstyle="round,pad=0.1", linewidth=1, edgecolor=color_border, facecolor=color_main))
        ax.text(2.2, y_pos[i], s, ha='center', va='center', fontweight='bold', fontsize=10)
        # Embedded SDK
        ax.add_patch(patches.Rectangle((3.8, y_pos[i]-0.3), 1.5, 0.6, facecolor=color_sdk, alpha=0.1, edgecolor=color_sdk, lw=1))
        ax.text(4.55, y_pos[i], "RCO SDK", ha='center', va='center', weight='bold', size=7, color=color_sdk)
        # Arrow to API
        ax.annotate('', xy=(9, 4.5), xytext=(5.3, y_pos[i]), arrowprops=dict(arrowstyle='->', lw=1.2, color=color_valid, alpha=0.6))

    ax.text(3.5, 5.0, "Independent Validation\nper Service", ha='center', fontsize=9, style='italic', color=color_api)

    # --- CENTER PANEL: STREAMING ---
    # Producer
    ax.add_patch(patches.FancyBboxPatch((8, 9.5), 4, 0.8, boxstyle="round,pad=0.1", linewidth=1, edgecolor=color_border, facecolor=color_main))
    ax.text(10, 9.9, "Event Producer", ha='center', va='center', fontweight='bold', fontsize=10)
    
    # Queue
    ax.add_patch(patches.Rectangle((8.5, 8.2), 3, 0.6, facecolor='#e9ecef', edgecolor=color_border, lw=1))
    ax.text(10, 8.5, "Message Stream (Kafka)", ha='center', va='center', fontsize=8)
    ax.annotate('', xy=(10, 8.2), xytext=(10, 9.5), arrowprops=dict(arrowstyle='->', lw=1.2, color=color_border))

    # Stream Processor
    ax.add_patch(patches.FancyBboxPatch((8, 6.5), 4, 1.2, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_border, facecolor=color_main))
    ax.text(10, 7.3, "Stream Processor", ha='center', va='center', fontweight='bold', fontsize=10)
    ax.add_patch(patches.Rectangle((8.5, 6.7), 3, 0.4, facecolor=color_sdk, alpha=0.1, edgecolor=color_sdk, lw=1))
    ax.text(10, 6.9, "RCO SDK", ha='center', va='center', weight='bold', size=8, color=color_sdk)
    
    ax.annotate('', xy=(10, 7.7), xytext=(10, 8.2), arrowprops=dict(arrowstyle='->', lw=1.2, color=color_border))
    ax.annotate('', xy=(10, 5.3), xytext=(10, 6.5), arrowprops=dict(arrowstyle='->', lw=1.2, color=color_valid))

    ax.text(10, 5.8, "Validation in-stream", ha='center', fontsize=9, style='italic', color=color_api)

    # --- RIGHT PANEL: GATEWAY ---
    # Devices
    ax.text(16.5, 10, "External SDK / Devices", ha='center', fontsize=9, color=color_api)
    for i in range(3):
        ax.add_patch(patches.Circle((15+i*1.5, 9.2), 0.3, facecolor=color_main, edgecolor=color_border))
    
    # Gateway
    ax.add_patch(patches.FancyBboxPatch((15, 6.5), 3, 2, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_border, facecolor=color_main))
    ax.text(16.5, 7.8, "Gateway / Proxy", ha='center', fontweight='bold', fontsize=10)
    ax.add_patch(patches.Rectangle((15.5, 6.8), 2, 0.6, facecolor=color_sdk, alpha=0.1, edgecolor=color_sdk, lw=1))
    ax.text(16.5, 7.1, "RCO SDK", ha='center', va='center', weight='bold', size=8, color=color_sdk)

    # Arrows
    ax.annotate('', xy=(16.5, 8.5), xytext=(16.5, 9.0), arrowprops=dict(arrowstyle='->', lw=1.2, color=color_border))
    ax.annotate('', xy=(14.5, 4.8), xytext=(15.5, 6.5), arrowprops=dict(arrowstyle='->', lw=1.2, color=color_valid, connectionstyle="arc3,rad=0.2"))

    ax.text(16.5, 5.8, "Centralized Entry Validation", ha='center', fontsize=9, style='italic', color=color_api)

    # --- SHARED BOTTOM: RCO API ---
    ax.add_patch(patches.FancyBboxPatch((2, 2), 16, 2.5, boxstyle="round,pad=0.1", linewidth=2.0, edgecolor=color_api, facecolor='#f1f3f5'))
    ax.text(10, 3.8, "RCO API & VALIDATION FABRIC", ha='center', fontweight='heavy', fontsize=16, color=color_text)
    ax.text(10, 3.0, "Processing Pipeline → Distributed Validators → Signature Aggregation → Proof", ha='center', fontsize=11, color=color_api)

    # Annotation
    ax.text(10, 1.2, "SDK acts as the abstraction layer, managing retries, lineage tracking, and protocol bindings.", ha='center', fontsize=12, fontweight='bold', color=color_sdk)

    plt.title("SDK Integration Model Across System Architectures", fontsize=22, pad=60, fontweight='bold', color=color_text)
    
    plt.tight_layout()
    plt.savefig('/Users/jitterx/Downloads/RCO_Patent_Documentation/figures/sdk_integration_model.png', bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    generate_sdk_model_diagram()
