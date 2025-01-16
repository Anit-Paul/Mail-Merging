# Mail Merge Project

## Description
This project automates the process of generating personalized letters for a list of names. The program reads a starting letter template and replaces a placeholder `[name]` with names from a provided `names.txt` file. For each name, a personalized letter is created and saved as a new text file in the specified output directory.

## Files Structure
- `main.py`: The Python script that performs the mail merge.
- `files/`
  - `input/`
    - `names/`
      - `names.txt`: Contains a list of names, one per line.
    - `letter/`
      - `starting_letter.txt`: The template letter with a placeholder `[name]`.
  - `output/`: The directory where the generated personalized letters will be saved.

## Dependencies
No external dependencies. The project uses built-in Python modules.

## How to Run
1. Ensure the directory structure looks like this:
    ```
    files/
    ├── mail-merge/
        ├── input/
            ├── names/
                └── names.txt
            ├── letter/
                └── starting_letter.txt
        ├── output/
    ```

2. Populate `names.txt` with names, one per line (e.g., `John`, `Alice`, `Bob`).
3. Run the script `main.py`:
    ```
    python main.py
    ```

4. After running the script, check the `output/` directory for the personalized letters. Each file will be named `letter_<name>.txt`.

## Example Output
- `letter_John.txt`
- `letter_Alice.txt`
- `letter_Bob.txt`

Each file will contain a personalized letter with the `[name]` placeholder replaced by the actual name.

## Troubleshooting
- Ensure the file paths are correct.
- Check that `names.txt` and `starting_letter.txt` are correctly formatted.
- Make sure the `output/` directory is writable.

