import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "render_diagnosis_card.py"
EXAMPLE_DATA = ROOT / "examples" / "photographer_card_data.json"


class RenderDiagnosisCardTest(unittest.TestCase):
    def test_render_example_card_svg(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            out = Path(tmpdir) / "card.svg"
            subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--data",
                    str(EXAMPLE_DATA),
                    "--out",
                    str(out),
                ],
                check=True,
                cwd=ROOT,
            )
            svg = out.read_text(encoding="utf-8")

        data = json.loads(EXAMPLE_DATA.read_text(encoding="utf-8"))
        self.assertIn("<svg", svg)
        self.assertIn("Clarity Map", svg)
        self.assertIn(data["title"], svg)
        self.assertIn(data["diagnosis"], svg)
        self.assertIn("本轮诊断已完成", svg)


if __name__ == "__main__":
    unittest.main()
