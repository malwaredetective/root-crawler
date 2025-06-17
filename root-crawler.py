import os
import random
import argparse
import socket
import sqlite3
import sys

import docker
import pyfiglet
from colorama import Fore, Style, init
from docker.errors import ImageNotFound

# ---------------------- CONSTANTS -------------------------
init(autoreset=True)  # Initialize colorama for colored terminal output

DB_PATH = "database/root_crawler.db"
LEVEL_FILE = os.path.join("database", ".level")
DOCKER_IMAGE = "root-crawler"
DEFAULT_CREDENTIALS = "hacker:hacker"

# ---------------------- UTILITY FUNCTIONS -------------------------
def ascii_art():
    """Prints the ASCII art title for the application."""
    title = pyfiglet.figlet_format("Root Crawler", font="standard")
    print(Fore.CYAN + title)

def log_message(tag, message, tag_color):
    """
    Prints a formatted log message with a colored tag.
    Args:
        tag (str): The tag (e.g., "[ERROR]", "[SUCCESS]", "[INFO]").
        message (str): The message to print.
        tag_color (str): The color for the tag (e.g., Fore.RED, Fore.GREEN).
    """
    print(f"{tag_color}{tag}{Style.RESET_ALL} {message}")

def query_database(query, params=()):
    """
    Execute a SQL query with given parameters and return all results.

    Args:
        query (str): SQL query string.
        params (tuple): Parameters for query substitution.

    Returns:
        list: Query results as a list of tuples.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
    except sqlite3.Error as e:
        log_message("[ERROR]", f"Database query failed. Details: {e}", Fore.RED)
        return []

def get_docker_client():
    """
    Initialize and return the Docker client.

    Returns:
        docker.client.DockerClient or None: Docker client if successful, else None.
    """
    try:
        return docker.from_env()
    except Exception as e:
        log_message(
            "[ERROR]",
            (
                f"Failed to initialize Docker client. Details: {e}. "
                "If you configured this script within a Python virtual environment, make sure it is enabled."
            ),
            Fore.RED
        )
        return None

def is_port_in_use(port):
    """
    Returns True if the TCP port is already bound on localhost.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        result = s.connect_ex(('127.0.0.1', port))
        return result == 0
    
# ---------------------- DATABASE OPERATIONS -------------------------
def get_incomplete_levels(difficulty=None):
    """
    Retrieve all incomplete levels, optionally filtered by difficulty.
    Args:
        difficulty (str or None): Difficulty filter ('easy', 'medium', 'hard'), or None for all.
    Returns:
        list of tuples: (level, difficulty)
    """
    if difficulty:
        query = "SELECT level, difficulty FROM levels WHERE completed = 0 AND difficulty = ?"
        return query_database(query, (difficulty,))
    else:
        query = "SELECT level, difficulty FROM levels WHERE completed = 0"
        return query_database(query)

def get_hint_for_level(level_id):
    """Retrieve the hint for a specific level."""
    query = "SELECT hint FROM levels WHERE level = ?"
    result = query_database(query, (level_id,))
    return result[0][0] if result else None

