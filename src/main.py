"""CLI entrypoint for the src package."""

import argparse
from . import collectors, analyzer


def main():
    parser = argparse.ArgumentParser(description="Cloud Forensics Analyzer (src)")
    parser.add_argument("--source", choices=["dropbox", "gdrive"], required=False)
    args = parser.parse_args()

    if args.source == "dropbox":
        files = collectors.list_dropbox_files("/")
    elif args.source == "gdrive":
        files = collectors.collect_gdrive_files("root")
    else:
        print("No source specified. Exiting.")
        return

    meta = analyzer.analyze_file_metadata(files)
    print(f"Analyzed {len(meta)} files")


if __name__ == "__main__":
    main()
