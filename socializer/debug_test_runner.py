"""Helper to run tests with debugging via vscode enabled.

Usage:
    Run:
        python debug_test_runner.py -t <test_file_or_directory>
    inside container
"""
import argparse
import unittest
import debugpy
import importlib.util
import os


def load_tests_from_file(file_path):
    """Load tests from a single file."""
    module_name = file_path.replace("/", ".").rstrip(".py")
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    test_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(test_module)
    return unittest.TestLoader().loadTestsFromModule(test_module)


def load_tests_from_directory(directory_path):
    """Discover and load tests from a directory."""
    return unittest.TestLoader().discover(start_dir=directory_path)


def main():
    parser = argparse.ArgumentParser(
        description="Run specified tests with debugging."
    )
    parser.add_argument(
        "-t",
        "--test",
        type=str,
        required=True,
        help='''Path to the test module or directory
        (e.g., "tests/test_email.py" or "tests")''',
    )

    args = parser.parse_args()

    # Configure the debugpy server to listen
    debugpy.listen(("0.0.0.0", 5678))
    print("Waiting for debugger to attach...")
    debugpy.wait_for_client()

    if os.path.isdir(args.test):
        suite = load_tests_from_directory(args.test)
    elif os.path.isfile(args.test):
        suite = load_tests_from_file(args.test)
    else:
        raise FileNotFoundError(
            f"No test file or directory found at '{args.test}'"
        )

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == "__main__":
    main()
