import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
import json

from mdtxupdater.core import MarkdownTranslationUpdater
from mdtxupdater.prompt import generate_llm_prompt


class App(tk.Tk):
    """
    Minimal cross-platform GUI using Tkinter (no external dependencies).
    Provides fields for all inputs, a preview action, LLM prompt generation,
    and update execution with a simple log area.
    """

    def __init__(self) -> None:
        super().__init__()
        self.title("Markdown Translation Updater")
        self.geometry("960x720")
        self.minsize(900, 680)

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

        ttk.Label(top, text="  Reference language:").pack(side="left", padx=(12, 4))
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

        ttk.Label(mode_frame, text="  Paragraph number:").pack(side="left", padx=(12, 4))
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

        # JSON area
        json_frame = ttk.LabelFrame(self, text="Translations JSON (must contain 'translations')")
        json_frame.pack(fill="both", expand=True, **pad)
        self.json_txt = tk.Text(json_frame, height=12, wrap="word")
        self.json_txt.pack(fill="both", expand=True, padx=6, pady=6)

        # Buttons
        btns = ttk.Frame(self)
        btns.pack(fill="x", **pad)
        ttk.Button(btns, text="Load files", command=self._load_files).pack(side="left")
        ttk.Button(btns, text="Preview", command=self._preview).pack(side="left", padx=4)
        ttk.Button(btns, text="Generate LLM Prompt", command=self._generate_prompt).pack(side="left", padx=4)
        ttk.Button(btns, text="Run Update", command=self._run_update).pack(side="left", padx=4)

        # Log area
        log_frame = ttk.LabelFrame(self, text="Log")
        log_frame.pack(fill="both", expand=True, **pad)
        self.log_txt = tk.Text(log_frame, height=10, wrap="word", state="disabled")
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

    def _generate_prompt(self) -> None:
        src = self.ref_lang_var.get()
        prompt = generate_llm_prompt(src)
        # Show in a separate window for easy copy
        win = tk.Toplevel(self)
        win.title("LLM Prompt (copy & paste)")
        win.geometry("800x600")
        txt = tk.Text(win, wrap="word")
        txt.pack(fill="both", expand=True)
        txt.insert("1.0", prompt)

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
                    ok = self.engine.update_file(path, lower_raw, upper_raw, paragraph_num, data["translations"][lang], insert_mode)
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
