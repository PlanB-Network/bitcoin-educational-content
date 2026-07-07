# Lesson format — the generative HTML UI paradigm

A lesson is **one self-contained, interactive HTML file** in `./lessons/`, named
`0001-<dash-name>.html` (increment the number each time). It is *generated for
this learner, this mission, this moment* — not a template you fill in. Treat HTML
as a **generative UI surface**: invent the interaction the concept deserves (a
quiz, a reveal, a tiny in-browser simulator, a step checklist), then render it.

## Hard rules

- **Self-contained & offline.** No build step, no CDN, no framework, no network
  at runtime. Link only the local shared stylesheet and (optionally) a local
  shared script. Plain HTML + a little vanilla JS.
- **Link, don't inline, shared style.** Every lesson links
  `../assets/planb-lesson.css` so the course looks like one consistent thing.
  Seed it into `./assets/` from the skill's `assets/planb-lesson.css` on the
  first lesson.
- **Short.** One tangible win, within working memory, in the zone of proximal
  development, tied to the mission.
- **Beautiful & re-readable.** It will be revisited and may be printed.
- **Cited.** Every non-trivial claim links a `RESOURCES.md` entry via a `.cite`
  superscript and a `.sources` list at the foot.
- **At least one feedback loop** — a quiz, a reveal-after-attempt, or a task with
  a checkable outcome.
- **Accessible.** Real semantic elements, `lang`, focusable controls,
  `aria-live` on quiz feedback, sufficient contrast (the stylesheet handles it).

## Required parts (in order)

1. **Masthead** — `.kicker` ("LESSON 03 · door: btc202"), `<h1>`, `.lede` that
   names the win and ties it to the mission.
2. **Knowledge** — only what the skill needs. Cite as you go.
3. **Feedback loop** — quiz / reveal / task with immediate feedback.
4. **Primary source** — the single best thing to read/watch next (`.primary-source`).
5. **Your next door** — the `.next-door` CTA linking the recommended Plan ₿
   Academy course/tutorial by **content UUID** (never the human slug — a slug URL
   404s), plus the repo path. See the **Links** rules in `RIGHT-DOOR.md`.
6. **Ask your teacher** — reminder that you (the agent) are their teacher and can
   clarify anything.

## Quiz authoring

- Make every option the **same word/character count** — no formatting or length
  tells. Exactly one correct.
- Mark options with `data-correct="true|false"`; the script reveals feedback on
  click and locks the question.

## Skeleton (copy, then make it specific)

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Lesson 03 — Verify before you trust</title>
  <link rel="stylesheet" href="../assets/planb-lesson.css">
</head>
<body>
<main class="lesson">
  <p class="kicker">Lesson 03 · door: btc202</p>
  <h1>Verify a Bitcoin Core release before you run it</h1>
  <p class="lede">Your mission is to run your own node. Step one of sovereignty:
     never run software you haven't verified. You'll do it once, here.</p>
  <hr class="rule">

  <h2>Why signatures, not vibes</h2>
  <p>Bitcoin Core releases are signed so you can prove the binary is the one the
     maintainers built<span class="cite"><a href="#s1">1</a></span>.</p>

  <div class="callout">
    <span class="tag">Recall first</span>
    <p>Before reading on: what could go wrong if you skip verification?</p>
  </div>

  <h2>Check yourself</h2>
  <div class="quiz" aria-label="Knowledge check">
    <p class="q">What does verifying the release signature actually prove?</p>
    <button class="opt" data-correct="false">The node will always stay online</button>
    <button class="opt" data-correct="true">The binary matches the signed build</button>
    <button class="opt" data-correct="false">Your seed phrase is encrypted now</button>
    <p class="feedback" aria-live="polite"></p>
  </div>

  <details class="reveal">
    <summary>Show the exact commands</summary>
    <pre><code>gpg --verify SHA256SUMS.asc
sha256sum --check SHA256SUMS --ignore-missing</code></pre>
  </details>

  <p class="primary-source">
    <span class="tag">Read this next</span> —
    <a href="https://bitcoincore.org/en/download/">bitcoincore.org — verifying downloads</a>
  </p>

  <a class="next-door" href="https://planb.academy/en/courses/UUID-FROM-course.yml">
    <span class="nd-kicker">Your next door</span>
    <span class="nd-title">btc202 — Setting up your first Bitcoin node</span>
    <span class="nd-meta">intermediate · Plan ₿ Academy · repo: courses/btc202/</span>
  </a>

  <ol class="sources">
    <li id="s1"><a href="https://bitcoincore.org/en/download/">Bitcoin Core — release verification</a></li>
  </ol>

  <p class="ask-teacher">Stuck or curious? <strong>Ask your teacher</strong> — come
     back to the chat and I'll go deeper on anything here.</p>
</main>

<script>
  // Minimal, dependency-free quiz feedback. Factor into ../assets/lesson.js
  // once a second lesson needs it, then load with <script src="../assets/lesson.js" defer>.
  document.querySelectorAll('.quiz').forEach((quiz) => {
    const fb = quiz.querySelector('.feedback');
    quiz.querySelectorAll('.opt').forEach((btn) => {
      btn.addEventListener('click', () => {
        const right = btn.dataset.correct === 'true';
        btn.classList.add(right ? 'correct' : 'wrong');
        if (fb) {
          fb.textContent = right ? 'Correct — that is exactly the guarantee.'
                                 : 'Not quite. Re-read the section above, then retry.';
          fb.className = 'feedback ' + (right ? 'ok' : 'no');
        }
        if (right) quiz.querySelectorAll('.opt').forEach((o) => (o.disabled = true));
      });
    });
  });
</script>
</body>
</html>
```

## After writing

Open it for the learner with a portable command and tell them the path:

```bash
xdg-open lessons/0003-verify-before-you-trust.html   # Linux
open      lessons/0003-verify-before-you-trust.html   # macOS
```

Then, if there is evidence they learned something non-trivial, write a learning
record (`LEARNING-RECORD-FORMAT.md`) and update the recommended door in
`MISSION.md` if their level moved.
