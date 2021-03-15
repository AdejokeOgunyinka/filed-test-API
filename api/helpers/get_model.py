from ..models import Song, Podcast, Audiobook


def get_model(file_type):
    all_models = {"Song": Song, "Podcast": Podcast, "Audiobook": Audiobook}

    return all_models[file_type]
