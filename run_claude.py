import os
import sys
from anthropic import Anthropic

def run_claude_enhancement():
    """
    Constructs the prompt, calls the Claude API, and prints the response.
    """
    try:
        client = Anthropic(api_key=os.environ['ANTHROPIC_API_KEY'])

        task = os.environ.get('CLAUDE_TASK')
        main_py = os.environ.get('MAIN_PY_CONTENT')
        index_html = os.environ.get('INDEX_HTML_CONTENT')
        reqs_txt = os.environ.get('REQS_TXT_CONTENT')

        prompt = f"""
You are an expert AI software engineer. Your task is to help improve a project based on the user's request.
The user's request is:
---
{task}
---

Here are the contents of the relevant files:

**File: main.py**
```python
{main_py}
```

**File: static/index.html**
```html
{index_html}
```

**File: requirements.txt**
```
{reqs_txt}
```

Please provide the complete, updated file content for each file you modify.
Enclose each updated file's content in a markdown code block, with the file path specified after the backticks and on the same line. For example:

```main.py
# The full, updated content of main.py
print('hello world')
```

If you do not need to modify a file, do not include it in your response.
Only output the code blocks for the files you are changing. Do not include any other text or explanations.
"""

        response = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=4096,
            messages=[{
                'role': 'user',
                'content': prompt
            }]
        )

        if not response or not response.content:
            raise ValueError('No response received from Claude')

        # Print the raw response content to be captured by the workflow
        print(response.content[0].text)

    except Exception as e:
        print(f"Error occurred in run_claude.py: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    run_claude_enhancement()
