import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
import json

from mdtxupdater.core import MarkdownTranslationUpdater
from mdtxupdater.prompt import generate_llm_prompt


class App(tk.Tk):
    """
    Minimal cross-platform GUI using Tkinter (no external deps).
    Includes:
      - Source paragraph input used directly in the LLM prompt.
      - "Copy LLM Prompt" button: copies prompt to clipboard (no popup window).
      - Smaller JSON box, larger Log box (standard layout, no colored frame).
      - Clearer instructions for the paragraph number field.
      - Run Update button styled in red with hover effect.
    """

    def __init__(self) -> None:
        super().__init__()
        self.title("Polyglotter")
        self.geometry("960x720")
        self.minsize(900, 680)
        self.after(0, lambda: self.state('zoomed'))

        self.engine = MarkdownTranslationUpdater()
        self.files_map = {}

        self._build_widgets()

    # ---------------------------- UI Building -----------------------------

    def _build_widgets(self) -> None:
        pad = {"padx": 8, "pady": 6}

        # Top frame — directory + reference language
        top = ttk.Frame(self)
        top.pack(fill="x", **pad)

        self.dir_var = tk.StringVar()
        ttk.Label(top, text="Markdown folder:").pack(side="left")
        ttk.Entry(top, textvariable=self.dir_var, width=70).pack(side="left", padx=6)
        ttk.Button(top, text="Browse…", command=self._choose_dir).pack(side="left")

        ttk.Label(
            top,
            text="  Reference language (used for preview & source label):"
        ).pack(side="left", padx=(12, 4))
        self.ref_lang_var = tk.StringVar(value="en")
        ttk.Combobox(
            top,
            textvariable=self.ref_lang_var,
            values=self.engine.REF_LANG_CHOICES,
            state="readonly",
            width=6,
        ).pack(side="left")

        # Mode + paragraph
        mode_frame = ttk.Frame(self)
        mode_frame.pack(fill="x", **pad)

        self.mode_var = tk.StringVar(value="replace")
        ttk.Label(mode_frame, text="Mode:").pack(side="left")
        ttk.Radiobutton(mode_frame, text="Replace", variable=self.mode_var, value="replace").pack(side="left")
        ttk.Radiobutton(mode_frame, text="Append", variable=self.mode_var, value="append").pack(side="left", padx=(4, 0))

        # Clear instructions for the paragraph number
        ttk.Label(
            mode_frame,
            text="  Paragraph number (count non-empty lines INSIDE the bounded section; 1 = first non-empty line):"
        ).pack(side="left", padx=(12, 4))
        self.par_num = tk.Spinbox(mode_frame, from_=1, to=9999, width=6)
        self.par_num.pack(side="left")

        # Bounds frames (multiline)
        bounds = ttk.Frame(self)
        bounds.pack(fill="both", expand=False, **pad)

        lower_frame = ttk.LabelFrame(bounds, text="LOWER bound (START, *.webp, <chapterId>UUID</chapterId>, or code block)")
        upper_frame = ttk.LabelFrame(bounds, text="UPPER bound (END, *.webp, <chapterId>UUID</chapterId>, or code block)")
        lower_frame.pack(side="left", fill="both", expand=True, padx=(0, 4))
        upper_frame.pack(side="left", fill="both", expand=True, padx=(4, 0))

        self.lower_txt = tk.Text(lower_frame, height=8, wrap="word")
        self.upper_txt = tk.Text(upper_frame, height=8, wrap="word")
        self.lower_txt.pack(fill="both", expand=True, padx=6, pady=6)
        self.upper_txt.pack(fill="both", expand=True, padx=6, pady=6)

        # Source paragraph used in the LLM prompt
        src_frame = ttk.LabelFrame(
            self,
            text="Original paragraph to translate (this exact text will be placed in the LLM prompt)"
        )
        src_frame.pack(fill="both", expand=False, **pad)
        self.src_paragraph_txt = tk.Text(src_frame, height=6, wrap="word")
        self.src_paragraph_txt.pack(fill="both", expand=True, padx=6, pady=6)

        # JSON area (reduced height ~60%)
        json_frame = ttk.LabelFrame(self, text="Translations JSON (must contain 'translations')")
        json_frame.pack(fill="both", expand=False, **pad)
        self.json_txt = tk.Text(json_frame, height=5, wrap="word")
        self.json_txt.pack(fill="both", expand=True, padx=6, pady=6)

        # Buttons row
        btns = ttk.Frame(self)
        btns.pack(fill="x", **pad)
        ttk.Button(btns, text="Load files", command=self._load_files).pack(side="left")
        ttk.Button(btns, text="Preview", command=self._preview).pack(side="left", padx=4)
        ttk.Button(btns, text="Copy LLM Prompt", command=self._copy_prompt).pack(side="left", padx=4)

        # Custom red "Run Update" button (tk.Button for reliable colors across themes)
        self.run_btn = tk.Button(
            btns,
            text="Run Update",
            command=self._run_update,
            bg="#D32F2F",          # base red
            fg="white",            # white text
            activebackground="#B71C1C",
            activeforeground="white",
            relief="raised",
            bd=2,
            highlightthickness=0,
            cursor="hand2",
            padx=12,
            pady=6,
        )
        self.run_btn.pack(side="left", padx=4)

        # Hover effect for the red button
        self.run_btn_default_bg = "#D32F2F"
        self.run_btn_hover_bg = "#C62828"
        self.run_btn.bind("<Enter>", lambda e: self.run_btn.configure(bg=self.run_btn_hover_bg))
        self.run_btn.bind("<Leave>", lambda e: self.run_btn.configure(bg=self.run_btn_default_bg))

        # Log area (standard look, no colored frame)
        log_frame = ttk.LabelFrame(self, text="Log")
        log_frame.pack(fill="both", expand=True, **pad)

        # Larger log box to use the space gained by shrinking the JSON box
        self.log_txt = tk.Text(log_frame, height=14, wrap="word", state="disabled")
        self.log_txt.pack(fill="both", expand=True, padx=6, pady=6)

        self._log("Ready.")

    # ------------------------------- Actions -------------------------------

    def _choose_dir(self) -> None:
        d = filedialog.askdirectory(title="Choose the Markdown folder")
        if d:
            self.dir_var.set(d)

    def _load_files(self) -> None:
        try:
            self.files_map = self.engine.find_markdown_files(self.dir_var.get().strip())
            self._log(f"Found {len(self.files_map)} translation files.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _preview(self) -> None:
        if not self.files_map:
            self._load_files()
            if not self.files_map:
                return
        try:
            ref_file = self.engine.pick_reference_file(self.files_map, self.ref_lang_var.get())
            insert_mode = (self.mode_var.get() == "append")
            paragraph_num = int(self.par_num.get())
            lower_raw = self.lower_txt.get("1.0", "end").strip()
            upper_raw = self.upper_txt.get("1.0", "end").strip()
            a, b = self.engine.preview_context(ref_file, lower_raw, upper_raw, paragraph_num, insert_mode)
            if insert_mode:
                self._log("Preview (APPEND):\n- Above: " + a + "\n- Below: " + b)
            else:
                self._log("Preview (REPLACE):\n- Start: " + a + "\n- End: " + b)
            messagebox.showinfo("Preview", "Check the Log panel for preview context.")
        except Exception as e:
            messagebox.showerror("Preview error", str(e))

    def _copy_prompt(self) -> None:
        """Build and copy the LLM prompt directly to clipboard."""
        src_lang = self.ref_lang_var.get()
        original = self.src_paragraph_txt.get("1.0", "end").strip()
        if not original:
            messagebox.showwarning("Missing text", "Please paste the original paragraph to translate.")
            return
        prompt = generate_llm_prompt(src_lang, original)
        try:
            self.clipboard_clear()
            self.clipboard_append(prompt)
            # Ensure clipboard is populated even if the app closes quickly
            self.update()
            self._log("LLM prompt copied to clipboard.")
            messagebox.showinfo("Copied", "LLM prompt has been copied to your clipboard.")
        except Exception as e:
            messagebox.showerror("Clipboard error", str(e))

    def _run_update(self) -> None:
        if not self.files_map:
            self._load_files()
            if not self.files_map:
                return

        try:
            data = json.loads(self.json_txt.get("1.0", "end").strip())
        except Exception as e:
            messagebox.showerror("JSON error", f"Invalid JSON: {e}")
            return

        if "translations" not in data:
            messagebox.showerror("JSON error", "JSON must contain a 'translations' key.")
            return

        insert_mode = (self.mode_var.get() == "append")
        paragraph_num = int(self.par_num.get())
        lower_raw = self.lower_txt.get("1.0", "end").strip()
        upper_raw = self.upper_txt.get("1.0", "end").strip()

        def worker():
            success = 0
            for lang, path in self.files_map.items():
                if lang in data["translations"]:
                    ok = self.engine.update_file(
                        path, lower_raw, upper_raw, paragraph_num, data["translations"][lang], insert_mode
                    )
                    if ok:
                        self._log(f"✓ {Path(path).name} updated")
                        success += 1
                    else:
                        self._log(f"✗ Failed on {Path(path).name}")
                else:
                    self._log(f"⚠ No translation provided for {lang}")
            self._log(f"Completed: {success}/{len(self.files_map)} files updated")

        threading.Thread(target=worker, daemon=True).start()

    # ------------------------------- Utils ---------------------------------

    def _log(self, msg: str) -> None:
        self.log_txt.configure(state="normal")
        self.log_txt.insert("end", msg + "\n")
        self.log_txt.see("end")
        self.log_txt.configure(state="disabled")


def main() -> None:
    App().mainloop()
