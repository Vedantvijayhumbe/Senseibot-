import gradio as gr

gr.load(
   "models/deepseek-ai/DeepSeek-R1",
   provider="replicate",
).launch()
