import sys
import subprocess
from datetime import datetime

def run():
    print("=" * 56)
    print("          Automaticky Git Push na GitHub")
    print("=" * 56)

    # Zobrazeni stavu
    print("\nPrehled zmen:")
    subprocess.run(["git", "status", "-s"])

    # Commit zprava
    if len(sys.argv) > 1:
        commit_msg = " ".join(sys.argv[1:])
    else:
        user_input = input("\nZadej popis zmen (stiskni ENTER pro automaticky popis): ").strip()
        if user_input:
            commit_msg = user_input
        else:
            now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
            commit_msg = f"Aktualizace: {now_str}"

    print("\n1/3 Pridavam soubory (git add .)...")
    res_add = subprocess.run(["git", "add", "."])
    if res_add.returncode != 0:
        print("\n[CHYBA] git add selhal.")
        return

    print(f'2/3 Vytvarim commit: "{commit_msg}"...')
    res_commit = subprocess.run(["git", "commit", "-m", commit_msg])
    if res_commit.returncode != 0:
        print("\n[INFO] Nebyly nalezeny zadne nove zmeny k odeslani.")
        return

    print("3/3 Odesilam na GitHub (git push origin main)...")
    res_push = subprocess.run(["git", "push", "origin", "main"])
    if res_push.returncode == 0:
        print("\n" + "=" * 56)
        print("[OK] Vse bylo uspesne nahrano na GitHub!")
        print("=" * 56)
    else:
        print("\n" + "=" * 56)
        print("[CHYBA] Nahravani na GitHub se nezdarilo.")
        print("=" * 56)

if __name__ == "__main__":
    run()
