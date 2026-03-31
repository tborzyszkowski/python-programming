"""Demonstracja wszystkich typow callbackow HTMLParser.

Uruchomienie:
    python src/_07-html-parser/03-event-handling/examples/callbacks_demo.py
"""
from html.parser import HTMLParser


class FullEventLogger(HTMLParser):
    """Parser logujacy kazdy typ zdarzenia z pelnym kontekstem."""

    def __init__(self) -> None:
        # convert_charrefs=False, zeby zobaczyc entityref/charref
        super().__init__(convert_charrefs=False)
        self.log: list[str] = []

    def _emit(self, event: str, detail: str) -> None:
        msg = f"  [{event:14s}] {detail}"
        self.log.append(msg)
        print(msg)

    def handle_starttag(self, tag: str, attrs: list) -> None:
        self._emit("STARTTAG", f"<{tag}> attrs={attrs}")

    def handle_endtag(self, tag: str) -> None:
        self._emit("ENDTAG", f"</{tag}>")

    def handle_data(self, data: str) -> None:
        self._emit("DATA", repr(data))

    def handle_comment(self, data: str) -> None:
        self._emit("COMMENT", repr(data.strip()))

    def handle_decl(self, decl: str) -> None:
        self._emit("DECL", repr(decl))

    def handle_pi(self, data: str) -> None:
        self._emit("PI", repr(data))

    def handle_entityref(self, name: str) -> None:
        self._emit("ENTITYREF", f"&{name};")

    def handle_charref(self, name: str) -> None:
        self._emit("CHARREF", f"&#{name};")

    def handle_startendtag(self, tag: str, attrs: list) -> None:
        self._emit("STARTENDTAG", f"<{tag}/> attrs={attrs}")


# ── Przyklady ─────────────────────────────────────────────────────

EXAMPLES = {
    "Pelny dokument HTML5": """\
<!DOCTYPE html>
<!-- Wersja robocza -->
<html lang="pl">
<head><title>Test</title></head>
<body>
    <h1>Witaj &amp; dzien dobry!</h1>
    <p>Znak &#169; to copyright.</p>
    <br/>
    <img src="logo.png" alt="Logo">
</body>
</html>
""",
    "Komentarze i encje": """\
<!-- TODO: poprawic -->
<p>Cena: 10 &euro; za &#8364; szt.</p>
<!-- KONIEC -->
""",
    "Processing Instruction (rzadkie)": """\
<?xml version="1.0" encoding="utf-8"?>
<note><body>Tresc</body></note>
""",
}

if __name__ == "__main__":
    for title, html in EXAMPLES.items():
        print(f"\n{'=' * 60}")
        print(f"  {title}")
        print(f"{'=' * 60}")
        parser = FullEventLogger()
        parser.feed(html)
        parser.close()

