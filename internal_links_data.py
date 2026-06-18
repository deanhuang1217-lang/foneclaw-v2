# Internal links mapping for FoneClaw articles
# Format: slug -> [(link_text, target_url), ...]
# Each article should have 3-5 internal links
# This file is loaded by build_multi.py and injected into article HTML

INTERNAL_LINKS = {
    # Batch 1: How-To Guides
    'howto_voice_android': [
        ('hands-free driving commands', '/voice-commands-driving.html'),
        ('senior-friendly setup guide', '/ai-phone-seniors.html'),
        ('texting without touching', '/send-texts-hands-free.html'),
    ],
    'howto_texts_handsfree': [
        ('voice control basics', '/voice-control-android.html'),
        ('driving safety commands', '/voice-commands-driving.html'),
        ('multi-step automation', '/automate-multi-step-tasks.html'),
    ],
    'howto_multistep': [
        ('voice control foundation', '/voice-control-android.html'),
        ('driving scenarios', '/voice-commands-driving.html'),
        ('smart home integration', '/smart-home-voice-control.html'),
    ],
    'howto_elderly_setup': [
        ('voice control basics', '/voice-control-android.html'),
        ('senior phone features', '/ai-phone-seniors.html'),
        ('accessibility options', '/voice-control-visually-impaired.html'),
    ],
    
    # Batch 2: Use Cases
    'howto_driving_voice': [
        ('core voice commands', '/voice-control-android.html'),
        ('hands-free texting', '/send-texts-hands-free.html'),
        ('emergency features', '/emergency-voice-commands.html'),
    ],
    'howto_smart_home': [
        ('voice control basics', '/voice-control-android.html'),
        ('driving integration', '/voice-commands-driving.html'),
        ('senior accessibility', '/ai-phone-seniors.html'),
    ],
    'uc_commuting': [
        ('voice control setup', '/voice-control-android.html'),
        ('driving safety', '/voice-commands-driving.html'),
        ('hands-free messaging', '/send-texts-hands-free.html'),
    ],
    'uc_seniors': [
        ('voice control guide', '/voice-control-android.html'),
        ('elderly setup guide', '/voice-control-elderly.html'),
        ('visual accessibility', '/voice-control-visually-impaired.html'),
    ],
    
    # Batch 3: More Use Cases
    'uc_cooking': [
        ('voice control basics', '/voice-control-android.html'),
        ('smart home commands', '/smart-home-voice-control.html'),
        ('hands-free texting', '/send-texts-hands-free.html'),
    ],
    'uc_emergency': [
        ('voice control setup', '/voice-control-android.html'),
        ('driving emergencies', '/voice-commands-driving.html'),
        ('senior safety', '/ai-phone-seniors.html'),
    ],
    'uc_productivity': [
        ('voice control basics', '/voice-control-android.html'),
        ('task automation', '/automate-multi-step-tasks.html'),
        ('driving productivity', '/voice-commands-driving.html'),
    ],
    'uc_visual_impaired': [
        ('voice control setup', '/voice-control-android.html'),
        ('senior accessibility', '/ai-phone-seniors.html'),
        ('elderly phone guide', '/voice-control-elderly.html'),
    ],
    
    # Batch 4: Comparisons
    'uc_parenting': [
        ('voice control basics', '/voice-control-android.html'),
        ('kitchen voice commands', '/hands-free-cooking.html'),
        ('hands-free texting', '/send-texts-hands-free.html'),
    ],
    'uc_fitness': [
        ('voice control setup', '/voice-control-android.html'),
        ('driving commands', '/voice-commands-driving.html'),
        ('smart home fitness', '/smart-home-voice-control.html'),
    ],
    'comp_vs_siri': [
        ('Android voice control', '/voice-control-android.html'),
        ('vs Google Assistant', '/foneclaw-vs-google-assistant.html'),
        ('vs Alexa', '/foneclaw-vs-alexa.html'),
    ],
    'comp_vs_google': [
        ('voice control basics', '/voice-control-android.html'),
        ('vs Siri comparison', '/foneclaw-vs-siri.html'),
        ('vs Alexa comparison', '/foneclaw-vs-alexa.html'),
    ],
    
    # Batch 5: More Comparisons
    'comp_vs_alexa': [
        ('Android voice control', '/voice-control-android.html'),
        ('vs Siri comparison', '/foneclaw-vs-siri.html'),
        ('vs Google comparison', '/foneclaw-vs-google-assistant.html'),
    ],
    'comp_best_apps': [
        ('voice control basics', '/voice-control-android.html'),
        ('vs Siri comparison', '/foneclaw-vs-siri.html'),
        ('senior accessibility', '/ai-phone-seniors.html'),
    ],
    'comp_ai_replacing': [
        ('voice control basics', '/voice-control-android.html'),
        ('AI agent comparison', '/ai-agent-vs-traditional-apps.html'),
        ('top AI agents', '/top-10-ai-agents-2026.html'),
    ],
    
    # Batch 7: Standalone articles
    'ai-agent-vs-traditional-apps': [
        ('voice control basics', '/voice-control-android.html'),
        ('AI agent ranking', '/top-10-ai-agents-2026.html'),
        ('Hermes comparison', '/hermes-agent-vs-openclaw-vs-foneclaw.html'),
    ],
    'tasker-alternative-voice-automation': [
        ('voice control basics', '/voice-control-android.html'),
        ('multi-step automation', '/automate-multi-step-tasks.html'),
        ('smart home control', '/smart-home-voice-control.html'),
    ],
    'voice-assistant-privacy-security': [
        ('voice control basics', '/voice-control-android.html'),
        ('driving privacy', '/voice-commands-driving.html'),
        ('senior privacy', '/ai-phone-seniors.html'),
    ],
    'voice-control-dirty-hands': [
        ('voice control basics', '/voice-control-android.html'),
        ('cooking commands', '/hands-free-cooking.html'),
        ('driving commands', '/voice-commands-driving.html'),
    ],
}
