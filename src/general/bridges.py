from pathlib import Path
import matplotlib.pyplot as plt

def save_init_bridge(output_path):
    output_path = Path(output_path)

    plt.figure(figsize=(6, 3))
    plt.plot([0, 1], [0, 1], linewidth=3)
    plt.title("Initial Bridge")
    plt.xlabel("signal")
    plt.ylabel("continuation")
    plt.grid(True, alpha=0.3)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=180, bbox_inches="tight")
    plt.close()
