# Binary Injector (Binder) - macOS

## 📌 Introduction
This project is a **Mach-O Binary Binder** that merges two executable programs into one. When the merged file is executed, it runs both original programs.

## ⚙️ How It Works
1. Reads the target Mach-O binary.
2. Reads the second binary to be injected.
3. Merges the two binaries.
4. Outputs a new executable that runs both programs.

## 🖥️ Usage
1. Make the files:
   ```bash
   echo -e '#!/bin/bash\necho "01"' > bin
   chmod +x bin
   echo -e '#!/bin/bash\necho "hello world"' > helloworld
   chmod +x helloworld
   ```
2. Run the script:
   ```bash
   python3 injector.py bin helloworld merged_bin
   ```
3. Grant execution permission to the merged binary:
   ```bash
   chmod +x merged_bin
   ```
4. Execute it:
   ```bash
   ./merged_bin
   ```
5. 📜 Example Output
   ```bash
   01
   hello world
   ```


# injector
