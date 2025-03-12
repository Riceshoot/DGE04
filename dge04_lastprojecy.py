import time
import sys
from datetime import datetime

class GraduationMessage:
    """Class to manage and decorate graduation messages for output."""
    
    COLORS = {
        "reset": "\033[0m",
        "cyan": "\033[96m",
        "yellow": "\033[93m",
        "green": "\033[92m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "bold": "\033[1m"
    }

    FRAME_TOP = "╔" + "═" * 50 + "╗"
    FRAME_BOTTOM = "╚" + "═" * 50 + "╝"

    def __init__(self, generation, start_year):
        self.generation = generation
        self.start_year = start_year
        self.end_year = self.get_graduation_year()
        self.messages = {
            "Japanese": {
                "congrats": "🎓 みんな大学4年間、お疲れ様！",
                "future": "🚀 これからそれぞれの道に進むけれど、\n   みんなにとって素晴らしい未来が待っていますように。",
                "memories": "📖 このアルバムには、みんなとの大切な思い出を詰め込みました。\n💡 忘れられない日々を、いつまでも心に刻んで。",
                "title": f"✨ Digital Engineering {self.generation}期生 ✨",
                "year": f"{self.start_year}-{self.end_year}"
            },
            "English": {
                "congrats": "🎓 Congratulations to everyone on completing four years of university!",
                "future": "🚀 As we each embark on our own paths,\n   may a bright and promising future await us all.",
                "memories": "📖 This album captures our precious memories together,\n💡 so we can always cherish the unforgettable moments.",
                "title": f"✨ Digital Engineering {self.generation}th Generation ✨",
                "year": f"{self.start_year}-{self.end_year}"
            }
        }

    def get_graduation_year(self):
        """Automatically calculates the graduation year based on the start year."""
        return self.start_year + 4

    def animated_print(self, text, color="reset", delay=0.05):
        """Prints text one character at a time to create an animation effect."""
        sys.stdout.write(self.COLORS[color])  # Apply color
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write(self.COLORS["reset"] + "\n")  # Reset color

    def display_message(self, language="Japanese"):
        """Displays the message in the specified language, decorated and animated."""
        if language not in self.messages:
            return "⚠️ Language not supported."

        msg = self.messages[language]

        print(self.COLORS["cyan"] + self.FRAME_TOP + self.COLORS["reset"])
        self.animated_print(f"🎉 {msg['congrats']}", "yellow", 0.05)
        self.animated_print(f"📅 {msg['year']}", "green", 0.05)
        print("─" * 50)
        self.animated_print(f"{msg['future']}", "blue", 0.05)
        self.animated_print(f"{msg['memories']}", "magenta", 0.05)
        print("─" * 50)
        self.animated_print(f"🏫 {msg['title']}", "bold", 0.05)
        print(self.COLORS["cyan"] + self.FRAME_BOTTOM + self.COLORS["reset"])

    def calculate_values(self, time_spent, memory_shared, lessons_learned):
        """Calculate friendship, knowledge, and memories based on input values."""
        friendship = (time_spent + memory_shared) * 1.5
        knowledge = (lessons_learned + time_spent) * 2
        memories = (memory_shared + lessons_learned) * 1.2
        return {
            "Friendship": round(friendship, 2),
            "Knowledge": round(knowledge, 2),
            "Memories": round(memories, 2)
        }

# Create instance (4th generation, starting in 2021)
graduation = GraduationMessage(generation=4, start_year=2021)

# Display Japanese message
graduation.display_message("Japanese")

# Display English message
graduation.display_message("English")

# Calculate and print friendship, knowledge, and memories
values = graduation.calculate_values(time_spent=100, memory_shared=80, lessons_learned=120)
print("\n💖 Friendship Level:", values["Friendship"])
print("📚 Knowledge Level:", values["Knowledge"])
print("📸 Memories Level:", values["Memories"])
