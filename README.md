<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mail Merge Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        h1, h2 {
            color: #0056b3;
        }
        code {
            background-color: #e0e0e0;
            padding: 0.2em 0.4em;
            font-family: "Courier New", Courier, monospace;
        }
        pre {
            background-color: #e0e0e0;
            padding: 10px;
            font-family: "Courier New", Courier, monospace;
            overflow-x: auto;
        }
        ul {
            list-style-type: none;
        }
        li {
            margin: 10px 0;
        }
        .file-tree {
            margin: 20px;
            padding: 10px;
            background-color: #e7e7e7;
        }
        .file-tree pre {
            background-color: #f1f1f1;
        }
    </style>
</head>
<body>

    <h1>Mail Merge Project</h1>

    <h2>Description</h2>
    <p>This project automates the process of generating personalized letters for a list of names. The program reads a starting letter template and then replaces a placeholder <code>[name]</code> with names from a provided <code>names.txt</code> file. For each name, a personalized letter is created and saved as a new text file in the specified output directory.</p>

    <h2>Files Structure</h2>
    <div class="file-tree">
        <pre>
        files/
        ├── mail-merge/
            ├── input/
                ├── names/
                    └── names.txt
                ├── letter/
                    └── starting_letter.txt
            ├── output/
        </pre>
    </div>

    <h2>Dependencies</h2>
    <p>This project uses only the built-in Python modules, so no additional dependencies are required.</p>

    <h2>File Overview</h2>
    <ul>
        <li><strong>names.txt</strong>: Contains a list of names. Each name is expected to be on a new line (e.g., <code>John</code>, <code>Alice</code>, <code>Bob</code>).</li>
        <li><strong>starting_letter.txt</strong>: A template letter that contains the placeholder <code>[name]</code>. For example:
            <pre>
            Dear [name],

            This is a personalized letter just for you!

            Sincerely,
            Your Team
            </pre>
        </li>
        <li><strong>output/</strong>: The directory where the generated personalized letters will be saved. Each letter will be saved as <code>letter_<name>.txt</code>.</li>
    </ul>

    <h2>How to Run</h2>
    <ol>
        <li>Make sure the directory structure looks like this:</li>
        <div class="file-tree">
            <pre>
            files/
            ├── mail-merge/
                ├── input/
                    ├── names/
                        └── names.txt
                    ├── letter/
                        └── starting_letter.txt
                ├── output/
            </pre>
        </div>

        <li>Ensure that the <code>names.txt</code> file is populated with names, one per line, such as:</li>
        <pre>
        John
        Alice
        Bob
        </pre>

        <li>Run the <code>main.py</code> script.</li>
        <pre>
        python main.py
        </pre>

        <li>After running the script, check the <code>output</code> directory. It will contain personalized letter files named like <code>letter_John.txt</code>, <code>letter_Alice.txt</code>, etc.</li>
    </ol>

    <h2>Code Explanation</h2>
    <h3>Reading the Names</h3>
    <pre>
    names = []
    with open(r'.\files\mail-merge\input\names\names.txt', 'r') as f:
        data = f.read()
        names = data.split('\n')
    </pre>
    <p>This code reads the <code>names.txt</code> file and stores each name in the <code>names</code> list. It splits the contents by line breaks.</p>

    <h3>Mail Merge Process</h3>
    <pre>
    for name in names:
        file_name = f'letter_{name}.txt'
        file_path = os.path.join(path, file_name)
        
        with open(r'.\files\mail-merge\input\letter\starting_letter.txt', 'r') as f:
            content = f.read()
            content = content.replace('[name]', name)  # Replace placeholder with actual name
            
            with open(file_path, 'w') as file:
                file.write(content)
    </pre>
    <p>This loop processes each name, creates a personalized letter by replacing the <code>[name]</code> placeholder in the template with the actual name, and then saves the result in the <code>output</code> directory as <code>letter_<name>.txt</code>.</p>

    <h2>Example Output</h2>
    <p>After running the script with the example <code>names.txt</code>, the following files will be created in the <code>output</code> directory:</p>
    <ul>
        <li><code>letter_John.txt</code></li>
        <li><code>letter_Alice.txt</code></li>
        <li><code>letter_Bob.txt</code></li>
    </ul>
    <p>Each file will contain a personalized version of the <code>starting_letter.txt</code> template, with the <code>[name]</code> placeholder replaced by the actual name.</p>

    <h2>Troubleshooting</h2>
    <ul>
        <li>Ensure that the file paths in the code are correct and relative to where you are running the script.</li>
        <li>Verify that <code>names.txt</code> and <code>starting_letter.txt</code> exist and are correctly formatted.</li>
        <li>If you encounter permission issues with writing files, ensure the <code>output/</code> directory is writable.</li>
    </ul>

</body>
</html>
