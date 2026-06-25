#!/usr/bin/env sh
# install.sh — wire this repo's tracked agent config into the tool-specific
# locations your coding agent looks for. Safe to re-run (idempotent).
#
# What lives where:
#   docs/agents/            ← canonical, tracked, tool-agnostic agent config
#   docs/agents/AGENTS.md   ← the agent guide (CLAUDE.md is a symlink to it)
#   docs/agents/skills/     ← published skills (e.g. teach)
#
# This script creates the pointers tools expect (all gitignored):
#   ./AGENTS.md            -> docs/agents/AGENTS.md
#   ./CLAUDE.md            -> docs/agents/CLAUDE.md
#   .claude/skills/teach   -> ../../docs/agents/skills/teach   (Claude Code)
#
# Usage:  sh docs/agents/install.sh        (run from the repo root)

set -eu

# Resolve repo root as the parent of docs/agents/, regardless of cwd.
script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
root=$(CDPATH= cd -- "$script_dir/../.." && pwd)
cd "$root"

# link <target-relative-to-link-dir> <link-path>
link() {
  target=$1
  linkpath=$2
  dir=$(dirname -- "$linkpath")
  mkdir -p "$dir"
  if [ -L "$linkpath" ]; then
    current=$(readlink "$linkpath")
    if [ "$current" = "$target" ]; then
      echo "ok    $linkpath -> $target"
      return
    fi
    rm -f "$linkpath"
  elif [ -e "$linkpath" ]; then
    echo "skip  $linkpath (real file exists, not touching it)"
    return
  fi
  ln -s "$target" "$linkpath"
  echo "link  $linkpath -> $target"
}

link "docs/agents/AGENTS.md" "AGENTS.md"
link "docs/agents/CLAUDE.md" "CLAUDE.md"
link "../../docs/agents/skills/teach" ".claude/skills/teach"

echo
echo "Done. In Claude Code, try:  /teach   (e.g. 'teach me how Bitcoin self-custody works')"
echo "Other agents: point your skills dir at docs/agents/skills/ and read docs/agents/AGENTS.md."
