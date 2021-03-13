accepted_file_types = ['Song', 'Podcast', 'Audiobook']

def is_file_type_correct(file_type):
    if file_type in accepted_file_types:
        return True
    else:
        return False
