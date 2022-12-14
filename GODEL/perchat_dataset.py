import datasets
import jsonlines

"""Corpus for PerChatPretrain"""

_DESCRIPTION = """\
PerChatPretrain
"""

_CITATION = """\
PerChatPretrain
"""

_WEBPAGE = ""

class PerChatPretrain(datasets.GeneratorBasedBuilder):
    """RedditPretrain"""

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "Context": datasets.Value("string"),
                    "Response": datasets.Value("string"),
                    "Knowledge": datasets.Value("string")
                }
            ),
            homepage=_WEBPAGE,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        train_path = './perchat/perchat_single_train.jsonl'
        validation_path = './perchat/perchat_single_valid.jsonl'
        test_path = './perchat/perchat_single_valid.jsonl'

        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={
                                    "filepath": train_path}),
            datasets.SplitGenerator(name=datasets.Split.VALIDATION, gen_kwargs={
                                    "filepath": validation_path}),
            datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={
                                    "filepath": test_path}),
        ]

    def _generate_examples(self, filepath):
        key = 0
        with open(filepath, "r", encoding="utf-8") as reader:
            for item in jsonlines.Reader(reader):
                yield key, item
                key += 1