def submit_flag(flag):
    """
    Process a submitted flag:
      Returns a tuple (status, level_num)
      - status: 'invalid', 'already_completed', 'completed', 'db_error'
      - level_num: level number if found, else None
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT level, completed FROM levels WHERE flag = ?", (flag,))
            result = cursor.fetchone()
    except sqlite3.Error as e:
        log_message("[ERROR]", f"Database error while validating flag: {e}", Fore.RED)
        return ("db_error", None)

    if not result:
        return ("invalid", None)
    level_num, completed = result
    if completed == 1:
        return ("already_completed", level_num)
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE levels SET completed = 1 WHERE level = ?", (level_num,))
            conn.commit()
        return ("completed", level_num)
    except sqlite3.Error as e:
        log_message("[ERROR]", f"Database error while updating level: {e}", Fore.RED)
        return ("db_error", level_num)

# ---------------------- MAIN FUNCTIONALITIES -------------------------
def show_hint():
    """
    Display a hint for the currently active level, if any.
    """
    client = get_docker_client()
    if not client:
        return

    tag_prefix = "root-crawler-level-"
    containers = [c for c in client.containers.list() if any(tag.startswith(tag_prefix) for tag in c.image.tags)]
    if not containers:
        log_message("[WARNING]", "No levels are currently active. Hints can only be displayed for active levels.", Fore.YELLOW)
        return

    if not os.path.exists(LEVEL_FILE):
        log_message("[WARNING]", f"No details about the currently active level were found in {LEVEL_FILE}.", Fore.YELLOW)
        return

    try:
        with open(LEVEL_FILE, "r") as level_file:
            active_level = None
            for line in level_file:
                if line.strip().startswith("Level:"):
                    try:
                        active_level = int(line.strip().split(":",1)[1].strip())
                    except Exception as e:
                        log_message("[ERROR]", f"Error parsing level from {LEVEL_FILE}: {e}", Fore.RED)
            if active_level is None:
                log_message("[ERROR]", f"Could not determine active level from {LEVEL_FILE}.", Fore.RED)
                return
            hint = get_hint_for_level(active_level)
            if hint:
                log_message("[HINT]", f"Level {active_level}: {hint}", Fore.MAGENTA)
            else:
                log_message("[ERROR]", f"No hint was found for Level {active_level}.", Fore.RED)
    except Exception as e:
        log_message("[ERROR]", f"Failed to read active level details. Details: {e}", Fore.RED)

def show_progress():
    """
    Display progress of all levels and their completion status.
    """
    query = "SELECT level, difficulty, completed FROM levels ORDER BY level ASC"
    levels = query_database(query)

    total_levels = len(levels)
    if total_levels == 0:
        log_message("[INFO]", "No levels found in the database.", Fore.CYAN)
        return

    total_completed = sum(1 for level in levels if level[2] == 1)
    completion_percentage = (total_completed / total_levels) * 100

    log_message("[INFO]", f"You have successfully pwned {completion_percentage:.1f}% of Root Crawler!\n", Fore.CYAN)
    for level, difficulty, completed in levels:
        status = Fore.GREEN + "Pwned" if completed == 1 else Fore.RED + "~"
        print(f"- Level {level} ({difficulty.capitalize()}): {status}")
    print("")

def reset_progress():
    """
    Reset the progress of all levels in the database, with user confirmation.
    """
    confirmation = input(
        f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} This action will reset all of your progress in the local database. Are you sure? (Yes/No): "
    ).strip().lower()
    if confirmation not in ("yes", "y"):
        log_message("[INFO]", "The reset operation was aborted.", Fore.CYAN)
        return

    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE levels SET completed = 0")
            conn.commit()
        log_message("[SUCCESS]", "Your progress has been successfully reset. All levels are now marked as incomplete.", Fore.GREEN)
    except sqlite3.Error as e:
        log_message("[ERROR]", f"Could not reset progress: {e}", Fore.RED)

def show_status():
    """
    Display details about the active level and running container, if any.
    """
    client = get_docker_client()
    if not client:
        return

    # List all running containers
    containers = client.containers.list()
    tag_prefix = "root-crawler-level-"

    # Filter containers that match the new tag scheme
    rc_containers = [
        container for container in containers
        if any(tag.startswith(tag_prefix) for tag in container.image.tags)
    ]

    if not rc_containers:
        log_message("[INFO]", "There are currently no active containers running.", Fore.CYAN)
        return

    if not os.path.exists(LEVEL_FILE):
        log_message("[INFO]", "No details about the currently active level were found.", Fore.CYAN)
        return

    try:
        log_message("[SUCCESS]", "A root-crawler instance is currently running ...\n", Fore.GREEN)
        with open(LEVEL_FILE, "r") as level_file:
            print(level_file.read())
        
        for container in rc_containers:
            tags = container.image.tags
            tag_display = tags[0] if tags else "<untagged>"
            print(
                f"CONTAINER ID: {container.short_id}\n"
                f"NAME: {container.name}\n"
                f"IMAGE: {tag_display}\n"
                f"STATUS: {container.status}\n"
                f"PORTS: {container.attrs['NetworkSettings']['Ports']}\n"
            )
    except Exception as e:
        log_message("[ERROR]", f"Failed to display container or level details. Details: {e}", Fore.RED)


def manage_containers(remove=False):
    """
    Stop (and optionally remove) all containers related to root-crawler.

    Args:
        remove (bool): If True, also remove the containers after stopping them.
    """
    client = get_docker_client()
    if not client:
        return

    containers = client.containers.list(all=True)
    tag_prefix = "root-crawler-level-"
    matched = False

    for container in containers:
        try:
            tags = container.image.tags
        except ImageNotFound:
            # The image for this container no longer exists; skip it but warn.
            log_message("[WARNING]", f"Image for container {container.short_id} ({container.name}) not found. Skipping.", Fore.YELLOW)
            continue
        except Exception as e:
            log_message("[ERROR]", f"Could not get image tags for container {container.short_id} ({container.name}): {str(e)}", Fore.RED)
            continue

        if any(tag.startswith(tag_prefix) for tag in tags):
            matched = True
            try:
                log_message("[INFO]", f"Stopping container: {container.short_id} ({container.name})", Fore.CYAN)
                container.stop()
            except Exception as e:
                log_message("[ERROR]", f"Failed to stop container {container.short_id} ({container.name}). Details: {e}", Fore.RED)
            if remove:
                try:
                    log_message("[INFO]", f"Removing container: {container.short_id} ({container.name})", Fore.CYAN)
                    container.remove(force=True)
                except Exception as e:
                    log_message("[ERROR]", f"Failed to remove container {container.short_id} ({container.name}). Details: {e}", Fore.RED)
    if not matched:
        msg = "No containers related to root-crawler were found." if remove else "No active containers related to root-crawler were found."
        log_message("[INFO]", msg, Fore.CYAN)
    elif remove:
        log_message("[SUCCESS]", "All root-crawler containers have been stopped and removed.", Fore.GREEN)


def stop_containers():
    """Stop all active containers tagged with 'root-crawler'."""
    manage_containers(remove=False)

def purge_containers():
    """Stop and remove all containers and images related to root-crawler, including root-crawler-labeled dangling images."""
    confirmation = input(f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} This will remove all root-crawler containers and images. Proceed? (Yes/No): ").strip().lower()
    if confirmation not in ("yes", "y"):
        print("Aborted.")
        return

    manage_containers(remove=True)
    client = get_docker_client()
    if not client:
        return

    base_images = ["khub/root-crawler-base:latest", "khub/root-crawler-legacy:latest"]
    for base_image in base_images:
        try:
            client.images.remove(base_image, force=True)
            log_message("[SUCCESS]", f"Removed image: {base_image}", Fore.GREEN)
        except docker.errors.ImageNotFound:
            log_message("[INFO]", f"The base image {base_image} not found. Skipping.", Fore.CYAN)
        except Exception as e:
            log_message("[ERROR]", f"Failed to remove base image {base_image}. Details: {e}", Fore.RED)

    tag_prefix = "root-crawler-level-"
    for image in client.images.list():
        for tag in image.tags:
            if tag.startswith(tag_prefix):
                try:
                    log_message("[INFO]", f"Removing image: {tag}", Fore.CYAN)
                    client.images.remove(image.id, force=True)
                except Exception as e:
                    log_message("[ERROR]", f"Failed to remove image {tag}. Details: {e}", Fore.RED)

    try:
        dangling_images = client.images.list(filters={"dangling": True, "label": "project=root-crawler"})
        if not dangling_images:
            log_message("[INFO]", "No dangling images with label project=root-crawler found.", Fore.CYAN)
        else:
            for img in dangling_images:
                try:
                    log_message("[INFO]", f"Removing dangling image ID: {img.id}", Fore.CYAN)
                    client.images.remove(img.id, force=True)
                except Exception as e:
                    log_message("[ERROR]", f"Failed to remove dangling image {img.id}. Details: {e}", Fore.RED)
            log_message("[SUCCESS]", f"Pruned {len(dangling_images)} dangling root-crawler images.", Fore.GREEN)
    except Exception as e:
        log_message("[ERROR]", f"Error during dangling image prune: {e}", Fore.RED)

    if os.path.exists(LEVEL_FILE):
        os.remove(LEVEL_FILE)
    log_message("[SUCCESS]", "All root-crawler containers, images, and caches have been removed.", Fore.GREEN)

def update_base_images():
    client = get_docker_client()
    if not client:
        return
    base_images = ["khub/root-crawler-base:latest", "khub/root-crawler-legacy:latest"]
    for image in base_images:
        try:
            log_message("[INFO]", f"Pulling {image} ...", Fore.CYAN)
            client.images.pull(image)
            log_message("[SUCCESS]", f"Pulled latest {image}.", Fore.GREEN)
        except Exception as e:
            log_message("[ERROR]", f"Failed to pull {image}. Details: {e}", Fore.RED)


def check_and_handle_existing_container(client):
    """
    Check for running root-crawler containers and prompt the user to stop them.

    Args:
        client: Docker client instance.
    Returns:
        bool: True if user wants to stop the container and proceed, False otherwise.
    """
    containers = client.containers.list()
    matching_containers = [
        container for container in containers
        if any(tag.startswith('root-crawler-level-') for tag in container.image.tags)
    ]

    if matching_containers:
        user_input = input(
            f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} There is currently an active container. Would you like to stop the running container(s) and spin up a new level? (Yes/No): "
        ).strip().lower()
        if user_input in ("yes", "y"):
            for container in matching_containers:
                try:
                    log_message("[INFO]", f"Stopping container: {container.short_id} ({container.name})", Fore.CYAN)
                    container.stop()
                except Exception as e:
                    log_message("[ERROR]", f"Failed to stop container {container.short_id}. Details: {e}", Fore.RED)
            return True
        elif user_input in ("no", "n"):
            log_message("[INFO]", "Operation aborted by the user.", Fore.CYAN)
            return False
        else:
            log_message("[ERROR]", "Invalid input. Operation aborted.", Fore.RED)
            return False
    return True

def build_and_run_instance(difficulty=None, port=2222):
    """
    Randomly select a level (optionally filtered by difficulty), build, and run the container.
    Args:
        difficulty (str or None): Difficulty to filter levels, or None for any.
    """
    client = get_docker_client()
    if not client:
        return

    if not check_and_handle_existing_container(client):
        return

    log_message("[INFO]", "Choosing a random level ...", Fore.CYAN)
    incomplete_levels = get_incomplete_levels(difficulty=difficulty)
    if not incomplete_levels:
        if difficulty:
            log_message("[SUCCESS]", f"Congratulations! You've completed all levels rated as: {difficulty.capitalize()}. Try a different difficulty or use the `--reset` flag to reset your progress!", Fore.GREEN)
        else:
            log_message("[SUCCESS]", "Congratulations! You've pwned all the levels. To restart the challenge, use the `--reset` flag to reset your progress!", Fore.GREEN)
        return

    # Select and launch a random incomplete level
    selected_level = random.choice(incomplete_levels)
    build_and_run_specific_level(selected_level[0], port)


def build_and_run_specific_level(level_id, port=2222):
    """
    Spin up a specific level based on the provided level ID.

    Args:
        level_id (int): The ID of the level to launch.
    """
    client = get_docker_client()
    if not client:
        return

    if not check_and_handle_existing_container(client):
        return

    query = "SELECT level, difficulty FROM levels WHERE level = ?"
    level_details = query_database(query, (level_id,))
    if not level_details:
        log_message("[ERROR]", f"Level {level_id} does not exist in the database.", Fore.RED)
        return

    docker_tag = f"{DOCKER_IMAGE}-level-{level_id}"
    difficulty = level_details[0][1]
    instance_path = f"level/{level_id}"
    credentials = DEFAULT_CREDENTIALS
    ssh_command = f"ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no hacker@127.0.0.1 -p {port}"

    log_message("[INFO]", f"Level {level_id}", Fore.CYAN)
    log_message("[INFO]", f"Difficulty: {difficulty.capitalize()}", Fore.CYAN)
    log_message("[INFO]", f"Credentials: `{credentials}`", Fore.CYAN)
    log_message("[INFO]", "Creating your instance ...", Fore.CYAN)

    try:
        # Build Docker image (show minimal context to user)
        client.images.build(path=instance_path, tag=docker_tag, rm=True)
        log_message("[SUCCESS]", "Docker build completed successfully!", Fore.GREEN)

        # Run the container, forward SSH on port 2222
        container = client.containers.run(
            docker_tag,
            detach=True,
            tty=True,
            ports={"22/tcp": port},
            auto_remove=True,
            hostname=f"root-crawler-level-{level_id}"
        )
        log_message("[SUCCESS]", "Your instance was successfully deployed!", Fore.GREEN)

        # Write active level details for reference
        with open(LEVEL_FILE, "w") as level_file:
            level_file.write(f"Level: {level_id}\n")
            level_file.write(f"Difficulty: {difficulty.capitalize()}\n")
            level_file.write(f"Credentials: `{credentials}`\n")
            level_file.write(f"Command: `{ssh_command}`\n")

        log_message("[INFO]", f"Log into your instance with SSH: `{ssh_command}`", Fore.CYAN)
        log_message("[CHALLENGE]", "Can you escalate your privileges to root and get the flag!?", Fore.RED)
    except docker.errors.BuildError as e:
        log_message("[ERROR]", f"Failed to build the Docker image for Level {level_id}. Details: {e}", Fore.RED)
    except docker.errors.ContainerError as e:
        log_message("[ERROR]", f"Failed to run the container for Level {level_id}. Details: {e}", Fore.RED)
    except Exception as e:
        log_message("[ERROR]", f"Failed to create your instance for Level {level_id}. Details: {e}", Fore.RED)

# ---------------------- MAIN -------------------------
def main():
    parser = argparse.ArgumentParser(
        description="A Python script that dynamically builds and deploys vulnerable Linux containers, providing a hands-on environment for practicing Linux Privilege Escalation techniques."
    )
    parser.add_argument("--random", action="store_true", help="Play a random level.")
    parser.add_argument("--difficulty", choices=["easy", "medium", "hard"], type=str.lower, help="Specify difficulty for --random")
    parser.add_argument("--flag", type=str, help="Submit a flag.")
    parser.add_argument("--hint", action="store_true", help="Display a hint for the current level.")
    parser.add_argument("--level", type=int, help="Play a specific level.")
    parser.add_argument("--port", type=int, help="Customize the local SSH port for the challenge containers. [Default 2222]")
    parser.add_argument("--progress", action="store_true", help="Display all levels, difficulties and your current progress.") 
    parser.add_argument("--reset", action="store_true", help="Reset all progress.")
    parser.add_argument("--status", action="store_true", help="Print details about the current active level and running container.")
    parser.add_argument("--stop", action="store_true", help="Stop all active containers related to root-crawler.")
    parser.add_argument("--purge", action="store_true", help="Stop and remove all containers related to root-crawler.")
    parser.add_argument("--update", action="store_true", help="Pull the latest root-crawler base images from dockerhub.")

    args = parser.parse_args()

    def validate_port(port):
        if port is None:
            return 2222
        try:
            p = int(port)
            if not (1 <= p <= 65535):
                log_message("[ERROR]", f"Invalid port: {port}. Must be between 1 and 65535.", Fore.RED)
                sys.exit(1)
            if is_port_in_use(p):
                log_message("[ERROR]", f"Port: {p} is already in use on this system. Please choose another port using the --port argument.", Fore.RED)
                sys.exit(1)
            if p < 1024:
                log_message("[WARNING]", f"Port: {p} is a privileged port and may require root privileges on your system.", Fore.YELLOW)
            return p
        except (TypeError, ValueError):
            log_message("[ERROR]", f"Invalid port: {port}. Must be an integer between 1 and 65535.", Fore.RED)
            sys.exit(1)
    
    custom_port = validate_port(args.port)

    if args.random:
        build_and_run_instance(difficulty=args.difficulty, port=custom_port)  
    elif args.level is not None:
        if args.level < 0:
            log_message("[ERROR]", "Level ID must be >= 0.", Fore.RED)
            return
        build_and_run_specific_level(args.level, port=custom_port)
    elif args.hint:
        show_hint()
    elif args.flag:
        status, level = submit_flag(args.flag)
        if status == "completed":
            log_message("[SUCCESS]", f"Flag validated. Level {level} marked as pwned!", Fore.GREEN)
        elif status == "already_completed":
            log_message("[INFO]", f"Flag validated. Level {level} was already pwned!", Fore.CYAN)
        elif status == "invalid":
            log_message("[ERROR]", "Invalid flag submitted.", Fore.RED)
        elif status == "db_error":
            log_message("[ERROR]", "A database error occurred while processing your flag. Please try again later.", Fore.RED)
    elif args.progress:
        show_progress()
    elif args.reset:
        reset_progress()
    elif args.status:
        show_status()
    elif args.stop:
        stop_containers()
    elif args.purge:
        purge_containers()
    elif args.update:
        update_base_images()

    else:
        parser.print_help()

if __name__ == "__main__":
    ascii_art()
    main()
