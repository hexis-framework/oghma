# /// script
# requires-python = ">=3.10"
# dependencies = ["oghma"]
# ///
"""Seed a temporary database with sample memories for the demo GIF."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from oghma.storage import Storage

DEMO_MEMORIES = [
    {
        "content": "sqlite-vec cosine similarity returns distance, not similarity. Subtract from 1 to get actual similarity score.",
        "category": "gotcha",
        "source_tool": "claude_code",
        "source_file": "session-a1b2c3.jsonl",
        "confidence": 0.95,
    },
    {
        "content": "Python subprocess.run with capture_output=True silently swallows stderr. Use check=True to surface errors, or log stderr explicitly.",
        "category": "gotcha",
        "source_tool": "claude_code",
        "source_file": "session-d4e5f6.jsonl",
        "confidence": 0.90,
    },
    {
        "content": "FTS5 tokenizer treats hyphens as separators. 'sqlite-vec' matches 'sqlite' and 'vec' independently. Use double quotes for phrase matching.",
        "category": "learning",
        "source_tool": "codex",
        "source_file": "rollout-g7h8i9.jsonl",
        "confidence": 0.95,
    },
    {
        "content": "Reciprocal Rank Fusion with k=60 balances keyword and vector results well for technical queries. Lower k over-weights top results.",
        "category": "learning",
        "source_tool": "claude_code",
        "source_file": "session-j0k1l2.jsonl",
        "confidence": 1.0,
    },
    {
        "content": "OpenAI text-embedding-3-small occasionally returns NaN for empty strings. Always validate input before embedding.",
        "category": "gotcha",
        "source_tool": "opencode",
        "source_file": "ses_m3n4o5",
        "confidence": 0.90,
    },
    {
        "content": "Use WAL mode for SQLite when reading and writing concurrently. Default journal mode blocks readers during writes.",
        "category": "learning",
        "source_tool": "claude_code",
        "source_file": "session-p6q7r8.jsonl",
        "confidence": 0.95,
    },
    {
        "content": "Git pre-commit hooks don't run on amend by default. Set core.hooksPath and use prepare-commit-msg for consistent enforcement.",
        "category": "workflow",
        "source_tool": "codex",
        "source_file": "rollout-s9t0u1.jsonl",
        "confidence": 0.85,
    },
    {
        "content": "MCP tool schemas cost ~350 tokens per turn. Prefer CLI integration over MCP when the tool is only used occasionally.",
        "category": "learning",
        "source_tool": "claude_code",
        "source_file": "session-v2w3x4.jsonl",
        "confidence": 0.90,
    },
]


def main() -> None:
    db_path = Path(__file__).resolve().parent.parent / "demo.db"
    db_path.unlink(missing_ok=True)

    storage = Storage(db_path=str(db_path))

    for mem in DEMO_MEMORIES:
        storage.add_memory(**mem)

    print(f"Seeded {len(DEMO_MEMORIES)} memories → {db_path}")


if __name__ == "__main__":
    main()
