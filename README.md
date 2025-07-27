# 🧑‍⚖️ Legal Assistant: Fine-Tuned Phi-2 with LoRA

A lightweight legal assistant chatbot fine-tuned on [Lawyer-Instruct](https://huggingface.co/datasets/Alignment-Lab-AI/Lawyer-Instruct) using **LoRA + Phi-2**, deployed with a clean Streamlit UI. It answers legal questions clearly, accurately, and concisely based on civil law instructions.

## 📌 Features

- ✅ Fine-tuned [`microsoft/phi-2`](https://huggingface.co/microsoft/phi-2) with [LoRA](https://arxiv.org/abs/2106.09685)
- ✅ Dataset: [Lawyer-Instruct](https://huggingface.co/datasets/Alignment-Lab-AI/Lawyer-Instruct)
- ✅ Merged and exported final model: [🧠 Hugging Face Model Card](https://huggingface.co/Jasur05/phi2-legal)
- ✅ Fast, Streamlit-based frontend
- ✅ Output formatting, fallback messages, and prompt engineering

---

## 🚀 Demo

Launch the app locally:

```bash
git clone https://github.com/your-username/phi2-legal-assistant
cd phi2-legal-assistant
pip install -r requirements.txt
streamlit run app.py
