import os


# These can also be set as arguments via the command line.
class Config:
    dialog_gap = 150
    max_length = 100  # max number of words in 1 utterance (100)
    max_books = 100000  # limit size of the dataset
    min_delimiters = 150  # per 10.000 words (150)
    kl_threshold = 2  # (2)
    size_threshold = 20000  # minimum number of words in a book for filtering
    vocab_threshold = 0.2  # (0.2)
    min_double_delim = 50
    clean_dialogs = True  # if True, run preprocessing on dialogs
    languages = ['pt']
    download = False
    pre_filter = True
    extract = True
    post_filter = True
    create_dataset = True
    directory = os.path.join('data', 'filtered')
