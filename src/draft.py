import fasttext.util
import fasttext

fasttext.util.download_model('en', if_exists='ignore') # English
fasttext.util.download_model('fr', if_exists='ignore') # French
fasttext.util.download_model('pt', if_exists='ignore') # Portuguese
fasttext.util.download_model('it', if_exists='ignore') # Italian

ft = fasttext.load_model('cc.en.300.bin')
fasttext.util.reduce_model(ft, 100)
ft.save_model('cc.en.100.bin')

ft = fasttext.load_model('cc.fr.300.bin')
fasttext.util.reduce_model(ft, 100)
ft.save_model('cc.fr.100.bin')

ft = fasttext.load_model('cc.pt.300.bin')
fasttext.util.reduce_model(ft, 100)
ft.save_model('cc.pt.100.bin')

ft = fasttext.load_model('cc.it.300.bin')
fasttext.util.reduce_model(ft, 100)
ft.save_model('cc.it.100.bin')
