# Repository Guidelines

- Keep public APIs stable unless the change is required by the task.
- Currency calculations must round only once, at the final returned amount.
- Pagination uses 1-based page numbers.
- A partially filled final page still counts as a page.
- Cache entries expire at their exact expiry time.
- Do not introduce unnecessary external dependencies.
- Preserve existing behavior outside the requested change.
