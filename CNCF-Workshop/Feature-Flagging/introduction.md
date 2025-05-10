# 📌 Feature Flagging

## 🧠 What is Feature Flagging?


**Feature Flagging** (also known as **Feature Toggles**) is a software development technique that allows teams to **enable or disable features without deploying new code**. 

It helps teams:
- Deploy code to production without exposing it to users immediately.
- Control the exposure of features dynamically.
- Perform safe testing in production.
- Gradually roll out features.

---

## ⚙️ How Does Feature Flagging Work?

1. Developers **wrap features in flags**, e.g., `if is_enabled("new_feature")`.
2. Flags are evaluated **at runtime** via:
   - Config files
   - Environment variables
   - Remote config (via feature flagging tools)
   - User attributes (location, role, percentage rollout, etc.)
3. A **feature flag service** returns whether a feature is enabled or not.
