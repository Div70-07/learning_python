import os
import re

# Total number of chapters based on learning_python_notes.html
TOTAL_CHAPTERS = 28

def get_completed_chapters(repo_path):
    completed = set()
    # Find all chapter files
    for filename in os.listdir(repo_path):
        match = re.match(r'chapter(\d+)\.py', filename)
        if match:
            completed.add(int(match.group(1)))
            
    # Chapter 1 is Installation which doesn't have a code file usually.
    # If they have Chapter 2, 3, or 4 done, assume Chapter 1 is done.
    if completed.intersection({2, 3, 4}):
        completed.add(1)
        
    return completed

def generate_progress_bar(completed_count, total, length=20):
    percent = completed_count / total
    filled_length = int(length * percent)
    bar = '█' * filled_length + '░' * (length - filled_length)
    return f"{bar} {percent:.0%}"

def update_readme(readme_path, completed_chapters, total):
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Progress Bar
    completed_count = len(completed_chapters)
    progress_bar = generate_progress_bar(completed_count, total)
    
    progress_text = (
        "<!-- PROGRESS:START -->\n"
        "**Python Learning Progress**\n\n"
        f"`{progress_bar}`\n\n"
        f"*{completed_count} / {total} chapters completed*\n"
        "<!-- PROGRESS:END -->"
    )

    pattern = re.compile(r'<!-- PROGRESS:START -->.*?<!-- PROGRESS:END -->', re.DOTALL)
    if pattern.search(content):
        content = pattern.sub(progress_text, content)
    else:
        print("❌ Could not find PROGRESS markers in README.md.")
        return

    # 2. Update Checklist
    # The format is `- [ ] **Chapter XX:** Title` or `- [x] **Chapter XX:** Title`
    
    def replace_checklist(match):
        chapter_num_str = match.group(2)
        chapter_num = int(chapter_num_str)
        
        if chapter_num in completed_chapters:
            new_checkbox = "x"
        else:
            new_checkbox = " "
            
        return f"- [{new_checkbox}] **Chapter {chapter_num_str}:**"
    
    # Matches '- [ ] **Chapter 01:**' or '- [x] **Chapter 01:**'
    checklist_pattern = re.compile(r'- \[(x| )\] \*\*Chapter (\d{2}):\*\*')
    content = checklist_pattern.sub(replace_checklist, content)

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"README.md updated successfully! Progress: {completed_count}/{total} ({completed_count/total:.0%})")

if __name__ == '__main__':
    # Define paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_path = os.path.dirname(script_dir)
    readme_path = os.path.join(repo_path, 'README.md')
    
    # Run logic
    completed_chapters = get_completed_chapters(repo_path)
    update_readme(readme_path, completed_chapters, TOTAL_CHAPTERS)
