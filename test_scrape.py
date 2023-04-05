from scrape import scrape

def test_if_scrape_works(monkeypatch):
    url = "https://rekvizitai.vz.lt/imone/lindyhop_lt_klubas/"
    monkeypatch.setattr('builtins.input', lambda _: url )
    soup = scrape()
    assert 'html' in str(soup)