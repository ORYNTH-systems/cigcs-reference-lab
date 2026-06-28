import sys
import json

from engine import CIGCSEngine

def main():
    if len(sys.argv) < 2:
        print("Usage: cigcs run <case_dir>")
        sys.exit(1)

    command = sys.argv[1]

    if command != "run":
        print("Only 'run' supported in v1.0 production mode")
        sys.exit(1)

    case_dir = sys.argv[2]

    engine = CIGCSEngine()

    result = engine.run_all(case_dir)

    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
