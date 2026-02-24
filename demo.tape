# Oghma demo — search your coding memories
# Run: python3 scripts/seed_demo_db.py && vhs demo.tape

Output demo.gif

Set Shell zsh
Set FontSize 14
Set Width 1200
Set Height 600
Set Padding 20
Set Theme "Catppuccin Mocha"
Set TypingSpeed 50ms
Env OGHMA_DB_PATH "demo.db"

# Show stats first — establishes scale
Type "oghma stats"
Enter
Sleep 3s

# Core feature: search past learnings
Type 'oghma search "sqlite" --limit 3'
Enter
Sleep 4s
