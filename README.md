# 😌 improductivetoday

![lowcortisol](low-cortisol.png)

> A GitHub Actions bot that commits a "productive" message to your repo every day so your contribution graph stays green while you question your life choices.

---

## 🤔 What is this?

`improductivetoday` is an automated workflow that runs daily and writes a randomly selected "productive" message to `productive.txt`, then commits and pushes it to the repo. It makes your GitHub calendar look busy whether you actually did something or did something "productive".

---

## 📁 Project Structure

```
improductivetoday/
├── .github/
│   └── workflows/
│       └── productive.yml   # GitHub Actions workflow
├── build.py                 # Picks a random message and writes it
├── work.json                # List of "productive" messages
└── productive.txt           # Output file (updated daily by the bot)
```

---

## ⚙️ How It Works

1. The workflow triggers every day at **1:00 PM UTC** via a cron schedule
2. It runs `build.py`, which picks a random message from `work.json`
3. It makes sure the new message is **different** from the last one
4. The bot commits the updated `productive.txt` with the message `"Productive Work"`
5. The commit is pushed back to the repo by `github-actions[bot]`

---

## 🚀 Setup

### 1. Clone the repo

```bash
git clone https://github.com/daveaillerr/improductivetoday.git
cd improductivetoday
```

### 2. Enable the workflow toggle

Go to your repo → **Settings** → **Secrets and variables** → **Actions** → **Variables**

Create a new variable:

- **Name:** `WORKFLOW_ENABLED`
- **Value:** `true`

### 3. Give Actions write permission

Go to **Settings** → **Actions** → **General** → **Workflow permissions**

Select **Read and write permissions** and hit **Save**.

### 4. Configure your email and user name

- Replace "<GITHUB_EMAIL_ADDRESS>" with the email linked to your GitHub account.
- Replace "<GITHUB_USER_NAME>" with your GitHub username or preferred display name.
- This ensures your commits are properly attributed to your GitHub profile.

```
git config --global user.email "<GITHUB EMAIL ADDRESS>"
git config --global user.name "<GITHUB USER NAME>"
```
---

## 🔛 Turning It On / Off

No code changes needed. Just update the repo variable:

| `WORKFLOW_ENABLED` | Result                 |
| ------------------ | ---------------------- |
| `true`             | Workflow runs daily ✅ |
| `false`            | Workflow is skipped ⏸️ |

---

## 🛠️ Running Manually

Go to the **Actions** tab → select `Pushing a very productive work` → click **Run workflow**.

---

## 📝 Adding Your Own Messages

Edit `work.json` and add to the `"work"` array:

```json
{
  "work": [
    "I'm going to be productive today",
    "Turning coffee into commits",
    "Pushing to prod and praying",
    "Your message here"
  ]
}
```

---

## 📦 Requirements

- Python 3.14
- No external dependencies — uses only the Python standard library (`json`, `random`)

---

## 📄 License

Do whatever you want with this. It's a bot that writes fake productivity messages.
