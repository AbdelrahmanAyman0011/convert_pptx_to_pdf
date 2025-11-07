import os
import subprocess

def pptx_to_pdf(input_path, output_path=None):
    if not output_path:
        output_path = os.path.splitext(input_path)[0] + ".pdf"

    # Run LibreOffice and capture its output
    result = subprocess.run([
        "libreoffice", "--headless", "--convert-to", "pdf", input_path,
        "--outdir", os.path.dirname(output_path)
    ], capture_output=True, text=True)

    if result.returncode == 0 and os.path.exists(output_path):
        print(f"✅ Converted successfully: {input_path} → {output_path}")
    else:
        print(f"❌ Conversion failed for: {input_path}")
        print("🔍 LibreOffice output:\n", result.stderr or result.stdout)

def convert_all_pptx_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pptx"):
            full_input_path = os.path.join(folder_path, filename)
            pptx_to_pdf(full_input_path)

if __name__ == "__main__":
    choice = input("Do you want to convert a (f)ile or a (d)irectory? [f/d]: ").strip().lower()

    if choice == "f":
        pptx_file = input("Enter the full path to the .pptx file: ").strip() or "/home/bedo/Downloads/10.pptx"
        if os.path.isfile(pptx_file) and pptx_file.lower().endswith(".pptx"):
            pptx_to_pdf(pptx_file)
        else:
            print("❌ Invalid file path or not a .pptx file.")
    elif choice == "d":
        folder = input("Enter the full directory path: ").strip() or "/home/bedo/Downloads"
        if os.path.isdir(folder):
            convert_all_pptx_in_folder(folder)
        else:
            print("❌ Invalid directory path.")
    else:
        print("❌ Invalid choice. Please enter 'f' or 'd'.")

