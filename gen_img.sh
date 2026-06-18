#!/bin/bash
cd /home/administrator/clawfone-v2
export GEMINI_API_KEY=$(grep GEMINI_API_KEY /home/administrator/video-workflow/.env | cut -d'=' -f2)
python3 ~/.hermes/skills/openclaw-imports/nano-banana-pro/scripts/generate_image.py \
  --prompt "VS comparison: left side Google cloud server with blue glow, right side smartphone with cyan voice waves. Lightning bolt between them. Dark background. Clean editorial futuristic style. No text." \
  --filename "images/articles/gemini-spark-vs-foneclaw.jpg" \
  --resolution 1K --aspect-ratio 16:9
