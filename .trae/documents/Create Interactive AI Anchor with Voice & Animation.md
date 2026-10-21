I will upgrade your system to create a functioning **AI Anchor Prototype**. Since generating full AI video (like HeyGen/Sora) requires expensive paid APIs, I will build a **Real-Time Interactive Anchor** using the following approach:

1.  **Voice Synthesis (TTS)**:
    *   Integrate `gTTS` (Google Text-to-Speech) to convert your optimized scripts into professional-grade audio.
    *   The voice will effectively "read" the news script.

2.  **Visual Avatar Interface**:
    *   Update the UI to display a professional "News Anchor" avatar.
    *   Implement a **Lip-Sync Simulation**: The avatar's mouth/visuals will animate in real-time while the audio plays, creating the illusion of a talking anchor.

3.  **Workflow Integration**:
    *   When you click "Process", the system will now:
        1.  Analyze & Rewrite the script.
        2.  **Generate Audio** for the optimized script.
        3.  **Launch the Avatar** to deliver the news immediately.

### Implementation Steps
1.  **Backend**: Install `gTTS`, update `models.py` to support audio outputs, and implement audio generation in `engine.py`.
2.  **Frontend**: Create a "News Room" view in `index.html` with an avatar image and audio-reactive animations.
3.  **Verify**: Run a test to ensure the anchor "speaks" the text correctly.