from app.models import InputObject, OutputObject, Analysis, OptimizedScript, DeliveryGuidance, ActionStep
from textblob import TextBlob
import edge_tts
import random
import os
import uuid
import asyncio

class AvatarEngine:
    def __init__(self):
        # Initialize any ML models or API clients here
        self.static_dir = "app/static"
        if not os.path.exists(self.static_dir):
            os.makedirs(self.static_dir)

    def analyze_script(self, script: str, audience: str) -> Analysis:
        """
        Parse intent, audience, tone, and platform using TextBlob for basic NLP.
        """
        if not script:
            return Analysis(issues=["No script provided"], opportunities=["Provide a script for analysis"])
        
        blob = TextBlob(script)
        issues = []
        opportunities = []
        
        # 1. Length Check
        word_count = len(blob.words)
        if word_count < 10:
            issues.append("Script is extremely short; lacks substance.")
        elif word_count > 300:
            issues.append("Script is very long; consider splitting for better retention.")

        # 2. Sentiment Analysis
        polarity = blob.sentiment.polarity # -1 to 1
        subjectivity = blob.sentiment.subjectivity # 0 to 1
        
        if polarity < -0.3:
            issues.append("Tone detected as negative. Ensure this aligns with your goal.")
            opportunities.append("Inject more positive language to boost engagement.")
        elif polarity > 0.5:
            opportunities.append("Great positive energy detected!")

        if subjectivity > 0.7:
            opportunities.append("Highly subjective. Good for storytelling, but check facts for educational content.")
        elif subjectivity < 0.2:
            opportunities.append("Very objective. Consider adding personal anecdotes to connect with the audience.")

        # 3. Readability (Heuristic: avg sentence length)
        avg_sentence_len = sum(len(s.words) for s in blob.sentences) / (len(blob.sentences) or 1)
        if avg_sentence_len > 25:
            issues.append("Sentences are too complex (avg > 25 words). Simplify for video.")
            opportunities.append("Break down long sentences for better speech flow.")

        # Default fallback
        if not issues:
            issues.append("No major structural issues detected.")
        if not opportunities:
            opportunities.append("Refine word choice for stronger impact.")

        return Analysis(issues=issues, opportunities=opportunities)

    def optimize_script(self, script: str, tone: str, platform: str) -> OptimizedScript:
        """
        Rewrite for clarity, emotion, and flow.
        Uses heuristics to 'simulate' optimization since we lack a generative LLM key.
        """
        if not script:
            return OptimizedScript(primary_version="N/A", alternate_version=None)

        blob = TextBlob(script)
        
        # Simulated Optimization Strategies
        primary = script
        alternate = script

        # 1. Tone Adjustment (Simple replacement heuristics)
        if tone == "energetic":
            primary = primary.replace(".", "!").replace(" is ", " is absolutely ")
        elif tone == "serious":
            primary = primary.replace("!", ".").replace("awesome", "significant")
        elif tone == "dramatic":
            primary = "Listen closely... " + primary + " ...and that changes everything."

        # 2. Platform Adaptation
        if platform == "shorts" or platform == "reels":
            # Truncate or summarize
            if len(blob.words) > 60:
                 alternate = " ".join(blob.words[:60]) + "... (Check Link in Bio)"
            else:
                 alternate = "WAIT! " + script
        elif platform == "youtube":
             alternate = "Hey guys, welcome back! " + script + " Don't forget to like and subscribe."

        # Special News Anchor Logic
        # (This overrides the above if the tone/context suggests news, or we can assume it's handled by role)
        # Note: In a real system, we'd pass 'role' to this function too.
        # Since we can't change signature easily without breaking models, we'll infer or just add it.
        # Let's check for typical news keywords or just force it if the user chose "News" in the frontend which usually maps to "Serious".
        
        return OptimizedScript(primary_version=primary, alternate_version=alternate)

    def optimize_script_with_role(self, script: str, tone: str, platform: str, role: str) -> OptimizedScript:
        """
        Enhanced optimization that considers the Role.
        """
        # Base optimization
        optimized = self.optimize_script(script, tone, platform)
        primary = optimized.primary_version

        if role == "news":
            # Enforce News Structure
            # 1. Add Dateline/Intro
            dateline = "BREAKING NEWS: " if "breaking" in script.lower() else "REPORTING LIVE: "
            
            # 2. Formalize
            primary = primary.replace("I think", "Reports indicate")
            primary = primary.replace("maybe", "allegedly")
            primary = primary.replace("gonna", "going to")
            
            # 3. Add Sign-off
            sign_off = " This is your AI Anchor, reporting for Trae News."
            
            primary = dateline + primary + sign_off
            
            optimized.primary_version = primary

        return optimized
    
    def get_voice_for_role(self, role: str) -> str:
        """
        Maps roles to specific Edge Neural voices.
        """
        voice_map = {
            "news": "en-US-GuyNeural",         # Professional, standard
            "storyteller": "en-US-AriaNeural", # Expressive, clear
            "influencer": "en-US-DavisNeural", # Friendly, conversational
            "educator": "en-US-EricNeural",    # Authoritative, calm
            "neutral": "en-US-ChristopherNeural"
        }
        return voice_map.get(role, "en-US-ChristopherNeural")

    async def generate_audio(self, text: str, role: str) -> str:
        """
        Generates audio from text using Edge TTS (Neural Voices) and returns the relative URL.
        """
        print(f"Generating audio for role: {role}, text: {text[:50]}...")
        if not text or text == "N/A":
            print("Skipping audio generation: No text provided.")
            return ""
        
        try:
            filename = f"audio_{uuid.uuid4()}.mp3"
            filepath = os.path.join(self.static_dir, filename)
            
            # Select voice based on role
            voice = self.get_voice_for_role(role)
            print(f"Selected voice: {voice}")
            
            # Create audio file using Edge TTS
            communicate = edge_tts.Communicate(text, voice)
            await communicate.save(filepath)
            
            # Verify file creation
            if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
                print(f"Audio generated successfully: {filename}")
                return f"/static/{filename}"
            else:
                print("Error: File not created or empty.")
                return ""
        except Exception as e:
            print(f"Error generating audio: {e}")
            import traceback
            traceback.print_exc()
            return ""

    def generate_delivery_guidance(self, tone: str, role: str) -> DeliveryGuidance:
        """
        Suggest delivery style based on tone and role.
        """
        guidance_map = {
            "energetic": {
                "pace": "Fast and punchy",
                "expressions": "High energy, wide eyes, frequent smiling",
                "emphasis": ["Key verbs", "Call to action", "Power words"],
                "gesture_frequency": 0.8,
                "gesture_types": ["open_palm", "point", "fist_pump"]
            },
            "serious": {
                "pace": "Slow and deliberate",
                "expressions": "Neutral to concerned, focused gaze",
                "emphasis": ["Statistics", "Warnings", "Conclusion"],
                "gesture_frequency": 0.3,
                "gesture_types": ["small_hand_chop", "steeple_hands"]
            },
            "calm": {
                "pace": "Relaxed and steady",
                "expressions": "Soft smile, gentle nodding",
                "emphasis": ["Reassuring phrases", "Transitions"],
                "gesture_frequency": 0.4,
                "gesture_types": ["open_palm", "slow_nod"]
            },
            "dramatic": {
                "pace": "Varied with strategic pauses",
                "expressions": "Intense, expressive eyebrows",
                "emphasis": ["The 'Turn'", "The Reveal", "Emotional peaks"],
                "gesture_frequency": 0.6,
                "gesture_types": ["wide_arms", "point", "dramatic_pause"]
            }
        }
        
        defaults = guidance_map.get(tone, guidance_map["energetic"])
        
        # Role adjustments
        if role == "news":
            defaults["expressions"] += ", Professional posture"
            defaults["gesture_types"] = ["paper_shuffle", "finger_point"] + defaults["gesture_types"]
        elif role == "influencer":
            defaults["expressions"] += ", Hand gestures towards camera"
            defaults["gesture_frequency"] = min(1.0, defaults["gesture_frequency"] + 0.2)

        return DeliveryGuidance(
            tone=tone,
            pace=defaults["pace"],
            expressions=defaults["expressions"],
            emphasis_points=defaults["emphasis"],
            gesture_frequency=defaults["gesture_frequency"],
            gesture_types=defaults["gesture_types"]
        )

    def create_action_plan(self, goal: str) -> list[ActionStep]:
        """
        Convert scripts into executable task sequences based on the goal.
        """
        steps = []
        if goal == "automation":
            steps = [
                ActionStep(step=1, action="Input script into TTS Engine (ElevenLabs/OpenAI)", tool_required=True),
                ActionStep(step=2, action="Generate Talking Head Video (HeyGen/D-ID)", tool_required=True),
                ActionStep(step=3, action="Auto-caption and Sync", tool_required=True),
                ActionStep(step=4, action="Schedule upload via API", tool_required=True)
            ]
        elif goal == "engagement":
            steps = [
                ActionStep(step=1, action="Identify high-retention hook (0-3s)", tool_required=False),
                ActionStep(step=2, action="Add B-roll/overlays every 2-5 seconds", tool_required=True),
                ActionStep(step=3, action="Insert 'Comment Below' prompt", tool_required=False),
                ActionStep(step=4, action="Reply to first 10 comments", tool_required=False)
            ]
        elif goal == "conversion":
            steps = [
                ActionStep(step=1, action="Clearly state the problem", tool_required=False),
                ActionStep(step=2, action="Present solution (Product/Service)", tool_required=False),
                ActionStep(step=3, action="Add urgent Call-To-Action (CTA)", tool_required=False),
                ActionStep(step=4, action="Track link clicks via UTM parameters", tool_required=True)
            ]
        else: # Clarity / General
            steps = [
                ActionStep(step=1, action="Read aloud to check flow", tool_required=False),
                ActionStep(step=2, action="Remove jargon and simplify", tool_required=False),
                ActionStep(step=3, action="Record final take", tool_required=True),
                ActionStep(step=4, action="Publish", tool_required=True)
            ]
        return steps

    async def process(self, input_data: InputObject) -> OutputObject:
        """
        Orchestrates the pipeline: UI -> Backend -> AI Engine -> Output
        """
        # 1. Script Comprehension
        analysis = self.analyze_script(input_data.script, input_data.audience)

        # 2. Script Optimization
        # Use the new role-aware optimization
        optimized = self.optimize_script_with_role(
            input_data.script, 
            input_data.tone.value, 
            input_data.platform.value,
            input_data.role.value
        )
        
        # 2b. Generate Audio (Async with Neural Voices)
        audio_url = await self.generate_audio(optimized.primary_version, input_data.role.value)
        optimized.audio_url = audio_url

        # 3. Performance Intelligence
        delivery = self.generate_delivery_guidance(input_data.tone.value, input_data.role.value)

        # 5. Action Planning
        plan = self.create_action_plan(input_data.goal.value)

        return OutputObject(
            analysis=analysis,
            optimized_script=optimized,
            delivery_guidance=delivery,
            action_plan=plan
        )
