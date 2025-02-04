import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def add_noise(image, noise_level):
    """Adds Gaussian noise to an image."""
    noise = np.random.normal(0, noise_level, image.shape)
    noisy_image = np.clip(image + noise, 0, 255).astype(np.uint8)
    return noisy_image

# Load the uploaded image
image_path = "Dall-e2.webp"
image = Image.open(image_path).convert("RGB")
image = image.resize((128, 128))  # Resize for visualization
image = np.array(image)

# Number of diffusion steps
steps = 4  
fig, axes = plt.subplots(2, steps, figsize=(15, 6))

# Forward Process (Adding Noise)
for i in range(steps):
    noise_level = (i / (steps - 1)) * 300  # Gradual noise increase
    noisy_image = add_noise(image, noise_level)
    
    axes[0, i].imshow(noisy_image)
    axes[0, i].axis("off")
    axes[0, i].set_title(f"$x_{i}$", fontsize=12)

    if i < steps - 1:
        axes[0, i].annotate("", xy=(1.05, 0.5), xytext=(1.2, 0.5),
                             xycoords='axes fraction', textcoords='axes fraction',
                             arrowprops=dict(arrowstyle='<-', color='black', lw=1.5))

axes[0, 0].set_ylabel("Forward Process", fontsize=14, labelpad=15)

# Reverse Process (Denoising)
for i in range(steps):
    reverse_step = steps - 1 - i  # Reverse order
    noisy_image = add_noise(image, reverse_step * 80)
    
    axes[1, i].imshow(noisy_image)
    axes[1, i].axis("off")
    axes[1, i].set_title(f"$x_{reverse_step}$", fontsize=12)

    if i < steps - 1:
        axes[1, i].annotate("", xy=(1.05, 0.5), xytext=(1.2, 0.5),
                             xycoords='axes fraction', textcoords='axes fraction',
                             arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

axes[1, 0].set_ylabel("Reverse Process", fontsize=14, labelpad=15)

fig.suptitle("Diffusion Process Visualization", fontsize=16, fontweight='bold')
# Adjust layout for clarity
plt.tight_layout()

pdf_path = "./diffusion_process.pdf"
plt.savefig(pdf_path, bbox_inches='tight', format='pdf')
plt.show()

print(f"Saved visualization as {pdf_path}")
