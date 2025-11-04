import anthropic
import base64
from rich.console import Console
from rich.markdown import Markdown

console = Console()

# Read and encode your image
with open("Algoverse-Huanzhi-Research/static/water_drop.jpg", "rb") as image_file:
    image_data = base64.standard_b64encode(image_file.read()).decode("utf-8")

# Add api key **GOTTA ADD SOME ENV VARIABLES
client = anthropic.Anthropic(api_key="")

message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",  # or "image/png", "image/gif", "image/webp"
                        "data": image_data,
                    },
                },
                {
                    "type": "text",
                    "text": "You are a tool using ai agent using the opencv library to edit images. give me the code to convert this image to greyscale using opencv. only include the code with no explanation."
                }
            ],
        }
    ],
)

# Extract only text content blocks (skip thinking blocks)
text_content = ""
for block in message.content:
    if block.type == "text":
        text_content += block.text


# Make output readable from the terminal
md = Markdown(text_content)
console.print(md)