---
trigger: always_on
---

1. Descriptive Naming

- Variables, functions, and classes should clearly state their purpose.

- Avoid abbreviations unless they are universally understood.

2. Simplicity Over Cleverness

- Choose the simplest working solution.

- Avoid unnecessary abstractions and over-engineering.

3. Separation of Concerns

- Each function does one thing and does it well.

- Group related logic together; keep unrelated logic apart.

4. Avoiding Spaghetti Code

- No deeply nested logic or tangled dependencies.

- Flatten conditionals and loops where possible.

- Use early returns to reduce nesting.

5. Clear Function Signatures

- Functions should be short, predictable, and have clear inputs and outputs.

- Avoid side effects where possible.

6. Modular Design

- Split code into self-contained, testable modules.

- Reuse logic without duplicating code.

7. Consistent Formatting

- Follow language-specific style guides (e.g., PEP 8 for Python, Airbnb for JS).

- Use tools like Prettier, ESLint, or Black.

8. Error Handling with Context

- Catch and log errors with enough information to debug.

- Avoid swallowing errors silently.

9. Minimal Dependencies

- Use built-in tools and standard libraries when possible.

- Avoid bloating the project with unnecessary packages.