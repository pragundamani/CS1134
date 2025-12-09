import argparse
import re
import sys
from pathlib import Path

# Base directory for all folders
BASE_DIR = Path(r"./").expanduser().resolve()


def prompt_if_missing(
    folder_arg: str | None, number_arg: str | None
) -> tuple[str, str]:
    folder = folder_arg or input("Enter folder: ").strip()
    number = number_arg or input("Enter homework number (digits only): ").strip()
    return folder, number


def validate_inputs(folder: str, number: str) -> tuple[Path, str]:
    raw = Path((folder or "").strip())
    # Resolve folder: if not absolute, treat as subfolder of BASE_DIR
    p = (BASE_DIR / raw) if not raw.is_absolute() else raw
    p = p.expanduser()
    # If the folder does not exist, create it
    try:
        if not p.exists():
            p.mkdir(parents=True, exist_ok=True)
            print(f"Created folder: {p}")
    except Exception as e:
        print(f"Failed to create folder: {p}: {e}", file=sys.stderr)
        sys.exit(1)
    # Validate that the path is a directory
    if not p.is_dir():
        print(f"Path is not a directory: {p}", file=sys.stderr)
        sys.exit(1)
    # Validate homework number
    if not re.fullmatch(r"\d+", number or ""):
        print("Homework number must be digits only.", file=sys.stderr)
        sys.exit(1)
    return p.resolve(), number


def is_hw_pdf(name: str, number: str) -> bool:
    # Skip any file named exactly hw{number}.pdf (case-insensitive)
    return re.fullmatch(rf"hw{re.escape(number)}\.pdf", name, re.IGNORECASE) is not None


# Prompt helper for yes/no
def ask_yes_no(message: str, default: bool | None = False) -> bool:
    prompt = " [y/n]: "
    if default is True:
        prompt = " [Y/n]: "
    elif default is False:
        prompt = " [y/N]: "
    while True:
        resp = input(message + prompt).strip().lower()
        if not resp and default is not None:
            return default
        if resp in ("y", "yes"):
            return True
        if resp in ("n", "no"):
            return False
        print("Please answer y or n.")


# New helpers to validate range and create q-files
def validate_q_range(q_start: int, q_end: int) -> tuple[int, int]:
    if not isinstance(q_start, int) or not isinstance(q_end, int):
        print("Question numbers must be integers.", file=sys.stderr)
        sys.exit(1)
    if q_start < 1 or q_end < 1 or q_start > q_end:
        print(
            "Invalid question range. Ensure start/end are >= 1 and start <= end.",
            file=sys.stderr,
        )
        sys.exit(1)
    return q_start, q_end


def create_q_files(
    folder: Path, number: str, q_start: int, q_end: int
) -> tuple[int, int, int]:
    created = skipped = errors = 0
    for q in range(q_start, q_end + 1):
        fname = f"pd2752_hw{number}_q{q}.py"
        fpath = folder / fname
        if fpath.exists():
            print(f"Skip (exists): {fname}")
            skipped += 1
            continue
        try:
            with fpath.open("w", encoding="utf-8") as fh:
                fh.write(f"#q{q} answer pd2752\n")
            print(f"Created: {fname}")
            created += 1
        except Exception as e:
            print(f"Failed to create {fname}: {e}", file=sys.stderr)
            errors += 1
    return created, skipped, errors


# New: creators for lab/hw structures under BASE_DIR
def create_lab_structure(base_dir: Path, number: str) -> tuple[int, int, int]:
    created = skipped = errors = 0
    lab_dir = base_dir / f"L{number}"
    try:
        if lab_dir.exists():
            print(f"Skip (exists): {lab_dir}")
            skipped += 1
        else:
            lab_dir.mkdir(parents=True, exist_ok=True)
            print(f"Created: {lab_dir}")
            created += 1
    except Exception as e:
        print(f"Failed to create {lab_dir}: {e}", file=sys.stderr)
        errors += 1
        # If folder failed, abort file creation
        return created, skipped, errors

    lab_py = lab_dir / f"lab{number}.py"
    theory_md = (
        lab_dir / "thory.md"
    )  # intentional? If 'theory.md' is desired, change filename accordingly
    # Correct the filename to 'theory.md'
    theory_md = lab_dir / "theory.md"

    for path in (lab_py, theory_md):
        try:
            if path.exists():
                print(f"Skip (exists): {path.name}")
                skipped += 1
                continue
            # Create empty files; minimal content optional
            content = "" if path.suffix != ".py" else f"# lab {number}\n"
            path.write_text(content, encoding="utf-8")
            print(f"Created: {path.name}")
            created += 1
        except Exception as e:
            print(f"Failed to create {path.name}: {e}", file=sys.stderr)
            errors += 1
    return created, skipped, errors


