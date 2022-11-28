# -*- coding: utf-8 -*-

from contextlib import redirect_stdout
from io import StringIO
from unittest import TestCase, main

from t3.arguments import version
from t3.entrypoint import main as entrypoint_main


class EntrypointTestCase(TestCase):
    def test_version(self):
        buffer = StringIO()
        with self.assertRaises(SystemExit):
            with redirect_stdout(buffer):
                entrypoint_main(["--version"])
        self.assertEqual(version(), buffer.getvalue().strip())


if __name__ == "__main__":
    main()
