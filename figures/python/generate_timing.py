import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_timing_comparison():
    # Setup figure and axis
    fig, ax = plt.subplots(figsize=(18, 12), dpi=300)
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 12)
    ax.axis('off')

    # Color palette
    color_main = '#f0f4f8'
    color_border = '#627d98'
    color_text = '#102a43'
    color_risk = '#fff5f5'
    color_risk_border = '#e53e3e'
    color_secure = '#e3f9e5'
    color_secure_border = '#38a169'

    box_w = 3.2
    box_h = 1.0
    y_trad = 9
    y_rco = 3

    # --- TOP SECTION: TRADITIONAL SYSTEMS ---
    ax.text(9, y_trad + 2, "TRADITIONAL TELEMETRY / LOGGING SYSTEMS", ha='center', fontweight='bold', fontsize=16, color=color_text)
    
    # 1. Input
    ax.add_patch(patches.FancyBboxPatch((0.5, y_trad - 0.5), box_w, box_h, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_border, facecolor=color_main))
    ax.text(2.1, y_trad, "Telemetry\nInput $D_t$", ha='center', va='center', fontweight='bold', fontsize=11)
    
    # 2. Storage (The Risk Point)
    ax.add_patch(patches.FancyBboxPatch((4.5, y_trad - 0.5), box_w, box_h, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_risk_border, facecolor=color_risk))
    ax.text(6.1, y_trad, "Storage\n(Unverified Data)", ha='center', va='center', fontweight='bold', fontsize=11)
    ax.text(6.1, y_trad - 0.8, "⚠ Malicious data stored", ha='center', va='center', color=color_risk_border, fontsize=9, fontweight='bold')
    
    # 3. Post-hoc
    ax.add_patch(patches.FancyBboxPatch((8.5, y_trad - 0.5), box_w, box_h, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_border, facecolor=color_main))
    ax.text(10.1, y_trad, "Post-hoc\nValidation", ha='center', va='center', fontweight='bold', fontsize=11)
    
    # 4. Detection
    ax.add_patch(patches.FancyBboxPatch((12.5, y_trad - 0.5), box_w, box_h, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_border, facecolor=color_main))
    ax.text(14.1, y_trad, "Detection\nof Issues", ha='center', va='center', fontweight='bold', fontsize=11)
    
    # Note
    ax.text(9, y_trad - 1.8, "DETECTION OCCURS AFTER INGESTION", ha='center', fontweight='bold', color=color_risk_border, fontsize=12)

    # --- BOTTOM SECTION: RCO PROTOCOL ---
    ax.text(9, y_rco + 2.5, "RCO PROTOCOL (PRE-INGESTION VALIDATION)", ha='center', fontweight='bold', fontsize=16, color=color_text)
    
    # 1. Input
    ax.add_patch(patches.FancyBboxPatch((0.5, y_rco - 0.5), box_w, box_h, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_border, facecolor=color_main))
    ax.text(2.1, y_rco, "Telemetry\nInput $D_t$", ha='center', va='center', fontweight='bold', fontsize=11)
    
    # 2. Pipeline (The Enforcer)
    ax.add_patch(patches.FancyBboxPatch((4.5, y_rco - 0.7), box_w + 1, 1.4, boxstyle="round,pad=0.1", linewidth=2.0, edgecolor=color_secure_border, facecolor=color_secure))
    ax.text(6.6, y_rco, "RCO Validation\nPipeline", ha='center', va='center', fontweight='heavy', fontsize=12)
    ax.text(6.6, y_rco - 0.45, "Canonicalization → Hash\nLineage → State Binding", ha='center', va='center', fontsize=8)
    
    # Decision Split
    # Valid
    ax.add_patch(patches.FancyBboxPatch((10.5, y_rco + 0.5), box_w, box_h, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_secure_border, facecolor=color_secure))
    ax.text(12.1, y_rco + 1, "Storage\n(Only Verified)", ha='center', va='center', fontweight='bold', fontsize=11)
    ax.text(12.1, y_rco + 1.8, "✔ Validated Data Only", ha='center', va='center', color=color_secure_border, fontsize=9, fontweight='bold')
    
    # Invalid
    ax.add_patch(patches.FancyBboxPatch((10.5, y_rco - 1.5), box_w, box_h, boxstyle="round,pad=0.1", linewidth=1.5, edgecolor=color_risk_border, facecolor=color_risk))
    ax.text(12.1, y_rco - 1, "REJECTED\n(Not Stored)", ha='center', va='center', fontweight='bold', fontsize=11)
    
    # Note
    ax.text(6.6, y_rco - 1.8, "VALIDATION OCCURS BEFORE INGESTION", ha='center', fontweight='bold', color=color_secure_border, fontsize=12)

    # --- CENTER LABEL ---
    ax.text(9, 6, "CORE INNOVATION: VALIDATION TIMING", ha='center', va='center', fontweight='heavy', fontsize=18, color='#00d2ff', bbox=dict(facecolor='white', edgecolor='#00d2ff', boxstyle='round,pad=0.8', lw=2))

    # Arrows
    def arrow(x1, y1, x2, y2, color):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle='->', lw=1.5, color=color))

    # Trad Arrows
    arrow(3.7, y_trad, 4.5, y_trad, color_border)
    arrow(7.7, y_trad, 8.5, y_trad, color_border)
    arrow(11.7, y_trad, 12.5, y_trad, color_border)

    # RCO Arrows
    arrow(3.7, y_rco, 4.5, y_rco, color_border)
    ax.annotate('', xy=(10.5, y_rco + 1), xytext=(8.7, y_rco), arrowprops=dict(arrowstyle='->', lw=1.5, color=color_secure_border, connectionstyle="angle,angleA=0,angleB=90,rad=10"))
    ax.annotate('', xy=(10.5, y_rco - 1), xytext=(8.7, y_rco), arrowprops=dict(arrowstyle='->', lw=1.5, color=color_risk_border, connectionstyle="angle,angleA=0,angleB=-90,rad=10"))

    plt.title("Validation Timing: Traditional Systems vs RCO Protocol", fontsize=20, pad=60, fontweight='bold', color=color_text)
    
    plt.tight_layout()
    plt.savefig('/Users/jitterx/Downloads/RCO_Patent_Documentation/figures/validation_timing.png', bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    generate_timing_comparison()