def create_hw_structure(base_dir: Path, number: str) -> tuple[int, int, int]:
    created = skipped = errors = 0
    hw_dir = base_dir / f"hw{number}"
    try:
        if hw_dir.exists():
            print(f"Skip (exists): {hw_dir}")
            skipped += 1
        else:
            hw_dir.mkdir(parents=True, exist_ok=True)
            print(f"Created: {hw_dir}")
            created += 1
    except Exception as e:
        print(f"Failed to create {hw_dir}: {e}", file=sys.stderr)
        errors += 1
    return created, skipped, errors


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(
        description="Prefix files with pd2752_hw{N}_ while skipping hw{N}.pdf."
    )
    ap.add_argument("--folder", "-f", help="Folder containing files to rename")
    ap.add_argument("--number", "-n", help="Homework number (digits only)")
    # New flags for creating q-files
    ap.add_argument(
        "--make-q-files",
        "-q",
        action="store_true",
        help="Create files pd2752_hw{N}_q{q}.py for a question range",
    )
    ap.add_argument("--q-start", type=int, help="Starting question number (inclusive)")
    ap.add_argument("--q-end", type=int, help="Ending question number (inclusive)")
    args = ap.parse_args(argv)

    folder_str, number_str = prompt_if_missing(args.folder, args.number)
    folder, number = validate_inputs(folder_str, number_str)

    prefix = f"pd2752_hw{number}_"
    renamed = skipped = errors = 0

    script_path = Path(__file__).resolve()

    for entry in folder.iterdir():
        if not entry.is_file():
            continue
        name = entry.name

        # Do not touch the script itself if it lives in the same folder
        if entry.resolve() == script_path:
            print(f"Skip (this script): {name}")
            skipped += 1
            continue

        if name.startswith(prefix):
            print(f"Skip (already prefixed): {name}")
            skipped += 1
            continue

        if is_hw_pdf(name, number):
            print(f"Skip (protected hw{number}.pdf): {name}")
            skipped += 1
            continue

        new_name = prefix + name
        target = entry.with_name(new_name)
        if target.exists():
            print(f"Skip (target exists): {new_name}")
            skipped += 1
            continue

        try:
            entry.rename(target)
            print(f"Renamed: {name} -> {new_name}")
            renamed += 1
        except Exception as e:
            print(f"Failed: {name} -> {new_name}: {e}", file=sys.stderr)
            errors += 1

    # Optional creation of q-files (ask user y/n; flag sets default)
    created = c_skipped = c_errors = 0
    default_choice = True if args.make_q_files else False
    create_qs = ask_yes_no("Create q-files?", default=default_choice)
    if create_qs:
        q_start = args.q_start
        q_end = args.q_end
        # Prompt if missing
        if q_start is None:
            try:
                q_start = int(input("Enter starting question number: ").strip())
            except Exception:
                print("Invalid starting question number.", file=sys.stderr)
                sys.exit(1)
        if q_end is None:
            try:
                q_end = int(input("Enter ending question number: ").strip())
            except Exception:
                print("Invalid ending question number.", file=sys.stderr)
                sys.exit(1)
        q_start, q_end = validate_q_range(q_start, q_end)
        created, c_skipped, c_errors = create_q_files(folder, number, q_start, q_end)

    # New: creation of lab/hw structures under BASE_DIR
    s_created = s_skipped = s_errors = 0
    if ask_yes_no("Create lab or hw structure?", default=False):
        # Choose type
        kind = ""
        while kind not in ("lab", "hw"):
            kind_in = input("Type to create (lab/hw): ").strip().lower()
            if kind_in in ("l", "lab"):
                kind = "lab"
            elif kind_in in ("h", "hw"):
                kind = "hw"
            else:
                print("Please enter 'lab' or 'hw'.")
        if kind == "lab":
            s_created, s_skipped, s_errors = create_lab_structure(BASE_DIR, number)
        else:
            s_created, s_skipped, s_errors = create_hw_structure(BASE_DIR, number)
        print(
            f"Structure summary: Created: {s_created}, Skipped: {s_skipped}, Errors: {s_errors}"
        )

    # Summaries and exit code
    print(f"Rename summary: Renamed: {renamed}, Skipped: {skipped}, Errors: {errors}")
    if create_qs:
        print(
            f"Create summary: Created: {created}, Skipped: {c_skipped}, Errors: {c_errors}"
        )
    overall_errors = errors + c_errors + s_errors
    print("Done.")
    return 0 if overall_errors == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
