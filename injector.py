import sys

def merge_macho_binaries(target_bin, inject_bin, output_bin):
    try:
        
        with open(target_bin, "rb") as f:
            target_data = f.read()

        with open(inject_bin, "rb") as f:
            inject_data = f.read()

        merged_data = target_data + inject_data

        with open(output_bin, "wb") as f:
            f.write(merged_data)

        print(f"[+] Successfully created {output_bin}, containing both {target_bin} and {inject_bin}")
    
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python injector.py <target_bin> <inject_bin> <output_bin>")
        sys.exit(1)

    target_bin = sys.argv[1]
    inject_bin = sys.argv[2]
    output_bin = sys.argv[3]

    merge_macho_binaries(target_bin, inject_bin, output_bin)
