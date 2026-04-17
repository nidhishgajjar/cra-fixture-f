import sys
from configctl.loaders import dispatch
from configctl.errors import ConfigError


def main(argv=None):
    argv = argv or sys.argv[1:]
    if not argv:
        print("usage: configctl <path>", file=sys.stderr)
        return 2
    path = argv[0]
    with open(path, "rb") as f:
        data = f.read()
    try:
        result = dispatch(path, data)
    except ConfigError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
