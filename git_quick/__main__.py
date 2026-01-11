import subprocess # allows us to run other programs (external commands, like Git)
import sys # allows us to stop cleanly on failure/ success


def run(cmd: list[str]) -> None: # list makes the whole process safer
    result = subprocess.run(cmd)
    if result.returncode != 0:
        sys.exit(result.returncode)


def main() -> None:
    run(["git", "add", "."])

    message = input("enter commit message: ").strip()
    if not message:
        print("Aborted, no commit message")
        sys.exit(1)

    run(["git", "commit", "-m", message])
    run(["git", "push"])


if __name__ == "__main__":
    main()