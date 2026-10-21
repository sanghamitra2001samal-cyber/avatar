To make the AI Avatar act more human and perform gestures, I will upgrade the frontend to a **Multi-Layered Animation System**. Instead of a static image, we will simulate "live" movement using CSS composites and JavaScript state management.

### The "Human-Like" Upgrade Plan

1.  **Visual Architecture (Frontend)**:
    *   **Layered Composition**: Split the avatar into **Body**, **Head**, and **Hands** (using overlaid assets).
    *   **State Machine**: Implement states: `IDLE` (Breathing, Blinking), `SPEAKING` (Head bob, Mouth sync), and `GESTURING` (Hand movements).
    *   **Camera Dynamics**: Add subtle "Camera Shake" and "Slow Zoom" to simulate a real cameraman.

2.  **Gesture Logic (Backend -> Frontend)**:
    *   The **Engine** will calculate a `gesture_density` based on the **Tone** (e.g., "Energetic" = high frequency, "Serious" = low).
    *   The **Frontend Director** will randomly trigger specific gestures (e.g., "Hand Raise", "Open Palm", "Point") during playback, synchronized with the audio flow.

3.  **Implementation Steps**:
    *   **Update Engine**: Add `gesture_config` to the output.
    *   **Update Frontend**:
        *   Add CSS Keyframes for `breathing`, `nodding`, `hand-slide-in`.
        *   Add a "Hand" layer (using a stock image with transparency).
        *   Write a JS `AvatarController` to manage the "Acting" loop.

This will create a convincing illusion of a living, breathing anchor without needing heavy video files.