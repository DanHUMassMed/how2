Sometimes, getting a single shell command can feel unnecessarily complicated. You might know roughly what you want to do, but finding the exact syntax often means switching between browser tabs, scrolling through forum answers, or consulting AI tools—and then copying snippets back into your terminal.

It’s a small task, but the friction adds up—breaking focus and slowing down workflow. What I really wanted was simple: **ask a question, get a ready-to-run command, and paste it immediately—without leaving the terminal**. Even with powerful AI assistants available, bouncing between tools adds friction, so I wanted something **local**, **fast**, and **clipboard-ready** that fits seamlessly into my workflow.

I came across an interesting tool called [“how” by Ademking](https://github.com/Ademking/how) that did much of what I needed.

## Why Fork `how`?

Although “how” was simple and effective, I also wanted a version that could run locally and leverage open-source LLMs. I could have started from scratch, but “how” had already laid a solid foundation for translating plain English into shell commands. The real strength of that code lies in the **prompt engineering** by Adem Kouki. By carefully structuring the prompt—including details about the environment such as OS, shell, current directory, files, Git repo, and available tools—the LLM can generate commands that are precise, context-aware, and safe to run.

Rewriting the tool around **Ollama** makes it easy to use local or self-hosted models, preserving the original tool’s strengths while keeping everything self-contained and efficient.


## Key Features ✨

* **Plain English → Shell Command**
* **Automatic Clipboard Copy**
* **Command History**
* **Environment-Aware Suggestions**
* **Configurable Ollama Models**

In other words—plain language in, executable command out.

---

## Installation 📦

Requires Python and an Ollama installation.

Inside the project folder:

```bash
pip install how2
```

`how2` was written and tested on macOS.
(Windows support may require manual adaptation.)

---

## Download + Source Code

Grab the code or fork it here:

```
https://github.com/DanHUMassMed/how2
```