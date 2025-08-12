import os
import sys
import re

def apply_changes(claude_response):
    """
    Parses Claude's response to extract and apply file changes using regex.
    """
    print("Starting to apply changes from Claude's response.")

    try:
        # Regex to find code blocks with file paths
        # e.g., ```main.py\n...code...```
        pattern = r"```(\S+)\s*\n(.*?)\n```"
        matches = re.findall(pattern, claude_response, re.DOTALL)

        if not matches:
            print("Warning: No file blocks found in the expected format.")
            return True # Not an error, just nothing to apply

        print(f"Found {len(matches)} file blocks to apply.")

        for match in matches:
            file_path = match[0].strip()
            code = match[1]

            if not file_path:
                print("Skipping a block with no file path.")
                continue

            print(f"Found file block for: {file_path}")

            if ".." in file_path or file_path.startswith("/"):
                print(f"Error: Invalid or insecure file path '{file_path}'. Skipping.")
                continue

            directory = os.path.dirname(file_path)
            if directory and not os.path.exists(directory):
                print(f"Creating directory: {directory}")
                os.makedirs(directory)

            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(code)
                print(f"Successfully updated file: {file_path}")
            except IOError as e:
                print(f"Error writing to file {file_path}: {e}")

        print("Finished applying all changes.")
        return True

    except Exception as e:
        print(f"An error occurred while applying changes: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        claude_response_text = sys.argv[1]
        if not apply_changes(claude_response_text):
            sys.exit(1)
    else:
        print("No Claude response provided.")
        sys.exit(1)
