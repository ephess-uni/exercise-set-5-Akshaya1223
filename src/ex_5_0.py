"""ex_5_0.py"""


def line_count(infile):
 #   pass
    file=open(infile,'rt')
    count=0
    for i in file.readlines():
        count+=1
    print(count)

if __name__ == "__main__":
    # get the utility function for path discovery
    try:
        from src.util import get_repository_root
    except ImportError:
        from util import get_repository_root

    # Test line_count with a file from the data directory
    data_directory = get_repository_root() / "data"
    line_count(data_directory / "ex_5_2-data.csv")
