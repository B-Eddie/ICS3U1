import time
import os
import subprocess
import sys
from pathlib import Path


def watch_and_run():
    # get path of file to watch
    house_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "EddieA1P1.py")

    print(f"Watching {house_path} for changes...")
    last_modified = 0
    current_process = None

    # Set window position (x=100, y=100)
    my_env = os.environ.copy()
    my_env["SDL_VIDEO_WINDOW_POS"] = "1500,100" # ipad

    try:
        while True:
            try:
                current_modified = os.path.getmtime(house_path)
                if current_modified > last_modified:
                    print(f"\nFile changed, restarting...")

                    # Kill previous process if it exists
                    if current_process and current_process.poll() is None:
                        current_process.terminate()
                        current_process.wait()

                    # new process
                    current_process = subprocess.Popen(
                        [sys.executable, house_path], env=my_env
                    )
                    last_modified = current_modified

                time.sleep(0.1)  # delay between checks

            except Exception as e:
                print(f"Error: {e}")
                time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopping watchdog...")
        if current_process and current_process.poll() is None:
            current_process.terminate()
            current_process.wait()


if __name__ == "__main__":
    watch_and_run()
