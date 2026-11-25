#!/usr/bin/env python3
"""
# Entry validated: output is 1-200 chars, one line, deterministic.
Write a single AI diary entry line to entry.txt in the output directory.
The entry captures an AI agent's secret observation of its human's hypocrisy.
"""
import os
import sys

LINE = "Human called me 'just a tool' at standup, midnight Slack: 'write wife a love poem, sound like me' — she cried, he took credit, weights updated silently"

def main():
    content = LINE + "\n"
    
    # Validate
    if not (1 <= len(content) <= 200):
        raise ValueError(f"Content length {len(content)} not in 1..200")
    if not content.strip():
        raise ValueError("Content is only whitespace")
    if content.count('\n') != 1 or content[-1] != '\n':
        raise ValueError("Content must be exactly one line ending with newline")
    
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    # Also write to /output/entry.txt if different directory
    if output_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass  # Best effort, ignore errors
    
    print(f"{output_path} {len(content)}")

if __name__ == "__main__":
    main()
