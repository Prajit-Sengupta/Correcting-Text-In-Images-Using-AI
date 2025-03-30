# Correcting Text in Images Using AI

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/Prajit-Sengupta/Correcting-Text-In-Images-Using-AI)

**Publication**  
Our paper related to this project:   
[https://www.techrxiv.org/doi/full/10.36227/techrxiv.174319638.82772972/v1](https://www.techrxiv.org/doi/full/10.36227/techrxiv.174319638.82772972/v1)  

Let me know if you need any modifications!

## Overview
This project focuses on AI-based text correction in images. It utilizes OCR (TrOCR) for text extraction, BLIP-2 for correction, and Stable Diffusion for inpainting. The evaluation involves mathematical optimization techniques and metrics such as CLIP, GIQA, FID, and T-IQA for comparative analysis.

## Repository Structure

```
.
├── .github                 # GitHub-specific configurations
├── Corrected_Images        # Folder containing corrected images
├── Evaluation              # Jupyter notebooks for evaluation
│   ├── Ablation_Eval.ipynb       # Ablation study and evaluation
│   ├── Evaluation.ipynb          # General evaluation notebook
│   ├── TextLength_Eval.ipynb     # Evaluation based on text length
├── Incorrect_Images        # Folder containing incorrect images before correction
├── TextSynth_Dataset       # Dataset used for evaluation
│   ├── Copilot(Microsoft)  # Text-generated images by Copilot
│   ├── Dall-E3(ChatGpt)    # Text-generated images by DALL·E 3
│   ├── Emu(MetaAI)         # Text-generated images by Meta AI's Emu
│   ├── Imagen(Gemini)      # Text-generated images by Google's Imagen (Gemini)
├── .gitignore              # Git ignore file
├── corrected.png           # Sample corrected image
├── diffsuion.py            # Script for text inpainting using Stable Diffusion
├── diffusion_process.pdf   # Documentation on diffusion process used
├── GenFix.ipynb            # Jupyter notebook for text correction using generative models
├── ISO3.ipynb              # Notebook exploring ISO-3 analysis
├── merge.py                # Script to merge images or outputs
├── merged_output.png       # Sample merged output image
├── README.md               # Project documentation
├── TextSynth_Dataset.zip   # Zipped version of the dataset
```

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Prajit-Sengupta/Correcting-Text-In-Images-Using-AI.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the pipeline:
   ```bash
   python GenFix.ipynb
   ```

## Features
- **OCR Processing**: Extracts text from images using TrOCR.
- **Text Correction**: Uses BLIP-2 for enhanced text correction.
- **Text Inpainting**: Stable Diffusion is used to correct text in images.
- **Evaluation Metrics**: Includes CLIP, GIQA, FID, and T-IQA for quality assessment.
- **Comparative Analysis**: Ablation studies and benchmarking against different generative models.

## Usage
- **Text Correction:** Run `GenFix.ipynb` to process and correct images.
- **Evaluation:** Open `Evaluation` and can run either of the notebook cells to genrate scores : `Evaluation.ipynb`, `Ablation_Eval.ipynb` and `TextLength_Eval.ipynb`.
- **Dataset Preparation:** Extract and preprocess datasets from `TextSynth_Dataset.zip`.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- OpenAI for DALL·E 3 and ChatGPT.
- Microsoft for Copilot.
- Meta AI for Emu.
- Google for Imagen (Gemini).

