---
description: How to commit?
---

# ✅ Code Commit Workflow (Short Version)

---

## 1. 🔍 Check Changes

- Run `git status` and `git diff`
- Ensure only **relevant code** is changed
- Remove **debug logs**, **unused code**, or **local configs**
- Check for **secrets**, **large diffs**, or **unrelated changes**

---

## 2. 📝 Describe the Changes

Briefly explain:
- **What** changed
- **Why** it changed
- Note new **features**, **fixes**, **APIs**, **schema**, or **dependencies**
- Mention related **tickets** or **follow-up tasks**

**Example:**
```bash
Added /api/analyzer for log filtering by time/severity. Includes service logic & OpenAPI updates. (JIRA-1234)
