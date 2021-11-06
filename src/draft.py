import fasttext.util
import fasttext

"""fasttext.util.download_model('en', if_exists='ignore') # English
fasttext.util.download_model('fr', if_exists='ignore') # French
fasttext.util.download_model('pt', if_exists='ignore') # Portuguese
fasttext.util.download_model('it', if_exists='ignore') # Italian
"""
ft = fasttext.load_model('cc.it.300.bin')
fasttext.util.reduce_model(ft, 100)
# to get the vector : ft.get_word_vector(word)
ft.save_model('cc.it.100.bin')
