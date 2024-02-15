# todo_md_maker
Inspiration from Reddit user 

## How to implement

At the moment "todo_md_maker.py" should be a simple as dropping into your git repo. However I recommend the following:
 - Ensure the constant "MD_PATH" is pointed at the desired markdown document
 - Ensure the constant "SRC_DIR" is pointed at the top directory for your project/source code.
 - As you are coding in your Repo/Project
    - "# TODO:" will add the checkbox to the Generated Todo's section
    - "# TODONE:" will format the checkbox so it can be checked off


## Generated Todo's
### Src\main.py
- [ ] line #10: Make code that will rock user's socks
### Src\subdir\stuff.py
- [ ] line #5: Create database wrapper.py
- [x] line #14: Create Convenience Class
- [ ] line #19: Make getter/setter methods
---
---

## Markdown preservation
If the generated todo's section does not exist, it will append to the end of the markdown document. If it does exist, the code will preserve any content that exists after the double horizontal rule ("---\r\n---")