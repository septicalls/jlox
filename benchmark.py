import subprocess
import os

pwd = os.getcwd()
script_directory = pwd + "/benchmark"
java_lox_interpreter = pwd + "/jlox.sh"


def run_lox_script(script_filename):
    try:
        script_path = os.path.join(script_directory, script_filename)
        result = subprocess.run(
            [java_lox_interpreter, script_path],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr


def main():
    lox_scripts = [
        filename
        for filename in os.listdir(script_directory)
        if filename.endswith(".lox")
    ]

    for script_filename in lox_scripts:
        script_name = os.path.splitext(script_filename)[0]
        print("=========================================")
        print(f"Running script: {script_name}")

        script_output = run_lox_script(script_filename)
        print(script_name)


if __name__ == "__main__":
    main()
