"""Contract tests for the public behavior promised by this Skill."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SkillContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        cls.rubric = (ROOT / "references/scoring-rubric.md").read_text(encoding="utf-8")
        cls.scenario_design = (ROOT / "references/scenario-design.md").read_text(encoding="utf-8")
        cls.progress = (ROOT / "references/progress-template.md").read_text(encoding="utf-8")
        cls.quickstart = (ROOT / "QUICKSTART.md").read_text(encoding="utf-8")

    def test_initial_scenario_must_not_leak_solution(self):
        self.assertIn("Do not reveal the answer in the question", self.skill)
        self.assertRegex(self.skill, r"Do not provide answers before the user attempts")
        self.assertRegex(self.skill, r"no answer hints")

    def test_answer_evaluation_covers_five_dimensions(self):
        for expected in (
            "Hypotheses and causal reasoning",
            "Evidence quality and technical accuracy",
            "Decision criteria and falsifiability",
            "Mitigation and operational risk",
            "Recovery acceptance and prevention",
        ):
            with self.subTest(dimension=expected):
                self.assertIn(expected, self.rubric)
        self.assertIn("0–2", self.rubric)
        self.assertIn("Score interpretation", self.rubric)

    def test_scenario_contract_is_bounded(self):
        self.assertIn("5–10 minutes", self.skill)
        self.assertIn("Three or four", self.skill)
        self.assertIn("假设 → 验证 → 判断标准 → 止血 → 验收", self.skill)

    def test_domain_rotation_covers_core_domains(self):
        for expected in (
            "Linux/kernel", "Network/security", "Kubernetes/runtime",
            "Observability/reliability", "Go/service runtime",
            "Database/cache/queues", "GPU device/scheduling",
            "LLM inference", "Agent runtime/control plane",
        ):
            with self.subTest(domain=expected):
                self.assertIn(expected, self.scenario_design)

    def test_progress_record_tracks_at_least_eight_recent_topics(self):
        topic_numbers = re.findall(r"^  \d+\. <domain", self.progress, flags=re.MULTILINE)
        self.assertGreaterEqual(len(topic_numbers), 8)
        self.assertIn("Next step", self.progress)

    def test_quickstart_is_usable_without_skill_installation(self):
        self.assertIn("现在开始：只给第一道新题，不给答案或提示。", self.quickstart)
        self.assertIn("每日一题", self.quickstart)


if __name__ == "__main__":
    unittest.main()
