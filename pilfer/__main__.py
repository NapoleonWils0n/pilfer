import sys
def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]
    import pilfer
    print("pilfer is imported.")
    print("usage command line >>>>  pilfer file_name.txt -t 00:00:00")

    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do.

if __name__ == "__main__":
    main()
