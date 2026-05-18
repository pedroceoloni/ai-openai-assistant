import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ── Core functions ────────────────────────────────────────────────────────────

def improve_text(text: str) -> str:
    """Rewrite text to be clear, professional, and well-structured."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional writing assistant. Improve texts to be clear, concise, and professional. Return only the improved text, no explanations."},
            {"role": "user", "content": f"Improve this text:\n\n{text}"}
        ]
    )
    return response.choices[0].message.content


def correct_text(text: str) -> str:
    """Fix grammar, spelling, and punctuation errors."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a grammar expert. Correct all spelling, grammar, and punctuation errors. Return only the corrected text, no explanations."},
            {"role": "user", "content": f"Correct this text:\n\n{text}"}
        ]
    )
    return response.choices[0].message.content


def summarize_text(text: str) -> str:
    """Summarize text into the 3 most important points."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a summarization expert. Summarize texts into clear, concise bullet points. Always use exactly 3 bullet points covering the most important ideas."},
            {"role": "user", "content": f"Summarize this text in 3 bullet points:\n\n{text}"}
        ]
    )
    return response.choices[0].message.content


def standardize_tone(text: str, tone: str = "formal") -> str:
    """Rewrite text in a specified tone: formal, casual, or friendly."""
    tone_instructions = {
        "formal":   "professional and formal, suitable for business communication",
        "casual":   "casual and conversational, like talking to a friend",
        "friendly": "warm, friendly, and approachable, suitable for customer service",
    }
    description = tone_instructions.get(tone, tone_instructions["formal"])
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"You are a writing tone specialist. Rewrite texts to sound {description}. Return only the rewritten text, no explanations."},
            {"role": "user", "content": f"Rewrite this text in a {tone} tone:\n\n{text}"}
        ]
    )
    return response.choices[0].message.content

# ── Menu helpers ──────────────────────────────────────────────────────────────

MENU = """
╔══════════════════════════════════════╗
║       AI TEXT ASSISTANT              ║
║       Powered by OpenAI API          ║
╠══════════════════════════════════════╣
║  1 — Improve text                    ║
║  2 — Correct grammar & spelling      ║
║  3 — Summarize text                  ║
║  4 — Standardize tone                ║
║  0 — Exit                            ║
╚══════════════════════════════════════╝
"""

TONE_MENU = """
Select tone:
  1 — Formal   (business / professional)
  2 — Casual   (conversational)
  3 — Friendly (customer-facing / warm)
"""

def get_tone_choice() -> str:
    tone_map = {"1": "formal", "2": "casual", "3": "friendly"}
    print(TONE_MENU)
    choice = input("Tone choice (1/2/3): ").strip()
    return tone_map.get(choice, "formal")


def get_multiline_input() -> str:
    """Allow multiline input; user types END on a new line to finish."""
    print("Enter your text (type END on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    return "\n".join(lines)

# ── Main loop ─────────────────────────────────────────────────────────────────

def main():
    print(MENU)
    while True:
        choice = input("Select an option: ").strip()

        if choice == "0":
            print("\nGoodbye! 👋")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid option. Please enter 1, 2, 3, 4 or 0.\n")
            continue

        text = get_multiline_input()
        if not text.strip():
            print("No text entered. Please try again.\n")
            continue

        print("\nProcessing...\n")

        if choice == "1":
            result = improve_text(text)
            label  = "✅ Improved Text"
        elif choice == "2":
            result = correct_text(text)
            label  = "✅ Corrected Text"
        elif choice == "3":
            result = summarize_text(text)
            label  = "✅ Summary"
        elif choice == "4":
            tone   = get_tone_choice()
            result = standardize_tone(text, tone)
            label  = f"✅ Text in {tone.capitalize()} Tone"

        print(f"\n{'─' * 40}")
        print(f"{label}:\n")
        print(result)
        print(f"{'─' * 40}\n")

        again = input("Process another text? (y/n): ").strip().lower()
        if again != "y":
            print("\nGoodbye! 👋")
            break
        print(MENU)


if __name__ == "__main__":
    main()
