#!/usr/bin/env bash
# Remote command menu for devAItester/aishare/cmd.
# Requires Bash and curl. Remote .txt files are executed locally as Bash code.

set -uo pipefail

readonly API_URL="https://api.github.com/repos/devAItester/aishare/contents/cmd?ref=main"
readonly RAW_BASE="https://raw.githubusercontent.com/devAItester/aishare/main/cmd"

if ! command -v curl >/dev/null 2>&1; then
  printf 'Error: curl is required.\n' >&2
  exit 1
fi

load_commands() {
  local response
  if ! response=$(curl -fsSL "$API_URL"); then
    printf 'Error: could not read the remote cmd/ directory.\n' >&2
    return 1
  fi

  # GitHub's Contents API returns one JSON object per file. This extracts
  # only top-level .txt names; files in subdirectories are not listed here.
  mapfile -t COMMANDS < <(
    printf '%s\n' "$response" |
      sed -n 's/^[[:space:]]*"name":[[:space:]]*"\([^"]*\.txt\)",*$/\1/p'
  )

  (("${#COMMANDS[@]}" > 0)) || {
    printf 'No .txt operations found in cmd/.\n'
    return 1
  }
}

run_command() {
  local filename=$1
  local url="$RAW_BASE/$filename"

  printf '\n--- %s ---\n\n' "$filename"
  # Stream the remote text directly into Bash; no local copy is created.
  # pipefail ensures a failed download is not reported as a successful run.
  if curl -fsSL "$url" | bash; then
    printf '\n--- Operation finished ---\n'
  else
    local status=$?
    printf '\n--- Operation failed (status %s) ---\n' "$status"
  fi
}

declare -a COMMANDS=()

while :; do
  if ! load_commands; then
    printf '\nPress Enter to retry, or Ctrl+C to exit. '
    read -r _
    continue
  fi

  printf '\nRemote operations in devAItester/aishare/cmd:\n\n'
  for i in "${!COMMANDS[@]}"; do
    printf '  %2d. %s\n' "$((i + 1))" "${COMMANDS[$i]}"
  done
  printf '   0. Exit\n\n'
  read -r -p 'Select operation: ' choice

  [[ "$choice" == "0" ]] && exit 0
  [[ "$choice" =~ ^[0-9]+$ ]] || {
    printf 'Enter a number from the menu.\n'
    continue
  }

  index=$((choice - 1))
  if (( index < 0 || index >= ${#COMMANDS[@]} )); then
    printf 'No operation with that number.\n'
    continue
  fi

  while (( index >= 0 && index < ${#COMMANDS[@]} )); do
    run_command "${COMMANDS[$index]}"
    printf '\n  1. Run next operation\n'
    printf '  2. Return to list\n'
    printf '  0. Exit\n\n'
    read -r -p 'Choose: ' action

    case "$action" in
      1) ((index += 1)) ;;
      2) break ;;
      0) exit 0 ;;
      *) printf 'Returning to list.\n'; break ;;
    esac
  done
done
