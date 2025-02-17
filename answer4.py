import os
import subprocess
def check_updates():
    cmd = "apt list --upgradable"
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        updates = result.stdout.strip().split("\n")[1:] 
        return updates
    except Exception as e:
        print(f" Error checking updates: {e}")
        return []


def list_updates(updates):
    print("\n Available Updates:")
    for idx, package in enumerate(updates, 1):
        print(f"{idx}. {package}")
    print("\n")

def install_updates(updates):
    choice = input("Enter package index to update (or 'all' to update everything): ").strip()

    if choice.lower() == "all":
        install_cmd = "apt upgrade -y" if package_manager == "apt" else "yum update -y"
    else:
        try:
            index = int(choice) - 1
            if 0 <= index < len(updates):
                package_name = updates[index].split()[0]  # Extract package name
                install_cmd = f"apt install -y {package_name}" if package_manager == "apt" else f"yum update -y {package_name}"
            else:
                print(" Invalid index. Exiting.")
                return
        except ValueError:
            print(" Invalid input. Exiting.")
            return

    print(f"\nRunning: {install_cmd}\n")
    
    try:
        result = subprocess.run(install_cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("Update successful!")
        else:
            error_message = f" Update failed for {install_cmd}: {result.stderr}"
            print(error_message)
            with open("update_log.txt", "a") as log_file:
                log_file.write(error_message + "\n")
    except Exception as e:
        print(f"Error installing updates: {e}")

# Main execution
if __name__ == "__main__":

    updates = check_updates()

    if not updates:
        print(" All packages are up to date.")
    else:
        list_updates(updates)
        install_updates(updates)

