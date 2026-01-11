import subprocess # allows us to run other programs (external commands, like Git)
import sys # allows us to stop cleanly on failure/ success


def run(cmd: list[str]) -> None: # list makes the whole process safer
    result = subprocess.run(cmd)
    if result.returncode != 0:
        sys.exit(result.returncode)


def main() -> None:
    status = subprocess.run(["git", "status", "--porcelain"], capture_output = True, text = True) # --porcelain tells Git to make the output machine-readable, capture_output saves it in status.stdout (standard output), text saves it as string, not bytes

    if not status.stdout:
        print("no changes to stage")
        sys.exit(0)

    run(["git", "add", "."])

    message = input("enter commit message: ").strip()
    if not message:
        run(["git", "reset"])
        print("Aborted, no commit message, unstaged changes")
        sys.exit(1)

    run(["git", "commit", "-m", message])
    run(["git", "push"])


if __name__ == "__main__":
    main()