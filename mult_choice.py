from prodigy import recipe
from prodigy.components.loaders import get_stream
from prodigy.components.loaders import Images

@recipe("image.multchoice")
def image_mult_choice(dataset, source, labels):
    options = [{"id": label, "text": label} for label in labels.split(",")]
    stream = Images(source)

    def add_choices(task):
        task["options"] = options
        task["view_id"] = "choice"
        return task

    return {
        "dataset": dataset,
        "view_id": "choice",
        "stream": (add_choices(task) for task in stream),
        "config": {
            "choice_style": "multiple",
            "labels": labels.split(","),
        },
    }

