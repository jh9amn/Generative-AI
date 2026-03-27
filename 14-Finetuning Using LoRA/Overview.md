# 🚀 The Ultimate Guide to LLM Optimization: Fine-Tuning & Quantization

As LLMs like **Gemma**, **Llama**, and **Mistral** grow larger, training them becomes expensive and memory-intensive. This guide explains how we use "math hacks" to make these models run on consumer hardware.

---

## 🏗️ 1. The Core Problem: VRAM & Weights
In a standard LLM, every "parameter" (weight) is usually stored in **FP32** (32-bit Floating Point).
* **Gemma 2B** has 2 billion parameters.
* $2,000,000,000 \times 4 \text{ bytes (FP32)} \approx 8 \text{ GB of VRAM}$ just to load the model.
* Training requires **3-4x** more memory for gradients and optimizer states.



---

## 📉 2. Quantization (The Shrinkage)
**Quantization** is the process of reducing the precision of the model's weights (e.g., from 16-bit to 8-bit or 4-bit).

### How it works:
Think of it like rounding a number. Instead of storing `3.14159265`, we store `3.1`. We lose a tiny bit of "intelligence" but save massive amounts of space.

* **FP16/BF16:** 2 bytes per parameter.
* **INT8:** 1 byte per parameter (50% savings).
* **INT4/NF4:** 0.5 bytes per parameter (75% savings).

> **Example:** Quantizing Gemma 2B to 4-bit reduces its size from **8GB** to roughly **1.5GB**, allowing it to run on a phone or a basic laptop.

---

## 🖇️ 3. LoRA: Low-Rank Adaptation
Standard fine-tuning updates **all** billions of parameters. **LoRA** changes the game by freezing the original model and only adding a tiny "adapter."

### The "Matrix" Secret:
Instead of updating a huge weight matrix $W$ of size $(d \times d)$, LoRA represents the change ($\Delta W$) as the product of two much smaller matrices, $A$ and $B$.

$$W_{updated} = W_{frozen} + (A \times B)$$

* **Rank ($r$):** The width of these small matrices. A rank of 4 or 8 is usually enough.
* **Trainable Params:** Typically $< 1\%$ of the original model.



---

## 🧪 4. QLoRA: The Best of Both Worlds
**QLoRA (Quantized LoRA)** is the state-of-the-art method that combines Quantization and LoRA.

1.  **Quantize** the base model to **4-bit** (NF4).
2.  **Freeze** those 4-bit weights.
3.  **Attach** LoRA adapters (in 16-bit) to the frozen 4-bit model.
4.  **Train** only the tiny adapters.

**Why use QLoRA?** It allows you to fine-tune a massive model (like Llama-70B) on a single professional GPU (like an A100) or a 7B model on a free Google Colab T4 GPU.

---

## 💻 5. Practical Example (Keras/Gemma)

Here is how the concepts translate into code using the libraries you've installed:

```python
import os
os.environ["KERAS_BACKEND"] = "jax"
import keras_hub

# 1. LOAD & QUANTIZE (The "Q" in QLoRA)
# Keras handles quantization during loading from presets
model = keras_hub.models.GemmaCausalLM.from_preset("gemma_2b_en")

# 2. APPLY LoRA (The "LoRA" part)
model.backbone.enable_lora(rank=4)

# 3. VERIFY
model.summary() 
# You will see: 
# Total params: 2.5 Billion
# Trainable params: 1.3 Million (The tiny adapters!)
```

---

## 📊 Summary Table

| Method | Base Model | Trainable Params | VRAM Usage | Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **Full Fine-Tuning** | 16-bit | 100% | Ultra High | Massive clusters, maximum accuracy. |
| **LoRA** | 16-bit | < 1% | Medium | Standard consumer GPUs. |
| **QLoRA** | 4-bit | < 1% | **Very Low** | Large models on limited hardware. |

---

### 🛠️ Setup Checklist for your Project
1. **Compute:** Use Google Colab (T4 GPU) or a local NVIDIA GPU.
2. **Libraries:** `keras-hub`, `jax[cpu]` or `jax[cuda]`.
3. **Data:** `databricks-dolly-15k.jsonl` (Instruction-Response format).

---
Since you're working on the **"14-Finetuning Using LoRA"** folder, here is the complete Python script to load that `databricks-dolly-15k.jsonl` file and prepare it specifically for the **Gemma** model.

I've added the **Quantization** and **LoRA** configuration so this acts as a "one-click" training starter.

---

### 🐍 `train_gemma_lora.py`

```python
import os
import json

# 1. SET BACKEND (Must be done BEFORE importing Keras)
os.environ["KERAS_BACKEND"] = "jax" 

import keras
import keras_hub

# 2. DATA LOADING & PREPROCESSING
def load_and_format_data(file_path, limit=1000):
    formatted_data = []
    print(f"Loading data from {file_path}...")
    
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            # Parse each line as a JSON object
            entry = json.loads(line)
            
            # Filter: We want simple Instruction -> Response pairs
            # We skip entries with extra 'context' to keep it simple for a 2B model
            if entry.get("context"):
                continue
                
            # Gemma works best with a consistent prompt template
            template = "Instruction:\n{instruction}\n\nResponse:\n{response}"
            formatted_data.append(template.format(**entry))
            
            if len(formatted_data) >= limit:
                break
                
    return formatted_data

# 3. INITIALIZE MODEL & LORA
print("Initializing Gemma 2B...")
# Load the model with pre-set weights
gemma_lm = keras_hub.models.GemmaCausalLM.from_preset("gemma_2b_en")

# ENABLE LoRA (This turns it into QLoRA if the model is quantized)
# rank=4 is computationally cheap and effective for 2B parameters
gemma_lm.backbone.enable_lora(rank=4)

# 4. CONFIGURATION
# Set the sequence length (lower = less VRAM used)
gemma_lm.preprocessor.sequence_length = 512

optimizer = keras.optimizers.Adam(learning_rate=5e-5)
gemma_lm.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=optimizer,
    weighted_metrics=[keras.metrics.SparseCategoricalAccuracy()],
)

# 5. START TRAINING
data = load_and_format_data("databricks-dolly-15k.jsonl")

print(f"Starting fine-tuning on {len(data)} examples...")
gemma_lm.fit(data, epochs=1, batch_size=1)

# 6. SAVE YOUR ADAPTERS
# This saves only the tiny LoRA weights, not the whole 8GB model
gemma_lm.save_weights("gemma_dolly_lora.weights.h5")
print("✅ Training complete! Weights saved.")
```

---

### 📊 Understanding the "Why"


* **`batch_size=1`**: Since you are running this locally in your `venv`, keeping the batch size at 1 prevents **Out of Memory (OOM)** errors on consumer GPUs.
* **`rank=4`**: This creates tiny "update" matrices. For Gemma 2B, this means you are only training about **1.5%** of the total parameters.
* **Encoding**: Always use `encoding="utf-8"` when reading JSONL files on Windows to avoid Unicode errors.

### 🛠️ Next Steps for your Project
1.  **Run a Test:** Run the script with `limit=10` just to make sure the loop works.
2.  **Inference:** After training, you can test it with:
    ```python
    response = gemma_lm.generate("Instruction:\nExplain AI to a 5 year old.\n\nResponse:\n", max_length=128)
    print(response)
    ```
