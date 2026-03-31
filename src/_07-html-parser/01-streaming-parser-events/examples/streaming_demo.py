"""Demonstracja strumieniowego parsera HTML i modelu zdarzen.

Uruchomienie:
    python src/_07-html-parser/01-streaming-parser-events/examples/streaming_demo.py
"""
from html.parser import HTMLParser


class EventLogger(HTMLParser):
    """Parser logujacy kazde zdarzenie na standardowe wyjscie."""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_str = " ".join(f'{k}="{v}"' for k, v in attrs) if attrs else ""
        print(f"  [STARTTAG]  <{tag}> {attrs_str}".rstrip())

    def handle_endtag(self, tag: str) -> None:
        print(f"  [ENDTAG]    </{tag}>")

    def handle_data(self, data: str) -> None:
        print(f"  [DATA]      {data!r}")

    def handle_comment(self, data: str) -> None:
        print(f"  [COMMENT]   <!--{data}-->")

    def handle_decl(self, decl: str) -> None:
        print(f"  [DECL]      <!{decl}>")

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        print(f"  [STARTEND]  <{tag}/>")


# ── Przykladowy dokument HTML ─────────────────────────────────────

SAMPLE_HTML = """\
<!DOCTYPE html>
<!-- Prosty przyklad -->
<html lang="pl">
<head>
    <meta charset="utf-8">
    <title>Demo HTMLParser</title>
</head>
<body>
    <h1>Witaj!</h1>
    <p>To jest <b>przykladowy</b> akapit.</p>
    <img src="logo.png" alt="Logo"/>
    <br>
</body>
</html>
"""


def demo_pelny_dokument() -> None:
    """Parsuje caly dokument jednym wywolaniem feed()."""
    print("=" * 60)
    print("DEMO 1: Pelny dokument (jedno feed)")
    print("=" * 60)
    parser = EventLogger()
    parser.feed(SAMPLE_HTML)
    parser.close()


def demo_streaming() -> None:
    """Parsuje dokument karmiac parser malymi fragmentami."""
    print("\n" + "=" * 60)
    print("DEMO 2: Streaming (wiele feed)")
    print("=" * 60)
    parser = EventLogger()

    # Symulujemy odczyt danych fragmentami (np. z sieci)
    fragmenty = [
        "<div class='container'>",
        "Tekst ",
        "w kilku czesciach",
        "</div>",
    ]
    for i, fragment in enumerate(fragmenty):
        print(f"\n--- feed #{i}: {fragment!r} ---")
        parser.feed(fragment)

    parser.close()


def demo_reset() -> None:
    """Pokazuje dzialanie reset() miedzy dokumentami."""
    print("\n" + "=" * 60)
    print("DEMO 3: Reset parsera")
    print("=" * 60)
    parser = EventLogger()

    print("\nDokument A:")
    parser.feed("<p>AAA</p>")

    parser.reset()  # Czyścimy stan wewnetrzny

    print("\nDokument B (po reset):")
    parser.feed("<div>BBB</div>")
    parser.close()


if __name__ == "__main__":
    demo_pelny_dokument()
    demo_streaming()
    demo_reset()

