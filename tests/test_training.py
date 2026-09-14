from train_model import build_reinforcement_examples


def test_reinforcement_examples_are_unique():
    examples = build_reinforcement_examples()
    assert len(examples) == len(examples["message"].unique())