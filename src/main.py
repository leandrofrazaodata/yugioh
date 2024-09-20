from utils.ingestion import Collector


if __name__ == "__main__":
    url = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
    ing = Collector(url, prefix='cards')
    ing.get_and_save()