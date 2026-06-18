#!/bin/bash
cd /home/administrator/clawfone-v2
export GEMINI_API_KEY=*** GEMINI_API_KEY /home/administrator/video-workflow/.env | cut -d'=' -f2)
python3 ~/.hermes/skills/openclaw-imports/nano-banana-pro/scripts/generate_image.py \
  --prompt "WWDC stage with Apple logo on left, smartphone with voice waves on right. Split comparison concept. Dark background with Apple silver on left and cyan on right. Clean editorial futuristic style. No text." \
  --filename "images/articles/wwdc-2026-ai-do-over-phone-agent.jpg" \
  --resolution 1K --aspect-ratio 16:9
